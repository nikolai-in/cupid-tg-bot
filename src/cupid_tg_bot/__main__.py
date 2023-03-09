"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Cupid Telegram Bot."""


if __name__ == "__main__":
    main(prog_name="cupid-tg-bot")  # pragma: no cover
