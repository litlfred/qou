#!/usr/bin/env python3
"""q6pp_unique_n_is_reading_dependent_probe.py
==============================================

**Beans `qou-jgg0` (strand count) x `qou-q6pp` (p-n splitting sign). The
strand-count reading is not cosmetic for `qou-q6pp`: its central coincidence
holds under `n = A+Z`, INVERTS under `n = 3A`, and EVAPORATES under `n = 3A+Z`.**

WHY THIS EXISTS
----------------
`qou-jgg0` establishes that three strand counts are live for the atomic braid
(`A+Z`, `3A`, `3A+Z`) with no block saying which is canonical. That reads as a
naming problem. It is not only a naming problem, and this probe is the
counter-example.

`qou-q6pp` (status todo, unclaimed since 2026-08-25) offers, as the better of
two candidate explanations for a wrong-signed p-n splitting, this argument:

    the three-Phi formula is LEADING-ORDER, exact only while the three extremal
    blocks (sym, std, alt) exhaust the partitions of n; n = 3 is the UNIQUE n
    where they do; and D is the ONLY atom whose sign comes out right

The force of it is a coincidence: **the uniquely-exact `n` is occupied by the
uniquely-right-signed atom.** That is a real argument -- under one reading of
`n`. The bean computes `n = A+Z` throughout, because `thm:wedderburn-mass-formula`
says `H_{A+Z}(q)`.

WHAT THIS MEASURES
-------------------
Which atom sits at the uniquely-exact `n`, under each of the three live readings.
`p(3) = 3` is the only partition count equal to the extremal count, so the
question is which atom has `n = 3`:

    n = A + Z    ->  A=2, Z=1  ->  D      -- the right-signed atom. Coincidence HOLDS.
    n = 3A       ->  A=1       ->  H-1    -- which the bean itself records as
                                             over-specified and 5e5 off.
                                             Coincidence INVERTS: the uniquely-
                                             exact n lands on the WORST atom.
    n = 3A + Z   ->  needs Z=0 ->  none   -- no neutral atom (Z >= 1) reaches it.
                                             Coincidence EVAPORATES.

WHAT THIS DOES *NOT* CLAIM
---------------------------
- It does **not** resolve the p-n splitting sign. `qou-q6pp` stays open.
- It does **not** say which reading is right. `qou-jgg0` leaves that with the
  author, and this probe deliberately does not vote -- it prices the decision.
- It does **not** refute the bean's argument. Under the reading the bean uses,
  which is the reading its own source theorem states, the argument stands.

What it establishes is narrower and, for the naming decision, the point:
**one of the three readings is not interchangeable with the others**, so
"three counts, pick one later" understates the cost. Choosing `3A` would move
this bean's leading explanation onto its worst data point; choosing `3A+Z`
would remove the explanation's subject entirely.

ARITHMETIC
----------
Exact integers throughout -- partition counts by a dynamic-programming recurrence
over ints, strand counts by integer arithmetic. No approximate binary arithmetic
is used or needed, so the NO-FLOAT64 family is satisfied by construction. No
witness emitted; nothing here is q-dependent.
"""

from __future__ import annotations

import sys

fails = 0


def chk(label: str, ok: bool, detail: str = "") -> None:
    global fails
    if not ok:
        fails += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  ({detail})" if detail else ""))


def p(n: int) -> int:
    """Number of partitions of n. Exact integer DP; p(0) = 1."""
    if n < 0:
        return 0
    tab = [0] * (n + 1)
    tab[0] = 1
    for part in range(1, n + 1):
        for tot in range(part, n + 1):
            tab[tot] += tab[tot - part]
    return tab[n]


# (name, A, Z, sign verdict recorded in qou-q6pp)
ATOMS = [
    ("H-1", 1, 1, "over-specified, 5e5 off"),
    ("D",   2, 1, "RIGHT sign (1.448)"),
    ("T",   3, 1, "wrong sign (-0.179)"),
    ("3He", 3, 2, "wrong sign (-0.605)"),
    ("4He", 4, 2, "wrong sign (-0.227)"),
]

READINGS = {
    "A+Z":   lambda A, Z: A + Z,
    "3A":    lambda A, Z: 3 * A,
    "3A+Z":  lambda A, Z: 3 * A + Z,
}

EXTREMAL = 3  # sym, std, alt


