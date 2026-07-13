## Proof

The Habiro ring $\widehat{\mathbb{Z}[q]}$ is by definition the
inverse limit $\varprojlim_n \mathbb{Z}[q]/((q;q)_n)$; an element is
specified by a coherent sequence of cyclotomic remainders
\cite{habiro2004}. Existence of the
expansion: the Markov trace of a finite braid word in the standard
Hecke generators $\sigma_i$ lies in $\mathbb{Z}[q^{± 1/2}]$ after
clearing the cyclotomic denominators that arise from the Wedderburn
weights $w_\lambda(q) = \dim_q(\lambda)^2/[n]_q!$ (Markov–Jones
integrality, \cite{jones1987} Thm 3). Sequential cyclotomic division
by $(1 - q^{m+1})$ produces the unique sequence
$\{a_m\} \subset \mathbb{Z}[q^{± 1}]$ with $\deg_q a_m \leq m$
([atomic Habiro expansion](#cor:habiro-expansion-atomic), Step 2).
Property (1) is immediate from $(q;q)_m(\zeta_n^{(j)}) = 0$ for
$n \leq m$. Property (2) is the definition of the Habiro topology.
Property (3) is the termination clause of the atomic case. $\square$

## Inadequacy of the previous wording

Two specific failures of the "meromorphic on $\mathbb{C}$" picture:

1. **Density on $S^1$.** The set
 $\{\zeta_n^{(j)} : \gcd(j,n)=1, n \geq 2\}$ is dense in $S^1$.
 A meromorphic function on a connected open set has only
 isolated poles; with poles dense in $S^1$ the only consistent
 picture is that $S^1$ is a natural boundary, and there is no
 single connected meromorphic continuation across it. The Habiro
 ring sidesteps this by working in the cyclotomic completion of
 $\mathbb{Z}[q]$, where evaluation at each root of unity is
 defined polynomially without any complex-analytic continuation.
2. **Convergence.** The Cauchy-kernel partial sum
 $\sum_{n \leq N} \sum_j r_n^{(j)}/(q - \zeta_n^{(j)})$ does not
 converge uniformly on any neighbourhood that crosses $S^1$.
 The Habiro expansion converges in the $q$-adic
 $((q;q)_\bullet)$-topology by construction, and reduces
 modulo $(q;q)_m$ at every truncation order.

This proposition replaces the earlier "meromorphic with poles at
all primitive roots of unity" wording with the algebraically
correct Habiro-ring statement; the residue spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) is
retained as the **symbolic feeding lemma** that produces the
cyclotomic coefficients $a_m$ from the Wedderburn-stratum residues
$r_n^{(j)}$, but is no longer claimed to define a global
$\mathbb{C}$-meromorphic function.
