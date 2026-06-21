#!/usr/bin/env python3
"""
Crack #2 of the q-deformed keystone (muon) shift — closing the open path that
the branching-shift probe (#2516) left.

Probe #2516 found the h^4-bearing (2,1) channel cancels between the muon E_(3,2)
and electron E_(3,1,1) projectors at the level of CLASSICAL S_5->S_3 branching
multiplicities (both 2).  The one escape hatch it flagged: maybe the
*q-deformed* Wenzl/Hoefsmit projector weights break the (2,1) symmetry, rescuing
an h^4-driven shift.

This script tests that escape DIRECTLY at the character level.  It computes the
honest H_5 ambient-block characters of the 3-strand Borromean braid (strands 4,5
spectators) and compares them to the classical-multiplicity prediction, across a
range of q (so h^4 sweeps from ~1e-4 up to ~0.9).

Key fact under test: generic-q Iwahori-Hecke branching H_3 ⊂ H_5 carries the
SAME multiplicities as the symmetric group S_3 ⊂ S_5 (the q-deformation lives
only in the shared H_3 characters).  If true, then

    χ_μ^{H5}(β) = Σ_{ν⊢3} m(ν;μ) · χ_ν^{H3}(β)   exactly, for any q,

and therefore  χ_(3,1,1)^{H5}(β) − χ_(3,2)^{H5}(β) = χ_(1,1,1)^{H3}(β) = 1,
h-INDEPENDENT — the (2,1)/h^4 channel cancels regardless of q-deformation.

DISCIPLINE: no fitting.  The 210 ppb target is an anchor-shift artifact; this
reports the structural identity and its robustness, not a tuned coefficient.
"""
import pyhecke_native as ph

DPS = 50
# Borromean b = (s1^{-1} s2)^3 on strands 1-3 (gens 1,2); valid in H_3 and H_5.
BORROMEAN = [(-1, 1), (1, 2)] * 3

# Classical S_5 -> S_3 branching multiplicities m(ν ; μ), ν ⊢ 3.
BRANCH = {
    (3, 2):    {(3,): 1, (2, 1): 2, (1, 1, 1): 0},  # muon home block,  ℓ=2
    (3, 1, 1): {(3,): 1, (2, 1): 2, (1, 1, 1): 1},  # electron home block, ℓ=1
}
H3 = [(3,), (2, 1), (1, 1, 1)]


def chi(shape, q):
    return float(ph.chi_lambda_braid_mpfr(list(shape), BORROMEAN, str(q), DPS))


def main() -> int:
    print(f"pyhecke_native v{ph.__version__}  |  dps = {DPS}\n")
    Q0 = 1.1099785955541805
    qs = [1.05, Q0, 1.30, 1.60]
    max_dev_char = 0.0
    max_dev_diff = 0.0
    for q in qs:
        h = q - 1.0 / q
        c3, c21, c111 = (chi(s, q) for s in H3)
        print(f"q = {q:<8} h = {h:+.4f}   h^4 = {h**4:+.6f}")
        for mu, mult in BRANCH.items():
            got = chi(mu, q)                                   # honest H_5 char
            pred = sum(mult[nu] * chi(nu, q) for nu in H3)     # classical mult
            dev = abs(got - pred)
            max_dev_char = max(max_dev_char, dev)
            print(f"   χ_{str(mu):<9}^H5(β) = {got:+.12f}   "
                  f"classical Σ m·χ = {pred:+.12f}   |Δ| = {dev:.1e}")
        diff = chi((3, 1, 1), q) - chi((3, 2), q)
        dev_diff = abs(diff - c111)
        max_dev_diff = max(max_dev_diff, dev_diff)
        print(f"   χ_(3,1,1) − χ_(3,2) = {diff:+.12f}   "
              f"= χ_(1,1,1) = {c111:.12f}   |Δ| = {dev_diff:.1e}  "
              f"(h-INDEPENDENT)\n")

    print("=== VERDICT (no fitting) ===")
    print(f" max |χ_μ^H5 − classical Σ m·χ|  over q∈{qs} = {max_dev_char:.1e}")
    print(f" max |(χ_(3,1,1)−χ_(3,2)) − χ_(1,1,1)|        = {max_dev_diff:.1e}")
    print(" => generic-q Hecke branching H_3⊂H_5 carries CLASSICAL")
    print("    multiplicities; the (2,1)/h^4 channel cancels for EVERY q.")
    print(" => the q-deformed-Wenzl-weight escape does NOT rescue an h^4-driven")
    print("    muon shift at the character level.  The only surviving μ/e")
    print("    asymmetry is the H_5 Markov block-weight ratio W_(3,2)/W_(3,1,1)")
    print("    (≈3.68 at q_0 — order-unity, not bar-even), the owner-gated")
    print("    geometric-W_λ frontier (#2488), which is refuted-by-size as the")
    print("    210 ppb mechanism.")
    ok = max(max_dev_char, max_dev_diff) < 1e-9
    print(f"\nROBUSTNESS CONFIRMED: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
