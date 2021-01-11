from core.Simulator.Models import BallBase


class WhiteBall(BallBase):
    name="通常"


class RedBall(BallBase):
    name="高品质"
    quality = 1.5


class BlueBall(BallBase):
    name="结实"
    durability = 0.5


class GreenBall(BallBase):
    name="高效"
    cp = 0.5

class YellowBall(BallBase):
    name="安定"


class RainbowBall(BallBase):
    quality = 4


class BlackBall(BallBase):
    quality = 0.5


DefaultBall = WhiteBall()