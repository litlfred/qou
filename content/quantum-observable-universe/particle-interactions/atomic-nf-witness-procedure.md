The construction and verification of the normal-form witness proceed as follows.

1. At each construction step: the Gröbner--Shirshov reduction is run to convergence. Convergence is guaranteed by the Diamond Lemma.
2. The final NF element is accumulated without mid-construction stripping for $A \leq 9$. For $A > 9$, the element is stripped at controlled thresholds and the stripped contributions are accumulated into the Pauli character $F_{\mathrm{Pauli}} = |\mathrm{tr}_{\mathrm{alt}}/\mathrm{net}|$.
3. Certificates (JSON) are committed to the repository for each computed atom. Each certificate records: $F_{\mathrm{Pauli}}$, $\mathrm{tr}_{\mathrm{alt}}(q_0)$, $\mathrm{net}(q_0)$, computation time, word count, and engine version.

The three Wedderburn invariants $\Phi_1$, $\Phi_2$, $\Phi_3$ used in the mass formula are computed from the transfer matrix chain. The transfer matrix output is in normal form by construction.
