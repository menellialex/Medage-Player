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
            console.log("pause button hit, play state is now: ", mediaPlayer.playbackState);
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
             console.log("play button hit, play state is now: ", mediaPlayer.playbackState);
             console.log("the loaded song is: ", mediaPlayer.activeAudioTrack);
         }
    }

    Button {
        id: stopButton
        x: 92
        y: 420
        width: 75
        height: 20
        text: qsTr("Stop")

        onClicked: {
            mediaPlayer.stop();
            console.log("stop button hit, play state is now: ", mediaPlayer.playbackState);
        }
    }

    Button {
        id: button1
        x: 163
        y: 400
        width: 75
        height: 20
        text: qsTr("Forward")
    }

    Button {
        id: button2
        x: 20
        y: 400
        width: 75
        height: 20
        text: qsTr("Backwards")
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
