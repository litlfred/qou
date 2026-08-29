#!/usr/bin/env python3
"""What a quadratic-in-charge EM term says about the baryon octet: nothing new.

RETRACTION (2026-08-29).  This script was first written and committed under the
title "Coleman-Glashow from a quadratic-in-charge EM term: parameter-free, and
checked", claiming CG as a prediction of the ansatz and as the first
parameter-free EM consequence on this branch.  Both claims were wrong, and the
corpus already contained the refutation -- `QOU/Eightfold/ColemanGlashowIdentity`
proves CG sorry-free from a WEAKER premise, and
`eightfold-way/u-spin-coleman-glashow.md` records the same -0.064 MeV residual
this script "measured", together with the verdict "Reproducing Coleman-Glashow
would therefore be no evidence for this framework, or for any other."  My
corpus-grep had matched the topic and not the object.  The script is kept, with
its arithmetic intact and its conclusion reversed.

Bean `qou-bn8e`.  Companion to
`QOU/MassTheory/ChargeQuadraticSumRule.lean`, which proves the algebra
sorry-free.  This script does the two things Lean does not: it enumerates the
octet's charge configurations from the quark contents, and it checks the
resulting sum rule against measured masses.

THE STRUCTURE.  Symmetric quadratics in three charges span a 2-dim space, basis
{sum q_i^2 (self), sum_{i<j} q_i q_j (interaction)}; total charge is not
independent since Q^2 = sum q_i^2 + 2 sum q_i q_j.  So the general quadratic EM
energy is  E = A*self + B*inter.  The corpus
(`QOU/MassTheory/NeutronProtonEMSign.lean`) uses `inter` alone -- the choice
A = 0, standard renormalisation, not derived and not flagged there.

TWO CONSEQUENCES.
  (1) The proton and neutron differ by 1/3 in BOTH invariants, so the nucleon
      splitting fixes only A + B.  A second splitting is needed to separate them,
      and the Sigma triplet supplies one.
  (2) Because s and d carry the SAME charge -1/3, the octet's seven baryons
      occupy only THREE distinct charge configurations.  Three configurations,
      two couplings => exactly one relation, holding for every A and B.  It is
      Coleman-Glashow.

(3) THE REASON (2) IS NOT A PREDICTION.  The map (A, B) -> (the two independent
    octet splittings) has determinant -1/3, hence is a BIJECTION: for any octet
    EM pattern whatsoever some (A, B) reproduces it (Lean:
    `octet_em_pattern_surjective`, exhibiting A = 2u+v, B = u-v).  A class that
    reaches every pattern excludes none, so CG could not have failed here and is
    no evidence for the ansatz.  The same bijection says the octet FITS A and B
    rather than constraining them -- which is why `qou-bn8e` stays open.

Exact rationals for the algebra; mpmath for the mass comparison.  No float64.
Emits no witness.
"""
from fractions import Fraction as F

from mpmath import mp

mp.dps = 30

Q_U, Q_D, Q_S = F(2, 3), F(-1, 3), F(-1, 3)      # s and d share charge

OCTET = {                                          # name -> quark charges
    "p":     (Q_U, Q_U, Q_D),
    "n":     (Q_U, Q_D, Q_D),
    "Sig+":  (Q_U, Q_U, Q_S),
    "Sig0":  (Q_U, Q_D, Q_S),
    "Sig-":  (Q_D, Q_D, Q_S),
    "Xi0":   (Q_U, Q_S, Q_S),
    "Xi-":   (Q_D, Q_S, Q_S),
}

# PDG 2024 central values, MeV, with quoted uncertainties.
MASS = {"p": ("938.27208943", "0.00000029"), "n": ("939.56542194", "0.00000048"),
        "Sig+": ("1189.37", "0.07"), "Sig-": ("1197.449", "0.030"),
        "Xi0": ("1314.86", "0.20"), "Xi-": ("1321.71", "0.07")}


def invariants(charges):
    a, b, c = charges
    return (a * a + b * b + c * c, a * b + a * c + b * c)


