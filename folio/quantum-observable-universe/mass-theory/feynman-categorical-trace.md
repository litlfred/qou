Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$, $V$ the fundamental representation, $q$ real and not a root of unity, and $\mathrm{tr}_M$ the Markov trace at $z = q^3/(q^2+1)$. Let $\varrho \colon \mathbf{1} \to A$ be a closed cycle with braid representative $\beta \in B_n$.

**Proposition.**
*The Feynman transition amplitude evaluated on the knot-type eigenbasis equals the Jones--Markov trace of the braid representation in the Hecke algebra:*

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  =
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr)
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr),
$$

*where $w_\lambda = \dim_q(V_\lambda)/\dim_q(V^{\otimes n}) = [\lambda_1 - \lambda_2 + 1]_q/[2]_q^{\,n}$. The trace satisfies $\mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x)$ and $\mathrm{tr}_M(x \sigma_n^{-1}) = (z - h)\,\mathrm{tr}_M(x)$ for $x \in H_n(R, q)$, where $h = q - q^{-1}$.*

*The sum has $\lfloor n/2 \rfloor + 1$ terms. The categorical mass at a single brane level is the absolute value of this amplitude:*

$$
  \mathfrak{m}(\varrho)\big|_{\text{single level}}
  =
  \bigl|\mathrm{tr}_M\bigl(\rho(\beta)\bigr)\bigr|
  =
  \bigl|
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  \bigr|.
$$
