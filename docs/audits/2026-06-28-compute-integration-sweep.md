# Compute-integration idle-sweep — 2026-06-28

Branch: `claude/wlambda-ladder-higher-rungs-2026-06-28`
Skill: `local/compute-integration-watcher` (IDLE-SWEEP, Group A focus: I1 / I2)
Scope: all `prop:` / `thm:` / `lem:` / `cor:` blocks under
`content/quantum-observable-universe/`.

## Executive summary

- **640 provable labels** (prop/thm/lem/cor) enumerated; **1033 witness
  files** and **25 production-consumer scripts** indexed.
- **56 provable blocks carry a probe witness** (`contentBlock: "<label>"`).
  Of these, **8 are WIRED** into a production consumer and **48 are
  PROBE-ONLY (I2)** — a witness exists but no `derive_*` / `build_*chain` /
  `paper_six_term*` / `atomic_mass_*` / `mass_table_ppb` / `canonical_mass`
  consumer references the label or its witness file.
- **584 provable blocks have no probe witness at all.** Restricting to
  *live-math* labels (mass / binding / q_beta / markov / hecke / wedderburn /
  sdp / tau / trace / volume / pole / nucleon …) and to those whose Lean
  sibling is **sorry-free single-decl** and is **not** conditional-class /
  conjecture-dependent gives **73 genuine I1 (proved, not-probed)** blocks.
  A further **8 are UNVERIFIED** (the label appears inside a real probe
  witness under a non-`contentBlock` field — likely already probed; needs
  manual confirmation) and **13 are conditional-class / conj-touching**
  (skipped per the skill — they do not require a compute consumer).
- **Highest-value wiring targets** are the q_beta `c_k` closed-form
  coefficient identities (Lean-proved, extensive `c3-hopf-habiro` /
  `c-k-beta-decay-bound` probe compute exists but its witnesses do **not**
  set `contentBlock` to these props) and the absolute-mass / binding props
  (`neutron-proton-mass-splitting`, `derived-mass-formula-light-isotopes`,
  `hoefsmit-binding-amplitude`, `mass-tower-coefficient-stratification`).

> **Conservatism note (per AGENTS.md "do not over-declare not-wired").**
> "PROBE-ONLY (I2)" below is a *consumer-grep* verdict: a witness may still
> be consumed through a `upstream_witness_hashes` chain or via an
> intermediate witness this sweep did not transitively follow. Where the
> grep was ambiguous the row is marked **UNVERIFIED**. Treat I2 rows as
> "no *direct* production reference found", not as proof of non-use.

## Method

1. `grep` every `label: "prop:|thm:|lem:|cor:..."` in `content/.../*.ts`
   → 640 labels.
2. `grep '"contentBlock"'` across `computations/*.witness.json` → probe map.
3. Production consumers = `derive_*.py`, `paper_six_term*.py`,
   `atomic_mass_*.py`, `mass_table_ppb.py`, `build_*chain*.py`,
   `canonical_mass.py` (25 files). A block is **WIRED** if a consumer
   references its label string **or** one of its witness filenames.
4. Lean status: sibling `.lean` (single-decl, reliable `sorry` count) or
   `lean.ref`-resolved library module (file-wide `sorry` count — less
   reliable, marked UNVERIFIED where the file is shared).
5. Skipped: conjecture-class (`class C : Prop`), conditional-class
   (`[Conj]`-hypothesis theorems with conditional banner), and blocks whose
   `uses[]` touches a `conj:`.

## I2 — PROBE-ONLY (witness exists, no direct production consumer)

Ranked by leverage (mass/binding/q_beta first). Lean status is the
single-decl sibling sorry count where available.

