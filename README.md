# Rhythmbox Currently Playing Song

## Purpose
Originally made for personal use, the motivation for this project was
to have something that could automatically update the music credit on
my livestreams.

This simple python script writes the artist and title of the
currently playing song from Rhythmbox, the native Linux client
for playing music, to a file: CurrentSong.txt, in the native
directory. The script checks every second to see if Rhythmbox is open, and if
it is, writes the currently playing song to the file.

From there, you may have software like OBS read from the
CurrentSong.txt file to easily display what's playing without having
to change anything manually!

## Customization
You may easily change the format of the output by amending either the
write statements or the terminal command "--print-playing".  
Here are the formatting options for Rhythmbox from the Linux man page:

>%at album title
>%aa album artist
>%aA album artist (lowercase)
>%as album artist sortname
>%aS album artist sortname (lowercase)
>%ay album year
>%ag album genre
>%aG album genre (lowercase)
>%an album disc number
>%aN album disc number, zero padded
>%st stream title
>%tn track number (i.e 8)
>%tN track number, zero padded (i.e 08)
>%tt track title
>%ta track artist
>%tA track artist (lowercase)
>%ts track artist sortname
>%tS track artist sortname (lowercase)
>%td track duration
>%te track elapsed time