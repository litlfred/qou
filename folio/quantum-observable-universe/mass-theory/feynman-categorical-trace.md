Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$, $V$ the fundamental representation, and $q$ not a root of unity. Let $\varrho \colon \mathbf{1} \to A$ be a closed cycle with braid representative $\beta \in B_n$.

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

*where the sum spans partitions $\lambda \vdash n$ with at most two parts. The Markov weights $w_\lambda$ satisfy the Markov property $\mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x)$ and $\mathrm{tr}_M(x \sigma_n^{-1}) = (z - h)\,\mathrm{tr}_M(x)$, $h = q - q^{-1}$, and evaluate to $w_\lambda = \dim_q(V_\lambda) / \dim_q(V^{\otimes n})$, with $\dim_q(V_\lambda) = [2j+1]_q$.*

*The transition amplitude is a finite sum over $\lfloor n/2 \rfloor + 1$ terms. Its absolute value equals the categorical mass at a single brane level:*

$$
  \mathfrak{m}(\varrho)\big|_{\text{single level}}
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr)
  =
  \bigl|
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  \bigr|.
$$
