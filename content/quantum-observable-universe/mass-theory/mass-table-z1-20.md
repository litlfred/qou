### Computation path (algebraic)

Each row is produced by purely algebraic steps, under the Kashaev
volume--density reading
([Kashaev volume--density](#rem:kashaev-volume-density)):

1. *Extract the braid $\beta_{Z, N}$* from the knot--particle dictionary
   (independent of $q$).
2. *Compute three Laurent polynomials*
   $\mathrm{Vol}_{q}^{(i)}(\beta_{Z, N}) \in \mathbb{Z}[q^{1/2},
   q^{-1/2}]$, $i = 1, 2, 3$, via the Markov trace product
   ([Markov trace product](#thm:markov-trace-product)) on the
   transfer-matrix chain at each Wedderburn branch
   ([algebraic quantum volume](#def:algebraic-quantum-volume)).
3. *Evaluate at* $q = q_{0}$ *and take* $\ln\lvert\cdot\rvert$.

The prediction column is the substitution of step 3 into the
three-invariant mass formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)).  No
continuous integration, no dilogarithm evaluation; the dependence on
$q_{0}$ is confined to step 3 alone.

See [Table](#tbl:mass-table-z1-20-table-data).

> **Status — unverified (2026-05-29).** The quoted row values are not
> currently reproducible from a committed witness: the cited
> `atom-mass-complete-wedderburn.witness.json` is absent from the
> repository. The live mass-prediction pipelines give substantially
> larger errors than the figures tabulated here — nucleons at $+2.89\%$
> (Family-A Geom_full); $\mathrm{D}/\mathrm{T}/{}^{3}\mathrm{He}$ at
> $\sim 1$–$3\%$ via census-assigned knots; and $A \geq 4$ via the
> $\alpha$-cluster rule at $+5$–$20\%$ (growing with $A$, e.g.
> ${}^{40}\mathrm{Ca}$ at $+19.5\%$). The earlier "zero fitted
> parameters" characterisation does not hold for the census /
> $\alpha$-cluster methods that are actually available; closing the
> $A \in \{5,6,7\}$ atom$\to$knot gap with a derived (SDP) rule is the
> prerequisite for a reproducible canonical table. See the
> [low-mass sweep audit](../../../docs/audits/2026-05-29-low-mass-sweep-full-audit.md).
