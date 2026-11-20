#!/usr/bin/env python3
"""space_index_separability_probe.py — a space index cannot break the pn
degeneracy if it enters as a FACTOR, because both channels are S-wave.

THE BEAN'S PREMISE.  `qou-vbyi` is titled *"derive the interface offset t from a
SPACE index (3S1-3D1 tensor channel) -- the only route past the proved
flavour-only degeneracy"*, and is recorded as one of only two surviving routes
for 2H.  Its warrant is `qou-kj4v`, which observes that in the Standard Model the
3S1/1S0 split is the tensor force, a spin-SPACE coupling, and that *"the Hecke
interface has one index (the strand) and no space index to carry it."*

THE CHECK, and it does not survive.  `qou-kj4v`'s own sentence supplies the
counter:

    "In S-wave Pauli LOCKS spin to isospin (SPACE SYMMETRIC => spin and isospin
     symmetry opposite): S=1 <=> T=0, S=0 <=> T=1."

**Both pn channels are S-wave.**  3S1 and 1S0 are both `S` in the term symbol
`2M+1 L_J`, i.e. `L = 0`.  A factor keyed on `L` therefore takes the SAME value
on both channels, and a common factor cannot separate what is already equal.

Proved, and axiom-free:
`QOU.QBeta.InterfaceScalar.separable_interface_degenerate` -- for an arbitrary
separable interface `fSpin(S) * fIso(T) * fSpace(L)`, with the Pauli lock as
hypothesis and one and the same `ell` on both sides, the two channels are equal
for EVERY `fSpace`.  So the result is not specific to `L`: it covers any space
index entering multiplicatively and keyed on anything constant across the two
channels.

WHAT THIS DOES AND DOES NOT CLOSE.

  * It closes **"add a space FACTOR"** as a route past the degeneracy.  Scope (b),
    structural, invariant cited: commutativity plus a common factor.
  * It does NOT close `qou-vbyi`.  The Standard Model's tensor force is a spin-
    space **COUPLING**, and a product of a spin function and a space function is
    exactly what a coupling is not.  A non-separable interface -- one whose value
    depends jointly on `(S, L)` and does not factor -- is untouched by this and
    remains the live shape.
  * It does NOT bear on 3S1-3D1 mixing itself, which is a genuine `L = 0` vs
    `L = 2` admixture WITHIN the deuteron.  A space index is the right home for
    that; it is simply not what separates the deuteron from the virtual state.

So the bean's redirect should read: the space index must enter as a COUPLING,
not as a factor -- which is a sharper construction target than the bean states,
and one that can be checked before anything is built.

NUMERICAL GROUNDING (proton pin, 50 dps, convention D):

    mu+ = (z + 1/q)/(q + 1/q) = 0.75270211325196540159
    mu- = (q - z)/(q + 1/q)   = 0.24729788674803459841
    mu+ + mu-                 = 1        exactly
    mu+ * mu-                 = 0.18614164195799085217   <- qou-kj4v's value

Run:  python3 -u computations/probes/space_index_separability_probe.py \
        2>&1 | tee /tmp/space_index_separability.log
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
for _p in (COMPUTATIONS, COMPUTATIONS / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

CORPUS_DEGENERATE_VALUE = "0.18614164195799085217"   # qou-kj4v
LEAN_DECLS = (
    "QOU.QBeta.InterfaceScalar.separable_interface_degenerate",
    "QOU.QBeta.InterfaceScalar.common_factor_preserves_degeneracy",
)


def main() -> int:
    q = Q_MP
    qi = mp.mpf(1) / q
    z = q ** 3 / (q ** 2 + 1)
    mu_p = (z + qi) / (q + qi)
    mu_m = (q - z) / (q + qi)

    print("=" * 80)
    print("a space index entering as a FACTOR cannot split the two pn channels")
    print("=" * 80)
    print(f"\n  q_0 (proton) = {mp.nstr(q, 40)}")
    print(f"  z (conv. D)  = {mp.nstr(z, 30)}")
    print(f"  mu+          = {mp.nstr(mu_p, 30)}")
    print(f"  mu-          = {mp.nstr(mu_m, 30)}")
    print(f"  mu+ + mu-    = {mp.nstr(mu_p + mu_m, 20)}   (convex decomposition of 1)")

    triplet = mu_p * mu_m      # (S=1, T=0)
    singlet = mu_m * mu_p      # (S=0, T=1)
    print(f"\n  mu(3S1) = mu+ * mu- = {mp.nstr(triplet, 30)}")
    print(f"  mu(1S0) = mu- * mu+ = {mp.nstr(singlet, 30)}")
    print(f"  difference          = {mp.nstr(abs(triplet - singlet), 8)}")

    # Both channels are S-wave, so ANY space factor is applied to both alike.
    print(f"\n  applying a space factor g(L=0) -- the same on both, since both are S-wave:")
    worst = mp.mpf(0)
    for g_str in ("1", "0.5", "2", "0.0001", "137", "3.14159265358979"):
        g = mp.mpf(g_str)
        d = abs(triplet * g - singlet * g)
        worst = max(worst, d)
        print(f"    g = {g_str:<18} |mu(3S1)g - mu(1S0)g| = {mp.nstr(d, 6)}")
    print(f"\n  worst split achieved over any space factor: {mp.nstr(worst, 8)}")

    corpus = mp.mpf(CORPUS_DEGENERATE_VALUE)
    print(f"\n  vs qou-kj4v's recorded degenerate value {CORPUS_DEGENERATE_VALUE}:"
          f"  {mp.nstr(abs(triplet - corpus), 8)}")

    w = WitnessBuilder("space-index-separability", engine="python")
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D")
    w.add_data("lean_declarations", list(LEAN_DECLS))
    w.add_data("mu_plus", mp.nstr(mu_p, 40))
    w.add_data("mu_minus", mp.nstr(mu_m, 40))
    w.add_data("mu_triplet_3S1", mp.nstr(triplet, 40))
    w.add_data("mu_singlet_1S0", mp.nstr(singlet, 40))
    w.add_data("both_channels_are_S_wave", True)
    w.add_data("L_of_3S1", 0)
    w.add_data("L_of_1S0", 0)

    w.add_assertion(
        "the two pn channels are exactly degenerate before any space index",
        computed=mp.nstr(abs(triplet - singlet), 30), expected="0", tolerance="0",
        source="mu+ * mu- vs mu- * mu+ -- commutativity, so equal identically",
    )
    w.add_assertion(
        "and no space FACTOR splits them, because both channels are S-wave",
        computed=mp.nstr(worst, 30), expected="0", tolerance="0",
        source="six values of g(L=0) applied to both channels alike; "
               "Lean separable_interface_degenerate covers every fSpace",
    )
    w.add_assertion(
        "the degenerate value reproduces qou-kj4v's recorded figure",
        computed=mp.nstr(abs(triplet - corpus), 30), expected="0",
        tolerance="1e-20",
        source=f"qou-kj4v records {CORPUS_DEGENERATE_VALUE}",
    )
    w.add_assertion(
        "mu+ + mu- = 1 -- the projector decomposition, so both channels bind",
        computed=mp.nstr(abs(mu_p + mu_m - 1), 30), expected="0", tolerance="1e-40",
        source="stated in qou-kj4v; unbinding needs mu > 1, outside the convex hull",
    )

    w.add_caveat(
        "Scope (b) for what it excludes -- a space index entering as a FACTOR -- "
        "with the invariant cited: commutativity plus a factor common to both "
        "channels. It does NOT close qou-vbyi. The Standard Model's tensor force "
        "is a spin-space COUPLING, and a product of a spin function and a space "
        "function is exactly what a coupling is not. A non-separable interface, "
        "depending jointly on (S, L), is untouched and remains the live shape."
    )
    w.add_caveat(
        "Nothing here bears on 3S1-3D1 mixing itself, which is a genuine L = 0 vs "
        "L = 2 admixture WITHIN the deuteron. A space index is the right home for "
        "that; it is simply not what separates the deuteron from the virtual state, "
        "since both of those are S-wave."
    )
    w.add_caveat(
        "The physics input -- that both pn channels are S-wave -- is quoted from "
        "qou-kj4v ('space symmetric'), not derived here. It is standard: 3S1 and "
        "1S0 are both S in the term symbol."
    )

    out = w.save()
    print(f"\n  witness -> {out}")
    failed = [a for a in w.assertions if not a.passed]
    print(f"  assertions: {len(w.assertions) - len(failed)}/{len(w.assertions)} pass")
    for a in failed:
        print(f"    FAIL  {a.name}: computed={a.computed} expected={a.expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
