*Define the curvature-rank-$k$ residue functional using the Molien (fake-degree) weight*

$$
  w_\lambda(q) \;=\; \frac{f^\lambda \, q^{-\kappa_\lambda} \, \dim_q V_\lambda}{[n]_q!},
  \qquad
  \kappa_\lambda \;=\; \sum_{\square \in \lambda} c(\square)
  \;=\; n(\lambda') - n(\lambda),
$$

*where $f^\lambda$ is the number of standard Young tableaux (the classical Wedderburn block dimension), $c(\square) = j - i$ is the content of the box in row $i$, column $j$, and $\lambda'$ is the conjugate partition:*

$$
  \Phi_k(\mathcal{K}, \mathcal{T})
  \;:=\; \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
  w_\lambda(q) \cdot \log\Bigl|\!\int_{A_\lambda}\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|.
$$

*The universal residue extracts the high-tower contribution as:*

$$
  \mathfrak{m}^{\geq 4}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \alpha \cdot \!\!\sum_{k \geq 4}\!\Phi_k(\mathcal{K}, \mathcal{T}),
  \qquad \alpha \;=\; m_e \cdot 8G.
$$

At low strata ($k \leq 3$), the restricted Frobenius integral routes through distinct hyperbolic-knot ideals. At deep strata ($k \geq 4$), specific knot identities evaporate. The surviving residue isolates the universal Frobenius co-Casimir tail, dependent solely on the block weight topology.

**On the choice of weight family.** The functional was formerly defined against $\dim_q^2 V_\lambda/[n]_q!$. The replacement is not a change of normalisation: the two weights differ by up to a factor $1831$ per partition at $n = 9$, which is $A = 3$. Three properties distinguish the Molien weight.

**Three objects carry the name "Molien" in the corpus, and only the first two are used here.** (i) The *fake-degree identity* $\sum_\lambda f^\lambda q^{-\kappa_\lambda}\dim_q(\lambda) = [n]_q!$. (ii) The *Molien weight* $f^\lambda q^{-\kappa_\lambda}\dim_q(\lambda)/[n]_q!$, the measure that identity normalises. (iii) The two-variable *Molien series* $M_\nu(u,t)$ of `QOU.QBeta.MolienJonesMarkovN3` and `QOU.QBeta.MolienJonesMarkovN4`, a generating function and not a weight on partitions.

1. **It is the weight of the symmetrising trace.** Every Markov trace on $H_n(q)$ yields weights with $\sum_\lambda f^\lambda y_\lambda(z) = 1$ (at $n = 4$, `QOU.QBeta.MolienJonesMarkovN4.n4_markov_normalisation`), so being normalised does not single the Molien weight out. What does is that it is the weight of the $z = 0$ trace, the symmetrising trace $\tau(T_w) = \delta_{w,1}$: `QOU.SchurWeyl.ocneanuWeight_zero_eq_molienWeight` identifies the Ocneanu weight at $z = 0$ with the Molien weight, and `QOU.SchurWeyl.sum_dim_molienWeight_eq_one` is the normalisation $\tau(1) = 1$. Classically, $q^{-\kappa_\lambda}\dim_q(\lambda) = q^{-n(n-1)/2}R_\lambda(q^2)$ with $R_\lambda$ the fake degree, so the identity (i) is Steinberg's theorem on the graded coinvariant algebra of $S_n$ \cite{steinberg1964}. The alternative $\dim_q^2/D^2$ is normalised by dividing by $D^2 = \sum_\mu \dim_q^2$, i.e. by construction.
2. **The exponent $\kappa_\lambda$ is forced, not chosen.** In the family $f^\lambda q^{c\kappa_\lambda}\dim_q/[n]_q!$ with $c$ real, normalisation already at $n = 2$ reads $(q^c + q^{-c})/(q + q^{-1}) = 1$, which for $q > 1$ forces $c = \pm 1$. The two signs are one measure read on transposed diagrams: conjugation fixes $f^\lambda$ and the hook multiset and negates $\kappa$.
3. **It is the literature's $q$-Plancherel measure.** $f^\lambda q^{-\kappa_\lambda}\dim_q(\lambda)/[n]_q! = \mathbb{M}_{n,q^2}(\lambda)$ for every $n$, every partition and every $q$: substituting $Q = q^2$ into $\mathbb{M}_{n,Q}(\lambda) = Q^{n(\lambda)}f^\lambda/\prod_x\{h(x)\}_Q$ and using $\sum_x h(x) = n(\lambda) + n(\lambda') + n$ gives the left side exactly. So the Féray–Méliot asymptotics apply to this weight and to nothing else in the corpus. See [Asymptotic skeleton of the q-Plancherel measure $\mathbb{M}_{n,q}$](../observations/q-plancherel-asymptotic-skeleton.md).

**Molien within the Wenzl family.** Convention D and the colour trace are the Wenzl levels $r = 2$ and $r = 3$; the Molien weight is the $z = 0$ member of the same Ocneanu family, its $r \to \infty$ end. A finite level carries a row cap, and $\Phi_k$ for $k \geq 3$ is non-zero only at the Molien end. The choice of Molien therefore rests on its being the uncapped member of the family, not on the $+21.4\%$ gain reported below.

