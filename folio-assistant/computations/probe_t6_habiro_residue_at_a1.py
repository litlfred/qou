"""
probe_t6_habiro_residue_at_a1.py — m_p chain Item C from PR #671.

Question: is T6 at A=1 truncated or actually small at the full
residue depth?

The Habiro residue T6 for the proton at A=1 currently reads
``0.98 MeV`` from ``term6-habiro-residue-mpfr-50dps.witness.json``.
The audit at
``docs/audits/2026-05-17-m-p-chain-closure-gap-analysis.md`` asks
whether this value reflects the full series or is truncated by
the cyclotomic-residue pipeline's depth parameter ``k``.

This probe surveys the existing T6 witness for the convergence
pattern across atoms and reports whether T6 at A=1 looks
structurally small or merely truncated.

OBSERVED PATTERN (existing witness, cyclotomic depth k_default):

  A=1 (proton):     T6 ≈ +0.98  MeV    [|T6| / m_p ≈ 0.001]
  A=2 (deuteron):   T6 ≈ +55.8   MeV   [|T6| / m_D ≈ 0.03]
  A=3 (tritium):    T6 ≈ -21375  MeV   [|T6| / m_T ≈ 7.6]    ← divergent
  A=4 (helium-4):   T6 ≈ +692957 MeV   [|T6| / m_He4 huge]   ← extremely divergent

The divergent T6 at tritium (|T6| > m_T) is the smoking-gun:
the residue series at higher A is structurally NOT convergent
at the current truncation depth.  Either:

  - the truncation k is too small at higher A → the residue tail
    is being aggressively chopped (probe item C's question), OR
  - T6 is fundamentally NOT a small correction at A ≥ 3 — the
    series structure changes.

For A=1 specifically the value ~1 MeV is consistent with a small
convergent tail, but without re-running ``term6_residues_at_roots.py``
at multiple depths we cannot rule out a truncation artefact.

This probe DOCUMENTS the per-A pattern and the open question; the
deep re-run (recomputing residues at depth k+10, k+20, …) is
deferred (each tritium-level run is minutes-of-sympy work; ⁴He
is hours per the audit doc).

CONCLUSION: T6 at A=1 is small either by structural convergence
(plausible — quadratic Habiro residue at single-strand baryon is
small) or by aggressive truncation matching the small target.
Distinguishing requires a per-A residue-depth sweep.  Recommended:
do not invest in T6 closure until B (T5 attribution) is resolved,
since T5 dominates the gap.
"""
from __future__ import annotations

import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

T6_WIT = HERE / "term6-habiro-residue-mpfr-50dps.witness.json"


def _fmt(x, dps=30):
    try:
        return mp.nstr(x, dps, strip_zeros=False)
    except Exception:
        return str(x)


def main() -> int:
    print("=" * 78)
    print("  Item C: T6 Habiro residue at A=1 — convergence/truncation audit")
    print("=" * 78)

    w = (WitnessBuilder("probe-t6-habiro-residue-at-a1", engine="mpmath")
         .set_description(
             "m_p chain Item C from PR #671 audit: survey the existing T6 "
             "witness for the per-A convergence pattern.  Documents whether "
             "T6 at A=1 (≈0.98 MeV) is structurally small or truncated; "
             "full residue-depth sweep is deferred (compute-heavy)."
         ))
    body = w.add_upstream(T6_WIT)

    records = (body.get("results_by_atom")
               or body.get("data", {}).get("results_by_atom", []))
    if not records:
        print("  ERROR: term6 witness has no results_by_atom")
        return 1

    # CODATA atomic masses for normalisation (read from the validation
    # set — used for COMPARISON only, no prediction inputs)
    from codata_constants import (
        M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
        M_D_MEV_VALIDATION, M_T_MEV_VALIDATION,
    )
    M_BY_A = {
        1: mpf(str(M_P_MEV_VALIDATION)),  # A=1 nucleon scale (proton)
        2: mpf(str(M_D_MEV_VALIDATION)),  # deuteron
        3: mpf(str(M_T_MEV_VALIDATION)),  # tritium
    }

    out = []
    print(f"  {'A':>2} {'source':<14s} {'T6 (MeV)':>18s} {'M_codata (MeV)':>16s} "
          f"{'|T6|/M':>12s} {'note':>30s}")
    print("  " + "-" * 90)
    for r in records:
        A = r.get("A")
        src = r.get("source_particle", "")
        t6_str = r.get("term6_b_pred_mev_50dps")
        if t6_str is None:
            continue
        t6 = mpf(t6_str)
        m_codata = M_BY_A.get(A)
        ratio = abs(t6) / m_codata if m_codata else None
        if ratio is None:
            ratio_str = "N/A"
            note = "no CODATA ref"
        elif ratio > 1:
            ratio_str = f"{float(ratio):.3f}"
            note = "DIVERGENT — truncation suspect"
        elif ratio > 0.1:
            ratio_str = f"{float(ratio):.3f}"
            note = "large fraction of M"
        else:
            ratio_str = f"{float(ratio):.5f}"
            note = "small / convergent-looking"
        print(f"  {A:>2} {src:<14s} {_fmt(t6, 10):>18s} "
              f"{_fmt(m_codata, 10) if m_codata else 'N/A':>16s} "
              f"{ratio_str:>12s}  {note}")
        out.append({
            "A": A, "source": src,
            "T6_MeV": _fmt(t6),
            "M_codata_MeV": _fmt(m_codata) if m_codata else None,
            "abs_T6_over_M": _fmt(ratio) if ratio is not None else None,
            "interpretation": note,
        })

    print()
    print("  Conclusion:")
    print("    - T6 at A=1 ≈ 0.98 MeV is consistent with either a structurally")
    print("      small convergent tail OR an aggressive truncation that")
    print("      happens to match a small target.  Distinguishing requires")
    print("      a residue-depth sweep (re-run term6_residues_at_roots.py")
    print("      with k = k_default + Δ for proton, see how T6 moves).")
    print("    - T6 at A=3 (tritium) is DIVERGENT (|T6| > m_T).  This is the")
    print("      smoking gun that the cyclotomic truncation is too small at")
    print("      higher A.  Whether A=1 has a similar (smaller-magnitude)")
    print("      problem is the open audit question.")
    print()
    print("  Recommended workplan: pause Item C; address Item B (T5) first")
    print("  since T5 = -7.79 dominates the m_p chain gap by ~order 10.")

    w.add_data("rows", out)
    w.add_data("conclusion",
               "T6 at A=1 is consistent with either small-convergent or "
               "aggressive-truncation; T6 at A=3 (tritium) DIVERGENT under "
               "the current truncation depth.  Full per-A residue-depth "
               "sweep deferred (compute-heavy).  Item B (T5) takes priority.")
    # Fixed expected row count (Copilot review on PR #757) — catches
    # an upstream T6 witness that drops the A=1..4 rows.
    EXPECTED_T6_ROWS = 4  # A ∈ {1, 2, 3, 4}
    w.add_assertion(
        "t6_witness_loaded",
        computed=len(out),
        expected=EXPECTED_T6_ROWS,
        tolerance=0,
    )
    print(f"  Witness: {w.save().name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
