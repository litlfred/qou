#!/usr/bin/env python3
"""🛑 SUPERSEDED — do NOT quote `B_pred_MeV`, the T-vs-³He ordering, or this
module's committed witness as a binding-energy result. Marked 2026-09-27 on
owner instruction ("resolve issues"), bean `qou-7xa5`. Kept for provenance and
comparison, exactly as `binding_canonical.py` is.

**TWO INDEPENDENT GROUNDS**, either one sufficient. Both are checkable against a
corpus artifact without re-running anything here.

1. **The FUNCTIONAL is the refuted one.** `B_xy = E_0·(tr_M_free − tr_M_atom)` is
   a constant times `Δtr`, the same law class as `binding_canonical.B_MeV`, whose
   own banner records the refutation: `tr_M` is MULTIPLICATIVE along the chain
   while binding energy is EXTENSIVE, and `Δtr/tr_free = 1 − exp(−S)` exactly —
   within 7.7e-4 of 1 by A = 11. Above that, `Δtr` does not merely MIS-SCALE the
   binding, it does not CONTAIN it. The replacement is forced rather than chosen
   (`log` is the unique multiplicative-to-additive map) and consumes the SAME
   derived bond factors:

       B = E_0 · log( tr_M(W_free) / tr_M(W_atom) )

   in `computations/binding_log_free_energy.py`.

2. **The BOND COMPOSITION is the complete graph, which is structurally
   refuted.** `n_pp + n_pn + n_nn = C(Z,2) + Z·N + C(N,2) = C(A,2)` — every pair
   bonded. `QOU.Mass.CoordinationSaturation.complete_graph_no_saturation`
   (sorry-free) proves that for `ε > 0`, `perNucleonComplete ε A = ε·C(A,2)/A`
   exceeds EVERY bound: no finite `B/A` plateau exists, so observed saturation
   refutes complete-graph coordination structurally, not merely at ⁴He.

   **Scope note — the Lean is stated for a UNIFORM `ε`, and this module has
   three bond energies.** The extension is a one-line monotonicity argument and
   it is MINE, not the theorem's: with all three bond bindings positive,
   `B(A) ≥ min(B_pp,B_pn,B_nn)·C(A,2)`, so `B/A` is unbounded by the same
   theorem applied at `ε = min`. Measured 2026-09-27 the three are `0.6421 /
   0.6155 / 0.5636` MeV, all positive, so the hypothesis holds here. Do not
   restate this as though the Lean covered the three-type case directly.
   The replacement's composition is a CHAIN (`(Z−1), 1, (N−1)` — `A−1` bonds,
   bounded degree), which is the point of that change as much as the `log` is.

**THE COMMITTED WITNESS IS STALE, AND ITS HEADLINE ASSERTION HAS FLIPPED.**
Committed `computedAt` 2026-06-22, `allPassed: true`; a fresh run 2026-09-27
reports FAILURES. The module's whole purpose — the T-vs-³He discriminator — went
from MATCHES to **MISMATCH**:

    bond        2026-06-22   2026-09-27   |   iso    B_pred then -> now    err% then -> now
    B_pp           2.3785       0.6421    |   D       2.4914 ->  0.6155    +12.0 -> -72.3
    B_pn           2.4914       0.6155    |   T       7.5151 ->  1.7946    -11.4 -> -78.8
    B_nn           2.5323       0.5636    |   3He     7.3612 ->  1.8732     -4.6 -> -75.7
                                          |   4He    14.8763 ->  3.6678    -47.4 -> -87.0

**DO NOT re-run this and commit the regenerated witness.** That publishes a red
for a law already known to be wrong, which is noise, not a finding. The drift is
recorded here and on `qou-7xa5`; the witness stays as the 2026-06-22 artifact it
is. Route (b) of that bean — porting the bond-type decomposition onto the
log-ratio law — is a separate arc and has not been taken.

Two further defects, recorded so nobody reads them as live findings. The
`ordering:` line hardcoded `<` between all three bonds, which was true in June
(2.379 < 2.491 < 2.532) and is false now (0.642 > 0.616 > 0.564); it now derives
its operators. And the witness carries **17 raw float64 fields** (`float(E0)`,
`float(B[xy])`, `B_pred_MeV`, `AME_MeV`, `err`, `A_growth`) — the run's own
ratchet warns about them. They are NOT fixed here, because serializing them
correctly would only take effect by regenerating the witness, which the
paragraph above forbids.

**WHAT SURVIVES.** This is a scope-(a) negative on the functional and the
composition — NOT an exclusion of bond-TYPE decomposition as an ingredient. The
three derived 2-nucleon sub-braid traces are the same objects the log-ratio law
consumes, and isospin-dependent bonds remain the T-vs-³He discriminator in
principle. What is excluded is `constant × Δtr` summed over the complete graph.

Original docstring follows, unchanged.

DERIVATION — bond-TYPE per-bond binding sum (level 1, pure-Python, 0 fit).

Level-0 (derive_binding_bond_sum.py) used one isospin-symmetric bond and got
A-growth 1.65×→6.00×, but couldn't distinguish T from ³He (both C(A,2)=3). This
level derives the three bond TYPES from their 2-nucleon sub-braids and sums by
composition:

    B(K) = n_pp·B_pp + n_pn·B_pn + n_nn·B_nn ,
    B_xy = E_0 · ( tr_M(W_free^{xy}) − tr_M(W_atom^{xy}) ) ,   xy ∈ {pp, pn, nn},

with the 2-nucleon traces from the canonical pure-Python Markov trace
(binding_canonical.binding_canonical(Z,N): pn=(1,1)=deuteron, pp=(2,0)=diproton,
nn=(0,2)=dineutron) and E_0 = m_e/(q₀(q₀−1)) ≈ 4.186 MeV (calibration-fixed). The
deuteron (pn) is the derived base case. Bond composition from (Z,N):
    n_pp = C(Z,2),  n_nn = C(N,2),  n_pn = Z·N.

ZERO fit. AME used only for the final comparison.

Note: this uses the SCALAR signed Δtr_M (collapse-first; the double-modulus
|tr_free|−|tr_atom| was a non-archimedean misuse, see
2026-06-01-paper-modulus-nonarchimedean-audit). The observe-per-block
Σ_λ y_λ|χ^λ| version (deuteron +3.6% vs scalar +12%; |·| is the archimedean
per-block realization, bar-pairing χ^λ(q)·χ^λ(q⁻¹) is the general form) and
the per-bond GROWTH
(bonds embedded in the A-nucleon braid, the ⁴He residual) both need the Rust
per-partition χ kernel (CI) — this level isolates the bond-TYPE effect, which is
the T-vs-³He discriminator.
"""
from __future__ import annotations

