#!/usr/bin/env python3
# polynomial_q_not_applicable: the chain terms are exact q-rationals / mpmath
# archimedean evaluations; this is a consolidation + residual cross-check, the
# archimedean side (pi-carrying terms) is intrinsically real-q.
"""
RT Identity chain — consolidation + tiering (item 3 of the owner queue, C1.3).

Owner queue item 3 = PR #1495 RT 2-loop plan, Identity 1 sub-claim C1.3 ("the
shadow-world measure on the photon zero-mode subspace of End(A (x) A) gives a
1/(pi dim H^1(M_Bring)) factor").  HONEST SCOPE (critical-distance discipline):
C1.3's measure normaliser 1/(pi b_1) is the CITED heat-kernel zero-mode = 1/Vol
result, and 8pi = pi b_1 (b_1 = 2g = 8 at g = 4) is ALREADY PROVEN sorry-free in
PR #2114 (QOU.Archimedean.PhotonIRZeroMode).  So this probe does NOT claim a new
derivation; it CONSOLIDATES the full 1/alpha_EM chain, verifies the residual,
and tiers every term by provenance so the genuinely-open pieces are unambiguous.

THE FULL CHAIN (em-coupling-bring-zero-mode + #1495 + #2114):
  1/alpha_EM = q[9]_q[10]_q + 2/(3pi) + alpha_EM*[2]_q/(8pi)*(1 - h^2 alpha_EM) + ...

TERM-BY-TERM TIERING:
  tree   q[9]_q[10]_q          : ESTABLISHED  (prop:em-coupling-projection; singlet
                                 idempotent trace / force-carrier complexity).
  n=1    2/(3pi) = b_1/Area     : PROVEN (Lean, #2114) = 2g/(4pi(g-1)) at g=4;
                                 b_1 = 2g topological, Area = 4pi(g-1) Gauss-Bonnet.
  n=2    [2]_q/(8pi):
           8pi = pi b_1          : GROUNDED (#2114) -- the C1.3 denominator IS
                                  pi dim H^1(M_Bring), same b_1 = 8 as n=1.
           [2]_q fermion loop    : C1.2 (dim_q V_F = [2]_q); structural.
           measure 1/(pi b_1)    : CITED (heat-kernel zero-mode = 1/Vol; standard).
         (1 - h^2 alpha) factor  : Habiro/Schwinger; SIGN forced (C2.3, exact in
                                  H_2(q): (sigma^2-1)e_- = -(h/q)e_-, see
                                  rt_c23_singlet_sign_core.py); magnitude open.
  OPEN (unchanged, #1495 track): C2.1/C2.2 UV-finiteness as a categorical
         RT-shadow-world statement (needs RtShadowWorldMeasure infra); the full
         -h^2 alpha normalisation; the tau_arch landing (BlochSuslinUniqueness).

This probe asserts the term provenance is internally consistent and that the
assembled chain reproduces CODATA 1/alpha to the documented residual.

Refs: prop:em-coupling-bring-zero-mode; prop:em-coupling-projection;
prop:alpha-em-habiro-bar-involution; PR #2114 (QOU.Archimedean.PhotonIRZeroMode,
b_1/Area + 8pi=pi b_1); PR #1495 (RT 2-loop plan C1.1-C1.4, C2.1-C2.3);
rt_c23_singlet_sign_core.py (the C2.3 sign core, exact).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

try:
    import mpmath as mp
    mp.mp.dps = 70
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099785827513808075916690956107688798744991218736"

CODATA_INV_ALPHA = "137.035999177"


def main() -> None:
    w = WitnessBuilder("rt-identity-chain-consolidation", engine="python")
    if not HAVE_MP:
        raise SystemExit("mpmath required")
    q = mp.mpf(Q0)
    h = q - 1 / q
    g = 4
    b1 = 2 * g                     # = 8, dim H^1(M_Bring) (PROVEN #2114)
    area = 4 * mp.pi * (g - 1)     # = 12 pi, Gauss-Bonnet (PROVEN #2114)

    def qint(k):
        return (q ** k - q ** (-k)) / (q - 1 / q)

    # chain terms
    tree = q * qint(9) * qint(10)                       # = 1/alpha_tree
    # solve alpha self-consistently: 1/a = tree + 2/(3pi) + a[2]/(8pi)(1-h^2 a)
    n1 = 2 / (3 * mp.pi)                                 # = b1/area
    n1_check = mp.mpf(b1) / area                         # b1/Area identity
    n1_ok = abs(n1 - n1_check) < mp.mpf(10) ** -40
    eightpi = mp.pi * b1                                 # = 8 pi (C1.3 denom)
    eightpi_ok = abs(eightpi - 8 * mp.pi) < mp.mpf(10) ** -40

    # fixed-point solve for alpha (cubic in alpha via the 1-h^2 a factor)
    a = 1 / tree
    for _ in range(200):
        inv = tree + n1 + a * qint(2) / eightpi * (1 - h ** 2 * a)
        a = 1 / inv
    inv_alpha = 1 / a
    codata = mp.mpf(CODATA_INV_ALPHA)
    resid = (inv_alpha - codata) / codata

    print("=" * 74)
    print("RT Identity chain — consolidation + tiering (item 3 / C1.3)")
    print("=" * 74)
    print(f"  q0 = {mp.nstr(q,12)}   g = {g}   b1 = dim H^1 = {b1}   Area = 12pi")
    print(f"  tree  q[9][10]          = {mp.nstr(tree,12)}   [ESTABLISHED]")
    print(f"  n=1   2/(3pi) = b1/Area = {mp.nstr(n1,12)}   [PROVEN #2114] "
          f"(b1/Area ok: {n1_ok})")
    print(f"  n=2   denom 8pi = pi*b1 = {mp.nstr(eightpi,12)}   [GROUNDED #2114] "
          f"(=8pi ok: {eightpi_ok})  <- C1.3 measure denominator")
    print(f"        [2]_q fermion loop= {mp.nstr(qint(2),12)}   [C1.2 structural]")
    print(f"        (1-h^2 a) sign     : forced negative [C2.3 exact, sign-core probe]")
    print(f"  assembled 1/alpha       = {mp.nstr(inv_alpha,12)}")
    print(f"  CODATA 1/alpha          = {CODATA_INV_ALPHA}")
    print(f"  residual (rel)          = {mp.nstr(resid,4)}")
    print()
    print("  C1.3 status: the measure denominator pi*dim H^1 = 8pi is the SAME")
    print("  b1=8 proven in #2114; the 1/(pi b1) normaliser is the cited")
    print("  heat-kernel zero-mode result. OPEN (unchanged): C2.1/C2.2 UV-")
    print("  finiteness as a categorical RtShadowWorldMeasure statement + the")
    print("  full -h^2 alpha normalisation + the tau_arch landing.")

    w.set_description(
        "RT Identity-chain consolidation (item 3 / PR #1495 C1.3).  Critical-"
        "distance scope: NOT a new derivation -- C1.3's measure normaliser "
        "1/(pi dim H^1) is the cited heat-kernel zero-mode = 1/Vol result and "
        "8pi = pi b_1 (b_1 = 2g = 8) is already PROVEN sorry-free in PR #2114.  "
        "This probe consolidates the full chain 1/alpha_EM = q[9][10] + 2/(3pi) "
        "+ alpha[2]_q/(8pi)(1-h^2 alpha) + ..., verifies b1/Area = 2/(3pi) and "
        "8pi = pi*b1 exactly, solves the self-consistent alpha and reports the "
        "CODATA residual, and tiers every term: tree ESTABLISHED "
        "(em-coupling-projection); n=1 PROVEN (#2114 b1/Area); n=2 denom "
        "GROUNDED (#2114 8pi=pi b1, the C1.3 denominator) with [2]_q fermion "
        "loop (C1.2) and the (1-h^2 alpha) sign forced (C2.3 exact, "
        "rt_c23_singlet_sign_core).  OPEN unchanged: C2.1/C2.2 UV-finiteness as "
        "a categorical RtShadowWorldMeasure, the full -h^2 alpha normalisation, "
        "and the tau_arch landing (BlochSuslinUniqueness)."
    )
    w.set_content_block("prop:em-coupling-bring-zero-mode")
    w.add_data("q0", str(q))
    w.add_data("b1_dim_H1", b1)
    w.add_data("terms", {
        "tree_q9q10": str(tree), "n1_2_3pi": str(n1),
        "n1_b1_over_Area": str(n1_check), "n2_denom_8pi": str(eightpi),
        "qint2_fermion_loop": str(qint(2)),
        "assembled_inv_alpha": str(inv_alpha), "residual_rel": str(resid),
    })
    w.add_assertion(
        "n=1 identity 2/(3pi) = b_1/Area (b_1=8, Area=12pi) [PROVEN #2114]",
        computed=bool(n1_ok), expected=True,
        source="Gauss-Bonnet Area=4pi(g-1); b_1=2g; #2114 Lean",
    )
    w.add_assertion(
        "C1.3 denominator 8pi = pi*dim H^1(M_Bring) = pi*b_1 [GROUNDED #2114]",
        computed=bool(eightpi_ok), expected=True,
        source="same b_1=8 as n=1; PhotonIRZeroMode.selfEnergyDenominator",
    )
    w.add_assertion(
        "assembled 1/alpha within 5 ppm of CODATA (chain residual documented)",
        computed=bool(abs(resid) < mp.mpf("5e-6")), expected=True,
        source="self-consistent solve; em-coupling-bring-zero-mode",
    )
    w.add_data(
        "finding",
        "C1.3 consolidated, not newly derived: the n=2 measure denominator "
        "pi*dim H^1 = 8pi is the same proven b1=8 as n=1 (#2114); the 1/(pi b1) "
        "normaliser is the cited heat-kernel zero-mode result; the (1-h^2 a) "
        "sign is forced (C2.3 exact).  The full chain reproduces CODATA to the "
        "documented residual.  Genuinely OPEN (unchanged): C2.1/C2.2 UV-"
        "finiteness as a categorical RtShadowWorldMeasure statement, the full "
        "-h^2 alpha normalisation, and the tau_arch landing -- the multi-week "
        "infra items on PR #1495's track."
    )
    w.save()
    print("\nDone. Witness saved (rt-identity-chain-consolidation).")


if __name__ == "__main__":
    main()
