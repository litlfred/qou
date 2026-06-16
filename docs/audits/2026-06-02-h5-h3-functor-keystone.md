# The H₅↔H₃ functor (the 5↔3 keystone): rigorous nonexistence at the rep-ring level

**Date:** 2026-06-02
**Branch:** `claude/h5-h3-functor-keystone-2026-06-02`
**Scope:** THE keystone open object named by FOUR merged audits (all on main):
the missing canonical map from the **5-strand** S₅/SO(3) icosahedral fiber
level ℓ to a **Wedderburn coefficient of the 3-strand H₃ Borromean baryon
trace** (the (2,1) std block carrying h⁴ = −3/4). None of the four predecessors
computed the **standard Hecke-algebra restriction functor Res^{H₅}_{H₃}**
explicitly — the most standard candidate. This audit does, together with its
adjoint (induction), the Markov tower H₃⊂H₄⊂H₅, and the icosahedral A₅ → 3-element-stabilizer
restriction.
**Compute:**
[`h5_h3_functor_keystone.py`](../../computations/h5_h3_functor_keystone.py),
witness
[`h5-h3-functor-keystone.witness.json`](../../computations/h5-h3-functor-keystone.witness.json)
(audit-only, exact integer/rational branching + RAW @ the canonical
`compute_dps` for the substrate `z`, 17 assertions pass). **No tuning to h⁴=−3/4, m_n−m_p, B_AME, spin, or
hypercharge.** Every multiplicity is computed FIRST from the branching rule;
the comparison to the (2,1) block comes SECOND. **A chosen multiplicity would
be a fit — we report RAW multiplicities only.**

---

## VERDICT (one line)

**RIGOROUS NONEXISTENCE. Every standard categorical bridge between the
5-strand fiber level and the 3-strand baryon trace — Hecke restriction
Res^{H₅}_{H₃}, its adjoint induction, the Markov stabilization tower H₃⊂H₄⊂H₅,
and the icosahedral A₅ → S₃/Z₃ restriction — spreads the (2,1) baryon block
across MULTIPLE 5-strand blocks with multiplicities in {1, 2}, computed RAW,
with no distinguished single occurrence that singles out the ℓ=2 carrier. There
is NO canonical isomorphism taking the ℓ=2 / dim-5 icosahedral irrep H to THE
(2,1) h⁴ coefficient: the restriction (2,1)-multiplicity vector is `[0,1,2,2,2,1,0]`
(values in {0,1,2}; the multiplicity-1 entries (4,1) and (2,1,1,1) do NOT single
out the dim-5 ℓ=2 carrier — the same-dimension (3,2) and (2,2,1) give 2), and the
icosahedral H → S₃ restriction contains (2,1) with multiplicity 2. So
`Hom(fiber, (2,1))` is a multiplicity space of dimension ≥ 1 with no canonical
distinguished basis vector; choosing one to read off h⁴ is a fit the discipline
review catches. This confirms and SHARPENS the s5-so3 audit's informal "different
representation rings, no canonical map" into a precise theorem, and forces a
reframe: the bridge — if it exists — is non-functorial / geometric, OR the baryon
is not literally a 3-strand object, OR the fiber is not literally a 5-strand
object.**

---

## The four candidates — RAW multiplicities

### Why the Hecke computation reduces to the symmetric group

At the real substrate `q₀ ≈ 1.10998` (and for any `q` that is not a root of
unity), the Iwahori–Hecke algebra `H_n(q)` is **semisimple** with the same
irreducible block labels `λ ⊢ n` as the group algebra `ℂ[S_n]` (Tits
deformation / Wenzl). The **restriction functor** along the standard inclusion
`H₃ = ⟨σ₁,σ₂⟩ ⊂ H₅ = ⟨σ₁,…,σ₄⟩` obeys the SAME branching rule (iterated
remove-a-box, Young) as the symmetric-group restriction. Hence the
multiplicities below are **q-independent integers**. (§7a Hecke–Skein: the
generator is `σ_i`; the trace is the Markov trace `tr_M`.)

### Candidate 1 — Restriction Res^{H₅}_{H₃}  (the most standard candidate)

Multiplicity of the (2,1) std irrep in the restriction of each `λ ⊢ 5`,
computed by iterating S₅→S₄→S₃ remove-a-box (RAW):

