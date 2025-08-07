import argparse
import json

from config import JSON_FILE, SQL_FILE
from generator import Generator


def run_strava_sync(
    client_id,
    client_secret,
    refresh_token,
    only_run=False,
    force=False,
):
    generator = Generator(SQL_FILE)
    generator.set_strava_config(client_id, client_secret, refresh_token)

    generator.only_run = only_run

    generator.sync(force)

    activities_list = generator.load()
    with open(JSON_FILE, "w") as f:
        json.dump(activities_list, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("client_id", help="strava client id")
    parser.add_argument("client_secret", help="strava client secret")
    parser.add_argument("refresh_token", help="strava refresh token")
    parser.add_argument(
        "--only-run",
        dest="only_run",
        action="store_true",
        help="if is only for running",
    )
    parser.add_argument(
        "--force",
        dest="force",
        action="store_true",
        help="force full sync of all data instead of incremental sync",
    )
    options = parser.parse_args()
    run_strava_sync(
        options.client_id,
        options.client_secret,
        options.refresh_token,
        only_run=options.only_run,
        force=options.force,
    )
