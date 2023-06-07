import React from 'react'
import '../styles/DashView.css'

function DashView() {
    return (
        <span className='dash-view'>
            <div className='dash-view-item'>
                <h1 className='dash-view-number'>54</h1>
                <p className='dash-view-item-desc'>pending</p>
            </div>
            <div className='dash-view-item'>
                <h1 className='dash-view-number'>4</h1>
                <p className='dash-view-item-desc'>confirmed</p>
            </div>
            <div className='dash-view-item'>
                <h1 className='dash-view-number'>32</h1>
                <p className='dash-view-item-desc'>completed</p>
            </div>
            <div className='dash-view-item'>
                <h1 className='dash-view-number'>8</h1>
                <p className='dash-view-item-desc'>rejected</p>
            </div>
        </span>
    )
}

export default DashView