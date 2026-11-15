---
# qou-qs1x
title: 'GAP: flavour readout from γγ needs a word (product) of letters, and the photon letter orientation is underived'
status: todo
type: task
priority: normal
tags:
    - quark-state
created_at: 2026-11-15T08:45:00Z
updated_at: 2026-11-15T08:45:00Z
parent: qou-usxh
---

From qou-qs1d exploration (PR #7827, audit §4c; all statements below are proved, sorry-free).

- **Net flavour, the h¹ coefficient on the unit, is the only flavour datum D1 supplies.** It is additive.
  `letter_sum_flavour_swap` shows that a SUM of letters does not determine which letter carries which bit
  (residual freedom).
- **NF(γγ) with σ-letter photons has net flavour 0 identically** (`pairNF_netFlavour`). So uud and udd
  are not extractable from one pair: the set is empty (`pairNF_three_letters_all_up`; scope b, the
  invariant is net flavour).
- **Flavour comes only from flipped photon letters** (`pairBar_netFlavour`): it is an input, not
  produced by the collision.

Open:
- [ ] Per-letter readout from a WORD of letters. The h¹ part of a word is Σₖ cₖ·(word with letter k
      deleted), so the bits are recoverable iff those deleted words are linearly independent in NF. Test
      this on the nucleon word, exactly, before claiming anything.
- [ ] What fixes a photon's letter orientation (σ vs σ⁻¹)? Not derived. Check against qou-qs2u
      (u = polarization). Do not choose it.
