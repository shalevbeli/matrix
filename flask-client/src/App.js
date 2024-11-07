import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [inputData, setInputData] = useState("");
  const [processedData, setProcessedData] = useState("");
  const [dbData, setDbData] = useState([]);

  const serverUrl = process.env.REACT_APP_SERVER_URL;

  // Fetch message from server
  const fetchMessage = async () => {
    try {
      const response = await axios.get(`${serverUrl}/message`);
      setMessage(response.data.message);
    } catch (error) {
      console.error("Error fetching message:", error);
    }
  };

  // Send data to server for processing
  const sendData = async () => {
    try {
      const response = await axios.post(`${serverUrl}/process`, {
        input_data: inputData,
      });
      setProcessedData(response.data.processed_data);
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };

  // Fetch data from MongoDB
  const fetchDbData = async () => {
    try {
      const response = await axios.get(`${serverUrl}/data`);
      setDbData(response.data);
    } catch (error) {
      console.error("Error fetching data from MongoDB:", error);
    }
  };

   // useEffect with proper dependencies
   useEffect(() => {
    fetchMessage(); // Fetch message when component mounts
    fetchDbData();  // Fetch MongoDB data when component mounts
  }, [fetchMessage, fetchDbData]);

  return (
    <div className="App">
      <h1>React Client for Flask API</h1>

      <div>
        <button onClick={fetchMessage}>Get Message from Server</button>
        <p>Server Message: {message}</p>
      </div>

      <div>
        <input
          type="text"
          value={inputData}
          onChange={(e) => setInputData(e.target.value)}
          placeholder="Enter text to process"
        />
        <button onClick={sendData}>Send Data to Server</button>
        <p>Processed Data from Server: {processedData}</p>
      </div>

      <div>
        <h2>Data from MongoDB:</h2>
        <ul>
          {dbData.map((item, index) => (
            <li key={index}>{JSON.stringify(item)}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;