**$\tau_M$ ladder — representation-theoretic structure.**

**Proposition (conditional on the open recursion kernel of
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference)).**
The low-order data ($c_0 = 0$, 1-d triviality, the $N=1$ coupling $b$, and the
bar-even seed $c_2 = -1$) together with the $\hbar_q$-parity are proved
*unconditionally* (Proof, below). The full ladder
$\prod_{k \geq 2}\bigl(1 + c_k^{(\lambda)} u_\lambda^k\bigr)$ is rigorous **modulo**
the substrate-derivation of the kernel $R(q,\xi)$ that fixes $c_k$ for $k \geq 3$
— the open $s5$–$so_3$ keystone. The higher rungs are therefore conjectural
pending that kernel; nothing beyond $N=2$ is wired to production.

For a typed braid $\beta$ and a Hecke irrep $V_\lambda$ of $H_n(q)$, the
Markov-traced character at single wrap admits the canonical factorisation, in
the substrate ladder variable $u_\lambda = b_\lambda\,\hbar_q^2$
($\hbar_q = (q-1)/q$):

$$
\boxed{
  \tau_M^{V_\lambda}(\beta)
   \;=\;
   \mathrm{Tr}\,\rho_\lambda(\beta) \cdot
   \cos\!\Bigl(\alpha_\lambda - \tfrac{b_\lambda \hbar_q^2}{2}\Bigr) \cdot
   \prod_{k \geq 2}\bigl(1 + c_k^{(\lambda)}\, u_\lambda^{\,k}\bigr),
}
$$

matching the canonical $\mathfrak{Q}_\beta$ precision ladder
([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)),
where:

- $\rho_\lambda$ is the **Hoefsmit seminormal representation** of
  $H_n(q)$ on $V_\lambda$;
- $b_\lambda$ is the **off-diagonal coupling** of $\rho_\lambda(\sigma_i)$
  in the standard-tableau basis (for $V_{(2,1)}$ of $H_3$ the scalar
  $b = \sqrt{q^4+q^2+1}/(q^2+1) = \sqrt{d_1 d_2 + 1}$ of
  [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization));
- $\alpha_\lambda$ is the single-wrap eigenphase on $V_\lambda$, so the
  $\cos(\alpha_\lambda - b_\lambda\hbar_q^2/2)$ envelope carries the $N=1$
  coupling $b_\lambda$;
- $c_k^{(\lambda)}$ are the rung coefficients of the ladder, the higher
  Ohtsuki invariants of the correction factor.

The factorisation defines the correction factor
$F_\lambda := \tau_M^{V_\lambda}(\beta) / \mathrm{Tr}\,\rho_\lambda(\beta)$
(valid wherever $\mathrm{Tr}\,\rho_\lambda(\beta) \neq 0$); the content is the
$\hbar_q$-parity and the determination of the rung coefficients. The ladder is
**even in $\hbar_q$** (only even powers survive) by Markov-cyclicity invariance
under the bar involution $q \leftrightarrow q^{-1}$ — see
[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation).

