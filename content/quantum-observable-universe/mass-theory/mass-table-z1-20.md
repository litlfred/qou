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
[`wedderburn_mass_table_z1_20.py`](https://github.com/litlfred/qou/blob/main/computations/wedderburn_mass_table_z1_20.py)
from the committed witness `wedderburn-mass-table-z1-20`, evaluating the
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

Two limitations remain. The three invariants
$\Phi_{1}, \Phi_{2}, \Phi_{3}$ are carried from the superseded producer
rather than re-derived, so the transfer-matrix computation behind them is
not itself reproduced here. And the base masses used are
$44$ and $36\;\mathrm{ppm}$ below CODATA, which accounts for roughly
$1.5\;\mathrm{MeV}$ at $Z = 20$; correcting them is a separate change and
has not been made.

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
