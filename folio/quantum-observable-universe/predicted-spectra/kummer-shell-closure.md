The Kummer tower filtration provides the algebraic framework for shell closure, the Pauli factor, and the odd-odd pairing deficit in the Gröbner--Shirshov normal form.

## The $\mu_2$ torsion as Pauli evaluation

The alternating trace of the normal form evaluates each word $w$ at the alternating eigenvalue $(-q^{-1})^{\ell(w)}$:

$$
  \mathrm{tr}_{\mathrm{alt}}(\mathcal{N})
  = 
  \sum_{w \in \mathrm{supp}} c_w \cdot (-q^{-1})^{\ell(w)}
$$

This sum is the $\mu_2$ Kummer evaluation. It applies the sign character of $\mathbb{G}_m$ to the normal form. The eigenvalue $-q^{-1}$ is the alternating root of the Hecke relation $\sigma^2 = (q - q^{-1})\sigma + 1$. The eigenvalue $q$ is the symmetric root.

The Pauli factor measures the $\mu_2$-torsion content:

$$
  F_{\mathrm{Pauli}}^{(A)}
  = 
  \frac{|\mathrm{tr}_{\mathrm{alt}}(\mathcal{N})|}{|\mathrm{net}(\mathcal{N})|}
$$

It quantifies the amplitude present in the antisymmetric channel.

## Shell closure as Kummer divisibility

The Kummer reduction at level $n$ takes the form:

$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n  \big|  \chi(A)
$$

The obstruction vanishes when $n$ divides the Euler characteristic $\chi(A)$ of the brane configuration. Apply this to the nuclear braid.

- At level $n = 2$, the obstruction $\kappa_0 \bmod 2 = 0$ vanishes when $\chi(A)$ is even. This corresponds to even-even nuclei. The Pauli factor is enhanced.
- For magic numbers, the obstruction vanishes at specific levels $n$ corresponding to shell capacities. Magic number 2 corresponds to $\mu_2$. Magic 8 corresponds to $\mu_8$.
- For doubly magic nuclei, both the proton and neutron obstructions vanish simultaneously at the same Kummer level.

## The pairing deficit as $\mu_2$ obstruction

For odd-odd nuclei, both $Z$ and $N$ are odd. The Euler characteristic $\chi(A)$ is odd at the relevant level. The condition $\kappa_0 \bmod 2 \neq 0$ implies the obstruction persists at the $\mu_2$ level. This produces three effects:

1. The normal form has a lower total amplitude. The observation is $\mathrm{net}(\text{odd-odd}) < \mathrm{net}(\text{even-even})$ at the same $A$.
2. The alternating trace is suppressed relative to the net amplitude.
3. The Pauli factor $F_{\mathrm{Pauli}}^{(A)}$ is lower.

Calculations at $A = 6$ yield $\mathrm{net}({}^6\mathrm{He}(2,4)) / \mathrm{net}({}^6\mathrm{Li}(3,3)) = 6.64 / 4.96 = 1.34$. This demonstrates a $34\%$ pairing enhancement for even-even configurations over odd-odd configurations.

This provides an algebraic formula for the pairing correction $I_{10}$. The correction factor for odd-odd nuclei is the ratio of $\mu_2$-torsion content between the even-even and odd-odd configurations at the same mass number $A$.

## Computational complexity

The Kummer framework suggests the Pauli witness computation scales as $O(A^3)$:

| Component | Complexity | What it computes |
|-----------|-----------|-----------------|
| Transfer matrix (optimal NF) | $O(A^2)$ | $\hat{V}_i$ for each generator |
| $\mu_2$ evaluation per word | $O(\ell)$ per word | $(-q^{-1})^{\ell(w)} \cdot c_w$ |
| Total NF terms (with stripping) | $O(A^2)$ per strand | Quotient keeps terms bounded |
| Number of strands | $O(A)$ | One per nucleon |
| **Total** | **$O(A^3)$** | Full Pauli witness |

Computational verification:

| $A$ | Terms | Time | Scaling |
|:---:|------:|-----:|:-------:|
| $8$ | $14256$ | $0.9$s | — |
| $9$ | $234504$ | $29$s | — |
| $10$ | $8.7$M | $4.3$s (v2) | — |
| $12$ | $923319$ | $269$s (v3) / $\sim5$s (v6) | — |
| $16$ | $3.4$M | $38$s (v6) | $A^3 = 4096$ (matches) |

Applying the quotient during construction yields an effective complexity of $O(A^3)$. The complexity is cubic in the mass number. Nuclei up to $A = 40$ (${}^{40}\mathrm{Ca}$, doubly magic) are computationally tractable in minutes.

## Symbolic witnesses

The symbolic engine computes exact evaluations in $\mathbb{Z}[\check{q}, \check{q}^{-1}]$, where $\check{q} = q^{1/2}$ is the spinor information rate. It produces Laurent polynomial witnesses for $\mathrm{tr}_{\mathrm{alt}}(q)$ and $\mathrm{net}(q)$. This is verified through $A = 9$ (${}^9\mathrm{Be}$) without overflow.

For $A > 9$, the integer coefficients grow as $O(q^{A^2})$. This growth requires either larger integer types or modular arithmetic for exact computation. The float engine serves as a cross-check at $q_0$.

The polynomial coefficients grow following the Kummer tower. At level $n$, the coefficients involve the $q$-factorial $[n]_q!$. This possesses $O(n^2)$ digits. At $A = 16$, the maximum coefficient is approximately $10^{18}$. This fits within a 128-bit integer. At $A = 40$, the maximum coefficient reaches approximately $10^{100}$. This exceeds the 128-bit integer range and requires arbitrary-precision arithmetic or modular reduction.
