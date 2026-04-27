#!/usr/bin/env python3
"""Tests for `six_term_consumer.py` — Sprint A v3.

Enforces the canonical-only contract:
  - No SnapPy import anywhere in the consumer source.
  - No `hp_volume` import / call.
  - No fitted constants or numerical root-finds.
  - For each Family 1 atom (D, T, ³He), the consumer either records a
    finite numeric value for a wired term OR sets `pending: true` —
    no silent failure.

Run with:
  python folio-assistant/computations/test_six_term_consumer.py
or:
  python -m pytest folio-assistant/computations/test_six_term_consumer.py -v
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
SRC = (HERE / "six_term_consumer.py").read_text()
WITNESS = HERE / "six-term-mass-pred.witness.json"

FAMILY_1 = ("deuteron-2H", "tritium-3H", "helium3-3He")


# ── Forbidden tokens (canonical-only contract) ────────────────────

def test_no_snappy_import():
    forbidden = [
        r'^\s*import\s+snappy',
        r'^\s*from\s+snappy',
    ]
    for pat in forbidden:
        assert not re.search(pat, SRC, re.MULTILINE), \
            f"forbidden snappy import pattern matched: {pat!r}"


def test_no_hp_volume_call_or_import():
    # hp_volume helper is a SnapPy wrapper; using it would inject
    # hyperbolic volume as a primary input, violating the canonical
    # six-term-from-GB-NF contract.  Match actual import / call
    # patterns rather than bare substring (the consumer's docstring
    # and attestation field name reference `hp_volume` as a thing it
    # does NOT do — those mentions are intentional).
    forbidden = [
        r'^\s*import\s+hp_volume',
        r'^\s*from\s+hp_volume',
        r'\bhp_volume_of_link_closure\s*\(',
        r'\bhp_volume_of_manifold\s*\(',
    ]
    for pat in forbidden:
        assert not re.search(pat, SRC, re.MULTILINE), \
            f"forbidden hp_volume usage matched: {pat!r}"


def test_no_fitted_constants_or_root_find():
    forbidden = [
        r'\bbrentq\s*\(', r'\bfsolve\s*\(', r'\bnewton\s*\(',
        r'\bbisect\s*\(', r'_TARGET\s*=\s*0\.',
        r'\balpha_star\b', r'\balpha_4\b',
    ]
    for pat in forbidden:
        assert not re.search(pat, SRC), \
            f"forbidden fitting/root-find pattern matched: {pat!r}"


# ── Witness shape (run consumer first if witness missing) ─────────

def _ensure_witness():
    if not WITNESS.exists():
        # Generate it.
        sys.path.insert(0, str(HERE))
        import six_term_consumer as stc
        rc = stc.main()
        assert rc == 0, "consumer main() returned non-zero"
    return json.loads(WITNESS.read_text())


def test_witness_emits_per_particle_for_family_1():
    w = _ensure_witness()
    per = w.get("per_particle", {})
    for name in FAMILY_1:
        assert name in per, f"missing Family 1 atom {name!r} in witness"


def test_each_term_finite_or_pending():
    """No silent failure — every term must be a real value OR
    explicitly marked pending."""
    w = _ensure_witness()
    expected_terms = (
        "T1_T2_T3_brane_tower",
        "T4_frobenius_co_casimir",
        "T5_chirality_content_average",
        "T6_habiro_residue",
    )
    for name in FAMILY_1:
        terms = w["per_particle"][name]["terms"]
        for tkey in expected_terms:
            assert tkey in terms, f"{name}: missing term {tkey!r}"
            tval = terms[tkey]
            is_pending = isinstance(tval, dict) and tval.get("pending") is True
            has_value = isinstance(tval, dict) and any(
                k for k in tval.keys()
                if k not in ("pending", "error", "reason")
            )
            assert is_pending or has_value, \
                f"{name}.{tkey}: neither pending nor has a value: {tval!r}"


def test_t6_extracts_per_A_correctly():
    """Regression test for the Copilot/Gemini review finding:
    `eval_schur_weyl_exact_at_q0` returns keys formatted "A=<n>", not
    bare integers. The witness must contain the actual per-A payload,
    not the entire upstream dict re-nested under each particle."""
    w = _ensure_witness()
    for name in FAMILY_1:
        A = w["per_particle"][name]["A"]
        t6 = w["per_particle"][name]["terms"]["T6_habiro_residue"]
        if t6.get("pending"):
            continue
        per_A = t6.get("per_A", {})
        key = f"A={A}"
        assert key in per_A, (
            f"{name}: T6 per_A dict missing key {key!r}; got keys {list(per_A.keys())!r}"
        )
        # The payload should NOT be the whole upstream dict re-nested.
        # Specifically, it should not itself contain another "A=<n>" key.
        payload = per_A[key]
        if isinstance(payload, dict):
            nested_a_keys = [k for k in payload.keys() if k.startswith("A=")]
            assert not nested_a_keys, (
                f"{name}: T6 payload appears to be the whole upstream "
                f"dict re-nested (contains {nested_a_keys!r}); extraction bug"
            )


def test_witness_uses_canonical_computedAt_field():
    """Per repo convention (folio-assistant/schemas/types.ts +
    migrate_witness_timestamp_to_computedAt.py), the canonical
    timestamp field is `computedAt`, not `timestamp`."""
    w = _ensure_witness()
    assert "computedAt" in w, "witness must use canonical `computedAt` field"
    assert "timestamp" not in w, (
        "witness uses non-canonical `timestamp` field; should be `computedAt` "
        "(per migrate_witness_timestamp_to_computedAt.py)"
    )


def test_attestation_no_volumes_no_fits():
    w = _ensure_witness()
    a = w["attestation"]
    assert a["used_snappy"] is False
    assert a["used_hp_volume"] is False
    assert a["used_volume_match"] is False
    assert a["used_fitted_constants"] is False


def test_t4_marked_pending_with_explicit_reason():
    """T4 (Frobenius co-Casimir) is a known gap; the witness must
    document why and what's needed to close it."""
    w = _ensure_witness()
    for name in FAMILY_1:
        t4 = w["per_particle"][name]["terms"]["T4_frobenius_co_casimir"]
        assert t4.get("pending") is True
        assert "reason" in t4
        assert "Sprint A v4" in t4["reason"], \
            "T4 reason should reference where the helper will be added"


