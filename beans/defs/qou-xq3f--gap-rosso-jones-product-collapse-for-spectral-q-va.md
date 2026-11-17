---
# qou-xq3f
title: 'GAP: Rosso-Jones product-collapse for spectral Q-value decomposition (Lean)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T19:36:58Z
updated_at: 2026-11-17T08:44:47Z
parent: b9cj
---

The corollary cor:spectral-decomposition-qvalue (folio/quantum-observable-universe/predicted-spectra/spectral-decomposition-qvalue.lean) claims Q = Q_bare × Π_{τ∈E_g} F(τ,N), with (iv) the product collapsing to a single active-shell term and (v) the decomposition exact by Rosso-Jones completeness of torus-knot invariants (prop:cohomological-embedding).

STATUS: the product-collapse + exactness are NOT formalized in Lean. As of 2026-08-22 the theorem is restated §3b-cond: a RossoJonesCollapse class carries the collapse (product = activeShellTerm) as a hypothesis and the theorem DERIVES the factorization from it (replacing the prior vacuous trivial existential ∃Q_q, Q_q=rhs).

OPEN: derive the collapse itself — that the knot-operator product over the embeddable basis reduces to the single active term (all other shells cancel parent↔daughter; non-embeddable knots give F=1), from Rosso-Jones completeness. This needs the torus-knot invariant / Markov-trace machinery not yet in this Lean development. Until then the class stays uninstantiated (honestly conditional).



## PROGRESS 2026-08-22 — collapse MECHANISM now proved (sorry-free)

The opaque assumption is gone. Replaced the class field `collapse : product = activeTerm` (which *asserted* the collapse) with a proved theorem:

  knot_operator_product_collapse (E : Finset ι) (F : ι → ℝ) (active) :
    (∀ τ ∈ E, τ ≠ active → F τ = 1) → ∏ τ ∈ E, F τ = F active

via Finset.prod_eq_single. #print axioms: [propext, Classical.choice, Quot.sound] — no sorryAx. spectral_decomposition_qvalue now derives the Q-value collapse from this.

So step (iv) 'the product collapses to a single term' is DERIVED, not assumed. The assumption is reduced from 'the product equals the active term' to the strictly weaker, more primitive per-shell statement 'each inactive shell contributes F τ = 1'.

STILL OPEN (the actual Rosso-Jones content): proving that hypothesis — that each non-active shell's knot operator F τ = 1 (parent↔daughter shell-cancellation + F=1 for non-embeddable knots). That needs the F-operator (Markov trace of τ·T_β) defined in Lean + the completeness/self-duality of the torus-knot basis, none of which is in this Lean development yet. Bean stays open for that.



## PROGRESS 2026-08-22 (2) — per-shell cancellation: two inactive branches DISCHARGED

Added a ratio-level shell model + discharged the hInactive hypothesis for the two inactive branches:
- ShellState (parentTrace, daughterTrace, embeddable); shellFactor s = if embeddable then daughterTrace/parentTrace else 1.
- shellFactor_nonembeddable: non-embeddable ⇒ F=1 (definitional).
- shellFactor_unchanged: embeddable & daughterTrace=parentTrace≠0 ⇒ F=1 (div_self — the genuine 'cancels in ratio' mechanism).
- shell_product_collapse: every non-active shell non-embeddable-or-unchanged ⇒ ∏ shellFactor = shellFactor(active), with hInactive now PROVED for this model (not assumed).

#print axioms: [propext, Classical.choice, Quot.sound] — no sorryAx.

So step (iv) is now: collapse mechanism proved (progress 1) + the two INACTIVE branches (non-embeddable, unchanged) proved to give 1 (progress 2). The hInactive hypothesis is discharged for the ratio model.

