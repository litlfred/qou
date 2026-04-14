**Definition (Universal ILP Algorithm).**
*A single integer linear program selects the operator at every
level of the QOU construction.  The same Gram matrix $G$, the
same Frobenius check $Gx \geq 0$, and the same ILP are applied
to quarks, nucleons, atoms, and molecules.*

### Input

- *Current state $x \in H_3(q)$ (NF vector in the 6-element basis
  $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$).*
- *Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ (computed
  once from the Hecke algebra relations).*
- *Markov traces $t_i = \mathrm{tr}_M(b_i)$.*

### Algorithm

1. **Frobenius check.**
   Compute $Gx$.  If $Gx_i < 0$ for any $i$, the state is
   **unstable** — go to Step 2a.  Otherwise the state is
   **stable** — go to Step 2b.

2a. **Unstable → restore stability.**
    Solve the ILP:
    $$
      \min_{K} \; \mathrm{cr}(K) \quad
      \text{s.t.} \quad K \in \mathcal{B}_3, \quad
      G \cdot \mathrm{NF}(x \cdot K) \geq 0
    $$
    where $\mathcal{B}_3$ is the braid group on 3 strands and
    $\mathrm{cr}(K)$ is the crossing number.  The ILP finds the
    **minimum-crossing braid** that restores Frobenius positivity.
    Apply $K$ to the state: $x \leftarrow \mathrm{NF}(x \cdot K)$.
    Return to Step 1.

2b. **Stable → create binding.**
    Solve the ILP:
    $$
      \min_{K} \; \mathrm{cr}(K) \quad
      \text{s.t.} \quad K \in \{\text{knots}\}, \quad
      E(x, K, y) > 0
    $$
    where $\{\text{knots}\}$ is the set of single-component braid
    closures, and $E(x, K, y)$ is the binding energy between
    states $x$ and $y$ mediated by $K$.  The ILP finds the
    **minimum-crossing knot** with positive binding.

3. **Update state.**
   Apply the selected operator to the state.  The new state
   becomes the input for the next level.

### Instantiations

| Level | Input | Frobenius | ILP selects | Crossings |
|:------|:------|:----------|:-----------|:----------|
| Quarks → confinement | uud (3 crossings) | **FAIL** ($Gx[\gamma] < 0$) | $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ | 6 |
| Proton → gluon | $\mathcal{B}_3 \times$ quarks (9) | **FAIL** ($Gx[\gamma] < 0$) | $\sigma_0 \sigma_0$ | 2 |
| Proton → H atom | proton + gluon (11) | **PASS** | $\sigma_1^{-1}$ (pe crossing) | 1 |
| H → H₂ molecule | H atom | **PASS** | $T_{2,3}^{-1} = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ | 3 |

*At every level, the algorithm uses the same $6 \times 6$ Gram
matrix $G$ and the same Frobenius positivity constraint
$Gx \geq 0$.  The only difference between levels is the
**topological constraint**:*

- *Step 2a (unstable): the operator must be a **braid group
  element** — any product of generators $\sigma_0^{\pm 1}$,
  $\sigma_1^{\pm 1}$ that restores stability.*
- *Step 2b (stable): the operator must be a **knot** — a braid
  whose closure is a single-component curve.  The unknot
  (identity) gives zero binding; the trefoil is the first
  non-trivial knot.*

### Topological hierarchy

*The topological constraint upgrades at each level:*

- *Level 1 (confinement): the operator must have the
  **Borromean property** — no proper subset of quarks is
  separable.  This selects $\mathcal{B}_3$ over simpler braids.*
- *Level 2 (gluon): the operator must restore
  **Frobenius stability** — the minimum crossing fix.*
- *Level 3 (electron): the operator is the **pe crossing** —
  physically determined by the electromagnetic interaction.*
- *Level 4 (molecule): the operator must be a **knot** —
  a topologically non-trivial single-component bond.
  The inverse trefoil $T_{2,3}^{-1}$ is the minimum.*

### Consistency

*The same energy functional $\Phi_1 = \ln|\mathrm{tr}_M|$ and
the same Wedderburn weights
$(w_s, w_d, w_a) = (q^2, (q^2+1)^2, q^2)/(q^4+4q^2+1)$
are used at every level.  The binding energy is:*

$$
  E_{\mathrm{bind}} = \bigl(\Phi_1^{\mathrm{unbonded}}
  - \Phi_1^{\mathrm{bonded}}\bigr) \times E_{\mathrm{scale}}
$$

*where $E_{\mathrm{scale}}$ is the appropriate energy unit:*

| Level | $E_{\mathrm{scale}}$ | Expression |
|:------|:--------------------|:-----------|
| Nuclear mass | $m_e$ | Electron mass |
| Molecular binding | $E_{\mathrm{hartree}}/[2]_q^2$ | $m_e \alpha_{\mathrm{EM}}^2 / (q+q^{-1})^2$ |
| $Q$-value | $E_\times \cdot \mu_0$ | $\frac{1}{2}(q-q^{-1}) \cdot \frac{m_e}{3(q-q^{-1})/2}$ |

*All energy scales are derived from $q_0$ and $m_e$ alone.*
