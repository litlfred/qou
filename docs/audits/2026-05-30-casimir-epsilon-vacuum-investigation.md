# Audit: Casimir-vacuum conjecture investigation routes

**Date.** 2026-05-30
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Status.** Three speculative closure routes surveyed; one quick
empirical probe run. **Null result on naïve q-rational closed form.**

This audit accompanies PR #1497 (scaffolding the conjecture) and
documents the routes considered for closing it, so that future
agents pick up where this session stopped instead of repeating
the search.

The audit is the right place for these routes — they are
investigation records, not paper content. The conjecture's `.md`
already enumerates the three open sub-problems; this document
goes into the *how* of attacking each.

## Sub-problem summary (from the conjecture)

| # | Open content | Tractability |
|---|---|---|
| 1 | Existence of categorical `N⊙(A, d)` as a surreal-valued plate-bounded knot-density | medium |
| 2 | `A/d³` scaling of the categorical mode-count | medium (blocked on 1) |
| 3 | `π²/720` prefactor from a Hecke-trace identity matching `ζ(-3) = -1/120` | hard |

## Route A — q-deformed ζ-regularisation (sub-problem 3)

**Sketch.** The standard Casimir prefactor comes from
`ζ(-3) = -B₄/4 = -1/120` regularising `Σ_{n≥1} n³`. A QOU-native
analogue would substitute `n ↦ [n]_q` (q-integer at the substrate)
and look for a closed-form q-rational at `q = q₀ ≈ 1.110`.

**Candidates surveyed.**

1. **`ζ_q(s) = Σ [n]_q⁻ˢ`** (Kaneko–Kurokawa–Wakayama 2002). Converges
   for `s ≥ 1, q > 1`. Computed in the probe:
   - `ζ_q(1) = 3.5370`
   - `ζ_q(2) = 1.5480`
   - `ζ_q(3) = 1.1902`
   - `ζ_q(4) = 1.0789`

   None lie near `π²/720 ≈ 0.0137`.

2. **Damped cubic sum `Σ [n]_q³ · q⁻ᵏⁿ`** for `k ∈ {3, …, 15}`. All
   values are `≥ 1`, ranging from `~21000` (k=3) to `~1.0` (k=15).
   No convergence to `π²/720`.

3. **Low-degree q-rationals `a · π²/(720 · [m]_q^p)`** with
   `m ∈ {2,…,10}`, `p ∈ {1,2,3}`, `a ∈ {1,…,12}`. Closest match:

   ```
   2 · π² / (720 · [2]_q)  =  1.3634e-2
   target:  π²/720         =  1.3708e-2
   residue:                =  7.4e-5  (0.54% relative)
   ```

   Since `[2]_q = q + q⁻¹ → 2` as `q → 1`, this expression
   approaches `π²/720` trivially in the classical limit. The 0.54%
   deviation at substrate `q₀` is *consistent with* but not
   *forced by* this particular q-deformation.

**Empirical witness.**
[`casimir-q-zeta-probe.witness.json`](../../folio-assistant/computations/casimir-q-zeta-probe.witness.json)
records the full search; assertion `best_match_within_one_percent_of_target`
fires at 0.54% residue.

**Honest reading.** This is a **null result** for "trivial q-rational
closed form of π²/720 at substrate". The candidate `2·π²/(720·[2]_q)`
matches at 0.5%, but its `q → 1` limit recovers the textbook
expression for trivial reasons (continuity), not because `[2]_q`
plays a special role.

**Suggestive but non-conclusive prediction.** *If* the categorical
mode-count happens to factor exactly as `2/[2]_q × (textbook)`, the
QOU prediction would be a 0.54% deviation from standard Casimir at
substrate `q₀`. This is **below** the Mohideen–Roy 1998 experimental
precision (~1%), so it would not be falsified by current data — but
also not confirmed. A higher-precision (~0.1%) Casimir measurement
would distinguish.

**Status.** Route A does not close sub-problem 3 on its own.
Recommended follow-up: investigate Cherednik 2006 q-zeta definition
(distinct from Kaneko–Kurokawa–Wakayama) which uses Macdonald
operators and might be more naturally aligned with QOU's
Hecke-algebra substrate.

## Route B — Hoefsmit additivity on plate-bounded links (sub-problem 1)

**Sketch.** The Hoefsmit scattering pipeline
([`prop:hoefsmit-scattering-pipeline`](../../content/quantum-observable-universe/appendix-surreals/hoefsmit-bridge.md))
assigns to each link `L` a geometric energy `Geom(L) ∈ ℝ`. Under
the ε-relaxed vacuum axiom
([`prop:vacuum-epsilon`](../../content/quantum-observable-universe/appendix-surreals/vacuum-epsilon.md)),
the unknot contributes `Geom(⊙) = ε`. If `Geom` is **additive on
disjoint unions**:

