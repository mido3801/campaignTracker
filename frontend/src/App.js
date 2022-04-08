import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import Container from '@mui/material/Container';
import { Button } from '@material-ui/core';
import axios from "axios";

function App() {

  const [profileData, setProfileData] = useState(null)

  function getData(){
    axios({
        method: "GET",
        url: "/api/test"
    })
    .then((response) => {
        const res = response.data
        setProfileData(({
            profile_name: res.name,
            about_me: res.about}))
    }).catch((error) => {
        if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.handlers)
        }
    })
  }

  return (
  <div>
    <Container maxWidth="lg" style={{backgroundColor: "red"}}>
        <h1>test</h1>
        <Button onClick={getData}>Button</Button>
        {profileData && <div>
            <p>Profile name: {profileData.profile_name}</p>
            <p>About me: {profileData.about_me}</p>
            </div>}
        <h1>test</h1>
    </Container>
  </div>
  );
}

export default App;
