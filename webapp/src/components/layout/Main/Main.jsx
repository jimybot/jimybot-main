import classnames from 'classnames'
import PropTypes from 'prop-types'
import React from 'react'
import { Modal } from 'redux-react-modals'

const Main = ({ children, name, Tag }) => (
  <Tag className={classnames("main", { [`${name}-main`]: name })}>
    <Modal name="main" />
    {children}
  </Tag>
)

Main.defaultProps = {
  Tag: 'main',
  name: null
}

Main.propTypes = {
  Tag: PropTypes.string,
  children: PropTypes.node.isRequired,
  name: PropTypes.string,
}

export default Main
