#!/usr/bin/env python3
"""What object is the "bar-odd sinh partner"? Im(frak V) -- and the chain violates it.

BEAN `qou-cds1`. Settles a question left open by
`qbeta_bar_odd_sinh_partner_check_probe.py`, which measured that the computed
closed form Q_A = m_e|q^2-2q-1|(q+1)/(2q^3) is NEITHER bar-odd nor bar-even
(bar(Q_A)/Q_A = 1.6868), contradicting four corpus sites, and concluded that a
bar-parity constraint on the D-frame correction was "not available from the
chain as written".

THAT CONCLUSION WAS WRONG, and this probe corrects it. The constraint IS
available. The object carrying the parity is not the closed form -- it is the
COMPLEX VOLUME, and it lives in q-hyperbolic geometry.

WHERE THE DESCRIPTION COMES FROM. `three-calibration-discipline.md:18` cites
`mass-theory/substrate-cohomology-calibration-story.md`, whose line 11 says:

  "A crossing has two eigenvalues, q and -q^{-1}. Setting lambda = log q, these
   split as cosh(lambda) +- sinh(lambda). ... The binding observables sit on the
   cosh, bar-even side. The beta-decay observable Q_beta and its precision
   coefficients sit on the sinh, bar-odd side. ... That single element is the
   COMPLEX VOLUME frak-V. Its bar-even part is Re frak-V = E_bind. Its bar-odd
   part is Im frak-V = Q_beta, forming the QOU analogue of the Neumann-Zagier
   Vol + i CS."

and `conj:binding-qbeta-complex-volume` states it:

    frak-V(K) = E_0 * tr_M((Pi_free - 1) . M)  in  C
    E_bind(K) = Re frak-V(K),     Q_beta(K) = Im frak-V(K).

So the sinh/cosh split is the q = e^lambda split of the crossing eigenvalues,
and bar (q -> 1/q) IS lambda -> -lambda; sinh/cosh parity is exactly
bar-odd/bar-even. The "sinh partner" is Im(frak V), the Chern-Simons-analogue
part of the complex volume.

STATUS OF THE CLAIM. `conj:binding-qbeta-complex-volume` is a CONJECTURE,
class-axiomatised in Lean (ComplexVolumeMatch / SingleFrakVAssembly /
StageCSigma3Lift). Per AGENTS.md section "Conditional-proved != premise-
established", the bar-odd property of Q_beta is therefore CONDITIONAL on that
conjecture. The four sites that state it -- three-calibration-discipline.md:18,
epistemic-status-of-calibrations.md:3, three-calibration-discipline-proof.md:36,
AGENTS.md -- state it as established fact, without the conditional.

THE USABLE CONSTRAINT. If Q_beta = Im(frak V) is bar-odd, then writing the
prediction as Q_beta^pred(q) = Q_A(q) * F(q), the requirement is NOT that F be
bar-even. It is

    Q_A(q) * F(q)   must be BAR-ODD:    Q_beta(1/q) = -Q_beta(q).

MEASURED at the proton anchor:

    Q_A alone                 bar-ratio = +1.686826456
    Q_beta^C = Q_A * ladder   bar-ratio = +1.687595234        (bar-odd needs -1)

Two readings, both worth recording:

  * The chain violates the conjecture's parity requirement outright -- the ratio
    is +1.69, not -1.
  * The LADDER moves the ratio by only 0.05 % (1.68683 -> 1.68760). The
    violation is inherited wholesale from the closed form Q_A; the entire
    precision ladder does essentially nothing to restore bar-oddness.

So either Q_A is not Im(frak V) -- i.e. the closed form is a different object
from the one the parity claim is about -- or the conjecture's parity claim fails
for the computed object. The corpus does not currently distinguish these.

WHY THIS MATTERS FOR THE D RE-DERIVATION. It restores a constraint that the
previous probe had (wrongly) removed from the toolkit, and it is a strong one:
any candidate F must make Q_A*F bar-odd, and the current C-frame ladder misses
that by ~2.7 in the ratio. That is a far sharper filter than matching
1 - F(q0) = 1.6748e-3 at one point.

Scope-(a): measurement plus a citation trail. Nothing derived, nothing wired,
no search run, no value proposed.
"""
from __future__ import annotations

import sys

import mpmath as mp

mp.mp.dps = 40

ANCHORS = {
    "proton": mp.mpf("1.10997858275138080759166909561076887987449912187357873607281"),
    "muon": mp.mpf("1.10997859555418057528159407960950937799328227995868622546675"),
}


def _sub(q: mp.mpf):
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h**2 + 3) / (h**2 + 4))
    return h, hbar, b, b * hbar**2


def qa_over_me(q: mp.mpf) -> mp.mpf:
    return abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)


def qbeta_C_over_me(q: mp.mpf) -> mp.mpf:
    """The committed C-frame prediction: Q_A * cos(alpha - u/2) * (1 + c_2 u^2)."""
    h, hbar, b, u = _sub(q)
    z = mp.sqrt(q) / (q + 1)
    a = (z - 1) * h / 2
    return qa_over_me(q) * mp.cos(a - b * hbar**2 / 2) * (1 - u**2)


def main() -> int:
    ok = True
    for name, q in ANCHORS.items():
        print(f"=== anchor {name}")
        for nm, f in (("Q_A alone (closed form)", qa_over_me),
                      ("Q_beta^C = Q_A * ladder", qbeta_C_over_me)):
            v, vbar = f(q), f(1 / q)
            ratio = vbar / v
            print(f"  {nm:<26} bar-ratio = {mp.nstr(ratio, 12)}   "
                  f"(bar-ODD requires -1)")
            # the constraint is violated, and not marginally
            ok &= abs(ratio + 1) > mp.mpf("2")

        r_a = qa_over_me(1 / q) / qa_over_me(q)
        r_c = qbeta_C_over_me(1 / q) / qbeta_C_over_me(q)
        moved = abs(r_c - r_a) / abs(r_a)
        print(f"  ladder moves the bar-ratio by {mp.nstr(moved*100, 6)} %")
        # the ladder does essentially nothing to the parity
        ok &= moved < mp.mpf("0.01")
        print()

    print("SETTLED: the 'bar-odd sinh partner' is Im(frak V), the")
    print("  Chern-Simons-analogue part of the complex volume")
    print("  frak-V = E_0 tr_M((Pi_free - 1).M), per conj:binding-qbeta-complex-volume")
    print("  and substrate-cohomology-calibration-story.md:11. It is a CONJECTURE,")
    print("  class-axiomatised in Lean -- so the parity of Q_beta is CONDITIONAL,")
    print("  and the four sites asserting it omit the conditional.")
    print()
    print("CONSTRAINT (usable): Q_A(q)*F(q) must be BAR-ODD -- not F bar-even.")
    print("  The committed C-frame chain misses it by ~2.7 in the ratio, and the")
    print("  ladder moves the ratio by <0.1 %, so the violation comes from Q_A.")
    print()
    print("ASSERTIONS PASS" if ok else "ASSERTIONS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
