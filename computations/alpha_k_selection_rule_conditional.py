#!/usr/bin/env python3
# polynomial_q_not_applicable: every identity is EXACT/symbolic over Q(q)
# (sympy; hook-length q-dimensions, transpose combinatorics, the product
# identity in R); the only archimedean touch is a reference evaluation at q_0.
"""
alpha_{basis-knot} per-force SELECTION rule — conditional derivation (no pi).

Owner directive (2026-06-12): work the OPEN scope of
alpha_k_per_force_assembly.py — "the per-force SELECTION rule: which carrier
PAIR mediates each of the other forces (strong alpha_s, weak alpha_W, ...)" —
conditional on conj:e-hartree-categorical-derivation, WITHOUT enumeration
against measured couplings (anti-fishing).

THE SELECTION RULE (conditional, structural; derived here exactly).

  Setting: n = 4 reference braid (covalent worked example of
  prop:force-carrier-intertwining-correspondence).  Two established layers:
    - q-dimension layer (SU_q(2) fibre): A^{(x)4} = V_2 + 3 V_1 + 2 V_0; the
      multiplicity space of the unit is 2-dimensional
      (alpha_k_four_strand_singlet_selection.py) and, under Schur-Weyl
      duality, IS the Hecke irrep V_{(2,2)} — the UNIQUE SELF-TRANSPOSE
      block at n = 4 ((2,2)^T = (2,2)).  dim V_{(2,2)} = 2 standard
      tableaux; dim_q V_{(2,2)} = [4]_q/[2]_q = q^2 + q^{-2}.
    - Markov/Wedderburn layer: the carriers land on the transpose PAIR
      lambda(T_{2,9}) = (2,1,1) and lambda(T_{3,5}) = (3,1), with
      (3,1)^T = (2,1,1) and equal q-dimensions
      dim_q V_{(3,1)} = dim_q V_{(2,1,1)} = [3]_q (hook lengths, exact).

  Rule (conditional on the gate conjecture):
    1. A UNIVERSAL (scalar) coupling must land in the self-transpose scalar
       block (2,2) (antipode/bar-closed; the only block both layers share
       beyond the trivial ones).  A SINGLE carrier insertion lands on
       (2,1,1) or (3,1) — NOT self-transpose — so no single carrier
       mediates a universal coupling (the round-17 exact zero of the (2,2)
       component under single insertion is the computational shadow of
       this).  The MINIMAL insertion reaching the self-dual block is the
       transpose PAIR (T_{2,9}, T_{3,5}).  Hence EM (the universal force) is
       the pair coupling:  1/alpha_EM = q [9]_q [10]_q  (established).
    2. The two SHORT-RANGE forces are the two single-carrier channels:
           strong  <->  (2,1,1), carrier T_{2,9}, decoration h[9]_q,
           weak    <->  (3,1),   carrier T_{3,5}, decoration h[10]_q.
       Short-range BECAUSE non-scalar: their channels are not
       antipode-closed individually, so they cannot appear as a universal
       1/r^2-type scalar coupling — confinement/massive-mediation is the
       archimedean image of non-self-duality (structural reading,
       conditional).
    3. INVARIANT product identity (exact in R, derived not fitted):
           (q^{1/2} [9]_q) * (q^{1/2} [10]_q) = q [9]_q [10]_q
       i.e. IF the per-channel couplings are defined by the symmetric split
       1/alpha_s := q^{1/2}[9]_q and 1/alpha_W := q^{1/2}[10]_q, then
           alpha_s * alpha_W = alpha_EM      (exact).
       The INVARIANT content is the product identity (any split with
       q^{p} q^{p'} = q^1 satisfies it); the symmetric split is the unique
       carrier-symmetric convention and is marked CONVENTION, not derived.

HONESTY TIER.
  - established: the role table, the writhe decorations, 1/alpha_EM.
  - exact-derived (this probe): the Schur-Weyl slot identification, the
    transpose/self-transpose combinatorics, the hook q-dimensions, the
    product identity.
  - conditional-structural: the selection rule 1-2 (gated on
    conj:e-hartree-categorical-derivation round-18 state).
  - convention: the symmetric q^{1/2} split of the q-prefactor.
  - NOT done: any comparison of q^{1/2}[9]_q or q^{1/2}[10]_q against
    measured alpha_s(mu)/alpha_W (running couplings, scheme-dependent —
    a comparison would be fishing until the archimedean functor for
    non-scalar channels is derived).

Refs: prop:force-carrier-intertwining-correspondence;
prop:alpha-em-categorical-trace-ratio; prop:torus-knot-delta-q-writhe;
thm:em-spectral-completeness; cor:gauge-coupling-uniqueness;
prop:alpha-em-shift-multiplicative-chain (pole-order primitive);
conj:e-hartree-categorical-derivation (gate; round-17 (2,2)-zero,
round-18 intertwining reframing).
"""
from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

import sympy as sp

try:
    import mpmath as mp
    mp.mp.dps = 70
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099785827513808075916690956107688798744991218736"


