# N2 pre-registration: are the neutron and proton DISTINCT gamma-gamma-selected elements?

Bean `qou-99qc` (Q_beta derived, not chosen) and `qou-ales` (gamma-gamma + reading-3 word
selection). Owner 2026-11-20 ~19:25: replace the typed-crossing definition
`Delta_S = B_n - B_p` by a DERIVED difference of two gamma-gamma-selected nucleon elements.
Written 2026-11-20 BEFORE any number in this directory was computed. Nothing below has
been evaluated at q_0 when this file is committed.

## What "the selection" is (fixed here, not tuned later)

* Candidate words: `GammaGammaWord` (`QOU.Mass.GammaGammaWordSelection`): left-to-right
  products of vertices `V_i = sigma_i sigma_{i+1}^{-1}`. Cost = number of crossings.
  Budget k <= 5 vertices (the 11-crossing nucleon budget, bean qou-1qsw), as in #8564.
* Reading 3 (owner 2026-09-12, scope whole word 2026-09-13): Frobenius positivity,
  `chi_lambda(w) >= 0` on every block with `y_lambda > 0`, convention D.
* Selected element: the minimal NON-ZERO-cost feasible word (owner 2026-08-30 H_2
  precedent); the literal minimum (identity) is also reported.

## Where a nucleon label could enter

The ruled reading 3 takes no state argument: its inputs are the word, `chi_lambda` and
`y_lambda`. A state can enter only if the selection is made STATE-WEIGHTED. The one
extension tested here (named choice **S-w**): replace "every block with y_lambda > 0" by
"every H_3-isotypic component of the nucleon's own state space s, with y_lambda > 0",
i.e. `tr(Pi_s^lambda rho(w)) >= 0`, where `rho` is the Jimbo R-matrix action on
`V^{tensor n}`, `V = K^2 = span(u, d)`, and `Pi_s^lambda` projects onto the lambda-isotypic
part of `s` under strands 1-3.

Two state models:

* **M3 (three strands).** `s = W_n` (one u) or `W_p` (two u), basis as
  `IsospinRaisingRoundTrip.lean` (#8632).
* **M4 (four strands, lepton strand, named choice C-lep).** Strand 4 is a lepton doublet
  line with the same `V` (nu = u-type, e = d-type). The T3 = 0 weight space of `V^{tensor 4}`
  (6-dim) splits as `N = n (x) nu` (strand 4 = u) and `P = p (x) e` (strand 4 = d). Both are
  H_3-modules; `sigma_3` (strand 3-4) maps between them, so `<P| X |N>` is a
  charge-conserving Hecke matrix element (crossed beta decay `n nu -> p e`, no T+ needed).

## Predictions (priors, stated before computing)

* **P1 (definitional).** Ruled reading 3 selects the same element for n and p: it has no
  nucleon argument.
* **P2 (scope b, M3 and the H_3 words of M4).** S-w on H_3 words selects the same element
  for n and p, because `rho_n = Delta rho_p Delta^{-1}` (#8616 `rho_n_eq_conj`) and the
  isotypic projectors are polynomials in the central full twist, hence conjugated too.
  To be proved in Lean as an abstract statement: any selection predicate built from
  traces of `Pi^lambda rho(w)` is invariant under simultaneous conjugation.
* **P3 (M4, words touching strand 4).** Compressions to N and P differ for words containing
  `sigma_3`. Prior (low confidence, ~60 %): the minimal non-zero feasible element is
  nevertheless the SAME for n and p, because a 3-strand vertex power is already feasible at
  or below the length at which a strand-4 word first differs. If they do differ, the
  difference is reported, not chosen between.
* **P4.** Whatever comes out, the difference of H_3-word compressions has zero content on
  every H_3 block (follows from P2); so a nonzero isospin-1/2 Delta can only come from
  strand-4 letters.

## What is reported in every case

1. Feasibility table per word, per state, per block (exact in Q(q); sign at proton q_0,
   70 dps).
2. Selected element(s) for n and p (or "identical").
3. If distinct: isotypic content of the difference on N (identified with W_n by the basis
   `uddu, dudu, dduu -> udd, dud, ddu`), label-C value
   `eps_C(X) = tr(T- T+ X)/tr(T- T+)` and its isospin-1/2 part (#8632), and the R1
   closed form `Q_beta/m_e = (q+1)(q^2+1)/(2q^3) * y3` with `y3 = eps_C` (#8623), order-zero
   `E_0 = m_e/(q(q-1))`. CODATA appears only in a final comparison row.
4. The M4 process amplitude `<P| rho(w) |N>` for the selected word(s), exact in q, with its
   order of vanishing as q -> 1 (requested by the coordinator for N1/N3).

## Named choices (none is selected against data)

S-w (state-weighted positivity), C-lep (strand 4 = lepton doublet), the identification
N ~ W_n by basis order, E_0 (posited, bean qou-mkm8).
