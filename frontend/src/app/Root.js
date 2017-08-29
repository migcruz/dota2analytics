import React from "react";
import {Provider} from "react-redux";
import {BrowserRouter, Route} from "react-router-dom";

import stylesheets from "app/stylesheets/index.less"; //eslint-disable-line no-unused-vars
import configureStore from "app/configureStore";
import history from "app/history";
import urls from "app/urls";

const store = configureStore();


class Root extends React.Component {
    render() {
        return (
            <Provider store={store}>
                <BrowserRouter>
                    <div>
                    	{urls}
                    </div>
                </BrowserRouter>
            </Provider>
        );
    }
}

export default Root;