```
  Geom(L₁ ⊔ L₂) = Geom(L₁) + Geom(L₂)
```

then any link `L = L_test ⊔ (N copies of ⊙)` has
`Geom(L) = Geom(L_test) + N · ε`. Multiplying the conjectural
plate-mode-count `N(A, d) ~ ε⁻¹ · A/d³` then gives the desired
finite contribution `A/d³ · (constant)` after taking the standard-
part — *modulo verifying Hoefsmit additivity*.

**What needs checking.** Two structural lemmas:

1. **Hoefsmit additivity on disjoint sums.** Does
   `Geom(L₁ ⊔ L₂) = Geom(L₁) + Geom(L₂)` hold for the current
   Hoefsmit pipeline? If yes, sub-problem (1) reduces to
   "construct a plate-bounded `L = ⊔ⁿ ⊙_n`".

2. **Möbius energy and disjoint unions.** Since `Geom` is built
   on Möbius energy + Hoefsmit normalisation, the Möbius-energy
   regularisation
   ([`prf:mobius-energy`](../../content/quantum-observable-universe/appendix-surreals/mobius-energy-proof.md))
   determines additivity behaviour. Standard Möbius energy IS
   additive on disjoint unions when the cross-term integral
   `∫∫ 1/|x-y|² dx dy` converges (which it does for components
   at non-zero separation).

**Status.** Plausible but not pursued; the disjoint-union lemma
should be checkable by reading the existing Hoefsmit code, but
the *categorical construction* of a plate-bounded disjoint family
of unknots is still novel content.

**Recommended follow-up.** Check the existing Hoefsmit code for
explicit disjoint-union behaviour:

```bash
grep -B2 -A8 "disjoint\|⊔\|sqcup" \
  folio-assistant/computations/hecke_core.py \
  content/quantum-observable-universe/lean/QOU/AppendixSurreals/HoefsmitBridge.lean
```

If the additivity lemma is already implicit, this route reduces
the conjecture to "existence of a plate-bounded multi-unknot
configuration" — a simpler question than the original existence
sub-problem.

## Route C — Functorial uniqueness (option 4e from the related Bohr-radius proposition)

**Sketch.** Same idea as
[`prop:bohr-radius-categorical`](../../content/quantum-observable-universe/observations/bohr-radius-categorical.md)
round 4 option 4e: prove that any q-smooth archimedean functor
`ρ_∞ : Ẑ[q] → ℝ` satisfying `ρ_∞|_{q=1} = standard QED Casimir`
must be the unique functor that reproduces `π² ℏc/(240 d⁴)` as the
force per area. This reduces the empirical input from "match the
textbook prefactor" to "match at one point", which is
philosophically equivalent to standard QED at `q = 1` but more
defensible structurally.

**Status.** Not pursued in this audit. Same caveat as the
Bohr-radius proposition: still appeals to standard physics at the
classical limit, so it's not a "fully internal QOU derivation" —
but it does narrow the appeal to a single matching condition.

## Why we did not pursue these in the paper

These routes are speculative — they identify *where* the proof
might land, not *what* the proof is. Including them in the
conjecture's `.md` would dilute the conjecture statement with
investigation noise. Per CLAUDE.md "Author notes vs. scholarly
prose" (§4d), this is exactly the kind of material that belongs
in an audit doc, not in the paper's narrative prose.

When (and if) any of routes A–C closes, the resulting derivation
belongs in a *new proposition* (or a refined conjecture), not as
an addendum to the original block.

## Summary

| Route | Sub-problem | Empirical result | Status |
|---|---|---|---|
| A — q-deformed ζ | 3 (prefactor) | No closed-form match; closest candidate `2·π²/(720·[2]_q)` at 0.54% residue | Null result documented |
| B — Hoefsmit additivity | 1 (existence) | Not run; needs reading of Hoefsmit code | Recommended next step |
| C — Functorial uniqueness | 1+3 | Not pursued; carries same caveat as `prop:bohr-radius-categorical` option 4e | Parked |

**Tractability ranking (revised after this session):**

1. **Route B** — most concrete: a single lemma check on existing
   Hoefsmit code could partially close sub-problem 1.
2. **Route A with Cherednik q-zeta** — second-most-concrete; the
   Cherednik definition uses Macdonald operators and may have a
   natural Hecke-trace interpretation.
3. **Route C** — least appealing because it externalises the
   reduction to standard physics, but most likely to succeed if
   one accepts the q → 1 boundary condition.

**Recommendation to next agent.** Start with Route B
disjoint-union check (low-cost, high-information). Defer Routes A
and C until B has been ruled in or out.
