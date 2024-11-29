import React, { useState, useRef, useEffect } from 'react';

const MusicPlayer = () => {
    const tracks = [
        { title: 'Chillanjirukkiye Song', artist: 'Shivangi', src: '/audio/song1.mp3', albumArt: '/lubber.jpeg' },
        { title: 'Manasilayo Song', artist: 'Anirudh', src: '/audio/song2.mp3', albumArt: '/vettayan.jpeg' },
        { title: 'Hey Minnale', artist: 'Swetha', src: '/audio/song3.mp3', albumArt: '/minnale.jpeg' },
    ];

    const [currentTrackIndex, setCurrentTrackIndex] = useState(0);
    const [isPlaying, setIsPlaying] = useState(false);
    const [shuffle, setShuffle] = useState(false);
    const [repeat, setRepeat] = useState(false);
    const [currentTime, setCurrentTime] = useState(0);
    const [duration, setDuration] = useState(0);
    const [volume, setVolume] = useState(0.5); // Default volume is 50%

    const audioRef = useRef(null);

    useEffect(() => {
        if (audioRef.current) {
            if (isPlaying) {
                audioRef.current.play();
            } else {
                audioRef.current.pause();
            }
        }
    }, [isPlaying, currentTrackIndex]);

    useEffect(() => {
        if (audioRef.current) {
            audioRef.current.volume = volume; // Set audio volume
        }
    }, [volume]);

    const handlePlayPause = () => {
        setIsPlaying(!isPlaying);
    };

    const handleNext = () => {
        if (shuffle) {
            setCurrentTrackIndex(Math.floor(Math.random() * tracks.length));
        } else {
            setCurrentTrackIndex((prevIndex) => (prevIndex + 1) % tracks.length);
        }
    };

    const handlePrevious = () => {
        setCurrentTrackIndex((prevIndex) => (prevIndex - 1 + tracks.length) % tracks.length);
    };

    const handleProgressClick = (e) => {
        const progressBar = e.target;
        const clickPosition = e.nativeEvent.offsetX;
        const newTime = (clickPosition / progressBar.clientWidth) * duration;
        audioRef.current.currentTime = newTime;
        setCurrentTime(newTime);
    };

    const handleTimeUpdate = () => {
        setCurrentTime(audioRef.current.currentTime);
    };

    const handleLoadedMetadata = () => {
        setDuration(audioRef.current.duration);
    };

    const handleShuffle = () => setShuffle(!shuffle);

    const handleRepeat = () => setRepeat(!repeat);

    const handleEnded = () => {
        if (repeat) {
            audioRef.current.currentTime = 0;
            audioRef.current.play();
        } else {
            handleNext();
        }
    };

    const handleVolumeChange = (e) => {
        setVolume(e.target.value);
    };

    const handleTrackClick = (index) => {
        setCurrentTrackIndex(index);
        setIsPlaying(true); // Automatically play the selected track
    };

    return (
        <div className="music-player">
            <div className="track-info">
                <img src={tracks[currentTrackIndex].albumArt} alt="Album Art" className="album-art" />
                <div>
                    <h2>{tracks[currentTrackIndex].title}</h2>
                    <p>{tracks[currentTrackIndex].artist}</p>
                </div>
            </div>

            <audio
                ref={audioRef}
                src={tracks[currentTrackIndex].src}
                onTimeUpdate={handleTimeUpdate}
                onLoadedMetadata={handleLoadedMetadata}
                onEnded={handleEnded}
            ></audio>

            <div className="controls">
                <button onClick={handlePrevious}>⏮</button>
                <button onClick={handlePlayPause}>{isPlaying ? '⏸' : '▶️'}</button>
                <button onClick={handleNext}>⏭</button>
            </div>

            <div className="progress-bar" onClick={handleProgressClick}>
                <div
                    className="progress"
                    style={{ width: `${(currentTime / duration) * 100}% ` }}
                ></div>
            </div>

            <div className="actions">
                <button onClick={handleShuffle} className={shuffle ? 'active' : ''}>
                    🔀
                </button>
                <button onClick={handleRepeat} className={repeat ? 'active' : ''}>
                    🔁
                </button>
            </div>

            <div className="volume-control">
                <label htmlFor="volume">🔊</label>
                <input
                    id="volume"
                    type="range"
                    min="0"
                    max="1"
                    step="0.01"
                    value={volume}
                    onChange={handleVolumeChange}
                />
            </div>

            <div className="playlist">
                <h3>Playlist</h3>
                <ul>
                    {tracks.map((track, index) => (
                        <li
                            key={index}
                            className={index === currentTrackIndex ? 'active' : ''}
                            onClick={() => handleTrackClick(index)}
                        >
                            <img src={track.albumArt} alt="Track Art" />
                            <div>
                                <strong>{track.title}</strong>
                                <p>{track.artist}</p>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default MusicPlayer;