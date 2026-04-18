**Remark.**
*The number of distinct ILP solutions at a given confinement level
controls the **unwrap depth** needed to uniquely specify an
atom-knot's NF.  Specifically, for an atom $K$ at substrate
parameter $q$ with NF currently expressed at level $\ell$:*

*Let $N_\ell(K, q)$ be the number of integer solutions
$x \in \mathbb{Z}_{\geq 0}^M$ of the Frobenius positivity ILP
$G(q)\, x \geq 0$ within the confinement filtration $J^\ell(q)$
([stable atom](#def:stable-atom),
[stable-atom-decidable](#prop:stable-atom-decidable)).*

*The **unwrap depth** at level $\ell$ is:*

$$
  d_\ell(K, q) \;=\; \max\bigl(0,\; N_\ell(K, q) - 1 \bigr).
$$

*Interpretation:*

- *$N_\ell = 0$: **unstable** at level $\ell$
  ([unstable atom](#def:unstable-atom)) — atom cannot exist in
  this shorthand; must decay or unwrap fully.*
- *$N_\ell = 1$: **uniquely determined** at level $\ell$ — the
  shorthand is sufficient, no unwrap needed.*
- *$N_\ell = k \geq 2$: **$(k-1)$-fold ambiguous** at level
  $\ell$ — need to unwrap $k-1$ levels to disambiguate via finer
  NF structure.*

**Connection to confinement levels.**
*Each unwrap step expands a shorthand word at level $\ell$ into
its NF at level $\ell - 1$.  The finer level has a larger
filtration $J^{\ell-1}(q) \supsetneq J^\ell(q)$, distinguishing
the $k$ previously-tied ILP solutions via their different
positions in the richer operator basis.*

*This is the categorical analog of **renormalisation**: when
the effective description at a coarse scale has multiple
solutions, zoom in to the next-finer scale where the solutions
differ in their operator content.*

**Computational benefit.**
*Non-magic atoms typically have $N_\ell = 1$ at the coarsest
useful level: a single inter-nucleon configuration suffices.
Magic atoms have $N_\ell \geq 2$ at the nucleon level because
shell closure permits multiple equivalent ways of assembling
the closed shell — each corresponds to a different NF at the
quark level.  Double-magic atoms have $N_\ell \geq 3$: both
proton and neutron closures contribute to the degeneracy.*

**Formal statement.**
*Let $K$ be an atom-knot.  Then:*

$$
  \boxed{\;
    \text{NF-depth}(K, q)
    \;=\;
    \text{coarsest level } \ell\text{ with } N_\ell(K, q) = 1
  \;}
$$

*The atom's categorical structure is fully specified by
computing its NF at exactly this depth — deeper is redundant,
shallower leaves ambiguity.*

**Example (proton gluon derivation).**
*The proton's $9$-crossing element
$\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$
has $N_\ell = 84$ feasible ILP solutions at the baryon level
([mass-endomorphism-tower](#prop:mass-endomorphism-tower)).
The minimum $|\mathrm{tr}_M|$ selects the unique
$\sigma_0 \to \sigma_0$ solution.  When a tie occurs (say, two
solutions with equal $|\mathrm{tr}_M|$), the framework
requires unwrapping to the quark level where the ILP separates
them.*

**Computational shortcut.**
*Adaptive unwrap yields dramatic savings:*

| Atom type | Typical $N_\ell$ at nucleon level | Unwrap depth | $n_{\text{strands}}$ used |
|---|---|---|---|
| Non-magic (e.g. $^6$Li) | $1$ | $0$ | $A$ (nucleon-words) |
| Single-magic (e.g. $^{14}$C) | $2$ | $1$ | $3A$ (quark-level) |
| Double-magic (e.g. $^4$He, $^{16}$O) | $3$ | $2$ | $3A$ + shell NF |

*Storage and Gröbner reduction scale with $n_{\text{strands}}^{\text{used}}$
rather than uniformly with $3A$.*
