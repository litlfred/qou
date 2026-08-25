#!/usr/bin/env python3
"""`WitnessBuilder` records how the producer was invoked (bean qou-nok3).

## Why

A producer can gate real compute on `sys.argv`, and nothing in its witness
said so. Measured case: `computations/whitehead_c0_mpmath.py` puts its N=12
data point behind `"--n12" in sys.argv`. The committed witness CONTAINS
N=12 -- so it was generated with the flag -- and a plain re-run silently
drops the point and moves the headline `factor` 1.9678 -> 1.8973 (3.6 %).
Nothing warns you; the diff reads as ordinary drift.

A corpus scan found **4** producers confirmed to gate payload on a flag their
committed witness does not record (and 11 `--strict` audit flags that are
exit-code-only and are NOT defects).

This mirrors `Generation` in `tools/hecke-engine/src/provenance.rs`, which
already does this for the Rust binaries.
"""
from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[3]
PKG = REPO / "tools" / "qou-substrate" / "python"


def _run_producer(tmp_path: Path, args: list[str]) -> dict:
    """Write a minimal producer, run it with `args`, return its witness."""
    script = tmp_path / "argv_provenance_probe.py"
    script.write_text(textwrap.dedent(f"""
        import sys
        sys.path.insert(0, {str(PKG)!r})
        from qou_substrate.witness import WitnessBuilder
        w = WitnessBuilder("argv-provenance-probe", engine="mpmath")
        w.set_description("fixture")
        w.add_data("saw_flag", "--deep" in sys.argv)
        w.save()
    """))
    subprocess.run([sys.executable, str(script), *args],
                   cwd=tmp_path, check=True, capture_output=True)
    out = tmp_path / "argv-provenance-probe.witness.json"
    return json.loads(out.read_text())


def test_invocation_block_is_present(tmp_path):
    w = _run_producer(tmp_path, [])
    assert "invocation" in w, "every witness must record how it was invoked"
    assert set(w["invocation"]) >= {"argv", "reproduce"}


def test_a_flag_is_recorded_verbatim(tmp_path):
    """The `--n12` case: the flag must appear in the witness."""
    w = _run_producer(tmp_path, ["--deep", "--n12"])
    assert "--deep" in w["invocation"]["argv"]
    assert "--n12" in w["invocation"]["argv"]
    # and the producer really did branch on it, so the two runs differ
    assert w["data"]["saw_flag"] is True


def test_two_invocations_are_distinguishable(tmp_path):
    """The whole point: flagged and unflagged runs must not look identical.

    Before this field existed, these two witnesses differed only in the
    payload the flag produced -- which is exactly what reads as drift.
    """
    plain = _run_producer(tmp_path, [])
    flagged = _run_producer(tmp_path, ["--deep"])
    assert plain["invocation"]["argv"] != flagged["invocation"]["argv"]
    assert plain["data"]["saw_flag"] is False
    assert flagged["data"]["saw_flag"] is True


def test_no_flags_is_recorded_as_such_not_omitted(tmp_path):
    """An empty argument list is informative, not absent.

    It distinguishes "run with no flags" from "written before this field
    existed", which is what absence of the block means.
    """
    w = _run_producer(tmp_path, [])
    assert w["invocation"]["argv"][1:] == []


def test_argv0_is_a_stable_path_not_the_invocation_path(tmp_path):
    """argv[0] must not carry the caller's cwd, or every run differs.

    `provenance.rs` normalises for the same reason -- without it the record
    depends on where the script was built or launched from, and comparing
    two machines' witnesses becomes noise.
    """
    w = _run_producer(tmp_path, [])
    head = w["invocation"]["argv"][0]
    assert not head.startswith("/"), f"argv[0] is absolute: {head}"
    assert str(tmp_path) not in head


def test_reproduce_is_a_runnable_command(tmp_path):
    w = _run_producer(tmp_path, ["--deep"])
    rep = w["invocation"]["reproduce"]
    assert rep.startswith("python3 -u ")
    assert "--deep" in rep
    # the `-u` matters: the long-compute logging discipline in AGENTS.md
    # requires unbuffered output for progress lines to be teeable.
    assert " -u " in rep


def test_invocation_is_NOT_ephemeral(tmp_path):
    """It must participate in substantive comparison.

    If it were masked like `environment` or `computedAt`, a re-run with
    different flags would compare equal -- which is the bug, not the fix.
    """
    sys.path.insert(0, str(PKG))
    from qou_substrate.witness import _EPHEMERAL_META_FIELDS, _strip_ephemeral_fields
    assert "invocation" not in _EPHEMERAL_META_FIELDS
    w = _run_producer(tmp_path, ["--deep"])
    assert "invocation" in _strip_ephemeral_fields(w)
