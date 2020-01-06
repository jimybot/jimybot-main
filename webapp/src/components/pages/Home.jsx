import React from 'react'
import { NavLink } from 'react-router-dom'

import HeaderContainer from 'components/layout/Header/HeaderContainer'
import MainContainer from 'components/layout/Main/MainContainer'

const Home = () => (
  <>
    <HeaderContainer />
    <MainContainer className="home with-header">
      <div className="navigations">
        <NavLink to="diagnostic">
          Créer un nouveau diagnostic
        </NavLink>
        <NavLink to="eligibilite">
          Connaître une éligibilité
        </NavLink>
        <NavLink to="telecharger">
          Télécharger des documents sur le drive
        </NavLink>
      </div>
    </MainContainer>
  </>
)

export default Home
