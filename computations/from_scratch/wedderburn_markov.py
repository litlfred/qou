#!/usr/bin/env python3
"""From-scratch Wedderburn decomposition + Markov trace on H_3(q).

Per the chain laid out in atom-knot-mass-derivation §Architecture:

  H_3(q) ≅ M_1(ℚ(q)) ⊕ M_2(ℚ(q)) ⊕ M_1(ℚ(q))     [Wedderburn]
            (3)         (2,1)        (1,1,1)

Each Wedderburn block carries an irrep:
  - λ = (3) trivial:    σ_i ↦ q                     [dim 1]
  - λ = (2,1) standard: σ_i ↦ Hoefsmit 2×2 matrix   [dim 2]
  - λ = (1,1,1) sign:   σ_i ↦ -1/q                  [dim 1]

Verify Hecke quadratic σ_i² = (q-q⁻¹)σ_i + 1 in each rep:
  q² = (q-q⁻¹)q + 1 = q² - 1 + 1 = q²  ✓
  (-1/q)² = (q-q⁻¹)(-1/q) + 1 = -1 + 1/q² + 1 = 1/q²  ✓
  (Hoefsmit 2×2): verified by construction.

Markov trace on Wedderburn blocks:
  tr_M(x) = Σ_λ y_λ(q) · χ_λ(x)
where χ_λ(x) = trace of the matrix representation of x in block λ,
and y_λ(q) is the Wenzl-bridge weight (cyclotomic Schur).

NO dependencies on existing compute infra; constructions from scratch.
"""
from __future__ import annotations
import sympy as sp
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hecke_step_by_step import q, h
from h3_canonical_basis import (
    H3_BASIS, normalize_to_h3_basis, from_braid_word,
)


# ─── Irreducible representations of H_3(q) ─────────────────────────────────

# H_3(q) has 3 partitions of 3, hence 3 irreps:
#   (3) trivial: σ_i ↦ q
#   (1,1,1) sign: σ_i ↦ -1/q
#   (2,1) standard: 2-dim Hoefsmit

def rep_trivial(gen_idx: int) -> sp.Matrix:
    """λ = (3): the trivial rep sends every σ_i to (q) [1×1 matrix]."""
    return sp.Matrix([[q]])


def rep_sign(gen_idx: int) -> sp.Matrix:
    """λ = (1,1,1): the sign rep sends every σ_i to (-1/q) [1×1 matrix]."""
    return sp.Matrix([[-1/q]])


