*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Lepton number is the count of Skein smoothings applied to the
nuclear normal form.**

Each beta decay
([beta decay](#def:beta-decay-skein)) applies the Skein relation
at one crossing, producing a smoothing $L_0^{\pm}$ that contains
exactly one lepton--antilepton pair.  Lepton number counts these
smoothings.

**Definition.**
Let $\mathcal{N}$ be a nuclear link in Gröbner--Shirshov normal
form and let $\mathcal{N}'$ be obtained from
$\mathcal{N}$ by a sequence of $k$ Skein crossing changes.
The **lepton number** of the transition is $L = k$.

Each smoothing $L_0^{\pm}$ contributes:
- One charged lepton ($T_{2,3}$ or $T_{2,3}^{\sigma}$) with
  lepton number $+1$
- One (anti)neutrino ($K_{0_1}$ or $K_{0_1}^{\sigma}$) with lepton
  number $-1$

The net lepton number of each $L_0^{\pm}$ pair is $+1 + (-1) = 0$.

**Conservation.**
Lepton number is conserved by construction:

1. **Skein smoothings** produce lepton pairs with net lepton
   number $0$.  The nuclear sector loses one crossing (lepton
   number $0$ for hadrons).  Total: $\Delta L = 0$.

2. **Gröbner--Shirshov re-reduction** (R2, R3, far-commutativity) acts
   within the Iwahori--Hecke algebra and does not produce smoothings.
   $\Delta L = 0$.

3. **Markov moves** (conjugation, stabilisation) change the
   braid representative but not the link type.
   $\Delta L = 0$.

Therefore: **every process that can be expressed as a sequence of
Skein relations and Hecke reductions conserves lepton number.**

**Lepton number is a $\mathbb{Z}$-grading on the Skein module.**
The Skein module $\mathcal{K}(S^3; q)$ has a natural
$\mathbb{Z}$-grading by the number of smoothings applied.  Links
in the nuclear sector have grade $0$; each smoothing shifts the
grade by $+1$.  The grade is preserved by the Hecke relations
(which act within a fixed grade) and by Reidemeister moves (which
do not change the smoothing count).

**Individual lepton assignments.**

| Particle | Knot type | Lepton number $L$ | Origin |
|----------|-----------|:---:|--------|
| $e^-$ | $T_{2,3}$ (trefoil) | $+1$ | $L_0^{-}$ charged component ($\beta^-$) |
| $e^+$ | $T_{2,3}^{\sigma}$ (mirror trefoil) | $-1$ | $L_0^{+}$ charged component ($\beta^+$) |
| $\nu_e$ | $K_{0_1}$ (unknot) | $+1$ | $L_0^{+}$ neutral component ($\beta^+$) |
| $\nu_e^{\sigma}$ | $K_{0_1}^{\sigma}$ (mirror unknot) | $-1$ | $L_0^{-}$ neutral component ($\beta^-$) |

The charged lepton carries $L = +1$ (or $-1$ for the
antiparticle) and the neutrino carries $L = -1$ (or $+1$)
so that each pair sums to zero.

**The $\chi = -6$ constraint.**
In the Descartes universe, the Euler characteristic
$\chi(A) = -6$ constrains the Bring's surface.  The torus knot
generators $T(2, n)$ with $n$ odd and $n \leq 7$ exhaust the
fermion spectrum ([torus knot generators](#prop:torus-knot-generators)).
The electron ($T_{2,3}$) and neutrino ($K_{0_1} = T_{2,1}$) are
the two lowest torus knots in this sequence.  The smoothing
$L_0^{-}$ must decompose into exactly these knot types because
they are the only single-component closures of a 2-arc
resolution at a Borromean crossing.

**Why lepton number is not broken.**
In the Standard Model, lepton number conservation is an accidental
symmetry.  In QOU, it is a **structural invariant**: the Skein
relation is the unique operation that changes crossing type, and
it always produces exactly one lepton pair.  There is no
mechanism in the Iwahori--Hecke algebra to produce an odd number of
leptons — the smoothing is a topological operation on a single
crossing, and each smoothing is binary (two arcs).

Lepton number violation would require a process that changes
crossing type without going through the Skein relation — i.e.,
a process outside the Iwahori--Hecke algebra.  In the $\chi = -6$ universe,
no such process exists.
