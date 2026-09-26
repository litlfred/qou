---
# fwr3
title: '40 forward-ref defects are adjacent-block transpositions'
status: completed
type: task
priority: normal
created_at: 2026-08-09T21:35:00Z
updated_at: 2026-08-09T23:10:00Z
parent: fwr1
---
Forty of the 236 surviving forward references point at a block within two
manifest positions. These are inversions, not structural problems — a lemma
before the definition it uses, an interpretation before the result it
interprets. Each is a swap.

Clearest of them: `lem:staircase-corner-hook` (757) needs `def:staircase-partition`
(759); `def:quantum-temperature` (110) needs `def:quantum-entropy` (111);
`rem:operational-entropy-properties` (24) needs the self-consistency remark at 25.

Swapping changes chapter order, so re-run the `detangler` axis afterwards rather
than assuming each swap is independent — several of these are neighbours of each
other.

Full list (chapter: source (pos) ↔ target (pos)):

- appendix-surreals-archimedean: rem:st-is-median-resummation (7) ↔ def:standard-part-functor (8)
- braids-and-knots: prf:hecke-satisfies-blitvic-hypothesis (14) ↔ prop:trace-locality-meets-gs-non-locality (16)
- information-theory: rem:operational-entropy-properties (24) ↔ rem:operational-entropy-self-consistency (25)
- information-theory: rem:reeb-turing-completeness (80) ↔ def:computational-horizon (82)
- information-theory: def:quantum-temperature (110) ↔ def:quantum-entropy (111)
- knots-particles-confinement: rem:quark-antiquark-production-reduction (6) ↔ prop:four-term-pair-nucleon (7)
- knots-particles-confinement: conj:electroweak-higgs-torus-link-triplet (88) ↔ thm:ew-triplet-charge-spin-from-involution (89)
- lifting-and-descent: rem:prolongation-categorical (6) ↔ def:recursive-brane-tower (7)
- lifting-and-descent: rem:hochschild-kummer-connection (49) ↔ def:motivic-substrate (50)
- mass-endomorphism: rem:atomic-mass-gb-nf-interpretation (56) ↔ prop:rho-k-graded-expansion (57)
- mass-endomorphism: rem:categorical-neutrality-saturated-shells-interpretation (83) ↔ rem:phi-n-global-section (84)
- mass-theory: rem:two-tier-scaling-pq (23) ↔ prop:three-calibration-inputs (24)
- mass-theory: rem:three-calibration-inputs-context (26) ↔ prop:three-parameters-wedderburn (27)
- mass-theory: prf:skein-generation (74) ↔ lem:skein-mass-from-linking (75)
- mass-theory: prop:lusztig-vs-hermitian-bar (110) ↔ prop:q-zero-complex-extension (112)
- mass-theory: rem:markov-chain-fluctuations (283) ↔ prop:q-gaussian-obstruction-at-q0 (284)
- mass-theory: rem:feynman-qou-dictionary (295) ↔ prop:feynman-classical-limit (297)
- mass-theory: rem:qz-bicompletion-properties (308) ↔ prop:quantum-dilogarithm-stratified (309)
- mass-theory: conj:pachner-pentagon-borromean (315) ↔ prop:q-rogers-pentagon-archimedean (316)
- mass-theory: conj:mass-volume-factorization (354) ↔ rem:frobenius-packing-density (355)
- mass-theory: conj:phi-q-wkb-greens-function (386) ↔ conj:algebraic-geometric-dilog-equivalence (387)
- mass-theory: prop:explicit-alpha-k-h4 (645) ↔ prop:wedderburn-bratteli-recursion (647)
- mass-theory: lem:staircase-corner-hook (757) ↔ def:staircase-partition (759)
- models-of-qous: rem:witt-lift-qou (47) ↔ ex:finite-field-realisation (49)
- nuclear-interactions: prop:confinement-lp (18) ↔ prop:confinement-operator-selection (20)
- nuclear-interactions: rem:hyperelliptic-z5-classification-interpretation (136) ↔ rem:bring-z5-descent (137)
- nuclear-interactions: rem:weight-identification-consequences (139) ↔ rem:u1-phase-tube (140)
- predicted-spectra: rem:alpha-em-derivation-open-problems (69) ↔ prop:em-coupling-bring-zero-mode (70)
- predicted-spectra: prop:em-coupling-fixed-point (71) ↔ prop:photon-ir-zero-mode-bring (73)
- predicted-spectra: rem:em-coupling-fixed-point-derivation-status (72) ↔ prop:photon-ir-zero-mode-bring (73)
- predicted-spectra: rem:nf-computation-strategy (181) ↔ rem:kummer-shell-closure (182)
- predicted-spectra: def:inter-shell-operator (209) ↔ def:chebyshev-torus-coefficients (210)
- predicted-spectra: rem:rj-inner-product-interpretation (227) ↔ cor:spectral-decomposition-qvalue (228)
- quantum-observable-universes: rem:braiding-eigenvalue-extraction-novelty (80) ↔ prop:tannaka-krein-reconstruction (82)
- quantum-observable-universes: rem:reeb-flow-bridge (108) ↔ def:brings-coordinate-ring (110)
- quantum-observable-universes: rem:laplace-fourier-wick-rotation (239) ↔ def:q-exponential (241)
- quantum-universes: ex:frobenius-pairing-su2 (18) ↔ ex:quantum-universe-su2 (20)
- stochastic-mechanics: rem:markov-closure-map-axiomatic (19) ↔ rem:F3-eps6-leading-eq-neg-2b-cubed (20)
- stochastic-mechanics: rem:classical-limit-topology-free (27) ↔ def:classical-limit-obstruction (29)
- stochastic-mechanics: rem:qou-obstruction-millennium-specializations (34) ↔ tbl:qou-obstruction-reduction-table4-data (35)

