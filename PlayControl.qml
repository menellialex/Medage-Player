import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 6.3
import QtQuick.Layouts 6.3
import QtMultimedia 6.3

import QtQuick3D 6.4

Item {
    id: pausePlay

    required property MediaPlayer mediaPlayer
    property int playerState: mediaPlayer.playbackState

    Button {
        id: pauseButton
        x: 92
        y: 400
        width: 75
        height: 20
        text: qsTr("Pause")

        onClicked: {
            mediaPlayer.pause();
        }
    }

    Button {
        id: playButton
         x: 92
         y: 400
         width: 75
         height: 20
         text: qsTr("Play")

         onClicked: {
             mediaPlayer.play();
         }
    }

    Button {
        id: button1
        x: 163
        y: 400
        width: 75
        height: 20
        text: qsTr("Forward")
        onClicked: {
            if (songQueue.nextInLine() === true)
            {
                mediaPlayer.source = songQueue.songGetter(1);
            }
            else
            {
                console.log("No song next");
            }
        }
    }

    Button {
        id: button2
        x: 20
        y: 400
        width: 75
        height: 20
        text: qsTr("Backwards")

        onClicked: {
            //restart song
            mediaPlayer.stop();
            mediaPlayer.play();
        }

        onDoubleClicked: {
            //we want to go back one song.
            if (songQueue.playedLast() === true)
            {
                mediaPlayer.source = songGetter(-1);
            }
            else
            {
                console.log("no song played last");
            }
        }
    }

    //States for the pause and play button
    states: [
        State {
                name: "play"
                when: playerState == MediaPlayer.PlayingState
                PropertyChanges { target: pauseButton; visible: true}
                PropertyChanges { target: playButton; visible: false}
        },
        State {
                name: "pause"
                when: playerState == MediaPlayer.PausedState
                PropertyChanges { target: pauseButton; visible: false}
                PropertyChanges { target: playButton; visible: true}
        },
        State {
                name: "stop"
                when: playerState == MediaPlayer.PausedState
                PropertyChanges { target: pauseButton; visible: false}
                PropertyChanges { target: playButton; visible: true}
        }

    ]
}
