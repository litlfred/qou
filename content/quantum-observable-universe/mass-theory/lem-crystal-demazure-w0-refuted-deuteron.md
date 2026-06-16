**Lemma (refutation).**
*The principal-specialisation crystal-graph weight
$c_\lambda(q) := s_\lambda(1, q, \dots, q^{n-1})$ — which at this
specialisation equals the Demazure character $D_{w_0}(\lambda)$ — does
**not** serve as the per-block binding density $\Delta_\lambda$ in the
Path-D density formula*

$$
  \rho_K \;=\; \rho_K^{\mathrm{LO}}
    \;+\; \frac{1}{|\mathrm{tr}_M|}\sum_{\lambda \,\vdash\, 3A}
            y_\lambda\,\chi^\lambda\,\Delta_\lambda .
$$

*At the deuteron it overshoots the empirical target by far more than the
viability tolerance $\mathrm{tol} = 1$ (in $m_e$ units),*

$$
  \mathrm{tol} \;<\; \Sigma_{\mathrm{crystal}}(D) - \tau(D),
  \qquad
  \Sigma_{\mathrm{crystal}}(D) \approx +1796.735,\quad
  \tau(D) = -B_D/m_e \approx -4.353
$$

*(in $m_e$ units): a gap of $\approx 1801$ — the **wrong sign** and
$\approx 412\times$ the target magnitude.*

This refutes **simultaneously** the Option C (Demazure-fibre) and the
Option E principal-specialisation (crystal-graph weight) closure attempts
for the $\Delta_\lambda$ gate, because the two coincide at the principal
specialisation, $c_\lambda(q) = D_{w_0}(\lambda)$ (verified by
`demazure-markov-trace.witness.json`).

*Proof.* This is an **archimedean** statement: the predicted sum
$\Sigma_{\mathrm{crystal}}(D)$ and the target $\tau(D)$ are obtained by
**numerical evaluation** at the substrate $q_0$ (50 dps, post-$\tau$,
real/rational arithmetic) in
`computations/rho-k-h3a-crystal.py` (witness
`rho-k-h3a-crystal.witness.json`, field `residual_target_minus_sum`
$\approx -1801.089$); the Lean sibling accordingly works over $\mathbb{Q}$
with ordering and `abs` (CLAUDE.md §7c). The resulting inequality
$\mathrm{tol} < \Sigma_{\mathrm{crystal}}(D) - \tau(D)$ is a decidable
rational comparison, discharged by `norm_num` in the Lean sibling. $\square$

**Scope — what this does *not* refute.**
The refutation is confined to the **principal-specialisation** weight. It
does **not** bear on:

- the bar-symmetric / isospin Option-E *v9* Kashiwara-crystal variants
  (`option-e-v9-bar-symmetric-test-probe`, `option-e-isospin-probe`),
  which remain open research directions; nor on
- the **successful** deuteron closure via the free-subtracted atomic
  Frobenius co-Casimir trace + Wigner pairing
  ([deuteron binding from Frobenius co-Casimir](#prop:deuteron-binding-frobenius-codim),
  matching $B_{\mathrm{AME}}(D)$ to $+0.19\%$) — that construction uses a
  different functional and is unaffected.

In the language of `compute-author.md` §3.4, this is the *formalize-the-
refutation* mirror of the formalize-first discipline: a numerically refuted
$\Delta_\lambda$ ansatz is recorded as a machine-checked inequality so it
cannot be silently re-proposed.

**Witness:** `rho-k-h3a-crystal.witness.json`.
