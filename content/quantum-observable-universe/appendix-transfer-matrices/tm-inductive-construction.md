Given a nucleus with $A$ nucleons and transfer matrix chains $\{M_i\}_{i=0}^{A-2}$, we describe how adding one nucleon produces the $A+1$ nucleus. This inductive step is the engine behind every Skein polynomial computation. 

## The inductive step: $A \to A+1$

Given nucleus $\mathcal{N}(Z, N)$ with $A$ nucleons ordered $[\tau_0, \ldots, \tau_{A-1}]$ where $\tau_k \in \{\mathfrak{p}, \mathfrak{n}\}$. The braid has generators $\sigma_0, \ldots, \sigma_{A-2}$ with transfer matrix products $M_i$ and traced volumes $\hat{V}_i$.
Add nucleon $\tau_A$ at position $A$.
Result: Nucleus $\mathcal{N}'$ with $A+1$ nucleons, generators $\sigma_0, \ldots, \sigma_{A-1}$, and updated products $M_i'$.

**Rule 1: Existing generators gain one crossing.** Every existing generator $\sigma_i$ acquires one crossing between nucleon $i$ and nucleon $A$. The transfer matrix product appends one new factor on the left:

$$
  M_i'(q) = T_{\tau_i, \tau_A}(q) \cdot M_i(q)
$$

where $T_{\tau_i, \tau_A}$ is $T_{pp}$, $T_{nn}$, or $T_{\mathrm{mix}}$.

**Rule 2: One new generator is created.** A new generator $\sigma_{A-1}$ appears with a single crossing:

$$
  M_{A-1}'(q) = T_{\tau_{A-1}, \tau_A}(q)
$$

**Rule 3: Skein polynomial update.** The new polynomial factors as:

$$
  P_{\mathcal{N}'}(q) = \left( \prod_{i=0}^{A-2} \hat{V}_i'(q) \right) \cdot \hat{V}_{A-1}'(q)
$$

