# Conjecture triage — corpus-grep status-drift sweep (2026-06-07)

**Scope.** All 137 `kind: "conjecture"` content blocks in
`content/quantum-observable-universe/`. Each was triaged against the
CLAUDE.md *"Before declaring open"* corpus-grep checklist — searching
`docs/audits/`, `content/`, `folio-assistant/computations/`, and
`docs/coordination/` for an owner-authorised resolution, a witness
that already realises the claim, or a coordination ledger that closed
it — and against the §3b conjectural-propagation rule to separate root
open problems from merely contingent-downstream ones.

**Goal.** Find conjectures that are *secretly already resolved*,
*mis-classified* (proved/refuted parts still wearing `kind:
"conjecture"`), or merely *contingent on another conjecture*, and clean
up the resulting status drift.

## Headline counts

| Bucket | Count |
|--------|-------|
| Resolved-drift (resolved/refuted but still `conjecture`) | 5 |
| Mis-classified (proved/refuted/conditional parts inside a conjecture) | 7 |
| Contingent-downstream (conjectural only via `uses[]` → another `conj:`) | ~25 |
| Genuinely-open roots | ~100 |
| **Total triaged** | **137** |

Of the ~100 genuine open roots, ~13 are *imported* famous open
problems (Millennium / classical), 6 are *QOU-native keystone roots*
(high downstream fan-out), and the remaining ~80 are *leaf roots*
(real open conjectures with nothing hanging off them).

---

## A. Resolved-drift (5) — resolved or refuted, but block still says `conjecture`

| Block | Corpus evidence | Recommended action |
|-------|-----------------|--------------------|
| [`q-integer-mass-formula`](../../content/quantum-observable-universe/mass-theory/q-integer-mass-formula.md) | Seven Bethe–Weizsäcker coefficients derived as q-integer products; **0.020 % MAE on 32 isotopes (He–U), zero fitted parameters** — witness `mass_table_ppb.py`. No remaining conjectural content in the achieved result. | Promote the achieved-result core to a **proposition/theorem** (conditional banner where the categorical *derivation* of the coefficients is still open); keep the open derivation as a clearly-scoped remainder. |
| [`brane-tower-z-habiro`](../../content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md) | `n⋆` level-selection existence **refuted across 6 probed families** (scalar, operator-valued, multiplicity-refined, pair-knot product, pair-knot Markov-trace); only the algebraic Cauchy-limit claim survives. `.ts` tag `partial-refutation-six-families`. | **Split**: (i) surviving algebraic Cauchy-limit claim stays `conjecture`; (ii) refuted `n⋆`-existence recorded as a closed-negative remark/authorNote. |
| [`spin-from-so3-fiber`](../../content/quantum-observable-universe/particle-interactions/spin-from-so3-fiber.md) | Stated premises **falsified 2026-06-01** (`docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md`): S₃ is not ℓ-truncated; the icosahedral h⁴=−3/4 link is impossible (A₅⊂S₅ vs H₃, different algebras). Positive core (spin-Z₂ ≠ sign-Z₂) survives. | Trim the conjecture statement to the surviving core; the falsified premises already carry an authorNote — make sure the `.md` statement no longer asserts them. |
| [`casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md) | authorNotes 2026-05-31 "ε-scaling refinement RESOLVED"; the conditional implication is already **formalised as a §3b-cond conditional theorem** with two class hypotheses (`VacuumEpsilon`, `PlateModeCount`). | Reframe as a **conditional proposition** (theorem-from-class), not an open conjecture. |
| [`qbeta-ck-truncation-canonical`](../../content/quantum-observable-universe/appendix-qvalues/qbeta-ck-truncation-canonical.md) | Mixed status per the canonical c_k framing: **c₂ = −1 proved** (Taylor-exact), c₃ = −2 is a **near-match** (anchor-dependent swing, not a derivation), c_{k≥3} cal-anchored. | Re-state as a **tiered** statement (proved / near-match / cal-anchored), not a monolithic open conjecture. |

---

## B. Mis-classified (7) — proved, refuted, or conditional parts inside a `conjecture`

| Block | Issue | Recommended action |
|-------|-------|--------------------|
| [`knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/mass-theory/knot-factor-frobenius-pairing.md) | Parts 1–3 (single-level Markov identity, Yekutieli 2D non-abelian Stokes, Skein eigenvalue product at A=2,3,4) are **proved**; only the A≥5 closed-form extension (Part 4) is open. | Promote to **proposition** with a §3b-cond conditional banner scoping the open Part 4. |
| [`reidemeister-mass-invariance`](../../content/quantum-observable-universe/mass-theory/reidemeister-mass-invariance.md) | Already written "**Proposition** (conditional on conj:borromean-quark)" in the `.md`; the three Reidemeister-move invariances are proved from knot-theory facts. Block kind is still `conjecture`. | Reclassify kind to **proposition** (conditional-on-class) / remark — bring `kind:` in line with the already-proposition prose. |
| [`conj-atom-braid-exterior-algebra`](../../content/quantum-observable-universe/mass-theory/conj-atom-braid-exterior-algebra.md) | Filtration-shape (Pascal-row binomial) **verified** at A≤4 via the Rust R5-SDP solver; the LP/SDP active-partition implication is **falsified** (`docs/audits/2026-05-25-exterior-algebra-lp-claim-falsified.md`: all 77 partitions of ⁴He non-trivial). | Narrow the claim to the verified filtration-shape; mark the LP/SDP active-partition implication falsified. |
| [`conj-chirality-ribbon-frobenius`](../../content/quantum-observable-universe/mass-theory/conj-chirality-ribbon-frobenius.md) | **Refuted at A≥2** (witness `chirality-avg-content-atomic.witness.json`, ~10⁴ divergence). authorNotes already flag falsification. | Convert to a **remark** documenting why the ribbon-twist ratio fails (closed-negative), or a theorem-false note. |
| [`conj-lepton-tower-h-n-plus-1-branching`](../../content/quantum-observable-universe/mass-theory/conj-lepton-tower-h-n-plus-1-branching.md) | Original `d_q((n,1))` form **falsified** at τ; the unifying `[2m−1]_q·[m]_q/[2m]_q` form matches μ (0.034 %) and τ (0.79 %) but is **conditional on an unproved τ-embedding**. | Reframe statement to the current best form, scoped **conditional-on-τ-categorical-embedding** — not a blank open conjecture. |
| [`wenzl-positivity-implies-substrate-positivity`](../../content/quantum-observable-universe/appendix-surreals-archimedean/wenzl-positivity-implies-substrate-positivity.md) | Wenzl (1988) positivity + Müger/BKLR are **off-the-shelf**; only the substrate **transcription bridge** is conjectural (the `.md` itself lists the three "ingredients"). | Reframe as a **proposition conditional on the Müger/BKLR Lean transcription**, not a fundamental conjecture. |
| [`reading-a-conditional-linking-weight`](../../content/quantum-observable-universe/braids-and-knots/reading-a-conditional-linking-weight.md) | A **falsified candidate** (5/2 + (−G)h² contradicts the proved Family-A 5/2 + ¾h²; falsified across 5 structural routes). Does not change production. Carried only as a conditional class with explicit `sorry`. | Mark **archived / falsified** (historical audit trail); ensure it is not presented as a live open conjecture. |

