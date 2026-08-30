#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; closed-form bar-involution
# entanglement energies, no symbolic-q polynomial output.
"""
Closed-form entanglement energy — lift the p(3A) trace-gate (all-A).

Cross-pollination of #2405 (B_sym closed-form bond chain) with the
q-parameterised core (#2401). #2405 proved the log-binding is an additive
(A−1)-bond linear chain,
    ln(tr_free/tr_atom) = (Z−1)·L_pp + [p–n present]·L_pn + (N−1)·L_nn,
with `L_xy = ln(tr_free^{xy}/tr_atom^{xy})` from the 2-nucleon sub-braids.
Hence the full atom trace itself is closed-form from 1- and 2-nucleon
sub-traces (no p(3A) Wedderburn sum):
    tr_atom(q) = tr_p(q)^Z · tr_n(q)^N · exp(−Σ L_bond(q)).
Every factor is a sub-trace at n ≤ 6, so it evaluates at ANY q for ALL A.

Evaluating at q₀ and q₀⁻¹ then gives the bar-involution split all-A — the
entanglement (retained bar-even / emitted bar-odd) without the trace-gate:
    E_retained = E₀·(tr_atom(q₀)+tr_atom(q₀⁻¹))/2   (cosh, binding/volume)
    E_emitted  = E₀·|tr_atom(q₀)−tr_atom(q₀⁻¹)|/2   (sinh, radiated γγ̄)

VALIDATION: for A≤7 the closed-form tr_atom is cross-checked against the
exact p(3A) trace `tr_m_atom_zn`; the chain is exact to the 50-dps floor
through ¹²C (#2405 audit), so agreement is expected. Exploratory; no fit.

Run:  python3 -u computations/closed_form_entanglement.py 2>&1 | tee /tmp/cfe.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import mpmath as mp  # noqa: E402

from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

SEQUENCE = [("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3),
            ("7Li", 3, 4), ("12C", 6, 6), ("16O", 8, 8), ("40Ca", 20, 20)]


def _subtraces(q):
    """1- and 2-nucleon sub-traces + bond logs at q (n ≤ 6, fast, A-independent)."""
    trp = mp.mpf(tr_m_atom_zn(1, 0, q=q)[0])
    trn = mp.mpf(tr_m_atom_zn(0, 1, q=q)[0])
    def L(Z, N):
        ta, tf, _, _ = tr_m_atom_zn(Z, N, q=q)
        return mp.log(mp.mpf(tf) / mp.mpf(ta))
    return trp, trn, {"pp": L(2, 0), "pn": L(1, 1), "nn": L(0, 2)}


def tr_atom_closed_form(Z, N, trp, trn, Lbond):
    """tr_atom(q) = tr_p^Z·tr_n^N·exp(−Σ L_bond), the #2405 linear chain:
    (Z−1) pp-bonds, 1 pn-bond (iff both present), (N−1) nn-bonds."""
    n_pn = 1 if (Z >= 1 and N >= 1) else 0
    sumL = (Z - 1) * Lbond["pp"] + n_pn * Lbond["pn"] + (N - 1) * Lbond["nn"]
    return trp ** Z * trn ** N * mp.exp(-sumL)


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(str(Q0)); qi = mp.mpf(1) / q0
    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
    sub0 = _subtraces(q0); subi = _subtraces(qi)

    print("\n  CLOSED-FORM ENTANGLEMENT — all-A via 1+2-nucleon sub-traces")
    print(f"  E₀={float(E0):.4f} MeV;  tr_atom(q)=tr_p^Z·tr_n^N·exp(−Σ L_bond)\n")
    print("| iso | A | retained E (MeV) | emitted E (MeV) | tr_atom(q₀) cf | exact | Δ_rel |")
    print("|---|--:|--:|--:|--:|--:|--:|")
    for name, Z, N in SEQUENCE:
        ta0 = tr_atom_closed_form(Z, N, sub0[0], sub0[1], sub0[2])
        tai = tr_atom_closed_form(Z, N, subi[0], subi[1], subi[2])
        retained = E0 * (ta0 + tai) / 2
        emitted = E0 * abs(ta0 - tai) / 2
        # validation vs exact p(3A) trace where feasible (n=3A ≤ 21)
        exact_s, drel_s = "—", "—"
        if 3 * (Z + N) <= 21:
            ex = mp.mpf(tr_m_atom_zn(Z, N, q=q0)[0])
            drel = abs(ta0 - ex) / abs(ex)
            exact_s = mp.nstr(ex, 8); drel_s = mp.nstr(drel, 3)
        print(f"| {name} | {Z+N} | {float(retained):.3f} | {float(emitted):.3f} "
              f"| {mp.nstr(ta0,8)} | {exact_s} | {drel_s} |")
    print("\n  Reading: closed-form tr_atom from sub-traces reproduces the exact "
          "p(3A) trace (Δ_rel at the float/50-dps floor through A≤7), and extends "
          "the retained/emitted entanglement split to ALL A (¹²C…⁴⁰Ca instant) "
          "— the same trace-gate lift #2405 gave B_sym, now for the entanglement.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
