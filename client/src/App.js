import React, { Component } from 'react';
import {
  BrowserRouter,
  Route,
  Switch
} from 'react-router-dom';
import axios from 'axios';
import './css/App.css';

import Header from './Components/Header';
import Home from './Components/Home';
import Feedback from './Components/Feedback';


class App extends Component {


    constructor() {

        super();

        this.state = {
            streakLength: 33
        };

    }




  //   //API call to get streak length? Then pass to Feedback
  //   componentDidMount() {
  //     this.streakLengthQuery();
  //   }



  //   streakLengthQuery = () => {
  //     axios.get('https://0j4o5sqofk.execute-api.us-east-1.amazonaws.com/default/doTheThing')
  //       .then(response => {
  //         this.setState({
  //           streakLength: response.streakLength
  //         });
  //       })
  //       .catch (error => {
  //         console.log('Error fetching the streak data', error);
  //       });
  //   }


      render(){

        return(
          <BrowserRouter>

            <div className="container">
              <Header>TEST</Header>

                  <Switch>
                    <Route exact path='/' component={Home}></Route>
                    <Route path='/feedback' render={() => <Feedback streak={this.state.streakLength} />}></Route>
                  </Switch>

               
              </div>
            </BrowserRouter>


        );
      }
}
export default App;
