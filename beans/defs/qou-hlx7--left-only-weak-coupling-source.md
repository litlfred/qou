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
updated_at: 2026-11-15T09:00:00Z
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