The rung coefficients are not free: they are determined by the proved
second-order $q$-difference (Hahn–Exton $q$-Bessel) recursion of
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference),
and the whole product is the Taylor expansion of the **exact finite Habiro sum**
that production evaluates without truncation
([`prop:habiro-precision-ladder-equivalence`](#prop:habiro-precision-ladder-equivalence)).

| order | datum | status |
|------:|:---:|:---|
| $k = 0$ | $c_0 = 0$ | proved (Form A baseline, $q = 1$) |
| 1-d irreps | $F_\lambda \equiv 1$ | proved ($V_{(n)}, V_{(1^n)}$: $b_\lambda = 0$) |
| $N=1$ envelope | $\cos(\alpha - b\hbar_q^2/2)$, coupling $b$ | proved (Hoefsmit $\tilde f_1$ matrix element) |
| $k = 2$ | $c_2 = -1$, factor $(1 - b^2\hbar_q^4)$ | proved seed (bar-even, PR #1602); **wired** ($\mathfrak{Q}_\beta$ production) |
| $k = 3$ | $c_3 \approx -2$, factor $(1 - 2b^3\hbar_q^6)$ | near-match (recursion + open kernel) |
| $k \geq 4$ | $c_k^{(\lambda)}$ | recursion-generated; kernel open |

For the production mass formula ($\mathfrak{m}_{\mathfrak{n}} = \mathfrak{m}_{\mathfrak{p}} + \mathfrak{Q}_\beta + \mathfrak{m}_{\mathfrak{e}}$) only the $N=1$ envelope and the proved
seed $c_2 = -1$ are used (`derived_masses.q_beta_kashiwara_n2_mev`); the higher
rungs matter only for the $1\,\mathrm{ppQ}$ stretch target, where the kernel
$R(q,\xi)$ / order $\nu$ that the recursion needs is the open $s5$–$so_3$
keystone (the same open input as the absolute-mass $F_{\mathrm{Bor}}$ term-6
Habiro tail — one keystone, not two fits).

## Proof

*Proof (Lean: `tau_M_asymptotic_rep_theory`).* The factorisation defines
$F_\lambda$; the substance is the parity and the proved rungs.

**Parity (even in $\hbar_q$).** Markov cyclicity $\tau_M(xy) = \tau_M(yx)$ with
the bar involution $q \leftrightarrow q^{-1}$ forces
$F_\lambda(\hbar_q) = F_\lambda(-\hbar_q)$: the single-wrap character
symmetrises over the two eigenphases of $\rho_\lambda$ into
$\mathrm{tr}\,\rho_\lambda(\beta)\cdot\cos\alpha$
([`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization),
[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation)), and
$\cos$ is even; the rung exponents $u_\lambda^k = b_\lambda^k\hbar_q^{2k}$ are
even in $\hbar_q$ by construction. The bar-parity alternation of the rung
coefficients ($\overline{c_k} = (-1)^k c_k$, bar-even seed $c_2 = -1$) is the
sorry-free `esymm_bar_parity` of
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference).
$\square$ (parity)

**Baseline $c_0 = 0$.** At $q = 1$, $\hbar_q = 0$ and
$\rho_\lambda(\sigma_i) \mapsto$ the symmetric-group permutation matrix, so
$\tau_M^{V_\lambda} = \mathrm{Tr}\,\rho_\lambda(\beta)$ and $F_\lambda(0) = 1$,
i.e. $c_0 = 0$. $\square$

**One-dimensional irreps.** For $V_{(n)}$ (trivial) and $V_{(1^n)}$ (sign),
$\rho_\lambda(\sigma_i)$ is a scalar, the off-diagonal coupling vanishes
($b_\lambda = 0$, hence $u_\lambda = 0$), and the Markov-symmetrised character
equals the bare character; thus $F_\lambda \equiv 1$. The 1-d closed forms are
[`prop:hecke-1d-irrep-closed-form-character`](#prop:hecke-1d-irrep-closed-form-character).
$\square$

**$N=1$ envelope (coupling $b$), $V_{(2,1)}$.** The first non-trivial irrep is
the 2-d $V_{(2,1)}$ of $H_3$. Its single $\tilde f_1$ Kashiwara edge carries
weight $b_\lambda = b$, giving the eigenphase shift $-b\,\hbar_q^2/2$ (the
$\tilde f_1$ matrix element in the seminormal basis times $\hbar_q^2/2$),
resummed into the $\cos(\alpha - b\hbar_q^2/2)$ envelope. This is the $N=1$
result of
[`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization).
$\square$

**Second rung (production wire), $V_{(2,1)}$: $c_2 = -1$.** The first product
rung is $(1 + c_2 u^2)$ with $u = b\hbar_q^2$. The seed $c_2 = -1$ is proved
categorically (the bar-even constraint, PR #1602), giving the factor
$(1 - u^2) = (1 - b^2\hbar_q^4)$ — exactly the second-order correction the
production neutron consumes
($\mathfrak{Q}_\beta = \mathfrak{Q}_\beta^{(N=1)}\cdot(1 - b^2\hbar_q^4)$,
`derived_masses.q_beta_kashiwara_n2_mev`). One coupling $b$ thus drives both the
$N=1$ envelope and the proved second rung. $\square$

The proof determines $c_0$, the 1-d triviality, the $N=1$ coupling $b$, and the
proved seed $c_2 = -1$, together with the $\hbar_q$-parity. The rungs
$c_k^{(\lambda)}$ for $k \geq 3$ are *generated* by the proved recursion of
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference)
once its kernel $R(q,\xi)$ is fixed; that kernel is the open keystone (see
below). $\blacksquare$

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
