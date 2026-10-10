---
# qou-1gix
title: 'Derivation route qou-ni4b: instantiate ColourStabilizerAction via the DV-Todorov M3(C) column module — build the Q-form of O = C + C^3 at the corpus fixed imaginary unit, exhibit injective Phi: su3 e -> End(C^3-analogue) (DV-T 1808.08110 Sec 3)'
status: scrapped
type: task
priority: normal
tags:
    - 8f-colour
    - reorg-2026-10-04
created_at: 2026-08-01T01:36:17Z
updated_at: 2026-10-10T14:47:26Z
parent: qou-8lxd
---

2026-08-02 session note: this is the medium-term colour-side child for the eightfold-way / SU3 queue attack; use it to keep colour SU(3) separate from the new flavor-SU(3) bean qou-d7h1.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Scrapped 2026-10-10 as superseded by `qou-ni4b` (the open question stays there)

The instantiation this bean asked for has landed, sorry-free:
`folio/quantum-observable-universe/lean/QOU/MathlibExt/OctonionColourActionBaseModule.lean`
proves `su3ToEndOct_injective` (line 59) and gives
`instance : ColourStabilizerAction ↥(su3 e) (Fin 8 → ℚ)` (line 68). Its own header
calls the instance **tautological**: `su3 e` is by construction a submodule of
`Der 𝕆 ⊆ End 𝕆`, so the inclusion is already injective, and the abstract class is
closed without touching the physics. The header names the remaining gap as
`qou-ni4b`, the Hecke-side instantiation.

One scope difference, recorded so it is not lost: the title asks for an injective map
into `End(ℂ³-analogue)`, while the landed instance acts on all of `𝕆 = Fin 8 → ℚ`, not
on the `ℂ³` summand. Neither version bears on the open content, which is whether the
three-strand Hecke state space carries the action. That is `qou-ni4b`, which stays
open. Rule 13a holds: no open conjecture is closed by scrapping this bean.

Found by the read-only 8f-colour pre-read (`/mnt/project-files/eightfold/8f-colour-preread.md`),
re-checked against `main` `3c0351a40d` before scrapping.
