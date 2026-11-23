#!/usr/bin/env python3
"""Chain walk, step 11: the cheat sheet's HADRONIC `E_0` inverts the very
quantity step 11 then derives.

CONTEXT.  The canonical-derivation cheat sheet's step table gives two forms
for the energy scale at step 9:

    step  9.  E_0 = m_e/(q_0(q_0-1)) = m_e c_q^2 hbar_q   (lept)
              E_0 = Q_beta / |h(h-2)/2|                    (had)

and step 11 as

    step 11.  Q_beta = |Delta(net(T_w))| . E_0 ,
              free neutron:  Delta(net) = h(h-2)/2 ~ -0.1872071945

Substituting the hadronic form into step 11 gives

    Q_beta = |h(h-2)/2| . ( Q_beta / |h(h-2)/2| ) = Q_beta

**identically.**  Read literally, step 11 derives its own input.  This is
AGENTS.md §"Derive-then-check" item 8 verbatim: if it is true by unfolding,
it is notation, not a derivation.

THE CIRCULARITY IS CONVENTION-INDEPENDENT, which is what makes it worth
recording.  Whichever functional `Delta(net)` turns out to be -- the
retired `z = 1` cell, the augmentation at `z = q`, or the RULED Markov
trace at `z_D = q^3/(q^2+1)` (owner ruling 2026-09-08) -- defining
`E_0 := Q_beta/|Delta|` and then computing `Q_beta := |Delta| . E_0` is an
identity.  Nothing about the fork in bean `qou-99qc` changes that.

WHAT PRODUCTION ACTUALLY DOES, and it is not this.  The live producers carry
a CLOSED SUBSTRATE expression with no `Q_beta` in it:

    E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR_Q**2)     # tower-summed, as ruled

(`qbeta_asymmetry_sign_is_a_bar_branch_probe.py:99`,
`qbeta_bar_branch_refuted_probe.py:88`, and `qbeta_e0.canonical()`).  So the
defect is in the primary coordination document, not in the compute -- the
same class as C10b in this walk, but worse: C10b made the chain look more
fitted than it is, while this one makes a derivation step vacuous.

WHAT THE HADRONIC FORM ACTUALLY IS.  Measured below: it is the LEPTONIC form
divided by 1.0016776 -- i.e. it is nothing but the famous "0.17 % vs CODATA"
agreement written backwards.  And that 0.17 % is the `z = 1` cell which
AGENTS.md has RETIRED as the base (owner ruling 2026-09-08).  So the line
carries no content the corpus still stands behind, and reads as a second,
independent definition of `E_0` when it is not one.

NO-FLOAT64: mpmath `mp.dps = 60` throughout; `float` appears nowhere.

Run:  python3 computations/audits/step11_qbeta_e0_circularity_probe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "computations"))
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

from mpmath import mp  # noqa: E402

mp.dps = 60

from qou_substrate.constants import (  # noqa: E402
    M_E_MEV,
    Q_50_DIGIT_STR,
    Q_NEUTRON_MEV,
)

FAILURES: list[str] = []
CHECKS = 0

# CODATA free-neutron beta-decay Q value -- the CAL-2 numerical proxy -- read
# from the corpus constant rather than hardcoded.  A first version of this
# probe carried the literal `0.7823334` copied out of AGENTS.md prose; the live
# table has `0.7823334093099085`, 1.2e-8 relative away, which moves the fourth
# significant figure of every percentage below.
QB_CODATA = mp.mpf(str(Q_NEUTRON_MEV))


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


# `Q` is a float64; `mpf(str(Q))` would launder 17 digits into a 60-dps
# computation and the f64-into-mpmath gate correctly flags it.  `Q_50_DIGIT_STR`
# is the exact decimal the corpus publishes for the proton pin.
q = mp.mpf(Q_50_DIGIT_STR)
m_e = mp.mpf(str(M_E_MEV))
hbar_q = 1 - 1 / q
h = q - 1 / q
dnet = h * (h - 2) / 2                       # the cheat sheet's free-neutron Delta(net)

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0_lept = _qbeta_e0.order_zero_scaled(m_e, q)                # step 9, leptonic
E0_tower = E0_lept / (1 - hbar_q**2)         # production, tower-summed (ruled 2026-09-05)
E0_had = QB_CODATA / abs(dnet)               # step 9, hadronic -- Q_beta inverted


def section1() -> None:
    print("\n=== 1. the three E_0, at the proton pin ===\n")
    print(f"    q0             = {mp.nstr(q, 20)}   (proton pin, the standing default)")
    print(f"    h = q - 1/q    = {mp.nstr(h, 20)}")
    print(f"    h(h-2)/2       = {mp.nstr(dnet, 20)}")
    print()
    print(f"    E0 leptonic    = {mp.nstr(E0_lept, 20)} MeV   m_e/(q(q-1))")
    print(f"    E0 tower-summed= {mp.nstr(E0_tower, 20)} MeV   <- PRODUCTION")
    print(f"    E0 hadronic    = {mp.nstr(E0_had, 20)} MeV   <- cheat sheet, = Q_beta/|dnet|")
    print()

    check(
        abs(dnet + mp.mpf("0.1872071945")) < mp.mpf("1e-9"),
        "h(h-2)/2 reproduces the cheat sheet's -0.1872071945",
        f"computed {mp.nstr(dnet, 20)}",
    )


def section2() -> None:
    print("\n=== 2. the circularity, exactly ===\n")

    qb_from_had = abs(dnet) * E0_had
    residual = qb_from_had - QB_CODATA
    check(
        residual == 0,
        "Q_beta from the HADRONIC E_0 returns CODATA, bit for bit at this dps",
        f"|dnet| . E0_had - Q_beta_CODATA = {mp.nstr(residual, 10)}\n"
        "The MATHEMATICAL content is that it is the same number -- E0_had was\n"
        "obtained by dividing that number by |dnet| -- so step 11 recovers its\n"
        "own input and there is no derivation here to be right or wrong.  The\n"
        "bit-exactness is a bonus of this particular division round-tripping at\n"
        "mp.dps = 60 and is NOT the evidence; the algebra below is.",
    )

    # And it is convention-independent: ANY nonzero Delta gives the same identity.
    #
    # Demonstrated over EXACT RATIONALS, not in mpmath.  A first version of this
    # asserted bit-equality at mp.dps = 60 for an arbitrary Delta and FAILED on
    # pi/10 -- correctly, because `|d| * (Q/|d|) == Q` bit-for-bit is a claim
    # about the ARITHMETIC, not about the mathematics, and it happens to hold
    # for `dnet` only because that particular division round-trips.  The
    # identity being demonstrated is algebraic, so demonstrate it algebraically;
    # asserting it in floating point would be the error AGENTS.md names as
    # reporting an arithmetic floor as though it were exactness.
    from fractions import Fraction

    qb_exact = Fraction(str(Q_NEUTRON_MEV))
    for name, delta in (
        ("the retired z = 1 cell (dnet as an exact rational)",
         Fraction("-0.18720719452937830985")),
        ("an arbitrary positive Delta", Fraction(31415926535, 100000000000)),
        ("a negative Delta", Fraction(-2718281828, 1000000000)),
        ("a Delta far from any physical scale", Fraction(1, 10**9)),
    ):
        e0 = qb_exact / abs(delta)
        check(
            abs(delta) * e0 == qb_exact,
            f"identity holds exactly over Q for {name}",
        )
    print("         => the circularity does not depend on which functional Delta is.")
    print("            The qou-99qc fork (z = 1 / z = q / z_D) cannot repair it.\n")


def section3() -> None:
    print("\n=== 3. what the hadronic form actually IS ===\n")

    ratio = E0_lept / E0_had
    check(
        abs(ratio - 1) < mp.mpf("0.002"),
        "E0_hadronic is E0_leptonic divided by 1.0016776",
        f"E0_lept / E0_had = {mp.nstr(ratio, 12)}\n"
        f"i.e. a relative gap of {mp.nstr((ratio - 1) * 100, 6)} %",
    )
    check(
        abs((ratio - 1) * 100 - mp.mpf("0.1678")) < mp.mpf("0.002"),
        "and that gap IS the famous \"0.17 % vs CODATA\" for Q_beta",
        "so the hadronic line is that agreement written backwards.  It is not a\n"
        "second, independent determination of E_0 -- it is the first one, with\n"
        "the residual divided out.  AGENTS.md RETIRES that cell as the base\n"
        "(owner ruling 2026-09-08: eps is the Markov trace at z_D), so the line\n"
        "carries no content the corpus still stands behind.",
    )


def section4() -> None:
    print("\n=== 4. production does not do this ===\n")

    hits = []
    for p in sorted((REPO / "computations" / "qbeta").glob("*.py")):
        try:
            txt = p.read_text(encoding="utf-8")
        except Exception:                                  # pragma: no cover
            continue
        if "M_E/(Q0*(Q0 - 1))/(1 - HBAR_Q**2)" in txt:
            hits.append(p.relative_to(REPO))
    check(
        len(hits) >= 2,
        "live producers carry a CLOSED SUBSTRATE E_0 with no Q_beta in it",
        "E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR_Q**2)   # tower-summed, as ruled\n"
        + "\n".join(f"  {h}" for h in hits),
    )

    qb_tower = abs(dnet) * E0_tower
    rel = (qb_tower - QB_CODATA) / QB_CODATA * 100
    print()
    print(f"    |dnet| . E0_tower = {mp.nstr(qb_tower, 20)} MeV")
    print(f"    CODATA            = {mp.nstr(QB_CODATA, 20)} MeV")
    print(f"    relative          = {mp.nstr(rel, 6)} %\n")
    check(
        abs(rel) > mp.mpf("1"),
        "with the production E_0 the step is a real claim with a real miss",
        f"{mp.nstr(rel, 6)} % -- a number that CAN be wrong, which the hadronic\n"
        "form's 0.00 % cannot.\n"
        "\n"
        "🛑 DO NOT QUOTE THAT PERCENTAGE AS THE FRAMEWORK'S Q_beta ACCURACY.\n"
        "It is a MIXED cell: the OLD functional Delta(net) = h(h-2)/2 against\n"
        "the NEW tower-summed E_0.  The RULED cell is eps = the Markov trace at\n"
        "z_D on the gamma-gamma-selected element, and AGENTS.md records it at\n"
        "-16.678 % -- itself scored on an element the confinement SDP rejects\n"
        "(owner ruling 2026-09-13).  Quote the witness, not this probe.",
    )


def main() -> int:
    print("step 11 Q_beta / E_0 circularity probe")
    print("=" * 72)
    section1()
    section2()
    section3()
    section4()
    print("\n" + "=" * 72)
    if FAILURES:
        print(f"FAILED {len(FAILURES)}/{CHECKS}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"all {CHECKS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
