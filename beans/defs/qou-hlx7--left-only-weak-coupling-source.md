---
# qou-hlx7
title: 'GAP: source of the left-only weak coupling (V-A) — not a single Hecke letter'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - chirality
    - weak
parent: qou-qs0e
created_at: 2026-11-15T09:00:00Z
updated_at: 2026-11-15T10:30:00Z
---

Follow-up from qou-hlx6 (PR #7836). Corpus-grepped 2026-11-15 (beans, docs/audits,
content .md for "left-handed weak|parity violation|V-A|chiral weak|weak isospin"): no
bean tracks WHERE a chirality-selective (left-only) weak coupling comes from.

What is established:
- The corpus flavour flip s -> s^{-1} is chirality-blind: it inverts the eigenvalue on BOTH
  eigenlines (flip_eigen_plus / flip_eigen_minus, HelicityCommonSource.lean).
- no_one_sided_letter: an element inverting the eigenvalue on one eigenline only satisfies a
  Hecke relation at no parameter unless q^2 = 1. So V-A is not a single letter
  (scope (b) for that claim; scope (a) for V-A overall).
- Owner D-H1 = A (Hecke-parameter labelling; BW +q root = L), D-H2 = no (chirality stays on
  the cone side, 6b's polarization point u) — relayed by coordinator 2026-11-15.

Candidates to examine (not adopted):
- `predicted-spectra/force-knot-identification.md` attributes parity violation to the q != 1
  Skein sign-asymmetry q[L+] - q^{-1}[L-]; check whether that is chirality-selective in the
  eigenline sense or only crossing-sign-selective.
- A non-letter operator on the (2,1) block, or structure at higher tower depth.
- The cone-side coupling of u (6b, #7825) to the letter's eigenlines.
Related: qou-qs4c (lists "weak isospin acts on L only" as a relation), qou-tdrd (T3 grading).

## 2026-11-15 result: the corpus parity mechanism is eigenline-selective (proved)

q·s − q⁻¹·s⁻¹ = (q − q⁻¹)(q + q⁻¹)·P₊ exactly (skein_asym_eq, HelicityCommonSource.lean). It
kills the (−q⁻¹)-line, acts by q² − q⁻² on the q-line, vanishes at h = 0, and is bar-odd. The
mirror weighting and the swapped letter give P₋. It is h·[2]·(idempotent), not a letter, which
is the escape no_one_sided_letter leaves. NOT established: that the weak coupling IS this
(scope (a)), or how it composes with the flavour flip. Also noted: the content's skein
equation (RHS (q^{1/2}−q^{−1/2})[L0]) cannot be an identity in H_n(q); it reads as the Jones
skein after trace. Not edited. Owner decision D-H3 is framed in audit §8. Stays in-progress
pending D-H3.

## 2026-11-15 coordinator Q2: does knot chirality fix the L/R labelling? (audit §9)

The knot mirror is the flip σ ↦ σ⁻¹ on every letter, which preserves the eigenlines. The L↔R
relabelling σ ↦ −σ⁻¹ satisfies the Hecke and braid relations (swap_hecke, swap_braid), so it
is a re-presentation of the algebra. It equals the mirror on even words (swap_word2) and
−mirror on odd words (swap_word3). It sends e⁻ ↦ −e⁺ ≠ e⁻ (swap_electron, electron_ne_swap).

Verdict: fixing e⁻ as the positive word σ₀σ₁σ₀ fixes the labelling relationally. But the pair
(labelling, electron) is moved together by the relabelling, so nothing intrinsic selects it
(scope b): the choice is moved, not removed.

Content finding, reported and not edited: type-b-folding-cpt.md realises P as the braid
mirror, which is chirality-blind at letter level (scope a). Owner decision D-H4 is framed in
audit §9.

## 2026-11-15 D-H5 (A vs B for P), audit §10

The three letter maps flip σ↦σ⁻¹ (A), swap σ↦−σ⁻¹ (B) and neg σ↦−σ form a Klein four-group
(flip_neg, flip_swap, each an involution). Profiles:
- flip keeps helicity and sends e⁻ ↦ e⁺. It is not K-linear (no_linear_flip).
- swap exchanges helicity, sends e⁻ ↦ −e⁺, and is linear on the generators.
- neg exchanges helicity, sends e⁻ ↦ −e⁻, and is not K-linear (no_linear_neg).

Verdict: (A) has the C (or CT) profile and (B) has the CP profile. Neither is P. The P profile
is neg, under the reading that q↦q⁻¹ is non-physical, and neg does not exist at real q₀.

Tension reported (scope a): σ↦σ⁻¹ is the positron in the BW block and the d-flavour in 6a; it
cannot be C in both. No numbers used. Recommendation (judgement): D-H5 (D) now, (C) as a
separate bean.

## 2026-11-15 mechanism: the one-sided vertex is a non-letter, forced up to one bit

Session: https://claude.ai/code/session_01Qmmkt6YA78a79y4cG3D5Pk (sibling of coordinator
session_01M5GA1LmsEf8tSMxFjMkmnn). Lean `QOU/QuarkState/OneSidedWeakVertex.lean` (sorry-free,
lean-direct exit 0, axioms standard). Audit: docs/audits/2026-11-15-one-sided-weak-vertex.md.

- W_L := P+ s^-1 P+ + P- s P- = q^-1 J and W_R := P+ s P+ + P- s^-1 P- = q J, with
  J = P+ - P- = (s + s^-1)/[2], J^2 = 1, J bar-invariant (oneSidedL_eq, oneSidedR_eq,
  grading_sq, grading_flip). Neither is a letter (oneSidedL_not_letter).
- Forced given the line (eq_of_eigen_action, any ambient algebra). The line is a real binary
  choice: {W_L, W_R}, mutually inverse, swapped by bar (oneSidedL_flip). Scope (b) inside one
  letter for "the letter picks L".
- Observation (not identification): the nucleon word's ud letter s - h/2 = ([2]/2) J.
- Q_beta (probe qbeta_one_sided_weak_vertex_probe.py, no witness, dashboard untouched): base
  tr reproduced (-0.15419488504724); one-sided placements move |tr| by -83 % to +273 %,
  choice-dependent; L vs R differ. Markov trace is not chirality-blind, the word is.
- Ruled Q_beta trace is NOT bar-odd: f(q0) = -0.15419, f(1/q0) = +0.10929. "bar-odd sinh
  partner" belongs to the retired z = 1 form.
- Owner decisions D-W1 (take the bit from cone point u?) and D-W2 (scope the bar-odd label?)
  framed in audit section 7. Stays in-progress: the L/R bit source is open.
- Addendum (coordinator input, 9a's skein_asym_eq): [2]W_L = [2]s − (q s − q⁻¹ s⁻¹) and
  [2]W_R = [2]s − (q⁻¹ s − q s⁻¹), both sorry-free. The one-sided vertex is the letter minus
  the normalised skein difference. L vs R is exactly the weighting convention (which crossing
  carries q), and bar swaps both. 9a's risk is confirmed, scope (b) within one letter. Audit §8.
- 🛑 CORRECTION 2026-11-15 (own claim). The line above saying "bar-odd sinh partner belongs
  to the retired z = 1 form" was unmeasured and is FALSE. Retired Form A, the retired z = 1
  trace, and the ruled z_D trace all lack definite bar parity. The two traces only carry an
  overall factor h. Audit §4 corrected; follow-up question is bean qou-hlxp.

## 2026-11-15 D-W1 = A result: the cone point u cannot pick the bit equivariantly (scope b)

ConePointChiralityBit.lean (sorry-free, lean-direct exit 0, axioms standard). Algebra maps
preserve the L/R type (map_oneSidedL), so any assignment u -> vertex that is equivariant under
the unit-quaternion gauge is constant on orbits (type_invariant). Conjugation by j sends i to
-i, which is the photon swap. Hence tau(-u) = tau(u) (cone_point_cannot_pick_bit); a constant
convention satisfies the hypotheses (non-vacuity). Only the bar involution q -> 1/q swaps
W_L <-> W_R, so the bit IS the orientation of q (= which crossing carries weight q). Owner
decision D-W3 (convention / look for a q-orientation datum / stop) is framed in
docs/audits/2026-11-15-cone-point-chirality-bit.md section 6. Default: stop. The bean stays
in-progress: the conjecture (where V-A comes from) is open.

## 2026-11-15 owner decisions (relayed by coordinator)

D-H5 = D + C. (D): type-b-folding-cpt.md is scoped at fixed q. (C): the neg route is research
bean qou-hlxp. The mirror/positron vs d-flavour tension is bean qou-hlxt. The force-knot §III
fix (the coordinator's "D-H4 (b)") merged as #7852.

Also found, reported and NOT edited: `conj:p-from-braid-mirror` (mass-theory/p-from-braid-mirror.md)
defines P as σᵢ ↦ σᵢ⁻¹ with q held FIXED. no_linear_flip proves no K-linear algebra map of
H_n(q) does that unless q² = 1. So that P is well defined on the braid group B_n but does not
descend to H_n(q) at fixed q. The block also calls the bar involution "composite CPT", whereas
§10 finds the C/CT profile for the mirror.

## 2026-11-15 D-H3 derivation attempt (stream 9a, continued as a project thread)

Owner D-H3: record "weak vertex ∝ left projector" as an open conjecture AND try to derive
it. Branch claude/weak-vertex-left-projector-2026-11-15. Audit:
docs/audits/2026-11-15-weak-vertex-left-projector.md.

- DERIVED, one crossing (WeakVertexLeftProjector.lean): weakVertex − σ = −(q − q⁻¹)·leftLine
  (weakVertex_sub_letter), both regimes. Inside the letter algebra, killing the right line ⇔
  ∝ leftLine (one_sided_iff_smul_leftLine). Label-free skein form: weighting the positive
  crossing by its own eigenvalue of modulus > 1 gives (t − t⁻¹)(t + t⁻¹)·leftLine
  (skein_dominant_root), which closes the "which crossing carries q is a convention" caveat
  of force-knot-identification §III under the leftLine ruling. Relative to the ruled
  leftLine and the corpus weakVertex; no new input.
- EXACT NEGATIVE, weak knot (weak_knot_left_line_split_probe.py): τ_D((σ₁σ₂)⁵ P_R) =
  −q²/(q²+1)³ ≠ 0; right-line share −9.33 % at q₀. T(3,N): period 3, never zero.
- Owner asked (decision card) how to record: proposition + negative (recommended) /
  conjecture / audit only. No PR without the owner's go.
