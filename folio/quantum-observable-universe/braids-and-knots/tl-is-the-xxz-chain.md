The production Markov trace is the $\mathrm{SU}_q(2)$ / Temperley--Lieb one: a fibre of quantum dimension $[N]_q$ forces the Ocneanu parameter to satisfy $z\,[N]_q = q^{N}$, and at $N = 2$ this is the convention in use. What that fixes is an *algebra*; the present remark records what that algebra is as a mechanics.

Let $e_i$ denote the Temperley--Lieb generator acting on neighbouring tensor factors of $V^{\otimes n}$, with $V$ the two-dimensional fibre. Then

$$
  -2\sum_{i=1}^{n-1} e_i
  \;=\;
  H_{\mathrm{XXZ}}
  \;-\; \Delta\,(n-1)\,\mathbb{I}
  \;-\; \tfrac{1}{2}\bigl(q - q^{-1}\bigr)\bigl(\sigma^z_1 - \sigma^z_n\bigr),
$$

where $H_{\mathrm{XXZ}} = \sum_i \bigl(\sigma^x_i \sigma^x_{i+1} + \sigma^y_i \sigma^y_{i+1} + \Delta\,\sigma^z_i \sigma^z_{i+1}\bigr)$ and $\Delta$ is the anisotropy of the accompanying proposition. The right-hand side is the open $U_q(\mathfrak{sl}_2)$-symmetric chain on $n$ sites: the surface term proportional to $q - q^{-1}$ is what replaces the $\mathrm{SU}(2)$ symmetry of the isotropic chain by its quantum deformation, and it is a boundary term because the per-bond contributions telescope.

The identification is not an additional hypothesis. It follows from the two scalar identities recorded in the proposition, which are exactly the entries of the two-site operator in the singlet channel; the remaining entries are identically zero on both sides.

## Structural corollaries

Three follow without further input.

**The chain is gapped.** Since $\Delta > 1$ for every real $q \neq 1$, the chain sits in the massive regime. Bound states of several down spins --- Bethe strings --- are stable there, whereas in the massless regime they are not.

**The gap is small.** The relevant elliptic scale is $\exp\bigl(-\pi^2 / 2\log q\bigr)$, which at the aether is of order $10^{-21}$. The chain is therefore only marginally inside the massive phase, and any statement about its spectrum that is not uniform in $\Delta - 1$ should be treated as delicate.

**Bound states in one dimension need not be pairwise.** In the exactly soluble attractive case, an $n$-particle string binds as $n(n^2-1)$ rather than as the $\binom{n}{2}$ of a pairwise sum, an enhancement of $(n+1)/3$ over pairwise additivity. This is the shape of object the many-body binding term elsewhere in the framework is missing, and it is available here in closed form.

## Scope

The matrix identity above is verified numerically at both documented aether anchors, to the precision of the computation; the accompanying proposition establishes the scalar identities on which the two-site singlet decomposition rests. The coefficient of the boundary term was initially transcribed with the wrong sign, and the discrepancy was resolved by solving for the coefficients from the matrix entries; the witness script records this, and the coefficients should not be restored to a remembered form without re-running it.

Nothing here identifies the sites of the chain with any physical object. The claim is about the algebra the trace computes in, not about what it is a chain *of*.
