---
# qou-qs1x
title: 'GAP: flavour readout from γγ needs a word (product) of letters, and the photon letter orientation is underived'
status: in-progress
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
- [x] Per-letter readout from a WORD of letters. DONE 2026-11-15, see the result below. The h¹ part of a word is Σₖ cₖ·(word with letter k
      deleted), so the bits are recoverable iff those deleted words are linearly independent in NF. Test
      this on the nucleon word, exactly, before claiming anything.
- [ ] What fixes a photon's letter orientation (σ vs σ⁻¹)? Not derived. Check against qou-qs2u
      (u = polarization). Do not choose it.


## Result 2026-11-15: word readout (audit §4d; probe flavour_readout_word_probe.py; Lean sorry-free)

- **The bits are readable per letter except inside runs of same-generator letters**, which commute
  (`sameGen_letters_commute`). There, only the multiset is readable.
- **The h¹ part carries all the readable information:**
  - alternating word: (c₂,0,0,c₁,c₃,0), so all 8 assignments are distinct;
  - builder word σ₀σ₀σ₁: (c₃,0,0,0,c₁+c₂+1,0), so 6 are distinct.
- **At the builder placement:** the proton uud is unique; the neutron udd ≡ dud.
- **The (2,1) channel also merges uuu ≡ ddd on Δ**, because ρ(Δ⁻¹) = ρ(Δ) (the full twist is trivial on
  (2,1)): `rho_delta_inv`, `rho_delta_sq`.
- **Still open:**
  - what fixes the photon letter orientation;
  - which placement is canonical (qou-ales).

## 2026-11-15 — γγ-built nucleon (PR #7741, `h2_gg_atom/`, `h2_gg_electron/`; owner decision C)

On three strands every γγ word is a power of V = σ₀σ₁⁻¹, so a γγ-built nucleon is V^m. Pre-registered and measured: only V³ and V⁶ pass reading 3 at every level (m = 3…7); proton and neutron are then the same word, so there is no flavour on three strands. With a γγ electron (V³ or V⁶) H₂ passes every level and the only passing bond is V³. Every γγ word has χ_(1³) = 1 (#7896). Scope (a). Bearing on this bean: a three-strand γγ word cannot carry a flavour bit; per-letter readout needs letters outside V or more strands.
