# Transitive-prune audit — 785 dependencies removed, not deduplicated

Generated 2026-08-10. Data: `.beans/` bean `prn1`.

Two bulk commits pruned `uses[]` edges on the rule *if A→B and B→C, drop A→C*.
That is a valid transitive reduction only when B→C survives the same pass.
Where both were dropped together, the dependency was removed rather than deduplicated.

| commit | edges dropped | genuine reduction | reachability destroyed |
|---|---|---|---|
| `aa07f51383` | 1796 | 1259 | **537** |
| `d2dcd93ebf` | 764 | 445 | **319** |

Of those 856, on `main` today: 25 source blocks no longer exist, 46 became
reachable again, and **785 remain unreachable across 335 blocks** —
80 of which still declare nothing at all.

## Blocks by edges still lost

| lost | block | now empty |
|---|---|---|
| 15 | `rem:millennium-unification` |  |
| 10 | `rem:phase-scoped-applicability` | yes |
| 10 | `rem:bsd-surreal-bound` | yes |
| 9 | `rem:ns-surreal-bound` | yes |
| 9 | `conj:p-vs-np-qou` | yes |
| 9 | `rem:rh-surreal-bound` | yes |
| 8 | `prop:level-sufficiency` | yes |
| 8 | `rem:level-sufficiency-interprets` | yes |
| 8 | `prop:shell-schur-weyl-self-duality` | yes |
| 8 | `rem:yang-mills-surreal-bound` | yes |
| 8 | `prop:surreal-rate-calculus` |  |
| 8 | `rem:adelic-tate-squeeze` |  |
| 8 | `rem:p-vs-np-surreal-bound` | yes |
| 7 | `rem:archimedean-stpart-strategy` | yes |
| 7 | `conj:crossing-graded-mass-expansion` | yes |
| 6 | `prop:jet-tower-convergence` |  |
| 6 | `prop:shell-closure-stability` |  |
| 6 | `rem:ns-blowup-physical-evidence` |  |
| 6 | `conj:archimedean-stpart` |  |
| 6 | `rem:body-asymptotics-catalog` |  |
| 6 | `rem:q-metric-contact-deformation` |  |
| 6 | `prop:phi-q-categorical-truncation` |  |
| 5 | `def:dressed-particle` | yes |
| 5 | `rem:hecke-algebra-from-braiding` | yes |
| 5 | `prop:delta-max-uniform-bound` |  |
| 5 | `prop:full-pole-structure-mass-trace` | yes |
| 5 | `prop:compound-beta-shell-calibration` |  |
| 5 | `prop:descended-level-zero` |  |
| 5 | `rem:mass-tower-syt-cells` | yes |
| 5 | `rem:analytic-obstructions` |  |
| 5 | `rem:braid-fluid` |  |
| 5 | `prop:ilp-covalent-bond` | yes |
| 5 | `rem:bw-mass-decomposition-dictionary` | yes |
| 5 | `prop:quantum-dilogarithm-stratified` | yes |
| 5 | `prop:alpha-em-categorical-trace-ratio` | yes |
| 5 | `prop:confinement-frobenius-reciprocity` | yes |
| 4 | `def:local-shadow-ordering` |  |
| 4 | `prop:hecke-mass-trace` |  |
| 4 | `prop:atom-knot-exists` | yes |
| 4 | `def:typed-crossing-operator` | yes |
| 4 | `prop:confinement-phase-stratification` |  |
| 4 | `rem:hecke-charge-mass-duality` |  |
| 4 | `rem:knot-particle-generation-interpretation` | yes |
| 4 | `rem:quarks-borromean-picture` | yes |
| 4 | `rem:nucleon-nf-observability` | yes |
| 4 | `rem:down-quark-properties` | yes |
| 4 | `prop:q-turbulence-spectrum` | yes |
| 4 | `def:classical-limit-functor` |  |
| 4 | `prop:wedderburn-as-noncomm-fourier` | yes |
| 4 | `prop:frobenius-self-duality-forces-lp-dual-extraction` | yes |
| 4 | `prf:quantum-dilogarithm-stratified` | yes |
| 4 | `prop:topological-mass-formula-algebraic` |  |
| 4 | `thm:wedderburn-mass-formula` | yes |
| 4 | `lem:vhat-pair-commutation-trace` | yes |
| 4 | `prf:phi-q-categorical-truncation` | yes |
| 4 | `prop:nuclear-knot-classification` |  |
| 4 | `prop:per-braid-mass-tower` |  |
| 4 | `prop:cyclotomic-orbit-sum-all-depths` | yes |
| 4 | `prop:alpha-em-shift-multiplicative-chain` | yes |
| 4 | `thm:groebner-shirshov-energy` |  |
| 4 | `rem:binding-knots-visual-inventory` | yes |
| 3 | `rem:shell-closure-stability-interprets` | yes |
| 3 | `def:unstable-atom` | yes |
| 3 | `prop:atom-knot-unique` |  |
| 3 | `prop:pentagon-uv-commutation` |  |
| 3 | `rem:hadron-interpretation` | yes |
| 3 | `def:confinement-category` |  |
| 3 | `def:confined-particle` | yes |
| 3 | `prop:hadron-exists` | yes |
| 3 | `prop:unified-iterative-correction` |  |
| 3 | `prop:mass-endomorphism-tower` |  |
| 3 | `prop:stable-atom-decidable` | yes |
| 3 | `rem:ilp-solution-count-unwrap` |  |
| 3 | `prop:gb-spectral-sequence` | yes |
| 3 | `conj:higgs-t28` |  |
| 3 | `prop:borromean-hopf-energy-crossover` |  |
| 3 | `prop:strangelet-crossing-energy` | yes |
| 3 | `def:hopf-diquark` | yes |
| 3 | `rem:fermion-boson-chart-localization` |  |
| 3 | `prop:torus-knot-shell-binding` |  |
| 3 | `rem:meson-to-proton-via-borromean` |  |
| 3 | `def:breit-wheeler-pair-production` | yes |
| 3 | `conj:classical-limit-stpart` |  |
| 3 | `rem:planck-reynolds` |  |
| 3 | `prop:kelvin-dispersion-derivation` |  |
| 3 | `sim:knot-periodic-table` |  |
| 3 | `def:q-from-epsilon` |  |
| 3 | `prop:q-gl-obstruction-calc` | yes |
| 3 | `def:q-local-system` |  |
| 3 | `ex:hydrogen-derived-nf` |  |
| 3 | `rem:strutinsky-from-graded-trace` |  |
| 3 | `prop:knot-operator-transition` |  |
| 3 | `prop:three-calibration-inputs` | yes |
| 3 | `prop:jonquiere-cyclotomic-tate-rationality` |  |
| 3 | `lem:degree-one-braid-trivial-volume` | yes |
| 3 | `prop:graded-markov-trace-from-gs-filtration` | yes |
| 3 | `prose:pre-archimedean-derivation-chain` |  |
| 3 | `prop:operator-selection-lp` |  |
| 3 | `rem:bound-state-frobenius-self-dual-channel` | yes |
| 3 | `prop:atom-knot-mass-derivation` |  |
| 3 | `lem:tower-pair-equality-fixed-level` |  |
| 3 | `rem:qvalue-derivation-chain` |  |
| 2 | `prop:knot-particle-correspondence` |  |
| 2 | `rem:knot-particle-dictionary` |  |
| 2 | `ex:hadron-proton` |  |
| 2 | `rem:borromean-baryon-interpretation` | yes |
| 2 | `def:hecke-mass-element` |  |
| 2 | `prop:unstable-atom-decay-channel` |  |
| 2 | `def:skein-binding-lagrangian` |  |
| 2 | `prop:mobius-energy` |  |
| 2 | `rem:kashaev-volume-density` |  |
| 2 | `def:isotope-knot` |  |
| 2 | `ex:hydrogen-knot-structure` | yes |
| 2 | `prop:neutron-proton-mass-splitting` |  |
| 2 | `prop:eos-borromean-cfl` |  |
| 2 | `rem:half-life-as-q-probe` |  |
| 2 | `sec:strangelet-intro` |  |
| 2 | `prop:strangelet-double-beta` |  |
| 2 | `def:quark-antiquark-production` | yes |
| 2 | `prop:nuclear-spin-parity` | yes |
| 2 | `prop:torus-hopf-stability` | yes |
| 2 | `def:categorical-meson` |  |
| 2 | `rem:up-quark-properties` | yes |
| 2 | `prop:categorical-proton-exists` | yes |
| 2 | `sim:valley-stability` |  |
| 2 | `prop:skein-coulomb-enhancement` | yes |
| 2 | `conj:vacuum-epsilon` |  |
| 2 | `conj:bigbang-heatdeath` |  |
| 2 | `thm:q-ns-wellposedness` |  |
| 2 | `prop:acoustic-horizon-conditions` |  |
| 2 | `rem:hamilton-jacobi-phase` |  |
| 2 | `rem:knot-centric-table` |  |
| 2 | `prose:knot-periodic-table` |  |
| 2 | `prop:braiding-eigenvalue-extraction` | yes |
| 2 | `def:quantum-gauge-group` |  |
| 2 | `prop:tannaka-krein-reconstruction` |  |
| 2 | `rem:affine-chart-origin-of-i-and-q` |  |
| 2 | `def:q-flat-connection` |  |
| 2 | `rem:q-holonomy-locality-derivation` |  |
| 2 | `prop:confinement-operator-selection` |  |
| 2 | `ex:helium4-derived-nf` |  |
| 2 | `rem:frobenius-packing-density` | yes |
| 2 | `def:per-nucleon-channel-decomposition` |  |
| 2 | `conj:mass-volume-factorization` |  |
| 2 | `rem:soft-confinement-at-q0` |  |
| 2 | `prop:four-term-pair-nucleon` |  |
| 2 | `thm:generation-completeness` | yes |
| 2 | `rem:epistemic-status-of-calibrations` |  |
| 2 | `rem:feynman-qou-comparison` |  |
| 2 | `def:three-calibration-discipline` |  |
| 2 | `prop:magic-numbers-from-q` | yes |
| 2 | `rem:townsend-biot-savart-strain` | yes |
| 2 | `rem:hyperbolic-overlap-saturation` |  |
| 2 | `prop:recursive-atom-knot-atlas` |  |
| 2 | `tm-inductive-construction` |  |
| 2 | `tm-heavy-atom-examples` |  |
| 2 | `prop:habiro-residue-sum-equivalence` |  |
| 2 | `prop:lepton-bring-surface-h3-3channel` |  |
| 2 | `def:algebraic-quantum-volume` | yes |
| 2 | `conj:depth-stratified-frobenius-reciprocity` |  |
| 2 | `prop:rho-k-h3a-refinement` |  |
| 2 | `prop:ground-state-ordering` |  |
| 2 | `prop:confined-knot-binding` |  |
| 2 | `prop:jucys-murphy-central-elements-qou` |  |
| 2 | `rem:archimedean-image-table` |  |
| 2 | `prop:gram-determinant-plancherel-ratio` |  |
| 2 | `prop:phi-q-tower-algebraic-stratification` |  |
| 2 | `prop:cyclotomic-dimension-synthesis-all-depths` |  |
| 2 | `prop:he4-two-row-dominance` |  |
| 2 | `def:z-habiro-ring` |  |
| 2 | `def:motivic-mass-measure` |  |
| 2 | `def:q-pochhammer-partial-product` |  |
| 2 | `prop:pieri-photon-shift` |  |
| 2 | `rem:hopf-link-non-magic` |  |
| 2 | `def:qz-bicompletion` |  |
| 2 | `prop:residue-at-root` |  |
| 2 | `def:delta-q-decoration` |  |
| 2 | `def:archimedean-realization-functor` |  |
| 2 | `ex:qvalue-benchmark-table` |  |
| 2 | `prop:rho-k-graded-expansion` |  |
| 2 | `def:qou-motivic-galois-instance` |  |
| 2 | `prop:em-coupling-bring-zero-mode` |  |
| 2 | `rem:force-carrier-spectral-interpretation` | yes |
| 2 | `rem:alpha-em-derivation-exploration-options` |  |
| 2 | `cor:spectral-decomposition-qvalue` | yes |
| 2 | `sim:beta-decay-braid` |  |
| 2 | `prop:gram-weighted-qvalue` |  |
| 1 | `prop:feynman-classical-limit` |  |
| 1 | `prop:hecke-markov-transition` | yes |
| 1 | `def:bundle-initial-conditions` |  |
| 1 | `def:nucleon-hecke-element` |  |
| 1 | `prop:terms-2-6-higher-operations` |  |
| 1 | `def:atom-knot` |  |
| 1 | `prop:confinement-level-exists` | yes |
| 1 | `def:hecke-normal-form` |  |
| 1 | `def:bundle-isotopy-equivalence` |  |
| 1 | `def:borromean-baryon` |  |
| 1 | `rem:shell-transition-knot-interpretation` |  |
| 1 | `def:crossing-energy` |  |
| 1 | `def:confinement-level` | yes |
| 1 | `def:knot-particle-generation` |  |
| 1 | `prop:hecke-convergence-bound` | yes |
| 1 | `thm:six-term-mass-formula-complete` |  |
| 1 | `def:localized-hadron` |  |
| 1 | `def:hadron` | yes |
| 1 | `def:knot-operator-energy` |  |
| 1 | `prop:graded-trace-residue-split` |  |
| 1 | `def:stable-atom` |  |
| 1 | `prop:hadron-unique` |  |
| 1 | `prop:gb-residue-spectral-sum` |  |
| 1 | `prop:universal-braid-branching` |  |
| 1 | `rem:mass-endomorphism-jet-tower` | yes |
| 1 | `conj:borromean-quark` |  |
| 1 | `rem:strangelet-witten-stability` |  |
| 1 | `prf:terminal-resolution` |  |
| 1 | `conj:color-superconductivity-borromean` |  |
| 1 | `prop:noble-gas-characterization` |  |
| 1 | `def:stable-nucleus` |  |
| 1 | `rem:torus-knot-prime-powers` |  |
| 1 | `prop:categorical-neutron-exists` |  |
| 1 | `rem:unmapped-torus-knots` |  |
| 1 | `prop:categorical-neutron-unique` |  |
| 1 | `prop:categorical-proton-unique` |  |
| 1 | `def:transfer-matrix-operator` | yes |
| 1 | `prop:beta-decay-transfer-matrix` |  |
| 1 | `prop:parity-violation-skein` |  |
| 1 | `def:neutrino-knot` |  |
| 1 | `rem:knot-formula-table` |  |
| 1 | `def:positron-knot` |  |
| 1 | `rem:algebraic-core-survives` |  |
| 1 | `rem:calculus-up-to-epsilon` |  |
| 1 | `conj:infinitesimal-frobenius` |  |
| 1 | `conj:infinitesimal-observability` |  |
| 1 | `def:ns-obstruction` |  |
| 1 | `prop:helicity-conservation` |  |
| 1 | `rem:geodesic-vortices` |  |
| 1 | `prop:universality` |  |
| 1 | `def:q-navier-stokes` | yes |
| 1 | `prop:q-spectral-sobolev` |  |
| 1 | `prop:ns-obstruction-computation` |  |
| 1 | `prop:horizon-conformal-invariance` |  |
| 1 | `rem:penrose-ccc` | yes |
| 1 | `rem:cmb-photon-color-content` |  |
| 1 | `prop:photon-threading-mass` |  |
| 1 | `def:cmb-boundary-datum` |  |
| 1 | `prop:qou-is-ccc` |  |
| 1 | `def:aeon` |  |
| 1 | `rem:jet-planck-steps` |  |
| 1 | `rem:knot-atom-diagrams` |  |
| 1 | `tm-knot-pairs` |  |
| 1 | `rem:braiding-unit-circle-convention` |  |
| 1 | `prop:spectral-chart-correspondence` | yes |
| 1 | `rem:geometric-rh-exposition` |  |
| 1 | `rem:glossary-q-bit` |  |
| 1 | `rem:particle-nf-table` |  |
| 1 | `rem:hadron-level-knot-table` |  |
| 1 | `rem:gluon-model-comparison` |  |
| 1 | `rem:q-flat-connection` |  |
| 1 | `def:typed-garside-element` |  |
| 1 | `prop:atomic-lp-stability` |  |
| 1 | `prop:confinement-sdp` |  |
| 1 | `conj:lifted-crossing-locality` |  |
| 1 | `ex:chi-minus-six-derivation` |  |
| 1 | `ex:archimedean-yekutieli` |  |
| 1 | `prop:sdp-regime-switch` |  |
| 1 | `rem:atom-mass-full-hecke` |  |
| 1 | `rem:mass-comparison-table` |  |
| 1 | `rem:color-confinement-observation` |  |
| 1 | `prop:algebraic-gns-embedding` |  |
| 1 | `rem:physics-names-knot-operations` |  |
| 1 | `rem:electron-immortality` |  |
| 1 | `rem:vacuum-polarization-virtual-pairs` |  |
| 1 | `sim:beta-decay-halflife` |  |
| 1 | `rem:fine-structure-observation` |  |
| 1 | `prf:algebraic-gns-embedding` |  |
| 1 | `prop:toffoli-lp-stability` |  |
| 1 | `rem:generating-functions-solve-reeb-flow` |  |
| 1 | `def:q-dilogarithm` |  |
| 1 | `rem:t211-ideal-annihilation` |  |
| 1 | `rem:commutative-crossing-energy` |  |
| 1 | `def:motivic-galois-character` |  |
| 1 | `rem:kummer-tower` |  |
| 1 | `prop:y-lambda-cyclotomic-factorization` |  |
| 1 | `rem:kashaev-as-archimedean-realization` |  |
| 1 | `rem:vassiliev-filtration-mass-tower` |  |
| 1 | `prop:rigid-monoidal-structural-gap-invariance` |  |
| 1 | `prop:curvature-rank-gb-stratification` |  |
| 1 | `prop:per-nucleon-shift-additive-linearity` | yes |
| 1 | `prop:joint-tower-sdp-confinement` |  |
| 1 | `rem:vol-as-motivic-period` |  |
| 1 | `prop:mass-tower-coefficient-stratification` |  |
| 1 | `prop:y-lambda-closed-form-wenzl-bridge` |  |
| 1 | `prop:e-infinity-page-identifications` |  |
| 1 | `prop:y-lambda-recipe-from-partition` |  |
| 1 | `prop:confinement-nf-partial-proof` |  |
| 1 | `rem:hecke-markov-interpretation` |  |
| 1 | `prop:qmn-recursive-memoized` |  |
| 1 | `prop:markov-trace-ratio-exact` |  |
| 1 | `prop:wigner-coefficient-derivation` |  |
| 1 | `cor:commutative-chirality-vanishes` |  |
| 1 | `prop:explicit-alpha-k-h3` |  |
| 1 | `conj:kashaev-volume-conjecture` |  |
| 1 | `rem:two-tier-scaling-pq` |  |
| 1 | `prop:mass-coefficient-shadow-price` |  |
| 1 | `prop:wedderburn-weight-canonical` |  |
| 1 | `prop:six-term-per-derivation-weights` |  |
| 1 | `prop:knot-factor-spectral-form` |  |
| 1 | `prop:alpha-shift-torus-knot` |  |
| 1 | `prop:sigma-shell-from-beta-chain-derivation` |  |
| 1 | `def:adelic-substrate` | yes |
| 1 | `prop:force-carrier-intertwining-correspondence` |  |
| 1 | `def:two-row-stratum` |  |
| 1 | `thm:knot-mass-formula-unified` |  |
| 1 | `prop:hook-weight-derivation` |  |
| 1 | `thm:markov-trace-factorization` |  |
| 1 | `prop:spin-involution-lp-dual-invariance` |  |
| 1 | `prop:demazure-fiber-markov-trace` |  |
| 1 | `def:phi-q-piece` |  |
| 1 | `prop:wenzl-bridge-applicability-qou` |  |
| 1 | `prop:knot-operator-lp-selection` |  |
| 1 | `prop:wenzl-qmn-synergy` |  |
| 1 | `rem:isospin-mass-split-em-localisation` |  |
| 1 | `prf:atom-knot-mass-derivation` |  |
| 1 | `prop:explicit-central-idempotent` |  |
| 1 | `prop:hecke-baer-star-generic` |  |
| 1 | `prop:shell-structure-eigenvalues` |  |
| 1 | `prop:em-coupling-projection` |  |
| 1 | `prop:quantum-dilogarithm-volume` |  |
| 1 | `prop:tau-leptonic-universality` |  |
| 1 | `rem:em-completeness-interpretation` |  |
| 1 | `prop:knot-operator-selection` |  |
| 1 | `rem:beta-decay-interpretation` |  |
| 1 | `rem:ontological-agnosticism` |  |
| 1 | `rem:energy-scale-planck` |  |
| 1 | `rem:confinement-nucleon-unit` |  |

