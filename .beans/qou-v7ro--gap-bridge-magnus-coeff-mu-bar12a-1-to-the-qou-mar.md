---
# qou-v7ro
title: 'GAP: bridge Magnus coeff mu-bar(12..A)=+/-1 to the QOU Markov-trace deficit leading coefficient (close MilnorExactOrderConjecture)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T23:10:14Z
updated_at: 2026-08-31T03:18:43Z
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

## 2026-08-30 — RECURSION PROVED ∀A (mathematically) by TL structural induction

D_{A+1}=−h²(h²+2)D_A is now PROVED for all A on the Temperley–Lieb Markov trace:
- (I) qtr(ρ(w_n))=[2]^n(1+h²)−h²Q_n [3 of 4 terms A-independent ∀n].
- (R) Q_n=qtr_{n-2}(c·B), c=ptr_{μ⁻¹}(ρ(w_{n-1})), B=ptr_{μ⁻¹}(ρ(w_{n-1})⁻¹) [cap-cup ptr_{μ⁻¹}(e)=1 + Markov].
- (C) coupled recursions B_m=[2](1+h²)1−h²(c_{m-1}⊗1)ρ(w_{m-1})⁻¹, c_m=[2](1+h²)1−h²ρ(w_{m-1})(B_{m-1}⊗1).
- (P) pairing qtr((c⊗1)ρ⁻¹)=qtr(ρ(B⊗1))=Q_{n-1} [μ↔μ⁻¹ trace-swap + cyclicity].
- (T) T4=h⁴[2]Q_{n-1} [cyclicity cancels ρ⁻¹ρ].
- assembly: Q_n=(1+h²)²[2]^n−uh²[2]Q_{n-1}, and (1+h²)²=1+uh² EXACTLY (u=h²+2), so
  Q_n=[2]^n(1+uh²)−uh²[2]Q_{n-1}; with (I) ⟹ D_n=−h²(h²+2)D_{n-1}. ∎ Base D_3.

Every step is a uniform TL/Markov/cyclicity identity; inductive step verified symbolically at n=5;
direct recursion A=3–6. Probe milnor_recursion_forall_A_proof_probe.py; audit
docs/audits/2026-08-30-milnor-recursion-forall-A-PROVED.md.

STILL OPEN (Lean only): the BrunnianDeficitRecursion INSTANCE is NOT created — the proof is on the
TL operator algebra (symbolic), not Lean-formalized. Discharging the instance requires formalizing
the TL machinery (quantum trace, cap-cup, Markov) in Lean — mechanical formalization work, not a
mathematical gap. Bean stays in-progress for that Lean formalization.

## 2026-08-30 (option #3, brick 1) — concrete spin-½ TL relations formalized in Lean

QOU.MassTheory.TemperleyLiebSpinHalf (Mathlib-only, generic [Field K], sorry-free, lean-direct
exit 0, axioms {propext,Classical.choice,Quot.sound}):
- eTL = q•1 − R (TL generator = q − Hecke R-matrix)
- eTL_mul_eTL: e² = [2]·e (defining TL relation)
- ptr_muInv_eTL: ptr_{μ⁻¹}(e) = 1 (the cap-cup weight correction — the crux μ⁻¹, now Lean)
- ptr_mu_eTL: ptr_μ(e) = diag(q⁻²,q²) (the contrast that forces μ⁻¹)
- band = q²•1 − h·e, bandInv = q⁻²•1 + h·e, band_mul_bandInv = 1

This is brick 1 of the BrunnianDeficitRecursion instance: the 2-strand/4-dim atomic relations the
∀A induction composes. STILL OPEN for the instance: the ∀n tensor-power quantum trace, ρ(w_n), and
the composing induction. No instance fabricated.

## 2026-08-31 — Lean formalization of the instance: bricks landed

