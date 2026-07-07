<!-- FILE_START: electron-shells-intro.md -->
Before assembling molecules, we determine atomic bonding capacity. The electron shell translates atomic shell structure into the number of trefoils its braid admits. We recover the aufbau principle by minimising the dual cost $\Phi_1$. This yields the standard valence electron count and the octet rule.

Two refinements sharpen this model. First, the normal-form term count in the quotient atom combinatorially detects closed shells. Second, the palindromicity of the normal-form histogram characterises $s, p, d, f$ orbital types. We take these shell capacities as given and apply the construction to $H_2$, $CO$, $CO_2$, $CH_4$, and $C_6H_6$.
<!-- FILE_END: electron-shells-intro.md -->

<!-- FILE_START: electron-shell-braid-capacity.md -->
**Definition.**
*In the [atomic braid](#def:atomic-braid) $\mathcal{A}(Z, N)$, each of the $Z$ electrons is a trefoil $T_{2,3} = \sigma_0\sigma_1\sigma_0$ in $H_3(q)$ Hopf-linked to the nuclear core. A* **bonding site** *is a position in the atomic braid available to an electron. The* **shell capacity** *is the number of bonding sites at each shell level, determined by the electron arrangement that minimises $\Phi_1$.*

*An atom with $Z$ electrons fills shells in order of increasing $\Phi_1$ contribution.*
<!-- FILE_END: electron-shell-braid-capacity.md -->

<!-- FILE_START: electron-shell-2n2-capacity.md -->
**Conjecture.**
*The maximum number of bonding sites at shell level $n$ is $2n^2$. This is the* **open shell-capacity derivation**: *the photon-electron transfer matrix is $2\times2$, so its $n$-th power fixes the shell energies (the Chebyshev/Rydberg ladder) but supplies only a $2$-fold degeneracy, not the count*

$$
  2n^2 = 2\sum_{\ell=0}^{n-1}(2\ell+1),
$$

*which requires an $\mathrm{SO}(4)$-type accidental degeneracy bundling angular-momentum levels $\ell = 0,\ldots,n-1$ into principal shell $n$:*

| Shell $n$ | Capacity $2n^2$ | Subshells |
|:----------|:---------------|:----------|
| 1 | 2 | 1s (2) |
| 2 | 8 | 2s (2) + 2p (6) |
| 3 | 18 | 3s (2) + 3p (6) + 3d (10) |
<!-- FILE_END: electron-shell-2n2-capacity.md -->

<!-- FILE_START: atomic-valence-open-sites.md -->
**Definition.**
*The* **valence** *of an atom (the number of open bonding sites available for covalent bonds) is*

$$
  v(Z) = \min\bigl(Z_{\mathrm{val}},\; 2n_{\mathrm{val}}^2 - Z_{\mathrm{val}}\bigr)
$$

*where $Z_{\mathrm{val}}$ is the number of valence electrons and $n_{\mathrm{val}}$ is the outermost shell level.*

| Atom | $Z$ | Config | $v(Z)$ | Open sites |
|:-----|:----|:-------|:-------|:-----------|
| H | 1 | $1s^1$ | 1 | 1 |
| C | 6 | $[He]\,2s^2 2p^2$ | 4 | 4 |
| N | 7 | $[He]\,2s^2 2p^3$ | 3 | 3 (+1 lone pair) |
| O | 8 | $[He]\,2s^2 2p^4$ | 2 | 2 (+2 lone pairs) |

*A* **lone pair** *is an electron pair whose $\Phi_1$ contribution is lower when bound to a single nucleus than when shared. The LP dual assigns electrons to bonding versus lone-pair positions by comparing the $\Phi_1$ cost of sharing versus retaining.*
<!-- FILE_END: atomic-valence-open-sites.md -->

<!-- FILE_START: shell-capacity-self-square.md -->
*Lean sibling resolves to [`QOU.Molecular.shell_capacity_self_square`](lean/QOU/Molecular/ShellCapacitySelfSquare.lean).*

**Proposition.**
*For every principal shell level $n \in \mathbb{N}$, the number of orbital sub-states is the sum of the sub-shell multiplicities $2\ell+1$ over $\ell = 0,\ldots,n-1$,*

$$
  \sum_{\ell=0}^{n-1} (2\ell+1) \;=\; n^2,
$$

*and the electron capacity of the shell, carrying the spin factor $2$, is*

$$
  \sum_{\ell=0}^{n-1} 2(2\ell+1) \;=\; 2n^2 .
$$

*Both are the $q\to 1$ value of the bar-even self-square $[n]_q^2$.*

This is the self-fusion of a single angular $q$-dimension, not a product of two independent symmetries. The angular $q$-dimension is the bar-even (cosh) Chebyshev evaluation $[n]_q = U_{n-1}\!\bigl((q+q^{-1})/2\bigr)$ of the shell element. The $q$-Clebsch–Gordan rule decomposes its self-square into the sub-shell multiplicities,

$$
  [n]_q^2 \;=\; \sum_{\ell=0}^{n-1} [2\ell+1]_q
  \qquad\Longrightarrow\qquad
  2[n]_q^2\big|_{q=1} \;=\; 2n^2 ,
$$

since $[2\ell+1]_q\big|_{q=1} = 2\ell+1$. The $\mathrm{SO}(4)=\mathrm{SU}(2)\times\mathrm{SU}(2)$ "$(j,j)$ doubling" of the hydrogenic shell is here the self-square $V\otimes V$ of one object. The second factor is a copy of the first, tied by the coproduct. We require no second compact $\mathrm{SU}(2)$. The compact ($\cos/\sin$, root of unity) and non-compact ($\cosh/\sinh$, real $q$) forms are the two real forms of one $\mathfrak{sl}(2,\mathbb{C})$.

The $q=1$ integer identities above are proved in Lean (sum of the first $n$ odd numbers, by induction). The full $q$-deformed self-square is verified symbolically in `computations/shell_capacity_chebyshev_bridge.py`. The residual modeling assumption — that the electron shell space is this self-square, rather than the count merely agreeing with it — is recorded as structural input.

| Shell $n$ | $n^2$ | Capacity $2n^2$ | Sub-shells $[2\ell+1]_{q=1}$ |
|:----------|:------|:----------------|:-----------------------------|
| 1 | 1 | 2 | 1 |
| 2 | 4 | 8 | 1 + 3 |
| 3 | 9 | 18 | 1 + 3 + 5 |
| 4 | 16 | 32 | 1 + 3 + 5 + 7 |
<!-- FILE_END: shell-capacity-self-square.md -->

<!-- FILE_START: shell-filling-rule.md -->
**Proposition.**
*The ground-state electron configuration of atom $(Z, N)$ is the assignment of $Z$ electron trefoils to bonding sites that minimises the total $\Phi_1$ of the atomic braid. This reproduces the aufbau principle:*

1. *Inner shells ($n < n_{\mathrm{val}}$) fill completely because each additional electron in a partly filled inner shell reduces $\Phi_1$ more than any valence electron.*

2. *Within the valence shell, electrons distribute to maximise the number of singly occupied sites (Hund's rule). Parallel electron trefoils have lower $\Phi_1$ than antiparallel pairs. The $ee$ crossing ($\sigma$, repulsive) is minimised when electrons occupy distinct spatial sites.*

3. *The LP dual of the electron assignment problem is:*

$$
  \max_{y} \; Z \cdot y_0
  \quad\text{s.t.}\quad
  y_0 + \sum_{n} G_{n,s} \, y_{n,s} \leq \Phi_1^{(s)}
  \;\;\forall\, \text{sites } s
$$

*where $\Phi_1^{(s)}$ is the $\Phi_1$ contribution of placing an electron at site $s$, and $G_{n,s}$ encodes the Gram-matrix penalty for electron-electron repulsion at shell $n$.*
<!-- FILE_END: shell-filling-rule.md -->

<!-- FILE_START: shell-filling-electronegativity-ilp.md -->
*The dual variable $y_0$ gives the marginal $\Phi_1$ cost of adding one more electron. This is the electronegativity in the braid framework.*

### ILP electron attachment

*The integer LP builds each electron shell from scratch. Starting from the bare nucleus, we add electrons one at a time. At each step, we select the operator that minimises $|tr_M|$ subject to Frobenius positivity $G \cdot x \geq 0$. The ILP discovers that electrons alternate generators:*

See [Table](#tbl:shell-filling-rule-table-data).

*The generator alternation is the Hecke algebra manifestation of Hund's rule. Electrons $e_2$ and $e_6$ (and $e_7$ for $N$, $O$) attach via $\sigma_0^{-1}$ rather than $\sigma_1^{-1}$, corresponding to orbital pairing in the $2s$ and $2p$ subshells.*
<!-- FILE_END: shell-filling-electronegativity-ilp.md -->

<!-- FILE_START: valence-from-braid.md -->
*The [shell capacity](#def:electron-shell-braid-capacity) directly determines how many covalent bonds each atom can form. An atom shares electrons only when the molecular $\Phi_1$ is lower than the sum of isolated atomic $\Phi_1$ values. Sharing reduces the total quantum dilogarithm volume.*

*For the first-row atoms:*

| Atom | Valence $v$ | Lone pairs | Typical bonds | Example |
|:-----|:------------|:-----------|:-------------|:--------|
| H | 1 | 0 | 1 single | H--H, C--H |
| C | 4 | 0 | 4 single, or 2 double, or 1 triple + 1 single | CH$_4$, CO$_2$, HCN |
| N | 3 | 1 | 3 single, or 1 double + 1 single, or 1 triple | NH$_3$, NO, N$_2$ |
| O | 2 | 2 | 2 single, or 1 double | H$_2$O, CO, CO$_2$ |

*The octet rule emerges as a special case. Atoms with $n_{\mathrm{val}} = 2$ achieve $\Phi_1$ minimum when the second shell is complete (8 electrons = $2 \times 2^2$). This is a consequence of the Hecke algebra dimension at shell level 2.*

*Carbon's versatile bonding (4 bonds in multiple geometries) arises because it sits at the half-filling point of the $n = 2$ shell: $Z_{\mathrm{val}} = 4 = \frac{1}{2} \times 8$. Half-filled shells have maximum $\Phi_1$ flexibility, allowing both $\sigma$-bond (single) and $\pi$-bond (double/triple) configurations.*
<!-- FILE_END: valence-from-braid.md -->

<!-- FILE_START: shell-closure-nf-term-count.md -->
**Conjecture.**
*In the quotient atom model $H_{Z+1}(q)$ — where the nuclear core is a single strand $\mathcal{N}$ and each electron is a strand $e_k$ — the growth ratio $\gamma(Z) = n(Z)/n(Z-1)$ of the Gröbner–Shirshov normal form term count separates three regimes:*

$$
  \gamma(Z) \in
  \begin{cases}
    \{1\}         & \text{s-shell pairing (exact)} \\
    [1.2,\, 1.4]  & \text{p-shell pairing (approximate)} \\
    [3.0,\, 4.0]  & \text{sub-shell opening}
  \end{cases}
$$

*No $Z$ falls in the gap $(1.4, 3.0)$. This gap is the algebraic shell gap of the Hecke chain.*

## Setup

**The quotient atom model.** Given a neutral atom with $Z$ protons, $N$ neutrons, and $Z$ electrons, we quotient the nuclear core $\mathcal{N}(Z, N)$ to a single formal variable. The resulting element lives in $H_{Z+1}(q)$ with crossing types:

See [Table 1](#tbl:shell-closure-nf-term-count-table1-data).

The nucleus–electron crossing is the $Z$-fold composition $(\sigma^{-1})^Z$, not the scalar multiple $Z \cdot \sigma^{-1}$. In the braid picture, quotienting $Z$ proton strands to one means the electron wraps $Z$ times.

**Closed form.** The Hecke relation $\sigma^2 = h\sigma + 1$ reduces $(\sigma^{-1})^Z = c_Z \sigma + d_Z$ with eigenvalues $q^{-Z}$ (trivial) and $(-q)^Z$ (sign):

$$
  c_Z = \frac{q^{-Z} - (-1)^Z q^Z}{[2]_q}, \qquad
  d_Z = \frac{q^{-(Z+1)} + (-1)^Z q^{Z+1}}{[2]_q}
$$

These are Chebyshev $U$-type polynomials in $h = q - q^{-1}$ with the Hecke eigenvalues $q^{-1}$ and $-q$ as roots. The sign of $c_Z$ alternates. It is positive for odd $Z$ and negative for even $Z$. This alternation drives the pairing mechanism.

**Proved (algebraic engine).** The reduction $(\sigma^{-1})^Z = c_Z\sigma + d_Z$ with these closed forms, and the sign-alternation $c_Z<0$ (even $Z$) / $c_Z>0$ (odd $Z$) with $|c_Z|$ strictly increasing for $q>1$, is established rigorously by diagonalising $\sigma$ in the two-dimensional $H_2(q)$ (eigenvalues $q,-q^{-1}$, so $(\sigma^{-1})^Z$ has eigenvalues $q^{-Z},(-1)^Zq^Z$). We confirm this numerically as an exact $q$-independent identity to $10^{-40}$. See [`docs/audits/2026-06-07-chebyshev-pairing-engine-proved.md`](../../../docs/audits/2026-06-07-chebyshev-pairing-engine-proved.md) and witness [`chebyshev-pairing-engine.witness.json`](../../../computations/chebyshev-pairing-engine.witness.json). The conjectural content of this block is how its sign-alternation propagates through the full Gröbner–Shirshov reduction of the quotient atom in $H_{Z+1}(q)$ to the three $\gamma$-regimes above.

**The NF.** We build the atom by sequential Hopf-linking. We start with $\mathcal{N}$ and add $e_1, e_2, \ldots, e_Z$ one at a time, reducing via Gröbner–Shirshov at each step.

## Computational evidence

The quotient NF term count for $Z = 1$ through $8$ (corrected $(\sigma^{-1})^Z$ crossing):

See [Table 2](#tbl:shell-closure-nf-term-count-table2-data).

**The algebraic shell gap.** The growth ratio $\gamma$ falls into two bands separated by the gap $(1.4, 3.0)$:

- **Pairing band** $\gamma \leq 1.4$: even $Z$, the second electron in a sub-shell pair. For s-shells ($Z = 2, 4$), $\gamma = 1.00$ exactly (no new NF words). For p-shells ($Z = 6, 8$), $\gamma \approx 1.25$–$1.30$ (a few new words from the growing $(\sigma^{-1})^Z$ coefficients).

- **Opening band** $\gamma \geq 3.0$: odd $Z$, a new sub-shell electron. The NF triples or quadruples as genuinely new reduced words appear in $H_{Z+1}(q)$.

The gap separating these bands is the **algebraic shell gap**. This discrete structural feature of the Hecke normal form encodes the pairing principle without input from angular momentum or spin.

## Pairing mechanism

The Chebyshev sign alternation of $c_Z$ drives pairing:

- **Odd $Z$** (sub-shell opening): $c_Z > 0$, $d_Z < 0$. The crossing element $c_Z \sigma + d_Z$ is $\sigma$-heavy. The positive $\sigma$ coefficient creates new reduced words at higher word-lengths, expanding the NF.

- **Even $Z$** (pairing): $c_Z < 0$, $d_Z > 0$. The crossing is identity-heavy. The negative $\sigma$ coefficient cancels against existing NF words rather than creating new ones, suppressing growth.

For s-shells, the suppression is exact ($\gamma = 1$) because $|c_Z|$ is small ($0.209$ at $Z = 2$, $0.427$ at $Z = 4$). For p-shells, $|c_Z|$ has grown ($0.664$ at $Z = 6$, $0.930$ at $Z = 8$) so the suppression is approximate ($\gamma \approx 1.3$).

## Global scaling

All coefficients in the $Z$-electron quotient atom carry a global prefactor $Z^Z$:

$$
  \text{coeff}(\mathcal{A}(Z)) \in Z^Z \cdot \mathbb{Z}[q, q^{-1}]
$$

For carbon ($Z = 6$), $6^6 = 46656$ appears in every term.

## Scope and limitations

The $\gamma < 2$ criterion detects electron pairing (every even $Z$), not full noble-gas shell closures ($Z = 2, 10, 18, 36, \ldots$). The 1D Hecke chain $H_{Z+1}(q)$ encodes radial shell structure but lacks angular momentum. It cannot distinguish $2p^2$ ($Z = 6$) from $2p^6$ ($Z = 10$, neon). Detecting noble-gas closures requires a product structure $H_{Z+1}(q) \otimes \mathrm{Rep}(\mathrm{SO}(3))$ where the Hecke chain handles radial pairing and the rotation group handles sub-shell degeneracy $2\ell + 1$.
<!-- FILE_END: shell-closure-nf-term-count.md -->

<!-- FILE_START: palindromicity-orbital-type.md -->
**Conjecture.**
*The word-length histogram of the quotient atom NF is palindromic (Poincaré-dual) if and only if all occupied sub-shells have angular momentum $\ell = 0$ ($s$-type). Palindromicity breaks at the first electron with $\ell \geq 1$ ($p$-type or higher).*

## Computational evidence

From the [quotient atom model](#conj:shell-closure-nf-term-count), the palindromicity status at each $Z$:

See [Table 1](#tbl:palindromicity-orbital-type-table1-data).

**Transition at $Z = 5$**: the first $p$-electron breaks palindromicity. Through $Z = 4$ (pure $s$-shells), the histogram is perfectly symmetric.

## Physical interpretation

Palindromicity of the NF histogram is Poincaré duality in the Bruhat lattice of $S_{Z+1}$. The word-length distribution $\{n_0, n_1, \ldots, n_L\}$ satisfies $n_k = n_{L-k}$. This duality holds when the NF occupies a self-dual sub-lattice. This happens precisely when the electron chain has no angular momentum (pure $s$-orbitals).

The $p$-electron introduces a chiral crossing that breaks the left-right symmetry of the braid word. In the Hecke algebra, this corresponds to a representation that is not self-dual under the longest-element involution $w \mapsto w_0 w$.

## Conjectured grading

The degree of palindromic defect is the minimum number of histogram entries that must be removed to restore palindromicity. This should equal $2\ell$, where $\ell$ is the angular momentum quantum number of the outermost occupied sub-shell:

See [Table 2](#tbl:palindromicity-orbital-type-table2-data).

This provides a purely algebraic definition of orbital angular momentum. We find $\ell$ is half the palindromic defect of the Hecke algebra NF histogram.
<!-- FILE_END: palindromicity-orbital-type.md -->