## Every still-unreachable edge

### `rem:millennium-unification`

- `thm:macroscopic-stability-equivalence`
- `thm:quantum-gap-collapse`
- `conj:p-vs-np-qou`
- `conj:q-birch-swinnerton-dyer`
- `def:categorical-reeb-derivation`
- `prop:surreal-rate-calculus`
- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `rem:rh-surreal-bound`
- `rem:ns-surreal-bound`
- `rem:p-vs-np-surreal-bound`
- `rem:bsd-surreal-bound`
- `rem:adelic-tate-squeeze`
- `rem:conway-normal-form`
- `rem:body-asymptotics-catalog`

### `rem:phase-scoped-applicability`

- `prop:confinement-phase-stratification`
- `def:confined-particle`
- `def:confinement-category`
- `prop:confinement-sdp`
- `prop:level-sufficiency`
- `prop:shell-closure-stability`
- `def:electron-shell`
- `def:dressed-particle`
- `rem:deconfinement-golden-threshold`
- `thm:parity-regime-selection`

### `rem:bsd-surreal-bound`

- `conj:q-birch-swinnerton-dyer`
- `thm:quantum-gap-collapse`
- `lem:surreal-squeeze`
- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `prop:surreal-rate-calculus`
- `rem:rh-surreal-bound`
- `rem:adelic-tate-squeeze`
- `rem:conway-normal-form`
- `rem:calculus-up-to-epsilon`

