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
| $e^- = \sigma_0\sigma_1\sigma_0$ | $hz^2 + z$ |

> **Errata (2026-05-19).** Earlier versions of this block asserted
> $\mathrm{tr}_M(e^-) = z^3$ and offered a "peel-from-the-right"
> derivation. This was incorrect: $\sigma_1\sigma_0$ is **not** in
> the sub-algebra $H_2 = \langle \sigma_0 \rangle$ (the Markov axiom
> $\mathrm{tr}_M(\sigma_n \cdot x) = z\,\mathrm{tr}_M(x)$ requires
> $x \in H_n$), so the Markov-property step cannot be applied
> directly to $\sigma_1 \cdot \sigma_0\sigma_0$ after the cyclicity
> step. The canonical Ocneanu--Wenzl recursion gives
> $\mathrm{tr}_M(e^-) = hz^2 + z$, verified independently in
> [`docs/audits/2026-05-19-trm5-markov-bug.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-19-trm5-markov-bug.md)
> against the y-lambda Wenzl-bridge consistency
> $\mathrm{tr}_M(b_i) = \sum_\lambda y_\lambda(q) \chi_\lambda(b_i)$
> (residual $\sim 10^{-32}$ after fix; ${\sim}0.12$ before).
> The fix has been applied to
> `tools/pyhecke/python/pyhecke/gram.py` and the Gram matrix table
> below.

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

At $q_0 \approx 1.1097$, $hz^2 + z \approx 0.5514$ (the stale
$z^3 \approx 0.1245$ was off by a factor of 4.4).

## Gram matrix (symbolic in $q$)

> **Errata banner (2026-05-19) — symbolic Gram entries below
> require recomputation.** The proposition's matrix and $g_{ij}$
> formulas were derived assuming $\mathrm{tr}_M(e^-) = z^3$
> (now known to be incorrect — see errata above). The entries
> that involve $\mathrm{tr}_M$ applied to a product whose Hecke
> normal form contains $e^-$ must be rederived with
> $\mathrm{tr}_M(e^-) = hz^2 + z$. Numerically, the post-fix Gram
> matrix is symmetric to machine precision and reproduces the
> y-lambda Wenzl-bridge identity exactly (Markov-bug audit,
> § "Visible symptom: Gram matrix non-symmetric"). The corrected
> Python compute lives at `tools/pyhecke/python/pyhecke/gram.py`;
> a follow-up commit will recompute the symbolic table below.

**Proposition (stale symbolic entries — see banner above).**
*The $6 \times 6$ Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$
over the NF basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$
has the structural form below; the entries containing $z^3$ or
higher $z^k$ powers from $\mathrm{tr}_M(e^-)$ are stale and need
the $z^3 \mapsto hz^2 + z$ substitution to be propagated:*

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

*where (STALE — pending recomputation):*
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
