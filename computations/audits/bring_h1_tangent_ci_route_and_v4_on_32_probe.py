#!/usr/bin/env python3
"""H^1(T) of Bring's curve by the complete-intersection route, and what V_4 does to the 5-dimensional [3,2].

CONTEXT.  computations/audits/dimq_regularisation_schemes_probe.py measured
H^1(T_{Sigma_4}) = [4,1] + [3,2] as an S_5-module by ONE route (Serre duality
+ Max Noether: H^1(T) = (Sym^2 V_4 / quadric)^vee).  The owner then asked
whether something natural acts on T_{M_0}, whether the Frobenius pairing /
self-duality gives V_4 an action on the 5-dimensional piece with a kernel or
quotient to take, and whether what is missing is a lifting.  This probe
answers the representation-theoretic half of that exactly, and derives the
decomposition a SECOND, independent way so that the first is not the only
evidence.

ROUTE 2 (complete intersection).  A non-hyperelliptic genus-4 curve is the
canonical complete intersection of a quadric Q_2 and a cubic Q_3 in
P^3 = P(V_4); for Bring's curve Q_2 = sum x_i^2 and Q_3 = sum x_i^3 on
V_4 = {sum x_i = 0}, both S_5-invariant.  The normal-bundle sequence
0 -> T_C -> T_{P^3}|_C -> N_C -> 0 with N_C = O_C(2) + O_C(3) (split by the
invariant equations, so S_5-equivariantly) gives, since H^0(T_C) = 0 (g >= 2)
and H^1(T_{P^3}|_C) = 0 (Euler sequence: H^1(O_C) -> H^1(O_C(1))^4 is dual to
the isomorphism V_4^* -> H^0(K_C)),

    H^1(T_C) = H^0(N_C) - sl(V_4)                      (virtual characters)
             = [Sym^2 V - 1] + [Sym^3 V - 1 - V] - [V (x) V - 1],

where the two brackets are H^0(O_C(2)) = Sym^2 V^*/(Q_2) and
H^0(O_C(3)) = Sym^3 V^*/(Q_3, V^*.Q_2), and V^* ~ V (all S_5 characters are
real).  Route 1 and route 2 agree iff Sym^3 V = V (x) V + V as S_5-modules;
that identity is checked below (it is what forces the two routes to agree).

WHAT V_4 DOES TO [3,2].  Exact multiplicities of every irreducible in
V_4 (x) [3,2], Sym^2 [3,2], Alt^2 [3,2], Sym^2 V_4, Sym^3 V_4, and the
invariants of Sym^2 and Alt^2 of the whole 9-dimensional H^1(T).  The
"action" question is Hom_{S_5}(V_4 (x) [3,2], [3,2]); the "kernel/quotient"
question is [3,2] = Sym^2 V_4 / (1 + V_4) = ker(Sym^2 V_4 -> 1 + V_4).

THE INVARIANT HOCHSCHILD LEDGER OF THE BASE.  By HKR for a smooth curve,
HH_n(C) = H^0(Omega^n) + H^1(Omega^{n+1}) and HH^n(C) = H^0(Lambda^n T) +
H^1(Lambda^{n-1} T).  With H^0(K) = V_4, H^1(O) = V_4 (Serre), H^1(K) = 1,
H^0(T) = 0, H^1(T) = [4,1] + [3,2], the S_5-INVARIANT part is k in HH_0 (twice:
H^0(O) and H^1(K)) and k in HH^0, and ZERO in HH_{+-1}, HH^1 and HH^2.  So an
S_5-equivariant map from any one-dimensional substrate obstruction space to
HH^2(M_0) is zero: the archimedean image of the Wigner class w(A), if it is
equivariant, cannot be a deformation of the base curve; the only invariant
lines are H^0(O) and H^1(K) = H^2(M_0; k), the latter being where the Euler
class e(T_{M_0}) with <e, [M_0]> = chi_eu(M_0) = -6 lives.

CROSS-CHECK OF THE SYMMETRIC-POWER FORMULAS.  Sym^2 and Sym^3 characters of
the permutation representation are ALSO computed by brute force over all 120
permutations (count of fixed monomials), and compared with the power-sum
formulas, so the formulas are not taken on trust.

WHAT THIS DOES NOT CLAIM.  The geometric inputs (N_C = O(2) + O(3),
H^0(T_C) = 0, H^1(T_{P^3}|_C) = 0, HKR for the curve, Serre duality) are
standard theorems cited in the content blocks, not re-derived here.  The
probe does not construct any map from the substrate to the base; it shows
what equivariance forbids.  Nothing here selects a reading of the -6.

No float anywhere: exact integers and Fractions throughout.

Run:  python3 computations/audits/bring_h1_tangent_ci_route_and_v4_on_32_probe.py
"""

