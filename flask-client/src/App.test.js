import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';  // Import additional matchers
import App from './App';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';

// Create a mock adapter instance
const mock = new MockAdapter(axios);

test('renders the app with the expected text', async () => {
  // Mock the GET request to the API
  mock.onGet('http://localhost:5000/message').reply(200, { message: 'Mocked message from server' });

  render(<App />);
  
  // Simulate waiting for data to load
  const linkElement = await screen.findByText(/Mocked message from server/i);
  expect(linkElement).toBeInTheDocument();

  // You can also check other UI elements that depend on the API data
});