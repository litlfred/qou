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

**Lepton number is not a $\mathbb{Z}$-grading (proved).**
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

This is a scope-(b) exclusion of *one construction*, with its invariant
cited (the defining disjointness of homogeneous components); it does not
touch lepton number itself, the Skein module, or the $Y = B - L$ route.

**What this leaves, and where $L$ does live.**
An inhomogeneous relation is what a *filtration* tolerates rather than a
grading, but the corpus's Vassiliev filtration
(`QOU/KnotTheory/Vassiliev/`) grades **invariants** $v : K \to R$, not states,
so it does not by itself supply a state-valued $L$.

The carrier is the **braid word**, not the knot type. This is forced:
`QOU/StandardModel/LeptonNumberCarrierChirality.lean` proves $L$ cannot factor
through the unframed knot type, since the mirror must move the carrier and the
unknot is amphichiral. It is also what the corpus already does --
`AntiparticleCrossingReversalContext` takes the mirror to be
$\sigma_i \mapsto \sigma_i^{-1}$ on braid words and records that it
*preserves the knot type*.

The braid words are fixed by the $\chi = -6$ constraint below: $T(2,n)$ is the
closure of $\sigma_1^n$, so $\nu_e = \sigma_1$, $e^- = \sigma_1^3$, and the
antiparticles are $\sigma_1^{-1}, \sigma_1^{-3}$ --- distinct braid words that
both close to the unknot, which is exactly how the mirror acts freely.
`QOU/StandardModel/ChiralFermionBraidWords.lean` proves the writhes from the
words and shows the candidate
$$
  L(\beta) = \mathrm{sign}\bigl(\mathrm{writhe}(\beta)\bigr)
$$
reproduces every row of the table below, hadrons included. It is a
**candidate**, not a derivation: $\mathrm{sign}$ is a choice of function, the
quark braid word is still absent from the corpus, and chirality ($u_L$ vs
$u_R$) is not yet represented.

**And it is refuted, under both readings of the gauge freedom.**

*Markov II.* Stabilisation raises the writhe by $1$ without changing the link,
so $L$ jumps from $0$ to $1$ on the baryon --- violating conservation clause 3
above, which requires $\Delta L = 0$ under Markov moves
.

*The minimal-level ruling.* The escape from the first refutation was that
states are Gröbner--Shirshov normal forms, with the observable evaluated at the
lowest level of the substrate tower. That closes the escape rather than opening
it. The table above assigns $\nu_e = K_{0_1} = T_{2,1}$, the **unknot**, whose
braid index is $1$: its minimal-level normal form is the *empty* word, and so is
its mirror's. At the level where the framework says observables live, $\nu_e$
and $\nu_e^{\sigma}$ are the **same state**, and no function of the state can
give them $+1$ and $-1$ --- quite apart from $\mathrm{sign}(0) = 0 \neq +1$.
This is `QOU/StandardModel/WritheLevelParity.lean`'s
`leptonNumber_collapses_at_minimal_level`, and it is the same obstruction
`LeptonNumberCarrierChirality.lean` proved for the unframed knot type,
reappearing once the canonical representative is pinned.

So the "carrier is the braid word, not the knot type" escape is unavailable at
minimal level, where the braid word is determined by the knot type. **Scope-(a)**:
$L = \mathrm{sign}(w)$ is refuted; lepton number itself and the $Y = B - L$
route are untouched, and what the refutation locates is that $L$ must come from
data the writhe does not carry --- the framing or the smoothing history, not the
crossing sum.

**Individual lepton assignments.**

| Particle | Knot type | Lepton number $L$ | Origin |
|----------|-----------|:---:|--------|
| $e^-$ | $T_{2,3}$ (trefoil) | $+1$ | $L_0^{-}$ charged component ($\beta^-$) |
| $e^+$ | $T_{2,3}^{\sigma}$ (mirror trefoil) | $-1$ | $L_0^{+}$ charged component ($\beta^+$) |
| $\nu_e$ | $K_{0_1}$ (unknot) | $+1$ | $L_0^{+}$ neutral component ($\beta^+$) |
| $\nu_e^{\sigma}$ | $K_{0_1}^{\sigma}$ (mirror unknot) | $-1$ | $L_0^{-}$ neutral component ($\beta^-$) |

The charged lepton carries $L = \pm 1$. The neutrino carries $L = \mp 1$. Each pair sums to zero.

**The $\chi = -6$ constraint.**
In the Descartes universe, the Euler characteristic $\chi_{\mathrm{eu}}(M_0) = -6$ constrains Bring's surface. The torus knot generators $T(2, n)$ with odd $n \leq 7$ exhaust the fermion spectrum. The electron ($T_{2,3}$) and neutrino ($K_{0_1} = T_{2,1}$) are the lowest torus knots in this sequence. The smoothing $L_0^{-}$ must decompose into exactly these knot types. They are the only single-component closures of a 2-arc resolution at a Borromean crossing.

**Structural origin of lepton-number conservation.**
In the Standard Model, lepton number conservation is an accidental symmetry. Here, it is a structural invariant. The Skein relation is the unique operation that changes crossing type. It always produces exactly one lepton pair. The Iwahori–Hecke algebra contains no mechanism to produce an odd number of leptons. The smoothing is a topological operation on a single crossing. Each smoothing is binary.

Lepton number violation requires a process that changes crossing type without passing through the Skein relation. Such a process must exist outside the Iwahori–Hecke algebra. In the $\chi = -6$ universe, no such process exists.
