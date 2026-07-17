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

Probe [`computations/habiro_interpolation_wlambda.py`](../../computations/habiro_interpolation_wlambda.py)
+ witness [`habiro-interpolation-wlambda.witness.json`](../../computations/habiro-interpolation-wlambda.witness.json)
(1 assertion, passed). **Verdict: one uniform candidate `F_λ = [mark]²/D²` interpolates every
computed root** — a uniform-candidate win (consistency, not injectivity).

### (E) Exact per-root candidate (ℚ(√5) ∪ ℤ; zero floats)

The candidate is **exactly normalized** (`Σ_λ F_λ = 1`) at every root, with the fold derived per r:

| fibre root | `2cos(π·ℓ/p)` | `D²` | `F_λ` (distinct values) |
|---|---|---|---|
| order-2 `ζ=i` | 0 | 4 | `{1/4 (marks 1,3,5), 0 (2,4,6)}` |
| order-3 `e^{iπ/3}` | 1 | 6 | `{1/6 (marks 1,2,4,5), 0 (3,6)}` |
| order-5 `e^{iπ/5}` (m=1) | φ | 10+2√5 | `{1/8−√5/40, 1/8+√5/40, 0}` |
| order-5 `e^{2iπ/5}` (m=2) | φ−1 | 10−2√5 | `{1/8+√5/40, 1/8−√5/40, 0}` |

`D²` values verified exactly (`4, 6, 10±2√5`); the order-5 pair is #3822's `ℚ(√5)` fold. Rotation
numbers derived: `ℓ_5 = (1,2)` (the Galois pair), `ℓ_2 = ℓ_3 = 1` (both connections).

### (F) LR flat-amplitude factorization confirmed at orders 2, 3 (40 dps)

Parameter-free 2×2 amplitude inversion (fresh N-pairs `(81,113)` / `(121,163)`), ratio
`|A_m(α)|/|A_m(1)|` against the predicted character `|[α]_{ζ_{p}^{ℓ}}|`:

- **order 2** (`ζ=i`, `ℓ=1` both m): nonzero chars `α=1,3,5 → |[α]_i|=1` matched (ratios
  0.96–1.02); char-zero `α=2 → |[2]_i|=0` is **flat-free** (ratio ~0.012, no √N growth). ✅
- **order 3** (`ζ=e^{iπ/3}`, `ℓ=1` both m): `α=1,2,4 → |[α]_ζ|=1` matched (0.97–1.01); char-zero
  `α=3 → 0` flat-free (~0.018). ✅
- **order 5** (re-verify #3822 Galois structure): `α=2` gives `|[2]_{ζ}|=φ=1.618` at m=1 (ℓ=1) and
  `|[2]_{ζ²}|=φ−1=0.618` at m=2 (ℓ=2), both matched — the two connections see the two Galois
  embeddings, as #3822 found. ✅

The color-independence of the bare amplitude is thus confirmed, so the normalized squared amplitude
`= [mark]²_ζ/Σ[mark]²_ζ = F_λ(ζ)` at every root — the candidate matches, **structurally, not fitted**.

### (Q) Archimedean `F_λ(q₀)` — reported, NOT wired

`F_λ(q₀) = [mark]²_{q₀}/Σ[mark]²_{q₀}` at both documented pins. The physical blocks
(#3685 dictionary): electron = mark 6, muon class `(3,2)` = mark 5.

| block (mark) | `F_λ(muon q₀)` | `F_λ(proton q₀)` | rel cross-pin swing |
|---|---|---|---|
| electron (6) | 0.31522570 | 0.31522570 | 2.6e-12 |
| muon (5) | 0.21052053 | 0.21052053 | 5.3e-13 |
| (4) | 0.13046576 | 0.13046576 | 1.2e-12 |
| (3) | 0.07156249 | 0.07156249 | 2.6e-12 |
| (2) | 0.03123630 | 0.03123630 | 3.5e-12 |
| triv (1) | 0.00772467 | 0.00772467 | 4.1e-12 |

**Finding — `F_λ(q₀)` is pin-robust.** The cross-pin swing (~10⁻¹²) is ~10⁴× *smaller* than the
11.5 ppb (~10⁻⁸) q₀-pin difference, because `F_λ` is a ratio (the leading q₀-scale cancels). So the
interpolant's observable `W_λ(q₀)` **does not discriminate** between the μ and p pins at this order —
tiered **consistent-not-identified**. This is reported as a candidate value only; it is **not** a
resolution of the μ–p tension (which lives elsewhere in the mass chain, not in `W_λ`'s ratio).

## Coordination

Stacked on #3822 (boundary data source). Extends — does not edit — the #3681 Lean carriers
(new sibling `BWVacuumRowHabiroBoundaryData.lean`).

Refs: [hikami2005brieskorn], [lawrence-zagier-1999], [fintushelstern1990],
[murakami-murakami2001]; audit `2026-07-12-fibre-observable-categorical-not-analytic.md`;
ledger `docs/coordination/s5-so3-keystone.md`.
