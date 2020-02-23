import React, { Component } from 'react';
import {
    NavLink
  } from 'react-router-dom';

class Home extends Component {

    render(){

        return(
            <div className="buttons">
                    <NavLink to='/feedback' className="btn-hover color-8">
                        <img src="img/habitat-logo.png" alt="" className="btn-img"></img>
                    </NavLink>
            </div>
        )
    }


}


export default Home;