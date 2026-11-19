While the existence of the Habiro expansion for quantum invariants with integer coefficients is a standard result in quantum topology, its application here uses the strictly finite nature of this algebraic ladder to eliminate arbitrary truncation choices in evaluating physical mass differences, anchoring the observable spectrum directly to the exact cyclotomic integrality of the trace.
## Proton Habiro coefficients (verified integral)

The denominator-cleared numerator of the proton's Markov trace has
$M = 8$ (series terminates). Under convention D the proton trace is
$p_p(u)/d_p(u)$ with $d_p = 4u^{18}(u^4+1)^2$, and the expansion of
$p_p$ is:

| $m$ | $a_m(u) \in \mathbb{Z}[u]$ |
|-----|---------------------------|
| 0 | $8$ |
| 1 | $-100u - 100$ |
| 2 | $385u^2 + 418u + 449$ |
| 3 | $-722u^3 - 819u^2 - 899u - 1010$ |
| 4 | $732u^4 + 846u^3 + 979u^2 + 1116u + 1286$ |
| 5 | $-411u^5 - 485u^4 - 586u^3 - 689u^2 - 826u - 966$ |
| 6 | $119u^6 + 150u^5 + 185u^4 + 229u^3 + 283u^2 + 353u + 431$ |
| 7 | $-16u^7 - 23u^6 - 31u^5 - 33u^4 - 47u^3 - 62u^2 - 77u - 114$ |
| 8 | $u^8 + u^7 + 2u^6 + 3u^5 + 2u^4 + 4u^3 + 5u^2 + 6u + 15$ |

In contrast, the Convention-C expansion yields non-monic coefficients ($a_0 = 4$, $a_1 = -74u - 74$, ...).

The neutron has the same structure with $M = 8$ and different integer
coefficients. The deuteron has $M = 13$ under convention D (it was $12$ under C).

## Uniqueness of the archimedean evaluation

The archimedean realisation is not an arbitrary map — it is the unique
evaluation $\widehat{\mathbb{Z}[q]} \to \mathbb{R}$ that:

1. Sends $\mathrm{tr}_M(T_w) = p_w/d_w$ to its value at $q = q_0$.
2. Respects the cyclotomic integrality: each $a_m \in \mathbb{Z}[u]$.
3. Terminates at finite $M$ (no truncation needed).

The integrality and finiteness of the $a_m$ require no fitting and no
free parameters beyond $(m_e, q_0)$ — the Habiro evaluation of
$\mathrm{tr}_M$ at $q_0$ is determined.

## Scope of the exact evaluation

Since the Habiro expansion is **finite** ($M = 8$ for proton), the
evaluation $\mathrm{tr}_M(\beta_K, q_0)$ is **exact**: it is a
well-defined element of $\mathbb{Q}(q_0)$ rather than a truncated series.

What this does **not** give is experiment-grade agreement with
data. An observable such as $\mathfrak{Q}_\beta$ is
$m_e \cdot f(\mathrm{tr}_M(\beta_n), \mathrm{tr}_M(\beta_p),
q_0)$, and the exact Habiro evaluation of that map lands at the
aether's *intrinsic* accuracy (improving once the derived low-order
$\mathrm{tr}_M$ corrections of `prop:tau-M-asymptotic-rep-theory` are
included; specific intrinsic-accuracy and ladder-correction figures
live in the archimedean witness ledger, not here).
Reaching experiment-grade precision requires higher-order
corrections that are **not** currently derived from the $a_m$;
attempts to read them off as a "precision ladder" tuned the
coefficients against the experimental value rather than evaluating
them categorically. The canonical content here is the
integrality of the $a_m$ rather than a high-precision prediction.

