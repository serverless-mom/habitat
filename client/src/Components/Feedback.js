import React, { Component } from 'react'


class Feedback extends Component {


    render(){


    return(

            <div className='success'>
                <h1>YOU DID THE THING!</h1>
                    <p>{this.props.streak + ` times!`}</p>
            </div>
    )
}


}

export default Feedback;