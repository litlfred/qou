The Gröbner--Shirshov normal form computation has three distinct
complexity regimes, requiring different algorithmic strategies.

## The three regimes

**Regime 1: Transfer matrix ($O(A^2)$).**
The optimal NF $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$
has coefficients equal to the Markov-traced volumes $\hat{V}_i(q)$.
Each $\hat{V}_i$ is computed by a product of $A - i - 1$ transfer
matrices $T(c_j, d_j)$ — a total of $\binom{A}{2}$ matrix
multiplications.  This gives the $Q$-value, the Skein polynomial,
and the full optimal NF coefficients.  No Iwahori--Hecke algebra expansion
needed.

**Regime 2: Symbolic Gröbner--Shirshov with stripping ($O(A^3)$).**
The full NF is needed for the Pauli factor $F_{\mathrm{Pauli}}$,
the color content, and the per-length weight distribution.  With
inductive quotient stripping at strand boundaries (I$_{8}$ + I$_{9}$
applied after each strand), the intermediate term count stays
bounded at $O(A^2)$ per strand, giving $O(A^3)$ total.  All
coefficients are exact Laurent polynomials in $\mathbb{Z}[t, t^{-1}]$.

**Regime 3: Full expansion ($O(A!)$).**
Without stripping, the raw NF has up to $|S_A| = A!$ terms.
This is tractable only for $A \leq 9$ (234,504 terms for
${}^9\mathrm{Be}$).  The full expansion gives the raw histogram
and palindromic structure, but is not needed for any physical
observable.

## Inductive quotient chaining

The key optimisation: at each strand boundary, apply I$_{9}$
(chain collapse) and accumulate the **Pauli data** of stripped
terms as symbolic polynomials.  The surviving element has only
$\sim A$ terms (the optimal basis).  The next strand's
computation starts from $A$ terms, not $A!$.

The accumulation is **exact**: each stripped term contributes
its coefficient $c_w(t)$ to the running totals
$\mathrm{tr}_{\mathrm{alt}}(t)$ and $\mathrm{net}(t)$, weighted
by $(-t^{-2})^{\ell(w)}$ for the alternating trace.  The final
witness is the **sum** of accumulated (stripped) and kept
(surviving) contributions.

**Critical correctness requirement**: only accumulate
**stripped terms**, not all terms.  If all terms are accumulated
before stripping, survivors get double-counted when they
contribute to subsequent strands.

## The bottleneck: strand 8

For all nuclei with $A > 8$, the computation follows a
characteristic pattern:

1. **Strands 1–7**: build the NF for the first 8 nucleons.
   The term count grows to $\sim 14{,}000$ (for $A = 8$) or
   $\sim 230{,}000$ (for $A = 9$).  This takes $\leq 10$ seconds.

2. **Strand 8 boundary**: the I$_{9}$ strip reduces $\sim 230{,}000$
   terms to $\sim 9$ terms.  The stripped terms' Pauli data is
   accumulated exactly.

3. **Strands 9+**: each starts from $\sim 10$ terms, expands
   to $\sim 5{,}000$–$240{,}000$ during the strand, then strips
   back to $\sim 10$–$600$ terms at the boundary.

The bottleneck is always the **last crossing of a large strand**
(typically the n–n crossings at the end, which have $c = 1$, $d = -(q - q^{-1})$ and
produce the most new terms).  Peak memory occurs at the moment
before stripping.

## Optimisation strategies

### Monomial ordering (LenLex)

The engine uses length-lexicographic ordering: shorter words
reduce first (Hecke lowers degree), then lex order within the
same degree (far-comm and YB sort generators).  This is optimal
for the Iwahori--Hecke algebra because the Hecke relation
$\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ is the only
degree-changing rule.

### Junction-only reduction

When appending $\sigma_k$ to a reduced word $w$, only the
**junction** (last 2–3 characters of $w \cdot \sigma_k$) needs
checking.  The prefix $w$ was already reduced.  This reduces
the per-word reduction cost from $O(\ell)$ to $O(1)$ amortised.

### Separated reduction pools

Terms are split into **stable** (fully reduced, never rescanned)
and **Open** (needs checking).  Each reduction produces new
pending terms; stable terms are moved once and never revisited.
When a pending term collides with a stable term, the merged
result goes back to pending for re-checking.

### Batch quotient stripping ($O(A \cdot L_{\max})$)

The I$_{9}$ strip processes all terms at each length level in one
pass, from longest to shortest.  At length $\ell$: collect all
terms whose prefix (length $\ell - 1$) exists; remove them in
batch.  This is $O(n)$ per length level, $O(n \cdot L_{\max})$
total — compared to $O(n^2)$ for the one-at-a-time approach.

### Mid-crossing stripping

For very large strands, the quotient strip fires **within**
a crossing multiplication (not just at strand boundaries) when
the term count exceeds a threshold (30,000 terms).  This prevents
the exponential blowup from adjacent generator cascading
(e.g., 3 consecutive n–n crossings would produce $8\times$ terms
without mid-crossing stripping).

### Pattern discovery during construction

At each strand boundary, the engine reports the **most frequent
suffix patterns** (sub-words appearing in many terms).  These
are candidates for new structural ideals beyond I$_{8}$ and I$_{9}$.
High-frequency patterns that persist across strands indicate
universal structural operations that could be added to the
quotient ideal, further reducing term counts.

## Scalability

| $A$ | Strategy | Time | Memory | Coefficients |
|:---:|----------|-----:|-------:|:------------:|
| $\leq 9$ | Full expansion | $\leq 30$s | $\leq 562$MB | $\leq 10^{12}$ |
| $10$–$12$ | Inductive stripping | $10$–$45$s | $\leq 2.5$GB | $\leq 10^{17}$ |
| $13$–$16$ | Inductive + mid-crossing | est. $1$–$5$min | $\leq 3$GB | $\leq 10^{22}$ |
| $17$–$20$ | Needs big integer | est. $5$–$30$min | $\leq 5$GB | $> 10^{38}$ (i128 overflow) |
| $\leq 40$ | Transfer matrix only | $< 1$s | $< 1$MB | $O(A^2)$ |

For $Q$-values: the transfer matrix ($O(A^2)$) suffices for any $A$.
For $F_{\mathrm{Pauli}}$ and color content: the symbolic engine
handles $A \leq 16$ in minutes and $A \leq 20$ with big integer
arithmetic.  Beyond $A = 20$: float engine (v6) with per-length
accumulation, sacrificing exact-in-$q$ for tractability.
