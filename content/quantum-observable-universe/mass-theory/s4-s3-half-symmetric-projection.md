**Proposition (conditional on
[`conj:borromean-baryon-mass-formula`](#conj:borromean-baryon-mass-formula)
— half-symmetric $H_4$ projection extracts one octahedral cell via
$S_4 \downarrow S_3$ branching).**
*The half-symmetric Wedderburn projection on $H_4(q)$, further
restricted to the $S_3$-trivial subspace (where $S_3$ acts by permuting
the three components of the Borromean rings $\mathcal{B}_3$), extracts
the curvature contribution of exactly **one** of the 8 ideal octahedral
cells in the $\mathcal{B}_3$-complement tessellation.*

## Structural role in $\mathrm{VolDensity}(\mathcal{B}_3)$ refinement

> ** reframing.** This section originally proposed a
> Yekutieli per-cell additive form
> $\lambda_{\text{scale}}^{\text{Yekutieli}} = \tfrac{5}{2} + (\tfrac{3}{4} - G)\,h^2$.
> That form was **purged from production** on (commit
> `71d674da1`) as non-canonical:  found the natural-reading
> bijection gives the per-cell curvature $\kappa = +0.5$, not $-G$,
> and no categorical derivation supplies a $-G \cdot h^2$ term.
> Per , the
> canonical mass formula is
> $$m(K) = m_e \cdot \mathrm{VolDensity}(K, q_0),$$
> with no separate $\lambda_{\text{scale}}$ constant.

The bijection $\tfrac{5}{2} \times \tfrac{2}{5} = 1$ established
above is a **structural input** that constrains how
$\mathrm{VolDensity}(\mathcal{B}_3, q_0)$ should evaluate at $h^2$
order on the half-symmetric Wedderburn subspace: exactly one of the
eight ideal octahedra of $S^3 \setminus \mathcal{B}_3$ is selected
by the combined H_4 half-symmetric projection and $S_3$-trivial
restriction. The bijection is sound combinatorics regardless of
any per-cell curvature value; it speaks to *which* cell contributes,
not *how much* it contributes.

The "how much" question — the per-cell curvature value — remains
open. The framework's current production prediction
$m_p \approx 965\;\text{MeV}$ ($+2.89\%$ vs CODATA) is the
$\mathrm{VolDensity}(\mathcal{B}_3)$ value at the framework's
current categorical-exactness order; refining that exactness at
higher $h^2$ orders is the open frontier (see the Family A gap
audit [`docs/audits/-family-a-gap-audit.md`](https://github.com/litlfred/qou/blob/claude/family-a-gap-audit-/docs/audits/-family-a-gap-audit.md),
currently in ;
relative path resolves once that PR merges).
This bijection is one of two structural inputs needed for the
refinement (the other being the $S_5 \leftrightarrow SO(3)$ fiber
action on Bring's surface).
