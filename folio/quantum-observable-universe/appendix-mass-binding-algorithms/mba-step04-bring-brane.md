**Algorithm (Topological and Hodge invariants of the genus-4 Bring curve).**
*Compute the algebraic, cohomological, and hyperbolic-area invariants of Bring's curve $\Sigma_4 \subset \mathbb{P}^4$ together with its $S_5$ automorphism action and genus-saturating torus-knot pair.*

### Input

- *Complete intersection equations of Bring's curve in homogeneous coordinates $[z_0 : z_1 : z_2 : z_3 : z_4] \in \mathbb{P}^4$:*
  $$
    \sum_{i=0}^{4} z_i \;=\; 0,
    \qquad
    \sum_{i=0}^{4} z_i^2 \;=\; 0,
    \qquad
    \sum_{i=0}^{4} z_i^3 \;=\; 0.
  $$

### Output

- *Topological invariants: smooth curve genus $g(\Sigma_4) = 4$, Euler characteristic $\chi(\Sigma_4) = 2 - 2g = -6$, and Betti rank $\dim H^1(\Sigma_4; \mathbb{R}) = 2g = 8$.*
- *Hyperbolic and Hodge invariants: constant-negative-curvature ($K = -1$) Gauss–Bonnet area $\mathrm{Area}(\Sigma_4) = -2\pi\chi(\Sigma_4) = 12\pi$, and Hodge zero-mode density*
  $$
    \frac{\dim H^1(\Sigma_4; \mathbb{R})}{\mathrm{Area}(\Sigma_4)}
    \;=\;
    \frac{2g}{4\pi(g - 1)}
    \;=\;
    \frac{8}{12\pi}
    \;=\;
    \frac{2}{3\pi}.
  $$
- *Symmetry and force-carrier embedding data: automorphism group $\mathrm{Aut}(\Sigma_4) \cong S_5$ ($|\mathrm{Aut}(\Sigma_4)| = 120$, maximal Hurwitz-type symmetry at genus $4$), symplectic homology representation $H_1(\Sigma_4; \mathbb{Z}) \cong \mathbb{Z}^8$, and the unique genus-$4$ coprime torus-knot pair $\{T_{2,9}, T_{3,5}\}$ ($g(T_{p,r}) = \tfrac{1}{2}(p-1)(r-1) = 4$).*

### Algorithm

1. Intersect the hyperplane $H_1 = \{\sum z_i = 0\} \cong \mathbb{P}^3$ with the quadric $Q_2 = \{\sum z_i^2 = 0\}$ and cubic $C_3 = \{\sum z_i^3 = 0\}$; check Jacobian maximal rank across $\Sigma_4$ to certify smoothness and compute $\deg(\Sigma_4) = 2 \cdot 3 = 6$.
2. Apply adjunction on $\mathbb{P}^3$: $K_{\Sigma_4} = \mathcal{O}_{\Sigma_4}(-4 + 2 + 3) = \mathcal{O}_{\Sigma_4}(1)$, giving $2g - 2 = \deg K_{\Sigma_4} = 6$, hence $g = 4$, $\chi = 2 - 2g = -6$, and $\dim H^1(\Sigma_4; \mathbb{R}) = 8$.
3. Evaluate the Gauss–Bonnet area $\mathrm{Area}(\Sigma_4) = 4\pi(g - 1) = 12\pi$ and the ratio $\dim H^1 / \mathrm{Area} = \frac{2}{3\pi}$.
4. Enumerate coprime integer pairs $2 \le p < r$ solving $(p - 1)(r - 1) = 2g = 8$: the factorisations $8 = 1 \times 8 = 2 \times 4$ yield $(p, r) \in \{(2, 9), (3, 5)\}$, both coprime, isolating $\{T_{2,9}, T_{3,5}\}$ with $[9]_q[10]_q$ tree-level electromagnetic weight.

### Termination and Complexity

All steps consist of bounded finite-degree intersection arithmetic and divisor enumeration, terminating in $O(1)$ exact integer and rational operations.

### Mathematical Justification

1. **Curve definition and topology:** Smoothness, $S_5$-equivariance, and $\chi(\Sigma_4) = -6$ follow from [Bring's surface](#def:brings-surface) and [its Euler-characteristic lemma](#lem:brings-euler-characteristic).
2. **Force-carrier uniqueness:** Exhaustiveness of $\{T_{2,9}, T_{3,5}\}$ among genus-$4$ torus knots is established in [force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness); both invariants $g = 4$ and $\frac{2}{3\pi}$ enter the electromagnetic fixed-point equation of [Step 9a](#alg:mass-identity) with zero free parameters.
