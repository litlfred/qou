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

The row values tabulated here are reproduced by
[the mass-table computation](https://github.com/litlfred/qou/blob/main/computations/wedderburn_mass_table_z1_20.py),
evaluating the
formula above at the proton-pin $q_{0}$ with zero fitted parameters: the
three coefficients are fixed by $m_{e}$, Catalan's constant and $q_{0}$
through the formula's own definitions.

These values supersede an earlier table computed with a third coefficient
of $0.0499$ in place of $h_{\mathrm{A}}^{2}$. That coefficient has no
derivation in the corpus, and it is inconsistent with the same table's
second coefficient: since
$[3]_{q} - 3 = q^{2} - 2 + q^{-2} = h_{\mathrm{A}}^{2}$, the two are locked
as $-2[3]_{q} = -6 - 2h_{\mathrm{A}}^{2}$, and the recorded
$-2[3]_{q} = -6.087415$ agrees with $h_{\mathrm{A}}^{2} = 0.0437$, not with
$0.0499$. Every row moved, by at most $1.206\;\mathrm{MeV}$; agreement with
AME2020 is materially unchanged (mean $0.075\%$, max $0.191\%$, against
$0.074\%$ and $0.192\%$), because $\Phi_{3}$ enters roughly fifty times more
weakly than $\Phi_{1}$. The correction is one of provenance, not of fit.

### Convention D, and what it costs

The table above is computed under the **canonical Markov convention**
$z = q^{3}/(q^{2}+1)$ (convention D). The values it supersedes were computed
under the excised convention C, $z = \sqrt{q}/(q+1)$.

**Agreement with AME2020 is worse under D, and materially so.** Mean
$\lvert\Delta\rvert/\mathfrak{m}$ rises from $0.0746\%$ to $0.1827\%$ and
the maximum from $0.1909\%$ to $0.3214\%$ — a factor of about $2.4$ on the
mean. This is reported as measured. It is not an improvement and is not
presented as one.

The two changes involved were separated rather than quoted together:

| change | mean $\lvert\Delta\rvert/\mathfrak{m}$ |
|:---|:---|
| published, convention C, recorded base masses | $0.0746\%$ |
| convention $C \to D$, base masses held fixed | $0.1787\%$ |
| base masses recorded $\to$ CODATA, convention held at D | $0.1827\%$ |

So the convention accounts for nearly all of the change and the base-mass
correction for very little. Note the direction of that last row: replacing
the recorded base masses with the *correct* CODATA values makes agreement
slightly **worse**, which is what one expects if the formula had been
absorbing part of the input error.

Convention D is fixed structurally by two-row Temperley–Lieb factorisation rather than by numerical fitting to composite masses; tables originally calibrated in the Convention-C frame therefore shift when evaluated at $z_D$.

### What is now derived, and what is not

$\Phi_{2}$ and $\Phi_{3}$ are no longer carried from the superseded
producer. Both are derived from the strand content and the per-crossing
values,

$$
  \Phi_{2} = Z N \ln\left(1 + h_{\mathrm{A}}^{2}/4\right),
  \qquad
  \Phi_{3} = -\left(2Z + N(N-1)\right)\ln q ,
$$

and both are **convention-independent** — neither involves the Markov
parameter $z$, so neither moved when $C \to D$. Both reproduce all nineteen
non-hydrogen values of the superseded table exactly. The per-crossing
determinants and ratios they rest on are proved.

$\Phi_{1}$ is the only invariant that uses $z$, and it is the only one the
convention change moves. It is recomputed here rather than carried.

**One limitation remains.** The ground-state ordering minimises $\Phi_{1}$
over arrangements, which is exponential in $A$; the search is exhaustive
where feasible (five atoms, where the minimum is global) and hill-climbing
beyond, validated against exhaustive search on every atom where exhaustive
search can be run. The witness records the regime per row. The base masses
are now CODATA, so the earlier $44$ and $36\;\mathrm{ppm}$ discrepancy is
closed.

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
