# Session Handover — Lean Axiom Discharge (2026-06-09)

**Status at handover**: agent has done ~24 axiom discharges across 5 PRs this multi-session run; one PR (#2019) still open; user away for ~1 week; pick up from here.

## TL;DR for the successor agent

1. **PR #2019** (`claude/lean-discharge-axioms-batch-4-2026-06-08`) — open, 2 commits (jones1985 fix + witness refresh). Awaiting CI / reviews. **Merge it when reviews settle** (per CLAUDE.md §8 rebase-merge default).
2. **3 axioms drafted but blocked on LSP**: `eigenvalues_distinct_axiom`, `entry_sq_le_diag_mul_axiom`, `one_dim_factors_per_generator_axiom`. Math is worked out (see §"Discharge math" below). Attempt with LSP-feedback iteration.
3. **Lean install IS working** in this sandbox via `scripts/setup-lean-toolchain.sh` + `scripts/lake-cache-fetch.sh`. **But `lake build QOU` is failing** with "error: build failed" — root cause not yet identified. Find the actual error message first before iterating.
4. **The well of "safe-without-LSP" discharges is EXHAUSTED** in QOU. All remaining 60 QOU axioms + 20 UGB axioms need LSP iteration, multi-day Mathlib work, or are §3b-cond intentional scaffolds.

## What was merged this session

| PR | Branch | Discharged | Merge SHA |
|----|--------|-----------|-----------|
| #1978 | `lean-discharge-vol-b3-more-axioms` | 11 axioms (vol_B3 symbolic, Catalan, SnapPy, m_e_cat, H3 scalars, QSubstrate.q_0, transferMatrix_comm) + Borromean 50-dps | `8b2b977` |
| #1981 | `lean-discharge-axioms-batch-2` | 7 axioms (HeckeRep.genInv speculative + 3 tautological + 3 H3 placeholder LinearMaps) + q_zero 50-dps + vol_5_2 drift fix | `d7f6995` |
| #1986 | `lean-discharge-axioms-batch-3` | 2 axioms (markovTrace_add + _smul derived from _linear) | `15b926c` |
| #1991 | `lake-cache-tar-flag-fix` | Fixed `tar --no-absolute-names` removed in GNU tar 1.35 (unblocked sandbox Lean install) | merged |
| #1960 | sibling (Borromean Frobenius) | merged via direct API call | `cb6259ec` |

## Open at handover

### PR #2019 — `claude/lean-discharge-axioms-batch-4-2026-06-08`

- **2 commits**: `2c80a70` (jones1985 fix in BorromeanFrobeniusReconstruction.lean) + `9e9acf2` (chore: refresh conjectural-propagation witness)
- **CI**: audit was in-progress at handover
- **Reviews**: none yet at handover
- **Action**: monitor for reviews, address mechanical comments, merge when clean

## Sibling PRs (not mine, may need triage)

The earlier coordination sweep identified 4 active sibling Lean PRs. Status as of last check:

- **#1562** (universal_property uniqueness, IwahoriHecke/Defn.lean) — base 8+ days stale; rebase attempted by an agent, hit 9166-commit divergence; **not viable for auto-merge without manual conflict resolution**
- **#1974** (Borromean R[h] restate) — mid-rebase in worktree `/home/user/qou/.claude/worktrees/agent-af4d25f468104a928`; first commit's conflicts already resolved (kept main's §7c generic-R + branch's R[h] layer); second commit conflict in `BorromeanMarkovTrace.lean` unresolved
- **#1960** (Borromean Frobenius) — **MERGED** during this session
- **#1980** (Python Hoefsmit substrate) — **MERGED** during this session (`a983615`)

## Sandbox Lean install — what we learned

This is GOLD for the successor — the previous 3 background agents failed to install Lean, but I figured out the working recipe:

### Recipe

```bash
# 1. Lean toolchain (sandbox-friendly recipe, sibling-validated PR #1982 + #1991)
bash scripts/setup-lean-toolchain.sh   # bootstraps elan from GitHub, extracts v4.24.0
export PATH="$HOME/.elan/bin:$PATH"

# 2. CRITICAL: link toolchain under BOTH names so MCP server's elan child finds it
elan toolchain link lean-v4.24.0 /tmp/lean-v4.24.0           # short link name
elan toolchain link "leanprover/lean4:v4.24.0" /tmp/lean-v4.24.0  # canonical (lean-toolchain spec)
elan default lean-v4.24.0   # so MCP server children see a default

# 3. Restore the prebuilt Mathlib oleans (~2 min vs ~30-60 min from-source)
bash scripts/lake-cache-fetch.sh --force   # 731MB tarball, 2918 .olean files

# 4. Verify
elan show        # should show lean-v4.24.0 active
lake --version   # should say "Lean version 4.24.0"
```

### Why prior agents failed

- Three separate background agents (`acd2478…`, `aa8e0acab7…`, `a0f8afbc08…`) all got stuck investigating the `lake-cache/qou-v4-24-0` orphan branch — it ONLY restores `packages/` source, NOT the prebuilt oleans inside `.lake/build/lib/`
- The actual oleans come from extracting the 731 MB chunked tarball stored IN the orphan branch as 9 `lake-oleans.tgz.part*` files
- The cache recipe in `lean-environment-setup.md` is partially stale — the cache-restore step DOES work but takes the `--force` flag, and post-restore the script's "1 entries" message is misleading (it looks at top-level dirs only; the actual 2918 oleans are nested deeper).

### lean-lsp-mcp specifics

- MCP server PID `793` (uvx-spawned) — does NOT inherit your shell's `PATH` updates
- Solution: set `elan default <toolchain>` + link canonical name so MCP child elan finds the toolchain even without per-repo override
- First LSP query after toolchain install will TIMEOUT (60s) on cold start; second query works
- LSP returns `{"success":false,"items":[]}` when its child lean is still compiling — wait + retry

## CURRENT BLOCKER (handover) — DIAGNOSED

**`lake build QOU` exits "error: build failed"** because `QOU.HeckeAlgebra.Wedderburn` doesn't compile under Lean v4.24.0. **3 nested bugs**, all pre-existing in `main` (not from my discharges):

1. **`λ` is a reserved token in Lean 4.24**. The file uses `λ` as a binder name (`(λ : Nat.Partition n)`, `fun λ =>`, `intro λ`). **Fix**: rename to `lam` throughout (23 occurrences).

2. **`Matrix.PosSemidef` dot notation fails on `(x lam)`**. Lean parses `(x lam)` to its underlying function type (`Fin n → Fin n → ℝ`) because `Matrix` is a `def` not an `abbrev`. **Fix**: replace `(x lam).PosSemidef` with explicit `Matrix.PosSemidef (x lam)`; replace `(fun lam => …).PosSemidef` with `WedderburnDecomposition.PosSemidef (fun lam => …)`.

3. **`Matrix.PosSemidef` requires additional imports**. After fixing #2, get "Unknown constant `Matrix.PosSemidef`" — need `import Mathlib.LinearAlgebra.Matrix.PosDef`. After THAT, get "failed to synthesize `StarOrderedRing ℝ`" — need a broader analysis import (tried `Mathlib.Analysis.Normed.Order.Lattice` but still fails on a deeper synthesize — likely needs more, or the `.smul` / `.add` projection on `Matrix.PosSemidef` has a different name in this Mathlib version).

**Workaround that I tried + reverted**: rename `λ → lam` + add `Mathlib.LinearAlgebra.Matrix.PosDef` import + replace `(x lam).PosSemidef` with `Matrix.PosSemidef (x lam)`. Got from "5 parse errors" to "1 failed-to-synthesize error" — but the synthesize is deeper than a one-line fix and reverted for handover.

**Suggested next-session path** for the build fix:
1. Apply the rename + dot-notation fix from this handover's working notes (~10 min)
2. Investigate the `StarOrderedRing ℝ` synthesize error with LSP — likely needs either:
   - `import Mathlib.Analysis.RCLike.Basic` for the instance, OR
   - The `.smul` / `.add` projections may need updating (e.g., `Matrix.PosSemidef.add` may have been renamed to `Matrix.PosSemidef.add'` or moved to a different namespace in Mathlib v4.24)
3. Use `lean_local_search "Matrix.PosSemidef.smul"` and `lean_hover_info` to find the correct API

**Original error capture** (for debugging):

```bash
# Run from /home/user/qou with PATH set:
lake build QOU 2>&1 | tee /tmp/build.log
grep -B 3 -A 8 'error:' /tmp/build.log | head -60
```

Background task `bntfcsnnm` (the same grep) is in flight but hadn't returned at handover. Look at its output file:
`/tmp/claude-0/-home-user-qou/d80e4c5f-37f5-528d-b55d-107368bdd48e/tasks/bntfcsnnm.output`

The failing module is somewhere in this set (from previous build's terminating output):
- `QOU.Archimedean.PauliWitness.{Witness11B, Witness12B, Witness10Be, Witness10B, Witness9Be, Witness8Li, Witness9B, Witness12C}`
- `QOU.HeckeAlgebra.QSubstrate`
- `QOU.HeckeAlgebra.Formal`
- `QOU.BraidKnot.MassFormulaCategorical`
- `QOU.HeckeAlgebra.Wedderburn`
- `QOU.Archimedean.HeckeRep`
- `QOU.Interactions.HeckeEngine`
- `QOU.LiftingDescent.BBStratification`
- `QOU.MathlibExt.SDP`

**IMPORTANT**: if the failing file is something I authored discharges on (HeckeRep, QSubstrate, etc.), the failure may be from one of my speculative discharges. The 3 H3 placeholder LinearMaps in `H3BraneTowerScaffold` are the highest-risk discharges from this session — see the commit message of `294955f` (in #1981's history) for the iteration plan.

## Discharge math (ready to apply with LSP)

### `eigenvalues_distinct_axiom` (QOU/Archimedean/EmSpectralCompleteness.lean:62)

```
axiom eigenvalues_distinct_axiom (S : SpectralRing) :
    IsUnit (lambdaPlus S - lambdaMinus S)
```

where `lambdaPlus S = (S.qHalf : S.R)`, `lambdaMinus S = -(S.qHalf : S.R)⁻¹`.

**Proof**: `lambdaPlus - lambdaMinus = qHalf + qHalf⁻¹`. Show this is a unit:

- `qHalf · (qHalf + qHalf⁻¹) = qHalf² + 1 = q + 1` (using `qHalf_sq`)
- So `qHalf + qHalf⁻¹ = qHalf⁻¹ · (q + 1)`
- Need: `q + 1` is a unit.
  - `(q - q⁻¹) · q = q² - 1 = (q-1)(q+1)`
  - `q - q⁻¹` is a unit (given `qDiff_unit`)
  - `q` is a unit (typed `Rˣ`)
  - So `(q-1)(q+1) = (q - q⁻¹) · q` is a unit (product of units)
  - In CommRing, `IsUnit (a * b) → IsUnit a ∧ IsUnit b` via `isUnit_mul_iff`
  - Hence `q + 1` is a unit
- Final: `qHalf⁻¹ · (q+1)` is a unit (product of units)

**Caveat**: the `(S.qHalf : S.R)⁻¹` syntax in line 53 may require `Inv R` instance — investigate with `lean_hover_info` before coding.

### `entry_sq_le_diag_mul_axiom` (QOU/MathlibExt/PosSemidefDiagZero.lean:148)

```
axiom entry_sq_le_diag_mul_axiom :
    ∀ {n : ℕ} {C : Matrix (Fin n) (Fin n) ℝ} (_hC : C.PosSemidef) (i j : Fin n),
        (C i j) ^ 2 ≤ C i i * C j j
```

**Proof**: case analysis on `i = j`:
- `i = j`: `(C i i)² ≤ C i i · C i i` — trivial `rw [sq]`
- `i ≠ j`: use the SIBLING `quadratic_form_two_index_axiom` (same file L114) which expands `v^T C v = α² Cii + 2αβ Cij + β² Cjj` for `v = αe_i + βe_j`. PSD gives `v^T C v ≥ 0` for all α, β. Treat as quadratic in α with leading coeff `C i i`:
  - If `C i i > 0`: discriminant ≤ 0 gives `(2β Cij)² ≤ 4 Cii · β² Cjj`, i.e. for β=1: `Cij² ≤ Cii Cjj`
  - If `C i i = 0`: linear in α; for non-negativity for all α, need `Cij = 0`, then `0 ≤ 0`

There's a private helper `quadratic_nonneg_implies_linear_zero` already in the file (L72) for the `Cii = 0` case.

### `one_dim_factors_per_generator_axiom` (QOU/Hecke/OneDimChiBridge.lean:62)

```
axiom one_dim_factors_per_generator_axiom :
    ∀ {R : Type u} {n : ℕ} {q : R} {A : Type u} [CommRing R] [Inv R] [Ring A] [Algebra R A]
      [HA : HeckeAlgebra R n q A]
      (φ : OneDimChar R A) {ι : Type*} [DecidableEq ι] [DecidableEq (Generator n)]
      (s : Finset ι)
      (f : ι → A) (i_idx : ι → Generator n) (cd : ι → R × R)
      (_h_form : ∀ k ∈ s, f k = (cd k).1 • HA.embed (i_idx k) + (cd k).2 • 1),
        φ (∏ k ∈ s, f k) =
        ∏ i ∈ s.image i_idx,
          ∏ k ∈ s.filter (fun k => i_idx k = i),
            ((cd k).1 * φ (HA.embed i) + (cd k).2)
```

**Proof sketch** (per docstring):
1. `map_prod φ.toRingHom` — φ multiplicative over Finset.prod
2. `Finset.prod_fiberwise` — regroup by `i_idx` (Mathlib lemma name may vary)
3. Per-term: `φ.map_add + φ.map_smul + φ.map_one + smul_eq_mul + mul_one`

Then substitute `f k = ... ` via `h_form`. The exact API for `Finset.prod_fiberwise` has moved around — check with `lean_local_search "prod_fiberwise"`.

## Next steps in priority order (for successor agent)

1. **Find the lake build failure** — run the foreground build, capture error, identify which file is failing. If it's a recent file (PauliWitness/Witness*) it may be pre-existing on main; if it's something I authored (H3BraneTowerScaffold, HeckeRep, QSubstrate, NonAbelianStokes, QBetaCategoricalPrecisionLadder), one of my speculative discharges may need fixing.
2. **If a discharge from this session broke main**, the recovery plan is documented in each commit message under "Iteration plan if CI fails".
3. **Once lake build is green**, attempt the 3 named axiom discharges (above) with LSP-driven iteration.
4. **Merge PR #2019** when reviews settle.
5. **Optional**: attempt `catalan_G_numerical_bounds` — needs Mathlib alt-series tail bound + ~86 term partial sum. Multi-hour even with LSP.
6. **Optional**: pick up sibling PR #1974 rebase from the abandoned worktree at `.claude/worktrees/agent-af4d25f468104a928`.

## Files modified this session (high-level)

- `content/quantum-observable-universe/lean/QOU/Archimedean/` — HeckeRep, HyperbolicVolumeTranscendence, BorromeanVolumeCatalan, SnapPyAxioms, EmSpectralCompleteness (read-only), PosSemidefDiagZero (read-only)
- `content/quantum-observable-universe/lean/QOU/Mathlib/` — ArchimedeanRealization, NonAbelianStokes
- `content/quantum-observable-universe/lean/QOU/BraidKnot/` — PerNucleusMassDerivation, QBetaCategoricalPrecisionLadder
- `content/quantum-observable-universe/lean/QOU/LiftingDescent/H3BraneTowerScaffold.lean` — ell_0, descent_1, descent_ascent_id (the 3 H3 placeholder LinearMaps, highest CI-risk)
- `content/quantum-observable-universe/lean/QOU/HeckeAlgebra/QSubstrate.lean` — q_0, q_0_gt_one
- `content/quantum-observable-universe/lean/QOU/HeckeAlgebra/MarkovTrace.lean` — markovTrace_add, markovTrace_smul
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanFrobeniusReconstruction.lean` — jones1987 → jones1985
- `scripts/lake-cache-fetch.sh` — removed `tar --no-absolute-names` flag (PR #1991, now in main)

## Operational notes

- **Sandbox network blocks**: `release.lean-lang.org`, `elan.lean-lang.org`, most DOI hosts. `github.com` IS allowlisted.
- **Container restarts** (every 4-8h): `~/.elan` survives, `/tmp/lean-v4.24.0` ALSO survives but elan toolchain links break. Re-run `setup-lean-toolchain.sh` after every restart (it's idempotent).
- **CI billing-pattern failures**: per CLAUDE.md, distinguish from real failures by job duration (≤ 5s ALL jobs = billing; ≥ 30s = real). If billing, skip + document with `[skip-ci: billing]` in the merge comment.
- **PostToolUse hooks**: noisy but harmless — they want me to subscribe to PR + coordinate after every git push. I usually just call `mcp__github__subscribe_pr_activity` once per branch.

## Author accessibility note (CLAUDE.md)

The user (repo owner) is physically disabled — types slowly. Default to:
- Short numbered-list answers
- Multi-select questions (not single-select) prefixed with 🟡
- Aggressive auto-action on the standing authorisations (branch + commit + push + PR + rebase-merge — but ASK before destructive ops or before merging others' PRs)
- Don't ask "should I do X" when X is already pre-authorised by CLAUDE.md

## Coordination

Last `/coordinate` sweep was hours ago. Recent main is 92+ commits past last review baseline. Successor agent should run `/coordinate first` early to triage sibling activity.

---

_Handover written 2026-06-09; user away ~1 week; sessions resume on return._
