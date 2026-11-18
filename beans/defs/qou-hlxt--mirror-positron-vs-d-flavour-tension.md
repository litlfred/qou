---
# qou-hlxt
title: 'Tension: σ ↦ σ⁻¹ is the positron (BW) and the d flavour (quark_template / 6a) — which reading is derivable?'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - flavour
    - charge-conjugation
parent: qou-qs0e
created_at: 2026-11-15T10:00:00Z
updated_at: 2026-11-15T18:20:00Z
---

Owner, relayed by coordinator 2026-11-15: open this bean and frame it; do NOT resolve it by
choice.

## The tension

- `rem:breit-wheeler-vertex` (`mass-theory/breit-wheeler-vertex.md:34-36`): e⁺ is the mirror
  word σ₀⁻¹σ₁⁻¹σ₀⁻¹ of e⁻ = σ₀σ₁σ₀. So σ ↦ σ⁻¹ is particle ↦ antiparticle, i.e. C-like.
- Stream 6a (`QOU/QuarkState/PhotonPairNormalForm.lean`, `quarkLetter`) and
  `computations/probes/quark_template/`: the flavour bit is σ (u-type) vs σ⁻¹ (d-type). So
  σ ↦ σ⁻¹ is u ↦ d.
- Physical C sends u to ū, not to d, so one map cannot be C in both places.
- Proved context: σ ↦ σ⁻¹ keeps the eigenlines (`flip_Pp`) and is not a K-linear algebra map
  (`no_linear_flip`). On leptons it has the C (or CT) profile (audit §10).

## Which reading is DERIVABLE? Options, none adopted

**(1) Mirror = antiparticle everywhere; the quark flavour bit needs another source.**
- Means: the d quark is not σ⁻¹; 6a's flavour extraction is re-read as an antiquark bit.
- Costs: re-deriving 6a's flavour shift; the nucleon uud/udd needs a new flavour carrier.
- Risks: 6a's net-flavour results (scope b), stated for σ vs σ⁻¹, need re-scoping.
- Commits to: C = mirror.

**(2) Mirror = flavour orientation everywhere; the positron needs another source.**
- Means: e⁺ is not the mirror word, and the BW block's pairing is re-derived.
- Costs: re-derivation of the BW vertex.
- Risks: the e⁻/e⁺ trefoil-chirality picture is lost.
- Commits to: σ ↦ σ⁻¹ being a weak-isospin-like flip.

**(3) Leptons and quarks are different sectors in which the same map plays different roles.**
- Means: a sector-dependent reading.
- Costs: a stated, derived reason the sectors differ.
- Risks: per-case dispatch is a fitting form (AGENTS.md, NO FITTING); it needs a derivation,
  not convenience.
- Commits to: a sector structure.

**(4) Neither is C; C is a different map.** The corpus has `conj:c-from-color-flavor-swap`,
which acts on colour-sheet flavour labels with no Hecke-generator action.
- Means: the mirror is CT, or a flavour flip, in both blocks; the BW "positron" wording is
  scoped.
- Costs: checking c-from-color-flavor-swap against the letter algebra.
- Risks: the BW block's e⁺ identification becomes a model statement.

**Default if nothing is decided:** nothing changes; both blocks stand and this bean records
the tension.

**Recommendation (judgement):** check (4) first against `conj:c-from-color-flavor-swap` in
Lean, because it uses only existing corpus objects. No reading is chosen by reproducing a
label or a number.

## 2026-11-15 what the colour-tube sign rule already says (PR #7952, issue #7951)

A third corpus source bears on the tension. `conj:inter-nucleon-channel-color-tube` gives
each colour-sheet contact a sign: +1 (σ) for the same flavour, −1 (σ⁻¹) for a flavour
against its antiflavour, and 0 (the averaged crossing ½(σ+σ⁻¹)) for mixed flavours.
`ColourTubeMirrorReading.lean` (sorry-free) proves from that rule:
- σ⁻¹ occurs exactly at f against f̄, and never between two matter flavours;
- a u–d contact gets the averaged crossing, not σ⁻¹;
- proton and neutron contacts never carry σ⁻¹.

So two sources (Breit–Wheeler, colour tube) read σ⁻¹ as the antiparticle contact, and only
stream 6a's `quarkLetter` reads it as d. The colour tube's u–d element is the one #7948
showed the weak vertex is a scalar multiple of. Caveat: the sign rule is stated data of the
upstream conjecture (its open question 2), so this counts sources and does not derive a
reading. Option (1) gains corroboration; nothing is chosen. Status stays todo.
