**Conjecture.** *Let $H_n(q)$ be the Iwahori–Hecke algebra over a field $K$ of characteristic $0$ at generic $q$ ($q \neq 0$, not a root of unity), and let*

$$
  e_\lambda \;=\; \sum_{T \in \mathrm{SYT}(\lambda)} \; \prod_{k=1}^{n} \; \prod_{\substack{|d| \le n-1 \\ d \neq c_T(k)}} \frac{J_k - q^{2d}}{q^{2 c_T(k)} - q^{2d}}
$$

*be the Murphy–Lagrange element attached to a partition $\lambda \vdash n$, built from the Jucys–Murphy elements $J_1, \ldots, J_n$, where $c_T(k)$ is the content $j - i$ of the box of $T$ holding $k$ and $q^{2 c_T(k)}$ is its $q$-content. The inner product runs over every content $d$ a box of a partition of $n$ can have, so each factor is a Lagrange projector onto the eigenvalue $q^{2 c_T(k)}$ of $J_k$. Let $x \mapsto \overline{x}$ be the bar involution ($\sigma_i \mapsto \sigma_i^{-1}$, $q \mapsto q^{-1}$, antilinear) and $\#$ the sign twist ($\sigma_i \mapsto -\sigma_i^{-1}$, $q$ fixed). Then the four cross-checks*

1. *sum-to-identity — $\sum_{\lambda \vdash n} e_\lambda = 1$;*
2. *orthogonality — $e_\lambda e_\mu = \delta_{\lambda\mu} \, e_\lambda$, in particular idempotency $e_\lambda^2 = e_\lambda$;*
3. *bar-invariance — $\overline{e_\lambda} = e_\lambda$ for every $\lambda$, self-conjugate or not;*
4. *conjugate pairing — $\#(e_\lambda) = e_{\lambda'}$ for every $\lambda$, so $\#$ fixes $e_\lambda$ exactly when $\lambda = \lambda'$*

*all follow from Lagrange interpolation in the commuting variables $J_1, \ldots, J_n$.*

## Why this is stated separately

The cross-checks are what makes $e_\lambda$ *the* central primitive idempotent rather than merely an element of $Z(H_n(q))$, and they are the sole unproved input to
[Explicit central primitive idempotents $e_\lambda$ via Murphy elements](#prop:explicit-central-idempotent). That proposition is proved in Lean *conditionally* on them, with the class carrying them as an explicit instance hypothesis. Naming the conjecture as its own block is what lets the proposition's `uses[]` record the dependency, so the conditional cone is auditable from the manifest and not only from the Lean signature.

## Status in Lean

All four cross-checks are proved, sorry-free, on the real Iwahori–Hecke algebra `QOU.SchurWeyl.Hecke`, for every $n$:

- Cross-checks 1 and 2, and centrality: `explicit_central_idempotent_cross_checks` in `QOU.BraidKnot.ExplicitCentralIdempotentGeneral`. The Wedderburn isomorphism sends each Lagrange projector to a diagonal matrix unit (`JMProjector.heckeWedderburn_symm_single`). `mulProj_eq_proj` identifies the formula above, written in the multiplicative $J_k$, with that projector.
- Cross-check 3: `IsBar.fixes_centralIdem` in `QOU.BraidKnot.CentralIdempotentInvolution`. Every map with the bar properties fixes every $e_\lambda$. No bar map is constructed; that needs a field automorphism with $q \mapsto q^{-1}$.
- Cross-check 4: `hashMap_centralIdem` in `QOU.BraidKnot.CentralIdempotentSignTwist`. The sign twist is constructed from the universal property and sends $e_\lambda$ to $e_{\lambda'}$.

**Which involution pairs $\lambda$ with $\lambda'$.** The bar involution does not: it fixes every $e_\lambda$, so an earlier form of cross-check 4, $\overline{e_\lambda} = e_{\lambda'}$, is false already at $n = 2$. The bar involution is the symmetry of the convention-D Markov trace and of non-abelian Stokes path reversal. The sign twist is not a symmetry of that trace: it relates the trace at $q$ to the trace at $-q^{-1}$.

**Formula.** An earlier form took the inner product over the boxes of $\lambda$. Two boxes on one diagonal share a content, so that product can divide by zero (for example $\lambda = (2,2)$). The form above, over all contents $|d| \le n - 1$, is the one in [Explicit central primitive idempotents $e_\lambda$ via Murphy elements](#prop:explicit-central-idempotent).
