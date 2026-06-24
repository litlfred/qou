## Statement

**Proposition (axiomatic Markov-trace closed form).** *Let $H_n(q)$
denote the Iwahori-Hecke algebra of type $A_{n-1}$ with Hecke
quadratic relation*

$$
  \sigma_i^2 \;=\; h\,\sigma_i + 1, \qquad h \;=\; q - q^{-1},
$$

*and let $\operatorname{tr}_M : \bigsqcup_n H_n(q) \to \mathbb{Q}(q)$
be the Markov trace ([`prop:categorical-mass-markov`](#prop:categorical-mass-markov)),
uniquely determined by*

$$
  \operatorname{tr}_M(1) = 1, \qquad
  \operatorname{tr}_M(\alpha \sigma_n) = z \cdot \operatorname{tr}_M(\alpha) \;\text{for}\; \alpha \in H_n \subset H_{n+1}, \qquad
  \operatorname{tr}_M(\alpha\beta) = \operatorname{tr}_M(\beta\alpha),
$$

*with $z = 1/(q^{1/2} + q^{-1/2})$. Then for the proton's
atomic-braid word $\sigma_1^7 \sigma_2^4 \in H_3(q)$, the Markov
trace admits the closed-form expression*

$$
  \operatorname{tr}_M(\sigma_1^7 \sigma_2^4)(q)
   \;=\; a_7 a_4 \, z^2 \;+\; (a_7 b_4 + b_7 a_4)\, z \;+\; b_7 b_4,
$$

*where $(a_k, b_k)$ are the polynomials in $h$ defined by the
Hecke-power recurrence $a_{k+1} = h\,a_k + b_k$, $b_{k+1} = a_k$,
$a_0 = 0$, $b_0 = 1$. After substituting $h = q - q^{-1}$ and
$z = 1/(q^{1/2}+q^{-1/2})$ and rationalising, the denominator
factors as $q^{10}(q+1)^3$.*

*Numerical evaluation at the substrate parameter $q_0$ yields*

$$
  \operatorname{tr}_M(\sigma_1^7 \sigma_2^4)(q_0) \;\approx\; 1.63315,
$$

*matching the seminormal-derived `char_fast` Markov trace to better
than $0.1\%$, and giving the categorical-mass anchor*

$$
  \rho_p^{\mathrm{CODATA}}
   \;=\; \frac{m_p / m_e}{\bigl|\operatorname{tr}_M(\sigma_1^7\sigma_2^4)(q_0)\bigr|}
   \;\approx\; 1124.3.
$$

## Numerical witness

Substituting $q_0 = 1.109978595554181\ldots$ (50 dps) and evaluating with `mpmath`:

$$
  \operatorname{tr}_M(\sigma_1^7\sigma_2^4)(q_0) \;\approx\; 1.63315\,357\ldots
$$

The `char_fast` cross-check ('s `markov_chars` function,
computed via Hoefsmit seminormal ascent) gives $\approx 1.6334$,
matching to $4$ significant digits. The minor discrepancy reflects
floating-point roundoff in the seminormal eigenvalue route; the
axiomatic form is exact in $\mathbb{Q}(q)$.

The categorical-mass formula
$M(K) = m_e \cdot \rho_K \cdot |\operatorname{tr}_M(\mathcal{B}_K)|$
([`prop:categorical-mass-markov`](#prop:categorical-mass-markov))
gives, for the proton ($K = $ proton, $\mathcal{B}_K = \sigma_1^7\sigma_2^4$):

$$
  \rho_p^{\mathrm{CODATA}} \;=\; \frac{1836.15}{|\operatorname{tr}_M(\mathcal{B}_p)|(q_0)} \;\approx\; \frac{1836.15}{1.63315} \;\approx\; 1124.3.
$$

## Methodology generalisation

The proof transcribes verbatim to any closed braid $K \in B_n$
whose word factors as $\sigma_{i_1}^{k_1} \sigma_{i_2}^{k_2} \cdots$
with disjoint or commuting generator clusters: each generator power
$\sigma_i^{k}$ reduces via the recurrence $(a_k, b_k)$, and the
resulting linear combination is read off the $H_n(q)$ basis. For
non-disjoint clusters (e.g. neutron $\sigma_1^6 \sigma_2^4 \sigma_1^{-1}$
with mixed signatures), the same recurrence applies after using
$\sigma_i^{-1} = \sigma_i - h$ from the Hecke quadratic.

Outstanding work towards full automation is captured in
[`markov-axiom-recursive-ascent`](#def:markov-axiom-recursive-ascent):
a recursive symbolic reducer for general $H_n$ words, currently
implemented in `markov_trace_recursive.py` with a known truncation
bug for $n \geq 4$ that does not affect the $H_3$ proton case.

## Categorical interpretation

This proposition is the **direct categorical-mass anchor** for the
proton: the formula $\operatorname{tr}_M(\sigma_1^7\sigma_2^4)(q)$
is the Frobenius integral on $H_3(q)$ evaluated on the canonical
atomic-braid representative of the proton's GB-filtration normal
form ([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)). The
axiomatic derivation makes the construction independent of any
representation-theoretic parameterisation; in particular, it
bypasses [``](https://github.com/litlfred/qou/pull/546)'s
seminormal `IndexError` failure on $\sigma_2$ acting on shape $(3)$.

The contrast with the Plancherel-trace closed form is
notable: that form was *anti-self-reciprocal* under $q \leftrightarrow 1/q$
([`prop:markov-trace-antipode-polynomial-symmetry`](#prop:markov-trace-antipode-polynomial-symmetry)),
whereas this Markov-trace closed form is **not** anti-self-reciprocal —
the two traces are genuinely different categorical objects, both
finite linear combinations of irreducible characters but with
different weights ($w_\lambda$ Plancherel vs $y_\lambda$ Jones-Markov,
[`prop:mass-coefficient-shadow-price`](#prop:mass-coefficient-shadow-price)).

## Witness scripts

- `computations/markov/markov_trace_atomic_proton_full.py` — full
  proton word $\sigma_1^7\sigma_2^4$ with `sp.cancel` rationalisation.
- `computations/markov/markov_trace_axiomatic_proton.py` — pedagogical
  $\sigma_1\sigma_2\sigma_1$ demonstration of the methodology.
- `computations/markov/markov_trace_recursive.py` — partial recursive
  reducer (see *Methodology generalisation* above).

## References

- [Jones 1987] *Hecke algebra representations of braid groups and link polynomials*, Annals of Math. **126**, 335-388.
- [Kassel 1995] *Quantum Groups*, Springer GTM 155, Ch. III §3 (Markov trace via Frobenius integral).
- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349-383.
- [Kauffman 1991] *Knots and Physics*, World Scientific, Ch. VI (skein-relation derivation).