| label | Lean sorry-free? | probe witness(es) | consumer? | I-pattern | recommended fix |
|---|---|---|---|---|---|
| `prop:markov-trace-axiomatic-closed-form` | yes* | `option-b-proton-mass-full-chain`, `mp-habiro-c4-keystone-probe`, `li2q-fbor-expansion-probe` | **WIRED** (`build_proton_mass_50dps_chain.py`) | — | already wired |
| `prop:full-pole-structure-mass-trace` | yes* | `term6-full-pole-sum`, `proton-mass-codata-50dps` | **WIRED** (3 chains) | — | already wired |
| `prop:mass-endomorphism-tower` | yes* | `proton-mass-full-tower-50dps` +4 | **WIRED** (`derive_m_p_hecke_full_tower_50dps.py`) | — | already wired |
| `prop:atomic-mass-gb-nf` | yes* | `binding-combiner-markov-peel-fallback` +2 | **WIRED** (2 4He/canonical chains) | — | already wired |
| `prop:mass-coefficient-shadow-price` | yes* | `a-K-via-lp-dual-hecke-basis` | **WIRED** (`atomic_mass_via_rho_k.py`) | — | already wired |
| `prop:neutron-qvalue-symbolic` | yes* | `q-beta-form-a-n1-extension` | **WIRED** (`derive_m_baryon_volume_form.py`) | — | already wired |
| `prop:proton-mass-substrate-identity` | yes* | `m-p-substrate-identity-50dps` | **WIRED** (witness filename) | — | already wired |
| `prop:y-lambda-closed-form-wenzl-bridge` | yes* | `y-lambda-at-q0`, `y-lambda-q-schur-lean-verify` | **WIRED** (`y-lambda-at-q0` referenced) | — | already wired |
| `thm:knot-mass-formula-unified` | yes* | `mass-formula-6term-mpfr-50dps`, `build-six-term-substrate-model-b` | **WIRED** (witness filename) | — | already wired |
| `prop:rho-k-h3a-refinement` | yes* | `delta-lambda-2row-stratum` +3 | none found | **I2** | thread `delta-lambda-*` Δ_λ stratum into `atomic_mass_via_rho_k.py` or mark probe-only (Δ_λ gate is a Track-A blocker) |
| `prop:rho-k-graded-expansion` | yes* | `binding-K-direct`, `v-hat-to-delta-lambda-bridge` | none found | **I2** | wire ρ_k graded expansion into the binding chain or `# probe-only` |
| `prop:full-pole-structure-mass-trace` (dup) | — | — | — | — | — |
| `prop:q-beta-categorical-precision-ladder` | yes* | `q-beta-predicted`, `qbeta-multi-block-eigenphase-probe` +2 | none found | **I2** | wire Q_β ladder witness into `derive_q_values.py` / `derive_m_baryon_volume_form.py` (note c_k tiered framing) |
| `prop:q-beta-spectral-bridge` | yes* | `q-beta-spectral-bridge` | none found | **I2** | probe-only spectral cross-check; add `# probe-only` header if intentional |
| `prop:three-calibration-inputs` | yes* | `cal-3-q-beta`, `codata-masses` +2 | none found | **I2** | the CAL inputs are read in chains via constants, not by label — likely WIRED indirectly; **UNVERIFIED** |
| `prop:he4-two-row-dominance` | yes* | `he4-canonical-tr-m-block-fingerprint` | none found | **I2** | wire into `build_atomic_braid_recipe_4he_chain.py` or probe-only |
| `prop:confined-knot-binding` | yes* | `confined-knot-binding` +2 | none found | **I2** | wire into binding chain or probe-only |
| `prop:knot-operator-lp-selection` | yes* | `wedderburn-lp-ew-wiring`, `wedderburn-pair-volumes` | none found | **I2** | LP-dual selection; ensure `derive_e_0_lp_dual_h3.py` consumes it |
| `prop:h2-lp-dual-binding` | yes* | `h2-integer-lp`, `h2-molecular-binding` | none found | **I2** | molecular; wire into a molecular consumer or probe-only |
| `prop:co-lp-dual-binding` | yes* | `co-bond-order-active-set` | none found | **I2** | molecular; probe-only candidate |
| `prop:h2o-bond-angle-shift` | yes* | 7 witnesses | none found | **I2** | molecular; probe-only candidate (no molecular production consumer) |
| `prop:symmetric-block-domain-weight` | yes* | 7 witnesses | none found | **I2** | molecular angle family; probe-only candidate |
| `prop:em-coupling-bring-zero-mode` | yes* | 11 witnesses (α_EM RT phases) | none found | **I2** | α_EM is exploratory; confirm `# probe-only` headers |
| `prop:alpha-em-categorical-trace-ratio` | yes* | `alpha-basis-knot-couplings`, `delta-q-h-bracket-identity` | none found | **I2** | α_EM exploratory; probe-only |
| `prop:alpha-em-shift-multiplicative-chain` | yes* | `alpha-k-split-pole-order-audit` | none found | **I2** | α_EM exploratory; probe-only |
| `prop:alpha-basis-knot-delta-q` | yes* | `rosso-jones-three-strand-delta-q` | none found | **I2** | probe-only |
| `prop:alpha-shift-torus-knot` | yes* | `nh-basis-shift` | none found | **I2** | probe-only |
| `prop:force-carrier-intertwining-correspondence` | yes* | `alpha-k-per-force-assembly` +1 | none found | **I2** | probe-only |
| `prop:frobenius-lepton-meson-bridge` | yes* | `cal3-meson-decay-binding-amplitude`, `knot-operator-sdp-4_1` | none found | **I2** | wire into meson scale (CAL-3) or probe-only |
| `prop:lepton-meson-torus-knot-dictionary` | yes* | `meson-spectrum-predictions`, `meson-symmetry-bar-involution` | none found | **I2** | wire into meson prediction consumer or probe-only |
| `prop:pion-half-figure-eight` | yes* | `mass-table-l1-full-crosscheck` +2 | none found | **I2** | meson; probe-only candidate |
| `prop:atom-knot-mass-derivation` | yes* | `unified-low-isotope-predictor` +4 | none found | **I2** | wire into a low-isotope production chain or probe-only |
| `prop:recursive-atom-knot-atlas` | yes* | `mass-table-comprehensive` | none found | **I2** | probe-only candidate |
| `prop:per-nucleon-shift-additive-linearity` | yes* | `per-nucleon-shift-derivation` | none found | **I2** | wire into binding chain or probe-only |
| `prop:bring-residue-resolvent` | yes* | `bring-residue-resolvent-probe` | none found | **I2** | probe-only |
| `prop:bring-trefoil-cinquefoil-channel` | yes* | `bring-trefoil-cinquefoil-channel` | none found | **I2** | probe-only |
| `prop:chirality-writhe-ribbon-derivation` | yes* | `chirality-avg-content` | none found | **I2** | probe-only |
| `prop:confinement-categorical` | yes* | `atomic-chirality-residue` | none found | **I2** | probe-only |
| `prop:confinement-frobenius-reciprocity` | yes* | `borromean-axial-coupling` | none found | **I2** | probe-only |
| `prop:confinement-nf-partial-proof` | yes* | `shift-from-nf-basis` | none found | **I2** | probe-only |
| `prop:demazure-fiber-markov-trace` | yes* | `demazure-markov-trace` | none found | **I2** | Δ_λ Demazure ansatz (failed on deuteron); probe-only |
| `prop:figure-eight-reeb-rotation` | yes* | `eigenvalue-reeb-extension-h4-h5` | none found | **I2** | probe-only |
| `prop:flavor-dressed-mass-from-substrate-split` | yes* | `flavor-dressed-mass-from-substrate-split` | none found | **I2** | substrate-pure flavor split (I2-a candidate — supersedes a CAL input; see skill §I2-a) |
| `prop:gram-matrix-h3-symbolic` | yes* | `gram-h3-symbolic-regression` | none found | **I2** | wire H3 Gram into Hecke chain or probe-only |
| `prop:macdonald-hook-telescope` | yes* | `y-lambda-macdonald-telescope` | none found | **I2** | y_λ telescope; ensure `y-lambda-at-q0` chain uses it (likely UNVERIFIED) |
| `prop:borromean-markov-trace-closed-form` | yes* | `borromean-chi-independent-crosscheck` | none found | **I2** | core Borromean closed form — verify it feeds `canonical_mass.py` F_Bor (likely UNVERIFIED) |
| `prop:q-beta-bar-even-kernel-typeclass` | yes* | `mass-theory-formalize-first-invariants-probe` | none found | **I2** | probe-only (typeclass invariant) |
| `prop:q-laplacian-spectral-tower` | yes* | `q-spectral-truncation-tower` | none found | **I2** | probe-only |
| `prop:q-zero-complex-extension` | yes* | `real-star-lift-candidates` | none found | **I2** | probe-only |
| `prop:quantum-ideal-gas-law` | yes* | `hbond-categorical-action` | none found | **I2** | probe-only |
| `prop:vdw-pskew-isolation` | yes* | `vdw-pskew-sinh-probe` | none found | **I2** | probe-only |
| `prop:six-canonical-knot-operators` | yes* | `reeb-flow-garside-closed-form-verification` | none found | **I2** | probe-only |
| `prop:rigid-monoidal-structural-gap-invariance` | yes* | `rigid-monoidal-gap-invariance` | none found | **I2** | probe-only |
| `thm:em-spectral-completeness` | yes* | `alpha-k-four-strand-singlet-selection` +1 | none found | **I2** | α_EM; probe-only |
| `thm:six-term-mass-formula-complete` | yes* | `term6-residues-at-roots` | none found | **I2** | verify the six-term residues feed the mass chain (likely UNVERIFIED) |
| `thm:topological-mass` | yes* | `mass-from-q-symbolic` | none found | **I2** | core symbolic mass thm — verify chain use (likely UNVERIFIED) |

