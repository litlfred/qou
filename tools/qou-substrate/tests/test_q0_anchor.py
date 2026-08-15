"""Tests for q₀-anchor provenance (parameterize the muon/proton pin so a
witness value can never be silently misread — bean tnjb flip-flop)."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))

import qou_substrate.witness as w  # noqa: E402


def test_env_override_muon():
    a, v = w.resolve_q0_anchor("whatever.py", env={"QOU_Q0_ANCHOR": "muon"})
    assert a == "muon"
    # The muon pin as the COMPUTE path actually uses it. Do NOT "correct" this
    # to the q_muon_at() value (1.109978595554…): a muon-tagged producer
    # computes with the witness string, so a derived label would disagree with
    # the number the witness reports. See _q0_value_for_anchor's note.
    assert v is None or v.startswith("1.109978595557")


def test_env_override_proton():
    a, _ = w.resolve_q0_anchor("whatever.py", env={"QOU_Q0_ANCHOR": "proton"})
    assert a == "proton"


def test_default_is_proton_when_not_ideal_muon():
    # A stem that is not in the ideal_muon manifest resolves to proton
    # (mirrors q_parameter's runtime default), with an empty env.
    a, _ = w.resolve_q0_anchor("definitely_not_a_real_producer_stem_xyz.py", env={})
    assert a in ("proton", "ambiguous")


def test_stamp_records_anchor_and_preserves_values():
    payload = {"result": 3.14159, "note": "physics value must survive untouched"}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="mpmath",
        q0_anchor="muon", q0_value="1.10997859555733471989976322048322502665620840878015368660798114614493",
    )
    assert payload["q0Anchor"] == "muon"
    assert payload["q0Value"].startswith("1.109978595557")
    # provenance fields are additive — the physics values are untouched
    assert payload["result"] == 3.14159
    assert payload["note"] == "physics value must survive untouched"
    assert payload["engine"] == "mpmath"


def test_explicit_anchor_overrides_resolution():
    payload = {}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="python", q0_anchor="proton",
    )
    assert payload["q0Anchor"] == "proton"


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("all q0-anchor tests passed")


def test_save_carries_forward_a_recorded_pin(tmp_path):
    """Rebuilding a witness must not drop a q₀ pin it already carried.

    The pin is written by `stamp_staleness_metadata`, which a producer has to
    call explicitly — most do not, while ~600 witnesses carry the pin from a
    backfill. Re-running such a producer used to silently drop it: a
    value-preserving write that removes the very guard the pin exists to
    provide.
    """
    import json

    script = tmp_path / "some_producer.py"
    script.write_text("# a producer\n")
    out = tmp_path / "carry-forward.witness.json"
    out.write_text(json.dumps({
        "computation": "carry-forward",
        "scriptFile": "some_producer.py",
        "allPassed": True,
        "assertions": [],
        "q0Anchor": "muon",
        "q0Value": "1.1099785955570000000000000000000000000000000000000",
    }) + "\n")

    b = w.WitnessBuilder(name="carry-forward", _script_path=str(script),
                         output_dir=str(tmp_path))
    b.save()

    got = json.loads(out.read_text())
    assert got["q0Anchor"] == "muon", "recorded pin was dropped on rebuild"
    assert got["q0Value"].startswith("1.109978595557")


def test_save_does_not_invent_a_pin(tmp_path):
    """A witness with no recorded pin must not acquire one on rebuild.

    Q0_ANCHOR_MISSING is a tolerated state; inventing "proton" here would
    assert a pin the producer never established.
    """
    import json

    script = tmp_path / "unpinned_producer.py"
    script.write_text("# a producer\n")
    out = tmp_path / "unpinned.witness.json"
    out.write_text(json.dumps({
        "computation": "unpinned",
        "scriptFile": "unpinned_producer.py",
        "allPassed": True,
        "assertions": [],
    }) + "\n")

    b = w.WitnessBuilder(name="unpinned", _script_path=str(script),
                         output_dir=str(tmp_path))
    b.save()

    got = json.loads(out.read_text())
    assert "q0Anchor" not in got, "rebuild invented a pin that was never recorded"


# RETRACTED 2026-08-15. Two tests stood here asserting the muon label must
# equal `q_muon_at()`, on the premise that re-running `q_pinning_50_digit.py`
# would flip the label to a proton value. That premise is FALSE — the producer
# is manifest-tagged `ideal_muon`, so `q_at` returns the witness string and the
# producer is a fixed point. The tests encoded the wrong invariant and would
# have failed correct code.
#
# The real defect is that the muon 50-dps constant is CIRCULAR (its producer
# reads, via `q_at`, the witness it writes). A test for that belongs with a fix
# that gives the muon anchor a real derivation and moves the label and the
# computed value together — not here.
