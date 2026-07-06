The Gröbner--Shirshov normal form computation separates into three complexity regimes.

## The three regimes

**Regime 1: Transfer matrix ($O(A^2)$).**
The optimal normal form $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$ possesses coefficients equal to the Markov-traced volumes $\hat{V}_i(q)$. Each $\hat{V}_i$ is a product of $A - i - 1$ transfer matrices $T(c_j, d_j)$, totalling $\binom{A}{2}$ multiplications. This yields the $Q$-value, the Skein polynomial, and the optimal normal form coefficients without Iwahori--Hecke algebra expansion.

**Regime 2: Symbolic Gröbner--Shirshov with stripping ($O(A^3)$).**
The full normal form dictates the Pauli factor $F_{\mathrm{Pauli}}$, the color content, and the per-length weight distribution. We apply inductive quotient stripping (ideals I$_{8}$ and I$_{9}$) after each strand. This bounds the intermediate term count to $O(A^2)$ per strand, giving $O(A^3)$ overall. All coefficients remain exact Laurent polynomials in $\mathbb{Z}[t, t^{-1}]$.

**Regime 3: Full expansion ($O(A!)$).**
Without stripping, the raw normal form generates up to $A!$ terms. This limits tractability to $A \leq 9$. The full expansion exposes the raw histogram and palindromic structure, but contributes to no physical observable.

## Inductive quotient chaining

At each strand boundary, we apply the chain collapse ideal I$_{9}$ and accumulate the Pauli data of stripped terms as symbolic polynomials. The surviving optimal basis contains roughly $A$ terms. The subsequent strand computation initiates from these $A$ terms, bypassing the $A!$ explosion.

The accumulation is exact. Each stripped term contributes its coefficient $c_w(t)$ to the running totals $\mathrm{tr}_{\mathrm{alt}}(t)$ and $\mathrm{net}(t)$, weighted by $(-t^{-2})^{\ell(w)}$ for the alternating trace. The final witness sums the accumulated (stripped) and kept (surviving) contributions.

We accumulate only stripped terms. If we accumulated all terms before stripping, surviving terms would double-count when contributing to subsequent strands.

## The bottleneck: strand 8

For all nuclei with $A > 8$, the computation exhibits a characteristic bottleneck:

1. **Strands 1–7**: The normal form builds to $\sim 14{,}000$ terms ($A = 8$) or $\sim 230{,}000$ terms ($A = 9$), taking under 10 seconds.
2. **Strand 8 boundary**: The I$_{9}$ strip collapses $\sim 230{,}000$ terms to roughly 9 terms. We accumulate the Pauli data for the stripped terms.
3. **Strands 9+**: Each strand expands from $\sim 10$ terms to $5{,}000$–$240{,}000$ terms, then strips back to $10$–$600$ terms at the boundary.

The computational bottleneck is the final crossing of a large strand—typically the neutron–neutron crossings characterized by $c = 1, d = -(q - q^{-1})$. Peak memory occurs immediately before stripping.

## Optimisation strategies

**Monomial ordering (LenLex).**
We use length-lexicographic ordering. The engine reduces shorter words first, then applies lexicographic ordering within the same degree. This aligns with the Iwahori--Hecke algebra, where the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ acts as the sole degree-changing rule.

**Junction-only reduction.**
When appending $\sigma_k$ to a reduced word $w$, we only check the junction (the final characters of $w \cdot \sigma_k$). The prefix $w$ remains reduced. This lowers the amortized per-word reduction cost from $O(\ell)$ to $O(1)$.

**Separated reduction pools.**
We partition terms into stable (fully reduced) and pending pools. Stable terms are never rescanned. When a pending term collides with a stable term, the merged result returns to the pending pool.

**Batch quotient stripping ($O(A \cdot L_{\max})$).**
The I$_{9}$ strip processes all terms at each length level simultaneously, descending from longest to shortest. We collect and remove all terms containing a specific length $\ell - 1$ prefix. This operates in $O(n \cdot L_{\max})$ rather than $O(n^2)$.

**Mid-crossing stripping.**
For large strands, the quotient strip fires within a crossing multiplication once the term count exceeds 30,000. This halts the exponential blowup from cascaded adjacent generators.

**Pattern discovery.**
At each strand boundary, the engine identifies frequent suffix patterns. These candidate sub-words suggest structural ideals beyond I$_{8}$ and I$_{9}$. Persisting patterns indicate universal structural operations eligible for inclusion in the quotient ideal.

## Scalability

| $A$ | Strategy | Time | Memory | Coefficients |
|:---:|----------|-----:|-------:|:------------:|
| $\leq 9$ | Full expansion | $\leq 30$s | $\leq 562$MB | $\leq 10^{12}$ |
| $10$–$12$ | Inductive stripping | $10$–$45$s | $\leq 2.5$GB | $\leq 10^{17}$ |
| $13$–$16$ | Inductive + mid-crossing | est. $1$–$5$min | $\leq 3$GB | $\leq 10^{22}$ |
| $17$–$20$ | Needs big integer | est. $5$–$30$min | $\leq 5$GB | $> 10^{38}$ (i128 overflow) |
| $\leq 40$ | Transfer matrix only | $< 1$s | $< 1$MB | $O(A^2)$ |

The transfer matrix ($O(A^2)$) yields $Q$-values for any $A$. The symbolic engine supplies $F_{\mathrm{Pauli}}$ and color content up to $A \leq 16$ (minutes) or $A \leq 20$ (with big integers). Beyond $A = 20$, we sacrifice exact-in-$q$ calculations for a per-length accumulation float engine.
