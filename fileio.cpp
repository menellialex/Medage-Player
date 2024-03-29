//found online through stack overflow and Nokia wiki
//credit to khaverim and Nokia Wiki
//https://stackoverflow.com/questions/8894531/reading-a-line-from-a-txt-or-csv-file-in-qml-qt-quick?noredirect=1&lq=1

#include "fileio.h"
#include <QFile>
#include <QTextStream>
#include <iostream>
#include <QtGlobal>
#include <QLoggingCategory>

FileIO::FileIO(QObject *parent) :
    QObject(parent)
{

}

QString FileIO::read()
{
    if (mSource.isEmpty())
    {
        emit error("source is empty");
        return QString();
    }

    QFile file(mSource);
    QString fileContent;
    if (file.open(QIODevice::ReadOnly))
    {
        QString line;
        QTextStream t(&file);
        do
        {
            line = t.readLine();
            fileContent += line;
        } while (!line.isNull());
        file.close();
    }
    else
    {
        emit error("unable to open the file");
        return QString();
    }
    return fileContent;
}

int FileIO::write(const QString& data)
{
    if (mSource.isEmpty())
    {
        return 3;
        printf("no source");
    }

    QFile file(mSource);
    if (file.open(QFile::WriteOnly|QFile::Truncate))
    {
        return 2;
        printf("open fail");
    }

    QTextStream out(&file);
    out << data;

    file.close();

    return 0;
}






