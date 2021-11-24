
Download rtsp-simple-server from:

https://github.com/aler9/rtsp-simple-server/releases

Edit line 5 with your stream path.

Then run:

`python3 stream.py`


Notes:

1- If you're processing with a variable rate make sure to stream and record with the variable rate param -vfr

2- If your camera is streaming in h264, you can switch the encoding from libx264 to copy, this will just copy the content vs transcode it resulting in improved performance. Leaving the param ensures your restreams and recorded files will work with browsers and most clients.

3- On publish executes record.sh, which records and automatically builds hls lists.

4- record.sh also defines how the files and playlists are recorded to file storage `recordings/$RTSP_PATH/%Y%m%d-%s.ts` `recordings/$RTSP_PATH/stream.m3u8`

5- to change the duration of time you record, edit -hls_time and -hls_list_size in record.sh

6- You can test hls with VLC, to display the recorded stream in the browser, serve the playlist to a player such as hls js.

7- to display the rtsp stream in the browser, use a proxy server such as Axis Media stream js library
