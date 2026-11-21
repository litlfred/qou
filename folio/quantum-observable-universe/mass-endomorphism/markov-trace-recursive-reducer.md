## Statement

*Let $\beta \in B_n$ be any braid word. There is a terminating algorithm (termination proved in prose below) that returns a closed-form symbolic expression for $\mathrm{tr}_M(\beta) \in \mathbb{Q}(q)$ using only:*
- *the Hecke quadratic $\sigma_i^2 = h \sigma_i + 1$ (with $h = q - q^{-1}$);*
- *the Markov axiom $\mathrm{tr}_M(\alpha \sigma_n) = z \mathrm{tr}_M(\alpha)$ for $\alpha \in H_n \subset H_{n+1}$, for the Markov parameter $z$;*
- *cyclicity $\mathrm{tr}_M(\alpha\beta) = \mathrm{tr}_M(\beta\alpha)$;*
- *and the braid relations.*

*The trace it computes has the **disjoint-product property**. Number the generators from $1$. Let $\alpha$ be a word in $\sigma_1, \ldots, \sigma_{k+1}$ and $\beta$ a word in $\sigma_1, \ldots, \sigma_m$, and write $\beta^{\uparrow}$ for $\beta$ with every generator index raised by $k+1$, so that $\beta^{\uparrow}$ uses $\sigma_{k+2}, \ldots, \sigma_{k+m+1}$. Then*
$$
  \mathrm{tr}_M(\alpha \beta^{\uparrow}) \;=\; \mathrm{tr}_M(\alpha) \cdot \mathrm{tr}_M(\beta).
$$
*The two clusters share the strand $k+2$.*

*If, in addition, $\mathrm{tr}_M$ is invariant under a uniform shift of generator indices, the split form also holds: $\mathrm{tr}_M(\alpha \otimes \beta) = \mathrm{tr}_M(\alpha) \cdot \mathrm{tr}_M(\beta)$ for $\alpha \in H_k(q)$ on strands $\{1, \ldots, k\}$ and $\beta \in H_{n-k-1}(q)$ on strands $\{k+2, \ldots, n\}$, separated by the unused generator $\sigma_{k+1}$.*

The shared-strand law is formalised in Lean (`markovTrace_disjointProduct`). Correctness is formalised as uniqueness (`markovTrace_unique`): two traces satisfying the axioms with the same $z$ and $h$ agree on every positive word, so any procedure that uses only these axioms, the reducer included, returns the trace. Since $\sigma_i^{-1} = \sigma_i - h$, positive words suffice. Termination of the algorithm itself is proved below in prose and is not formalised. Shift invariance is not proved here, so the split form is stated only under that hypothesis.

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

**Termination.** Each invocation of the recursive $\mathrm{tr}_M$ call either:
(i) truncates the ambient algebra ($n \to \text{max\_gen} + 2$ where $\text{max\_gen} + 2 < n$), strictly decreasing the integer $n$; or
(ii) peels one $\sigma_{n-2}$ from the word and recurses on basis elements $w'$ with $\ell(w') \leq \ell(\text{rotated}) = \ell(w) - 1$, strictly decreasing the Coxeter length.

The lex order on $(n, \ell(w))$ has no infinite descending chain, so termination is guaranteed. Each basis expansion involves at most $n!$ basis elements; no bound on the total number of evaluations is proved here. $\square$

**Correctness.** Each step is an exact equality in $\mathbb{Q}(q)$:
- Step 1 is exact (Hecke-quadratic expansion).
- The truncation case (max_gen < n - 2) uses the embedding $H_{n-1} \hookrightarrow H_n$. This preserves $\mathrm{tr}_M$ (the Markov axiom yields the same value regardless of ambient algebra, by stability of $z$).
- The peeling case uses cyclicity to put $\sigma_{n-2}$ at the rightmost position. The Markov axiom then contributes a $z$ factor. The remainder $\alpha \beta$ (with $\alpha, \beta$ on either side of the rotated cut) need not lie in $H_{n-1}$ if $\alpha$ contained another $\sigma_{n-2}$. In that case, the basis-expansion subroutine handles the Hecke-quadratic firings exactly.