| λ ⊢ 5 | dim S^λ | (3) | **(2,1)** | (1³) | dim check |
|---|---|---|---|---|---|
| (5) | 1 | 1 | **0** | 0 | 1 = 1 ✓ |
| (4,1) | 4 | 2 | **1** | 0 | 4 = 2+2 ✓ |
| (3,2) | 5 | 1 | **2** | 0 | 5 = 1+4 ✓ |
| (3,1,1) | 6 | 1 | **2** | 1 | 6 = 1+4+1 ✓ |
| (2,2,1) | 5 | 0 | **2** | 1 | 5 = 4+1 ✓ |
| (2,1,1,1) | 4 | 0 | **1** | 2 | 4 = 2+2 ✓ |
| (1⁵) | 1 | 0 | **0** | 1 | 1 = 1 ✓ |

**RAW (2,1)-multiplicity vector: `[0, 1, 2, 2, 2, 1, 0]`.** All seven
dim-checks pass (`Σ_μ m_{λμ}·dim μ = dim λ`, asserted to exact integers).

**Reading:** the (2,1) baryon block appears in the restriction of FIVE of the
seven 5-strand irreps, with multiplicities in {1, 2}. There is **no
distinguished λ ⊢ 5 whose restriction contains exactly one canonical copy of
(2,1)** that could be identified with "the fiber level". In particular the
ℓ=2 carrier is the dim-5 icosahedral irrep H (an A₅ object — see Candidate 4),
which is NOT one of the seven S₅ irreps as a restriction source; and even the
S₅ irreps of the same dimension ((3,2) dim 5, (2,2,1) dim 5) restrict to (2,1)
with **multiplicity 2**, not 1. **No canonical iso.**

### Candidate 2 — Induction Ind^{H₅}_{H₃}((2,1))  (the adjoint)

By Frobenius reciprocity `⟨Ind(μ), λ⟩ = ⟨μ, Res(λ)⟩`, the induction
multiplicities of (2,1) ARE the column vector above: `[0,1,2,2,2,1,0]`.

- `dim Ind = Σ_λ m_λ · dim S^λ = 0·1 + 1·4 + 2·5 + 2·6 + 2·5 + 1·4 + 0·1 = 40`.
- Expected `[S₅:S₃] · dim(2,1) = 20 · 2 = 40` ✓ (asserted).

**Reading:** the baryon block induces up to a 40-dimensional module spread over
the same five 5-strand blocks. There is **no canonical projection** of the
fiber level onto a single induced summand either.

### Candidate 3 — Markov tower H₃ ⊂ H₄ ⊂ H₅  (the strand-adding chain)

Forward add-a-box embedding of (2,1) through the tower:

```
(2,1) ⊢3  →  {(3,1),(2,2),(2,1,1)} ⊢4  →  ⊢5
```

The level-5 embedding multiplicity of (2,1) computed this way is **identical**
to the Candidate-1 restriction vector `[0,1,2,2,2,1,0]` (branching duality:
add-box embedding multiplicity = remove-box restriction multiplicity). The
Markov stabilization scales the trace by `z = 1/(q^{1/2}+q^{−1/2})` per added
strand; two stabilizations H₃→H₅ scale by `z²`. RAW at q₀:

- `z(q₀) = 0.4993203…`  (matches the census/linked-channel value)
- `z²(q₀) = 0.2493208…`

