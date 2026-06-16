**Remark.**

Empirical data on $y_0^*$ from
[`alpha-5-lp-dual-crystal.witness.json`](computations/alpha/alpha-5-lp-dual-crystal.witness.json)
(2-row stratum, $\ell = 5$):

| $q$ | $y_0^*(D)$ <br/>$(A=2,|T_3|=0)$ | $y_0^*(T) = y_0^*({}^3\mathrm{He})$ <br/>$(A=3,|T_3|=\tfrac{1}{2})$ | ratio $T/D$ |
|----:|------------:|--------------:|--------:|
| 1.110 | 10.31 | 570.68 | 55.34 |
| 1.050 | 7.69 | 247.93 | 32.24 |
| 1.001 | 6.03 | 127.69 | 21.18 |

**Mirror-pair invariance** ($T = {}^3\mathrm{He}$) holds exactly,
as proved by [`prop:spin-involution-lp-dual-invariance`](#prop:spin-involution-lp-dual-invariance).

**Non-separability of $g(q) \cdot h(A, |T_3|)$.** The ratio
$T/D$ depends on $q$ non-by definition (21 $\to$ 55 across the physical
regime). This rules out the simplest separable closed form

$$
  y_0^*(A, |T_3|) \stackrel{?}{=} g_\ell(q) \cdot h_\ell(A, |T_3|),
$$

since separability would force $T/D$ to be $q$-independent.

**Candidate closed forms (research directions).** Listed in
order of increasing structural specificity:

(a) **Partition-of-unity decomposition.** Sum over the
LP-dual active set:

$$
  y_0^*(A, |T_3|) \;=\;
  \sum_{\lambda \in \mathrm{active}(A, |T_3|)}
  a_\lambda(A, |T_3|) \cdot b_\lambda(q).
$$

At $q_0$ the active set is $3/4$ channels for $D$ and $4/5$
channels for $T, {}^3\mathrm{He}$. The $q$-dependent ratio
arises because the LP constraints re-weight at different $q$.

(b) **Wedderburn-block-resolved form.** Each $y_0^*$
decomposes as a sum over per-block contributions

$$
  y_0^*(A, |T_3|)
  \;=\;
  \sum_{\lambda \in \mathrm{active}}
  u_\lambda^*\bigl(A, |T_3|, q\bigr),
$$

with each $u_\lambda^*$ depending on the per-block Frobenius
pairing $y_\lambda \cdot \chi^\lambda(\mathcal{B}_K)$. Mirror-pair
invariance follows because the active sets of $T$ and
${}^3\mathrm{He}$ are $\lambda$-conjugate under the Hopf
antipode (per
[`prop:spin-involution-lp-dual-invariance`](#prop:spin-involution-lp-dual-invariance)).

(c) **$q \to 1$ classical limit.** At $q = 1$ the $q$-numbers
collapse to ordinary integers and the LP-dual should reduce
to a Specht-dim-weighted sum recovering the classical BW
coefficients $\alpha_k$. Empirically the $q = 1.001$ numbers
($D = 6.03$, $T = 127.69$) suggest the limit exists but with
a non-trivial $T/D$ ratio that needs a Specht-combinatorial
explanation.

(d) **Kashiwara crystal limit $q \to 0^+$.** The genuine
Kashiwara crystal limit (NOT $q \to 1$). In that limit the
JM eigenvalues become integer content multiplicities and the
LP becomes integer programming over a Kashiwara crystal graph
(open
follow-up (H)). The current probe sweeps $q \to 1^+$ only;
a separate $q \to 0^+$ probe is needed.

(e) **Demazure sub-crystal selector.**  empirically
found that the categorical rule for $\lambda^*(Z, N)$ is
$\max(y_\lambda \cdot |\chi^\lambda|)$ — not a pure structural
property of $\lambda$. This selector picks out a Demazure
sub-crystal of the canonical basis. The LP-dual $u_\lambda^*$
may decompose along Demazure components, yielding
$y_0^*(A, |T_3|)$ as a sum of crystal-graph weights.

**Witness-able next probes.**

1. **${}^4\mathrm{He}$ probe** ($A = 4, |T_3| = 0$, $n = 12$;
 sympy expensive). *Hypothesis*:
 $y_0^*({}^4\mathrm{He}) / y_0^*(D)$ is $q$-rational — both
 sit on the $|T_3| = 0$ branch — distinct from the
 $|T_3| = \tfrac{1}{2}$ branch ($T, {}^3\mathrm{He}$).

2. **$q \to 0^+$ crystal sweep** at $q \in \{1/2, 1/4, \ldots\}$
 to approach the Kashiwara crystal limit.

3. **Demazure-sliced LP**: solve the LP restricted to a
 single Demazure sub-crystal (chosen by the
 $\max(y_\lambda \cdot |\chi^\lambda|)$ selector of #619)
 to test (e).

**No closed form is asserted as proved.** This remark
consolidates the empirical structure (mirror-pair invariance
holds; simple separable form refuted) and lists the next
research probes. Resolving the $A$-scaling is the highest-
leverage next step for the iterative-LP-dual mass formula.
