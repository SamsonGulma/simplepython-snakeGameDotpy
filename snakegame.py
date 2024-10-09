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
    
    for segment_at_number in range(len(all_the_segments) - 1, 0, -1):
        x_move = all_the_segments[segment_at_number - 1].xcor()
        y_move = all_the_segments[segment_at_number - 1].ycor()
        all_the_segments[segment_at_number].goto(x_move, y_move)
    all_the_segments[0].forward(20)
    all_the_segments[0].left(90)

yard.exitonclick()