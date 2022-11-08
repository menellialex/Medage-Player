import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 6.3
import QtQuick.Layouts 6.3

Window {
    width: 750
    height: 480
    visible: true
    title: qsTr("Hello World")

    Button {
        id: button
        x: 97
        y: 400
        text: qsTr("Pause/Play")
    }

    Button {
        id: button1
        x: 182
        y: 400
        text: qsTr("Forward")
    }

    Button {
        id: button2
        x: 20
        y: 400
        text: qsTr("Backwards")
    }

    Image {
        id: image
        x: 44
        y: 51
        width: 171
        height: 157
        source: "qrc:/qtquickplugin/images/template_image.png"
        fillMode: Image.PreserveAspectFit
    }

    Text {
        id: text1
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
        id: text2
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
            text: qsTr("Tab Button")
        }
    }

    //allows for differing tabs.
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

            ComboBox
            {
                id: styleDropdown
                x: 286
                y: 41
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


        }

    }
}



