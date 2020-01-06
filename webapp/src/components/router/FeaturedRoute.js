import PropTypes from 'prop-types'
import React, { PureComponent } from 'react'
import { Route } from 'react-router-dom'

class FeaturedRoute extends PureComponent {
  componentDidMount() {
    const { areFeaturesLoaded, requestGetFeatures } = this.props

    if (areFeaturesLoaded) {
      return
    }

    requestGetFeatures()
  }

  render() {
    const { areFeaturesLoaded, isRouteDisabled, renderWhenDisabled, ...routeProps } = this.props
    const { path } = routeProps

    if (!areFeaturesLoaded) {
      return null
    }

    if (isRouteDisabled) {
      return (
        <Route
          path={path}
          render={renderWhenDisabled}
        />
      )
    }

    return <Route {...routeProps} />
  }
}

FeaturedRoute.propTypes = {
  areFeaturesLoaded: PropTypes.bool.isRequired,
  isRouteDisabled: PropTypes.bool.isRequired,
  renderWhenDisabled: PropTypes.func.isRequired,
  requestGetFeatures: PropTypes.func.isRequired,
}

export default FeaturedRoute
