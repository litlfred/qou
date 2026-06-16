**Remark.**
*The classical Murnaghan–Nakayama recursion computes characters
$\chi^\lambda(\sigma)$ of the symmetric group $S_n$ on a permutation
$\sigma$ specified by its cycle type.  When applied to the
$S_{3A}$-projection $\pi(\mathcal{A})$ of the atomic braid word
$\mathcal{A}$, the classical Specht character $\chi^\lambda(\pi(\mathcal{A}))$
cannot distinguish a proton from a neutron, because the two
have identical permutation images.*

**Computational evidence.**
*Using `computations/schur_weyl_mn_witness.py`:*

See [Table](#tbl:mn-classical-parity-blind-table-data).

*Proton and neutron collapse onto the same cycle type $(2, 1)$
because both atomic-braid words have an odd number of crossings at
generator $0$ and an even number at generator $1$ — so the
parity pattern is identical.  At the $S_n$ level, positive and
negative crossings $\sigma_i^{\pm 1}$ project to the same
transposition $(i, i+1)$.*

**Origin of the loss of information.**
*The Hecke algebra $H_n(R, q)$ has two eigenvalues for each Hecke
generator: $\sigma_i$ has spectrum $\{q, -q^{-1}\}$.  The q-deformed
character $\chi^\lambda_q(\sigma_w)$ distinguishes these eigenvalues
through q-weighted ribbon tableaux — a positive crossing and a
negative crossing contribute **different** q-factors to the same
ribbon removal.  In the classical limit $q \to 1$, the two
eigenvalues collide at $\{+1, -1\}$ but the character becomes the
plain $S_n$-character, which only sees the transposition
(parity-blind).*

*Consequence: the **classical Murnaghan–Nakayama is the wrong
character** for mass predictions.  It captures the correct
partition support $\{\lambda : \chi^\lambda(\pi(\mathcal{A})) \neq 0\}$
but the wrong weights for atoms that differ only in $\sigma^{\pm 1}$
content (like $\mathfrak{p}$ vs $\mathfrak{n}$).  Any $\beta$-decay
calibration $E_0 = 0.782\;\mathrm{MeV} / (|\mathrm{tr}_M(\mathfrak{n})|
- |\mathrm{tr}_M(\mathfrak{p})|)$ fails because the classical
difference is zero.*

**Structural value of the classical computation.**
*Even though the classical MN gives zero proton–neutron splitting,
the computation is valuable as a **structural diagnostic**:*

1. *It identifies exactly which partitions $\lambda \vdash 3A$
   carry nonzero Schur–Weyl weight for each atom.*
2. *The partition set is sparse: for $A = 4$ only $5$ of the
   $77$ partitions of $12$ contribute.*
3. *Because the q-deformed character $\chi^\lambda_q$ has the same
   support as $\chi^\lambda$ (ribbon removability is a shape
   property, not a q-weight property), the classical support
   list **is** the support list for the full Hecke character.*
4. *The full mass calculation therefore requires evaluating
   q-deformed $\chi^\lambda_q(\sigma_w)$ only on this pre-computed
   support — a substantial pruning of the partition sum.*

**Next step: q-deformed ribbon characters.**
*The full Hecke-algebra character is*

$$
  \chi^\lambda_q(\sigma_w)
  \;=\;
  \sum_{\text{ribbon tableau of shape } \lambda}
    q^{\operatorname{charge}(\text{tableau})}
    \cdot (\text{sign accounting for } \sigma^{\pm 1}),
$$

*a q-weighted version of the Murnaghan–Nakayama sum.  Ram and
Wenzl (1992) give explicit formulas for small cases, and the
general ribbon-q-weight recipe is in the Ram 1991 thesis.
Implementing this recipe over the Murnaghan–Nakayama support
identified here closes the proton–neutron splitting gap and is
the natural next iteration of the symbolic engine.*

**Reference implementation.**
*Script: `computations/schur_weyl_mn_witness.py`.
Uses `murnaghan_nakayama.py` (classical MN recursion) and
`schur_weyl_symbolic.py` (global $H_{3A}$ sum with q symbolic).
Witness file: `schur-weyl-mn.witness.json`.  Evaluation time: 
a few seconds for $A \leq 3$, under a minute for $A = 4$ (77
partitions).*
