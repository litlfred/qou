<!-- FILE_START: lepton-meson-parallel.md -->
Leptons and mesons occupy dual positions in the Hecke hierarchy. Both are indexed by the torus-knot family $T(2,n)$. Both participate in a mass-ratio tower governed by hyperbolic volume. Both feature the flavor transition $3 \to 5$ (electron $\to$ muon; $d$-quark $\to$ $s$-quark).

This duality exchanges fundamental particles (leptons, single strand) with composite bound states (mesons, quark–antiquark pair). It exchanges highest-weight representations with lowest-weight representations.

## The torus-knot dictionary

| | Lepton sector | Meson sector |
|---|---|---|
| **Hecke level** | $H_2(q)$ (2-strand) | $H_3(q)$ (3-strand) |
| **Braid** | $\sigma_1^n$ (torus knot $T(2,n)$) | $(\sigma_1\sigma_2)^2 \cdot \sigma_2\sigma_1$ (Hopf-bound pair) |
| **Valence** | 1 (fundamental) | 2 (quark–antiquark composite) |
| **First generation** | $\mathfrak{e}$: $n = 3$ (trefoil) | $\pi$: quark pair $\bar{u}d$, 6 crossings |
| **Second generation** | $\mu$: $n = 5$ (cinquefoil) | $K$: quark pair $\bar{u}s$, 8 crossings |
| **Third generation** | $\tau$: $n = 7$ (septafoil) | $\eta, \phi$: heavy-strange, 10 crossings |
| **Flavor transition** | $3 \to 5$: $\mathfrak{e} \to \mu$ | $3 \to 5$: $d \to s$ (same torus-knot step) |
| **Mass ratio** | $m_\mu / m_\mathfrak{e} = \mathrm{Vol}(4_1) / \hbar_q^2$ | $m_K / m_\pi = \;?$ |
| **Weight type** | highest weight ($\sigma^n$ saturates positive eigenvalue) | lowest weight ($\sigma^{-1}$ crossings in binding) |

## The highest-weight / lowest-weight duality

In the lepton sector, the braid representative $\sigma_1^n$ is a positive-crossing word. In the Hoefsmit seminormal basis, the eigenvalue of $\sigma_i$ on the trivial (highest-weight) partition $(n)$ is $q$. This is the positive Hecke eigenvalue. The lepton mass formula evaluates the Markov trace on this highest-weight strand. The torus knot $T(2,n)$ lives entirely in the $\sigma \mapsto q$ eigenspace.

In the meson sector, the binding Hopf link introduces negative crossings via $\sigma^{-1} = \sigma - h$. The Hecke normal form $\mathfrak{M}_+$ has its dominant contribution from $L_+$ (coefficient $h^2 + 1 \approx 1.044$). This is the lowest-weight Hecke basis element because $L_+ = \sigma_1\sigma_2$ mixes both eigenspaces through the off-diagonal Hoefsmit blocks.

The duality is:

$$
\text{lepton: } \sigma^n \;\longleftrightarrow\;
\text{meson: } (\sigma\sigma^{-1})^k \cdot \sigma
$$

The lepton evaluates the top of the Hecke spectrum ($q$-eigenvalue). The meson evaluates the full spectrum through binding (both $q$ and $-q^{-1}$ eigenvalues participate).
<!-- FILE_END: lepton-meson-parallel.md -->

<!-- FILE_START: lepton-meson-torus-knot-dictionary.md -->
**Proposition (torus-knot dictionary).**
*The lepton and meson mass towers are both indexed by torus knots $T(2, n)$ for $n = 3, 5, 7, \ldots$ (odd primes). We establish the following correspondence:*

| Generation | $n$ | Lepton ($H_2$) | Quark flavor ($H_3$) | Meson ($q\bar{q}$) |
|---|---|---|---|---|
| 1st | 3 | $\mathfrak{e}$ (electron) | $u, d$ | $\pi$ (pion) |
| 2nd | 5 | $\mu$ (muon) | $s$ (strange) | $K$ (kaon) |
| 3rd | 7 | $\tau$ (tau) | $s$ (heavy-strange) | $\eta, \phi$ |

*The lepton at generation $k$ is the closure of $\sigma_1^{2k+1}$ in $H_2(q)$. The meson at the same generation is the Hopf-bound pair of quarks whose flavor content involves $T(2, 2k+1)$ crossing structure in $H_3(q)$.*
<!-- FILE_END: lepton-meson-torus-knot-dictionary.md -->

<!-- FILE_START: c-equals-bar-iff-all-1dim.md -->
**Proposition ($C = \mathrm{bar}$ iff all irreps are one-dimensional).**
*On the Iwahori--Hecke algebra $H_n(q)$, charge conjugation $C\colon \sigma_i \mapsto \sigma_i^{-1}$ and the bar involution $\mathrm{bar}\colon q \mapsto q^{-1}$ agree on all irreducible characters if and only if every irreducible representation of $H_n(q)$ is one-dimensional.*

*At $H_2(q)$ (leptons), $C = \mathrm{bar}$. At $H_3(q)$ (mesons, baryons), $C \ne \mathrm{bar}$.*
<!-- FILE_END: c-equals-bar-iff-all-1dim.md -->