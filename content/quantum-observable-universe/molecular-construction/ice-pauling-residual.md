*Lean sibling: combinatorial, exact over $\mathbb{Q}$ (the entropy $S = R\ln W_1$ step is archimedean).*

**Proposition (Pauling residual entropy of ice).** In ice $I_h$ each water is hydrogen-bonded to four neighbours — two as **donor** (its two H's) and two as **acceptor** (its two lone pairs), the four directions of [the H$_2$O braid](#def:h2o-molecular-braid). Subject to the ice rule that every bond carries exactly one hydrogen, the per-molecule multiplicity is
$$ W_1 \;=\; \binom{4}{2}\left(\tfrac12\right)^{2} \;=\; \frac{6}{4} \;=\; \frac{3}{2}, $$
so the molar residual entropy is $S = R\ln\tfrac32 \approx 3.37\ \mathrm{J\,mol^{-1}\,K^{-1}}$ (Pauling, 1935), in close agreement with the measured ice calorimetry.

**Proof.** A water assigns its two donated hydrogens among its four bonds in $\binom{4}{2}=6$ ways; each of its two bonds is shared with a neighbour and, on the independent estimate, carries exactly one hydrogen with probability $\tfrac12$, giving $W_1 = 6\cdot(\tfrac12)^2 = \tfrac32$. The Lean sibling proves $\binom{4}{2}=6$ and $\binom{4}{2}(\tfrac12)^2 = \tfrac32$ exactly over $\mathbb{Q}$; the entropy $S = Nk\ln W_1 = R\ln\tfrac32$ is the archimedean evaluation. $\qquad\blacksquare$