**The former weight is $n$-dependent, and $n = 3A$.** $c_n = \sum_\lambda \dim_q^2/[n]_q!$ is $0.9874 / 0.9911 / 1.1109 / 1.5171$ at $n = 3/6/9/12$ at the substrate $q_0$, and the defect is structural rather than a $q$-integer-convention artifact — the $q$-deformation breaks Burnside's $\sum_\lambda (f^\lambda)^2 = n!$, and no convention restores it. Because $\Phi_k$ is *linear* in $w_\lambda$, a $\lambda$-independent rescaling cancels from a ratio of two $w$-weighted sums **at the same $n$** and from nothing else. Two ways that fails, both of which occurred in production:

1. **Across $n$.** Any quantity comparing different $n$ — equivalently different mass number $A$ — is distorted by the spread of $c_n$.
2. **At fixed $n$, against a non-$w$-weighted quantity.** A $w$-weighted number compared to an experimental magnitude, a closed-form scalar, or a $y_\lambda$-weighted object does not cancel, because only one side carries $c_n$. Measured instances: [`probes/deuteron_fpn_wlambda_wiring.py`](../../../computations/probes/deuteron_fpn_wlambda_wiring.py) and [`yekutieli_volume_join.py`](../../../computations/yekutieli_volume_join.py).

**A same-$n$ ratio is necessary for cancellation but not sufficient — the numerators must match too.** This is the trap in the present migration and it is easy to get backwards. All six candidates in [`beta_ew_delta_I_321_and_wedderburn.py`](../../../computations/beta_ew_delta_I_321_and_wedderburn.py) are ratios of $w$-weighted sums at fixed $n = 6$, so they are exactly invariant under $\dim_q^2/[n]_q! \to \dim_q^2/D^2$ — same numerator, $\lambda$-independent constant. They are **not** invariant under the move to Molien, whose numerator is $\lambda$-dependent relative to $\dim_q^2$.

**The second arm is retained and labelled.** The requirement set does not separate Molien from $\dim_q^2/D^2$ — it asks only that the normaliser be $n$-independent, and both satisfy that; both are legitimate probability measures. So [`fr_pullback_k3_test.py`](../../../computations/fr_pullback_k3_test.py) computes and reports **both arms**, Molien primary. They disagree: Molien ranks $5_2$ best ($+21.4\%$ against its own baseline, with $6_1$ *worse* than baseline), while $\dim_q^2/D^2$ ranks $6_1$ best ($+1.7\%$). Quoting one number would conceal that. Note the corpus's structural $6_1$ naming comes from the GB-filtration route, which carries no weight family at all and is untouched by either arm.

**Two further measures exist and are not arms here.** The $V^{\otimes n}$ Schur–Weyl share $f^\lambda \prod[N+c]_q/[h]_q$ lives on partitions with at most $N$ rows and is normalised by $[N]_q^n$ — a different index set *and* normaliser, so not a rescaling of anything above; at $N = 2$ the $\mathrm{SU}(N)$ row cap zeroes it on every partition with more than two rows, exactly as it zeroes $y_\lambda$. The classical $(f^\lambda)^2/n!$ reached via $\mathrm{End}(V^{\otimes n})$ is Burnside-normalised at every $n$ but is **$q$-independent**, so it could carry no substrate dependence into $\Phi_k$ at all.

Measurements: [`2026-09-04-plancherel-convention-gap.md`](../../../docs/audits/2026-09-04-plancherel-convention-gap.md); producers [`probes/molien_feray_meliot_bridge_probe.py`](../../../computations/probes/molien_feray_meliot_bridge_probe.py), [`probes/plancherel_deformation_uniqueness_probe.py`](../../../computations/probes/plancherel_deformation_uniqueness_probe.py), [`audits/w_lambda_family_consumer_audit.py`](../../../computations/audits/w_lambda_family_consumer_audit.py); registry [§B-norm](../../../docs/coordination/trace-convention-registry.md).

**Two candidates are excluded outright**, independently of the choice between the two that remain. The Markov weights $y_\lambda$ of the canonical Frobenius pairing are scope-(b) excluded: the $\mathrm{SU}(N)$ row cap sets $y_\lambda = 0$ on every stratum of depth $\geq N$, so $\Phi_3$ vanishes identically and all three candidate knots reproduce the no-FR baseline to the last digit. The historical $\dim_q^2/[n]_q!$ is scope-(b) excluded *for cross-nucleus use* by the $n$-dependence above; it remains valid within a single $n$, by `QOU.BraidKnot.WLambdaNormalizationInvariance.ratio_invariant`.

**One caution on citing the identity.** `molienSum_eq_qFactorial` is $\sum_\lambda f^\lambda q^{-\kappa_\lambda} \dim_q(\lambda) = [n]_q!$ — the $q^{-\kappa_\lambda}$ is part of it. A "Molien weight" written as $f^\lambda\dim_q(\lambda)$ without that factor is a different object and is **not** normalised: with $\dim_q$ in the balanced convention it sums to $\approx 0.922$ at $n = 6$ at $q_0$, and $\approx 0.061$ at $q = 2$, rather than $1$. (In the fake-degree convention the power of $q$ already sits inside $\dim_q$, and the plain sum is exactly $1$: it is the same identity.)
