# Working notes: Wedderburn-orthogonal r_k at H_n via class functions

These are *agent working notes* — partial structural progress on the
open cohomological question of "canonical depth-k representatives r_k
at H_n>3" identified in
[explicit-alpha-k-h3.md / Open](#prop:explicit-alpha-k-h3) and
[wedderburn-bratteli-recursion.md / Open](#prop:wedderburn-bratteli-recursion).

## The question

At $H_3(R, q)$, the canonical r_k were

| depth k | r_k | length |
|:--:|--|:--:|
| 0 | $1$ | 0 |
| 1 | $\sigma_1 - \sigma_2$ | 1 |
| 2 | $\sigma_1\sigma_2 + \sigma_2\sigma_1$ | 2 |
| 3 | $\sigma_1\sigma_2\sigma_1$ | 3 |

These pair with $\mathrm{tr}_M$ to give $\alpha_k = 1, 0, z^2, hz^2 + z$.
At $H_n > 3$ the analogous representatives need cohomological
justification — which length-k word pairs cleanly with depth-k
characters, orthogonal to lower depths?

## Initial approach (failed): length-k word subspace

**Diagnostic** (`coxeter_h4_depth_test.py`): at H_4, the linear Coxeter
prefix $\sigma_1\sigma_2\sigma_3$ has Markov pairing $\mathrm{tr}_M = z^3$,
but only **0.0006** of that ($-0.7\%$) sits in the depth-3 stratum
$\{(1^4)\}$. The other $99.7\%$ comes from depths 0, 1, 2.

**Why**: in $H_4$ there are 6 length-3 reduced words, but they fall
into only 2 conjugacy classes in $S_4$ (3-cycle vs 4-cycle). After
character-equivalence collapse, the length-3 stratum spans a
**2-dimensional** class-function space.

Imposing 4 lower-depth orthogonality constraints
($\chi_{(4)} = \chi_{(3,1)} = \chi_{(2,2)} = \chi_{(2,1,1)} = 0$)
in a 2D space is **over-constrained** — generically no solution.

## Correct approach: full class-function basis

The conjugacy classes of $S_n$ form the natural class-function basis.
At $H_4$ there are $p(4) = 5$ classes:

| label | cycle type | length of canonical word |
|--|:--:|:--:|
| $e$ | $1^4$ | 0 |
| $(12)$ | $2 \cdot 1^2$ | 1 |
| $(12)(34)$ | $2^2$ | 2 (disjoint pair) |
| $(123)$ | $3 \cdot 1$ | 2 |
| $(1234)$ | $4$ | 3 |

Each class has a canonical Hecke representative $T_{w_C}$ in
$H_4(R, q)$. A general class function on $H_4$ is

$$
  r \;=\; \sum_C c_C \cdot T_{w_C}, \qquad C \in \{e, (12), (12)(34), (123), (1234)\}.
$$

Imposing $\chi_\lambda(r) = 0$ for $\lambda \in \{(4), (3,1), (2,2), (2,1,1)\}$
(four depth-$<3$ partitions) gives a $4 \times 5$ system in 5 unknowns —
a **1-dimensional** solution space, uniquely determining $r_3$ up to
scale. This is the cohomologically-correct $r_3$.

## Status: blocked on missing Hoefsmit characters

`wedderburn_orthogonal_r_k.py` implements the diagnostic but tabulates
characters only for 4 of the 5 classes — the disjoint-pair class
$(12)(34)$ requires explicit Hoefsmit-seminormal evaluation of
$T_1 T_3$ on the standard tableaux of each shape. The 4-class
restriction is **full rank** (det = 3.39 at $q_0$), confirming the
need for the 5th class.

**Outstanding tabulation work** (single-session feasible):

| $\lambda$ | $\chi_\lambda(T_1 T_3)$ |
|:--:|--|
| $(4)$ | $q^2$ ✓ |
| $(3, 1)$ | needs Hoefsmit |
| $(2, 2)$ | needs Hoefsmit |
| $(2, 1, 1)$ | needs Hoefsmit |
| $(1^4)$ | $q^{-2}$ ✓ |

Once the missing values are supplied, the linear system is
$4 \times 5$ with 1-dim kernel — the closed-form $r_3$ at $H_4$ falls
out as a $q$-rational vector $\{c_C\}_{C}$ in $\mathbb{Q}(q^{1/2})$
analogous to the H_3 closed forms.

## Effort estimate

| Task | Effort |
|--|:--:|
| Tabulate $\chi_\lambda(T_1 T_3)$ for $\lambda \in \{(3,1), (2,2), (2,1,1)\}$ via Hoefsmit | 1 session (mechanical) |
| Solve 4×5 system, extract $r_3$ closed form | trivial after above |
| Verify $\alpha_3(H_4) = \mathrm{tr}_M(r_3) / \dim(r_3)$-equivalent | trivial |
| Repeat for $r_4$ at $H_5$ (class-function basis size 7) | 1-2 sessions |
| Repeat for $H_6$ (class-function basis size 11) | 2-3 sessions |
| **Pattern conjecture**: closed form for $r_k$ at general $H_n$ | research-grade |

## Witness

[`wedderburn-orthogonal-r-3-h4.witness.json`](#) — diagnostic JSON
with rank check showing 4-class basis is full rank, so 5th class is
required.

[`wedderburn_orthogonal_r_k.py`](#) — extraction script (currently
blocked at $(12)(34)$ Hoefsmit values).
