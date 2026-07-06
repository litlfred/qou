#!/usr/bin/env python3
"""
Refutation test for H_scalar (the one open hypothesis from the Aufbau-ordering
arc): "an atomic orbital's energy is the SYMMETRIC-BLOCK (scalar, σ_i↦q) component
of its braid word, q^ℓ (a=+1, Madelung) — not the non-scalar V_ℓ action q^{2ℓ}."

The question H_scalar hides: WHAT IS "the orbital energy" in QOU, and is q^ℓ
canonically privileged?  This script shows it is NOT — the framework offers THREE
natural energy functionals giving THREE different ℓ-coefficients a∈{0,+1,+2}, and
H_scalar selects the a=+1 one **because it matches Madelung**, with no atomic
justification (the q^ℓ object is the MOLECULAR C_nv-projector construct; an
isolated atom has no C_nv).  Selecting the functional to match the answer is
fitting — which the three-calibration discipline (STRICT) forbids.

  (i)   σ_F  (confinement-SDP dual, bare T_ee)        a = 0   Coulomb degeneracy
  (ii)  symmetric-block scalar  q^ℓ   [H_scalar]      a = +1  Madelung
  (iii) tr_M / q-dimension      q^{2ℓ}                a = +2  ℓ-dominated

REP-THEORY (the decisive part): the atomic orbital with angular momentum ℓ is the
irreducible spin-ℓ rep V_ℓ.  Its TRIVIAL-block (symmetric, q^ℓ) multiplicity is
δ_{ℓ,0} — ZERO for ℓ≥1.  So q^ℓ is NOT a component of the atomic orbital; it only
arises from a braid WORD acting on the trivial rep (the C_nv-projected molecular
domain, `prop:symmetric-block-domain-weight`).  The rotation-INVARIANT scalar of
V_ℓ (the natural atomic "energy", a trace) is the q-dimension [2ℓ+1]_q ~ q^{2ℓ}
(a=+2).  Hence importing q^ℓ to the atom is unjustified.
"""
from __future__ import annotations
import sympy as sp

LET = "spdfghi"
NMAX = 6
ORB = [(n, l) for n in range(1, NMAX + 1) for l in range(n)]


def aufbau_ref():
    return sorted(ORB, key=lambda o: (o[0] + o[1], o[0]))


def order_by(key):
    return sorted(ORB, key=lambda o: (key(*o), o[0]))


def fmt(seq, k=12):
    return " ".join(f"{n}{LET[l]}" for n, l in seq[:k])


def cg_trivial_mult(a, b):
    """Multiplicity of the trivial rep V_0 in V_a ⊗ V_b (SU(2) Clebsch–Gordan:
    V_a⊗V_b = ⊕_{c=|a-b|}^{a+b} V_c; trivial appears iff a==b, once)."""
    return 1 if a == b else 0


def main() -> int:
    q = sp.symbols("q", positive=True)
    ref = aufbau_ref()

    print("  THREE NATURAL ORBITAL-ENERGY FUNCTIONALS → THREE ORDERINGS")
    funcs = [
        ("(i)   σ_F  SDP dual, bare T_ee      a=0   [Coulomb degeneracy]", lambda n, l: n),
        ("(ii)  symmetric-block q^ℓ  H_scalar  a=+1  [Madelung]", lambda n, l: n + l),
        ("(iii) tr_M / q-dim q^{2ℓ}            a=+2  [ℓ-dominated]", lambda n, l: n + 2 * l),
    ]
    for label, key in funcs:
        seq = order_by(key)
        div = next((i for i in range(len(seq)) if seq[i] != ref[i]), None)
        tag = "= Aufbau ✓" if div is None else f"diverges #{div} ({fmt([seq[div]],1)} vs {fmt([ref[div]],1)})"
        print(f"    {label}\n        {fmt(seq)}  → {tag}")
    print("    ⇒ a=+1 (Madelung) sits BETWEEN the framework's natural a=0 and a=+2.\n")

    print("  REP-THEORY — is q^ℓ a property of the ATOMIC orbital V_ℓ?")
    print("    trivial-block (q^ℓ, symmetric) multiplicity in V_ℓ  = δ_{ℓ,0}:")
    for l in range(4):
        print(f"      ℓ={l}: mult(V_0 ⊂ V_{l}) = {cg_trivial_mult(l, 0) if l==0 else 0}"
              + ("   (s — trivial)" if l == 0 else "   (ℓ≥1 — NO trivial component)"))
    print("    trivial-block multiplicity in the SELF-SQUARE V_ℓ⊗V_ℓ (the capacity):")
    for l in range(4):
        print(f"      ℓ={l}: mult(V_0 ⊂ V_{l}⊗V_{l}) = {cg_trivial_mult(l, l)}   "
              "(=1 — the 2n² self-square, NOT the energy)")
    print("    rotation-INVARIANT scalar of V_ℓ (natural atomic energy = a trace):")
    for l in range(4):
        m = 2 * l + 1
        qd = sp.simplify((q ** m - q ** (-m)) / (q - 1 / q))
        print(f"      ℓ={l}: q-dim [{m}]_q = {qd}  (~q^{{{2*l}}}, a=+2)")
    print()

    print("### Verdict — H_scalar REFUTED as a derivation (post-hoc functional choice)")
    print("  • q^ℓ is NOT a component of the atomic orbital V_ℓ (ℓ≥1): its trivial-")
    print("    block multiplicity is 0.  q^ℓ only arises as a braid WORD on the")
    print("    trivial rep — the MOLECULAR C_nv-projected domain (symmetric-block-")
    print("    domain-weight).  An isolated atom has full SO(3)_q symmetry; its")
    print("    trivial rep is ONLY ℓ=0, and there is NO C_nv projector to import.")
    print("  • The rotation-invariant ATOMIC scalar of V_ℓ is the q-dim TRACE")
    print("    [2ℓ+1]_q ~ q^{2ℓ} (a=+2), NOT q^ℓ.  Demanding an invariant energy")
    print("    gives the overshoot, not Madelung.")
    print("  • The framework brackets a=+1 between a=0 (σ_F) and a=+2 (tr_M) but")
    print("    never PRODUCES it.  H_scalar picks the a=+1 functional BECAUSE it")
    print("    matches Madelung — selecting the functional to fit the answer.")
    print("  • ⇒ H_scalar is a FIT-BY-FUNCTIONAL-CHOICE, not a derivation. The")
    print("    canonical QOU observable (tr_M / rotation-invariant) predicts a=+2.")
    print("    Per owner STRICT, Madelung stays an OPEN problem — and the honest")
    print("    framework-level statement is that QOU's canonical ordering is the")
    print("    ℓ-dominated overshoot, DISAGREEING with the empirical periodic table.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
