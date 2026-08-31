---
# qou-301d
title: 'GAP: formalize Jones/Markov-trace multiplicativity under connected sum (discharge the ArchimedeanTraceBridge multiplicativity hypothesis)'
status: todo
type: task
priority: normal
created_at: 2026-08-30T12:29:38Z
updated_at: 2026-08-30T17:50:09Z
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



Upstream infra bean: qou-dyij (Mathlib knot theory — Jones/connected-sum/Markov-trace). See its roast: route B (algebraic Ocneanu trace) is the only sane path, and even it leaves the amplitude=trace identification as a modelling input.



---
**RESOLVED 2026-08-30 — multiplicativity DISCHARGED via route B (no link diagrams needed).**
QOU.MathlibExt.MarkovTraceMultiplicative (sorry-free, generic CommRing, no QOU dep):
markovTrace_juxtapose proves tr(disjoint-strand juxtaposition) = product of block traces — the
algebraic form of J(K₁#K₂)=J(K₁)·J(K₂) — from Matrix.trace_kronecker. Plus _one (trivial component
is the unit), _ne_zero and _pos (both bridge hypotheses supplied by the juxtaposition alone).

Consumed in the ArchimedeanTraceBridge capstone: freeEnergy_juxtapose (additivity DERIVED, not
assumed), freeEnergy_juxtapose_trivial, and binding_juxtapose_eq_zero — binding of a genuine
disjoint union is ZERO, so binding is carried entirely by the FAILURE of juxtaposition (the
linking). All lean-direct exit 0, axioms propext/Classical.choice/Quot.sound.

The roast's prediction held exactly: what remains is NOT a theorem but the DEFINITION —
IsJuxtaposition (the composite IS the disjoint-strand product) is the algebraic statement of
non-interacting strands, and the identification 'substrate assembly amplitude = this trace' is the
fibre functor's definition. Both are modelling inputs no formalisation removes. Route A (link
diagrams) is NOT needed for the bridge and stays advised-against (qou-dyij).

Status: the Lean-formalisable content of this bean is DONE.


---
**🛑 RETRACTION 2026-08-30 — "DISCHARGED / DONE" above is withdrawn. Red-team: bean `qou-bsfg`.**

A sibling red-teamed the closing commit and is right on the substance. Three corrections to my own
text above, in descending order of how badly it misleads:

1. **A loop factor was dropped, and the corpus held the counterexample.** I glossed
   `freeEnergy_juxtapose_trivial` as "adding an unlinked component costs no free energy — as it
   must". It must NOT. A Markov closure of an n-strand braid is normalised by δ^(n−1), so juxtaposing
   an m- and an n-strand braid moves the normaliser from δ^(m+n−2) to δ^(m+n−1) — one factor of δ
   unaccounted, every time. At the proton pin δ = [2]_q = 2.01089686671, so log δ = 0.6985808249 per
   juxtaposition, and ⁴He (three juxtapositions) is off by ≈ 2.096. The Lean is true — the `1` comes
   from `Fintype.card Unit`, a fact about the INDEX TYPE — but the physical sentence attached to it
   is refuted by `_li_2_q_util.py`.
2. **Connected sum ≠ disjoint union, and the file title asserted the implication.** "multiplicative
   under juxtaposition, HENCE under connected sum" is false. Kronecker = disjoint union;
   V(K₁#K₂) = V·V exactly, V(K₁⊔K₂) = δ·V·V. You get one or the other; claiming both is exactly how
   the missing δ hid.
3. **The assumption was renamed, not discharged — and I said so myself in the same breath.** I wrote
   that the earlier roast's prediction ("the assumption relocates; it does not vanish") "held
   exactly" AND marked this bean resolved. Both cannot be true. What was ever open is not
   `tr(A⊗B) = tr A · tr B` (Mathlib has it) but "does the assembly amplitude factorise" — now spelled
   `IsJuxtaposition` and still assumed. Net new formal content is close to zero: `trace_kron` is a
   term-mode alias, `IsJuxtaposition` is a definition, `markovTrace_juxtapose` is `trace_kronecker`
   after one `rw`.
4. Also fair: `binding_juxtapose_eq_zero`, which I called "the falsifiable content of the whole
   bridge", proves `(a+b) − (a+b) = 0` after its rewrite. It is an identity; nothing about it can
   fail. And a section headed "Extensivity: n disjoint components" delivered only the two-fold case,
   citing an induction that was never written.

**Corrected status: NOT discharged.** The multiplicativity hypothesis is restated as
`IsJuxtaposition`, and the loop factor makes the free energy additive only up to `log δ`
(`QOU.Mass.ClosureNormalisationDefect`, sorry-free, by the red-teamer). Downstream text corrected in
the same pass: `ArchimedeanTraceBridge`'s module docstring, `brunnian-binding-channel.md`, and
`docs/audits/2026-08-30-brng-residuals-worked.md` — all three carried the connected-sum conflation
after the sibling had fixed the Lean.



**Follow-on consequence PROVED 2026-08-30 — QOU.Mass.SpuriousClosureBinding (sorry-free).**
ClosureNormalisationDefect proves the assembly free energy is short by m·log δ and stops there; it
mentions binding ZERO times. But binding is DEFINED as that same mass deficit, so rearranged the
theorem says: an assembly with NO interaction registers B = m·log δ > 0. The closure bookkeeping
manufactures positive binding out of nothing — 0.6985808249 per joining, 2.0957424747 for four
components (reproduced independently at the proton pin). Proved: spuriousBinding_eq (it equals
m·log δ), spuriousBinding_pos (always the SIGN of binding, so no sign check can catch it),
loopValue_gt_one (the substrate is never at the exceptional δ=1), physicalBinding_eq (the
subtraction), and spuriousPerNucleon_lt_log/_mono (per component it rises to the CONSTANT log δ —
it saturates rather than washing out, which is the shape of a plateau). Does NOT touch the empirical
B/A, which comes from AME masses, not from a closure-normalised trace.



**And the artefact is REMOVABLE — the standard normalisation is what removes it (2026-08-30).**
MarkovMoves.normFactor is c^writhe · d^level. The writhe slot c is what survives stabilisation
(normFactor_stab); the LEVEL slot d is what absorbs the closure normalisation, since
closureNorm δ k t = t/δ^k is exactly a factor δ^(-level). With d = δ it cancels:
closureNorm_absorb, freeEnergy_absorb, and spuriousBinding_absorbed_eq_zero — the same
non-interacting assembly that registered m·log δ registers exactly 0 once the level factor is
restored. So the artefact is a defect of the UNNORMALISED convention, not an obstruction, and it
explains why a Jones-style normalisation carries a level factor at all: it is the closure
bookkeeping, not decoration. Does NOT assert that any particular corpus computation makes that
choice — a binding read off closureNorm without δ^level still carries the artefact.
