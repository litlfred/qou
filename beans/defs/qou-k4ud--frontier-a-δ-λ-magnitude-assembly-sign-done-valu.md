---
# qou-k4ud
title: 'FRONTIER A: Δ_λ MAGNITUDE assembly — sign done (valuation); is |Δ_λ|=dim_λ closed-form? tr(g_ρ)→B wiring'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T03:32:44Z
updated_at: 2026-11-17T11:52:00Z
parent: qou-v2om
---


## SCOPING + ATTACK RESULT (2026-07-19)

**The magnitude is SETTLED, not open:** Δ_λ = (−1)^{n(λ)}·dim_λ (sign=valuation, |Δ_λ|=classical q=1 dim). The single-trace form Σ_λ y_λ χ^λ(β_D)(−1)^{n(λ)}dim_λ = −0.7439 → B(D)=0.380 MeV vs AME 2.2246 (−82.9%, under-binds ×5.85). Witnesses: deltalambda-magnitude-graded-trace, binding_energy_categorical_deuteron.

**The real wall = the He4-local ≥4-body cumulant b₄=−ln det(I+mS)**, structure DERIVED (b4_slater_antisymmetrizer_exchange_sign 7/7; Lean SU4SupermultipletGate + ReebPnMagnitude): eig(S)={±√5,±1} ⇒ det=(1−5m²)(1−m²), binding for 0<m<1/√5; SU(4) [1⁴] rank=C(4,A) vanishes A>4 (⁴He-locality structural); pp→+1, nn→−1 derived. OPEN: the scalar m∈(0,1/√5) + the pn sign + E0→MeV dressing.

**ATTACK on the icosahedral-m lead (Vector 2, docs/audits/2026-07-18-deltalambda-attack-vector-map.md):** probe `computations/deltalambda/b4_icosahedral_m_ceiling_probe.py` (2/2, scope-a, NO AME fit). The 1/√5 ceiling is genuinely √5/binary-icosahedral, BUT the primary Σ(2,3,5) objects OVERSHOOT it: S_00=0.526, S_01=0.851, φ⁻¹=0.618 all >1/√5=0.447 (unphysical as m); only secondary powers fall below (φ⁻²=0.382, 1/D²=0.276, sin²π/5=0.345), none structurally forced. So the lead does NOT yet supply a forward parameter-free m; picking by AME is the forbidden fit.

**KEY CROSS-LINK (Frontier A ↔ B):** the Σ(2,3,5) S-matrix lives at the root-of-unity FIBRE (|q|=1, unitary); the physical m (and τ=tr B, Frontier B qou-2v7k) live at real q₀. Both frontiers share the SAME fibre→observable archimedean-continuation wall (AGENTS.md Im(q) table). The continuation is the common bottleneck.

Status: magnitude sign+|Δ_λ| settled; b₄ structure derived; m/pn-sign open; icosahedral lead narrowed to "needs the archimedean continuation". Next = Frontier B (the shared wall).

## RECONCILIATION with Frontier B (2026-07-19): the shared wall is CONSTRUCTION, not continuation
Frontier B found the fibre→observable CONTINUATION is trivial (well-posed). So the A↔B cross-link is
sharper: the shared object is the icosahedral/Hecke S-matrix, and the shared WALL is the categorical
CONSTRUCTION (keystone: bwS0_eq_hecke S³/2I localization; b₄: a forward selection principle for m from
the identified S-matrix datum). Note the keystone's λ⊢5 Hecke S-matrix has sub-ceiling entries
(0.088/0.362/0.460), unlike the 2-block Fibonacci vacuum row (0.526/0.851) my ceiling probe used — so
"which icosahedral S-matrix" is itself part of the forward-m question. Neither is a continuation problem.

## #2 pn-sign attack (2026-07-19) — ALREADY SETTLED (corpus ahead; Frontier-A overstatement corrected)
The Frontier-A scoping listed "open pn sign" as a b₄ piece. Corpus check: it's PROVEN irrelevant for the
uniform b₄ magnitude — `QOU.MassTheory.ReebPnMagnitude.pn_sign_det_invariant` (sorry-free): conjugating
the uniform [1⁴] complete-graph exchange matrix by D=diag(1,1,−1,−1) flips every pn sign while fixing
pp/nn ⇒ det(1+S(a,w))=det(1+S(a,−w)). So NO determinant-class observable at uniform magnitude
distinguishes the two pn signs — the "open pn sign" (PR #3426) is unobservable in this class. Only
per-pair NON-UNIFORM framings break it (a separate, harder item — the ³H/³He mirror split, distinct
probes). So the only genuinely-open b₄ piece is the scalar m (Frontier A above), NOT the pn sign.

## RE-SCOPE (2026-07-19, PR #4084) — the b₄ scalar m is FOUND; the pole regulator is the open object
`b4_deformed_sspole_sector_probe.py` (forward, no fit, 6/6). Two exact facts resolve "icosahedral
overshoots the ceiling" and re-scope the open item:
- **FACT 1.** `(1+[2]_v²)·g_reeb² = 1` EXACTLY. The corpus-derived magnitude
  `g_reeb = 1/√(5+(q₀−1)²/q₀) = 1/√(1+[2]_v²)` IS the q-deformed A=4 ss-sector eigenvalue-criticality
  (I2, 2026-07-06 reeb provenance §2b), not a value "below 1/√5". The 4.9e-4 sub-ceiling gap is the
  classical(integer-5)-vs-deformed artifact (`1−5g²=2.2e-3>0` only via the q=1 integer). So there is NO
  sub-ceiling icosahedral entry to select — the physical m sits ON the deformed boundary. The
  reconciliation's "keystone λ⊢5 Hecke sub-ceiling entries" lead is therefore NOT a distinct forward-m
  source either: the boundary equals the derived magnitude.
- **FACT 2.** K₄(ppnn) writhe spectrum splits: ±√5 = species-SYMMETRIC (pp-sym,nn-sym) ss-modes
  (carry the pole, factor 1−5m²); ±1 = Pauli intra-pair antisym (finite at g_reeb, factor 1−m²). The
  divergent factor is the NON-Pauli α-condensation mode.
- **Consequence.** m=g_reeb is forward-derived (deuteron +0.41%); the single-scalar det(I+g_reeb·S)
  DIVERGES at the ss-pole — that IS the #3952 ⁴He 2.6–10.6× overshoot and the bareven ρ₄-forces-ρ₃
  failure, seen through the classical ceiling. Open b₄ object re-scoped: NOT "the scalar", but the
  POLE REGULATOR of the α-condensation mode (the near-critical ss-mode → finite ⁴He binding, ρ₄=13).
  Fully projecting the pole out (Pauli sector only) undershoots (b=0.223, deuteron-scale), so the
  regulator keeps the near-pole enhancement — a genuine open item, NOT to be fit (anti-fit stands).

Status: b₄ SCALAR m = g_reeb SETTLED (deformed ss-criticality); Vector 2 (icosahedral-entry=m) REFUTED
as stated; the open magnitude object is now the α-condensation pole regulator. Attack map §4a updated.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-19 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 88 Progress (`litlfred/qou#8330`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/SelfConjugateMultiplicityAndProlongationKernelBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all directory-mode static audits).
- **80-dps Probe & Witness**: `computations/probes/self_conjugate_multiplicity_and_prolongation_kernel_brick_probe.py` & `computations/probes/self-conjugate-multiplicity-and-prolongation-kernel-brick.witness.json` (`scriptCommitSha = b74bffb0d148592f3bcef84a6e80235048fdcaad`, HEAD `10687cdc1c1ca67ba352499264f665447671cbf9`, `allPassed = true`).
