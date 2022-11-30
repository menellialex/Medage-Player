import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 6.3
import QtQuick.Layouts 6.3
import QtMultimedia 6.3
import QtQuick3D 6.4
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
        id: fileDialog
        title: "Please choose a .mp3, .mp4 or .wav file"
        onAccepted: {
            mediaPlayer.stop()
            mediaPlayer.source = fileDialog.currentFile
            mediaPlayer.play()
        }
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

    TextInput {
        id: fileInputSongs
        x: 286
        y: 120
        width: 147
        height: 20
        text: "Enter Here"

        onAccepted: {
            url = getText();
            loadUrl(url);
        }
    }

    Button {
        x: 433
        y: 120
        width: 20
        height: 20

        onClicked: {
            fileDialog.open();
        }
    }

}
