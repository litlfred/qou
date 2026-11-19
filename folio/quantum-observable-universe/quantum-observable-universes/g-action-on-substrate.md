This conjecture posits that the Frobenius–Hopf substrate $A$ in $\mathbf{Rep}(\mathrm{SU}_q(2))$ admits a unique $G$-equivariant structure under $G = \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$. This structure is governed by four constraints linking the categorical data to the electroweak sector. From these constraints, the symmetric-channel Frobenius trace $\mathcal{N}_{\rm sym}(q) = \mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ is computable in closed form.

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

This rank-1 projector isolates the unbroken 1-dimensional subspace of $A^{(H)}$. By Constraint (G-2), its trace dimension is $[2]_q$.

### Derivation of $\mathcal{N}_{\rm sym}(q)$

Composing the traces over the components yields:

$$
  \mathrm{tr}_F\bigl(e_{\rm sym}^{\rm EW} \cdot e_H\bigr)
  \;=\;
  \dim_q(e_{\rm sym}^{\rm EW}\bigl[A^{(W^+)} \oplus A^{(W^-)} \oplus A^{(Z)}\bigr]) \;\cdot\;
  \dim_q\bigl(e_H \cdot A^{(H)}\bigr).
$$

Applying the assignments from the first two constraints yields:

- $\dim_q(e_{\rm sym}^{\rm EW}[A^{(W^\pm)}]) = [4]_q$
- $\dim_q(e_{\rm sym}^{\rm EW}[A^{(Z)}]) = [6]_q$
- $\dim_q(e_H \cdot A^{(H)}) = [2]_q$

Thus,

$$
  \mathcal{N}_{\rm sym}(q)
  \;=\;
  [4]_q \cdot [4]_q \cdot [6]_q \cdot [2]_q
  \;=\;
  [2]_q \cdot [4]_q^2 \cdot [6]_q.
$$

This derivation grounds Anchor II explicitly in categorical structures. See [Table 2](#tbl:g-action-on-substrate-table2-data).

### Verification

At the value $q_0 = {{ qou.computations.q-pinning-50-digit.derived_50_digit.q | precision: 6 }}\ldots$, the predicted trace evaluates to:

$$
  [2]_q \cdot [4]_q^2 \cdot [6]_q \;=\; 2.0109 \cdot 16.892 \cdot 6.388
  \;\approx\; 216.96.
$$

Compared to the CODATA target $\mathcal{N}_{\rm sym}(q_0) = 213.11$, this leaves a residual deviation of $-1.81\%$.

The small discrepancy suggests an incomplete specification of the constraints. Possible physical origins include a categorical correction to the vacuum volume normalization, a Plancherel weight for the electroweak block, or a Higgs-mixing correction of order $\mathcal{O}(\hbar_q^2)$ on the $Z$-host. Precise discrimination requires refining the substrate's categorical structure, and results that depend on $\mathcal{N}_{\rm sym}$ inherit this residual.
