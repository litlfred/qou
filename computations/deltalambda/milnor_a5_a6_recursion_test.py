#!/usr/bin/env python3
"""milnor_a5_a6_recursion_test.py — TEST the candidate all-A recursion for the
convention-D Brunnian trace-deficit (bean qou-v7ro).

THE CANDIDATE (from the two EXACT points A=3, A=4, milnor_a4_deficit_h_form.py):

    D_3(h) =  h⁴(h²+3)/(h²+4)
    D_4(h) = −h⁶(h²+2)(h²+3)/(h²+4)
    ⇒  D_4/D_3 = −h²(h²+2)      ⇒  candidate:  D_{A+1}(h) = −h²(h²+2)·D_A(h)

which predicts the closed form  D_A = (−1)^{A−3} h^{2(A−1)}(h²+2)^{A−3}(h²+3)/(h²+4)
and leading coeff (3/4)(−2)^{A−3} (= the measured μ̄_A, A=3..6).

THE TEST (anti-fit: a 2-point ratio only pins the LEADING coeff via the measured
μ̄_A; the recursion claims the WHOLE rational function). So compute the EXACT
convention-D deficit at A=5 (decisive 3rd point) and A=6 (4th), and check the FULL
rational-function identities

    D_5 == −h²(h²+2)·D_4      and      D_6 == −h²(h²+2)·D_5

exactly (sympy simplify == 0). PASS on the full function (not just leading coeff)
is strong evidence for the recursion; a mismatch means the recursion is
leading-order-only and must be reported as such. Either way this does NOT by itself
prove the recursion (that needs a structural TL/strand-addition derivation) and
creates no Lean instance.

Convention D (Jones/Temperley-Lieb; the Lean tauBorromean frame): SIGNED χ_λ,
weights y_{(a,b)}=[a−b+1]/[2]^n, only ≤2-row diagrams contribute. So at A=5 we need
χ for (5),(4,1),(3,2); at A=6 for (6),(5,1),(4,2),(3,3). Brunnian words
w_A = left-normed iterated band commutator [[[[A01,A12],A23],A34],…].

0-fit; exact sympy over ℚ(q); ZERO float64. Long-compute: χ_symbolic on H₅/H₆
words is the bottleneck — run with `-u | tee` per the compute-audit discipline.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# band machinery + exact symbolic characters (SAME code that produced the committed
# a4 χ_λ — reused, not re-derived)
from a4_brunnian_deficit_closed_form import (  # noqa: E402
    band_comm, band_word_to_sigma, chi_symbolic, A01, A12, A23,
)
# convention-D weights + the h-folding, from the A=4 h-form script
from milnor_a4_deficit_h_form import (  # noqa: E402
    q, h, tl_weight, fold_bar_symmetric_to_h,
)

A34 = [(3, 4, +1)]
A45 = [(4, 5, +1)]

_T0 = time.time()


def _log(m):
    print(f"[{time.time()-_T0:7.1f}s] {m}", flush=True)


def two_row_partitions(n):
    """λ ⊢ n with ≤ 2 rows: (n), (n−1,1), …, (⌈n/2⌉, ⌊n/2⌋)."""
    out = [(n,)]
    for b in range(1, n // 2 + 1):
        out.append((n - b, b))
    return out


def deficit_h_conventionD(n, sigma_word):
    """Exact convention-D deficit D_n(h) = 1 − τ_n, τ_n = Σ_{≤2row} y_λ^TL χ_λ, folded to h."""
    tau = sp.Integer(0)
    for lam in two_row_partitions(n):
        w = tl_weight(lam, n)
        if w == 0:
            continue
        _log(f"    χ_{lam} …")
        chi = chi_symbolic(lam, sigma_word)   # exact rational in q
        tau += w * sp.cancel(chi)
    tau = sp.cancel(tau)
    D_q = sp.cancel(1 - tau)
    D_h = sp.cancel(fold_bar_symmetric_to_h(D_q))
    return D_q, D_h


# hardcoded EXACT convention-D h-forms for A=3, A=4 (from milnor_a4_deficit_h_form,
# committed witness) — the recursion's base points, no recompute needed
D3_h = sp.cancel((h**4 * (h**2 + 3)) / (h**2 + 4))
D4_h = sp.cancel((-h**6 * (h**2 + 2) * (h**2 + 3)) / (h**2 + 4))
R = -h**2 * (h**2 + 2)   # candidate recursion factor


def main():
    # sanity: the base recursion the candidate was read off from
    base_ok = sp.simplify(D4_h - R * D3_h) == 0
    _log(f"[base] D4 == R·D3 (defining ratio): {base_ok}")

    _log("building Brunnian σ-words w5, w6 (band iterated commutators)")
    W4 = band_comm(band_comm(A01, A12), A23)
    W5 = band_comm(W4, A34)
    W6 = band_comm(W5, A45)
    w5 = band_word_to_sigma(W5)
    w6 = band_word_to_sigma(W6)
    _log(f"w5 σ-length={len(w5)}  w6 σ-length={len(w6)}")

    results = {"base_D4_eq_R_D3": bool(base_ok),
               "candidate_recursion": "D_{A+1} = -h^2(h^2+2)·D_A",
               "predicted_closed_form": "D_A = (-1)^(A-3) h^(2(A-1)) (h^2+2)^(A-3) (h^2+3)/(h^2+4)"}

    _log("=== A=5 (decisive 3rd point) ===")
    D5_q, D5_h = deficit_h_conventionD(5, w5)
    pred5 = sp.cancel(R * D4_h)
    a5_ok = sp.simplify(D5_h - pred5) == 0
    _log(f"[A5] D5 == R·D4 (full rational function): {a5_ok}")
    _log(f"[A5] D5_h = {D5_h}")
    results["A5"] = {
        "D5_h_form": str(sp.cancel(D5_h)),
        "recursion_D5_eq_R_D4_exact": bool(a5_ok),
        "predicted_D5": str(pred5),
    }

    a6_ok = None
    try:
        _log("=== A=6 (4th point) ===")
        D6_q, D6_h = deficit_h_conventionD(6, w6)
        pred6 = sp.cancel(R * D5_h)
        a6_ok = sp.simplify(D6_h - pred6) == 0
        _log(f"[A6] D6 == R·D5 (full rational function): {a6_ok}")
        results["A6"] = {
            "D6_h_form": str(sp.cancel(D6_h)),
            "recursion_D6_eq_R_D5_exact": bool(a6_ok),
        }
    except Exception as e:  # A=6 may be too heavy; A=5 is the decisive test
        _log(f"[A6] skipped/failed: {e!r}")
        results["A6"] = {"skipped": repr(e)}

    verdict = (
        "RECURSION CONFIRMED on the FULL rational function at A=5"
        + (" and A=6" if a6_ok else "")
        + " — strong evidence D_{A+1}=-h^2(h^2+2)D_A holds for all A; next: structural "
        "TL/strand-addition derivation to PROVE it (would close MilnorExactOrderConjecture "
        "nonvanishing ∀A by induction)."
        if a5_ok else
        "RECURSION FAILS on the full function at A=5 — the -h^2(h^2+2) pattern is "
        "leading-order-only (it reproduces μ̄_A but not the whole deficit). Report as "
        "asymptotic, NOT a closed form. Do not claim the general form."
    )
    results["verdict"] = verdict
    _log(f"[verdict] {verdict}")

    out = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. The stem IS "
            "declared physical_proton in "
            "computations/q0_anchor_manifest.json, and that declaration "
            "cannot stamp this witness: the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build(). Hence the declaration "
            "here, which is the only route that reaches the file."),
        "computation": "milnor-a5-a6-recursion-test",
        "scriptFile": "milnor_a5_a6_recursion_test.py",
        "engine": "python-sympy-exact",
        "free_parameters": 0,
        "description": (
            "Tests the candidate convention-D deficit recursion D_{A+1}=-h^2(h^2+2)D_A "
            "against the EXACT A=5 (and A=6) closed forms — full rational function, not "
            "just leading coeff. Convention D (signed chi, TL weights, 2-row diagrams). "
            "0-fit; exact Q(q); zero float64. No Lean instance created."),
        "results": results,
    }
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    # P30: add the staleness provenance (scriptHash / commitSha /
    # engine) that a hand-rolled dump cannot get from build().
    # The q0Anchor lines just below own the anchor decision and run
    # after this, so their value stands.
    _WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python")
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    out["q0Anchor"] = _q0a
    if _q0v:
        out["q0Value"] = _q0v
    (HERE / "milnor-a5-a6-recursion-test.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    _log("wrote milnor-a5-a6-recursion-test.witness.json")


if __name__ == "__main__":
    main()
