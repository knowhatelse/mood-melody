import "./SongsList.css";

function SongsList({songsData}) {
  return (
    <div className="sl-content-holder">
      <div className="sl-upper-container">
        <p className="sl-title">Your Top 10 songs based on your mood are:</p>
      </div>
      <div className="sl-center">
        <ul>
          {
            songsData.map((song) => (
              <li key={song.Track}>{song.Artist} - {song.Track} ({ song.ReleaseDate }) | {song.Genre}</li>
            ))
          }
        </ul>
      </div>
    </div>
  );
}

export default SongsList;