from math import comb
from pathlib import Path

import _path_bridge  # noqa: F401, E402 — Phase-6 bridge
from mpmath import mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV  # noqa: E402 — CAL-1
import binding_canonical as bc  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
M_E = mpf(str(M_E_MEV))
q0 = mpf(str(Q0))
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, q0)   # 𝔈₀ ≈ 4.186 MeV (calibration-fixed)

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": mpf("7.7180"), "4He": AME_B_HE4_MEV_VALIDATION}
BOND_ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2)}


def bond_binding(Z, N):
    """E_0·(tr_M_free − tr_M_atom) for the 2-nucleon (Z,N) sub-braid.

    SIGNED categorical trace difference; the double-modulus form
    |tr_free|−|tr_atom| was a non-archimedean misuse (see
    docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md). Both
    traces are positive at q_0 → value-preserving and sign-correct.
    """
    r = bc.binding_canonical(Z, N)
    # `tr_M_*` are stored as STRINGS; a complex trace would serialize as
    # "(re+imj)" which mpf() cannot parse. Parse via complex() and take
    # the real part (archimedean projection, Im(q_0)=0) for robustness.
    # NB: Gemini's literal `r["tr_M_free"].real` is wrong here — the value
    # is a str, which has no `.real`; complex(str).real is the fix.
    tr_f = mpf(str(complex(r["tr_M_free"]).real))
    tr_a = mpf(str(complex(r["tr_M_atom"]).real))
    return E0 * (tr_f - tr_a)


