# Sidecar re-triage: mass-theory (2026-11-21)

Part of umbrella issue #8766. This pass wrote 170 verdict entries:
- 158 stale entries: 129 re-stamps and 29 full reviews.
- 12 blocks that had never been genuinely reviewed, or held only unhashed heuristic entries: all 12 got full reviews.
- 1 correction entry (`pieri-photon-shift`, where a shell-quoting slip truncated the first entry's evidence).

The work was split into five parts reviewed in parallel. Each part's table is below. "stmt" means `proof-narrative-lean-equiv` and "proof" means `da-non-sequitur`.

Census after the pass: 143/143 statement blocks fresh. Proof blocks: 140/143 show fresh. The other 3 (`feynman-categorical-trace-proof`, `q-bessel-second-order-qdifference`, `jackson-q-bessel-contiguity`) are proof blocks that carry a `lean.ref`. The writer hashes that Lean, but the temporary census script does not resolve Lean for proof blocks, so it reports a hash mismatch. All three got entries today. This is a census-script artifact, not a stale verdict.

## Part 1

Part 1: 37 items, 30 re-stamps, 7 full reviews (2 pass, 3 warn, 2 fail).

| block | criterion | old → new | reason |
|---|---|---|---|
| knot-operator-lp-selection | stmt | fail->pass | LP rewritten as minimisation with G+S constraint (Moore-Penrose); optimality and complementary slackness proved; residue: G, S, t free fields, not tied to tr_M |
| tau-M-asymptotic-rep-theory | stmt | fail->fail major | md fixed; Lean only returns class fields; docstring calls c2=-1 "proved" |
| unstable-atom-decay-channel-proof | proof | fail->fail major | scope note admits x=0 triviality; body still claims unique vertex of a cone with no objective |
| unit-modulus-eigenvalue-proof | proof | pass->warn major | NEW false sentence chi_(2,1)(beta_Bor)=2-h^4 (correct 2-3h^4-h^6); "complex-conjugate" contradicted at q=2 |
| binding-genfun-qdifference | stmt | warn->warn minor | coefficient form derived; item 2 not encoded |
| feynman-categorical-trace-proof | proof | warn->warn minor | dim(S_lambda) factor fixed; Lean still definitional |
| rho-k-h3a-refinement | stmt | pass->pass | derived from balance premise; md:29 leftover "conditional" |

Rulings: none.

## Part 2

Part 2: 40 items, 31 re-stamps, 9 full reviews (0 pass, 4 warn, 5 fail).

| block | criterion | old → new | reason |
|---|---|---|---|
| crystal-r-matrix-sub-lemma | stmt | fail->warn minor | self-assuming class gone; factorisations proved; pole-order indicator not encoded; Wenzl=Hoefsmit cited |
| binding-closure-conditional | stmt | fail->warn major | (C),(B) now hypotheses; generic factor-out; residue form/growth law not encoded; md:37 novelty overclaim |
| operator-selection-lp-proof | proof | fail->warn minor | dual fixed; t>=0 "for generic q" unproved; box multipliers missing |
| wedderburn-mass-formula | stmt | fail->fail major | ref is def atomicMass; decide lookups; "zero fitted parameters" vs free m_p, m_n; absolute mass (excised 2026-08-11) |
| rho-k-graded-expansion | stmt | fail->fail major | class field lifted to theorem; alpha fit inside proposition; absolute mass |
| flavor-split-substrate-proof | proof | fail->fail major | convention C, fitted ansatz, CODATA step 7 at muon pin; "no calibration" claim |
| content-genfun-palindromic | stmt | fail->fail major | ref proves n=4 only; md claims general n proved |
| pair-skein-mass-formula-proof | proof | fail->fail major | double-Skein step uncomputed; denominator convention C; mu_a undefined |
| frobenius-codim-universal | stmt | warn->warn minor | new block-model claims proved in CoCasimirSurvivingBlocks.lean; retarget ref to tr_coCasimirSurv_of_forall_ne_zero |

Rulings: no-fitting/empirical-in-proof (rho-k-graded-expansion, flavor-split-substrate-proof, wedderburn-mass-formula); absolute-mass excision (wedderburn-mass-formula, rho-k-graded-expansion); proton-pin default (flavor-split-substrate-proof).

## Part 3

Part 3: 40 items, 32 re-stamps, 8 full reviews (2 fail, 6 warn).

| block | criterion | old → new | reason |
|---|---|---|---|
| mass-endomorphism-tower | stmt | fail->fail major | pairSum now covers i<j; formula is only def massPoly; ref proves positivity not stated in md; z^2 pair weight not derived |
| residue-at-root-proof | proof | fail->warn minor | Habiro membership now a hypothesis, pi_n ring hom built; n_l undefined, primitive-root condition missing |
| pieri-photon-shift | stmt | fail->fail major | md uses ruled photon; ref still self-assuming class projection; Lean "removal" vs md two additions |
| confinement-sdp-proof | proof | warn->warn minor | false sorry claim removed; Slater point not exhibited |
| degree-one-braid-trivial-volume | stmt | warn->warn minor | photon paragraph correct; Vol=0 not encoded |
| degree-one-braid-trivial-volume-proof | proof | pass->warn minor | proof never treats vertex word s0 s1^-1; cites a conjecture |
| confinement-categorical-proof | proof | pass->warn minor | HH0 conflation; trace unspecified; post-QED numerology |
| topological-mass-formula-algebraic | stmt | warn->warn minor | new Vol!=0 hypothesis not in Lean; class takes formula as hypothesis |

Rulings: none found. Note: mass-endomorphism-tower.lean docstring carries empirical-refutation wording (comment only).

## Part 4

Part 4: 41 items, 36 re-stamps, 5 full reviews (0 pass, 4 warn, 1 fail).

| block | criterion | old → new | reason |
|---|---|---|---|
| residue-at-root | stmt | fail->warn minor | Habiro completion and projection built in QHabiroCompletion.lean; residue_at_root is rfl; Phi_q, tr_{M,l}, n_l absent |
| pieri-photon-shift-proof | proof | pass->warn minor | ruled photon; b=n step one asserted sentence; a>=n untreated |
| binding-closure-conditional-proof | proof | warn->warn minor | conditionality aligned; finiteness unstated; pole set equated with an unsettled S_c^hyp |
| q-beta-c-k-recursion-from-habiro-q-difference | stmt | fail->fail major | CKRecursion asserts nothing; parity premise false ((q-1)mu not bar-odd) |
| feynman-markov-identification-proof | proof | fail->warn minor | sigma^-1 rule and weight fixed; z unfixed; weight asserted |

Rulings: no-fitting/empirical premises persist in re-stamped meson-kaon-pion-hecke-seifert-proof, derived-mass-formula-light-isotopes-proof, mass-tower-coefficient-stratification-proof, unified-iterative-correction (AME2020 in statement). Possible conflict: skein-polynomial-transfer-matrix (stmt+proof) now calls convention C "alternative" rather than excised.

## Part 5 (never genuinely reviewed)

12 full reviews: 2 pass, 4 warn, 6 fail.

| block | criterion | result | reason |
|---|---|---|---|
| y-lambda-closed-form-wenzl-bridge | stmt | fail major | main theorem equates two definitions of the same Wenzl ratio; no Markov trace appears |
| archimedean-functor-uniqueness | stmt | fail major | ref is the real-slice class projection, whose hypotheses force tau_arch = 0; repoint to `archimedean_functor_uniqueness_complex` |
| markov-trace-frobenius-selection | stmt | warn major | n=3 selection genuinely derived; the whole-tower uniqueness, radical = TL ideal, and general-n parts are not encoded |
| delta-lambda-dt-index-unification | stmt | warn major | chirality leg proved for general n; value leg is a tautology (d is never tied to dim V_λ) |
| piece-a-corner-removal-obligation-proof | proof | pass | steps L1–L6 checked |
| phi-q-tower-algebraic-stratification-proof | proof | fail major | Step 3 rests on a remark; Step 2 is unargued; J-filtration grading is not addressed |
| mass-coefficient-shadow-price-proof | proof | fail major | uses Plancherel weights where Markov weights belong; dual not derived; SEMF term shapes imported |
| markov-trace-frobenius-selection-proof | proof | warn minor | general-n closed form rests on a numerical check up to n ≤ 7 |
| feynman-categorical-trace-proof | proof | warn minor | statement drops the absolute value; result holds under convention D only |
| q-bessel-second-order-qdifference | proof | pass | every step verified; matches the Lean |
| jackson-q-bessel-contiguity | proof | fail major | no argument given; the cited Lean assumes the recurrence |
| habiro-expansion-atomic-proof | proof | fail major | expands D(u)·tr_M, not Vol_alg; degree arithmetic is wrong; uses convention-C z |

## Ruling check summary

- **Photon, electron, up quark, T(2,n_s):** no conflicts in mass-theory. `pieri-photon-shift` and `degree-one-braid-trivial-volume` use the ruled photon form.
- **No fitting, and no empirical data in proofs:**
  - `rho-k-graded-expansion` (α fit inside the proposition)
  - `flavor-split-substrate-proof` (fitted ansatz; CODATA at the muon pin)
  - `wedderburn-mass-formula` (m_p and m_n are free inputs)
  - `meson-kaon-pion-hecke-seifert-proof` (290 ppm scan against data)
  - `derived-mass-formula-light-isotopes-proof` and `mass-tower-coefficient-stratification-proof` (CODATA muon pin)
  - `unified-iterative-correction` (AME2020 figure in the statement)
- **Absolute mass excised (2026-08-11):** `wedderburn-mass-formula` and `rho-k-graded-expansion` still target Z·m_p + N·m_n.
- **Convention D canonical:**
  - `habiro-expansion-atomic-proof` uses convention-C z.
  - The two `skein-polynomial-transfer-matrix` blocks now call convention C "alternative" instead of "excised". That was re-stamped as a wording change, but it may conflict with the ruling.
- **New error introduced by a recent diff:** `unit-modulus-eigenvalue-proof` states χ_(2,1)(β_Bor) = 2 − h⁴. The correct value is 2 − 3h⁴ − h⁶, checked with sympy. The same sentence calls the eigenvalues complex-conjugate, but they are real at q = 2.
