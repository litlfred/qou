The proton/neutron *difference* observables — the β-decay Q-value
$\mathfrak{Q}_\beta = \lvert\Delta(\mathrm{net})\rvert\cdot\mathfrak{E}_0$
([neutron Q-value](#prop:neutron-qvalue-symbolic)) and the binding
energy $B(K)$ — are computed in a definite **order of operations**: the
categorical difference $\Delta = x_{\mathfrak n} - x_{\mathfrak p}$ is
formed at the **fibre level**, and only then is the archimedean functor
$\tau$ applied. This proposition records *why* that order is forced, and
draws the line between what is **proved** and what is **expository
convention** — a point that is otherwise ambiguous.

**Proposition (delta is pre-archimedean).**
*Let $f$ be any fibre fold — the bar involution $q\mapsto q^{-1}$, the
Hecke antipode $\sigma_i\mapsto\sigma_i^{-1}$, or a Type-B fold — i.e.
any additive map on the fibre coefficient ring. Then for fibre
quantities $x_{\mathfrak n}, x_{\mathfrak p}$:*

$$
  f\bigl(x_{\mathfrak n} - x_{\mathfrak p}\bigr)
  \;=\; f(x_{\mathfrak n}) - f(x_{\mathfrak p}).
$$

*By contrast, the archimedean functor $\tau$ is **nonlinear** (it is a
$\mathrm{Li}_2^q$-tower / Markov-product / $\mathfrak{E}_0$-scaling), so
in general*

$$
  \tau(x_{\mathfrak n}) - \tau(x_{\mathfrak p})
  \;\neq\; \tau\bigl(x_{\mathfrak n} - x_{\mathfrak p}\bigr).
$$

## What is proved vs. what is expository (the clarification)

This distinction is easy to blur; the paper means all three of the
following, and only the first two are theorems:

1. **PROVED (fibre algebra).** A fold $f$ commutes with the categorical
   subtraction: $f(x_{\mathfrak n}-x_{\mathfrak p}) =
   f(x_{\mathfrak n})-f(x_{\mathfrak p})$. This is `fold_commutes_sub`,
   a one-line consequence of additivity over a generic commutative ring
   — **no reality, no archimedean input**. It is *why* the bar
   involution, the $\sigma\leftrightarrow\sigma^{-1}$ reduction, and
   Type-B folding may be applied freely inside the difference
   $\Delta(\mathrm{net})$ that defines $\mathfrak{Q}_\beta$ and inside the binding
   tower.

2. **PROVED (non-commutation of $\tau$).** A nonlinear functor does not
   commute with the difference: there exist $\tau, x_{\mathfrak n},
   x_{\mathfrak p}$ with $\tau(x_{\mathfrak n})-\tau(x_{\mathfrak p})
   \neq \tau(x_{\mathfrak n}-x_{\mathfrak p})$
   (`archimedean_does_not_commute_sub`, witnessed by $\tau=(\cdot)^2$).
   Thus the two orders — *masses-then-delta* and
   *delta-then-archimedean* — are different operations; one
   cannot be substituted for the other.

3. **EXPOSITORY CONVENTION (not a theorem).** *Which* order the paper
   uses for *which* observable is a modelling choice dictated by the
   physics, not forced by (1)–(2):
   - **Difference observables** ($\mathfrak{Q}_\beta$, binding $B$) are computed
     **delta-then-archimedean**: form $\Delta(\mathrm{net})$ in the
     fibre, then apply $\tau$ once via $\cdot\,\mathfrak{E}_0$. This is
     the canonical chain of [neutron Q-value](#prop:neutron-qvalue-symbolic)
     and the cheat-sheet step $\mathfrak{Q}_\beta = \lvert\Delta(\mathrm{net})\rvert
     \cdot\mathfrak{E}_0$. It keeps the fold discipline (1) available and
     keeps the imaginary parts of the archimedean tower cancelling in
     the difference.
   - **Absolute observables** ($m_{\mathfrak p}, m_{\mathfrak n}$
     individually) are computed **archimedean-then-(no delta)**: each is
     a full $\tau$-image of its own braid tower.

   The proton–neutron *mass split* $\Delta_{pn} = m_{\mathfrak n} -
   m_{\mathfrak p}$ may be read either way **only because** it sits at
   the boundary; the framework's *predicted* split goes through the
   difference observable $\mathfrak{Q}_\beta$ (plus the electron: $\mathfrak{Q}_\beta =
   \Delta_{pn} - m_e$), i.e. the delta-then-archimedean route.

## Why the order is forced for binding

Folding/unfolding is the engine of the binding/$\mathfrak{Q}_\beta$ derivations
(Hecke reduction to normal form, bar-symmetric channel sorting). By (1)
those folds commute with the pre-archimedean delta, so they are
legitimate moves inside $\Delta(\mathrm{net})$. By (2) the *same* folds
would **not** commute with the difference of two $\tau$-images. Hence:

> **Folding/unfolding works for binding precisely because binding is a
> pre-archimedean delta.** Computing the absolute masses first and
> subtracting would interleave the nonlinear $\tau$ with the
> subtraction, breaking fold-invariance and (empirically) over-
> amplifying the split by $\sim\!10^2$.

## Lean structure

`FibreFold R` bundles the one property the argument needs (additivity);
`fold_commutes_sub` proves $f(x-y)=f(x)-f(y)$ by `sub_eq_add_neg` +
`map_add` + `map_neg` over a generic `CommRing` — no `ℝ`, no ordering.
`archimedean_does_not_commute_sub` exhibits a concrete nonlinear
witness ($\tau=(\cdot)^2$ over $\mathbb Z$) closing by `norm_num`. The
fibre/observable level discipline matches the front-matter
$\mathrm{Im}(q)$ convention: the fold lives in the fibre; reality enters
only at $\tau$.