\* "Lean sorry-free" is the single-decl sibling count or the resolved
library decl; not re-verified per-decl in shared library files this pass.

## I1 — PROVED, NOT PROBED (sorry-free single-decl, no witness `contentBlock`)

Genuine I1 set = 73. High-value subset (concrete numerical / closed-form
claims that *should* carry a probe witness):

| label | Lean | probe? | consumer? | I-pattern | recommended fix |
|---|---|---|---|---|---|
| `prop:q-beta-c-2-eq-neg-one-structural` | sorry=0 | none | none | **I1** | write `probe_qbeta_c2.py` emitting `contentBlock` = this prop; c_2=-1 is the *proved* Taylor-exact coefficient (cheat-sheet) — its probe should fail CI if c_2≠-1 |
| `prop:q-beta-c-k-recursion-from-habiro-q-difference` | sorry=0 | only forward-ref ledger | none | **I1** | point an existing `c3-hopf-habiro-analysis` / `c-k-beta-decay-bound` witness's `contentBlock` at this prop |
| `prop:q-beta-c-k-leading-bias-correction-identity` | sorry=0 | none | none | **I1** | probe the leading-bias identity at q₀; set `contentBlock` |
| `prop:qbeta-c4-from-c3-c8-product-identity` | sorry=0 | none | none | **I1** | probe the c4 = f(c3,c8) product identity |
| `prop:qbeta-c8-c10-silver-rationals` | sorry=0 | none | none | **I1** | probe c8/c10 silver-ratio rationals at q₀ |
| `prop:qbeta-z-recursion-to-ck-recursion-bridge` | sorry=0 | none | none | **I1** | probe the z→c_k recursion bridge |
| `prop:q-beta-bar-even-kernel-invariant` | sorry=0 | none | none | **I1** | bar-even kernel invariant; probe at q₀ |
| `prop:q-beta-over-e0-classical-vanishing` | sorry=0 | none | none | **I1** | probe q→1 classical-vanishing limit |
| `prop:neutron-proton-mass-splitting` | sorry=0 | none | none | **I1** | write a probe asserting Δ_pn from the split formula vs CODATA (note L2 Δ_pn is a failing observable) |
| `prop:derived-mass-formula-light-isotopes` | sorry=0 | none | none | **I1** | probe light-isotope masses; should cross-check the low-isotope chain |
| `prop:hoefsmit-binding-amplitude` | sorry=0 | none | none | **I1** | probe Hoefsmit binding amplitude at q₀ |
| `prop:mass-tower-coefficient-stratification` | sorry=0 | none | none | **I1** | probe the mass-tower coefficient strata |
| `prop:per-braid-mass-tower` | sorry=0 | none | none | **I1** | probe per-braid mass tower |
| `prop:tower-binding-energy` | sorry=0 | none | none | **I1** | probe tower binding energy |
| `prop:torus-knot-shell-binding` | sorry=0 | none | none | **I1** | probe torus-knot shell binding |
| `prop:markov-trace-ratio-exact` | sorry=0 | none | none | **I1** | probe the exact Markov-trace ratio (core to mass formula) |
| `prop:markov-trace-recursive-reducer` | sorry=0 | none | none | **I1** | probe the recursive reducer against `tr_M` engine |
| `thm:markov-trace-factorization` | sorry=0 | none | none | **I1** | probe the factorization identity |
| `prop:gram-weighted-qvalue` | sorry=0 | none | none | **I1** | probe Gram-weighted Q-value |
| `prop:topological-mass-formula` | sorry=0 | none | none | **I1** | probe the topological mass formula (core) |
| `prop:topological-mass-formula-algebraic` | sorry=0 | none | none | **I1** | probe the algebraic form |
| `prop:unified-curvature-rank-mass-formula` | sorry=0 | none | none | **I1** | probe the unified curvature-rank mass formula |
| `prop:mass-formula-regime-switching` | sorry=0 | none | none | **I1** | probe the regime-switch boundary |
| `prop:binding-scale-catalan` | sorry=0 | none | none | **I1** | probe the Catalan binding scale |
| `prop:binding-error-amplification` | sorry=0 | none | none | **I1** | probe error amplification |
| `prop:chirality-residue-mass-term` | sorry=0 | only forward-ref ledger | none | **I1** | probe the chirality residue mass term |
| `prop:residue-at-root` | sorry=0 | none | none | **I1** | probe residue-at-root |
| `prop:sw-period-residue-sum` | sorry=0 | none | none | **I1** | probe Seifert-van Kampen period residue sum |
| `prop:plancherel-term-7-formulation` | sorry=0 | none | none | **I1** | probe the term-7 Plancherel formulation |