### `rem:ns-surreal-bound`

- `prop:blowup-yekutieli`
- `thm:q-ns-wellposedness`
- `lem:surreal-squeeze`
- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `prop:surreal-rate-calculus`
- `prop:ns-obstruction-computation`
- `rem:conway-normal-form`
- `rem:body-asymptotics-catalog`

### `conj:p-vs-np-qou`

- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `def:classical-limit-functor`
- `thm:quantum-gap-collapse`
- `prop:surreal-rate-calculus`
- `lem:surreal-squeeze`
- `rem:p-vs-np-surreal-bound`
- `rem:conway-normal-form`
- `rem:calculus-up-to-epsilon`

### `rem:rh-surreal-bound`

- `thm:quantum-gap-collapse`
- `conj:classical-riemann-hypothesis`
- `thm:macroscopic-stability-equivalence`
- `lem:surreal-squeeze`
- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `prop:surreal-rate-calculus`
- `rem:conway-normal-form`
- `rem:calculus-up-to-epsilon`

### `prop:level-sufficiency`

- `def:confined-particle`
- `def:confinement-category`
- `def:confinement-level`
- `def:hecke-normal-form`
- `prop:confinement-sdp`
- `prop:confinement-topological`
- `prop:confinement-operator-selection`
- `prop:confinement-phase-stratification`

### `rem:level-sufficiency-interprets`

- `prop:level-sufficiency`
- `def:confined-particle`
- `def:confinement-category`
- `def:confinement-level`
- `def:electron-shell`
- `def:dressed-particle`
- `prop:confinement-sdp`
- `prop:confinement-topological`

### `prop:shell-schur-weyl-self-duality`

- `def:confinement-level`
- `def:stable-atom`
- `prop:bw-coefficient-shadow-price`
- `def:hecke-normal-form`
- `thm:jones-markov-trace`
- `def:quantum-su2`
- `prop:skein-crossing-asymmetry`
- `prop:shell-transition-knot`

