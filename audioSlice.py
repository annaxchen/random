//splices audiofile into first 15 minutes. Can be adjusted to save diff formats / lengths
from pydub import AudioSegment

sound = AudioSegment.from_file("/Users/achen/Desktop/NameOfFile.m4a")
AudioSegment.converter = "/Users/achen/Desktop/Pydub/ffmpeg"
AudioSegment.ffmpeg = "/Users/achen/Desktop/Pydub/ffmpeg"
AudioSegment.ffprobe = "/Users/achen/Desktop/Pydub/ffprobe"

#startingtime
StartMin = 0
StartSec = 0

#endingtime (min + sec)
EndMin = 15
EndSec = 0

StartTime = StartMin*60*1000 + StartSec*1000
EndTime = EndMin*60*1000 + EndSec*1000

extract = sound[StartTime:EndTime]
extract.export("Marie Gassee 1.mp3", format = "mp3")

