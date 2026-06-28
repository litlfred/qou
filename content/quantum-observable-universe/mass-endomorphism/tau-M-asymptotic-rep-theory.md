**$\tau_M$ ladder — representation-theoretic structure.**

**Proposition (conditional on the open recursion kernel of
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference)).**
The low-order data ($c_0 = 0$, 1-d triviality, the $N=1$ coupling $b$, and the
bar-even seed $c_2 = -1$) together with the $\hbar_q$-parity are proved
*unconditionally* (Proof, below). The full ladder
$\prod_{k \geq 2}\bigl(1 + c_k^{(\lambda)} u_\lambda^k\bigr)$ is rigorous **modulo**
the substrate-derivation of the kernel $R(q,\xi)$ that fixes $c_k$ for $k \geq 3$
— the open $s5$–$so_3$ keystone. The higher rungs are therefore conjectural
pending that kernel; only the $N \leq 2$ truncation enters the
calibrated mass evaluation.

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
