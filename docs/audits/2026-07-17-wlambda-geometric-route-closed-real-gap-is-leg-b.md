# W_λ (m_p/m_μ): the geometric realisation is closed; the real open piece is leg (B), not a Ẑ/F_K search

**Date:** 2026-07-17 · **Axis:** W_λ keystone / Subgoal-2 (m_p, m_μ) · **Tier:**
synthesis (corpus-grep-gated; no new probe — a probe here would be a laundering
risk against an already-closed route) · **Discipline:** no fit, no c_k, nothing
wired, no tier change.

## Why this note runs no probe

Front 2 of the three-front plan was "the Lawrence–Rozansky modulus ID". The
closed-manifold SU(2)-fibre-coloring route was refuted this session (D=2 collapse,
merged `5766bb6c32`); the recon's suggested redirect was colored **Ẑ/F_K**
knot-complement blocks. The corpus-grep discipline (AGENTS.md §"Before declaring
open") requires checking the ledger first — and the s5-so3 keystone ledger
records the geometric realisation as **comprehensively refuted, with sources**,
across *all four* realisation routes:

1. Σ(2,3,5) golden **D=2** (the closed-manifold vacuum row is 2-dimensional);
2. Σ(3,4,5) **D=6** (wrong dimension);
3. **colored LR pure-sign** — the amplitude values are pure signs, not `d_q`
   (this is exactly the class the Ẑ/F_K redirect lives in);
4. q-Bessel (Tricomi + Hahn–Exton, free-scale families).

An Ẑ/F_K colored-block probe is a *variant of route 3* (colored knot-complement
LR amplitudes). Running it would at best re-derive the pure-sign refutation and at
worst manufacture a large-menu 1% graze (the entropy/PSLQ caution the ledger
already flags). **That is the laundering trap; this note declines it.**

## What actually answers the value step (redirect iii, formalized)

The ledger's standing answer is the **non-geometric** categorical "why":
`S_{0λ}/S_{00} = d_q` (Verlinde vacuum row), selected by Markov-trace uniqueness /
Wenzl bridge / Perron–Frobenius positivity (= confinement SDP). Since 2026-07-05
this is **formalized sorry-free across three legs + a capstone**:

- **(A) Frobenius** — quantum-dimension measure `d²/𝒟²` (`verlindeMeasure_eq_plancherel`);
- **(B) Perron–Frobenius** — `KeystonePerronFrobeniusGroundState.lean`: normalised
  positive fusion ground eigenvector pinned uniquely to `d_q` (`eq_d_of_normalized`);
- **(C) self-duality** — `KeystoneSelfDualSpectralNarrowing.lean`: `S²=C ⇒ S⁴=1`,
  eigenvalues 4th-roots-of-unity, vacuum row `C`-fixed;
- **capstone** — `keystone_value_map_pinned`: (A)+(B)+(C) ⇒ a positive normalised
  fusion-ground `S`-eigenvector **is `d_q`**.

Leg (C)'s `S⁴=1` narrowing is the ledger's stated *structural reason a
free-scale (geometric/q-Bessel) family cannot be the realisation* — i.e. the
geometric route is not merely unfound, it is structurally excluded from carrying
the self-dual `d_q` vacuum row. The closed-manifold D=2 collapse and the LR
pure-sign refutation are two faces of that same obstruction.

## The real open piece for m_p/m_μ

The value step (`W_λ = d_q`) is **answered and formalized**; it is not the m_p/m_μ
gap. The one remaining conditional is **leg (B)'s owner-gated physical instance**:
identifying the concrete fusion category whose PF-positive ground eigenvector is
the Hecke `d_q` (the `§3b-cond` `Prop`-class hypothesis in
`KeystonePerronFrobeniusGroundState.lean`, carrying the cited Ocneanu–Wenzl
up-to-scale uniqueness). That is a categorical-instance identification, **not** a
geometric-realisation / Ẑ-amplitude search.

**Redirect for m_p/m_μ effort (this note's contribution):** stop searching for a
geometric (WRT/Ẑ/F_K/LR) realisation of the value map — it is comprehensively
closed and structurally excluded by self-duality. Point Subgoal-2 effort at
leg (B): the physical fusion-category instance discharging `pf_proportional`. The
substrate-q₀ (μ–p pin) tension that m_p/m_μ actually miss on is a *separate* leg
(the q₀ derivation), not the value map.

## Cross-references

- Ledger (all refutations + redirect iii + the three legs): [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
- Value-step formalization: [`2026-07-05-keystone-selfduality-spectral-narrowing.md`](2026-07-05-keystone-selfduality-spectral-narrowing.md), `KeystoneValueMapSynthesis.lean`, `KeystonePerronFrobeniusGroundState.lean`, `KeystoneSelfDualSpectralNarrowing.lean`
- Closed-manifold LR refutation (this session, merged): `5766bb6c32`, [`2026-07-04-keystone-qhankel-eq2-vacuum-row-sourced-refutation.md`](2026-07-04-keystone-qhankel-eq2-vacuum-row-sourced-refutation.md)
- Front-3 companion (α_EM): [`2026-07-17-alpha-em-bring-jacobian-zeta-determinant.md`](2026-07-17-alpha-em-bring-jacobian-zeta-determinant.md)
