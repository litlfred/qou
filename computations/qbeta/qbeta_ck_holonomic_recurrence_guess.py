"""qbeta_ck_holonomic_recurrence_guess — c_11+ attempt via D-finiteness.

The structural ladder above the rational case (Step 2 / #1823 proved the c_k are
NOT low-order constant-coefficient C-finite ⇒ F not low-degree rational). The
next class up — which SUBSUMES the cosh-avatar / generating-function hypothesis
(#1824) — is **holonomic (D-finite)**: do the c_k satisfy a *polynomial*-
coefficient recurrence `∑_i p_i(n)·c_{n-i} = 0` (deg p_i ≤ r)? Every coefficient
sequence of an algebraic, exp/cosh, hypergeometric, or q-difference-ODE solution
is holonomic. A positive low-order fit would **predict c_11+** outright.

DATA-RELIABILITY CONTEXT (from `2026-06-04-c6-c10-crossanchor-biascorrected-
falsification.md`, on main): the canonical extraction IMPOSES closed forms at
c_2..c_7, then extracts c_8..c_10 FREELY from a single anchor — and c_8 (first
free rung) is erratic. So a NEGATIVE result here is NOT decisive (could be free-
rung extraction noise, not a true non-holonomicity). A POSITIVE result on the
applied+reliable part is the informative branch.

Formalize-first justification (compute-author §3.3): this tests a STRUCTURAL
CLASS (holonomic), not a free fit — the polynomial-recurrence ansatz is the
defining property of D-finiteness, validated by over-determination.

Diagnostic-only; no production wiring.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# Align runtime precision with the witness's recorded compute_dps (the
# canonical COMPUTE_DPS, not a hardcoded 40) so the script, the witness
# precisionMetadata, and the audit all agree (Copilot review #1844). At
# this precision a genuine low-order holonomic recurrence would drive the
# column-normalised σ_min/σ_max to ~1e-(input-precision); see guess_holonomic.
COMPUTE_DPS = set_compute_dps()

# Bias-corrected c_k (#1824 probe 6.a) — the cleaner available series.
CK = {
    2: "-0.9999932040076931361502732", 3: "-1.999996827617395134712207",
    4: "-1.13311756459707959859922", 5: "-1.252711779918944930214874",
    6: "3.010650514307294654575538", 7: "-8.021139527655621439078256",
    8: "-0.2149930668457213266989321", 9: "-297.3428270114312225913704",
    10: "105411380.1026009785765566",
}
# c_2..c_7 are APPLIED (imposed) in the extraction; c_8..c_10 are FREE
# (single-anchor, flagged unreliable). Test both windows.
APPLIED_KS = [2, 3, 4, 5, 6, 7]


def guess_holonomic(ks: list[int], ck: dict[int, mp.mpf], order: int, deg: int):
    """Test for ∑_{i=0}^order p_i(n)·c_{n-i} = 0, deg p_i ≤ deg.

    Unknowns: (order+1)*(deg+1) polynomial coeffs (scale-free → homogeneous).
    Equations: one per usable n. A holonomic recurrence ⇒ the homogeneous
    matrix M is rank-deficient ⇒ σ_min/σ_max → 0. Returns (rel_sv, n_eq,
    n_unk).
    """
    nunk = (order + 1) * (deg + 1)
    ks_sorted = sorted(ks)
    have = set(ck)
    # Row n is usable only if EVERY required term c_{n-i} (i=0..order) is
    # present — robust to non-contiguous ks / missing keys (Copilot #1844):
    # avoids KeyError and the silent inclusion of equations referencing a
    # term that is not in ck. Independent of caller ks ordering (sorted here).
    rows = [n for n in ks_sorted
            if all((n - i) in have for i in range(order + 1))]
    if len(rows) <= nunk:
        return None, len(rows), nunk
    # Build the homogeneous matrix M (n_eq × nunk); columns = p_i monomials.
    M = mp.matrix(len(rows), nunk)
    for r, n in enumerate(rows):
        col = 0
        for i in range(order + 1):
            for dd in range(deg + 1):
                M[r, col] = mp.mpf(n) ** dd * ck[n - i]
                col += 1
    # Column-normalise BEFORE the SVD. The raw columns span a huge dynamic
    # range (the erratic free rung c_10 ≈ 1e8 times the n^deg monomials),
    # which would otherwise dominate the conditioning and inflate the
    # apparent noise floor. Column scaling is a change of variables on the
    # solution vector, so it preserves the null space — rank-deficiency
    # detection is unchanged — while making σ_min numerically meaningful
    # (Copilot #1844, option a).
    for c in range(nunk):
        cn = mp.sqrt(sum(M[r, c] ** 2 for r in range(len(rows))))
        if cn > 0:
            for r in range(len(rows)):
                M[r, c] /= cn
    # Smallest singular value via a DIRECT SVD of M — NOT eigenvalues of
    # MᵀM. Forming MᵀM squares the condition number and inflates the
    # apparent noise floor, which directly biases the holonomic verdict
    # (Copilot #1844, option b). A rank-deficient (holonomic) M ⇒
    # σ_min/σ_max → 0; a full-rank (non-holonomic) M ⇒ σ_min/σ_max = O(1).
    try:
        S = mp.svd_r(M, compute_uv=False)
    except Exception:
        return None, len(rows), nunk
    sv = [abs(s) for s in S]
    smax, smin = max(sv), min(sv)
    rel = smin / smax if smax > 0 else mp.mpf(1)
    return rel, len(rows), nunk


def main() -> int:
    print("=" * 78)
    print("c_k holonomic (D-finite) recurrence guess — c_11+ attempt")
    print("=" * 78)
    ck = {k: mp.mpf(v) for k, v in CK.items()}
    allks = sorted(ck)

    results = {}
    print("\n  Over-determined polynomial-coeff recurrence search:")
    print(f"  {'window':14s} {'order':5s} {'deg':3s} {'n_eq':4s} {'n_unk':5s} "
          f"{'rel_sv':12s} holonomic?")
    for label, ks in (("applied c2..c7", APPLIED_KS), ("full c2..c10", allks)):
        for order in (1, 2):
            for deg in (1, 2):
                rel, neq, nunk = guess_holonomic(ks, ck, order, deg)
                if rel is None:
                    continue
                hol = bool(rel < mp.mpf("1e-12"))
                results[f"{label}|o{order}d{deg}"] = {
                    "rel_sv": mp.nstr(rel, 6), "n_eq": neq, "n_unk": nunk,
                    "holonomic": hol}
                print(f"  {label:14s} {order:<5d} {deg:<3d} {neq:<4d} {nunk:<5d} "
                      f"{mp.nstr(rel, 6):12s} {hol}")

    any_hol = any(v["holonomic"] for v in results.values())
    inconclusive = not results   # every SVD evaluation failed ⇒ no real test
    print("\n" + "=" * 78)
    print("VERDICT (c_11+ attempt):")
    if inconclusive:
        print("  • ⚠ INCONCLUSIVE — no (order,deg) case evaluated (all SVD calls")
        print("    failed). This is NOT a clean negative; the witness assertion")
        print("    'holonomic_search_evaluated' fails so the run can't read green.")
    elif any_hol:
        print("  • A low-order HOLONOMIC recurrence FITS — F is D-finite. This")
        print("    would predict c_11+ via the recurrence. SURFACE to author +")
        print("    cross-anchor before any closure claim (the free rungs are")
        print("    single-anchor; confirm the recurrence on independent data).")
    else:
        print("  • No low-order (order≤2, deg≤2) holonomic recurrence fits — over")
        print("    the over-determined system, no polynomial-coefficient kernel.")
        print("  • NOT DECISIVE for c_11+: the only FREE (independent) rungs")
        print("    (c_8..c_10) are single-anchor-unreliable (c_8 erratic, per the")
        print("    c6-c10 cross-anchor falsification on main). So this is consistent")
        print("    with EITHER F non-holonomic OR free-rung extraction noise.")
        print("  • ⇒ the c_11+ keystone is blocked at the DATA level — and the")
        print("    precision-floor probe (this PR) proves WHY: σ(c_k) = σ_R/u^k,")
        print("    so only c_2,c_3 clear the measured-Q_β floor and c_4+ are below")
        print("    it at ANY anchor count (multi-anchor would need ~1e4 physical")
        print("    anchors). The genuine unblock is a FRAMEWORK DERIVATION of the")
        print("    c_k (Habiro element, parallel α_EM #1521), not an extraction.")
    print()

    w = WitnessBuilder("qbeta-ck-holonomic-recurrence-guess", engine="mpmath")
    w.set_description(
        f"c_11+ attempt: tests whether the c_k are HOLONOMIC (D-finite) — a "
        f"polynomial-coefficient recurrence, the class subsuming the cosh-avatar "
        f"/ generating-function hypothesis (#1824) and one level above the "
        f"rational case Step 2 refuted. No low-order (order≤2, deg≤2) holonomic "
        f"recurrence fits the over-determined system: {any_hol}. NOT decisive — "
        f"the only FREE rungs (c_8..c_10) are single-anchor-unreliable (c6-c10 "
        f"falsification on main), so a negative is consistent with F "
        f"non-holonomic OR extraction noise. The c_11+ keystone is blocked at "
        f"the data level — the precision-floor probe (this PR) proves WHY: "
        f"σ(c_k)=σ_R/u^k, so only c_2,c_3 clear the measured-Q_β floor and c_4+ "
        f"are below it at any anchor count. The genuine unblock is a FRAMEWORK "
        f"DERIVATION of the c_k (Habiro element), not an extraction. "
        f"Formalize-first structural test, not a fit. Diagnostic-only."
    )
    w.add_data("ck_source", "#1824 probe 6.a bias-corrected (cleaner available)")
    w.add_data("applied_rungs", "c_2..c_7 (imposed); c_8..c_10 free/unreliable")
    w.add_data("compute_dps", int(COMPUTE_DPS))
    w.add_data("evaluations", len(results))
    w.add_data("holonomic_fits", {k: {"rel_sv": v["rel_sv"], "holonomic": v["holonomic"]}
                                  for k, v in results.items()})
    w.add_data("genuine_unblock",
               "framework derivation of the c_k (Habiro element, parallel α_EM "
               "#1521): the precision-floor probe (this PR) shows extraction — "
               "single- OR multi-anchor — cannot reach c_4+ (σ(c_k)=σ_R/u^k below "
               "the measured-Q_β floor), so the c_k must be DERIVED from "
               "Hecke/SDP structure, not fitted.")
    # Guard (Copilot #1844): a run where NO (order,deg) case evaluated is
    # INCONCLUSIVE, not a clean negative — fail this assertion so an
    # all-SVD-fail run cannot emit a passing (non-holonomic) witness.
    w.add_assertion(
        name="holonomic_search_evaluated",
        computed=not inconclusive, expected=True, tolerance=0,
        source="≥1 (order,deg) SVD case must evaluate; all-fail ⇒ inconclusive run.",
    )
    w.add_assertion(
        name="low_order_holonomic_recurrence_found",
        computed=bool(any_hol), expected=False, tolerance=0,
        source="No order≤2 deg≤2 holonomic recurrence on the available c_k. "
               "Expected False (and not decisive — free rungs unreliable).",
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 1 if inconclusive else 0


if __name__ == "__main__":
    sys.exit(main())