def main() -> int:
    B = {xy: bond_binding(*zn) for xy, zn in BOND_ZN.items()}
    print(f"E_0 = {float(E0):.4f} MeV (calibration)\n")
    print("Derived per-bond-type binding (E_0·Δtr_M, scalar, 0 fit):")
    for xy in ("pp", "pn", "nn"):
        print(f"    B_{xy} = {float(B[xy]):.4f} MeV   ({BOND_ZN[xy]})")
    # Operators DERIVED, not hardcoded. This line read `<` between all three
    # bonds, which was true when it was written (2.379 < 2.491 < 2.532) and is
    # false now (0.642 > 0.616 > 0.564) — the ordering inverted while the
    # literal stayed put, so the producer printed a false statement one line
    # below the numbers that refute it. Comparing mpf, not the display floats.
    _o1 = "<" if B["pp"] < B["pn"] else (">" if B["pp"] > B["pn"] else "=")
    _o2 = "<" if B["pn"] < B["nn"] else (">" if B["pn"] > B["nn"] else "=")
    print(f"  ordering: B_pp={float(B['pp']):.4f} {_o1} B_pn={float(B['pn']):.4f} "
          f"{_o2} B_nn={float(B['nn']):.4f}\n")

    print(f"{'iso':<5}{'(pp,pn,nn)':<14}{'B_pred':<10}{'AME':<10}{'err%':<9}")
    results = {}
    for name, (Z, N) in ZN.items():
        npp, npn, nnn = comb(Z, 2), Z * N, comb(N, 2)
        Bk = npp * B["pp"] + npn * B["pn"] + nnn * B["nn"]
        err = (Bk - AME_B[name]) / AME_B[name]
        results[name] = {"n_pp": npp, "n_pn": npn, "n_nn": nnn,
                         "B_pred_MeV": float(Bk), "AME_MeV": float(AME_B[name]),
                         "err": float(err)}
        print(f"{name:<5}({npp},{npn},{nnn}){'':<{14-len(f'({npp},{npn},{nnn})')}}"
              f"{float(Bk):<10.4f}{float(AME_B[name]):<10.4f}{float(err)*100:<+9.1f}")

    # T vs ³He ordering check (the bond-type discriminator)
    t_gt_he3 = results["T"]["B_pred_MeV"] > results["3He"]["B_pred_MeV"]
    ame_t_gt = float(AME_B["T"]) > float(AME_B["3He"])
    print(f"\nT vs ³He ordering: pred B_T {'>' if t_gt_he3 else '≤'} B_³He ; "
          f"AME B_T {'>' if ame_t_gt else '≤'} B_³He — "
          f"{'MATCHES' if t_gt_he3 == ame_t_gt else 'MISMATCH'}")
    g = results["4He"]["B_pred_MeV"] / results["D"]["B_pred_MeV"]
    print(f"A-growth B(⁴He)/B(D) = {g:.2f}  (level-0 6.00; AME 12.72)")
    print("Residual = per-bond GROWTH (⁴He bonds embedded in 12-strand braid); "
          "needs embedded sub-braid χ (Rust kernel, CI).")

    wb = WitnessBuilder("derive-binding-bond-type", engine="mpmath")
    wb.set_description(
        "DERIVATION (0 fit, level-1): bond-TYPE per-bond binding sum "
        "B(K)=n_pp·B_pp+n_pn·B_pn+n_nn·B_nn, B_xy=E_0·Δtr_M of the 2-nucleon "
        "(Z,N) sub-braid (pure-Python canonical Markov trace; pn=deuteron). "
        "E_0=m_e/(q₀(q₀−1)) calibration. Isolates the bond-type T-vs-³He "
        "discriminator; per-block + per-bond-growth need the Rust χ kernel."
    )
    wb.add_parameter("E0_MeV", float(E0))
    wb.add_data("bond_type_binding_MeV",
                {xy: float(B[xy]) for xy in BOND_ZN})
    wb.add_data("per_atom", results)
    wb.add_data("t_he3_ordering_matches", bool(t_gt_he3 == ame_t_gt))
    wb.add_data("A_growth", float(g))
    wb.add_assertion(
        name="bond_type_reproduces_T_He3_ordering",
        computed=str(int(t_gt_he3 == ame_t_gt)),
        expected="1",
        tolerance=0,
        source=(f"bond-type sum gives B_T={results['T']['B_pred_MeV']:.3f} vs "
                f"B_³He={results['3He']['B_pred_MeV']:.3f}; AME 8.48 vs 7.72 — "
                f"ordering {'matches' if t_gt_he3==ame_t_gt else 'MISMATCH'} "
                "(the bond-type discriminator, 0 fit)."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