By induction on $(n, \ell)$, the output equals $\mathrm{tr}_M(\beta)$ in $\mathbb{Q}(q)$. $\square$

## Disjoint-product property

Write $\beta^{\uparrow}$ for $\beta$ with every generator index raised by $k+1$, so that $\alpha$ uses $\sigma_1, \ldots, \sigma_{k+1}$ and $\beta^{\uparrow}$ uses $\sigma_{k+2}, \ldots$. Then
$$
  \mathrm{tr}_M(\alpha \beta^{\uparrow}) \;=\; \mathrm{tr}_M(\alpha) \cdot \mathrm{tr}_M(\beta).
$$
The proof is by induction on the number $m$ of generators of $\beta$, with Ocneanu's reduction inside each level. Fix $\alpha$ and let $F(\beta)$ be the difference of the two sides. Both sides satisfy the Hecke quadratic, braid and far-commutation relations in any context, so $F$ does too.

- If $\beta$ avoids its top generator $\sigma_{m}$, stability lowers $m$ on both sides, and the induction hypothesis gives $F(\beta) = 0$.
- If $\beta = a\,\sigma_{m}\,b$ uses it once, cyclicity moves $b^{\uparrow}$ to the front, the Markov axiom strips the top letter with a factor $z$, and cyclicity restores $\alpha (ab)^{\uparrow}$. The same steps on the right side give $z\,\mathrm{tr}_M(ab)$, and the induction hypothesis closes the case.
- If $\beta$ uses $\sigma_m$ twice or more, take two consecutive occurrences $\sigma_m x \sigma_m$. If $x$ avoids $\sigma_{m-1}$, far commutation brings the two letters together and the quadratic relation shortens the word. If $x$ uses $\sigma_{m-1}$ once, one braid move removes a $\sigma_m$. Otherwise $x$ is first reduced one level down by the same argument.

Every function on words that satisfies the three relations and vanishes on words using the top generator at most once therefore vanishes, so $F = 0$. Both clusters share the strand $k+2$, so the closures form a connected sum.

For the split form, let $\alpha \in H_k$ use $\sigma_1, \ldots, \sigma_{k-1}$ and let $\beta_0$ be $\beta$ written on $\sigma_1, \ldots, \sigma_{n-k-2}$. Apply the shared-strand law with $k-1$ in place of $k$ to $\alpha$ and to $\beta'$, the word $\beta_0$ with every index raised by $1$; then $\beta'^{\uparrow}$ is $\beta$ on strands $\{k+2, \ldots, n\}$, and the law gives $\mathrm{tr}_M(\alpha \otimes \beta) = \mathrm{tr}_M(\alpha)\,\mathrm{tr}_M(\beta')$. Shift invariance gives $\mathrm{tr}_M(\beta') = \mathrm{tr}_M(\beta_0)$. That hypothesis is not proved here.

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

Normalisation and stability are therefore part of the axiom set, but they are
not enough either: if stripping, stability and cyclicity are quantified over
every word, they force $\mathrm{tr}_M(\beta) = z^{\ell(\beta)}$, which
contradicts $\mathrm{tr}_M(\sigma_1^2) = hz + 1$. The axiom set
therefore restricts stripping, stability and cyclicity to words of $H_n$ and adds
the Hecke quadratic, braid and far-commutation relations. From these axioms it
proves $\mathrm{tr}_M(\sigma_n^2) = hz + 1$ and the product law when $\beta$ is
an ascending run $\sigma_{k+1}\cdots\sigma_{k+m}$, and the general product law
by the reduction in the previous section (Lean: `markovTrace_disjointProduct`,
sorry-free).

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
