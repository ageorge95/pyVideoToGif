from moviepy.editor import VideoFileClip, CompositeVideoClip

input_video_path = r''
resize_factor = 0.6 # the lower this param is, the smaller the gif will be, but with a lower quality

videoClip = VideoFileClip(input_video_path).resize(0.6)

video = CompositeVideoClip([videoClip])
videoClip.write_gif("output.gif")