**$\mathfrak{Q}_\beta$ categorical-derivation precision ladder.**
This derives the free-neutron $\beta$-decay Q-value $\mathfrak{Q}_\beta$ at the substrate $q_0$ via a four-rung categorical recursion. Residuals are quoted as $(\mathfrak{Q}_\beta^{\mathrm{cat}} - \mathfrak{Q}_\beta^{\mathrm{CODATA}}) / \mathfrak{Q}_\beta^{\mathrm{CODATA}}$, and the ladder approaches CODATA from above, so every rung is positive. At the muon-pin (CAL-2) $q_0$ this block is written in, the five-rung series reaches a $+0.0071$ ppm residual against CODATA; at the canonical proton pin the same five rungs give $+0.0377$ ppm.

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
  is the single-wrap Form A baseline;
- $\alpha = (z-1)h/2$ is the single-wrap eigenphase on $V_{(2,1)}$;
- $b = \sqrt{q^4+q^2+1}/(q^2+1)$ is the Hoefsmit off-diagonal coupling
  on $V_{(2,1)}$ (per [Hoefsmit seminormal matrix for $V_{(2,1)}$ + Markov-symmetrized cos character](#prop:hoefsmit-V21-cos-symmetrization));
- $\hbar_q = (q-1)/q$ is the substrate quantum Planck constant.

The per-rung categorical sources, the truncation-order and error
analysis, the canonical precision ladder, the implication for the
$n{-}p$ mass split, and the open questions — together with the
Habiro-ring supersession note — are collected in
[the precision-ladder derivation context](#rem:q-beta-categorical-precision-ladder-context).
