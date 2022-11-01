import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 6.3

Window {
    width: 640
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
        y: 40
        width: 171
        height: 168
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

    Column {
        id: column
        x: 304
        y: 40
        width: 314
        height: 400
    }
}
