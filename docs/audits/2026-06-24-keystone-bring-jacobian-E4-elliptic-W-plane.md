# Keystone geometric `W`: `Jac(Bring) ~ E⁴` — the rank-2 W-plane is the elliptic curve `Bring/S₄`

**Date:** 2026-06-24
**Branch:** `claude/mass-open-keystone-w-l2-root-2026-06-24`
**Status:** exact (character theory); concretely identifies the keystone "W-plane" as a specific elliptic curve and reduces the keystone q-family monodromy from genus-4 to genus-1. No fit.
**Probe:** [`computations/substrate/bring_jacobian_isogeny_factors.sage`](../../computations/substrate/bring_jacobian_isogeny_factors.sage) · **Witness:** [`computations/substrate/bring-jacobian-isogeny-factors.witness.json`](../../computations/substrate/bring-jacobian-isogeny-factors.witness.json)
**Builds on:** merged [#2701](https://github.com/litlfred/qou/pull/2701) (`H^{1,0}(Bring)` is the A₅-irreducible 4-dim standard rep).

## The question this answers

#2701 established that the framework's `H¹(Bring) = 2W` cannot be an A₅-subrep of
the holomorphic differentials (they are the *irreducible* 4-dim standard rep), so
`W` must be an **isogeny/CM factor of `Jac(Bring)`**. That left *which* factor. This
probe pins it exactly.

## Method — quotient genera (exact, no period integration)

For any `H ≤ S₅ = Aut(Bring)`, the quotient curve has
`genus(Bring/H) = dim (H^{1,0})^H = dim std^H = (1/|H|) Σ_{h∈H} χ_std(h)`,
and the quotient map `Bring ↠ Bring/H` makes `Jac(Bring/H)` an isogeny factor of
`Jac(Bring)`. This is pure character theory — no period matrix (which #2701 showed
is tool-limited by conjugate singularities), no fit.

## The result

| `H` (subgroup of S₅) | `\|H\|` | `genus(Bring/H) = dim std^H` |
|---|---|---|
| `S₄` (point stabilizer) | 24 | **1 — elliptic** |
| `A₄`, `D₆` | 12 | **1 — elliptic** |
| `D₄` | 8 | **1 — elliptic** |
| `S₃`, `C₆` | 6 | **1 — elliptic** |
| `C₂×C₂`, `C₄` | 4 | **1 — elliptic** |
| `C₃` | 3 | 2 |
| `C₂` (transposition) | 2 | 2 or 3 |
| `A₅`, `S₅`, `F₂₀`, `D₅` | 60/120/20/10 | 0 |

**Eight subgroup classes give genus-1 (elliptic) quotients.** The cleanest is
`E := Bring/S₄`, an elliptic curve.

### `Jac(Bring) ~ E⁴`

1. `H^{1,0}(Bring) = std` is **irreducible** as an S₅-representation (#2701). A
   curve whose analytic representation `H^{1,0}` is `G`-irreducible has a
   **`G`-isotypic Jacobian** — isogenous to a power `B^n` of a single
   isogeny-simple abelian variety `B`.
2. `E = Bring/S₄` is a genus-1 **quotient**, hence an isogeny **factor**. A simple
   factor of an isotypic `B^n` must be isogenous to `B`, so `B = E` and
   `Jac(Bring) ~ E⁴` (`4 = dim Jac`).

This is the established Riera–Rodríguez result ("The period matrix of Bring's
curve", *Pacific J. Math.* **154** (1992)); here it is re-derived from quotient
genera + the #2701 irreducibility.

## Why this sharpens the keystone

> **🟧 Correction (2026-07-18) — the `SL₂(ℤ)` monodromy framing below is structurally
> excluded (scope-(b)).** The consistency bullet in this section writes "`M ∈ SL₂(ℤ)`
> acting on `H¹(E)` has char. poly `x² − (tr M)x + 1`" next to the non-integer target
> `tr B = 3(3q₀⁴+8q₀²+3)/(4q₀(q₀+1)²) ≈ 2.6423863`. Those two statements are jointly
> impossible: integer matrices have **integer** traces (the cited invariant —
> automorphisms/Gauss–Manin monodromies of algebraic families act on `H₁(·, ℤ)` by
> integer symplectic matrices, Riera–Rodríguez 1992 Thm 1 / Braden–Northover 2012
> §5.2), and `2 < tr B < 3` on the whole documented q₀ interval. Machine-checked
> sorry-free in
> [`QOU/BraidKnot/TrBIntegerTracePrune.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/TrBIntegerTracePrune.lean)
> (`no_SL2Z_realizes_trB`). Per AGENTS.md §Before declaring "refuted", this is a
> **structural exclusion (b)** of the *integral*-monodromy reading only: the
> genus-4 → genus-1 reduction and the 2×2 depth-2 `det = 1` recurrence structure below
> **stand**; the surviving object is a **real-analytic `SL₂(ℝ)` transfer-matrix
> family** `M(q)` with `tr M(q₀) = 2.6424` — not the integral monodromy of an
> algebraic elliptic surface. This also prunes the "search algebraic elliptic
> fibrations / modular monodromies for trace 2.6424" class before anyone runs it.
> Cross-ref: uploaded-papers audit idea A3,
> [`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md).
> The original text below is retained unedited for the record.

The framework's **rank-2 "W-plane scale + modulus"** (2 real DOF, cheat-sheet) is
**literally `E = Bring/S₄`**: an elliptic curve's period is exactly a scale and a
modulus — 2 real DOF. So:

- **`H¹(Bring) = 2W` is concrete:** `H¹(Bring) = H¹(E) ⊗ std = 2·std`, with `W`
  the elliptic factor `E` and the "2" the rank of `H¹(E)`. Consistent with #2701
  (W is an abelian-variety factor, not an A₅-subrep of forms).
- **The keystone q-family monodromy `M` drops from genus-4 to genus-1.** Instead of
  an `Sp(8,ℤ)` Gauss–Manin monodromy on the full genus-4 family, the W-plane data is
  a **2×2 `SL₂` Gauss–Manin monodromy on a q-family of elliptic curves `E(q)`**
  (`SL₂` because it preserves the principal polarization on `E`). The keystone
  trace target `tr B = 2.6424` (merged lever-1 #2701) is then literally
  `tr M` of that 2×2 monodromy.
- **Consistency with lever-1.** The lever-1 binding kernel is the depth-2,
  `det = 1` recurrence `R = x² − τx + 1` with `τ = tr B = 2.6424` — exactly the
  characteristic polynomial of a 2×2 `SL₂` matrix. The elliptic-W-plane picture
  *predicts* this 2×2 structure: `M ∈ SL₂(ℤ)` acting on `H¹(E)` has char. poly
  `x² − (tr M)x + 1`. The lever-1 recurrence and the elliptic W-plane are the same
  object.

## What remains open (the genuine keystone)

The fixed elliptic curve `E = Bring/S₄` has no monodromy; the keystone needs the
**q-family `E(q)`** (the deformation whose Gauss–Manin monodromy `M(q)` has
`tr M(q₀) = 2.6424`). Two concrete sub-questions, now genus-1 (tractable):

1. **Identify `E(q)`** — the q-deformation of `Bring/S₄`. Candidate: the elliptic
   fibre of the s5-so3 / Seifert `S³/2I` construction (#2524) restricted to the
   `S₄`-quotient. Its j-invariant / modulus as a function of q.
2. **`tr M(q₀) = 2.6424`?** — compute the Gauss–Manin monodromy trace of `E(q)`
   around `q₀` and test against the lever-1 target. The torus shortcut is *refuted*
   (#2701: `τ_torus = 2.0437 ≠ 2.6424`), so `E` is **not** the substrate torus `E_q`
   — it is the distinct elliptic curve `Bring/S₄`, and finding its modulus is the
   open step.

This converts the keystone from "derive a genus-4 Gauss–Manin matrix" to "identify
one q-family of elliptic curves and check a 2×2 monodromy trace" — a substantial
reduction in difficulty, and it ties the geometric-`W_λ` keystone (#2503/#2524) to
the merged lever-1 recurrence.

## Discipline

Exact character theory (`genus(Bring/H) = dim std^H`); no fit; nothing wired. The
`Jac(Bring) ~ E⁴` decomposition is exact (isotypic + elliptic-quotient argument,
matching Riera–Rodríguez). The q-family `E(q)` and its monodromy trace are the
open keystone, now at genus-1.

## Explicit `j(E)` — status and method (T1 follow-up)

Attempting the *explicit* `E = Bring/S₄` (its j-invariant) surfaced a subtlety worth
recording so it is not re-walked:

- The **symmetric P³ model** `Bring = {s₁²+s₂ = 0, s₃ − s₁³ = 0}` (power sums of
  `x₀..x₃`, after eliminating `x₅ = −s₁`) is genus 4 (Sage-verified), and on it the
  elementary symmetric invariants collapse: `e₂ = e₁²`, `e₃ = e₁³` (ideal-membership
  verified).
- **So the ambient S₄-invariant ring restricts to only a genus-0 subfield**
  `ℚ(e₁,e₂,e₃,e₄)|_{Bring} = ℚ(e₄/e₁⁴)` — the map `(e₁:e₂:e₃:e₄)` lands in
  `{e₂=e₁², e₃=e₁³} ≅ P(1,4) ≅ P¹`. This is a *proper* genus-0 subfield of
  `K(Bring)^{S₄}`; restriction and "take S₄-invariants" do **not** commute through
  the Bring relations, so the symmetric polynomials do **not** generate the genus-1
  quotient field.
- ⟹ **`j(E)` is not obtained from elementary invariants.** It needs either (a) the
  function-field **fixed field** `K(Bring)^{S₄}` (extra invariants beyond the
  symmetric polynomials), or (b) the **periods** of the unique S₄-invariant
  differential `ω_E ∈ (H^{1,0})^{S₄}` (dim 1) — tool-blocked here by the same
  conjugate-singularity `RiemannSurface` limitation as #2701, or (c) the **5:1 cover**
  `E = Bring/S₄ → Bring/S₅ = P¹` (branch data).

`j(E)` is therefore a **bounded next step** (fixed-field computation), distinct from
the genuinely keystone-gated parts (`E(q)` and `tr M(q₀) = 2.6424`). The structural
reduction above (genus-4 → elliptic, `M` a 2×2 `SL₂`) stands independent of the
explicit `j(E)`.

### Resolution — the tool-block is removed by the literature (2026-07-18, `library/`)

The `RiemannSurface` tool-block above (option (b)) is **superseded**: two Bring
period-matrix papers landed in `library/` and are now registered in
`references.ts`. They supply the explicit period matrix **analytically** — no Sage
`RiemannSurface` computation on the conjugate singularities is needed:

- **Riera–Rodríguez 1992** (`[riera-rodriguez-1992]`, Pacific J. Math. 154): the
  explicit period matrix `Z = τ₀·C` (`C` = the 4×4 matrix with diagonal `4`,
  off-diagonals `±1`); the natural isogeny diagonalises `Z` to `(5τ, 5τ, 5τ, τ)`,
  i.e. `E_{5τ}³ × E_τ`, recovering `Jac ~ E⁴`. Gives the elliptic model
  `E: y² = x³ − 675x − 79650`.
- **Braden–Northover 2012** (`[braden-northover-2012]`, SIGMA 8 065): recovers the
  same `τ₀·C` via the Hulek–Craig sextic, adds the Vector of Riemann Constants and
  the explicit anti-holomorphic **real structure** (conjugation) on `Jac(Bring)`.

**Explicit j-invariants (Braden–Northover convention, authoritative):**
`j(τ₀) = −5·29³/2⁵` and `j(5τ₀) = −25/2`. **Convention caveat:** Riera–Rodríguez
**swap** these two equations — a typographical error flagged by Braden–Northover.
Any corpus site quoting Riera–Rodríguez as the `j` source must use the
Braden–Northover labelling (the `alpha-em.md` ledger's `j(τ₀) = −5·29³/2⁵` already
matches it, via `[braden-disney-hogg-2022]`). So `j(E)` is **no longer a bounded
open step — it is in the literature**; option (b) is closed analytically, option (a)
(fixed-field) is unnecessary.

**Bearing on the fibre-level correspondence.** Braden–Northover's explicit
anti-holomorphic involution on `Jac(Bring)` is the **concrete Hodge-side object** of
the α_EM per-loop `1/(8π)` fibre-level correspondence — the geometric realisation of
the abstract anti-linear `R` named in
[`2026-07-18-alpha-em-involution-type-nome-independent.md`](2026-07-18-alpha-em-involution-type-nome-independent.md)
(merged #3949). It is the object to compare against the Hecke channel-swap
`q ↦ −q⁻¹` image.
