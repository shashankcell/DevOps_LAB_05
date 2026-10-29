"""Tiny module for practicing a reviewed team contribution."""


def format_contribution(name: str, task: str) -> str:
    """Return a readable contribution note."""
    clean_name = name.strip()
    clean_task = task.strip()
    if not clean_name or not clean_task:
        raise ValueError("name and task must not be empty")
    return f"{clean_name} — {clean_task}"


if __name__ == "__main__":
    print(format_contribution("Contributor", "reviewed a pull request"))
