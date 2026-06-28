## Representation-theoretic structure of the rung coefficients

The rung coefficients are the $q$-Bessel power-series coefficients of the fibre
Habiro element $F$, obeying the proved first-order recurrence
$c_k(1-q^k)(1-q^{\nu+k}) = -q^{k-1}c_{k-1}$ (Lean:
`QOU.QBeta.qbessel_second_order_recurrence`, sorry-free). Four constructions in
Hecke representation theory describe this *same* expansion from complementary
angles; they are structural anchors, not independent numerical derivations — a
distinction an earlier four-anchor cross-check (archived probe
`_deprecated/probes/probe_tau_M_four_anchors.py`) blurred, as noted per
construction.

### 1. Kashiwara crystal graph (the load-bearing anchor)

For each irrep $V_\lambda$ of $U_q(\mathfrak{sl}_n)$ (hence $H_n(q)$), the
Kashiwara crystal $B(\lambda)$ has $\dim V_\lambda$ vertices (one per SYT) and
edges given by the $\tilde f_i$ operators. For $V_{(2,1)}$:

```
  T_1 = [[1,2],[3]]  --(\tilde{f}_1)-->  T_2 = [[1,3],[2]]
```

a single edge of weight $b_\lambda = b$. The $N=1$ eigenphase shift
$-b\,\hbar_q^2/2$ is exactly this matrix element times $\hbar_q^2/2$; the same
coupling at the second rung supplies the proved factor $(1 - b^2\hbar_q^4)$.
This is the construction that fixes the data used downstream.

### 2. Jucys–Murphy elements (diagonal eigenphase envelope)

The Jucys–Murphy elements $J_k \in Z(H_n(q))$ ($2 \leq k \leq n$) generate the
centre, with $J_k|_{V_\lambda^T} = q^{c_T(k)} - q^{-c_T(k)}\hbar_q$, $c_T(k)$ the
$q$-content of the cell holding $k$ in SYT $T$. For $V_{(2,1)}$ on $H_3$, $J_3$
has eigenvalues $\pm h$ ($h = q - q^{-1}$), so $p_1(J_3) = 0$ while
$p_2(J_3) = 2h^2$. Because $J_k$ is *diagonal* in the seminormal basis, it
produces the $\pm h$ eigenphase envelope but cannot, on its own, generate the
off-diagonal coupling $b$ that lives in $\sigma_1$; the JM data is therefore
**complementary** to the Kashiwara coupling, not an independent route to the
$N=1$ term. (The archived probe reported "$c_1^{\mathrm{JM}} = 0$" from
$p_1 = 0$ and mis-indexed the $O(\hbar_q^2)$ quantity
$p_2/2 = h^2 = (q+1)^2\hbar_q^2$ as a higher rung; both are artefacts of the
wrong index, not a disagreement with the Kashiwara value.)

### 3. Macdonald $(q,t)$-degeneration at $t = q^2$

Macdonald polynomials $P_\lambda(x; q, t)$ interpolate between Schur ($t = q$),
Hall–Littlewood ($q = 0$), and zonal ($t = q^2$) specialisations. The $t = q^2$
point is the "second deformation parameter" absent from Form A, and the
$(q,t)$-inner-product expansion in powers of $(t/q^2 - 1)$ is the natural home
for the higher rungs. The normalisation must be taken with care: the bare zonal
norm $\langle P_\lambda, P_\lambda\rangle_{q,q^2}$ is an $O(1)$ quantity (for
$V_{(2,1)}$ it tends to $20/9$ as $q \to 1$, not to $1$), so a coefficient must
be read from a ratio that is $1 + O(\hbar_q^2)$, not from
$(\text{norm} - 1)/\hbar_q^2$. With the correct normalisation this anchor is
open; the archived probe's large candidate was the un-normalised artefact.

### 4. Habiro residue at roots of unity

At $q = \zeta_N$ a primitive $N$-th root of unity the Habiro ring evaluation
([`prop:habiro-residue-sum-equivalence`](#prop:habiro-residue-sum-equivalence))
gives a *finite* residue sum, and near $q = 1$ a Habiro element's coefficients
are its Ohtsuki invariants — so $c_k^{(\lambda)}$ is the $k$-th Ohtsuki
invariant of $F$. This is the canonical home of the rungs: the recursion's
kernel $R(q,\xi)$ is fixed once $F$ is exhibited as a quantum-modular form on
the brane-tower (contraction) limit, the open $s5$–$so_3$ keystone. At leading
order this reproduces the $N=1$ coupling $b$ (by the residue-sum equivalence);
the real-$x$ archimedean closure of $c_3$ is refuted (PR #2300), so the
identification is **fibre-level only** and the rungs stay cal-anchored pending
the keystone.

## Synthesis

The Kashiwara coupling fixes the proved data ($N=1$ envelope $b$, second rung
$c_2 = -1$); Habiro supplies the Ohtsuki-invariant reading and the recursion's
canonical home; Jucys–Murphy supplies the complementary diagonal eigenphase
envelope; Macdonald places the higher rungs in the $(q, q^2)$ inner product. The
rungs themselves obey one proved recursion; only its kernel is open.

```
                  Kashiwara crystal (coupling b → N=1, c_2)
                              │
                              ▼
  JM eigenphase  ─────►  τ_M ladder in u = bℏ_q²  ◄───── Macdonald (q,q²)
   envelope                   ▲                          (higher rungs, open)
                              │
                  Habiro residue (c_k = Ohtsuki invariants; proved recursion)
```

Empirical verification per probe sequence:
1. [`probe_q_beta_per_irrep_cos.py`](../../../computations/probe_q_beta_per_irrep_cos.py) — $V_{(2,1)}$ character + KL decategorification.
2. [`probe_q_beta_three_irrep_closed_form.py`](../../../computations/probe_q_beta_three_irrep_closed_form.py) — 1-d closed forms (rep-theory triviality).
3. [`probe_q_beta_operator_valued_N1.py`](../../../computations/probe_q_beta_operator_valued_N1.py) — Kashiwara $\tilde f_1$ at $N=1$ (envelope coupling $b$).
4. [`probe_q_beta_operator_valued_N2.py`](../../../computations/probe_q_beta_operator_valued_N2.py) — second rung $(1 - b^2\hbar_q^4)$, $c_2 = -1$.
