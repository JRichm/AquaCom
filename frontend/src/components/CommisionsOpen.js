import React from 'react';
import '../styles/CommisionsOpen.css'

function Header() {
    return (
        <>
            <article>
                <aside>
                    <img></img>
                </aside>
                <form>
                    <h1>Commissions are open!</h1>
                    <button className='btn btn-primary'>View Pricing</button>
                </form>
            </article>
        </>
    )
}

export default Header;