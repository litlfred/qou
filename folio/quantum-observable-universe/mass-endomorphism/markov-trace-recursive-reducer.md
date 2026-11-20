## Statement

*Let $\beta \in B_n$ be any braid word. There is a terminating algorithm that returns a closed-form symbolic expression for $\mathrm{tr}_M(\beta) \in \mathbb{Q}(q)$ using only:*
- *the Hecke quadratic $\sigma_i^2 = h \sigma_i + 1$ (with $h = q - q^{-1}$);*
- *the Markov axiom $\mathrm{tr}_M(\alpha \sigma_n) = z \mathrm{tr}_M(\alpha)$ for $\alpha \in H_n \subset H_{n+1}$, for the Markov parameter $z$;*
- *cyclicity $\mathrm{tr}_M(\alpha\beta) = \mathrm{tr}_M(\beta\alpha)$;*
- *and the braid relations.*

*The algorithm is correct, terminates in $O(\ell(\beta) \cdot n!)$ basis-element evaluations, and verifies the **disjoint-product property**:*
$$
  \mathrm{tr}_M(\alpha \otimes \beta) \;=\; \mathrm{tr}_M(\alpha) \cdot \mathrm{tr}_M(\beta)
$$
*for $\alpha \in H_k(q) \hookrightarrow H_n(q)$ on strands $\{1, \ldots, k\}$ and $\beta \in H_{n-k-1}(q) \hookrightarrow H_n(q)$ on strands $\{k+2, \ldots, n\}$ (separated by the unused generator $\sigma_{k+1}$).*

The algorithm and its correctness are **parametric in $z$**: no step below
evaluates the Markov parameter, so the statement holds for whatever value the
Markov axiom is given. Production evaluates it at $z = q^{3}/(q^{2}+1)$. This is
worth stating explicitly because the statement previously fixed $z$ to
$1/(q^{1/2}+q^{-1/2})$ inside a claim that never used it, which made a
convention choice look like a hypothesis of the theorem.

## Proof — the algorithm

**Input:** braid word $\beta = \sigma_{i_1}^{\varepsilon_1} \cdots \sigma_{i_m}^{\varepsilon_m}$ with $\varepsilon_j \in \{\pm 1\}$ and $1 \leq i_j \leq n - 1$.

**Step 1 (Hecke expansion).** Expand $\beta$ into the standard Iwahori-Hecke basis $T_w$ for $w \in S_n$:
$$
  \beta \;=\; \sum_{w \in S_n} c_w(q) T_w.
$$

**Step 2 (recursive basis-element trace).** For each $w \in S_n$ appearing with non-zero coefficient, compute $\mathrm{tr}_M(T_w)$ recursively:

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

**Step 3 (combine).** Output $\mathrm{tr}_M(\beta) = \sum_w c_w \cdot \mathrm{tr}_M(T_w)$.

## Correctness

**Termination.** Each invocation of the recursive `tr_M` call either:
(i) truncates the ambient algebra ($n \to \text{max\_gen} + 2$ where $\text{max\_gen} + 2 < n$), strictly decreasing the integer $n$; or
(ii) peels one $\sigma_{n-2}$ from the word and recurses on basis elements $w'$ with $\ell(w') \leq \ell(\text{rotated}) = \ell(w) - 1$, strictly decreasing the Coxeter length.

The lex order on $(n, \ell(w))$ has no infinite descending chain, so termination is guaranteed. $\square$

**Correctness.** Each step is an exact equality in $\mathbb{Q}(q)$:
- Step 1 is exact (Hecke-quadratic expansion).
- The truncation case (max_gen < n - 2) uses the embedding $H_{n-1} \hookrightarrow H_n$. This preserves $\mathrm{tr}_M$ (the Markov axiom yields the same value regardless of ambient algebra, by stability of $z$).
- The peeling case uses cyclicity to put $\sigma_{n-2}$ at the rightmost position. The Markov axiom then contributes a $z$ factor. The remainder $\alpha \beta$ (with $\alpha, \beta$ on either side of the rotated cut) need not lie in $H_{n-1}$ if $\alpha$ contained another $\sigma_{n-2}$. In that case, the basis-expansion subroutine handles the Hecke-quadratic firings exactly.

By induction on $(n, \ell)$, the output equals $\mathrm{tr}_M(\beta)$ in $\mathbb{Q}(q)$. $\square$

## Disjoint-product property

