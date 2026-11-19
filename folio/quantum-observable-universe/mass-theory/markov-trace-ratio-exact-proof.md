**Proof.** The Jones polynomial of a braid closure $\hat\beta$ on
$n$ strands is $J(\hat\beta, q) = C(n, q) \cdot \mathrm{tr}_M(\beta)$
where $C(n, q) = (-q^{1/2} - q^{-1/2})^{n-1} \cdot (-q^{-3/2})^{-w(\beta)}$
depends on the strand count $n$, the substrate parameter $q$, and the
writhe $w(\beta)$ — but the factor $(-q^{-3/2})^{-w}$ also cancels in
ratios of braids with the same writhe. For braids with different
writhes, the writhe correction is a known power of $q$ that can be
applied post-hoc without affecting the Gram-matrix or LP structure.

The ratio $J_1/J_2 = C \cdot \mathrm{tr}_1 / (C \cdot \mathrm{tr}_2)
= \mathrm{tr}_1 / \mathrm{tr}_2$ is immediate from cancellation of
the common factor $C$. $\square$

**Consequence for the HOMFLYPT engine.** The
the canonical formalism
returns Markov-trace-normalised values at SU(2) (row 3 of
[archimedean-image-table remark](#rem:archimedean-image-table)), which
are proportional to the Jones polynomial. For all optimisation
consumers — the canonical formalism,
the canonical formalism,
the canonical formalism — the
ratios are exact and the LP shadow prices, Gram inverse, and Frobenius
duals are normalisation-independent.

At SU($N > 2$), the engine uses the quantum Schur function weights,
which give a DIFFERENT invariant (the SU($N$) quantum invariant, row 5
of the Archimedean-image table). The same ratio-exactness holds within
each $N$-channel: the normalisation factor $C_N(n, q)$ cancels in ratios.
