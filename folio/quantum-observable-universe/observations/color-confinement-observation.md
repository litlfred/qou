Feynman noted \cite{feynman1963} that three color primaries cannot reproduce all visible spectral colors using strictly positive coefficients. The CIE chromaticity diagram makes this precise. The spectral locus is a curve that no inscribed triangle contains. Certain spectral colors require negative coefficients for at least one primary.

In the Descartes universe, this geometric constraint transplants to the Skein algebra. It provides a mechanism for color confinement.

**Analogy.**
See [Table](#tbl:color-confinement-observation-table-data).

**Three-color canonicity.**
The automorphism group $S_5$ of Bring's surface contains exactly three conjugate $S_3$ subgroups. Each subgroup is the quotient of the trefoil knot group restricted to one color fiber. The number three arises from geometric structure:
1. The degree of the Bring curve is $5$ (quintic in $\mathbb{P}^4$).
2. The resolvent structure factors as $5 = 1 + 1 + 3$ (one spacetime base, one longitudinal backbone, three chiral fibers).
3. The $S_5$ subgroup structure contains three $S_3$ subgroups permuted by the remaining generators.

In the CIE diagram, three primaries model human color vision. In this paper, the algebraic geometry of Bring's surface forces three color tubes.

**Confinement strength.**
The Skein asymmetry $q - q^{-1}$ controls the necessity of negative coefficients:
- At $q = 1$ (classical limit): the Skein relation simplifies to $[L_+] = [L_-]$. All coefficients can be made positive. Confinement vanishes. Individual colors are separately observable.
- At $q = q_0$ (Descartes value): $q - q^{-1} = 0.209$. This produces roughly $20\%$ negativity in Skein coefficients. Individual quarks have negative $\tau$-evaluations and remain confined.
- At $q \to \infty$: negativity saturates and confinement becomes absolute.

Confinement strength is finite and depends on $q$. This provides a geometric basis for asymptotic freedom. At short distances (high energies), the effective $q$ flows toward $1$ under Reeb dynamics. This reduces the Skein asymmetry. At the QCD scale, the running $q$ requires more energy for color extraction than pair creation. This reproduces the standard confinement mechanism via the $q$-chromaticity constraint.

**Quantitative prediction.**
The Skein negativity at a single crossing is $q^{-1} = 0.901$ (the antisymmetric $R$-matrix eigenvalue). For a baryon with $n$ internal crossings, the probability of isolating a single quark scales as

$$
  P_{\mathrm{isolation}} \sim (-q^{-1})^n \to 0
$$

This decays exponentially in the number of crossings. The proton consists of three trefoils linked by $T_{2,9}$, forming a Borromean structure. It requires $9$ binding crossings from the force carrier and $9$ matter crossings from the three trefoils, giving

$$
  P_{\mathrm{isolation}} \sim q^{-18} \approx 0.153
$$

at the bare level. Confinement is probabilistically suppressed rather than topologically absolute, as the knots embed freely. The fibre functor assigns exponentially small weight to single-color states.

A complete proof of confinement requires demonstrating that $\tau(\psi_{\mathrm{color}}) < 0$ for all single-color states $\psi_{\mathrm{color}}$ at $q = q_0$. This reduces to a positivity theorem for the $S_5$-invariant Skein submodule.
