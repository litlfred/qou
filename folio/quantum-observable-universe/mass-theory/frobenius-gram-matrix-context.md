The Frobenius self-duality $A \cong A^\vee$ induces a concrete
bilinear form on $H_3(q)$ via the Markov trace.  The **Gram
matrix** $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ over the NF
basis encodes all interaction pairings, and its inverse
$G^{-1}$ gives the explicit dual construction
$K^\vee = \sum_{i,j} c_i (G^{-1})_{ij} b_j$.

> **$G$ is singular on $H_3$ under Convention D — read $G^{-1}$ on the
> Temperley–Lieb quotient.** The dual
> construction it defines, presuppose $\det G \neq 0$. That holds under the
> excised **convention C**, where the antisymmetric weight
> $y_{(1^3)} = 0.0227449\ldots$ is small but nonzero. It fails under the
> production **convention D**: the pin $z(q^2+1) = q^3$ forces
> $y_{(1^3)} = 0$ exactly, so the $(1^3)$ block **is** the radical of the trace
> form and $\det G = 0$ — not "numerically singular", zero. A $G^{-1}$ computed
> under C is therefore not an approximation to one under D; the latter does not
> exist, and at $n = 3$ the corank is exactly $1$.
>
> The Frobenius structure itself is not lost, only relocated: the radical is a
> two-sided ideal, so $\mathrm{tr}_M$ descends to
> $H_3/\mathrm{rad} \cong \mathrm{TL}_3$ and the induced pairing there **is**
> non-degenerate. Every use of $G^{-1}$ and of $K^\vee$ below should be read on
> that $5$-dimensional quotient ($\sum \dim^2 = C_3 = 5$), not on the
> $6$-dimensional $H_3$.
>
> Proved in
> [`MarkovGramDegenerate.lean`](../lean/QOU/QBeta/MarkovGramDegenerate.lean):
> `block_mem_radical` (a zero-weight block lies in the radical) `$\to$`
> `gram_det_eq_zero_of_radical_combination` ($\det G = 0$), with
> `pairing_descends` and `mem_radical_of_pairing_zero` giving the descent.

## Markov trace of NF basis elements

Write $h = q - q^{-1}$ and $z = q^{3}/(q^{2}+1)$ (**convention D**).

See [Table 1](#tbl:frobenius-gram-matrix-table1-data).

The trace of $e^-$ follows from the Ocneanu--Wenzl Markov recursion
(cyclicity + Hecke quadratic + Markov axiom restricted to the
sub-algebra):
$\mathrm{tr}_M(\sigma_0\sigma_1\sigma_0)
= \mathrm{tr}_M(\sigma_1\sigma_0^2) \;\text{(cyclicity)}
= \mathrm{tr}_M(\sigma_1(h\sigma_0+1)) \;\text{(Hecke quadratic)}
= h\cdot\mathrm{tr}_M(\sigma_1\sigma_0) + \mathrm{tr}_M(\sigma_1)
= h \cdot z\,\mathrm{tr}_M(\sigma_0) + z
= hz^2 + z$
(the last step uses the Markov axiom on $\sigma_1$ paired with
$\sigma_0 \in H_1$).

At the proton-pinned $q_0 \approx 1.1099785828$ with $z = q^3/(q^2+1)$,
$hz^2 + z \approx 0.6912$, and the naive $z^3 \approx 0.2300$ is off by a
factor of 3.0 (compared with $0.5514$ and $0.1245$ under Convention C at the muon anchor).

## Operator identification via the dual

The Frobenius dual
([def:frobenius-dual-h3](#def:frobenius-dual-h3)) exactly
identifies each basis element with its corresponding knot operator.

**Proposition (operator identification).**
*For each NF basis element $b_k$, the pairing of $b_k^\vee$
with the knot operators $\beta(T_{m,n})$ satisfies:*

See [Table 2](#tbl:frobenius-gram-matrix-table2-data).

*Each basis element pairs maximally with exactly one knot
operator (the operator whose braid word contains that element).
The electron dual $e^{-\vee}$ pairs with $T_{2,3}$ (trefoil)
with coefficient $1$ — the Frobenius dual selects the trefoil
operator for the electron.*

## Annihilation identity (symbolic)

**Proposition.**
*$e^- \cdot e^+ = \gamma$ (the photon / identity), for all $q$.*
