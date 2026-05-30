import axios from 'axios';

const BASE_URL = "http://127.0.0.1:8000";

export const fetchTopArtistsWithTracks =
async (token) => {

    const response = await axios.get(
        "http://127.0.0.1:8000/top-artists-tracks",
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.data;
};