STILL OPEN (the deep Rosso-Jones content):
1. The ACTIVE shell value = |tr_M(e·τ·T_β·e)|/|tr_M(T_β)| — needs the weighted Markov-trace tower (QOU.Braiding.HnMarkovTrace) wired into this file.
2. Identifying WHICH shell is active (the converting neutron's shell) and that all others are genuinely unchanged/non-embeddable — the physical shell-assignment, not yet modeled.
3. Basis completeness/self-duality (prop:cohomological-embedding) that guarantees the torus-knot basis is complete.



## PROGRESS 2026-08-22 (3) — active-shell numerator: idempotent sandwich collapse PROVED

Wired into the general Hecke Markov-trace infra (QOU.Hecke.MarkovTrace, which carries trace : A →ₗ[R] R + cyclic tr(xy)=tr(yx) + normalised). Added two generic-ring lemmas (sorry-free, #print axioms [propext, Classical.choice, Quot.sound]):
- MarkovTrace.trace_idempotent_sandwich (e x : A) (he : e*e=e) : trace (e*x*e) = trace (e*x)
- MarkovTrace.trace_idempotent_sandwich' : trace (e*x*e) = trace (x*e)

Derivation: tr(e·x·e) = tr(e·(e·x)) [cyclic] = tr((e·e)·x) = tr(e·x) [idempotency]. Pure consequence of the M2 cyclicity axiom.

This formalizes the Pauli-FULL-shell branch of F(τ,N): its numerator |tr_M(e_{(1³)}·τ·T_β·e_{(1³)})| simplifies to |tr_M(e_{(1³)}·τ·T_β)| — the outer alternating-idempotent sandwich collapses. So the active-shell F numerator STRUCTURE is now derived, not opaque.

STILL OPEN (remaining deep content):
1. The VALUE tr_M(e·τ·T_β) and the denominator tr_M(T_β) as explicit closed forms — needs the weighted Wedderburn sum tr_M = Σ_λ y_λ χ^λ instantiated for the specific τ, T_β=σ_0σ_1⁻¹, e_{(1³)} (the y_λ closed forms exist in schur_principal_mpmath / WenzlSchurElement but aren't wired to a general braid-word trace in Lean).
2. Shell-assignment (which shell active) + basis completeness (prop:cohomological-embedding).
Progress ladder so far: collapse mechanism (1) + inactive branches (2) + active-numerator idempotent collapse (3).



## ═══ TIERED WORKPLAN (2026-08-23) ═══

Goal: fully derive cor:spectral-decomposition-qvalue's F(τ,N) = |tr_M(e·τ·T_β·e)|/|tr_M(T_β)| and the exact decomposition, in Lean. Ordered by tractability.

**T0 — collapse bookkeeping [DONE].**
  - knot_operator_product_collapse (#5481): ∏ mostly-1 factors → active.
  - shellFactor + inactive branches (#5491): non-embeddable/unchanged ⇒ F=1.
  - trace_idempotent_sandwich (#5496): tr(e·x·e)=tr(e·x), numerator outer-e collapse.

**T1a — denominator closed form [DONE 2026-08-23].**
  MarkovTrace.trace_gen_mul_invGen: tr_M(σ_i·σ_j⁻¹) = z²−(q−q⁻¹)z for i<j.
  So tr_M(T_β)=tr_M(σ_0σ_1⁻¹)=z²−(q−q⁻¹)z. sorry-free, no sorryAx.

**T1b — numerator value tr_M(e_{(1³)}·τ·T_β) [NEXT, medium].**
  Needs: e_{(1³)} the alternating Young idempotent of H_3 as a concrete Hecke
  element (check QOU.Hecke for a Young-symmetrizer def; if absent, define via the
  antisymmetrizer over S_3). Then tr_M of the specific word e·τ·T_β. For the
  trefoil τ=σ_1² the σ_1²-trace closed form already exists
  (MarkovTraceTower.trM_sigma1_sq / TrMHopfSigma1SqClosedForm). Tractable for
  small specific τ; general τ needs T2.

**T2 — general braid-word tr_M via weighted Wedderburn sum [KEYSTONE, hard].**
  Wire tr_M = Σ_λ y_λ χ^λ to a general braid-word trace. y_λ closed forms exist
  in schur_principal_mpmath / WenzlSchurElement (compute side) but not as a Lean
  A→R trace on arbitrary words. This is the 08a2 keystone-de-abstraction epic.
  Prereq for the general active-shell value + exactness.

**T3 — shell-assignment [physical].**
  Model which shell is active (converting neutron's shell) and that all others
  are unchanged/non-embeddable, discharging shell_product_collapse's hypothesis
  for the real nuclear decay, not an abstract Finset.

**T4 — basis completeness [hard, conj-backed].**
  prop:cohomological-embedding (Rosso-Jones completeness + self-duality
  τ(r,s)↔τ(s,r)). Guarantees the torus-knot basis is complete ⇒ (v) exactness.
  Depends on T2.



## PROGRESS 2026-08-23 (4) — T2 keystone: first brick (weighted-trace cyclicity)

Started the T2 keystone (general braid-word tr_M = Σ_λ y_λ χ^λ) in
QOU/MathlibExt/MarkovTrace.lean §5:
- weightedCharacterTrace s dim ρ y w = Σ_{i∈s} y i · (ρ i).character w — the
  Wedderburn-weighted trace shape, per-block dimensions dim i, over a finite
  index set (the partitions λ⊢n). y_λ are the compute-side input (not fixed).
- weightedCharacterTrace_append_comm: the weighted sum inherits Markov cyclicity
  (M2) — tr_M(v++w)=tr_M(w++v) — derived block-by-block from character_append_comm
  via Finset.sum_congr. Independent of the particular y_λ.

lean-direct exit 0; #print axioms no sorryAx; audit 0 defects.

So the Wedderburn-weighted trace is now KNOWN to be a class function (M2) whatever
weights are supplied. STILL OPEN for the full tr_M: fixing the y_λ(q) values
(the deep compute-side closed forms), M1 normalisation (tr_M 1 = 1 ⟹ Σ y_λ d_λ = 1),
M3 Markov peel, and then the specific numerator tr_M(e_{(1³)}·τ·T_β). Ladder:
collapse mechanism + inactive branches + numerator idempotent collapse + denominator
+ weighted-trace cyclicity (this). The y_λ-value fix remains the 08a2 keystone core.



## PROGRESS 2026-08-23 (5) — T2 brick 2: identity value (M1 shadow)

weightedCharacterTrace_nil: tr_M(1) = Σ_λ y_λ·d_λ (χ^λ(1)=tr(𝟙_{d_λ})=d_λ via
eval_nil+trace_one+card_fin). So M1 normalisation tr_M(1)=1 ⟺ Σ y_λ d_λ = 1 —
the relation that pins y_λ given the block dims. lean-direct exit 0, no sorryAx.

T2 structural bricks now landed (PR #5528): M2 cyclicity + M1 identity-value, both
independent of the y_λ values. The Wedderburn-weighted trace has its class-function
property AND its normalisation-relation established.

HONEST WALL (08a2 keystone core, genuinely large): what remains for the full tr_M
is (a) the y_λ(q) CLOSED-FORM VALUES — the compute-side schur_principal_mpmath /
WenzlSchurElement results, which must be transcribed/derived into Lean and shown to
satisfy Σ y_λ d_λ = 1 + the M3 Markov peel; (b) M3 (Markov peel) as a theorem; (c)
the concrete e_{(1³)}, τ, T_β braid elements + the numerator value. This is
multi-session infra, not a single-session brick — the structural scaffolding (M1/M2
shadows) is now in place for it.



## ═══ REVISED WORKPLAN 2026-08-28 (post-keystone-closure) ═══

PIVOT: my prior notes called the SYT-count f_λ sum 'the deep Mathlib gap' blocking
the Markov-trace normalisation + Macdonald telescope. That gap is now CLOSED on
main (sibling work: RSK_substrate_axiom de-axiomatised; RSKBijection n for every n;
list-model dimension identity for every n; Identity-I chain closed). So what was
'multi-session infra' is now WIRING.

Landed (structural T2 bricks, all sorry-free, on main): collapse mechanism +
inactive branches + numerator idempotent-sandwich + denominator closed form +
weightedCharacterTrace M2 cyclicity + M1 identity (Σ y_λ d_λ). Also: schurElement
prefactor corrected nLambda (NOT contentSum) by sibling 2026-08-26 — do not
reintroduce contentSum there.

REVISED TIERS (tractability order):
 T-n1  Prove Wenzl/Macdonald normalisation Σ_λ f_λ·s_λ = ((1−X)/(1−Q))^n using the
       now-available RSK/SYT-count machinery — de-abstract wenzlNormalisation
       (currently defined as the closed form ((1−X)/(1−Q))^n, with the SYT sum
       'abstracted'). This is the unblocking lemma.
 T-n2  jonesMarkovCoeff normalisation Σ_λ y_λ·f_λ = 1 (M1 for the REAL y_λ) —
       derives from T-n1; wires weightedCharacterTrace M1 shadow to concrete y_λ.
 T-n3  M3 (Markov peel) as a theorem — check whether the sibling HnMarkovTrace /
       tower work already supplies it before building.
 T-n4  Numerator value tr_M(e_{(1³)}·τ·T_β) — concrete braid elements; last brick,
       once M1/M2/M3 + y_λ values are in place.
Starting T-n1 this session (user directive 2026-08-28).

T-n2 (n=3) LANDED: jonesMarkov_normalisation_three in MacdonaldTelescope.lean — M1 axiom tr_M(1)=1 at nucleon rank H3 for the concrete jonesMarkovCoeff weights (f_lambda = 1,2,1 over partitions of 3), derived from proved telescope_three / Z3. lean-direct exit 0, #print axioms = [propext, Classical.choice, Quot.sound], sorry-free.

General conditional M1 LANDED: jonesMarkov_normalisation_of_telescope in MacdonaldTelescope.lean — for any partition list of common size n, IF the multiplicity-weighted schurElement sum = Z_n (the open general Macdonald telescope, carried as an explicit hypothesis) THEN the same weights normalise jonesMarkovCoeff to 1. Generalises T-n2 off the three partitions of 3 to arbitrary rank; instantiate with a proved telescope and normalisation follows. lean-direct exit 0, #print axioms = [propext, Classical.choice, Quot.sound], sorry-free.

T-n3 (M3 Markov peel) LANDED in MacdonaldTelescope.lean: markovParameter z=(1-X)/(1-Q); wenzlNormalisation_markov_recursion (Z_{n+1}=z*Z_n, the trace-side Markov property tr(x sigma_n)=z tr(x)); telescopeRHS_markov_recursion; pieriStep_iff_markov (Pieri corner-sum = z*s_lambda); markov_peel_two_one (concrete peel at the rank-2->3 (2,1) shape); plus jonesMarkov_normalisation_one/_two completing the concrete M1 ladder at ranks 1,2. All lean-direct exit 0, #print axioms = [propext, Classical.choice, Quot.sound], sorry-free. Concrete M1 now closed at ranks 1,2,3; general M1 conditional on telescope; M3 z-recursion of the normalisation proved + concrete peel at (2,1).

T-n1 RE-SCOPED after corpus-grep (Explore agent map): the GENERAL Macdonald hook telescope is ALREADY PROVED sorry-free in the corpus -- QOU.SchurWeyl.sum_dim_wenzlWeight_eq_one (WenzlNormalisation.lean:129), general n, general level r, resting on sorry-free (F) numStandardYoungTableaux_branching (SYTBranchingRule.lean) and (P) sum_wenzlWeight_addCellOrSelf (BranchingGenericity.lean). Even n=3 is mirrored on the canonical carrier by ocneanuWeight_normalisation_three (OcneanuWeightMarkov3.lean). So re-deriving the telescope in the List layer would DUPLICATE a solved result (forbidden by anti-dup discipline). The general telescope is on the YoungDiagram carrier (wenzlWeight/schurPrincipal, X=Q^r); my MacdonaldTelescope.lean is a parallel List carrier (schurElement, X free); Explore confirmed NO bridge lemma between the two schurElement objects. Re-scoped to build that missing bridge: schurElement Q (Q^r) lam = schurPrincipal r Q (ofRowLens lam hl). NEXT after bridge: full unconditional M1 (discharge jonesMarkov_normalisation_of_telescope htel) also needs a SECOND carrier bridge -- SYT count numSYTenum (List) vs numStandardYoungTableaux (YoungDiagram) -- plus a List-of-partitions vs Finset-of-diagrams sum match; deferred as its own gap.

CARRIER BRIDGE COMPLETE (unconditional, sorry-free): schurElement_eq_schurPrincipal in WenzlSchurElementBridge.lean proves schurElement Q (Q^r) lam = schurPrincipal r Q (ofRowLens lam hl) for weakly-decreasing positive lam, Q!=0. Bricks: B1 content_eq_cellContent, B2 rowLen_ofRowLens_getD, B5 prod_cells_ofRowLens (+ list_range_map_prod, schurElement_eq_finset_prod, cells_ofRowLens_eq_biUnion), B4 nPart_ofRowLens_eq_nLambda (+ list_range_foldl_add), B6 schurElement_eq_schurPrincipal_of_hook, B3 hook_ofRowLens_eq_hookLength. B3 collapsed via corpus-grep: reused QOU.Mathlib.colLen_rowLens + QOU.Mathlib.SYTBeta.colLen_eq_succ_add_cnt_drop (the sorted-list leg identity, already sorry-free in the corpus). All #print axioms = [propext, Classical.choice, Quot.sound]. This is the missing carrier link the Explore map flagged. NEXT: the full unconditional M1 via sum_dim_wenzlWeight_eq_one still needs the SYT-count carrier bridge (numSYTenum vs numStandardYoungTableaux) + List-of-partitions vs Finset-of-diagrams sum match -- deferred.

FULL UNCONDITIONAL M1 drafted (WenzlJonesMarkovNormalisation.lean): sum_dim_jonesMarkovCoeff_eq_one -- SUM over SYT-weighted diagrams of size n of f^nu * jonesMarkovCoeff Q (Q^r) nu.rowLens = 1, general n, unconditional. Route AVOIDS a List-sum conversion: proved termwise = wenzlWeight via the carrier bridge + ofRowLens_to_rowLens_eq_self, then cites the proved SchurWeyl.sum_dim_wenzlWeight_eq_one. Sub-lemmas: rowLens_sum_eq_card, levelBracket_eq (geom sum), jonesMarkovCoeff_rowLens_eq_wenzlWeight. Proof written; blocked only on the SchurWeyl olean cone (WenzlNormalisation + deps missing from restored cache) -- delegated env-build + verification.

FULL UNCONDITIONAL M1 VERIFIED (sorry-free): sum_dim_jonesMarkovCoeff_eq_one compiles via lake build (3308 jobs, whole SchurWeyl cone from source; cache get 403'd). #print axioms = [propext, Classical.choice, Quot.sound]. This closes the M1 arc: general-n Markov normalisation tr_M(1)=1 for the concrete List-carrier jonesMarkovCoeff weights, DERIVED from the proved SchurWeyl.sum_dim_wenzlWeight_eq_one via the carrier bridge (no fit, no assumption). INFRA FINDING: lake-cache/qou-v4-24-0 has ZERO SchurWeyl oleans -- the whole cone must be rebuilt from source by anyone touching it; candidate for re-seeding.

GENERAL-X TELESCOPE (research frontier) STARTED: MacdonaldTelescopeGeneralX.lean lays out the polynomial-identity route (both telescope sides are polynomials in X of degree n, agreeing at all X=Q^r via the merged bridge + sum_dim_wenzlWeight_eq_one; {Q^r} infinite for Q>1 ⇒ Polynomial.eq_of_infinite_eval_eq forces equality for ALL X). Brick 1 landed sorry-free (powers_infinite: {x|∃n,Q^n=x} infinite for Q>1). Bricks 2-4 open + substantial (schurElementPoly : ℝ[X] lift of the nested product; un-normalised X=Q^r agreement; assembly). Research tranche, not one-sitting.

General-X BRICK 2 landed (sorry-free): schurElementPoly Q λ : ℝ[X] (cellFactorPoly per cell) + eval_schurElementPoly ((schurElementPoly Q λ).eval X0 = schurElement Q X0 λ). Proves schurElement Q · λ is a genuine polynomial in X, via WenzlSchurElementBridge.schurElement_eq_finset_prod + Polynomial.eval_prod/eval_mul/eval_C/eval_X + ring. #print axioms = [propext, Classical.choice, Quot.sound]. Remaining: brick 3 (un-normalised X=Q^r agreement Σ f_λ s_λ(Q,Q^r) = Z_n from SchurWeyl.sum_dim_wenzlWeight_eq_one + bridge) and brick 4 (assembly via eq_of_infinite_eval_eq).

GENERAL-X TELESCOPE COMPLETE (sorry-free, all 4 bricks): telescope_generalX proves Σ_{|ν|=n} f^ν·schurElement Q X ν.rowLens = ((1-X)/(1-Q))^n for ALL X (Q>1) -- the corpus previously had it only at X=Q^r. Route: bricks 1 (powers_infinite), 2 (schurElementPoly + eval_schurElementPoly, the ℝ[X] lift), 3 (sum_dim_schurElement_rowLens_eq, un-normalised X=Q^r agreement via sum_dim_wenzlWeight_eq_one + bridge), 4 (telescopeLHS/RHSPoly + eval lemmas + levelBracket_succ_ne_zero + eq_of_infinite_eval_eq over {Q^{r+1}}). All #print axioms = [propext, Classical.choice, Quot.sound]. This generalises the conditional jonesMarkov_normalisation_of_telescope's hypothesis to free X.


## Round 81 Execution Note (2026-11-17T08:44:47Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8288`](https://github.com/litlfred/qou/pull/8288) (`feat/qou-b9cj-6poy-q64u-regz-w3eg-xq3f`, HEAD `3f9d9bb7e2af7c3353cc2779b429d84aae572cda`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/NeumannZagierDeterminantAndVassilievMilnorBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/neumann_zagier_determinant_and_vassiliev_milnor_brick_probe.py` & `computations/probes/neumann-zagier-determinant-and-vassiliev-milnor-brick.witness.json` (`scriptCommitSha = b4b438fbfa2d06efdb0e7b096ec45a7a03973e2b`, `scriptHash = cf7e93178098`, `outputHash = c7210b5eb72906d3c61c7e19a0c46a0a3457be0f703d99c7dd7475108da381b1`).
