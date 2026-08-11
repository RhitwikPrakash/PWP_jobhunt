from pathlib import Path

import yaml

from jobhunt.cli import main


ROOT = Path(__file__).resolve().parent.parent


def test_no_record_dry_run_does_not_create_seen_file(tmp_path):
    cfg = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))
    seen = tmp_path / "seen.json"
    cfg.update({
        "profile_file": str(ROOT / "profile.example.json"),
        "seen_file": str(seen),
        "digest_file": str(tmp_path / "digest.html"),
        "tracker_csv": str(tmp_path / "tracker.csv"),
    })
    config_path = tmp_path / "config.yaml"
    config_path.write_text(yaml.safe_dump(cfg), encoding="utf-8")

    result = main([
        "--config", str(config_path), "run", "--mock",
        "--scorer", "keyword", "--no-record",
    ])

    assert result == 0
    assert not seen.exists()