For $\alpha \in H_k$ on strands $\{1, \ldots, k\}$ and $\beta \in H_{n-k-1}$ on strands $\{k+2, \ldots, n\}$ (no $\sigma_{k+1}$ appears in $\beta$), the words commute. We have $\alpha \beta = \beta \alpha$, and the Markov axiom plus cyclicity gives:
$$
  \mathrm{tr}_M(\alpha \beta) \;=\; \mathrm{tr}_M(\alpha) \cdot \mathrm{tr}_M(\beta)
$$
by induction on $\ell(\beta)$. The recursive algorithm realises this property automatically. The peeling phase strips $\beta$'s top generators $\sigma_{n-2}, \sigma_{n-3}, \ldots, \sigma_{k+2}$ in order. This contributes factors of $z$ that exactly match the standalone $\mathrm{tr}_M(\beta)$ computed in its own algebra $H_{n-k-1}$.

## Which axioms the disjoint product actually needs

**Scope of the right-induction step.** Right-induction yields $z^{\ell(\beta)}$ directly only when every generator in $\beta$ occurs with multiplicity one; for general words containing repeated generators (such as $\sigma_1^2$, where $\mathrm{tr}_M(\sigma_1^2) = hz + 1 \neq z^2$), the disjoint-product reduction alternates right-peeling with the quadratic Hecke relation $\sigma_i^2 = h\sigma_i + 1$.


The argument above is stated in terms of the Markov axiom and cyclicity, but it
uses two further properties silently, and both are named in the correctness
section: **normalisation** $\mathrm{tr}_M(1) = 1$, and **stability under the
trivial embedding** — *"the Markov axiom yields the same value regardless of
ambient algebra"*. Neither follows from stripping and cyclicity.

Stripping and cyclicity alone admit a counter-model. Put $\mathrm{tr}_M$ on
$H_n$ equal to $2^n$ for every word, with $z = 2$. Stripping holds, since
$2^{n+1} = 2 \cdot 2^n$; cyclicity holds because both sides ignore the word.
The product law fails at $k = 0$, $n = 2$, $\alpha = \beta = 1$, where the left
side is $4$ and the right is $2^0 \cdot 2^1 = 2$. So a trace that grows with the
ambient index alone is not excluded by stripping and rearrangement.

With normalisation and stability added, the product law is a **consequence**
rather than a further axiom: stability makes the value independent of the
ambient index, stripping then peels one generator for a factor of $z$, and
induction from the right gives $z^{\ell(\beta)}$ on both sides. The separating
slot $\sigma_{k+1}$ plays no role in that argument, and the generator indices of
$\beta$ must be non-negative for the peel to apply — a word on the upper cluster
satisfies this, which is what the support condition $\{k+2, \ldots, n\}$ above
amounts to in the index encoding.

## Empirical verification

| atom | braid word | $H_n$ | $\mathrm{tr}_M(q_0)$ |
|---|---|---|---|
| proton | $\sigma_1^7 \sigma_2^4$ | $H_3$ | $1.884319\ldots$ |
| neutron | $\sigma_1^6 \sigma_2^4 \sigma_1^{-1}$ | $H_3$ | $1.464034\ldots$ |
| deuteron disjoint | $\sigma_1^7\sigma_2^4 \oplus \sigma_4^6\sigma_5^4\sigma_4^{-1}$ | $H_6$ | $\mathrm{tr}_M(p)\cdot\mathrm{tr}_M(n)$ |

The two numeric entries are evaluated at
$z = q^{3}/(q^{2}+1)$. They are *not* nucleon mass inputs: these braid words are
not the canonical nucleon words, so the values must not be used for mass
predictions.

The producer additionally checks the closed forms the Markov axioms force —
$\mathrm{tr}_M(\sigma_i) = z$, $\mathrm{tr}_M(\sigma_1\sigma_2) = z^2$,
$\mathrm{tr}_M(\sigma_1^2) = hz + 1$, and $z^3$, $z^4$ on the $H_4$ and $H_5$
chains — together with the disjoint-product identity above, evaluated as
$\mathrm{tr}_M(H_6;\sigma_1\sigma_2\sigma_4\sigma_5)$ against
$\mathrm{tr}_M(H_3;\sigma_1\sigma_2)^2$. All nine agree to the working
precision. These are the substantive checks: each is a prediction of the axioms
that the reducer reaches by an independent route (Hecke-basis expansion, then
recursive descent), whereas the two table entries above have no independent
reference to be checked against.

## References

- [Jones 1987] *Hecke algebra representations of braid groups and link polynomials*, Annals of Math. **126**, 335-388.
- [Kassel 1995] *Quantum Groups*, Springer GTM 155, Ch. III §3.
- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349-383.
