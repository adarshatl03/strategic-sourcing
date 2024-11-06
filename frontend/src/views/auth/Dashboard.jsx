import React from 'react'
import { useAuthStore } from '../../store/auth'
import { Link } from 'react-router-dom'

const Dashboard = () => {
    const isLoggedIn = useAuthStore((state) => state.isLoggedIn)
    return (
        <>
            {isLoggedIn() ? 
            <div>
                <h2>Dashboard</h2>
                <Link to="/logout">Logout</Link>

            </div> : <div>Home</div>}
        </>

    )
}

export default Dashboard
