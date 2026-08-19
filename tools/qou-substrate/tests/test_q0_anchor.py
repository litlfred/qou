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


def test_stamp_does_not_overwrite_a_declared_anchor():
    """A `q0Anchor` the producer already wrote WINS over manifest resolution.

    `build()` has always had this guard (`if "q0Anchor" not in witness`);
    `stamp_staleness_metadata` did not, so the two writers of one field
    disagreed and this path silently relabelled explicit declarations.

    The case that caught it is `"ambiguous"` — a producer that evaluates at
    BOTH pins on purpose, which is not resolvable from the manifest and can
    only be declared. `markov/peel_anchor_identification_probe.py` declares it
    and got `"proton"` stamped over it from the running script's manifest
    entry. A witness asserting a pin its contents do not carry is precisely
    what this field exists to prevent, so the relabel defeated the mechanism
    while looking like it was applying it.
    """
    payload = {"q0Anchor": "ambiguous", "result": 1.0}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="python",
    )
    assert payload["q0Anchor"] == "ambiguous"
    # No `q0Value` is invented alongside a declaration that has none: an
    # ambiguous payload spans both pins, so asserting either one is wrong.
    assert "q0Value" not in payload


def test_stamp_still_fills_in_an_undeclared_anchor():
    """The guard must not turn the stamper into a no-op.

    Most producers never touch `q0Anchor` and rely on the stamper to resolve
    it. Guarding the overwrite is only correct if THIS path is untouched —
    otherwise the fix trades a rare mislabel for a mass regression to
    Q0_ANCHOR_MISSING.
    """
    payload = {"result": 1.0}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="python",
    )
    assert payload["q0Anchor"] in ("muon", "proton")


def test_explicit_kwarg_still_wins_on_an_undeclared_payload():
    """`q0_anchor=` is the same declaration, one call frame out.

    The guard keys on the PAYLOAD, so an explicit argument must keep beating
    manifest resolution when the payload itself declares nothing.
    """
    payload = {"result": 1.0}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="python",
        q0_anchor="muon", q0_value="1.10997859555",
    )
    assert payload["q0Anchor"] == "muon"
    assert payload["q0Value"] == "1.10997859555"




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


def test_stamp_records_independent_without_a_value():
    """`independent` states the compute never reads q₀, so it carries no value.

    A `q0Value` next to this label is a contradiction the consistency audit
    reports as Q0_FLIP, so the stamp must not manufacture one.
    """
    payload = {}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="python",
        q0_anchor="independent",
    )
    assert payload["q0Anchor"] == "independent"
    assert "q0Value" not in payload


def _tmpdir():
    import tempfile
    return tempfile.TemporaryDirectory()


def test_save_carries_forward_independent():
    """An independence declaration survives a rebuild, like any recorded pin.

    Fixture-free on purpose: the direct-run path at the bottom of this file
    skips anything taking a pytest fixture, and this invariant is worth having
    under both runners.
    """
    import json
    from pathlib import Path as _P

    with _tmpdir() as d:
        tmp = _P(d)
        script = tmp / "qfree_producer.py"
        script.write_text("# a producer that never reads q0\n")
        out = tmp / "qfree.witness.json"
        out.write_text(json.dumps({
            "computation": "qfree",
            "scriptFile": "qfree_producer.py",
            "allPassed": True,
            "assertions": [],
            "q0Anchor": "independent",
        }) + "\n")

        b = w.WitnessBuilder(name="qfree", _script_path=str(script),
                             output_dir=str(tmp))
        b.save()

        got = json.loads(out.read_text())
        assert got["q0Anchor"] == "independent", "independence claim was dropped"
        assert "q0Value" not in got