def main() -> int:
    print(f"{'baryon':8s} {'Q':>6s} {'sum q^2':>9s} {'sum qq':>9s}")
    configs = {}
    for name, ch in OCTET.items():
        s2, pij = invariants(ch)
        configs.setdefault((s2, pij), []).append(name)
        print(f"{name:8s} {str(sum(ch)):>6s} {str(s2):>9s} {str(pij):>9s}")

    print(f"\ndistinct charge configurations: {len(configs)}")
    for (s2, pij), names in configs.items():
        print(f"   ({s2}, {pij})  <-  {', '.join(names)}")
    ok = len(configs) == 3
    if not ok:
        print("   FAIL: expected 3")

    # (1) the nucleon degeneracy
    sp_, ip_ = invariants(OCTET["p"])
    sn_, in_ = invariants(OCTET["n"])
    print(f"\nnucleon gaps:  d(sum q^2) = {sp_ - sn_}   d(sum qq) = {ip_ - in_}")
    if sp_ - sn_ != ip_ - in_:
        print("   FAIL: expected equal gaps (the degeneracy)"); ok = False
    else:
        print("   equal => E(p) - E(n) = (A + B)/3; the nucleon fixes only the SUM")

    # (2) Sigma separates them
    ss_, is_ = invariants(OCTET["Sig+"])
    sm_, im_ = invariants(OCTET["Sig-"])
    det = (sp_ - sn_) * (is_ - im_) - (ip_ - in_) * (ss_ - sm_)
    print(f"Sigma gaps:    d(sum q^2) = {ss_ - sm_}   d(sum qq) = {is_ - im_}")
    print(f"   determinant against the nucleon row = {det}"
          f"  => {'separates A from B' if det != 0 else 'FAILS to separate'}")
    if det == 0:
        ok = False

    # (3) Coleman-Glashow, symbolically in A and B, then measured
    def E(name, A, B):
        s2, pij = invariants(OCTET[name])
        return A * s2 + B * pij

    for A, B in ((F(1), F(0)), (F(0), F(1)), (F(3), F(-7)), (F(-2), F(5))):
        cg = (E("n", A, B) - E("p", A, B)) - (E("Sig-", A, B) - E("Sig+", A, B)) \
             + (E("Xi-", A, B) - E("Xi0", A, B))
        if cg != 0:
            print(f"\n   FAIL: Coleman-Glashow != 0 at (A,B)=({A},{B}): {cg}")
            ok = False
    print("\nColeman-Glashow vanishes identically in (A, B)  [4 sample pairs]")

    m = {k: mp.mpf(v[0]) for k, v in MASS.items()}
    e = {k: mp.mpf(v[1]) for k, v in MASS.items()}
    cg = (m["n"] - m["p"]) - (m["Sig-"] - m["Sig+"]) + (m["Xi-"] - m["Xi0"])
    err = mp.sqrt(sum(e[k] ** 2 for k in ("p", "n", "Sig+", "Sig-", "Xi0", "Xi-")))
    largest = max(abs(m["n"] - m["p"]), abs(m["Sig-"] - m["Sig+"]),
                  abs(m["Xi-"] - m["Xi0"]))
    print(f"\nmeasured residual = {mp.nstr(cg, 6)} MeV")
    print(f"  combined PDG error (quadrature) = {mp.nstr(err, 4)} MeV")
    print(f"  as % of the largest term ({mp.nstr(largest, 6)} MeV) = "
          f"{mp.nstr(100 * abs(cg) / largest, 4)}%")
    print(f"  |residual| / error = {mp.nstr(abs(cg) / err, 4)}")
    if abs(cg) > 3 * err:
        print("  NOTE: residual exceeds 3 sigma of the quoted errors; the relation")
        print("  is standardly quoted as approximate, and higher-order EM and")
        print("  isospin-breaking terms are expected at this level.")

    # (4) SATURATION: the ansatz reaches EVERY octet EM pattern, so it excludes
    #     none.  Exhibit A = 2u+v, B = u-v for arbitrary target splittings.
    print("\nSATURATION CHECK -- does the ansatz forbid any octet pattern?")
    sat_ok = True
    for (u, v) in [(F(1), F(0)), (F(0), F(1)), (F(-7, 5), F(3, 11)), (F(22, 7), F(-9, 4))]:
        A, B = 2 * u + v, u - v
        def _E(cfg):
            sf, it = invariants(cfg)
            return A * sf + B * it
        a, b, c = _E(OCTET["p"]), _E(OCTET["n"]), _E(OCTET["Sig-"])
        if (a - b, b - c) != (u, v):
            sat_ok = False
            print(f"   FAIL: target ({u}, {v}) not reproduced by (A,B)=({A},{B})")
    if sat_ok:
        print("   every target (u, v) is reproduced  =>  the ansatz excludes NOTHING")
        print("   determinant of (A,B) -> (a-b, b-c) is -1/3, a bijection")
    ok = ok and sat_ok

    print("\nWHAT THIS DOES NOT DO: it derives neither A nor B, so the magnitude")
    print("target in `qou-bn8e` is untouched.")
    print("\nAND WHAT IT DOES NOT SHOW (retracted 2026-08-29): Coleman-Glashow")
    print("holding here is NOT evidence for the quadratic-in-charge ansatz. By the")
    print("saturation check above the ansatz reproduces every octet EM pattern, so")
    print("CG could not have failed; a test nothing can fail discriminates nothing.")
    print("CG is already proved sorry-free in QOU/Eightfold/ColemanGlashowIdentity")
    print("from a WEAKER premise, and u-spin-coleman-glashow.md already records")
    print("this same -0.064 MeV residual and this same verdict.")
    print("\nVERDICT:", "arithmetic checks out; adds no octet prediction" if ok
          else "CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
