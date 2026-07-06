We compute the Hecke algebra normal form by iterative Gröbner–Shirshov reduction with three rewriting rules:

1. **Hecke relation** (Rule 0):
   $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.
   Reduces word length by 1; produces two output words.

2. **Far commutativity** (Rule 1):
   $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $|i - j| \geq 2$.
   Permutes generators without changing length.

3. **Yang–Baxter relation** (Rule 2):
   $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$.
   Applied in the direction that decreases shortlex order.

The reduction is confluent. The final normal form is independent of the order in which rules are applied. The intermediate word count, however, depends critically on the reduction strategy.

## The $H_A$-power factorization

For the $\mathfrak{p}\mathfrak{p}\cdots\mathfrak{n}\mathfrak{n}$ ordering (all protons first, then all neutrons), every normal form coefficient factors as $\pm 2^a \times H_A^k$. Here $a$ counts the number of $\mathfrak{p}\mathfrak{n}$ crossings in the reduction path and $k$ counts the number of Hecke-relation applications. We verify this for ${}^1\mathrm{H}$ through ${}^9\mathrm{Be}$.

The factorization enables a compressed representation. Each word stores only $(\mathrm{sign}, a, k)$ instead of a full Laurent polynomial. For atoms with mixed orderings ($\mathfrak{p}\mathfrak{n}\mathfrak{p}\mathfrak{n}\cdots$), the factorization breaks. The coefficients become general Laurent polynomials.

## Computational engines

Four Rust engines implement the reduction with increasing optimization:

| Engine | Representation | Peak memory | Speed |
|:-------|:---------------|:------------|:------|
| v9 (hecke-bigint) | BigInt polynomial | $O(A!)$ bytes | exact, slow |
| v11 (hecke-modular) | $\mathbb{F}_P$ dense array | $O(A! \times 200)$ bytes | 5$\times$ faster |
| v13 (hecke-stream) | streaming + leading-term cancel | $O(N)$ during reduce | lower peak |
| v14 (hecke-hapower) | sparse $H_A^k$ pairs | $O(A! \times 20)$ bytes | fits ${}^{11}\mathrm{B}$ |

The modular engine uses the Mersenne prime $P = 2^{127} - 1$ with fast Mersenne reduction: $x \bmod P = (x \gg 127) + (x \mathbin{\&} P)$. Modular multiplication uses four $\texttt{u64} \times \texttt{u64} \to \texttt{u128}$ products instead of the $O(128)$-step Russian peasant algorithm.

## LP-dual reduction ordering

Since confluent reductions permit arbitrary rule ordering, the LP dual determines the most efficient strategy:

- **Cancellation-first**. We apply Rule 0 when the shortened word already exists in the stable set. This produces immediate cancellation. It reduces the word count before other rules fire.

- **Leading-term cancellation**. We consolidate pending words before reduction. Words with opposite-sign coefficients on the same basis element cancel without any reduction work (the Buchberger S-polynomial criterion applied to Hecke algebras).

- **Crossing order**. Within the braid construction, the order of crossing multiplication affects intermediate size. Adjacent generators do not commute. Only far-commuting pairs ($|i - j| \geq 2$) may be reordered.

## Reproducibility

All computations are reproducible from the Rust source in `tools/hecke-engine/`. The engine generates certificates (JSON files containing $F_{\mathrm{Pauli}}$, $\mathrm{tr}_{\mathrm{alt}}$, and $\mathrm{net}$ polynomials evaluated at $q_0$) and commits them to the repository. Witness files in `computations/` record every mass prediction with full intermediate values.
