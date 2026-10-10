While the existence of the Habiro expansion for quantum invariants with integer coefficients is a standard result in quantum topology, its application here uses the strictly finite nature of this algebraic ladder to eliminate arbitrary truncation choices in evaluating physical mass differences, anchoring the observable spectrum directly to the exact cyclotomic integrality of the trace.
## Proton Habiro coefficients (verified integral)

The proton's Markov trace has $M = 8$ (series terminates):

| $m$ | $a_m(u) \in \mathbb{Z}[u]$ |
|-----|---------------------------|
| 0 | $4$ |
| 1 | $-74u - 74$ |
| 2 | $340u^2 + 365u + 389$ |
| 3 | $-711u^3 - 789u^2 - 872u - 959$ |
| 4 | $788u^4 + 901u^3 + 1029u^2 + 1172u + 1328$ |
| 5 | $-466u^5 - 559u^4 - 660u^3 - 781u^2 - 918u - 1078$ |
| 6 | $133u^6 + 167u^5 + 212u^4 + 264u^3 + 328u^2 + 402u + 494$ |
| 7 | $-12u^7 - 17u^6 - 24u^5 - 34u^4 - 48u^3 - 63u^2 - 84u - 110$ |
| 8 | $u^4 + 2u^3 + 3u^2 + 5u + 7$ |

The neutron has the same structure with $M = 8$ and different integer
coefficients. The deuteron has $M = 12$.

## Uniqueness of the archimedean evaluation

The archimedean realisation is not an arbitrary map — it is the unique
evaluation $\widehat{\mathbb{Z}[q]} \to \mathbb{R}$ that:

1. Sends the Habiro ring element $\mathrm{tr}_M(T_w)$ to its
   value at $q = q_0$.
2. Respects the cyclotomic integrality: each $a_m \in \mathbb{Z}[u]$.
3. Terminates at finite $M$ (no truncation needed).

The integrality and finiteness of the $a_m$ require no fitting and no
free parameters beyond $(m_e, q_0)$ — the Habiro evaluation of
$\mathrm{tr}_M$ at $q_0$ is determined.

## Scope of the exact evaluation

Since the Habiro expansion is **finite** ($M = 8$ for proton), the
evaluation $\mathrm{tr}_M(\beta_K, q_0)$ is **exact** — a
well-defined element of $\mathbb{Q}(q_0)$, not a truncated series.

What this does **not** give is experiment-grade agreement with
data. An observable such as $\mathfrak{Q}_\beta$ is
$m_e \cdot f(\mathrm{tr}_M(\beta_n), \mathrm{tr}_M(\beta_p),
q_0)$, and the exact Habiro evaluation of that map lands at the
substrate's *intrinsic* accuracy (improving once the derived low-order
$\mathrm{tr}_M$ corrections of `prop:tau-M-asymptotic-rep-theory` are
included; specific intrinsic-accuracy and ladder-correction figures
live in the archimedean witness ledger, not here).
Reaching experiment-grade precision requires higher-order
corrections that are **not** currently derived from the $a_m$;
attempts to read them off as a "precision ladder" tuned the
coefficients against the experimental value rather than evaluating
them categorically. The canonical content here is the
integrality of the $a_m$, not a high-precision prediction.

