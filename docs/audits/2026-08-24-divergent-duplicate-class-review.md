# The 21 `DIVERGENT` duplicate-class groups, reviewed

**Date:** 2026-08-24 · **Bean:** `qou-hjf4`
**Inputs:** [`duplicate-class-declaration-census.py`](../../scripts/duplicate-class-declaration-census.py),
[`duplicate-class-divergence-triage.py`](../../scripts/duplicate-class-divergence-triage.py)
**Companion:** [`2026-08-24-faithful-instance-family.md`](2026-08-24-faithful-instance-family.md)

---

## Summary — "21 need the author" was too pessimistic

Reading all 21 field-by-field, they fall into five kinds, and **only six
actually turn on a question of what the paper claims.** The rest are naming
collisions, a systematic summary-class pattern, or differences my triage
over-flagged.

| kind | groups | needs the author? |
|---|---|---|
| A. Cosmetic — same statement, different spelling | 2 | **no** — triage over-flagged |
| B. Name collision — unrelated claims sharing a class name | 1 group / 5 files | **no** — rename |
| C. The `core-levi-form` summary pattern | 5 | **no** — one decision covers all five |
| D. Style fork — same concept, two formalisation idioms | 3 | probably not |
| E. Genuinely different claims | **6** | **yes** |

---

## A. Cosmetic (2) — my triage over-flagged these

The comparison is intentionally conservative (a false `DIVERGENT` costs a read;
a false `IDENTICAL` could delete a statement). These two are the cost of that
choice.

**`GradedTraceResidueSplit`** [`QOU.BraidKnot`] — same eight fields; two differ
only by name qualification inside the class that declares them:

    smooth = GradedTraceResidueSplit.gradedTrace q element     (library)
    smooth = gradedTrace q element                             (sibling)

**`R5FullWitness`** [`QOU.BraidKnot`] — same seven fields; one bound written
two ways, and they are the same number:

    |primal_obj - dual_obj| ≤ (10 : ℝ)⁻¹^6      (library)
    |primal_obj - dual_obj| ≤ (1e-6 : ℝ)        (sibling)

Both are `IDENTICAL` in substance and can be resolved by import, like
`QOU.PhiQJSJ` was.

## B. Name collision, not a fork (1 group, 5 files) — rename

**`QIntegerMassFormula`** [`QOU.Molecular`] — five *library* files each declare
a class of this name, each with exactly **one** field, and all five fields are
different:

| file | its single field |
|---|---|
| `benzene_threading_emergence.lean` | `threading_minimises` |
| `ch4_lp_dual_binding.lean` | `bonds_symmetric` |
| `co2_lp_dual_binding.lean` | `symmetric_minimises` |
| `co_lp_dual_binding.lean` | `triple_minimises` |
| `h2_lp_dual_binding.lean` | `ground_state_minimises` |

These are five unrelated per-molecule claims that happen to share a name — and
that name belongs to a *different* class in `QOU.Interactions` (the seven-term
nuclear binding formula). Nothing here is a fork of anything, so there is no
canonical copy to choose: **the fix is renaming**, e.g.
`H2GroundStateMinimises`. Mechanical, no authorial input.

This is also the sharpest collision risk in the corpus: five same-named classes
in one namespace, so any two of these modules in one import closure clash.

## C. The `core-levi-form` summary pattern (5) — one decision covers all five

`fluid-dynamics/core-levi-form.lean` declares **five** classes that are each
also declared, in full, by a dedicated file in the same namespace:

| class | `core-levi-form.lean` | the full declaration |
|---|---|---|
| `QAubinLions` | `exists_compactness_constant` | `q-aubin-lions.lean` — `compactness_threshold` |
| `NSCounterexample` | `exists_singularity_time` | `p5-counterexample.lean` — 4 fields |
| `CriticalExponent` | `alpha_three_eq_four` | `p2-critical-exponent.lean` — 5 fields |
| `RegularityBreakdown` | `exists_breakdown_measure` | `regularity-breakdown.lean` — `critical_reynolds` |
| `BlowupYekutieli` | `exists_blowup_rate` | `p3-blowup-yekutieli.lean` — 3 fields |

The pattern is uniform: `core-levi-form` carries a one-field *existence*
summary; the dedicated file carries the construction. That reads as deliberate
— a lightweight interface — but implemented as five same-named classes in one
namespace rather than as an abstraction over them, so it collides. **One
decision (rename the summaries, or have them `extends` the full versions)
resolves all five**, and it is a structuring choice rather than a claim about
the physics.

## D. Style fork — same concept, two idioms (3)

Three library/sibling pairs where the library copy uses an `impl_*`-prefixed
field style and the sibling uses mathematical names:

