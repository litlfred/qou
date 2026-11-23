Compute the Gröbner--Shirshov normal form of a nuclear braid word via the division algorithm, specialized to the Iwahori--Hecke algebra.

**Input:** Mass number $A = Z + N$, proton number $Z$, neutron number $N$. The algebra $H_A(q)$, admissible system $(B, <)$, and Gröbner--Shirshov basis $G$.

**Output:** The unique normal form $\mathcal{N}(Z, N) \in H_A(q)$ and its Markov trace.

The algorithm proceeds inductively.

1. Initialize with the normal form of the first nucleon.
2. For each subsequent nucleon, determine the crossing type based on nucleon pairs ($pp$, $nn$, or mixed).
3. Form the product and apply the division algorithm.
4. Return the final reduced form and its trace.

**Correctness.** The output is independent of the choice of $g \in G$ because $G$ is a Gröbner--Shirshov basis.

**Complexity.** The inductive strategy requires $O(A^2)$ multiplications and $O(A^3)$ Hecke reduction steps. Multiplying all crossings before reduction would generate $O(2^{Z \cdot N})$ terms.
