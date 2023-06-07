import React from 'react'
import '../../styles/App.css'
import ListBox from '../ListBox.js'
import DashView from '../DashView'

function Dashboard() {
    return (
        <>
            <DashView />
            <ListBox />
        </>
    )
}

export default Dashboard