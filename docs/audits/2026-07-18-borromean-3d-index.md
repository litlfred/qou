# The 3D-index of the Borromean rings complement I_𝓑₃ — computed and self-tested (2026-07-18)

**Tier:** executes idea **B1** of
[`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md),
standing on the validated 4₁ machinery of
[`2026-07-18-figure-eight-3d-index-closed.md`](2026-07-18-figure-eight-3d-index-closed.md)
and the triality pin
[`2026-07-18-tetrahedron-index-triality-pin.md`](2026-07-18-tetrahedron-index-triality-pin.md).
Audit-only; scope-(a); comparison-only; **no fit; nothing wired**. Deliberately **no**
comparison to F_Bor / tr_M / ρ(𝓑₃) / masses in this probe — no canonical bridge from
index coefficients to the QOU density objects has been derived, and none is fitted.

## Result

The 3D-index of the Borromean rings complement (the nucleon carrier 𝓑₃), exact integer
q-series at trivial peripheral class, **all four self-tests green** (probe
[`borromean_3d_index.py`](../../computations/probes/borromean_3d_index.py) + witness):

$$I_{\mathcal B_3}(0) = 1 + 13q^2 - 16q^3 - 97q^4 + 16q^5 + 586q^6 + 992q^7 - 514q^8 - 5600q^9 - 11451q^{10} + \cdots$$

i.e. coefficients `[1, 0, 13, -16, -97, 16, 586, 992, -514, -5600, -11451]` for
q⁰…q¹⁰. Notable graded structure: the **q¹ coefficient vanishes** (the 4₁ index has
−2q there), and no half-integer powers appear at integral peripheral class. Nonzero
peripheral classes (to q⁶, exact):

| orbit b | series |
|---|---|
| µ_h (any single meridian) | `[0, 0, 8, -16, -64, 48, 464]` = 8q² − 16q³ − 64q⁴ + 48q⁵ + 464q⁶ + … |
| µ_h + λ_h | `[0, 0, 0, -8, 8, 64, 96]` = −8q³ + 8q⁴ + 64q⁵ + 96q⁶ + … |

This is, per the B1 idea audit's literature grep, the first computation of this
invariant in the corpus and apparently in the cited literature. Wall time: ~90 s
total (2415 lattice vectors for q¹⁰; log `/tmp/borromean_index.log`).

## Well-definedness (primary sources, not guessed)

- SnapPy `Manifold('L6a4')` (Borromean rings complement): 8 ideal tetrahedra, 3 cusps,
  solution type *all tetrahedra positively oriented*, volume 7.327724753 = 2·Vol(octahedron)
  — the arguments of the positively-oriented geometric shapes give a **strict angle
  structure**, hence the triangulation is **1-efficient** (GHRS arXiv:1303.5278 Thm 1.5 +
  Rmk 1.6), hence the index is **well-defined** (Thm 1.2 + Thm 1.1(a)); Rmk 1.10 covers all
  link complements in S³. Gluing data taken from `M.gluing_equations()` — the exact matrix
  GHHR §3.1 says is the gluing matrix (no hand-transcription).
- **General gluing formula** (GHHR arXiv:1604.02688 §4, eq 15/16): for n tetrahedra, r cusps,
  $$I_T(b)(q) = \sum_{k\in\mathbb Z^{n-r}} q^{\sum_i k_i}\ \prod_{j=1}^{n} J_\Delta\bigl(a_j(k,b),\,b_j(k,b),\,c_j(k,b)\bigr),$$
  charges = the tetrahedron-j entries of $\sum_i k_i E_i + \sum_h (p_h M_h + q_h L_h)$
  (edge rows + peripheral rows), $b=(p_1,q_1,p_2,q_2,p_3,q_3)\in H_1(\partial M;\mathbb Z)=\mathbb Z^6$.
- **Sublattice choice** (GHRS §4.5 eq 17 + §4.6 Thm 4.3 / Rmk 4.4 / Rmk 4.6): the r = 3
  excluded edges must leave the remaining n−r = 5 Neumann–Zagier edge rows an **integer
  basis** of the NZ row lattice Λ. The probe enforces this *directly by integer linear
  algebra* (each excluded row solved as an integer combination of the kept rows; NZ rank
  = n−r asserted; Σᵢ Eᵢ = 0 asserted), rather than trusting a hand-picked tree.
  Selected basic edges for L6a4: `[3, 4, 5, 6, 7]` (excluded `[0, 1, 2]`).
- **Finiteness per order:** each summand's minimum q-degree
  $D(k) = \sum_i k_i + \tfrac12\sum_j \nu_j(k)$ is exact ($J_\Delta$ has leading
  coefficient ±1 with min Q-degree $\nu = AB - m$), so the ℤ⁵ sum truncates finitely per
  order; enumeration over ℓ∞ shells with a 3-consecutive-empty-shell stopping rule.

## Validation ladder (all gates before the 𝓑₃ run)

1. **Kernel preflight** — reflection triality $I_\Delta(m,e)=I_\Delta(-e,-m)$, full S₃
   invariance of $J_\Delta$, and the eq-6 leading term $q^{AB/2}$, all checked exactly on
   the series — green.
2. **m004 general-machinery check** — the *general* n,r implementation rebuilt the
   figure-eight index from SnapPy's **own** `m004` gluing rows (which differ from GHHR
   Ex 4.1's table in quad + peripheral conventions) and matched
   [`figure_eight_3d_index.py`](../../computations/probes/figure_eight_3d_index.py)
   **exactly to q¹⁰ on 4 peripheral classes** ((0,0), (µ), (2µ), (λ)), sign map (1,1)
   on every class — green.

## Self-tests (4/4 green)

| # | test | source | result |
|---|---|---|---|
| i | genuine power series (no negative q-powers) | GHHR Cor 10.21 (1-efficiency) | **pass** (also no half-integer powers at integral b) |
| ii | constant term 1 | GHHR normalization | **pass** |
| iii | S₃ cusp-permutation symmetry of I_𝓑₃(b) | Borromean component symmetry | **pass, direct equality** (no orientation-flip fallback needed) on both nonzero orbits {µ₁,µ₂,µ₃} and {µ₁+λ₁, µ₂+λ₂, µ₃+λ₃} to q⁶ |
| iv | triangulation independence (2–3 moves) | GHRS Thm 1.1(b) | **pass** — SnapPy randomized retriangulation (8 tets, positively oriented, first attempt), I(0) reproduced exactly to q⁶ |

Implementation notes recorded for the next consumer: (1) the per-summand minimum
q-degree D(k) is *exact* (J_Δ leading coefficients are ±1), so the truncation is a
theorem-level bound, not a heuristic; (2) for L6a4 the shell minimum degree grows
**linearly** in the ℓ∞ radius (Dmin(shell R) = 2R empirically), not quadratically —
the B1 idea entry's quadratic guess was wrong in the flat directions — so shells stay
populated up to R ≈ N for order q^N and the enumeration must be vectorized (numpy);
2415 admissible vectors for q¹⁰, stop radius 13 with a 3-consecutive-empty-shell rule.

## Files

- Probe: [`computations/probes/borromean_3d_index.py`](../../computations/probes/borromean_3d_index.py)
- Witness: [`computations/probes/borromean-3d-index.witness.json`](../../computations/probes/borromean-3d-index.witness.json)
- Log: `/tmp/borromean_index.log` (ephemeral)

## What this does and does not claim

- **Does:** produce the first exact integer-graded 3D-index data for the nucleon carrier
  𝓑₃ in the corpus (and, per the B1 idea audit's 0/7 grep, apparently absent from the
  cited literature), with the ℤ⁶ peripheral grading available as per-cusp quantum numbers,
  on a machine-verified GHRS-compliant basis choice.
- **Does not:** relate any coefficient to F_Bor, ρ(𝓑₃), the 2.89 % m_p gap, or any
  observable. That bridge is open math; deriving it (not fitting it) is the follow-on.
  Per the (a)/(b) discipline this audit records *computed values and passed self-tests
  only* — no refutations, no open-item declarations beyond the bridge already tracked in
  the B1 idea entry.
