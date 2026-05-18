# Kana Clicker

---
## Video Demo:  [CS50 Final Project - Kana Clicker](https://youtu.be/D0-__fXnNVQ)

---
## Description:

---
### Purpose

Japanese is a complex language composed of three different writing systems: hiragana, katakana, and kanji.
New Japanese students typically start with hiragana and katakana because each of their symbols is a unique mora, so this neatly maps onto Japanese phonology.

Hiragana has 46 basic characters. There are also modified characters that offer additional sounds, called "dakuten" and "handakuten."
Katakana is essentially a copy of hiragana written with alternate symbols, yet these are still required because they are used to write "loan words," words borrowed from a non-Japanese language.
Kanji are a set of symbols initially taken from ancient China, where each individual symbol represents a unique concept.
One way of thinking about it is that kanji is an alphabet where the size of the alphabet is equal to the number of words in the language.

People who attempt to learn Japanese are often discouraged by the learning curve and quit before they can make significant progress.
I created Kana Clicker to serve as a fun game to help uplift novices by helping them learn the basic hiragana and katakana characters.
Given the sheer scale of the character quantity needed to fluently read Japanese, I needed to make some design considerations about which characters to include and what to omit.
After all, the player would be unable to learn any new characters if they're exposed to a firehose of thousands of new symbols all at once.

I split the game into two different modes so that the player could consistently focus on a single system at a time and learn to associate the symbols with each other.
Additionally, the modified characters are modifications of base characters with slight accent marks, which does not lend itself well to a game with moving assets. By omitting the modified hiragana and katakana, I could reduce the alphabets down to a more manageable 46 characters each.

Then there was the issue of kanji. I decided to omit kanji for this specific game since the player would need to learn thousands of kanji, which would require gaming sessions that are too long for a "time trial" genre game.
After all, new students are typically encouraged to learn hiragana and katakana first because kanji is a more advanced topic.
---
### Gameplay

Kana Clicker is a "time trial" style game where the player must identify the given characters as quickly as possible by selecting them as prompted.
There are two game modes: hiragana and katakana. The gameplay is the same between modes; the difference is in the set of loaded characters for the kana balls.
As soon as the game starts, a timer is displayed in the top right corner so the player can always see their performance. If the player has a score from a previous run, then that is displayed underneath the active timer as a "best score."
Naturally, the goal is to improve performance by completing it more quickly and earning a new best score.

Aside from the timer, gameplay utilizes seven main widgets. At the top-middle of the screen is a button that displays the target character written in romaji.
The player may click the button to command the game to play an audio clip of a native Japanese speaker pronouncing the target.

There are six dynamic widgets. There are pink balls that bounce around the screen with the characters written on them.
The goal is for the player to click the ball with the correct character written on it.
These characters are the Japanese variants used to write the romaji sound displayed by the target button.
The game requires the player to select all 46 character values in the correct order, but only 6 characters are displayed at any given time to help avoid overwhelming the player.

The balls are always interactive, even when they are the wrong choice.
Clicking any kana ball always triggers an audio clip pronouncing its displayed character.
Each time the player correctly selects the target character ball, then that ball will flash green and disappear.
Afterward, if there are any remaining undisplayed characters, then the game will populate the screen with a new sixth ball.
Whenever the player incorrectly selects the wrong character ball, then that ball will flash red before persisting in its normal behavior.

The widgets are designed to be interactive and engaging for the player.
The widgets are pink so that they resemble falling cherry blossoms and synergize well with the Japanese visual motif.
Whenever the player hovers over a widget, then the widget turns yellow to quickly grab the player's attention and keep them mindful about their cursor location, an important characteristic for a "point-and-click" game.
Whenever the player clicks any of the widgets, then that widget will always play an audio clip of its displayed character, spoken by a native Japanese speaker.
This will help the player learn how to pronounce the characters.
The goal is for the player to learn to associate the romaji writing and audio clips with their related kana characters.

