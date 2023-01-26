import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 6.3
import QtQuick.Layouts 6.3
import QtMultimedia 6.3
import QtQuick3D 6.3
import FileIO 1.0
import QtQuick.Dialogs

Item {

    required property MediaPlayer mediaPlayer
    required property FileIO fileio

    function loadUrl(url) {
        mediaPlayer.stop()
        mediaPlayer.source = url
        mediaPlayer.play()
    }

    FileDialog {
        id: fileDialogChooseSong
        title: "Please choose a .mp3, .mp4 or .wav file"
        onAccepted: {
            mediaPlayer.stop();
            mediaPlayer.source = fileDialogChooseSong.currentFile;
            mediaPlayer.play();
        }
    }

    FileDialog {
        id: fileDialogTest
        title: "Choose a .mp3, .mp4 or .wav file"
        onAccepted: {
            console.log(fileDialogTest.currentFile);
            var check = fileio.write(fileDialogTest.currentFile);
            console.log(check);
        }
    }

    FileDialog {
        id: playlistDialog
        title: "Choose a .txt file";
        onAccepted: {
            console.log(playlistDialog.currentFile);
            fileio.setSource(playlistDialog.currentFile);
        }
    }

    Text {
        id: styleText
        x: 40
        y: 40
        width: 60
        height: 20
        text: qsTr("Style Dropdown")
    }

    ComboBox
    {
        id: styleDropdown
        x: 286
        y: 40
        width: 167
        height: 20
        editable: true
        model: ListModel
        {
            id: dropdownModel
            ListElement { Text: "Default" }
            ListElement { Text: "Material" }
            ListElement { Text: "Dark" }
        }
        onAccepted:
        {
            if (combo.find(currentText) === -1)
            {
                dropdownModel.append({text: editText})
                currentIndex = combo.fine(editText)
            }
        }
    }

    Text {
        id: addSongs
        text: qsTr("Add Songs from File Explorer")
        x: 40
        y: 80
        width: 60
        height: 20
    }

    Button {
        x: 286
        y: 80
        width: 167
        height: 20
        text: "Open File Explorer"
        onClicked: {
            fileDialogChooseSong.open();
        }
    }

    Text {
        id: addSongtoPlaylist
        text: qsTr("Add Songs to Playlists")
        x: 40
        y: 120
        width: 60
        height: 20
    }

    Button {
        x: 286
        y: 120
        width: 167
        height: 20
        text: "Open File Explorer"
        onClicked: {
            fileDialogTest.open();
        }
    }

    Text {
        id: playlistSelect
        text: qsTr("Select a playlist")
        x: 40
        y: 160
        width: 60
        height: 20
    }

    Button {
        x: 286
        y: 160
        width: 167
        height: 20
        text: "Open File Explorer"
        onClicked: {
            playlistDialog.open();
        }
    }

    Item {
        id: __materialLibrary__
    }

}
