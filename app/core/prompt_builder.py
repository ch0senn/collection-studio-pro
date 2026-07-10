from dataclasses import dataclass


@dataclass
class RobotPrompt:

    name: str

    hairstyle: str

    background: str = "Bright summer blue sky with soft white clouds"

    pose: str = "Three-quarter view, turned slightly to the left"

    style: str = "High-quality stylized 3D render"

    expression: str = "Friendly"

    composition: str = "Head and shoulders portrait"


class PromptBuilder:

    def build(self, robot: RobotPrompt) -> str:

        return f"""
Create a unique robot portrait.

Character:
{robot.name}

Pose:
{robot.pose}

Composition:
{robot.composition}

Expression:
{robot.expression}

Background:
{robot.background}

Lighting:
Natural daylight.

Render Style:
{robot.style}

Hair Style:
{robot.hairstyle}

Requirements:

The robot must be unique.

The robot must not face directly towards the camera.

The robot should be turned approximately 20 degrees to the left.

Maintain the same robot identity throughout the image.

No text.

No logos.

No watermark.

Square composition.
""".strip()
