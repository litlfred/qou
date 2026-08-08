"""`record_upstream` — declaring an upstream before a builder exists.

`WitnessBuilder.add_upstream` is a method, so it needs a builder. 290 of the
330 witness-consuming producers in this corpus read their upstreams *before*
constructing one, which is why declaration adoption sat at 5.7%.
`record_upstream(path, into)` closes that gap by letting the caller own the
list.

The property that matters most here is the one in `test_lists_do_not_leak`:
the safe-looking alternative — a module-level accumulator drained on builder
construction — would silently attach one producer's upstreams to another's
witness whenever two builders exist in a process. These tests pin that it
cannot happen.
"""

import json

import pytest

from qou_substrate.witness import (
    WitnessBuilder,
    load_and_hash_upstream,
    record_upstream,
)


def _upstream(tmp_path, name="up.witness.json", value=1):
    p = tmp_path / name
    p.write_text(json.dumps({
        "computation": name.replace(".witness.json", ""),
        "value": value,
        "commitSha": "c0ffee",
        "scriptCommitSha": "deadbeef",
        "computedAt": "2026-08-08T00:00:00+00:00",
    }))
    return p


def test_returns_body_and_appends_record(tmp_path):
    """Drop-in for json.loads(path.read_text()) — the body comes back."""
    p = _upstream(tmp_path)
    got = []
    body = record_upstream(p, got)
    assert body["value"] == 1
    assert len(got) == 1
    assert got[0]["path"] == "up.witness.json"
    assert got[0]["commitSha"] == "c0ffee"
    assert got[0]["sha256"] == load_and_hash_upstream(p)[1]["sha256"]


def test_records_reach_the_witness(tmp_path):
    p = _upstream(tmp_path)
    got = []
    record_upstream(p, got)
    w = WitnessBuilder("downstream", output_dir=str(tmp_path))
    w.add_upstream_records(got)
    built = w.build()
    edges = built["data"]["upstream_witness_hashes"]
    assert [e["path"] for e in edges] == ["up.witness.json"]


def test_lists_do_not_leak(tmp_path):
    """THE reason the list is explicit rather than a module-level global.

    Two producers alive in one process. A drained global would hand B's
    upstream to A, or both to whichever built first. An owned list cannot.
    """
    a_src = _upstream(tmp_path, "a-up.witness.json", 1)
    b_src = _upstream(tmp_path, "b-up.witness.json", 2)
    a_up, b_up = [], []
    record_upstream(a_src, a_up)
    record_upstream(b_src, b_up)

    a = WitnessBuilder("a", output_dir=str(tmp_path)).add_upstream_records(a_up)
    b = WitnessBuilder("b", output_dir=str(tmp_path)).add_upstream_records(b_up)

    assert [e["path"] for e in a.build()["data"]["upstream_witness_hashes"]] \
        == ["a-up.witness.json"]
    assert [e["path"] for e in b.build()["data"]["upstream_witness_hashes"]] \
        == ["b-up.witness.json"]


def test_attach_is_idempotent(tmp_path):
    """Re-attaching, or overlapping with add_upstream, must not duplicate."""
    p = _upstream(tmp_path)
    got = []
    record_upstream(p, got)
    w = WitnessBuilder("downstream", output_dir=str(tmp_path))
    w.add_upstream(p)                 # declared the normal way too
    w.add_upstream_records(got)
    w.add_upstream_records(got)       # and again
    edges = w.build()["data"]["upstream_witness_hashes"]
    assert len(edges) == 1


def test_distinct_upstreams_both_recorded(tmp_path):
    a, b = _upstream(tmp_path, "a.witness.json", 1), _upstream(tmp_path, "b.witness.json", 2)
    got = []
    record_upstream(a, got)
    record_upstream(b, got)
    w = WitnessBuilder("d", output_dir=str(tmp_path)).add_upstream_records(got)
    edges = w.build()["data"]["upstream_witness_hashes"]
    assert sorted(e["path"] for e in edges) == ["a.witness.json", "b.witness.json"]


def test_empty_and_none_are_safe(tmp_path):
    w = WitnessBuilder("d", output_dir=str(tmp_path))
    w.add_upstream_records([])
    w.add_upstream_records(None)
    assert "upstream_witness_hashes" not in w.build().get("data", {})


def test_missing_upstream_still_raises(tmp_path):
    """The early-record path must not soften the missing-input error."""
    with pytest.raises(FileNotFoundError):
        record_upstream(tmp_path / "nope.witness.json", [])
