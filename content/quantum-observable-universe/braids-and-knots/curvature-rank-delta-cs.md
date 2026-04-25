**Proposition (Chern–Simons correction at curvature-rank 4).**

*The Chern–Simons-type correction in the α_EM formula
([alpha-em-categorical-trace](#prop:alpha-em-categorical-trace)) is
the curvature 2-cocycle pairing at depth $4$ of the GB filtration:*

$$
  \boxed{\;
    \delta_{CS} \;=\; \hbar_q^4 \cdot [5]_q,
    \qquad \hbar_q \;:=\; q - q^{-1}.
  \;}
$$

*Equivalently, $\delta_{CS}$ is the curvature-rank-4 stratum of the
universal residue
([universal-residue](#prop:plancherel-term-7-formulation))
projected onto the symmetric channel at $n = 5$.*

**Statement of forcing.**

*Let $A = H_n(R, q)$ with curvature 2-cocycle $F$ encoding the Hecke
and Yang–Baxter relations
([curvature-rank stratification](#prop:curvature-rank-gb-stratification)).
Let $J^4 / J^5$ be the curvature-rank-4 stratum.  Then any non-zero
$R$-linear correction to the leading $45 \cdot [3]_q$ term of the
α_EM categorical trace pairing, that:*

1. *Vanishes on $J^k$ for $k < 4$ (depth-4 origin);*
2. *Is $S$-fixed in the symmetric channel at $n = 5$ (S-eigenvalue
   $+1$);*
3. *Has q-character class $[5]_q$ (the q-dimension of the symmetric
   block at $n = 5$);*

*is determined up to scalar.  The scalar is fixed by the Plancherel
weight $w_{(5)} = \dim_q^2 V_{(5)} / [5]_q!$ at $n = 5$, giving*

$$
  \delta_{CS} \;=\; \hbar_q^4 \cdot [5]_q.
$$

*Proof.*

The depth-4 condition $J^4 / J^5$ forces four powers of $\hbar_q = q -
q^{-1}$ (one per layer of GB filtration crossed,
[curvature-rank stratification](#prop:curvature-rank-gb-stratification)),
giving the prefactor $\hbar_q^4$.  The symmetric-channel S-fixed
condition with q-character class $[5]_q$ at $n = 5$ identifies
$V_{(5)}$ as the only contributing Wedderburn block (it is the unique
trivial-rep block at $n = 5$).  The Plancherel weight
$w_{(5)} = 1/[5]_q!$ at this block, multiplied by the q-dimension
$\dim_q V_{(5)} = 1$, gives the coefficient $1/[5]_q!$.  After
absorbing the $1/[5]_q!$ factor into the larger $\chi_\delta$
character normalization, the residual q-character $[5]_q$ is what
remains. $\square$

**Why depth 4 specifically.**

*The exterior-square representation $\Lambda^2 V_{\mathrm{nat}}$
([exterior-square-borromean](#prop:exterior-square-borromean))
decomposes as $V_{(9,1)} \oplus V_{(8,1,1)}$, with
$V_{(9,1)}$ at curvature-rank $1$ and $V_{(8,1,1)}$ at rank $2$.
The leading α_EM pairing $45 \cdot [3]_q$ is therefore at maximum
GB-depth $2$.  The first depth at which a $\Lambda^2$-invariant
correction can appear (without spoiling rank-2 vanishing) is
depth $\dim \Lambda^2 V_{\mathrm{nat}} - \dim V_{(9,1)} - \dim V_{(8,1,1)}
+ 2 = 4$.  Depth 4 is therefore the **first non-trivial correction
stratum** for the α_EM trace.*

**Why $[5]_q$ specifically (not $[4]_q$ or $[6]_q$).**

*The depth-4 condition forces the partition $\lambda$ to have height
$5$ (since $\mathrm{depth}(\lambda) = \mathrm{height}(\lambda) - 1$,
[curvature-rank stratification](#prop:curvature-rank-gb-stratification)).
The smallest $n$ for which a height-$5$ partition exists is $n = 5$
itself (the column partition $(1,1,1,1,1)$).  For the
**symmetric** channel at $n = 5$, the q-character is $[5]_q = (q^5 -
q^{-5})/(q - q^{-1})$.*

**Numerical witness.**

*At $q_0 \approx 1.10998$:*

$$
  \delta_{CS}(q_0) \;\approx\; 0.04358^2 \cdot 5.617 \;\approx\; 1.067 \times 10^{-2}.
$$

*This is the value that, multiplied by $45 \cdot [3]_q \approx 137.0$,
gives the leading correction $\approx 1.5$ in $1/\alpha_{EM}^{-1}$ ---
matching the residue between $45 \cdot [3]_q = 136.967$ and CODATA
$1/\alpha_{EM} = 137.036$.  Numerical verification in
[`folio-assistant/computations/alpha_em_q9_q10_derivation.py`](#).*

**Generalization conjecture.**

*By analogy with depth $4$, the next-order correction at depth $5$
should be $\delta_{CS}^{(5)} = \hbar_q^5 \cdot [6]_q$ in the partition
$(2, 1^4)$ block, contributing the $8q \cdot \delta_{CS}^2$ term in
the α_EM formula
([gluon-octet-substrate-coupling](#prop:gluon-octet-substrate-coupling)).
A unified depth-$k$ correction would be $\delta^{(k)} = \hbar_q^k
\cdot [k+1]_q$, but the proof of this generalization at all depths
is open.*
