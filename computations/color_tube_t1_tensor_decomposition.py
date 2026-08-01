#!/usr/bin/env python3
"""color_tube_t1_tensor_decomposition.py — the color-pair space from the fiber action.

Bean qou-ctkw / open question 1 of `conj:inter-nucleon-channel-color-tube`:
what is the closed form of the 9-element color-pair weight tensor
`W_{c1c2}(F1,F2)` "from the SO(3)-fiber tensor over Bring"?

The pieces are now in place and Lean-proved:

  * `BringFiberAction` is DISCHARGED by the icosahedral Reeb instance
    (`bringFiberAction_icosahedral`);
  * the three color sheets ARE the T1 irrep of A5 ~ I — `color_sheets_carry_T1`
    (3 sheets = dim T1, and T1 is the l=1 Hopf generation selection).

So the space of ordered color-sheet PAIRS carries T1 (x) T1, a 9-dimensional
representation of the icosahedral group. This probe decomposes it EXACTLY by
character arithmetic over Q(sqrt 5), extracts the isotypic projectors, and reads
off the induced weight systems.

WHAT IS TESTED (derive-then-check, 0 free parameters)
-----------------------------------------------------
1. The decomposition `T1 (x) T1 = A (+) T1 (+) H` (dims 1+3+5 = 9), by exact
   inner products of characters on the 5 conjugacy classes of A5.
2. The symmetric/antisymmetric split: `Sym^2 T1 = A (+) H` (dim 6),
   `Alt^2 T1 = T1` (dim 3) — a canonical Z/2 grading of the color-pair space,
   which is the shape the block's own "representation-theoretic constraint on
   eps" demands.
3. The diagonal of each isotypic projector, normalised to sum to 1 — i.e. the
   canonical weight system each summand induces on the 9 color pairs.
4. The relation of those to the uniform-flavor projection W = 1/9.

NOT claimed: this does not by itself close open question 1. The flavor
dependence `(F1,F2)` is not supplied by the color-side decomposition; what the
decomposition gives is a canonical BASIS of admissible weight systems. Reported
as a scope-(a) narrowing, and nothing is wired.

STRICT anti-fit: no target is consulted; no quantity is tuned. Exact arithmetic
throughout (sympy over Q(sqrt 5)); all identities are equalities, not fits.

Run:  python3 -u color_tube_t1_tensor_decomposition.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

import sympy as sp  # noqa: E402

_T0_MONO = time.monotonic()

# ── A5 ~ I: five conjugacy classes, with sizes summing to |A5| = 60 ──────────
# (identity, double-transposition, 3-cycle, and the two enantiomorphic 5-cycles
#  — the class-side face of the T1/T2 chirality, per S5SO3FiberAction.)
CLASSES = ["e", "2", "3", "5A", "5B"]
SIZES = {"e": 1, "2": 15, "3": 20, "5A": 12, "5B": 12}

phi = (1 + sp.sqrt(5)) / 2          # golden ratio
phibar = (1 - sp.sqrt(5)) / 2       # = 1 - phi

# Character table of A5 (standard; the T1/T2 golden-ratio entries on the
# 5-cycle classes are the icosahedral fingerprint validated in PR #2591).
CHAR = {
    "A":  {"e": sp.Integer(1), "2": sp.Integer(1),  "3": sp.Integer(1),  "5A": sp.Integer(1),  "5B": sp.Integer(1)},
    "T1": {"e": sp.Integer(3), "2": sp.Integer(-1), "3": sp.Integer(0),  "5A": phi,            "5B": phibar},
    "T2": {"e": sp.Integer(3), "2": sp.Integer(-1), "3": sp.Integer(0),  "5A": phibar,         "5B": phi},
    "G":  {"e": sp.Integer(4), "2": sp.Integer(0),  "3": sp.Integer(1),  "5A": sp.Integer(-1), "5B": sp.Integer(-1)},
    "H":  {"e": sp.Integer(5), "2": sp.Integer(1),  "3": sp.Integer(-1), "5A": sp.Integer(0),  "5B": sp.Integer(0)},
}
IRREPS = ["A", "T1", "T2", "G", "H"]

# Squaring map on classes: g -> g^2 (needed for Sym^2 / Alt^2 characters).
# e^2=e; (ab)(cd)^2=e; (abc)^2=(acb) is still a 3-cycle; a 5-cycle squared
# lands in the OTHER 5-class (the index-2 fusion that swaps 5A <-> 5B).
SQUARE = {"e": "e", "2": "e", "3": "3", "5A": "5B", "5B": "5A"}


def inner(chi1: dict, chi2: dict) -> sp.Expr:
    """<chi1, chi2> = (1/|G|) sum_classes |class| chi1(g) conj(chi2(g)).
    All characters here are real, so conjugation is the identity."""
    return sp.nsimplify(sp.expand(sp.Rational(1, 60) * sum(
        SIZES[c] * chi1[c] * chi2[c] for c in CLASSES)))


def orthonormality_check() -> bool:
    """Guard: the table must be orthonormal, else every result below is junk."""
    for a in IRREPS:
        for b in IRREPS:
            want = 1 if a == b else 0
            if sp.simplify(inner(CHAR[a], CHAR[b]) - want) != 0:
                return False
    return True


def main() -> int:
    print("=" * 84)
    print("T1 (x) T1 in A5 ~ I — the color-pair space from the discharged fiber action")
    print("=" * 84)

    assert orthonormality_check(), "A5 character table failed orthonormality"
    print("\ncharacter table orthonormality: OK (exact over Q(sqrt 5))")

    t1 = CHAR["T1"]
    # tensor-square character
    chi_tensor = {c: sp.expand(t1[c] ** 2) for c in CLASSES}
    # Sym^2 / Alt^2 characters
    chi_sym = {c: sp.expand(sp.Rational(1, 2) * (t1[c] ** 2 + t1[SQUARE[c]])) for c in CLASSES}
    chi_alt = {c: sp.expand(sp.Rational(1, 2) * (t1[c] ** 2 - t1[SQUARE[c]])) for c in CLASSES}

    def decompose(chi, label):
        mult = {irr: inner(chi, CHAR[irr]) for irr in IRREPS}
        dim = sum(mult[i] * CHAR[i]["e"] for i in IRREPS)
        parts = " + ".join(f"{irr}" if mult[irr] == 1 else f"{mult[irr]}*{irr}"
                           for irr in IRREPS if mult[irr] != 0)
        print(f"  {label:12s} = {parts:24s}  (dim {sp.simplify(dim)}, "
              f"chi(e) = {chi['e']})")
        assert sp.simplify(dim - chi["e"]) == 0, f"{label}: dim mismatch"
        return {k: int(v) for k, v in mult.items()}

    print("\nDecompositions (exact character inner products):")
    m_tensor = decompose(chi_tensor, "T1 (x) T1")
    m_sym = decompose(chi_sym, "Sym^2 T1")
    m_alt = decompose(chi_alt, "Alt^2 T1")

    # ── isotypic projector diagonals on the 9 ordered color pairs ────────────
    # Basis e_{c1} (x) e_{c2}, c in {r,g,b}. The three isotypic projectors are:
    #   P_A   = (1/3) * |sum_c e_c (x) e_c><...|      (the invariant/metric line)
    #   P_alt = antisymmetriser                        (= Alt^2 T1 = T1)
    #   P_H   = Sym^2 minus the invariant line
    # Their diagonal entries in this basis (same-color vs different-color):
    diag = {
        "A":   {"same": sp.Rational(1, 3), "diff": sp.Integer(0)},
        "T1":  {"same": sp.Integer(0),     "diff": sp.Rational(1, 2)},
        "H":   {"same": sp.Rational(2, 3), "diff": sp.Rational(1, 2)},
    }
    print("\nIsotypic projector diagonals on the 9 ordered color pairs")
    print("  (3 same-color pairs rr/gg/bb, 6 different-color pairs):")
    print("  summand   diag(same)  diag(diff)   trace = dim   normalised weights")
    weights = {}
    for irr in ("A", "T1", "H"):
        s, d = diag[irr]["same"], diag[irr]["diff"]
        tr = sp.simplify(3 * s + 6 * d)
        assert sp.simplify(tr - CHAR[irr]["e"]) == 0, f"{irr}: projector trace != dim"
        w_same, w_diff = sp.nsimplify(s / tr), sp.nsimplify(d / tr)
        assert sp.simplify(3 * w_same + 6 * w_diff - 1) == 0, f"{irr}: weights must sum to 1"
        weights[irr] = {"same": w_same, "diff": w_diff}
        print(f"  {irr:8s}  {str(s):10s}  {str(d):10s}   {tr}            "
              f"same={w_same}, diff={w_diff}")

    # ── relation to the uniform-flavor projection W = 1/9 ────────────────────
    # sum of the three projectors = identity on the 9-dim space, whose diagonal
    # is 1 everywhere; normalising by 9 gives exactly the uniform W = 1/9.
    id_same = sp.simplify(sum(diag[i]["same"] for i in ("A", "T1", "H")))
    id_diff = sp.simplify(sum(diag[i]["diff"] for i in ("A", "T1", "H")))
    uniform_same = sp.nsimplify(id_same / 9)
    uniform_diff = sp.nsimplify(id_diff / 9)
    print(f"\nSum of the three projectors = identity: diag(same)={id_same}, "
          f"diag(diff)={id_diff}")
    print(f"  normalised by 9  ->  same={uniform_same}, diff={uniform_diff} "
          f"= the UNIFORM projection W = 1/9")
    uniform_is_barycentre = (uniform_same == sp.Rational(1, 9)
                             and uniform_diff == sp.Rational(1, 9))

    print("\n" + "=" * 84)
    print("FINDING (scope-(a) narrowing, NOT a closure)")
    print("=" * 84)
    print("* T1 (x) T1 = A (+) T1 (+) H, exactly (1+3+5 = 9) — the color-pair space")
    print("  has a canonical 3-summand isotypic decomposition from the DISCHARGED")
    print("  fiber action, with no free parameters.")
    print("* Sym^2 T1 = A (+) H (dim 6), Alt^2 T1 = T1 (dim 3) — a canonical Z/2")
    print("  grading of the 9 color pairs, the shape the block's eps constraint needs.")
    print("* Each summand induces a normalised weight system on the 9 pairs, and the")
    print("  UNIFORM projection W = 1/9 is exactly their identity-sum barycentre —")
    print("  i.e. the 'flavor-only projection' the conjecture calls lossy IS the")
    print("  isotypy-blind average. That is a structural reading of the projection,")
    print("  not a fit.")
    print("* So W is narrowed from an arbitrary nonneg normalised 9-vector (8 free")
    print("  parameters per flavor pair) to a convex combination of THREE canonical")
    print("  weight systems (2 free parameters).")
    print("* OPEN: the flavor dependence (F1,F2) is NOT supplied by the color-side")
    print("  decomposition. Open question 1 is narrowed, not closed. Nothing wired.")

    w = WitnessBuilder("color-tube-t1-tensor-decomposition", engine="python",
                       start_time=_T0_MONO)
    w.set_description(
        "Decomposes the color-pair space T1 (x) T1 of the icosahedral fiber action "
        "(bean qou-ctkw; open question 1 of conj:inter-nucleon-channel-color-tube). The "
        "three color sheets ARE the T1 irrep (Lean color_sheets_carry_T1) and "
        "BringFiberAction is discharged, so ordered color-sheet pairs carry T1 (x) T1. "
        "Exact character arithmetic over Q(sqrt 5) on the 5 classes of A5 gives "
        "T1 (x) T1 = A + T1 + H (1+3+5=9), with Sym^2 = A + H (6) and Alt^2 = T1 (3) — a "
        "canonical Z/2 grading of the 9 color pairs, the shape the block's "
        "representation-theoretic eps constraint requires. Each isotypic projector "
        "induces a normalised weight system, and the uniform-flavor projection W=1/9 is "
        "exactly their identity-sum barycentre: the projection the conjecture calls "
        "lossy IS the isotypy-blind average. NARROWS W from 8 free parameters per "
        "flavor pair to a 2-parameter convex combination of three canonical systems. "
        "Does NOT close open question 1 — the flavor dependence (F1,F2) is not supplied "
        "by the color side. Scope-(a); 0 free parameters; no target consulted; nothing "
        "wired."
    )
    w.add_data("tensor_multiplicities", m_tensor)
    w.add_data("sym2_multiplicities", m_sym)
    w.add_data("alt2_multiplicities", m_alt)
    w.add_data("isotypic_normalised_weights",
               {k: {kk: str(vv) for kk, vv in v.items()} for k, v in weights.items()})
    w.add_data("uniform_projection_is_barycentre", bool(uniform_is_barycentre))
    w.add_assertion(
        "t1_tensor_t1_eq_A_plus_T1_plus_H",
        computed=float(m_tensor["A"] * 100 + m_tensor["T1"] * 10 + m_tensor["H"]),
        expected=111.0, tolerance=0.0,
        source="Exact character inner products on the 5 conjugacy classes of A5 give "
               "multiplicity 1 for each of A, T1, H and 0 for T2, G — so "
               "T1 (x) T1 = A + T1 + H with dims 1+3+5 = 9. Character table "
               "orthonormality is asserted first, so the decomposition is not read off "
               "an unvalidated table.",
    )
    w.add_assertion(
        "sym_alt_split_is_6_plus_3",
        computed=float(sum(m_sym[i] * CHAR[i]["e"] for i in IRREPS)) * 10
        + float(sum(m_alt[i] * CHAR[i]["e"] for i in IRREPS)),
        expected=63.0, tolerance=0.0,
        source="Sym^2 T1 = A + H (dim 6) and Alt^2 T1 = T1 (dim 3), computed from the "
               "class-squaring map (note the 5-cycle classes swap under squaring — the "
               "index-2 fusion behind the T1/T2 chirality). This is the canonical Z/2 "
               "grading of the 9 color pairs.",
    )
    w.add_assertion(
        "uniform_projection_is_isotypy_blind_barycentre",
        computed=1.0 if uniform_is_barycentre else 0.0,
        expected=1.0, tolerance=0.0,
        source="The three isotypic projectors sum to the identity on the 9-dimensional "
               "color-pair space, whose diagonal is 1 on every pair; normalising by 9 "
               "returns exactly W = 1/9. So the uniform-flavor projection is the "
               "isotypy-blind average of the canonical weight systems — a structural "
               "reading of the projection the conjecture identifies as lossy.",
    )
    out = w.save()
    print(f"\nwitness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
