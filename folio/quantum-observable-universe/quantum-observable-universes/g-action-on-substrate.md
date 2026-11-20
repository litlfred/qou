The proposal is that the Frobenius–Hopf substrate $A$ in $\mathbf{Rep}(\mathrm{SU}_q(2))$ admits a unique $G$-equivariant structure under $G = \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$. This structure is governed by four constraints linking the categorical data to the electroweak sector. From these constraints, the symmetric-channel Frobenius trace $\mathcal{N}_{\rm sym}(q) = \mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ is computable in closed form.

### The four constraints

**Constraint (G-1) — $G$-isotypic decomposition.**
The substrate $A$ decomposes as a direct sum of $G$-isotypic components:

$$
  A \;=\; A^{(\gamma)} \;\oplus\; A^{(W^+)} \;\oplus\; A^{(W^-)}
  \;\oplus\; A^{(Z)} \;\oplus\; A^{(H)} \;\oplus\; A^{(\rm matter)}
$$

where each $A^{(X)}$ carries a unique irreducible representation of $G$. See [Table 1](#tbl:g-action-on-substrate-table1-data).

**Constraint (G-2) — Per-host $q$-dimension assignment.**
The categorical $q$-dimension of each component is determined by its torus-link host:

$$
  \dim_q\bigl(A^{(W^\pm)}\bigr) \;=\; [4]_q,
  \qquad
  \dim_q\bigl(A^{(Z)}\bigr) \;=\; [6]_q,
  \qquad
  \dim_q\bigl(A^{(H)}\bigr) \;=\; [2]_q.
$$

The $W$-host scale $[4]_q$ reflects the $T(2,4)$ crossing count, and the $Z$-host scale $[6]_q$ reflects $T(2,6)$. The Higgs scale $[2]_q$ is the $q$-dimension of the fundamental representation, restricted to the neutral component.

**Constraint (G-3) — Higgs vacuum vortex morphism.**
The Higgs vacuum value $\langle\Phi\rangle \in A$ is the unique non-zero vortex morphism $\varrho_\Phi \colon \mathbf{1} \to A^{(H)}$ satisfying

$$
  Q \cdot \varrho_\Phi = 0, \qquad
  \mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi) = v^2 / m_e^2,
$$

where $Q = T_3 + Y$ is the unbroken charge generator and $v \approx 246\,\mathrm{GeV}$ is the weak vacuum expectation value. The first condition forces neutrality under the unbroken $\mathrm{U}(1)_{\text{em}}$. The second fixes the categorical norm to the empirical Higgs VEV.

**Constraint (G-4) — Higgs idempotent.**
The categorical Higgs idempotent $e_H$ is defined from $\varrho_\Phi$ by:

$$
  e_H \;=\; \frac{\varrho_\Phi \cdot \varrho_\Phi^*}{\mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi)}.
$$

This rank-1 projector isolates the unbroken 1-dimensional subspace of $A^{(H)}$. Its trace is

$$
  \mathrm{tr}_F(e_H) \;=\; 1.
$$

The idempotent factors through the monoidal unit: $e_H = \varrho_\Phi \circ \bigl(t^{-1}\varrho_\Phi^*\bigr)$ with $t = \mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi)$, and $\varrho_\Phi^* \cdot \varrho_\Phi = t \cdot \mathrm{id}_{\mathbf{1}}$. Cyclicity of the trace gives $\mathrm{tr}_F(e_H) = \mathrm{tr}_F(\mathrm{id}_{\mathbf{1}})$, which is $1$ for a unit-normalised cyclic trace. The value $[2]_q$ of (G-2) is the $q$-dimension of all of $A^{(H)}$, not the trace of its rank-one image.

### Derivation of $\mathcal{N}_{\rm sym}(q)$

Composing the traces over the components gives

$$
  \mathrm{tr}_F\bigl(e_{\rm sym}^{\rm EW} \cdot e_H\bigr)
  \;=\;
  \dim_q(e_{\rm sym}^{\rm EW}\bigl[A^{(W^+)} \oplus A^{(W^-)} \oplus A^{(Z)}\bigr]) \;\cdot\;
  \dim_q\bigl(e_H \cdot A^{(H)}\bigr).
$$

Applying the assignments from the first two constraints yields:

- $\dim_q(e_{\rm sym}^{\rm EW}[A^{(W^\pm)}]) = [4]_q$
- $\dim_q(e_{\rm sym}^{\rm EW}[A^{(Z)}]) = [6]_q$
- $\dim_q(e_H \cdot A^{(H)}) = \mathrm{tr}_F(e_H) = 1$

Thus,

$$
  \mathcal{N}_{\rm sym}(q)
  \;=\;
  [4]_q \cdot [4]_q \cdot [6]_q \cdot 1
  \;=\;
  [4]_q^2 \cdot [6]_q.
$$

This derivation grounds Anchor II explicitly in categorical structures. See [Table 2](#tbl:g-action-on-substrate-table2-data).

### Verification

At the value $q_0 = {{ qou.computations.q-pinning-50-digit.derived_50_digit.q | precision: 6 }}\ldots$, the predicted trace evaluates to:

$$
  [4]_q^2 \cdot [6]_q \;\approx\; 16.889 \cdot 6.388
  \;\approx\; 107.89.
$$

The CODATA target is $\mathcal{N}_{\rm sym}(q_0) \approx 213.11$. The predicted value is $49.4\%$ below it ($107.89/213.11 - 1 \approx -0.494$).

The constraints as stated do not reproduce the target. An earlier version of (G-4) gave $\mathrm{tr}_F(e_H)$ the value $[2]_q$, and the resulting product $[2]_q \cdot [4]_q^2 \cdot [6]_q \approx 216.96$ came within $1.81\%$ of the target; that factor is the $q$-dimension of $A^{(H)}$, not the trace of $e_H$, so the near-match does not survive. The discrepancy points to an incomplete specification of the constraints. Possible physical origins include a categorical correction to the vacuum volume normalization, a Plancherel weight for the electroweak block, or a Higgs-mixing correction of order $\mathcal{O}(\hbar_q^2)$ on the $Z$-host. Precise discrimination requires refining the substrate's categorical structure, and results that depend on $\mathcal{N}_{\rm sym}$ inherit this residual.
