"""Tests for `_check_producer_takeover` — the bean `qou-okl8` guard.

The defect: two producers emitted the SAME witness name with different
schemas (`per_irrep_pole_atom.py` writes `f"per-irrep-pole-{atom}-h{n}"`,
which for the deuteron is exactly the literal `per_irrep_pole_deuteron_h6.py`
wrote). Whichever ran last won, and the narrower one silently deleted three
`data.*` fields — 230 deletions against 39 insertions — with no warning.

The guard keys on OWNERSHIP CHANGE plus FIELD LOSS, both required. The tests
below pin exactly that pairing, because the tempting alternative — a bare
"refuse to shrink" rule — fires on ordinary schema evolution and would be
silenced within a week.
"""
import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))
import qou_substrate.witness as w  # noqa: E402


def _existing(tmp_path, name, script_file, extra_data=None, **top):
    """Write a committed-looking witness produced by `script_file`."""
    body = {
        "computation": name,
        "scriptFile": script_file,
        "allPassed": True,
        "assertions": [],
    }
    body.update(top)
    if extra_data is not None:
        body["data"] = extra_data
    (tmp_path / f"{name}.witness.json").write_text(json.dumps(body) + "\n")


def _builder(tmp_path, name, script_name):
    script = tmp_path / script_name
    script.write_text("# a producer\n")
    return w.WitnessBuilder(name=name, _script_path=str(script),
                            output_dir=str(tmp_path))


def test_refuses_poorer_witness_from_a_different_producer(tmp_path):
    """The qou-okl8 case: different producer, fields would be lost."""
    _existing(tmp_path, "poles", "per_irrep_pole_atom.py",
              extra_data={"atom_chi_fingerprint": {"q0": "1.1"},
                          "per_generator_crossings": [1, 2],
                          "max_term_lambda": [4, 2]})

    b = _builder(tmp_path, "poles", "per_irrep_pole_deuteron_h6.py")
    b.add_data("max_term_lambda", [4, 2])          # keeps one, drops two

    with pytest.raises(RuntimeError) as exc:
        b.save()

    msg = str(exc.value)
    assert "REFUSING to overwrite" in msg
    assert "per_irrep_pole_atom.py" in msg          # names the owner
    assert "atom_chi_fingerprint" in msg            # names what is lost
    assert "per_generator_crossings" in msg
    assert "qou-okl8" in msg

    # and the on-disk file is untouched
    got = json.loads((tmp_path / "poles.witness.json").read_text())
    assert got["scriptFile"] == "per_irrep_pole_atom.py"
    assert "atom_chi_fingerprint" in got["data"]


def test_same_producer_may_drop_fields(tmp_path):
    """Schema evolution by the OWNER is not this guard's business.

    This is the false positive a naive shrink-guard would produce, and the
    reason the ownership half of the condition exists.
    """
    _existing(tmp_path, "evolving", "owner.py",
              extra_data={"old_field": 1, "kept": 2})

    b = _builder(tmp_path, "evolving", "owner.py")
    b.add_data("kept", 2)                           # drops `old_field`
    b.save()                                        # must not raise

    got = json.loads((tmp_path / "evolving.witness.json").read_text())
    assert "old_field" not in got.get("data", {})


def test_different_producer_may_write_a_richer_witness(tmp_path):
    """A consolidation that loses nothing is legitimate — note, don't refuse."""
    _existing(tmp_path, "consolidating", "narrow.py",
              extra_data={"kept": 1})

    b = _builder(tmp_path, "consolidating", "general.py")
    b.add_data("kept", 1)
    b.add_data("extra", 2)
    b.save()                                        # must not raise

    got = json.loads((tmp_path / "consolidating.witness.json").read_text())
    assert got["scriptFile"] == "general.py"
    assert got["data"]["extra"] == 2


def test_override_env_permits_a_deliberate_takeover(tmp_path):
    _existing(tmp_path, "handover", "old.py", extra_data={"gone": 1})

    b = _builder(tmp_path, "handover", "new.py")
    b.add_data("other", 2)

    os.environ[w._TAKEOVER_OVERRIDE_ENV] = "1"
    try:
        b.save()                                    # must not raise
    finally:
        del os.environ[w._TAKEOVER_OVERRIDE_ENV]

    got = json.loads((tmp_path / "handover.witness.json").read_text())
    assert got["scriptFile"] == "new.py"


def test_nested_payload_shape_changes_do_not_trip_the_guard(tmp_path):
    """Only top-level and `data.*` keys are compared.

    Per-partition tables and result lists legitimately change shape run to
    run; walking into them would make the guard fire on ordinary recomputation,
    which is the other way a guard like this dies.
    """
    _existing(tmp_path, "nested", "a.py",
              extra_data={"table": {"rows": [{"lam": [3], "chi": "1"},
                                             {"lam": [2, 1], "chi": "2"}]}})

    b = _builder(tmp_path, "nested", "b.py")
    b.add_data("table", {"rows": [{"lam": [3], "chi": "9"}]})   # fewer rows
    b.save()                                        # must not raise


def test_path_qualified_scriptfile_is_not_a_producer_change(tmp_path):
    """`computations/foo.py` and `foo.py` are the same producer.

    `save()` writes a bare `.name`, but 32 committed witnesses carry a
    path-qualified `scriptFile` from older producers, 29 of which still
    resolve to a live file. Raw string comparison would flag every one of them
    on its next run — enough false alarms to get the guard switched off.
    """
    _existing(tmp_path, "qualified", "computations/owner.py",
              extra_data={"dropped_later": 1, "kept": 2})

    b = _builder(tmp_path, "qualified", "owner.py")   # bare name, same file
    b.add_data("kept", 2)                             # and it drops a field
    b.save()                                          # must not raise

    got = json.loads((tmp_path / "qualified.witness.json").read_text())
    assert got["scriptFile"] == "owner.py"


def test_no_existing_witness_is_never_a_takeover(tmp_path):
    b = _builder(tmp_path, "fresh", "brand_new.py")
    b.add_data("x", 1)
    b.save()                                        # must not raise
    assert (tmp_path / "fresh.witness.json").exists()
