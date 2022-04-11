"""Contains abstract Route object to be used for CRUD operations on varying
   MongoDB document models"""
from flask import Response, request
from flask.views import MethodView
import mongoengine as me


class Route(MethodView):
    """Abstract object for simple routes"""

    def __init__(self, model):
        """Set provided model"""
        self.resource = model

    def get(self):
        """How to handle GET requests being made to the route.
           If an id is specified then we return the object
           associated with that id. If no id provided then
           all instances of the object are returned."""
        body = request.get_json()
        ref_id = body.get('id')
        if ref_id is None:
            objects = self.resource.objects().to_json()
            return Response(objects,
                            mimetype="application/json",
                            status=200)
        specified_object = self.resource.objects.get(id=ref_id).to_json()
        return Response(specified_object,
                        mimetype="application/json",
                        status=200)

    def post(self):
        """Method for handling POST requests to the route.
           For the designated object model we go through fields
           and if there are any reference fields then we first
           grab the objects specified in the request."""
        body = request.get_json()
        field_dict = self.resource._fields
        for field_name, field in field_dict.items():

            if isinstance(field, me.ReferenceField):
                if field_name in body:
                    reference_key = body[field_name]
                    reference_object = field.document_type.objects.\
                        get(id=reference_key)
                    body[field_name] = reference_object

            elif isinstance(field, me.ListField):
                if field_name in body:
                    reference_keys = body[field_name]
                    reference_objects = [field.field.document_type.objects.
                                         get(id=key) for key in reference_keys]
                    body[field_name] = reference_objects

        created_object = self.resource(**body).save()
        return {'id': str(created_object.id)}, 200

    def put(self):
        """Method for handling PUT requests to the route"""
        body = request.get_json()
        self.resource.objects.get(id=body['id']).update(**body)
        return '', 200

    def delete(self):
        """Method for handling DELETE methods to the route"""
        body = request.get_json()
        self.resource.objects.get(id=body['id']).delete()
        return '', 200
