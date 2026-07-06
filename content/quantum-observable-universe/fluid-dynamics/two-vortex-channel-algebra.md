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

We bundle the three conclusions into the single Lean theorem `channel_algebra` (the `lean` reference of this block). We state the companion identity $(-q^{-1})/q = -(q^2)^{-1}$ — the per-crossing eigenvalue ratio, requiring no channel data — as the separate lemma `eigenvalue_ratio`.

The intended model is the commutant of $\sigma_1$ in the two-strand Hecke algebra $H_2(q)$. The elements $e_\pm$ form the Wedderburn pair of the [Hopf channel](#def:van-der-waals-hopf-channel). The element $\sigma$ acts as the braid operator of the [$R$-matrix braiding](#prop:r-matrix-braiding-structure). We identify $u = q^{-1}$. The spectral form provides the eigenvalue decomposition of $\sigma_1$ with channel eigenvalues $q$ and $-q^{-1}$. The Hecke relation demonstrates that the abstract channel data (1)–(4) forces the skein relation without further presentation input.
