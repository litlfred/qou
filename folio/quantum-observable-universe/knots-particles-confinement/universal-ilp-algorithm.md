**Definition (Universal ILP Algorithm).**
*A single integer linear program selects the operator at every level of the QOU construction. The same Gram matrix $G$, the same Frobenius check $Gx \geq 0$, and the same ILP are applied to quarks, nucleons, atoms, and molecules.*

### Input

- *Current state $x \in H_3(q)$.*
- *Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$.*
- *Markov traces $t_i = \mathrm{tr}_M(b_i)$.*

### Algorithm

*A single LP handles both unstable and stable states:*

$$
  \min_{K} \; \mathrm{cr}(K) \quad
  \text{s.t.} \quad K \in \{\text{knots}\} \setminus \{1\}, \quad
  G \cdot \mathrm{NF}(x \cdot K) \geq 0
$$

*with objective among feasible $K$: minimise $|\mathrm{tr}_M(x \cdot K)|$ at each crossing number. Select the smallest $\mathrm{cr}(K)$ that satisfies Frobenius positivity.*

*The two constraints are:*

1. ***$K$ is a non-trivial knot**. The unknot leaves the state unchanged.*
2. ***Frobenius positivity**. The resulting state must be LP-stable.*

- *When the state is **unstable** ($Gx \not\geq 0$): the Frobenius constraint forces a non-trivial $K$ that restores stability. The LP selects the minimum-crossing knot that achieves $Gx' \geq 0$.*
- *When the state is **stable** ($Gx \geq 0$): any non-trivial knot is a candidate. The LP selects the minimum-crossing one, with $|\mathrm{tr}_M|$ minimised as tiebreaker. This is the bond operator.*

*Apply $K$ to the state: $x \leftarrow \mathrm{NF}(x \cdot K)$. Proceed to the next level.*

### Instantiations

| Level | Input | Frobenius | ILP selects | Crossings |
|:------|:------|:----------|:-----------|:----------|
| Quarks $\to$ confinement | uud | **FAIL** | $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ | 6 |
| Proton $\to$ gluon | $\mathcal{B}_3 \times$ quarks | **FAIL** | $\sigma_0 \sigma_0$ | 2 |
| Proton $\to$ H atom | proton + gluon | **PASS** | $\sigma_1^{-1}$ | 1 |
| H $\to$ H$_{2}$ molecule | H atom | **PASS** | $T_{2,3}^{-1}$ | 3 |

*At every level, the algorithm uses the same Gram matrix $G$ and the same Frobenius positivity constraint. The only difference between levels is the **topological constraint**:*

- *Step 2a (unstable): the operator must be a **braid group element**.*
- *Step 2b (stable): the operator must be a **knot**.*

### Topological hierarchy

*The topological constraint upgrades at each level:*

- *Level 1 (confinement): the operator must have the **Borromean property**.*
- *Level 2 (gluon): the operator must restore **Frobenius stability**.*
- *Level 3 (electron): the operator is the **pe crossing**.*
- *Level 4 (molecule): the operator must be a **knot**.*

### Consistency

*Use the same energy functional $\Phi_1 = \ln|\mathrm{tr}_M|$ and the same Wedderburn-Artin weights at every level. All energy scales are derived from $q_0$ and $m_e$ alone.*

**Archimedean specialisation.**
*What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.*
