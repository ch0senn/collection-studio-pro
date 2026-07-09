
class PromptBuilder:
    """
    Builds prompts for Collection Studio Pro.
    """

    def robot_portrait(
        self,
        robot: str,
        hairstyle: str,
    ) -> str:

        return f"""
Create a high-quality stylized 3D robot portrait.

Robot:
{robot}

Pose:
Three-quarter view, turned slightly to the left.

Composition:
Head and shoulders only.

Background:
Bright summer sky with soft white clouds.

Lighting:
Natural daylight.

Expression:
Friendly.

Hairstyle:
{hairstyle}

The robot identity must remain consistent.

No text.

No watermark.
""".strip()
