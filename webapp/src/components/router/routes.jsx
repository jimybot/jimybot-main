import React from 'react'
import { Redirect } from 'react-router-dom'

import Home from 'components/pages/Home'

const routes = [
  {
    exact: true,
    path: '/',
    render: () => <Redirect to="/home" />,
  },
  {
    exact: true,
    path: '/home',
    render: () => <Home />,
    title: 'Home',
  },
]

export default routes