---

## C. Where the open conjectures are (excluding contingent-downstream)

### C.1 Imported famous open problems (~13) — open by definition

`classical-riemann-hypothesis`, `qou-p-neq-np`, `p-vs-np-conjecture`,
`regularity-breakdown`, `levi-degeneracy-conjecture`,
`yang-mills-mass-gap`, `q-birch-swinnerton-dyer`,
`q-collatz-conjecture`, `kashaev-volume-conjecture`, `kashaev-surreal`,
`qou-infra-discharges-goncharov-zeta5`,
`hyperbolic-volume-transcendence`, `single-volume-irrationality`,
`borel-zagier-qou-volumes`.

These are QOU reframings of Millennium / classical problems. Not
QOU's to close; genuinely open by definition.

### C.2 QOU-native keystone roots (6) — high downstream fan-out

| Root conjecture | Gates (downstream contingent blocks) |
|-----------------|--------------------------------------|
| [`conj:q-geometric-langlands`](../../content/quantum-observable-universe/q-geometric-langlands/q-gl-conjecture.md) | q-oper-hecke, q-gl-fiber-functor, q-gl-kummer-filtration, q-gl-classical-limit |
| [`conj:dilogarithm-archimedean-limit`](../../content/quantum-observable-universe/mass-theory/dilogarithm-archimedean-limit.md) | borromean-bloch-group-element, phi-q-wkb-greens-function, algebraic-geometric-dilog-equivalence |
| [`conj:gb-depth-period-correspondence`](../../content/quantum-observable-universe/mass-theory/gb-depth-period-correspondence.md) | bring-figure-eight-depth-2-witness, graded-baer-star-Hq |
| [`conj:gs-graded-markov-trace-existence`](../../content/quantum-observable-universe/mass-theory/gs-graded-markov-trace-existence.md) | **root of the 6-block GS spectral chain** (gs-residue-at-root-existence, gs-spectral-decomposition-existence, gs-spectral-sum-finite, gs-archimedean-agreement-trace/-residue) |
| [`conj:qdifference-kernel-prolongation-symbol`](../../content/quantum-observable-universe/mass-theory/qdifference-kernel-prolongation-symbol.md) | binding-manybody-jet-filtration (step-9b binding closure keystone) |
| [`conj:borromean-quark`](../../content/quantum-observable-universe/observations/borromean-quark.md) | hydrogen-shell-writhe, orbital-space-normal-bundle → orbital-fourier-decomposition, reidemeister-mass-invariance (partial) |

