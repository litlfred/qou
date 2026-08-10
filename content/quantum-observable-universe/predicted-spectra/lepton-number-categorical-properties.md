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
An earlier version of this section asserted that the Skein module
$\mathcal{K}(S^3; q)$ admits a natural $\mathbb{Z}$-grading by the smoothing
count, with the nuclear sector in grade $0$ and each smoothing shifting the
grade by $+1$. **That is false**, and the obstruction is proved sorry-free in
`QOU/StandardModel/LeptonNumberGradingObstruction.lean`.

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

**What the correct structure appears to be: a filtration.** An inhomogeneous
relation is exactly what a *filtration* tolerates — the skein relation lowers
the filtration degree by one rather than preserving a grade. That is the
Vassiliev / finite-type filtration, and the corpus already carries it under
`QOU/KnotTheory/Vassiliev/` (`finiteTypeSubmodule_mono` is the increasing
family). Whether lepton number is recovered as a filtration degree there is
**open** and is not claimed here; see bean `qou-kl39`.

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
