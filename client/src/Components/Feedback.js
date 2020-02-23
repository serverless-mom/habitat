import React, { Component } from 'react'


class Feedback extends Component {


    render(){


    return(

            <div className='success'>
                    <p className="streak">You did it {`${this.props.streak}`} times!</p>
            </div>
    )
}


}

export default Feedback;