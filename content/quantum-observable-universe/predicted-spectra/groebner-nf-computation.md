The Gröbner--Shirshov normal form $\mathcal{N}(Z, N)$ of a nucleus in
$H_A(q)$ is a formal sum over reduced braid words:

$$
  \mathcal{N}(Z, N)
  = 
  \sum_{w \in \mathrm{supp}} c_w \cdot w
$$

where each $c_w \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$ is an exact
Laurent polynomial in the substrate parameter $q$, and the
support $\mathrm{supp} \subset S_A$ consists of reduced words in
the symmetric group.

## What the NF encodes

Each reduced word $w$ of length $\ell(w)$ represents a configuration
of $\ell(w)$ **simultaneously active crossings** in the nuclear braid.
The coefficient $c_w$ is the amplitude of that configuration.

The word length $\ell$ has a direct physical interpretation:

See [Table 1](#tbl:groebner-nf-computation-table1-data).

The **weight distribution** $W(\ell) = \sum_{|w| = \ell} |c_w|$
gives the total amplitude at each correlation level. For all
nuclei computed ($A \leq 12$):

- $W(L_{\max}) \gg W(0)$: the fully correlated state carries the
 largest amplitude. This is the **shell binding energy** — the
 many-body correlations that hold the nucleus together.
- $W(0) + W(1)$ is the amplitude in the **optimal basis**
 $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$. This is what the
 transfer matrix computes directly via the traced volumes $\hat{V}_i$.
- The weight grows exponentially from short to long words:
 $W(\ell) / W(\ell - 1) \approx q^{c}$ for a constant $c$ depending
 on the crossing structure. Each Hecke reduction
 $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ transfers amplitude from
 degree $\ell$ to degrees $\ell - 1$ and $\ell - 2$, with the
 $\sigma$-coefficient scaling by $q - q^{-1} \approx 0.209$.

## Quotient ideals: reducing $A!$ to $A$

The raw NF has up to $|S_A| = A!$ terms. Two quotient ideals
reduce this to exactly $A$ terms — the **optimal Gröbner--Shirshov basis** —
for nuclei in the valley of stability ($N \geq Z - 1$):

**$I_8$ (adjacency correlation).** A reduced word $\sigma_i \sigma_{i+1}$
of length $2$ is *absorbed* into the single-generator term $\sigma_{i+1}$
when the latter is present. The coefficient of $\sigma_i \sigma_{i+1}$
equals the off-diagonal entry of the transfer matrix product $M_i$
at generator $\sigma_i$ — it is structurally determined, not
independent.

Physically: the adjacency correlation is the **non-commutative
coupling** between neighbouring crossings. It is the off-diagonal
entry of the $2 \times 2$ transfer matrix $T(c, d)$ acting on the
Hecke state $(a \sigma + b)$. In the optimal basis, this coupling
is encoded in the ratio $c_{\sigma_i \sigma_{i+1}} / c_{\sigma_{i+1}}$,
which is a function of $q$ alone.

**$I_9$ (closed shell chain collapse).** A reduced word $w \cdot \sigma_j$
is absorbed when its prefix $w$ is also present. Applied recursively
from longest words to shortest, this collapses the entire NF to the
standard basis $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$.

Physically: each generator $\sigma_i$ contributes a **transfer matrix
chain** $M_i = \prod_{j > i} T_{K_i, K_j}(q)$, and the chain extends
word by word. The extension $w \cdot \sigma_j$ is the next step in
the chain — its coefficient is determined by $c_w$ times the crossing
coefficient at $\sigma_j$. Collapsing the chain to a single term
$\hat{V}_i = z \cdot (M_i)_{00} + (M_i)_{10}$ is exactly the
Markov-traced volume.

**Why $I_9$ needs $d \neq 0$ (the valley of stability).** When
multiplying the NF by $(c \cdot \sigma_k + d)$, the $d$-term
preserves every existing word (scales it by $d$), while the $c$-term
extends each word by $\sigma_k$. For every extended word $w \cdot
\sigma_k$, its prefix $w$ survives (from the $d$-term) — so $I_9$
can absorb it. This requires $d \neq 0$.

For proton–proton crossings: $d = 0$ (no constant term). The
prefix is **not** preserved. Without the prefix, $I_9$ has no
anchor for the chain stripping. The condition $d \neq 0$ holds for
neutron–neutron ($d = -(q - q^{-1})$) and proton–neutron ($d = -(q - q^{-1})/2$)
crossings. The valley of stability condition $N \geq Z - 1$ ensures
at least one $d \neq 0$ crossing at every generator.

## The histogram: universal in $A$

The **term-count histogram** $h(\ell) = \#\{w : |w| = \ell\}$
counts how many reduced words appear at each length. This histogram
is **the same for all $(Z, N)$ at the same $A$**: verified
computationally for $A \leq 8$ (e.g., ${}^8\mathrm{Be}(4,4)$ and
${}^8\mathrm{Li}(3,5)$ have identical histograms).

The histogram depends only on the Iwahori--Hecke algebra $H_A(q)$, not on
the crossing coefficients. It factors as a product of $q$-integers:

See [Table 2](#tbl:groebner-nf-computation-table2-data).

These are $q$-multinomial coefficients — the $q$-analogue of
Pascal's triangle. The palindromicity of the histogram polynomial
(verified for all $A \leq 7$) reflects the Poincaré duality of the
Bruhat order on the support.

## The weight distribution: where pairing lives

While the histogram is $A$-universal, the **weight distribution**
$W(\ell)$ depends on $(Z, N)$. At the same $A$:

- **Even-even** nuclei have higher total weight (stronger coherence
 from nucleon pairing).
- **Odd-odd** nuclei have lower total weight (unpaired crossings
 weaken the chain anchor).

The ratio $\mathrm{net}(\text{even-even}) / \mathrm{net}(\text{odd-odd})$
at the same $A$ quantifies the **pairing energy**. At $A = 6$:
$\mathrm{net}({}^6\mathrm{He}(2,4)) / \mathrm{net}({}^6\mathrm{Li}(3,3))
= 6.64 / 4.96 = 1.34$ — a $34\%$ enhancement from pairing.

The pairing mechanism in the NF: when two same-type crossings are
adjacent (even occupancy), their Hecke product $\sigma^2 = (q - q^{-1})
\sigma + 1$ creates **both** $\sigma$ and $\mathbf{1}$ terms. The
$\mathbf{1}$ term anchors the $I_9$ chain at that position. When
unpaired (odd occupancy), only the $\sigma$ term exists — the chain
anchor is weaker, and the total amplitude is reduced.

## The Pauli factor: multi-generator phenomenon

The **alternating trace** $\mathrm{tr}_{\mathrm{alt}} = \sum_w c_w
\cdot (-q^{-1})^{\ell(w)}$ evaluates each word at the alternating
eigenvalue $-q^{-1}$ of the Hecke relation. The ratio

$$
  F_{\mathrm{Pauli}}^{(A)}
  = 
  \frac{|\mathrm{tr}_{\mathrm{alt}}(\mathcal{N})|}{|\mathrm{net}(\mathcal{N})|}
$$

measures how much of the NF amplitude lives in the **alternating
irrep** of $S_A$ — the antisymmetric channel governed by Pauli
exclusion.

This quantity **cannot** be computed from the $2 \times 2$ transfer
matrix. The per-generator transfer matrix has only two eigenvalues
($q$ and $-q^{-1}$), and both the symmetric and alternating irreps
share these eigenvalues. The irrep separation requires the
**multi-generator interaction** — how $\sigma_0$ and $\sigma_1$ act
together — which is exactly the content of the full Gröbner--Shirshov NF.

## The $6 \times 6$ transfer matrix: no shortcut

we expect that enlarging the transfer matrix from $2 \times 2$
to $6 \times 6$ (acting on the full $H_3(q)$ basis
$\{\mathbf{1}, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0,
\sigma_0\sigma_1\sigma_0\}$) would separate the irreps.

**Proved symbolically**: the $6 \times 6$ transfer matrix
$T_6(c, d) = c \cdot R(\sigma_0) + d \cdot I_6$ has exactly
**two distinct eigenvalues**, each of multiplicity $3$:

$$
  \lambda_+ = c \cdot q + d,
  \qquad
  \lambda_- = c \cdot (-q^{-1}) + d.
$$

These are **identical** to the $2 \times 2$ eigenvalues. The
multiplicity $3$ corresponds to:
- $\lambda_+$: $1$ from sym + $2$ from std (the $q$-eigenvalue
 subspace of the standard irrep)
- $\lambda_-$: $1$ from alt + $2$ from std (the $-q^{-1}$-eigenvalue
 subspace)

The standard irrep has **both** eigenvalues ($q$ and $-q^{-1}$)
because $\sigma_0$ in the $2$-dimensional standard representation
has a $2 \times 2$ matrix with both eigenvalues. The $6 \times 6$
matrix does not separate sym from std or alt from std — it only
sees the two eigenvalue sectors.

**Conclusion**: the Pauli factor $F_{\mathrm{Pauli}}$ is
irreducibly a **multi-generator phenomenon**. No per-generator
transfer matrix (of any size) can compute it. The full Gröbner--Shirshov
NF — the multi-generator Iwahori--Hecke algebra expansion — is required.

This has a physical interpretation: the Pauli exclusion principle
acts between **pairs** of fermions (quarks in a Borromean triplet),
not on individual crossings. The multi-generator structure IS the
inter-quark correlation that the Pauli principle creates.

Computed witnesses (exact in $\mathbb{Z}[\check{q}, \check{q}^{-1}]$ for $A \leq 12$,
$f_{64}$ at $q_0$ for display):

See [Table 3](#tbl:groebner-nf-computation-table3-data).

For each nucleus through $A = 12$, the symbolic witnesses are
**exact in $q$**: the polynomials $\mathrm{tr}_{\mathrm{alt}}(\check{q})$,
$\mathrm{net}(\check{q})$, $\mathrm{observable}(\check{q})$, and $\mathrm{color}(\check{q})$
are elements of $\mathbb{Z}[\check{q}, \check{q}^{-1}]$ (Laurent polynomials over
$\mathbb{Z}$ in $\check{q} = q^{1/2}$, the spinor information rate). The denominator $2^{p_n}$ is
tracked separately (from the doubled pn crossing convention).

The $H_3(q)$ Pauli factor (from $3$-strand irrep decomposition)
is $F_{\mathrm{Pauli}} = 0.6382$. The $A$-strand values differ
because they capture the full multi-generator interaction, not the $3$-strand projection.

## Streaming pattern discovery

During the inductive construction, the quotient ideals $I_8$ and
$I_9$ strip terms at each strand boundary. Before stripping, the
engine reports the **most frequent suffix patterns** — sub-words
that appear in many terms. These are candidates for new structural
ideals beyond $I_8$ and $I_9$.

For ${}^{16}\mathrm{O}$ at strand $8$:
$\sigma_7 \sigma_8$ appeared $52{,}230$ times (the $I_8$ adjacency
pattern at the newest generator). The pattern $\sigma_4 \sigma_6
\sigma_7 \sigma_8$ ($14{,}262$ times) is a $4$-generator chain
that skips $\sigma_5$ — a potential $I_{11}$ candidate.

The per-length weight distribution $W(\ell)$ and the Pauli
accumulator $\mathrm{tr}_{\mathrm{alt}}$ are preserved exactly through
stripping, so no physical data is lost. The histogram $h(\ell)$
is $A$-universal (compute once from the easiest case $N(1, A-1)$).
