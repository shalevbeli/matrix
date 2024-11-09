import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders the app with the expected text', () => {
  render(<App />);
  const linkElement = screen.getByText(/React Client for Flask API/i);
  expect(linkElement).toBeInTheDocument();
});