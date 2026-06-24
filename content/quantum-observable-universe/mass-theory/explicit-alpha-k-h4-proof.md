By [α_k derivation procedure](#prop:alpha-k-derivation-procedure),
the depth-$k$ stratum coefficient $\alpha_k(H_n)$ is the Markov pairing
of $\mathrm{tr}_M$ with a class-function representative $r_k$ that is
**Wedderburn-orthogonal** to every lower-depth irrep — i.e.\
$\chi_\lambda(r_k) = 0$ for every $\lambda \,\vdash\, n$ with
$\mathrm{depth}(\lambda) < k$.

**Why class-function basis.**  The natural basis for class functions
on $H_n$ is the set of canonical conjugacy-class representatives
$\{T_{w_C}\}_C$.  At $H_4$ this is 5-dimensional.  The
length-restricted (length-$k$ word) approach fails: at $H_4$ the 6
length-3 reduced words collapse to just 2 conjugacy classes (3-cycle
$+$ 4-cycle) — only a 2-dim space, insufficient to satisfy 4
lower-depth orthogonality constraints (working note:
`computations/r-k-wedderburn-orthogonal-derivation-notes.md`).

**Linear system.**  Let
$M \in \mathbb{R}^{4 \times 5}$ have entries
$M_{i, C} = \chi_{\lambda_i}(T_{w_C})$ for the four lower-depth
partitions $\lambda \in \{(4), (3, 1), (2, 2), (2, 1, 1)\}$ indexed
by $i$, and the five conjugacy classes $C$.  The system

$$
  M \cdot \mathbf{c} \;=\; \mathbf{0},
  \qquad \mathbf{c} \in \mathbb{R}^5,
$$

has a 1-dimensional solution space at generic $q$ (the Hoefsmit
character matrix is full row-rank since the irreps are distinct).
Fixing the gauge $c_{C_4} = 1$, the remaining coefficients are
uniquely determined.

**Numerical evaluation at $q_0$.**  Hoefsmit characters computed via
[seminormal matrices](#prop:hoefsmit-seminormal-form) (see
`computations/hecke/hecke_characters.py`); the $5 \times 5$
character matrix at $q_0$ is recorded in
[`wedderburn-orthogonal-r-3-h4.witness.json`](https://github.com/litlfred/qou/blob/main/computations/wedderburn-orthogonal-r-3-h4.witness.json).

**Sanity verification** — central character identity at every class:

$$
  \mathrm{tr}_M(T_{w_C})
  \;=\;
  \sum_{\lambda \,\vdash\, 4} y_\lambda \cdot \chi_\lambda(T_{w_C})
$$

verifies to $\sim 10^{-17}$ numerical precision against the
Jones-Markov witness ([y-lambda witness](#witness:y-lambda-jones-markov)).
This anchors the Hoefsmit character values.

**Solving the system.**  $\mathbf{c} = (-0.3056, +1.4541, -0.6127,
-1.5593, +1.0000)$.

**Markov pairing on $r_3$.**  Markov-trace values on the 5 class
representatives are universal (Markov reduction):
$\mathrm{tr}_M(T_{w_C}) \in \{1, z, z^2, z^2, z^3\}$ for the five
classes respectively.  Hence

$$
  \mathrm{tr}_M(r_3)
  \;=\;
  c_0 + c_1 z + c_2 z^2 + c_3 z^2 + c_4 z^3
  \;\approx\; +0.003463.
$$

By the central character expansion plus orthogonality,

$$
  \mathrm{tr}_M(r_3)
  \;=\; \sum_\lambda y_\lambda \chi_\lambda(r_3)
  \;=\; y_{(1^4)} \cdot \chi_{(1^4)}(r_3)
$$

(only the depth-3 term survives).  Both sides agree to numerical
precision, confirming the construction.  $\square$
