import QtQuick 2.15
import QtMultimedia 6.3

//Ideas come from the mediaplayer example in qt.

Item {

    function read(metadata) {
        //we will set the values of the author, album and author to n/a first
        songtitle.text = "N/A";
        album.text = "N/A";
        artist.text = "N/A";

        //read metadata and change as needed.
        if (metadata) {
            for (var key of metadata.keys())
            {
                switch (key)
                {
                case MediaMetaData.Title:
                    songtitle.text = metadata.stringValue(key);
                    break;
                case MediaMetaData.AlbumTitle:
                    album.text = metadata.stringValue(key);
                    break;
                case MediaMetaData.Author:
                    artist.text = metadata.stringValue(key);
                    break;
                case MediaMetaData.CoverArtImage:
                    albumart.source = metadata.stringValue(key);
                    console.log(metadata.stringValue);
                    break;
                }
            }
        }
    }
}