### `rem:yang-mills-surreal-bound`

- `thm:quantum-gap-collapse`
- `prop:surreal-rate-calculus`
- `lem:surreal-squeeze`
- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `rem:ns-surreal-bound`
- `rem:conway-normal-form`
- `rem:calculus-up-to-epsilon`

### `prop:surreal-rate-calculus`

- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `thm:quantum-gap-collapse`
- `def:categorical-reeb-derivation`
- `rem:conway-normal-form`
- `rem:body-asymptotics-catalog`
- `def:surreal-blowup-calculus`
- `rem:calculus-up-to-epsilon`

### `rem:adelic-tate-squeeze`

- `thm:hasse-weil-bound`
- `thm:macroscopic-stability-equivalence`
- `rem:rh-surreal-bound`
- `rem:bsd-surreal-bound`
- `lem:surreal-squeeze`
- `def:q-from-epsilon`
- `prop:surreal-rate-calculus`
- `rem:conway-normal-form`

### `rem:p-vs-np-surreal-bound`

- `conj:p-vs-np-qou`
- `lem:surreal-squeeze`
- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `prop:surreal-rate-calculus`
- `rem:millennium-unification`
- `rem:conway-normal-form`
- `rem:calculus-up-to-epsilon`

### `rem:archimedean-stpart-strategy`

- `conj:archimedean-stpart`
- `conj:classical-limit-stpart`
- `def:standard-part-functor`
- `rem:fibre-functor-rigidity`
- `conj:infinitesimal-frobenius`
- `conj:infinitesimal-observability`
- `conj:vacuum-epsilon`

### `conj:crossing-graded-mass-expansion`

- `conj:mass-volume-factorization`
- `rem:kashaev-volume-density`
- `def:crossing-energy`
- `def:algebraic-quantum-volume`
- `prop:descartes-elliptic-curve`
- `prop:thurston-volume-additivity`
- `prop:tower-binding-energy`

### `prop:jet-tower-convergence`

- `prop:mass-endomorphism-tower`
- `rem:mass-endomorphism-jet-tower`
- `rem:conway-normal-form`
- `rem:calculus-up-to-epsilon`
- `def:surreal-blowup-calculus`
- `rem:body-asymptotics-catalog`

### `prop:shell-closure-stability`

- `def:electron-shell`
- `def:confined-particle`
- `def:confinement-category`
- `prop:confinement-sdp`
- `prop:confinement-topological`
- `prop:confinement-phase-stratification`

### `rem:ns-blowup-physical-evidence`

- `rem:ns-surreal-bound`
- `rem:millennium-unification`
- `def:reeb-epsilon`
- `def:q-from-epsilon`
- `rem:conway-normal-form`
- `rem:calculus-up-to-epsilon`

### `conj:archimedean-stpart`

- `def:standard-part-functor`
- `def:surreal-blowup-calculus`
- `conj:infinitesimal-frobenius`
- `conj:infinitesimal-observability`
- `conj:vacuum-epsilon`
- `rem:fibre-functor-rigidity`

### `rem:body-asymptotics-catalog`

- `rem:conway-normal-form`
- `rem:calculus-up-to-epsilon`
- `prop:universal-braid-branching`
- `rem:kashaev-volume-density`
- `rem:mass-endomorphism-jet-tower`
- `conj:kashaev-surreal`

### `rem:q-metric-contact-deformation`

- `prop:levi-degeneracy`
- `def:ns-obstruction`
- `prop:core-levi-form`
- `rem:hyperbolic-overlap-saturation`
- `rem:townsend-biot-savart-strain`
- `thm:q-ns-wellposedness`

### `prop:phi-q-categorical-truncation`

- `prop:spectral-sequence-collapse`
- `prop:curvature-rank-gb-stratification`
- `prop:categorical-mass-markov`
- `cor:quantum-dilogarithm`
- `def:hecke-normal-form`
- `def:confinement-level`

### `def:dressed-particle`

- `def:confined-particle`
- `def:electron-shell`
- `def:confinement-category`
- `prop:confinement-sdp`
- `prop:confinement-phase-stratification`

### `rem:hecke-algebra-from-braiding`

- `prop:braiding-eigenvalue-extraction`
- `thm:jones-markov-trace`
- `def:substrate-parameter`
- `def:crossing-energy`
- `prop:nuclear-groebner-reduction`

### `prop:delta-max-uniform-bound`

- `rem:mass-endomorphism-jet-tower`
- `prop:mass-endomorphism-tower`
- `def:recursive-brane-tower`
- `thm:markov-trace-factorization`
- `prop:descent-eigenspaces`

### `prop:full-pole-structure-mass-trace`

- `def:hecke-normal-form`
- `def:habiro-ring`
- `def:habiro-ring`
- `prop:gb-residue-spectral-sum`
- `prop:schur-weyl-mass-decomposition`

### `prop:compound-beta-shell-calibration`

- `def:confinement-level`
- `def:stable-atom`
- `prop:bw-coefficient-shadow-price`
- `def:hecke-normal-form`
- `def:knot-operator-energy`

### `prop:descended-level-zero`

- `prop:mass-endomorphism-tower`
- `rem:mass-endomorphism-jet-tower`
- `prop:jet-tower-convergence`
- `prop:categorical-mass-markov`
- `thm:markov-trace-factorization`

### `rem:mass-tower-syt-cells`

- `rem:mass-endomorphism-jet-tower`
- `prop:mass-endomorphism-tower`
- `thm:markov-trace-factorization`
- `def:recursive-brane-tower`
- `def:descent-involution`

### `rem:analytic-obstructions`

- `def:birthday-grading`
- `def:classical-limit-functor`
- `prop:hoefsmit-scattering-pipeline`
- `prf:mobius-energy`
- `rem:kashaev-volume-density`

### `rem:braid-fluid`

- `prop:braid-action-tensor`
- `prop:r-matrix-braiding-structure`
- `thm:jones-markov-trace`
- `rem:skein-crossing-asymmetry`
- `def:crossing-energy`

### `prop:ilp-covalent-bond`

- `def:molecular-braid`
- `def:atomic-braid`
- `prop:wedderburn-mass-formula`
- `def:universal-ilp-algorithm`
- `prop:q-integer-mass-formula`

### `rem:bw-mass-decomposition-dictionary`

- `prop:schur-weyl-mass-decomposition`
- `prop:gb-residue-spectral-sum`
- `prop:markov-pair-z2`
- `prop:shell-schur-weyl-self-duality`
- `prop:wigner-2-coefficient`

### `prop:quantum-dilogarithm-stratified`

- `cor:quantum-dilogarithm`
- `prop:curvature-rank-gb-stratification`
- `prop:spectral-sequence-collapse`
- `def:hecke-normal-form`
- `def:q-pochhammer-partial-product`

### `prop:alpha-em-categorical-trace-ratio`

- `def:delta-q-decoration`
- `prop:em-coupling-projection`
- `prop:force-carrier-bring-uniqueness`
- `prop:force-carrier-intertwining-correspondence`
- `prop:e-hartree-categorical-derivation`

### `prop:confinement-frobenius-reciprocity`

- `prop:frobenius-gram-matrix`
- `prop:operator-selection-lp`
- `prop:mass-coefficient-shadow-price`
- `prop:confinement-operator-selection`
- `prop:knot-factor-frobenius-pairing`

### `def:local-shadow-ordering`

- `def:knot-operator-energy`
- `prop:bw-coefficient-shadow-price`
- `def:confinement-level`
- `prop:mass-endomorphism-tower`

### `prop:hecke-mass-trace`

- `def:mass-identity`
- `thm:jones-markov-trace`
- `thm:topological-mass`
- `prop:topological-mass-formula`

### `prop:atom-knot-exists`

- `def:atom-knot`
- `def:atomic-braid`
- `def:hecke-normal-form`
- `def:borromean-baryon`

### `def:typed-crossing-operator`

- `def:up-quark`
- `def:down-quark`
- `def:borromean-baryon`
- `rem:hecke-algebra-from-braiding`

### `prop:confinement-phase-stratification`

