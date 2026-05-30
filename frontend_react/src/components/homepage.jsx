import { useState, useEffect } from "react";
import TopArtistsTracks from "./TopArtistsTracks.jsx";

//creates simple header and button that when clicked, runs /login endpoint
export default function Homepage() {
    const [artists, setArtists] = useState([]); // will hold your top 5 artists + their tracks
    const [isLoading, setIsLoading] = useState(false);
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        const loadData = async () => {
            setIsLoading(true);
            try {
                const data = await fetchMusicData();
                if (data && data.length > 0) {
                    setArtists(data);
                    console.log("Artists state data:", data);
                    setIsLoggedIn(true);
                }
            } catch (err) {
                // User not logged in yet
            }
            setIsLoading(false);
        };

        loadData();
    }, []);

    useEffect(() => {
    console.log("artists state changed:", artists);
    }, [artists]);

    // button that calls /login endpoint
    const handleLogin = async() => {

        const response = await fetch ("http://127.0.0.1:8000/login");
        const data = await response.json();

        // redirect to spotify auth url here
        window.location.href = data.url;
    };

    // calls /top_artists_tracks endpoint
    const fetchMusicData = async() => {
        const response = await fetch ("http://127.0.0.1:8000/top-artists-tracks");
        const data = await response.json();
        
        console.log("Backend returned:", data);


        return data;
    };


    return (
        <div>
            <h1> Welcome to my Web App!</h1>

            {!isLoggedIn && (
                <button onClick={handleLogin}>
                    Connect to Spotify
                </button>
            )}

            {isLoading && <p>Loading your music data...</p>}

            {artists.length > 0 && <TopArtistsTracks artists={artists} />}
        </div>
    );

}