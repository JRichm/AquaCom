import React from 'react'
import '../../styles/App.css'
import HeroSection from '../HeroSection.js'
import Cards from '../Cards.js'
import Footer from '../Footer'

function Home() {
    return (
        <>
            <HeroSection />
            <Cards />
            <Footer />
        </>
    )
}

export default Home