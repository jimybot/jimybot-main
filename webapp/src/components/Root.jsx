import React from 'react'
import { PersistGate } from 'redux-persist/integration/react'
import { Provider } from 'react-redux'
import { BrowserRouter, Route, Switch } from 'react-router-dom'

import App from 'components/App'
import FeaturedRouteContainer from 'components/router/FeaturedRouteContainer'
import routes from 'components/router/routes'
import NotMatch from 'components/pages/NotMatch'
import { configureStore } from 'utils/store'

const { store, persistor } = configureStore()

const renderWhenFeatureRouteDisabled = () => <NotMatch />

const Root = () => (
  <Provider store={store}>
    <PersistGate loading={null} persistor={persistor}>
      <BrowserRouter>
        <App>
          <Switch>
            {routes && routes.map(obj => obj && (
              <FeaturedRouteContainer
                {...obj}
                key={obj.path}
                renderWhenDisabled={renderWhenFeatureRouteDisabled}
              />
            ))}
            <Route component={NotMatch} />
          </Switch>
        </App>
      </BrowserRouter>
    </PersistGate>
  </Provider>
)

export default Root