- `def:confined-particle`
- `def:confinement-category`
- `prop:confinement-sdp`
- `prop:confinement-topological`

### `rem:hecke-charge-mass-duality`

- `def:coulomb-charge`
- `def:crossing-energy`
- `def:vertex-operator`
- `def:frobenius-pairing`

### `rem:knot-particle-generation-interpretation`

- `def:knot-particle-generation`
- `prop:skein-generation`
- `rem:color-tube-interpretation`
- `def:color-tube-coordinates`

### `rem:quarks-borromean-picture`

- `def:hadron`
- `conj:borromean-quark`
- `def:borromean-baryon`
- `prop:terminal-resolution`

### `rem:nucleon-nf-observability`

- `prop:nuclear-groebner-reduction`
- `def:categorical-neutron`
- `def:categorical-proton`
- `def:color-tube-fibers`

### `rem:down-quark-properties`

- `def:down-quark`
- `def:up-quark`
- `def:borromean-baryon`
- `rem:skein-crossing-asymmetry`

### `prop:q-turbulence-spectrum`

- `rem:planck-reynolds`
- `prop:discrete-vortex-spectrum`
- `rem:vortex-intensity-modes`
- `def:substrate-parameter`

### `def:classical-limit-functor`

- `conj:classical-limit-stpart`
- `conj:archimedean-stpart`
- `rem:archimedean-stpart-strategy`
- `def:motivic-substrate`

### `prop:wedderburn-as-noncomm-fourier`

- `thm:wedderburn-mass-formula`
- `thm:jones-markov-trace`
- `thm:markov-trace-product`
- `prop:wedderburn-weight-canonical`

### `prop:frobenius-self-duality-forces-lp-dual-extraction`

- `prop:mass-coefficient-shadow-price`
- `prop:operator-selection-lp`
- `prop:wedderburn-trace-identity`
- `thm:jones-markov-trace`

### `prf:quantum-dilogarithm-stratified`

- `cor:quantum-dilogarithm`
- `prop:curvature-rank-gb-stratification`
- `prop:spectral-sequence-collapse`
- `prop:categorical-mass-markov`

### `prop:topological-mass-formula-algebraic`

- `thm:topological-mass`
- `def:algebraic-quantum-volume`
- `def:quantum-planck-constant`
- `thm:markov-trace-factorization`

### `thm:wedderburn-mass-formula`

- `prop:atomic-mass-gb-nf`
- `prop:three-parameters-wedderburn`
- `prop:binding-scale-catalan`
- `def:atomic-braid`

### `lem:vhat-pair-commutation-trace`

- `def:algebraic-quantum-volume`
- `thm:markov-trace-factorization`
- `thm:jones-markov-trace`
- `prop:markov-pair-z2`

### `prf:phi-q-categorical-truncation`

- `prop:spectral-sequence-collapse`
- `prop:curvature-rank-gb-stratification`
- `prop:unified-curvature-rank-mass-formula`
- `prop:categorical-mass-markov`

### `prop:nuclear-knot-classification`

- `def:atomic-braid`
- `thm:topological-mass`
- `prop:topological-mass-formula`
- `prop:hook-weight-derivation`

### `prop:per-braid-mass-tower`

- `rem:mass-endomorphism-jet-tower`
- `prop:graded-trace-residue-split`
- `prop:wedderburn-weight-canonical`
- `prop:schur-weyl-mass-decomposition`

### `prop:cyclotomic-orbit-sum-all-depths`

- `prop:cyclotomic-cl3-orbit-sum-general`
- `prop:jonquiere-cyclotomic-tate-rationality`
- `prop:cyclotomic-dimension-synthesis-all-depths`
- `rem:transcendental-accounting`

### `prop:alpha-em-shift-multiplicative-chain`

- `prop:em-coupling-projection`
- `prop:alpha-shift-torus-knot`
- `prop:force-carrier-bring-uniqueness`
- `def:delta-q-decoration`

### `thm:groebner-shirshov-energy`

- `prop:nuclear-groebner-reduction`
- `def:habiro-ring`
- `def:motivic-substrate`
- `def:archimedean-realization-functor`

### `rem:binding-knots-visual-inventory`

- `rem:knot-particle-dictionary`
- `def:localized-knot`
- `def:atomic-braid`
- `def:borromean-baryon`

### `rem:shell-closure-stability-interprets`

- `prop:shell-closure-stability`
- `def:dressed-particle`
- `def:electron-shell`

### `def:unstable-atom`

- `def:stable-atom`
- `def:atom-knot`
- `def:knot-operator-energy`

### `prop:atom-knot-unique`

- `def:atom-knot`
- `thm:jones-markov-trace`
- `def:hecke-normal-form`

### `prop:pentagon-uv-commutation`

- `prop:mass-endomorphism-tower`
- `rem:mass-endomorphism-jet-tower`
- `rem:mass-endomorphism-jet-tower`

### `rem:hadron-interpretation`

- `def:hadron`
- `def:coulomb-charge`
- `def:localized-hadron`

### `def:confinement-category`

- `prop:confinement-sdp`
- `prop:confinement-phase-stratification`
- `def:hecke-normal-form`

### `def:confined-particle`

- `def:hecke-normal-form`
- `def:confinement-level`
- `prop:confinement-sdp`

### `prop:hadron-exists`

- `def:hadron`
- `def:crossing-energy`
- `def:categorical-proton`

### `prop:unified-iterative-correction`

- `prop:mass-endomorphism-tower`
- `rem:conway-normal-form`
- `rem:body-asymptotics-catalog`

### `prop:mass-endomorphism-tower`

- `def:quantum-bloch-group`
- `rem:mass-endomorphism-jet-tower`
- `cor:quantum-dilogarithm`

### `prop:stable-atom-decidable`

- `def:stable-atom`
- `def:atom-knot`
- `def:confinement-level`

### `rem:ilp-solution-count-unwrap`

- `def:confinement-level`
- `def:stable-atom`
- `def:atom-knot`

### `prop:gb-spectral-sequence`

- `def:hecke-normal-form`
- `prop:graded-trace-residue-split`
- `thm:knot-mass-formula-unified`

### `conj:higgs-t28`

- `conj:borromean-quark`
- `def:exceptional-divisor`
- `prop:borromean-quark`

### `prop:borromean-hopf-energy-crossover`

- `def:hadron`
- `conj:borromean-quark`
- `def:crossing-energy`

### `prop:strangelet-crossing-energy`

- `def:crossing-energy`
- `def:coulomb-charge`
- `prop:torus-hopf-stability`

### `def:hopf-diquark`

- `conj:borromean-quark`
- `def:crossing-energy`
- `def:coulomb-charge`

### `rem:fermion-boson-chart-localization`

- `prop:spectral-chart-correspondence`
- `prop:braiding-eigenvalue-extraction`
- `rem:affine-chart-origin-of-i-and-q`

### `prop:torus-knot-shell-binding`

- `prop:torus-knot-generators`
- `def:transfer-matrix-operator`
- `prop:skein-finiteness-bound`

### `rem:meson-to-proton-via-borromean`

- `def:categorical-proton`
- `conj:borromean-quark`
- `def:quark-antiquark-production`

### `def:breit-wheeler-pair-production`

- `def:electron-knot`
- `def:positron-knot`
- `sec:knot-notation-convention`

### `conj:classical-limit-stpart`

- `def:standard-part-functor`
- `conj:archimedean-stpart`
- `rem:archimedean-stpart-strategy`

### `rem:planck-reynolds`

- `rem:madelung-fluid`
- `prop:discrete-vortex-spectrum`
- `rem:vortex-intensity-modes`

### `prop:kelvin-dispersion-derivation`

- `prop:discrete-vortex-spectrum`
- `rem:vortex-intensity-modes`
- `rem:geodesic-vortices`

### `sim:knot-periodic-table`

- `def:borromean-baryon`
- `prop:fermion-boson-knot-link`
- `prop:shell-transition-knot`

### `def:q-from-epsilon`

- `def:substrate-parameter`
- `conj:infinitesimal-frobenius`
- `def:surreal-blowup-calculus`

### `prop:q-gl-obstruction-calc`

