The threading link picture makes a quantitative prediction —
with **no free parameters** — that can be compared to
experimental data.

**Derivation chain.**
Every quantity is determined by the Bring's surface geometry:

$$
  \chi(A) = -6
  \xrightarrow{\text{Bring's surface}}
  \mathcal{G}
  \xrightarrow{\text{knot spectrum}}
  q, \alpha, m_e/m_p
  \xrightarrow{\text{scale separation}}
  |q + q^{-1}|_{\mathrm{mol}}
  \xrightarrow{\Delta_{T(2,6)}(q)}
  \mathfrak{E}_{\mathrm{cross}}.
$$

1. The substrate parameter $q$ is fixed by $\chi(A) = -6$
   ([substrate parameter](#def:substrate-parameter)).

2. The nuclear crossing energy quantum $|q + q^{-1}|_{\mathrm{nuc}} \sim 8\mathrm{MeV}$ is determined by the Skein binding
   Lagrangian volume term.

3. $\alpha$ and $m_e/m_p$ are determined by the knot spectrum
   ([topological mass formula](#prop:topological-mass-formula)).

4. The molecular crossing energy quantum follows by scale
   separation: $|q + q^{-1}|_{\mathrm{mol}} = (\alpha^2 m_e / m_p) \cdot |q + q^{-1}|_{\mathrm{nuc}}$.

5. The Alexander polynomial $\Delta_{T(2,6)}(q) = q^2 + 1 + q^{-2}$
   is a topological invariant — it requires no input beyond $q$.

**The factor of $1/2$.**
The pairwise Hopf link picture
([earlier estimate](#rem:chain-ring-energy)) predicted
$\sim 400\text{--}800 \mathrm{kJ/mol}$ — a factor of 2
overshoot.  The threading link resolves this exactly:
$\Delta_{T(2,6)}(q) / 6 \approx 1/2$, halving the predicted
barrier.  This is not a correction or a fit — it is a
consequence of replacing $N$ separate Hopf links with the
single threading invariant $T(2,N)$.

**Predictions for other even-$N$ rings.**
The same framework, with no additional parameters, predicts
barriers for even-$N$ cyclic molecules (where $T(2,N)$ is a
2-component link and the Alexander formula
$\Delta_{T(2,2m)}(q) = (q^m - q^{-m})/(q - q^{-1})$ applies):

See [Table 3](#tbl:chain-ring-comparison-table3-data).

For odd $N$, the threading link $T(2,N)$ is a knot (1 component),
and the Alexander polynomial takes a different form — the
torus knot formula.  The barrier analysis for odd-$N$ rings
requires separate treatment.

The barrier increases with $N$ (more pairwise links to dissolve
and replace), but the threading efficiency ratio
$\Delta_{T(2,N)}(1) / N = 1/2$ is constant for all even $N$.
The prediction that larger rings have higher cyclisation barriers
is consistent with the experimental observation that macrocyclic
ring closure becomes progressively harder.

**Experimental data.**

See [Table 1](#tbl:chain-ring-comparison-table1-data).

**Comparison.**

See [Table 2](#tbl:chain-ring-comparison-table2-data).
