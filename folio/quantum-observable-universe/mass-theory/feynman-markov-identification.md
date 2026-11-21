*Let $\beta \in B_n$ act on $V^{\otimes n}$ via $\rho_n$. The transition amplitude on the eigenbasis is the Markov-weighted sum of partial traces:*

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  :=
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr).
$$

*This equals the Jones--Markov trace $\mathrm{tr}_M\bigl(\rho(\beta)\bigr)$ on $H_n(R, q)$, where the Markov weights are $w_\lambda = \dim_q(V_\lambda) / \dim_q(V^{\otimes n})$.*
