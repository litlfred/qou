*Lean sibling: generic commutative ring, no archimedean input (AGENTS.md §7c);
library module `QOU.FluidDynamics.TwoVortexChannelAlgebra`.*

**Proposition (channel algebra of the two-vortex interaction).** *Let $R$ be a
commutative ring carrying elements $e_+, e_-, \sigma, q, u$ satisfying*

1. *(partition of unity)* $e_+ + e_- = 1$;
2. *(orthogonality)* $e_+ e_- = 0$;
3. *(inverse witness)* $q\,u = 1$;
4. *(spectral form)* $\sigma = q\,e_+ - u\,e_-$.

*Then:*

- *(derived idempotency)* $e_+^2 = e_+$ *and* $e_-^2 = e_-$;
- *(spectral square)* $\sigma^2 = q^2\,e_+ + u^2\,e_-$, *using only (1)–(2)*;
- *(Hecke relation)* $\sigma^2 = (q - u)\,\sigma + 1$.

The three conclusions are bundled as the single Lean theorem
`channel_algebra` (the `lean` reference of this block). The companion
identity $(-q^{-1})/q = -(q^2)^{-1}$ — the per-crossing eigenvalue ratio,
over any field, needing no channel data — is the separate lemma
`eigenvalue_ratio` in the same module.

The intended model is the commutant of $\sigma_1$ in the two-strand Hecke
algebra $H_2(q)$, with $e_\pm$ the Wedderburn pair of the
[Hopf channel](#def:van-der-waals-hopf-channel) and $\sigma$ the braid
operator of the [$R$-matrix braiding](#prop:r-matrix-braiding-structure);
there $u = q^{-1}$ and the spectral form is the eigenvalue decomposition of
$\sigma_1$ with channel eigenvalues $q$ and $-q^{-1}$. The Hecke relation
shows the abstract channel data (1)–(4) already forces the skein relation:
no further presentation input is required.