where $\hat{V}_i'(q) = z \cdot (M_i')_{11} + (M_i')_{21}$.

**Rule 4: Crossing count grows by $A$.** Adding the $(A+1)$-th nucleon creates $A$ new crossings. The total crossing count goes from $\binom{A}{2}$ to $\binom{A+1}{2}$.

## The recurrence at each generator

At generator $\sigma_i$, the coefficients $(a_i, b_i)$ in $M_i = \bigl(\begin{smallmatrix} a_i \\ b_i \end{smallmatrix}\bigr)$ satisfy the transfer matrix recurrence. Starting from $(a, b) = (0, 1)$, each new crossing with nucleon $j$ updates:

$$
  \begin{pmatrix} a' \\ b' \end{pmatrix} = T(c_j, d_j) \cdot \begin{pmatrix} a \\ b \end{pmatrix}
$$

Explicitly: $a' = ac_j(q - q^{-1}) + ad_j + bc_j$ and $b' = ac_j + bd_j$.

## Jet expansion interpretation

The crossing product stratifies into jet orders. Jet order $r$ is the $(r+1)$-body correlation, present with multiplicity $\binom{k_i}{r}$. Adding nucleon $A$ increases the chiral degree at every existing generator by 1. Single beta decay is a 1-jet variation. The $Q$-value sums only over generators $\sigma_i$ with $i \leq p$, where $p$ is the converting nucleon's position. Unaffected generators cancel exactly.

## Gröbner--Shirshov normal form (inductive proof)

The inductive construction produces a canonical normal form at every step: given the reduced nucleus element $\bar{\mathcal{N}}(A)$, Hopf-linking the next nucleon and applying the Gröbner--Shirshov division algorithm requires only Hecke reductions — zero Yang--Baxter and zero far-commutativity steps — and the resulting chain state is the exact normal form. The inductive argument is as follows.

**Setup.** Each crossing between nucleons of types $\tau_i$ and $\tau_j$ at generator $\sigma_i$ is the linear element $c\,\sigma_i + d \in H_A(q)$ with coefficients $(c, d)$ read from the crossing type. By Rules 1 and 2 the crossings at a fixed generator are contiguous in the braid word, and the blocks are ordered by increasing generator index, so the nucleus element is the block-ordered product

$$
\Xi_A \;=\; \prod_{i=0}^{A-2} \; \prod_{j=A-1}^{i+1} \bigl(c_{ji}\,\sigma_i + d_{ji}\bigr),
$$

with the inner product taken in decreasing $j$, matching the transfer-matrix order. The Gröbner--Shirshov rewriting system for $H_A(q)$ has three families of rules — the Hecke rule $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$, far-commutativity $\sigma_j\sigma_i \to \sigma_i\sigma_j$ for $j \geq i + 2$, and Yang--Baxter $\sigma_j\sigma_i\sigma_j \to \sigma_i\sigma_j\sigma_i$ for $j = i + 1$ — and is confluent by the Diamond Lemma, so the normal form is unique and independent of the reduction order.

**Inductive claim.** For every $A \geq 2$, the reduction of $\Xi_A$ uses only the Hecke rule, and the result is the chain form

$$
\bar{\mathcal{N}}(A) \;=\; \prod_{i=0}^{A-2} \bigl(a_i\,\sigma_i + b_i\bigr),
$$

whose full expansion $\sum_{S} \bigl(\prod_{i \in S} a_i\bigr)\bigl(\prod_{i \notin S} b_i\bigr)\,\sigma_S$, over subsets $S \subseteq \{0, \ldots, A-2\}$ with $\sigma_S$ the product of the $\sigma_i$, $i \in S$, in increasing order, is already in normal form.

**Base case** $A = 2$. The word is the single factor $c\,\sigma_0 + d$: one linear block, no reducible subword, and the chain state is $(a_0, b_0) = (c, d)$.

**Normality of the expansion.** Every monomial $\sigma_S$ of the chain form contains each generator at most once, with indices strictly increasing left to right. Such a word contains no subword $\sigma_i^2$ (no repeated letter), no far-commutativity leading word $\sigma_j\sigma_i$ with $j \geq i+2$ (adjacent letters are strictly increasing), and no Yang--Baxter leading word $\sigma_j\sigma_i\sigma_j$ (that pattern repeats the letter $\sigma_j$). Hence every $\sigma_S$ is a normal word, and distinct $S$ give distinct normal words, so the expansion is the unique normal-form expression.

**Inductive step** $A \to A+1$. Adding nucleon $\tau_A$ modifies the word in exactly two ways. At each existing block $i \leq A-2$, one new factor $c\,\sigma_i + d$ with $(c, d) = (c_{Ai}, d_{Ai})$ enters on the left of the block (Rule 1). Inside that block,

$$
\bigl(c\,\sigma_i + d\bigr)\bigl(a_i\,\sigma_i + b_i\bigr)
\;=\;
c\,a_i\,\sigma_i^2 + \bigl(c\,b_i + d\,a_i\bigr)\sigma_i + d\,b_i ,
$$

and the single occurrence of $\sigma_i^2$ is the only reducible subword created: the letters adjacent to the block across its boundaries carry strictly smaller (left) and strictly larger (right) generator indices, so no far-commutativity pattern arises, and a Yang--Baxter pattern would need the same letter twice separated by one position, which the block structure never produces. One application of the Hecke rule $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ gives

$$
a_i' \;=\; a_i c\,(q - q^{-1}) + a_i d + b_i c,
\qquad
b_i' \;=\; a_i c + b_i d,
$$

which is precisely the transfer-matrix recurrence $\bigl(\begin{smallmatrix} a_i' \\ b_i' \end{smallmatrix}\bigr) = T(c, d)\bigl(\begin{smallmatrix} a_i \\ b_i \end{smallmatrix}\bigr)$ of Rule 1. Second, one new block $c\,\sigma_{A-1} + d$ appears at the right end of the word (Rule 2), already linear, requiring no reduction. The result is again a block-ordered product of linear factors, so the inductive claim holds for $A+1$.

**Conclusion.** By induction, the reduction of $\Xi_A$ to $\bar{\mathcal{N}}(A)$ uses Hecke reductions only: one per crossing after the first at each generator (none when the running coefficient $a_i$ vanishes, as happens for purely scalar crossing types with $c = 0$), for a total of at most $\binom{A}{2} - (A-1) = \binom{A-1}{2}$ Hecke steps, and zero Yang--Baxter or far-commutativity steps. Since the rewriting system is confluent and the chain-form expansion consists of pairwise distinct normal words, the chain is the exact Gröbner--Shirshov normal form of the nucleus element.

## Shell closure signatures

At doubly-magic configurations $(p, p)$, the normal form exhibits special structure:
1. **Palindromic histogram.** The word-length histogram is a palindrome. For $p \neq n$, it is not.
2. **Dominant term jump.** The dominant coefficient jumps discontinuously. The ratio is larger at shell closures.
3. **Shell energy gap.** The Hecke reduction energy drops at shell closures and jumps at the next step.

## Complexity bound and magic-shell folding

The total number of matrix multiplications to build $\bar{\mathcal{N}}(A)$ without shell-folding is $C_{\mathrm{bare}}(A) = \binom{A}{2}$.

At a magic configuration $m \in \{2, 8, 20, 28, 50, 82, 126\}$, the shell-closure signatures identify the closed shell as a single Markov-equivalence class. When the next nucleon is added, it interacts with the collective torus-knot operator $T_{2, k}$ instead of $k$ internal nucleons separately. The folded step costs $O(1)$ matrix multiplications. Folding preserves Reidemeister equivalence because the palindromic histogram certifies the closed shell is in the totally-antisymmetric Wedderburn block. The polynomial agrees identically with the unfolded product.
