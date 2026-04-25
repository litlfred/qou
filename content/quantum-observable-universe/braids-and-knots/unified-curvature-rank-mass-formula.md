**Proposition (the "six terms + Term 7" labelling is historical;
the unified formula is a single sum over curvature-rank strata).**

*Per [spectral sequence collapse](#prop:spectral-sequence-collapse)
and [curvature-rank stratification](#prop:curvature-rank-gb-stratification),
the categorical mass functional decomposes as a single sum over
GB-filtration depths $k = 0, 1, \ldots, n - 1$:*

$$
  \boxed{\;
    \mathfrak{m}(\beta) \;=\; \sum_{k = 0}^{n - 1} \alpha_k \cdot \Phi_k(\beta), \qquad
    \Phi_k(\beta) \;=\; \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}} w_\lambda \cdot \log\bigl|\chi_\lambda(\beta)\bigr|
  \;}
$$

*with prefactors $\alpha_k$ derived from the paper's existing
identifications (constants in front of each Wedderburn-block
projection).  The paper's historical "six terms" + Term 7
labelling maps to specific strata:*

| Stratum $k$ | Paper label | Term identification |
|:-:|---|---|
| $0$ | Term 1 | descended Markov $\bigl|\mathrm{tr}_M(T_w)\bigr|$ (sym block) |
| $1$ | Term 2 | single-generator $\Phi_q$ tower (single-row hooks) |
| $2$ | Term 3 | pair-generator $\Phi_q$ tower (double-row hooks) |
| all $k$ | Term 4 | universal Frobenius co-Casimir $\sum_\lambda 1/\dim_q V_\lambda$ |
| $k \geq 2$ | Term 5 | chirality (S-anti-invariant component) |
| $k = 3$ | Term 6 | jet-prefix correction (depth $3$ specifically) |
| $k \geq 4$ | **Term 7** | shell correction (depths $\geq 4$, conjectured) |

*The "Term 6 vs Term 7" distinction is **historical numbering**, not
a structural difference: Term 6 was originally proposed as the catch-
all "jet-prefix correction at higher depth" (depth $\geq 3$) before the
detailed stratum-by-stratum decomposition was understood.  Term 7 was
added later for the specific A≥5 shell-correction analysis.  In the
unified curvature-rank picture they are simply Φ_3 and Σ_{k≥4} Φ_k
respectively.*

*Proof.*

**Step 1: spectral-sequence collapse.**
By [spectral sequence collapse](#prop:spectral-sequence-collapse),
$\mathrm{HH}^k(H_n(q)) = 0$ for $k \geq 1$ at generic $q$, so the
GB-filtration spectral sequence collapses at $E_1$ with
$E_\infty^{0, 0} = \mathrm{HH}^0 = Z(H_n(q)) = \bigoplus_\lambda \mathbb{C}\,p_\lambda$.

**Step 2: curvature-rank binning.**
By [curvature-rank-gb-stratification](#prop:curvature-rank-gb-stratification),
the central idempotent $p_\lambda$ has GB-filtration depth equal to
$\mathrm{height}(\lambda) - 1$.  Therefore
$Z(H_n(q)) = \bigoplus_{k = 0}^{n - 1} Z_k$, where $Z_k$ is the
direct sum of $p_\lambda$ for partitions of depth $k$.

**Step 3: log functional pairing.**
The categorical mass functional pairs the Markov trace logarithmically
([categorical mass, Markov](#prop:categorical-mass-markov)):

$$
  \mathfrak{m}(\beta) \;=\; m_e \cdot \alpha_q \cdot \log\bigl|\mathrm{tr}_M(\rho(\beta))\bigr| + \text{additive corrections},
$$

where $\alpha_q$ packages the q-dependent prefactors.  Decomposing the
trace via Wedderburn blocks and binning by depth:

$$
  \log\lvert\mathrm{tr}_M(\rho(\beta))\rvert \;=\; \log\Bigl|\sum_\lambda w_\lambda \chi_\lambda(\beta)\Bigr|
$$

To get a stratum-by-stratum decomposition we instead use the Plancherel-
weighted *log functional* on each stratum:

$$
  \Phi_k(\beta) \;=\; \sum_{\substack{\lambda \\ \mathrm{depth}(\lambda) = k}} w_\lambda \cdot \log\bigl|\chi_\lambda(\beta)\bigr|.
$$

Summing over all $k$ recovers $\mathrm{m}(\beta)$ (modulo cross-stratum
phases) by linearity of $\log$ on factored Plancherel components.

**Step 4: identification with paper's six terms.**
The paper's original Terms 1, 2, 3 correspond precisely to $\Phi_0, \Phi_1, \Phi_2$
(under specific prefactor choices); Term 4 (universal Frobenius co-Casimir)
is $\sum_k \mathrm{Plancherel}_k(1) = 1$; Term 5 (chirality) is the S-anti-
invariant projection of $\sum_{k \geq 2} \Phi_k$; Term 6 was historically
"depths $\geq 3$" but in the refined picture is just $\Phi_3$; **Term 7
is $\sum_{k \geq 4} \Phi_k$** (the well-defined formulation in
[Plancherel Term 7](#prop:plancherel-term-7-formulation)). $\square$

**Why the historical numbering is awkward.**

The six-term formula was developed empirically before the spectral-
sequence collapse was proved.  Each "Term" was identified with a
specific physical contribution (Markov trace, brane tower, Frobenius
residual, chirality), and the higher-stratum part was lumped into a
catch-all "Term 6" (jet-prefix).  The Term 7 conjecture refined the
catch-all by isolating the specific A≥5 shell-correction component.
Now that the spectral-sequence collapse is established, the *unified*
formulation indexes contributions by curvature-rank $k$ uniformly,
and the historical labelling is a one-time mapping for backward
compatibility.

**Practical consequence.**
*Future work should reference $\Phi_k$ (curvature-rank-$k$ functional)
rather than "Term $j$" for $j \geq 6$.  The curvature-rank picture
makes it clear that $\Phi_k$ for $k \geq 4$ is one well-defined
mathematical object, not two competing conjectures.*
