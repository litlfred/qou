<!-- Theorem (proved by composition of two named identities). -->

**Proposition (multiplicative-chain form of $\alpha_{EM}^{-1}$).**
*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$ with
the canonical substrate parameter $q$,*

$$
  \boxed{\;\;
    \alpha_{EM}^{-1}
    \;=\;
    q \cdot
    \bigl[\alpha_{\mathrm{shift}}(T_{2,9})\bigr]_q \cdot
    \bigl[\alpha_{\mathrm{shift}}(T_{3,5})\bigr]_q.
  \;\;}
$$

### Proof.

The identity is a composition of two named identities:

1. [`prop:em-coupling-projection`](#prop:em-coupling-projection)
   establishes the bare combinatorial form

   $$
     \alpha_{EM}^{-1} \;=\; q \cdot [9]_q \cdot [10]_q,
   $$

   derived from the antisymmetric eigenvalue $-q^{-1}$ of the
   $R$-matrix and the $q$-deformed crossing numbers of the two
   force-carrier generators $T_{2,9}$ (crossing number $9$) and
   $T_{3,5}$ (crossing number $10$). The basis is exactly two knots
   by [`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)
   — the genus-$4$ saturating torus-knot set on $\Sigma_4$.

2. [`prop:alpha-shift-torus-knot`](#prop:alpha-shift-torus-knot)
   establishes the closed-form identity

   $$
     \alpha_{\mathrm{shift}}(T_{p,k}) \;=\; k(p-1)
     \qquad (\gcd(p, k) = 1)
   $$

   on the all-anti-symmetric channel $V_{(1^p)}$. Specialising at
   $(p, k) \in \{(2, 9), (3, 5)\}$:

   $$
     \alpha_{\mathrm{shift}}(T_{2,9}) \;=\; 9 \cdot 1 \;=\; 9,
     \qquad
     \alpha_{\mathrm{shift}}(T_{3,5}) \;=\; 5 \cdot 2 \;=\; 10.
   $$

Substituting these two values into the bare formula yields the
stated identity exactly:

$$
  \alpha_{EM}^{-1}
  \;=\; q \cdot [9]_q \cdot [10]_q
  \;=\; q \cdot \bigl[\alpha_{\mathrm{shift}}(T_{2,9})\bigr]_q
              \cdot \bigl[\alpha_{\mathrm{shift}}(T_{3,5})\bigr]_q.
  \qquad \square
$$

### Significance — bridge to the w3-w4 atomic-shift framework

Both ingredients now expose the **same combinatorial primitive** —
pole order at $q = 0$ of a seminormal Hecke trace:

| Object                          | Shift role                                                                                            |
|---------------------------------|--------------------------------------------------------------------------------------------------------|
| Atomic Markov-trace denominator | $D(u) = 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^2)^{3A-1}$ ([`docs/audits/2026-05-03-w3-habiro-unblocked.md`](../../docs/audits/2026-05-03-w3-habiro-unblocked.md)) |
| Torus knot $T_{p,k}$ on $V_{(1^p)}$ | $\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ ([`prop:alpha-shift-torus-knot`](#prop:alpha-shift-torus-knot))            |
| Inverse fine-structure constant | $\alpha_{EM}^{-1} = q \cdot [\alpha_{\mathrm{shift}}(T_{2,9})]_q \cdot [\alpha_{\mathrm{shift}}(T_{3,5})]_q$           |

The torus-braid case is the **clean limit** of the atomic-braid
shift framework: no inter-nucleon term, all generators are $\sigma_i$
(none averaged, none $\sigma^{-1}$), no within-partition Hecke
$\sigma^2$-cancellation (because the SYT path through the single
column visits distinct axial distances at every step), and no
cross-partition Ocneanu cancellation (because the maximum is
realised on a unique irrep).

### Numerical verification

The composition is exact at the symbolic level. Numerical
re-evaluation at $q_0$
([`alpha-em-shift-multiplicative-chain.witness.json`](../../folio-assistant/computations/alpha-em-shift-multiplicative-chain.witness.json),
mpmath 50-dps) reads $\alpha_{\mathrm{shift}}(T_{2,9})$ and
$\alpha_{\mathrm{shift}}(T_{3,5})$ from the upstream witness
[`alpha-shift-torus.witness.json`](../../folio-assistant/computations/alpha-shift-torus.witness.json)
and compares the chain expression $q \cdot [\alpha_{\mathrm{shift}}(T_{2,9})]_q
\cdot [\alpha_{\mathrm{shift}}(T_{3,5})]_q$ to the bare expression
$q \cdot [9]_q \cdot [10]_q$:

$$
  |\,\text{chain} - \text{bare}\,| \;=\; 0
  \quad (\text{exactly, to mpmath precision}),
$$

with both equalling $\alpha_{EM}^{-1}(q_0) \approx 136.823$. (The
gap $|\,\text{chain} - \text{CODATA}\,| \approx 0.213$ is the same
$\mathcal{O}(10^{-3})$ precision gap inherited from
[`prop:em-coupling-projection`](#prop:em-coupling-projection),
unchanged by this refactoring; closing it remains the work of
[`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation)
and the higher-order $C_5$-invariant corrections discussed there.)

All $3$ assertions in the witness pass.