def test_save_drops_independent_when_payload_gains_a_q0():
    """The mirror of the muon/proton payload-evidence check.

    If a producer acquires a q₀ dependency, a carried-forward `independent`
    would vouch for layer-freedom that no longer holds — strictly worse than
    dropping it, since Q0_ANCHOR_MISSING is a tolerated state.
    """
    import json
    from pathlib import Path as _P

    with _tmpdir() as d:
        tmp = _P(d)
        script = tmp / "now_uses_q0.py"
        script.write_text("# this producer grew a q0 dependency\n")
        out = tmp / "grew.witness.json"
        out.write_text(json.dumps({
            "computation": "grew",
            "scriptFile": "now_uses_q0.py",
            "allPassed": True,
            "assertions": [],
            "q0Anchor": "independent",
        }) + "\n")

        b = w.WitnessBuilder(name="grew", _script_path=str(script),
                             output_dir=str(tmp))
        b.add_data("q0", "1.1099785827513808075916690956107688798744991218736")
        b.save()

        got = json.loads(out.read_text())
        assert "q0Anchor" not in got, (
            "a stale independence claim survived onto a witness that now "
            "records a proton q0")


def test_save_carries_forward_the_reason_with_the_anchor():
    """`q0AnchorReason` rides with the anchor it explains.

    The token alone is a thin record — a reader who finds only `"independent"`
    has to re-derive the import cone to check it, which is the work the
    declaration exists to save (bean `qou-mw1p`).
    """
    import json
    from pathlib import Path as _P

    with _tmpdir() as d:
        tmp = _P(d)
        script = tmp / "qfree_with_reason.py"
        script.write_text("# a producer that never reads q0\n")
        out = tmp / "reasoned.witness.json"
        out.write_text(json.dumps({
            "computation": "reasoned",
            "scriptFile": "qfree_with_reason.py",
            "allPassed": True,
            "assertions": [],
            "q0Anchor": "independent",
            "q0AnchorReason": "free parameter u; no substrate value read",
        }) + "\n")

        b = w.WitnessBuilder(name="reasoned", _script_path=str(script),
                             output_dir=str(tmp))
        b.save()

        got = json.loads(out.read_text())
        assert got["q0Anchor"] == "independent"
        assert got.get("q0AnchorReason") == (
            "free parameter u; no substrate value read"
        ), "the reason was dropped while its anchor survived"


def test_save_drops_the_reason_with_the_anchor():
    """A reason must not outlive the anchor it explains.

    Left behind, it would explain a label that is no longer on the witness —
    worse than no reason at all, because it reads as provenance for a claim
    nothing is making.
    """
    import json
    from pathlib import Path as _P

    with _tmpdir() as d:
        tmp = _P(d)
        script = tmp / "grew_a_dep.py"
        script.write_text("# this producer grew a q0 dependency\n")
        out = tmp / "orphan.witness.json"
        out.write_text(json.dumps({
            "computation": "orphan",
            "scriptFile": "grew_a_dep.py",
            "allPassed": True,
            "assertions": [],
            "q0Anchor": "independent",
            "q0AnchorReason": "no substrate value read",
        }) + "\n")

        b = w.WitnessBuilder(name="orphan", _script_path=str(script),
                             output_dir=str(tmp))
        b.add_data("q0", "1.1099785827513808075916690956107688798744991218736")
        b.save()

        got = json.loads(out.read_text())
        assert "q0Anchor" not in got
        assert "q0AnchorReason" not in got, (
            "the reason outlived the anchor it explains — it now reads as "
            "provenance for a claim the witness no longer makes")


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


# NOTE: this MUST stay at the end of the file. It enumerates `globals()`, so
# any test defined BELOW it is invisible to the direct-run path — which is how
# two tests added on 2026-08-15 silently never ran that way (pytest collects
# them regardless, since it imports the whole module first).
if __name__ == "__main__":
    import inspect
    ran = skipped = 0
    for name, fn in sorted(globals().items()):
        if not (name.startswith("test_") and callable(fn)):
            continue
        # This runner cannot supply pytest fixtures. Skip loudly rather than
        # crash: moving this block to the end (2026-08-15) exposed a test
        # taking `tmp_path`, which the old placement had hidden by never
        # reaching it at all.
        if inspect.signature(fn).parameters:
            print(f"skip {name}  (needs pytest fixtures: "
                  f"{', '.join(inspect.signature(fn).parameters)})")
            skipped += 1
            continue
        fn()
        print(f"ok   {name}")
        ran += 1
    print(f"q0-anchor: {ran} passed, {skipped} skipped "
          f"(run under pytest for full coverage)")
