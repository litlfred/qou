## Proof (conditional on [Existence of the cyclotomic residue at each filtration level](#conj:gs-residue-at-root-existence))

The conjectural hypothesis, assumed throughout, is the existence of the cyclotomic projections $\pi_n$ on the Habiro completion; every remaining step is unconditional.

The graded Markov trace
$\mathrm{tr}_{M, \ell}(T_w) \in \mathbb{Q}(q)$ has, by
construction
([Graded Markov trace as the induced trace on $J^\ell / J^{\ell+1}$](#prop:graded-markov-trace-from-gs-filtration)),
$q$-degree $= \ell$ in the GS-filtration grading. Multiplied by
$\Phi_q$, the product is an element of the Habiro ring:

$$
  \Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)
  \;\in\;
  \widehat{\mathbb{Z}[q]}.
$$

The Habiro ring's cyclotomic projection
$\pi_n : \widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q] / \Phi_n(q)$
is a $\mathbb{Z}$-algebra map for each $n$ \cite{habiro2002}.
Applying $\pi_{n_\ell}$ (the cyclotomic projection at the
distinguished order for stratum $\ell$) and identifying
$\mathbb{Z}[q] / \Phi_{n_\ell}(q)$ with $\mathbb{Z}[\zeta_\ell]$
gives an element of the cyclotomic ring — the residue.

Equivalence with the analytic definition (when both apply) is the
content of the Habiro-completion theorem
\cite{habiro2002}: the cyclotomic projections agree with the
analytic residue at $\zeta_\ell$ for any element of
$\widehat{\mathbb{Z}[q]}$ that converges as a complex function on
$|q| > 1$. The algebraic projection, however, is well-defined
*regardless* of analytic convergence: the
algebraic-side derivation does not need analytic continuation.
