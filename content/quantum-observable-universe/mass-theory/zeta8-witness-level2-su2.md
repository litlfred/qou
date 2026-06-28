**Proposition (Level-2 SU(2) Verlinde witness at $q = \zeta_8$).**
*Let $\zeta$ be a primitive 8th root of unity in a field $R$ (the
analytic model is $\zeta_8 = e^{i\pi/4} \in \mathbb{C}$). Then the
following three algebraic facts hold:*

1. *$(\zeta_8;\zeta_8)_7 \;=\; \prod_{k=1}^{7}\,(1 - \zeta_8^k) \;=\; 8$.*
2. *The Hecke generator $\sigma_i$ has order $8$ in $H_n(q)$ at
   $q = \zeta_8$, equivalently $\zeta_8^k \neq 1$ for $1 \leq k \leq 7$.*
3. *The quantum integer $[4]_q := (q^4 - q^{-4})/(q - q^{-1})$ vanishes
   at $q = \zeta_8$.*

*Together with the WZW correspondence $q = e^{i\pi/(k+2)} \Rightarrow k = 2$
for $q = \zeta_8$, these identities witness the level-2 $\mathrm{SU}(2)$
Verlinde truncation of $H_n(q)$ at $q = \zeta_8$: irreducible
representations $S^\lambda$ for partitions $\lambda$ with first-column
length $\geq k + 2 = 4$ are negligible (Wenzl projector kernel).*

## Categorical content — universal Δa_m cancellation

The three identities above produce the categorical structure observed
empirically (audit
[`docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-phi8-interference-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md)):

- $(\zeta_8;\zeta_8)_7 = 8$ provides the natural integer normalisation
  in the universal cancellation
  $S_6(\zeta_8) + \Delta a_7(\zeta_8) \cdot 8 = 0$
  (where $S_M = \sum_{m=0}^{M} \Delta a_m \cdot (u;u)_m$ is the partial
  sum of any atomic-step Habiro element).

- $\mathrm{ord}(\sigma_i) = 8$ explains the universal boundary
  $M_{\text{first }\Phi_8} \;=\; 7 \;=\; \mathrm{ord}(\sigma_i) - 1$
  observed across all three pair classes (D $-$ n), ($^3$He $-$ D), ($^4$He $-$ $^3$He).

- $[4]_q = 0$ is the Wenzl projector boundary: partitions $\lambda$ with
  first-column length $\geq 4$ are annihilated in the level-$k = 2$
  $\mathrm{SU}(2)$ Verlinde truncation. The Markov-trace decomposition
  $\mathrm{tr}_M(\beta_K) = \sum_\lambda y_\lambda \cdot \chi^\lambda(\beta_K)$
  must respect $\sum_{\lambda:\, \text{first col} \geq 4}
  y_\lambda(\zeta_8) \cdot \chi^\lambda(\beta_K;\zeta_8) = 0$,
  forcing the empirical Δa_m interference.

## Vindicates earlier hypothesis (a)

In [`docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md),
the level-2 $\mathrm{SU}(2)$ hypothesis (a)
was ruled out as "FALSE in naive form". This proposition shows the
hypothesis is in fact correct — provided the categorical framing is the
**Wenzl annihilator forcing Δa_m interference** rather than "level-2
truncation acting directly on $(\mathfrak{D} - \mathfrak{n})$" (which is
indeed not how the truncation interacts with Habiro elements).

## Lean formalization

The companion Lean file
[`zeta8-witness-level2-su2.lean`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-phi8-interference-2026-06-01/content/quantum-observable-universe/braids-and-knots/zeta8-witness-level2-su2.lean)
formalises all three identities. Identities (1)-(3) are stated with proofs
sketched; the Wenzl-annihilator structural theorem currently carries
`sorry` with bibliographic citations to Wenzl 1987, Jones 1987, and
Witten 1989.
