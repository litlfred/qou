# Hoefsmit Tier 2 formal-adjoin migration plan

**Companion PR**: [#1640](https://github.com/litlfred/qou/pull/1640) (q-usage audit scaffold + dispensation plan)
**Audit reference**: `q-usage-positivity-implicit` criterion in
[`docs/audits/2026-06-01-q-usage-dispensation-plan.md`](2026-06-01-q-usage-dispensation-plan.md)
§Policy B

## Goal

Replace `Real.sqrt q` (archimedean specialisation) with the generic
formal-adjoin pattern `b : R, h : b² = b_sq q` (categorical, works
over any commutative ring). Aligns with the author's strongest stated
preference: keep `q` symbolic / generic-`R` as long as possible.

## Scope (4 Hoefsmit-pattern blocks)

| Block | File | Current Real.sqrt usage |
|---|---|---|
| `rem:markov-axioms-primitive` | `braids-and-knots/markov-axioms-primitive.lean` | `markovZax (q : ℝ) := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)` |
| `rem:braid-group-n-strand` | `braids-and-knots/braid-group-n-strand.lean` | Imports `markovZax`; uses `markovZ` definition |
| `prop:hoefsmit-V21-cos-symmetrization` | `mass-theory/hoefsmit-V21-cos-symmetrization.lean` | Matrix entries `Real.sqrt (hoefsmit_b_sq q)` |
| `rem:chi-v21-hoefsmit-matrix-derivation` | `mass-endomorphism/chi-v21-hoefsmit-matrix-derivation.lean` | Matrix entries `Real.sqrt (hoefsmit_v21_b_sq q)` |

Additional callsites of `markovZax`:
- `braids-and-knots/markov-trace-inductive-limit.lean`
- `mass-theory/markov-trace-product.lean`

## Migration pattern

### Before (Tier 5 — real specialisation)

```lean
noncomputable def markovZax (q : ℝ) : ℝ :=
  1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

class MarkovTraceAxioms (q : ℝ) : Type where
  ...
  tau_stab_factor_eq_z : tau_stab_factor = markovZax q
```

### After (Tier 2 — formal adjoin)

```lean
-- Generic-R primary definition. `u` is the formal square root of q
-- (i.e. `u² = q`); over ℝ with `0 < q`, instantiate `u := Real.sqrt q`.
def markovZax {R : Type*} [Field R] (u : R) : R := u / (u^2 + 1)

class MarkovTraceAxioms {R : Type*} [Field R] (u : R) : Type where
  ...
  tau_stab_factor_eq_z : tau_stab_factor = markovZax u

-- Backward-compat archimedean specialisation.
noncomputable def markovZax_real (q : ℝ) (hq : 0 < q) : ℝ :=
  markovZax (Real.sqrt q)
```

Equivalence check: `1 / (u + 1/u) = u / (u² + 1)` for any unit `u`
in a field. Specialising `u := Real.sqrt q` with `0 < q` recovers
the original `Real`-only formula.

### Hoefsmit matrix entries

```lean
-- Before (Tier 5)
noncomputable def hoefsmit_b (q : ℝ) (hq_pos : 0 < hoefsmit_b_sq q) : ℝ :=
  Real.sqrt (hoefsmit_b_sq q)

-- After (Tier 2)
variable {R : Type*} [CommRing R] (q : R)
def hoefsmitMatrix (b : R) (h : b^2 = hoefsmit_b_sq q) :
    Matrix (Fin 2) (Fin 2) R :=
  !![hoefsmit_d1 q, b; b, hoefsmit_d2 q]
```

## Migration order (proposed)

1. **Phase 1** (this PR): Introduce the generic-R variants ALONGSIDE the
   existing `Real`-only definitions; mark the latter as
   `@[deprecated]`. No callsite breakage. Validates the pattern works
   under Lake build.

2. **Phase 2** (follow-up PRs, one per block): migrate callsites of
   `markovZax` to use the generic variant. The 5 callsites are:
   - `markov-axioms-primitive` itself
   - `markov-trace-inductive-limit`
   - `markov-trace-product`
   - `braid-group-n-strand`
   - downstream Hoefsmit matrix users

3. **Phase 3**: Remove the deprecated `Real`-only definitions. Audit
   re-sweep confirms `q-usage-positivity-implicit` warns drop to zero.

## What's NOT in scope

The other 6 `q-usage-positivity-implicit` warns
(`toffoli-lp-stability`, `qbeta-c-k-closed-forms`, `dilog-equivalence`,
`dilogarithm-archimedean-limit`, `ck-extraction-from-algebraic-rules`,
`q-beta-spectral-bridge`) are in archimedean chapters
(`mass-theory`, `particle-interactions`, `information-theory`) where
the archimedean specialisation is the *intended* form. For those,
adding `hq : 0 < q` to the existing signature (Tier 5) is the
appropriate fix — not Tier 2 formal adjoin. Tracked separately.

## Cross-references

- Dispensation plan: [`2026-06-01-q-usage-dispensation-plan.md`](2026-06-01-q-usage-dispensation-plan.md)
  §Policy B
- Audit witness: [`2026-06-01-q-usage-audit.witness.json`](2026-06-01-q-usage-audit.witness.json)
- Watcher skill: [`q-usage-watcher`](../../.claude/skills/local/q-usage-watcher.md)
- Base-ring convention: [CLAUDE.md §7c](../../CLAUDE.md)