---

**Outcome: 24 within-section moves applied; forward references 236 → 211.**

Done as a constrained search over within-section orderings, scored by the exact
`detangler-no-forward-ref` rule, with three rounds of narrative review as the
gate. The raw metric wanted far more: an unconstrained search claimed −66, and
review found **18 of its 53 moves made the paper worse**. That pass was reverted
whole. The sequence of honest numbers is −66 → −52 (guards derived from the
data) → −36 (round-one vetoes) → **−25, three-times reviewed, zero bad.**

Guards the search now respects, each traceable to a specific failure:

| guard | what it prevents |
|---|---|
| section opener + `meta.position: "opening"` pinned | a block landing above the framing prose it presupposes |
| a block may not precede one it `interprets` (1027 declare it) | splitting a narrative pair whose slugs share no prefix |
| forward refs over inline `(#label)` **and** backticked `kind:slug` prose may not rise | stranding a block from a dependency `uses[]` never declared |
| a unit headed by a descendant of a block in the section is pinned | an already-detached `-proof` wandering further from its proposition |
| comments never move; the entry beneath one is pinned | a note re-attaching to a block it was not written about |
| families atomic (`X`, `X-proof`, `X-interpretation`, `X-tableN-data`) | a proposition separated from its proof |

What no guard sees, and why this needed readers: section intros that narrate
order ("**First** … **Second** …", hand-numbered arcs, "**Finally**, …"), bare
anaphora ("**These axioms** carry…"), definite articles pointing above ("**the**
terminal Skein resolution"), and a block closing by announcing the next. Those
28 verdicts are recorded per block with their reason in
`.beans/fwr3-immovable-blocks.txt`, so a rerun does not rediscover them.

Verified: the in-memory model and the real checker agree exactly; slug multisets
per manifest unchanged; comments byte-identical; graph acyclic; `run-validate`
✓ Valid on the same 5 pre-existing issues.
