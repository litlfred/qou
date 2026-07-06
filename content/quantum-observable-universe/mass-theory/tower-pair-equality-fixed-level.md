The jet-tower mass formula
([rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower))
contains a pair contribution

$$
  z^2 \sum_{(i, j) \in \mathcal{P}_n}
    \Phi_q\!\bigl(\bigl|\hat V_i^{(n)} \hat V_j^{(n)}\bigr|\bigr)
$$

at each jet level $n$. The audit
[`derivation-audit-.md` line 114](../../../docs/audits/derivation-audit-.md)
flagged this as an **upper bound** (because the original
heuristic was the pentagon-ascension argument, which gives only
an inequality), with **sharpness open**. This block closes
audit GAP 17b by replacing the bound with an equality.

## Statement

**Lemma (pair-contribution equality at fixed jet level).**
*Let $n \in \mathbb{N}$ be a brane jet level and let
$\mathcal{P}_n = \{(i, j) : 0 \le i < j\}$ be the full set of
unordered pair blow-up centres at jet level $n$
([rem:mass-endomorphism-jet-tower §$\mathcal{P}_n$ all-pairs](#rem:mass-endomorphism-jet-tower)).
Then the pair contribution at level $n$ is the **exact** value*

$$
  \mathrm{pairs}_n
  \;=\;
  z^2 \sum_{(i, j) \in \mathcal{P}_n}
    \Phi_q\!\bigl(\bigl|\hat V_i^{(n)} \hat V_j^{(n)}\bigr|\bigr),
$$

*with no upper-bound slack — i.e., the formula is an equality, not an
inequality.*

## Equality versus bound

The original "upper bound" framing came from the pentagon-ascension
argument. By
[`lem:vhat-pair-commutation-trace`](#lem:vhat-pair-commutation-trace)
(P3.2), the pentagon identity in its operator form does **not** apply
to scalar traced volumes $\hat V_i \in \mathbb{Z}[q^{\pm 1/2}, z]$;
it applies only to inter-level operator lifts. Hence the pentagon
gives no bound — upper or otherwise — on the level-$n$ pair
contribution. The bound was vacuous to begin with.

The actual algebraic content of the pair contribution is the
**Markov-pair identity**
[`prop:markov-pair-z2`](#prop:markov-pair-z2):

$$
  \mathrm{tr}_M\!\bigl(\sigma_i \sigma_j\bigr) \;=\; z^2
  \qquad\text{for all } i < j,
$$

which is an exact equality (proved by Markov peel, no inequality
involved). Lifting this from raw braid generators $\sigma_i$ to
traced volumes $\hat V_i^{(n)}$ via the algebraic-quantum-volume
factorization
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)) and
the Markov-trace factorization theorem
([`thm:markov-trace-factorization`](#thm:markov-trace-factorization))
preserves the equality at every jet level $n$.