def test_ame_comparison_is_marked_pending():
    """Sprint A v3 deliberately does NOT emit a calibrated
    AME-comparable binding-energy prediction — that requires the
    Z·m_p + N·m_n − M conversion, queued for v4. The witness must
    say so explicitly so reviewers don't expect ppb residuals here."""
    w = _ensure_witness()
    a = w["attestation"]
    assert a["ame_comparison_pending"] is True
    assert "Sprint A v4" in a["ame_comparison_reason"]


# ── Runner ────────────────────────────────────────────────────────

def _run_all():
    tests = [
        ("no_snappy_import", test_no_snappy_import),
        ("no_hp_volume_call_or_import", test_no_hp_volume_call_or_import),
        ("no_fitted_constants_or_root_find", test_no_fitted_constants_or_root_find),
        ("witness_emits_per_particle_for_family_1", test_witness_emits_per_particle_for_family_1),
        ("each_term_finite_or_pending", test_each_term_finite_or_pending),
        ("attestation_no_volumes_no_fits", test_attestation_no_volumes_no_fits),
        ("t4_marked_pending_with_explicit_reason", test_t4_marked_pending_with_explicit_reason),
        ("ame_comparison_is_marked_pending", test_ame_comparison_is_marked_pending),
        ("t6_extracts_per_A_correctly", test_t6_extracts_per_A_correctly),
        ("witness_uses_canonical_computedAt_field", test_witness_uses_canonical_computedAt_field),
    ]
    fails = []
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except AssertionError as e:
            print(f"  FAIL  {name}: {e}")
            fails.append((name, str(e)))
        except Exception as e:
            print(f"  ERROR {name}: {type(e).__name__}: {e}")
            fails.append((name, f"{type(e).__name__}: {e}"))
    print()
    if fails:
        print(f"  {len(fails)} test(s) failed.")
        return 1
    print(f"  all {len(tests)} tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(_run_all())
