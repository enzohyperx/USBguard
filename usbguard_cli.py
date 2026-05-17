import subprocess
import re
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import HEAVY

console = Console()

GITHUB = "https://github.com/enzohyperx"


def clear():
    os.system("clear")


def run(cmd):
    return subprocess.check_output(cmd, text=True)


def get_devices():
    output = run(["usbguard", "list-devices"])
    devices = []

    for line in output.strip().split("\n"):
        match = re.match(r"(\d+):\s+(\w+)\s+id\s+([0-9a-fA-F:]+)\s+(.*)", line)

        if match:
            devices.append({
                "id": match.group(1),
                "state": match.group(2),
                "usb_id": match.group(3),
                "info": match.group(4)
            })

    return devices


def badge(state):
    return "[green]ALLOWED[/green]" if state.lower() == "allow" else "[red]BLOCKED[/red]"


def render(devices, selected):
    clear()

    console.print(
        Panel.fit(
            "[bold cyan]USBGUARD SECURITY DASHBOARD[/bold cyan]\n"
            "[dim]Device access control system[/dim]\n\n"
            f"[white]Project by:[/white] {GITHUB}",
            border_style="cyan",
            box=HEAVY
        )
    )

    table = Table(box=HEAVY, header_style="bold cyan")

    table.add_column("#", width=4, justify="center")
    table.add_column("STATUS", width=12)
    table.add_column("USB ID", style="yellow")
    table.add_column("DEVICE", style="white")

    for i, d in enumerate(devices):
        style = "on grey15" if i == selected else ""

        table.add_row(
            str(i + 1),
            badge(d["state"]),
            d["usb_id"],
            d["info"][:60],
            style=style
        )

    console.print(table)

    console.print("\n[bold]Commands:[/bold]")
    console.print("  [cyan]number[/cyan] → select device")
    console.print("  [cyan]b[/cyan] → block | [cyan]a[/cyan] → allow")
    console.print("  [cyan]q[/cyan] → quit")

    # Footer pro
    console.print(f"\n[dim]usbguard-cli-dashboard • {GITHUB}[/dim]")


def apply(dev, action):
    if action == "b":
        subprocess.run(["usbguard", "block-device", dev["id"]], check=True)
    elif action == "a":
        subprocess.run(["usbguard", "allow-device", dev["id"]], check=True)


def main():
    devices = get_devices()
    selected = 0

    while True:
        render(devices, selected)

        cmd = input("\n> ").strip().lower()

        if cmd == "q":
            clear()
            break

        if cmd.isdigit():
            idx = int(cmd) - 1
            if 0 <= idx < len(devices):
                selected = idx

        elif cmd in ["a", "b"]:
            try:
                apply(devices[selected], cmd)
            except Exception:
                pass

        devices = get_devices()


if __name__ == "__main__":
    main()import subprocess
import re
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import HEAVY

console = Console()


def clear():
    os.system("clear")


def run(cmd):
    return subprocess.check_output(cmd, text=True)


def get_devices():
    output = run(["usbguard", "list-devices"])
    devices = []

    for line in output.strip().split("\n"):
        match = re.match(r"(\d+):\s+(\w+)\s+id\s+([0-9a-fA-F:]+)\s+(.*)", line)

        if match:
            devices.append({
                "id": match.group(1),
                "state": match.group(2),
                "usb_id": match.group(3),
                "info": match.group(4)
            })

    return devices


def badge(state):
    return "[green]ALLOWED[/green]" if state.lower() == "allow" else "[red]BLOCKED[/red]"


def render(devices, selected):
    clear()

    console.print(
        Panel.fit(
            "[bold cyan]USBGUARD SECURITY DASHBOARD[/bold cyan]\n"
            "[dim]Device access control system[/dim]",
            border_style="cyan",
            box=HEAVY
        )
    )

    table = Table(box=HEAVY, header_style="bold cyan")

    table.add_column("#", width=4, justify="center")
    table.add_column("STATUS", width=12)
    table.add_column("USB ID", style="yellow")
    table.add_column("DEVICE", style="white")

    for i, d in enumerate(devices):
        style = "on grey15" if i == selected else ""

        table.add_row(
            str(i + 1),
            badge(d["state"]),
            d["usb_id"],
            d["info"][:60],
            style=style
        )

    console.print(table)

    console.print("\n[bold]Commands:[/bold]")
    console.print("  [cyan]number[/cyan] → select device")
    console.print("  [cyan]b[/cyan] → block | [cyan]a[/cyan] → allow")
    console.print("  [cyan]q[/cyan] → quit")


def apply(dev, action):
    if action == "b":
        subprocess.run(["usbguard", "block-device", dev["id"]], check=True)
    elif action == "a":
        subprocess.run(["usbguard", "allow-device", dev["id"]], check=True)


def main():
    devices = get_devices()
    selected = 0

    while True:
        render(devices, selected)

        cmd = input("\n> ").strip().lower()

        if cmd == "q":
            clear()
            break

        if cmd.isdigit():
            idx = int(cmd) - 1
            if 0 <= idx < len(devices):
                selected = idx

        elif cmd in ["a", "b"]:
            try:
                apply(devices[selected], cmd)
            except Exception:
                pass

        devices = get_devices()


if __name__ == "__main__":
    main()
