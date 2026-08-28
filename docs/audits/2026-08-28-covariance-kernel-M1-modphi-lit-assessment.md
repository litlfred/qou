# Covariance-kernel epic (`qou-x631`) — M₁>0 finite-n: assessment of the owner-provided quantitative CLT literature

**Date:** 2026-08-28 · **Branch:** `claude/m1-biane-concentration-effective-tool-2026-08-28` · **Tier:**
literature assessment (the right quantitative framework is now in hand; states precisely what it does
and does not close) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged.
**Epic:** `qou-x631`; gap `qou-k5r5`.

## Context

The finite-n step needs a **quantitative second-order (variance-convergence rate)** control for the
(CS) margin. The owner uploaded (commit `bdbcb2c9`) the papers that supply the framework:

| upload | paper | what it gives |
|---|---|---|
| `0501112` | Śniady, *Gaussian fluctuations of characters … and of Young diagrams* | second-order (variance/covariance) fluctuation structure via **higher-order free probability** + genus expansion |
| `1304.2934` | Féray–Méliot–Nikeghbali, *Mod-φ convergence I* | **explicit joint cumulant bounds** (Prop 11.10 / Rem 11.11), normality zones, precise deviations |
| `1705.10485` | *Mod-φ convergence II* | Berry–Esseen **speed-of-convergence** estimates (zones of control) |
| `1009.4034` | Méliot, *Kerov CLT for Schur–Weyl* | CLT for a related deformation |
| `0911.1038`, `0701051` | Dołęga–Féray(–Śniady), Stanley/Kerov character polynomials | structure of the character expansions |

## What the framework delivers (real, quantitative)

- **Mod-φ I, Prop 11.10 / Rem 11.11:** explicit bounds on the **joint cumulants** of the character-ratio
  statistics `X_ρ` (`χ̂^λ(ρ)`), with explicit constants and `n`-scaling; the cumulant convergence has
  **speed `O(1/n)`** (p96). This is exactly a *quantitative second-order* control — **for the
  character-ratio / polynomial-content-moment class.** `ω₃` (the 3-cycle character) is in this class.
- **Śniady `0501112`** gives the limiting fluctuation covariances of both characters **and Young-diagram
  shapes**, generalising Kerov's CLT — the leading second-order structure.

## What it does NOT close, and why (the recurring obstruction)

`M₁ = Cov_Planch(Σh, ω₃)` couples `ω₃` (character ratio — **covered**, with cumulant rate `O(1/n)`) with
`Σh = ΣD² + Σ|c|` (equivalently `Σλ_i²`). **`Σh ∉ A`** — it is transpose-invariant with odd leading
degree (`E~n^{3/2}`), proved earlier — so it is **not** a character ratio, a polynomial content moment,
or a free-cumulant polynomial. Every quantitative tool above (mod-φ cumulant bounds, Śniady genus,
Biane concentration) is built on that polynomial/character algebra. So:

- the **character leg `ω₃`** now has an explicit quantitative rate;
- the **shape leg `Σh`** has only its **leading** variance (Kerov/IO CLT — used to derive `κ` and the
  (CS) leading margin); its **variance-convergence rate** is still not furnished, because the machinery
  that provides rates does not reach outside the algebra `A`.

This is the exact quantitative-level echo of the `Σh ∉ A` obstruction that pruned the genus route in
Track A. Two further specifics sharpen it:

- **Plancherel is a degenerate case for mod-φ (mod-φ I, p97):** with `p_k(ω)=0` the mod-Gaussian
  parameters vanish and character fluctuations are order `n^{-k/2}`, not `n^{-1/2}`; the authors flag
  Plancherel as needing separate, harder combinatorics. So even the covered character side needs the
  Plancherel-specific renormalisation, not the generic theorem.
- The (CS) route needs the **variance** of `Σ|c|` (`∫|x|`, non-polynomial) and `ΣD²` (quadratic) — both
  outside the polynomial-moment class the cumulant bounds control.

## Honest status

- **The owner's lit is the correct quantitative framework** and closes the *character-side* rate
  (`ω₃`, cumulant speed `O(1/n)`). This is a real advance — the tool is no longer "not in the corpus".
- **It does not push-button-close `M₁>0`:** the persistent gap is the **variance-convergence rate for
  the non-`A` shape statistic `Σh`** (`Σ|c|`, `ΣD²`), which the character/free-cumulant/mod-φ machinery
  does not directly reach. Closing it needs either an extension of higher-order free probability / the
  Kerov-field mode-covariance corrections to this non-`A` statistic, or a direct estimate — a genuine,
  now precisely-scoped derivation.
- Gap `qou-k5r5` stays **OPEN**; leading order proved (#5901), `M₁>0` exact to n=78.

## Cross-references

- Finite-n step: [`2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md`](2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md)
- The `Σh ∉ A` obstruction (Track A): [`2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md`](2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md)
- Biane concentration (first-order, insufficient): [`2026-08-28-covariance-kernel-M1-biane-concentration-effective-tool.md`](2026-08-28-covariance-kernel-M1-biane-concentration-effective-tool.md)
- Gap bean `qou-k5r5`.
