import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 6.3
import QtQuick.Layouts 6.3
import QtMultimedia 6.3
import QtQuick3D 6.4
import FileIO 1.0

Window {
    id: root
    width: 750
    height: 480
    visible: true
    title: qsTr("Medage Player")

    PlayControl {
        //this controls the backwards, forwards, pause and play features
        mediaPlayer: mediaPlayer
    }

    FileIO {
        //fileio item for everything
        id: fileio
        onError: {console.log(msg);}
    }

    SongController {
        //This is the slider and song timer text.
        id: songController
        mediaPlayer: mediaPlayer
    }


    Slider {
        id: volumeSlider
        x: 43
        y: 453
        width: 167
        height: 20
        value: 1
        from: 0.
        to: 1.
    }

    Text {
        id: title
        x: 93
        y: 226
        width: 74
        height: 28
        text: qsTr("Title")
        font.pixelSize: 20
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: "Verdana"
    }

    Text {
        id: artist
        x: 102
        y: 260
        width: 55
        height: 35
        text: qsTr("Artist")
        font.pixelSize: 16
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: "Verdana"
    }

    Text {
        id: text3
        x: 101
        y: 301
        width: 57
        height: 24
        text: qsTr("Album")
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    TabBar {
        //creation of the tab and its buttons
        id: tabBar
        x: 250
        y: 20
        width: 500
        height: 50

        TabButton {
            id: tabButton
            x: 0
            y: 0
            width: 125
            height: 40
            text: qsTr("Library")
        }

        TabButton {
            id: tabButton1
            x: 123
            y: 0
            width: 128
            height: 40
            text: qsTr("Playlists")
        }

        TabButton {
            id: tabButton2
            x: 250
            y: 0
            width: 125
            height: 40
            text: qsTr("Recommendations")
        }

        TabButton {
            id: tabButton3
            x: 375
            y: 0
            width: 125
            height: 40
            text: qsTr("Settings")
        }
    }

    //allows for differing tabs.
    //This stack is for the library, playlist, recommendation and settings tab
    StackLayout {
        id: stackLayout
        x: 250
        y: 75
        width: 500
        height: 405
        currentIndex: tabBar.currentIndex

        Item {
            //anything in library tab goes here
            id: libraryTab
            Library {

            }
        }
        Item {
            //anything in playlist tab goes here
            id: playlistTab

        }
        Item {
            //anything in recommendation tab goes here
            id: recommendationTab
        }

        Item {
            //anything in settings tab goes here
            id: settingsTab

            SettingsTab{
                mediaPlayer: mediaPlayer
                fileio: fileio

            }

        }

    }

    StackLayout {
        id: stackLayout1
        x: 39
        y: 45
        width: 176
        height: 160
        currentIndex: tabbar1.currentIndex

        Item {
            id: albumTab
            Image {
                id: image
                width: 171
                height: 157
                source: "ITCOTD.png"
                fillMode: Image.PreserveAspectFit
            }
        }

        Item {
            id: visulizerTab

            Text {
                id: text4
                x: 46
                y: 53
                width: 109
                height: 56
                text: qsTr("Hello World!")
                font.pixelSize: 12
            }
        }
    }

    TabBar {
        x: 47
        y: 20
        width: 159
        height: 25
        id: tabbar1

        TabButton {
            id: tabbutton4
            text: qsTr("Album Cover")
        }

        TabButton {
            id: tabbutton5
            text: qsTr("Visualizer")
        }

    }

    Item {
        id: __materialLibrary__
    }

    MediaPlayer {
        id: mediaPlayer
        audioOutput: audioOut
    }

    AudioOutput {
        id: audioOut
        volume: volumeSlider.value
    }

}



