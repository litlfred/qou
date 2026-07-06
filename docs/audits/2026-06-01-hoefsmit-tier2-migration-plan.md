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
| `rem:markov-axioms-primitive` | `braids-and-knots/markov-axioms-primitive.lean` | `markovZax_legacy (q : ℝ) := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)` (post-PR-1658 name; was `markovZax` pre-rename) |
| `rem:braid-group-n-strand` | `braids-and-knots/braid-group-n-strand.lean` | Locally defines `markovZN (q : ℝ) := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)` — an independent copy of the same formula, NOT an import of `markovZax_legacy` |
| `prop:hoefsmit-V21-cos-symmetrization` | `mass-theory/hoefsmit-V21-cos-symmetrization.lean` | Matrix entries `Real.sqrt (hoefsmit_b_sq q)` |
| `rem:chi-v21-hoefsmit-matrix-derivation` | `mass-endomorphism/chi-v21-hoefsmit-matrix-derivation.lean` | Matrix entries `Real.sqrt (hoefsmit_v21_b_sq q)` |

Adjacent files (NOT direct callsites of `markovZax_legacy`):
- `braids-and-knots/markov-trace-inductive-limit.lean` — uses `markovZN q` (from `braid-group-n-strand`); references `markovZax` only in a doc comment.
- `mass-theory/markov-trace-product.lean` — uses an independent abstract parameter `z : R_q`; no `markovZax` / `markovZN` / `Real.sqrt` reference. Out of scope for this migration.

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

1. **Phase 1** (this PR — DONE for all 4 blocks): Introduce the
   generic-R variants ALONGSIDE the existing `Real`-only definitions;
   mark the latter as `@[deprecated]`. No callsite breakage.

   Per-block scaffold status:
   - `markov-axioms-primitive.lean` — DONE: `markovZax (u : R)` /
     `markovZax_real q hq` / `markovZax_legacy` (deprecated).
   - `braid-group-n-strand.lean` — DONE: `markovZN (u : R)` /
     `markovZN_real q hq` / `markovZN_legacy` (deprecated); in-file
     callsite at `MarkovTraceN.tau_stab_factor_eq_z` routed to
     `markovZN_legacy`; downstream callsite in
     `markov-trace-inductive-limit.lean` also routed to `_legacy`.
   - `hoefsmit-V21-cos-symmetrization.lean` — DONE: `markovZ (u : R)`
     + `markovZ_legacy` (deprecated); `hoefsmit_sigma1_gen d1 d2 b`
     (Tier 2 matrix form) + `hoefsmit_sigma1_legacy` (deprecated);
     existing `hoefsmit_sigma1` kept as a backward-compat alias to
     `hoefsmit_sigma1_legacy` so the existing theorems compile
     unchanged (with deprecation warnings).
   - `chi-v21-hoefsmit-matrix-derivation.lean` — DONE: `sigma1_v21_gen
     d1 d2 b` (Tier 2 matrix form) + `sigma1_v21_legacy` (deprecated);
     existing `sigma1_v21` kept as a backward-compat alias.

2. **Phase 2** (partial — this PR + remaining follow-ups):
   migrate callsites to the generic forms, file-by-file.

   Done in this PR:
   - `markov-axioms-primitive.lean` — generic-R variants
     `markov_iterated_stab_gen` and `disjoint_product_factorisation_gen`
     added alongside the legacy archimedean variants. Legacy variants
     now route through the generic forms (so the algebraic content
     lives at the generic level).

   Remaining for follow-up PRs:
   - `markov-axioms-primitive.lean` — refactor `MarkovTraceAxioms`
     class to take `{R : Type*} [Field R] (u : R)` instead of `(q :
     ℝ)`; ripple-update downstream instances in
     `markov-trace-inductive-limit.lean` and elsewhere. Larger Lean
     work — best done on a dedicated follow-up branch.
   - `braid-group-n-strand` — apply the same Tier 2 scaffold pattern
     to the locally-defined `markovZN` (rename to `markovZN_legacy`,
     introduce generic `markovZN (u : R)` and `markovZN_real`).
   - `markov-trace-inductive-limit` — uses `markovZN q` from
     braid-group-n-strand; follow-up after that file migrates.
   - `hoefsmit-V21-cos-symmetrization` + `chi-v21-hoefsmit-matrix-
     derivation` — apply the formal-adjoin pattern to the matrix
     entries `Real.sqrt (hoefsmit_b_sq q)`.

   Out of scope: `mass-theory/markov-trace-product.lean` uses an
   abstract `z : R_q` parameter (no `Real.sqrt` reference); already
   on the Tier 2 / generic side.

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
- Base-ring convention: [AGENTS.md §7c](../../AGENTS.md)
