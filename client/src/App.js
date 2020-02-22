import  {React, Component} from 'react';
import {
  BrowserRouter,
  Route
} from 'react-router-dom';

import logo from './logo.svg';
import './App.css';

import Home from './Componenets/Home';
import Feedback from './Componenets/Feedback';






class App extends Component {

  constructor() {

      super();
      this.state = {
          streakLength: null
      };

  }
//API call to get streak length? Then pass to Feedback
componentDidMount() {
  this.streakLengthQuery();
}

streakLengthQuery = () => {
  axios.get('PLACEHOLDER URL')
    .then(response => {
      this.setState({
        streakLength: response.streakLength
      });
    })
    .catch (error => {
      console.log('Error fetching the streak data', error);
    });
}







  return (

      <BrowserRouter>
          <Route exact path='/' component={Home}></Route>
          <Route path='/feedback' render={() => <Feedback streak={this.state.streakLength} />}></Route>
      </BrowserRouter>
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>
  );
}

export default App;
