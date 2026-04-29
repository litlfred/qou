**Proof of [$\Phi_q$ categorical truncation depth](#prop:phi-q-categorical-truncation).**

*Step 1 (spectral-sequence reduction).* By
[GB spectral sequence collapse](#prop:spectral-sequence-collapse), for
$A = H_n(R, q)$ semisimple at generic $q$,

$$
  E_\infty^{p, *}
  \;=\;
  \begin{cases} Z(A) = \bigoplus_{\lambda \vdash n} R \cdot e_\lambda & p = 0, \\ 0 & p \geq 1. \end{cases}
$$

In particular, every Hochschild cocycle of degree $\geq 1$ is a
coboundary; the entire mass functional content is concentrated in
$E_\infty^{0, *} = Z(A)$.

*Step 2 (centre projection of the mass functional).* By
[categorical mass = Markov trace](#prop:categorical-mass-markov)
and [Plancherel-weighted centre projection](#prop:spectral-sequence-collapse),

$$
  \mathfrak{m}_{q,\mathcal{K}}(T_w)
  \;=\;
  \sum_{\lambda \vdash n}
    w_\lambda \cdot \frac{\chi_\lambda(\rho(\beta))}{\dim_q V_\lambda},
  \qquad
  w_\lambda \;=\; \frac{\dim_q^2 V_\lambda}{[n]_q!}.
$$

This sum is intrinsically finite (over partitions $\lambda \vdash n$)
and supported on $\mathrm{supp}(T_w) = \{\lambda : \chi_\lambda(\rho(\beta)) \neq 0\}$.

*Step 3 (curvature-rank stratification).* By
[curvature-rank stratification](#prop:curvature-rank-gb-stratification),
the centre $Z(A)$ admits a GB-depth filtration

$$
  Z(A) \;=\; \bigoplus_{k = 0}^{k_\star(T_w)} Z^{(k)}(A),
  \qquad
  Z^{(k)}(A) \;=\; \mathrm{span}\bigl\{e_\lambda : \mathrm{depth}_{\mathrm{GB}}(\lambda) = k\bigr\},
$$

with $k_\star(T_w) := \max_{\lambda \in \mathrm{supp}(T_w)} \mathrm{depth}_{\mathrm{GB}}(\lambda)$
finite by NF support finiteness. The mass decomposes as the
finite sum

$$
  \mathfrak{m}_{q,\mathcal{K}}(T_w)
  \;=\;
  \sum_{k = 0}^{k_\star(T_w)} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(T_w),
$$

where $\mathfrak{m}^{(k)}_{q,\mathcal{K}}$ is the depth-$k$ centre
projection
([unified mass formula](#prop:unified-curvature-rank-mass-formula)).

*Step 4 ($\Phi_q$-product representation).* By
[quantum dilogarithm = localized torsion volume](#cor:quantum-dilogarithm),
the analytic representation of the curvature-rank-$k$ stratum on the
$i$-th exceptional divisor is

$$
  \mathfrak{m}^{(k)}_{q,\mathcal{K}}\big|_{i\text{-th divisor}}
  \;=\;
  \bigl[\Phi_q^{[\leq k]}(z_i) - \Phi_q^{[\leq k-1]}(z_i)\bigr],
$$

where $\Phi_q^{[\leq k]}(z) = \prod_{j=1}^{k}(1 - q^{-j}z)^{-1}$ is
the depth-$k$ truncation. Telescoping the sum over $k = 0, \ldots, k_\star(T_w)$
gives

$$
  \sum_{k=0}^{k_\star(T_w)} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}\big|_i
  \;=\;
  \Phi_q^{[\leq k_\star(T_w)]}(z_i),
$$

so the brane-tower contribution from the $i$-th divisor is
$\Phi_q^{[\leq k_\star(T_w)]}(z_i)$, a **finite product** of
$k_\star(T_w)$ factors.

*Step 5 (truncation invariance for $k \geq k_\star$).* For any
$k \geq k_\star(T_w)$, the additional factors
$(1 - q^{-j}z)^{-1}$ for $j > k_\star(T_w)$ correspond by Step 4 to
strata $Z^{(j)}(A)$ with $j > k_\star(T_w)$, on which $T_w$ has zero
projection by definition of $k_\star$. Therefore

$$
  \Phi_q^{[\leq k]}(z_i) \cdot \mathrm{proj}_{\mathrm{supp}(T_w)}
  \;=\;
  \Phi_q^{[\leq k_\star(T_w)]}(z_i) \cdot \mathrm{proj}_{\mathrm{supp}(T_w)}
$$

inside $Z(A)$, where $\mathrm{proj}_{\mathrm{supp}(T_w)}$ projects onto
the NF-support stratum. Combined with Step 1's vanishing
$E_\infty^{\geq 1, *} = 0$, this gives the corollary: any
$k \geq k_\star(T_w)$ yields the same categorical brane-tower
contribution. $\square$

**Proof gaps (open).**
The proof above is complete *modulo* two structural inputs that
deserve their own verification:

1. **Step 4's identification**
   $\mathfrak{m}^{(k)}_{q,\mathcal{K}}\big|_i = \Phi_q^{[\leq k]}(z_i) - \Phi_q^{[\leq k-1]}(z_i)$
   is asserted via [cor:quantum-dilogarithm](#cor:quantum-dilogarithm)
   but the latter states the level-$k$ archimedean torsion volume **is**
   $\Phi_q(z_i)$ (analytic, infinite product), not the truncated
   product. Bridging "infinite analytic $\Phi_q$" with "finite
   curvature-rank-$k$ truncation" requires a refinement of
   [cor:quantum-dilogarithm](#cor:quantum-dilogarithm) at the level of
   the curvature-rank stratification — currently asserted, not
   derived. This is the essential **categorical-versus-analytic gap**
   of the brane tower.

2. **Step 5's truncation invariance** assumes that the analytic
   factors $(1 - q^{-j}z)^{-1}$ for $j > k_\star(T_w)$ act trivially
   on $\mathrm{proj}_{\mathrm{supp}(T_w)} Z(A)$. This is plausible
   (they involve higher-depth centre strata with zero $T_w$-projection),
   but requires a careful argument that the analytic product respects
   the depth grading — which is non-obvious because the analytic
   product mixes depths through the $z_i$-coordinate.

These gaps make the proposition a **conditional structural identity**
rather than a fully proven theorem. The structural content — that the
brane tower is centre-stratified and truncates at a finite depth
$k_\star(T_w)$ structurally determined by NF support — survives the
gaps. The open part is whether the analytic $\Phi_q$ product
faithfully represents this finite centre-stratified sum at $|\hat{V}|\approx 1$
or whether the analytic representation introduces spurious
$E_\infty^{\geq 1, *}$-content that the categorical truncation discards.

The empirical $k=2$ subtractive sweet spot
([brane-tower in $z$-Habiro §"Empirical observation"](#conj:brane-tower-z-habiro))
is consistent with $k_\star(T_w) \leq 2$ for D, T, ${}^3\mathrm{He}$
under this proposition, supporting the structural picture; the
${}^3\mathrm{He}$ residual overshoot is then attributable to multiplicity
in $\mathrm{supp}(T_w)$ rather than to a missing brane-tower
correction. The witness's anomalous $k_{\max} = 9$ for tritium remains
the most concrete falsifier — if it reflects a genuine $k_\star(T) = 9$
rather than a strand-padding artifact, the proposition fails.
