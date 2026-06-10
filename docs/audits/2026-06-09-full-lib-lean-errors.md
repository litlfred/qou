# Audit — full-lib Lean build errors (2026-06-09)

## Goal

Drive `lake build QOU` (the QOU paper library) to a clean compile by
fixing the residual Lean errors that have accumulated on `main` —
the tranche deferred at the end of the Subsingleton-axiom remediation
(PR #2070), where ~340 error lines were observed in files this branch
did not touch (heartbeat timeouts, `unfold` failures, a syntax error).

## Method

- Build locally with `lake build QOU` (no `-R` — the `--reconfigure`
  flag triggers a destructive dependency re-clone in this sandbox;
  plain build trusts the manifest-lock). mathlib oleans restored from
  the `lake-cache/qou-v4-24-0` orphan branch.
- Enumerate erroring modules, classify (syntax / heartbeat / `unfold`
  / synth-failure / real-math-gap), fix in dependency order, verify
  each via direct `lean` compile against the built oleans.

## Findings (in progress)

Error categories observed in the local `lake build QOU`:

1. **`λ`-prefixed identifiers** (the partition symbol `λ` used as a Lean
   identifier, e.g. `λ_Z`, `λ_N`) — `λ` is Lean 4's lambda token, so
   `structure … where λ_Z : …` no longer parses (`unexpected token 'λ'`).
   Confirmed by a minimal compile on the pinned v4.24.0. A toolchain-bump
   regression; ~dozen+ files affected (the dominant pattern; e.g.
   `LRFusion.lean` had 20 cascade errors from this).
2. **`field_simp; ring` on q-integer identities** — `field_simp` (with
   `q ≠ 0` in scope) rewrites `q⁻¹ → 1/q`, then cannot match the
   `q − q⁻¹ ≠ 0` denominator hypothesis, leaving unsolved goals. Fix:
   clear the denominator with `div_eq_iff hq` (no `q⁻¹` rewrite) +
   `ring`, or `linear_combination (q−q⁻¹) * (q*q⁻¹=1)` where the identity
   genuinely needs `q·q⁻¹ = 1`.
3. **Forward references** — a `def`/`theorem` used before its
   declaration (`qFactorial`, `qFactorial_zero`). Fix: reorder, or a
   local definitional `have … := rfl`.
4. **`unfold X Y Z <;>`** where not all of `X Y Z` appear in each goal —
   `unfold` errors on an absent target. Fix: `norm_num [X, Y, Z]` /
   `simp only [X, Y, Z]`.

5. **Mathlib-bump tightening on the SDP infrastructure** (the
   foundational blocker — `SDPRealUniqueness` / `SDPEmptyConstraints`
   are low in the import DAG, so their errors *cascade-block the whole
   build*; until fixed, every downstream module reports "depends on
   errored module" and 0 useful oleans are produced):
   - `Matrix.PosDef.one` now requires `[StarOrderedRing R]` — the file
     declared only `[StarRing R]`. Fix: add `[StarOrderedRing R]` to the
     `variable` block (Lean auto-includes it only where used).
   - The SDP constraint-index operations (`dualSlack`, `objAt`,
     `constraint i`) now require `[Fintype ι]` — dropped from the
     `SlaterStrictComplementarityKernel` class field + the cited axiom
     binders. Fix: add `[Fintype ι]` to both `∀`-binders (6 synth
     failures → 0).
   - Dependent `rw` through a subtype coercion `↑⟨Φ, h_feas, …⟩` →
     "motive is not type correct" (rewriting `Φ` breaks `h_feas`'s
     dependent type). Fix: prove `Φ₁ = Φ₂` transitively via
     `(h₁ : Φ₁ = Φ*).trans (h₂ : Φ₂ = Φ*).symm` — no `rw`.
   - Orphaned docstring (theorem refactored to class+axiom in the
     §3b-cond migration) left two stacked `/--` blocks →
     "unexpected token '/--'". Fix: demote the stale one to a `/- … -/`
     comment.

## Fixes applied (per-commit)

| Commit | File(s) | Fix | Verified |
|--------|---------|-----|----------|
| — | `WedderburnMassFormula` | `unfold` → `norm_num [...]` (cat 4) | ✅ exit 0 |
| — | `GaugeFieldFluidDynamics` | `qFactorial` reorder + `div_eq_iff`/`linear_combination` (cat 2/3) + `λ_j`→`lam_j` | ✅ exit 0 |
| `aa5f4283` | `HeckeAlgebra/LRFusion` | `λ_Z/λ_N/λ_A` → `ydZ/ydN/ydA` (cat 1) | ✅ exit 0 |
| `9e52e29f` | `Hecke/Hoefsmit`, `Archimedean/shell_structure_eigenvalues` | `λZ1N2`/`λ_plus`… → `lam*` (cat 1) | mechanical-checked |
| `6c8166b7` | `ParticleInteractions/ground_state_ordering` | `λ_plus/λ_minus` → `lam_*` (cat 1) | mechanical-checked |
| `8f9dcb8e` | `MathlibExt/SDPRealUniqueness` | orphaned docstring + `[Fintype ι]`×6 + rewrite-motive×2 (cat 5) | ✅ exit 0 (3127 jobs) |
| `6bdcf5da` | `MathlibExt/SDPEmptyConstraints` | `[StarOrderedRing R]` (cat 5) | ✅ exit 0 (3127 jobs) |
| `47c6b5e0` | 17 files | `λ_*` → `lam_*` targeted batch (cat 1) | mechanical-checked |

**Verification method.** Each structurally-substantive fix was confirmed
by a targeted **cone-build** (`lake build QOU.<Module>`, `exit 0`). The
mechanical λ-renames were checked by: target-name collision scan (0 prior
uses), lambda-binder false-positive scan (`lam_x =>` signature absent),
residual-λ scan (0 code `λ_`-identifiers remain in renamed files), and
cross-tree downstream-reference scan (only comment-`λ` residuals). A full
`lake build QOU` pass over all 25 together is the final local gate; CI is
the authoritative gate once Actions billing clears.

**Comment-only `λ` (false positives — left intact):**
`WenzlSchurElement`, `DeltaLambdaSignRule`, `WenzlBridgeConcrete`,
`SkewSYT` — their `λ` occurrences are all inside docstrings/`--` comments.

## Scope correction (2026-06-10) — tightened to in-closure files

A classification of the 25 touched `.lean` files against the
`lake build QOU` closure (the root `QOU.lean` aggregator's 92 imports
+ transitive cone) revealed that **14 of them are orphan content-block
stubs** (`imported-by = 0`) — never compiled by `lake build QOU`, so
their λ-parse errors were never part of the failing build, and some
carry deeper pre-existing issues (e.g. `integer_stability` has no
imports at all → `ℝ` unknown). Those 14 renames were **dropped** from
this PR (restored to `main`); they are harmless latent fixes but not
build fixes, and belong with a future wiring effort.

**This PR is now the 10 in-closure files only:** `SDPRealUniqueness`,
`SDPEmptyConstraints` (the foundational unblock), `GaugeFieldFluidDynamics`,
`WedderburnMassFormula`, `LRFusion`, `Hoefsmit`, `JonesMarkovWenzl`,
`QHeckeSeminormalCharacterClosure`, `BringsSurface`, `atomic_lp_stability`.

**Remaining in-closure errors (follow-up tranche, pre-existing, NOT in
this PR):** `HeckeH3` (`kernel declaration has metavariables` + `simp`
failure — a real proof bug), `Hecke/Generators` (`Unknown identifier
'Algebra'` — missing import), plus likely more deeper in the closure.
These block a fully-green `lake build QOU` and are diverse (proof bugs +
imports), so they are a separate tranche rather than mechanical renames.
