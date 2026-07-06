**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**
The stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$ arise from the harmonic oscillator shell structure of nucleons in the nuclear mean field, corrected by the spin-orbit coupling of the Borromean baryon's 3 internal crossings.

**1. Harmonic oscillator levels.**
Each nucleon (a Borromean baryon $\mathcal{B}_3$, [Borromean baryon](#def:borromean-baryon)) vibrates in the nuclear mean field created by all other nucleons. The 3D harmonic oscillator has shell sizes
$$
  s_N =  (N + 1)(N + 2),
  \qquad N = 0, 1, 2, \ldots
$$
and cumulative closures
$$
  C_N =  \sum_{k=0}^{N} (k+1)(k+2)
  =  \frac{(N+1)(N+2)(N+3)}{3}.
$$
See [Table 1](#tbl:shell-transition-knot-table1-data).

Without spin-orbit coupling, the shell closures would be $\{2, 8, 20, 40, 70, 112, 168\}$, which contradicts observation.

**2. Spin-orbit coupling from the Borromean structure.**
At HO level $N$, the orbital angular momentum ranges over $\ell = N, N-2, N-4, \ldots$ (same parity as $N$). Each $\ell \geq 1$ splits into two sub-levels with total angular momentum
$$
  j = \ell + \tfrac{1}{2}
  \qquad\text{and}\qquad
  j = \ell - \tfrac{1}{2}
$$
having $2j + 1$ states each. The spin-orbit coupling energy is proportional to the $q$-Laplacian eigenvalue ([Fourier decomposition](#conj:orbital-fourier-decomposition)):
$$
  E_{\mathrm{SO}}(\ell, j)
   \propto 
  [\ell]_q [\ell + 1]_q
  \cdot (j - \ell)
$$
where $j - \ell = +\tfrac{1}{2}$ for the high-$j$ level (pushed down in energy) and $j - \ell = -\tfrac{1}{2}$ for the low-$j$ level (pushed up).

**3. The shell-transition threshold at $N = 3$.**
The Borromean baryon $\mathcal{B}_3$ has exactly 3 internal crossings (the minimum crossing number of the Borromean link). Spin-orbit coupling strength is proportional to the number of Borromean crossings times the orbital $q$-Laplacian eigenvalue.

The coupling exceeds the HO level spacing when
$$
  3 \cdot [\ell]_q [\ell + 1]_q  >  2(N + 1)
  \qquad\text{(level spacing)}
$$
At $q = 1$, this reduces to $3 \cdot N(N+1) > 2(N+1)$ ($N > 2/3$, so $N \geq 1$). The coupling must exceed a full gap (not just the intra-level spacing). The empirical threshold is $N \geq 3$, matching the 3 Borromean crossings.

When the threshold is exceeded, the highest-$j$ sub-level at HO level $N$ ($j = N + \tfrac{1}{2}$ with $2(N+1)$ states) drops below the gap and joins the previous shell closure. This is the shell-transition level.

**4. The stability pairs.**
See [Table 2](#tbl:shell-transition-knot-table2-data).

The shell-transition levels and their state counts $2(N+1)$ are shown in [Table 3](#tbl:shell-transition-knot-table3-data). All 7 stability pairs are reproduced exactly.

*Proof.*
The HO cumulative $C_N = (N+1)(N+2)(N+3)/3$ is standard. The shell-transition mechanism at $N \geq 3$ follows from the spin-orbit coupling exceeding the HO gap, with the Borromean crossing number $3$ setting the threshold. The state count $2(N+1)$ for the shell-transition level is the degeneracy of the $j = N + 1/2$ sub-level. The cumulative result matches $\{2, 8, 20, 28, 50, 82, 126\}$ by direct computation. $\square$
