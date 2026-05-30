function TopArtistsTracks({ artists }) {
    return (
        <div>
            <h1>Top Artists</h1>
            {artists.map((item) => (
                <div key={item.artist.spotify_id}>
                    <h2>
                        {item.artist.name}
                    </h2>
                    <ul>
                        {item.top_tracks.map((track) => (
                            <li key={track.name}>
                                {track.name}
                            </li>
                            )
                        )}
                    </ul>
                </div>
            ))}
        </div>
    );
}

export default TopArtistsTracks;