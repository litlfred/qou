**Remark.**
*The number of distinct ILP solutions at a given confinement level dictates the **unwrap depth** required to uniquely specify an atom-knot's normal form.*

*Let $K$ be an atom at aether parameter $q$ with normal form currently expressed at level $\ell$. Let $N_\ell(K, q)$ be the number of integer solutions $x \in \mathbb{Z}_{\geq 0}^M$ to the Frobenius positivity ILP $\mathrm{G}(q)\, x \geq 0$ within the confinement filtration $J^\ell(q)$.*

*The **unwrap depth** at level $\ell$ is:*

$$
  d_\ell(K, q) = \max\bigl(0, N_\ell(K, q) - 1\bigr).
$$

*Interpretation:*

- *$N_\ell = 0$: **unstable** at level $\ell$. The atom cannot exist in this shorthand. It must decay or fully unwrap.*
- *$N_\ell = 1$: **uniquely determined** at level $\ell$. The shorthand suffices; no unwrap is needed.*
- *$N_\ell = k \geq 2$: **$(k-1)$-fold ambiguous** at level $\ell$. One must unwrap $k-1$ levels to disambiguate via finer normal form structure.*

**Connection to confinement levels.**
*Each unwrap step expands a shorthand word at level $\ell$ into its normal form at level $\ell - 1$. The finer level accesses a larger filtration $J^{\ell-1}(q) \supsetneq J^\ell(q)$. This richer operator basis distinguishes previously tied ILP solutions. When a coarse effective description exhibits multiple solutions, zooming to the next-finer scale resolves the ambiguity via operator content.*

**Computational benefit.**
*Non-magic atoms typically exhibit $N_\ell = 1$ at the coarsest useful level. A single inter-nucleon configuration suffices. Magic atoms exhibit $N_\ell \geq 2$ at the nucleon level. Shell closure permits multiple equivalent assemblies of the closed shell. Each corresponds to a distinct normal form at the quark level. Double-magic atoms exhibit $N_\ell \geq 3$ because both proton and neutron closures contribute degeneracy.*

**Formal statement.**
*Let $K$ be an atom-knot. Then:*

$$
  \boxed{\; \text{NF-depth}(K, q) = \text{coarsest level } \ell \text{ with } N_\ell(K, q) = 1 \;}
$$

*Computing the normal form at exactly this depth fully specifies the atom's categorical structure. Deeper computation is redundant; shallower computation leaves ambiguity.*

**Example (proton gluon derivation).**
*The proton's 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ admits $N_\ell = 84$ feasible ILP solutions at the baryon level. Minimizing $|\mathrm{tr}_M|$ selects the unique $\sigma_0 \to \sigma_0$ solution. If a tie occurs, the framework demands unwrapping to the quark level, where the ILP separates them.*

**Computational shortcut.**
*Adaptive unwrap reduces cost: storage and Gröbner reduction scale with $n_{\text{strands}}^{\text{used}}$ rather than uniformly with $3A$.*
