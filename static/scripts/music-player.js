const music_player_play = document.querySelector('.music-player-play');
music_player_play.addEventListener('click', play_pause);

const music_player_forward = document.querySelector('.music-player-next');
music_player_forward.addEventListener('click', forward);

const music_player_prev = document.querySelector('.music-player-previous');
music_player_prev.addEventListener('click', previous);

const music_player_repeat = document.querySelector('.music-player-repeat');
music_player_repeat.addEventListener('click', repeat);

const a = document.getElementById('audio');
a.addEventListener('ended', forward);


// const document_loaded = document.addEventListener('DOMContentLoaded', play);


let paused = true
let first_time = true

let prev_name = '';
let prev_artist = '';
let prev_img = '';

let next_name = '';
let next_artist = '';
let next_img = '';




window.onload = song_play()

function repeat(){
  let audio = document.getElementById('audio')
  audio.pause();
  audio.load();
  audio.play();
}

function song_play(){
  let source = document.getElementById("audio-file")
  let audio= document.getElementById("audio")
  if(first_time){
    first_time = false;
    let data = new FormData();
    data.check = 'works';
    fetch("/getSong", {
        method: "POST",
        headers: new Headers({
          "Content-Type": "application/json"
        }),
        body: JSON.stringify(data)
    })
    .then(response => response.json()).then(data => 
      {
        if (data['image_url'] != null){
          let img = document.getElementById('music-player-image1');
          img.src = data['image_url'];
        }
        if (data['artist'] != null){
          let artist = document.getElementById('music-player-artist');
          artist.innerHTML = data['artist']; 
        }
        if (data['name'] != null){
          let name = document.getElementById('music-player-name');
          name.innerHTML = data['name']; 
        }
        console.log('/songs/'+ data['filename']);

        source.src = '/songs/'+ data['filename'];
        audio.load();

      })
    
  }
         
}

function previous(){
  let source = document.getElementById('audio-file');
  let aud = document.getElementById('audio');
  let prev_source = document.getElementById('prev-audio-file');
  let prev_aud = document.getElementById('prev_audio')
  let next_source = document.getElementById('next-audio-file');
  let next_aud = document.getElementById('next-audio');

  if(prev_source.src != 'http://127.0.0.1:5000/music-player'){

    let img = document.getElementById('music-player-image1');
    console.log(prev_img + ' prev');
    next_img = img.src;
    img.src = prev_img;
    let artist = document.getElementById('music-player-artist');
    next_artist = artist.innerHTML
    artist.innerHTML = prev_artist; 
    let name = document.getElementById('music-player-name');
    next_name = name.innerHTML;
    name.innerHTML = prev_name;
    
    prev_artist = '';
    prev_img = '';
    prev_name = '';


    aud.pause();
    console.log(prev_source.src);
    next_source.src = source.src;
    source.src = prev_source.src;
    aud.load();
    prev_source.src = 'http://127.0.0.1:5000/music-player';
    aud.play();


  }
}


function forward(){
  let source = document.getElementById('audio-file');
  let aud = document.getElementById('audio');
  let prev_source = document.getElementById('prev-audio-file');
  let prev_aud = document.getElementById('prev_audio')
  let next_source = document.getElementById('next-audio-file');
  let next_aud = document.getElementById('next-audio');
  
  console.log(next_source.src);
  if(next_source.src != 'http://127.0.0.1:5000/music-player'){

    let img = document.getElementById('music-player-image1');
    console.log(img.src + ' forward');
    prev_img = img.src;
    img.src = next_img;
    console.log(prev_img)
    let artist = document.getElementById('music-player-artist');
    prev_artist = artist.innerHTML
    artist.innerHTML = next_artist; 
    let name = document.getElementById('music-player-name');
    prev_name = name.innerHTML;
    name.innerHTML = next_name;

    next_img = '';
    next_artist = '';
    next_name = '';


    aud.pause();
    prev_source.src = source.src;
    source.src = next_source.src;
    aud.load();
    next_source.src = 'http://127.0.0.1:5000/music-player';
    aud.play();
  }else{

    let name = document.getElementById('music-player-name');
    prev_name = name.innerHTML;
    let artist = document.getElementById('music-player-artist');
    prev_artist = artist.innerHTML
    let img = document.getElementById('music-player-image1');
    prev_img = img.src;

    prev_source.src = source.src
    prev = true;
    data = new FormData();
    data.check = 'works'
    fetch("/getSong", {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json"
      }),
      body: JSON.stringify(data)
    })
    .then(response => response.json()).then(data =>{
      if (data['image_url'] != null){
        let img = document.getElementById('music-player-image1');
        img.src = data['image_url'];
        console.log(data['image_url'] + ' new');
      }
      if (data['artist'] != null){
        let artist = document.getElementById('music-player-artist');
        artist.innerHTML = data['artist'];
      }
      if (data['name'] != null){
        let artist = document.getElementById('music-player-name');
        artist.innerHTML = data['name']; 
      }
      console.log('/songs/'+ data['filename']);
  
      source.src = '/songs/'+ data['filename'];



      aud.load();
      aud.play();
    })
  }
}

function play_pause(){
  let next_source = document.getElementById('next-audio-file');
  let next_aud = document.getElementById('next-audio');
  console.log(next_source.src);
  let aud = document.getElementById('audio')
  if(!paused){
    console.log('Will pause song')
    paused = true
    aud.pause();

  }else{
    paused = false
    console.log('Will unpause song')
    aud.play();
  }
}
