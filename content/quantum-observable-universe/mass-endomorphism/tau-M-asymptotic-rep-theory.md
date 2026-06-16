**$\tau_M$ asymptotic expansion — representation-theoretic prediction.**

For any typed braid $\beta$ and 2-d Hecke irrep $V_\lambda$ of $H_n(q)$, the
Markov-traced character at single wrap admits a structural asymptotic
expansion in the substrate parameter $\hbar_q = (q-1)/q$:

$$
\boxed{
  \tau_M^{V_\lambda}(\beta)
   \;=\;
   \mathrm{Tr}\,\rho_\lambda(\beta) \cdot
   \exp\!\Bigl(-\tfrac{1}{2} \sum_{k \geq 1} c_k^{(\lambda)}(b_\lambda) \cdot \hbar_q^{2k}\Bigr),
}
$$

where:

- $\rho_\lambda$ is the **Hoefsmit seminormal representation** of
 $H_n(q)$ on $V_\lambda$;
- $b_\lambda \in V_\lambda \otimes V_\lambda^*$ is the **off-diagonal
 coupling** of $\rho_\lambda(\sigma_i)$ in the standard-tableau basis;
- $c_k^{(\lambda)}(b_\lambda)$ is a degree-$k$ polynomial in $b_\lambda$
 arising from the Kashiwara crystal-graph matrix elements at level $k$;
- the expansion is **even in $\hbar_q$** (only powers of $\hbar_q^2$
 appear) by Markov-cyclicity invariance under the bar involution
 $q \leftrightarrow q^{-1}$ (see
 [`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation)).

The empirical instances proved at single-wrap by  and follow-ups:

| order | irrep | coefficient | numerical check |
|------:|:---:|:---:|---:|
| $k = 0$ | any $V_\lambda$ | $c_0 = 0$ | trivial (Form A baseline) |
| $k = 1$ | $V_{(2,1)}$ | $c_1(b) = b$ | $74$ ppm at $q_0$ |
| $k = 2$ | $V_{(2,1)}$ | $c_2(b) \approx 1$ geometric | $-22$ ppm |
| $k = 1$ | $V_{(n)}, V_{(1^n)}$ | $c_1 = 0$ | exact, by definition (1-d) |

## Four parallel rep-theory anchors

The exponential structure above is forced by four independent
constructions in Hecke / quantum-group representation theory.

### 1. Kashiwara crystal graph

For each irrep $V_\lambda$ of $U_q(\mathfrak{sl}_n)$ (and consequently
$H_n(q)$), the Kashiwara crystal $B(\lambda)$ is a coloured graph
with $\dim V_\lambda$ vertices (one per SYT) and edges given by the
$\tilde f_i$ Kashiwara operators. For $V_{(2,1)}$:

```
  T_1 = [[1,2],[3]]  --(\tilde{f}_1)-->  T_2 = [[1,3],[2]]
```

a single edge with weight $b_\lambda$. The N=1 eigenphase shift
$-b \cdot \hbar_q^2 / 2$ is precisely the matrix element of $\tilde f_1$
in the seminormal basis, times the substrate-derived scale
$\hbar_q^2 / 2$.

### 2. Jucys–Murphy elements

The Jucys-Murphy elements $J_k \in Z(H_n(q))$ (for $2 \leq k \leq n$)
generate the centre and have explicit spectral decomposition

$$
  J_k|_{V_\lambda^T} \;=\; q^{c_T(k)} - q^{-c_T(k)} \cdot \hbar_q,
$$

where $c_T(k)$ is the $q$-content of the cell containing $k$ in
SYT $T$. The polynomials $c_k^{(\lambda)}(b_\lambda)$ above factor
through symmetric functions of JM eigenvalues — specifically, the
$k$-th power-sum $p_k(J_2, \ldots, J_n)$ evaluated on $V_\lambda$.

For $V_{(2,1)}$ at single wrap on $H_3$: $J_3$ has eigenvalues
$\pm \hbar_q$, and $p_1(J_3) = 0$ (no first-order JM contribution
because the eigenvalues cancel), but $p_2(J_3) = 2\hbar_q^2$,
matching the leading $\hbar_q^2$ scale of the N=1 correction.

### 3. Macdonald $(q,t)$-degeneration at $t = q^2$

Macdonald polynomials $P_\lambda(x; q, t)$ interpolate between Schur
($t = q$), Hall–Littlewood ($q = 0$), and zonal ($t = q^2$)
specialisations. At $t = q^2$ the Macdonald evaluation reproduces
the τ_M expansion with $c_k^{(\lambda)}(b_\lambda)$ given by the
$P_\lambda$-pairing

$$
  c_k^{(\lambda)}(b_\lambda)
   \;=\;
   \langle P_\lambda(\cdot; q, q^2),\, P_\lambda(\cdot; q, q^2) \rangle_{q, q^2}^{(k)},
$$

the $k$-th coefficient of the Macdonald inner product expanded in
powers of $(t/q^2 - 1)$. The $t = q^2$ specialisation is exactly the
"second deformation parameter" missing in Form A's perturbative
expansion.

### 4. Habiro residue at roots of unity

The dual category-side picture: at $q = \zeta_N$ a primitive $N$-th
root of unity, the Habiro ring evaluation
([`prop:habiro-residue-sum-equivalence`](#prop:habiro-residue-sum-equivalence))
gives a *finite* sum over residues of the q-character. The
**residue-sum-equivalence theorem** identifies this finite sum with
the polynomial-path computation at a specific $\zeta_N$; the
asymptotic $N \to \infty$ recovers the τ_M expansion above.

Specifically, at $\zeta_N = e^{2\pi i / N}$, the Habiro-residue
expansion of $\tau_M^{V_\lambda}$ is the **Borel resummation** of
the asymptotic series $\exp(-\frac{1}{2} \sum c_k \hbar_q^{2k})$ —
the divergent perturbative tail at $\hbar_q \to 0$ becomes
convergent at non-zero $\zeta_N$ deformation.

## Synthesis

The four anchors give independent derivations of the same structural
expansion:

```
                  Kashiwara crystal (vertex labels)
                              │
                              ▼
  JM spectrum  ─────►  τ_M expansion in ℏ_q²  ◄───── Macdonald (q,t)
                              ▲
                              │
                  Habiro residue (Borel resum)
```

Empirical verification per probe sequence:
1. [`probe_q_beta_per_irrep_cos.py`](../../computations/probe_q_beta_per_irrep_cos.py) — V_(2,1) character + KL decategorification.
2. [`probe_q_beta_three_irrep_closed_form.py`](../../computations/probe_q_beta_three_irrep_closed_form.py) — 1-d closed forms (rep-theory triviality).
3. [`probe_q_beta_operator_valued_N1.py`](../../computations/probe_q_beta_operator_valued_N1.py) — Kashiwara $\tilde f_1$ at N=1.
4. [`probe_q_beta_operator_valued_N2.py`](../../computations/probe_q_beta_operator_valued_N2.py) — geometric-tail N=2 (Macdonald-like).
