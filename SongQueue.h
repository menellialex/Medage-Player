#ifndef SONGQUEUE_H
#define SONGQUEUE_H

#include "qqmlintegration.h"
#include <QAbstractItemModel>
#include <QtCore>
#include <QUrl>
#include <vector>

class songqueue : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QUrl song
                 READ currentsong
                 WRITE enqueue
                 NOTIFY onBad)
    QML_ELEMENT

public:
    explicit songqueue(QObject *parent = nullptr);

    QUrl currentsong() {return queue.at(queueiterator);}

public slots:
    void enqueue(const QUrl newsong) {queue.push_back(newsong);}

signals:
    void onBad(const QUrl newsong);

private:
    std::vector<QUrl> queue;
    int queueiterator;
};

#endif // SONGQUEUE_H