- **`DiscreteVortexSpectrumContext`** — sibling 15 fields (`qInt`, `hbar`, `Lq`,
  `energy_level`, `classical_limit`, …) vs library 13 (`q_int`, `hbar_q`, `L_q`,
  `impl_spin_levels`, `impl_classical_kelvin_limit`, …).
- **`RootOfUnityTruncationContext`** — sibling 8 (`tStar`, `coreAspect`,
  `blowup_iff_nondegenerate`) vs library 12 (`j_max`, `impl_root_unity`,
  `impl_blowup_iff_levi_iff_kappa`).
- **`VorticityLowerBoundContext`** — sibling 7 (`vortNorm`,
  `bkmIntegralDiverges`) vs library 8 (`CategoricalObj`, `bound_active`,
  `impl_lower_bound`).

The field *names* differ throughout, so these are not textual duplicates, but
the correspondence is close enough that they look like the same content written
twice rather than two claims. Probably resolvable without an authorial call —
but confirming that means reading three pairs in full, which is real work and is
not done here.

## E. Genuinely different claims (6) — these need the author

### E1. `BorromeanQuark` [`QOU.Archimedean`] — *which* mass does the volume calibrate?

Both copies carry a field named `volume_calibrates_mass`, with **different
types**:

    ∀ q : ℝ, q > 1 → bare_mass q        = borromean_volume / (1 - 1/q)^2   (sibling)
    ∀ q : ℝ, q > 1 → topological_mass q = borromean_volume / (1 - 1/q)^2   (library)

Same equation, different left-hand side. The sibling also carries
`is_baryon_realisation` and `is_baryon_realisation_holds`, which the library
copy does not. This is a claim about the physics, not about the code.

### E2. `BorromeanQuark` [`<root>`] — three more, at root namespace

`orbital-fourier-decomposition.lean` (`orbitalDim`, `decomposition_law`),
`reidemeister-mass-invariance.lean` (`volume_calibrates_mass`) and
`hydrogen-shell-writhe.lean` (`bareMass`, `bareMass_pos`) each declare a
`BorromeanQuark` **at root namespace**, with disjoint fields. Root-namespace
declarations collide with everything, so this is the widest-reach group.
Whether these are three facets of one object or three unrelated uses of a name
is the question.

### E3. `QIntegerMassFormula` [`QOU.Interactions`] — the AME gate

Already analysed in the companion audit. Same four fields; `fits_AME` differs:

    ∀ … (B_AME : ℝ) [IsAMEValue Z N B_AME], ∃ δ, …    (library — gated)
    ∀ … (B_AME : ℝ),                        ∃ δ, …    (sibling — arbitrary real)

The sibling's form is false as written; the library's gate carries the
conjecture inside it (`IsAMEValue.fits_bound`). Neither is currently right.

### E4. `HeckeAnyonicSubstrate` [`QOU.BraidKnot`] and E5. `KnotFactorFrobeniusPairing` [`QOU.BraidKnot`]

Both have the same shape: the library copy carries four content-bearing fields
(`NormalForm`, `braidAction`, `heckeQuadratic`, `anyonic_holds`;
`markov_trace_q`, `frobenius_pairing_q`, `knot_factor`, `factorisation_holds`)
and the sibling carries a **single field named `holds`**. A one-field `holds`
against a four-field construction is close to the `STUB` verdict, but the field
is not `True`-typed so the triage did not call it one. Whether the sibling is a
deliberate opaque interface or an abandoned placeholder decides it.

### E6. `QuantumComputationalUniversality` — disjoint fields, same name and namespace

Sibling: `quadratic_level`, `universality`, `descent_decomposition`,
`information_content`. Library: `reachable`, `dense`, `cost`, `cost_antitone`.
Four fields each, **no overlap at all** — two different axiomatisations of
computational universality sharing a name.

*(`MotivicGaloisCharacter` [`QOU.LiftingDescent`] is the seventh of this kind —
two fields each, `frobenius_realize_ne_zero` vs `almost_everywhere_nontrivial`
— counted under E6's kind but listed separately for completeness.)*

---

## Recommendation

Kinds A, B and C — **8 groups, 12 files** — can be resolved without any
authorial input: two by import, five by renaming the `core-levi-form`
summaries, one by renaming five per-molecule classes. That removes the widest
collision risk in the corpus (the five same-named `QOU.Molecular` classes) and
leaves a much smaller review surface.

Kind E is the real queue, and **E1/E2 (`BorromeanQuark`) is where I would start
— five declarations across two namespaces disagreeing about whether the
Borromean volume calibrates the bare or the topological mass** is a question
about the framework, not about Lean.
