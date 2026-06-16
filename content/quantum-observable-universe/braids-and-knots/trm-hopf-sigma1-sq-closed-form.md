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

See [Table 1](#tbl:trm-hopf-sigma1-sq-closed-form-table1-data).

verified numerically via
[`probe_F_n_categorical_derivation.py`](folio-assistant/computations/probe_F_n_categorical_derivation.py)
([witness](folio-assistant/computations/F-n-categorical-derivation-probe.witness.json),
2/2 assertions pass).

## Implication for the $\mathfrak{Q}_\beta$ precision-ladder

The 𝔔_β factorisation ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
writes
$$
  \mathfrak{Q}_\beta \;=\; Q_A \cdot \cos\bigl(\alpha - b\hbar_q^2/2\bigr)
              \cdot \prod_{n \geq 2} (1 + c_n \hbar_q^{2n})
$$
with claimed coefficients $c_2 = b^2$, $c_3 = -2 b^3$
, $c_4 = b^2 + 1/2$.
The bare-Markov $\varepsilon^{2n}$ coefficients of
$\mathrm{tr}_M(\sigma_1^2) - 1$ above are NOT equal to these:

See [Table 2](#tbl:trm-hopf-sigma1-sq-closed-form-table2-data).

The mismatch proves the $F_n := 1 + c_n \hbar_q^{2n}$ are NOT
extracted from the bare Markov trace of $\sigma_1^2$. They are a
SEPARATE decomposition of $\mathfrak{Q}_\beta$ in which each factor must
arise from a distinct categorical object $\mathcal{B}_n$ — for $F_3$
specifically, the V_(2,2,2) Wedderburn-block projection inside
Hoefsmit $V_{(2,1)} \otimes V_{(2,1)}$ embedded in $H_6$
(per the c_3 = J_Hopf(q=1) = −2 structural identification, locked
behind the §3b-cond `QbetaC3StructuralFormClass` in
`q-beta-categorical-precision-ladder.lean`; see
[`docs/audits/2026-05-31-ck-exploratory-probes-removed.md`](../../../docs/audits/2026-05-31-ck-exploratory-probes-removed.md)
for the derivation status).

## Remarks

1. The closed form $1 + (q-1) \cdot q^{-1/2}$ is the simplest
   nontrivial Markov-trace value in the framework and serves as a
   sanity check for all canonical-Markov implementations
   ([`markov_peel.tr_M_atomic`](folio-assistant/computations/markov/markov_peel.py),
   [`markov_weights_symbolic.tr_M_canonical`](folio-assistant/computations/markov/markov_weights_symbolic.py),
   [`markov_trace_canonical.tr_M_word`](folio-assistant/computations/markov/markov_trace_canonical.py)).
   All three produce identical output for $\sigma_1^2$ at $q = q_0$ to 50 dps.

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

4. **Lean realisation (archimedean specialisation, §7c).** The
   propositional content above is the exact algebraic identity over the
   formal field $\mathbb{Q}(q^{1/2})$ — categorical/fibre level, holding
   for all $q$ with no ordering or analytic hypothesis. The Lean
   formalisation `QOU.Braiding.TrMHopfSigma1SqClosedForm` realises it on
   the **archimedean side**: it specialises $q$ to $\mathbb{R}$ in the
   Wenzl positivity regime $q > 1$ and discharges the identity by the
   substitution $u := \sqrt{q}$ (`Real.sqrt`), reducing
   $\frac{u^5 - u + u^4 + u^2}{u^4 + u^2} = 1 + (u^2 - 1)\,u^{-1}$ via
   `field_simp; ring` under $u > 0$. The square-root substitution and the
   $q > 1$ ordering are the archimedean constructs that pin the
   formalisation to $\mathbb{R}$; the underlying identity itself is
   substrate-side and base-ring-agnostic.


**Mathematical Novelty:** While the derivation itself follows a standard Hecke/Markov calculation, this closed form represents the simplest nontrivial derived Markov-trace in the framework. The value-driven finding that the bare-Markov $\epsilon^{2n}$ coefficients are *not* the $\mathfrak{Q}_\beta$ precision-ladder $c_n$ (meaning $F_n$ is a separate categorical decomposition) adds substantive novel mathematical content to the framework.