def main() -> int:
    print("qou-q6pp's unique-n coincidence under the three live strand readings")
    print()

    # --- 1. p(3) = 3 is the unique n where extremal blocks exhaust ---------
    print("CHECK 1 -- n = 3 is the unique n with p(n) = 3 (extremal count)")
    eq = [n for n in range(1, 61) if p(n) == EXTREMAL]
    print("    p(n) for n = 1..8:  " + ", ".join(f"{n}:{p(n)}" for n in range(1, 9)))
    chk("p(n) = 3 at exactly one n, and it is n = 3", eq == [3], f"n in {eq}")
    chk("p(n) > 3 for every n >= 4 -- the formula is outside its domain there",
        all(p(n) > EXTREMAL for n in range(4, 61)), "n = 4..60")
    print()

    # --- 2. reproduce the bean's own table under A+Z ----------------------
    print("CHECK 2 -- reproducing qou-q6pp's table under its own reading (n = A+Z)")
    print("    atom     n  p(n)  missing  recorded verdict")
    bean = {"H-1": 2, "D": 3, "T": 4, "3He": 5, "4He": 6}
    ok_tab = True
    for name, A, Z, verdict in ATOMS:
        n = A + Z
        if n != bean[name]:
            ok_tab = False
        print(f"    {name:5s} {n:4d} {p(n):5d} {max(0, p(n)-EXTREMAL):8d}  {verdict}")
    chk("the n column reproduces the bean's table exactly", ok_tab, "5 of 5 atoms")
    right = [nm for nm, A, Z, v in ATOMS if v.startswith("RIGHT")]
    at3 = [nm for nm, A, Z, v in ATOMS if A + Z == 3]
    chk("under A+Z the uniquely-exact n is occupied by the right-signed atom",
        right == at3 == ["D"], "D at n = 3 -- the coincidence the bean rests on")
    print()

    # --- 3. which atom sits at n = 3 under each reading --------------------
    print("CHECK 3 -- who occupies the uniquely-exact n, per reading")
    print("    reading   atom(s) at n = 3   their recorded verdict")
    occupants = {}
    for label, f in READINGS.items():
        occ = [(nm, v) for nm, A, Z, v in ATOMS if f(A, Z) == EXTREMAL]
        occupants[label] = occ
        shown = ", ".join(nm for nm, _ in occ) or "(none)"
        note = "; ".join(v for _, v in occ) or "no neutral atom reaches n = 3"
        print(f"    {label:8s}  {shown:17s}  {note}")
    chk("A+Z  -> D, the right-signed atom: coincidence HOLDS",
        [nm for nm, _ in occupants["A+Z"]] == ["D"])
    chk("3A   -> H-1, which the bean records as its WORST point: coincidence INVERTS",
        [nm for nm, _ in occupants["3A"]] == ["H-1"], "over-specified, 5e5 off")
    chk("3A+Z -> nobody: coincidence EVAPORATES",
        occupants["3A+Z"] == [], "3A+Z = 3 needs Z = 0, not a neutral atom")
    print()

    # --- 4. no neutral atom can reach n = 3 under 3A+Z --------------------
    print("CHECK 4 -- the 3A+Z gap is structural, not a small-sample artifact")
    reach = [(A, Z) for A in range(1, 61) for Z in range(1, A + 1) if 3 * A + Z == EXTREMAL]
    chk("3A+Z = 3 has no solution with A >= 1, Z >= 1", not reach,
        "min over neutral atoms is 3*1+1 = 4")
    chk("and the minimum 3A+Z over neutral atoms is 4, already past the domain",
        min(3 * A + Z for A in range(1, 61) for Z in range(1, A + 1)) == 4)
    print()

    # --- 5. the three readings disagree on every atom ----------------------
    print("CHECK 5 -- the readings are not interchangeable at any atom")
    print("    atom      A   Z | A+Z   3A  3A+Z")
    all_distinct = True
    for name, A, Z, _ in ATOMS:
        vals = [f(A, Z) for f in READINGS.values()]
        if len(set(vals)) != 3:
            all_distinct = False
        print(f"    {name:5s} {A:5d} {Z:3d} | {vals[0]:3d}  {vals[1]:3d}  {vals[2]:4d}")
    chk("all three readings differ at every atom in the bean's sample",
        all_distinct, "5 of 5")
    print()

    total = 10
    print(f"{total - fails}/{total} checks passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
