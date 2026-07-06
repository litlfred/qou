The proton/neutron difference observables—the $\beta$-decay Q-value $\mathfrak{Q}_\beta = \lvert\Delta(\mathrm{net})\rvert\cdot\mathfrak{E}_0$ ([neutron Q-value](#prop:neutron-qvalue-symbolic)) and the binding energy $B(K)$—are computed in a specific order. The categorical difference $\Delta = x_{\mathfrak n} - x_{\mathfrak p}$ is formed at the fibre level, and only then is the archimedean functor $\tau$ applied. We record why this order is forced and distinguish between proved statements and expository conventions.

**Proposition.** Let $f$ be any fibre fold (the bar involution $q\mapsto q^{-1}$, the Hecke antipode $\sigma_i\mapsto\sigma_i^{-1}$, or a Type-B fold). Since $f$ is an additive map on the fibre coefficient ring, for any fibre quantities $x_{\mathfrak n}, x_{\mathfrak p}$:

$$
  f\bigl(x_{\mathfrak n} - x_{\mathfrak p}\bigr)
  \;=\; f(x_{\mathfrak n}) - f(x_{\mathfrak p}).
$$

By contrast, the archimedean functor $\tau$ is a nonlinear $\mathrm{Li}_2^q$-tower / Markov-product / $\mathfrak{E}_0$-scaling. Thus, in general:

$$
  \tau(x_{\mathfrak n}) - \tau(x_{\mathfrak p})
  \;\neq\; \tau\bigl(x_{\mathfrak n} - x_{\mathfrak p}\bigr).
$$

## Fibre algebra vs nonlinear functors

This establishes two theorems:

1. **Fibre folds commute with subtraction.** A fold $f$ commutes with the categorical subtraction. This relies on additivity over a generic commutative ring, with no archimedean input. It allows the bar involution, the $\sigma\leftrightarrow\sigma^{-1}$ reduction, and Type-B folding to be applied inside the difference $\Delta(\mathrm{net})$ and inside the binding tower.
2. **Archimedean functors do not commute with subtraction.** A nonlinear functor does not commute with the difference. The two operations—masses-then-delta and delta-then-archimedean—are distinct.

The choice of which order to use is an expository convention dictated by physics:

- **Difference observables** ($\mathfrak{Q}_\beta$, binding $B$) are computed via **delta-then-archimedean**. We form $\Delta(\mathrm{net})$ in the fibre, then apply $\tau$. This preserves fold invariance and cancels the imaginary parts of the archimedean tower in the difference.
- **Absolute observables** ($m_{\mathfrak p}, m_{\mathfrak n}$) are computed via **archimedean-then-(no delta)**. Each is a full $\tau$-image of its own braid tower.

The proton–neutron mass split $\Delta_{pn} = m_{\mathfrak n} - m_{\mathfrak p}$ sits at the boundary. The framework's predicted split evaluates via the difference observable $\mathfrak{Q}_\beta$ (plus the electron: $\mathfrak{Q}_\beta = \Delta_{pn} - m_e$), following the delta-then-archimedean route.

## Necessity of the ordering for binding

Folding and unfolding drive the binding and $\mathfrak{Q}_\beta$ derivations. By the first theorem, these folds commute with the pre-archimedean delta, making them legitimate moves inside $\Delta(\mathrm{net})$. By the second theorem, they do not commute with the difference of two $\tau$-images. Thus, folding works for binding precisely because binding is a pre-archimedean delta. Computing the absolute masses first and then subtracting would interleave the nonlinear $\tau$ with the subtraction, breaking fold-invariance.

## Lean structure

`FibreFold R` bundles additivity. The lemma `fold_commutes_sub` proves $f(x-y)=f(x)-f(y)$ over a generic `CommRing`—no `ℝ`, no ordering. The lemma `archimedean_does_not_commute_sub` exhibits a concrete nonlinear witness. The fold lives in the fibre; reality enters only at $\tau$.
