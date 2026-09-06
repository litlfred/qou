# The elliptic-θ idea for `c₃` — refutation, redirect, and the resurgence-modularity synthesis (2026-07-25)

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**PR:** #4189. **Branch:** `claude/elliptic-r-theta-ck-2026-07-25`.
**Origin:** owner intuition — `sinh/cosh` (bar-odd/bar-even) are not independent;
the R-matrix / transfer matrix mixes them; perhaps a q-elliptic function for the
q-heat kernel closes `c₃` / mass binding.

## What is solid (proved / structural)

- **Tier degeneration** (`EllipticRTheta.lean`, verified): the Hecke combos
  `q ± q⁻¹ = 2cosh/2sinh` are the trigonometric (`τ→i∞`) degeneration of the even/odd
  Jacobi theta; `eᵘ = cosh u + sinh u` is the θ-even ⊕ θ-odd split. The
  Belavin–Drinfeld tier rational → trigonometric → elliptic is real, and the
  bar-even/bar-odd = θ-even/θ-odd identification is exact.
- **The Faddeev uniqueness ratio is elliptic** (`faddeevPhi_mul_elliptic`, PR #4155)
  on the lattice `⟨ib, i/b⟩`, modular parameter `τ = 1/b²`
  (`faddeev_modular_parameter`). Elliptic functions ARE the natural gauge objects
  here — the structure is genuinely present.

## What is REFUTED (scope-a, quantitative)

The naive reading — *the `c₃` cross-anchor swing is the elliptic correction of the
Faddeev period lattice* — **fails by 40+ orders of magnitude.** At real `q₀ > 1`
(`q = e^{iπb²}`), `τ = 1/b² = iπ/ln q₀ ≈ 30.1i`, so the lattice sits deep at
`τ→i∞`; the nome is `e^{2πiτ} ≈ 1e-83` (dual `e^{iπτ} ≈ 1e-42`), against a swing of
`2.4e-2` (`elliptic_r_theta_single_tau_probe.py`). This is exactly WHY `sinh/cosh`
already works: the Faddeev lattice is trigonometric at real `q₀`. The elliptic
freedom of the uniqueness ratio is a **different** elliptic structure and does not
carry the swing.

## The synthesis — resurgence ⇔ modularity (the honest reconciliation)

The apparent tension — the corpus treats the bar-odd swing as **resurgent** (KC22:
the `D(ũ)` ladder is non-`q`-holonomic; Écalle–Borel median resummation,
`ecalle-borel-resurgence-vocabulary.md`; the `1/u³` `BarOddLadderShape`), whereas
an elliptic/modular object is holonomic — **dissolves** under the
**resurgence-modularity correspondence** (Garoufalidis–Gu–Mariño state integrals;
Zagier quantum modular forms): *the Stokes constants of a resurgent asymptotic
series ARE modular data.* The two descriptions are one object seen through Borel
vs modular lenses.

Concretely for QOU:

- the bar-odd swing is resurgent, its **Stokes constant is `A_ω`** — the very
  keystone worked this session on the uniqueness leg (#4155) and #3805;
- `A_ω` is the **modular / Stokes datum** of the figure-eight state integral, living
  on the **geometric** structure — the `4₁` A-polynomial / holonomy curve at the CM
  point `q² = e^{iπ/3}` (disc `−3`, `j = 0`), where θ-values are algebraic — **not**
  the Faddeev period lattice;
- so the owner intuition is realized: `c₃` (bar-odd) and the mass channel (bar-even)
  share one modular structure — but it is the **resurgent-modular `A_ω`** (a quantum
  modular form / GGM Stokes constant), not a Faddeev-lattice elliptic correction.

## Net

| Claim | Verdict |
|---|---|
| bar-even/bar-odd = θ-even/θ-odd (tier degeneration) | proved |
| Faddeev uniqueness ratio is elliptic (`τ=1/b²`) | proved |
| the `c₃` swing = Faddeev-lattice elliptic correction | **refuted (scope-a)**, 40+ orders too small |
| the `c₃` swing is governed by modular data | **plausible** — via resurgence-modularity, as the `A_ω` Stokes constant |
| that modular data lives on the Faddeev lattice | **no** — on the geometric A-poly / CM curve |

**Redirect (correctly pinned):** the elliptic/θ structure for `c₃` is the
**resurgent-modular `A_ω`** on the figure-eight geometric curve — i.e. this front
**merges into the existing A_ω / GGM keystone program** (#3805 and the uniqueness
leg #4155), not a separate elliptic-R construction. The `SingleTauChannelClosure`
class stays open; its `τ` should be read as the quantum-modular parameter of `A_ω`,
not `1/b²`. No fit; scope-(a) throughout.
