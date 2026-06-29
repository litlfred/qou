"""
chi_convention_audit.py — audit chi-*.witness.json files for an explicit,
correct crossing-CONVENTION label.

## Why this audit exists (2026-06-28, bean b0vf)

There are TWO production conventions for the per-λ character
χ^λ(β_atomic(Z, N)) at the substrate q_0, and they give *different*
values by design — the character is the trace of a *different braid
word* in each:

  1. **sign-only-crossings** (Geck–Pfeiffer / `chi_q_via_gp`): the braid
     word is a list of `(sign, gen)` pairs — every crossing is ±1.
     Producers: `chi_at_q0_via_matrix_m_mpfr.py`, the Rust lossless
     producers (`chi_4he_via_rust_lossless.py`, `chi_via_rust_lossless.py`),
     and anything tagged `rust-chi-q-via-gp-lossless` / `matrix-m-chi-q-via-gp`.
     Output files: `chi-*-at-q0-50dps-matrix-m.witness.json`,
     `chi-at-q0-matrix-m-*.witness.json`, `chi-*-rust-lossless-*`.

  2. **averaged-crossings** (Hoefsmit seminormal, full `atom_braid_word_3A`
     triples — `d ≠ 0` entries weight crossings by per-color factors):
     "different physics, different character values". Producers:
     `chi_at_q0_via_hoefsmit_mpfr.py` (q_0) and
     `chi_at_q_inv_via_native_mpfr.py` (q_0^{-1}, the bar-image cache,
     same word). Output files: plain `chi-*-at-q0-50dps.witness.json`
     and `chi-*-at-qinv-50dps.witness.json`.

The smoking-gun (from `chi_at_q0_via_matrix_m_mpfr.py`'s own docstring):
on the deuteron the two paths give χ^(6) = 1.56 (sign-only) vs 11.02 =
q_0^23 (averaged) at q_0 ≈ 1.11.

## The bug class this catches

A chi witness that does NOT declare its `convention` can be silently
consumed by a downstream binding / τ_M compute under the WRONG
convention — the two value sets differ by large factors, so the
binding number is quietly wrong. The `*-matrix-m` files already declare
`"convention": "sign-only-crossings"`; the Hoefsmit/native families
historically declared nothing. This audit:

  - **flags** every chi value-witness missing a `convention` field
    (`missing-inferable` if the producer is in the registry below;
    `missing-ambiguous` if not — needs manual classification);
  - **flags MISMATCH** (critical): a declared convention that contradicts
    what the producer should emit;
  - **flags unknown-convention** (a `convention` string not in the
    known set);
  - with `--fix`, **stamps** the inferable conventions into the witness
    (idempotent), recording `convention_inferred_by` for provenance.

`--strict` exits 1 on the hard contradictions (mismatch / unknown).
Missing labels are reported and counted but are warn-only by default so
the gate stays focused on contradictions; run `--fix` to clear the
inferable ones.

Usage:
    python3 chi_convention_audit.py            # report
    python3 chi_convention_audit.py --strict   # exit 1 on mismatch/unknown
    python3 chi_convention_audit.py --fix       # stamp inferable conventions

Output: structured stdout report + chi-convention-audit.witness.json
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

SIGN_ONLY = "sign-only-crossings"
AVERAGED = "averaged-crossings"

# Convention strings recognised as valid for a chi value-witness. A
# `convention` field outside this set is flagged `unknown-convention`.
KNOWN_CONVENTIONS = {SIGN_ONLY, AVERAGED}

# ---- Canonical reconciliation (per docs/canonical-derivation-cheat-sheet.md
# §Phase 5q + docs/audits/2026-06-09-binding-trace-convention-split.md) ----
# The canonical per-λ character convention is sign-only-crossings (= the
# convention-split audit's "convention A": matrix-M / chi_q_via_gp, deuteron
# χ^(6) = 11.02 = q₀²³). It is the production character convention — the
# marshalling `marshal_to_chi_lambda_braid` maps the averaged p-n form
# (c=1, d=−h/2) → (sign=+1) ("# averaged → σ convention"), so production
# chi_lambda_braid and the derived_chi_catalogue use sign-only — and it is
# consistent with the canonical Jones–Markov trace C
# (markov/markov_trace_canonical, prop:categorical-mass-markov).
CANONICAL_CONVENTION = SIGN_ONLY
# averaged-crossings = the convention-split audit's "convention B"
# (markov_trace_3A Plancherel, deuteron χ^(6) = 1.56), DEPRECATED for binding
# (markov_trace_3A docstring: "Do not use for new binding calculations").
# Legitimate only as an opt-in audit-trail probe (pn_convention=
# "strict_averaged"); NOT canonical. Witnesses in this convention are flagged
# `off-canonical` (informational — not a --strict failure, they are valid
# probes — but a downstream binding consume should use the sign-only sibling).
DEPRECATED_FOR_BINDING = {
    AVERAGED: "convention B (markov_trace_3A Plancherel) — deprecated for "
              "binding; canonical per-λ character is sign-only (A), per the "
              "2026-06-09 convention-split audit",
}

# Producer identity → convention. Matched as a substring against the
# witness's `producer` / `scriptFile` field (the reliable signal). This is
# the single source of truth for expected convention; extend it (not the
# computation-id patterns) when a new producer is added.
PRODUCER_CONVENTION: dict[str, str] = {
    # sign-only / chi_q_via_gp
    "chi_at_q0_via_matrix_m_mpfr.py": SIGN_ONLY,
    "chi_4he_via_rust_lossless.py": SIGN_ONLY,
    "chi_via_rust_lossless.py": SIGN_ONLY,
    "rust-chi-q-via-gp-lossless": SIGN_ONLY,
    "matrix-m-chi-q-via-gp": SIGN_ONLY,
    # averaged / Hoefsmit full atom_braid_word_3A
    "chi_at_q0_via_hoefsmit_mpfr.py": AVERAGED,
    "chi_at_q_inv_via_native_mpfr.py": AVERAGED,
    # symbolic + numeric catalogue (same full-canonical-word as Hoefsmit):
    # value-confirmed averaged — deuteron symbolic χ^(6) @q0 = 1.5598
    # matches the averaged numerical cache (1.5599), NOT sign-only (11.02).
    "delta_lambda_empirical_tabulation.py": AVERAGED,
    # FREE-config χ via LR induction-product of the averaged proton/neutron
    # h3 caches — the LR product of averaged characters IS the averaged free
    # character; chi_free_via_lr validates against these existing caches.
    "chi_free_via_lr.py": AVERAGED,
}

# Witnesses that are NOT atom-braid χ caches — they evaluate a *different*
# braid object, so the sign-only/averaged crossing dichotomy does not apply.
# Reported as `not-applicable`, never stamped. Keyed on computation-id stem.
CONVENTION_NOT_APPLICABLE: dict[str, str] = {
    "chi-content-eigenbasis":
        "twist-eigenbasis rewrite of the Lean-proved H₃ χ relations — "
        "not a braid-word evaluation",
    "chi-content-single-mode":
        "isolates the c=0 (2,1)-block winding tower (q-Bessel test) — "
        "not a full atom-braid character",
    "chi-lambda-he4-full-partition-table":
        "heuristic 4·Borromean tensor template, not atom_braid_word_3A — "
        "different braid",
    "chi-lambda-multi-block-first-measurement":
        "exploratory multi-block first-measurement (pyhecke chi_lambda_braid); "
        "no per-partition atom-braid cache",
}

# Fallback when a witness records no usable producer field: infer from the
# `computation` id. Tried in order; first match wins. These mirror the
# producer output-name conventions documented in the module docstring.
COMPUTATION_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"-at-q0-50dps-matrix-m$"), SIGN_ONLY),
    (re.compile(r"^chi-at-q0-matrix-m-"), SIGN_ONLY),
    (re.compile(r"rust-lossless"), SIGN_ONLY),
    # Hoefsmit q_0 family (incl. the FREE-config LR partner): plain
    # -at-q0-50dps, NOT -matrix-m. Free caches are the averaged free
    # character (LR product of the averaged nucleon caches).
    (re.compile(r"^chi-.*-at-q0-50dps$"), AVERAGED),
    # native bar-image q_0^{-1} family (incl. free): -at-qinv-50dps.
    (re.compile(r"^chi-.*-at-qinv-50dps$"), AVERAGED),
    # symbolic catalogue `chi-{atom}-h{n}` with no producer field (the he4
    # sibling lacks one): same full-canonical-word family — value-confirmed
    # averaged (he4 symbolic [12] @q0 = 2.41966 = the averaged numeric cache).
    (re.compile(r"^chi-[a-z0-9-]+-h\d+$"), AVERAGED),
]

# Computation ids that are NOT chi value-witnesses (audits / meta) — skip.
EXCLUDE_SUBSTRINGS = ("audit",)


def _producer_field(w: dict) -> str:
    return str(w.get("producer") or w.get("scriptFile") or "")


def expected_convention(w: dict, comp: str) -> tuple[str | None, str]:
    """Return (expected_convention | None, basis) for a witness dict.

    `comp` is the computation id (falls back to the clean filename stem when
    the witness carries no `computation` field). `basis` explains how the
    expectation was derived: 'producer', 'computation-id', or 'none'.
    """
    prod = _producer_field(w)
    for key, conv in PRODUCER_CONVENTION.items():
        if key and key in prod:
            return conv, f"producer:{key}"
    for pat, conv in COMPUTATION_PATTERNS:
        if pat.search(comp):
            return conv, f"computation-id:/{pat.pattern}/"
    return None, "none"


def classify(path: Path) -> dict:
    try:
        w = json.loads(path.read_text())
    except Exception as e:  # noqa: BLE001
        return {"path": path.name, "status": "parse-error", "error": str(e)}

    stem = path.stem.replace(".witness", "")
    comp = str(w.get("computation") or stem)
    declared = w.get("convention")

    na_reason = CONVENTION_NOT_APPLICABLE.get(comp) or CONVENTION_NOT_APPLICABLE.get(stem)
    if na_reason is not None:
        return {
            "path": path.name, "computation": comp, "declared": declared,
            "expected": None, "expected_basis": "not-applicable",
            "producer": _producer_field(w), "status": "not-applicable",
            "reason": na_reason,
        }

    expected, basis = expected_convention(w, comp)

    if declared is not None:
        if declared not in KNOWN_CONVENTIONS:
            status = "unknown-convention"
        elif expected is not None and declared != expected:
            status = "mismatch"
        else:
            status = "ok"
    else:
        status = "missing-inferable" if expected is not None else "missing-ambiguous"

    return {
        "path": path.name,
        "computation": comp,
        "declared": declared,
        "expected": expected,
        "expected_basis": basis,
        "producer": _producer_field(w),
        "status": status,
    }


def chi_value_witnesses(d: Path) -> list[Path]:
    out = []
    for fp in sorted(d.glob("chi-*.witness.json")):
        comp = fp.stem.replace(".witness", "")
        if any(s in comp for s in EXCLUDE_SUBSTRINGS):
            continue
        out.append(fp)
    return out


def apply_fix(path: Path, expected: str, basis: str) -> bool:
    """Stamp `convention` into an unlabeled witness. Idempotent. Returns
    True if the file was modified."""
    w = json.loads(path.read_text())
    if w.get("convention") is not None:
        return False
    # Insert convention + a provenance note that it was back-filled (this
    # script is not the original producer, so be transparent).
    w["convention"] = expected
    w["convention_inferred_by"] = (
        f"chi_convention_audit.py --fix ({basis})"
    )
    path.write_text(json.dumps(w, indent=2, ensure_ascii=False) + "\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="audit chi witness conventions")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 on mismatch / unknown-convention")
    parser.add_argument("--fix", action="store_true",
                        help="stamp the inferable conventions into witnesses")
    args = parser.parse_args()

    records = [classify(fp) for fp in chi_value_witnesses(HERE)]

    by_status: dict[str, list[dict]] = {}
    for r in records:
        by_status.setdefault(r["status"], []).append(r)

    fixed: list[str] = []
    if args.fix:
        for r in by_status.get("missing-inferable", []):
            if apply_fix(HERE / r["path"], r["expected"], r["expected_basis"]):
                fixed.append(r["path"])
                r["status"] = "ok"
                r["declared"] = r["expected"]
        # recompute buckets after fix
        by_status = {}
        for r in records:
            by_status.setdefault(r["status"], []).append(r)

    # ---- report ----
    print(f"{'witness':<54} {'declared':<22} {'expected':<22} {'status'}")
    print("-" * 118)
    for r in sorted(records, key=lambda x: (x["status"], x["path"])):
        print(f"{r['path']:<54} {str(r.get('declared')):<22} "
              f"{str(r.get('expected')):<22} {r['status']}")

    mismatch = by_status.get("mismatch", [])
    unknown = by_status.get("unknown-convention", [])
    missing_inferable = by_status.get("missing-inferable", [])
    missing_ambiguous = by_status.get("missing-ambiguous", [])
    not_applicable = by_status.get("not-applicable", [])
    parse_error = by_status.get("parse-error", [])

    # Canonical reconciliation: among labeled witnesses, which sit in the
    # deprecated-for-binding (averaged / convention B) convention. Legitimate
    # audit-trail probes, but a binding consume should use the sign-only (A)
    # sibling. Informational — does NOT gate --strict.
    labeled = [r for r in records
               if r["status"] in ("ok", "not-applicable") and r.get("declared")]
    off_canonical = [r for r in labeled if r["declared"] in DEPRECATED_FOR_BINDING]
    canonical = [r for r in labeled if r["declared"] == CANONICAL_CONVENTION]

    print()
    print("=== SUMMARY ===")
    print(f"  total chi value-witnesses : {len(records)}")
    print(f"  ok                        : {len(by_status.get('ok', []))}")
    print(f"  mismatch        (CRITICAL): {len(mismatch)}")
    print(f"  unknown-convention        : {len(unknown)}")
    print(f"  missing-inferable         : {len(missing_inferable)}")
    print(f"  missing-ambiguous (manual): {len(missing_ambiguous)}")
    print(f"  not-applicable (diff braid): {len(not_applicable)}")
    print(f"  parse-error               : {len(parse_error)}")
    print(f"  --- canonical reconciliation ---")
    print(f"  canonical (sign-only / A) : {len(canonical)}")
    print(f"  off-canonical (avg / B)   : {len(off_canonical)}  "
          f"[deprecated for binding; valid only as audit-trail probes]")
    if args.fix:
        print(f"  stamped this run          : {len(fixed)}")
        for p in fixed:
            print(f"    + {p}")
    if missing_ambiguous:
        print("  MISSING-AMBIGUOUS (need manual classification):")
        for r in missing_ambiguous:
            print(f"    {r['path']}  (producer={r['producer'] or '—'})")

    builder = WitnessBuilder("chi-convention-audit")
    builder.set_description(
        "Audit chi-*.witness.json for an explicit, correct crossing-"
        "CONVENTION label (sign-only-crossings vs averaged-crossings). "
        "Catches the bug class where an unlabeled chi witness is consumed "
        "downstream under the wrong convention (the two value sets differ "
        "by large factors). See docs/audits/2026-06-28-chi-convention-"
        "label-audit.md (bean b0vf)."
    )
    builder.add_data("records", records)
    builder.add_data("totals", {
        "scanned": len(records),
        "ok": len(by_status.get("ok", [])),
        "mismatch": len(mismatch),
        "unknown_convention": len(unknown),
        "missing_inferable": len(missing_inferable),
        "missing_ambiguous": len(missing_ambiguous),
        "not_applicable": len(not_applicable),
        "parse_error": len(parse_error),
    })
    builder.add_data("canonical_reconciliation", {
        "canonical_convention": CANONICAL_CONVENTION,
        "canonical_basis": "convention A (matrix-M / chi_q_via_gp); production "
                           "character convention (marshalling maps averaged→sign); "
                           "consistent with Jones–Markov trace C "
                           "(prop:categorical-mass-markov). Ref: "
                           "docs/audits/2026-06-09-binding-trace-convention-split.md",
        "canonical_count": len(canonical),
        "off_canonical_averaged": [r["path"] for r in off_canonical],
        "off_canonical_note": DEPRECATED_FOR_BINDING.get(AVERAGED),
    })
    if args.fix:
        builder.add_data("stamped_this_run", fixed)

    builder.add_assertion(
        "no_convention_mismatch",
        computed=len(mismatch), expected=0, tolerance=0,
        unit="count", source="audit (this script)",
    )
    builder.add_assertion(
        "no_unknown_convention",
        computed=len(unknown), expected=0, tolerance=0,
        unit="count", source="audit (this script)",
    )
    builder.add_assertion(
        "no_unlabeled_chi_witness",
        computed=len(missing_inferable) + len(missing_ambiguous),
        expected=0, tolerance=0, unit="count",
        source="audit (this script)",
    )
    builder.save()

    # --strict gates on the hard contradictions; missing is warn-only.
    if args.strict and (mismatch or unknown or parse_error):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
