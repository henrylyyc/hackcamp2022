import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 1200
    height: 600
    x: screen.desktopAvailableWidth - width
    y: screen.desktopavailableHeight - height

    title: "HelloApp"

    property string currTime: "00:00:00"
    property QtObject backend
    
    Rectangle {
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/test.jpg"
            fillMode: Image.PreserveAspectCrop
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: currTime
                font.pixelSize: 48
                color: "white"
            }
        }
    }
    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg;
        }
    }
}