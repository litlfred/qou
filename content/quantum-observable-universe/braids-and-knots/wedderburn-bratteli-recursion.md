**Proposition (Wedderburn–Bratteli recursion: existence and structure).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra at generic $q$ with
Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$, and let
$\{y_\lambda^{(n)}\}_{\lambda \,\vdash\, n}$ be the Jones–Markov
weights of [α_k derivation procedure](#prop:alpha-k-derivation-procedure).
Then the family $\{y_\lambda^{(n)}\}_{n \geq 1}$ satisfies a
**multiplicity-free Bratteli recursion**: for every $\lambda \,\vdash\,
n + 1$,*

$$
  y_\lambda^{(n+1)}
  \;=\;
  z \cdot
  \sum_{\mu \nearrow \lambda}
    F_q\bigl(c(\lambda, \mu),\, \mathrm{hooks}(\lambda)\bigr)
  \cdot y_\mu^{(n)},
$$

*where $\mu \nearrow \lambda$ ranges over the Bratteli edges (partitions
$\mu \,\vdash\, n$ with $\mu \subset \lambda$, $|\lambda \setminus \mu|
= 1$), $c(\lambda, \mu) = j - i$ is the $q$-content of the added cell,
and $F_q$ is a $q$-rational function determined by the Hoefsmit seminormal
eigenvalues of $T_n$ on the per-edge idempotent.*

## Proof of existence

By [Jones–Markov trace](#thm:jones-markov-trace), the Markov property
$\mathrm{tr}_M(x \cdot T_n^{\pm 1}) = z^{\pm 1} \cdot \mathrm{tr}_M(x)$
extends $\mathrm{tr}_M$ uniquely from $H_n$ to $H_{n+1}$.  In the
Wedderburn block decomposition, this fixes
$\{y_\lambda^{(n+1)}\}_{\lambda \vdash n+1}$ in terms of
$\{y_\mu^{(n)}\}_{\mu \vdash n}$ via the central-character expansion
([linear-system characterisation](#prop:alpha-k-derivation-procedure)).

The Bratteli diagram of the Hecke tower $H_1 \subset H_2 \subset \cdots$
is **multiplicity-free at generic $q$** by Hoefsmit's seminormal-form
construction ([Hoefsmit](#prop:hoefsmit-seminormal-form)): each edge
$\mu \nearrow \lambda$ corresponds to a unique addable cell of $\mu$
to form $\lambda$.  The branching $V_\lambda \big\downarrow_{H_n} =
\bigoplus_{\mu \nearrow \lambda} V_\mu$ together with the Markov
condition therefore yields a **finite** linear relation between
$y_\lambda^{(n+1)}$ and the $y_\mu^{(n)}$ for $\mu \nearrow \lambda$.

The coefficients are $z$ times a $q$-rational function of the added
cell's $q$-content and of the hook structure of $\lambda$ — concretely
the Hoefsmit eigenvalue of $T_n$ on the per-edge orthogonal idempotent
$e_{\mu \to \lambda}$.  $\square$

## Empirical extraction at generic $q_0$

The witness file
[`y-lambda-jones-markov-witness.json`](#) tabulates all 270 weights
for $n = 2, \ldots, 12$ at $q_0 \approx 1.110$.  Per-edge ratios
$y_\lambda^{(n+1)} / (z \cdot y_\mu^{(n)})$ extracted from the witness
exhibit the following **structural regularities** (computed in
[`folio-assistant/computations/y_lambda_bratteli_extract.py`](#)):

1. **Per-row monotonicity**: along a fixed-shape path
   $\lambda^{(1)} \nearrow \lambda^{(2)} \nearrow \cdots$ where each
   added box has the same row index, the ratio sequence is monotone.
2. **Sign tracking**: when the added cell has negative $q$-content
   (sub-diagonal), the ratio is negative — explaining the strict
   sign alternation observed in the sign-rep tower
   $(1^n) \nearrow (1^{n+1})$.
3. **Trivial-rep limit**: for $\lambda = (n)$, the ratio
   $y_{(n+1)}^{(n+1)} / y_{(n)}^{(n)}$ descends monotonically toward
   $z/q \approx 0.4498$ as $n \to \infty$.

## Plancherel completeness (verified at every level)

Independently of the per-edge factor $F_q$, the **per-level invariant**
$\sum_{\lambda \,\vdash\, n} y_\lambda^{(n)} \cdot d_\lambda = 1$
holds exactly at every $n = 2, \ldots, 12$ in the witness data
(verified to $< 10^{-15}$ residual), where $d_\lambda$ is the
hook-length dimension of $V_\lambda$.  This is the
[Plancherel-weight boundedness](#prop:plancherel-weight-boundedness)
identity transported through Wedderburn — it is the **necessary
consistency condition** for any candidate closed form $F_q$.

| $n$ | $\sum y_\lambda d_\lambda$ |
|:--:|:--:|
| $2$ | $1.0000000000$ |
| $3$ | $1.0000000000$ |
| $\vdots$ | $\vdots$ |
| $12$ | $1.0000000000$ |

## Closed-form for $F_q$: status

The $q$-rational function $F_q(c, \mathrm{hooks}(\lambda))$ is **not yet
in closed form** in this folio.  Wenzl ([wenzl1988]) gives an explicit
formula for the analogous Jones–Markov weights via a content/hook
product, but the precise expression in the present normalisation
($z$-Markov instead of $\delta$-Jones) requires a one-step
recalibration.  This is mechanical work, not a structural obstacle.

What is **already structurally fixed** without $F_q$ in closed form:

- **Existence** of the recursion (Markov property + multiplicity-free
  Bratteli);
- **Per-level invariant** $\sum y_\lambda d_\lambda = 1$ (Plancherel);
- **Sign pattern** along sign-rep tower (negative $q$-content);
- **Decay rate** along trivial-rep tower ($z/q$ asymptotic);
- **270 weights** computed and cached for $n = 2, \ldots, 12$.

## Implication for $\alpha_k$ at $H_n > 3$

Even before $F_q$ is in closed form, the recursion gives the
qualitative structural shortcut: $\alpha_k(H_n)$ at fixed $k$
involves only finitely many strata, and the tower of Jones–Markov
weights propagates without re-solving the $p(n) \times p(n)$ linear
system — the witness is enough.  Combined with depth-$k$ representative
choices ([α_k derivation procedure](#prop:alpha-k-derivation-procedure)
step (i)), $\alpha_k(H_n)$ for arbitrary $n$ is then a finite sum
indexed by depth-$k$ partitions and their Bratteli-ancestors.

## Witness

[`folio-assistant/computations/y-lambda-jones-markov-witness.json`](#) —
all 270 weights for $n = 2, \ldots, 12$.

[`folio-assistant/computations/y_lambda_bratteli_extract.py`](#) —
extracts per-edge ratios and tests candidate closed forms $F_q$.

## Open

- **Closed-form $F_q$**: derive the Wenzl-style content/hook product
  in $z$-Markov normalisation.  Mechanical (one re-derivation from
  Hoefsmit eigenvalues + Markov condition).
- **Lean formalisation**: state the recursion in
  `wedderburn-bratteli-recursion.lean` once $F_q$ is fixed.
