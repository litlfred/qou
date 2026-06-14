For any ground ring $R$ in which $(q - q^{-1})$ is invertible, the
[$q$-Casimir element](#def:q-casimir)

$$
  C_q \;=\; F E + \frac{q  K + q^{-1} K^{-1} - (q + q^{-1})}{(q - q^{-1})^2}
$$

exists as a central element of $\mathcal{U}_q(\mathfrak{su}(2))$ and
acts as $[j]_q [j+1]_q  \mathrm{id}$ on every simple module $V_j$.

Uniqueness up to scalar is
([uniqueness of the $q$-Casimir](#prop:q-casimir-unique)).


**Mathematical Novelty:** This is a standard quantum-group Casimir existence result (Kassel/Lusztig). The formalization axiomatizes this standard mathematical fact pending a complete formalization of $U_q(\mathfrak{su}_2)$, providing a rigorous structural interface without claiming a novel mathematical argument.

**Formalization Goal Plausibility:** The goal is highly plausible and correctly scoped: we isolate the existence of the Casimir element as an explicit `QCasimir.exists_axiom` to bypass constructing the full quantum group internally. The formal derivation cleanly obtains `Nonempty QCasimirData` from this axiom, validating the external integration strategy without introducing unstated gaps.