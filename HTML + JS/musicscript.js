


  /**
   * Sample JavaScript code for youtube.videos.list
   * See instructions for running APIs Explorer code samples locally:
   * https://developers.google.com/explorer-help/guides/code_samples#javascript
   */

  function authenticate() {
    return gapi.auth2.getAuthInstance()
        .signIn({scope: "https://www.googleapis.com/auth/youtube.readonly"})
        .then(function() { console.log("Sign-in successful"); },
              function(err) { console.error("Error signing in", err); });
  }
  function loadClient() {
    gapi.client.setApiKey("AIzaSyAjM6lW4y4OZ6-_SZ2RVasTSgsewimEQyU");
    return gapi.client.load("https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest")
        .then(function() { console.log("GAPI client loaded for API"); },
              function(err) { console.error("Error loading GAPI client for API", err); });
  }
  // Make sure the client is loaded and sign-in is complete before calling this method.
  function execute() {
    return gapi.client.youtube.videos.list({
      "part": [
        "snippet,contentDetails,statistics"
      ],
      "id": [
        "Ks-_Mh1QhMc"
      ]
    })
        .then(function(response) {
                // Handle the results here (response.result has the parsed body).
                console.log("Response", response);
              },
              function(err) { console.error("Execute error", err); });
  }
  gapi.load("client:auth2", function() {
    gapi.auth2.init({client_id: "YOUR_CLIENT_ID"});
  });

{/* <button onclick="authenticate().then(loadClient)">authorize and load</button>
<button onclick="execute()">execute</button> */}


const YOUR_API_KEY = `AIzaSyAjM6lW4y4OZ6-_SZ2RVasTSgsewimEQyU`;

document.getElementById("btn-get-music").addEventListener("click", function(event) {
    // alert("hello");
    getMusic();
});


function getMusic(){
  fetch(
    `https://www.googleapis.com/youtube/v3/videos`
  ).then(function(response){
   return response.json();
 }).then(function(json){
   let kind = json['kind'];

   console.log(kind)


   let music = document.querySelector(".musicvideo");
   music.textContent = `${kind}`;
  })
}


// let music = document.querySelector(".musicvideo");
// music.textContent = "hello";

function init(){
    getMusic();
}

init();
