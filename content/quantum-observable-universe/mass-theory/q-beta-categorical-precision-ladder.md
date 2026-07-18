**$\mathfrak{Q}_\beta$ categorical-derivation precision ladder.**
This derives the free-neutron $\beta$-decay Q-value $\mathfrak{Q}_\beta$ at the substrate $q_0$ via a four-rung categorical recursion. The series reaches a $-0.0066$ ppm residual against CODATA, below the $0.0094$ ppm $N=3$ c(K) ceiling from `conj:archimedean-remainder-exponential-decay`.

$$
\boxed{
  \mathfrak{Q}_\beta^{\mathrm{cat}}
   \;=\;
   \mathfrak{Q}_\beta^A \cdot
   \cos\!\bigl(\alpha - \tfrac{b\,\hbar_q^2}{2}\bigr) \cdot
   \bigl(1 - b^2 \hbar_q^4\bigr) \cdot
   \bigl(1 - 2 \, b^3 \hbar_q^6\bigr) \cdot
   \bigl(1 - 2\,b^4 \cdot b^4 \hbar_q^8\bigr) \cdot
   \bigl(1 - (b^2 + \tfrac{1}{2})\, b^5 \hbar_q^{10}\bigr) \cdot \cdots
}
$$

where:

- $\mathfrak{Q}_\beta^A = m_e \cdot |q^2 - 2q - 1| (q+1) / (2 q^3)$
  is the single-wrap Form A baseline from [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic);
- $\alpha = (z-1)h/2$ is the single-wrap eigenphase on $V_{(2,1)}$
  (per [`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge));
- $b = \sqrt{q^4+q^2+1}/(q^2+1)$ is the Hoefsmit off-diagonal coupling
  on $V_{(2,1)}$ (per [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization));
- $\hbar_q = (q-1)/q$ is the substrate quantum Planck constant.

The per-rung categorical sources, the truncation-order and error
analysis, the canonical precision ladder, the implication for the
$n{-}p$ mass split, and the open questions — together with the
Habiro-ring supersession note — are collected in
[the precision-ladder derivation context](#rem:q-beta-categorical-precision-ladder-context).
