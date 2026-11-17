---
# qou-ebs6
title: 'RULING: b_alpha-alpha 2.41 MeV is NOT closable — record the non-closability and its falsification condition'
status: in-progress
pr: 8327
branch: feat/qou-3lsb-3wxk-ebs6-se8k-wdij
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:47:13Z
updated_at: 2026-10-04T15:24:15Z
parent: qou-v2om
---

Arc bk-crossing mass-binding. Raised as the third of three candidate closures (with the
signed/unsigned multiplicity criterion and the n_α≥5 geometry, both of which CLOSED — PR #6252).
This one does NOT close, and this bean records why, so the next agent does not spend a session
rediscovering it or, worse, lands a fit.

## What it is
`bk-coordination-multiplicity.md`: B(n_α) ≈ n_α·B(⁴He) + N_bonds·b_αα, with N_bonds = C(n_α,2) and
b_αα ≈ 2.41 MeV read off AME (¹²C: 2.425, ¹⁶O: 2.406). The block ALREADY labels it honestly — "a
single empirical residual (the classical Hafstad–Teller value), not a derivation" — and says do not
wire until derived. Nothing here contradicts that; this bean supplies the evidence for how thin the
support actually is.

## Why it is not closable on present evidence — and the NEW argument
Three data points exist in the model's domain, and after the n_α≥5 geometry result that domain is
now provably small:

1. **QOU.Mass.EquilateralBound (PR #6252) shows the complete-graph bond count C(n_α,2) is
   GEOMETRICALLY UNREALIZABLE for n_α ≥ 5** — at most four mutually equidistant centres fit in ℝ³.
   So the model's own bond count is valid only for n_α ≤ 4.
2. Inside that valid domain the available nuclei are ⁸Be (n_α=2), ¹²C (3), ¹⁶O (4). **Exactly
   three points.**
3. b_αα is fitted on TWO of them (¹²C, ¹⁶O). The third, ⁸Be, gives ≈ 0 and is not predicted but
   EXCUSED ("consistent with being unbound relative to two α-particles").

**Net: one parameter, two fitting points, zero out-of-sample support inside the model's own domain
of validity.** The "near-constancy" of b_αα is the agreement of two numbers, 2.425 vs 2.406 — which
is what fitting one parameter to two points looks like whether or not the model is right. That is
not evidence for a derivable constant; it carries essentially no information.

This is a SHARPENING, not a refutation: nothing here shows b_αα is underivable in principle. It
shows the empirical support cannot distinguish a derived value from a fitted one, so a "derivation"
landed now would be unfalsifiable by the data it is calibrated against.

## Falsification / closure condition (what WOULD change the verdict)
A closure must do at least one of:
- **(a)** Derive b_αα from the 13 categorical drivers with NO AME input, and state the value BEFORE
  comparison — a genuine prediction, not a postdiction of 2.41.
- **(b)** Also account for ⁸Be ≈ 0 from the same construction rather than excusing it, turning the
  third point from an exception into a test.
- **(c)** Supply an independent out-of-sample point inside n_α ≤ 4, or extend the model with a
  DERIVED close-packing count valid at n_α ≥ 5 (note EquilateralBound bounds what is possible but
  does NOT derive that count).

## Standing recommendation
Do not attempt a derivation of b_αα as a target in itself. With one parameter and two points it is
the single easiest place in this arc to land a fit dressed as a derivation, and the anti-fit /
anti-laundering discipline would catch it only if the reviewer knows the DOF count — which is why
the count is recorded here. If b_αα falls out of a construction built for another reason, that is
route (a) and is welcome; reverse-engineering it is not.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`AlphaClusterContactCeilingAndDOFCount.lean`, `ExpansionParameterMismatchAndIMMEIsoscalarBlindness.lean`, `NonMonotoneBorromeanWordAndDisjointBlockEpsilonProduct.lean`) and verified at 50 dps in `computations/probes/alpha_contact_expansion_hierarchy_imme_blindness_nonmonotone_block_probe.py` (`computations/probes/alpha-contact-expansion-hierarchy-imme-blindness-nonmonotone-block-probe.witness.json`, `allPassed = true`). Opened PR #8327 (`ready: 826901651d0315e3267e85bf8f3b7fc2527847c3`).
