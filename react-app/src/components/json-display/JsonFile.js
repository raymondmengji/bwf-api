import React, { Component } from 'react';
import ReactJson from 'react-json-view';
import CircularProgress from '@material-ui/core/CircularProgress';
import './JsonFile.css';


class JsonFile extends Component{
    
    constructor(props) {
        super(props)
        this.state = {
            notRan: true,
            json: null
        }
    }

    getRanking() {
        const {event, year, week, rows} = this.props.match.params
        console.log(this.props.match.params)
        
        if (typeof year == 'undefined' && typeof week == 'undefined' && typeof rows == 'undefined') {
            return fetch(`https://bwf-api.herokuapp.com/api/${event}`).then(data => data.json()).then(json => {
                this.setState({ notRan: false, json})
            })
        }
        else if (typeof year == 'undefined' && typeof week == 'undefined') {
            return fetch(`https://bwf-api.herokuapp.com/api/${event}/${rows}`).then(data => data.json()).then(json => {
                this.setState({ notRan: false, json})
            })
        }
        else if (typeof rows == 'undefined') {
            return fetch(`https://bwf-api.herokuapp.com/api/${event}/${year}/${week}`).then(data => data.json()).then(json => {
                this.setState({ notRan: false, json})
            })
        }
        return fetch(`https://bwf-api.herokuapp.com/api/${event}/${year}/${week}/${rows}`).then(data => data.json()).then(json => {
            this.setState({ notRan: false, json})
        })
    }

    render() {

        if (this.state.notRan) {
            this.getRanking()
            return (
                <div className="loading">
                    <CircularProgress />
                </div>
            )
        }
        else {
            return(
                <ReactJson src={this.state.json} />

            )
        }
        
    }
}

export default JsonFile