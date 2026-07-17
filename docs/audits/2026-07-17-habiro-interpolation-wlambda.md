# Habiro interpolation of the folded fibre boundary data — the W_λ keystone

**Date:** 2026-07-17 · **Axis:** s5-so3 keystone geometric `W_λ` (1ppQ front 2 —
m_p/m_μ root cause; Subgoal-2, open for all) · **Branch:**
`claude/habiro-interpolation-wlambda-2026-07-17` (stacked on
[#3822](https://github.com/litlfred/qou/pull/3822), the LR modulus identification) ·
**No fit; no constant wired; the geometric `W_λ` gate is NOT closed.**

## The problem (formalize-first)

The keystone's observable is `W_λ = |S_{0λ}|² = d_q(λ)²/D(q)²`, the q-Plancherel /
Verlinde measure that the μ–p mass chain consumes at the substrate `q₀`. The
[fibre-observable audit](2026-07-12-fibre-observable-categorical-not-analytic.md) and the
merged Lean carriers ([`BWVacuumRowHabiroRigidity.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/BWVacuumRowHabiroRigidity.lean),
#3681) reframe the continuation `‖q‖=1 → q₀>1` as **Habiro rigidity**: the observable
`W_λ(q₀)` is the archimedean evaluation `τ_∞` of a **Habiro-ring element** `F_λ(q)` whose
root-of-unity values are the colored-WRT fibre amplitudes. Habiro's injectivity miracle
(carried as the class hypothesis `root_injective`) makes such an element **determined by
sufficient root data — no fit is possible in principle**.

[#3822](https://github.com/litlfred/qou/pull/3822) computed the **boundary data at the
single order-5 fibre root** `ζ = e^{iπ/5}`: the corrected exact identity
`|S_{0λ}^{(m)}| = 2|[mark λ]_{ζ^m}|/D_{Ê₈}(ζ^m)`, Galois-indexed by the flat connection
`m = 1, 2`. **Single-order data does NOT pin a Habiro element** — its strength comes from
**multiple fibre orders**. This PR poses and attacks that:

> **Q.** Is there a single Habiro-ring element `F_λ(q)` — one uniform expression, no
> per-root tuning — whose evaluation at *every* colored-fibre root of Σ(2,3,5) (orders
> 2, 3, 5 and their Galois orbits) reproduces the folded modulus boundary data
> `{|S_{0λ}^{(m,j)}|²}`? If a uniform candidate survives every computed root it is a win
> (consistency, not a fit); a root-dependent fudge refutes the naive candidate (scope-(a)).

### The candidate interpolant

The obvious candidate is the **q-deformed Verlinde measure of the affine-Ê₈ McKay data**:

$$
F_\lambda(q) \;:=\; \frac{[\mathrm{mark}\,\lambda]_q^2}{D(q)^2},
\qquad D(q)^2 = \sum_{\mu\in\text{9 nodes}} [\mathrm{mark}\,\mu]_q^2,
$$

the marks being the `2I` irrep dimensions `1,2,3,4,5,6,4,2,3` (Σ mark² = 120 = |2I|). At a
root ζ this is exactly `d_ζ(λ)²/D(ζ)²`, the Verlinde measure; the `#3822` fold factor
`2/√2` is the `Ê₈`-node vs folded-MTC normalizer `D_{Ê₈}² = 2 D_{MTC}²`. `F_λ(q)` is a
ratio of `ℤ[q,q⁻¹]` elements (a rational-function candidate for the Habiro element, in the
"determined by root values" sense), uniform in λ.

### Why the candidate should interpolate — the structural reason (not a fit)

Σ(2,3,5) has exactly **two** irreducible SU(2) flat connections (`D(2,3,5) = 2`,
Fintushel–Stern), with rotation numbers around the three exceptional fibres
`(p₁,p₂,p₃) = (2,3,5)`:

| flat connection `m` | CS | E₈ exponent `e_m` | `(ℓ₂, ℓ₃, ℓ₅)` |
|---|---|---|---|
| m = 1 | −1/120 | 1 | (1, 1, 1) |
| m = 2 | −49/120 | 7 | (1, 1, 2) |

(`ℓ_j^{(m)} = e_m·(P/p_j) mod p_j`, `P = 30`.) The Lawrence–Rozansky colored flat amplitude
**factorizes**: coloring fibre `j` by the SU(2) color `α` multiplies the color-independent
bare amplitude by the character of the α-dim rep at the flat holonomy,

$$
|A_m^{(j)}(\alpha)| \;=\; |A_m^{(j),\text{bare}}|\cdot\bigl|[\alpha]_{\zeta_{p_j}^{\ell_j^{(m)}}}\bigr|,
\qquad \zeta_{p_j} = e^{i\pi/p_j}.
$$

Because the bare amplitude is color-independent, the **normalized squared amplitude**
(sum-to-1 over the McKay nodes) at fixed `(m,j)` is exactly `[mark]²_ζ / Σ[mark]²_ζ = F_λ(ζ)`
— a **structural identity**, forced by the factorization, not tuned. So the candidate
matches at *every* colored-fibre root with the *same* prescription `[mark]²/Σ[mark]²`; the
normalizer `D(ζ)²` is root-dependent in **value** but uniform in **form**. That is the
uniform-candidate win the question asks for — **if** the amplitude factorization holds at
orders 2 and 3, which this PR verifies numerically.

### The roots probed (the fold changes with r — derived per fibre)

The colored-fibre root at order `p_j` is `ζ_{p_j}^{ℓ_j^{(m)}}`. Because both connections have
`ℓ₂ = ℓ₃ = 1`, the order-2 and order-3 fibres each contribute **one** root; the order-5
fibre contributes **two** (`ℓ₅ = 1, 2`, the Galois pair). Total: **4 nontrivial roots + q=1**.
The affine-Weyl fold differs per root (the `r`-alcove shrinks as `p` shrinks) and is derived,
not assumed from r=5:

| fibre `p_j` | root `ζ` | `2cos(π/p_j)` | alcove | marks `1..6 → [·]_ζ` | `D²=Σ[mark]²` |
|---|---|---|---|---|---|
| 2 | `e^{iπ/2}=i` | 0 | {1} | `1,0,−1,0,1,0` | 4 |
| 3 | `e^{iπ/3}` | 1 | {1,2} | `1,1,0,−1,−1,0` | 6 |
| 5 (m=1) | `e^{iπ/5}` | φ | {1,2,3,4} | `1,φ,φ,1,0,−1` | 10+2√5 |
| 5 (m=2) | `e^{2iπ/5}` | φ−1 | {1,2,3,4} | `1,φ−1,…,0,…` | 10−2√5 |

All characters lie in `ℤ ∪ ℚ(√5)` (order 2, 3 give integers; order 5 gives `ℚ(√5)`), so the
per-root evaluation of `F_λ` is **exact** (zero floats). The amplitude factorization at
orders 2, 3 is verified by the colored Gauss sum (40-dps, parameter-free extraction).

## What this closes / does not close (anti-laundering)

- **Not closed:** the geometric `W_λ` gate, Habiro's injectivity for the actual `z`-Habiro
  ring, and the identification of `F_λ` with the `S³/2I` WRT element. Those remain the open,
  now-in-scope (Subgoal-2) objects; this PR does **not** prove them.
- **Not claimed:** that 4 roots + q=1 *uniquely pin* `F_λ`. Habiro rigidity's uniqueness is
  the class **hypothesis** (`root_injective`); a finite root set constrains, it does not
  prove injectivity. The honest deliverable is *consistency of one uniform candidate with
  every computed root*.
- **The μ–p tension is NOT resolved.** The archimedean `F_λ(q₀)` values are reported as
  *candidates* with cross-pin swing (tiered: consistent-not-identified at best), never wired.

## Results

_(filled after the compute — see `computations/habiro_interpolation_wlambda.py` +
`habiro-interpolation-wlambda.witness.json`.)_

## Coordination

Stacked on #3822 (boundary data source). Extends — does not edit — the #3681 Lean carriers
(new sibling `BWVacuumRowHabiroBoundaryData.lean`).

Refs: [hikami2005brieskorn], [lawrence-zagier-1999], [fintushelstern1990],
[murakami-murakami2001]; audit `2026-07-12-fibre-observable-categorical-not-analytic.md`;
ledger `docs/coordination/s5-so3-keystone.md`.
