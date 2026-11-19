**Algorithm (Per-partition Springer / Donaldson–Thomas weight $\Delta_\lambda$ and extensive multi-body separation).**
*Evaluate the signed per-partition weight $\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda \in \mathbb{Z}$ for any partition $\lambda \vdash n$ and separate intensive single-trace weights from extensive 3D multi-nucleon binding.*

### Input

- *Braid strand index $n \in \mathbb{N}_{\ge 1}$ and Young partition $\lambda = (\lambda_1 \ge \cdots \ge \lambda_r > 0) \vdash n$ (with conjugate partition $\lambda'$).*

### Output

- *Exact integer weight $\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda \in \mathbb{Z}$, where $n(\lambda) = \sum_{i \ge 1} (i - 1)\lambda_i = \sum_{j \ge 1} \binom{\lambda'_j}{2}$ is the dominance/valuation statistic and $\dim V_\lambda = d_\lambda$ is the Specht module dimension.*

*(Terminological note: for a unipotent element $x \in \mathrm{GL}_n$ of Jordan type $\lambda$, the top cohomology of the Springer fibre $\mathcal{B}_x$ realises the irreducible $S_n$-representation $V_\lambda$ \cite{springer1976}, \cite[Thm.~2.1]{shoji2019}. Both the sign $(-1)^{n(\lambda)}$ and the dimension $d_\lambda$ below follow directly from the categorical Donaldson–Thomas / 3d-index construction without invoking external algebraic-group cohomology.)*

### Algorithm

1. **Compute the valuation parity $n(\lambda)$:** Evaluate $n(\lambda) = \sum_{i=1}^{r} (i - 1)\,\lambda_i \in \mathbb{N}$ and sign $\varepsilon_\lambda = (-1)^{n(\lambda)} \in \{+1, -1\}$.
2. **Compute the Specht dimension $d_\lambda$:** Evaluate the hook-length product $H(\lambda) = \prod_{(i,j) \in \lambda} \bigl(\lambda_i - j + \lambda'_j - i + 1\bigr)$ and divide $n!$ exactly by $H(\lambda)$ to obtain $d_\lambda = \dim V_\lambda \in \mathbb{N}_{\ge 1}$.
3. **Return the signed weight:** Output $\Delta_\lambda = \varepsilon_\lambda \cdot d_\lambda$.

### Termination and Complexity

Computing $n(\lambda)$ takes $O(r) = O(n)$ additions and computing $H(\lambda)$ takes $O(n)$ integer multiplications once $\lambda'$ is tabulated, giving $O(n)$ exact integer operations per partition.

### Intensive-versus-Extensive Separation and Multi-Body Scope

1. **Unconditional per-partition value:** [Donaldson–Thomas index unification](#prop:delta-lambda-dt-index-unification) and [the Wedderburn trace identity](#prop:wedderburn-trace-identity) establish $\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda$ for arbitrary $n \ge 1$ (with the linear-combination structure of [the binding-density remark](#rem:term6-binding-density)).
2. **Why single-trace block weights cannot supply extensive bulk binding:** Because $\sum_{\lambda \vdash n} d_\lambda\,w_\lambda(z) = 1$, a bare single-trace difference $E_0\,\Delta\mathrm{tr}_M$ is intensive ($O(1)$), whereas nuclear binding $B(Z, N)$ scales extensively ($O(A)$). Moreover, at $A = 4$ the exact determinant inequality $(1 - m^2)^6 \le (1 + 3m)(1 - m)^3$ on $m \in [0, 1]$ caps purely pairwise exchange log-determinants at $\binom{4}{2} = 6$, proving that $^4\mathrm{He}$ saturation requires irreducible $\ge 3$-body cumulants. Six historical attempts to absorb extensive nuclear binding into a modified per-block weight $\Delta_\lambda$ alone (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius, level-$0$ crystal-graph, and augmented-Markov ansätze) failed on the deuteron/$\alpha$ scale for this structural reason.
3. **Resolution via multi-scale 3D simplicial and shell structure, and open problems:** In [Step 9b](#alg:per-isotope-binding), extensive bulk and shell energies arise instead from the 3D compact-ball triangulation $(f_0, f_1, f_2, f_3)$ weighted by Convention-D two-body bonds and GPMT three- and four-body Mayer cumulants $(w_3, w_4)$, combined with $(2j + 1)$ spin–orbit subshell filling, Temperley–Lieb seniority pairing, and discrete FCC Coulomb potentials. Two specific derivations in the heavy and sub-nucleonic regimes await first-principles closure: (i) exact coarse-graining of the 12-quark algebra $H_{12}(q)$ onto its cabled four-nucleon parabolic subalgebra $H_3(q)^{\otimes 4}$ ($(3^4)$ cabling) to project inter-$\alpha$ couplings directly from quark-strand braids, and (ii) parameter-free derivation of the prolate Nilsson quadrupole stiffness $\kappa_{\mathrm{Nilsson}}$ from deformed spin–orbit level crossings in open-shell lanthanides and actinides.
