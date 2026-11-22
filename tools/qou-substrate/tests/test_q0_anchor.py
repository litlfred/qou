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
    # The muon pin as the COMPUTE path actually uses it. The original comment
    # here warned against "correcting" this to a derived value, because a
    # muon-tagged producer computes with the witness string and a derived label
    # would disagree with the number the witness reports. That intent is kept
    # and is now satisfied by construction: PR #5500 made the WITNESS ITSELF
    # derive, so reading the same resolver the compute path reads IS the witness
    # string, and the hard-coded prefix was the thing that had gone stale.
    assert v is None or v == str(w._q0_value_for_anchor("muon"))


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
        assert got.get("q0Anchor") != "independent", (
            "a stale independence claim survived onto a witness that now "
            "records a proton q0")
        # TIGHTENED 2026-08-24 (bean qou-aj91). This asserted `"q0Anchor" not
        # in got` — correct when the only two outcomes were "keep the stale
        # label" or "keep none". `build()` now reads the pin off the payload,
        # so the third and best outcome exists: the stale claim is gone AND
        # the witness carries the pin its own numbers show. Asserting the
        # exact label is STRICTER than asserting absence, not looser.
        assert got.get("q0Anchor") == "proton"
        assert got["q0Value"].startswith("1.10997858275")


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
        # See the note in test_save_drops_independent_when_payload_gains_a_q0:
        # the witness now carries the pin its payload shows, not none.
        assert got.get("q0Anchor") == "proton"
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


# ── payload-first anchor resolution (bean qou-aj91) ──────────────────
#
# `q0Anchor`/`q0Value` answer "at which pin was this payload computed?".
# Resolving them from the manifest answers a different question — what the
# producer was CONFIGURED to do — and the two diverge for the 85 producers
# that read `q-pinning-50-digit.witness.json` -> `derived_50_digit.q`
# directly: that string IS the muon anchor's definition, 67 of the 85 are
# absent from the manifest, and the manifest's runtime default is proton.

# DERIVED, not frozen (bean qou-y98b). These were literals, and the muon one
# went stale the moment PR #5500 landed: it made the muon anchor DERIVE from the
# live CODATA-2022 m_mu/m_e instead of reading a frozen string, so the pin moved
# 1.109978595557... -> 1.109978595642... Five tests here then failed, and the two
# payload-evidence ones failed in a way that reads as a logic bug rather than
# stale data -- a payload carrying the OLD literal is no longer muon evidence,
# so it fell through to proton and the assertion said `'proton' == 'muon'`.
#
# Re-freezing at the new value would reintroduce exactly what #5500 removed and
# would break again at the next CODATA revision. Reading them from the same
# resolver the compute path uses keeps these tests about BEHAVIOUR -- does
# payload evidence outrank the manifest, does an explicit declaration win --
# which is what they were always for.
_MUON = str(w._q0_value_for_anchor("muon"))
_PROTON = str(w._q0_value_for_anchor("proton"))
# A REAL path (the stamper hashes the file) whose stem is absent from
# `q0_anchor_manifest.json`, so it resolves to the runtime default, proton.
_UNLISTED = __file__


def test_payload_evidence_beats_the_manifest_default():
    """An unlisted producer defaults to proton — unless its payload says muon."""
    payload = {"parameters": {"q0": _MUON}}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="mpmath",
    )
    assert payload["q0Anchor"] == "muon"
    assert payload["q0Value"] == _MUON      # derived, see _MUON above


def test_payload_evidence_is_read_before_serialisation():
    """The commonest producer idiom stamps BEFORE `json.dump(..., default=str)`.

    At that moment `parameters.q0` is still an `mpmath.mpf`, so a check keyed
    on `isinstance(v, str)` reads the evidence as absent on exactly the
    witnesses that carry it — and fails silently, falling back to the manifest.
    Measured on `meson_mass_from_hecke`, whose committed witness reads as muon
    while a live re-run stamped proton.
    """
    mpmath = __import__("mpmath")
    mpmath.mp.dps = 60
    payload = {"parameters": {"q0": mpmath.mpf(_MUON)}}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="mpmath",
    )
    assert payload["q0Anchor"] == "muon"


