---
# qou-v7ro
title: 'GAP: bridge Magnus coeff mu-bar(12..A)=+/-1 to the QOU Markov-trace deficit leading coefficient (close MilnorExactOrderConjecture)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T23:10:14Z
updated_at: 2026-08-30T09:24:19Z
---

## What is proved (branch claude/milnor-exact-order-coefficient-proof-2026-08-01)

`MilnorMagnusCoefficient.lean` (sorry-free, lean-direct exit 0): the length-A
Milnor/Magnus coefficient `μ̄(12…A) = ±1 ≠ 0`, derived by evaluating #4471's Lie
iterated-commutator tower on the elementary matrices `E_{i,i+1}` (faithful
nilpotent rep) → `iterCommTower magnusGen n = (−1)ⁿ • E_{0,n+1}`. The surviving
coefficient is the off-diagonal `(0,A)` matrix coordinate (a NON-cyclic
functional); its cyclic trace is 0 (`trace_magnusGen_realization_eq_zero`),
matching #4480's Route-B `cyclic_trace_kills_iterCommTower`.

## What stays OPEN (this GAP)

`MilnorExactOrderConjecture` (#4471) — the QOU **Markov-trace** deficit
`D_A(h) = 1 − τ_A` leading coefficient ≠ 0 — is NOT closed. The proved Magnus
coefficient lives in the off-diagonal `(0,A)` coordinate; the QOU deficit uses a
**cyclic Markov trace**, which annihilates that off-diagonal element (Route B).
The bridge — that the Markov-trace deficit's order-`2(A−1)` leading coefficient
equals (up to a nonzero normalisation) the off-diagonal Magnus coefficient `±1`
— is the Bar-Natan / Habegger–Masbaum Milnor = leading-Vassiliev theorem
(`BrunnianVassilievBridge`, instance-less in the Vassiliev scaffold).

## Why it failed / what's needed

Mathlib has no Kontsevich-integral / finite-type invariant theory, so the bridge
cannot be discharged from library results. Two sub-obstructions:
  1. **DD-1 factor-of-2 grading** (`MilnorVassilievGrading.lean`): QOU order is
     `2(A−1)` but the standard Milnor Vassiliev degree is `A−1` — the doubling
     (h = 2·sinh ℏ, plus the deficit being a *squared*-magnitude object) must be
     proved, not assumed.
  2. **trace ↔ Magnus-coordinate identification**: connect the cyclic Markov
     trace's degree-`2(A−1)` part to the off-diagonal Magnus coordinate. The
     Jones-polynomial Vassiliev expansion (Bar-Natan) is the route; needs a
     formalised weight-system evaluation on the Brunnian chord diagram.

## Next honest step

Either (a) formalise enough of the Jones-Vassiliev weight system to evaluate the
degree-`2(A−1)` weight on the A-component Brunnian diagram and show it is the
Magnus coefficient (large), or (b) leave `MilnorExactOrderConjecture` /
`BrunnianVassilievBridge` instance-less and keep the honest conditional results.
Do NOT fabricate an instance; do NOT wire `μ̄_A = (3/4)(−2)^{A−3}` as canonical
(it is MEASURED, #4480).



--- 2026-08-29/30 A=5 CONFIRMS the recursion (PR #6077) ---
A=4 tight slice PROVED in Lean (borromean4_tight_slice, lean-direct exit 0, axiom-clean;
convention D, cofactor(0)=-3/2). Candidate recursion D_{A+1}=-h^2(h^2+2)D_A read off A=3,A=4.
NOW: exact convention-D A=5 computed (milnor_a5_a6_recursion_test.py) — D_5 == -h^2(h^2+2)*D_4
holds on the FULL rational function (not just leading coeff): D_5=h^8(h^2+2)^2(h^2+3)/(h^2+4).
3 exact points agree. A=6 running (92-crossing H_6 word, slow). If A=6 also holds -> 4 points;
then the OPEN prize is the STRUCTURAL derivation of the -h^2(h^2+2) factor from the TL/
strand-addition (Jones-Wenzl) property, which would prove MilnorExactOrderConjecture
NONVANISHING for all A by induction from A=3 (no weight-system bridge needed). Still no
instance fabricated; recursion is measured-exact at 3 pts, not yet derived.



--- A=6 confirms (4 exact points) + reduction Lean (2026-08-30) ---
A=6 also holds on the FULL rational function: D_6=-h^10(h^2+2)^3(h^2+3)/(h^2+4)=-h^2(h^2+2)*D_5.
So D_{A+1}=-h^2(h^2+2)D_A verified EXACT at A=3,4,5,6 (whole function, not just leading coeff).
Closed form: D_A=(-1)^(A-3)h^(2(A-1))(h^2+2)^(A-3)(h^2+3)/(h^2+4). New Lean file
BrunnianDeficitRecursion.lean (verifying): PROVES the recursion => tight slice for ALL A>=3
(cofactor(0)=(3/4)(-2)^(A-3)!=0), via a BrunnianDeficitRecursion conjecture CLASS (no instance).
This REDUCES MilnorExactOrderConjecture nonvanishing from 'needs weight-system bridge' to 'the
deficit obeys this 1-line recursion' (4-pt verified). REMAINING OPEN (the instance): structural
TL/Jones-Wenzl derivation of the -h^2(h^2+2)=-h^2*(q^2+q^-2) strand-addition factor. Not
fabricated; conditional result only.



--- 2026-08-30 operator-level derivation of -h^2(h^2+2) (PR #6077) ---
Derived the recursion MECHANISM in the spin-1/2 rep (= convention D, verified C0). Verified as
matrices (C2): rho(w_{A+1}) = 1 + q^2 h e_A - h q^-2 We_AW^-1 - h^2 We_AW^-1 e_A; the SOLE
w_A-dependent term carries coeff exactly -h^2. qtr of it reproduces D_{A+1}=-h^2(h^2+2)D_A
(C3/C4). e_A=q-R, band=q^2-h e_A. Verified A=3 (A=4 = 32-dim symbolic inverse, intractable);
recursion A=3..6. CORRECTION: my clean 'single conditional-expectation identity' guess was
REFUTED by the probe (messy rational, not affine) - the recursion is the full 4-term assembly.
Caught pre-durable; Lean+PR unaffected. STATUS: -h^2 derived at operator level; the (h^2+2)
trace-assembly + forall-A Brunnian induction (a concrete TL statement, NOT the weight-system
bridge) remain open. No instance.



--- 2026-08-30 MERGED (#6077 f50bd72b03) + ∀A reduction ---
PR #6077 rebase-merged to main: A=4 slice PROVED, recursion verified A=3-6, reduction Lean
(recursion=>∀A tight slice) proved, operator-level -h^2(h^2+2) derivation (A=3). Also carried
the dp32 Magnus commits (MagnusPairingSignStructure.lean) -> #6057 now redundant (noted there).

∀A PROOF PROGRESS (milnor_recursion_forall_A_reduction_probe.py, verified A=3,4): 3 of 4 qtr-terms
proven A-INDEPENDENT ([2]^A): T1 loop-closure, T2 via [rho(braid),mu]=0, T3 scalar q^2h-hq^-2=h^2[2].
Recursion collapses EXACTLY to ONE identity (star-star): qtr_{A+1}(W e_A W^-1 e_A)=[2]^{A+1}(1-u)+u[2]qtr_A(W0),
u=q^2+q^-2. HONEST: an earlier conditional-expectation reduction of star-star's LHS was WRONG
(verification caught it); star-star is for the DIRECT 4th-term qtr. Recursive handle
E_A(w_A^-1)=E_A(b w_{A-1} b^-1)w_{A-1}^-1 verified (A=4). REMAINING: prove star-star ∀A (the single
open step). NOT yet ∀A-proven; no instance fabricated.

## 2026-08-30 (merged #6135, 3dd1ba12fb) — cap-cup weight corrected to μ⁻¹; (★★) pinned to trace level

The ∀A recursion D_{A+1}=−h²(h²+2)D_A is reduced to ONE identity and no further:
- 3 of 4 qtr-terms A-independent ∀A (qtr(e_A)=qtr(We_AW⁻¹)=[2]^A; scalar q²h−hq⁻²=h²[2]).
- The clean algebra (★★)⟹recursion is rigorous ∀A (eliminate the 4th term ⇒ 1−D_A=1+h²u·D_{A-1}).
- (★★) ⟺ trace identity (†'') qtr_{A-1}(P·F)=[2]^{A+1}(1−u)+u[2]qtr_{A-1}(P),
  P=ptr_μ(ρ(w_A)), F=ptr_{μ⁻¹}(ρ(w_A)⁻¹). Verified A=3,4.

Corrections vs last session (probe milnor_recursion_capcup_weight_probe.py, exact ℚ(q)):
- Cap-cup contraction weight is μ⁻¹, NOT μ. Clean sub-lemma ptr_{μ⁻¹}(e)=1; ptr_μ(e)=diag(q⁻²,q²).
  μ-weighted control fails — that was last session's bug.
- (†'') is a genuine TRACE identity: matrix form P·F=[2]²(1−u)1+u[2]P is FALSE at A=3,4.
  ⇒ the ∀A proof must be a trace/Brunnian argument, not linear algebra.
- No affine collapse: P not in span{1,ρ(w_{A-1}),ρ(w_{A-1})⁻¹}. Brunnian closures constrain but don't collapse.

STILL OPEN ∀A: proving (†''). No BrunnianDeficitRecursion instance created. Recursive handle
E_A(w_A⁻¹)=E_A(b·w_{A-1}·b⁻¹)·w_{A-1}⁻¹ (b=A_{A-1,A}, verified A=4) is the induction skeleton.
