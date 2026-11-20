The proposal is that the Frobenius–Hopf substrate $A$ in $\mathbf{Rep}(\mathrm{SU}_q(2))$ admits a unique $G$-equivariant structure under $G = \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$. This structure is governed by four constraints linking the categorical data to the electroweak sector. The constraints are intended to give the symmetric-channel Frobenius trace $\mathcal{N}_{\rm sym}(q) = \mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ in closed form. The closed form depends on how the trace composes across the hosts, which is not yet fixed (see below).

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
The Higgs vacuum value $\langle\Phi\rangle \in A$ is a non-zero vortex morphism $\varrho_\Phi \colon \mathbf{1} \to A^{(H)}$, unique up to a non-zero scalar, satisfying

$$
  Q \cdot \varrho_\Phi = 0, \qquad
  \mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi) = v^2 / m_e^2,
$$

where $Q = T_3 + Y$ is the unbroken charge generator and $v \approx 246\,\mathrm{GeV}$ is the weak vacuum expectation value. The first condition forces neutrality under the unbroken $\mathrm{U}(1)_{\text{em}}$ and, when the neutral subspace of $A^{(H)}$ is one-dimensional, fixes $\varrho_\Phi$ up to a non-zero scalar. The second fixes the modulus of that scalar to the empirical Higgs VEV and leaves its phase free, so $\varrho_\Phi$ is unique only up to a phase. The idempotent $e_H$ of (G-4) does not depend on that phase.

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

### The closed form for $\mathcal{N}_{\rm sym}(q)$: an open identification

The previous version of this section wrote
$\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ as $\dim_q$ of the image of $e_{\rm sym}^{\rm EW}$ on $A^{(W^+)} \oplus A^{(W^-)} \oplus A^{(Z)}$ times $\dim_q(e_H \cdot A^{(H)})$. It then multiplied the per-host dimensions. That step is not justified, for two reasons.

1. *$q$-dimension is additive over direct sums and multiplicative over tensor products.* (G-1) makes $A^{(W^+)}$, $A^{(W^-)}$, $A^{(Z)}$ and $A^{(H)}$ direct summands of $A$, so the $q$-dimension of their direct sum is the sum of the per-host values, not their product.
2. *The trace of a composite of idempotents is not in general a product of traces.* If $e_{\rm sym}^{\rm EW}$ and $e_H$ are idempotents of $A$ supported on the orthogonal summands of (G-1), then $e_{\rm sym}^{\rm EW} \cdot e_H = 0$. A non-zero value of $\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ therefore needs the two idempotents to act on different tensor factors, which (G-1) does not supply.

The corpus does not settle which object is meant. Two readings are recorded, and neither is selected.

- **Reading (a), tensor product.** The electroweak host is $A^{(W^+)} \otimes A^{(W^-)} \otimes A^{(Z)}$, the Higgs host $A^{(H)}$ is a further tensor factor, and $\mathrm{tr}_F$ is multiplicative on $e_{\rm sym}^{\rm EW} \otimes e_H$. Then, with (G-2) and (G-4),

$$
  \mathcal{N}_{\rm sym}^{(a)}(q)
  \;=\;
  [4]_q \cdot [4]_q \cdot [6]_q \cdot 1
  \;=\;
  [4]_q^2 \, [6]_q.
$$

This reading needs a tensor structure on the hosts that (G-1) does not state. The nearest corpus object is the disjoint-strand-pair realisation of [the Hoefsmit cell-content theorem](#thm:hoefsmit-ew-cell-content), where $W$, $Z$ and $H$ act on separate strand pairs of $V^{\otimes 6}$. That object has a single $W$ slot rather than separate $W^+$ and $W^-$ hosts, and it assigns $H$ the link $T(2,8)$, not the $q$-dimension $[2]_q$ of (G-2). So it does not establish reading (a).

- **Reading (b), direct sum, as (G-1) states.** The $q$-dimension of the symmetric-channel image is additive over the summands:

$$
  \dim_q\!\bigl(e_{\rm sym}^{\rm EW}\bigl[A^{(W^+)} \oplus A^{(W^-)} \oplus A^{(Z)}\bigr]\bigr)
  \;=\;
  2\,[4]_q + [6]_q,
$$

taking $e_{\rm sym}^{\rm EW}$ to act as the identity on each host, as (G-2) assumes. Keeping the outer factor $\dim_q(e_H \cdot A^{(H)}) = \mathrm{tr}_F(e_H) = 1$ gives $\mathcal{N}_{\rm sym}^{(b)}(q) = 2\,[4]_q + [6]_q$. By point 2 this is not $\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$. It is the $q$-dimension of the symmetric-channel image, and the composition rule that would turn it into the trace is not specified.

The factor $1$ in both readings is (G-4): $e_H$ factors through $\mathbf{1}$ ([the Higgs vacuum-residual idempotent](#prop:higgs-vacuum-residual-idempotent), Lean `VacuumPairing.tr_proj_eq_one`). The host labels $T(2,4)$ and $T(2,6)$ of (G-2) come from [the electroweak/Higgs torus-link identification](#conj:electroweak-higgs-torus-link-triplet), which is itself a conjecture. See [Table 2](#tbl:g-action-on-substrate-table2-data).

### Comparison with the anchor value

The comparison point is the value $\mathcal{N}_{\rm sym}(q_0) \approx 213.11$ that `computations/n_sym_numerical_anchor.py` obtains by dividing the CODATA-derived crossing count $N_v$, fixed by $G_F$, by the host product $\prod_{k=2,3,4}[2k]_q^2/[2]_q$. It is a back-solve from an experimental input, so the comparison below is where this block makes an empirical claim. At $q_0 = {{ qou.computations.q-pinning-50-digit.derived_50_digit.q | precision: 6 }}\ldots$, with $[n]_q = (q^n - q^{-n})/(q - q^{-1})$, $[4]_{q_0} \approx 4.1097$ and $[6]_{q_0} \approx 6.3881$:

| reading | closed form | value at $q_0$ | relative to $213.11$ |
|---------|-------------|---------------:|---------------------:|
| (a) tensor product | $[4]_q^2\,[6]_q$ | $\approx 107.89$ | $\approx -49.4\%$ |
| (b) direct sum | $2\,[4]_q + [6]_q$ | $\approx 14.607$ | $\approx -93.1\%$ |

Neither reading reproduces the anchor. The miss does not bear on which reading is correct: the choice between them is a question about the categorical structure of the hosts, not about which value lies closer to $213.11$. Until the composition rule is specified, the block does not ground the anchor value, and results that depend on $\mathcal{N}_{\rm sym}$ inherit both the unresolved identification and the miss.

An earlier version of (G-4) gave $\mathrm{tr}_F(e_H)$ the value $[2]_q$, and the resulting product $[2]_q \cdot [4]_q^2 \cdot [6]_q \approx 216.96$ came within $1.81\%$ of the target. That factor is the $q$-dimension of $A^{(H)}$, not the trace of $e_H$, and the product rests on reading (a), so the near-match does not survive.
