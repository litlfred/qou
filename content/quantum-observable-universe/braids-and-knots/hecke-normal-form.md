The **Hecke normal form** of an element $h \in H_n(R, q)$ is the unique representative obtained by iterated application of three rewriting rules:
1. Hecke relation: $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.
2. Far commutativity: $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $|i - j| \geq 2$.
3. Yang--Baxter: $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$ (in the shortlex-decreasing direction).

This reduction is confluent, making the normal form independent of rule order. The resulting basis elements correspond bijectively to the symmetric group $S_n$. Computationally, this may be evaluated by directed Kashiwara crystal traversal rather than S-polynomial overlap analysis.
