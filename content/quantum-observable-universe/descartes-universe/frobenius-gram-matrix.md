The Frobenius self-duality $A \cong A^\vee$ induces a concrete
bilinear form on $H_3(q)$ via the Markov trace.  The **Gram
matrix** $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ over the NF
basis encodes all interaction pairings, and its inverse
$G^{-1}$ gives the explicit dual construction
$K^\vee = \sum_{i,j} c_i (G^{-1})_{ij} b_j$.

## Markov trace of NF basis elements

Write $h = q - q^{-1}$ and $z = 1/(q^{1/2} + q^{-1/2})$.

| Basis element $b_k$ | $\mathrm{tr}_M(b_k)$ |
|:---:|:---:|
| $\gamma = \mathbf{1}$ | $1$ |
| $\sigma_0$ | $z$ |
| $\sigma_1$ | $z$ |
| $L_+ = \sigma_0\sigma_1$ | $z^2$ |
| $L_- = \sigma_1\sigma_0$ | $z^2$ |
| $e^- = \sigma_0\sigma_1\sigma_0$ | $z^3$ |

The trace of $e^-$ follows from Yang--Baxter and the Markov property:
$\mathrm{tr}_M(\sigma_0\sigma_1\sigma_0)
= \mathrm{tr}_M(\sigma_1\sigma_0\sigma_1)
= z \cdot \mathrm{tr}_M(\sigma_1\sigma_0)
= z \cdot z^2 = z^3$.

**Note.** An earlier version of this document used a cyclicity
argument giving $hz^2 + z$.  That derivation incorrectly applied
$\sigma_0\sigma_1\sigma_0 = \sigma_0^2\sigma_1$ (cyclicity gives
$\mathrm{tr}_M(ABC) = \mathrm{tr}_M(CAB)$, yielding
$\sigma_0 \cdot \sigma_0\sigma_1 \neq \sigma_0^2\sigma_1$ as a
rewrite of $\sigma_0\sigma_1\sigma_0$).  The canonical Markov-property
derivation (peeling the boundary generator $\sigma_1$ from the right
at each step) gives $z^3$.

## Gram matrix (symbolic in $q$)

**Proposition.**
*The $6 \times 6$ Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$
over the NF basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ is:*

$$
  G
  =
  \begin{pmatrix}
    1     & z     & z     & z^2     & z^2     & z^3 \\
    z     & hz+1  & z^2   & hz^2+z  & z^3  & g_{15} \\
    z     & z^2   & hz+1  & z^3  & hz^2+z  & g_{15} \\
    z^2   & hz^2+z & z^3 & g_{15} & g_{34} & g_{35} \\
    z^2   & z^3 & hz^2+z & g_{34} & g_{15} & g_{35} \\
    z^3 & g_{15} & g_{15} & g_{35} & g_{35} & g_{55}
  \end{pmatrix}
$$

*where:*
- $g_{15} = hz^3 + z^2$ (from $\sigma_0 \cdot e^- = he^- + L_-$)
- $g_{34} = hz^3 + hz + 1$ (from $L_+ \cdot L_- = he^- + h\sigma_0 + \gamma$)
- $g_{35} = h^2z^3 + 2hz^2 + z$ (from $L_+ \cdot e^- = h^2e^- + hL_+ + hL_- + \sigma_1$)
- $g_{55} = (h^3+h)z^3 + 2h^2z^2 + 2hz + 1$ (from $e^- \cdot e^- = (h^3+h)e^- + h^2L_+ + h^2L_- + h\sigma_1 + h\sigma_0 + \gamma$)

*The matrix is **symmetric** ($G_{ij} = G_{ji}$, by cyclicity of the
Markov trace) and **non-degenerate** ($\det G \neq 0$ for $q \neq 0, 1$),
but **not positive definite** — it has indefinite signature.*

## Frobenius dual

**Definition.**
*For a state $K = \sum_i c_i b_i$ in NF, the **Frobenius dual**
is the unique element $K^\vee \in H_3(q)$ satisfying
$\langle K^\vee, b_j \rangle_F = c_j$ for all $j$.
Explicitly:*

$$
  K^\vee = \sum_{i,j} c_i (G^{-1})_{ij} b_j
$$

*The dual exists and is unique by non-degeneracy of $G$.*

**Verification.**
The pairing $\langle K^\vee, b_j \rangle_F = \sum_{i,k} c_i (G^{-1})_{ik} G_{kj} = \sum_i c_i \delta_{ij} = c_j$
by the defining property $G^{-1} G = I$.

## Operator identification via the dual

The Frobenius dual exactly identifies each basis element with
its corresponding knot operator.

**Proposition (operator identification).**
*For each NF basis element $b_k$, the pairing of $b_k^\vee$
with the knot operators $\beta(T_{m,n})$ satisfies:*

| $K$ | $\langle K^\vee, T_{1,0} \rangle$ | $\langle K^\vee, T_{2,1} \rangle$ | $\langle K^\vee, T_{2,2} \rangle$ | $\langle K^\vee, T_{2,3} \rangle$ | $\langle K^\vee, T_{2,5} \rangle$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\gamma$ | $1$ | $0$ | $1$ | $0$ | $0$ |
| $\sigma_0$ | $0$ | $1$ | $h$ | $0$ | $0$ |
| $\sigma_1$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $L_+$ | $0$ | $0$ | $0$ | $0$ | $h$ |
| $L_-$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $e^-$ | $0$ | $0$ | $0$ | $1$ | $h^2$ |

*Each basis element pairs maximally with exactly one knot
operator (the operator whose braid word contains that element).
The electron dual $e^{-\vee}$ pairs with $T_{2,3}$ (trefoil)
with coefficient $1$ — the Frobenius dual selects the trefoil
operator for the electron.*

## Annihilation identity (symbolic)

**Proposition.**
*$e^- \cdot e^+ = \gamma$ (the photon / identity), for all $q$.*

*Proof.* The braid word $\sigma_0\sigma_1\sigma_0 \cdot
\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1} = \mathbf{1}$ by the
group law in $B_3$.  No Hecke reduction is needed — the
cancellation is exact in the braid group, hence exact in
$H_3(q)$ for all $q$.

Equivalently, this is the Hopf relation
([vertex algebra relations](#prop:vertex-algebra-relations),
QU-2d): $\mu(S \otimes \mathrm{id})\Delta = \eta\varepsilon$,
where $S(\sigma_i) = \sigma_i^{-1}$ is the antipode.  The identity
$e^- \cdot e^+ = \gamma$ is the Hopf relation evaluated on
the trefoil.

**Witness**: `gram-matrix-dual.witness.json`.
