import React from 'react';
import './AboutUs.css';
import ShayAmitha from './ShayAmitha.png';
import BackendPhoto from './BackendPhoto.png';
import maya from './maya.png';
import moriah from './moriah.png';
import goo from './goo.png';
import MIL from './MIL.png';

const AboutUs = () => {
    return (
        <div className = "AboutUs">
            <h1>About Us</h1>
            <h2>Our Why</h2>
            <p>“Sororify” seeks to streamline the Villanova Panhellenic Recruitment process. At Villanova roughly 600 girls rush eight sororities in the first round of recruitment known as Sisterhood Round. The process of “matching” girls to each sorority’s existing members based on like qualities takes hours to ensure that potential members have a good experience. All of the tedious work done by hand still doesn’t guarantee the PNMs will be matched with their compatible counterparts in sororities.</p>
            <p>Our algorithm bridges the gap by ensuring the best possible match between PNMS and current chapter members the sorority that fits them the best.</p>
            <h2>About Our Team</h2>
            <p>We are all passionate Junior computer science majors looking to use our skills to improve and streamline processes.</p>
            <p>Front End Team: Shay McDowell and Amitha</p>
            <img className="centered-image" src={ShayAmitha} alt="Shay and Amitha" />
            <p> Back End Team: Moriah, Maya, Goo </p>
             <img className="centered-image" src={BackendPhoto} alt="Back-End" />
        </div>
    );
};

export default AboutUs;