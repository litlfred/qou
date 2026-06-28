*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The Markov trace $\mathrm{tr}_M(T_w, q)$ has been written so far as a
function of $q \in \mathbb{C}$ with poles at the roots of unity, and
the residue spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) has been
treated as a Mittag-Leffler partial-fraction expansion in $\mathbb{C}$.
That picture is misleading: the primitive roots of unity are dense
in $S^1$, so $S^1$ is a **natural boundary** of $\mathrm{tr}_M$, not
an isolated singular set, and the Cauchy-kernel sum
$\sum_{n,j} r_n^{(j)}/(q - \zeta_n^{(j)})$ is not a complex-analytic
identity in any neighbourhood of $S^1$.

The correct algebraic home is the **Habiro ring** — the cyclotomic
completion of $\mathbb{Z}[q]$ — where convergence is $q$-adic and
values at every root of unity are well-defined, but no
$\mathbb{C}$-meromorphic structure is asserted on or across $S^1$.

**Proposition (Habiro completion of the mass trace).**
*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$, the
Markov trace of any closed braid lies in the Habiro ring*

$$
  \mathrm{tr}_M(T_w) \;\in\; \widehat{\mathbb{Z}[q]}
  \;:=\; \varprojlim_n \mathbb{Z}[q] / (q;q)_n.
$$

*See [Habiro ring](#def:habiro-ring) for the cyclotomic-completion
construction. The trace admits a unique cyclotomic expansion*

$$
  \mathrm{tr}_M(T_w, q)
  \;=\;
  \sum_{m \geq 0} a_m(T_w)\,(q; q)_m,
  \qquad
  (q; q)_m = \prod_{k=1}^{m}(1 - q^k),
  \quad
  a_m(T_w) \in \mathbb{Z}\bigl[q^{\pm 1}\bigr].
$$

*The expansion has the following properties:*

1. *(Roots of unity.) $\mathrm{tr}_M(T_w, q)$ has well-defined values
 at every root of unity $\zeta_n^{(j)}$, since $(q;q)_m$ vanishes
 at $\zeta_n^{(j)}$ for every $n \leq m$ and the partial sums are
 polynomials in $q$.*
2. *(Cyclotomic truncation.) Truncation at order $m$ exactly
 suppresses the contribution from every root of unity of order
 $\leq m$: the residual $\mathrm{tr}_M(T_w) - \sum_{k < m} a_k (q;q)_k$
 lies in the ideal $((q;q)_m) \subset \widehat{\mathbb{Z}[q]}$.*
3. *(Confinement-level support.) For an atomic closed braid the
 expansion terminates: $a_m = 0$ for $m > m_{\max}(T_w)$ with
 $m_{\max}$ controlled by the confinement level
 ([atomic Habiro expansion](#cor:habiro-expansion-atomic)).*

**Empirical regimes.**
*The qualitative regimes formerly described as "$\zeta_1$-dominant",
"resonant cancellation", and "resonant enhancement" reflect the
distribution of nonzero $a_m$ across cyclotomic orders. In Habiro
form they are stated as: a braid is regime-(1) if only
$a_0, a_1$ are nonzero; regime-(2) if signs alternate across $a_m$;
regime-(3) if signs reinforce. The Habiro expansion is the natural
target for the symbolic computation of these regimes (see
[atomic Habiro expansion](#cor:habiro-expansion-atomic)).*

**Tail control at the substrate value via the $q \leftrightarrow q^{-1}$
involution.**
*The QOU substrate value $q_0 \approx 1.110$ lies in the supercritical
regime $q > 1$, where the naive Pochhammer monotonicity*
$|(q;q)_{N+1}| \leq |(q;q)_N|$ *fails — each new factor $|1 - q^{N+1}|$
exceeds $1$ and $|(q;q)_N|$ in fact grows roughly like $q^{N(N+1)/2}$.
The Habiro completion is, however, symmetric under the involution
$q \leftrightarrow q^{-1}$ \cite{habiro2004}: the explicit identity*
$$
  (q^{-1}; q^{-1})_N \;=\; (-1)^N q^{-N(N+1)/2} (q; q)_N
$$
*shows that control of the cyclotomic tail at $q_0 > 1$ is supplied
by the monotone bound on the dual Pochhammer factor*
$|(q_0^{-1}; q_0^{-1})_N|$, *which lives in the range
$q_0^{-1} \in (0, 1)$ where the elementary monotone bound applies.
The Lean corollary `habiro_truncation_bound_supercrit` discharges
this bridge: at $q > 1$ the dual sequence
$|(q^{-1}; q^{-1})_N|$ is non-increasing in $N$.*
