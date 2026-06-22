#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; signed entanglement binding
# variants, no symbolic-q polynomial output.
"""
Signed entanglement binding variants — add vs subtract the radiated channel.

The dashboard's `B_sym+ent = B_sym + E_emit` ADDS the inter-nucleon emitted
energy. But radiated energy LEAVES the bound state — physically it should be
a mass DEFECT, i.e. SUBTRACTED. This probe compares, all-A via the
closed-form bond chain (#2405 + closed_form_entanglement):
    B_sym          = α·Σ L_bond            (the log-trace binding)
    B_sym + E_emit (the dashboard "augmented", radiated energy added)
    B_sym − E_emit (radiated energy as a mass defect, removed)
against AME, to see which sign — if either — tracks the binding better.

E_emit here is the bar-odd (sinh / radiated) channel of the atom trace,
E_emit = E₀·|tr_atom(q₀) − tr_atom(q₀⁻¹)|/2, with tr_atom the closed-form
sub-trace product (no p(3A) wall). Exploratory; no fit.

Run:  python3 -u computations/entanglement_binding_variants.py 2>&1 | tee /tmp/ebv.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import mpmath as mp  # noqa: E402

from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, M_E_MEV  # noqa: E402

# AME2020 total binding (MeV)
B_AME = {"D": float(AME_B_DEUTERON_MEV_VALIDATION), "3He": float(AME_B_HE3_MEV_VALIDATION), "4He": float(AME_B_HE4_MEV_VALIDATION),
         "6Li": 31.994564, "7Li": 39.245389, "12C": 92.161728,
         "16O": 127.619296, "40Ca": 342.052}
SEQ = [("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3),
       ("7Li", 3, 4), ("12C", 6, 6), ("16O", 8, 8), ("40Ca", 20, 20)]


def _sub(q):
    trp = mp.mpf(tr_m_atom_zn(1, 0, q=q)[0])
    trn = mp.mpf(tr_m_atom_zn(0, 1, q=q)[0])
    def L(Z, N):
        ta, tf, _, _ = tr_m_atom_zn(Z, N, q=q)
        return mp.log(mp.mpf(tf) / mp.mpf(ta))
    return trp, trn, {"pp": L(2, 0), "pn": L(1, 1), "nn": L(0, 2)}


def _chain_sumL(Z, N, Lb):
    return (Z - 1) * Lb["pp"] + (1 if Z >= 1 and N >= 1 else 0) * Lb["pn"] + (N - 1) * Lb["nn"]


def _tr_atom(Z, N, trp, trn, Lb):
    return trp ** Z * trn ** N * mp.exp(-_chain_sumL(Z, N, Lb))


def main() -> int:
    mp.mp.dps = 40
    q0 = mp.mpf(str(Q0)); qi = mp.mpf(1) / q0
    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
    s0, si = _sub(q0), _sub(qi)

    print("\n  SIGNED ENTANGLEMENT BINDING VARIANTS (add vs subtract the radiated channel)")
    print(f"  E₀={float(E0):.4f} MeV;  err = B_AME/B (1.00 perfect, >1 under-binds)\n")
    print("| iso | A | B_AME | B_sym | err | B_sym+emit | err+ | B_sym−emit | err− |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|")
    for name, Z, N in SEQ:
        bsym = float(E0 * _chain_sumL(Z, N, s0[2]))
        ta0 = _tr_atom(Z, N, *s0); tai = _tr_atom(Z, N, *si)
        emit = float(E0 * abs(ta0 - tai) / 2)
        b_add, b_sub = bsym + emit, bsym - emit
        ba = B_AME[name]
        e, ep, em = ba / bsym, ba / b_add, (ba / b_sub if b_sub > 0 else float('inf'))
        print(f"| {name} | {Z+N} | {ba:.2f} | {bsym:.2f} | {e:.2f} "
              f"| {b_add:.2f} | {ep:.2f} | {b_sub:.2f} | {em:.2f} |")
    print("\n  Reading: B_sym under-binds increasingly with A (err grows). The "
          "emitted (radiated) channel is sub-MeV beyond the light isotopes, so "
          "neither +emit nor −emit materially changes the heavy-A under-binding "
          "— the dominant gap is the cooperative/Δ_λ shell term, not the "
          "radiated-energy sign. (+emit helps light over-binders slightly; "
          "−emit worsens them. The radiated channel is a small correction, not "
          "the gap.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
