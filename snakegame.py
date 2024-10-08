from turtle import Screen, Turtle
import time

yard = Screen()
yard.tracer(0)
yard.setup(width=700, height=700)
yard.bgcolor('lightgreen')
yard.title('Snake Game')

all_the_segments = []

segment_starting_position = [(0, 0), (-20, 0), (-40, 0)]
for single_segment_starts_at in segment_starting_position:
    newly_segment = Turtle('circle')
    newly_segment.color('black')
    newly_segment.penup()
    newly_segment.goto(single_segment_starts_at)
    all_the_segments.append(newly_segment)



game_over = False

while not game_over:
    yard.update()
    time.sleep(0.1)
    for every_segments in all_the_segments:
        every_segments.forward(10)
        


yard.exitonclick()