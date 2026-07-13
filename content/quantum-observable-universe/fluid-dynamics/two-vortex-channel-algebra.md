*Lean sibling: generic commutative ring, no archimedean input (AGENTS.md §7c); library module `QOU.FluidDynamics.TwoVortexChannelAlgebra`.*

**Proposition (channel algebra of the two-vortex interaction).** *Let $R$ be a commutative ring carrying elements $e_+, e_-, \sigma, q, u$ satisfying:*

1. *(partition of unity)* $e_+ + e_- = 1$;
2. *(orthogonality)* $e_+ e_- = 0$;
3. *(inverse witness)* $q\,u = 1$;
4. *(spectral form)* $\sigma = q\,e_+ - u\,e_-$.

*These axioms imply:*

- *(derived idempotency)* $e_+^2 = e_+$ and $e_-^2 = e_-$;
- *(spectral square)* $\sigma^2 = q^2\,e_+ + u^2\,e_-$, derived strictly from (1)–(2);
- *(Hecke relation)* $\sigma^2 = (q - u)\,\sigma + 1$.

The theorem `channel_algebra` unites these derivations. The parallel identity $(-q^{-1})/q = -(q^2)^{-1}$ — defining the per-crossing eigenvalue ratio over any field without channel data — resides in the standalone lemma `eigenvalue_ratio`.

The primary model assigns these elements to the commutant of $\sigma_1$ in the two-strand Hecke algebra $H_2(q)$. Here $e_\pm$ represents the Wedderburn pair of the [Hopf channel](#def:van-der-waals-hopf-channel) and $\sigma$ represents the braid operator of the [$R$-matrix braiding](#prop:r-matrix-braiding-structure). Setting $u = q^{-1}$ casts the spectral form as the eigenvalue decomposition of $\sigma_1$ supporting eigenvalues $q$ and $-q^{-1}$. The resulting Hecke relation proves that the abstract channel data logically forces the Skein relation without external topological presentation.
