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
updated_at: 2026-11-15T12:00:00Z
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
