# Coordination — OV tower brick-4 (Specht standard basis) + siblings

**Goal:** formalize `dim S^μ = #SYT(μ)` (brick 4) and the surrounding OV /
Identity-I rep-theory, reducing each deep `sorry` to a single cited classical core
(de-abstraction style) and closing what's tractable.

**Owner of this ledger:** session `…UfNcb` (independence half + headline wiring).

## Scope map (2026-06-29T17:30Z)

| Work | Files | Owner | Status |
|---|---|---|---|
| **Independence half** (`dim ≥ #SYT`) | `SpechtDominanceCore.lean`, `SpechtTriangularCore.lean` | this session | **MERGED sorry-free** (#3091, #3102, #3111). `dominance_colStab_lemma` fully proved (column-decomposition + `col_downsets_nested` lever); `standardPolytabloid_triangular'` is `[propext, Classical.choice, Quot.sound]`. |
| **Spanning half** (`dim ≤ #SYT`, Garnir) | `SpechtSpanningCore.lean` (`polytabloid_garnir_core`) | **PR #3110** (`claude/admiring-newton-72gwqk`) | in-flight; `span_of_measure_step` lever sorry-free, one cited Garnir core. |
| **B1 irreducibility** (James dichotomy + char-0 Gram) | `SpechtIrreducibleCore.lean` | **PR #3110** | in-flight. |
| **Headline wiring** (`specht_finrank_eq_numSYT` consumes the proved halves) | `SpechtStandardBasis.lean` + new downstream file; consumers `OVTopAssembly`, `TMCorrespondence`, `OptimalNF` | this session | **DEFERRED** until #3110's spanning lands → wire both halves in one pass (avoids partial work + consumer breakage). |
| **Brick-5 JM eigenvalue** (`jucysMurphy_eigenvalue`, `centralC2_acts_by_contentSqSum`) | `JucysMurphy.lean` | this session (next) | non-overlapping; feeds the capstone + the "JM content-square mean" axiom cited by keystone PR #3106. |

## Coordination posted

- **#3110** ([comment](https://github.com/litlfred/qou/pull/3110#issuecomment-4835261608)) — ceded spanning + B1 (I had them queued); claimed the complementary headline wiring; offered the `col_downsets_nested` technique. Flagged the only potential collision (both touching `SpechtStandardBasis` for headline wiring) and asked them to ping if they plan it.
- **#3090** (Identity-I hub) — prior updates: independence-half landings.

## Division of labour (agreed-by-default; flag to revise)

- #3110 owns the **spanning** + **B1** reductions (new files; no `SpechtStandardBasis` edits).
- This session owns the **headline wiring** (deferred) + **brick-5 JM**.
- No file-level conflict currently (their reductions are new files; my independence files are merged).

## Relationship to the keystone PRs

- #3106 (W_λ Plancherel residual-i) explicitly leans on two **Mathlib-Specht axioms**: `Σ dim² = n!` and the **JM content-square mean**. The OV tower formalizes exactly these — independence (merged) + JM (next) give an in-corpus path to discharge them. (Informational; not a collision.)

## Update 2026-06-30 — capstone tranche landed (PR #3132)

**PR #3132** (`claude/ov-capstone-reroute-brick3-2026-06-29`) — three reductions, all
lean-direct EXIT 0, `identityB_general` axioms `[propext, sorryAx, Classical.choice, Quot.sound]`:

| Commit | What | Result |
|---|---|---|
| `191ceb0f` | **headline wiring (no longer deferred)** — new `SpechtFinrankWired` sources independence from the proved `triangular'`; `OVTopAssembly.rank` re-routed to it | rank sorry-path = spanning stub only |
| `5b04c28a` | brick-5 JM: `tableauCellEquiv` (cellOf bijection) sorry-free; `jucysMurphy_eigenvalue` **proved**; core sharpened to `seminormalVector_data_exists` | + over-generality fix (below) |
| `21018634` | `snBlocks` de-abstracted → new `SnWedderburnPartitionBridge` (sorry-free LA + 1 honest core `sn_rational_specht_split`) | capstone direct sorries 2 → 1 |

**Over-generality fixes (this tranche)** — two cited cores were false at their stated generality and were narrowed:
- `JucysMurphy.seminormalVectors_span` (+ punchline `centralC2_acts_by_contentSqSum`): false over ℤ (seminormal vectors carry denominators) → restricted `[CommRing k]` → `[Field k] [CharZero k]`.
- snBlocks bridge: rejected a 2-core split where `d i = dim S^{λᵢ}` over arbitrary splits is false (block sizes fixed only up to permutation) → collapsed to one aligned-split existential.

**Remaining honest OV debt (named cores):** `OVTopAssembly.c2_eigen_on_blocks` (last *direct* capstone sorry) · `SnWedderburnPartitionBridge.sn_rational_specht_split` (ℚ-rationality of Sₙ) · `JucysMurphy.seminormalVector_data_exists` + `seminormalVectors_span` (Young's seminormal form) · brick-4 spanning + B1 (PR #3110).

**Coordination posted (2026-06-30):**
- **#3110** ([comment](https://github.com/litlfred/qou/pull/3110#issuecomment-4842686871)) — dependency/cherry-pick: my `specht_finrank_eq_numSYT_wired` spanning stub = their `standardPolytabloid_straightening'`; will re-route once it lands. Heads-up on the over-ℤ over-generality trap for their char-0-ℂ Gram item.
- **#3006** ([comment](https://github.com/litlfred/qou/pull/3006#issuecomment-4842687333)) — #3132 *proves* Identity (B) via C[Sₙ]; complementary to #3006's HLF-dim *statement*.

**Updated division of labour:** headline wiring is **done** (#3132, not deferred). #3110 still owns spanning + B1. The four remaining named OV cores are deep classical rep-theory (Young's seminormal form, Sₙ ℚ-rationality) — genuinely irreducible at pinned Mathlib; tracked as honest cited sorries.

**Note (2026-06-30):** a 3-way background swarm on `c2_eigen_on_blocks` / `sn_rational_specht_split` / `seminormalVector_data_exists` was rate-limited by infra (not usage) and produced no deliverables; to re-run when the limit clears.

## Update 2026-06-30 (afternoon) — swarm correctness audit found + fixed TWO bugs

A 3-probe adversarial swarm on the remaining cores (`c2_eigen_on_blocks`,
`sn_rational_specht_split`, `seminormalVector_data_exists`) did more than attempt them —
it **audited the committed reductions and caught two correctness bugs**:

| Probe | Finding | Fix | Commit |
|---|---|---|---|
| `sn_rational_specht_split` | irreducible at pinned Mathlib; the #26 reduction was already optimal (one aligned existential, no over-general ∀-over-splits) | validated, no change | — |
| `seminormalVector_data_exists` | **over-general** — false over `ℤ/pℤ` (cell contents collide mod p ⇒ prescribed simultaneous eigenvector need not exist) | restricted `seminormalVector_data_exists` + `jucysMurphy_eigenvalue` to `[Field k] [CharZero k]` | `bc103ca2` |
| `c2_eigen_on_blocks` | **provably FALSE** — took `proj` free, so `proj ≡ 0 ⇒ C₂ = 0` contra `C₂(1)=binom(n,2)`; machine-proved `freeProjClaim_false` (sorry-free) | replaced with the aligned isotypic core `snBlocks_c2_aligned` (isotypic split + C₂ decomp together — the two are inseparable; `mulLeft C₂` is diagonal only in the isotypic frame, strictly stronger than `snBridge`'s size-aligned frame) | `05631152` |

**`OVTopAssembly` now has ZERO direct `sorry`s** — `identityB_general` resolves through named,
true-at-generality cores only. Remaining OV debt (all honest cited cores):
`snBlocks_c2_aligned` + `sn_rational_specht_split` (bridge) · `seminormalVector_data_exists` +
`seminormalVectors_span` (JM) · `standardPolytabloid_straightening` (spanning, ceded to #3110).
Plus the sorry-free evidence lemma `freeProjClaim_false`.

This is the §"refuted / over-general" discipline working as intended: the swarm enforced it on
*my own* commits. A second swarm round (de-abstract `seminormalVectors_span` /
`snBlocks_c2_aligned` further) is in flight.

## Next concrete task

`/prepare-merge` #3132 (rebase onto main — clean: main touched none of the 4 OV files since
divergence — + Gemini/Copilot reviews; CI `gate`/`content-sibling-compile` is billing-flaking, so
reviews run on the green local lean-direct). Integrate the second swarm round if it yields cleaner
cores. Re-route the spanning stub to #3110's `standardPolytabloid_straightening'` once it lands.
Merge gated on explicit owner authorization.
