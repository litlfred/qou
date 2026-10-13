#!/usr/bin/env python3
"""The Wigner coefficient's menu is a singleton — and the number stays caveated.

`qou-w06d` capped the Wigner mechanism at `k = 4`. This probe asks whether
`(2,2)` alone suffices, and the answer is that the corpus's IMPLEMENTED Wigner
term already uses `(2,2)` alone:

    Delta_W = -m_e . H_q((2,2)) . min(Z,N)/A     (derived-mass-formula-light-isotopes.md)

so nothing needs fixing there. What carries `(3,1,1)` is the `T(T+1)/A` form in
`unified-iterative-correction-proof.md`, and that half is now known to price
nothing. Bean `qou-ld2a`; instantiates `QOU/Hecke/IsospinClassSingleton.lean`.

*** THE FIT-SHAPE OBJECTION, WHICH IS THE CORPUS'S OWN ***

The QA note on `mass-formula-regime-switching-table1-data` says of this whole
family of coefficients:

    "seven coefficients each written as a short product of q-integers drawn from
     a large menu, agreeing with known LDM values at the 1-6 % level, IS THE
     SHAPE A FIT TAKES; nothing in the table or its parent derives which product
     goes with which coefficient"

That is the right objection and it is not answered by a good number.

*** WHY IT DOES NOT BITE ON THE WIGNER ROW: THE MENU HAS ONE ITEM ***

`mass-coefficient-shadow-price-proof.md` classifies the scaling function by the
content sum: `c > 0` volume-type, `c = 0` **isospin-type** `T(T+1)/A^p`,
`c < 0` charge-type. The Wigner energy is T=0 isoscalar pn pairing — a QUARTET
correlation, so `n = 4`. At that level:

    (4)          c =  6    volume
    (3,1)        c =  2    volume
    (2,2)        c =  0    ISOSPIN   <- the only one, out of five
    (2,1,1)      c = -2    charge
    (1,1,1,1)    c = -6    charge

Say "isospin-type" and "quartet" and the partition is FORCED. No freedom is left
to fit. That is one row of seven; the objection stands for the other six and
nothing here touches them.

*** AND THE ROW CAP EMPTIES THE CLASS ABOVE n = 4 ***

`c = 0 AND ell <= 2` is a singleton at n = 1, 3, 4 and EMPTY at every n >= 5 —
the isospin-type contributions the row cap allows are exactly three, and only
`(2,2)` sits at the quartet level.

*** THE NUMBER, WITH ITS CAVEAT ATTACHED ***

`m_e . H_q((2,2)) = m_e [3]_q [2]_q^2 = 6.289300 MeV` against an empirically
extracted `Delta_W ~ 6.3 MeV` (Satula-Nazarewicz 1997, Phys. Lett. B 407 103).
0.17 %. **Reported, not offered as evidence** — already recorded in
`pn-bond-cannot-be-extremal.md`, and a 0.17 % agreement drawn from a menu proves
nothing on its own. What the singleton adds is that this one was not drawn from
a menu.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 40
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
M_E = mp.mpf("0.51099895069")
DELTA_W_EMPIRICAL = mp.mpf("6.3")   # EXTERNAL: Satula-Nazarewicz 1997
NMAX = 14


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield []
        return
    for f in range(min(n, mx), 0, -1):
        for rest in partitions(n - f, f):
            yield [f] + rest


def conj(lam):
    return [sum(1 for x in lam if x > j) for j in range(lam[0])] if lam else []


def content_sum(lam):
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def hooks(lam):
    """Hook lengths of every cell."""
    c = conj(lam)
    return [lam[i] - j + c[j] - i - 1
            for i, row in enumerate(lam) for j in range(row)]


def qint(n):
    n = mp.mpf(n)
    return (Q0**n - Q0**(-n))/(Q0 - 1/Q0)


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 78)
    print("1. THE FIVE PARTITIONS OF 4 AND THEIR SCALING CLASSES")
    print("=" * 78)
    p4 = list(partitions(4))
    print(f"    {'lambda':>14}{'c':>5}{'ell':>5}   class")
    rows = []
    for p in p4:
        c = content_sum(p)
        cls = "volume" if c > 0 else ("ISOSPIN" if c == 0 else "charge")
        rows.append({"lambda": tuple(p), "c": c, "ell": len(p), "class": cls})
        print(f"    {str(tuple(p)):>14}{c:>5}{len(p):>5}   {cls}")
    ok &= chk("p_of_four_is_five", len(p4), 5,
              note="the completeness the Lean file deliberately does NOT prove "
                   "-- `decide` there runs over an explicit list, and this is "
                   "what says the list is all of them")
    ok &= chk("the_isospin_class_at_level_four_is_a_singleton",
              [r["lambda"] for r in rows if r["c"] == 0], [(2, 2)],
              note="say 'isospin-type' (the corpus's own c(lambda) = 0 rule) and "
                   "'quartet' (n = 4) and the partition is FORCED. The "
                   "fit-shape objection to this family does not bite on this "
                   "row, because the menu has one item. Lean: "
                   "isospin_class_of_four_is_singleton")

    print()
    print("=" * 78)
    print("2. THE ISOSPIN CLASS AT EVERY LEVEL, AND WHAT THE ROW CAP LEAVES")
    print("=" * 78)
    print(f"    {'n':>4}{'parts':>8}{'c=0':>6}{'c=0 & ell<=2':>14}   shapes with c=0")
    census = []
    for n in range(1, NMAX + 1):
        ps = list(partitions(n))
        z = [p for p in ps if content_sum(p) == 0]
        zc = [p for p in z if len(p) <= 2]
        census.append({"n": n, "partitions": len(ps), "c_zero": len(z),
                       "c_zero_two_row": len(zc),
                       "shapes": [tuple(p) for p in z]})
        print(f"    {n:>4}{len(ps):>8}{len(z):>6}{len(zc):>14}   "
              f"{[tuple(p) for p in z]}")
    ok &= chk("the_row_cap_empties_the_isospin_class_above_level_four",
              [c["c_zero_two_row"] for c in census if c["n"] >= 5],
              [0]*(NMAX - 4),
              note="c = 0 AND ell <= 2 is a singleton at n = 1, 3, 4 and empty "
                   "at every n >= 5. So the isospin-type contributions "
                   "convention D allows are exactly three, and only (2,2) sits "
                   "at the quartet level")
    ok &= chk("and_every_c_zero_shape_is_self_conjugate",
              all(p == conj(p) for c in census for p in
                  [list(t) for t in c["shapes"]]), True,
              note="measured to n = %d, not proved: c(lambda') = -c(lambda) "
                   "gives self-conjugate => c = 0; the converse is observed "
                   "here, not established" % NMAX)

    print()
    print("=" * 78)
    print("3. THE NUMBER — REPORTED WITH ITS CAVEAT, NOT AS EVIDENCE")
    print("=" * 78)
    h22 = hooks([2, 2])
    Hq = mp.mpf(1)
    for h in h22:
        Hq *= qint(h)
    val = M_E*Hq
    print(f"    hook lengths of (2,2)      = {sorted(h22, reverse=True)}")
    print(f"    H_q((2,2)) = [3][2][2][1]  = {mp.nstr(Hq, 16)}")
    print(f"                = [2]^2([2]^2-1) = {mp.nstr(qint(2)**2*(qint(2)**2 - 1), 16)}")
    print(f"    m_e . H_q((2,2))           = {mp.nstr(val, 16)} MeV")
    print(f"    empirical Delta_W          ~ {mp.nstr(DELTA_W_EMPIRICAL, 4)} MeV"
          f"   (Satula-Nazarewicz 1997)")
    print(f"    relative                   = "
          f"{mp.nstr((val - DELTA_W_EMPIRICAL)/DELTA_W_EMPIRICAL*100, 6)} %")
    ok &= chk("the_hook_product_closed_form_holds",
              abs(Hq - qint(2)**2*(qint(2)**2 - 1)) < mp.mpf(10)**(-30), True,
              note="H_q((2,2)) = [3]_q[2]_q^2 and [3]_q = [2]_q^2 - 1, so the "
                   "whole coefficient is a polynomial in the loop value alone")
    ok &= chk("the_value_matches_the_one_already_in_the_corpus",
              mp.nstr(val, 5), "6.2893",
              note="pn-bond-cannot-be-extremal.md records 6.2894; this is NOT a "
                   "new number and is NOT offered as evidence. The QA note on "
                   "mass-formula-regime-switching-table1-data calls this family "
                   "'the shape a fit takes' -- correctly. What section 1 adds "
                   "is that THIS row's menu is a singleton")

    print()
    print("=" * 78)
    print("4. SO: IS (2,2) ALONE ENOUGH?")
    print("=" * 78)
    print("  For the IMPLEMENTED Wigner term, the question does not arise --")
    print("  derived-mass-formula-light-isotopes.md already uses (2,2) alone:")
    print("      Delta_W = -m_e . H_q((2,2)) . min(Z,N)/A")
    print("  and the row cap leaves it untouched.")
    print()
    print("  What carries (3,1,1) is the T(T+1)/A form in")
    print("  unified-iterative-correction-proof.md, whose k = 5 half is now")
    print("  known to price nothing (qou-w06d). That block should be re-stated")
    print("  over k = 4 alone, or its k = 5 term dropped.")
    print()
    print("  The gain is not numerical. It is that 'isospin-type at the quartet")
    print("  level' forces (2,2) with no freedom left -- which is exactly the")
    print("  derivation the fit-shape objection asks for, on this one row.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-isospin-class-singleton",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS, "n_max": NMAX,
                       "m_e_MeV": str(M_E),
                       "delta_W_empirical_MeV": str(DELTA_W_EMPIRICAL),
                       "delta_W_provenance": "EXTERNAL, Satula-Nazarewicz 1997 "
                                             "Phys. Lett. B 407 103; reported "
                                             "with the corpus's own fit-shape "
                                             "caveat, NOT offered as evidence",
                       "lean": "QOU/Hecke/IsospinClassSingleton.lean"},
        "data": {"level_four": rows, "census": census,
                 "H_q_two_two": mp.nstr(Hq, 20),
                 "m_e_H_q_MeV": mp.nstr(val, 20)},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_isospin_class_singleton_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-isospin-class-singleton.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
