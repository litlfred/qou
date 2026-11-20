Given a nucleus with $A$ nucleons and transfer matrix chains $\{M_i\}_{i=0}^{A-2}$, this describes how adding one nucleon produces the $A+1$ nucleus. This inductive step is the engine behind every Skein polynomial computation. 

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

## Gröbner--Shirshov normal form

The inductive construction produces a canonical normal form at every step. By Rules 1 and 2 the crossings at a fixed generator are contiguous in the braid word and the blocks are ordered by increasing generator index, so the nucleus element is a block-ordered product of linear factors $c\,\sigma_i + d \in H_A(q)$. Given the reduced nucleus element $\bar{\mathcal{N}}(A)$, Hopf-linking the next nucleon and applying the Gröbner--Shirshov division algorithm requires only Hecke reductions — zero Yang--Baxter and zero far-commutativity steps — and the resulting chain state, with coefficients produced by the transfer-matrix recurrence, is the exact normal form. This is the content of [the Hecke-only reduction proposition](#prop:tm-gs-normal-form), proved by induction on $A$.

## Shell closure signatures

At doubly-magic configurations $(p, p)$, the normal form exhibits special structure:
1. **Palindromic histogram.** The word-length histogram is a palindrome. For $p \neq n$, it is not.
2. **Dominant term jump.** The dominant coefficient jumps discontinuously. The ratio is larger at shell closures.
3. **Shell energy gap.** The Hecke reduction energy drops at shell closures and jumps at the next step.

## Complexity bound and magic-shell folding

The total number of matrix multiplications to build $\bar{\mathcal{N}}(A)$ without shell-folding is $C_{\mathrm{bare}}(A) = \binom{A}{2}$.

At a magic configuration $m \in \{2, 8, 20, 28, 50, 82, 126\}$, the shell-closure signatures identify the closed shell as a single Markov-equivalence class. When the next nucleon is added, it interacts with the collective torus-knot operator $T_{2, k}$ instead of $k$ internal nucleons separately. The folded step costs $O(1)$ matrix multiplications. Folding preserves Reidemeister equivalence because the palindromic histogram certifies the closed shell is in the totally-antisymmetric Wedderburn block. The polynomial agrees identically with the unfolded product.
