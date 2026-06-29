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

## Next concrete task

Brick-5 JM eigenvalue core (`JucysMurphy.lean`) — non-overlapping with #3110; then headline wiring once #3110's spanning lands.
