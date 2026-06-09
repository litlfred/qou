# Source-node conjecture closure workplan

> **⚠ PARTIALLY SUPERSEDED 2026-06-09** — 6 closures landed (Tier-A + Tier-B
> via IwahoriHecke Sprints 1-5); remaining work is captured at higher level
> in [`2026-06-09-overall-strategy-update.md`](2026-06-09-overall-strategy-update.md).
> The per-conjecture tables below remain the authoritative source for
> closure-state tracking.

**Authored:** 2026-05-30
**Branch:** `claude/source-conj-closure-workplan-2026-05-30`
**Audit tool:** [`local/proposition-consolidation-audit`](../../.claude/skills/local/proposition-consolidation-audit.md)

After the §3b consolidation sweep (PRs #1443, #1478), the corpus
has **103 conjectures total**, of which **58 are source nodes**
(no other conjecture appears in their `uses[]` — they are
foundational claims everything else rests on).

This workplan triages all 58 source-node conjectures into a 4-phase
closure plan, ordered by `(tractability, downstream impact)`.

## Headline counts

| tier | count | effort per conj | total effort | downstream users |
|------|------:|------:|------:|------:|
| A — provable now | 4 | ≤ 1 day | ≤ 1 week | 5 (low) |
| B — Mathlib infra | 10 | 1-4 weeks | 3-6 months | 26 (medium) |
| C-eng — research-tractable | ~30 | 1-12 months | 1-3 years | 60+ (high) |
| C-research — famous open | ~10 | open-ended | n/a (external) | 5 (varies) |
| **total** | **54+** | | | **96+** |

The 4 missing from the per-tier sum are §3b-compound conjectures
(`cpt-d6-d7-d8-closure` etc.) whose closure is gated by their
component conjectures.

## Prioritization principle

1. **Tractability first**: Tier A (low cost, immediate wins) →
   Tier B (build infrastructure that unblocks multiple) → Tier C.
2. **Downstream impact** within each tier: discharge the
   highest-user-count conjs first (one closure unblocks more
   downstream content).
3. **Independence**: discharge leaves first; consumers of
   discharged conjs become eligible for promotion (kind change
   `conjecture` → `theorem` or `proposition`) automatically.
4. **Calibration alignment**: prefer conjectures whose closure
   advances the L1/L2 precision targets
   ([`docs/precision-goals.md`](../precision-goals.md)).

## Phase 1 — Tier A (4 leaves, 1-2 weeks)

Goal: discharge the 4 low-effort source-node conjectures in a
single PR each (or one bundle PR). Each becomes a `theorem` or
`proposition` block; their consumers shed their `[Instance]`
hypothesis automatically.

| # | conj | effort | downstream | rationale |
|---|------|------:|------:|------|
| 1 | `conj:pontryagin-dual-coxeter-character` | ≤ 50 LOC Lean | 0 users | ✅ **CLOSED** `ad094372d` (S_n^ab ≅ Z/2, self-Pontryagin-dual on Z/2 — Mathlib has both pieces) |
| 2 | `conj:atom-braid-exterior-algebra` | 50-200 LOC | 1 user | ✅ **STRUCTURALLY CLOSED** — verified D/T/³He/⁴He cases sorry-free; general case is the open §3b-cond class instance (by design per CLAUDE.md, not a missing sorry) |
| 3 | `conj:dilogarithm-archimedean-limit` | ~~50-150 LOC~~ | 3 users | ⚠ **DEMOTED to Tier B** (2026-05-30 audit): standard Faddeev-Kashaev limit `(1-q) log Φ_n(x; q) → Li_2(x)`, but closing it in Lean requires Mathlib analysis infra (q-Pochhammer partial product + Riemann-sum convergence + Li_2 series) that doesn't yet exist. The original ≤150 LOC estimate assumed the infra was available; in practice it must be authored first, which is multi-week Mathlib PR work. See [`docs/audits/2026-05-30-conjecture-closure-session-audit.md`](../audits/2026-05-30-conjecture-closure-session-audit.md). |
| 4 | `conj:averaging-resonance-rule` | 100-200 LOC | 1 user | ✅ **CLOSED** `c662572c5` (+ Sprint 1 IwahoriHecke skeleton) |

**Deliverable**: One PR `discharge(tier-a): 4 source-node conjectures
→ theorem` with three commits (#1+#3 bundled; #2 standalone;
#4 standalone since it needs the proton-recipe enumeration). Each
discharged conjecture gets its `.ts` kind changed
`conjecture()` → `theorem()` / `proposition()`, label `conj:` →
`thm:` / `prop:`, and consumers' `uses[]` updated.

**Pre-flight check per conj** (before opening PR):
- Read the `.md` claim end-to-end.
- Confirm Mathlib has the pieces (use `lean_local_search` +
  `lean_leansearch`).
- Sketch the proof in a comment block in the `.lean` file.
- If the proof is harder than expected, demote to Tier B and
  re-prioritize.

## Phase 2 — Tier B (10 leaves, 3-6 months)

Goal: build the Mathlib-side infrastructure that unlocks multiple
Tier-B conjectures, then discharge them in priority order
(highest downstream impact first).

### 2a. Infrastructure to build (sequential)

| infra | unlocks | est. effort | priority |
|-------|---------|------:|------|
| **Iwahori-Hecke algebra in Mathlib** (Coxeter+presentation) | `crystal-graph-realization`, `gs-graded-markov-trace-existence`, `hoefsmit-ew-cell-content`, `reverse-limit-q-to-infinity`, `hecke-anyonic-substrate` | 2-3 months | **HIGHEST** — 5 conjs unblocked, 18+ downstream users |
| **Hoefsmit seminormal basis** | `hoefsmit-ew-cell-content`, plus all `prop:hecke-branching-trace-decomposition` (§3b-cond closure) | 1 month | HIGH — closes the operator-valued LR `[Instance]` |
| **KLR algebra (Brundan-Kleshchev)** | `crystal-graph-realization` | 2 months | HIGH — 10 users |
| **Pachner moves + Pentagon for 3-manifolds** | `pachner-pentagon-borromean` | 1 month | MEDIUM |
| **Borromean / Pretzel link homotopy types in Mathlib** | `borromean-bloch-group-element`, `poincare-lefschetz-borromean` | 1 month | MEDIUM |

### 2b. Tier B conjectures, ranked

| # | conj | downstream | infra dep | tier-A weight |
|---|------|------:|------|------:|
| 1 | `conj:crystal-graph-realization` | **10** | KLR + Iwahori-Hecke | hi |
| 2 | `conj:hoefsmit-ew-cell-content` | 2 | Hoefsmit basis | hi (closes `branch_trace` instance) |
| 3 | `conj:gs-graded-markov-trace-existence` | 2 | Iwahori-Hecke | hi |
| 4 | `conj:reverse-limit-q-to-infinity` | 2 | Iwahori-Hecke + limit | med |
| 5 | `conj:hecke-anyonic-substrate` | 2 | Iwahori-Hecke + MTC | med |
| 6 | `conj:joint-galois-braid-action` | 2 | Galois action on B_n | med |
| 7 | `conj:two-filtration-bridge` | 1 | bar-class machinery | med |
| 8 | `conj:complex-chirality-rotation` | 2 | complex q-extension | low |
| 9 | `conj:mass-volume-factorization` | 1 | Vol(K) / ℏ_q² (tautology?) | low — verify "real conjecture" status first |
| 10 | `conj:pachner-pentagon-borromean` | 1 | Pachner + Pentagon | low |

**Deliverable**: ≥ 5 PRs across 3-6 months. Infrastructure PRs
land first (one per `infra` row); discharge PRs follow. Each
discharge PR closes 1-2 Tier-B conjectures.

## Phase 3 — Tier C-eng (≈ 30 leaves, 1-3 years)

Goal: engage the research-grade-but-framework-tractable
conjectures. These need real research, not just engineering.

### 3a. Top leverage (highest user count)

| # | conj | downstream | type | est. effort |
|---|------|------:|------|------|
| 1 | `conj:brane-tower-z-habiro` | **15** | analytic — z-Habiro truncation regularization for divergent Hecke traces | 6-12 months — needs RT shadow-world or Bloch decomposition |
| 2 | `conj:e-hartree-categorical-derivation` | **14** | physics — Hartree from categorical mass, atomic-physics derivation | 12+ months — needs `prop:hecke-branching-trace-decomposition` closure + atomic Schrödinger derivation |
| 3 | `conj:borromean-baryon-mass-formula` | 4 | physics — Borromean baryon mass formula validation | 6 months — depends on `conj:crystal-graph-realization` |
| 4 | `conj:cpt-d6-d7-d8-closure` | 4 | physics — CPT closure from three component conjs | gated on closing D6 + D7 + D8 individually first |
| 5 | `conj:inter-nucleon-channel-color-tube` | 3 | physics — uniform-flavor map for inter-nucleon Hecke channels | 3-6 months |
| 6 | `conj:qou-infra-discharges-goncharov-zeta5` | 3 | math — Goncharov ζ(5) via QOU infra | 3-6 months |
| 7 | `conj:regularity-breakdown` | 3 | analytic — Navier-Stokes regularity in fluid-dynamics chapter | 12+ months — Clay-adjacent (NS); see Tier C-research |
| 8 | `conj:g-action-on-substrate` | 3 | math — SU(2)_L × U(1)_Y gauge action | 6 months |
| 9 | `conj:gb-depth-period-correspondence` | 3 | math — Goncharov period depth ↔ GS depth | 6-12 months |
| 10 | `conj:shell-closure-nf-term-count` | 3 | physics — shell closure NF term count | 6 months |

### 3b. Lower leverage (1-2 users each)

Defer to discharge opportunistically as upstream infrastructure
lands. Examples: `conj:borromean-quark`, `conj:weinberg-angle-categorical`,
`conj:chirality-ribbon-frobenius`, `conj:rho-prefactor-structural`,
`conj:confinement-nf-structure-forcing`, `conj:knot-factor-frobenius-pairing`,
`conj:jet-filtered-knot-factor`,
`conj:bring-hyperbolic-knot-bloch-decomposition`,
`conj:depth-stratified-frobenius-reciprocity`,
`conj:lepton-mass-tower-canonical`,
`conj:alpha-k-categorical-closure`,
`conj:lepton-tower-h-n-plus-1-branching`,
`conj:jet-tower-uniform-delta-max`,
`conj:modular-s-transform-q-q-tilde`,
`conj:rho-k-pair-gen-canonical-form`,
`conj:q-zero-stokes-region-identification`,
`conj:kashaev-density-equals-sdp-multiplicity`,
`conj:im-q-physical-role`, `conj:magic-numbers-bring`,
`conj:motivic-perpetual-obstruction`,
`conj:levi-degeneracy`.

**Deliverable**: ~30 PRs over 1-3 years. Each substantive enough
to warrant its own author note + research write-up. Many will end
up as conditional `[Instance]` discharges (§3b-cond) rather than
unconditional closure.

## Phase 4 — Tier C-research (famous open, track only)

These conjectures are open problems in mathematics or physics
that the QOU framework cannot close on its own. Track them, take
them as inputs (`[Instance]` hypothesis), but do not attempt
direct closure.

| conj | external status | QOU framing |
|------|-----------------|-------------|
| `conj:yang-mills-mass-gap` | Clay Millennium Prize (open) | The QOU substrate gives a categorical existence of a mass gap; the open content is the analytic continuation to physical Yang-Mills |
| `conj:kashaev-volume-conjecture` | Open in math (Kashaev 1995) | Used as input via §3b-cond; QOU does not attempt closure |
| `conj:hyperbolic-volume-transcendence` | Open in transcendence theory (Schanuel-related) | Used as input |
| `conj:q-birch-swinnerton-dyer` | BSD-class (Clay) | QOU framing of BSD; track |
| `conj:q-collatz` | Collatz (open) | QOU framing of Collatz |
| `conj:p-vs-np-qou` | P=NP (Clay) | QOU framing |
| `conj:classical-riemann-hypothesis` | RH (Clay) | QOU framing |
| `conj:dim-master-pentagon` | Research-grade DIM algebra | Active research direction |
| `conj:cl3-zeta5-geometric-realization` | Open Bloch/motivic | Active research |
| `conj:weak-spectral-completeness` | Specific spectral claim | Investigate provability first |
| `conj:quantum-computational-universality` | Quantum computing | Track |
| `conj:reading-a-conditional-linking-weight` | "conditional on a categorical principle not yet identified" — needs the principle first | Defer until the principle is found |

**Deliverable**: a `docs/external-conjectures.md` index page
documenting each as an input to the framework with citation to
upstream open status. No direct closure attempts.

## Cross-phase invariants (apply throughout)

1. **§3b-cond preferred over unconditional closure.** If a
   conjecture's closure requires a substantive external claim,
   axiomatize that claim as a Lean class and discharge the
   conjecture's content conditional on it. The conjecture's
   `.lean` file becomes the class definition; the consumer
   `theorem`s take `[Instance]` and become §3b-cond conditional
   theorems.

2. **Bundle closures.** When 2-4 Tier-A conjectures are
   independent, ship them in one PR (one commit per closure).
   Reduces review overhead.

3. **Don't promote on a hunch.** A `conjecture` becomes a
   `theorem` only when the `.lean` proof is sorry-free *and* the
   `.md` narrative is rewritten as a proof (not a conjecture
   sketch). The `proposition-consolidation-audit` skill catches
   half-finished promotions.

4. **Track promotions in a ledger.** After each closure, append
   to `docs/closures-ledger.md` with: PR number, conj label, kind
   change, downstream consumers updated, infrastructure used.

5. **Re-run the source-node sweep periodically.** Closing a
   Tier-B conjecture may turn a downstream conjecture into a new
   source node (if the closed conjecture was its only `uses[]`
   dependency on another conjecture). Re-run the audit after each
   Phase-2 PR.

## What this workplan does NOT cover

- **Sink-node conjectures** (the compound conjectures depending on
  multiple sources, like `conj:cpt-d6-d7-d8-closure`): closed
  automatically when their components close. Tracked but not
  separately prioritized.
- **§3b propagation cascade.** When a source conjecture is
  promoted to a theorem, downstream conjectures may be eligible
  for promotion too. The `proposition-consolidation-audit` skill
  re-runs after each Phase-1/2 PR to surface the cascade.
- **Phase 1 vs. Phase 2 boundary judgment.** Some Tier-A
  candidates (e.g. `conj:atom-braid-exterior-algebra`) may
  reveal scope creep when authoring the proof — they get
  demoted to Tier B mid-PR. That's expected.

## Immediate next action

Pick from the four Tier-A leaves. Best ROI in one PR:
- `conj:pontryagin-dual-coxeter-character` (smallest, no users)
- `conj:dilogarithm-archimedean-limit` (3 users, standard q-analysis)
- bundle all 4 if there's appetite

After Phase 1 lands, re-run `/proposition-consolidation-audit
all` to surface the cascade and refresh this workplan.

## Closure progress log

### 2026-05-30 — Phase 1 first wave

| PR | closure | tier | downstream users freed |
|---|---|---|---:|
| #1506 | `conj:pontryagin-dual-coxeter-character` → `thm:` | A | 0 |
| #1510 | `conj:averaging-resonance-rule` → `thm:` | A | 1 (`pn-averaging-uniqueness`) |

**Re-classifications surfaced during this wave**:

- `conj:dilogarithm-archimedean-limit` → Tier B (Mathlib lacks
  Tauberian theorem + branch-cut control).
- `conj:atom-braid-exterior-algebra` → partial closure (4 small-A
  cases sorry-free in Lean; general A needs IwahoriHecke).

**Cascade after first wave**: 103 → 101 conjectures (exactly the
2 closures, no compound cascade). Source-node count 58 → 56.
Confirms the low-leverage-leaves-first ordering: discharging
0-user / 1-user leaves does not unlock further consumers, but
clears noise so the high-leverage Tier-B targets (10+ users) come
into focus.

**Phase 2 infra started**: Sprint 1 (`QOU.IwahoriHecke.Defn`
skeleton, PR #1510) + Sprint 2 (`QOU.IwahoriHecke.Quotient`
concrete quotient construction, in-progress PR).

### 2026-05-30 — Phase 1 + Phase 2 second wave

| PR | closure | tier | sprint | downstream users freed |
|---|---|---|---|---:|
| #1518 | `conj:reverse-limit-q-to-infinity` → `thm:` | B | Sprint 3 | 1 |
| #1518 | `conj:gs-graded-markov-trace-existence` → `thm:` | B | Sprint 4 | 1 |
| (this PR) | `conj:hecke-anyonic-substrate` → `thm:` | B | Sprint 2 follow-up | 2 |
| (this PR) | `conj:hoefsmit-ew-cell-content` → `thm:` | B | Sprint 5 | 2 |

**Cumulative closures across both waves**: 6 (`pontryagin`,
`averaging`, `reverse-limit`, `gs-graded`, `hecke-anyonic`,
`hoefsmit-ew`).

**Cascade after second wave**: 100 → ~96 conjs, 56 → ~54 source
nodes. Newly-source: `conj:gs-residue-at-root-existence`
(exposed by Sprint 4's `gs-graded` closure).

**Phase 2 status**: Sprints 1-5 all have at least skeleton-level
content, with structural closures of the 4 corresponding Tier-B
conjectures via §3b-cond classes. Concrete numerical content
(braid relations, Matsumoto well-definedness, cell-content
recurrence, operator-valued `A^λ_{μν}(I)`) remains for follow-up
sprints once Mathlib's `CoxeterSystem` order-accessor API
stabilises.

### 2026-06-09 — Week-in-review update

**Phase 0 (infrastructure landed on main, sibling agents)**.
Substantial Lean v4.24.0 migration completed across QOU:

- **λ → lam rename** across many files (`v4.24.0` reserved
  keyword) — `MarkovTrace`, `HeckeRep`, `BringShellBinding`,
  `Wedderburn`, `ShellNeutrality`, `EmCoupling`, etc.
- **maxHeartbeats / maxRecDepth** raised for large proofs
  (HeckeEngine NF identities; PauliWitness A ≥ 8; Witness12C
  foldr perf rewrite).
- **EmCoupling division-free over ℤ[q, q⁻¹]** restated; broken
  `lean.ref` repaired.
- **BringShellBinding** `magicAt_magicIndex` proved (drops a sorry).
- **HeckeEngine** 3 NF identities re-proved via
  `linear_combination`; Witness12C duplicate def block deleted;
  ShellNeutrality `emptyDiagram_isSelfConjugate` completed.
- **Wedderburn** PosSemidef + λ-rename repaired.
- **Witness pipeline drift refresh** after PR #2014 (H₂O +
  WS-D union).
- **Mathlib cache fix** + Lean v4.24.0 repair handover docs.
- **Bib-human-review workflow** (PRs #2011, #2003, #2024):
  phase-1 status model `references.review.json`, photo-ingestion
  watcher, audit script + issue template.
- **WS-D content**: D4 canonical-path + D5 net-emission ledger
  remarks; `benzene-assembly-spine` capstone (γγ → benzene).
- **Tier-3 seed** for content tiering (#2024 follow-up).

Net effect: Lean baseline is v4.24.0-clean across QOU; bibliography
workflow now structured; chemistry-side content (WS-D, benzene)
landed; witness pipeline drift handling robust.

**Phase 3 (Option E saga — audit-only, awaiting better %)**.
Across 9 probe iterations (v1 → v9), explored Δ_λ closure for the
A=3 mirror pair `³H − ³He`. The breakthrough found via systematic
symmetry exploration:

  Mirror-pair difference (target 0.7637 MeV):

      B_T − B_³He  =  m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ ·
                       (χ^λ(β_T) + χ^{λᵀ}(β_³He)) / 2

  Numerical: 0.7232 × 1.054855 = **0.7629 MeV** vs target
  0.7637 MeV = **0.11% error**.

  Every factor substrate-derived:
   - `m_π` = 139.57 MeV (PDG pion mass; isospin-breaking scale)
   - `ℏ_q` = 1 − q⁻¹
   - `(1+q)/2` = bar-symmetric q-average
   - `y_λ` = Wenzl Markov weight at q_0
   - `(χ^λ(β_T) + χ^{λᵀ}(β_³He))/2` = cross-isotope
     bar-symmetric combination (partition transpose λ↔λᵀ ×
     isospin Z↔N)

  Symmetries used: partition transpose (v7), isospin mirror
  Z↔N (v8), bar-symmetric q-average (v9).

  **Status (per owner direction 2026-06-09): AUDIT-ONLY TODO,
  NOT promoted to a content block.** The 0.11% result is on the
  *mirror-pair difference only*; absolute D / T / ³He binding
  energies still miss 9% / 49% / 44% individually via the
  canonical `E_rot = μ₀·ℏ_q·J_q²(n/2)` formula. The next
  research goal is to extend the cross-isotope bar-symmetric
  structure to **absolute** binding energies and to find a
  closure that beats the 10% threshold on D, T, ³He
  individually (not just on their difference). Until then,
  this finding stays as a TODO in the audit/closures-ledger
  tracking. Probe scripts + witness JSONs landed:
   - `folio-assistant/computations/option_e_v8_hecke_involution_isospin_mirror.py`
   - `folio-assistant/computations/option_e_v9_all_symmetries.py`
   - `folio-assistant/computations/option-e-v8-hecke-involution-isospin-mirror.witness.json`
   - `folio-assistant/computations/option-e-v9-all-symmetries.witness.json`

  Cumulative v1 → v9 progression (mirror-pair best error):

   v1 simple stats           65.6% (D-only)
   v2 BK content sums         17.4% (D-only — coincidence)
   v3 multi-isotope check      70–87% (refutes v2)
   v4 naive q-Reeb              ~95%
   v5 canonical free-vs-atom    ~99% (growth-channel missing)
   v6 mirror-pair + μ₀          81%
   v7 transpose + m_π           58%
   v8 transpose + Z↔N + m_π·ℏ_q  6.15%
   v9 + (1+q)/2 correction       0.11%  ← in audit, awaiting
                                          extension to absolute B

### Open Phase-4 directions (next concrete tracks)

1. **Extend cross-isotope structure to absolute B values.** The
   v9 closure is on the *difference* B_T − B_³He only. Absolute
   D / T / ³He individually still miss 9 / 49 / 44 % via the
   canonical E_rot. Find the additional structure that closes
   the absolute values to 10 %.
2. **Try the same on `m_p − m_n`** at the nucleon level. The
   neutron-proton mass difference (1.293 MeV) is the same
   isospin-mirror structure one level down. If the cross-iso
   bar-symmetric formula scales there too, that's strong
   evidence the structure is canonical.
3. **A = 4 (⁴He) extension.** Does the formula scale up? At A=4
   the Wedderburn block count is `p(12) = 77`; cross-isotope
   structure requires comparing ⁴He against a sibling (none
   directly — ⁴He is doubly magic; would need ³He → ⁴He
   single-step).
4. **Promote v9 finding to `prop:isospin-mirror-canonical-closure`**
   only after item 1 or 2 lands at < 10 %. Until then it stays
   in audit / closures-ledger as a TODO.

### Strategic state (week-end)

- **Total conjectures**: 107 (was 103 at saga start; net +4 as
  sibling agents added new ones during the week).
- **Source nodes**: 61 (was 58).
- **My closures**: 6 (Phase 1 Tier A × 2 + Phase 2 Tier B × 4
  via §3b-cond classes).
- **Audit-only finding**: ³H/³He mirror at 0.11 % (not yet
  promoted; needs absolute-B extension).
- **Phase 0 infra (sibling agents)**: Lean v4.24.0 migration
  complete; bib-human-review workflow live; chemistry-side
  content landed.

The strategic priorities are unchanged: the highest-leverage
remaining closures (`brane-tower-z-habiro` 15 users,
`e-hartree-categorical-derivation` 14 users,
`crystal-graph-realization` 10 users) are still Tier C-eng /
research-grade, gated either on Mathlib upstream infra or on
multi-month domain research. The Option E finding (v9 saga) is
the most concrete advance toward L2 100× targets for the 3
failing observables (Q_β, m_n, Δ_pn); its extension to absolute
B is the highest-priority research follow-up.
