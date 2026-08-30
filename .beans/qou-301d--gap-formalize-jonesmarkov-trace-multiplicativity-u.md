---
# qou-301d
title: 'GAP: formalize Jones/Markov-trace multiplicativity under connected sum (discharge the ArchimedeanTraceBridge multiplicativity hypothesis)'
status: todo
type: task
priority: normal
created_at: 2026-08-30T12:29:38Z
updated_at: 2026-08-30T12:30:19Z
---

## Context
`QOU.Mass.ArchimedeanTraceBridge` (bean qou-brng, R2 lift) proves: IF the categorical assembly
amplitude is multiplicative — assembly = (∏ Tᵢ)·I with each factor positive — THEN the observable
free energy E=log T is additive and binding = −log I (the connected free energy). Two hypotheses:
- POSITIVITY (0<T): DISCHARGED (2026-08-30) via qIntR_pos — quantum integers are positive at q>1,
  so it is not a genuine assumption for the framework's amplitude class.
- MULTIPLICATIVITY (assembly amplitude factorises): STILL A HYPOTHESIS. This bean.

The mathematical fact is standard and citable — NO NEW LITERATURE NEEDED:
- Jones polynomial multiplicative under connected sum: J(K₁#K₂)=J(K₁)·J(K₂) [Jones 1987].
- Markov trace tower/multiplicativity: Kassel–Turaev "Braid Groups"; Goodman–de la Harpe–Jones.
The gap is purely LEAN FORMALISATION labour, not open math.

## Attack options
1. **Full geometric Jones formalisation.** Model links (or braids+closure), connected sum, the
   Kauffman bracket / Markov trace, prove J(K₁#K₂)=J(K₁)·J(K₂). Mathlib has ESSENTIALLY NO knot
   theory (no Jones polynomial, no connected sum, no Markov trace — only the repo's BraidGroup +
   exponentSum). Research-grade; months; the "keystone hard-Mathlib-gap infra" epic (qou-08a2).
2. **Algebraic Markov-trace-functional route.** Skip geometry: formalise the Markov trace as a
   functional on the Hecke tower with its defining multiplicativity under the tower product
   (tr(a⊗b)=tr(a)tr(b)) and prove the connected-sum image is that product. Smaller than (1) but
   still needs the Markov trace formalised as a functional with the tower property — the repo has
   BorromeanMarkovTrace (a specific closed form) but not the general multiplicative functional.
3. **Abstract MonoidHom + cite (DONE, in effect).** Prove the bridge for any multiplicative positive
   amplitude (done) and CITE Jones for the instance. This is the current state: the hypothesis is
   the citation boundary.

## ROAST (red-team — is it worth it?)
- **Payoff is hygiene, not physics.** Discharging this turns ONE cited-theorem hypothesis into a
  proved one. It adds no new prediction and closes no open physics. qou-brng is already "fully
  derived modulo declared calibrations."
- **Part of it is IRREDUCIBLE — a definition, not a theorem.** Even a complete Jones formalisation
  would not fully discharge the hypothesis, because the step "the SUBSTRATE assembly amplitude IS
  the Jones/Markov trace" is a MODELLING IDENTIFICATION (the fibre functor τ's definition), not a
  lemma. Formalising Jones proves J is multiplicative; it does not prove the mass amplitude is J.
  So the best achievable is: replace "assume multiplicative" with "assume amplitude = Jones trace"
  + "Jones is multiplicative (proved)". The assumption moves, it does not vanish.
- **Amplitude mismatch.** The mass self-carrier is lw = (Σ_{λ⊢c+1} dim_q λ)/(c+1), a SUM of q-dims,
  not the full Jones polynomial (a product-multiplicative object). The multiplicative object is J;
  the interaction factor I is the linking deviation J(linked)/∏J. Proving J multiplicative is the
  UNLINKED reference; the physics (binding) lives entirely in I≠1, which is the linking, not the
  multiplicativity. So the hypothesis being discharged is about the reference, not the binding.
- **Cost/benefit: LOW priority.** A months-long formalisation to convert a standard citation into a
  Lean proof, whose hardest half is a definitional identification that stays an input regardless.
  Recommend: leave as the citation boundary; pursue only as part of the qou-08a2 keystone epic IF
  the general Hecke Markov-trace functional is being built for other reasons anyway.

## Verdict
Positivity discharged. Multiplicativity is a large Lean-formalisation gap (option 1/2, ~epic
qou-08a2), NOT open math (Jones 1987 suffices), and is PARTLY irreducible (the amplitude=trace
identification is a definition). Low priority; the honest state is "modulo the Jones citation."