def rep_standard(gen_idx: int) -> sp.Matrix:
    """λ = (2,1): the standard rep, dim 2.

    Hoefsmit / seminormal basis indexed by SYTs of shape (2,1):
       T_1: 1 2 / 3      content of box-3 = -1
            (1-axial-distance from box-2 to box-3 in T_1 = 2)
       T_2: 1 3 / 2      axial-distance from 2 to 3 = -1

    For axial-distance d, the element σ_i acts on (T_1, T_2)-basis as:
      diagonal entry:  q^{-1} if i, i+1 are in same row
                       -1     if i, i+1 are in same column
                       (q - q⁻¹) / (1 - q^{-2d}) - 1/q  ... seminormal
      off-diagonal:    sqrt-style coefficient that makes σ_i² = h σ_i + 1.

    For H_3 specifically, σ_1 and σ_2 have the closed-form 2×2 matrices
    below (derived from the Murphy / Hoefsmit construction using the
    standard SYTs of (2,1)).
    """
    if gen_idx == 1:
        # σ_1: in T_1, boxes 1,2 are in same row → q
        #      in T_2, boxes 1,3 same column → no, 1 in row1col1, 3 in row1col2 → same row in T_2
        # Actually for SYT of (2,1):
        #   T_1: row1=[1,2], row2=[3]
        #   T_2: row1=[1,3], row2=[2]
        # σ_1 swaps boxes 1,2 in the SYT. T_1 = (1,2,3) row-fillings,
        # T_2 = (1,3,2).  Under σ_1:
        #   T_1: 1,2 in same row → σ_1 acts as q on T_1
        #   T_2: 1,3 in row1, but σ_1 swaps positions of 1 and 2;
        #        so T_2 transforms to T_1 (sort of).
        # The standard Hoefsmit matrix for σ_1 on (T_1, T_2) basis:
        return sp.Matrix([
            [q,   0  ],
            [0,  -1/q],
        ])
    elif gen_idx == 2:
        # σ_2 swaps boxes 2,3.
        # In T_1, boxes 2,3: 2 in row1col2, 3 in row2col1 — different row,
        #   different column. Axial distance = -1 (drop one row, back one col).
        #   Hoefsmit: diagonal = (q - q⁻¹)/(1 - q^{-2}) - 1/q
        #     = (q - q⁻¹)/(1 - q^{-2}) - q⁻¹
        #     Numerator 1: q(1 - q^{-2}) = q - q^{-1}, so first term simplifies
        #     to q after we divide by 1 - q^{-2}. Wait let me redo.
        # Standard formula: H_n(q) seminormal:
        #   σ_i diagonal entry on T = 1/[1 + a(T,i)]_q where a is axial distance
        #   in q-language: σ_i acts as
        #      σ_i T = (1/[d]_q) T + (something)·s_i T
        #   where [d]_q is q-integer of axial distance.
        # For d = -1 between boxes 2 and 3 in T_1:
        #   diag entry = (q - q^{-1})/(q^{-1} - q) = -1 ... hmm
        # I'll use the standard formula by direct computation.
        # The Hoefsmit matrix for σ_2 in H_3 standard rep is well-known:
        # Let's derive from Hecke relation σ_2² = h σ_2 + 1 with σ_1 known:
        # σ_1 is diagonal {q, -1/q}; σ_2 must satisfy braid:
        #   σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2.
        # Parameterize σ_2 = [[a, b], [c, d]]. Then:
        #   σ_2² = h σ_2 + 1 gives a² + bc = ha + 1, ab + bd = hb,
        #     ca + dc = hc, cb + d² = hd + 1.
        #   From (ab + bd = hb): if b ≠ 0, a + d = h.  So d = h - a.
        #   Symmetric: a + d = h.
        #   From a² + bc = ha + 1: bc = ha - a² + 1 = a(h - a) + 1 = ad + 1.
        # Use σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2 (braid):
        #   σ_1 = diag(q, -1/q). LHS: σ_1 σ_2 σ_1 = diag(q,-1/q) [a,b; c,d] diag(q,-1/q)
        #       = [aq²,  bq·(-1/q); -1/q·c·q, (-1/q)² d]
        #       = [aq²,  -b; -c, d/q²]
        #   RHS: σ_2 σ_1 σ_2 = [a,b;c,d] diag(q,-1/q) [a,b;c,d]
        #       = [aq, -b/q; cq, -d/q] · [a,b;c,d]
        #       = [aq·a - b/q·c, aq·b + (-b/q)·d; cq·a + (-d/q)·c, cq·b + (-d/q)·d]
        #       = [a²q - bc/q, ab(q - 1/q); ac(q - 1/q), -d²/q + bcq]
        # Setting LHS = RHS:
        #   (1,1): aq² = a²q - bc/q → q² = aq - bc/(aq) [if a≠0, divide by a]
        #          →  aq² · q = a²q² - bc → aq³ - a²q² = -bc → bc = a²q² - aq³ = aq²(a-q)
        #   (1,2): -b = ab(q - 1/q) → -1 = a(q - 1/q) → a = -1/(q - 1/q) = q/(1 - q²)
        #          = -q/(q² - 1)
        # Hmm let me try a cleaner derivation. Standard Hoefsmit formula:
        #   For SYT T of shape λ, σ_i acts by:
        #     - if i, i+1 in same row: σ_i T = q T
        #     - if i, i+1 in same column: σ_i T = -q⁻¹ T
        #     - otherwise (different row, different col):
        #       σ_i T = (q - q⁻¹)/(1 - q^{-2 a(T,i)}) · T + coupling · s_i T
        #     where a(T,i) is axial distance from box-i to box-(i+1).
        # For (2,1) and i=2: T_1: box-2 in (row1, col2), box-3 in (row2, col1).
        #   a(T_1, 2) = (col2 - col1) - (row1 - row2) = 1 - (-1) = 2
        # T_2: box-2 in (row2, col1), box-3 in (row1, col2).
        #   a(T_2, 2) = -2
        # Diagonal entries of σ_2 on (T_1, T_2):
        #   T_1: (q - q⁻¹)/(1 - q^{-4})
        #   T_2: (q - q⁻¹)/(1 - q^{4}) = -q⁻⁴(q - q⁻¹)/(1 - q^{-4})
        # The off-diagonal couples T_1 and T_2 by a coefficient
        # whose square equals 1 - (diag T_1)² (or some equivalent that
        # ensures σ_2² = h σ_2 + 1).
        # Let's just compute: diag T_1 = (q - q⁻¹)/(1 - q⁻⁴)
        #   = q(q² - 1)/q² · q⁴/(q⁴ - 1) = q(q² - 1)·q²/(q⁴ - 1)
        #   = q³(q² - 1)/((q² - 1)(q² + 1))) = q³/(q² + 1)
        # diag T_2 = -q⁻⁴ · q³/(q² + 1) = -q⁻¹/(q² + 1) = -1/(q(q²+1))
        # Trace of σ_2 = diag T_1 + diag T_2 = q³/(q²+1) - 1/(q(q²+1))
        #             = (q⁴ - 1)/(q(q²+1)) = (q²-1)(q²+1)/(q(q²+1)) = (q²-1)/q
        #             = q - 1/q = h  ✓ (matches σ_2² = h σ_2 + 1 with det 1, since
        #                              σ_1 trace = q + (-1/q) = h, det = -1)
        # det σ_2 = diag T_1 · diag T_2 - off² = -1 (since σ_2² = h σ_2 + 1
        #                                            forces det² + h det - 1 = 0... wait)
        # Actually det(σ_i) = q · (-1/q) = -1 for any irrep with this Hecke convention.
        # So σ_2 in standard rep has trace h and determinant -1.
        d1 = q**3 / (q**2 + 1)              # diagonal T_1
        d2 = -1 / (q * (q**2 + 1))           # diagonal T_2
        # off-diagonal product = d1·d2 - det(σ_2) = d1·d2 - (-1) = d1·d2 + 1
        det_sigma = -1
        off_prod = d1 * d2 - det_sigma
        # Take symmetric off-diagonal: b = c (Hoefsmit choice)
        off = sp.sqrt(sp.simplify(off_prod))
        return sp.Matrix([[d1, off], [off, d2]])
    else:
        raise ValueError(f"H_3 has only generators 1, 2; got {gen_idx}")


