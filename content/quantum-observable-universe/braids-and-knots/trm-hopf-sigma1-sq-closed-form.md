**Proposition (closed form for the canonical Markov trace of $\sigma_1^2$).**

*Let $H_n(q)$ be the Iwahori–Hecke algebra of type $A_{n-1}$ over
$\mathbb{Q}(q^{1/2})$ and let $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Q}(q^{1/2})$
be the canonical Markov trace ([`thm:jones-markov-trace`](#thm:jones-markov-trace)).
Then for every $n \geq 2$,*

$$
\boxed{\quad
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; \frac{q^{5/2} - q^{1/2} + q^2 + q}{q^2 + q}
  \;=\; 1 + \frac{q - 1}{q^{1/2}}.
\quad}
$$

*The value is independent of $n$ (Markov invariance under
stabilisation), and the closure $\widehat{\sigma_1^2}$ is the
positive Hopf link $L_+^{\mathrm{Hopf}}$.*

## Proof

The Hecke quadratic relation $\sigma_1^2 = (q - q^{-1})\sigma_1 + 1$
gives $\mathrm{tr}_M(\sigma_1^2) = (q - q^{-1})\,\mathrm{tr}_M(\sigma_1) + \mathrm{tr}_M(1)$.
The Markov axioms ([`thm:jones-markov-trace`](#thm:jones-markov-trace))
fix $\mathrm{tr}_M(1) = 1$ and
$\mathrm{tr}_M(\sigma_1) = z := 1/(q^{1/2} + q^{-1/2})$, so
$$
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; (q - q^{-1}) \cdot \frac{1}{q^{1/2} + q^{-1/2}} + 1.
$$
Simplifying the first term:
$\frac{q - q^{-1}}{q^{1/2} + q^{-1/2}} = \frac{(q - q^{-1}) \cdot q^{1/2}}{q + 1} = \frac{q^{3/2} - q^{-1/2}}{q + 1}$.
Multiplying numerator and denominator by $q^{1/2}$ and combining
with $+1$ over common denominator $q(q+1) = q^2 + q$ gives
$\frac{q^{5/2} - q^{1/2} + q^2 + q}{q^2 + q}$. Algebraically this
equals $1 + (q-1)/q^{1/2}$, as can be verified by clearing
denominators.

Markov invariance under stabilisation ([`thm:jones-markov-trace`](#thm:jones-markov-trace)
property 3): for $\beta \in H_n(q)$,
$\mathrm{tr}_M(\beta \cdot \sigma_n^{\pm 1}) = z^{\pm 1} \mathrm{tr}_M(\beta)$
when the new generator $\sigma_n$ is disjoint from $\beta$. Since
$\sigma_1^2$ involves only the first generator, its trace in $H_n$
for any $n \geq 2$ coincides with the trace in $H_2$: no
stabilisation factor enters because the new strand is unlinked from
the closure of $\sigma_1^2$. ∎

## Taylor expansion at $q = 1 + \varepsilon$

Substituting $q = 1 + \varepsilon$ and expanding gives a closed
binomial series:

$$
  \mathrm{tr}_M(\sigma_1^2) - 1
  \;=\; \varepsilon \cdot (1 + \varepsilon)^{-1/2}
  \;=\; \sum_{k \geq 0} \binom{-1/2}{k} \varepsilon^{k+1}.
$$

The $\varepsilon^k$ coefficients $\binom{-1/2}{k-1}$ for $k \geq 1$
are:

| $k$ | coefficient | $\binom{-1/2}{k-1}$ |
|---:|---:|---|
| 1 | $1$ | $\binom{-1/2}{0}$ |
| 2 | $-1/2$ | $\binom{-1/2}{1}$ |
| 3 | $3/8$ | $\binom{-1/2}{2}$ |
| 4 | $-5/16$ | $\binom{-1/2}{3}$ |
| 5 | $35/128$ | $\binom{-1/2}{4}$ |
| 6 | $-63/256$ | $\binom{-1/2}{5}$ |
| 7 | $231/1024$ | $\binom{-1/2}{6}$ |

verified numerically via
[`probe_F_n_categorical_derivation.py`](folio-assistant/computations/probe_F_n_categorical_derivation.py)
([witness](folio-assistant/computations/F-n-categorical-derivation-probe.witness.json),
2/2 assertions pass).

## Implication for the $Q_\beta$ precision-ladder

The Q_β factorisation ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
writes
$$
  Q_\beta \;=\; Q_A \cdot \cos\bigl(\alpha - b\hbar_q^2/2\bigr)
              \cdot \prod_{n \geq 2} (1 + c_n \hbar_q^{2n})
$$
with claimed coefficients $c_2 = b^2$ (PR #661, derived), $c_3 = -2 b^3$
(PR #657 Track-C, conjectured), $c_4 = b^2 + 1/2$ (PR #665, conjectured).
The bare-Markov $\varepsilon^{2n}$ coefficients of
$\mathrm{tr}_M(\sigma_1^2) - 1$ above are NOT equal to these:

| $n$ | framework $c_n$ at $q=1$ | bare-Markov $\varepsilon^{2n}$ |
|---:|---:|---:|
| 2 | $b^2(1) = 3/4 = 0.7500$ | $-5/16 \approx -0.3125$ |
| 3 | $-2 b^3(1) = -3\sqrt{3}/4 \approx -1.2990$ | $-63/256 \approx -0.2461$ |
| 4 | $b^2(1) + 1/2 = 5/4 = 1.2500$ | $-429/2048 \approx -0.2095$ |

The mismatch proves the $F_n := 1 + c_n \hbar_q^{2n}$ are NOT
extracted from the bare Markov trace of $\sigma_1^2$. They are a
SEPARATE decomposition of $Q_\beta$ in which each factor must
arise from a distinct categorical object $\beta_n$ — for $F_3$
specifically, the V_(2,2,2) Wedderburn-block projection inside
Hoefsmit $V_{(2,1)} \otimes V_{(2,1)}$ embedded in $H_6$
(per [`prop:hopf-jones-c3-categorical`](#prop:hopf-jones-c3-categorical)
claim, derivation pending).

## Remarks

1. The closed form $1 + (q-1) \cdot q^{-1/2}$ is the simplest
   nontrivial Markov-trace value in the framework and serves as a
   sanity check for all canonical-Markov implementations
   ([`markov_peel.tr_M_atomic`](folio-assistant/computations/markov_peel.py),
   [`markov_weights_symbolic.tr_M_canonical`](folio-assistant/computations/markov_weights_symbolic.py),
   [`markov_trace_canonical.tr_M_word`](folio-assistant/computations/markov_trace_canonical.py)).
   All three produce identical output for σ_1² at q = q_0 to 50 dps.

2. The binomial-coefficient closed form for the Taylor expansion is
   a special case of the more general identity
   $\mathrm{tr}_M(\sigma_1^k) - z^{k-1} = \mathrm{poly}_k(q) \cdot q^{-(k-1)/2}$
   for $k \geq 1$, derivable by iterating the Hecke quadratic
   relation.

3. The Markov-invariance of $\mathrm{tr}_M(\sigma_1^2)$ across
   $H_n$ for $n \geq 2$ is consistent with the Markov property at
   property 3 of [`thm:jones-markov-trace`](#thm:jones-markov-trace),
   and is verified empirically across H_3, H_4, H_5, H_6 in
   [`probe_F_n_categorical_derivation.py`](folio-assistant/computations/probe_F_n_categorical_derivation.py).
