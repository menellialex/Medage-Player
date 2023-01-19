#include "SongQueue.h"
#include <vector>
#include <QObject>
#include <QUrl>

songQueue::songQueue()
{
    queue = {};
    queueIterator = 0;
}

//returns true if there is a song behind the playing song
//protects songGetter
bool songQueue::nextInLine()
{
    QUrl urlNext;

    try
    {
        urlNext = queue[queueIterator + 1];
        return true;
    }
    catch (out_of_range)
    {
        emit error("No song next in queue");
        return false;
    }
}

//returns true if there is a song behind the current playing song
//protect songGetter
bool songQueue::playedLast()
{
    QUrl urlLast;

    try
    {
        urlLast = queue[queueIterator - 1];
        return true;
    }
    catch (out_of_range)
    {
        emit error("No song last played in queue");
        return false;
    }

}
