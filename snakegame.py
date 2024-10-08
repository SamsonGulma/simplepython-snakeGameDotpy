from turtle import Screen, Turtle

yard = Screen()
yard.setup(width=700, height=700)
yard.bgcolor('lightgreen')
yard.title('Snake Game')

segment_starting_position = [(0, 0), (-20, 0), (-40, 0)]
for single_segment_starts_at in segment_starting_position:
    newly_segment = Turtle('circle')
    newly_segment.color('black')
    newly_segment.goto(single_segment_starts_at)

yard.exitonclick()