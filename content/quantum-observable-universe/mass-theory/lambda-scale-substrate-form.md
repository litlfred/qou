## Family A theorem (the proved, canonical content)

*Let $q_0 \in \mathbb{R}$ be the substrate parameter
([def:substrate-parameter](#def:substrate-parameter)), $h = q_0 - q_0^{-1}$
the Hecke deformation, and $\dim_q V_\lambda$ the q-deformed dimension of the
irreducible $H_4(q)$-module indexed by $\lambda \vdash 4$ (Frame–Robinson–Thrall
hook-content formula).*

**Theorem (Family A closed form).** *The half-symmetric Wedderburn-sum
projection at $H_4$ has the closed form*

$$
  \lambda_A(q) = \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
             = \frac{3 q^2 + 4 + 3 q^{-2}}{4}
             = \frac{5}{2} + \frac{3}{4}\,h^2,
$$

*with no $h^4, h^6, \ldots$ corrections; all odd-$h$ coefficients vanish by
$q \leftrightarrow q^{-1}$ symmetry.*
## Structural interpretation of the leading term

At $H_4(q)$ the partition spectrum is $p(4) = 5$; the half-symmetric count over
conjugate pairs (each pair weight $1$, the self-conjugate $(2,2)$ weight
$\tfrac12$) gives $1 + 1 + \tfrac12 = \tfrac52$. The structural identity
$\mathrm{Vol}(\mathcal{B}_3) = 8G$ ($G$ = Catalan; the Borromean complement is
8 ideal regular octahedra, $V_{\mathrm{oct}} = 4G$, per Adams 1985) is derived;
how the half-symmetric $H_4$ count drives the production `VolDensity(𝓑_3)`
refinement at higher $h^2$ order is the current research direction (not a
$\lambda_{\mathrm{scale}}$-from-substrate derivation).

## Witness

- the canonical formalism — the proved Family A closed form.
- [`docs/audits/2026-05-18-lambda-scale-derivation-search.md`](../../../docs/audits/2026-05-18-lambda-scale-derivation-search.md) — the falsified-form audit trail (moved out of the paper).