def transpose(lam: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def standard_tableaux_count(lam: tuple[int, ...]) -> int:
    """Hook-length formula (classical), exact integers."""
    n = sum(lam)
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    hooks = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for r in lam[i + 1:] if r > j)
            hooks *= arm + leg + 1
    assert fact % hooks == 0
    return fact // hooks


def qdim(lam: tuple[int, ...], q: sp.Symbol) -> sp.Expr:
    """q-dimension via the hook-length formula: [n]_q! / prod hooks [h]_q."""
    def qint(k: int) -> sp.Expr:
        return (q ** k - q ** (-k)) / (q - 1 / q)
    n = sum(lam)
    num = sp.prod([qint(k) for k in range(1, n + 1)])
    den = sp.Integer(1)
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for r in lam[i + 1:] if r > j)
            den *= qint(arm + leg + 1)
    return sp.simplify(num / den)


def main() -> None:
    w = WitnessBuilder("alpha-k-selection-rule-conditional", engine="python")
    q = sp.symbols("q", positive=True)

    partitions4 = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    lam_strong, lam_weak, lam_scalar = (2, 1, 1), (3, 1), (2, 2)

    # 1. self-transpose classification at n=4
    self_dual = [lam for lam in partitions4 if transpose(lam) == lam]
    scalar_unique = self_dual == [lam_scalar]
    pair_transpose = transpose(lam_weak) == lam_strong

    # the carrier pair is the UNIQUE transpose-dual pair among the
    # intertwining channels (m,1^{4-m}) for m in {2,3}
    channels = [(2, 1, 1), (3, 1)]
    unique_pair = [frozenset((a, b)) for a, b in combinations(channels, 2)
                   if transpose(a) == b] == [frozenset(((2, 1, 1), (3, 1)))]

    # 2. dimensions: slot space = V_{(2,2)} (Schur-Weyl), carriers both [3]_q
    slot_dim_ok = standard_tableaux_count(lam_scalar) == 2  # = Catalan(2)
    d22 = qdim(lam_scalar, q)
    d31 = qdim(lam_weak, q)
    d211 = qdim(lam_strong, q)
    qint3 = sp.simplify((q ** 3 - q ** -3) / (q - 1 / q))
    d22_ok = sp.simplify(d22 - (q ** 2 + q ** -2)) == 0      # [4]_q/[2]_q
    carriers_eq = sp.simplify(d31 - d211) == 0
    carriers_3q = sp.simplify(d31 - qint3) == 0

    # 3. invariant product identity in R (exact):
    #    (q^{1/2}[9]_q)(q^{1/2}[10]_q) = q [9]_q [10]_q
    def qint_expr(k: int) -> sp.Expr:
        return (q ** k - q ** (-k)) / (q - 1 / q)
    inv_alpha_s = sp.sqrt(q) * qint_expr(9)
    inv_alpha_w = sp.sqrt(q) * qint_expr(10)
    inv_alpha_em = q * qint_expr(9) * qint_expr(10)
    product_ok = sp.simplify(inv_alpha_s * inv_alpha_w - inv_alpha_em) == 0

    # archimedean reference values at q_0 (no comparison to experiment)
    q0 = mp.mpf(Q0) if HAVE_MP else float(Q0)
    f = sp.lambdify(q, (inv_alpha_s, inv_alpha_w, inv_alpha_em), "mpmath")
    v_s, v_w, v_em = f(q0)

    print("=" * 74)
    print("alpha_K per-force SELECTION rule — conditional derivation (exact)")
    print("=" * 74)
    print(f"  self-transpose blocks at n=4: {self_dual}  (unique = (2,2): "
          f"{scalar_unique})")
    print(f"  carrier channels transpose pair (3,1)^T = (2,1,1): {pair_transpose}"
          f"   unique such pair: {unique_pair}")
    print(f"  slot space dim = #SYT(2,2) = 2: {slot_dim_ok}")
    print(f"  dim_q V_(2,2) = [4]/[2] = q^2 + q^-2: {d22_ok}")
    print(f"  dim_q V_(3,1) = dim_q V_(2,1,1) = [3]_q: {carriers_eq and carriers_3q}")
    print()
    print("  SELECTION (conditional on conj:e-hartree-categorical-derivation):")
    print("    EM     <-> scalar self-dual block (2,2); minimal reaching")
    print("               insertion = the transpose PAIR -> 1/alpha_EM = q[9][10]")
    print("    strong <-> single-carrier channel (2,1,1), T_{2,9}, h[9]_q")
    print("    weak   <-> single-carrier channel (3,1),   T_{3,5}, h[10]_q")
    print()
    print(f"  invariant product identity (exact in R): "
          f"(q^1/2 [9])(q^1/2 [10]) = q[9][10]: {product_ok}")
    print(f"    => alpha_s * alpha_W = alpha_EM  (split q^1/2|q^1/2 = CONVENTION)")
    print(f"  reference values at q0 (NOT compared to experiment):")
    print(f"    q^1/2[9]_q  = {mp.nstr(v_s, 12) if HAVE_MP else v_s}")
    print(f"    q^1/2[10]_q = {mp.nstr(v_w, 12) if HAVE_MP else v_w}")
    print(f"    q[9][10]    = {mp.nstr(v_em, 12) if HAVE_MP else v_em}")

    w.set_description(
        "Per-force SELECTION rule for the alpha_{basis-knot} family, "
        "conditional on conj:e-hartree-categorical-derivation (owner-directed "
        "continuation of alpha_k_per_force_assembly.py OPEN scope).  Exact "
        "combinatorial spine: (2,2) is the UNIQUE self-transpose partition of "
        "4 (the scalar/antipode-closed block; Schur-Weyl dual of the 2-dim "
        "unit-multiplicity slot space, dim_q = [4]/[2] = q^2+q^{-2}); the "
        "carrier intertwining channels (2,1,1) [T_{2,9}, h[9]_q] and (3,1) "
        "[T_{3,5}, h[10]_q] form the unique transpose-dual pair, each with "
        "dim_q = [3]_q.  Conditional rule: universal/scalar coupling requires "
        "the self-dual block, reachable minimally by the carrier PAIR (hence "
        "EM = pair coupling, 1/alpha_EM = q[9][10], established); the two "
        "single-carrier channels are the two short-range forces (strong = "
        "(2,1,1), weak = (3,1)), short-range BECAUSE non-self-dual.  Invariant "
        "product identity, exact in R: (q^{1/2}[9])(q^{1/2}[10]) = q[9][10], "
        "i.e. alpha_s * alpha_W = alpha_EM under the symmetric split "
        "(CONVENTION pending pole-order derivation; the product is the "
        "invariant).  NO comparison to measured running couplings (fishing "
        "gate: archimedean functor for non-scalar channels underived)."
    )
    w.set_content_block("prop:force-carrier-intertwining-correspondence")
    w.add_data("q0", str(q0))
    w.add_data("selection", {
        "EM": {"block": "(2,2) self-transpose scalar", "mediator": "pair "
               "(T_{2,9}, T_{3,5})", "inv_alpha": "q[9]_q[10]_q (established)"},
        "strong": {"block": "(2,1,1)", "mediator": "T_{2,9}",
                   "decoration": "h[9]_q",
                   "inv_alpha_conditional": "q^{1/2}[9]_q (split=convention)"},
        "weak": {"block": "(3,1)", "mediator": "T_{3,5}",
                 "decoration": "h[10]_q",
                 "inv_alpha_conditional": "q^{1/2}[10]_q (split=convention)"},
    })
    w.add_data("reference_values_at_q0", {
        "q_half_9q": str(v_s), "q_half_10q": str(v_w), "q_9q_10q": str(v_em),
    })
    w.add_assertion(
        "(2,2) is the unique self-transpose partition of 4 (scalar block)",
        computed=bool(scalar_unique), expected=True,
        source="transpose combinatorics, exact",
    )
    w.add_assertion(
        "carrier channels (3,1), (2,1,1) are the unique transpose-dual pair",
        computed=bool(pair_transpose and unique_pair), expected=True,
        source="prop:force-carrier-intertwining-correspondence channels",
    )
    w.add_assertion(
        "slot space dim 2 = #SYT(2,2) (Schur-Weyl identification)",
        computed=bool(slot_dim_ok), expected=True,
        source="hook-length formula; matches Catalan(2) ladder probe",
    )
    w.add_assertion(
        "dim_q V_(2,2) = [4]_q/[2]_q = q^2 + q^{-2} (exact)",
        computed=bool(d22_ok), expected=True, source="hook-length q-dims",
    )
    w.add_assertion(
        "dim_q V_(3,1) = dim_q V_(2,1,1) = [3]_q (exact; equal-carrier weights)",
        computed=bool(carriers_eq and carriers_3q), expected=True,
        source="hook-length q-dims; Frobenius self-duality of the pair",
    )
    w.add_assertion(
        "invariant product identity (q^{1/2}[9])(q^{1/2}[10]) = q[9][10] in R",
        computed=bool(product_ok), expected=True,
        source="exact symbolic; alpha_s * alpha_W = alpha_EM (conditional)",
    )
    w.add_data(
        "finding",
        "Conditional selection rule derived: EM = the transpose-PAIR coupling "
        "into the unique self-dual scalar block (2,2); strong/weak = the two "
        "single-carrier transpose channels ((2,1,1) h[9]_q / (3,1) h[10]_q), "
        "short-range because non-self-dual.  Invariant: alpha_s * alpha_W = "
        "alpha_EM exactly in R under any split of the q-prefactor; the "
        "symmetric q^{1/2} split is convention pending the pole-order "
        "derivation (prop:alpha-em-shift-multiplicative-chain primitive).  "
        "Falsifiable once the archimedean functor for non-scalar channels is "
        "derived; until then NO experimental comparison (running-coupling "
        "scheme dependence)."
    )
    w.save()
    print("\nDone. Witness saved (alpha-k-selection-rule-conditional).")


if __name__ == "__main__":
    main()
