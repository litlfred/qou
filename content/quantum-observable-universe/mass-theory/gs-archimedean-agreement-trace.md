**Conjecture (archimedean agreement, generic instance).**
*For every closed braid $K$ admitting a Habiro polynomial trace $T_K(u) \in \mathbb{Z}[u]$ and a Gröbner–Shirshov mass value $\mathfrak{m}_{\mathrm{GB}}(K, q_0)$, the archimedean evaluation*

$$
  T_K\bigl(\sqrt{q_0}\bigr) \;\approx\; \mathfrak{m}_{\mathrm{GB}}(K, q_0)
$$

*agrees across pipelines.*

**Categorical statement.** The archimedean fibre functor intertwines the Habiro polynomial evaluation and the spectral-sequence residue sum.

**Lean encoding.** Encoded as the class field axiom `archimedean_agreement`. Instances supply it as a substrate axiom.

**Conjectural status.** A Lean proof requires the spectral decomposition existence, the `tail_in_ideal` axiom for the Habiro completion, and the analytic identification of the residues.

**Empirical witness.** Validation records exact agreement to machine precision.
