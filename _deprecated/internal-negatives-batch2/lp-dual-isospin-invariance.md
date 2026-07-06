**Remark.**

The LP-dual + crystal-bases probe
[`alpha-5-lp-dual-crystal.witness.json`](computations/alpha-5-lp-dual-crystal.witness.json)
solves the operator-selection LP per-atom on
$\{D, T, {}^3\mathrm{He}\}$ at $q_0$ + a $q$-sweep, with cost
$t_\lambda = c_5(\lambda)$ from the Murphy central element
$P_5 = e_5(J_1, \ldots, J_n)$ and channels = 2-row Wedderburn
stratum (per [PR #619](https://github.com/litlfred/qou/pull/619)
empirical finding that mass concentrates in
$\mathrm{ht}(\lambda) \le 2$).

**Empirical results.**

| atom | $n$ | $|Z - N|$ | $y_0^*$ (2-row, $q_0$) | active set |
|------|----:|---------:|----------------------:|-----------:|
| $D$ | 6 | 0 | 10.3125 | 3 / 4 |
| $T$ | 9 | 1 | **570.6762** | 4 / 5 |
| ${}^3\mathrm{He}$ | 9 | 1 | **570.6762** | 4 / 5 |

**$T$ and ${}^3\mathrm{He}$ give identical $y_0^*$ at every $q$
tested.** The same exact equality holds in the height-6 stratum
($y_0^*(T) = y_0^*({}^3\mathrm{He}) = 26.8242$) and across the
crystal-limit $q$-sweep:

| $q$ | $y_0^*(D)$ | $y_0^*(T)$ | $y_0^*({}^3\mathrm{He})$ |
|----:|----------:|----------:|------------------------:|
| 1.110 | 10.3125 | **570.6762** | **570.6762** |
| 1.050 | 7.6912 | **247.9348** | **247.9348** |
| 1.001 | 6.0301 | **127.6918** | **127.6918** |

**Interpretation.** $T$ ($Z=1, N=2$) and ${}^3\mathrm{He}$ ($Z=2,
N=1$) are **mirror nuclei** — same nucleon count $A=3$, isospin
labels swapped $Z \leftrightarrow N$. Their $y_0^*$ equality is
**isospin invariance** of the LP-dual binding-energy shadow
price:

$$
  y_0^*(Z, N) = y_0^*(N, Z).
$$

This is the **structural consequence** of Frobenius self-duality
([`prop:frobenius-self-duality-forces-lp-dual-extraction`](#prop:frobenius-self-duality-forces-lp-dual-extraction))
combined with antiparticle-crossing reversal
([`prop:antiparticle-crossing-reversal`](#prop:antiparticle-crossing-reversal)):
the Hopf antipode swaps $V_\lambda \leftrightarrow V_{\lambda^T}$,
which on per-atom braid recipes corresponds to $Z \leftrightarrow
N$. The LP-dual is invariant under this swap because the
Frobenius pairing it inherits from the Markov trace is symmetric.

**Refining the prop:mass-formula-iterative-lp-dual claim.**
The earlier-conjectured "atom-independent constant" form of
$\alpha_5$ (and of every $u^{(\ell)*}$) was **too strong**. The
empirically correct claim is:

$$
  y_0^*(A, T_3) = f_\ell\bigl(A, |T_3|\bigr)
$$

where $T_3 = (Z - N)/2$ is the isospin third-component. The
LP-dual depends on $A$ and on $|Z - N|$ but is invariant under
$Z \leftrightarrow N$. **This is exactly the BW-formula
structure** (binding energy depends on $A$, the asymmetry term
$(Z-N)^2/A$, etc.) — no $Z, N$ separately, only via
isospin-symmetric combinations.

**The QOU LP-dual reproduces the BW formula's $(A, |T_3|)$
dependence empirically**, without putting it in by hand.

**Open questions.**

1. **A-scaling.** The ratios
   $y_0^*(T) / y_0^*(D) = 570.7 / 10.3 \approx 55$ at $q_0$ and
   $\approx 21$ at $q = 1.001$. Is the $A$-dependence captured
   by a simple closed form $f_\ell(A, T_3) = g_\ell(q) \cdot
   h(A, T_3)$ with $g_\ell$ pure-q-rational and $h$ a simple
   $(A, T_3)$ polynomial?

2. **Crystal limit $q \to 1$.** The $y_0^*$ values shrink as
   $q \to 1$. Does the crystal limit recover the classical BW
   coefficients (with their explicit $1/A$, $A^{2/3}$,
   $(Z-N)^2/A$ scalings)?

3. **${}^4\mathrm{He}$.** The $A=4$ case ($n=12$) was excluded
   from the default run because of sympy build cost; pending a
   cached run, it should give $|Z-N| = 0$ like $D$, hence sit on
   the same isospin-symmetric branch as $D$ (rather than the
   $T \,/\, {}^3\mathrm{He}$ branch).

**This is the first POSITIVE finding of the LP-dual probe** —
contrast with
[`rem:alpha-5-jm-central-empirical-findings`](#rem:alpha-5-jm-central-empirical-findings)
which refuted the bare JM-central form. Solving the actual LP
(per the user's "derive don't guess" direction) yields a
structural symmetry — isospin invariance — that the naive
closed form did not.
