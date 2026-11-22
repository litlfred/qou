---
# qou-em1j
title: 'twwf n=3: Poincaré poly ∑_{w∈S_n} q^ℓ(w) = [n]_q! — the T_w Gram RHS'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-31T20:00:58Z
updated_at: 2026-11-22T21:30:49Z
parent: qou-1oif
---

## Round 64 Progress (`lane-e667`)
- Formalized `qou-7xt3`, `qou-ck0g`, `qou-em1j`, `qou-kbjc`, `qou-w0zn` in `QOU.Foundations.ThreeCellPosetOrbitSizeBarSymEigenvalueLengthGeneratingQBinomialUpDownWeyl` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 directory-mode static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = 13e718201144523610e11912018cdb123e6155b3`, `COMMIT2 = 06940a10b90934e8a8d7233d592147be01aa5979`, `scriptHash = 01e1202f7b26`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8323 (`ready-to-merge`, `release`, `ready: 06940a10b90934e8a8d7233d592147be01aa5979`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8323, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-22 — proved for every n, on branch claude/hecke-sw-bean-drain-2026-11-22 (wave-2 drain)

`QOU.MathlibExt.SymmetricGroupPoincare.sum_pow_length`: Σ_{w∈S_n} q^{ℓ(w)} = ∏_{i<n}(1+q+⋯+q^i) over any commutative semiring, ℓ = `PermutationEnumeration.coxeterLength`; `sum_pow_length_three` is this bean's n = 3 case. Proof: first-value insertion `ins p τ` is a bijection Fin(n+1)×S_n → S_{n+1} with ℓ(ins p τ) = p + ℓ(τ). lean-direct exit 0, axioms [propext, Classical.choice, Quot.sound]. Commit 4fe9541d9. Close when merged; PR waits on the owner.

## 2026-11-22 applicability verdict (hecke-schur-weyl-lean drain): APPLIES. No retired premise (photon form, electron, convention C, z=1 base, census, absolute mass, muon pin A) appears; the content is pure Hecke/S_n algebra, independent of today's rulings. Proved for every n in PR #9132 (open); close on merge.
