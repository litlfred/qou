# W1 formalize-first: the `I_𝓑₃ → F_Bor` bridge invariant (state before touching coefficients)

**Date:** 2026-07-25
**Scope:** formalize-first invariant + go/no-go for the unclaimed W1 bridge (binding workplan `2026-07-24-binding-mass-workplan-refresh.md` §4 item 1). **scope-(a); no fit, nothing wired, no `c_k`, L2 unchanged (2/7).** States the constraint a *derived* bridge must satisfy — deliberately **before** proposing any coefficient map, per the workplan's "derive, don't fit; formalize-first."

## The two objects (different variables, different TQFTs)

- **`F_Bor(h)` — the categorical density** in the proton identity `m_p = 2·m_μ·F_Bor − 12·m_e`:
  `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`, a series in the **substrate deformation `h`**
  (`h_expansion_F_Bor = {0:6, 1:−9, 2:19/2, 3:−57/8, …}`, exact rationals;
  `phase1d-f-bor-exact-h-expansion.witness.json`). Its substance is `tr_M(β_Bor)` — the
  **Markov trace / Jones (WRT) invariant** of the Borromean rings — the `[3]_q!/q³` being a
  fixed, exact dressing (Phase 1c: `h²(tr_M)=0`; `F_Bor`'s `h²=19/2` comes entirely from
  `[3]_q!` and `q³`).
- **`I_𝓑₃(Q)` — the Turaev–Garoufalidis 3D-index** of the Borromean complement
  (SnapPy `L6a4`), an **integer** graded series in the state-integral nome `Q`
  (`borromean-3d-index-graded.witness.json`: per-cusp table to `q⁶`, 729 peripheral classes,
  `S₃` cusp-permutation equivariant; `I_tot_meridian = [1, 6, 129, −510, −1205, 4004, 15898]`).
  A **DGG / 3d-3d-correspondence** object (BPS-state count), *not* a WRT/quantum-group trace.

## The bridge factors — substance is the first arrow

> `I_𝓑₃  --(A)-->  tr_M(β_Bor)  --(B: fixed)-->  F_Bor = |tr_M|·[3]_q!/q³`

Arrow **(B)** is already exact and proved (the `[3]_q!/q³` dressing). **All the content is arrow
(A): 3D-index → Markov trace.** This is *not* a within-one-TQFT `q`-specialization — it crosses
the DGG (3D-index) ↔ WRT (Jones) divide.

## The formalize-first invariant a *derived* (A) must satisfy

1. **Integrality.** `I_𝓑₃` has integer coefficients; `tr_M(β_Bor)` is an integer Laurent
   polynomial (Jones). A derived (A) is an **integer-preserving** map; every rational in `F_Bor`
   must arise **only** from the fixed `[3]_q!/q³` dressing (B), never from (A).
2. **`S₃` cusp equivariance.** `I_𝓑₃`'s per-cusp table is `S₃`-equivariant (verified). A derived
   (A) must respect the same symmetry — the Borromean rings' `S₃` permutation of components — so it
   is a map of `S₃`-representations, not a coefficient-by-coefficient ansatz.
3. **Variable identification is part of the claim, not free.** A derived (A) must *specify* how the
   state-integral nome `Q` relates to the substrate `h`/`q` (the 3d-3d dictionary), and that
   identification is fixed by the correspondence — it is **not** a tunable reparametrisation.
4. **Anti-fit boundary (STRICT).** The 2.89% gap between the categorical `Vol(𝓑₃)·ρ` and its exact
   value must **not** enter (A). Any map carrying a free real parameter chosen to close 2.89% is a
   fit, not a derivation, and is forbidden (three-calibration discipline; AGENTS.md §Δ_λ gate).

## Go/no-go verdict

**No naive bridge exists** at the level of a coefficient specialization: `I_tot_meridian` (integer
3D-index) and the Borromean Jones coefficients are invariants of **different TQFTs**, so (A) cannot
be a lookup or a within-model reparametrisation. A *derived* (A) is an instance of the **DGG 3d-3d
correspondence / quantum modularity** relating the 3D-index to the **colored-Jones asymptotics** —
for which the corpus already carries the natural substrate,
[`aj_borromean_colored_jones_tower.py`](../../computations/aj_borromean_colored_jones_tower.py)
(colored Jones tower) and the octahedral 4-dilogarithm machinery (#4127). That is the honest route;
it is **open** and genuinely deep, not a coefficient-matching exercise.

**Recommended next step (for a focused session):** compute the colored-Jones → 3D-index limit for
`β_Bor` on the tower producer, and test whether the 3D-index's integer data reproduces `tr_M(β_Bor)`
through the *established* quantum-modularity dictionary (no free parameters) — a pass/fail against
this invariant, not a fit.

-- Ref: [manuscript] docs/coordination/2026-07-24-binding-mass-workplan-refresh.md
