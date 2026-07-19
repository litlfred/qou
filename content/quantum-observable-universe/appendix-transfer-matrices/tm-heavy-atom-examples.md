The light-nucleus examples use only the bare transfer matrix product. For heavy nuclei, shell corrections from the magic number structure become essential. This section works through the full $Q$-value algorithm. These examples demonstrate the mechanics: a definite $Q$-value output from the substrate parameter $q$ alone. The worked numbers below are conditional on the three shell-structure conjectures [(C1)–(C3)](#rem:shell-construction-rules) — the magic-number set is observed, not yet derived from $q$; the dominant-binding-operator selection and the inner-shell cancellation are unproven. Where a residual remains, it is bracketed as an open direction under those conjectures, not absorbed into a free parameter.

Recall: $s = q^{1/2} - q^{-1/2}$, $z = 1/(q^{1/2} + q^{-1/2})$, $\hbar_q = 1 - q^{-1}$, $E_{\times} = \frac{1}{2}(q - q^{-1})$, and $\mu_0$ the remaining conversion constant that carries the dimensionless bracket into MeV.

## The magic number table

Shell closures occur at specific nucleon counts where the Gröbner--Shirshov word-length histogram is palindromic:

$$
  \mathcal{M} = \{0, 2, 8, 20, 28, 50, 82, 126\}
$$

For nucleon count $X$, see [Table 1](#tbl:tm-heavy-atom-examples-table1-data). When $X$ is magic ($n_{\mathrm{out}} = 0$), the outermost shell is closed and the relevant shell size is $n_{\mathrm{shell}}(X)$.

## The $Q$-value algorithm (summary)

**Input:** $(Z, N)$, substrate parameter $q$.

1. Compute outer shell occupancies for parent $(Z, N)$ and daughter $(Z+1, N-1)$.
2. Compute torus knot Markov traces $\tau(n)$ for each occupancy from the Chebyshev recurrence.
3. Compute bare Skein polynomial ratio $R_{\mathrm{bare}} = \log_q(P_{\mathrm{dau}} / P_{\mathrm{par}})$.
4. Compute shell correction $\Delta_{\mathrm{shell}} = (\text{proton shell change}) + (\text{neutron shell change})$.
5. Add weak vertex $\Delta_{T_{3,5}} = -3.370$.
6. Convert: $Q = |R_{\mathrm{bare}} + \Delta_{\mathrm{shell}} + \Delta_{T_{3,5}}| \times \hbar_q \cdot E_{\times} \cdot \mu_0$.

