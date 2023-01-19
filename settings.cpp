#include "settings.h"
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <qquickstyle.h>

settings::settings()
{

}

//initialize the settings. read the file and change settings based on it.
bool initSettings()
{
    QFile openfile("settings.txt");
    bool status = true;
    QByteArray line;

    if (!openfile.open(QIODevice::ReadOnly|QIODevice::Text))
    {
        return false;
    }

    while (!openfile.atEnd())
    {
        //do reading.
        line = openfile.readLine();

        if (line.contains("Style") == true)
        {
            if (line.contains("Dark") == true)
            {
                QQuickStyle::setStyle("Dark");
            }
            else if(line.contains("Material") == true)
            {
                QQuickStyle::setStyle("Material");
            }
        }
    }


    return status;
}
