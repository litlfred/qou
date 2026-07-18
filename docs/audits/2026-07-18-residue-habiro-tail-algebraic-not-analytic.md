# residue ↔ Habiro cyclotomic-tail identity is FINITE-ALGEBRAIC, not analytic (formalize-first prune)

**Date:** 2026-07-18
**Bean:** `qou-b3ix` (deep-dive 2 of the alien-calculus ↔ Habiro review, milestone `qou-89f9`)
**Branch:** `claude/alien-calculus-habiro-50257v`
**Status:** AUDIT — structural reframing + §3b-cond upgrade proposal. No fit, no
production wiring, no new number.

## 0. The claim under review

[`prop:habiro-residue-sum-equivalence`](../../content/quantum-observable-universe/mass-theory/habiro-residue-sum-equivalence.md)
states that the two constructions of the Markov trace agree on the archimedean
realization `ρ_∞ : Ẑ[q] → ℝ`:

$$
  \underbrace{\sum_{m} a_m(u_0)\,(u_0;u_0)_m}_{\text{Habiro (cyclotomic)}}
  \;=\;
  \underbrace{|\mathrm{tr}_M^{(0)}| + \sum_\ell \mathrm{Res}_{q\to\zeta_\ell}(\Phi_q\cdot\mathrm{tr}_{M,\ell})}_{\text{GB (residue spectral sum)}}
$$

The `.md` labels this a **"non-trivial analytic identity"** whose **"analytic
identification of the residue contributions with the cyclotomic tail remains
open"**, and certifies it only as an **"empirical witness"** (machine-ε
agreement for p/n/D; proton `rel_diff = 0.0`).

## 1. Finding — the "analytic / open" label is mis-scoped

The two Lean siblings that *define* the objects contradict the "analytic"
framing:

- [`full-pole-structure-mass-trace.lean:25-29`](../../content/quantum-observable-universe/mass-theory/full-pole-structure-mass-trace.lean):
  the "Mittag-Leffler over ℂ" expression `Σ r_n^{(j)}/(q-ζ_n^{(j)})` is a
  **"formal residue spectral sum … that feeds the cyclotomic coefficients
  a_m. It is not a complex-analytic identity on or near S¹."** (`tr_M` is not
  meromorphic on ℂ — primitive roots of unity are dense in S¹, a natural
  boundary.)
- [`gb-residue-spectral-sum.lean:27-28`](../../content/quantum-observable-universe/mass-theory/gb-residue-spectral-sum.lean):
  `prop:residue-at-root` is **"the cyclotomic residue as a projection in the
  Habiro completion `ℤ̂[q] → ℤ[q]/Φ_{n_ℓ}(q) ≅ ℤ[ζ_ℓ]`, no analytic
  continuation."**

So **both sides are algebraic operations on one element `f ∈ Ẑ[q]`**:

| side | what it is | basis |
|---|---|---|
| Habiro | `Σ_m a_m (q;q)_m` | cyclotomic `(q;q)_m` basis of `Ẑ[q]` |
| GB residue | `descended + Σ_ℓ` projection to `ℤ[ζ_ℓ]` | root-of-unity values `f(ζ_ℓ)` |

These are **two coordinate systems on the same Habiro ring**, related by the
Habiro evaluation-at-roots-of-unity map `Ẑ[q] ↪ ∏_ζ ℤ[ζ]` (Habiro 2004, the
injectivity that makes an element determined by its root-of-unity values). The
change of basis is the **unipotent lower-triangular** transform

$$
  f(\zeta_N) \;=\; \sum_{m=0}^{N-1} a_m(\zeta_N)\,(\zeta_N;\zeta_N)_m,
  \qquad (\zeta_N;\zeta_N)_m = 0 \ \text{for}\ m\ge N,
$$

triangular because `a_m` first appears at `ζ_{m+1}`. This is a **finite
algebraic identity**, not an analytic one. Applying the ring hom `ρ_∞`
(evaluate at the regular real point `u_0 = √q_0`, neither a root of unity nor a
pole) to the Habiro-ring identity `f = descended + Σ_ℓ (residue projections)`
gives the archimedean agreement **for free** — `ρ_∞` is a ring hom, so it
commutes with the (finite) decomposition.

**Corroboration from the framework's own direction.** The z-Habiro brane-tower
conjecture
([`brane-tower-z-habiro.md`](../../content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md),
Consequence 1) explicitly aims to **"replace the analytic infinite product
`Φ_q(z)` with an algebraic element."** The residue↔tail identity is the *target*
of that program, so reading it as algebraic is consistent with corpus intent,
not a re-scope against it. And `rel_diff = 0.0` (exact, proton) is the signature
of an **exact algebraic identity**, not an analytic approximation — an analytic
resummation would leave a beyond-all-orders residual.

## 2. What is *actually* open (the honest residual)

Not analytic continuation, Borel resummation, or transcendence. The one open
input is the **algebraic identification of the two filtration decompositions of
the same trace**:

> The Gröbner–Shirshov-filtration graded trace `tr_{M,ℓ}` on `J^ℓ/J^{ℓ+1}`
> (`prop:graded-markov-trace-from-gs-filtration`) and the cyclotomic projection
> `Ẑ[q] → ℤ[q]/Φ_{n_ℓ}(q)` (`prop:residue-at-root`) descend from the **same**
> `f ∈ Ẑ[q]`.

`gb-residue-spectral-sum.lean:30-36` already flags this as deferred
infrastructure ("multi-week … `QOU.AlgebraicSubstrate`") — but it is an
**algebraic** identification (GS filtration ↔ cyclotomic filtration), squarely
in the anti-fit-safe formalize-first lane, **not** the analytic-number-theory
problem the `.md` implies.