Remaining 44 genuine I1 blocks are structural / existence-uniqueness
lemmas (e.g. `prop:frobenius-pairing-exists`, `prop:q-hecke-eigenvalue`,
`prop:confinement-level-exists`, `prop:wedderburn-as-noncomm-fourier`,
`prop:categorical-archimedean-bridge`, `lem:volume-from-rigidity`, …) —
**low-value I1**: they name a construction or assert a categorical
existence/uniqueness fact that does not yield a numerical witness. Probe
only if a downstream numerical consumer needs the constructed object.

## UNVERIFIED — label appears in a real probe witness (non-`contentBlock` field)

These are **NOT** declared not-wired. The label string occurs inside a
genuine probe witness (not just the `forward-ref-classification` ledger),
so a probe very likely exists under `reference_blocks` / `uses` / prose —
needs a manual open-the-witness check before any wiring action.

| label | witness(es) where label appears | note |
|---|---|---|
| `prop:joint-tower-sdp-confinement` | `joint-tower-sdp-h6-h9`, `joint-tower-sdp-rust` | almost certainly probed (named SDP witnesses) |
| `prop:categorical-mass-markov` | `canonical-isospin-pyhecke`, `delta-lambda-2row-stratum`, `delta-lambda-empirical-tabulation` | likely probed |
| `prop:schur-weyl-mass-decomposition` | `atom-level-wedderburn-tower` | likely probed |
| `thm:frobenius-codim-universal` | `atom-level-wedderburn-tower`, `mass-formula-6term`, `rho-k-h3a-co-casimir` | likely probed |
| `thm:wedderburn-mass-formula` | `atomic-braid-gb-filtration-extension` | likely probed |
| `thm:markov-trace-product` | `vhat-per-crossing-chain` | likely probed |
| `prop:magic-numbers-from-q` | `per-pair-wedderburn-enumeration` | likely probed |
| `prop:categorical-neutrality-saturated-shells` | `per-pair-wedderburn-enumeration`, `topic2-mirror-pair-phi8-boundary-scan` | likely probed |

