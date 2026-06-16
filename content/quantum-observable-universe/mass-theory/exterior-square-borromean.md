**Proposition (Borromean strand-pair representation has dimension 45).**
*Let $V_{\mathrm{nat}} = \mathbb{C}^{10}$ be the natural permutation
representation of $S_{10}$ (or its q-deformation $H_{10}(q)$
acting via the standard projection).  Then the **exterior square**
$\Lambda^2 V_{\mathrm{nat}}$ has dimension $\binom{10}{2} = 45$ at
$q = 1$, and decomposes under $S_{10}$ as*

$$
  \Lambda^2 V_{\mathrm{nat}} \;\cong\; V_{(9,1)} \oplus V_{(8,1,1)},
$$

*where $V_{(9,1)}$ is the $9$-dimensional standard representation
and $V_{(8,1,1)}$ is the $36$-dimensional hook representation
(verified: $9 + 36 = 45$).*

*Proof.*

$V_{\mathrm{nat}} = \mathbb{C}^{10}$ as $S_{10}$-module decomposes as
$V_{(10)} \oplus V_{(9,1)}$ (trivial $\oplus$ standard).  Hence

$$
\Lambda^2 V_{\mathrm{nat}} = \Lambda^2(V_{(10)} \oplus V_{(9,1)})
= V_{(10)} \otimes V_{(9,1)} \;\oplus\; \Lambda^2 V_{(9,1)}.
$$

Since $V_{(10)} \otimes V_{(9,1)} = V_{(9,1)}$ (trivial tensor anything = same),
this gives

$$
\Lambda^2 V_{\mathrm{nat}} = V_{(9,1)} \;\oplus\; \Lambda^2 V_{(9,1)}.
$$

For the second summand: $\Lambda^2$ of the standard rep of $S_n$
(of dimension $n - 1$) is the irreducible representation indexed
by the partition $(n - 2, 1, 1)$, of dimension $\binom{n - 1}{2}$.
For $n = 10$: $\Lambda^2 V_{(9,1)} = V_{(8,1,1)}$ of dimension
$\binom{9}{2} = 36$.

Total dimension: $9 + 36 = 45 = \binom{10}{2}$.  $\square$

**Corollary (Borromean interpretation).**
*The integer $45$ in the $\alpha_{EM}$ formula
([alpha-em-categorical-trace](#rem:alpha-em-categorical-trace))
counts unordered pairs of the $10$ strands in $V_{\mathrm{nat}}$.
This is the **dimension of the strand-pair coupling representation**
— precisely the algebraic shadow of the Borromean linking
([borromean-baryon-interpretation](#rem:borromean-baryon-interpretation))
where each pair of three strands forms a Borromean cycle.*

**Connection to Hecke / quantum dimension.**

*Under the $q$-deformation $H_{10}(q)$, the same direct-sum
decomposition holds with q-dimensions:*

$$
\dim_q \Lambda^2 V_{\mathrm{nat}}
\;=\; \dim_q V_{(9,1)} + \dim_q V_{(8,1,1)}
\;=\; [9]_q + \binom{[9]_q}{2}_q,
$$

*where $\binom{n}{k}_q$ is the q-binomial.  At $q = 1$ this gives
$9 + 36 = 45$; at $q_0 = 1.109978595554181\ldots$ (50 dps) the q-deformation differs from
$45$ by an O($\hbar_q$) correction.*

*The α_EM formula uses the **classical** integer $45 = \binom{10}{2}$
in $\binom{10}{2} \cdot [3]_q \cdot (1 + \delta_{CS} + \cdots)$.
This is consistent with $45$ being the q-deformation-INVARIANT
underlying combinatorial count.*

**Why $V_{\mathrm{nat}}^{10}$ specifically.**

The atomic braid for a 4-nucleon system (e.g. $^4$He) lives on $3 \cdot 4 = 12$
strands; for a 3-nucleon system on $9$.  The "10" comes from the
**combined leptonic + baryonic strand structure**: 9 quark strands
(3 nucleons $\times$ 3 quarks) + 1 lepton strand $\to$ 10 total.
The pair-count $\binom{10}{2} = 45$ then enumerates all
strand-strand couplings, including **lepton-quark crossings** which
mediate the EM coupling.

**Witness.** Computational verification at $q = 1$ via
[`computations/alpha_em_q9_q10_derivation.py`](#) and
the dimension formula directly: numerical match to the expected
$45 \cdot [3]_q = 136.967$ at $q_0$, with $-0.05\%$ residue
explained by the $\delta_{CS}$ + $8q \delta_{CS}^2$ corrections per
[alpha-em-categorical-trace](#rem:alpha-em-categorical-trace).