Once the player selects all 46 characters correctly, then the game displays the "You Win" screen where the recorded player score is displayed. 
The score is the amount of time that it took the player to complete the game.
There is also a message to instruct the player to return to the main menu screen by pressing the SPACE button.

The game also supports pausing.
At any time the player can pause the game by pressing the SPACE button on their keyboard.
Once paused, the game stops drawing all the character balls to the screen to prevent cheating.
Instead, the game flashes a message announcing the paused game state with instructions to unpause by pressing the SPACE button again.
Naturally, the timer does not increment whenever the game is paused.

Finally, the game can be exited at any time by pressing the ESC key on the player's keyboard.
This automatically quits the game without recording a score and returns the player back to the main menu screen.

---
### Other Features
Kana Clicker was developed using Python's pygame module as an interactive learning tool.
The game initially boots into a main menu that dynamically detects and adjusts itself to fit the player's screen size.

From the main menu, there are four buttons available to the player. The "hiragana" button launches gameplay in "hiragana mode," where the player plays the game (described by the "Gameplay" section above) with the basic hiragana alphabet. The "katakana" button also launches the same game, but the game loads the katakana characters instead of the hiragana ones.
These are "time trial" style games where the player attempts to identify all characters as quickly as possible. 

The game keeps a record of past player scores in a JSON file. Each time the player completes the game, the code checks to see if a previous time record exists for that game mode. If a record does not exist, then it is updated with the newly earned score.
Otherwise, a record exists, so the game checks to see if the new time is less than the old record. If the new score beats the old score, then the JSON file is updated with the new score.

The player can see these records by selecting the "scoreboard" button from the main menu.
This brings the player to a screen that displays the best scores for hiragana mode and katakana mode in a \<minutes>:\<seconds>:\<milliseconds> format.
The scoreboard also contains "reset" buttons, which allow the player to manually purge the time records stored in the JSON file.
Whenever a score is not available, then the game will display "NO SCORE" as the value.

Finally, the last button on the main menu is the "exit" button. This button will close the application whenever selected.

---
### Files

#### Constants.py
This file contains constant values that are used throughout the codebase.
This is a best practice because it allows me to make changes in this single file instead of hunting down each place where the value is used.

#### main.py
This file contains the main game loop.
The game is organized into scene classes, and it is the main's job to load the appropriate scene.
Every scene class has different implementations of three basic functions: handle_events(), draw(), and update().
Handle_events passes all player input, such as cursor hovers or button clicks, for the scene class to process.
Then the draw() function is used to add widgets related to that specific scene to the screen.
Finally, the update() function updates any class values that are not related to player input.
At the beginning, instances of each scene class are initialized and added to a dictionary indexed by the scene name as a key.
Per each game loop iteration, main checks to see if the application should be terminated, loads the requested scene into the loop, calls handle_events() + draw() + update() for that scene, and then displays the result for the player.

#### MainMenu.py
This class represents the scene that handles the main menu. It flashes the game title "Kana Clicker" at the top of the screen.
Below that four widgets are displayed: "hiragana," "katakana," "scoreboard," and "exit." The first three lead to different scenes, and exit terminates the application.
This class handles all logic to create and display these buttons as well as to tell main.py when and where scene changes should occur.

#### ScoreBoard.py
This scene displays the contents of the recorded time scores from the JSON file.
Additionally, it displays a button that changes the scene back to the main menu and buttons that reset the player scores.
The logic that actually handles JSON file updates is abstracted into the next file.

#### ScoreMgr.py
This file implements primitive read and write functions to extract JSON field values as well as the wrapper functions that are actually used by the scene classes.
The update_score() function checks the contents of the JSON file to ensure that its parameter score is quicker than the previous score before updating the JSON file.
The JSON scores are stored as an integer value in milliseconds, so whenever a score needs to be displayed in a player-friendly way, the display_score() function formats the score into a \<minutes>:\<seconds>:\<milliseconds> format by calling the format_timestamp() function. 

