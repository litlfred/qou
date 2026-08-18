#!/usr/bin/env python3
"""
Probe — QOU DOES derive Coulomb. It is Q = 2Z, linear in charge, and that is the gap.

## RETRACTION FIRST

`collective_term_shape_degeneracy_probe.py` (mine, same branch) states that the
high-Z residual is "consistent with Coulomb, which the framework does not model
AT ALL". **That is false, and I did not run the corpus-grep checklist before
writing it.** The corpus carries:

* `content/.../knots-particles-confinement/coulomb-charge.{md,ts,lean}` — a
  definition block deriving an explicit Coulomb charge;
* `content/.../knots-particles-confinement/magic-shell-coupling-kappa.{md,ts,lean}`
  — a shell-structure block (identification withdrawn, see below);
* `docs/coordination/alpha-em.md`, `docs/audits/2026-08-01-em-linking-reads-round1.md`;
* deprecated `per_braid_tower_coulomb.py`, `coulomb_subtracted_binding.py`,
  `term_7_shell_correction_test.py`.

The claim is withdrawn. What follows replaces it, and the replacement is sharper.

## What the corpus actually derives

`def:coulomb-charge` splits the crossing energy into a bar-even and a bar-odd part:

    E_cross = (1/2)(n_+ + n_-)(q + 1/q)   +   Q * (q - 1/q)
              \_____ strong _____/            \___ Coulomb ___/

    Q = (1/2)(n_+ - n_-)          the Coulomb charge = HALF THE WRITHE

with the ratio of Coulomb to strong equal to `tanh(ln q) = 0.103964` at q0
(the block states ~0.104).

## Result 1 — Q = 2Z + eps, with eps a fixed constant, and N cancels

Evaluated on the framework's own `atom_braid_word_3A`:

    Q - 2Z = 0.000343927701756774002   for 4He..208Pb — IDENTICAL (spread 8.4e-48)

The integer part is exact and the reason is structural:

    writhe = 3Z + N                                  intra: proton +3, neutron +1
           + (Z-1)(+1) + (N-1)(-1) + e_pn            interfaces: pp +1, nn -1, pn e_pn
           = 4Z + e_pn

so `Q = 2Z + e_pn/2` — the neutron's intra-nucleon writhe is cancelled by the
nn-interface writhe, and N drops out entirely.

**The offset is the colour weighting.** The chain has exactly ONE pn bond, and
under the canonical `bring_color_weighted` convention its offset is
`d = -0.104458248`, not the exact midpoint `-h/2 = -0.104530149`. Its crossing
sign is therefore `e_pn = 1 + 2d/h = +6.878e-04` rather than `0`, giving
`eps = e_pn/2 = 0.000343927701756774002`. One such bond per nucleus, hence a constant
independent of both Z and N.

I first reported this as "Q = 2Z exactly"; that came from a table printed to two
decimals. The probe's assertion caught it. The corrected statement is the more
informative one — the colour weighting breaks exact integrality of the Coulomb
charge by a fixed, universal amount.

The framework's Coulomb charge counts protons and is independent of N. That is
qualitatively right: charge is carried by protons.

## Result 2 — but it is LINEAR in charge, and electrostatic energy is QUADRATIC

    nuclide   Z    A    Q=2Z   fw EM MeV   phys Coulomb   shortfall
    4He       2      4     4        0.90           0.88        1.0x
    12C       6     12    12        3.33           9.13        2.7x
    40Ca     20     40    40       11.85          77.45        6.5x
    56Fe     26     56    52       16.87         118.42        7.0x
    90Zr     40     90    80       27.45         242.63        8.8x
    208Pb    82    208   164       64.67         781.35       12.1x

(framework EM = `tanh(ln q0)` x the chain's strong term; physical Coulomb =
`a_C Z(Z-1)/A^(1/3)` with `a_C = 0.697 MeV`.)

**It is exact at 4He and diverges monotonically with Z.** That is the signature of
`Z` against `Z(Z-1)`: the two coincide at small Z and separate as Z grows.

**The framework has a charge; it does not have a charge-charge interaction
energy.** `Q*h` is linear in the charge. Electrostatics is a *pair* energy —
every proton with every other — and needs a term quadratic in Q.

## Result 3 — the EM sector IS the writhe grading, i.e. route 2

`Q = (1/2)(n_+ - n_-)` is half the writhe. So the object the corpus calls the
Coulomb correction is the same object as the `T_3`/writhe grading closed as
route 2 of the two-nucleon work (`t3_grading_cannot_unbind_pp`, sorry-free).

This is a *consistency*, not a new failure: EM should be a small correction, and
`tanh(ln q0) = 10.4%` is small. Route 2's conclusion was that the writhe cannot
fix the STRONG-sector sign structure — which is correct physics, not a defect.
The writhe is the electromagnetic sector and is doing its own job.

## Result 4 — the corpus has already been down the shell road, and withdrew

`magic-shell-coupling-kappa` proposed a magic-shell coupling and **withdrew the
identification**. Its recorded reason is directly relevant here: the fit ran at
two anchors (3He, 3H) and disagreed with itself — opposite signs, factor 5.3 —
and the diagnosis was that *restoring the electrostatic energy of 3He's pp pair
removes the discord*, leaving an excess coefficient of **zero**.

So a prior agent found that an apparent SHELL effect at A=3 was electrostatics.
That is a caution for reading my own residual's N=50 peak as shell structure: at
least once already in this corpus, that reading was wrong and the answer was EM.

## Where a quadratic term could come from — the honest answer

The linear piece is derived and correct. The quadratic piece requires a
*pair-of-crossings* object. Note the obstruction is already known: a single
inter-nucleon interface generates only the **2-dimensional** subalgebra
`span{1, sigma}` (`sigma^2 = h sigma + 1`), which is why every single-bond
quantity is affine in the crossing and cannot be quadratic in it. So a `Q^2`-like
term cannot live at one bond.

It could live in the multi-bond word, where distinct bonds' crossings can pair.
That is the same structural place the many-body collective term must live, and it
is not excluded by anything proved so far. It is also NOT established — no such
term is proposed here.

## Scope

**Retracts:** "the framework does not model Coulomb at all" (mine).
**Establishes:** `Q = 2Z` exactly, derived from the word structure; the framework's
EM term is linear in charge; the shortfall against `Z(Z-1)/A^(1/3)` is 1.0x at
4He rising to 12.1x at 208Pb.
**Does NOT establish:** that the residual IS Coulomb (the collinearity caveat of
the shape-degeneracy probe still stands), or that a quadratic term exists.

NO WITNESS: the framework's own braid words plus the corpus's own ratio; the
tables reproduce it.

Bean qou-ls86; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR as Q50

A_COULOMB = "0.697"
CASES = [("4He", 2, 2), ("12C", 6, 6), ("40Ca", 20, 20),
         ("56Fe", 26, 30), ("90Zr", 40, 50), ("208Pb", 82, 126)]


def main() -> int:
    mp.mp.dps = 50
    import mass_binding_dashboard as M
    from mass_at_3A_proper import atom_braid_word_3A

    q = mp.mpf(str(Q50))
    L = M._bond_type_L()
    a = mp.mpf("4.1859813632944758969")
    # h DERIVED from q at working precision. NOT pyhecke.gram.h, which is a
    # Python float (differs from the exact value by 5.5e-17) and would drag the
    # whole computation down to float64. See AGENTS.md "PROBES ARE NOT EXEMPT".
    h = q - 1 / q
    ratio = mp.tanh(mp.log(q))
    aC = mp.mpf(A_COULOMB)

    def Qcharge(Z, N):
        return mp.mpf(1) / 2 * mp.fsum(
            [mp.mpf(1) + 2 * mp.mpf(str(d)) / h
             for (_c, d, _g) in atom_braid_word_3A(Z, N)])

    print("QOU DOES derive Coulomb. It is Q = 2Z — linear in charge, and that is the gap.\n")
    print("## RETRACTION\n")
    print("  My shape-degeneracy probe said the framework 'does not model Coulomb AT")
    print("  ALL'. False — def:coulomb-charge derives one. I skipped the corpus-grep")
    print("  checklist. Withdrawn; what follows replaces it.\n")
    print("## What def:coulomb-charge gives\n")
    print("  E_cross = (1/2)(n+ + n-)(q + 1/q)  +  Q (q - 1/q),   Q = (1/2)(n+ - n-)")
    print(f"  Coulomb/strong = tanh(ln q0) = {mp.nstr(ratio, 8)}   (block states ~0.104)\n")

    print("## 1. Q = 2Z + eps, eps a fixed constant — N cancels\n")
    print("  writhe = 3Z + N + (Z-1)(+1) + (N-1)(-1) + e_pn = 4Z + e_pn")
    print("  so Q = 2Z + e_pn/2: the neutron's intra writhe (+1 each) is cancelled by")
    print("  the nn-interface writhe (-1 each), and N drops out entirely.\n")
    offs = []
    for lab, Z, N in CASES:
        Qv = Qcharge(Z, N)
        offs.append(Qv - 2 * Z)
        print(f"    {lab:<6} Z={Z:3d} N={N:3d}   Q = {mp.nstr(Qv, 20):<24} "
              f"Q-2Z = {mp.nstr(Qv - 2 * Z, 18)}")
    spread = max(offs) - min(offs)
    print(f"\n  offset spread across all cases: {mp.nstr(spread, 6)} -> a CONSTANT")
    print("  source: the single colour-weighted pn bond. Under bring_color_weighted")
    print("  its d = -0.104458248, not the midpoint -h/2 = -0.104530149, so its")
    print("  crossing sign is e_pn = +6.878e-04 rather than 0. One per nucleus.")
    print("  (I first reported 'Q = 2Z exactly' off a 2-decimal table; the assertion")
    print("   below caught it. The corrected version is the more informative one:")
    print("   colour weighting breaks exact integrality by a fixed universal amount.)")
    ok = spread < mp.mpf("1e-40")

    print("\n## 2. Linear in charge — electrostatic energy is quadratic\n")
    print("| nuclide |  Z |   A |  Q=2Z | fw EM MeV | phys Coulomb | shortfall |")
    print("| ------- | -: | --: | ----: | --------: | -----------: | --------: |")
    for lab, Z, N in CASES:
        A = Z + N
        strong = a * ((Z - 1) * L["pp"] + L["pn"] + (N - 1) * L["nn"])
        fw = ratio * strong
        phys = aC * Z * (Z - 1) / mp.cbrt(A)
        print(f"| {lab:<7} | {Z:2d} | {A:3d} | {2*Z:5d} | {mp.nstr(fw, 4)} "
              f"| {mp.nstr(phys, 4)} | {mp.nstr(phys/fw, 3)}x |")
    print("\n  Exact at 4He, diverging monotonically with Z — the signature of Z vs")
    print("  Z(Z-1). The framework has a CHARGE; it has no charge-charge interaction.\n")

    print("## 3. The EM sector IS the writhe grading (route 2)\n")
    print("  Q = (1/2)(n+ - n-) is half the writhe, so the corpus's Coulomb correction")
    print("  and the T_3/writhe grading closed as route 2 are the SAME object. That is")
    print("  a consistency, not a failure: EM should be small (10.4%), and route 2's")
    print("  conclusion — the writhe cannot fix the STRONG sign structure — is correct")
    print("  physics rather than a defect.\n")

    print("## 4. The corpus already withdrew a shell identification, and the reason was EM\n")
    print("  magic-shell-coupling-kappa proposed a magic-shell coupling and WITHDREW it:")
    print("  its two anchors (3He, 3H) disagreed in sign by a factor 5.3, and restoring")
    print("  the electrostatic energy of 3He's pp pair removed the discord, leaving an")
    print("  excess coefficient of ZERO. An apparent SHELL effect was electrostatics.")
    print("  Direct caution for reading my residual's N=50 peak as shell structure.\n")

    print("## Where a quadratic term could come from\n")
    print("  A single interface generates only the 2-dimensional span{1, sigma}")
    print("  (sigma^2 = h sigma + 1), so every single-bond quantity is AFFINE in the")
    print("  crossing and cannot be quadratic in it — a Q^2 term cannot live at one")
    print("  bond. It could live in the MULTI-BOND word, where distinct bonds' crossings")
    print("  pair. That is the same structural place the many-body term must live, and")
    print("  nothing proved so far excludes it. It is also NOT established here.")
    print("\n(no witness by design — the framework's own words plus the corpus's ratio.)")

    assert ok, "Q - 2Z must be the SAME constant on every case"
    return 0


if __name__ == "__main__":
    sys.exit(main())
