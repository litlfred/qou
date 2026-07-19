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
