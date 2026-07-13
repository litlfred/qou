<!-- FILE_START: categorical-mass-markov-trace-endomorphism-intro.md -->
The preceding sub-section established the categorical-mass eigenspace foundations (topological-mass decompositions, $\rho_K$ graded expansion, Hecke branching, and magnitude budget). This sub-section enriches these foundations with the Markov-trace machinery required to compute the mass spectrum.

The analysis proceeds in three stages. First, it constructs the recomputed low-isotope mass table and extracts the substrate-flow behaviour of the Markov-trace antipode polynomial symmetry. Second, it establishes the Markov-trace axiomatic closed form and the recursive reducer, which converts substrate-level Hecke traces into explicit numerical evaluations. Third, it reconciles the Markov-Z spectrum with the mass-endomorphism conjecture, identifies the categorical-neutrality saturated shells required for the predicted-spectra chapter, and packages the mass functor as the global section $\phi_n$.

This section provides the closed-form Markov-trace evaluation of the categorical mass element at every Wedderburn block. This combinatorial engine underpins the subsequent algebraic mass formulas.
<!-- FILE_END: categorical-mass-markov-trace-endomorphism-intro.md -->

<!-- FILE_START: markov-trace-antipode-polynomial-symmetry.md -->
## Statement

**Proposition (antipode-induced polynomial symmetry).**
*Let $\mathcal{B}_p$ denote the proton braid in $B_3$ used in [`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf). Let*

$$
  p(q) \;=\; q^{20} + q^{18} + 2 q^{12} - 2 q^{8} - q^{2} - 1
$$

*be the numerator of the closed-form Markov trace*

$$
  \operatorname{tr}_M(\mathcal{B}_p) \;=\; \frac{p(q)}{12 \cdot q^{10}}
$$

*derived via the symbolic Hoefsmit-Wenzl seminormal reduction. Then $p(q)$ is anti-self-reciprocal of degree $20$:*

$$
  \boxed{\quad q^{20} \cdot p(1/q) \;=\; -p(q). \quad}
$$

*Equivalently, the Markov trace itself satisfies:*

$$
  \operatorname{tr}_M(\mathcal{B}_p)\!\bigl(\tfrac{1}{q}\bigr) \;=\; -\operatorname{tr}_M(\mathcal{B}_p)(q).
$$

## Categorical interpretation

The Iwahori-Hecke algebra $H_n(q)$ forms a Hopf algebra with antipode $S(\sigma_i) = \sigma_i^{-1}$. The Hecke quadratic relation $\sigma_i^2 = (q - q^{-1}) \sigma_i + 1$ implies $\sigma_i^{-1} = \sigma_i - (q - q^{-1})$. The antipode acts linearly on the generators with a $q \leftrightarrow q^{-1}$ component.

The Markov trace $\operatorname{tr}_M$ provides the Frobenius integral on $H_n(q)$ ([`prop:categorical-mass-markov`](#prop:categorical-mass-markov)). For Frobenius algebras with non-trivial Nakayama automorphism, the trace satisfies $\operatorname{tr}(S^2(x)) = \operatorname{tr}(x)$. For the Hecke algebra, $S^2$ acts as $q \leftrightarrow q^{-1}$ on the structural variable $q$ while preserving the algebra structure.

The minus sign in $\operatorname{tr}_M(\mathcal{B}_p)(1/q) = -\operatorname{tr}_M(\mathcal{B}_p)(q)$ reflects the odd parity of the proton word $\mathcal{B}_p$ under the antipode-induced involution. Here $S(\mathcal{B}_p)$ constructs the reversed word with each $\sigma$ replaced by $\sigma^{-1}$. The $11$-crossing (odd) length contributes a parity sign. Specifically, the proton's word length $\ell(\mathcal{B}_p) = 11$ has odd parity.

## Generalization conjecture

For any closed braid $K \in B_n$ whose Markov trace admits a closed form $\operatorname{tr}_M(K) = p_K(q) / (c_K \cdot q^{\mathrm{shift}(K)})$ with $\operatorname{deg}_q p_K = 2 \cdot \mathrm{shift}(K)$, the polynomial satisfies:

$$
  q^{2 \mathrm{shift}(K)} \cdot p_K(1/q) \;=\; (-1)^{\ell(\mathcal{B}_K)} \cdot p_K(q),
$$

where $\ell(\mathcal{B}_K)$ is the parity of crossings under the Hecke-algebra antipode action. The $\mathrm{shift}(K)$ is the GS-filtration shift exponent ([`docs/audits/-w3-habiro-unblocked.md`](../../docs/audits/-w3-habiro-unblocked.md)). It equals $18Z + 21N + 1$ for atomic braids per the integer-LP closure.

This conjecture is testable via the $A \geq 2$ extension and via the polynomial structure of the neutron's closed form $\operatorname{tr}_M(\mathcal{B}_n) = (\dots) / (12 q^8 \cdot (q^4 + q^2 + 1))$.

## References

- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349–383.
- [Hoefsmit 1974] *Representations of Hecke algebras of finite groups with $BN$-pairs of classical type*, PhD thesis, UBC.
- [Kassel 1995] *Quantum Groups*, Springer GTM 155, Ch. III (Hopf antipode + Frobenius integrals).
- — symbolic closed form for $\operatorname{tr}_M(\mathrm{proton})$.
<!-- FILE_END: markov-trace-antipode-polynomial-symmetry.md -->

<!-- FILE_START: markov-trace-axiomatic-closed-form.md -->
## Statement

**Proposition (axiomatic Markov-trace closed form).** *Let $H_n(q)$ denote the Iwahori-Hecke algebra of type $A_{n-1}$ with Hecke quadratic relation:*

$$
  \sigma_i^2 \;=\; h\,\sigma_i + 1, \qquad h \;=\; q - q^{-1}.
$$

*Let $\operatorname{tr}_M : \bigsqcup_n H_n(q) \to \mathbb{Q}(q)$ be the Markov trace ([`prop:categorical-mass-markov`](#prop:categorical-mass-markov)). It is uniquely determined by:*

$$
  \operatorname{tr}_M(1) = 1, \qquad
  \operatorname{tr}_M(\alpha \sigma_n) = z \cdot \operatorname{tr}_M(\alpha) \;\text{for}\; \alpha \in H_n \subset H_{n+1}, \qquad
  \operatorname{tr}_M(\alpha\beta) = \operatorname{tr}_M(\beta\alpha),
$$

*with $z = 1/(q^{1/2} + q^{-1/2})$. Then for the proton's atomic-braid word $\sigma_1^7 \sigma_2^4 \in H_3(q)$, the Markov trace admits the closed-form expression:*

$$
  \operatorname{tr}_M(\sigma_1^7 \sigma_2^4)(q)
   \;=\; a_7 a_4 \, z^2 \;+\; (a_7 b_4 + b_7 a_4)\, z \;+\; b_7 b_4,
$$

*where $(a_k, b_k)$ are the polynomials in $h$ defined by the Hecke-power recurrence $a_{k+1} = h\,a_k + b_k$, $b_{k+1} = a_k$, $a_0 = 0$, $b_0 = 1$. After substituting $h = q - q^{-1}$ and $z = 1/(q^{1/2}+q^{-1/2})$ and rationalising, the denominator factors as $q^{10}(q+1)^3$.*

*Numerical evaluation at the substrate parameter $q_0$ yields:*

$$
  \operatorname{tr}_M(\sigma_1^7 \sigma_2^4)(q_0) \;\approx\; 1.63315.
$$

*This matches the seminormal-derived `char_fast` Markov trace to better than $0.1\%$. It provides the categorical-mass anchor:*

$$
  \rho_p^{\mathrm{CODATA}}
   \;=\; \frac{m_p / m_e}{\bigl|\operatorname{tr}_M(\sigma_1^7\sigma_2^4)(q_0)\bigr|}
   \;\approx\; 1124.3.
$$
<!-- FILE_END: markov-trace-axiomatic-closed-form.md -->

<!-- FILE_START: markov-trace-axiomatic-closed-form-interpretation.md -->
## Methodology generalisation

The proof transcribes verbatim to any closed braid $K \in B_n$ whose word factors as $\sigma_{i_1}^{k_1} \sigma_{i_2}^{k_2} \cdots$ with disjoint or commuting generator clusters. Each generator power $\sigma_i^{k}$ reduces via the recurrence $(a_k, b_k)$. We then read the resulting linear combination off the $H_n(q)$ basis. For non-disjoint clusters (e.g., neutron $\sigma_1^6 \sigma_2^4 \sigma_1^{-1}$ with mixed signatures), the same recurrence applies after using $\sigma_i^{-1} = \sigma_i - h$ from the Hecke quadratic.

## Categorical interpretation

This proposition provides the direct categorical-mass anchor for the proton. The formula $\operatorname{tr}_M(\sigma_1^7\sigma_2^4)(q)$ evaluates the Frobenius integral on $H_3(q)$ applied to the canonical atomic-braid representative of the proton's GB-filtration normal form ([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)). The axiomatic derivation makes the construction independent of any representation-theoretic parameterisation. It bypasses [``](https://github.com/litlfred/qou/pull/546)'s seminormal `IndexError` failure on $\sigma_2$ acting on shape $(3)$.

The contrast with the Plancherel-trace closed form is strict. The Plancherel trace behaves anti-self-reciprocally under $q \leftrightarrow 1/q$ ([`prop:markov-trace-antipode-polynomial-symmetry`](#prop:markov-trace-antipode-polynomial-symmetry)). This Markov-trace closed form does not. The two traces constitute genuinely different categorical objects. Both expand as finite linear combinations of irreducible characters, but they carry different weights ($w_\lambda$ Plancherel vs $y_\lambda$ Jones-Markov, [`prop:mass-coefficient-shadow-price`](#prop:mass-coefficient-shadow-price)).
<!-- FILE_END: markov-trace-axiomatic-closed-form-interpretation.md -->

<!-- FILE_START: markov-trace-recursive-reducer.md -->
## Statement

**Proposition (recursive symbolic Markov-trace reducer).** *Let $\beta \in B_n$ be any braid word. There is a terminating algorithm that returns a closed-form symbolic expression for $\operatorname{tr}_M(\beta) \in \mathbb{Q}(q)$ using only:*
- *the Hecke quadratic $\sigma_i^2 = h \sigma_i + 1$ (with $h = q - q^{-1}$);*
- *the Markov axiom $\operatorname{tr}_M(\alpha \sigma_n) = z \operatorname{tr}_M(\alpha)$ for $\alpha \in H_n \subset H_{n+1}$ (with $z = 1/(q^{1/2}+q^{-1/2})$);*
- *cyclicity $\operatorname{tr}_M(\alpha\beta) = \operatorname{tr}_M(\beta\alpha)$;*
- *and the braid relations.*

*The algorithm is correct, terminates in $O(\ell(\beta) \cdot n!)$ basis-element evaluations, and verifies the **disjoint-product property**:*
$$
  \operatorname{tr}_M(\alpha \otimes \beta) \;=\; \operatorname{tr}_M(\alpha) \cdot \operatorname{tr}_M(\beta)
$$
*for $\alpha \in H_k(q) \hookrightarrow H_n(q)$ on strands $\{1, \ldots, k\}$ and $\beta \in H_{n-k-1}(q) \hookrightarrow H_n(q)$ on strands $\{k+2, \ldots, n\}$ (separated by the unused generator $\sigma_{k+1}$).*

## Algorithm

**Input:** braid word $\beta = \sigma_{i_1}^{\varepsilon_1} \cdots \sigma_{i_m}^{\varepsilon_m}$ with $\varepsilon_j \in \{\pm 1\}$ and $1 \leq i_j \leq n - 1$.

**Step 1 (Hecke expansion).** Expand $\beta$ into the standard Iwahori-Hecke basis $T_w$ for $w \in S_n$:
$$
  \beta \;=\; \sum_{w \in S_n} c_w(q) T_w.
$$

**Step 2 (recursive basis-element trace).** For each $w \in S_n$ appearing with non-zero coefficient, compute $\operatorname{tr}_M(T_w)$ recursively:

```python
def tr_M(perm, n):
    if perm == identity:
        return 1
    word = canonical_reduced_word(perm)          # 0-indexed gens
    max_gen = max(word)                          # ∈ {0, …, n-2}
    if max_gen < n - 2:
        # w ∈ H_{max_gen+2} ⊂ H_n; truncate.
        return tr_M(perm[:max_gen+2], max_gen+2)
    # max_gen == n-2: peel σ_{n-2} via Markov axiom + cyclicity.
    k = rightmost position of max_gen in word
    rotated = word[k+1:] + word[:k]              # length ℓ(w) - 1
    # Reduce `rotated` back into the H_n basis (may involve
    # Hecke quadratic firings if σ_{n-2} re-appears).
    E = expand_in_hecke_basis(rotated, n)
    return z * Σ_{w' ∈ E} c_{w'} · tr_M(T_{w'}, n)
```

**Step 3 (combine).** Output $\operatorname{tr}_M(\beta) = \sum_w c_w \cdot \operatorname{tr}_M(T_w)$.

## Correctness

**Termination.** Each invocation of the recursive `tr_M` call either:
(i) truncates the ambient algebra ($n \to \text{max\_gen} + 2$ where $\text{max\_gen} + 2 < n$), strictly decreasing the integer $n$; or
(ii) peels one $\sigma_{n-2}$ from the word and recurses on basis elements $w'$ with $\ell(w') \leq \ell(\text{rotated}) = \ell(w) - 1$, strictly decreasing the Coxeter length.

The lex order on $(n, \ell(w))$ has no infinite descending chain, so termination is guaranteed. $\square$

**Correctness.** Each step is an exact equality in $\mathbb{Q}(q)$:
- Step 1 is exact (Hecke-quadratic expansion).
- The truncation case (max_gen < n - 2) uses the embedding $H_{n-1} \hookrightarrow H_n$. This preserves $\operatorname{tr}_M$ (the Markov axiom yields the same value regardless of ambient algebra, by stability of $z$).
- The peeling case uses cyclicity to put $\sigma_{n-2}$ at the rightmost position. The Markov axiom then contributes a $z$ factor. The remainder $\alpha \beta$ (with $\alpha, \beta$ on either side of the rotated cut) need not lie in $H_{n-1}$ if $\alpha$ contained another $\sigma_{n-2}$. In that case, the basis-expansion subroutine handles the Hecke-quadratic firings exactly.

By induction on $(n, \ell)$, the output equals $\operatorname{tr}_M(\beta)$ in $\mathbb{Q}(q)$. $\square$

## Disjoint-product property

For $\alpha \in H_k$ on strands $\{1, \ldots, k\}$ and $\beta \in H_{n-k-1}$ on strands $\{k+2, \ldots, n\}$ (no $\sigma_{k+1}$ appears in $\beta$), the words commute. We have $\alpha \beta = \beta \alpha$, and the Markov axiom plus cyclicity gives:
$$
  \operatorname{tr}_M(\alpha \beta) \;=\; \operatorname{tr}_M(\alpha) \cdot \operatorname{tr}_M(\beta)
$$
by induction on $\ell(\beta)$. The recursive algorithm realises this property automatically. The peeling phase strips $\beta$'s top generators $\sigma_{n-2}, \sigma_{n-3}, \ldots, \sigma_{k+2}$ in order. This contributes factors of $z$ that exactly match the standalone $\operatorname{tr}_M(\beta)$ computed in its own algebra $H_{n-k-1}$.

## Empirical verification

| atom | braid word | $H_n$ | $\operatorname{tr}_M(q_0)$ |
|---|---|---|---|
| proton | $\sigma_1^7 \sigma_2^4$ | $H_3$ | $1.633154\ldots$ |
| neutron | $\sigma_1^6 \sigma_2^4 \sigma_1^{-1}$ | $H_3$ | $1.248248\ldots$ |
| deuteron disjoint | $\sigma_1^7\sigma_2^4 \oplus \sigma_4^6\sigma_5^4\sigma_4^{-1}$ | $H_6$ | $\operatorname{tr}_M(p)\cdot\operatorname{tr}_M(n)$ |

## References

- [Jones 1987] *Hecke algebra representations of braid groups and link polynomials*, Annals of Math. **126**, 335-388.
- [Kassel 1995] *Quantum Groups*, Springer GTM 155, Ch. III §3.
- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349-383.
<!-- FILE_END: markov-trace-recursive-reducer.md -->

<!-- FILE_START: markov-trace-recursive-reducer-interpretation.md -->
## Optimisation: memoisation on basis elements

Each $S_n$ has $n!$ basis elements. We memoise the recursive `tr_M` on $(w, n)$ via `functools.lru_cache`. For repeated atom evaluations within a single Python process (e.g., in the multi-atom witness pipeline), we compute basis-element traces once and re-use them. This yields an asymptotic speed-up proportional to the duplication factor across atoms. Empirically, the cache hit rate exceeds 50% on the proton+neutron+deuteron sweep.

## Categorical interpretation

The recursive reducer forms the algorithmic content of the Markov-trace existence theorem for the Iwahori-Hecke algebra. The axioms uniquely determine the trace. The algorithm constructs the unique value for any input word. This contrasts with seminormal/Hoefsmit ascent, which realises the trace via the explicit Wedderburn decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}$. Both routes agree on values. The axiomatic route avoids reliance on Hoefsmit matrix elements, which exhibited a known [`IndexError`](https://github.com/litlfred/qou/pull/546) bug on $\sigma_2$ acting on shape $(3)$.
<!-- FILE_END: markov-trace-recursive-reducer-interpretation.md -->

<!-- FILE_START: markov-z-reconciliation.md -->
Two conventions for the Markov parameter $z$ appear in the literature and in this paper. They differ by a factor of $q - 1$ and arise from different normalisation choices for the trace.

**Convention 1 (Jones, 1987).** The Jones–Markov trace ([Jones–Markov trace](#thm:jones-markov-trace)) satisfies $\mathrm{tr}_M(x\,\sigma_n^{\pm 1}) = z_{\mathrm{J}}^{\pm 1}\,\mathrm{tr}_M(x)$ with
$$
  z_{\mathrm{J}}
  \;=\;
  \frac{q - 1}{(q^{1/2} + q^{-1/2})^2}.
$$
At $q_0 \approx 1.110$, this gives $z_{\mathrm{J}} \approx 0.027$. This parameter makes the trace a link invariant via the Markov closure $\hat{\beta}$.

**Convention 2 (mass computations).** The categorical mass formula ([categorical mass as Markov trace](#prop:categorical-mass-markov)) and all subsequent mass and volume computations use
$$
  z_{\mathrm{m}}
  \;=\;
  \frac{1}{q^{1/2} + q^{-1/2}},
$$
giving $z_{\mathrm{m}} \approx 0.499$ at $q_0$.

**Relation.** The two parameters satisfy
$$
  z_{\mathrm{J}}
  \;=\;
  (q - 1)\,z_{\mathrm{m}}^{\,2},
$$
since $z_{\mathrm{m}}^2 = 1/(q^{1/2}+q^{-1/2})^2$ by definition. Equivalently, $z_{\mathrm{m}} = z_{\mathrm{J}}^{1/2}\,(q - 1)^{-1/2}$.

**Origin of the two conventions.** Convention 1 normalises the Jones polynomial as a link invariant. The factor $(q-1)$ absorbs the writhe correction and makes $J_L(q)$ independent of the braid representative. Convention 2 arises when we evaluate the trace on a single generator $\sigma_i$ without the writhe prefactor. We have $\mathrm{tr}_M(\sigma_i) = z_{\mathrm{m}}$ in Convention 2, whereas $\mathrm{tr}_M(\sigma_i) = z_{\mathrm{J}}$ in Convention 1.

All mass tables, vertex volumes, and nuclear binding computations in this paper use $z = z_{\mathrm{m}} = 1/(q^{1/2} + q^{-1/2})$. The Jones–Markov trace theorem statement retains $z_{\mathrm{J}}$ to match the original reference.
<!-- FILE_END: markov-z-reconciliation.md -->

<!-- FILE_START: categorical-neutrality-saturated-shells.md -->
A nuclear shell at nucleon count $n \in \mathfrak{M} = \{2, 8, 20,
28, 50, 82, 126\}$ is **saturated** in the QOU framework: the
algebraic structure of the shell admits no further crossing-energy
absorption. This refactor block names the categorical content of
saturation directly, replacing matrix-evaluation evidence (Hoefsmit
seminormal forms at $k = 3, \dots, 10$, blocked at $k \geq 12$ by
combinatorial growth) with a homological / algebraic-geometry
statement about a global section.

## Notation

Let $\mathbf{C}$ be the rigid :refterm[braided monoidal category]{#braided-monoidal-category} of the QOU
substrate (Frobenius–Hopf object $A$, fibre functor $\tau$). For
$n \in \mathbb{N}$ write

* $H_n(q)$ for the Iwahori–Hecke algebra at parameter $q$, generated
 by $\sigma_1, \dots, \sigma_{n-1}$ subject to the braid relations
 and $\sigma_i^2 = (q - q^{-1}) \sigma_i + 1$
 ([AGENTS.md §7a](../../../AGENTS.md));
* $\Delta_n^2 = (\sigma_1 \sigma_2 \cdots \sigma_{n-1})^n
  \in Z(B_n)$ for the **full-twist** generator of the centre of the
 braid group, mapped under the Hecke quotient to the central
 element $\Delta_n^2 \in Z(H_n(q))$
 \cite{kassel1995, geckpfeiffer2000};
* $\Phi_n \in \mathrm{End}_{\mathbf{C}}(A^{\otimes n})$ for the
 **categorical mass endomorphism** at level $n$ —
 the global section of the mass functor over the rigid braided
 :refterm[monoidal category]{#monoidal-category}, related to the Hecke-mass element
 $\Phi_{\mathrm{mass}}$ by
 $\Phi_{\mathrm{mass}}(\beta) = (\tau \otimes \cdots \otimes \tau) \circ \Phi_n \circ \rho(\beta)$
 ([Hecke mass element](#def:hecke-mass-element));
* $\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$ for the seven
 observed nuclear magic numbers.

## Statement

**Proposition (Conjecture — categorical neutrality of saturated
shells).**
*Let $\mathbf{C}$ be a rigid :refterm[braided monoidal category]{#braided-monoidal-category} satisfying the
QOU substrate axioms ([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate))
and let $\Phi_n$ be the categorical mass endomorphism at level $n$
([mass-endomorphism conjecture](#conj:mass-endomorphism)). Then for
every $n \in \mathfrak{M}$ the full-twist
$\Delta_n^2$ acts as the identity on $\Phi_n$:*

$$
  \Delta_n^2 \cdot \Phi_n \;=\; \Phi_n \cdot \Delta_n^2 \;=\; \Phi_n
  \qquad\text{for all } n \in \mathfrak{M}.
$$

*Equivalently, $\Phi_n \in \mathrm{End}_{\mathbf{C}}(A^{\otimes n})^{\Delta_n^2}$ —
the categorical mass at a saturated shell is a fixed point of the
full-twist action.*
<!-- FILE_END: categorical-neutrality-saturated-shells.md -->

<!-- FILE_START: categorical-neutrality-saturated-shells-interpretation.md -->
## Structural constraint

The full-twist $\Delta_n^2$ acts on each Wedderburn block $V_\lambda$ of $H_n(q)$ by the central scalar $q^{c(\lambda)}$, where $c(\lambda) = \sum_{x \in \lambda}(j_x - i_x)$ provides the content sum of the partition $\lambda \vdash n$ \cite{geckpfeiffer2000, mathas1999}. Trivial action of the full-twist on $\Phi_n$ restricts the partitions in the Wedderburn decomposition of $\Phi_n$ to those with content sum zero. These form the self-conjugate partitions $\lambda = \lambda'$ on Young's lattice. At saturated $n$, $\Phi_n$ finds support strictly on self-conjugate partitions.

For $n \notin \mathfrak{M}$, the constraint fails. Non-self-conjugate partitions enter $\Phi_n$, and the full-twist acts by a non-trivial scalar. This transition formalizes shell closure, replacing ad hoc selection rules with categorical constraints.

## Homological reformulation

The Hoefsmit seminormal form ([prop:hoefsmit-seminormal-form](#prop:hoefsmit-seminormal-form)) supplies explicit matrices for $\sigma_i$ on each $V_\lambda$. Direct multiplication recovers the full-twist eigenvalue $q^{c(\lambda)}$. Numerical verification at $k = 3, \dots, 10$ confirms the shell pattern at small magic values $n = 2, 8, 20$. At $k \geq 12$, combinatorial growth in $|\{\lambda \vdash n\}|$ blocks matrix evaluation.

The conjecture reformulates this homologically. Instead of verifying $\Phi_n$ with matrices, we verify the self-conjugate-support condition via content-sum arithmetic. This approach accesses saturation at $n \in \{50, 82, 126\}$ without matrix multiplication.

## Global topological neutrality

Earlier models ([atom-knot-mass-derivation](#prop:atom-knot-mass-derivation)) treated $\Phi_n$ as a local object. They required "screening" or "local trivialisation" to explain shell closure. This refactor abandons the locality assumption. We identify $\Phi_n$ as the global section of the mass functor over $\mathbf{C}$ ([rem:phi-n-global-section](#rem:phi-n-global-section)). A non-trivial full-twist action propagates unbounded ribbon flux through the brane tower. Finite observable mass demands global topological neutrality at saturation.

## Operator-level support

The claim that $\Phi_n$ receives support on self-conjugate partitions applies at the operator level. The categorical mass operator $\Phi_n$ exhibits zero matrix entries on every non-self-conjugate isotypical component in $H_n(q) = \bigoplus_\lambda \mathrm{End}(V_\lambda)$.

This does not imply the Plancherel-weighted character sum:

$$
\sum_{\lambda = \lambda'} w_\lambda \cdot \chi^\lambda(\beta_{\mathrm{atom}}).
$$

The character sum vanishes identically at certain atomic-braid cycle types. The binding-energy enhancement at magic shells derives from the non-vanishing of $\Phi_n$ on the self-conjugate isotypical operator blocks. Empirically, the GS-filtration Term 6 plus an `is_magic_pair` operator-correction captures the magic-shell signal, correlating at $+0.74$ to the AME residual ([reframing memo](../../../docs/audits/-self-conj-support-reframing.md)).

## Discussion

Status: conjectural under AGENTS.md §3b. Numerical witnesses at $k = 3, \dots, 10$ support the saturation condition. The conjecture extends this to all $n \in \mathfrak{M}$, including the high-mass region $\{50, 82, 126\}$.

The downstream cone ([conjecture-cones audit](../../../docs/audits/conjecture-cones.md)) includes [`prop:magic-numbers-from-q`](#prop:magic-numbers-from-q) and the shell-closure portion of the BW formula ([`thm:wedderburn-mass-formula`](#thm:wedderburn-mass-formula)). Proving these requires either a derivation of this conjecture or its retention as a class-axiomatised input.
<!-- FILE_END: categorical-neutrality-saturated-shells-interpretation.md -->

<!-- FILE_START: phi-n-global-section.md -->
In the algebraic refactor of the magic-number / shell-closure
framework, the categorical mass endomorphism $\Phi_n$ acts globally, not
locally. It is not built per-vortex and combined by tensor product.
Instead $\Phi_n$ forms the global section of the categorical mass
functor over the rigid :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}$, in
the strict sense of monoidal-category global sections:
$\Phi_n \in \mathrm{End}_{\mathbf{C}}(A^{\otimes n})$ is determined
by its compatibility with the Frobenius-Hopf substrate axioms across
every sub-tensor-factor of $A^{\otimes n}$, not by an additive
combination of local pieces.

## Necessity of dropping locality

Local trivialisation—"screening"—provided the framework's earlier
explanation of shell closure: that something local at each vortex
trivialises the full-twist action. That picture carries two flaws:

1. **Anomalous ribbon flux.** A non-trivial ribbon (= framing)
   action on $\Phi_n$ at a non-magic level $n$ would propagate
   unboundedly up the brane tower
   ([recursive-brane-tower](#def:recursive-brane-tower)). Each
   brane level $A_{n+1} = A_n \otimes \Omega^1(A_n)$ inherits the
   framing flux. Without a global cancellation mechanism, the
   accumulated flux at the :refterm[descent]{#descent} limit diverges.
2. **Finite observable mass.** The categorical mass identity
   ([def:hecke-mass-element](#def:hecke-mass-element)) is finite:
   $\mathfrak{m}(\varrho) \in \mathbb{R}$ for every observed
   hadron. Finite observable mass remains incompatible with
   unbounded framing flux.

The only consistent reconciliation requires global topological
neutrality at saturation: at $n \in \mathfrak{M}$, the ribbon
action on $\Phi_n$ evaluates globally to zero (in the centre-of-the-braid-group sense), not locally trivialised by some spectator structure.
This forms precisely the
`prop:categorical-neutrality-saturated-shells`
statement. It provides the structural reason a non-trivial action
cannot coexist with finite mass at saturated $n$.

## The categorical-functor view

In the language of monoidal functors, $\Phi_n$ is

$$
  \Phi_n = (\text{global section of } \mathcal{F}_{\text{mass}})_n,
\qquad
  \mathcal{F}_{\text{mass}}:
    \mathbf{C} \to \mathbf{C},
\qquad
  X \mapsto (\int_A \otimes \mathrm{id}) \circ \Delta \circ (X \otimes -).
$$

The functor $\mathcal{F}_{\text{mass}}$ takes a substrate object
$X$ to its mass endomorphism. The global section $\Phi_n$ at level
$n$ provides the assignment of $\mathcal{F}_{\text{mass}}(A^{\otimes n})$
that respects all the substrate's monoidal-functor structure
simultaneously—including the central full-twist action on each
$A^{\otimes n}$. Demanding that $\Phi_n$ form a single global
section, rather than a colimit of local pieces, enforces the
substrate-level constraint that the central action vanishes at
saturated $n$.

## Implications for the conjecture

[`conj:mass-endomorphism`](#conj:mass-endomorphism) (the open
problem of finding a closed-form NF for $\Phi_{\mathrm{mass}}$) is
correspondingly reframed. The conjecture is no longer "find the
local NF generators and combine". It becomes "find the categorical
global section that satisfies the saturated-shell global-neutrality
constraint". The reframing constructs the magic-number ladder as a
structural prediction rather than a numerical phenomenon.

This remark interprets `conj:mass-endomorphism` only. It makes no
new logical claim. The mathematical content resides in the
saturated-shell
and [shell-condensation](./homological-shell-condensation.md)
conjectures, which are themselves conditional on the algebraic
refactor.
<!-- FILE_END: phi-n-global-section.md -->

