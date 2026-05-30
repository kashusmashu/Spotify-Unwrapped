import { useState } from 'react'
import './App.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Homepage from "./components/homepage";
import TopArtistsTracks from "./components/TopArtistsTracks.jsx";

function App() {
   return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route
          path="/top-artists-tracks"
          element={<TopArtistsTracks />}
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App
