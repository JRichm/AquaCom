import React from 'react';
import Header from '../components/Header';
import CommisionsOpen from '../components/CommisionsOpen';
import '../styles/HomePage.css'
import 'bootstrap/dist/css/bootstrap.css'

function HomePage() {
    return (
        <div>
            <Header />
            <CommisionsOpen />
        </div>
    )
}

export default HomePage;