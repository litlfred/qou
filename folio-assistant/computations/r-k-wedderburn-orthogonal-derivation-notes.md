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

## RESOLVED — using `hecke_characters.build_seminormal_matrices`

Switched the Hoefsmit character evaluation to the existing
`build_seminormal_matrices` infrastructure in `hecke_characters.py`,
which constructs the proper seminormal-form matrices for $T_i$ on each
shape and computes $\chi_\lambda(T_w)$ as numpy matrix-trace.

**Sanity verification** (tr_M consistency on each class):

| class | direct $\mathrm{tr}_M(T_{w_C})$ | $\sum_\lambda y_\lambda \chi_\lambda$ | $\Delta$ |
|--|--:|--:|--:|
| $e$ | $1.000000$ | $1.000000$ | $5 \times 10^{-18}$ |
| $(12)$ | $0.499320$ | $0.499320$ | $1 \times 10^{-19}$ |
| $(12)(34)$ | $0.249321$ | $0.249321$ | $2 \times 10^{-17}$ |
| $(123)$ | $0.249321$ | $0.249321$ | $-8 \times 10^{-18}$ |
| $(1234)$ | $0.124491$ | $0.124491$ | $-2 \times 10^{-18}$ |

$\mathrm{tr}_M$ and $y_\lambda \chi_\lambda$ now agree to the
limit of float-trace precision.

**Depth-3 representative $r_3$ at $H_4$**:

$$
  r_3 \;=\;
    -0.3056 \cdot 1
    + 1.4541 \cdot T_{(12)}
    - 0.6127 \cdot T_{(12)(34)}
    - 1.5593 \cdot T_{(123)}
    + 1.0000 \cdot T_{(1234)}
$$

(coefficients in the class-function basis with $T_{(1234)} = 1$
free-parameter normalisation).

**Lower-depth orthogonality** verified to $\sim 10^{-31}$:

$$
  \chi_{(4)}(r_3) = \chi_{(3,1)}(r_3) = \chi_{(2,2)}(r_3) =
  \chi_{(2,1,1)}(r_3) = 0
$$

**Markov pairing**:

$$
  \mathrm{tr}_M(r_3) \;=\; y_{(1^4)} \cdot \chi_{(1^4)}(r_3)
                     \;=\; +0.003463
$$

Both sides agree to numerical precision — confirming $r_3$ is
genuinely depth-3 orthogonal under the central-character-defined
Markov trace.

**Reading**: $\alpha_3(H_4) = +0.003463$ at $q_0 \approx 1.110$ —
the depth-3 stratum coefficient extracted from H_4 via Wedderburn-
orthogonal projection.  This is a **structural number** (no fitting),
the analogue at $H_4$ of $\alpha_3(H_3) = h z^2 + z \approx 0.5514$
— note the dramatic decrease (factor 159×) reflecting the
increasing dilution of depth-3 contribution as $n$ grows.

## OUTSTANDING (not blocked anymore — extension work)

After extending the script to all 5 conjugacy classes with hand-derived
Hoefsmit characters (see `wedderburn_orthogonal_r_k.py`), the
4×5 system solves cleanly with 1D kernel:

```
class           c_C
e               +0.1046
(12)            -2.1753
(12)(34)        +0.2224
(123)           +0.5425
(1234)          +1.0000   (free parameter)
```

Lower-depth orthogonality verifies to $10^{-41}$ (full mp.dps=40 precision).

**However**, the Wedderburn consistency check fails: by the central
character expansion $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$,
we should have

$$
  \mathrm{tr}_M(r_3) \;=\; y_{(1^4)} \cdot \chi_{(1^4)}(r_3)
$$

since the lower-depth $\chi_\lambda(r_3)$ all vanish.  Numerically:

- $\mathrm{tr}_M(r_3)$ computed directly from Markov-reduced word
  values $= -0.667$
- $y_{(1^4)} \cdot \chi_{(1^4)}(r_3) = -0.000843 \cdot 1.954
  = -0.00165$

**Ratio: 400** — these should agree to numerical precision.

The discrepancy reveals that **my hand-derived Hoefsmit characters
for non-trivial irreps $(3, 1), (2, 2), (2, 1, 1)$ are not internally
consistent** with the central-character identity that actually defines
$y_\lambda$ in the witness file.

Independent verification (single-rep test):

$$
  \mathrm{tr}_M(T_{(1234)}) \;=\; z^3 \;\approx\; 0.124,
$$

but $\sum_\lambda y_\lambda \cdot \chi_\lambda(T_{(1234)})$ with my
hand-derived values gives $0.554$ — also off by ~4×.

The failure is in my non-trivial-rep entries; trivial rep $\chi_{(4)}$
and sign rep $\chi_{(1^4)}$ check out exactly.

## Status: blocked on correct Hoefsmit characters

`wedderburn_orthogonal_r_k.py` implements the diagnostic but tabulates
characters only for 4 of the 5 classes — the disjoint-pair class
$(12)(34)$ requires explicit Hoefsmit-seminormal evaluation of
$T_1 T_3$ on the standard tableaux of each shape. The 4-class
restriction is **full rank** (det = 3.39 at $q_0$), confirming the
need for the 5th class.

**RESOLVED** by switching to the existing
`hecke_characters.build_seminormal_matrices` infrastructure
(Hoefsmit matrices via numpy, traces direct). All five class
characters tabulated for the five partitions of 4. See "RESOLVED"
section above.

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

## H_5 and H_6 status (added 2026-04-26)

**Numerical extraction** (`r_k_h5_h6_numeric.py`): runs in <30 seconds via
`build_seminormal_matrices`. Sanity check `tr_M = Σ y_λ χ_λ` verifies to
~10⁻¹⁶ at every conjugacy class for both n.

**Hook shapes** (single-row, single-column-leg, $(n-2, 1, 1)$, …) extract
cleanly under the c[last]=1 numerical gauge:

| n | hook shape α_λ at q_0 |
|---|---|
| 5 | (5)=+0.617, (4,1)=−0.571, (3,1,1)=+0.088, (2,1,1,1)=+0.005, (1⁵)=+0.0005 |
| 6 | (6)=+0.378, (5,1)=−0.377, (4,1,1)=+0.065, (3,1,1,1)=+0.004, (2,1⁴)=+0.0006, (1⁶)=+0.00008 |

**Non-hook shapes** ((3,2), (2,2,1) at H_5; (4,2), (3,3), (3,2,1), (2,2,2),
(2,2,1,1) at H_6) hit gauge degeneracies analogous to the (2,2) case at
H_4. Symbolic null-space resolution is in principle the same as the H_4
case, but **sympy full-matrix construction at n=5 times out at 300s**
on the agent runner — partition (3,2) has dim 5 and the full character
matrix involves products of dim-5 sympy matrices.

## Next-step recommendations for closing H_5+ symbolic

- **Halverson–Ram explicit q-character formulas** (1995): bypass building
  the seminormal matrix entirely, evaluate $\chi_\lambda(T_w)$ via
  closed expressions on standard tableaux. Should be ~10× faster than
  full matrix products.
- **Lagrange/CRT interpolation**: evaluate the character matrix at
  $\sim 10$ rational $q$ values numerically, fit each character entry
  to a $q$-polynomial, then null-space symbolically. Only needs cheap
  numeric character evaluation.
- **Iterative LLL-style rationalisation**: use mpmath PSLQ on each
  numerical α_λ to recover the q-rational form. Has worked at α_EM and
  for the y_λ symbolic witness (cherry-picked from claude/spectral-
  derivation-followups).

Estimated effort for any of the three: 1–2 sessions.
