//found online through stack overflow and Nokia wiki
//credit to khaverim and Nokia Wiki
//https://stackoverflow.com/questions/8894531/reading-a-line-from-a-txt-or-csv-file-in-qml-qt-quick?noredirect=1&lq=1

#ifndef FILEIO_H
#define FILEIO_H

#include <QObject>
#include <QQmlComponent>

class FileIO : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString source
               READ source
               WRITE setSource
               NOTIFY sourceChanged)
    QML_ELEMENT

public:

    explicit FileIO(QObject *parent = 0);

    Q_INVOKABLE QString read();
    Q_INVOKABLE int write(const QString& data);

    QString source() { return mSource; };

public slots:
    void setSource(const QString& source) { mSource = source; };

signals:
    void sourceChanged(const QString& source);
    void error(const QString& msg);

private:
    QString mSource;
    QUrl urlSource;
};

#endif // FILEIO_H
