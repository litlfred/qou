# Conjecture triage — corpus-grep status-drift sweep (2026-06-07)

**Scope.** All 137 `kind: "conjecture"` content blocks in
`content/quantum-observable-universe/`. Each was triaged against the
AGENTS.md *"Before declaring open"* corpus-grep checklist — searching
`docs/audits/`, `content/`, `computations/`, and
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

## F. Tiered backlog of the open leaf roots (re-tiering)

Working classification of the ~80 genuine leaf roots (keystone roots
§C.2, imported famous problems §C.1, and contingent-downstream §D are
excluded). Tiers: **E** = empirical/physical prediction (near-match to a
measured quantity — the framework's *testable* set, highest priority);
**S** = structural-math derivation goal (no number, "derive X
categorically"); **P** = speculative surreal-appendix framing (retained
per owner decision 2026-06-07, not deprecated).

Two falsified leaf roots (`conj-chirality-ribbon-frobenius`,
`reading-a-conditional-linking-weight`) were **moved to
`_deprecated/falsified-conjectures/`** in this PR and are no longer in
the backlog.

### Tier E — empirical / physical predictions (testable; prioritise)

| Block | Chapter | Predicts | Current agreement |
|-------|---------|----------|-------------------|
| `lepton-mass-tower-canonical` | mass-theory | m_μ, m_τ | structural form open |
| `conj-lepton-tower-h-n-plus-1-branching` | mass-theory | m_μ, m_τ | μ 0.001%, τ +0.79% |
| `staircase-ew-residual` | mass-theory | Weinberg angle | 0.13% |
| `z-eq-n-rho-correction` | mass-theory | Z=N binding | ~10⁻³ |
| `conj-canonical-knot-id-sdp` | mass-theory | canonical knots ²H/³H/³He | SDP-selected |
| `borromean-baryon-mass-formula` | mass-theory | baryon rest masses | λ_scale open |
| `conj-rho-prefactor-structural` | mass-theory | SDP multiplicity rule | heuristic |
| `lifted-crossing-locality` | mass-theory | mass expansion | ≤6% |
| `kashaev-density-equals-sdp-multiplicity` | mass-theory | ρ_F density | Rule-14 |
| `alpha-k-categorical-closure` | mass-theory | prefactor resummation | witnessed |
| `n-v-bring-action` | observations | EW rescale = 120 | — |
| `n-v-tower-depth-ninety` | observations | tower depth = 90 → VEV | 244.79 vs 246.22 GeV |
| `higgs-t28` | observations | Higgs mass | ~125 GeV |
| `double-magic-delta-i-bound` | observations | doubly-magic isotopes | 9/9 |
| `color-superconductivity-borromean` | observations | diquark gap | 2.5 vs 10–100 MeV |
| `e-hartree-categorical-derivation` | predicted-spectra | Hartree energy | relative spacing only |
| `bring-hyperbolic-knot-bloch-decomposition` | predicted-spectra | 2/(3π) | numeric witness |
| `magic-numbers-bring` | quantum-observable-universes | {2,8,20,28,50,82,126} | period-lattice open |
| `shell-closure-nf-term-count` | molecular-construction | shell gaps | γ-alternation |
| `palindromicity-orbital-type` | molecular-construction | orbital s/p type | Poincaré-dual NF |
| `confinement-grading-correspondence` | particle-interactions | confinement levels | k≤7 atoms |

### Tier S — structural-math derivation goals

mass-theory: `categorical-higgs-mechanism`, `cl3-zeta5-geometric-realization`,
`conj-im-q-physical-role`, `conj-psd-trace-orthogonality`,
`confinement-nf-structure-forcing`, `crossing-graded-mass-expansion`,
`depth-stratified-frobenius-reciprocity`, `dim-master-pentagon`,
`joint-galois-braid-action`, `jet-filtered-knot-factor`,
`pachner-pentagon-borromean`, `p-from-braid-mirror`,
`poincare-lefschetz-borromean`, `tau-all-orders-bridge`,
`two-filtration-bridge`.
particle-interactions: `t-from-trace-cyclicity`,
`symmetric-crystal-pair-production`, `q-zero-stokes-region-identification`,
`root-of-unity-mtc-truncation`, `kazhdan-lusztig-classical-limit`,
`hecke-anyonic-substrate`, `geom-universality` (being upgraded in #1931),
`crystal-graph-realization`, `cemetery-group-emergence`,
`brunnian-property-of-borromean`, `complex-chirality-rotation`.
stochastic-mechanics: `graded-baer-star-Hq`, `g-action-on-substrate`.
q-geometric-langlands: `modular-s-transform-q-q-tilde`,
`mirror-3d-3d-correspondence`.
mass-endomorphism: `conj-rho-k-pair-gen-canonical-form`.

### Tier P — speculative (surreal appendix; retained)

appendix-surreals: `vacuum-epsilon`, `spectral-normal-form`,
`infinitesimal-observability`, `jones-birthday`, `local-infinitesimal-field`,
`classical-limit-stpart`, `bigbang-heatdeath`, `archimedean-stpart`,
`casimir-epsilon-vacuum` (resolved conditional core).
appendix-surreals-archimedean: `infinitesimal-frobenius`,
`diophantine-birthday`, `on-p-modular-hecke`,
`wenzl-positivity-implies-substrate-positivity` (bridges to Yang-Mills).
`qou-infra-discharges-goncharov-zeta5` and `kashaev-surreal` straddle
P and the imported-famous bucket (§C.1).

> This §F is the navigable re-tiering (owner picked "re-tier, don't
> deprecate" for the non-falsified backlog). It is a doc-level snapshot;
> machine-filterable `tier:E|S|P` tags on each `.ts` can be added as a
> follow-up mechanical sweep if programmatic filtering is wanted (cost:
> ~80 sidecar refreshes).

## Method note

Triage executed by five parallel read-only Explore sub-agents, one per
chapter cluster, each running the four-path corpus-grep checklist per
block and classifying into {resolved-drift, mis-classified,
contingent-downstream, genuinely-open}. One bucketing correction
applied during synthesis: `gs-graded-markov-trace-existence` was
re-graded from contingent to root (its dependencies are a theorem + a
proposition, not conjectures).

---

## 2026-06-08 refresh (addendum)

Same-discipline re-run on the refreshed tree (`main` @ `a983615f`, **136 live
conjectures**). The §A–§F qualitative findings above are **confirmed current** —
the 4 edits and the 2 deprecations landed; no conjecture is
secretly-resolved-and-mis-kinded. This addendum (a) corrects the approximate
headline counts against the actual `uses[]` graph and (b) adds one axis the
original sweep did not run.

### G. Count reconciliation — structural `uses[]` graph

The headline "~25 contingent / ~100 open roots" was an approximation. Computed
from the actual `uses[]` graph (excluding `_deprecated/`):

| Definition of "open root (not contingent-downstream)" | roots | contingent |
|---|---|---|
| **Direct** — block's own `uses[]` names no `conj:` | 69 | 67 |
| **Logical-transitive** — cone reaches no `conj:` via provable/conj edges (remark cites excluded per §3a) — *recommended* | **51** | 85 |
| **All-block transitive** — incl. remark `uses`/`interprets` (overcounts) | 39 | 97 |

The "~100 open roots" figure double-counted: it treated as "leaf roots" many
blocks whose `uses[]` directly names another conjecture. Three of the six §C.2
"keystone roots" are in fact transitively contingent
(`dilogarithm-archimedean-limit`, `gb-depth-period-correspondence`,
`qdifference-kernel-prolongation-symbol`); the first two only via remark cites
(weak links per §3a — so they remain *near*-roots), but
`qdifference → prop:binding-genfun-qdifference → conj:binding-manybody-eq-jet-filtration`
is a real logical edge (see §H). Note the arrow direction: `qdifference`
**depends on** `binding-manybody`, opposite to the "gates" wording in §C.2.

### H. New axis — provable blocks that `uses` a conjecture (§3b inverse drift)

The original sweep checked *conjectures wearing the wrong kind*. The inverse —
**propositions/theorems silently depending on a conjecture** — was not swept.
On the refreshed tree: **31** `proposition|theorem|lemma|corollary` blocks
directly `uses` a `conj:` (without the `conditional-on-class` tag). **16** were
already honest (a `(conditional on conj:X)` banner and/or a Lean class
hypothesis). **15** were silent. Per-block file-level investigation gave:

| Disposition | Count | Blocks |
|---|---|---|
| **Conditional banner added** (proof genuinely relies on the conj) | 10 | binding-genfun-qdifference, knot-mass-formula-unified, mass-element-nf, hook-weight-derivation, rho-k-h3a-refinement, jet-prefix-gb-filtration, force-carrier-intertwining-correspondence, knot-operator-lp-selection, knot-indexed-convolution-grid, critical-exponent (enstrophy-divergence exponent is meaningful only if blow-up occurs → genuinely conditional on regularity-breakdown, edge kept) |
| **Stale/contextual `uses[]` edge dropped** (result proved unconditionally) | 4 | bring-trilog-imaginary-tate-rational (Im Li₃(ζ₅)=4π³/125, 50-dps), reeb-u1-chart-swap (chart-swap U(1)=Reeb U(1)), blowup-yekutieli (unconditional reformulation "NS blowup ⟺ obstruction level n*"; regularity-breakdown kept as prose cross-ref), ns-obstruction-computation (Euler-class/jet-divergence computation unconditional; levi-degeneracy dropped) |
| **No change — already honest** | 1 | lambda-scale-substrate-form (deprecation authorNote: original form falsified 2026-05-18; Family-A core proved) |

The NS / Yang-Mills trio (`blowup-yekutieli`, `critical-exponent`,
`ns-obstruction-computation`) was originally deferred for an owner
"conditional-on vs stale-edge" judgment; resolved per owner direction —
1 conditional banner + 2 edge-drops, folded into the counts above.

The banner fixes disclose the dependency on the narrative side; the Lean
class-hypothesis wiring (second half of §3b-cond) is a tracked follow-up (Lean
toolchain network-blocked in this environment).

### I. Tier-tag completion

13 logical-transitive root conjectures lacked a machine-filterable
`tier:E|S|P|keystone` tag after the `a1259bed`/`3a217f4e` sweep. Tagged by
objective rule (fan-out ≥ 6 → `keystone`; predicts a measured observable → `E`;
else `S`): **keystone ×3** (`knot-factor-frobenius-pairing` fan-out 14,
`inter-nucleon-channel-color-tube` 7, `mass-endomorphism` 7), **E ×2**
(`qbeta-ck-truncation-canonical`, `weinberg-angle-categorical`), **S ×8**. Every
logical-transitive root now carries a tier tag.

### Method note (refresh)

Graph counts computed by a `uses[]`-parser over all `*.ts` blocks (three root
definitions: direct / logical-transitive / all-block). §3b candidates found by
intersecting provable-kind blocks with conjecture `uses[]`, then calibrated
against each block's `.md` banner + `.lean` class — 16 of 31 were already honest
(same "already-caveated" pattern as §E). Two read-only sub-agents did the
file-level per-block investigation of the 15 silent candidates.

---

## 2026-06-25 refresh — fresh inventory + new Lean-internal axis

Same-discipline re-run on the current tree (**147 live `conjecture()`
blocks**, up from the 136–137 of the 2026-06-07/08 sweeps). Two parts:
(J) a mechanical Lean-status inventory that **re-confirms** the §A–§I
qualitative findings, and (K) **one axis the prior sweeps did not run** —
the *Lean-internal* integrity of each conjecture's `.lean` (the earlier
sweeps triaged block **kind**, not the sibling Lean body).

### J. Lean-status inventory (re-confirmation)

Per-block resolution of every `conjecture()` sibling/ref Lean source
(`scripts/`-style grep classification):

| Lean-status bucket | Count (of 147) |
|---|---|
| carries `sorry` (open formalisation) | 119 |
| class-axiomatised (`class … : Prop where …`, §3b) | 142 |
| `axiom` keyword | 6 |
| contains a `: True := trivial` line | 9 |
| `native_decide` | 1 |

The 9 `: True := trivial` matches were each opened: **all are the
sanctioned patterns**, not vacuity dodges — §3b-cond witness defs
(`def X_conditional_on_Y [_inst : Y] : True := trivial`), class
placeholder fields (`holds : True`), `example : True := trivial` compile
markers, or already-fixed historical comments (the fluid-dynamics files
that document *"the earlier version stated only `theorem … : True`"*).
This **confirms the headline conclusion**: the mechanically-closeable
conjecture set is ≈ empty; the 147 are genuine q-deformed open roots,
correctly classified. The corpus-grep / §3b discipline is holding.

### K. New axis — Lean-internal vacuity / compile audit of conjecture siblings

The §A/§B/§E/§H sweeps checked *block kind* and *narrative banners*; they
did **not** typecheck or vacuity-scan the conjecture `.lean` bodies. A
lean-direct pass (toolchain v4.24.0, oleans restored from
`lake-cache/qou-v4-24-0`) over the suspicious siblings found **one**
genuine defect:

| Block | Lean-internal defect | Disposition |
|-------|----------------------|-------------|
| [`conj-rho-k-pair-gen-canonical-form`](../../content/quantum-observable-universe/mass-endomorphism/conj-rho-k-pair-gen-canonical-form.md) | (1) `def pair_gen_functional … : R := trivial` — a **type error** (`trivial : True`, expected `R`); the file did not compile. (2) `theorem pair_gen_kashaev_limit : ∃ f, ∀ args, pair_gen_functional = f args := ⟨pair_gen_functional, rfl⟩` — a **vacuous self-projection** (true for *any* function) whose docstring claimed it proved the Kashaev limit (AGENTS.md §1a violation). The sibling `.md`'s own "Lean formalization" block already documented the honest `:= sorry` form — the committed `.lean` had drifted from its own spec. | Fixed to the §3b sanctioned form: `pair_gen_functional := sorry` (cited placeholder, disposition 2) + the conjecture axiomatised as `class PairGenCanonical : Prop where holds : True` (disposition 3), replacing the vacuous theorem. `.ts` `lean.ref` repointed to the class; `.md` snippet synced. **lean-direct exit 0** (only the expected `uses 'sorry'` warning). Block stays a correctly-classified Tier-S open conjecture (per §F line "mass-endomorphism: `conj-rho-k-pair-gen-canonical-form`"). |
| [`conj-staircase-ew-residual`](../../content/quantum-observable-universe/mass-theory/staircase-ew-residual.md) | The block's `lean.ref` (`QOU.StaircaseCornerHook.StaircaseEWResidual`) resolved (§0a candidate-2 path) to a **degenerate duplicate** `StaircaseCornerHook/StaircaseEWResidual.lean`: `class StaircaseEWResidual where residual : ℝ; residual_eq_zero : residual = 0` + `noncomputable instance := sorry`. That class is **trivially inhabited** (`⟨0, rfl⟩`), so the `sorry` axiomatises nothing — a §3b-cond rule-5 / §1a vacuous-placeholder anti-pattern. A **faithful** same-named class (rich `Prop`, references the real Hoefsmit eigenvalue spectrum `HasEigenvalueRatio (wordImage (betaEWWord …))`, correct hypothesis-only §3b-cond) already existed in `QOU/StaircaseCornerHook.lean`, unreferenced. No module imported the degenerate file (no live build collision). | Deleted the degenerate `StaircaseCornerHook/StaircaseEWResidual.lean`; the `lean.ref` now resolves (§0a grep-fallback) to the faithful class; `.md` "Lean status" updated to the hypothesis-only encoding (no instance/sorry). Not lean-direct-verifiable in-sandbox (faithful file imports a mathlib module absent from the partial olean cache; pipeline ref-resolution out of scope → CI-verified); the deletion is build-safe (no importers, not in the `QOU.lean` aggregator). Block stays a correctly-classified Tier-E open conjecture. |
| [`conj-kashaev-volume-conjecture`](../../content/quantum-observable-universe/mass-theory/kashaev-volume-conjecture.md) | Surfaced by the full 147-sibling sweep (below). **Two** structural defects: (1) `noncomputable def pieceVolume … : ℝ := trivial` — a **type error** (`trivial : True`, expected `ℝ`); the in-code comment even said "we leave the value as `sorry`". (2) the `/-! -/` module docstring **preceded** `import QOU.PhiQPiece` → illegal import order in Lean 4 (the file never compiled). Latent because the file is a content-block sibling *outside* the CI `lean/QOU/**` target. | `trivial → sorry`; moved the import above the docstring. `lean`-direct confirms the import-order error is gone (then stops at the sibling `QOU.PhiQPiece` olean, absent in-sandbox → body CI-gated). `VolumeConjecture` itself is a faithful §3b class (real fields `hypVolume`/`kashaevLimit`/`kvc_holds`), unchanged. Block stays a correctly-classified imported-famous open conjecture. |

### Full Lean-internal sweep of all 147 conjecture siblings (2026-06-25)

A static analyzer (comments/docstrings stripped **before** matching — to avoid
the comment-false-positives that fooled earlier ad-hoc greps), cross-checked by
targeted reads + `lean`-direct, classified every `conjecture()` sibling.
Result: **37 flagged, 110 clean**, of which exactly **3 genuine defects** (all
now fixed) — rho-k, staircase, kashaev above. The other 34 flags are
**sanctioned / known patterns**:

- **34 `class … where residual : ℝ; residual_eq_zero` + global
  `instance := sorry`** — degenerate auto-generated §3b stubs (identical
  boilerplate). These are *known placeholder backlog* (cf. the
  `zslh`/`b3pe`/`mlt7` "resolve N placeholders" beans); maturing them to real
  §3b content is per-conjecture math, **not** a mechanical sweep — left to the
  backlog/owner.
- **5 duplicate FQNs** — all the intentional local-copy pattern (`…Local`
  suffix; the two `HyperbolicVolumeIndependence` copies are commented "package
  sibling for the canonical declaration", the real one in
  `QOU/Archimedean/HyperbolicVolumeTranscendence.lean`). Never co-imported →
  benign latent smells, not active collisions.
- **`native_decide` (many)** — all legitimate finite enumerate-then-assert
  checks (magic-number lists, dimension sums, Seifert genus, crossing-
  minimality), **not** the §1a kernel-masking dodge.

**Systemic insight.** All three genuine defects live in **content-block `.lean`
siblings** (`mass-theory/…`, `mass-endomorphism/…`) that sit *outside* the
CI-built `lean/QOU/**` library target — so they are never compile-checked and
accumulate latent type-errors / import-order breakage that both block-kind
triage and library CI miss. The library tree itself is clean. Closing this gap
(compile-checking content-block siblings) would catch the next such drift
automatically.

Net 2026-06-25: **no kind-flips**; **3** Lean-internal integrity fixes across
the session (rho-k, staircase, kashaev). The conjecture corpus is otherwise
sound; the closeable set remains ≈ empty — the 147 are genuine open problems.

### Compile-validity CI gate + the import-order backlog (2026-06-25 follow-up)

Acting on the systemic insight, the `lean-vacuity-axiom-audit.ts` scanner was
extended with two **compile-validity** categories (guaranteed Lean errors, not
heuristics) that the vacuity detectors miss:

- `proof-no-trivial-type-mismatch` — a term-mode `trivial` body under a
  non-`True`-typed `def`/`abbrev` (caught rho-k + kashaev). Tree-wide count
  after the fixes: **0**.
- `lean-import-after-content` — an `import` after a `/-!` module docstring or
  any command (illegal Lean-4 order; caught kashaev). Tree-wide count:
  **40 files** — a real, mechanical, latent-broken **backlog** (5 are under the
  CI-built `lean/QOU/**` tree and contribute to the already-red
  `lake build QOU`; 35 are content-block siblings outside it). Representative:
  `lean/QOU/Braiding/skein_crossing_asymmetry.lean:15` (`import …` after the
  module docstring). Fixing them is a uniform codemod (move the post-docstring
  imports above the docstring). **Drained 2026-06-25 in
  [PR #2770](https://github.com/litlfred/qou/pull/2770)** — a block-comment-aware
  codemod relocated the imports in all 44 (the count grew 40 → 44 as `main`
  advanced; **pure relocation**, the import set byte-identical per file). The
  gate's `lean-import-after-content` count is now **0**; full per-file compile
  remains CI-gated.

A new `--fail-on <categories>` flag drives a **diff-scoped** CI gate
([`.github/workflows/lean-content-siblings.yml`](../../.github/workflows/lean-content-siblings.yml)):
on each PR it runs the scanner over **only the changed `.lean` files** and
fails on the two compile-validity classes. Diff-scoping is deliberate — a
whole-tree gate would be red on the 40 pre-existing import-order defects and
block every PR; this blocks *new* drift instead (validated: green on this PR's
changed files, red on the skein control). This is the root-cause closure for
the class of latent breakage that produced the rho-k / kashaev defects.

### §3b stub-maturation backlog (2026-06-25)

Of the 34 degenerate `class … residual : ℝ; residual_eq_zero` + global
`instance := sorry` stubs, **`classical-riemann-hypothesis` was matured** in
[PR #2753](https://github.com/litlfred/qou/pull/2753) to the faithful statement
over Mathlib's `riemannZeta` — it is the one imported-famous stub cleanly
statable with a standard Mathlib definition. The remaining 33 **need infra
Mathlib lacks or per-conjecture formalization** and are **not** a mechanical
batch:

- **Imported-famous** (`qou-p-neq-np`, `yang-mills-mass-gap`,
  `q-birch-swinnerton-dyer`, `qou-infra-discharges-goncharov-zeta5`, the
  `single-volume-irrationality` / `hyperbolic-volume-transcendence` /
  `borel-zagier-qou-volumes` set) — require complexity-theory / QFT /
  elliptic-`L`-function / transcendence infrastructure **not in Mathlib**.
- **q-deformed / framework-specific** (`q-collatz`'s `C_q` map over
  `ℤ[q^±1]` with q-parity + positivity, the q-GL `q_oper_hecke` / `q_gl_*`
  family, the GS-spectral chain, the surreal-appendix set) — substantial
  **per-conjecture formalization**, often unverifiable in a partial-olean-cache
  sandbox.

These remain tracked under the existing `zslh` / `b3pe` / `mlt7` / `doth`
"resolve N placeholders" beans; maturation is research-formalization, best
done with a full Lean build (not a one-shot sandbox sweep).

### Spurious shadowing-duplicate stubs removed (2026-06-25)

A follow-up sweep split the degenerate `residual : ℝ := 0` + `instance :=
sorry` stubs into **spurious duplicates** vs **genuine** stubs. A stub is
*spurious* when the conjecture's `lean.ref` resolves (§0a candidate-2) to it
while its **exact** class FQN is *already declared faithfully* in another,
**in-build** file that the stub shadows (the staircase / double-magic pattern).
**None are false** — the real formalisation already exists.

**Deleted (9)** — each an orphan (imported nowhere) degenerate duplicate of an
in-build faithful class; deletion repoints the `lean.ref` (grep-fallback) to
the faithful declaration:

| Deleted stub | Faithful in-build twin |
|---|---|
| `DoubleMagicDeltaI/DeltaIBoundConjecture.lean` | `QOU/Interactions/DoubleMagicDeltaI.lean` (`DoubleMagicIsotope` data + `empirical_deltaI_le_one` proved + rich `DeltaIBoundConjecture` class + compute theorems) |
| `AppendixSurreals/{InfinitesimalFrobenius,InfinitesimalObservability,JonesBirthday,KashaevSurreal,OnPModularHecke,HahnSubstrate}.lean` (6) | `QOU/AppendixSurreals/Conjectures.lean` (Gemini-audited classes + `instProvable` + conditional theorems) |
| `Torsion/YangMillsMassGap.lean` | `QOU/Torsion/MassGap.lean` |
| `Observations/QCltNonCommutative/QCltNonCommutative.lean` | parent `QOU/Observations/QCltNonCommutative.lean` |

`VacuumEpsilon` was **excluded**: its stub class `VacuumEpsilon` ≠ the faithful
`VacuumEpsilon'` in `Conjectures.lean` (a rename), so it is a genuine stub, not
an exact duplicate — deleting it would dangle the ref.

**Net stub triage:** ~9 spurious shadowing-duplicates (deleted), 1 matured (RH,
#2753), and ~37 genuine open conjectures needing the per-conjecture
infrastructure above — not a mechanical batch.

### Method note (2026-06-25)

Inventory = a grep classifier over all `conjecture()` `.ts` blocks
resolving each `lean.ref` (sibling → lake-path → grep fallback) and
scanning the body for `sorry`/`class`/`axiom`/`: True := trivial`/
`native_decide`. The one defect was confirmed by `lean <file>` with
`LEAN_PATH` set to the restored oleans (full content-pipeline validation
could not run in-sandbox: the `litlfred/folio-assistant` platform repo is
out of session scope, proxy 403 — Lean compilation is the authoritative
check used instead).
