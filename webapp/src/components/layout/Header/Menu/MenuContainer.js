import { connect } from 'react-redux'
import { withRouter } from 'react-router-dom'
import { compose } from 'redux'
import { selectCurrentUser } from 'with-react-redux-login'

import Menu from './Menu'

const mapStateToProps = state =>  {
  return {
    currentUser: selectCurrentUser(state),
    isActive: state.menu.isActive
  }
}

export default compose(
  withRouter,
  connect(mapStateToProps)
)(Menu)