> Note: `gs-graded-markov-trace-existence` depends only on a *theorem*
> (`thm:jones-markov-trace`) and a *proposition* (`prop:gb-spectral-sequence`),
> so it is a genuine root, not contingent-downstream — the rest of the
> GS chain hangs off it.

### C.3 QOU-native leaf roots (~80)

Real open conjectures with no downstream fan-out. Representative
sample (not exhaustive — see the per-cluster tables in §D):
`borromean-baryon-mass-formula`, `lepton-mass-tower-canonical`,
`z-eq-n-rho-correction`, `staircase-ew-residual`,
`two-filtration-bridge`, `tau-all-orders-bridge`,
`kashaev-density-equals-sdp-multiplicity`, `geom-universality`,
`magic-numbers-bring`, `g-action-on-substrate`, `n-v-bring-action`,
`n-v-tower-depth-ninety`, `higgs-t28`,
`color-superconductivity-borromean`, `conj-canonical-knot-id-sdp`,
`conj-psd-trace-orthogonality`, `conj-rho-prefactor-structural`,
`confinement-nf-structure-forcing`, `depth-stratified-frobenius-reciprocity`,
`dim-master-pentagon`, `cl3-zeta5-geometric-realization`,
`alpha-k-categorical-closure`, `joint-galois-braid-action`,
`jet-filtered-knot-factor`, `lifted-crossing-locality`,
`pachner-pentagon-borromean`, `p-from-braid-mirror`,
`poincare-lefschetz-borromean`, plus the
`particle-interactions/` CPT/crystal/anyon set, the
`predicted-spectra/` and `brings-surface/` sets, and the
`appendix-surreals/` surreal-framing set.

---

## D. Contingent-downstream clusters (~25) — not root problems

These are conjectural only because their `uses[]` cone touches another
`conj:`. Resolving the named root discharges them automatically.

- **q-GL cluster** → root `conj:q-geometric-langlands`:
  q-oper-hecke, q-gl-fiber-functor, q-gl-kummer-filtration,
  q-gl-classical-limit; (and lusztig-canonical-basis-q-eq-1 via
  reverse-limit-q-to-infinity + kazhdan-lusztig-classical-limit).
- **GS spectral chain** → root `conj:gs-graded-markov-trace-existence`:
  gs-residue-at-root-existence, gs-spectral-decomposition-existence,
  gs-spectral-sum-finite, gs-archimedean-agreement-trace,
  gs-archimedean-agreement-residue.
- **Borromean-quark cluster** → root `conj:borromean-quark`:
  hydrogen-shell-writhe, orbital-space-normal-bundle,
  orbital-fourier-decomposition, c-from-color-flavor-swap,
  inter-nucleon-channel-color-tube, isospin-from-canonical-bowtie.
- **Dilog cluster** → root `conj:dilogarithm-archimedean-limit`:
  borromean-bloch-group-element, phi-q-wkb-greens-function,
  algebraic-geometric-dilog-equivalence,
  shared-denominator-cusp-holonomy.
- **CPT cluster** → root `conj:cpt-d6-d7-d8-closure`:
  type-b-folding-cpt, cpt-orbit-closure-density,
  wigner-su4-from-spin-isospin, cp-violation-spectral-form,
  symmetric-crystal-pair-production (partial).
- **Categorical-Higgs cluster** → root `conj:categorical-higgs-mechanism`:
  categorical-linking-operation, weinberg-angle-categorical (partial).
- **N_v cluster** → roots `conj:n-v-bring-action` + `conj:n-v-tower-depth-ninety`:
  n-v-leading-order-derivation.
