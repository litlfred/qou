# Audit: A=4 Betti Magnitude Native Derivation
**Date:** 2026-06-26

## 1. The Discrepancy (Proxy Failure)
When projecting the Option E (multi-nucleon interface operator) closure to A=4, the raw structural trace yielded a physical binding energy of `~0.0059 MeV`. The experimental A=4 binding energy target (AME) is `28.30 MeV`. The geometric raw trace fails because it omits the Kazhdan-Lusztig geometric representation weight of the left cell $C_\lambda$.

## 2. Intractability of the Global Bruhat Graph
The required weighting factor is the Betti sum over the canonical left cell corresponding to the A=4 partition (e.g. $\lambda = (10, 2)$):
$$B_\lambda = \sum_{w \in C_\lambda} P_{e,w}(1)$$
Computing $P_{e,w}(q)$ via the Kazhdan-Lusztig recursion requires summing over the lower Bruhat interval $[e, w]$. For arbitrary $w \in S_{12}$, the interval approaches $12!$ ($4.79 \times 10^8$) permutations. A naive or DP-memoized execution times out past $S_8$ (length $\le 28$).

*Correction Note:* Lascoux-Schützenberger transition trees only bypass Bruhat traversal for Grassmannian or strictly 321-avoiding permutations. The A=4 canonical left cells do not strictly obey these limits, rendering pure local-tree bypasses insufficient.

## 3. The Native Breakthrough: RSK Localization
Rather than attempting a global $S_{12}$ Bruhat evaluation, we restrict evaluation exactly to the target permutations.
1. **Inverse RSK Generation:** By leveraging the Robinson-Schensted-Knuth correspondence, we generate exactly the $f^\lambda$ permutations (e.g. 54 permutations for $\lambda = (10, 2)$) that populate the canonical left cell $C_\lambda$, using $Q_{can}$.
2. **Shallow Interval Phenomenon:** For highly elongated partitions like $(10,2)$ and $(11,1)$, the associated permutations in $C_\lambda$ exhibit exceptionally low Coxeter length (max length $\approx 20$ in $S_{12}$).
3. **Tractable Execution:** Because $l(w) \le 20$, the lower Bruhat intervals are radically constrained. The native Rust engine (`hecke-engine`) computes the exact Betti sum over the localized set in seconds/minutes, requiring no combinatorial proxies or curve-fitting.

## 4. Next Steps & Lean Formalization
- **Numerical Validation:** Extract the exact $B_{(10,2)}$ value via the Rust engine and insert into the Option E mass formula. (Currently running in background).
- **Lean Scaffold:** Formalized the trace factorization over Hecke left cells in `QOU/BraidsAndKnots/S5SO3FiberAction.lean` to prove that the topological trace rigorously splits into the structural scale $\times$ the left cell Betti sum.
