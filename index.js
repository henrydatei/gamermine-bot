const SteamUser = require('steam-user');
let user = new SteamUser();

options = {"accountName": "...", "password": "..."}
user.logOn(options);

user.on('loggedOn', () => {
    console.log("Logged in, playing csgo and other games")
    // 730 = CSGO
    // 570 = Dota 2
    // 578080 = PUBG
    // 271590 = GTA5
    // 1085660 = Destiny 2
    // 359550 = R6 Siege
    // 440 = TF2
    // 238960 = Path of Exile 
    user.gamesPlayed([730, 570, 578080, 271590, 1085660, 359550, 440, 238960]);
    console.log("...")
});