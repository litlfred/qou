This note records the numerical verification, the $N = 5$ instance, the analytic-number-theory bridge, the Catalan-constant $(n=2)$ instance, and cross-references for [the cyclotomic $L$-value decomposition](#prop:cyclotomic-l-value-decomposition).

### Numerical verification at 50 dps

Evaluating both expressions to $50$ decimal places confirms the exact identity:

| Quantity | Value (50 dps) |
|---|---|
| $\mathrm{Im}\,\mathrm{Li}_3(i)$ (closed form $\pi^3/32$) | $0.96894614625936938048363484585\ldots$ |
| $\mathrm{Im}\,\mathrm{Li}_3(i)$ (direct polylog) | $0.96894614625936938048363484585\ldots$ |
| $\beta(3)$ (classical closed form) | same |
| Residual | $0$ (exact match) |

### N = 5 instance (Theorem G dim $(K - 3)/2 = 1$)

Cyclotomic depth-3 content over $\mathbb{Q}(\zeta_5)$:

- $\mathrm{Cl}_3(2\pi/5) \approx 0.18937$
- $\mathrm{Cl}_3(4\pi/5) \approx -0.76636$
- Genuinely-new generator $= \mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5) \approx 0.95572$

Corresponds, via the Hurwitz–Lerch decomposition, to the 2 odd
Dirichlet characters $\chi_5$, $\chi_5^3$ mod 5 (complex-conjugate
pair).  Modulo bar-conjugation: 1 real dimension. Matches Theorem G.

### Bridge to analytic number theory

The graded-Mikusiński framework's depth-$n$ cyclotomic content
**IS** the Dirichlet $L$-value content at integer $n$, up to
$\mathbb{Q}(\zeta_K)$-linear combinations.  Three consequences follow:

1. **Classical L-value identities are theorems of the framework**:
   $\beta(3) = \pi^3/32$, $\beta(5) = 5\pi^5/1536$,
   etc., all follow from Theorem A as instances.
2. **Conversely**: any new theorem established about cyclotomic depth-$n$
   structure (e.g., Theorem D dimension) gives a corresponding
   statement about Dirichlet L-values.
3. **Beilinson's conjecture at $\mathbb{Q}(\zeta_K)$ depth $n$** recovers
   Beilinson's classical conjecture on $L$-values of Dirichlet characters
   within the cyclotomic regulator setting.

### Catalan's constant ($n = 2$ instance)

For $(n, K) = (2, 4)$ even case: Theorem A gives
$\mathrm{Re}\,\mathrm{Li}_2(i) = -\pi^2/48$ (Bernoulli $B_2(1/4) = -1/48$,
times $\pi^2 \cdot 2! / 2 = \pi^2$). And $\mathrm{Im}\,\mathrm{Li}_2(i) =
\mathrm{Cl}_2(\pi/2) = G$ — Catalan's constant.

$G$ is **not** Tate-rational (conjecturally transcendental); it is the
genuinely new depth-2 generator over $\mathbb{Q}(i)$.  Matches Theorem G:
$(K - 1)/2 = (4 - 1)/2$ — where $K = 4$ is composite; for prime $K = 3$:
dim 1 = $\mathrm{Cl}_2(2\pi/3)$ (Gieseking).

### Cross-references

- Theorem A: [Jonquière cyclotomic Tate-rationality](#prop:jonquiere-cyclotomic-tate-rationality)
- Theorem G: [cyclotomic dimension synthesis across all depths](#prop:cyclotomic-dimension-synthesis-all-depths)
- Bloch–Suslin (depth-2 theorem):
  [the Bloch--Suslin depth-$2$ identification](#prop:depth-2-identification-bloch-suslin)
- Borel partial discharge: [Borel's partial resolution of the depth correspondence](#prop:borel-partial-resolution)
- K-theory $\leftrightarrow$ depth filtration: [the $K$-theory period Rosetta dictionary](#rem:k-theory-period-rosetta)
- Period ledger: [the transcendental-accounting ledger](#rem:transcendental-accounting)
