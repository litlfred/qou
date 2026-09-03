#!/usr/bin/env python3
"""qbeta_cap_is_jointly_determined_probe.py — neither channel determines the
two-row cap alone; the TWO TOGETHER determine it exactly.

BEAN `qou-cds1`. The cross-channel route, and it does NOT work the way it was
posed to me ("the mass channel does force the cap, does it transfer?").

CORRECTING THE PREMISE FIRST. The mass channel does NOT force the cap. What is
proved is `markovWeights_eq_jones_of_threeRow_eq_zero`: TL-factorization
(`hTL : y_(1^3) = 0`) PLUS faithfulness forces `z = z_D`. The cap is a
HYPOTHESIS there, and the file says so under its own heading "What this does NOT
establish":

    "Nothing here shows that the *mass* fibre functor lands in Rep(SU_q(2)) = TL
     rather than in the full H_3(q). That is the categorical input the forcing
     argument consumes, and it is exactly the point on which the corpus is
     currently inconsistent"

and `docs/audits/2026-08-08-borromean-trace-convention-forcing.md` agrees: "The
step 'TL => D' is now proved ... The step 'the mass fibre functor lands in TL'
is NOT established, and is contradicted." So there is nothing to transfer.

BUT THE QUESTION REFRAMES INTO ONE WITH AN ANSWER.

Step 12 proved the DECAY channel cannot determine `y_(1^3)`: its pairing depends
on the weights only through `y_(3) - y_(1^3)`, so a one-parameter normalised
family gives the same Q_beta. Ask the same of the two channels jointly.

The Borromean characters, computed here from the corpus's own H_3 machinery on
the word `(sigma_0 sigma_1^-1)^3`:

    chi^(3)  (beta_Bor) = 1
    chi^(2,1)(beta_Bor) = -(q^4-q^2+1)(q^8-2q^6-2q^2+1)/q^6
    chi^(1^3)(beta_Bor) = 1

The two 1-dimensional characters are BOTH 1. So the mass channel sees
`y_(3) + y_(1^3)` (plus the two-row term) where the decay channel sees
`y_(3) - y_(1^3)`. SUM AND DIFFERENCE — which is exactly why they are
independent.

THE RESULT. With normalisation as the third row,

    det [ decay ; mass ; normalisation ]
      = -2 (q-1)^4 (q+1)^4 (q^2-q+1) (q^2+q+1) / q^6

nonzero for every q not in {0, 1, -1}. So the three functionals are INDEPENDENT
and the system determines `(y_3, y_21, y_111)` UNIQUELY — including the weight
the cap is about.

CONSEQUENCE. The cap is not undeterminable in principle. It is undeterminable by
either channel ALONE and determined by the two TOGETHER, so `y_(1^3)` is an
OBSERVABLE — a function of the measured Q_beta and the measured Borromean mass
pairing. One can therefore ASK whether the data says `y_(1^3) = 0` instead of
ruling it.

WHAT THIS PROBE DOES NOT DO. It does not plug in the numbers. Doing so honestly
needs a mass pairing extracted from measured m_p WITHOUT already assuming a
trace convention, and the corpus's own m_p route runs through `F_Bor`, which is
computed FROM a convention. Sorting that out is a separate piece of work and
doing it carelessly would be circular. The determinacy is structural and stands
on its own; the empirical solve is flagged, not performed.

SCOPE. Scope-(a) structural. Nothing wired, no convention selected, no c_k
proposed. `z = 1` is not readmitted.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp
from mpmath import mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, BASIS_NAMES, N, LEFT, basis_vec, reg_char, length, q, h,
)
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 60


def main() -> int:
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    I6 = sp.eye(N)
    S0, S1 = LEFT[1], LEFT[2]
    S1inv = sp.simplify(S1 - h * I6)
    check("sigma_1 * sigma_1^-1 = 1 (the inverse is built, not assumed)",
          sp.simplify(S1 * S1inv - I6) == sp.zeros(N, N))

    M = I6
    for _ in range(3):
        M = sp.simplify(S0 * S1inv * M)          # (sigma_0 sigma_1^-1)^3
    vB = sp.simplify(M * basis_vec(0))
    print("\n[1] beta_Bor = (sigma_0 sigma_1^-1)^3, NF vector")
    for i in range(N):
        print(f"    {BASIS_NAMES[i]:<8} {sp.factor(sp.simplify(vB[i]))}")

    c3B = sp.factor(sp.simplify(chi3(vB)))
    c21B = sp.factor(sp.simplify(chi21(vB)))
    c111B = sp.factor(sp.simplify(chi111(vB)))
    print(f"\n[2] Borromean block characters")
    print(f"    chi^(3)   = {c3B}")
    print(f"    chi^(2,1) = {c21B}")
    print(f"    chi^(1^3) = {c111B}")
    check("chi^(3)(beta_Bor) = 1", sp.simplify(c3B - 1) == 0)
    check("chi^(1^3)(beta_Bor) = 1", sp.simplify(c111B - 1) == 0)
    check("so the MASS channel sees y_3 + y_(1^3) where DECAY sees y_3 - y_(1^3)",
          sp.simplify(c3B - c111B) == 0)

    Mx = sp.Matrix([[1, 0, -1], [c3B, c21B, c111B], [1, 2, 1]])
    det = sp.factor(sp.simplify(Mx.det()))
    print(f"\n[3] det[decay ; mass ; normalisation] = {det}")
    check("the three functionals are INDEPENDENT (det != 0 identically)",
          sp.simplify(det) != 0)
    # and it vanishes only at q in {0, 1, -1}
    roots = sp.solve(sp.numer(sp.together(det)), q)
    check("det vanishes only at q in {0, 1, -1} (not on the substrate window)",
          all(sp.simplify(r) in (0, 1, -1) or not r.is_real for r in roots),
          f"roots = {roots}")

    # the explicit solve
    D_obs, M_obs = sp.symbols("D_obs M_obs")
    y3, y21, y111 = sp.symbols("y3 y21 y111")
    sol = sp.solve([sp.Eq(y3 - y111, D_obs),
                    sp.Eq(y3 + c21B * y21 + y111, M_obs),
                    sp.Eq(y3 + 2 * y21 + y111, 1)], [y3, y21, y111], dict=True)[0]
    print(f"\n[4] the weights as functions of the two observables")
    for k, nm in ((y3, "y_(3)"), (y21, "y_(2,1)"), (y111, "y_(1^3)")):
        print(f"    {nm:<9} = {sp.factor(sp.simplify(sol[k]))}")
    check("the solve is unique (3 equations, 3 unknowns, nonzero det)",
          len(sol) == 3)

    q0 = q_at(55)
    verdict = (
        "CROSS-CHANNEL DETERMINACY. The premise as posed is wrong: the mass "
        "channel does NOT force the cap -- markovWeights_eq_jones_of_threeRow_eq_zero "
        "takes y_(1^3) = 0 as a HYPOTHESIS, so nothing transfers THROUGH THAT "
        "LEMMA. (Its file's 'What this does NOT establish' note said the premise "
        "was unestablished; that note is STALE and is corrected on this branch -- "
        "the cap IS derived, from the 2-dim mass fibre, in "
        "FibreDimensionForcesTL.lean, sorry-free. That correction does not touch "
        "the determinacy result below, which is independent of HOW the cap is "
        "established.) BUT: chi^(3)(beta_Bor) = chi^(1^3)(beta_Bor) = 1, so the mass "
        "channel sees y_3 + y_(1^3) where the decay channel sees y_3 - y_(1^3). Sum "
        "and difference. With normalisation the determinant is "
        "-2(q-1)^4(q+1)^4(q^2-q+1)(q^2+q+1)/q^6, nonzero off {0,1,-1}, so the THREE "
        "TOGETHER determine all three weights UNIQUELY -- including y_(1^3). The cap "
        "is undeterminable by either channel alone (Step 12 for decay) and "
        "DETERMINED by the pair. So the cap is ALSO an observable -- measurable "
        "from the two pairings, not only derivable from the fibre dimension -- "
        "which makes it a falsifiable cross-check on the derived z_D rather than "
        "a second route that must be taken on trust. NOT DONE HERE: plugging in "
        "numbers, which needs a mass pairing from measured m_p that does not itself "
        "presuppose a convention -- the corpus's m_p route goes through F_Bor, which "
        "does. That circularity is a separate piece of work.")
    print(f"\n[5] {verdict}")

    wb = WitnessBuilder("qbeta-cap-is-jointly-determined", engine="sympy+mpmath")
    wb.set_description(
        "Neither channel determines the two-row cap alone; the decay and mass "
        "pairings plus normalisation are three INDEPENDENT functionals on the H_3 "
        "block weights, so together they determine y_(1^3) uniquely. Corrects the "
        "premise that the mass channel forces the cap (it takes it as a hypothesis). "
        "Structural only -- no numbers plugged in, no convention selected.")
    wb.add_data("beta_Bor_word", "(sigma_0 sigma_1^-1)^3")
    wb.add_data("beta_Bor_nf_vector",
                {BASIS_NAMES[i]: str(sp.factor(sp.simplify(vB[i]))) for i in range(N)})
    wb.add_data("borromean_characters",
                {"chi_3": str(c3B), "chi_21": str(c21B), "chi_111": str(c111B)})
    wb.add_data("determinant", str(det))
    wb.add_data("weights_from_observables",
                {str(k): str(sp.factor(sp.simplify(v))) for k, v in sol.items()})
    wb.add_data("premise_corrected",
                "the mass channel does NOT force the cap; TL-factorization is a "
                "HYPOTHESIS of markovWeights_eq_jones_of_threeRow_eq_zero. That "
                "file's 'What this does NOT establish' note claimed the categorical "
                "premise was unestablished; the note is STALE and is corrected on "
                "this branch -- FibreDimensionForcesTL.lean derives the cap from the "
                "2-dim mass fibre, sorry-free. What stands is that the cap does not "
                "transfer through THAT lemma, which is all the determinacy result "
                "below needs.")
    wb.add_data("not_done_here",
                "the empirical solve -- it needs a mass pairing from measured m_p "
                "that does not presuppose a convention; the corpus's F_Bor route does")
    wb.add_data("free_parameters", 0)
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) structural determinacy; nothing wired, no convention selected")
    wb.add_data("q0Anchor", "proton")
    wb.add_data("q0Value", mp.nstr(q0, 50))
    for c in checks:
        wb.add_assertion(c["name"],
                         computed=mp.mpf(1) if c["passed"] else mp.mpf(0),
                         expected=mp.mpf(1), tolerance=mp.mpf("0.5"), unit="bool")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