#### Button.py
This class implements all the logic for button widgets.
The buttons can be configured to change their screen position as well as their colors.
The draw() function has logic that allows the button to change its color whenever the player hovers or clicks the button, which is recorded by the handle_event() function.
Additionally, this class has an update_text() function so that the main gameplay loop can update the text to the next target romaji character without requiring the creation of an entirely new button.

Most notable is that button actions upon an event are configurable since the class that creates a button object can pass in a callback() function as a parameter.
This means that the callback() function is defined at the scene class level.
Those classes can reuse this single button class even when the individual buttons have different behaviors.

#### KanaBall.py
This class handles the logic for the character balls that the player needs to click on.
All the balls behave in the same way, so their appearance and behavior don't need to be configurable, with the obvious exception of their displayed character.

Each "kana ball" is initialized at a random (x,y) position within the screen.
They are also initialized with their own fixed x and y speed.
The ball speed is managed by the calc_speed() function that performs boundary checking and inverts the ball's speed along any axis that runs into the screen's boundaries.
Each time step, every ball's position is updated with the update() functions by that specific ball's speed.
Together these functions created the appearance that the kana balls are "bouncing" off of the sides of the screen.

Whenever the player clicks on a kana ball, then the ball will play the audio file for its displayed character by using the pygame sound mixer.
Then the check_button() function will verify that the selected ball's character matches the target character from the GameScene class.
If they match, then the kana ball flashes green and sets a flag indicating that it should be removed from the display by the GameScene class.
If they don't match, then the kana ball flashes red and continues its normal behavior.

#### GameScene.py
This class represents the game scene. There are two different game modes, so main.py has different instances of the GameScene available based on the game mode.
The GameScene manages all the game widgets and updates them. 

An ongoing timer is displayed in the top right corner of the screen. If the player has a previous best score, then the best score is displayed underneath the active timer.
The GameScene has its own ScoreMgr member class that handles retrieving the scores and formatting them.

At the top middle of the screen is a button that displays the target character written in romaji.
The Button class handles most button logic, but the GameScene defines the button's callback() function that plays audio whenever it's clicked.
The GameScene is also responsible for updating this button's displayed text to the next target character after the player successfully solves the previous target.

The GameScene also manages two key lists.
The first is a list of the active kana balls, and the other contains characters that are yet to be displayed.
The KanaBall class handles all the ball physics, but the GameScene is responsible for creating and tracking the displayed balls as well as calling their update() functions.
Whenever the player solves the current target character by clicking on the correct kana ball, then the GameScene removes the solved ball from its ball list, updates the target character to the next ball's character, and, if there are any non-displayed characters, inserts a new kana ball at the end of the list.

The GameScene also supports pausing.
Whenever the player presses the SPACE key on their keyboard, then GameScene stops updating the timer, stops displaying the kana balls, and stops updating the kana balls.
The GameScene flashes a paused message on screen with instructions to unpause the game by pressing the SPACE key again.

Finally, once the player solves all 46 kana balls, then the GameScene displays the player wins screen, which displays the new player score.

#### /assets/audio/.wav files
This directory contains all the audio files for each of the hiragana/katakana characters.
They are loaded and played whenever the player clicks on a character widget during gameplay.

#### /assets/background/fuji.jpg
This is the image file loaded as the background during gameplay.

#### /assets/fonts/PressStart2P.ttf
This is a font file used to display menu items.
This gives the game menu a retro arcade feel.
I added this font file as an asset because it is not available in the pygame system fonts.

#### /assets/json/scores.json
This is the JSON file that contains player scores.
There are two fields, "hiragana" and "katakana," one for each game mode, which have their best scores stored separately.
Both fields default to -1, which represents the "NO SCORE" value.
As the player earns better scores, then this JSON file is updated by the ScoreMgr class.
