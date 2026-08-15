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
    # Derived, not a hardcoded prefix. This assertion previously read
    # `startswith("1.109978595557")` — the STALE committed value — so it was
    # pinning the bug in place: the canonical muon q0 begins 1.109978595554,
    # and a correct implementation FAILED this test. Comparing against
    # `q_muon_at()` cannot rot that way.
    if v is not None:
        import mpmath as mp
        from qou_substrate.constants import q_muon_at
        assert v.startswith(mp.nstr(q_muon_at(30), 14, strip_zeros=False)[:14])


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
        q0_anchor="muon", q0_value="1.1099785955541805752815940796095093779932822799587",
    )
    assert payload["q0Anchor"] == "muon"
    assert payload["q0Value"].startswith("1.109978595554")
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


# ── the flip-flop this stamping exists to prevent ─────────────────────────

def test_muon_label_is_derived_not_read_from_a_witness():
    """The muon q0 label must be DERIVED, not read from a committed witness.

    Regression test for a latent bug that was live until 2026-08-15:
    `_q0_value_for_anchor("muon")` read
    `computations/q-pinning-50-digit.witness.json` -> `derived_50_digit.q`,
    but that producer sets `Q = q_at(mp.dps)` -- the PROTON solve. The
    committed witness held a muon-range value only because it predated that
    change, so simply RE-RUNNING the producer (an ordinary, encouraged act)
    would have made every subsequent muon-anchored witness stamp a proton
    value under `q0Anchor: "muon"`. Nothing would have failed; the label
    would just have started lying.

    This asserts the property that makes that impossible: the muon label
    matches `q_muon_at()` and is nowhere near the proton pin.
    """
    import mpmath as mp
    from qou_substrate.constants import q_muon_at, Q_50_DIGIT_STR

    label = w._q0_value_for_anchor("muon")
    assert label is not None
    assert label.startswith(mp.nstr(q_muon_at(50), 40, strip_zeros=False)[:40])

    # The two anchors are 11.5 ppb apart -- a muon label that has drifted onto
    # the proton value is the exact failure mode, so assert the separation.
    assert abs(float(label) - float(Q_50_DIGIT_STR)) / float(label) > 1e-9


def test_muon_label_survives_the_pinning_witness_being_wrong():
    """The label must not depend on that witness file at all any more.

    Even with the stale file present and holding a non-reproducible value,
    the derived label is the canonical one.
    """
    label = w._q0_value_for_anchor("muon")
    STALE = "1.10997859555733471989976322048322502665620840878015"
    assert not label.startswith(STALE[:20]), (
        "muon label regressed to the stale committed witness value"
    )