def test_low_precision_value_contributes_no_evidence():
    """`str(mpf)` at dps 15 is `1.10998` — it distinguishes neither pin.

    Such a value must fall through to the manifest rather than be guessed at:
    the two pins agree to 8 significant figures.
    """
    assert w._q0_anchor_from_payload({"parameters": {"q0": 1.10998}}) is None


def test_a_payload_carrying_both_pins_asserts_neither():
    both = {"a": {"q0": _MUON}, "b": {"q_0": _PROTON}}
    assert w._q0_anchor_from_payload(both) is None


def test_a_declared_payload_anchor_still_wins_over_evidence():
    """A producer that states its own pin is never overruled — including a
    cross-anchor probe declaring `ambiguous` over a payload that happens to
    record one readable q₀."""
    payload = {"q0Anchor": "ambiguous", "parameters": {"q0": _MUON}}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="mpmath",
    )
    assert payload["q0Anchor"] == "ambiguous"


def test_explicit_kwarg_still_wins_over_payload_evidence():
    payload = {"parameters": {"q0": _MUON}}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="mpmath",
        q0_anchor="proton", q0_value=_PROTON,
    )
    assert payload["q0Anchor"] == "proton"


def test_resolver_requires_a_declaration_when_there_is_no_evidence():
    """`build()`'s rule is unchanged for the no-evidence case: without a
    positive declaration nothing is stamped, because Q0_ANCHOR_MISSING is a
    tolerated, visible state while a defaulted pin is a silent claim."""
    a, v = w.resolve_q0_anchor_payload_first(
        {"nothing": "here"}, _UNLISTED, require_declared=True, env={},
    )
    assert (a, v) == (None, None)


def test_evidence_outranks_the_declaration_requirement():
    """A recorded q₀ IS a positive declaration — a stronger one than a manifest
    entry, since the producer made it by computing rather than by being listed."""
    a, _ = w.resolve_q0_anchor_payload_first(
        {"parameters": {"q0": _MUON}}, _UNLISTED, require_declared=True, env={},
    )
    assert a == "muon"


def test_payload_evidence_does_not_move_any_value():
    """The whole point: this changes the STAMP, never the numbers."""
    payload = {"parameters": {"q0": _MUON}, "result": 3.14159, "note": "keep me"}
    before = dict(payload["parameters"]), payload["result"], payload["note"]
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="mpmath",
    )
    assert (dict(payload["parameters"]), payload["result"], payload["note"]) == before


# ── q0_anchor=False: the q₀-independent opt-out (bean qou-4un2 / qou-iph3) ──


def test_false_declares_independence_and_stamps_no_pin():
    """A producer that never touches q₀ DECLARES that; it does not get a pin.

    The resolver has no "no anchor" outcome, so before this existed every
    caller got a pin whether or not the numbers depended on one — and an inert
    stamp is byte-identical to a load-bearing one. That is what this guards,
    and it still holds: no proton, no muon, no q0Value.

    CONTRACT CHANGED (bean qou-y98b): `False` now stamps
    `q0Anchor: "independent"` rather than omitting the field. Omission was
    byte-identical to never having asked, so a correctly-migrated
    q0-independent producer was indistinguishable from an unmigrated one, and
    `q0_anchor_ratchet.py --strict` counted it as Q0_ANCHOR_MISSING and failed
    on it. "independent" asserts no pin, so it does not reintroduce the inert
    anchor this branch exists to prevent — it is an established verdict of
    `q0_anchor_consistency_audit.py` (Q0_INDEPENDENT).
    """
    payload = {"result": 42}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="python", q0_anchor=False,
    )
    assert payload["q0Anchor"] == "independent"
    assert payload["q0AnchorReason"]          # audit reports _NO_REASON otherwise
    assert "q0Value" not in payload           # the original point: NO pin
    assert payload["q0Anchor"] not in ("proton", "muon")


def test_false_still_stamps_the_provenance_fields():
    """Opting out of the ANCHOR must not opt out of provenance — that is the
    whole point of the migration this flag exists for."""
    payload = {"result": 42}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="python", q0_anchor=False,
    )
    for field in ("scriptHash", "scriptCommitSha", "commitSha", "engine",
                  "computedAt", "durationMs"):
        assert field in payload, field


