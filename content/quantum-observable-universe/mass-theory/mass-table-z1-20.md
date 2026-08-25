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

The row values tabulated here are reproducible, but **not from the
formula above**. The referenced `atom-mass-complete-wedderburn` witness
is absent from the working tree yet recoverable from history (added
2026-04-10 in `1359fe23ac` under `folio-assistant/computations/`, left
the tree with the platform code in the miga split); evaluating the
formula on its recorded invariants returns every row to within
$0.0005\;\mathrm{MeV}$. It does so only with the producer's third
coefficient $0.0499$, which has no derivation in this corpus and is
neither $h_{\mathrm{A}}^{2}$ at any documented anchor nor a power of
$q_{0}$ times it. Under the published $h_{\mathrm{A}}^{2}
= 0.0437073$ the same invariants reproduce **none** of the twenty
quoted values, while agreeing with AME2020 equally well (mean
$0.075\%$, max $0.191\%$, against $0.074\%$ and $0.192\%$). So the
table does not discriminate between the two coefficients on accuracy, and
the computation that produced these rows is not the one stated above.
Which coefficient is *correct* is settled separately and does not rest on
the table: $h_{\mathrm{A}}^{2} = q^{2} + q^{-2} - 2 = [3]_{q} - 3$ is an
exact construction, while $0.0499$ has none.

The live mass-prediction
pipelines give substantially larger errors than these figures: nucleons
at $+2.89\%$ (Family-A VolDensity); $\mathrm{D}/\mathrm{T}/{}^{3}\mathrm{He}$
at $\sim 1$–$3\%$ via census-assigned knots; and $A \geq 4$ via the
$\alpha$-cluster rule at $+5$–$20\%$, growing with $A$ (e.g.
${}^{40}\mathrm{Ca}$ at $+19.5\%$). The "zero fitted parameters"
characterisation does not hold for the census / $\alpha$-cluster methods
actually available; a reproducible canonical table requires first
closing the $A \in \{5,6,7\}$ atom$\to$knot assignment with a derived
(SDP) rule rather than a hyperbolic-census search.
