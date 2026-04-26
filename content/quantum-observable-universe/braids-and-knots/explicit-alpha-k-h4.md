**Proposition (explicit $\alpha_3$ at $H_4(R, q)$).**
*Let $z = 1/(\sqrt q + 1/\sqrt q)$ be the Markov parameter and
$\{T_{w_C}\}_C$ canonical Hecke representatives of the $p(4) = 5$
conjugacy classes of $S_4$:*

| label | cycle type | reduced word $w_C$ | length |
|--|:--:|:--:|:--:|
| $C_0 = e$ | $1^4$ | $\emptyset$ | $0$ |
| $C_1$ | $2 \cdot 1^2$ | $\sigma_1$ | $1$ |
| $C_2$ | $2^2$ | $\sigma_1 \sigma_3$ | $2$ |
| $C_3$ | $3 \cdot 1$ | $\sigma_1 \sigma_2$ | $2$ |
| $C_4$ | $4$ | $\sigma_1 \sigma_2 \sigma_3$ | $3$ |

*Then the depth-3 Wedderburn-orthogonal representative*

$$
  \boxed{\;
    r_3 \;=\; \sum_{C} c_C \cdot T_{w_C},
    \qquad
    \mathbf{c} \,=\,
    (-0.3056, +1.4541, -0.6127, -1.5593, +1.0000)
  \;}
$$

*satisfies $\chi_\lambda(r_3) = 0$ for every $\lambda \,\vdash\, 4$ with
$\mathrm{depth}(\lambda) < 3$ (verified to $\sim 10^{-31}$), and pairs
to*

$$
  \alpha_3(H_4)
  \;=\; \mathrm{tr}_M(r_3)
  \;=\; y_{(1^4)} \cdot \chi_{(1^4)}(r_3)
  \;\approx\; +0.003463
$$

*at the substrate value $q_0 \approx 1.110$.*

## Proof

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
lower-depth orthogonality constraints
([working note](#wedderburn-orthogonal-r-k-notes)).

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
`folio-assistant/computations/hecke_characters.py`):

| class | $\chi_{(4)}$ | $\chi_{(3,1)}$ | $\chi_{(2,2)}$ | $\chi_{(2,1,1)}$ | $\chi_{(1^4)}$ |
|:--:|--:|--:|--:|--:|--:|
| $e$ | $1.000$ | $3.000$ | $2.000$ | $3.000$ | $1.000$ |
| $(12)$ | $1.110$ | $1.319$ | $0.209$ | $-0.692$ | $-0.901$ |
| $(12)(34)$ | $1.232$ | $-0.768$ | $2.044$ | $-1.188$ | $0.812$ |
| $(123)$ | $1.232$ | $0.232$ | $-1.000$ | $-0.188$ | $0.812$ |
| $(1234)$ | $1.368$ | $-1.110$ | $0.000$ | $+0.901$ | $-0.731$ |

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

## Significance

This proposition extends the H_3 closure of
[explicit α_k at H_3](#prop:explicit-alpha-k-h3) to H_4, providing
the second concrete data point in the structural derivation of
$\alpha_k(H_n)$ for the unified mass formula.

The dramatic decrease from $\alpha_3(H_3) = h z^2 + z \approx 0.5514$
to $\alpha_3(H_4) \approx 0.003463$ (factor $159$) reflects the
**dilution of the depth-3 stratum** as $n$ grows — at $H_4$ the
depth-3 partition $(1^4)$ has Plancherel weight $y_{(1^4)} \approx
-8.4 \times 10^{-4}$ (sign-indefinite, see
[sign-pattern remark](#rem:y-lambda-sign-pattern)), while at $H_3$
it has weight $y_{(1^3)} \approx 0.0227$.

## Open

- **Closed-form $\mathbf{c}$.**  The numerical $r_3$ coefficients
  should admit closed-form expressions in $\mathbb{Q}(q^{1/2})$
  via symbolic linear-system solve (analogous to
  [y-lambda symbolic witness](#witness:y-lambda-symbolic)).
  Mechanical extension; not yet executed.

- **Extension to $H_5, H_6$.**  Analogous construction with $p(5) = 7$
  and $p(6) = 11$ classes.  The class-function basis grows but
  remains finite-dimensional; the linear system always has 1D
  solution space generically.

## Witness

[`folio-assistant/computations/wedderburn_orthogonal_r_k.py`](#) —
implements the class-function basis construction, character
evaluation via `build_seminormal_matrices`, and 4×5 linear-system
solve.  Output:
[`wedderburn-orthogonal-r-3-h4.witness.json`](#).
