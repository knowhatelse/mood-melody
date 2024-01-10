import "./SongsList.css";

function SongsList() {
  return (
    <div className="sl-content-holder">
      <div className="sl-upper-container">
        <p className="sl-title">Your Top 10 songs based on your mood are:</p>
      </div>
      <div className="sl-center">
        <ul>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
          <li>Artist Neme - Track Name (Year) | Genre</li>
        </ul>
      </div>
    </div>
  );
}

export default SongsList;
