**Proposition (closed form for the canonical Markov trace of $\sigma_1^2$).**

*Let $H_n(q)$ be the Iwahori–Hecke algebra of type $A_{n-1}$ over $\mathbb{Q}(q^{1/2})$. Let $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Q}(q^{1/2})$ be the canonical Markov trace ([`thm:jones-markov-trace`](#thm:jones-markov-trace)). For every $n \geq 2$:*

$$
\boxed{\quad
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; \frac{q^{5/2} - q^{1/2} + q^2 + q}{q^2 + q}
  \;=\; 1 + \frac{q - 1}{q^{1/2}}.
\quad}
$$

*This value is independent of $n$ by Markov invariance under stabilisation. The closure $\widehat{\sigma_1^2}$ is the positive Hopf link $L_+^{\mathrm{Hopf}}$.*

## Implication for the $\mathfrak{Q}_\beta$ precision-ladder

The $\mathfrak{Q}_\beta$ factorisation ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)) writes
$$
  \mathfrak{Q}_\beta \;=\; Q_A \cdot \cos\bigl(\alpha - b\hbar_q^2/2\bigr)
              \cdot \prod_{n \geq 2} (1 + c_n \hbar_q^{2n})
$$
with claimed coefficients $c_2 = b^2$, $c_3 = -2 b^3$, and $c_4 = b^2 + 1/2$. The bare-Markov $\varepsilon^{2n}$ coefficients of $\mathrm{tr}_M(\sigma_1^2) - 1$ do not equal these, as shown in [Table 2](#tbl:trm-hopf-sigma1-sq-closed-form-table2-data).

This mismatch proves the $F_n := 1 + c_n \hbar_q^{2n}$ factors are not extracted from the bare Markov trace of $\sigma_1^2$. They form a separate decomposition of $\mathfrak{Q}_\beta$. Each factor must arise from a distinct categorical object $\mathcal{B}_n$. For $F_3$ specifically, this is the $V_{(2,2,2)}$ Wedderburn-block projection inside the Hoefsmit $V_{(2,1)} \otimes V_{(2,1)}$ embedded in $H_6$ (locked behind the conditional class `QbetaC3StructuralFormClass`; see [`docs/audits/2026-05-31-ck-exploratory-probes-removed.md`](../../../docs/audits/2026-05-31-ck-exploratory-probes-removed.md)).

## Remarks

1. The closed form $1 + (q-1) q^{-1/2}$ is the simplest nontrivial Markov-trace value in the framework. It serves as a sanity check for canonical-Markov implementations ([`markov_peel.tr_M_atomic`](computations/markov/markov_peel.py), [`markov_weights_symbolic.tr_M_canonical`](computations/markov/markov_weights_symbolic.py), [`markov_trace_canonical.tr_M_word`](computations/markov/markov_trace_canonical.py)). All produce identical output for $\sigma_1^2$ at $q = q_0$ to 50 dps.
2. The binomial-coefficient closed form for the Taylor expansion is a special case of the identity $\mathrm{tr}_M(\sigma_1^k) - z^{k-1} = \mathrm{poly}_k(q) \cdot q^{-(k-1)/2}$ for $k \geq 1$, derived by iterating the Hecke quadratic relation.
3. The Markov-invariance of $\mathrm{tr}_M(\sigma_1^2)$ across $H_n$ for $n \geq 2$ is consistent with the Markov property ([`thm:jones-markov-trace`](#thm:jones-markov-trace)) and holds empirically across $H_3, H_4, H_5, H_6$.
4. **Lean realisation.** The algebraic identity holds over the formal field $\mathbb{Q}(q^{1/2})$ without ordering or analytic hypotheses. The Lean formalisation `QOU.Braiding.TrMHopfSigma1SqClosedForm` realises it on the archimedean side by specialising $q$ to $\mathbb{R}$ in the Wenzl positivity regime $q > 1$. The identity is discharged by the substitution $u := \sqrt{q}$ under $u > 0$. The underlying identity remains substrate-side and base-ring-agnostic.
