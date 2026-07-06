The Gröbner--Shirshov normal form $\mathcal{N}(Z, N)$ of a nucleus in $H_A(q)$ is a formal sum over reduced braid words:

$$
  \mathcal{N}(Z, N)
  = 
  \sum_{w \in \mathrm{supp}} c_w \cdot w.
$$

Here, each amplitude $c_w \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$ is an exact Laurent polynomial in the substrate parameter $q$. The support $\mathrm{supp} \subset S_A$ consists of reduced words in the symmetric group.

## Content of the NF

Each reduced word $w$ of length $\ell(w)$ represents a configuration of $\ell(w)$ simultaneously active crossings in the nuclear braid. The amplitude of this configuration is $c_w$.

The word length $\ell$ has a direct physical interpretation:

See [Table 1](#tbl:groebner-nf-computation-table1-data).

The weight distribution $W(\ell) = \sum_{|w| = \ell} |c_w|$ defines the total amplitude at each correlation level. For all computed nuclei ($A \leq 12$):

- $W(L_{\max}) \gg W(0)$: The fully correlated state carries the largest amplitude. This determines the shell binding energy via many-body correlations.
- $W(0) + W(1)$: This is the amplitude in the optimal basis $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$, which the transfer matrix computes directly via traced volumes $\hat{V}_i$.
- $W(\ell) / W(\ell - 1) \approx q^{c}$: The weight grows exponentially. Each Hecke reduction $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ transfers amplitude from degree $\ell$ to degrees $\ell - 1$ and $\ell - 2$, scaling by $q - q^{-1} \approx 0.209$.

## Quotient ideals: reducing $A!$ to $A$

The raw normal form contains up to $|S_A| = A!$ terms. For nuclei in the valley of stability ($N \geq Z - 1$), two quotient ideals reduce this to exactly $A$ terms (the optimal Gröbner--Shirshov basis):

**$I_8$ (adjacency correlation).** A reduced word $\sigma_i \sigma_{i+1}$ of length $2$ is absorbed into the single-generator term $\sigma_{i+1}$ when the latter is present. The coefficient of $\sigma_i \sigma_{i+1}$ matches the off-diagonal entry of the transfer matrix product $M_i$ at $\sigma_i$.

Physically, adjacency correlation is the non-commutative coupling between neighbouring crossings. It appears as the off-diagonal entry of the $2 \times 2$ transfer matrix $T(c, d)$ acting on the Hecke state $(a \sigma + b)$. The optimal basis encodes this coupling in the ratio $c_{\sigma_i \sigma_{i+1}} / c_{\sigma_{i+1}}$, a function of $q$ alone.

**$I_9$ (closed shell chain collapse).** A reduced word $w \cdot \sigma_j$ is absorbed when its prefix $w$ is present. Applying this recursively from longest to shortest words collapses the entire normal form to the standard basis $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$.

Physically, each generator $\sigma_i$ contributes a transfer matrix chain $M_i = \prod_{j > i} T_{K_i, K_j}(q)$. The extension $w \cdot \sigma_j$ represents the next step in this chain. Collapsing the chain to a single term $\hat{V}_i = z \cdot (M_i)_{00} + (M_i)_{10}$ yields the Markov-traced volume.

**Necessity of $d \neq 0$ for $I_9$.** Multiplying the normal form by $(c \cdot \sigma_k + d)$ scales every existing word by $d$ and extends each word by $c \cdot \sigma_k$. For every extended word $w \cdot \sigma_k$, the prefix $w$ survives from the $d$-term, allowing $I_9$ to absorb it. This mechanism fails if $d = 0$.

For proton–proton crossings, $d = 0$. Without the prefix, $I_9$ lacks an anchor for chain stripping. The condition $d \neq 0$ holds for neutron–neutron ($d = -(q - q^{-1})$) and proton–neutron ($d = -(q - q^{-1})/2$) crossings. The valley of stability condition $N \geq Z - 1$ ensures at least one $d \neq 0$ crossing at every generator.

## The histogram: universal in $A$

The term-count histogram $h(\ell) = \#\{w : |w| = \ell\}$ tallies reduced words at each length. Verified for $A \leq 8$, this histogram is identical for all $(Z, N)$ at the same $A$ (e.g., ${}^8\mathrm{Be}(4,4)$ and ${}^8\mathrm{Li}(3,5)$).

The histogram depends only on the Iwahori--Hecke algebra $H_A(q)$, factoring as a product of $q$-integers:

See [Table 2](#tbl:groebner-nf-computation-table2-data).

These are $q$-multinomial coefficients. The palindromicity of the histogram polynomial (verified for $A \leq 7$) reflects the Poincaré duality of the Bruhat order on the support.

## The weight distribution: where pairing lives

Unlike the $A$-universal histogram, the weight distribution $W(\ell)$ depends on $(Z, N)$. At constant $A$:

- Even-even nuclei exhibit higher total weight, reflecting stronger coherence from nucleon pairing.
- Odd-odd nuclei exhibit lower total weight, as unpaired crossings weaken the chain anchor.

The ratio $\mathrm{net}(\text{even-even}) / \mathrm{net}(\text{odd-odd})$ quantifies the pairing energy. At $A = 6$, we find $\mathrm{net}({}^6\mathrm{He}(2,4)) / \mathrm{net}({}^6\mathrm{Li}(3,3)) = 6.64 / 4.96 = 1.34$, a $34\%$ pairing enhancement.

In the normal form, adjacent same-type crossings (even occupancy) trigger the Hecke product $\sigma^2 = (q - q^{-1})\sigma + 1$. The generated $\mathbf{1}$ term anchors the $I_9$ chain. Unpaired crossings (odd occupancy) produce only the $\sigma$ term, weakening the anchor and reducing total amplitude.

## The Pauli factor: multi-generator phenomenon

The alternating trace $\mathrm{tr}_{\mathrm{alt}} = \sum_w c_w \cdot (-q^{-1})^{\ell(w)}$ evaluates each word at the alternating eigenvalue $-q^{-1}$. The ratio

$$
  F_{\mathrm{Pauli}}^{(A)}
  = 
  \frac{|\mathrm{tr}_{\mathrm{alt}}(\mathcal{N})|}{|\mathrm{net}(\mathcal{N})|}
$$

measures the normal form amplitude residing in the alternating irrep of $S_A$, the antisymmetric channel governed by Pauli exclusion.

This quantity eludes the $2 \times 2$ transfer matrix. The per-generator transfer matrix has only eigenvalues $q$ and $-q^{-1}$, which are shared by both the symmetric and alternating irreps. Irrep separation demands the multi-generator interaction (e.g., how $\sigma_0$ and $\sigma_1$ act together). This requires the full Gröbner--Shirshov normal form.

## The $6 \times 6$ transfer matrix: no shortcut

One might expect an enlarged $6 \times 6$ transfer matrix (acting on the $H_3(q)$ basis $\{\mathbf{1}, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0\}$) to separate the irreps.

Symbolic proof shows otherwise. The matrix $T_6(c, d) = c \cdot R(\sigma_0) + d \cdot I_6$ possesses exactly two distinct eigenvalues, each with multiplicity $3$:

$$
  \lambda_+ = c \cdot q + d,
  \qquad
  \lambda_- = c \cdot (-q^{-1}) + d.
$$

These match the $2 \times 2$ eigenvalues. The standard irrep contains both eigenvalues because $\sigma_0$ in the standard representation has a $2 \times 2$ matrix with both eigenvalues. The $6 \times 6$ matrix fails to separate the symmetric from the standard irrep, or the alternating from the standard irrep.

The Pauli factor $F_{\mathrm{Pauli}}$ is irreducibly multi-generator. No per-generator transfer matrix can compute it.

Physically, the Pauli exclusion principle acts between pairs of fermions (quarks in a Borromean triplet), not on individual crossings. The multi-generator structure embodies this inter-quark correlation.

Computed witnesses (exact in $\mathbb{Z}[\check{q}, \check{q}^{-1}]$ for $A \leq 12$, displayed at $q_0$):

See [Table 3](#tbl:groebner-nf-computation-table3-data).

For $A \leq 12$, the symbolic witnesses $\mathrm{tr}_{\mathrm{alt}}(\check{q})$, $\mathrm{net}(\check{q})$, $\mathrm{observable}(\check{q})$, and $\mathrm{color}(\check{q})$ are exact Laurent polynomials over $\mathbb{Z}$ in the spinor information rate $\check{q} = q^{1/2}$. The denominator $2^{p_n}$ is tracked separately.

The $H_3(q)$ Pauli factor is $F_{\mathrm{Pauli}} = 0.6382$. The $A$-strand values differ because they capture the full multi-generator interaction rather than the $3$-strand projection.

## Streaming pattern discovery

During inductive construction, the quotient ideals $I_8$ and $I_9$ strip terms at each strand boundary. The engine identifies the most frequent suffix patterns before stripping. These identify candidates for new structural ideals.

For ${}^{16}\mathrm{O}$ at strand $8$, $\sigma_7 \sigma_8$ appeared $52{,}230$ times (the $I_8$ adjacency pattern at the newest generator). The pattern $\sigma_4 \sigma_6 \sigma_7 \sigma_8$ appeared $14{,}262$ times, revealing a $4$-generator chain that skips $\sigma_5$ (a potential $I_{11}$ candidate).

Because the weight distribution $W(\ell)$ and the Pauli accumulator $\mathrm{tr}_{\mathrm{alt}}$ are preserved exactly through stripping, no physical data is lost. The $A$-universal histogram $h(\ell)$ can be computed once from the minimal case $N(1, A-1)$.
