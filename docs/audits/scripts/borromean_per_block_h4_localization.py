#!/usr/bin/env python3
"""
Borromean per-block H_3(q) character check — h^4 lives EXCLUSIVELY in the (2,1) block.

Complement to the (sibling) combinatorial branching verifier in this directory
(`s5so3_branching_backbone_verify.py`), which establishes the Res^{S5}_{S3}
branchings + S5->A5 indexing.  That script shows the standard (2,1) irrep of S_3
is the load-bearing target block.  THIS script closes the last link the branching
alone does not: that the Borromean h^4 = -3/4 coefficient sits in the (2,1) block
*and nowhere else*, by evaluating all three H_3(q) Wedderburn blocks on the
Borromean braid b = (s1^{-1} s2)^3:

    chi^{(3)}(b)     = 1                  (1-dim trivial, sigma_i -> q)
    chi^{(1,1,1)}(b) = 1                  (1-dim sign,    sigma_i -> -q^{-1})
    chi^{(2,1)}(b)   = 2 - 3 h^4 - h^6    (2-dim standard; h = q - q^{-1})

Both 1-dimensional blocks evaluate to the CONSTANT 1 (no h-dependence), so every
power of h in tr_M(b) -- in particular h^4 -- comes from the (2,1) block alone.

Cross-references (this is an independent re-derivation, not new content):
  - branching: ./s5so3_branching_backbone_verify.py (sibling) + Lean
    QOU/BraidsAndKnots/S5SO3FiberAction.lean (s5_to_s3_restriction_mults,
    restriction_functor_yields_h4_irrep, native_decide/decide, sorry-free).
  - chi^{(2,1)} closed form: GAP-A-4 T15 probe
    (computations/probes/gap_a4_T15_character_polynomial_probe.py).

The 2x2 standard rep is built from scratch and its braid + Hecke relations are
self-checked; the character (matrix trace) is basis-invariant, so no Markov
normalisation convention enters.  q=1 / classical backbone only.
"""
import sympy as sp


def per_block_chars():
    q = sp.symbols("q", nonzero=True)
    h = q - 1 / q

    # 1-dim blocks on s1^{-1} s2, cubed:
    triv = (1 / q * q) ** 3            # trivial: s_i -> q          => 1
    sign = ((-q) * (-1 / q)) ** 3      # sign:    s_i -> -q^{-1}     => 1

    # 2-dim standard (2,1): eigenvalues {q, -1/q}; solve braid relation for the
    # single off-diagonal, then self-check both relations.
    b = sp.symbols("b")
    s1 = sp.Matrix([[q, 1], [0, -1 / q]])
    s2 = sp.Matrix([[-1 / q, 0], [b, q]])
    braid = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2)
    sol = sp.solve([sp.numer(sp.together(e)) for e in braid if e != 0], b, dict=True)
    bval = [s[b] for s in sol if s[b] != 0][0]
    s1, s2 = s1.subs(b, bval), s2.subs(b, bval)

    hecke_ok = (sp.simplify(s1 * s1 - (h * s1 + sp.eye(2))) == sp.zeros(2)
                and sp.simplify(s2 * s2 - (h * s2 + sp.eye(2))) == sp.zeros(2))
    braid_ok = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2)

    chi21 = sp.simplify(sp.trace((s1.inv() * s2) ** 3))
    chi21_target = sp.expand(2 - 3 * h**4 - h**6)
    chi21_ok = sp.simplify(sp.expand(chi21) - chi21_target) == 0
    return sp.simplify(triv), sp.simplify(sign), chi21, chi21_target, hecke_ok, braid_ok, chi21_ok


def main():
    triv, sign, chi21, target, hecke_ok, braid_ok, chi21_ok = per_block_chars()
    checks = [
        ("braid relation holds (2-dim std rep)", bool(braid_ok)),
        ("Hecke relation holds (2-dim std rep)", bool(hecke_ok)),
        ("chi^{(3)}(b) == 1  (no h-dependence)", triv == 1),
        ("chi^{(1,1,1)}(b) == 1  (no h-dependence)", sign == 1),
        ("chi^{(2,1)}(b) == 2 - 3 h^4 - h^6", bool(chi21_ok)),
    ]
    print("=== Borromean per-block H_3(q) characters, b = (s1^{-1} s2)^3 ===")
    print(f"  chi^(3)      = {triv}")
    print(f"  chi^(1,1,1)  = {sign}")
    print(f"  chi^(2,1)    = {sp.expand(chi21)}   (target 2 - 3 h^4 - h^6)")
    print()
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    allok = all(ok for _, ok in checks)
    print()
    print("CONCLUSION: both 1-dim blocks are the constant 1, so h^4 (indeed every")
    print("h^k, k>=1) in tr_M(b) lives EXCLUSIVELY in the (2,1) block.  PASS:", allok)
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