## 3. Proposed §3b-cond upgrade (turns the axiom into a derived theorem)

Currently `HabiroResidueSumEquivalence.archimedean_agreement`
([`habiro-residue-sum-equivalence.lean:97-98`](../../content/quantum-observable-universe/mass-theory/habiro-residue-sum-equivalence.lean))
axiomatizes the **whole** real equality (proton instance is a bare `axiom`,
`:154`). Formalize-first says: axiomatize only the genuine open input, derive
the rest. Shape:

```lean
-- The ONE honest open input (algebraic, §3b-cond class field):
--   the cyclotomic sum and the descended+residue sum are the SAME
--   Habiro element (before any real evaluation).
class HabiroGBSameElement (E : HabiroResidueSumEquivalence) : Prop where
  same_element :
    (E.habiro_trace.map (Int.castRingHom ℝ))          -- Σ a_m (u;u)_m rep
      = descendedPlusResiduePoly E                     -- descended + Σ residue rep
--   ^ an identity of ℝ[u] (or Ẑ[q]) representatives, NOT a numeric equality.

-- Then archimedean_agreement is DERIVED, not assumed:
theorem archimedean_agreement_of_sameElement
    (E : HabiroResidueSumEquivalence) [HabiroGBSameElement E] :
    (E.habiro_trace.map (Int.castRingHom ℝ)).eval (Real.sqrt E.q_0) = E.gb_mass :=
  by rw [HabiroGBSameElement.same_element]; -- eval the descended+residue rep
     …                                        -- = gb_mass by the GB decomposition
```

This is the exact §3b-cond pattern (verified exemplar: `q_bkm_criterion.lean`):
the class carries a genuine **sub-hypothesis** (common Habiro element), the
theorem **derives** the `.md` claim (real agreement) rather than projecting it.
Non-degenerate — the class field is the algebraic identification, not the
conclusion.

**Epistemic upgrade:** "the archimedean number-agreement is axiomatized"
(analytic, mysterious, `rel_diff` treated as evidence for an *analytic* claim) →
"one **algebraic** filtration-identification is axiomatized; the archimedean
agreement is **proved** modulo it." The proton `axiom` at `:154` shrinks from a
transcendental real equality to a corollary.

## 4. Formalizable structural core (generic-`R`, §7c wall-safe — provable now)

Independent of the deferred GS-infrastructure, the **triangular basis-change**
itself is a clean generic-`R` lemma (no `ℝ`, no analysis):

```lean
variable {R : Type*} [CommRing R]
-- qPochhammer already exists generic in habiro-expansion-atomic.lean.
-- Value-at-root-of-unity of a cyclotomic sum truncates:
theorem cyclotomic_value_truncates
    (a : ℕ → R) (ζ : R) (N : ℕ) (hζ : qPochhammer ζ N = 0)
    (M : ℕ) (hM : N ≤ M) :
    ∑ m ∈ Finset.range (M+1), a m * qPochhammer ζ m
      = ∑ m ∈ Finset.range N, a m * qPochhammer ζ m := …
--   because qPochhammer ζ m = 0 for m ≥ N (one factor already vanishes and
--   the product is over a CommRing) ⇒ the tail drops. Pure Finset algebra.
```

This is the Lean face of "the residue↔tail change of basis is unipotent
triangular and finite." It **prunes the analytic framing structurally**: if the
value at each `ζ_N` is a *finite* partial sum of the cyclotomic coefficients,
there is nothing to resum. (Draft; to be verified `lean`-direct against the
generic `qPochhammer` in `habiro-expansion-atomic.lean` before landing.)

## 5. Discipline / corpus-grep

- Prior art: `2026-07-12-borel-alien-calculus-utilization-audit.md` §G4
  (Habiro kernel ↔ Stokes automorphism — the *analytic* even-channel object,
  distinct: that is the Q_β `c_k` divergent tail, this is the *convergent*,
  finite per-braid trace) and `2026-07-13-alien-calculus-surreal-integration-review.md`
  (st = median resummation — again the analytic evaluation, not this algebraic
  identity). No prior doc reframes the residue↔tail equivalence as
  finite-algebraic; the two `.lean` "no analytic continuation" comments predate
  and support this note.
- Not touched: the deferred GS-filtration ↔ cyclotomic-projection identification
  (§2) — genuinely open, algebraic, multi-week. This note **narrows** what
  "open" means; it does not claim the residual closed.
- Anti-laundering: no fit, no wiring; the §3b-cond upgrade axiomatizes *strictly
  less* than the current bare axiom.
```

## 6. Update (same day) — §4 core lemma FORMALIZED and verified

The §4 structural-core lemma is landed and machine-checked, not a draft:
[`QOU/Common/CyclotomicValueTruncates.lean`](../../content/quantum-observable-universe/lean/QOU/Common/CyclotomicValueTruncates.lean)
— `cyclotomic_value_truncates` + `qPochDiag_eq_zero_of_ge`, generic `[CommRing R]`,
sorry-free, `lean`-direct against pinned Mathlib `f897ebcf` **exit 0** (Pochhammer
name is `qPochDiag` to avoid collision with the several existing `qPochhammer`
defs). Standalone library file per the `QOU/Common/` precedent
(`FormalResidue.lean`), agent-verified per QA-is-agent-owned. This is the
formalize-first prune: the residue↔tail change of basis is a **finite** truncation
at each root of unity — nothing to resum, confirming §1's "algebraic, not analytic".