- **OS/Wenzl** → `os-reflection-positivity-from-reeb` on
  wenzl-positivity-implies-substrate-positivity.
- **Surreal standard-part** → `archimedean-stpart` and the
  classical-limit-stpart family depend on multiple sub-conjectures.

---

## E. Verification pass — which flagged blocks actually needed a change

The §A/§B "recommended action" columns above are the *first-pass*
classification from the parallel triage agents. Before editing, every
flagged block was opened and read at file level. The result: **8 of the
12 were already honestly caveated** — the first-pass agents keyed on
each conjecture's aspirational *statement* and under-weighted its
already-present caveat apparatus (authorNotes, conditional banners,
tiered titles, dedicated `## Status` sections, `partial-refutation`
tags). Only **4 warranted an edit**.

### Already-honest — no change (8)

| Block | Why no change |
|-------|---------------|
| `q-integer-mass-formula` | `.md` already opens "*Conjecture (BW-emergence … conditional on conj:palindromicity-orbital-type and conj:shell-closure-nf-term-count)*"; coefficients are explicit near-matches (0.2–2.1 %); `uses[]` carries two conjectures → §3b forbids promotion to theorem. Correctly a conjecture. |
| `casimir-epsilon-vacuum` | Two authorNotes already split resolved ε-scaling vs still-open prefactor; `uses[]` carries three conjectures. Correctly a conjecture. |
| `qbeta-ck-truncation-canonical` | Title is already tiered (proved c₂ / near-match c₃ / cal-anchored c_{k≥3}); two authorNotes spell out the status. Gold-standard honesty. |
| `spin-from-so3-fiber` | authorNote (2026-06-01) already documents the falsified premises + surviving core; block correctly stays conjecture. |
| `knot-factor-frobenius-pairing` | `.md` opens "**Conjecture.**" — kind and prose agree; the conjectural content (bulk-binding = trace-defect, tower extension) is genuinely open. |
| `conj-atom-braid-exterior-algebra` | Title/prose say "partial-closure: verified at A≤4, general A open"; authorNote says "categorical proof open". Empirical table is accurate. |
| `conj-chirality-ribbon-frobenius` | Two authorNotes already say "Refuted at the audited atomic braids … scoped as historical/aspirational". Correctly flagged. |
| `wenzl-positivity-implies-substrate-positivity` | `uses[]` carries `conj:os-reflection-positivity-from-reeb`; the bridge is genuinely unproved. Correctly a conjecture (in the speculative surreals appendix). |

### Edited (4)

| Block | Edit |
|-------|------|
| `reidemeister-mass-invariance` | `uses[]` omitted the `conj:borromean-quark` its prose declares it conditional on (manifest gap) → added; prose banner said "**Proposition**" while kind is `conjecture` (env mismatch) → banner reworded to "**Conjecture (conditional on …)**" acknowledging the proved Reidemeister core; status authorNote added. |
| `conj-lepton-tower-h-n-plus-1-branching` | Title stated the *superseded* muon-only form `d_q(std_rep)·[2]_q/[n+1]_q` (whose τ prediction was falsified) → retitled to the unifying form `ξ_m = [2m−1]_q·[m]_q/[2m]_q` (PR #1253), which the authorNotes already document. |
| `brane-tower-z-habiro` | n⋆-refutation lived only in tags + scattered prose → consolidated into a first-class split-status authorNote (algebraic Cauchy-limit open; n⋆ refuted across six families). |
| `reading-a-conditional-linking-weight` | Falsified-candidate status lived only in the `.md` `## Status` section → lifted to a manifest authorNote + `falsified-candidate` tag. |

**Net:** no kind-flips were made. Every §3b constraint was respected
(no conjecture-downstream block promoted to a provable kind without the
§3b-cond class machinery, which none currently has). The corpus's
status-tracking discipline (authorNotes per §4d, conditional banners,
tiered titles) is working well; the residual drift was confined to two
stale headlines (lepton title, reidemeister banner), one manifest
dependency gap (reidemeister `uses[]`), and two not-yet-first-class
statuses (brane-tower, reading-a).

## Method note

Triage executed by five parallel read-only Explore sub-agents, one per
chapter cluster, each running the four-path corpus-grep checklist per
block and classifying into {resolved-drift, mis-classified,
contingent-downstream, genuinely-open}. One bucketing correction
applied during synthesis: `gs-graded-markov-trace-existence` was
re-graded from contingent to root (its dependencies are a theorem + a
proposition, not conjectures).