from __future__ import annotations

import itertools
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402

FAILURES: list[str] = []
CHECKS = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


# ---------------------------------------------------------------------------
# S_5: classes, sizes, character table (Fulton-Harris §2.3 / James-Kerber).
CYCLE_TYPES = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]
CLASS_SIZE = {(1, 1, 1, 1, 1): 1, (2, 1, 1, 1): 10, (2, 2, 1): 15, (3, 1, 1): 20,
              (3, 2): 20, (4, 1): 30, (5,): 24}
CHAR_TABLE: dict[str, dict[tuple[int, ...], int]] = {
    "[5] trivial":    {(1,1,1,1,1): 1, (2,1,1,1): 1, (2,2,1): 1, (3,1,1): 1, (3,2): 1, (4,1): 1, (5,): 1},
    "[1^5] sign":     {(1,1,1,1,1): 1, (2,1,1,1): -1, (2,2,1): 1, (3,1,1): 1, (3,2): -1, (4,1): -1, (5,): 1},
    "[4,1] standard": {(1,1,1,1,1): 4, (2,1,1,1): 2, (2,2,1): 0, (3,1,1): 1, (3,2): -1, (4,1): 0, (5,): -1},
    "[2,1^3]":        {(1,1,1,1,1): 4, (2,1,1,1): -2, (2,2,1): 0, (3,1,1): 1, (3,2): 1, (4,1): 0, (5,): -1},
    "[3,2]":          {(1,1,1,1,1): 5, (2,1,1,1): 1, (2,2,1): 1, (3,1,1): -1, (3,2): 1, (4,1): -1, (5,): 0},
    "[2,2,1]":        {(1,1,1,1,1): 5, (2,1,1,1): -1, (2,2,1): 1, (3,1,1): -1, (3,2): -1, (4,1): 1, (5,): 0},
    "[3,1,1]":        {(1,1,1,1,1): 6, (2,1,1,1): 0, (2,2,1): -2, (3,1,1): 0, (3,2): 0, (4,1): 0, (5,): 1},
}
Char = dict  # cycle type -> Fraction


