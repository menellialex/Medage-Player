#ifndef SONGQUEUE_H
#define SONGQUEUE_H

#include <QObject>
#include <vector>
#include <QUrl>
#include <QtQml>

using namespace std;

class songQueue: public QObject
{
    Q_OBJECT

    Q_PROPERTY(QUrl song READ song WRITE enqueue NOTIFY cantDo);

public:
    songQueue();

    explicit songQueue(QObject *parent = 0);

    Q_INVOKABLE bool nextInLine();
    Q_INVOKABLE bool playedLast();

    void enqueue(QUrl url)
    {
        queue.push_back(url);
    }

    QUrl song()
    {
        QUrl returnUrl = queue[queueIterator];
        return returnUrl;
    };

public slots:

signals:
    void cantDo(const QString url);
    void error(const QString msg);

private:
    int queueIterator;
    vector<QUrl> queue;
};

#endif // SONGQUEUE_H
