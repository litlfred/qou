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
    assert v is None or v.startswith("1.109978595557")  # muon pin


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
