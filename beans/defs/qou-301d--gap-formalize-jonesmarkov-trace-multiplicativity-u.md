---
# qou-301d
title: 'GAP: formalize Jones/Markov-trace multiplicativity under connected sum (discharge the ArchimedeanTraceBridge multiplicativity hypothesis)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T12:29:38Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-v2om
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


2026-09-07 (PR #7067): the gap is RE-LOCATED, and one of its two stated halves was never a gap.

1. TwoSidedMarkov is a THEOREM of MarkovTrace, not an axiom beyond it. Four lines: cyclicity moves
   y to the front, it merges with x inside H n (a Subalgebra, hence closed under multiplication),
   and T3 applies to y*x. Global instance registered, so every [TwoSidedMarkov T] theorem in
   DisjointBlockTraceLaw is UNCONDITIONAL (verified by elaborating three of them with no binder).
   The file's claim to have "isolated the gap to one axiom" was wrong -- that axiom was free.

2. THE REAL OBSTRUCTION IS REPETITION, NOT DESCENT. For a word w in generators at levels >= n with
   maximal level M: if g M occurs AT MOST ONCE, cyclicity rotates it to the right end, every other
   letter then has level < M so lies in H M, and T3 peels it; induction finishes. The blocker is a
   word of shape g M * x * g M with x below M -- no rotation puts one g M at the end while leaving
   the other in H M.

   Proved instances: tr_mul_gen_gen_lt / tr_mul_gen_gen_gt (two distinct levels, BOTH orderings --
   so descent alone is fine), and tr_mul_adjoin_gen (the whole subalgebra adjoin{g n}, not just
   powers; it escapes only because that subalgebra is 2-dimensional under the quadratic relation,
   so the induction terminates before repetition bites).

3. WHAT THE GAP ACTUALLY NEEDS, corrected. Not another trace axiom and not E_n alone: a STRUCTURE
   THEOREM FOR THE TOWER, H(m+1) = H m + H m . g m . H m, which is what rewrites g m x g m back
   down. That is a statement about the ALGEBRA, not the trace, and nothing in MarkovTrace implies
   it. (E_n is still the classical packaging, but its content is the independence fact
   E_n b = tr b . 1 on shifted n, not the stabilisation.)

4. THE PRODUCTION WORD IS ON THE WRONG SIDE OF THE LINE. Measured: one nucleon's generator sequence
   under qou-hu1f is [0,1,0,1,0,1,0,0,1,0,0] -- maximal level 1 occurs FOUR times, level 0 seven
   times. So the rotation argument does not cover the atom word at all. The same interleaving that
   killed the monotone theorem also puts the word past this route's reach. Bond product stays
   MEASURED, not derived.

NOT ACHIEVED: no counterexample. I tried to build a MarkovTrace violating the law and every small
model I tried had the axioms force the law to hold -- constant towers make it hold identically
(if r is in the trace-radical of H then a*r is too, so tr(a r^j) = 0 for all j >= 1), and M_2 is
excluded outright because Cayley-Hamilton gives every element a quadratic relation, which is exactly
tr_mul_adjoin_gen's hypothesis. Inconclusive: this is NOT evidence the law is true, only that these
models cannot separate it. Scope (a).


2026-09-07 (PR follow-on): TowerSpan reduced to ONE LOCAL REWRITING RULE. New module
QOU/MathlibExt/TowerSpanReduction.lean.

TowerSpan is a claim about every element of every filtration step. `SandwichReduces B m` is a claim
about one element SHAPE:

    for all c in B,   g m * c * g m   in   B + span(sandwich B m)

`towerSpan_of_sandwichReduces` proves the local rule implies the global decomposition, and
`disjointBlock_of_sandwichReduces` composes it end to end with disjointBlock_of_towerSpan.

WHY THIS IS THE RIGHT REDUCTION. DisjointBlockTraceLaw identified the obstruction as a REPEATED
maximal-level generator, a word g M * x * g M that no rotation can peel. SandwichReduces is exactly
the statement that such a word rewrites, and nothing more. Smaller (one shape, not a submodule
containment), local (one level m, not the tower), and it is where the braid relation lives -- in the
Hecke case the reduction is the content of g_i g_{i+-1} g_i = g_{i+-1} g_i g_{i+-1} plus the
quadratic relation.

THE PROOF is multiplication-closure of P = B + span(sandwich), which has exactly one non-trivial
case:
    (v g w)(v' g w') = v * (g * (w v') * g) * w'
whose middle factor is SandwichReduces applied to w v' in B. The rest is mul_base_left /
mul_base_right. With closure, P becomes a subalgebra via Submodule.toSubalgebra and Algebra.adjoin_le
finishes.

STILL NOT ESTABLISHED. SandwichReduces is NOT proved for any tower with a growing filtration. This
moves the hypothesis; it does not discharge it. A reduction between two unproved statements is
progress in SHAPE only. The disjoint-block law -- and hence the bond-product reading of the atom word
-- remains MEASURED, NOT DERIVED. The towerSpan_unit inhabitation caveat carries over unchanged: the
only witness has a constant filtration, and towerSpan_of_constant shows such a witness satisfies
TowerSpan for reasons unrelated to any of this.

Verification: lean-direct exit 0, no sorry; #print axioms clean on all declarations; import cone
rebuilt from current main source.


2026-09-07 (witness): the constant-filtration objection to towerSpan_unit is CLOSED. New module
QOU/MathlibExt/InvolutionTowerWitness.lean.

A = MonoidAlgebra R (Multiplicative (N ->_0 ZMod 2)) -- countably many COMMUTING INVOLUTIONS t m.
Tower H n = adjoin{t m : m < n}, g m = ginv m = t m, trace = augmentation, z = zinv = 1. All
MarkovTrace axioms hold.

  t_mul_t                    t m * t m = 1, so hquad holds with h = 0
  sandwichReduces_involution SandwichReduces holds NON-TRIVIALLY: t*c*t = c*(t*t) = c uses
                             commutativity AND the involution relation -- the local rewriting rule
                             of TowerSpanReduction doing real work
  towerSpan_involution       hence TowerSpan, via towerSpan_of_sandwichReduces
  t_not_mem_shiftedUpTo      THE FILTRATION GROWS: t N is not in shiftedUpTo n M for M < N.
                             Proved by an algebra endomorphism killN (induced by the coordinate
                             projection killing index N) that fixes every generator of the stage but
                             sends t N to 1; if t N were in the stage it would be fixed, forcing
                             t N = 1, which t_ne_one refutes.

WHAT IT STILL DOES NOT EXERCISE. The trace is an ALGEBRA HOMOMORPHISM, so DisjointBlockMultiplicative
holds there for EVERY pair a,b -- disjointness plays no part. The witness therefore tests the
FILTRATION content of TowerSpan and says nothing about its TRACE content. This removes the
constant-filtration objection and ONLY that one. A witness with a growing filtration AND a
non-multiplicative trace would essentially be a Hecke or symmetric-group tower, which Mathlib does
not supply.

SandwichReduces for a Hecke tower remains unproved; the disjoint-block law, and hence the
bond-product reading of the atom word, remains MEASURED, NOT DERIVED.

Verification: lean-direct exit 0, no sorry; #print axioms clean on involutionTrace,
sandwichReduces_involution, towerSpan_involution, t_not_mem_shiftedUpTo.

Taken over 2026-09-07 by claude/stalled-agents-em-linking-jilmbv after the #7079 session ended (f8e6fdaefff on main). Child task qou-fq1i builds the symmetric-group tower witness.

--------

**2026-09-07 (witness 2, bean qou-fq1i, PR #7131): the "trace is a homomorphism" objection to InvolutionTowerWitness is CLOSED.** `QOU/MathlibExt/SymmetricGroupTowerWitness.lean`: symmetric-group algebra tower `MonoidAlgebra R (Equiv.Perm ℕ)`, `g = ginv = t m = of (swap m (m+1))`, trace = coefficient of the identity, z = zinv = 0, all MarkovTrace axioms hold. The trace is NOT a hom (`tr(t t) = 1 ≠ 0`), the filtration grows (`t_not_mem_shiftedUpTo`), and `SandwichReduces` is PROVED at every level (`sandwichReduces_sym`) via the double-coset decomposition `S_{k+1} = S_k ∪ S_k s_k S_k`, itself from "adjacent transpositions generate interval-supported permutations" (double induction). Hence `TowerSpan` and `DisjointBlockMultiplicative` through the #7079 chain, cross-checked by a direct proof from `W_{<n} ∩ W_{≥n} = {1}`. Non-trivial pair: `a = 1 + t n`, `b = 1 + t(n+1)`: tr(ab) = 1 = tr a·tr b, while tr(a·a) = 2 ≠ 1 — the law is about disjointness, not multiplicativity. 0 sorry; lean-direct exit 0; #print axioms clean on 18 decls.

What remains: q = 1 / z = 0 / h = 0 only. The double coset is proved in the permutation model, never by rewriting with the braid + quadratic relations, so SandwichReduces for a Hecke tower at q ≠ 1 is still unproved and the bond-product reading of the atom word remains MEASURED, NOT DERIVED. Bean stays open.
--------

**2026-09-08 (PR #7153, branch `claude/hecke-sandwich-reduces-2026-09-08`): `TowerSpan` is PROVED from the braid relations. The gap this bean names is discharged as a hypothesis on the tower; what remains is an instance, not a proof.**

New module `QOU/MathlibExt/HeckeSandwichReduces.lean` (~250 lines, 10 decls, 0 sorry).

`class BraidedTower (T : MarkovTrace R A)` carries exactly three equations, each a
defining relation of `H_n(q)` and none of them mentioning the trace:

    quad   ∀ m, ∃ h : R, g m * g m = h • g m + 1      (Hecke: h = q − q⁻¹)
    far    ∀ m k, k + 1 < m → g m * g k = g k * g m
    braid  ∀ m, g (m+1) * g m * g (m+1) = g m * g (m+1) * g m

`sandwichReduces_all` proves `SandwichReduces T (shiftedUpTo T n M) (M+1)` for
every `n, M`, by induction on `M`. With `g₁ = g (M+1)`, `g₂ = g (M+2)` and the
previous level's decomposition `c = u + Σ vᵢ g₁ wᵢ` at level ≤ M:

  * `shiftedUpTo_commute` — everything at level ≤ M commutes with `g₂` (`far`,
    since `M+1 < M+2`); `ginv_far` carries this to `ginv` via `quad`.
  * `base_conj` — `g₂ u g₂ = u g₂² = h • (u g₂) + u`, the quadratic relation.
  * `sandwich_conj` — `g₂ (v g₁ w) g₂ = v (g₂ g₁ g₂) w = v (g₁ g₂ g₁) w
    = (v g₁) g₂ (g₁ w)`, the braid relation, and both outer factors have risen
    exactly one level.

Base case: the bottom stage of the full shift window is affine in `g 0` (`quad`
makes `ginv 0` affine), so one `quad` + one `braid` at `m = 0` suffice; below the
window the stage is `⊥` and `quad` alone does it.

`towerSpan_of_braided` / `disjointBlock_of_braided` compose it with #7079 and
`disjointBlock_of_towerSpan`.

**This is the thing qou-fq1i's own closing note said was still missing** — that
bean records "the double coset is proved in the permutation model, never by
rewriting with the braid + quadratic relations, so SandwichReduces for a Hecke
tower at q ≠ 1 is still unproved". This proof IS the rewriting proof, generic in
the tower, so it holds at q ≠ 1. The two results are complements, not duplicates.

Refactor: `TowerSpanReduction.step_of_sandwichReduces` extracted from the body of
`towerSpan_of_sandwichReduces` (now a one-line repackaging). The induction needs
the per-level form to feed level M's conclusion into level M+1's hypothesis. No
proof step changed.

**🛑 WHAT IS STILL OPEN, and the bean stays open for it.** No `BraidedTower`
instance on a Hecke tower is constructed. The class is bracketed by two witnesses
that no single object combines:

  * `braidedTower_unit` (this PR) — `unitMarkovTrace u` satisfies all three with
    `h = u − u⁻¹`, non-zero as soon as `u² ≠ 1` (`unit_quad_scalar_ne_zero`). So
    the relations do NOT force `h = 0`. Filtration constant.
  * the symmetric-group tower (qou-fq1i / #7131) — filtration grows,
    non-multiplicative trace, but `h = 0`.

`braid_forces_eq_of_commuting_involutions` proves the third existing witness
cannot be braided: for commuting involutions the braid relation collapses to
`g m = g (m+1)`, so `InvolutionTowerWitness` satisfies `SandwichReduces` for
reasons unrelated to this argument.

A witness with a growing filtration AND `h ≠ 0` is an Iwahori-Hecke tower, which
Mathlib does not supply. That is now the whole remaining distance, and the
bond-product reading of the atom word remains MEASURED, NOT DERIVED.

Verification: `lean -DautoImplicit=false -s 65536` against restored
`lake-cache/qou-v4-24-0` with `DisjointBlockTraceLaw` (29 s) and
`TowerSpanReduction` (6 s) rebuilt from main source into a hardlinked shadow —
exit 0, no errors, no warnings. `InvolutionTowerWitness` re-checked against the
refactored `TowerSpanReduction`: exit 0. `#print axioms` on all ten new
declarations plus both refactored ones: `[propext, Classical.choice, Quot.sound]`
(`unit_quad_scalar_ne_zero`: `[propext]` alone). Zero `sorryAx`.

--------

**2026-09-13 (PR #7153, second tranche): `BraidedTower` is INHABITED. The caveat #7153 shipped with is closed on a Hecke tower; what remains is a FAITHFUL TRACE, not a carrier.**

New module `QOU/MathlibExt/BraidedTowerInstances.lean` (175 lines, 7 decls, 0 sorry).

Two carriers landed on `main` while #7153 sat, and the sibling on #7228 explicitly
left the instantiation to whoever landed second — *"BraidedTower would be a
three-line instantiation once #7153 lands"*:

* `braidedTower_heckeTower` — `HeckeTowerWitness.heckeTowerMarkovTrace h z hz`
  (bean `qou-cins`, #7228). `HeckeTower R h` presents `H_∞` as `FreeAlgebra R ℕ`
  quotiented by exactly `quad` / `far` / `braid` via `RingQuot`, so
  `twGen_quad` / `twGen_far` / `twGen_braid` ARE the class fields, and `h` is a
  **free parameter** — the Hecke case `h = q − q⁻¹ ≠ 0` is available.
  `towerSpan_heckeTower` and `disjointBlock_heckeTower` follow: **the
  disjoint-block trace law on a Hecke tower at `h ≠ 0`**, the configuration every
  prior witness missed.
* `braidedTower_sym` — `SymmetricGroupTowerWitness.symTrace R` (bean `qou-fq1i`,
  #7131), `h = 0`. This gives `sandwichReduces_sym` a **second, independent
  derivation**: that file proves it in the permutation model by support and
  point-pushing through the double coset `S_{k+1} = S_k ∪ S_k s_k S_k`, while
  `sandwichReduces_all` reproves it by rewriting with the relations, never
  mentioning a permutation. The two group-level inputs are proved here from
  `Equiv.swap_apply_apply` alone — `s_far` (distant swaps commute) and `s_braid`
  (both sides are `swap m (m+2)`).

**CORRECTION to #7153's own docstring, which was wrong twice.** It read *"a
witness with both a growing filtration and `h ≠ 0` is an Iwahori-Hecke tower,
which Mathlib does not supply. That, and only that, is what stands between this
theorem and an unconditional disjoint-block law for the production trace."*
"Mathlib does not supply" was true and beside the point — the CORPUS supplies
one; and even against Mathlib it overstated, since
`SchurWeyl.finrank_le_factorial` (bean `qou-uoal`) is the upper half of the
coset-basis theorem strict growth needs. "That, and only that" was wrong about
what remains.

**🛑 WHAT REMAINS, and the instances repair neither. The bean stays open.**

1. **The Hecke trace is NOT FAITHFUL.** `HeckeTowerWitness`'s trace collapses
   every generator onto the rank-2 generator of `Hecke2` and composes with its
   Ocneanu trace, so `disjointBlock_heckeTower` is a statement about a coarse
   functional, **not** about the Ocneanu trace of `H_∞(q)`. Jones' existence
   theorem is open (bean `qou-g8i1`). This does NOT weaken `sandwichReduces_all`,
   which uses no trace field — it bounds what the COMPOSITION delivers.
2. **Strict growth is proved only at the bottom** (`twH_zero_lt_one`:
   `H 0 < H 1`). The symmetric-group carrier grows at every level
   (`t_not_mem_shiftedUpTo`) but has `h = 0`. **No single carrier yet has both
   `h ≠ 0` and growth at every level** — that needs the Iwahori-Hecke coset
   basis, whose `n!` lower bound is the open half of `qou-uoal`.

So the distance from here to an unconditional disjoint-block law for the
production trace is a **faithful trace**, not a carrier. The bond-product reading
of the atom word remains MEASURED, NOT DERIVED.

Verification: `lean -DautoImplicit=false -s 65536` against restored
`lake-cache/qou-v4-24-0`, with `DisjointBlockTraceLaw`, `TowerSpanReduction`,
`HeckeRankTwoMarkov`, `HeckeTowerWitness` and `SymmetricGroupTowerWitness`
rebuilt from `main` source into a hardlinked shadow (all exit 0).
`BraidedTowerInstances` exit 0, no warnings. `#print axioms` on all seven new
declarations: `[propext, Classical.choice, Quot.sound]`. Zero `sorryAx`.

--------

**2026-09-13 (correction, one hour after the merge of #7153): TWO citations I landed on `main` are wrong, and one of them is a false claim rather than a bad ID.**

The entry above says the remaining distance is *"a faithful trace, not a carrier"*,
and cites two beans for it. Both citations are wrong; the shape of the conclusion
survives, its content does not.

1. **"Jones' existence theorem is open (bean `qou-g8i1`)" — FALSE, both halves.**
   Jones' theorem is **proved in this corpus, with uniqueness**, sorry-free on
   `main` and predating my text:
   * `QOU/SchurWeyl/MarkovTraceInstance.lean` — `wtrace` with `wtrace_cyclic`
     (T1), `wtrace_one` (T2), `wtrace_markov` (T3) **and** `wtrace_incl` (tower
     compatibility), bundled as
     `ocneanuMarkovTrace : HeckeCoset.MarkovTraceFamily R q q⁻¹ (q³/(q²+1))`,
     plus `eq_wtrace_of_markov` (every such trace IS this one).
   * `QOU/SchurWeyl/MarkovTraceUnique.lean` — `markovTrace_unique`.

   **The real gap is a BRIDGE, and it is a much smaller and more tractable
   statement than the one I wrote:** all of that lives in
   `HeckeCoset.MarkovTraceFamily`, a *different* Markov-trace abstraction, and
   **nothing bridges it to `OcneanuTrace.MarkovTrace`** — the structure
   `DisjointBlockTraceLaw` / `TowerSpanReduction` / `HeckeSandwichReduces`
   actually consume. `qou-g8i1` is not that item at all: it is the `(z+d)` bond
   rule, and its status is `completed`.

   **I propagated this from `HeckeTowerWitness.lean` lines 59-60, which still
   carries it on `main`** — and that file's own plan bean `qou-0fmb` re-scoped
   it on **2026-09-12**, the day before I quoted it: *"MAJOR RE-SCOPE: S2 is NOT
   open. Jones' existence theorem is PROVED in the corpus, with uniqueness — in
   a DIFFERENT Markov-trace abstraction that nothing bridges."* A sibling's
   merged docstring is not a primary source; the bean was, and one grep would
   have caught it. Flagged to that arc rather than edited, since `qou-cins` /
   `qou-p8yg` are live (commits 9 h old).

2. **"the `n!` lower bound is the open half of `qou-uoal`" — wrong bean.**
   `qou-uoal` is `completed` and is the `≤ n!` **upper** half. The live bean is
   **`qou-p8yg`** (`todo`), and it says something better than "open":
   **`H 1 < H 2` is a WIRING job, not a build** — the rank-6 separator already
   exists sorry-free (`SchurWeyl.HeckeDim3Dim.finrank_hecke3`, `sixBasis`,
   `HeckeDim3.braid3`), with the relation check worked out in the bean. General
   `n` needs the `(n+1)!` lower bound. `qou-p8yg` also carries the negative that
   closes the cheap route — `scalar_tail_forces_central` excludes the whole
   tail-to-scalars family.

**What survives unchanged.** Every Lean statement merged in #7153 — the two
instances, `disjointBlock_heckeTower`, `sandwichReduces_all` and the rest — is
untouched by this: the error is in prose citing other work, not in any proof.
What changes is the *map of what remains*, and it changes in the direction of
tractability: a bridge between two Markov-trace abstractions and a wiring job on
an existing rank-6 separator, rather than Jones' theorem and an open `n!` bound.

Corrected in place in `BraidedTowerInstances.lean` and `HeckeSandwichReduces.lean`
rather than quietly dropped, per AGENTS.md §Terse ≠ compressed trigger 1.
lean-direct exit 0 on both after the edit.

### Same day, independently — the same two-citation error, plus one point the entry above does not carry

I hit the `qou-g8i1` error from the other direction (PR #7267) and reached the same
verdict: the bean is `completed` and about the (z+d) bond rule; Jones' existence
theorem is proved on `main` with uniqueness; the real gap is the bridge between
`HeckeCoset.MarkovTraceFamily` and `OcneanuTrace.MarkovTrace`, live at
`qou-ejde` / PR #7274. **Two independent readings, same conclusion** — recorded
because the convergence is evidence, not because the correction needed repeating.

**The additive point: "faithful on `H_∞(q)`" is not merely open, it is REFUTED at
convention D.** The Wenzl weight vanishes for `ℓ(λ) ≥ 3`
(`QOU/QBeta/WenzlWeightVanishing.conventionD_weight_eq_zero_iff_rowLens`,
sorry-free), so the radical is nonzero and no trace on `H_∞(q)` can be faithful at
the canonical convention. The attainable target is faithfulness on `H_∞(q)/rad`.
This is already adjudicated as bean `qou-phlk` (`completed`) — *"DEFECT:
prop:algebraic-gns-embedding claims faithfulness on H_inf(q); its proof gives
H_inf/rad"*. Anyone writing the bridge's target statement should write the quotient,
or they re-introduce an over-claim the corpus removed once.

**Contamination count from my side:** the stale pointer reached three sites in
`BraidedTowerInstances.lean` — the header, the "not faithful" bullet, and the
`-- Ref:` line — and **two of the three were not mine**, i.e. the same text the
entry above corrects. My PR #7267's measured finding is unaffected by any of it:
`ocneanuTrace_mul_of_markov` is about `Hecke2` and never mentions Jones' theorem.


---

### 2026-09-19 — MEASURED: the multiplicativity hypothesis is DISCHARGED at the Hecke colimit, and this bean's own framing is stale

This bean's "Attack options" offer (1) a full geometric Jones formalisation, months, and (2) an algebraic Markov-trace-functional route needing "the Markov trace formalised as a functional with the tower property". **Option 2 is DONE on `main`, sorry-free, and this bean does not say so.**

`QOU/SchurWeyl/HeckeColimitMarkovTrace.lean` (0 `sorry`; header: *"This is the bridge"*):

```
heckeColimitMarkovTrace : MarkovTrace ℝ (HeckeLim ℝ q q⁻¹)
instance braidedTower_heckeColimit
theorem  towerSpan_heckeColimit      : TowerSpan (heckeColimitMarkovTrace …)
theorem  disjointBlock_heckeColimit  : DisjointBlockMultiplicative (heckeColimitMarkovTrace …)
```

**And it is the non-degenerate carrier.** `MathlibExt/BraidedTowerInstances.lean` documents about *itself* that `heckeTowerMarkovTrace` needs `z*z = h*z + 1` to be a `MarkovTrace` at all and that the same equation makes its trace an algebra **homomorphism**, so its `disjointBlock_heckeTower` "holds for reasons that have nothing to do with disjoint blocks"; its verdict was **"no witness has all three properties"** (growing filtration, `h ≠ 0`, non-multiplicative trace). The colimit carrier has all three — `trLim` is `DirectLimit.Module.lift`, **not** `Ring.lift`, because *"`wtrace` is linear and is not a ring map (it is not multiplicative)"* — with `h = q − q⁻¹` at generic `q`, and `z = q³/(q²+1)` **convention D**, *"inherited from `wtrace_markov`, not chosen here"*, `zinv` *"derived, not posited"*. No fit.

**Machine-checked consequence (RC=0, 2026-09-19).** Sibling PR #7418's chain theorems take `hdb : DisjointBlockMultiplicative T` as an explicit hypothesis, and `disjointBlock_heckeColimit` discharges it: `three_body_cumulant_vanishes` and `tr_chainWord` both elaborate at `heckeColimitMarkovTrace`, fully instantiated over `HeckeLim ℝ q q⁻¹`, carrying only the four genericity hypotheses and **no `TowerSpan` argument**. Method: compiled #7418's file from its branch to an olean, staged into the gitignored `.lake/build`, `#check`-only probe, then removed — nothing of theirs committed. Recorded as §7c of the step-11 audit (PR #7442).

**What is still open, and it is NOT multiplicativity:** **faithfulness.** The colimit file's own "What is NOT proved here" — *"`H n` remains the image of level `n`, and whether `ofLim n` is injective is bean `qou-ejde`, assumed nowhere. Nor is `trLim` claimed faithful."*

**Sibling beans stale in the same direction, none recording the above:** `qou-0fmb` is `todo` while its own steps 4–6 are landed (it is the plan this file executes); `qou-ejde` is `todo` while its step-1 keystone `heckeProduct_injective` is landed on `main` (`SchurWeyl/HeckeProductInjective.lean`, 0 sorry).

**Bean stays open (rule 13a).** What remains is faithfulness and the geometric Jones statement, neither of which this discharges. Do not read "the hypothesis is dischargeable at one carrier" as "Jones multiplicativity is formalised" — that conflation is the error class this session recorded twice.


--------

**2026-10-12 — a second BraidedTower instance with growing filtration and h = q − q⁻¹ ≠ 0, now over ANY field** (`QOU/IwahoriHecke/HeckeColimitTensorTrace.lean`, commit `1b6dbbe2fb`, bean `qou-0fmb`). `disjointBlock_tensorColimit : DisjointBlockMultiplicative (tensorColimitMarkovTrace hq hq1)` with only `[Field K]`, `q ≠ 0`, `q²+1 ≠ 0` — the existing `disjointBlock_heckeColimit` needs `ℝ` and `q` not a root of unity. Trace = IwahoriHecke tensor-model quantum trace at z_D; tower compatibility by Markov-trace uniqueness. lean-direct exit 0, axioms clean, 0 sorry. Does NOT change what this bean says remains open (faithfulness; the amplitude = trace identification; the geometric Jones statement); the tensor trace is the TL quotient and is not faithful. Bean stays open.


--------

**2026-10-12 (later):** the BraidedTower instance and the disjoint-block law now also hold on the **Coxeter-presentation** Iwahori–Hecke tower `HeckeAlgebra K (q*q) (Aₙ n)` itself (`QOU/IwahoriHecke/CoxeterTower.lean`, commit `9d2b8bfd78`): `coxeterMarkovTrace`, `braidedTower_coxeter`, `disjointBlock_coxeter`, with generators the §7a `Balanced.sigma = q⁻¹·T_n`, over any field, q ≠ 0, q²+1 ≠ 0. Sorry-free. The trace is not faithful (tensor-model / TL), and the faithfulness, amplitude=trace identification and geometric Jones items this bean lists as open are unchanged. Bean stays open.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Round 75 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/TwoRowFrobeniusStratumAndConnectedSumTraceBrick.lean` (`connected_sum_amplitude_multiplicativity_free_energy_split`)
- **Summary**: Proved connected-sum free-energy subtraction `(L1 + L2) - L_total = -L_I` when `L_total = L1 + L2 + L_I`, and strict positivity `0 < T1 * T2 * I_conn` when `0 < T1`, `0 < T2`, `0 < I_conn`.
- **80-dps Probe & Witness**: `computations/probes/two_row_frobenius_stratum_and_connected_sum_trace_brick_probe.py` -> `computations/probes/two-row-frobenius-stratum-and-connected-sum-trace-brick.witness.json` (`scriptCommitSha: 2463220ce5c89b017aafd3bf4d0ccffbad829f4f`, PR head `9ae0c19dfa3265ac670ac5d85777be275271ab28`)