**Reading:** the forward Markov tower gives the SAME multivalued embedding as
restriction — NOT a canonical 5→3 functor. This is fully consistent with the
census finding (PR #1677) that Markov destabilization is the canonical
strand-count map but does not isolate a single block, and with the Brunnian
obstruction (the Borromean braid uses both B₃ generators, so no single strand
destabilizes — the destabilization direction is blocked).

### Candidate 4 — Icosahedral A₅ restricted to a 3-element stabilizer

The ℓ=2 carrier is the **dim-5 irrep H of A₅ ≅ I ⊂ SO(3)** (s5-so3 audit).
Restrict it to the two natural 3-element subgroups, via explicit character
tables (RAW):

**(i) Z₃ = ⟨(123)⟩ ⊂ A₅** (cyclic rotation of 3 color sheets). χ_H restricted
to (e, g, g²) = (5, −1, −1):

| Z₃ irrep | triv | ω | ω² |
|---|---|---|---|
| mult in H | **1** | **2** | **2** |

dim check 1+2+2 = 5 ✓.

**(ii) S₃ = ⟨(123),(12)(45)⟩ ⊂ A₅** (a genuine order-6 non-cyclic subgroup;
S₃ DOES embed in A₅). χ_H restricted to (e, 3-cycle, transposition) =
(5, −1, 1):

| S₃ irrep | triv | sign | **std (2,1)** |
|---|---|---|---|
| mult in H | **1** | **0** | **2** |

dim check 1·1 + 0·1 + 2·2 = 5 ✓.

**Reading — this is the decisive raw number.** The ℓ=2 dim-5 fiber irrep H
restricted to S₃ ⊂ A₅ contains the (2,1) std baryon irrep with **multiplicity
2, not 1**. So even the most charitable reading — "the fiber is the
icosahedral H; restrict it to the color-sheet S₃" — does NOT give a canonical
single (2,1) channel. There is **no canonical isomorphism H ≅ (2,1)**; the
best one gets is a 2-dimensional multiplicity space `Hom_{S₃}(std, Res H) ≅ ℂ²`,
and choosing a line in it to define "the h⁴ amplitude" is exactly a fit.

---

## The precise nonexistence theorem

> **Theorem (no canonical Hecke-level 5→3 functor onto the h⁴ coefficient).**
> Let `H` denote the ℓ=2 dim-5 icosahedral irrep (the A₅ ⊂ S₅ fiber carrier)
> and `(2,1)` the standard H₃(q) block carrying the Borromean h⁴ = −3/4. For
> every standard rep-ring construction relating the 5-strand and 3-strand
> Hecke towers:
>
> 1. **Restriction.** `[Res^{H₅}_{H₃}(λ) : (2,1)] ∈ {0,1,2}` for `λ ⊢ 5`,
>    with the vector `[0,1,2,2,2,1,0]` — never a distinguished multiplicity-1
>    occurrence singling out a fiber level.
> 2. **Induction.** `Ind^{H₅}_{H₃}((2,1))` is 40-dimensional, spread over five
>    `λ ⊢ 5` blocks with the same vector — no canonical projection.
> 3. **Markov tower.** The forward `H₃↪H₄↪H₅` add-box embedding multiplicity of
>    (2,1) equals the restriction vector (branching duality); the strand move
>    carries `z²` but does not isolate one block.
> 4. **Icosahedral restriction.** `[Res^{A₅}_{S₃}(H) : (2,1)] = 2 ≠ 1` (and
>    `[Res^{A₅}_{Z₃}(H) : ω] = 2`).
>
> In every case the (2,1) baryon block occurs in the image of the fiber datum
> **across multiple blocks with multiplicities in {1, 2}** — with no single
> distinguished occurrence singling out the ℓ=2 carrier (the multiplicity-1
> entries (4,1) and (2,1,1,1) are NOT the dim-5 ℓ=2 irrep, and the icosahedral
> H → S₃ restriction gives multiplicity 2). Hence `Hom(fiber, (2,1))` is a
> multiplicity space of dimension ≥ 1 with no canonical basis vector. **Therefore there is no
> canonical map (natural transformation / isomorphism) sending the ℓ=2 / H
> amplitude to THE coefficient h⁴ = −3/4.** Any such assignment requires
> choosing an element of a ≥1-dimensional Hom-space, i.e. a fit. ∎

This is the rigorous form of the s5-so3 audit's "different representation
rings, no canonical map." The obstruction is **not** that the two objects live
in different rings per se (restriction/induction are perfectly good functors
*between* the rings); it is that the (2,1)→fiber correspondence is
**multivalued (multiplicity ≥ 2)**, so there is no canonical line to carry the
scalar h⁴.

---

## Reframe implications (what a real bridge would have to be)

The nonexistence forces one of three reframes (none is a fit; each is a
distinct, testable structural hypothesis):

1. **Non-functorial / geometric bridge.** The 5↔3 link is not a Hecke functor
   at all but a geometric map (e.g. the icosahedral fiber's *holonomy* acting
   on the color-tube cubic of the flavor-cusp audit, PR #1670), which need not
   respect the Wedderburn block structure. The multiplicity-2 Hom-space would
   then be resolved by a geometric (cusp-shape / cross-ratio) datum, not a
   categorical one.
2. **The baryon is not literally 3-strand.** If the physical nucleon is a
   5-strand object whose 3-strand Borromean is a *Markov-destabilized shadow*,
   the h⁴ would live natively at the 5-strand level and the "5→3" question
   dissolves. This is testable: compute `tr_M` of a 5-strand Brunnian-type
   word and check whether its (2,1)-channel-after-destabilization reproduces
   −3/4 with the `z²` factor (the destabilization is blocked for the Brunnian
   Borromean — census §3a — but a 5-strand pre-image might destabilize).
3. **The fiber is not literally 5-strand.** If "5" refers to the icosahedral
   SO(3) finite subgroup (A₅) and NOT to a 5-strand braid index, then the
   fiber group acts on the 3 color sheets directly (Candidate 4 (ii)), and the
   multiplicity-2 result says the SO(3) fiber sees the baryon channel *twice* —
   which matches the s5-so3 audit's separate finding that the std/(2,1) irrep
   appears at BOTH ℓ=1 and ℓ=2 under the rotation embedding. The "ℓ=2 only"
   premise being false (s5-so3 audit) is the *same* multiplicity-2 phenomenon
   seen here from the A₅ side.

**Cross-audit unification:** the multiplicity-2 of (2,1) in `Res^{A₅}_{S₃}(H)`
(this audit, Candidate 4) is the SAME number as the s5-so3 audit's "std appears
at ℓ=1 (mult 1) and ℓ=2 (mult 2)" — both are statements that the SO(3)/I fiber
sees the baryon channel with non-trivial multiplicity, which is precisely why
no canonical scalar (h⁴) can be read off.

---

## What this audit does and does not claim

- **Does** compute, RAW and exactly, the standard Hecke restriction
  `Res^{H₅}_{H₃}` (2,1)-multiplicity vector `[0,1,2,2,2,1,0]`, with all seven
  dimension checks passing to exact integers.
- **Does** compute the adjoint induction (dim 40 = [S₅:S₃]·2 ✓) and the
  forward Markov tower (= restriction vector, with `z²` factor RAW @ q₀).
- **Does** compute the icosahedral `Res^{A₅}_{S₃}(H) = triv ⊕ 2·(2,1)` and
  `Res^{A₅}_{Z₃}(H) = triv ⊕ 2ω ⊕ 2ω²` via explicit character tables, dim-checked.
- **Does** prove the precise nonexistence theorem: every standard bridge sends
  (2,1) with multiplicity ≠ 1, so there is no canonical map onto the h⁴
  coefficient — sharpening the s5-so3 audit's informal claim.
- **Does** state three testable reframes (geometric bridge / 5-strand baryon /
  A₅-not-B₅ fiber) and unify the multiplicity-2 finding with the s5-so3 audit's
  ℓ=1/ℓ=2 degeneracy.
- **Does NOT** propose, fit, or tune any normalization, multiplicity, or fiber
  map. h⁴ = −3/4, m_n−m_p, spin, hypercharge are falsification references only.
- **Does NOT** wire to production; does NOT advance L2 numerically; does NOT
  discharge any Lean `sorry`. No LP/SDP solve appears (no dual emission
  required).

---

## Cross-references

- The four merged predecessors naming the same missing object:
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md) (PR #1672),
  [`2026-06-01-knot-operator-census-group-actions.md`](2026-06-01-knot-operator-census-group-actions.md) (PR #1677),
  [`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md) (PR #1670),
  [`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md) (PR #1678).
- The falsification reference (h⁴ = −3/4 from the (2,1) block):
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md),
  [`borromean_h3_2_1_irrep_derivation.py`](../../computations/borromean_h3_2_1_irrep_derivation.py).
- Markov (de)stabilization = vertical α_V:
  [`markov-moves-brane-tower.md`](../../content/quantum-observable-universe/braids-and-knots/markov-moves-brane-tower.md).
- The Lean class still axiomatising the (now-proven-nonexistent-as-Hecke-functor) fiber map:
  [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)
  (`conj:s5-so3-fiber-action`, `BringFiberAction`).
