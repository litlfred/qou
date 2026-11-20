*The mixed channel $\lambda = (2,1)$ of $V^{\otimes 3}$ carries the baryon
octet.  Unlike the decuplet, its weight diagram is degenerate --- and that
degeneracy is the one piece of eightfold-way structure in this chapter which
constrains rather than describes.*

Conditional on $N = 3$ ([Proposition](#prop:schur-weyl-eightfold)), the
three-fold product decomposes as

$$
  \mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3}
  \;=\;
  \mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1},
  \qquad
  27 = 10 \cdot 1 + 8 \cdot 2 + 1 \cdot 1 .
$$

The two octets are one flavour irrep counted with the multiplicity
$\dim S^{(2,1)} = 2$ of its Hecke partner, not two different multiplets.  The
decuplet is treated in [the preceding
proposition](#prop:borromean-decuplet); the octet is the subject here.

## The eight states

Writing the weight as $(2I_3, Y)$ keeps every entry an integer.

| State | Content | $2I_3$ | $Y$ | $I$ |
|---|---|---|---|---|
| $\mathfrak{p}$ | $uud$ | $+1$ | $+1$ | $1/2$ |
| $\mathfrak{n}$ | $udd$ | $-1$ | $+1$ | $1/2$ |
| $\Sigma^{+}$ | $uus$ | $+2$ | $0$ | $1$ |
| $\Sigma^{0}$ | $uds$ | $0$ | $0$ | $1$ |
| $\Lambda$ | $uds$ | $0$ | $0$ | $0$ |
| $\Sigma^{-}$ | $dds$ | $-2$ | $0$ | $1$ |
| $\Xi^{0}$ | $uss$ | $+1$ | $-1$ | $1/2$ |
| $\Xi^{-}$ | $dss$ | $-1$ | $-1$ | $1/2$ |

$\Sigma^0$ and $\Lambda$ share both the quark content $uds$ and the weight
$(0,0)$.  They are separated only by isospin, $I = 1$ against $I = 0$.  The
octet's eight states therefore occupy seven lattice points: six on the hexagon
and two stacked at the centre.

## The degeneracy is a constraint

Every other eightfold relation this chapter examines --- [Gell-Mann--Okubo](#rem:meson-mass-splitting),
[the decuplet equal-spacing rule](#rem:decuplet-equal-spacing) and
[Coleman--Glashow](#rem:u-spin-coleman-glashow) --- turns out to be an identity
of its first-order ansatz, true for all parameter values and therefore evidence
for no mechanism.  This one is different, and the difference is machine-checked
in `QOU/Eightfold/OctetWeightDegeneracy.lean`:

- The decuplet's ten weights are pairwise distinct
; the octet's eight are not
, with exactly one collision, at the origin
.
- Hence **no** function of the weight alone can separate $\Lambda$ from
  $\Sigma^0$.  The statement holds for an arbitrary target, not for
  real-valued masses alone
.  Any mass formula built
  from $(2I_3, Y)$ predicts $\mathfrak{m}_\Lambda = \mathfrak{m}_{\Sigma^0}$.

Experiment gives $\mathfrak{m}_\Lambda \approx 1115.7$ MeV against
$\mathfrak{m}_{\Sigma^0} \approx 1192.6$ MeV --- a $77$ MeV gap, about $7\%$,
two orders of magnitude larger than the $0.8\%$ Coleman--Glashow residual.
The class is excluded outright.

This is a scope-(b) structural exclusion, and the invariant justifying it is
proved rather than asserted: non-injectivity of the weight map on the octet.
The obligation it creates falls on every framework, this one included --- a
label beyond $(2I_3, Y)$ must be supplied.  Physically that label is isospin,
which is demonstrably not a function of the weight
.  The decuplet incurs no such obligation
, which is precisely why its
equal-spacing rule runs on $Y$ alone while Gell-Mann--Okubo needs the isospin
Casimir as well.

## Two twos, kept apart

The multiplicity $\dim S^{(2,1)} = 2$ and the $\Lambda$/$\Sigma^0$ degeneracy
are both doublings, and they are unrelated.  The first counts copies of the
whole eight-dimensional irrep inside $V^{\otimes 3}$; the second counts states
over a single lattice point inside one copy.  Reading either as the other would
make the octet's extra label look as though the Hecke algebra already supplied
it.  It does not: the channel arithmetic and the
degeneracy count are recorded separately for that
reason.

## What the framework supplies

The decomposition above, and everything drawn from it, is conditional on
$N = 3$.  The framework's single-fibre construction gives $\dim V = 2$, at
which the Schur--Weyl row cap removes the singlet entirely and there is no
octet to carry a weight diagram --- a proved obstruction, not an approximation
([Proposition](#prop:schur-weyl-eightfold)).  No construction here supplies
$N = 3$.

Nothing on this page is fitted and nothing is wired to any computation; the
PDG masses are comparators.  What the framework does contribute is the
negative result: a weight-only mass formula for the octet is structurally
impossible rather than inaccurate, so any future derivation must carry the
isospin label from the start.