- `def:q-flat-connection`
- `def:quantum-characteristic-classes`
- `def:q-local-system`

### `def:q-local-system`

- `def:categorical-q-connection`
- `def:substrate-parameter`
- `prop:categorical-dq-squared`

### `ex:hydrogen-derived-nf`

- `def:categorical-proton`
- `def:electron-knot`
- `ex:hydrogen-knot-structure`

### `rem:strutinsky-from-graded-trace`

- `prop:graded-trace-residue-split`
- `prop:gb-residue-spectral-sum`
- `prop:shell-schur-weyl-self-duality`

### `prop:knot-operator-transition`

- `def:atomic-braid`
- `rem:knot-particle-dictionary`
- `prop:nuclear-knot-classification`

### `prop:three-calibration-inputs`

- `rem:calibration-inputs`
- `prop:three-parameters-wedderburn`
- `prop:categorical-mass-markov`

### `prop:jonquiere-cyclotomic-tate-rationality`

- `prop:cyclotomic-orbit-sum-all-depths`
- `prop:cyclotomic-dimension-synthesis-all-depths`
- `rem:transcendental-accounting`

### `lem:degree-one-braid-trivial-volume`

- `thm:jones-markov-trace`
- `def:archimedean-realization-functor`
- `def:algebraic-quantum-volume`

### `prop:graded-markov-trace-from-gs-filtration`

- `prop:graded-trace-residue-split`
- `prop:gb-spectral-sequence`
- `prop:confinement-level-exists`

### `prose:pre-archimedean-derivation-chain`

- `def:archimedean-realization-functor`
- `prop:gb-spectral-sequence`
- `thm:jones-markov-trace`

### `prop:operator-selection-lp`

- `def:habiro-ring`
- `def:motivic-substrate`
- `def:archimedean-realization-functor`

### `rem:bound-state-frobenius-self-dual-channel`

- `prop:force-carrier-intertwining-correspondence`
- `prop:antiparticle-crossing-reversal`
- `def:delta-q-decoration`

### `prop:atom-knot-mass-derivation`

- `thm:jones-markov-trace`
- `def:archimedean-realization-functor`
- `prop:gb-spectral-sequence`

### `lem:tower-pair-equality-fixed-level`

- `prop:markov-pair-z2`
- `thm:markov-trace-factorization`
- `def:algebraic-quantum-volume`

### `rem:qvalue-derivation-chain`

- `prop:rj-canonical-inner-product`
- `prop:skein-polynomial-transfer-matrix`
- `prop:shell-closure-normal-form`

### `prop:knot-particle-correspondence`

- `def:localized-knot`
- `prop:knot-eigenbasis-complete`

### `rem:knot-particle-dictionary`

- `prop:fermion-boson-knot-link`
- `def:borromean-baryon`

### `ex:hadron-proton`

- `def:hadron`
- `def:borromean-baryon`

### `rem:borromean-baryon-interpretation`

- `def:borromean-baryon`
- `def:hadron`

### `def:hecke-mass-element`

- `def:mass-identity`
- `thm:jones-markov-trace`

### `prop:unstable-atom-decay-channel`

- `def:stable-atom`
- `def:knot-operator-energy`

### `def:skein-binding-lagrangian`

- `rem:skein-crossing-asymmetry`
- `def:hadron`

### `prop:mobius-energy`

- `conj:classical-limit-stpart`
- `conj:vacuum-epsilon`

### `rem:kashaev-volume-density`

- `def:habiro-ring`
- `conj:kashaev-surreal`

### `def:isotope-knot`

- `def:hecke-normal-form`
- `def:stable-atom`

### `ex:hydrogen-knot-structure`

- `def:electron-knot`
- `conj:electron-shells-hopf`

### `prop:neutron-proton-mass-splitting`

- `def:categorical-proton`
- `def:categorical-neutron`

### `prop:eos-borromean-cfl`

- `def:crossing-energy`
- `def:hadron`

### `rem:half-life-as-q-probe`

- `rem:hadron-half-life-regimes`
- `prop:hadron-q-self-correction`

### `sec:strangelet-intro`

- `conj:borromean-quark`
- `def:crossing-energy`

### `prop:strangelet-double-beta`

- `def:crossing-energy`
- `def:coulomb-charge`

### `def:quark-antiquark-production`

- `def:up-quark`
- `def:down-quark`

### `prop:nuclear-spin-parity`

- `def:stable-nucleus`
- `prop:fermion-boson-knot-link`

### `prop:torus-hopf-stability`

- `rem:skein-crossing-asymmetry`
- `def:categorical-neutron`

### `def:categorical-meson`

- `def:hadron`
- `sec:knot-notation-convention`

### `rem:up-quark-properties`

- `def:up-quark`
- `def:borromean-baryon`

### `prop:categorical-proton-exists`

- `def:categorical-proton`
- `conj:borromean-quark`

### `sim:valley-stability`

- `def:coulomb-charge`
- `prop:local-substrate-q`

### `prop:skein-coulomb-enhancement`

- `prop:hadron-half-life`
- `def:electron-knot`

### `conj:vacuum-epsilon`

- `def:standard-part-functor`
- `def:surreal-blowup-calculus`

### `conj:bigbang-heatdeath`

- `def:surreal-blowup-calculus`
- `def:standard-part-functor`

### `thm:q-ns-wellposedness`

- `rem:q-laplacian-interpretation`
- `prop:discrete-vortex-spectrum`

### `prop:acoustic-horizon-conditions`

- `rem:madelung-fluid`
- `rem:gr-substrate-geometry`

### `rem:hamilton-jacobi-phase`

- `rem:madelung-fluid`
- `rem:schrodinger-jet-coaction`

### `rem:knot-centric-table`

- `prop:fermion-boson-knot-link`
- `prop:shell-transition-knot`

### `prose:knot-periodic-table`

- `prop:fermion-boson-knot-link`
- `def:borromean-baryon`

### `prop:braiding-eigenvalue-extraction`

- `def:quantum-observable-universe`
- `thm:su2-emergence`

### `def:quantum-gauge-group`

- `prop:tannaka-krein-reconstruction`
- `prop:braiding-eigenvalue-extraction`

### `prop:tannaka-krein-reconstruction`

- `def:quantum-observable-universe`
- `thm:su2-emergence`

### `rem:affine-chart-origin-of-i-and-q`

- `def:commutative-qou`
- `def:quantum-gauge-group`

### `def:q-flat-connection`

- `def:categorical-q-connection`
- `prop:categorical-dq-squared`

### `rem:q-holonomy-locality-derivation`

- `conj:lifted-crossing-locality`
- `conj:crossing-graded-mass-expansion`

### `prop:confinement-operator-selection`

- `def:categorical-proton`
- `def:categorical-neutron`

### `ex:helium4-derived-nf`

- `def:categorical-proton`
- `def:categorical-neutron`

### `rem:frobenius-packing-density`

- `rem:kashaev-volume-density`
- `prop:tower-binding-energy`

### `def:per-nucleon-channel-decomposition`

- `thm:jones-markov-trace`
- `def:borromean-baryon`

### `conj:mass-volume-factorization`

- `rem:kashaev-volume-density`
- `prop:tower-binding-energy`

### `rem:soft-confinement-at-q0`

- `rem:kashaev-volume-density`
- `prop:algebraic-volume-specialization`

### `prop:four-term-pair-nucleon`

- `def:categorical-proton`
- `def:categorical-neutron`

### `thm:generation-completeness`

- `prop:torus-embeddable-complete`
- `rem:knot-formula-table`

### `rem:epistemic-status-of-calibrations`

- `rem:calibration-inputs`
- `prop:three-parameters-wedderburn`

### `rem:feynman-qou-comparison`

- `thm:wedderburn-mass-formula`
- `def:algebraic-quantum-volume`

### `def:three-calibration-discipline`

- `def:categorical-action`
- `thm:jones-markov-trace`

### `prop:magic-numbers-from-q`

- `prop:nuclear-knot-classification`
- `prop:mass-coefficient-shadow-price`

### `rem:townsend-biot-savart-strain`

- `prop:levi-degeneracy`
- `prop:core-levi-form`

### `rem:hyperbolic-overlap-saturation`

