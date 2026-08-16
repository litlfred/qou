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

*Step 3 (curvature-rank stratification).*
[Curvature-rank stratification](#prop:curvature-rank-gb-stratification)
supplies the filtration of $H_n(R, q)$ by the curvature rank $r(T_w)$ of
**words**. The grading of the centre by *partition* depth used below is a
further step, not stated there and assumed here; see
`docs/audits/2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md`.
Granting it, the centre $Z(A)$ admits a GB-depth filtration

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
the transient trace contribution at $p_i$ evaluates to $\Phi_q(z_i)$.
That identity is **unstratified** — it equates the whole transient
trace with the whole dilogarithm and says nothing about levels. The
level-by-level refinement this step needs is
[partition-depth stratification of $\Phi_q$](#prop:quantum-dilogarithm-stratified),
and with it the analytic representation of the curvature-rank-$k$
stratum on the $i$-th exceptional divisor is

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

The brane-tower contribution from the $i$-th divisor is
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

**Proof gap closure (partial).**
The structural bridge for Step 4 — identifying the level-$k$ factor of
$\Phi_q$ with the depth-$k$ centre stratum — is now provided by
[partition-depth stratification of $\Phi_q$](#prop:quantum-dilogarithm-stratified).
That proposition gives the depth-$k$ Frobenius-dual coefficients
$\phi_q^{(k)}(z_i) \in Z^{(k)}(A)$ such that the partial product
$\Phi_q^{[\leq k]}(z_i) = \sum_{j \leq k} \phi_q^{(j)}(z_i)$ on the
nose, and the truncation identity

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\Phi_q^{[\leq k_\star(T_w)]}(z_i) \cdot T_w\bigr)
$$

holds as a Frobenius-paired equality, derived from depth-orthogonality
under the Frobenius pairing on $Z(A)$.

**Remaining gap (canonical, not structural).**
The Frobenius-paired identity above is a **categorical equality**: the
sums $\sum_k \langle \phi_q^{(k)}(z_i), T_w \rangle$ and the analytic
$\mathrm{tr}_M(\Phi_q(z_i) \cdot T_w)$ agree as elements of $R$. To
conclude that the *canonical* mass formula at $q = q_0$ with $\Phi_q$
replaced by $\Phi_q^{[\leq k_\star(T_w)]}$ gives the same real-valued
answer, one needs the depth-$k$ projections
$\mathrm{proj}_{Z^{(k)}}(\Phi_q(z_i))$ to be uniformly bounded as
$|z_i| \to q$. The analytic infinite product diverges in this limit;
the Frobenius-paired identity says that whatever divergent content
$\Phi_q(z_i)$ accumulates above depth $k_\star(T_w)$ pairs to zero
with $T_w$, but the **uniform canonical bound** on the truncated
remainder is the open part — the conjectural target of
[$z$-Habiro completion](#conj:brane-tower-z-habiro).

The structural content of the proposition — that the brane tower is
centre-stratified, truncates categorically at a finite depth
$k_\star(T_w)$ structurally determined by NF support, and the analytic
$\Phi_q$ infinite product is a faithful Frobenius-pairing
representation up to the depth-$k_\star$ truncation — is closed
modulo the depth-stratified version of $\Phi_q$
([prop:quantum-dilogarithm-stratified](#prop:quantum-dilogarithm-stratified)).
The remaining gap is between the categorical equality and its
real-valued canonical evaluation at $|\hat{V}|\approx 1$.

The empirical $k=2$ subtractive sweet spot
([brane-tower in $z$-Habiro §"Empirical observation"](#conj:brane-tower-z-habiro))
is consistent with $k_\star(T_w) \leq 2$ for D, T, ${}^3\mathrm{He}$
under this proposition, supporting the structural picture; the
${}^3\mathrm{He}$ residual overshoot is then attributable to multiplicity
in $\mathrm{supp}(T_w)$ rather than to a missing brane-tower
correction. The witness's anomalous $k_{\max} = 9$ for tritium remains
the most concrete falsifier — if it reflects a genuine $k_\star(T) = 9$
rather than a strand-padding artifact, the proposition fails.
