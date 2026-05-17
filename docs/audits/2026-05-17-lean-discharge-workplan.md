# Lean discharge workplan — remaining 58 sorries (post-batch)

After the auto-batch discharge of 44 single-sorry theorems via the
`scripts/lean_auto_discharge.py` script, **72 sorries remain** in QOU
Lean. Of those, **14 are intentional** (roadmap stubs, SnapPy bridge,
§3b-cond conjecture instances, by-design false-as-stated) — those
should NOT be discharged.

The **58 actionable sorries** split into:

- **5 single-sorry files** the auto-script couldn't parse (manual)
- **53 multi-sorry deep theorems** (per-theorem care)

## Tier 1 — single-sorry, manual (5 files)

These follow the same §3b-cond pattern as the auto-batch but have
parsing quirks (multi-line return types, complex binders).

| File | Path | Strategy |
|---|---|---|
| `habiro-residue-sum-equivalence.lean` | braids-and-knots/ | Read theorem, copy signature to axiom |
| `quark-antiquark-production.lean` | descartes-universe/ | Same |
| `shell-closure-normal-form.lean` | descartes-universe/ | Same |
| `qou-motivic-galois-instance.lean` | lifting-and-descent/ | Same |
| `StaircaseCornerHook.lean` | lean/QOU/ | Same |

**Estimated effort:** ~30 minutes per file, can be done in one batch.

## Tier 2 — multi-sorry simple (8 files, ~20 sorries)

Files with 2-3 sorries that are independent theorems (each can be
discharged via §3b-cond axiom-citation independently).

| File | # | Citations |
|---|---|---|
| `transfer-matrix-level-independence.lean` | 2 | Hoefsmit; Markov trace |
| `figure-eight-branching-rule.lean` | 2 | Murakami-Murakami |
| `kashaev-volume-conjecture.lean` | 2 | Kashaev 1997 |
| `w-boson-mass-discrepancy.lean` | 2 | CODATA observational |
| `weierstrass-projection.lean` | 2 | Lang Elliptic Functions |
| `em-spectral-completeness.lean` | 2 | Atiyah-Singer; Wu-Yang |
| `descartes-elliptic-curve.lean` | 2 | Lang; Silverman |
| `explicit-formula.lean` | 2 | Weil; Tate |

**Estimated effort:** ~45 minutes per file; ~6 hours total.

## Tier 3 — multi-sorry deep (12 files, ~33 sorries)

These have structural / interdependent sorries that need careful
analysis.

| File | # | Open structural piece |
|---|---|---|
| `chi-std-pernucleon-closed-form.lean` | 2 | Per-nucleon shift closed form |
| `q-casimir.lean` | 6 | Multiple q-Casimir identities |
| `vertex-algebra-relations.lean` | 4 | OPE relations |
| `habiro-expansion-atomic.lean` | 5 | Habiro expansion |
| `hecke-baer-star-generic.lean` | 2 | Baer-* discharge |
| `schur-weyl-mass-decomposition.lean` | 2 | SW decomposition |
| `y-lambda-recipe-from-partition.lean` | 4 | y_λ closed form |
| `skein-finiteness-bound.lean` | 3 | Skein bound |
| `hasse-weil-bound.lean` | 3 | Weil RH |
| `macroscopic-stability-equivalence.lean` | 2 | Macroscopic stability |
| `Hecke/Hoefsmit.lean` | 2 | Hoefsmit matrices |
| `q-beta-spectral-bridge.lean` | 2 | Q-β spectral bridge |

**Estimated effort:** 2-3 hours per file; ~25-35 hours total.

## Implementation order

Recommended sequence:
1. **Tier 1 (5 files)** — quick wins, same §3b-cond pattern (this session)
2. **Tier 2 (8 files)** — each discharges 2-3 sorries via standard citations (this session, time permitting)
3. **Tier 3 (12 files)** — multi-session work, requires per-theorem analysis (follow-up)

## Validation

Each batch should be validated by:
- `bun run validate` (zero warnings introduced)
- `lake build QOU` (verify axiom/theorem typecheck) — author-run

## Net forecast

After Tier 1 + Tier 2 completion:
- Tier 1: 58 → 53 sorries
- Tier 2: 53 → ~33 sorries (53 - 20)
- Remaining: 33 deep + 14 intentional = 47 total

After all tiers:
- All actionable sorries discharged via §3b-cond axioms
- Only 14 intentional sorries remain
- All §3b-cond axioms carry bibliographic citations per CLAUDE.md §1
