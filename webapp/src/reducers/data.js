import { persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage'
import { createDataReducer } from 'redux-thunk-data'

import { APP_NAME } from 'utils/config'

const dataPersistConfig = {
  key: `${APP_NAME}-webapp-data`,
  storage,
  whitelist: [],
}

const dataReducer = createDataReducer({
  users: [],
})

const data = persistReducer(dataPersistConfig, dataReducer)

export default data
