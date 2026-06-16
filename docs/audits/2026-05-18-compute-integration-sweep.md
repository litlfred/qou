# Compute Integration Sweep — 2026-05-18

**Mode:** IDLE-SWEEP (one-shot, full content scan)
**Branch:** `claude/iw-compute-idle-sweep-2026-05-18`
**Source:** `origin/main` HEAD on 2026-05-18
**Skill:** `local/compute-integration-watcher` (PR #693 merge)
**Scope:** every `prop:*` / `thm:*` / `lem:*` / `cor:*` block under
`content/quantum-observable-universe/**/*.ts`.

The skill's I-pattern catalogue (I1–I12) is defined in
[`.claude/skills/local/compute-integration-watcher.md`](../../.claude/skills/local/compute-integration-watcher.md).

---

## 1. Inventory count by verdict


- **Total provable blocks scanned:** 558
- **WIRED** (probe + production consumer + Lean): **11**
- **PROBE-ONLY** (witness exists, not threaded into production): **34**
- **NOT-WIRED** (no probe witness; mostly I1 + I1-stated + I1-pre): **513**
- **CONDITIONAL** (skipped per §3b-cond): **0**

### Pattern frequency

| Pattern | Count | Description |
|---|---|---|
| `ok` (WIRED) | 11 | passes all 6 checklist items |
| `I1` | 483 | Lean-proved, no probe witness |
| `I1-stated` | 27 | Lean stated with open sorrys; needs proof first, then probe |
| `I1-pre` | 3 | no .lean sibling at all (deepest gap) |
| `I2` | 34 | probe-only — witness exists, no production consumer |

### Auxiliary pattern hits (cross-witness scan, beyond per-block)

- **I4 — upstream-hash drift:** 0 (clean — `witness_dependency_drift.py` policy holding)
- **I5 — `contentBlock` references missing label:** 9
- **I6 — empty `data` section in witness:** 0
- **I7 — probe stale > 7 days behind block `.md`:** 86 (across 86 witness files)
- **I12 — content `lean.ref` does not resolve to sibling decl:** 305

### Distribution by chapter

| Chapter | NOT-WIRED | PROBE-ONLY | WIRED |
|---|---|---|---|
| `appendix-surreals` | 11 | 0 | 0 |
| `braids-and-knots` | 192 | 23 | 11 |
| `descartes-universe` | 86 | 5 | 0 |
| `fluid-dynamics` | 21 | 0 | 0 |
| `information-theory` | 17 | 0 | 0 |
| `lifting-and-descent` | 30 | 0 | 0 |
| `models-of-qous` | 4 | 1 | 0 |
| `molecular-construction` | 6 | 1 | 0 |
| `observations` | 26 | 0 | 0 |
| `organic-chemistry` | 2 | 0 | 0 |
| `particle-interactions` | 40 | 4 | 0 |
| `q-geometric-langlands` | 6 | 0 | 0 |
| `quantum-observable-universes` | 63 | 0 | 0 |
| `quantum-universes` | 9 | 0 | 0 |

**Observation.** All 11 WIRED blocks live in `braids-and-knots/`; the production mass-pipeline (`paper_six_term_isotope_sweep.py`, `derive_m_{p,n}_hecke_full_tower_50dps.py`, `atomic_mass_via_rho_k.py`, `build_{proton,neutron}_mass_50dps_chain.py`) is the only sink for substrate compute today. The 13 other chapters have 0 wired blocks — Lean-only side of the substrate. Idle-sweep treats `quantum-observable-universes/`, `fluid-dynamics/`, `q-geometric-langlands/`, `quantum-universes/` as *structurally* below the wiring layer (they define the categorical infrastructure; consumers live in the physics chapters).

---

## 2. Ranked top-10 fixes by severity × tractability

Severity rubric:
- **S1** (top): block is a *direct* dependency of a WIRED production prop and the missing wiring is the main reason production has CAL-dependence elsewhere.
- **S2:** block is a high-degree hub (≥12 reverse-deps in `uses[]`) and missing from compute.
- **S3:** PROBE-ONLY block where the witness file already exists and the recipe is a one-line import into a production script.
- **S4:** I5/I12 cleanup — minor schema fixes, gating future `bun run validate` clean runs.
- **S5:** stale-probe rerun (I7) — re-run + commit when scripts haven't drifted.

Tractability: T1 = ≤30 min · T2 = 1–3 h · T3 = ≥1 day.

| # | Block / Action | I-pattern | Severity | Tractability | Recipe |
|---|---|---|---|---|---|
| 1 | **`thm:wedderburn-mass-formula`** (40 reverse-deps) — author probe pinning Wedderburn block weights against `mass-formula-6term-mpfr-50dps.witness.json` rows | I1 | S1 | T2 | `probe_wedderburn_mass_formula.py` → witness with `contentBlock`, threaded into `paper_six_term_isotope_sweep.py` as a cross-check |
| 2 | **`thm:jones-markov-trace`** (40 reverse-deps) — the cornerstone of all knot-mass → Markov-trace identities; currently I1 | I1 | S1 | T2 | author probe asserting Markov-trace closed-form vs `markov-peel-atomic-tr-m.witness.json` |
| 3 | **`prop:y-lambda-closed-form-wenzl-bridge`** + **`prop:y-lambda-recipe-from-partition`** — PROBE-ONLY; `y-lambda-at-q0.witness.json` and `probe-wedderburn-weight-scheme.witness.json` already exist | I2 | S1 | T1 | thread both witnesses into `paper_six_term_isotope_sweep.py` Term-7 closed-form (currently uses `\tilde w_\lambda` directly) |
| 4 | **`prop:three-calibration-inputs`** — PROBE-ONLY; `cal-3-q-beta.witness.json` and `codata-2022-validation-masses.witness.json` exist | I2 | S1 | T1 | `paper_six_term_isotope_sweep.py` already reads CAL constants; add explicit `import cal-3-q-beta` thread + `reference_blocks` field on the consumer witness |
| 5 | **`prop:mass-coefficient-shadow-price`** — PROBE-ONLY; LP-dual shadow-price machinery for `a_K` | I2 | S2 | T1 | thread `a-K-via-lp-dual-hecke-basis.witness.json` into `atomic_mass_via_rho_k.py` (currently uses hardcoded `a_K` magnitudes per audit witness) |
| 6 | **`prop:per-nucleon-shift-additive-linearity`** — PROBE-ONLY; `per-nucleon-shift-derivation.witness.json` | I2 | S2 | T1 | thread into `paper_six_term_isotope_sweep.py` per-nucleon term assembly |
| 7 | **`prop:markov-trace-axiomatic-closed-form`** — PROBE-ONLY; `option-b-proton-mass-full-chain.witness.json` | I2 | S2 | T1 | thread into `build_proton_mass_50dps_chain.py` as the canonical Markov-trace axiom |
| 8 | **I5 cleanup** — 9 witness files reference undefined labels (`prop:magic-shell-coupling-witness`×5, `prop:atomic-mass-via-rho-k`×2, `prop:codata-mass-anchors`, `prop:beta-decay-energy-scale`) | I5 | S4 | T1 | for each, either author the missing content block (preferred for magic-shell-coupling-witness, codata-mass-anchors, atomic-mass-via-rho-k) or repoint `contentBlock` to closest sibling |
| 9 | **I12 cleanup batch** — 305 `lean.ref` URIs do not resolve to a sibling-file declaration. Of these, a clean ~50% are name-drift on Lean side (theorem was renamed) | I12 | S4 | T2 | run `bun run validate <paper> --strict` and triage; either rename the Lean decl or update the `.ts` `ref:` URI |
| 10 | **I7 stale-probe rerun batch** — 86 witness files >7d behind `.md` mtime; 16 are >20d. Top offenders: `h2-integer-lp.witness.json` (32d), `mass-from-q-symbolic.witness.json` (31d), `confined-knot-binding.witness.json` (28d) | I7 | S5 | T1 | rerun each probe; commit if numerics unchanged, surface to author if shifted |

**Beyond the top-10:** the bulk of `I1` (483 hits) is a green-field formalization-vs-compute boundary. The pattern is: a `prop:` block in `braids-and-knots/` or `descartes-universe/` has a fully proved `.lean` sibling but no `probe_*.py` to materialize the numerical claim at $q_0$. These are individually low-leverage but collectively the path from substrate-pure derivation to a closed compute chain. Recommended batched fix (separate PR, after the top-10 land): a `claude/compute-integration-fixes-2026-05-18` follow-up branch that authors ~20 small probes for the top reverse-dep blocks listed below.

### Top-20 high-degree NOT-WIRED hubs (for batched probe authoring)

| Reverse-deps | Block | Verdict |
|---|---|---|
| 40 | `thm:jones-markov-trace` (theorem) | NOT-WIRED (I1) |
| 22 | `prop:gb-spectral-sequence` (proposition) | NOT-WIRED (I1) |
| 19 | `prop:categorical-mass-markov` (proposition) | NOT-WIRED (I1) |
| 17 | `thm:wedderburn-mass-formula` (theorem) | NOT-WIRED (I1) |
| 16 | `prop:hoefsmit-V21-cos-symmetrization` (proposition) | NOT-WIRED (I1) |
| 16 | `prop:beta-decay-transfer-matrix` (proposition) | NOT-WIRED (I1) |
| 15 | `prop:braid-action-tensor` (proposition) | NOT-WIRED (I1) |
| 14 | `prop:force-carrier-bring-uniqueness` (proposition) | NOT-WIRED (I1) |
| 13 | `prop:em-coupling-projection` (proposition) | NOT-WIRED (I1) |
| 13 | `prop:confinement-sdp` (proposition) | NOT-WIRED (I1) |
| 13 | `prop:borel-partial-resolution` (proposition) | NOT-WIRED (I1) |
| 13 | `prop:alpha-k-derivation-procedure` (proposition) | NOT-WIRED (I1) |
| 12 | `thm:markov-trace-factorization` (theorem) | NOT-WIRED (I1) |
| 12 | `prop:wedderburn-weight-canonical` (proposition) | NOT-WIRED (I1) |
| 12 | `prop:topological-mass-formula` (proposition) | NOT-WIRED (I1) |
| 12 | `prop:spectral-sequence-collapse` (proposition) | NOT-WIRED (I1) |
| 12 | `prop:hoefsmit-seminormal-form` (proposition) | NOT-WIRED (I1) |
| 12 | `cor:quantum-dilogarithm` (corollary) | NOT-WIRED (I1) |
| 11 | `prop:wedderburn-trace-identity` (proposition) | NOT-WIRED (I1) |
| 11 | `prop:gb-residue-spectral-sum` (proposition) | NOT-WIRED (I1) |

---

## 3. Per-block table

Full sweep results — 558 blocks, sorted by verdict (WIRED → PROBE-ONLY → NOT-WIRED) and within verdict by label. Stale-probe (I7) annotations are inlined into the fix-recipe column.
| label | kind | verdict | I-pattern | fix recipe |
|---|---|---|---|---|
| `prop:atom-knot-mass-derivation` | proposition | WIRED | ok | (probe stale 21d behind .md - I7) consumed in production chain |
| `prop:atomic-mass-gb-nf` | proposition | WIRED | ok | (probe stale 12d behind .md - I7) consumed in production chain |
| `prop:chirality-dual-space-derivation` | proposition | WIRED | ok | consumed in production chain |
| `prop:flavor-dressed-mass-from-substrate-split` | proposition | WIRED | ok | consumed in production chain |
| `prop:full-pole-structure-mass-trace` | proposition | WIRED | ok | (probe stale 17d behind .md - I7) consumed in production chain |
| `prop:hopf-jones-c3-categorical` | proposition | WIRED | ok | consumed in production chain |
| `prop:kashiwara-jones-c4-categorical` | proposition | WIRED | ok | consumed in production chain |
| `prop:markov-pair-z2` | proposition | WIRED | ok | (probe stale 11d behind .md - I7) consumed in production chain |
| `prop:mass-endomorphism-tower` | proposition | WIRED | ok | (probe stale 20d behind .md - I7) consumed in production chain |
| `prop:q-beta-categorical-precision-ladder` | proposition | WIRED | ok | consumed in production chain |
| `thm:knot-mass-formula-unified` | theorem | WIRED | ok | (probe stale 19d behind .md - I7) consumed in production chain |
| `prop:alpha-em-shift-multiplicative-chain` | proposition | PROBE-ONLY | I2 | (probe stale 10d behind .md - I7) Thread alpha-em-shift-multiplicative-chain.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:alpha-shift-torus-knot` | proposition | PROBE-ONLY | I2 | (probe stale 10d behind .md - I7) Thread nh-basis-shift.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:baryon-product-from-alt` | proposition | PROBE-ONLY | I2 | Thread baryon-product-from-alt.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:chi-lambda-w0-sign-weighting` | proposition | PROBE-ONLY | I2 | Thread chi-lambda-w0-sign-weighting.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:chirality-writhe-ribbon-derivation` | proposition | PROBE-ONLY | I2 | (probe stale 9d behind .md - I7) Thread chirality-avg-content.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:confined-knot-binding` | proposition | PROBE-ONLY | I2 | (probe stale 28d behind .md - I7) Thread jet-knot-invariants.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:confinement-frobenius-reciprocity` | proposition | PROBE-ONLY | I2 | (probe stale 9d behind .md - I7) Thread borromean-axial-coupling.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:confinement-nf-partial-proof` | proposition | PROBE-ONLY | I2 | Thread shift-from-nf-basis.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:demazure-fiber-markov-trace` | proposition | PROBE-ONLY | I2 | Thread demazure-markov-trace.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:graded-hecke-energy-truncation-bound` | proposition | PROBE-ONLY | I2 | Thread graded-hecke-energy-probe.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:h2-lp-dual-binding` | proposition | PROBE-ONLY | I2 | (probe stale 32d behind .md - I7) Thread h2-integer-lp.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:jet-gb-pl-correspondence` | proposition | PROBE-ONLY | I2 | Thread jet-gb-pl-correspondence.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:joint-tower-sdp-confinement` | proposition | PROBE-ONLY | I2 | (probe stale 17d behind .md - I7) Thread neutron-gap-probes.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:knot-operator-lp-selection` | proposition | PROBE-ONLY | I2 | (probe stale 7d behind .md - I7) Thread wedderburn-lp-ew-wiring.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:macdonald-hook-telescope` | proposition | PROBE-ONLY | I2 | (probe stale 9d behind .md - I7) Thread alpha-k-macdonald-closed-form.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:markov-trace-axiomatic-closed-form` | proposition | PROBE-ONLY | I2 | (probe stale 8d behind .md - I7) Thread option-b-proton-mass-full-chain.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:mass-coefficient-shadow-price` | proposition | PROBE-ONLY | I2 | (probe stale 8d behind .md - I7) Thread a-K-via-lp-dual-hecke-basis.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:mass-formula-iterative-lp-dual` | proposition | PROBE-ONLY | I2 | Thread iterative-lp-dual-levels.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `conj:mobius-limit-from-thimble` | conjecture | PROBE-ONLY | I2 | Thread mobius-limit-from-thimble.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:mostow-confinement` | proposition | PROBE-ONLY | I2 | Thread hyperbolic-volumes.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:neutron-qvalue-symbolic` | proposition | PROBE-ONLY | I2 | Thread q-beta-form-a-n1-extension.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:operator-selection-lp` | proposition | PROBE-ONLY | I2 | Thread he4-canonical-tr-m-block-fingerprint.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:per-nucleon-shift-additive-linearity` | proposition | PROBE-ONLY | I2 | (probe stale 10d behind .md - I7) Thread per-nucleon-shift-derivation.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:phi-q-categorical-truncation` | proposition | PROBE-ONLY | I2 | Thread probe-tritium-k-star.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:q-beta-spectral-bridge` | proposition | PROBE-ONLY | I2 | Thread q-beta-spectral-bridge.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:rho-k-h3a-refinement` | proposition | PROBE-ONLY | I2 | Thread delta-lambda-closure-v2-combined-pole.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:rigid-monoidal-structural-gap-invariance` | proposition | PROBE-ONLY | I2 | Thread tau-three-path-convention-independence.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:shell-schur-weyl-self-duality` | proposition | PROBE-ONLY | I2 | (probe stale 20d behind .md - I7) Thread probe-per-nucleon-self-duality.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:sw-period-thimble-equivalence` | proposition | PROBE-ONLY | I2 | Thread sw-period-thimble-equivalence.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:three-calibration-inputs` | proposition | PROBE-ONLY | I2 | (probe stale 8d behind .md - I7) Thread cal-3-q-beta.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:y-lambda-closed-form-wenzl-bridge` | proposition | PROBE-ONLY | I2 | Thread y-lambda-at-q0.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `prop:y-lambda-recipe-from-partition` | proposition | PROBE-ONLY | I2 | (probe stale 17d behind .md - I7) Thread probe-wedderburn-weight-scheme.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `thm:six-term-mass-formula-complete` | theorem | PROBE-ONLY | I2 | (probe stale 12d behind .md - I7) Thread term6-residues-at-roots.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `thm:topological-mass` | theorem | PROBE-ONLY | I2 | (probe stale 31d behind .md - I7) Thread mass-from-q-symbolic.witness.json into a production consumer (paper_six_term_isotope_sweep or mass-tower derive) OR add `# probe-only: <reason>` header. |
| `cor:commutative-chirality-vanishes` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:commutative-chirality-vanishes at q0; emit witness with contentBlock="cor:commutative-chirality-vanishes". |
| `cor:descartes-braid-structure` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:descartes-braid-structure at q0; emit witness with contentBlock="cor:descartes-braid-structure". |
| `cor:descartes-knot-eigenbasis` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:descartes-knot-eigenbasis at q0; emit witness with contentBlock="cor:descartes-knot-eigenbasis". |
| `cor:gauge-coupling-uniqueness` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:gauge-coupling-uniqueness at q0; emit witness with contentBlock="cor:gauge-coupling-uniqueness". |
| `cor:habiro-expansion-atomic` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:habiro-expansion-atomic at q0; emit witness with contentBlock="cor:habiro-expansion-atomic". |
| `cor:jet-prolongation-C` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:jet-prolongation-C at q0; emit witness with contentBlock="cor:jet-prolongation-C". |
| `cor:knot-factor-amphicheiral` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:knot-factor-amphicheiral at q0; emit witness with contentBlock="cor:knot-factor-amphicheiral". |
| `cor:knot-factor-borromean-composite` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:knot-factor-borromean-composite at q0; emit witness with contentBlock="cor:knot-factor-borromean-composite". |
| `cor:knot-factor-shell-closed` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:knot-factor-shell-closed at q0; emit witness with contentBlock="cor:knot-factor-shell-closed". |
| `cor:mass-identity-C` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:mass-identity-C at q0; emit witness with contentBlock="cor:mass-identity-C". |
| `cor:non-self-intersection` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:non-self-intersection at q0; emit witness with contentBlock="cor:non-self-intersection". |
| `cor:quantum-dilogarithm` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:quantum-dilogarithm at q0; emit witness with contentBlock="cor:quantum-dilogarithm". |
| `cor:spectral-decomposition-qvalue` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:spectral-decomposition-qvalue at q0; emit witness with contentBlock="cor:spectral-decomposition-qvalue". |
| `cor:spectral-half-line` | corollary | NOT-WIRED | I1 | Write probe_*.py exercising cor:spectral-half-line at q0; emit witness with contentBlock="cor:spectral-half-line". |
| `lem:brings-euler-characteristic` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:brings-euler-characteristic at q0; emit witness with contentBlock="lem:brings-euler-characteristic". |
| `lem:brings-riemann-hurwitz` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:brings-riemann-hurwitz at q0; emit witness with contentBlock="lem:brings-riemann-hurwitz". |
| `lem:categorical-irreducible` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:categorical-irreducible at q0; emit witness with contentBlock="lem:categorical-irreducible". |
| `lem:ccg-cosimplicial-identities` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:ccg-cosimplicial-identities at q0; emit witness with contentBlock="lem:ccg-cosimplicial-identities". |
| `lem:ccg-crossed-module-structure` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:ccg-crossed-module-structure at q0; emit witness with contentBlock="lem:ccg-crossed-module-structure". |
| `lem:chebyshev-degree-genus` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:chebyshev-degree-genus at q0; emit witness with contentBlock="lem:chebyshev-degree-genus". |
| `lem:degree-one-braid-trivial-volume` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:degree-one-braid-trivial-volume at q0; emit witness with contentBlock="lem:degree-one-braid-trivial-volume". |
| `lem:descent` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:descent at q0; emit witness with contentBlock="lem:descent". |
| `lem:descent-cocycle-deviation` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:descent-cocycle-deviation at q0; emit witness with contentBlock="lem:descent-cocycle-deviation". |
| `lem:deuteron-binding-energy` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:deuteron-binding-energy at q0; emit witness with contentBlock="lem:deuteron-binding-energy". |
| `lem:fai-projector-coadjoint-orbit` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:fai-projector-coadjoint-orbit at q0; emit witness with contentBlock="lem:fai-projector-coadjoint-orbit". |
| `lem:feynman-eigenbasis-decomposition` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:feynman-eigenbasis-decomposition at q0; emit witness with contentBlock="lem:feynman-eigenbasis-decomposition". |
| `lem:feynman-markov-identification` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:feynman-markov-identification at q0; emit witness with contentBlock="lem:feynman-markov-identification". |
| `lem:feynman-trace-collapse` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:feynman-trace-collapse at q0; emit witness with contentBlock="lem:feynman-trace-collapse". |
| `lem:genus-from-hecke-completeness` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:genus-from-hecke-completeness at q0; emit witness with contentBlock="lem:genus-from-hecke-completeness". |
| `lem:genus-ideal-characterisation` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:genus-ideal-characterisation at q0; emit witness with contentBlock="lem:genus-ideal-characterisation". |
| `lem:jet-prolongation-categorical-jet` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:jet-prolongation-categorical-jet at q0; emit witness with contentBlock="lem:jet-prolongation-categorical-jet". |
| `lem:mi-sw-abelianisation-cartan` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:mi-sw-abelianisation-cartan at q0; emit witness with contentBlock="lem:mi-sw-abelianisation-cartan". |
| `lem:mobius-energy-frobenius-kernel` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:mobius-energy-frobenius-kernel at q0; emit witness with contentBlock="lem:mobius-energy-frobenius-kernel". |
| `lem:nsi-q-deformed-kernel` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:nsi-q-deformed-kernel at q0; emit witness with contentBlock="lem:nsi-q-deformed-kernel". |
| `lem:nucleon-borromean-topology` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:nucleon-borromean-topology at q0; emit witness with contentBlock="lem:nucleon-borromean-topology". |
| `lem:pair-skein-mass-formula` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:pair-skein-mass-formula at q0; emit witness with contentBlock="lem:pair-skein-mass-formula". |
| `lem:qou-exists-axiom-1` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:qou-exists-axiom-1 at q0; emit witness with contentBlock="lem:qou-exists-axiom-1". |
| `lem:qou-exists-axiom-2` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:qou-exists-axiom-2 at q0; emit witness with contentBlock="lem:qou-exists-axiom-2". |
| `lem:qou-exists-axiom-3` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:qou-exists-axiom-3 at q0; emit witness with contentBlock="lem:qou-exists-axiom-3". |
| `lem:qou-exists-axiom-4` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:qou-exists-axiom-4 at q0; emit witness with contentBlock="lem:qou-exists-axiom-4". |
| `lem:skein-mass-from-linking` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:skein-mass-from-linking at q0; emit witness with contentBlock="lem:skein-mass-from-linking". |
| `lem:staircase-corner-hook` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:staircase-corner-hook at q0; emit witness with contentBlock="lem:staircase-corner-hook". |
| `lem:su2-emergence-dagger-unitarity` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:su2-emergence-dagger-unitarity at q0; emit witness with contentBlock="lem:su2-emergence-dagger-unitarity". |
| `lem:su2-emergence-volume-determinant` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:su2-emergence-volume-determinant at q0; emit witness with contentBlock="lem:su2-emergence-volume-determinant". |
| `lem:surreal-squeeze` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:surreal-squeeze at q0; emit witness with contentBlock="lem:surreal-squeeze". |
| `lem:tmli-constituent-composite-agreement` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:tmli-constituent-composite-agreement at q0; emit witness with contentBlock="lem:tmli-constituent-composite-agreement". |
| `lem:topological-mass-cat-descended` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:topological-mass-cat-descended at q0; emit witness with contentBlock="lem:topological-mass-cat-descended". |
| `lem:topological-mass-cat-eigenspace` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:topological-mass-cat-eigenspace at q0; emit witness with contentBlock="lem:topological-mass-cat-eigenspace". |
| `lem:topological-mass-cat-transient` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:topological-mass-cat-transient at q0; emit witness with contentBlock="lem:topological-mass-cat-transient". |
| `lem:topological-mass-dilogarithm` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:topological-mass-dilogarithm at q0; emit witness with contentBlock="lem:topological-mass-dilogarithm". |
| `lem:topological-mass-eigenspace-decomp` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:topological-mass-eigenspace-decomp at q0; emit witness with contentBlock="lem:topological-mass-eigenspace-decomp". |
| `lem:topological-mass-holonomy` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:topological-mass-holonomy at q0; emit witness with contentBlock="lem:topological-mass-holonomy". |
| `lem:topological-mass-transient-localisation` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:topological-mass-transient-localisation at q0; emit witness with contentBlock="lem:topological-mass-transient-localisation". |
| `lem:tower-pair-equality-fixed-level` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:tower-pair-equality-fixed-level at q0; emit witness with contentBlock="lem:tower-pair-equality-fixed-level". |
| `lem:vhat-pair-commutation-trace` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:vhat-pair-commutation-trace at q0; emit witness with contentBlock="lem:vhat-pair-commutation-trace". |
| `lem:volume-from-rigidity` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:volume-from-rigidity at q0; emit witness with contentBlock="lem:volume-from-rigidity". |
| `lem:yekutieli-leading-coefficient` | lemma | NOT-WIRED | I1 | Write probe_*.py exercising lem:yekutieli-leading-coefficient at q0; emit witness with contentBlock="lem:yekutieli-leading-coefficient". |
| `prop:acoustic-horizon-conditions` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:algebraic-filter-classification` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:algebraic-filter-classification at q0; emit witness with contentBlock="prop:algebraic-filter-classification". |
| `prop:algebraic-gns-embedding` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:algebraic-gns-embedding at q0; emit witness with contentBlock="prop:algebraic-gns-embedding". |
| `prop:algebraic-volume-specialization` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:algebraic-volume-specialization at q0; emit witness with contentBlock="prop:algebraic-volume-specialization". |
| `prop:alpha-em-categorical-trace-ratio` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:alpha-em-categorical-trace-ratio at q0; emit witness with contentBlock="prop:alpha-em-categorical-trace-ratio". |
| `prop:alpha-k-derivation-procedure` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:alpha-k-derivation-procedure at q0; emit witness with contentBlock="prop:alpha-k-derivation-procedure". |
| `prop:antiparticle-crossing-reversal` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:antiparticle-crossing-reversal at q0; emit witness with contentBlock="prop:antiparticle-crossing-reversal". |
| `prop:archimedean-functor-uniqueness` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:archimedean-functor-uniqueness at q0; emit witness with contentBlock="prop:archimedean-functor-uniqueness". |
| `prop:archimedean-hartree-derivation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:archimedean-hartree-derivation at q0; emit witness with contentBlock="prop:archimedean-hartree-derivation". |
| `prop:atom-knot-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:atom-knot-exists at q0; emit witness with contentBlock="prop:atom-knot-exists". |
| `prop:atom-knot-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:atom-knot-unique at q0; emit witness with contentBlock="prop:atom-knot-unique". |
| `prop:atomic-lp-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:atomic-lp-stability at q0; emit witness with contentBlock="prop:atomic-lp-stability". |
| `prop:atomic-nf-witness` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:atomic-nf-witness at q0; emit witness with contentBlock="prop:atomic-nf-witness". |
| `prop:b1-figure-8-row-theorem` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:b1-figure-8-row-theorem at q0; emit witness with contentBlock="prop:b1-figure-8-row-theorem". |
| `prop:b1-hyperbolic-rows-theorem` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:b1-hyperbolic-rows-theorem at q0; emit witness with contentBlock="prop:b1-hyperbolic-rows-theorem". |
| `prop:b1-soft-sharpness-theorem` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:b1-soft-sharpness-theorem at q0; emit witness with contentBlock="prop:b1-soft-sharpness-theorem". |
| `prop:b1-torus-knot-rows-theorem` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:b1-torus-knot-rows-theorem at q0; emit witness with contentBlock="prop:b1-torus-knot-rows-theorem". |
| `prop:bar-apply-transfer` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:bar-apply-transfer at q0; emit witness with contentBlock="prop:bar-apply-transfer". |
| `prop:bar-involution-invariance` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:bar-involution-invariance at q0; emit witness with contentBlock="prop:bar-involution-invariance". |
| `prop:bar-self-dual-confinement-band` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:bar-self-dual-confinement-band at q0; emit witness with contentBlock="prop:bar-self-dual-confinement-band". |
| `prop:bar-t-duality-substrate` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:bar-t-duality-substrate at q0; emit witness with contentBlock="prop:bar-t-duality-substrate". |
| `prop:benzene-threading-emergence` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:beta-decay-transfer-matrix` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:beta-decay-transfer-matrix at q0; emit witness with contentBlock="prop:beta-decay-transfer-matrix". |
| `prop:beta-decay-transfer-matrix` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:beta-decay-transfer-matrix at q0; emit witness with contentBlock="prop:beta-decay-transfer-matrix". |
| `prop:beta-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:beta-stability at q0; emit witness with contentBlock="prop:beta-stability". |
| `prop:binding-scale-catalan` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:binding-scale-catalan at q0; emit witness with contentBlock="prop:binding-scale-catalan". |
| `prop:bloch-group-quotient-construction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:bloch-group-quotient-construction at q0; emit witness with contentBlock="prop:bloch-group-quotient-construction". |
| `prop:bn-mtc-action` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:bohr-radius-categorical` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:bohr-radius-categorical at q0; emit witness with contentBlock="prop:bohr-radius-categorical". |
| `prop:boltzmann-constant` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:boltzmann-constant at q0; emit witness with contentBlock="prop:boltzmann-constant". |
| `prop:borel-partial-resolution` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:borel-partial-resolution at q0; emit witness with contentBlock="prop:borel-partial-resolution". |
| `prop:borromean-hopf-energy-crossover` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:borromean-hopf-energy-crossover at q0; emit witness with contentBlock="prop:borromean-hopf-energy-crossover". |
| `prop:box-braid-irreducibility` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:box-braid-irreducibility at q0; emit witness with contentBlock="prop:box-braid-irreducibility". |
| `prop:box-braid-irreducibility` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:box-braid-irreducibility at q0; emit witness with contentBlock="prop:box-braid-irreducibility". |
| `prop:braid-action-tensor` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:braid-action-tensor at q0; emit witness with contentBlock="prop:braid-action-tensor". |
| `prop:braiding-eigenvalue-extraction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:braiding-eigenvalue-extraction at q0; emit witness with contentBlock="prop:braiding-eigenvalue-extraction". |
| `prop:braiding-induced-ordering` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:braiding-induced-ordering at q0; emit witness with contentBlock="prop:braiding-induced-ordering". |
| `prop:branching-qvalue-factorization` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:branching-qvalue-factorization at q0; emit witness with contentBlock="prop:branching-qvalue-factorization". |
| `prop:brane-boundary` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:brane-boundary at q0; emit witness with contentBlock="prop:brane-boundary". |
| `prop:brane-tower-q-laplacian-decay` | proposition | NOT-WIRED | I1-pre | Block has no .lean sibling and no probe; if substantive, author Lean + probe; otherwise mark as derivative. |
| `prop:bring-trilog-imaginary-tate-rational` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:bring-trilog-imaginary-tate-rational at q0; emit witness with contentBlock="prop:bring-trilog-imaginary-tate-rational". |
| `prop:brings-is-qou` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:brings-is-qou at q0; emit witness with contentBlock="prop:brings-is-qou". |
| `prop:brings-smoothness-resolution` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:brings-smoothness-resolution at q0; emit witness with contentBlock="prop:brings-smoothness-resolution". |
| `prop:categorical-action-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-action-exists at q0; emit witness with contentBlock="prop:categorical-action-exists". |
| `prop:categorical-action-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-action-unique at q0; emit witness with contentBlock="prop:categorical-action-unique". |
| `prop:categorical-archimedean-bridge` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-archimedean-bridge at q0; emit witness with contentBlock="prop:categorical-archimedean-bridge". |
| `prop:categorical-chain-convergence-mechanisms` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-chain-convergence-mechanisms at q0; emit witness with contentBlock="prop:categorical-chain-convergence-mechanisms". |
| `prop:categorical-connection-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-connection-exists at q0; emit witness with contentBlock="prop:categorical-connection-exists". |
| `prop:categorical-connection-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-connection-unique at q0; emit witness with contentBlock="prop:categorical-connection-unique". |
| `prop:categorical-coordinate-ring` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-coordinate-ring at q0; emit witness with contentBlock="prop:categorical-coordinate-ring". |
| `prop:categorical-dirac-operator-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-dirac-operator-exists at q0; emit witness with contentBlock="prop:categorical-dirac-operator-exists". |
| `prop:categorical-dirac-operator-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-dirac-operator-unique at q0; emit witness with contentBlock="prop:categorical-dirac-operator-unique". |
| `prop:categorical-dq-squared` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-dq-squared at q0; emit witness with contentBlock="prop:categorical-dq-squared". |
| `prop:categorical-fourier-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-fourier-exists at q0; emit witness with contentBlock="prop:categorical-fourier-exists". |
| `prop:categorical-fourier-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-fourier-unique at q0; emit witness with contentBlock="prop:categorical-fourier-unique". |
| `prop:categorical-hodge-star-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-hodge-star-exists at q0; emit witness with contentBlock="prop:categorical-hodge-star-exists". |
| `prop:categorical-hodge-star-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-hodge-star-unique at q0; emit witness with contentBlock="prop:categorical-hodge-star-unique". |
| `prop:categorical-instanton-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-instanton-exists at q0; emit witness with contentBlock="prop:categorical-instanton-exists". |
| `prop:categorical-instanton-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-instanton-unique at q0; emit witness with contentBlock="prop:categorical-instanton-unique". |
| `prop:categorical-jet-prolongation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-jet-prolongation at q0; emit witness with contentBlock="prop:categorical-jet-prolongation". |
| `prop:categorical-lagrangian-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-lagrangian-exists at q0; emit witness with contentBlock="prop:categorical-lagrangian-exists". |
| `prop:categorical-lagrangian-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-lagrangian-unique at q0; emit witness with contentBlock="prop:categorical-lagrangian-unique". |
| `prop:categorical-laplace-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-laplace-exists at q0; emit witness with contentBlock="prop:categorical-laplace-exists". |
| `prop:categorical-laplace-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-laplace-unique at q0; emit witness with contentBlock="prop:categorical-laplace-unique". |
| `prop:categorical-mass-markov` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-mass-markov at q0; emit witness with contentBlock="prop:categorical-mass-markov". |
| `prop:categorical-neutron-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-neutron-exists at q0; emit witness with contentBlock="prop:categorical-neutron-exists". |
| `prop:categorical-neutron-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-neutron-unique at q0; emit witness with contentBlock="prop:categorical-neutron-unique". |
| `prop:categorical-proton-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-proton-exists at q0; emit witness with contentBlock="prop:categorical-proton-exists". |
| `prop:categorical-proton-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-proton-unique at q0; emit witness with contentBlock="prop:categorical-proton-unique". |
| `prop:categorical-q-connection-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-q-connection-exists at q0; emit witness with contentBlock="prop:categorical-q-connection-exists". |
| `prop:categorical-q-connection-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-q-connection-unique at q0; emit witness with contentBlock="prop:categorical-q-connection-unique". |
| `prop:categorical-q-ext-deriv-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-q-ext-deriv-exists at q0; emit witness with contentBlock="prop:categorical-q-ext-deriv-exists". |
| `prop:categorical-q-ext-deriv-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-q-ext-deriv-unique at q0; emit witness with contentBlock="prop:categorical-q-ext-deriv-unique". |
| `prop:categorical-reeb-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-reeb-unique at q0; emit witness with contentBlock="prop:categorical-reeb-unique". |
| `prop:categorical-self-duality` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:categorical-self-duality at q0; emit witness with contentBlock="prop:categorical-self-duality". |
| `prop:centered-hecke-variance-positive` | proposition | NOT-WIRED | I1-pre | Block has no .lean sibling and no probe; if substantive, author Lean + probe; otherwise mark as derivative. |
| `prop:ch4-lp-dual-binding` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:chain-ring-comparison` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:chain-ring-comparison at q0; emit witness with contentBlock="prop:chain-ring-comparison". |
| `prop:chirality-from-frobenius-self-pairing` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:chirality-from-frobenius-self-pairing at q0; emit witness with contentBlock="prop:chirality-from-frobenius-self-pairing". |
| `prop:chirality-residue-mass-term` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:chirality-residue-mass-term at q0; emit witness with contentBlock="prop:chirality-residue-mass-term". |
| `prop:cl2-pentagon-and-faddeev-partial` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cl2-pentagon-and-faddeev-partial at q0; emit witness with contentBlock="prop:cl2-pentagon-and-faddeev-partial". |
| `prop:cl3-zeta5-orbit-sum-identity` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cl3-zeta5-orbit-sum-identity at q0; emit witness with contentBlock="prop:cl3-zeta5-orbit-sum-identity". |
| `prop:cl3-zeta5-pslq-independence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cl3-zeta5-pslq-independence at q0; emit witness with contentBlock="prop:cl3-zeta5-pslq-independence". |
| `prop:co-lp-dual-binding` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:co2-lp-dual-binding` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:cohomological-embedding` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cohomological-embedding at q0; emit witness with contentBlock="prop:cohomological-embedding". |
| `prop:collatz-contact-boundary` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:collatz-contact-boundary at q0; emit witness with contentBlock="prop:collatz-contact-boundary". |
| `prop:collatz-no-cycles` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:collatz-no-cycles at q0; emit witness with contentBlock="prop:collatz-no-cycles". |
| `prop:composite-crossing-parity` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:composite-crossing-parity at q0; emit witness with contentBlock="prop:composite-crossing-parity". |
| `prop:compound-beta-shell-calibration` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:compound-beta-shell-calibration at q0; emit witness with contentBlock="prop:compound-beta-shell-calibration". |
| `prop:confinement-categorical` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-categorical at q0; emit witness with contentBlock="prop:confinement-categorical". |
| `prop:confinement-level-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-level-exists at q0; emit witness with contentBlock="prop:confinement-level-exists". |
| `prop:confinement-level-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-level-unique at q0; emit witness with contentBlock="prop:confinement-level-unique". |
| `prop:confinement-lp` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-lp at q0; emit witness with contentBlock="prop:confinement-lp". |
| `prop:confinement-operator-selection` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-operator-selection at q0; emit witness with contentBlock="prop:confinement-operator-selection". |
| `prop:confinement-phase-stratification` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-phase-stratification at q0; emit witness with contentBlock="prop:confinement-phase-stratification". |
| `prop:confinement-sdp` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-sdp at q0; emit witness with contentBlock="prop:confinement-sdp". |
| `prop:confinement-topological` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-topological at q0; emit witness with contentBlock="prop:confinement-topological". |
| `prop:confinement-universality` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:confinement-universality at q0; emit witness with contentBlock="prop:confinement-universality". |
| `prop:content-scaling-correspondence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:content-scaling-correspondence at q0; emit witness with contentBlock="prop:content-scaling-correspondence". |
| `prop:coral-elliptic` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:coral-elliptic at q0; emit witness with contentBlock="prop:coral-elliptic". |
| `prop:core-levi-form` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:corrected-markov-trace` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:corrected-markov-trace at q0; emit witness with contentBlock="prop:corrected-markov-trace". |
| `prop:cosimplicial-crossed-groupoid` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cosimplicial-crossed-groupoid at q0; emit witness with contentBlock="prop:cosimplicial-crossed-groupoid". |
| `prop:cpt-orbit-closure-density` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cpt-orbit-closure-density at q0; emit witness with contentBlock="prop:cpt-orbit-closure-density". |
| `prop:crossing-energy-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:crossing-energy-decomposition at q0; emit witness with contentBlock="prop:crossing-energy-decomposition". |
| `prop:crystal-basis-resolves-mass-tower-open-problems` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:crystal-basis-resolves-mass-tower-open-problems at q0; emit witness with contentBlock="prop:crystal-basis-resolves-mass-tower-open-problems". |
| `prop:crystal-isospin-degeneracy` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:crystal-isospin-degeneracy at q0; emit witness with contentBlock="prop:crystal-isospin-degeneracy". |
| `prop:crystal-r-matrix-sub-lemma` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:crystal-r-matrix-sub-lemma at q0; emit witness with contentBlock="prop:crystal-r-matrix-sub-lemma". |
| `prop:cs-evaluation-faithfulness` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cs-evaluation-faithfulness at q0; emit witness with contentBlock="prop:cs-evaluation-faithfulness". |
| `prop:curvature-rank-gb-stratification` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:curvature-rank-gb-stratification at q0; emit witness with contentBlock="prop:curvature-rank-gb-stratification". |
| `prop:cyclotomic-cl3-orbit-sum-general` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cyclotomic-cl3-orbit-sum-general at q0; emit witness with contentBlock="prop:cyclotomic-cl3-orbit-sum-general". |
| `prop:cyclotomic-depth3-dimension-synthesis` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cyclotomic-depth3-dimension-synthesis at q0; emit witness with contentBlock="prop:cyclotomic-depth3-dimension-synthesis". |
| `prop:cyclotomic-dimension-synthesis-all-depths` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cyclotomic-dimension-synthesis-all-depths at q0; emit witness with contentBlock="prop:cyclotomic-dimension-synthesis-all-depths". |
| `prop:cyclotomic-l-value-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cyclotomic-l-value-decomposition at q0; emit witness with contentBlock="prop:cyclotomic-l-value-decomposition". |
| `prop:cyclotomic-orbit-sum-all-depths` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cyclotomic-orbit-sum-all-depths at q0; emit witness with contentBlock="prop:cyclotomic-orbit-sum-all-depths". |
| `prop:cyclotomic-trilog-imaginary-closed-form` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:cyclotomic-trilog-imaginary-closed-form at q0; emit witness with contentBlock="prop:cyclotomic-trilog-imaginary-closed-form". |
| `prop:defect-legendrian-knot` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:defect-legendrian-knot at q0; emit witness with contentBlock="prop:defect-legendrian-knot". |
| `prop:degree-two-baryon-weight` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:degree-two-baryon-weight at q0; emit witness with contentBlock="prop:degree-two-baryon-weight". |
| `prop:delta-max-uniform-bound` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:delta-max-uniform-bound at q0; emit witness with contentBlock="prop:delta-max-uniform-bound". |
| `prop:demand-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:demand-stability at q0; emit witness with contentBlock="prop:demand-stability". |
| `prop:depth-2-identification-bloch-suslin` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:depth-2-identification-bloch-suslin at q0; emit witness with contentBlock="prop:depth-2-identification-bloch-suslin". |
| `prop:derived-mass-formula-light-isotopes` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:derived-mass-formula-light-isotopes at q0; emit witness with contentBlock="prop:derived-mass-formula-light-isotopes". |
| `prop:descartes-elliptic-curve` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:descartes-elliptic-curve at q0; emit witness with contentBlock="prop:descartes-elliptic-curve". |
| `prop:descended-level-zero` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:descended-level-zero at q0; emit witness with contentBlock="prop:descended-level-zero". |
| `prop:descent-condition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:descent-condition at q0; emit witness with contentBlock="prop:descent-condition". |
| `prop:descent-eigenspaces` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:descent-eigenspaces at q0; emit witness with contentBlock="prop:descent-eigenspaces". |
| `prop:deuterium-derived-binding` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:deuterium-derived-binding at q0; emit witness with contentBlock="prop:deuterium-derived-binding". |
| `prop:deuteron-binding-frobenius-codim` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:deuteron-binding-frobenius-codim at q0; emit witness with contentBlock="prop:deuteron-binding-frobenius-codim". |
| `prop:discrete-vortex-spectrum` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:double-slit-massive-pattern` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:double-slit-massive-pattern at q0; emit witness with contentBlock="prop:double-slit-massive-pattern". |
| `prop:dq-squared` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:dq-squared at q0; emit witness with contentBlock="prop:dq-squared". |
| `prop:e-infinity-page-identifications` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:e-infinity-page-identifications at q0; emit witness with contentBlock="prop:e-infinity-page-identifications". |
| `prop:eigenvalue-product-expansion` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:eigenvalue-product-expansion at q0; emit witness with contentBlock="prop:eigenvalue-product-expansion". |
| `prop:em-coupling-bring-zero-mode` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:em-coupling-bring-zero-mode at q0; emit witness with contentBlock="prop:em-coupling-bring-zero-mode". |
| `prop:em-coupling-projection` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:em-coupling-projection at q0; emit witness with contentBlock="prop:em-coupling-projection". |
| `prop:emergence-to-quantum-flat` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:emergence-to-quantum-flat at q0; emit witness with contentBlock="prop:emergence-to-quantum-flat". |
| `prop:eos-borromean-cfl` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:eos-borromean-cfl at q0; emit witness with contentBlock="prop:eos-borromean-cfl". |
| `prop:euler-char-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:euler-char-stability at q0; emit witness with contentBlock="prop:euler-char-stability". |
| `prop:explicit-alpha-k-h3` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:explicit-alpha-k-h3 at q0; emit witness with contentBlock="prop:explicit-alpha-k-h3". |
| `prop:explicit-alpha-k-h4` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:explicit-alpha-k-h4 at q0; emit witness with contentBlock="prop:explicit-alpha-k-h4". |
| `prop:explicit-central-idempotent` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:explicit-central-idempotent at q0; emit witness with contentBlock="prop:explicit-central-idempotent". |
| `prop:exterior-square-borromean` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:exterior-square-borromean at q0; emit witness with contentBlock="prop:exterior-square-borromean". |
| `prop:fermion-boson-knot-link` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:fermion-boson-knot-link at q0; emit witness with contentBlock="prop:fermion-boson-knot-link". |
| `prop:feynman-categorical-trace` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:feynman-categorical-trace at q0; emit witness with contentBlock="prop:feynman-categorical-trace". |
| `prop:feynman-classical-limit` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:feynman-classical-limit at q0; emit witness with contentBlock="prop:feynman-classical-limit". |
| `prop:fiber-adjoint-involution` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:fiber-adjoint-involution at q0; emit witness with contentBlock="prop:fiber-adjoint-involution". |
| `prop:fibre-functor-atlas` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:fibre-functor-atlas at q0; emit witness with contentBlock="prop:fibre-functor-atlas". |
| `prop:figure-eight-branching-rule` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:figure-eight-branching-rule at q0; emit witness with contentBlock="prop:figure-eight-branching-rule". |
| `prop:flavor-split-substrate` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:flavor-split-substrate at q0; emit witness with contentBlock="prop:flavor-split-substrate". |
| `prop:force-carrier-bring-uniqueness` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:force-carrier-bring-uniqueness at q0; emit witness with contentBlock="prop:force-carrier-bring-uniqueness". |
| `prop:force-carrier-intertwining-correspondence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:force-carrier-intertwining-correspondence at q0; emit witness with contentBlock="prop:force-carrier-intertwining-correspondence". |
| `prop:four-term-pair-nucleon` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:four-term-pair-nucleon at q0; emit witness with contentBlock="prop:four-term-pair-nucleon". |
| `prop:frobenius-gram-matrix` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:frobenius-gram-matrix at q0; emit witness with contentBlock="prop:frobenius-gram-matrix". |
| `prop:frobenius-pairing-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:frobenius-pairing-exists at q0; emit witness with contentBlock="prop:frobenius-pairing-exists". |
| `prop:frobenius-pairing-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:frobenius-pairing-unique at q0; emit witness with contentBlock="prop:frobenius-pairing-unique". |
| `prop:frobenius-positivity-filter` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:frobenius-positivity-filter at q0; emit witness with contentBlock="prop:frobenius-positivity-filter". |
| `prop:frobenius-relation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:frobenius-relation at q0; emit witness with contentBlock="prop:frobenius-relation". |
| `prop:frobenius-s-classification` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:frobenius-s-classification at q0; emit witness with contentBlock="prop:frobenius-s-classification". |
| `prop:frobenius-self-duality-forces-lp-dual-extraction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:frobenius-self-duality-forces-lp-dual-extraction at q0; emit witness with contentBlock="prop:frobenius-self-duality-forces-lp-dual-extraction". |
| `prop:gb-residue-spectral-sum` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:gb-residue-spectral-sum at q0; emit witness with contentBlock="prop:gb-residue-spectral-sum". |
| `prop:gb-spectral-sequence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:gb-spectral-sequence at q0; emit witness with contentBlock="prop:gb-spectral-sequence". |
| `prop:generator-volume-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:generator-volume-decomposition at q0; emit witness with contentBlock="prop:generator-volume-decomposition". |
| `prop:generator-volume-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:generator-volume-decomposition at q0; emit witness with contentBlock="prop:generator-volume-decomposition". |
| `prop:genus-filtration-ideal` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:genus-filtration-ideal at q0; emit witness with contentBlock="prop:genus-filtration-ideal". |
| `prop:genus-maximal-descent` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:genus-maximal-descent at q0; emit witness with contentBlock="prop:genus-maximal-descent". |
| `prop:geom-universality` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:geom-universality at q0; emit witness with contentBlock="prop:geom-universality". |
| `prop:geom-yekutieli-alignment` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:geom-yekutieli-alignment at q0; emit witness with contentBlock="prop:geom-yekutieli-alignment". |
| `prop:global-gluing` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:global-gluing at q0; emit witness with contentBlock="prop:global-gluing". |
| `prop:golden-quartet-galois` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:golden-quartet-galois at q0; emit witness with contentBlock="prop:golden-quartet-galois". |
| `prop:golden-skew-dual-node` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:golden-skew-dual-node at q0; emit witness with contentBlock="prop:golden-skew-dual-node". |
| `prop:graded-markov-trace-from-gs-filtration` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:graded-markov-trace-from-gs-filtration at q0; emit witness with contentBlock="prop:graded-markov-trace-from-gs-filtration". |
| `prop:graded-trace-residue-split` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:graded-trace-residue-split at q0; emit witness with contentBlock="prop:graded-trace-residue-split". |
| `prop:gram-determinant-plancherel-ratio` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:gram-determinant-plancherel-ratio at q0; emit witness with contentBlock="prop:gram-determinant-plancherel-ratio". |
| `prop:gram-weighted-qvalue` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:gram-weighted-qvalue at q0; emit witness with contentBlock="prop:gram-weighted-qvalue". |
| `prop:gravity-spectral-prefactor` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:gravity-spectral-prefactor at q0; emit witness with contentBlock="prop:gravity-spectral-prefactor". |
| `prop:ground-state-ordering` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:ground-state-ordering at q0; emit witness with contentBlock="prop:ground-state-ordering". |
| `prop:habiro-residue-sum-equivalence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:habiro-residue-sum-equivalence at q0; emit witness with contentBlock="prop:habiro-residue-sum-equivalence". |
| `prop:hadron-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hadron-exists at q0; emit witness with contentBlock="prop:hadron-exists". |
| `prop:hadron-half-life` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hadron-half-life at q0; emit witness with contentBlock="prop:hadron-half-life". |
| `prop:hadron-operations-closure` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hadron-operations-closure at q0; emit witness with contentBlock="prop:hadron-operations-closure". |
| `prop:hadron-q-self-correction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hadron-q-self-correction at q0; emit witness with contentBlock="prop:hadron-q-self-correction". |
| `prop:hadron-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hadron-unique at q0; emit witness with contentBlock="prop:hadron-unique". |
| `prop:he4-channel-active-set` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:he4-channel-active-set at q0; emit witness with contentBlock="prop:he4-channel-active-set". |
| `prop:he4-two-row-dominance` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:he4-two-row-dominance at q0; emit witness with contentBlock="prop:he4-two-row-dominance". |
| `prop:hecke-1d-irrep-closed-form-character` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hecke-1d-irrep-closed-form-character at q0; emit witness with contentBlock="prop:hecke-1d-irrep-closed-form-character". |
| `prop:hecke-baer-star-generic` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hecke-baer-star-generic at q0; emit witness with contentBlock="prop:hecke-baer-star-generic". |
| `prop:hecke-branching-trace-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hecke-branching-trace-decomposition at q0; emit witness with contentBlock="prop:hecke-branching-trace-decomposition". |
| `prop:hecke-convergence-bound` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hecke-convergence-bound at q0; emit witness with contentBlock="prop:hecke-convergence-bound". |
| `prop:hecke-log-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hecke-log-decomposition at q0; emit witness with contentBlock="prop:hecke-log-decomposition". |
| `prop:hecke-markov-transition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hecke-markov-transition at q0; emit witness with contentBlock="prop:hecke-markov-transition". |
| `prop:hecke-mass-trace` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hecke-mass-trace at q0; emit witness with contentBlock="prop:hecke-mass-trace". |
| `prop:hecke-satisfies-blitvic-hypothesis` | proposition | NOT-WIRED | I1-pre | Block has no .lean sibling and no probe; if substantive, author Lean + probe; otherwise mark as derivative. |
| `prop:heisenberg-commutator` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:heisenberg-commutator at q0; emit witness with contentBlock="prop:heisenberg-commutator". |
| `prop:helicity-conservation` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:hoefsmit-V21-cos-symmetrization` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hoefsmit-V21-cos-symmetrization at q0; emit witness with contentBlock="prop:hoefsmit-V21-cos-symmetrization". |
| `prop:hoefsmit-is-surreal-construction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hoefsmit-is-surreal-construction at q0; emit witness with contentBlock="prop:hoefsmit-is-surreal-construction". |
| `prop:hoefsmit-scattering-pipeline` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hoefsmit-scattering-pipeline at q0; emit witness with contentBlock="prop:hoefsmit-scattering-pipeline". |
| `prop:hoefsmit-seminormal-form` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hoefsmit-seminormal-form at q0; emit witness with contentBlock="prop:hoefsmit-seminormal-form". |
| `prop:hook-weight-derivation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hook-weight-derivation at q0; emit witness with contentBlock="prop:hook-weight-derivation". |
| `prop:horizon-conformal-invariance` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:horizon-conformal-invariance at q0; emit witness with contentBlock="prop:horizon-conformal-invariance". |
| `prop:hydrogen-shell-writhe` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:hydrogen-shell-writhe at q0; emit witness with contentBlock="prop:hydrogen-shell-writhe". |
| `prop:ilp-covalent-bond` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:incompleteness-implies-horizon` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:incompleteness-implies-horizon at q0; emit witness with contentBlock="prop:incompleteness-implies-horizon". |
| `prop:inductive-gb-reduction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:inductive-gb-reduction at q0; emit witness with contentBlock="prop:inductive-gb-reduction". |
| `prop:integer-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:integer-stability at q0; emit witness with contentBlock="prop:integer-stability". |
| `prop:isotope-knot-equivalence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:isotope-knot-equivalence at q0; emit witness with contentBlock="prop:isotope-knot-equivalence". |
| `prop:jet-prefix-gb-filtration` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:jet-prefix-gb-filtration at q0; emit witness with contentBlock="prop:jet-prefix-gb-filtration". |
| `prop:jet-prolongation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:jet-prolongation at q0; emit witness with contentBlock="prop:jet-prolongation". |
| `prop:jet-tower-convergence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:jet-tower-convergence at q0; emit witness with contentBlock="prop:jet-tower-convergence". |
| `prop:joint-galois-braid-discharged` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:joint-galois-braid-discharged at q0; emit witness with contentBlock="prop:joint-galois-braid-discharged". |
| `prop:joint-galois-braid-figure-8-verified` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:joint-galois-braid-figure-8-verified at q0; emit witness with contentBlock="prop:joint-galois-braid-figure-8-verified". |
| `prop:jonquiere-cyclotomic-tate-rationality` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:jonquiere-cyclotomic-tate-rationality at q0; emit witness with contentBlock="prop:jonquiere-cyclotomic-tate-rationality". |
| `prop:jucys-murphy-central-elements-qou` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:jucys-murphy-central-elements-qou at q0; emit witness with contentBlock="prop:jucys-murphy-central-elements-qou". |
| `prop:kelvin-dispersion-derivation` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:knot-eigenbasis-complete` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:knot-eigenbasis-complete at q0; emit witness with contentBlock="prop:knot-eigenbasis-complete". |
| `prop:knot-factor-spectral-form` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:knot-factor-spectral-form at q0; emit witness with contentBlock="prop:knot-factor-spectral-form". |
| `prop:knot-indexed-convolution-grid` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:knot-indexed-convolution-grid at q0; emit witness with contentBlock="prop:knot-indexed-convolution-grid". |
| `prop:knot-operator-energy-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:knot-operator-energy-exists at q0; emit witness with contentBlock="prop:knot-operator-energy-exists". |
| `prop:knot-operator-energy-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:knot-operator-energy-unique at q0; emit witness with contentBlock="prop:knot-operator-energy-unique". |
| `prop:knot-operator-selection` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:knot-operator-selection at q0; emit witness with contentBlock="prop:knot-operator-selection". |
| `prop:knot-operator-transition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:knot-operator-transition at q0; emit witness with contentBlock="prop:knot-operator-transition". |
| `prop:knot-particle-correspondence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:knot-particle-correspondence at q0; emit witness with contentBlock="prop:knot-particle-correspondence". |
| `prop:lagrange-resolvent-transform` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:lagrange-resolvent-transform at q0; emit witness with contentBlock="prop:lagrange-resolvent-transform". |
| `prop:lepton-continuant-recurrence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:lepton-continuant-recurrence at q0; emit witness with contentBlock="prop:lepton-continuant-recurrence". |
| `prop:leray-profile` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:level-sufficiency` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:level-sufficiency at q0; emit witness with contentBlock="prop:level-sufficiency". |
| `prop:local-substrate-q` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:local-substrate-q at q0; emit witness with contentBlock="prop:local-substrate-q". |
| `prop:lp-dual-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:lp-dual-stability at q0; emit witness with contentBlock="prop:lp-dual-stability". |
| `prop:magic-numbers-from-q` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:magic-numbers-from-q at q0; emit witness with contentBlock="prop:magic-numbers-from-q". |
| `prop:magic-shell-coupling-kappa` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:magic-shell-coupling-kappa at q0; emit witness with contentBlock="prop:magic-shell-coupling-kappa". |
| `prop:main-commutative-diagram` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:main-commutative-diagram at q0; emit witness with contentBlock="prop:main-commutative-diagram". |
| `prop:markov-trace-antipode-polynomial-symmetry` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:markov-trace-antipode-polynomial-symmetry at q0; emit witness with contentBlock="prop:markov-trace-antipode-polynomial-symmetry". |
| `prop:markov-trace-frobenius-selection` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:markov-trace-frobenius-selection at q0; emit witness with contentBlock="prop:markov-trace-frobenius-selection". |
| `prop:markov-trace-recursive-reducer` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:markov-trace-recursive-reducer at q0; emit witness with contentBlock="prop:markov-trace-recursive-reducer". |
| `prop:mass-categorical-descent` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:mass-categorical-descent at q0; emit witness with contentBlock="prop:mass-categorical-descent". |
| `prop:mass-formula-regime-switching` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:mass-formula-regime-switching at q0; emit witness with contentBlock="prop:mass-formula-regime-switching". |
| `prop:mass-identity-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:mass-identity-exists at q0; emit witness with contentBlock="prop:mass-identity-exists". |
| `prop:mass-identity-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:mass-identity-unique at q0; emit witness with contentBlock="prop:mass-identity-unique". |
| `prop:mass-tower-coefficient-stratification` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:mass-tower-coefficient-stratification at q0; emit witness with contentBlock="prop:mass-tower-coefficient-stratification". |
| `prop:metallic-character-knot` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:metallic-character-knot at q0; emit witness with contentBlock="prop:metallic-character-knot". |
| `prop:mi-sw-abelianisation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:mi-sw-abelianisation at q0; emit witness with contentBlock="prop:mi-sw-abelianisation". |
| `prop:mobius-energy` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:mobius-energy at q0; emit witness with contentBlock="prop:mobius-energy". |
| `prop:mobius-golden-fixed-points` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:mobius-golden-fixed-points at q0; emit witness with contentBlock="prop:mobius-golden-fixed-points". |
| `prop:moduli-symmetry-d4` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:moduli-symmetry-d4 at q0; emit witness with contentBlock="prop:moduli-symmetry-d4". |
| `prop:n-equals-1-vacuous-magic` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:n-equals-1-vacuous-magic at q0; emit witness with contentBlock="prop:n-equals-1-vacuous-magic". |
| `prop:neutron-prediction-comparison` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:neutron-prediction-comparison at q0; emit witness with contentBlock="prop:neutron-prediction-comparison". |
| `prop:neutron-proton-mass-splitting` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:neutron-proton-mass-splitting at q0; emit witness with contentBlock="prop:neutron-proton-mass-splitting". |
| `prop:neutron-proton-splitting` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:neutron-proton-splitting at q0; emit witness with contentBlock="prop:neutron-proton-splitting". |
| `prop:noble-gas-characterization` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:noble-gas-characterization at q0; emit witness with contentBlock="prop:noble-gas-characterization". |
| `prop:ns-kummer-specialisation` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:ns-obstruction-computation` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:ns-obstruction-tower` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:nuclear-groebner-reduction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:nuclear-groebner-reduction at q0; emit witness with contentBlock="prop:nuclear-groebner-reduction". |
| `prop:nuclear-groebner-reduction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:nuclear-groebner-reduction at q0; emit witness with contentBlock="prop:nuclear-groebner-reduction". |
| `prop:nuclear-knot-classification` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:nuclear-knot-classification at q0; emit witness with contentBlock="prop:nuclear-knot-classification". |
| `prop:nuclear-operator-regimes` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:nuclear-operator-regimes at q0; emit witness with contentBlock="prop:nuclear-operator-regimes". |
| `prop:nuclear-spin-parity` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:nuclear-spin-parity at q0; emit witness with contentBlock="prop:nuclear-spin-parity". |
| `prop:nucleon-ordering-factorization` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:nucleon-ordering-factorization at q0; emit witness with contentBlock="prop:nucleon-ordering-factorization". |
| `prop:observation-energy` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:observation-energy at q0; emit witness with contentBlock="prop:observation-energy". |
| `prop:orbital-fourier-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:orbital-fourier-decomposition at q0; emit witness with contentBlock="prop:orbital-fourier-decomposition". |
| `prop:orbital-space-normal-bundle` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:orbital-space-normal-bundle at q0; emit witness with contentBlock="prop:orbital-space-normal-bundle". |
| `prop:ordering-jet-compatibility` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:ordering-jet-compatibility at q0; emit witness with contentBlock="prop:ordering-jet-compatibility". |
| `prop:p-bandwidth-bound` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:p-bandwidth-bound at q0; emit witness with contentBlock="prop:p-bandwidth-bound". |
| `prop:parity-violation-skein` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:parity-violation-skein at q0; emit witness with contentBlock="prop:parity-violation-skein". |
| `prop:partition-sum-proton-residual` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:partition-sum-proton-residual at q0; emit witness with contentBlock="prop:partition-sum-proton-residual". |
| `prop:pauli-factor-wedderburn` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:pauli-factor-wedderburn at q0; emit witness with contentBlock="prop:pauli-factor-wedderburn". |
| `prop:pawlowski-leitner-basis` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:pawlowski-leitner-basis at q0; emit witness with contentBlock="prop:pawlowski-leitner-basis". |
| `prop:pawlowski-leitner-inner-product` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:pawlowski-leitner-inner-product at q0; emit witness with contentBlock="prop:pawlowski-leitner-inner-product". |
| `prop:pentagon-uv-commutation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:pentagon-uv-commutation at q0; emit witness with contentBlock="prop:pentagon-uv-commutation". |
| `prop:per-braid-mass-tower` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:per-braid-mass-tower at q0; emit witness with contentBlock="prop:per-braid-mass-tower". |
| `prop:phase-transition-boundary` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:phase-transition-boundary at q0; emit witness with contentBlock="prop:phase-transition-boundary". |
| `prop:phi-q-tower-algebraic-stratification` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:phi-q-tower-algebraic-stratification at q0; emit witness with contentBlock="prop:phi-q-tower-algebraic-stratification". |
| `prop:photon-threading-mass` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:photon-threading-mass at q0; emit witness with contentBlock="prop:photon-threading-mass". |
| `prop:pieri-photon-shift` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:pieri-photon-shift at q0; emit witness with contentBlock="prop:pieri-photon-shift". |
| `prop:plancherel-term-7-formulation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:plancherel-term-7-formulation at q0; emit witness with contentBlock="prop:plancherel-term-7-formulation". |
| `prop:plancherel-weight-boundedness` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:plancherel-weight-boundedness at q0; emit witness with contentBlock="prop:plancherel-weight-boundedness". |
| `prop:positive-definite-dagger` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:positive-definite-dagger at q0; emit witness with contentBlock="prop:positive-definite-dagger". |
| `prop:positron-correction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:positron-correction at q0; emit witness with contentBlock="prop:positron-correction". |
| `prop:q-beta-c3-hopf-three-fold-markov` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-beta-c3-hopf-three-fold-markov at q0; emit witness with contentBlock="prop:q-beta-c3-hopf-three-fold-markov". |
| `prop:q-beta-cos-resummation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-beta-cos-resummation at q0; emit witness with contentBlock="prop:q-beta-cos-resummation". |
| `prop:q-beta-form-a-n1-symbolic` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-beta-form-a-n1-symbolic at q0; emit witness with contentBlock="prop:q-beta-form-a-n1-symbolic". |
| `prop:q-casimir-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-casimir-exists at q0; emit witness with contentBlock="prop:q-casimir-exists". |
| `prop:q-casimir-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-casimir-unique at q0; emit witness with contentBlock="prop:q-casimir-unique". |
| `prop:q-codifferential-formula` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-codifferential-formula at q0; emit witness with contentBlock="prop:q-codifferential-formula". |
| `prop:q-dilogarithm-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-dilogarithm-exists at q0; emit witness with contentBlock="prop:q-dilogarithm-exists". |
| `prop:q-dilogarithm-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-dilogarithm-unique at q0; emit witness with contentBlock="prop:q-dilogarithm-unique". |
| `prop:q-exponential-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-exponential-exists at q0; emit witness with contentBlock="prop:q-exponential-exists". |
| `prop:q-exponential-taylor` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-exponential-taylor at q0; emit witness with contentBlock="prop:q-exponential-taylor". |
| `prop:q-exponential-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-exponential-unique at q0; emit witness with contentBlock="prop:q-exponential-unique". |
| `prop:q-game-of-life` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-game-of-life at q0; emit witness with contentBlock="prop:q-game-of-life". |
| `prop:q-gaussian-solves-q-heat` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-gaussian-solves-q-heat at q0; emit witness with contentBlock="prop:q-gaussian-solves-q-heat". |
| `prop:q-gl-obstruction-calc` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-gl-obstruction-calc at q0; emit witness with contentBlock="prop:q-gl-obstruction-calc". |
| `prop:q-heat-equation-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-heat-equation-exists at q0; emit witness with contentBlock="prop:q-heat-equation-exists". |
| `prop:q-heat-equation-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-heat-equation-unique at q0; emit witness with contentBlock="prop:q-heat-equation-unique". |
| `prop:q-heat-kernel-peter-weyl` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-heat-kernel-peter-weyl at q0; emit witness with contentBlock="prop:q-heat-kernel-peter-weyl". |
| `prop:q-hecke-eigenvalue` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-hecke-eigenvalue at q0; emit witness with contentBlock="prop:q-hecke-eigenvalue". |
| `prop:q-hecke-seminormal-character-closure` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-hecke-seminormal-character-closure at q0; emit witness with contentBlock="prop:q-hecke-seminormal-character-closure". |
| `prop:q-jacobiator` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-jacobiator at q0; emit witness with contentBlock="prop:q-jacobiator". |
| `prop:q-logarithm-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-logarithm-exists at q0; emit witness with contentBlock="prop:q-logarithm-exists". |
| `prop:q-logarithm-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-logarithm-unique at q0; emit witness with contentBlock="prop:q-logarithm-unique". |
| `prop:q-ns-nonlinear-uniqueness` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:q-plancherel-asymptotic-skeleton` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-plancherel-asymptotic-skeleton at q0; emit witness with contentBlock="prop:q-plancherel-asymptotic-skeleton". |
| `prop:q-resolvent-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-resolvent-exists at q0; emit witness with contentBlock="prop:q-resolvent-exists". |
| `prop:q-resolvent-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:q-resolvent-unique at q0; emit witness with contentBlock="prop:q-resolvent-unique". |
| `prop:q-spectral-sobolev` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:q-turbulence-spectrum` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:qmn-recursive-memoized` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:qmn-recursive-memoized at q0; emit witness with contentBlock="prop:qmn-recursive-memoized". |
| `prop:qou-canonical-action` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:qou-canonical-action at q0; emit witness with contentBlock="prop:qou-canonical-action". |
| `prop:qou-is-ccc` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:qou-is-ccc at q0; emit witness with contentBlock="prop:qou-is-ccc". |
| `prop:quantum-characteristic-classes-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:quantum-characteristic-classes-exists at q0; emit witness with contentBlock="prop:quantum-characteristic-classes-exists". |
| `prop:quantum-characteristic-classes-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:quantum-characteristic-classes-unique at q0; emit witness with contentBlock="prop:quantum-characteristic-classes-unique". |
| `prop:quantum-dilogarithm-stratified` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:quantum-dilogarithm-stratified at q0; emit witness with contentBlock="prop:quantum-dilogarithm-stratified". |
| `prop:quantum-dilogarithm-volume` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:quantum-dilogarithm-volume at q0; emit witness with contentBlock="prop:quantum-dilogarithm-volume". |
| `prop:quantum-ideal-gas-law` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:quantum-ideal-gas-law at q0; emit witness with contentBlock="prop:quantum-ideal-gas-law". |
| `prop:quantum-observable-universe-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:quantum-observable-universe-exists at q0; emit witness with contentBlock="prop:quantum-observable-universe-exists". |
| `prop:quantum-universe-exists` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:quantum-universe-exists at q0; emit witness with contentBlock="prop:quantum-universe-exists". |
| `prop:r-matrix-braiding-structure` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:r-matrix-braiding-structure at q0; emit witness with contentBlock="prop:r-matrix-braiding-structure". |
| `prop:recursive-atom-knot-atlas` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:recursive-atom-knot-atlas at q0; emit witness with contentBlock="prop:recursive-atom-knot-atlas". |
| `prop:reeb-operations-per-planck` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:reeb-operations-per-planck at q0; emit witness with contentBlock="prop:reeb-operations-per-planck". |
| `prop:reidemeister-action-table` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:reidemeister-action-table at q0; emit witness with contentBlock="prop:reidemeister-action-table". |
| `prop:reidemeister-mass-invariance` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:reidemeister-mass-invariance at q0; emit witness with contentBlock="prop:reidemeister-mass-invariance". |
| `prop:residue-at-root` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:residue-at-root at q0; emit witness with contentBlock="prop:residue-at-root". |
| `prop:rho-k-graded-expansion` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:rho-k-graded-expansion at q0; emit witness with contentBlock="prop:rho-k-graded-expansion". |
| `prop:ring-closure-barrier` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:ring-closure-barrier at q0; emit witness with contentBlock="prop:ring-closure-barrier". |
| `prop:rj-canonical-inner-product` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:rj-canonical-inner-product at q0; emit witness with contentBlock="prop:rj-canonical-inner-product". |
| `prop:root-of-unity-truncation` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:s5-equivariant-torus-knots` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:s5-equivariant-torus-knots at q0; emit witness with contentBlock="prop:s5-equivariant-torus-knots". |
| `prop:schur-weyl-mass-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:schur-weyl-mass-decomposition at q0; emit witness with contentBlock="prop:schur-weyl-mass-decomposition". |
| `prop:schur-weyl-vanishing` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:schur-weyl-vanishing at q0; emit witness with contentBlock="prop:schur-weyl-vanishing". |
| `prop:sdp-regime-switch` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:sdp-regime-switch at q0; emit witness with contentBlock="prop:sdp-regime-switch". |
| `prop:shell-closure-normal-form` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:shell-closure-normal-form at q0; emit witness with contentBlock="prop:shell-closure-normal-form". |
| `prop:shell-closure-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:shell-closure-stability at q0; emit witness with contentBlock="prop:shell-closure-stability". |
| `prop:shell-filling-rule` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:shell-structure-eigenvalues` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:shell-structure-eigenvalues at q0; emit witness with contentBlock="prop:shell-structure-eigenvalues". |
| `prop:shell-transition-knot` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:shell-transition-knot at q0; emit witness with contentBlock="prop:shell-transition-knot". |
| `prop:sigma-shell-from-beta-chain-derivation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:sigma-shell-from-beta-chain-derivation at q0; emit witness with contentBlock="prop:sigma-shell-from-beta-chain-derivation". |
| `prop:six-term-per-derivation-weights` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:six-term-per-derivation-weights at q0; emit witness with contentBlock="prop:six-term-per-derivation-weights". |
| `prop:skein-bar-antisymmetry` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:skein-bar-antisymmetry at q0; emit witness with contentBlock="prop:skein-bar-antisymmetry". |
| `prop:skein-coulomb-enhancement` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:skein-coulomb-enhancement at q0; emit witness with contentBlock="prop:skein-coulomb-enhancement". |
| `prop:skein-crossing-asymmetry` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:skein-crossing-asymmetry at q0; emit witness with contentBlock="prop:skein-crossing-asymmetry". |
| `prop:skein-finiteness-bound` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:skein-finiteness-bound at q0; emit witness with contentBlock="prop:skein-finiteness-bound". |
| `prop:skein-generation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:skein-generation at q0; emit witness with contentBlock="prop:skein-generation". |
| `prop:skein-polynomial-transfer-matrix` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:skein-polynomial-transfer-matrix at q0; emit witness with contentBlock="prop:skein-polynomial-transfer-matrix". |
| `prop:skein-polynomial-transfer-matrix` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:skein-polynomial-transfer-matrix at q0; emit witness with contentBlock="prop:skein-polynomial-transfer-matrix". |
| `prop:skew-poisson-integration` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:skew-poisson-integration at q0; emit witness with contentBlock="prop:skew-poisson-integration". |
| `prop:sorting-color-energy` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:sorting-color-energy at q0; emit witness with contentBlock="prop:sorting-color-energy". |
| `prop:spectral-chart-correspondence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:spectral-chart-correspondence at q0; emit witness with contentBlock="prop:spectral-chart-correspondence". |
| `prop:spectral-sequence-collapse` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:spectral-sequence-collapse at q0; emit witness with contentBlock="prop:spectral-sequence-collapse". |
| `prop:spectral-sequence-h3-explicit` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:spectral-sequence-h3-explicit at q0; emit witness with contentBlock="prop:spectral-sequence-h3-explicit". |
| `prop:spin-involution-lp-dual-invariance` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:spin-involution-lp-dual-invariance at q0; emit witness with contentBlock="prop:spin-involution-lp-dual-invariance". |
| `prop:spin-labels` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:spin-labels at q0; emit witness with contentBlock="prop:spin-labels". |
| `prop:stable-atom-decidable` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:stable-atom-decidable at q0; emit witness with contentBlock="prop:stable-atom-decidable". |
| `prop:strangelet-crossing-energy` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:strangelet-crossing-energy at q0; emit witness with contentBlock="prop:strangelet-crossing-energy". |
| `prop:strangelet-double-beta` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:strangelet-double-beta at q0; emit witness with contentBlock="prop:strangelet-double-beta". |
| `prop:substrate-consistency-window` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:substrate-consistency-window at q0; emit witness with contentBlock="prop:substrate-consistency-window". |
| `prop:substrate-radial-coordinate` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:substrate-radial-coordinate at q0; emit witness with contentBlock="prop:substrate-radial-coordinate". |
| `prop:surreal-rate-calculus` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:surreal-rate-calculus at q0; emit witness with contentBlock="prop:surreal-rate-calculus". |
| `prop:symbolic-character-table` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:symbolic-character-table at q0; emit witness with contentBlock="prop:symbolic-character-table". |
| `prop:tannaka-krein-reconstruction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:tannaka-krein-reconstruction at q0; emit witness with contentBlock="prop:tannaka-krein-reconstruction". |
| `prop:tau-M-asymptotic-rep-theory` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:tau-M-asymptotic-rep-theory at q0; emit witness with contentBlock="prop:tau-M-asymptotic-rep-theory". |
| `prop:tau-leptonic-universality` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:tau-leptonic-universality at q0; emit witness with contentBlock="prop:tau-leptonic-universality". |
| `prop:term6-binding-density` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:term6-binding-density at q0; emit witness with contentBlock="prop:term6-binding-density". |
| `prop:terminal-resolution` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:terminal-resolution at q0; emit witness with contentBlock="prop:terminal-resolution". |
| `prop:terms-2-6-higher-operations` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:terms-2-6-higher-operations at q0; emit witness with contentBlock="prop:terms-2-6-higher-operations". |
| `prop:three-calibration-discipline` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:three-calibration-discipline at q0; emit witness with contentBlock="prop:three-calibration-discipline". |
| `prop:three-parameters-wedderburn` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:three-parameters-wedderburn at q0; emit witness with contentBlock="prop:three-parameters-wedderburn". |
| `prop:thurston-volume-additivity` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:thurston-volume-additivity at q0; emit witness with contentBlock="prop:thurston-volume-additivity". |
| `prop:toffoli-lp-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:toffoli-lp-stability at q0; emit witness with contentBlock="prop:toffoli-lp-stability". |
| `prop:toffoli-transfer-matrix` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:toffoli-transfer-matrix at q0; emit witness with contentBlock="prop:toffoli-transfer-matrix". |
| `prop:topological-mass-formula` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:topological-mass-formula at q0; emit witness with contentBlock="prop:topological-mass-formula". |
| `prop:topological-mass-formula-algebraic` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:topological-mass-formula-algebraic at q0; emit witness with contentBlock="prop:topological-mass-formula-algebraic". |
| `prop:torus-embeddable-complete` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:torus-embeddable-complete at q0; emit witness with contentBlock="prop:torus-embeddable-complete". |
| `prop:torus-hopf-stability` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:torus-hopf-stability at q0; emit witness with contentBlock="prop:torus-hopf-stability". |
| `prop:torus-knot-generators` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:torus-knot-generators at q0; emit witness with contentBlock="prop:torus-knot-generators". |
| `prop:torus-knot-genus-four-unique` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:torus-knot-genus-four-unique at q0; emit witness with contentBlock="prop:torus-knot-genus-four-unique". |
| `prop:torus-knot-shell-binding` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:torus-knot-shell-binding at q0; emit witness with contentBlock="prop:torus-knot-shell-binding". |
| `prop:tower-binding-energy` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:tower-binding-energy at q0; emit witness with contentBlock="prop:tower-binding-energy". |
| `prop:trace-locality-meets-gs-non-locality` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:trace-locality-meets-gs-non-locality at q0; emit witness with contentBlock="prop:trace-locality-meets-gs-non-locality". |
| `prop:trace-ratio-observable` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:trace-ratio-observable at q0; emit witness with contentBlock="prop:trace-ratio-observable". |
| `prop:transfer-matrix-identities` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:transfer-matrix-identities at q0; emit witness with contentBlock="prop:transfer-matrix-identities". |
| `prop:transfer-matrix-level-independence` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:transfer-matrix-level-independence at q0; emit witness with contentBlock="prop:transfer-matrix-level-independence". |
| `prop:tritium-qvalue-symbolic` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:tritium-qvalue-symbolic at q0; emit witness with contentBlock="prop:tritium-qvalue-symbolic". |
| `prop:trm-hopf-sigma1-sq-closed-form` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:trm-hopf-sigma1-sq-closed-form at q0; emit witness with contentBlock="prop:trm-hopf-sigma1-sq-closed-form". |
| `prop:two-filtration-bridge-general` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:two-filtration-bridge-general at q0; emit witness with contentBlock="prop:two-filtration-bridge-general". |
| `prop:two-filtration-bridge-small-cases` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:two-filtration-bridge-small-cases at q0; emit witness with contentBlock="prop:two-filtration-bridge-small-cases". |
| `prop:type-b-folded-crystal-combinatorics` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:type-b-folded-crystal-combinatorics at q0; emit witness with contentBlock="prop:type-b-folded-crystal-combinatorics". |
| `prop:u1-equivariant-reduction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:u1-equivariant-reduction at q0; emit witness with contentBlock="prop:u1-equivariant-reduction". |
| `prop:unified-curvature-rank-mass-formula` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:unified-curvature-rank-mass-formula at q0; emit witness with contentBlock="prop:unified-curvature-rank-mass-formula". |
| `prop:unified-iterative-correction` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:unified-iterative-correction at q0; emit witness with contentBlock="prop:unified-iterative-correction". |
| `prop:universal-braid-branching` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:universal-braid-branching at q0; emit witness with contentBlock="prop:universal-braid-branching". |
| `prop:universality` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:unstable-atom-decay-channel` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:unstable-atom-decay-channel at q0; emit witness with contentBlock="prop:unstable-atom-decay-channel". |
| `prop:upstream-mathlib-additions` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:upstream-mathlib-additions at q0; emit witness with contentBlock="prop:upstream-mathlib-additions". |
| `prop:vacuum-state` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:vacuum-state at q0; emit witness with contentBlock="prop:vacuum-state". |
| `prop:variational-equations` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:variational-equations at q0; emit witness with contentBlock="prop:variational-equations". |
| `prop:vertex-algebra-jet-relations` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:vertex-algebra-jet-relations at q0; emit witness with contentBlock="prop:vertex-algebra-jet-relations". |
| `prop:vertex-algebra-relations` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:vertex-algebra-relations at q0; emit witness with contentBlock="prop:vertex-algebra-relations". |
| `prop:vertex-is-exceptional-divisor` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:vertex-is-exceptional-divisor at q0; emit witness with contentBlock="prop:vertex-is-exceptional-divisor". |
| `prop:vol-through-tau` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:vol-through-tau at q0; emit witness with contentBlock="prop:vol-through-tau". |
| `prop:volume-perturbation-formula` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:volume-perturbation-formula at q0; emit witness with contentBlock="prop:volume-perturbation-formula". |
| `prop:volume-tower-decomposition` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:volume-tower-decomposition at q0; emit witness with contentBlock="prop:volume-tower-decomposition". |
| `prop:vorticity-lower-bound` | proposition | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `prop:weak-equiv-invariance` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:weak-equiv-invariance at q0; emit witness with contentBlock="prop:weak-equiv-invariance". |
| `prop:weak-symmetric-normalization` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:weak-symmetric-normalization at q0; emit witness with contentBlock="prop:weak-symmetric-normalization". |
| `prop:wedderburn-as-noncomm-fourier` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wedderburn-as-noncomm-fourier at q0; emit witness with contentBlock="prop:wedderburn-as-noncomm-fourier". |
| `prop:wedderburn-bratteli-recursion` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wedderburn-bratteli-recursion at q0; emit witness with contentBlock="prop:wedderburn-bratteli-recursion". |
| `prop:wedderburn-mass-formula` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wedderburn-mass-formula at q0; emit witness with contentBlock="prop:wedderburn-mass-formula". |
| `prop:wedderburn-trace-identity` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wedderburn-trace-identity at q0; emit witness with contentBlock="prop:wedderburn-trace-identity". |
| `prop:wedderburn-weight-canonical` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wedderburn-weight-canonical at q0; emit witness with contentBlock="prop:wedderburn-weight-canonical". |
| `prop:wenzl-bridge-applicability-qou` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wenzl-bridge-applicability-qou at q0; emit witness with contentBlock="prop:wenzl-bridge-applicability-qou". |
| `prop:wenzl-qmn-synergy` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wenzl-qmn-synergy at q0; emit witness with contentBlock="prop:wenzl-qmn-synergy". |
| `prop:wigner-2-coefficient` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wigner-2-coefficient at q0; emit witness with contentBlock="prop:wigner-2-coefficient". |
| `prop:wigner-coefficient-derivation` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wigner-coefficient-derivation at q0; emit witness with contentBlock="prop:wigner-coefficient-derivation". |
| `prop:wigner-np-pairing` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:wigner-np-pairing at q0; emit witness with contentBlock="prop:wigner-np-pairing". |
| `prop:x5-bring-weight-identification` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:x5-bring-weight-identification at q0; emit witness with contentBlock="prop:x5-bring-weight-identification". |
| `prop:x5-z5-automorphism` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:x5-z5-automorphism at q0; emit witness with contentBlock="prop:x5-z5-automorphism". |
| `prop:y-lambda-cyclotomic-factorization` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:y-lambda-cyclotomic-factorization at q0; emit witness with contentBlock="prop:y-lambda-cyclotomic-factorization". |
| `prop:yekutieli-lifting` | proposition | NOT-WIRED | I1 | Write probe_*.py exercising prop:yekutieli-lifting at q0; emit witness with contentBlock="prop:yekutieli-lifting". |
| `thm:categorical-reeb-exists` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:categorical-reeb-exists at q0; emit witness with contentBlock="thm:categorical-reeb-exists". |
| `thm:confinement-grading-correspondence-conditional` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:confinement-grading-correspondence-conditional at q0; emit witness with contentBlock="thm:confinement-grading-correspondence-conditional". |
| `thm:descartes` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:descartes at q0; emit witness with contentBlock="thm:descartes". |
| `thm:em-spectral-completeness` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:em-spectral-completeness at q0; emit witness with contentBlock="thm:em-spectral-completeness". |
| `thm:embeddability-closure` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:embeddability-closure at q0; emit witness with contentBlock="thm:embeddability-closure". |
| `thm:explicit-formula` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:explicit-formula at q0; emit witness with contentBlock="thm:explicit-formula". |
| `thm:flavor-mass-splitting-bound` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:flavor-mass-splitting-bound at q0; emit witness with contentBlock="thm:flavor-mass-splitting-bound". |
| `thm:frobenius-antipode-unifies-chirality-and-tower` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:frobenius-antipode-unifies-chirality-and-tower at q0; emit witness with contentBlock="thm:frobenius-antipode-unifies-chirality-and-tower". |
| `thm:frobenius-codim-universal` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:frobenius-codim-universal at q0; emit witness with contentBlock="thm:frobenius-codim-universal". |
| `thm:generation-completeness` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:generation-completeness at q0; emit witness with contentBlock="thm:generation-completeness". |
| `thm:groebner-shirshov-energy` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:groebner-shirshov-energy at q0; emit witness with contentBlock="thm:groebner-shirshov-energy". |
| `thm:groebner-shirshov-energy` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:groebner-shirshov-energy at q0; emit witness with contentBlock="thm:groebner-shirshov-energy". |
| `thm:hasse-weil-bound` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:hasse-weil-bound at q0; emit witness with contentBlock="thm:hasse-weil-bound". |
| `thm:hyperelliptic-z5-classification` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:hyperelliptic-z5-classification at q0; emit witness with contentBlock="thm:hyperelliptic-z5-classification". |
| `thm:jones-markov-trace` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:jones-markov-trace at q0; emit witness with contentBlock="thm:jones-markov-trace". |
| `thm:macroscopic-stability-equivalence` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:macroscopic-stability-equivalence at q0; emit witness with contentBlock="thm:macroscopic-stability-equivalence". |
| `thm:markov-trace-factorization` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:markov-trace-factorization at q0; emit witness with contentBlock="thm:markov-trace-factorization". |
| `thm:markov-trace-factorization` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:markov-trace-factorization at q0; emit witness with contentBlock="thm:markov-trace-factorization". |
| `thm:markov-trace-product` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:markov-trace-product at q0; emit witness with contentBlock="thm:markov-trace-product". |
| `thm:mass-energy-equivalence` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:mass-energy-equivalence at q0; emit witness with contentBlock="thm:mass-energy-equivalence". |
| `thm:ns-singularity-descartes` | theorem | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `thm:observability-q-independent` | theorem | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `thm:parity-regime-selection` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:parity-regime-selection at q0; emit witness with contentBlock="thm:parity-regime-selection". |
| `thm:q-bkm` | theorem | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `thm:q-ns-wellposedness` | theorem | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `thm:qou-obstruction-reduction` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:qou-obstruction-reduction at q0; emit witness with contentBlock="thm:qou-obstruction-reduction". |
| `thm:qu-to-qou` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:qu-to-qou at q0; emit witness with contentBlock="thm:qu-to-qou". |
| `thm:quantum-gap-collapse` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:quantum-gap-collapse at q0; emit witness with contentBlock="thm:quantum-gap-collapse". |
| `thm:quantum-peter-weyl` | theorem | NOT-WIRED | I1-stated | Lean stated with 1 sorrys; once proved, author probe per I1. |
| `thm:su2-emergence` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:su2-emergence at q0; emit witness with contentBlock="thm:su2-emergence". |
| `thm:substrate-parameter-exists` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:substrate-parameter-exists at q0; emit witness with contentBlock="thm:substrate-parameter-exists". |
| `thm:substrate-parameter-unique` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:substrate-parameter-unique at q0; emit witness with contentBlock="thm:substrate-parameter-unique". |
| `thm:substrate-self-duality` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:substrate-self-duality at q0; emit witness with contentBlock="thm:substrate-self-duality". |
| `thm:tannaka-krein-isomorphism` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:tannaka-krein-isomorphism at q0; emit witness with contentBlock="thm:tannaka-krein-isomorphism". |
| `thm:topological-charge-quantization` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:topological-charge-quantization at q0; emit witness with contentBlock="thm:topological-charge-quantization". |
| `thm:wedderburn-mass-formula` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:wedderburn-mass-formula at q0; emit witness with contentBlock="thm:wedderburn-mass-formula". |
| `thm:weight-decomposition-exists` | theorem | NOT-WIRED | I1 | Write probe_*.py exercising thm:weight-decomposition-exists at q0; emit witness with contentBlock="thm:weight-decomposition-exists". |

---

## 4. Idle-sweep checkpoint

This was a one-shot IDLE-SWEEP. No `.wip.json` checkpoint needed (full scan completed without interruption).

- **Scan duration:** ~30 s
- **Witness files indexed:** 481
- **Production consumer scripts checked:** 7 (all exist on `main`)
    - `paper_six_term_isotope_sweep.py`
    - `derive_m_p_hecke_full_tower_50dps.py`
    - `derive_m_n_hecke_full_tower_50dps.py`
    - `atomic_mass_via_rho_k.py`
    - `mass_table_ppb.py`
    - `build_proton_mass_50dps_chain.py`
    - `build_neutron_mass_50dps_chain.py`
- **Underlying machine-readable result:** `/tmp/sweep-result.json` (rerun reproducible via the inline scan harness; not committed)

### Suggested follow-up branches

Per the skill's §B Idle-sweep clause ("batch fixes ≤30 minutes apiece into a single follow-up branch"):

1. **`claude/iw-i2-thread-y-lambda-2026-05-18`** — fixes #3 (PROBE-ONLY thread). Single edit to `paper_six_term_isotope_sweep.py`.
2. **`claude/iw-i2-thread-shadow-price-2026-05-18`** — fix #5. Single edit to `atomic_mass_via_rho_k.py`.
3. **`claude/iw-i5-cleanup-2026-05-18`** — fix #8 (9 witnesses). Either creates 3 small content blocks (`prop:magic-shell-coupling-witness`, `prop:atomic-mass-via-rho-k`, `prop:codata-mass-anchors`) or repoints `contentBlock` to closest sibling. Owner sign-off on the create-vs-repoint choice via author-question queue.
4. **`claude/iw-i7-stale-rerun-2026-05-18`** — fix #10 (86 stale probes). Mechanical `python3 probe_*.py` reruns; commit only when numerics unchanged; surface diffs to author for review.
5. **`claude/compute-integration-probes-2026-05-18`** — batched probe authoring for the top-20 high-degree hubs (fixes #1, #2, and 18 others). Largest of the five branches; ≥1 day estimate.

### Author-question queue items (P1)

Per skill §C, append to `docs/audits/compute-integration-question-queue.md` (gitignored):

- **Q-2026-05-18-A** (P1) — *I5 cleanup choice:* for `prop:magic-shell-coupling-witness` (referenced by 5 witnesses), should we (1) author a new prop block in `appendix-knot-periodic-table/`, (2) repoint all 5 witnesses to existing `prop:atom-knot-mass-derivation`, or (3) demote to `rem:` with `interprets:` link? Skill default: (1) — substantive enough to warrant a dedicated prop.
- **Q-2026-05-18-B** (P1) — *I7 batch policy:* for the 86 stale probes, is the policy "rerun all, commit unchanged, surface diffs" or "surface all 86 for owner review before any rerun"? Affects branch #4 above.
- **Q-2026-05-18-C** (P2) — *Coverage scope:* should `quantum-observable-universes/`, `fluid-dynamics/`, `q-geometric-langlands/` (currently 0 wired across 90+ provable blocks) ever have probes, or are these structural / categorical-only chapters by design? Affects how to interpret the global 11/558 = 2% WIRED rate.

---

## 5. Methodology notes

- **Provable-block enumeration:** every `.ts` file in `content/quantum-observable-universe/**` whose `import` line is `proposition`, `theorem`, `lemma`, or `corollary` (558 hits).
- **Lean status:** sibling-`.lean` file scan; sorry-count via regex `\bsorry\b`. Conjecture-class detection (CLAUDE.md §3b-cond) via `^class\s+`.
- **Witness coverage:** every `computations/*.witness.json` (481 files) parsed for a `contentBlock: "<label>"` field. 319 entries across 132 unique labels.
- **Production consumption:** grep of the 7 production-consumer scripts for either the block's label or one of its witness filenames. Producer relationship (a script writing the witness) also counts as consumption.
- **I5 / I12:** extra cross-witness scan, distinct from the per-block sweep.
- **I7 staleness:** witness `computedAt` (or file mtime) compared with sibling-`.md` mtime; >7 days = stale.
- **I4 hash drift:** witness `upstream_witness_hashes` checked against SHA1 of upstream witness on disk.
- **Out of scope:** I3 (guard-off) requires reading consumer source for `if False`/feature flags — left for manual triage of WIRED set. I6 cleared (0 hits). I8/I9 covered by `compute-audit` skill, not this skill. I10/I11 require deeper consumer audit.