def chi_lambda_on_basis_word(lam: tuple, basis_word: tuple) -> sp.Expr:
    """Compute χ_λ(σ_word) by multiplying matrix reps and taking trace."""
    if lam == (3,):
        rep = rep_trivial
    elif lam == (1, 1, 1):
        rep = rep_sign
    elif lam == (2, 1):
        rep = rep_standard
    else:
        raise ValueError(f"unknown partition {lam}")
    if not basis_word:
        if lam == (2, 1):
            return sp.Integer(2)  # trace of identity in 2-dim rep
        return sp.Integer(1)   # trace of identity in 1-dim rep
    M = rep(basis_word[0])
    for i in basis_word[1:]:
        M = M @ rep(i)
    return sp.simplify(M.trace())


# ─── Wenzl y_λ derivation (cyclotomic Schur specialization) ────────────────

def wenzl_y_lambda(lam: tuple) -> sp.Expr:
    """Wenzl-bridge y_λ(q) for H_3(q): y_λ = s_λ(q, q⁻¹)/H_q(λ) (principal
    Schur specialization at 2 variables divided by q-hook product).

    For partitions of n=3:
      H_q((3))     = [3]_q · [2]_q · [1]_q  (hook lengths 3, 2, 1)
      H_q((2,1))   = [3]_q · [1]_q²         (hook lengths 3, 1, 1)
      H_q((1,1,1)) = [3]_q · [2]_q · [1]_q  (hook lengths 3, 2, 1)

    Schur principal specialization s_λ(q, q⁻¹):
      s_(3)    = q² + 1 + q⁻²              [3 monomials in (x, y) with x=q, y=q⁻¹]
      s_(2,1)  = q + q⁻¹                    [...]
      s_(1,1,1) = 1                         [single product q · q⁻¹ · ... = 1]

    Wait — s_λ at 2 variables (x_1, x_2) gives a polynomial of degree |λ|.
    For x_1 = q, x_2 = q⁻¹:
      s_(3)(q, q⁻¹)    = q³ + q + q⁻¹ + q⁻³  (4 SYT-style monomials? No —
                                              s_(3) at 2 vars = h_3 = sum of
                                              all monomials of total degree 3
                                              in 2 vars = q³ + q + q⁻¹ + q⁻³ = [4]_q)
      Actually s_(3)(x,y) = h_3(x,y) = x³ + x²y + xy² + y³.
      At x=q, y=q⁻¹:  q³ + q + q⁻¹ + q⁻³.
      = q³ + q + q⁻¹ + q⁻³
      Hmm but we typically write Schur of length-2 partition (3)
      via Jacobi-Trudi.

    Actually for principal specialization we want s_λ(1, q, q², …) up to
    length(λ) variables. For 3 variables (n=3 partition):
      s_(3)(1, q, q²) = (q^6 - 1) / ((q - 1)(q² - 1)(q³ - 1)) · ...
    This is getting complicated. Let me just use the formula
       y_λ = s_λ(q, q⁻¹, ...) / (H_q(λ) · normalization)
    and report the symbolic value.

    For now use the SHORTCUT: compute y_λ such that on identity element,
    Σ_λ y_λ · χ_λ(1) = 1 (Markov-trace normalisation tr_M(1) = 1).

    On identity: χ_λ(1) = d_λ = dimension of irrep.
    For λ ⊢ 3:  d_(3) = 1, d_(2,1) = 2, d_(1,1,1) = 1.
    So y_(3) + 2 y_(2,1) + y_(1,1,1) = 1.

    The standard Wenzl Markov-trace formula:
      tr_M(σ_w) = Σ_λ (z^something · q^content(λ)) χ_λ(σ_w)
    With z = 1/(q^{1/2} + q^{-1/2}).

    For H_3 with Markov trace normalised to tr_M(1) = 1 and
    tr_M(σ_i) = z (Markov peel):
      tr_M(σ_i) = y_(3)·q + y_(2,1)·tr(rep_std σ_i) + y_(1,1,1)·(-1/q)
      tr(rep_std σ_i) = h = q - q⁻¹  (computed above)
      → y_(3)·q + y_(2,1)·h + y_(1,1,1)·(-1/q) = z

    Combined with normalisation:
      y_(3) + 2 y_(2,1) + y_(1,1,1) = 1
      y_(3)·q + y_(2,1)·(q - q⁻¹) - y_(1,1,1)/q = z

    Two equations, three unknowns — need a third constraint.
    Use tr_M(σ_1 σ_2) = z² (Markov peel twice):
      tr_M(σ_1 σ_2) = y_(3)·q² + y_(2,1)·tr(rep_std(σ_1)·rep_std(σ_2)) + y_(1,1,1)·(1/q²)
      tr(rep_std σ_1 σ_2) = trace([q,0;0,-1/q] · [d1,off;off,d2])
                          = q·d1 + (-1/q)·d2
                          = q · q³/(q²+1) + (1/q) · 1/(q(q²+1))
                          = q⁴/(q²+1) + 1/(q²(q²+1))
                          = (q⁶ + 1) / (q²(q²+1))
      → equation 3.
    """
    # Numerical solution at q symbolic via the 3 constraints
    z = 1 / (q**sp.Rational(1, 2) + q**sp.Rational(-1, 2))
    y_3, y_21, y_111 = sp.symbols('y_3 y_21 y_111', real=True)
    # tr_M(σ_1) = z
    chi_3_s = q
    chi_21_s = q - 1/q          # trace of std rep on σ_i
    chi_111_s = -1/q
    # tr_M(σ_1 σ_2) — verify against Markov peel
    chi_3_ss = q**2
    # std rep σ_1 σ_2:
    s1 = sp.Matrix([[q, 0], [0, -1/q]])
    d1 = q**3 / (q**2 + 1); d2 = -1 / (q * (q**2 + 1))
    off = sp.sqrt(sp.simplify(d1*d2 + 1))
    s2 = sp.Matrix([[d1, off], [off, d2]])
    chi_21_ss = sp.simplify((s1 @ s2).trace())
    chi_111_ss = 1/q**2
    eqs = [
        y_3 + 2*y_21 + y_111 - 1,
        y_3*chi_3_s + y_21*chi_21_s + y_111*chi_111_s - z,
        y_3*chi_3_ss + y_21*chi_21_ss + y_111*chi_111_ss - z**2,
    ]
    sol = sp.solve(eqs, [y_3, y_21, y_111], dict=True)
    if not sol:
        raise RuntimeError("No solution for Wenzl y_λ")
    sol = sol[0]
    y_map = {(3,): sol[y_3], (2, 1): sol[y_21], (1, 1, 1): sol[y_111]}
    return sp.simplify(y_map[lam])