The ∀A recursion is PROVED mathematically (#6217) and being formalized toward the
BrunnianDeficitRecursion instance (no instance fabricated). Progress:

- #6228 DeficitRecursionReduction (merged): field-algebra core — (I)+Q-recursion ⇒ D-recursion,
  sorry-free, generic field.
- #6268 TemperleyLiebSpinHalf (merged): BRICK 1 — concrete spin-½ TL relations (e=q−R, e²=[2]e,
  ptr_{μ⁻¹}(e)=1 the cap-cup crux, ptr_μ(e)=diag(q⁻²,q²), band σ²=q²−he + inverse). sorry-free.
- BRICK 2 (in progress, this branch): the ∀n weighted quantum trace — Kronecker multiplicativity
  qtr_{D₁⊗D₂}(X₁⊗X₂)=qtr(X₁)·qtr(X₂) and the loop tower qtr(1)=[2]^n. These are the two
  dimension-general facts identity (I) rests on (the [2]^n / [2]^{n-1} factors + the We_AW⁻¹
  juxtaposition term).

REMAINING for the instance (brick 3+): the Brunnian word ρ(w_n) as a concrete operator ∀n, the
e_{n-1} embedding qtr(e_{n-1})=[2]^{n-1}, and the composing induction. Mathlib has no knot theory,
so ρ(w_n) must be built from the R-matrix on tensor powers. Large; multi-session.

## 2026-08-31 — ROAST of brick 3 (feasibility red-team). Verdict: DEFER, banked bricks 1-2.

Evidence-based assessment (docs/audits/2026-08-31-milnor-brick3-roast.md). The QOU tree has MORE
relevant infra than 'Mathlib has no knot theory' suggested: abstract TemperleyLiebAlgebra (RingQuot,
∀n, universal property, TL_{n+1}), IwahoriHeckeAlgebra, HeckeRep (.eval/.character), MarkovTrace
(cyclic+conj lemmas), MarkovTraceMultiplicative (markovTrace_kronecker), OcneanuTrace, MarkovMoves,
YBE. BUT none computes the convention-D spin-½ μ-weighted quantum-trace deficit the recursion is about.

Five obstacles:
- R1 WRONG TRACE: HeckeRep.character is the un-normalised SINGLE-IRREP PLAIN matrix trace over
  ℤ[t,t⁻¹] (its own §Scope note) — not the y_λ-weighted, not normalised (tr_M(1)=1), not the
  μ-weighted qtr the deficit uses.
- R2 NO CONCRETE REP (the crux): r_matrix_braiding_structure is an ABSTRACT RMatrixBraidingContext
  (YBE on opaque R12/R13/R23); no concrete R̆ on V^⊗n ∀n, no position-indexed e_i/R_i on tensor
  powers satisfying TL relations ∀n. Brick 1 built e=q−R only at 2 strands. This is unbuilt and is
  the single hardest piece.
- R3 word tower: BraidWord n is fixed-n; the {w_n} family + strand embedding + ρ(w_{n-1})⊗1 must be
  built (doable, not free).
- R4 substance all new: (I), cap-cup reduction, coupled c/B recursions, pairing, T4 are
  representation-specific and unformalised; abstract TL relations don't supply them.
- R5 PARALLEL TRACK + self-correction: my bricks 1-2 (concrete Fin4/Fin n→Fin 2 μ-weighted) do NOT
  connect to HeckeRep/MarkovTrace; brick2 qtr_kron OVERLAPS MarkovTraceMultiplicative.markovTrace_kronecker
  (mine is the weighted generalization — I should have grepped BEFORE writing it). A design fork is
  forced (my model vs HeckeRep).

Verdict: brick 3 crux ≈ 'formalise the TL/Hecke Markov-trace REPRESENTATION on tensor powers' — a
multi-session project buying assurance not new math (recursion already proved+certified #6217). DEFER.
Bank bricks 1-2. If pursued: (3a) pick track + bridge qtr_kron↔markovTrace_kronecker; (3b) e_i on
V^⊗n ∀n (R2 crux); (3c) w_n tower; (3d) (I)+cap-cup+induction, close via #6228 glue. Instance stays
unfabricated (honest open state).
