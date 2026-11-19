The categorical lepton number possesses several structural properties.

Each beta decay applies the Skein relation at one crossing. This produces a smoothing $L_0^{\pm}$. It contains exactly one lepton–antilepton pair. Lepton number counts these smoothings.

Each smoothing $L_0^{\pm}$ contributes:
- One charged lepton ($T_{2,3}$ or $T_{2,3}^{\sigma}$) with lepton number $+1$.
- One neutrino or antineutrino ($K_{0_1}$ or $K_{0_1}^{\sigma}$) with lepton number $-1$.

The net lepton number of each $L_0^{\pm}$ pair is zero.

**Conservation.**
Lepton number is conserved by construction:

1. Skein smoothings produce lepton pairs with net lepton number $0$. The nuclear sector loses one crossing. Hadrons carry lepton number $0$. The total is $\Delta L = 0$.
2. Gröbner–Shirshov re-reduction acts within the Iwahori–Hecke algebra. It produces no smoothings. The total is $\Delta L = 0$.
3. Markov moves change the braid representative but not the link type. The total is $\Delta L = 0$.

Every process expressed as a sequence of Skein relations and Hecke reductions conserves lepton number.

**Lepton number is not a $\mathbb{Z}$-grading.**
The Skein module $\mathcal{K}(S^3; q)$ admits no $\mathbb{Z}$-grading by the
smoothing count with the nuclear sector in grade $0$ and each smoothing shifting
the grade by $+1$.

The skein relation is *inhomogeneous* for such a grading. Writing it as
$$
  L_+ - L_- = (q - q^{-1})\,L_0 ,
$$
the left-hand side is a difference of grade-$g$ classes, hence grade $g$,
while the right-hand side carries one further smoothing, hence grade $g+1$
(scalars are grade-preserving). An element lying in two distinct homogeneous
components is $0$, so the relation forces $(q - q^{-1})L_0 = 0$ and
$L_+ = L_-$. Imposing the grading therefore annihilates every smoothing:
it would make lepton number identically $0$, which is the one value it
cannot take.

This excludes only the $\mathbb{Z}$-graded construction, by the disjointness of
homogeneous components; it does not affect categorical lepton number itself, the
Skein module, or the $Y = B - L$ relation.

**Carrier and filtration structure.**
An inhomogeneous relation is compatible with a *filtration* rather than a
grading, whereas the Vassiliev filtration grades **invariants** $v \colon K \to R$
rather than states, and therefore does not by itself supply a state-valued $L$.

The carrier is the **braid word** rather than the knot type. Indeed, $L$ cannot factor
through the unframed knot type, since mirror reflection must invert the carrier
while the unknot is amphichiral. Consistently with antiparticle crossing reversal,
the mirror involution acts by $\sigma_i \mapsto \sigma_i^{-1}$ on braid words
while preserving the unframed knot type of the unknot.

The braid words are fixed by the $\chi = -6$ constraint below: $T(2,n)$ is the
closure of $\sigma_1^n$, so $\nu_e = \sigma_1$, $e^- = \sigma_1^3$, and the
antiparticles are $\sigma_1^{-1}, \sigma_1^{-3}$ --- distinct braid words that
both close to the unknot, which is exactly how the mirror acts freely.
Evaluating the writhes directly from these braid words shows that the candidate
functional
$$
  L(\beta) = \mathrm{sign}\bigl(\mathrm{writhe}(\beta)\bigr)
$$
reproduces every row of the table below, hadrons included. This expression
remains a **candidate** rather than a derivation: $\mathrm{sign}$ is an ad hoc
choice of function, and chiral quark braid words ($u_L$ versus $u_R$) require
additional structure beyond pure writhe.

**Obstructions to the bare writhe ansatz.**

*Markov II.* Stabilisation raises the writhe by $1$ without changing the link,
so $L$ jumps from $0$ to $1$ on the baryon --- violating conservation clause 3
above, which requires $\Delta L = 0$ under Markov moves.

*Minimal-level collapse.* Passing to Gröbner--Shirshov normal forms evaluated at
the lowest level of the aether tower does not remove this obstruction. The
table below assigns $\nu_e = K_{0_1} = T_{2,1}$, the **unknot**, whose braid
index is $1$: its minimal-level normal form is the *empty* word, and so is its
mirror's. At the minimal level, $\nu_e$ and $\nu_e^{\sigma}$ represent the
**same state**, so no function of the minimal-level state alone can assign them
$+1$ and $-1$ --- quite apart from $\mathrm{sign}(0) = 0 \neq +1$. This recovers
the same chirality obstruction encountered on unframed knot types once the
canonical minimal-level representative is fixed.

Passing from unframed knot types to braid words therefore fails to rescue
$L = \mathrm{sign}(w)$ at minimal level, where the canonical braid word is
determined by the knot type. Consequently, the bare writhe ansatz
$L = \mathrm{sign}(w)$ is ruled out, while categorical lepton number itself and
the $Y = B - L$ relation remain intact: $L$ must arise from framing data or the
skein smoothing history rather than the bare crossing sum.

**Individual lepton assignments.**

| Particle | Knot type | Lepton number $L$ | Origin |
|----------|-----------|:---:|--------|
| $e^-$ | $T_{2,3}$ (trefoil) | $+1$ | $L_0^{-}$ charged component ($\beta^-$) |
| $e^+$ | $T_{2,3}^{\sigma}$ (mirror trefoil) | $-1$ | $L_0^{+}$ charged component ($\beta^+$) |
| $\nu_e$ | $K_{0_1}$ (unknot) | $+1$ | $L_0^{+}$ neutral component ($\beta^+$) |
| $\nu_e^{\sigma}$ | $K_{0_1}^{\sigma}$ (mirror unknot) | $-1$ | $L_0^{-}$ neutral component ($\beta^-$) |

The charged lepton carries $L = \pm 1$. The neutrino carries $L = \mp 1$. Each pair sums to zero.

**The $\chi = -6$ constraint.**
In the Descartes universe, the Euler characteristic $\chi(A) = -6$ constrains Bring's surface. The torus knot generators $T(2, n)$ with odd $n \leq 7$ exhaust the fermion spectrum. The electron ($T_{2,3}$) and neutrino ($K_{0_1} = T_{2,1}$) are the lowest torus knots in this sequence. The smoothing $L_0^{-}$ must decompose into exactly these knot types. They are the only single-component closures of a 2-arc resolution at a Borromean crossing.

**Structural origin of lepton-number conservation.**
In the Standard Model, lepton number conservation is an accidental symmetry. Here, it is a structural invariant. The Skein relation is the unique operation that changes crossing type. It always produces exactly one lepton pair. The Iwahori–Hecke algebra contains no mechanism to produce an odd number of leptons. The smoothing is a topological operation on a single crossing. Each smoothing is binary.

Lepton number violation requires a process that changes crossing type without passing through the Skein relation. Such a process must exist outside the Iwahori–Hecke algebra. In the $\chi = -6$ universe, no such process exists.