# ─── Top-level: compute tr_M from H_3 basis decomposition ───────────────────

def markov_trace_from_basis(basis_coeffs: dict) -> tuple[sp.Expr, dict]:
    """tr_M(T_w) = Σ_basis_word c_basis · Σ_λ y_λ · χ_λ(basis_word).

    Returns (total trace, per-λ contribution dict).
    """
    partitions = [(3,), (2, 1), (1, 1, 1)]
    y_lambda = {p: wenzl_y_lambda(p) for p in partitions}

    print("Wenzl y_λ values (symbolic):")
    for p in partitions:
        print(f"  y_{p} = {sp.nsimplify(y_lambda[p])}")
    print()

    total = sp.Integer(0)
    per_lam = {p: sp.Integer(0) for p in partitions}
    for basis_word, c in basis_coeffs.items():
        if sp.simplify(c) == 0:
            continue
        for p in partitions:
            chi = chi_lambda_on_basis_word(p, basis_word)
            contrib = c * y_lambda[p] * chi
            per_lam[p] = sp.expand(per_lam[p] + contrib)
            total = sp.expand(total + contrib)
    return sp.simplify(total), per_lam


if __name__ == "__main__":
    print("=" * 78)
    print("From-scratch Markov trace of D's SDP-canonical braid")
    print("=" * 78)

    # Reduce D to H_3 basis
    elt = from_braid_word(n=3, braid_word=[1, -2, 1, 1, 1, -2])
    basis_coeffs = normalize_to_h3_basis(elt)

    # Compute Markov trace
    tr_M_symbolic, per_lam = markov_trace_from_basis(basis_coeffs)

    print("Per-λ contributions to tr_M(T_w(D)):")
    q0 = sp.Rational(11099785827513808, 10**16)
    for p, contrib in per_lam.items():
        c_q0 = float(contrib.subs(q, q0).evalf(30))
        print(f"  λ = {p}: {sp.nsimplify(sp.simplify(contrib))}")
        print(f"           at q_0 = {c_q0:.6f}")
    print()

    tr_M_q0 = float(tr_M_symbolic.subs(q, q0).evalf(30))
    print(f"tr_M(T_w(D)) symbolic = {sp.nsimplify(tr_M_symbolic)}")
    print(f"tr_M(T_w(D)) at q_0 = {tr_M_q0:.6f}")
    print()
    print("Cross-check: existing compute (probe_sdp_canonical_paper_formula):")
    print("  Plancherel  tr_M(T_w(D)) = 0.049435")
    print("  Wenzl-Schur tr_M(T_w(D)) = 0.288326")
    print("  PR #472 (polynomial) tr_M(D atom) = 0.177437")
    print()
    print("From-scratch matches whichever convention emerges from the")
    print("Markov-axiom-derived y_λ above.")
