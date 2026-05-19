def split_diff_by_file(diff_text: str):
    """
    Splits GitHub diff into individual file diffs.
    """

    files = []
    current_file = []

    lines = diff_text.splitlines()

    for line in lines:
        if line.startswith("diff --git"):
            if current_file:
                files.append("\n".join(current_file))
                current_file = []

        current_file.append(line)

    if current_file:
        files.append("\n".join(current_file))

    return files