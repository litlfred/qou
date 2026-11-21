## Proof

The Habiro completion $\widehat{\mathbb{Z}[q]}$ is realised as the ring of threads $(x_N)_{N \ge 0}$, $x_N \in \mathbb{Z}[q]/(q;q)_N$ with $(q;q)_N = \prod_{k=1}^{N}(1 - q^k)$, compatible under the reductions $\mathbb{Z}[q]/(q;q)_M \to \mathbb{Z}[q]/(q;q)_N$ for $N \le M$. These reductions exist because $(q;q)_N$ divides $(q;q)_M$. Compatibility is preserved by sums and products, so the threads form a subring of the product.

For $n \ge 1$ the cyclotomic polynomial $\Phi_n(q)$ divides $1 - q^n$, which is a factor of $(q;q)_n$. Reduction modulo $\Phi_n(q)$ therefore factors through $\mathbb{Z}[q]/(q;q)_n$, and

$$
  \pi_n(x) \;:=\; x_n \bmod \Phi_n(q)
  \;\in\; \mathbb{Z}[q]/\Phi_n(q)
$$

defines a ring homomorphism $\pi_n : \widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_n(q)$. On the constant thread of a polynomial $p$, $\pi_n$ returns the class of $p$, so $\pi_n$ is surjective and restricts to the usual reduction on $\mathbb{Z}[q]$.

By hypothesis, $\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)$ is an element of $\widehat{\mathbb{Z}[q]}$. Applying $\pi_{n_\ell}$ and identifying $\mathbb{Z}[q]/\Phi_{n_\ell}(q)$ with $\mathbb{Z}[\zeta_\ell]$ gives the residue, an element of the cyclotomic ring. Because $\pi_{n_\ell}$ is a ring homomorphism, the residue of a sum or product is the sum or product of the residues. $\blacksquare$

The construction does not use analytic continuation. Habiro shows that, for elements of $\widehat{\mathbb{Z}[q]}$, these projections agree with evaluation at roots of unity \cite{habiro2002}; that comparison is not needed for the statement.
