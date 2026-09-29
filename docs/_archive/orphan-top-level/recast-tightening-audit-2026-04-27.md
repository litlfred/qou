# Recast / tightening audit (Apr 2026)

This document is the deliverable for the inventory sweep that
accompanies the pre/post-Archimedean recast plan applied in
`copilot/explore-analogues-sqrtq` (mirrors the recast pattern from
`claude/mass-units-bridge-followups` commit `7588970f`).

## Part B — dual-leg / asymptotic-bridge candidates

Grep across `folio/quantum-observable-universe/**/*.md` for
"geometric leg / algebraic leg / two legs / both legs / the two agree"
returned **one** file, `partition-sum-proton-residual.md`, where
"the two" referred to two numerical values (q-deformed vs classical
limit), **not** the dual-leg structure. Result: no other true
dual-leg blocks exist on `main`; the one canonical case
(`atom-knot-mass-derivation`) is recast on the followups branch.

Grep for `mostow1968 / gromov1982 / kashaev1995 / murakami2001 /
thurston1978` cites returned 4 files. All 4 are already conjectures,
remarks, or genuinely post-Archimedean propositions
(`thurston-volume-additivity` literally states Thurston's theorem).
**Result: no core proposition borrows volume conjecture / Mostow /
Gromov / Kashaev for derivations.**

The only block on `main` that needed a recast in this pass was
`algebraic-quantum-volume-specialization.md` (route 1 and route 2
explicitly flagged as **post-Archimedean borrowed naming**;
route 3 is the only QOU-internal step). Done in this PR.

## Part C — paper-wide tightening

| Item | Status | Notes |
|------|--------|-------|
| C1: drop "why this is absent from core" passages | partial | Ribbon block done; $\tau$-suppression and categorical-instanton are already concise (no such passages). |
| C2: Markov-trace decomposition single canonical statement | OK | Only 5 files mention $\sum_\lambda y_\lambda \chi_\lambda$; canonical statement is `thm:jones-markov-trace` + `prop:alpha-k-derivation-procedure`. No rampant duplication. |
| C3: move illustrative $y_\lambda$ computations to witness JSON | **done** | Three illustrative tables removed and replaced with witness-file links: `explicit-alpha-k-h3.md` (numerical-at-$q_0$ table → `alpha-k-jones-markov-h3.witness.json`), `explicit-alpha-k-h4.md` (numerical depth-stratum table + Hoefsmit character matrix → `wedderburn-orthogonal-r-3-h4.witness.json`), `y-lambda-sign-pattern.md` (sign-pattern table → `y-lambda-jones-markov-witness.json`). Saved 27 narrative lines without losing rigor. |
| C4: unify Markov-trace symbol | done | Paper is 92% consistent on `\mathrm{tr}_M`; 7 brace-variants `\mathrm{tr}_{M}` normalized. |
| C5: cap proof length at ~40 lines | **done** (25/25 split or tightened) | 25 proof blocks initially exceeded 40 lines. **Tier 1** (>80 lines, 7 blocks): all 7 split via Pattern A (named-step extraction). **Tier 2** (50–80 lines, 11 blocks): 10 split via Pattern A or B (sub-proof extraction), `euler-char-stability-proof` tightened in prose. **Tier 3** (43–48 lines, 7 blocks): tightened in prose only (drop redundant connectives, merge adjacent display equations). All Lean stubs added with `-- Ref:` to parent's reference; no Lean proof content changed. Validation issue count remained 197 throughout (no regression). See per-block table below. |
| C6: transitive prune | done | `pipeline/prune-transitive-deps.ts --apply` removed **1797** transitive edges across **643** files; validation issue count 204 → 197 (7 unresolved-uses errors fixed as bonus). |

## Proof-length audit (Part C5 — completed)

Initial proof blocks exceeding 40 lines (25 total) and current status
after C5 splitting / tightening:

| Initial | Current | Block | Action |
|------:|------:|-------|--------|
| 169 | 42 | `lifting-and-descent/topological-mass-proof.md` | split → 4 lemmas (`eigenspace-decomp`, `holonomy`, `transient-localisation`, `dilogarithm`) |
| 111 | 40 | `quantum-observable-universes/quantum-observable-universe-exists-proof.md` | split → 4 lemmas (one per axiom) |
| 103 | 24 | `quantum-observable-universes/su2-emergence-proof.md` | split → 2 lemmas (`volume-determinant`, `dagger-unitarity`) |
| 100 | 22 | `observations/terminal-resolution-proof.md` | split → 4 lemmas (deuteron-binding, nucleon-borromean, nucleon-mass-splitting, pair-skein-mass-formula) |
| 95 | 19 | `braids-and-knots/topological-mass-categorical-proof.md` | split → 3 lemmas (`eigenspace`, `transient`, `descended`) |
| 93 | 23 | `braids-and-knots/feynman-categorical-trace-proof.md` | split → 3 lemmas (`eigenbasis-decomposition`, `trace-collapse`, `markov-identification`) |
| 82 | 18 | `descartes-universe/genus-filtration-ideal-proof.md` | split → 4 lemmas ((0)/(i)/(ii)/(iii)) |
| 69 | 31 | `lifting-and-descent/descent-condition-proof.md` | split → `lem:descent-cocycle-deviation` |
| 61 | 18 | `lifting-and-descent/cosimplicial-crossed-groupoid-proof.md` | split → 2 lemmas (`cosimplicial-identities`, `crossed-module-structure`) |
| 59 | 29 | `lifting-and-descent/jet-prolongation-proof.md` | split → `lem:jet-prolongation-categorical-jet` |
| 57 | 28 | `quantum-observable-universes/fiber-adjoint-involution-proof.md` | split → `lem:fai-projector-coadjoint-orbit` |
| 57 | 41 | `descartes-universe/brings-is-qou-proof.md` | split → 2 lemmas (Euler-characteristic, Riemann--Hurwitz) |
| 55 | 34 | `descartes-universe/mi-sw-abelianisation-proof.md` | split → `lem:mi-sw-abelianisation-cartan` |
| 53 | 38 | `braids-and-knots/transfer-matrix-level-independence-proof.md` | split → `lem:tmli-constituent-composite-agreement` |
| 53 | 29 | `braids-and-knots/non-self-intersection-proof.md` | split → `lem:nsi-q-deformed-kernel` |
| 53 | 39 | `braids-and-knots/mobius-energy-proof.md` | split → `lem:mobius-energy-frobenius-kernel` |
| 51 | 36 | `braids-and-knots/skein-generation-proof.md` | split → `lem:skein-mass-from-linking` |
| 50 | 37 | `lifting-and-descent/euler-char-stability-proof.md` | prose tightening (compact rigidity-trace unfolding) |
| 48 | 29 | `quantum-universes/frobenius-relation-proof.md` | prose tightening |
| 46 | 32 | `observations/skein-mass-relation-proof.md` | prose tightening (compact $m_\mu/m_e$ derivation) |
| 46 | 33 | `lifting-and-descent/vacuum-state-proof.md` | prose tightening |
| 45 | 40 | `quantum-observable-universes/substrate-parameter-unique-proof.md` | prose tightening |
| 44 | 42 | `lifting-and-descent/qu-to-qou-proof.md` | prose tightening |
| 43 | 39 | `quantum-observable-universes/categorical-dq-squared-proof.md` | prose tightening |
| 43 | 40 | `lifting-and-descent/descent-lemma-proof.md` | prose tightening |

**Method.** Two refactor patterns were used:
- **Pattern A** (named-step extraction): each labelled "Step 1/2/3" or
  "(i)/(ii)/(iii)" sub-block became its own `lemma` (with its own
  `proof` block). The parent shrinks to ~10–25 lines of "by Lemma A,
  then Lemma B, ∎" structure. Used for all blocks with explicit step
  markers.
- **Pattern B** (single technical extraction): a long single
  computation became a sibling lemma. Used for blocks without named
  steps but with an isolated technical core (e.g. the $q$-deformed
  kernel computation in `non-self-intersection-proof`).

**Constraints respected.**
- *No math content changes.* Extracted text was moved verbatim
  (modulo connective bridging sentences).
- *No Lean proof content changes.* Each new lemma's `.lean` file
  carries `:= by sorry` with a `-- Ref:` citation to the parent's
  existing reference. Existing parent Lean proofs are unchanged.
- *Cross-references preserved.* No external block references
  pointed to interior steps of the split parents (`grep` checked
  before each split); chapter manifests register all new sub-blocks
  in the section list.
- *Validation gate held.* `bun run validate quantum-observable-universe`
  remained at **197 issues** throughout (the project baseline; the
  remaining issues are pre-existing unresolved-cross-references
  unrelated to C5).

Lemma naming convention: `lem:<parent-slug>-<step-slug>` (e.g.
`lem:feynman-eigenbasis-decomposition`).

## Items that depend on the followups branch landing first

- **Part B step 4: collapse Lean `PipelineStage` enumerations.** The
  recast on the followups branch went from 11 stages to 8 by the
  $E_2$-collapse argument. Other multi-stage Lean stubs in the repo
  may collapse similarly, but the analysis depends on the recast
  Lean infrastructure (`YekutieliFiniteSliceMultiplicativeTrace`,
  `GbSpectralSequenceCollapseAtE2`,
  `CategoricalMassInvariantFinite`) which exists only on the
  followups branch. Defer to a follow-on PR after `7588970f` lands.

- **Part B step 3 (boxed $\mathbb{Q}(q)$-element form)** is a
  template-establishment pass. The template lives in the recast
  `atom-knot-mass-derivation-proof.md` on the followups branch
  ($M(\mathfrak{H}) := \rho \cdot \mathrm{tr}_M(T_w) \in \mathbb{Q}(q)$,
  $B(\mathfrak{H}) = m_e \cdot M(\mathfrak{H})|_{q=q_0}$). Once that
  lands, applying the same template to charge / magnetic moment /
  binding energy is a per-block edit that should reference rather
  than re-prove. Defer.
