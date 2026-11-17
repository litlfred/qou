---
# qou-v7ro
title: 'GAP: bridge Magnus coeff mu-bar(12..A)=+/-1 to the QOU Markov-trace deficit leading coefficient (close MilnorExactOrderConjecture)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:10:14Z
updated_at: 2026-10-04T15:12:48Z
parent: qou-m6dn
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

## Brick-3 RE-ROAST (2026-09-03) — DEFER stands, gap sharpened

Re-ran the 2026-08-31 brick-3 roast against machinery landed since (TwoRowStratum, TwoRowCapDerived, MagnusHookExteriorPower, MarkovWeightValueTransport, R5 qtr_kron→trace_kron #6425). Audit: docs/audits/2026-09-03-milnor-brick3-reroast.md.

VERDICT: DEFER still stands. R2 crux (concrete evaluable ρ(w_n) on V^⊗n + μ-weighted qtr) NOT filled — TwoRowStratum is a surjection STATEMENT (pre-Archimedean stub, no Mathlib Partition API); MagnusHookExteriorPower explicitly disclaims the concrete word rep ('outside Mathlib, numerical'); grep for a concrete reduced-Burau matrix def / two-row→2-dim sl2 evaluable rep returned EMPTY. BrunnianDeficitRecursion instance stays UNFABRICATED (honest open state; recursion proved+certified #6217, only Lean witness deferred).

BUT landscape shifted: (1) TwoRowCapDerived shrinks target to ≤2-row characters (exact ≥3-row vanishing), which reduce to 2-dim sl2; (2) lighter route now exists — reduced-Burau exterior-power character columns + landed esymm generating function (MagnusHookExteriorPower.prod_one_add_mul_eq_sum_esymm) + ≤2-row cap, avoiding the full 2^n V^⊗n operator; (3) R5 retired (#6425).

SHARPENED RESIDUAL GAP: Lean-derive w_n's two-row/reduced-Burau surviving spectrum ∀n, feed through esymm gen-fn + cap to reconstruct Q_n, close via DeficitRecursionReduction (#6228) glue. Upstream: qou-o6ov two-row character machinery (tr_{(k,1^{n-k})}=q^{L(1-j)}e_j). Smaller than 'all of R2'; still real work (position-indexed e_{n-1} on reduced space ∀n + Brunnian-word spectrum recursion).
## Brick 3 MINIMAL WEDGE landed (2026-09-03, PR #6466)

The R2 crux (concrete evaluable ρ(w_n)) is now supplied at the base case n=3, lean-direct exit 0 + axiom-clean. File QOU.MassTheory.BrunnianWordN3TwoRow (generic Field, sorry-free):
- w₃ = [A₀₁,A₁₂] = [σ₁²,σ₂²] in B₃, evaluated in the 2-dim reduced-Burau / (2,1) two-row irrep (the sorry-free heckeGen1/2 of GermRootVectorGaugeFixing) — the FIRST concrete ρ(w) in the arc.
- brunnianW3_eq (explicit 2×2), brunnianW3_det=1, brunnianW3_trace = exact χ^{(2,1)}(w₃).
- deficitA3_eq_closed_form: Schur–Weyl reconstruction [4]·χ^{(3)}+[2]·χ^{(2,1)} + D₃=1−qtr/[2]³ reproduces EXACTLY the certified D₃=h⁴(h²+3)/(h²+4). The concrete word closes to the certified recursion at A=3.

HONEST SEAM: Schur–Weyl duality itself ([4],[2] qdim weights, χ^{(3)}=1) is CITED as the def of survivingQTrace, not proved in Lean (Mathlib has no ribbon cat / quantum trace). BrunnianDeficitRecursion instance stays UNFABRICATED.

REMAINING (∀n body, still open): position-indexed e_{n-1} on the reduced (≤2-row) space ∀n + the Brunnian-word spectrum recursion. Upstream: qou-o6ov two-row character machinery. Blocked on the same categorical-trace infra gap as R2 (Jones/quantum-trace not in Mathlib) for the general-n closure.


## Note from qou-y98b (PR #6493, 2026-09-03) — your A=4 producer hardcodes the q0 pin

Not a request for action; a finding this arc should own the decision on.

**What I found.** `computations/deltalambda/milnor_a4_deficit_h_form.py`
(08bcf2524f, "exact A=4 Brunnian deficit in convention-D h-form") sets its
substrate modulus from a literal rather than from `q_parameter`:

    Q0 = sp.Rational("2584370278640139188197914756009",
                     "2328306436538696289062500000000")

      that value   1.1099785827513805166...
      canonical    1.1099785827513808075...   (proton pin, q_parameter.Q_50_DIGIT_STR)

Sixteen significant digits of agreement, then divergence. Relative deviation
2.62e-16. The denominator is 2^8 * 5^40, i.e. a decimal-exact rational built
from a ~17-digit decimal string — so NOT Fraction(float64), but carrying
float64's precision. The witness field is named `q0_pin_exact_rational`, which
is exact about the rational and silent about the pin.

**Why this does not change any of your numbers.** 2.62e-16 is inside the
framework's own 1 ppQ (1e-15) L1 target, and two orders of magnitude below this
probe's own comparison resolution — it checks against
`producer_tauL4 = sp.Rational(1000145898, 1000000000)`, nine digits. Everything
downstream of the substitution is exact sympy. I could not construct a way for
this to move the A=3 validation or the A=4 outcome.

**What I did, and deliberately did not do.** PR #6493 adds a producer-side
`q0Anchor: "proton"` with the above as its `q0AnchorReason`, so the witness
stops being unstamped and records its own provenance honestly. I did **not**
route the file through `q_parameter`, because that would move a committed number
inside your live arc and #6493 has no mandate here.

**The decision, and it is yours:**

- **Leave it.** Costs nothing, changes nothing, and the declaration now says
  plainly what the pin is. Risk: the literal cannot follow a re-pin, so if the
  proton anchor is ever re-derived (as the muon one was on 2026-08-28) this file
  silently keeps the old value while every routed producer moves. Commits you to
  re-checking it by hand at the next re-pin.
- **Route it through `q_parameter`** (`from q_parameter import Q_50_DIGIT_STR`;
  `Q0 = sp.Rational(Q_50_DIGIT_STR)` or the exact rational of it). Costs one
  line plus a re-run of this producer; the recorded numbers shift by ~1e-16 at
  most and no assertion of yours is near that. Buys immunity to re-pinning and
  matches what qou-aj91 is doing across the corpus. Risk: it does perturb a
  committed witness in an arc under active development, which is why I am not
  doing it unasked.
- **Rename the field** `q0_pin_exact_rational` -> `q0_pin_rational_16dp`, with
  or without either of the above. Nearly free; removes the only genuinely
  misleading part.

**Default if you do nothing:** the declaration from #6493 stands, the witness is
stamped `proton` with the provenance spelled out, and nothing else changes.

**My judgement (not a finding):** route it, on the next occasion you touch this
producer for a substantive reason rather than as a separate errand. The
correctness case is weak — nothing moves — but the re-pin exposure is real and
the fix is one line.

Blast radius, in real terms: `milnor-a4-deficit-h-form.witness.json` is the only
artifact, and grep finds no other producer or content block reading it.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 93 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/FaithfulWindowAndPretzelWronskianBrick.lean` with 80-dps probe `computations/probes/faithful_window_and_pretzel_wronskian_brick_probe.py` and witness `computations/probes/faithful-window-and-pretzel-wronskian-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8353 (`feat/qou-b9cj-uir6-upbq-v1eu-v4in-v7ro`, HEAD `026764a8eae99d01d2339d820089a669110ba022`).
