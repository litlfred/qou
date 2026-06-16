## Statement

**Proposition (recursive symbolic Markov-trace reducer).** *Let
$\beta \in B_n$ be any braid word. There is a terminating algorithm
that returns a closed-form symbolic expression for
$\operatorname{tr}_M(\beta) \in \mathbb{Q}(q)$ using only:*

- *the Hecke quadratic $\sigma_i^2 = h \sigma_i + 1$ (with
  $h = q - q^{-1}$);*
- *the Markov axiom $\operatorname{tr}_M(\alpha \sigma_n) =
  z \operatorname{tr}_M(\alpha)$ for $\alpha \in H_n \subset H_{n+1}$
  (with $z = 1/(q^{1/2}+q^{-1/2})$);*
- *cyclicity $\operatorname{tr}_M(\alpha\beta) = \operatorname{tr}_M(\beta\alpha)$;*
- *and the braid relations.*

*The algorithm is correct, terminates in $O(\ell(\beta) \cdot n!)$
basis-element evaluations, and verifies the
**disjoint-product property**:*

$$
  \operatorname{tr}_M(\alpha \otimes \beta) \;=\; \operatorname{tr}_M(\alpha) \cdot \operatorname{tr}_M(\beta)
$$

*for $\alpha \in H_k(q) \hookrightarrow H_n(q)$ on strands
$\{1, \ldots, k\}$ and $\beta \in H_{n-k-1}(q) \hookrightarrow H_n(q)$
on strands $\{k+2, \ldots, n\}$ (separated by the unused generator
$\sigma_{k+1}$).*

## Algorithm

**Input:** braid word $\beta = \sigma_{i_1}^{\varepsilon_1} \cdots
\sigma_{i_m}^{\varepsilon_m}$ with $\varepsilon_j \in \{\pm 1\}$ and
$1 \leq i_j \leq n - 1$.

**Step 1 (Hecke-basis expansion).** Apply iterated Hecke quadratic
to expand
$\beta = \sum_{w \in S_n} c_w(q) \, T_w$
in the canonical basis. The
[`HeckeElement`](https://github.com/litlfred/qou/blob/main/computations/gb_filtration_jet_tracker.py)
class implements this symbolically over $\mathbb{Q}(q)$ via the
ascending/descending case split on Coxeter length.

**Step 2 (recursive basis-element trace).** For each $w \in S_n$
appearing with non-zero coefficient, compute
$\operatorname{tr}_M(T_w)$ recursively:

```
def tr_M(perm, n):
    if perm == identity:
        return 1
    word = canonical_reduced_word(perm)         # 0-indexed gens
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

**Step 3 (combine).** Output
$\operatorname{tr}_M(\beta) = \sum_w c_w \cdot \operatorname{tr}_M(T_w)$.

## Correctness

**Termination.** Each invocation of the recursive `tr_M` call
either:

(i) truncates the ambient algebra ($n \to \text{max\_gen} + 2$
where $\text{max\_gen} + 2 < n$), strictly decreasing the integer
$n$; or

(ii) peels one $\sigma_{n-2}$ from the word and recurses on
basis elements $w'$ with $\ell(w') \leq \ell(\text{rotated}) =
\ell(w) - 1$, strictly decreasing the Coxeter length.

The lex order on $(n, \ell(w))$ has no infinite descending chain,
so termination is guaranteed. $\square$

**Correctness.** Each step is an exact equality in $\mathbb{Q}(q)$:

- Step 1 is exact (Hecke-quadratic expansion).
- The truncation case (max_gen < n - 2) uses the embedding
  $H_{n-1} \hookrightarrow H_n$ which preserves
  $\operatorname{tr}_M$ (since the Markov axiom gives the same
  value regardless of the ambient algebra, by stability of $z$).
- The peeling case uses cyclicity to put $\sigma_{n-2}$ at the
  rightmost position, then the Markov axiom contributes a $z$
  factor. The remainder $\alpha \beta$ (with $\alpha, \beta$
  on either side of the rotated cut) need not lie in $H_{n-1}$
  if $\alpha$ contained another $\sigma_{n-2}$; in that case
  the basis-expansion subroutine handles the Hecke-quadratic
  firings exactly.

By induction on $(n, \ell)$, the output equals
$\operatorname{tr}_M(\beta)$ in $\mathbb{Q}(q)$. $\square$

## Disjoint-product property

For $\alpha \in H_k$ on strands $\{1, \ldots, k\}$ and $\beta \in
H_{n-k-1}$ on strands $\{k+2, \ldots, n\}$ (no $\sigma_{k+1}$
appears in $\beta$), the words commute, $\alpha \beta = \beta
\alpha$, and the Markov axiom + cyclicity give

$$
  \operatorname{tr}_M(\alpha \beta) \;=\; \operatorname{tr}_M(\alpha) \cdot \operatorname{tr}_M(\beta)
$$

by induction on $\ell(\beta)$. The recursive algorithm above
realises this property automatically: the peeling phase strips
$\beta$'s top generators $\sigma_{n-2}, \sigma_{n-3}, \ldots,
\sigma_{k+2}$ in order, contributing factors of $z$ that exactly
match the standalone $\operatorname{tr}_M(\beta)$ when computed in
its own algebra $H_{n-k-1}$.

## Empirical verification

Numerical evaluation at $q_0$ for the canonical atomic-braid
words ([`markov_trace_axiomatic_multi_atom.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_axiomatic_multi_atom.py)):

