### Significance — Bridge to analytic number theory

The graded-Mikusiński framework's depth-$n$ cyclotomic content
**IS** the Dirichlet $L$-value content at integer $n$, up to
$\mathbb{Q}(\zeta_K)$-linear combinations.  Three consequences follow:

1. **Classical L-value identities are theorems of our framework**:
   $\beta(3) = \pi^3/32$, $\beta(5) = 5\pi^5/1536$,
   etc., all follow from Theorem A as instances.
2. **Conversely**: any new theorem we prove about cyclotomic depth-$n$
   structure (e.g., Theorem D dimension) gives a corresponding
   statement about Dirichlet L-values.
3. **Beilinson's conjecture at $\mathbb{Q}(\zeta_K)$ depth $n$** is
   the Beilinson conjecture on $L$-values of Dirichlet characters —
   a classical open problem now reframed within this framework.

### Catalan's constant ($n = 2$ instance)

For $(n, K) = (2, 4)$ even case: Theorem A gives
$\mathrm{Re}\,\mathrm{Li}_2(i) = -\pi^2/48$ (Bernoulli $B_2(1/4) = -1/48$,
times $\pi^2 \cdot 2! / 2 = \pi^2$). And $\mathrm{Im}\,\mathrm{Li}_2(i) =
\mathrm{Cl}_2(\pi/2) = G$ — Catalan's constant.

$G$ is **not** Tate-rational (conjecturally transcendental); it's the
genuinely-new depth-2 generator over $\mathbb{Q}(i)$.  Matches Theorem G:
$(K - 1)/2 = (4 - 1)/2$ — but $K = 4$ is not prime; for prime $K = 3$:
dim 1 = $\mathrm{Cl}_2(2\pi/3)$ (Gieseking).

### Cross-references

- Theorem A: [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
- Theorem G: [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)
- Bloch–Suslin (depth-2 theorem):
  [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- K-theory $\leftrightarrow$ depth filtration: [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