def test_false_beats_payload_evidence():
    """`False` is a caller DECLARATION and outranks payload evidence.

    A q₀-looking number in the payload is not proof the result depends on it —
    a probe may record the pin it ran beside without consuming it.
    """
    payload = {"parameters": {"q0": _MUON}, "result": 42}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="python", q0_anchor=False,
    )
    # The declaration still wins over the payload's q₀-looking number: the
    # result is "independent", NOT the muon pin that evidence would resolve to.
    assert payload["q0Anchor"] == "independent"
    assert "q0Value" not in payload


def test_none_and_str_are_unchanged_by_the_new_branch():
    """Regression: the default and the explicit-string paths still stamp.

    Deliberately asserts THAT an anchor is stamped, not WHICH one. What the
    `q0_anchor=False` branch could plausibly break is the other two paths
    silently stamping nothing; which anchor a given payload resolves to is a
    different question, owned by the resolution tests above.

    Naming a specific anchor here also made this test hostage to a value it is
    not about. It first read `assert default.get("q0Anchor") == "muon"` off
    `_MUON`, and `fca08de7d` ("muon anchor -> CODATA 2022 (owner ruling)")
    moved the anchor-defining witness to a different one of the THREE values
    the corpus calls "the muon q₀" (they diverge at the 13th significant
    digit). That turned this into a sixth instance of the five failures that
    commit already left in this module -- and it passed in a full-file run
    anyway, because an earlier test leaks `QOU_Q0_ANCHOR=muon` into the
    environment and masks it. A test that only passes via another test's
    leaked state is worse than one that fails honestly.
    """
    default = {"parameters": {"q0": _MUON}}
    w.WitnessBuilder.stamp_staleness_metadata(
        default, script_path=_UNLISTED, engine="python",
    )
    assert default.get("q0Anchor"), "the default path must still resolve and stamp"

    explicit = {"result": 1}
    w.WitnessBuilder.stamp_staleness_metadata(
        explicit, script_path=_UNLISTED, engine="python", q0_anchor="proton",
    )
    assert explicit.get("q0Anchor") == "proton"


def test_only_False_suppresses_not_any_falsy_value():
    """`is False`, not truthiness — so the only value that drops the field is
    the one that means it.

    An empty string is NOT suppression and is NOT resolved: it reaches the
    explicit-declaration branch and is stamped verbatim, which is this
    function's pre-existing behaviour for any non-None argument. Asserted so a
    future change to the `is False` check cannot quietly start swallowing other
    falsy values. (I first documented `""` as falling through to resolution;
    this test disagreed and the test was right.)
    """
    payload = {"parameters": {"q0": _MUON}}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="python", q0_anchor="",
    )
    assert payload.get("q0Anchor") == ""
    assert "q0Anchor" in payload


def test_engine_none_preserves_the_payloads_own_declaration(tmp_path):
    """`engine=None` keeps what the producer already declared.

    Without it the helper's unconditional `payload["engine"] = engine`
    DOWNGRADES a producer's own, more specific value. Measured while migrating
    bean qou-4un2: `qbeta-5two-leading-odd-datum` went from "sympy+mpmath" to
    "python" while `engineVersion` still read "sympy 1.14.0, mpmath 1.4.1" --
    an internally contradictory witness written by a provenance pass.
    """
    script = tmp_path / "p.py"
    script.write_text("# producer\n")

    declared = {"engine": "sympy+mpmath"}
    w.WitnessBuilder.stamp_staleness_metadata(
        declared, script_path=str(script), engine=None, q0_anchor=False)
    assert declared["engine"] == "sympy+mpmath"

    bare = {}
    w.WitnessBuilder.stamp_staleness_metadata(
        bare, script_path=str(script), engine=None, q0_anchor=False)
    assert bare["engine"] == "python", "None on a bare payload falls back"


def test_engine_default_is_unchanged_by_the_None_sentinel(tmp_path):
    """The 603 call sites relying on the default must not shift.

    `engine` defaults to the literal "python", NOT to None, precisely so that
    adding the sentinel changes no existing caller's behaviour. If someone
    "tidies" the default to None later, every one of those call sites silently
    starts preserving instead of overwriting -- which is the opposite of what
    they were written against.
    """
    script = tmp_path / "p.py"
    script.write_text("# producer\n")
    payload = {"engine": "sympy+mpmath"}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=str(script), q0_anchor=False)
    assert payload["engine"] == "python"