- `prop:levi-degeneracy`
- `prop:core-levi-form`

### `prop:recursive-atom-knot-atlas`

- `def:atomic-braid`
- `thm:jones-markov-trace`

### `tm-inductive-construction`

- `def:transfer-matrix-operator`
- `prop:shell-closure-normal-form`

### `tm-heavy-atom-examples`

- `def:transfer-matrix-operator`
- `prop:shell-closure-normal-form`

### `prop:habiro-residue-sum-equivalence`

- `prop:gb-residue-spectral-sum`
- `def:habiro-ring`

### `prop:lepton-bring-surface-h3-3channel`

- `prop:three-parameters-wedderburn`
- `rem:calibration-inputs`

### `def:algebraic-quantum-volume`

- `thm:wedderburn-mass-formula`
- `def:q-pochhammer-partial-product`

### `conj:depth-stratified-frobenius-reciprocity`

- `prop:plancherel-term-7-formulation`
- `prop:unified-curvature-rank-mass-formula`

### `prop:rho-k-h3a-refinement`

- `prop:atomic-mass-gb-nf`
- `prop:wedderburn-as-noncomm-fourier`

### `prop:ground-state-ordering`

- `prop:beta-decay-transfer-matrix`
- `prop:frobenius-gram-matrix`

### `prop:confined-knot-binding`

- `prop:three-parameters-wedderburn`
- `def:atomic-braid`

### `prop:jucys-murphy-central-elements-qou`

- `prop:wedderburn-trace-identity`
- `rem:hecke-algebra-from-braiding`

### `rem:archimedean-image-table`

- `def:archimedean-realization-functor`
- `def:spatial-realization-functor`

### `prop:gram-determinant-plancherel-ratio`

- `prop:force-carrier-bring-uniqueness`
- `thm:em-spectral-completeness`

### `prop:phi-q-tower-algebraic-stratification`

- `prop:graded-markov-trace-from-gs-filtration`
- `prop:gb-spectral-sequence`

### `prop:cyclotomic-dimension-synthesis-all-depths`

- `prop:jonquiere-cyclotomic-tate-rationality`
- `prop:cyclotomic-orbit-sum-all-depths`

### `prop:he4-two-row-dominance`

- `def:atomic-braid`
- `thm:jones-markov-trace`

### `def:z-habiro-ring`

- `def:habiro-ring`
- `def:algebraic-quantum-volume`

### `def:motivic-mass-measure`

- `def:motivic-substrate`
- `def:arc-space`

### `def:q-pochhammer-partial-product`

- `cor:quantum-dilogarithm`
- `def:hecke-normal-form`

### `prop:pieri-photon-shift`

- `prop:wedderburn-as-noncomm-fourier`
- `thm:jones-markov-trace`

### `rem:hopf-link-non-magic`

- `prop:knot-operator-selection`
- `def:brings-surface`

### `def:qz-bicompletion`

- `def:habiro-ring`
- `def:algebraic-quantum-volume`

### `prop:residue-at-root`

- `prop:graded-trace-residue-split`
- `def:q-pochhammer-partial-product`

### `def:delta-q-decoration`

- `prop:em-coupling-projection`
- `prop:force-carrier-bring-uniqueness`

### `def:archimedean-realization-functor`

- `def:motivic-substrate`
- `def:algebraic-quantum-volume`

### `ex:qvalue-benchmark-table`

- `prop:rj-canonical-inner-product`
- `prop:beta-decay-transfer-matrix`

### `prop:rho-k-graded-expansion`

- `thm:knot-mass-formula-unified`
- `prop:binding-scale-catalan`

### `def:qou-motivic-galois-instance`

- `def:habiro-ring`
- `def:motivic-substrate`

### `prop:em-coupling-bring-zero-mode`

- `prop:em-coupling-projection`
- `prop:force-carrier-bring-uniqueness`

### `rem:force-carrier-spectral-interpretation`

- `prop:force-carrier-bring-uniqueness`
- `rem:force-knot-identification`

### `rem:alpha-em-derivation-exploration-options`

- `prop:gb-spectral-sequence`
- `prop:force-carrier-bring-uniqueness`

### `cor:spectral-decomposition-qvalue`

- `prop:rj-canonical-inner-product`
- `prop:beta-decay-transfer-matrix`

### `sim:beta-decay-braid`

- `def:transfer-matrix-operator`
- `rem:force-knot-identification`

### `prop:gram-weighted-qvalue`

- `prop:frobenius-gram-matrix`
- `def:transfer-matrix-operator`

### `prop:feynman-classical-limit`

- `rem:hecke-algebra-from-braiding`

### `prop:hecke-markov-transition`

- `rem:hecke-algebra-from-braiding`

### `def:bundle-initial-conditions`

- `def:localized-knot`

### `def:nucleon-hecke-element`

- `def:borromean-baryon`

### `prop:terms-2-6-higher-operations`

- `def:habiro-ring`

### `def:atom-knot`

- `def:hecke-normal-form`

### `prop:confinement-level-exists`

- `def:hecke-normal-form`

### `def:hecke-normal-form`

- `def:substrate-parameter`

### `def:bundle-isotopy-equivalence`

- `def:localized-hadron`

### `def:borromean-baryon`

- `sec:knot-notation-convention`

### `rem:shell-transition-knot-interpretation`

- `def:borromean-baryon`

### `def:crossing-energy`

- `rem:r-matrix-braiding`

### `def:confinement-level`

- `def:hecke-normal-form`

### `def:knot-particle-generation`

- `prop:fermion-boson-knot-link`

### `prop:hecke-convergence-bound`

- `rem:conway-normal-form`

### `thm:six-term-mass-formula-complete`

- `def:habiro-ring`

### `def:localized-hadron`

- `def:categorical-point`

### `def:hadron`

- `def:exceptional-divisor`

### `def:knot-operator-energy`

- `def:hecke-normal-form`

### `prop:graded-trace-residue-split`

- `def:hecke-normal-form`

### `def:stable-atom`

- `def:hecke-normal-form`

### `prop:hadron-unique`

- `def:hadron`

### `prop:gb-residue-spectral-sum`

- `def:hecke-normal-form`

### `prop:universal-braid-branching`

- `rem:conway-normal-form`

### `rem:mass-endomorphism-jet-tower`

- `def:quantum-bloch-group`

### `conj:borromean-quark`

- `def:borromean-baryon`

### `rem:strangelet-witten-stability`

- `def:hadron`

### `prf:terminal-resolution`

- `prop:knot-eigenbasis-complete`

### `conj:color-superconductivity-borromean`

- `conj:borromean-quark`

### `prop:noble-gas-characterization`

- `def:electron-knot`

### `def:stable-nucleus`

- `def:categorical-neutron`

### `rem:torus-knot-prime-powers`

- `def:electron-knot`

### `prop:categorical-neutron-exists`

- `def:categorical-neutron`

### `rem:unmapped-torus-knots`

- `def:categorical-neutron`

### `prop:categorical-neutron-unique`

- `def:categorical-neutron`

### `prop:categorical-proton-unique`

- `def:categorical-proton`

### `def:transfer-matrix-operator`

- `rem:building-block-knots`

### `prop:beta-decay-transfer-matrix`

- `def:beta-decay-skein`

### `prop:parity-violation-skein`

- `rem:hecke-algebra-from-braiding`

### `def:neutrino-knot`

- `sec:knot-notation-convention`

### `rem:knot-formula-table`

- `prop:fermion-boson-knot-link`

### `def:positron-knot`

- `def:electron-knot`

### `rem:algebraic-core-survives`

- `prop:hoefsmit-seminormal-form`

### `rem:calculus-up-to-epsilon`

- `def:substrate-parameter`

### `conj:infinitesimal-frobenius`

- `def:standard-part-functor`

### `conj:infinitesimal-observability`

- `def:standard-part-functor`

### `def:ns-obstruction`

- `rem:hecke-algebra-from-braiding`

### `prop:helicity-conservation`

- `thm:jones-markov-trace`

### `rem:geodesic-vortices`

- `rem:madelung-fluid`

### `prop:universality`

- `prop:euler-char-stability`

### `def:q-navier-stokes`

