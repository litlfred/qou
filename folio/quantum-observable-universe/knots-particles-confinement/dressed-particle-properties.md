**Composition.**
*Dressing is not generally invertible. Stripping electrons changes the binding subword via the SDP. However, dressings compose:*

$$
  \mathrm{dress}_{S_2} \circ \mathrm{dress}_{S_1}
  \;=\;
  \mathrm{dress}_{S_1 \oplus S_2}
$$

*Here $\oplus$ concatenates shell data when the combined $Z$ remains SDP-feasible. Partial dressing ($0 < Z' < Z_{\max}$) yields **ions**.*

**Stability under dressing.**
*The Frobenius-stability index of $P_{\mathrm{dressed}}$ is monotonically non-decreasing along the dressing chain toward closed-shell noble-gas configurations ($Z \in \{2, 10, 18, 36, 54, 86\}$). Each shell closure is a $\mu \ge 2$ multi-operator fixed point of the SDP. Breaking the bond requires simultaneously breaking every tight dual block. Noble-gas objects are therefore local terminal objects of the dressing sub-diagram of $\mathbf{Conf}$.*

**Functoriality of the Markov trace.**
*Under dressing, the Markov trace transforms as:*

$$
  \mathrm{tr}_M(P_{\mathrm{dressed}})
  \;=\;
  \mathrm{tr}_M(P_{\mathrm{bare}}) \cdot
  \prod_{\lambda \in \mathcal{S}^*(S, q)} w_\lambda^{\,\langle \pi_\lambda, \Phi^* \rangle}
$$

*Here $\mathcal{S}^*(S, q)$ is the SDP active support and $w_\lambda$ are the block shadow prices. For $\mu(S, q) = 1$, this collapses to the scalar-LP product. For $\mu \ge 2$, the full matrix shadow contributes.*

**Typical bare particle.** In the [dressing morphism](#def:dressed-particle) the bare particle $P_{\mathrm{bare}}$ is typically a bare nucleus, at level $\ell = 2$.