def test_unmappable_anchor_warns_but_still_stamps(capsys):
    """An anchor outside the five-token vocabulary WARNS and is still written.

    Warn, not raise, and the trade is deliberate: stamping happens at the END
    of a producer, and several here run for tens of minutes. Raising would
    discard the whole compute to correct a label. The repo settled this same
    question once already in the same direction —
    `scripts/precommit-precision-warn.sh` was offered as a blocking hook and
    the owner declined it (2026-08-25).

    The value is stamped VERBATIM, unchanged, so the guard cannot silently
    guess a token the producer did not choose — and
    `test_only_False_suppresses_not_any_falsy_value` above keeps passing.
    """
    payload = {"parameters": {"q0": _MUON}}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="python",
        q0_anchor="proton (experimental pin)",
    )
    assert payload["q0Anchor"] == "proton (experimental pin)"
    assert "not one of" in capsys.readouterr().err


def test_valid_tokens_and_False_do_not_warn(capsys):
    """The five tokens and `False` are silent — a warning nobody can silence
    by writing correct code is a warning that gets learned as noise."""
    for token in w.Q0_ANCHOR_VOCABULARY:
        payload = {"parameters": {"q0": _MUON}}
        w.WitnessBuilder.stamp_staleness_metadata(
            payload, script_path=_UNLISTED, engine="python", q0_anchor=token)
        assert capsys.readouterr().err == "", token

    payload = {"parameters": {"q0": _MUON}}
    w.WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=_UNLISTED, engine="python", q0_anchor=False)
    assert payload["q0Anchor"] == "independent"
    assert capsys.readouterr().err == ""


def test_bool_True_is_not_a_documented_anchor_and_warns():
    """`q0_anchor=True` reads as "yes, it has an anchor" and is refused.

    `False` means "declare this witness q0-independent (`q0Anchor: 'independent'`)";
    `True` has no corresponding meaning and raises `ValueError` rather than
    stamping the literal boolean `True` (which the anchor audit cannot map;
    found in `markov_bond_rule_forces_pairwise_probe`, bean qou-eggf).
    """
    import pytest

    payload = {"parameters": {"q0": _MUON}}
    with pytest.raises(ValueError, match="q0_anchor=True has no meaning"):
        w.WitnessBuilder.stamp_staleness_metadata(
            payload, script_path=_UNLISTED, engine="python", q0_anchor=True)
    assert "q0Anchor" not in payload


def test_manifest_vocabulary_tokens_normalise_to_witness_tokens(tmp_path, capsys):
    """`ideal_muon` / `physical_proton` (manifest vocabulary) normalise to
    `muon` / `proton` (witness vocabulary) without warning (bean `qou-9du2`)."""
    import json

    p_proton = {"result": 1}
    w.WitnessBuilder.stamp_staleness_metadata(
        p_proton, script_path=_UNLISTED, engine="python",
        q0_anchor="physical_proton",
    )
    assert p_proton["q0Anchor"] == "proton"
    assert p_proton.get("q0Value")
    assert capsys.readouterr().err == ""

    p_muon = {" q0": 1, "q0Anchor": "ideal_muon"}
    w.WitnessBuilder.stamp_staleness_metadata(
        p_muon, script_path=_UNLISTED, engine="python",
    )
    assert p_muon["q0Anchor"] == "muon"
    assert p_muon.get("q0Value")
    assert capsys.readouterr().err == ""

    script = tmp_path / "m_vocab.py"
    script.write_text("# test\n")
    wb = w.WitnessBuilder.wrap_legacy(
        "m-vocab-wrap", {"q0Anchor": "physical_proton", "result": 2},
        script_path=script, output_dir=tmp_path,
    )
    out_wrap = json.loads(wb.save().read_text())
    assert out_wrap["q0Anchor"] == "proton"
    assert out_wrap.get("q0Value")
    assert capsys.readouterr().err == ""

    wb2 = w.WitnessBuilder(
        "m-vocab-extra", engine="python", output_dir=tmp_path, _script_path=script,
    )
    out_extra = json.loads(wb2.save(extra={"q0Anchor": "ideal_muon"}).read_text())
    assert out_extra["q0Anchor"] == "muon"
    assert out_extra.get("q0Value")
    assert capsys.readouterr().err == ""