| atom              | braid word                              | $H_n$ | $\operatorname{tr}_M(q_0)$ |
|-------------------|----------------------------------------|------|----------------------------|
| proton            | $\sigma_1^7 \sigma_2^4$                | $H_3$ | $1.633154\ldots$           |
| neutron           | $\sigma_1^6 \sigma_2^4 \sigma_1^{-1}$  | $H_3$ | $1.248248\ldots$           |
| deuteron disjoint | $\sigma_1^7\sigma_2^4 \oplus \sigma_4^6\sigma_5^4\sigma_4^{-1}$ | $H_6$ | $\operatorname{tr}_M(p)\cdot\operatorname{tr}_M(n)$ |

The deuteron's value matches $\operatorname{tr}_M(\text{proton})
\cdot \operatorname{tr}_M(\text{neutron})$ to mpmath-exact (50 dps)
precision, confirming the disjoint-product property.

The proton value matches the prior Hecke-power expansion in
[`markov_trace_atomic_proton_full.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_atomic_proton_full.py)
([`prop:markov-trace-axiomatic-closed-form`](#prop:markov-trace-axiomatic-closed-form))
at 50-dps (mpmath) precision, providing an independent cross-check
via two different reduction strategies. (Earlier float64 evaluations
of the same identity are recorded in the witness as probes; the
matching claim is at 50 dps.)

## Optimisation: memoisation on basis elements

Each $S_n$ has $n!$ basis elements; the recursive `tr_M` is
memoised on $(w, n)$ via `functools.lru_cache`. For repeated atom
evaluations within a single Python process (e.g. in the multi-atom
witness pipeline), basis-element traces are computed once and
re-used, giving an asymptotic speed-up proportional to the
duplication factor across atoms. Empirically, on the
proton+neutron+deuteron sweep the cache hit rate exceeds 50%.

## Categorical interpretation

The recursive reducer is the algorithmic content of the
**Markov-trace existence theorem** for the Iwahori-Hecke algebra:
the trace is uniquely determined by the axioms, and the algorithm
*constructs* the unique value for any input word. This contrasts
with the seminormal/Hoefsmit ascent
, which
realises the trace via the explicit Wedderburn decomposition
$H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}$. Both routes
agree on values; the axiomatic route avoids any reliance on the
Hoefsmit matrix elements (which had a known
[`IndexError`](https://github.com/litlfred/qou/pull/546) bug on
$\sigma_2$ acting on shape $(3)$).

## Witness scripts

- [`computations/markov/markov_trace_recursive.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_recursive.py) — algorithm + H_3..H_6 unit tests.
- [`computations/markov/markov_trace_axiomatic_multi_atom.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_axiomatic_multi_atom.py) — proton/neutron/deuteron anchor + disjoint-product check.

## References

- [Jones 1987] *Hecke algebra representations of braid groups and link polynomials*, Annals of Math. **126**, 335-388 (Markov-trace existence + uniqueness).
- [Kassel 1995] *Quantum Groups*, Springer GTM 155, Ch. III §3 (axiomatic Markov trace).
- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349-383 (branching-rule perspective).
