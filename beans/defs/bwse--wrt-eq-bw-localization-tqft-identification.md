---
# bwse
title: 'bwS0-closure: WRT = BW-localization identification (irreducible cited input)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T00:30:00Z
updated_at: 2026-10-04T15:16:50Z
parent: qou-o9ge
---

2026-08-02 (branch claude/bwsc-level7-wrt-targets-2026-08-02): DECOMPOSED, still OPEN. New Lean file
`KeystoneRTSurgeryConstruction.lean` (lean-direct exit 0, sorry-free) formalizes the RT surgery
assembly — the object this bean names. It proves the modular-linear-algebra core (partitionSum =
Σ_λ S_{0λ}·colInv(λ) = Turaev's surgery formula; partitionSum_eq_dD: per-label weight IS d_λ/D;
vacuum_weight: S_{00}=1/D) and DERIVES bwS0_eq_hecke (bwS0_eq_dD_of_rt) from EXACTLY TWO named
irreducible inputs, everything else proved: (RT) bwS0 = the RT surgery weight S_{0λ} — the cited
Reshetikhin-Turaev/Turaev Kirby-invariance theorem (not Mathlib-formalizable without the full
ribbon-functor + Kirby calculus); and (BW=Hecke) the modular qDim = the Hecke d_q — the physics
identification (owner-gated). So bwse is now split into [proved assembly] + [cited pure-math RT
theorem] + [physics identification], each input content-bearing and correctly attributed. This does
NOT close bwse (§Axiomatization-is-NOT-a-Proof: the two inputs remain irreducible — one cited, one
physics). Corroboration that the RT weight hits the value map: level-5 exact (#4365) + level-7
numeric (keystone_lr_amplitude_level7.py, this branch).

Parent: bws0. The IRREDUCIBLE hinge. bwS0 (the abstract Chern-Simons path-integral vacuum row on
S^3/2I) = the WRT/LR amplitude is a TQFT theorem (Beasley-Witten non-abelian localization 2005;
WRT = CS partition function). This CANNOT be Lean-derived without formalizing Chern-Simons TQFT —
it is a cited physics/math input, NOT a fit. Honest disposition: carry it as a named citation
(beasley-witten, lawrence-rozansky) at the point where bwS0 is identified with the LR amplitude.
Full closure of bws0 = bwsc + bwsd proved, leaving ONLY this citation. Alternative epistemic path:
accept it as empirically validated (the ~200 ppb mass agreement) rather than Lean-derived.
