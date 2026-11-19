## Proof

> **Scope of Steps (ii) and (iii).** In (ii) the $2\times2$ matrix is multiplication on the span of $\{\sigma_i, 1\}$, not the action on the two-dimensional standard representation of $H_3(q)$; the eigenvalue argument has to be redone on the standard representation. In (iii), the corpus does not prove that $\mathcal{B}_3$ is the unique braid-realizable minimum: confinement-operator-selection-proof and the confinement-topological caveat both leave uniqueness open. Step (iii) is therefore conditional on that uniqueness.


**(i)** The Wedderburn--Artin theorem decomposes $H_3(q)$ into
three irreducible representations: symmetric ($\dim = 1$),
standard ($\dim = 2$), and alternating ($\dim = 1$).  On the
one-dimensional representations, the crossing operator
$c \cdot \sigma_i + d \cdot \mathbf{1}$ acts as a scalar:
$\lambda_{\mathrm{sym}} = cq + d$ (eigenvalue $q$) and
$\lambda_{\mathrm{alt}} = -cq^{-1} + d$ (eigenvalue $-q^{-1}$).
The product of scalars commutes, so $S(\pi)$ and $A(\pi)$ are
permutation-invariant.

**(ii)** On the standard representation, the crossing acts by
the $2 \times 2$ transfer matrix
$T^{\mathrm{std}}(c, d) = \bigl(\begin{smallmatrix}
c(q - q^{-1}) + d & c \\ c & d
\end{smallmatrix}\bigr)$.
This follows from the Hecke relation $T^2 = (q - q^{-1})T + 1$
restricted to the $2$-dimensional standard representation, where
$T$ has eigenvalues $q$ and $-q^{-1}$ with trace $q - q^{-1}$.

**(iii)** The confinement theorem proves that $\mathcal{B}_3$
(Borromean braid) is the unique braid-realizable minimum of the
Markov trace among length $\leq 6$ braid words.  The nucleon NF
is stable under further Gröbner--Shirshov reduction — no rule
in the GS basis applies to a reduced nucleon word.  This stability
is exactly the jet-descended property: the nucleon contribution to
the transfer matrix is fixed, independent of the nuclear context.
Precomputing $T_\mathfrak{p}^{\mathrm{std}}$ and
$T_\mathfrak{n}^{\mathrm{std}}$ is justified by this stability.

**(iv)** The jet-stratified reduction algorithm partitions
$S$-polynomial pairs into descended $\times$ descended (already
resolved) and transient (requiring verification).  At the nuclear
level:
- Descended $\times$ descended = intra-nucleon reductions (cached)
- Transient = inter-nucleon crossings (simple $2 \times 2$ matrices)
- Mixed = cross-terms (resolved by the final pass of Algorithm 3
  in [jet-stratified reduction](#unital-groebner-bases:prop:jet-stratified-reduction))

The inter-nucleon crossing matrices follow from the crossing
conventions:
$\mathfrak{p}\mathfrak{p}$: $\sigma_0$ ($c = 1, d = 0$),
$\mathfrak{n}\mathfrak{n}$: $\sigma_0^{-1}$ ($c = 1, d = -(q - q^{-1})$),
$\mathfrak{p}\mathfrak{n}$: $\tfrac{1}{2}(\sigma_0 + \sigma_0^{-1})$
($c = 1, d = -\tfrac{1}{2}(q - q^{-1})$).  $\square$
