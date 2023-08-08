## Original Requirements
The boss has tasked us with creating a command line interface (CLI) game of Snake.

## Product Goals
```python
[
    "Create a simple, fun and addictive CLI game of Snake",
    "Ensure the game runs smoothly and without errors",
    "Ensure the game is easy to understand and play"
]
```

## User Stories
```python
[
    "As a user, I want to be able to easily start a new game so that I can play whenever I want",
    "As a user, I want the game to have clear instructions so that I can understand how to play",
    "As a user, I want the game to run smoothly without any glitches or errors so that I can enjoy the game",
    "As a user, I want to be able to see my score so that I can track my progress",
    "As a user, I want the game to be challenging and fun so that I can enjoy playing it"
]
```

## Competitive Analysis
```python
[
    "Python Snake Game: A simple CLI snake game. It lacks a score tracking feature",
    "Bash Snake: A CLI snake game written in Bash. It has a simple design but lacks in terms of gameplay",
    "CLI Snake: A CLI snake game with a modern design. It has a high learning curve due to its complex controls",
    "Terminal Snake: A CLI snake game with a retro design. It lacks a pause feature",
    "Snake Terminal: A CLI snake game with a unique design. It lacks a speed control feature"
]
```

## Competitive Quadrant Chart
```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    "Python Snake Game": [0.3, 0.6]
    "Bash Snake": [0.45, 0.23]
    "CLI Snake": [0.57, 0.69]
    "Terminal Snake": [0.78, 0.34]
    "Snake Terminal": [0.40, 0.34]
    "Our Target Product": [0.5, 0.6]
```

## Requirement Analysis
The product should be a CLI game of Snake. It should have a simple design and easy-to-understand controls. The game should run smoothly without any errors or glitches. It should also include features such as score tracking and speed control to enhance the gameplay experience.

## Requirement Pool
```python
[
    ("Implement basic snake game mechanics", "P0"),
    ("Implement score tracking feature", "P0"),
    ("Implement speed control feature", "P1"),
    ("Ensure the game runs smoothly without errors", "P0"),
    ("Create a simple and intuitive user interface", "P0")
]
```

## UI Design draft
The game will be played in a terminal window. The snake will be represented by a line of characters that grows in length as the game progresses. The food will be represented by a single character. The score will be displayed at the top of the screen. The game will have a simple, monochrome design to keep the focus on the gameplay.

## Anything UNCLEAR
There are no unclear points.