## Conditional-class / conj-dependent — SKIPPED (no compute consumer required)

Per skill: conjecture-class and §3b-cond conditional-class blocks do not
need a compute consumer. Flagged here for completeness (some flags are
from a broad `class.*: Prop` grep and may include false positives):
`prop:mass-element-nf`, `thm:binding-closure-conditional`,
`prop:shell-structure-eigenvalues`, `prop:graded-hecke-energy-truncation-bound`,
`prop:wedderburn-weight-canonical`, `prop:spin-involution-lp-dual-invariance`,
`prop:hecke-branching-trace-decomposition`, `prop:graded-trace-residue-split`,
`prop:homological-shell-condensation`, `prop:diagrammatic-double-magic-lr-fusion`,
`prop:q-beta-c3-hopf-three-fold-markov`,
`prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor`,
`prop:shell-schur-weyl-self-duality`.

## Recommended next actions (ranked by leverage × tractability)

1. **q_beta c_k closed-form probes (I1, high value).** The Lean side proves
   `c_2=-1`, the c_k recursion, c4/c8/c10 identities, but the extensive
   existing c_k probe compute (`c3-hopf-habiro-analysis`,
   `c-k-beta-decay-bound`, `c-3-categorical-derivation-attempt`) does **not**
   set `contentBlock` to these props. *Cheapest fix:* add the
   `contentBlock` field to the existing witnesses (no new compute). Mind the
   tiered c_k framing (proved / near-match / fitted) — do **not** wire c_3≥
   as Taylor-exact.
2. **Verify the UNVERIFIED 8** by opening the named witnesses; if a probe
   genuinely exists, no action (reclassify WIRED/PROBE-ONLY); if not,
   promote to I1.
3. **Core mass/markov I1 probes:** `markov-trace-ratio-exact`,
   `topological-mass-formula`, `markov-trace-factorization` — these are
   load-bearing for the mass chain and deserve a CI-failing witness.
4. **I2 → production for the live mass/binding props:** `rho-k-h3a-refinement`
   / `rho-k-graded-expansion` (Δ_λ — Track-A gated; probe-only is acceptable
   given the gate) and `he4-two-row-dominance` into the 4He chain.
5. **Molecular + α_EM I2 cluster** (`h2o-*`, `co-*`, `alpha-em-*`,
   `em-coupling-bring-zero-mode`): these are exploratory; the right action is
   usually a `# probe-only: <reason>` header rather than production wiring.
