import capitalize from 'lodash.capitalize'
import PropTypes from 'prop-types'
import React from 'react'
import Helmet from 'react-helmet'

import {
  APP_NAME,
  IS_DEVELOPMENT,
  ROOT_LOGO_ICONS_PATH,
  ROOT_PATH
} from 'utils/config'


const App = ({ children }) => (
  <>
    <Helmet>
      <meta charset="utf-8" />
      <meta
        content="width=device-width, initial-scale=1, user-scalable=no, shrink-to-fit=no"
        name="viewport"
      />
      <meta
        content="yes"
        name="apple-mobile-web-app-capable"
      />
      <meta
        content="yes"
        name="mobile-web-app-capable"
      />
      <meta
        content="#000000"
        name="theme-color"
      />
      <meta
        content={`default-src 'self' blob: data: https: http: gap://ready 'unsafe-inline'
                ${IS_DEVELOPMENT && "'unsafe-eval'"};
                connect-src 'self'
                https: http: ws://localhost:3000 wss://web-local:3000`}
        httpEquiv="Content-Security-Policy"
      />

      <link
        href={`${ROOT_LOGO_ICONS_PATH}/Icon.png`}
        rel="apple-touch-icon"
        type="image/png"
      />
      <link
        href={`${ROOT_LOGO_ICONS_PATH}/icon_60pt@2x.png`}
        rel="apple-touch-icon"
        sizes="120x120"
        type="image/png"
      />
      <link
        href={`${ROOT_LOGO_ICONS_PATH}/icon_76pt@2x.png`}
        rel="apple-touch-icon"
        sizes="152x152"
        type="image/png"
      />
      <link
        href={`${ROOT_LOGO_ICONS_PATH}/icon_60pt@3x.png`}
        rel="apple-touch-icon"
        sizes="180x180"
        type="image/png"
      />

      <link
        href={`${ROOT_LOGO_ICONS_PATH}/favicon-neg-16.png`}
        rel="icon"
        sizes="16x16"
        type="image/png"
      />

      <link rel="manifest" href={`${ROOT_PATH}/manifest.json`} />

      <title>{capitalize(APP_NAME)} Webapp</title>

    </Helmet>
    {children}
  </>
)

App.propTypes = {
  children: PropTypes.node.isRequired,
}

export default App