- `rem:madelung-fluid`

### `prop:q-spectral-sobolev`

- `rem:q-laplacian-interpretation`

### `prop:ns-obstruction-computation`

- `rem:conway-normal-form`

### `prop:horizon-conformal-invariance`

- `def:big-bang-state`

### `rem:penrose-ccc`

- `def:big-bang-state`

### `rem:cmb-photon-color-content`

- `rem:knot-basis-color-content`

### `prop:photon-threading-mass`

- `thm:groebner-shirshov-energy`

### `def:cmb-boundary-datum`

- `def:big-bang-state`

### `prop:qou-is-ccc`

- `def:big-bang-state`

### `def:aeon`

- `def:big-bang-state`

### `rem:jet-planck-steps`

- `prop:fermion-boson-knot-link`

### `rem:knot-atom-diagrams`

- `def:borromean-baryon`

### `tm-knot-pairs`

- `rem:building-block-knots`

### `rem:braiding-unit-circle-convention`

- `def:quantum-observable-universe`

### `prop:spectral-chart-correspondence`

- `def:commutative-qou`

### `rem:geometric-rh-exposition`

- `rem:yekutieli-stokes`

### `rem:glossary-q-bit`

- `prop:skein-generation`

### `rem:particle-nf-table`

- `rem:knot-particle-dictionary`

### `rem:hadron-level-knot-table`

- `rem:knot-particle-dictionary`

### `rem:gluon-model-comparison`

- `conj:borromean-quark`

### `rem:q-flat-connection`

- `prop:categorical-dq-squared`

### `def:typed-garside-element`

- `prop:nuclear-groebner-reduction`

### `prop:atomic-lp-stability`

- `def:borromean-baryon`

### `prop:confinement-sdp`

- `rem:hecke-algebra-from-braiding`

### `conj:lifted-crossing-locality`

- `conj:mass-volume-factorization`

### `ex:chi-minus-six-derivation`

- `def:motivic-substrate`

### `ex:archimedean-yekutieli`

- `def:motivic-substrate`

### `prop:sdp-regime-switch`

- `prop:wigner-2-coefficient`

### `rem:atom-mass-full-hecke`

- `def:transfer-matrix-operator`

### `rem:mass-comparison-table`

- `rem:knot-formula-table`

### `rem:color-confinement-observation`

- `prop:em-coupling-projection`

### `prop:algebraic-gns-embedding`

- `thm:jones-markov-trace`

### `rem:physics-names-knot-operations`

- `prop:force-carrier-bring-uniqueness`

### `rem:electron-immortality`

- `prop:reidemeister-mass-invariance`

### `rem:vacuum-polarization-virtual-pairs`

- `prop:reidemeister-mass-invariance`

### `sim:beta-decay-halflife`

- `def:transfer-matrix-operator`

### `rem:fine-structure-observation`

- `prop:em-coupling-projection`

### `prf:algebraic-gns-embedding`

- `thm:jones-markov-trace`

### `prop:toffoli-lp-stability`

- `def:hecke-mass-element`

### `rem:generating-functions-solve-reeb-flow`

- `def:archimedean-realization-functor`

### `def:q-dilogarithm`

- `prop:tannaka-krein-reconstruction`

### `rem:t211-ideal-annihilation`

- `prop:shell-transition-knot`

### `rem:commutative-crossing-energy`

- `def:crossing-energy`

### `def:motivic-galois-character`

- `def:motivic-substrate`

### `rem:kummer-tower`

- `def:motivic-substrate`

### `prop:y-lambda-cyclotomic-factorization`

- `thm:jones-markov-trace`

### `rem:kashaev-as-archimedean-realization`

- `def:archimedean-realization-functor`

### `rem:vassiliev-filtration-mass-tower`

- `def:knot-operator-energy`

### `prop:rigid-monoidal-structural-gap-invariance`

- `prop:operator-selection-lp`

### `prop:curvature-rank-gb-stratification`

- `prop:gb-spectral-sequence`

### `prop:per-nucleon-shift-additive-linearity`

- `prop:alpha-shift-torus-knot`

### `prop:joint-tower-sdp-confinement`

- `prop:gb-spectral-sequence`

### `rem:vol-as-motivic-period`

- `def:archimedean-realization-functor`

### `prop:mass-tower-coefficient-stratification`

- `prop:plancherel-weight-boundedness`

### `prop:y-lambda-closed-form-wenzl-bridge`

- `prop:wedderburn-weight-canonical`

### `prop:e-infinity-page-identifications`

- `prop:gb-spectral-sequence`

### `prop:y-lambda-recipe-from-partition`

- `thm:jones-markov-trace`

### `prop:confinement-nf-partial-proof`

- `prop:alpha-shift-torus-knot`

### `rem:hecke-markov-interpretation`

- `prop:hoefsmit-seminormal-form`

### `prop:qmn-recursive-memoized`

- `thm:jones-markov-trace`

### `prop:markov-trace-ratio-exact`

- `def:archimedean-realization-functor`

### `prop:wigner-coefficient-derivation`

- `prop:q-integer-mass-formula`

### `cor:commutative-chirality-vanishes`

- `prop:frobenius-s-classification`

### `prop:explicit-alpha-k-h3`

- `prop:unified-curvature-rank-mass-formula`

### `conj:kashaev-volume-conjecture`

- `def:archimedean-realization-functor`

### `rem:two-tier-scaling-pq`

- `prop:reidemeister-mass-invariance`

### `prop:mass-coefficient-shadow-price`

- `prop:wedderburn-weight-canonical`

### `prop:wedderburn-weight-canonical`

- `thm:jones-markov-trace`

### `prop:six-term-per-derivation-weights`

- `prop:binding-scale-catalan`

### `prop:knot-factor-spectral-form`

- `prop:unified-curvature-rank-mass-formula`

### `prop:alpha-shift-torus-knot`

- `def:delta-q-decoration`

### `prop:sigma-shell-from-beta-chain-derivation`

- `prop:atomic-mass-gb-nf`

### `def:adelic-substrate`

- `def:motivic-substrate`

### `prop:force-carrier-intertwining-correspondence`

- `def:delta-q-decoration`

### `def:two-row-stratum`

- `thm:jones-markov-trace`

### `thm:knot-mass-formula-unified`

- `prop:atomic-mass-gb-nf`

### `prop:hook-weight-derivation`

- `prop:wedderburn-weight-canonical`

### `thm:markov-trace-factorization`

- `thm:markov-trace-product`

### `prop:spin-involution-lp-dual-invariance`

- `prop:antiparticle-crossing-reversal`

### `prop:demazure-fiber-markov-trace`

- `thm:jones-markov-trace`

### `def:phi-q-piece`

- `thm:jones-markov-trace`

### `prop:wenzl-bridge-applicability-qou`

- `thm:jones-markov-trace`

### `prop:knot-operator-lp-selection`

- `prop:operator-selection-lp`

### `prop:wenzl-qmn-synergy`

- `thm:jones-markov-trace`

### `rem:isospin-mass-split-em-localisation`

- `def:coulomb-charge`

### `prf:atom-knot-mass-derivation`

- `thm:jones-markov-trace`

### `prop:explicit-central-idempotent`

- `prop:wedderburn-weight-canonical`

### `prop:hecke-baer-star-generic`

- `prop:wedderburn-weight-canonical`

### `prop:shell-structure-eigenvalues`

- `rem:hydrogen-orbitals`

### `prop:em-coupling-projection`

- `prop:force-carrier-bring-uniqueness`

### `prop:quantum-dilogarithm-volume`

- `cor:quantum-dilogarithm`

### `prop:tau-leptonic-universality`

- `rem:force-knot-identification`

### `rem:em-completeness-interpretation`

- `prop:em-coupling-projection`

### `prop:knot-operator-selection`

- `def:breit-wheeler-pair-production`

### `rem:beta-decay-interpretation`

- `prop:beta-decay-transfer-matrix`

### `rem:ontological-agnosticism`

- `def:exceptional-divisor`

### `rem:energy-scale-planck`

- `rem:calibration-inputs`

### `rem:confinement-nucleon-unit`

- `def:transfer-matrix-operator`