def power_class(ct: tuple[int, ...], k: int) -> tuple[int, ...]:
    """Cycle type of g^k: a c-cycle splits into gcd(c,k) cycles of length c/gcd(c,k)."""
    from math import gcd
    out: list[int] = []
    for c in ct:
        d = gcd(c, k)
        out += [c // d] * d
    return tuple(sorted(out, reverse=True))


def cycle_type(perm: tuple[int, ...]) -> tuple[int, ...]:
    seen, cycles = set(), []
    for i in range(len(perm)):
        if i in seen:
            continue
        n, j = 0, i
        while j not in seen:
            seen.add(j); j = perm[j]; n += 1
        cycles.append(n)
    return tuple(sorted(cycles, reverse=True))


def const(v: int) -> Char:
    return {ct: Fraction(v) for ct in CYCLE_TYPES}


def add(a: Char, b: Char) -> Char:
    return {ct: a[ct] + b[ct] for ct in CYCLE_TYPES}


def sub(a: Char, b: Char) -> Char:
    return {ct: a[ct] - b[ct] for ct in CYCLE_TYPES}


def mul(a: Char, b: Char) -> Char:
    return {ct: a[ct] * b[ct] for ct in CYCLE_TYPES}


def sym2(chi: Char) -> Char:
    return {ct: (chi[ct] ** 2 + chi[power_class(ct, 2)]) / 2 for ct in CYCLE_TYPES}


def alt2(chi: Char) -> Char:
    return {ct: (chi[ct] ** 2 - chi[power_class(ct, 2)]) / 2 for ct in CYCLE_TYPES}


def sym3(chi: Char) -> Char:
    return {ct: (chi[ct] ** 3 + 3 * chi[ct] * chi[power_class(ct, 2)] + 2 * chi[power_class(ct, 3)]) / 6
            for ct in CYCLE_TYPES}


def multiplicity(chi: Char, irrep: dict) -> Fraction:
    return sum((CLASS_SIZE[ct] * chi[ct] * irrep[ct] for ct in CYCLE_TYPES), Fraction(0)) / 120


def decompose(chi: Char) -> dict[str, int]:
    out = {}
    for name, row in CHAR_TABLE.items():
        m = multiplicity(chi, row)
        assert m.denominator == 1 and m >= 0, (name, m)
        if m:
            out[name] = int(m)
    return out


def fmt(dec: dict[str, int]) -> str:
    return " + ".join(f"{m}x{n}" if m > 1 else n for n, m in dec.items()) or "0"


def brute_force_symk_perm5(k: int) -> Char:
    """Character of Sym^k(C^5) for the permutation representation of S_5:
    number of degree-k monomials in x_1..x_5 fixed by each permutation."""
    monos = [m for m in itertools.combinations_with_replacement(range(5), k)]
    acc: dict[tuple[int, ...], list[int]] = {ct: [] for ct in CYCLE_TYPES}
    for p in itertools.permutations(range(5)):
        fixed = sum(1 for m in monos if tuple(sorted(p[i] for i in m)) == m)
        acc[cycle_type(p)].append(fixed)
    out = {}
    for ct, vals in acc.items():
        assert len(set(vals)) == 1 and len(vals) == CLASS_SIZE[ct], (ct, Counter(vals))
        out[ct] = Fraction(vals[0])
    return out


def main() -> int:
    triv = {ct: Fraction(v) for ct, v in CHAR_TABLE["[5] trivial"].items()}
    perm5 = {ct: Fraction(sum(1 for c in ct if c == 1)) for ct in CYCLE_TYPES}
    V = sub(perm5, triv)                                  # standard V_4
    W = {ct: Fraction(v) for ct, v in CHAR_TABLE["[3,2]"].items()}
    print("S_5 on the deformations of Bring's curve, exactly")
    print()

    # -- 0. the table is orthonormal (sanity on the input) ----------------
    print("0. character table sanity")
    names = list(CHAR_TABLE)
    gram_ok = all(
        multiplicity({ct: Fraction(v) for ct, v in CHAR_TABLE[a].items()}, CHAR_TABLE[b]) == (1 if a == b else 0)
        for a in names for b in names)
    check("the seven rows are orthonormal for the class-weighted inner product", gram_ok)
    check("sum of squared dimensions is 120", sum(r[(1, 1, 1, 1, 1)] ** 2 for r in CHAR_TABLE.values()) == 120)
    check("every character value is an integer, so every irreducible is self-dual (chi = chi-bar)",
          all(isinstance(v, int) for r in CHAR_TABLE.values() for v in r.values()))
    print()

    # -- 1. symmetric-power formulas vs brute force -----------------------
    print("1. Sym^2 and Sym^3 of the permutation representation: formula vs brute force over 120 permutations")
    for k, f in ((2, sym2), (3, sym3)):
        bf, fo = brute_force_symk_perm5(k), f(perm5)
        check(f"Sym^{k}(perm_5): power-sum formula agrees with the fixed-monomial count on all 7 classes", bf == fo,
              "  ".join(f"{ct}:{int(bf[ct])}" for ct in CYCLE_TYPES))
    print()

    # -- 2. the pieces --------------------------------------------------
    print("2. decompositions")
    dS2V, dS3V, dA2V, dVV = decompose(sym2(V)), decompose(sym3(V)), decompose(alt2(V)), decompose(mul(V, V))
    check("Sym^2 V_4 = [5] + [4,1] + [3,2]   (dim 10)", dS2V == {"[5] trivial": 1, "[4,1] standard": 1, "[3,2]": 1},
          fmt(dS2V))
    check("Sym^3 V_4 = [5] + 2[4,1] + [3,2] + [3,1,1]   (dim 20)",
          dS3V == {"[5] trivial": 1, "[4,1] standard": 2, "[3,2]": 1, "[3,1,1]": 1}, fmt(dS3V))
    check("Alt^2 V_4 = [3,1,1]   (irreducible, dim 6)", dA2V == {"[3,1,1]": 1}, fmt(dA2V))
    check("V_4 (x) V_4 = [5] + [4,1] + [3,2] + [3,1,1]   (so sl(V_4) = [4,1] + [3,2] + [3,1,1], dim 15)",
          dVV == {"[5] trivial": 1, "[4,1] standard": 1, "[3,2]": 1, "[3,1,1]": 1}, fmt(dVV))
    print()

    # -- 3. route 2: complete intersection -------------------------------
    print("3. H^1(T_C) by the complete-intersection route")
    h0O2 = sub(sym2(V), triv)                  # H^0(O_C(2)) = Sym^2 V^* / (Q_2)
    h0O3 = sub(sub(sym3(V), triv), V)          # H^0(O_C(3)) = Sym^3 V^* / (Q_3, V^*.Q_2)
    h0N = add(h0O2, h0O3)                      # H^0(N_C)
    sl4 = sub(mul(V, V), triv)                 # H^0(T_{P^3}|_C) = sl(V_4)
    h1T_ci = sub(h0N, sl4)
    h1T_noether = sub(sym2(V), triv)           # route 1: (Sym^2 V / Q_2)^vee, V self-dual
    check("dim H^0(O_C(2)) = 9 = 3g-3 and dim H^0(O_C(3)) = 15 = 5g-5 at g = 4",
          h0O2[(1, 1, 1, 1, 1)] == 9 and h0O3[(1, 1, 1, 1, 1)] == 15)
    check("dim H^0(N_C) = 24 and dim sl(V_4) = 15, so dim H^1(T_C) = 9 = 3g-3",
          h0N[(1, 1, 1, 1, 1)] == 24 and sl4[(1, 1, 1, 1, 1)] == 15 and h1T_ci[(1, 1, 1, 1, 1)] == 9)
    dCI = decompose(h1T_ci)
    check("route 2: H^1(T_C) = [4,1] + [3,2]", dCI == {"[4,1] standard": 1, "[3,2]": 1}, fmt(dCI))
    check("route 1 (Serre + Noether) gives the same virtual character on every class", h1T_ci == h1T_noether)
    check("the identity forcing agreement: Sym^3 V_4 = V_4 (x) V_4 + V_4 as S_5-modules",
          sym3(V) == add(mul(V, V), V))
    dH0N = decompose(h0N)
    check("H^0(N_C) = 2[4,1] + 2[3,2] + [3,1,1]; the sl(V_4) image removes one of each and all of [3,1,1]",
          dH0N == {"[4,1] standard": 2, "[3,2]": 2, "[3,1,1]": 1}, fmt(dH0N))
    check("H^1(T_C)^{S_5} = 0 (no invariant first-order deformation: Bring's curve is rigid as an S_5-curve)",
          multiplicity(h1T_ci, CHAR_TABLE["[5] trivial"]) == 0)
    check("H^1(T_C) has no sign summand either", multiplicity(h1T_ci, CHAR_TABLE["[1^5] sign"]) == 0)
    print()

    # -- 4. what V_4 does to [3,2] ---------------------------------------
    print("4. V_4 and the five-dimensional [3,2]")
    dVW = decompose(mul(V, W))
    check("V_4 (x) [3,2] = [4,1] + [3,2] + [3,1,1] + [2,2,1]   (dim 20)",
          dVW == {"[4,1] standard": 1, "[3,2]": 1, "[3,1,1]": 1, "[2,2,1]": 1}, fmt(dVW))
    check("Hom_{S_5}(V_4 (x) [3,2], [3,2]) is ONE-dimensional: V_4 acts on [3,2] equivariantly in exactly one way up to scale",
          multiplicity(mul(V, W), CHAR_TABLE["[3,2]"]) == 1)
    check("Hom_{S_5}(V_4 (x) [3,2], V_4) is one-dimensional too: a unique equivariant pairing [3,2] x V_4 -> V_4",
          multiplicity(mul(V, W), CHAR_TABLE["[4,1] standard"]) == 1)
    check("[3,2] = Sym^2 V_4 / ([5] + [4,1]): the quotient of quadratic forms on V_4 by the invariant quadric and the diagonal copy of V_4",
          dS2V.get("[3,2]") == 1 and dS2V.get("[5] trivial") == 1 and dS2V.get("[4,1] standard") == 1)
    dS2W, dA2W = decompose(sym2(W)), decompose(alt2(W))
    check("Sym^2 [3,2] carries exactly ONE invariant: the Frobenius (self-duality) form on the block is symmetric",
          dS2W.get("[5] trivial") == 1, f"Sym^2[3,2] = {fmt(dS2W)}")
    check("Alt^2 [3,2] carries NO invariant: there is no S_5-invariant symplectic form on [3,2]",
          dA2W.get("[5] trivial", 0) == 0, f"Alt^2[3,2] = {fmt(dA2W)}")
    check("[3,2] (x) [3,2] contains V_4 exactly once (the unique equivariant product [3,2] x [3,2] -> V_4)",
          multiplicity(mul(W, W), CHAR_TABLE["[4,1] standard"]) == 1)
    h1T = h1T_ci
    dS2H, dA2H = decompose(sym2(h1T)), decompose(alt2(h1T))
    check("Sym^2 H^1(T) has exactly 2 invariants (one symmetric form per summand) and Alt^2 H^1(T) has NONE: "
          "no S_5-invariant symplectic structure on the 9-dimensional deformation space",
          dS2H.get("[5] trivial") == 2 and dA2H.get("[5] trivial", 0) == 0,
          f"Sym^2 = {fmt(dS2H)}\nAlt^2 = {fmt(dA2H)}")
    print()

    # -- 5. invariant Hochschild ledger of the base curve ----------------
    print("5. S_5-invariants of the Hochschild (co)homology of the base curve (HKR + Serre)")
    h0K, h1O, h1K, h0O = V, V, triv, triv       # H^0(K) = V_4, H^1(O) = H^0(K)^vee = V_4, H^1(K) = H^0(O) = 1
    HH = {"HH_1": h0K, "HH_0": add(h0O, h1K), "HH_-1": h1O}
    HHc = {"HH^0": h0O, "HH^1": h1O, "HH^2": h1T}     # H^0(T) = 0 for g >= 2
    inv = {k: int(multiplicity(v, CHAR_TABLE["[5] trivial"])) for k, v in {**HH, **HHc}.items()}
    dims = {k: int(v[(1, 1, 1, 1, 1)]) for k, v in {**HH, **HHc}.items()}
    check("dimensions: HH_1 = 4, HH_0 = 2, HH_-1 = 4; HH^0 = 1, HH^1 = 4, HH^2 = 9",
          dims == {"HH_1": 4, "HH_0": 2, "HH_-1": 4, "HH^0": 1, "HH^1": 4, "HH^2": 9}, str(dims))
    check("invariants: HH_0^{S_5} = k^2 (H^0(O) and H^1(K) = H^2(M_0;k)), HH^0^{S_5} = k, and ZERO in HH_{+-1}, HH^1, HH^2",
          inv == {"HH_1": 0, "HH_0": 2, "HH_-1": 0, "HH^0": 1, "HH^1": 0, "HH^2": 0}, str(inv))
    check("alternating sum of the invariant homology is chi(Sigma_4 / S_5) = chi(P^1) = 2",
          inv["HH_0"] - inv["HH_1"] - inv["HH_-1"] == 2)
    check("alternating sum of the full homology is chi_eu(Sigma_4) = 2 - 2g = -6",
          dims["HH_0"] - dims["HH_1"] - dims["HH_-1"] == -6)
    check("consequence: an S_5-equivariant map from ANY one-dimensional space to HH^2(M_0) is zero; "
          "the Wigner class cannot land in the deformations of the base curve", inv["HH^2"] == 0)
    print()

    print(f"{CHECKS - len(FAILURES)}/{CHECKS} checks pass")

    w = WitnessBuilder("bring-h1-tangent-ci-route-and-v4-on-32", engine="exact-rational")
    out = w.save(
        {
            "q0Anchor": "independent",
            "q0_anchor_reason": "q-independent: S_5 representation theory over Q; no substrate parameter enters",
            "description": (
                "H^1(T) of Bring's curve = [4,1] + [3,2] as an S_5-module, derived by the "
                "complete-intersection route (H^0(N_C) - sl(V_4)) and shown to agree with the "
                "Serre + Max Noether route; exact multiplicities of V_4 (x) [3,2], Sym^2/Alt^2 of "
                "[3,2] and of H^1(T); the S_5-invariant Hochschild ledger of the base curve "
                "(invariants only in HH_0 = k^2 and HH^0 = k; none in HH^2)."
            ),
            "h1_tangent_bring_s5_decomposition_ci_route": dCI,
            "h0_normal_bundle_s5_decomposition": dH0N,
            "sym2_V4": dS2V, "sym3_V4": dS3V, "alt2_V4": dA2V, "V4_tensor_V4": dVV,
            "V4_tensor_32": dVW, "sym2_32": dS2W, "alt2_32": dA2W,
            "sym2_h1T": dS2H, "alt2_h1T": dA2H,
            "hom_V4_tensor_32_to_32": 1, "hom_V4_tensor_32_to_V4": 1,
            "hochschild_ledger_dims": dims, "hochschild_ledger_s5_invariants": inv,
            "checks": CHECKS,
            "failures": FAILURES,
            "scope": "b: exact finite computations from the S_5 character table; geometric inputs cited, not re-derived",
        }
    )
    print(f"witness -> {out}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
