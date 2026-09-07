import os
import subprocess
import sys


def main():

    os.makedirs(
        "reports",
        exist_ok=True
    )

    command = [
        sys.executable,
        "-m",
        "pytest",
        "-v",
    ]

    # Optional marker selection
    if len(sys.argv) > 1:
        marker = sys.argv[1]

        command.extend([
            "-m",
            marker
        ])

    command.extend([
        "--html=reports/test_report.html",
        "--self-contained-html"
    ])

    print("\nRunning command:")
    print(" ".join(command))
    print()

    result = subprocess.run(
        command
    )

    sys.exit(
        result.returncode
    )


if __name__ == "__main__":
    main()