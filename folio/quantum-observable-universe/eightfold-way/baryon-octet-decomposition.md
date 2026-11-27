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
for no mechanism.  This one is different, and the difference is proved:

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

## Two twos, kept apart, and the diquark projector split

The multiplicity $\dim S^{(2,1)} = 2$ and the $\Lambda$/$\Sigma^0$ degeneracy
are distinct phenomena: the first counts copies of the eight-dimensional
flavour irrep inside $V^{\otimes 3}$, whereas the second counts two states over
the $(0,0)$ weight inside *one* copy.  Within the two-dimensional mixed-symmetry
Hecke module $S^{(2,1)}$ itself, however, the $(1,2)$ diquark exchange $\sigma_1$
has distinct eigenvalues $-q^{-1}$ ($I = 0$, antisymmetric $ud$ diquark for
$\Lambda$) and $+q$ ($I = 1$, symmetric $ud$ diquark for $\Sigma^0$), supplying
two mutually orthogonal rank-$1$ idempotents
$$
  P_\Lambda = [2]_q^{-1}(q - \sigma_1),
  \qquad
  P_{\Sigma^0} = [2]_q^{-1}(\sigma_1 + q^{-1}),
  \qquad
  P_\Lambda + P_{\Sigma^0} = 1_{S^{(2,1)}},
$$
whose traces match the $3 \times 3$ baryon weight-space sub-projectors across
$\sigma_1$, $\sigma_2$, $V = \sigma_1\sigma_2^{-1}$, and $V^3$.  On the
commuting Jucys--Murphy twists $J_2 = \sigma_1^2$ and $J_3 = \sigma_2\sigma_1^2
\sigma_2$ ($[J_2, J_3] = 0$), $\mathrm{tr}(P_{\Sigma^0} J_2) = q^2$ and
$\mathrm{tr}(P_\Lambda J_2) = q^{-2}$; on a single Borromean step,
$\mathrm{tr}(P_{\Sigma^0} V) = q^6\,\mathrm{tr}(P_\Lambda V)$; and on the full
Borromean baryon braid $V^3 = (\sigma_1\sigma_2^{-1})^3$, the zero-parameter
diquark splitting is
$$
  \mathrm{tr}(P_\Lambda V^3) - \mathrm{tr}(P_{\Sigma^0} V^3)
  \;=\;
  \frac{(q - q^{-1})^3 (q^2 + q^{-2}) [3]_q}{[2]_q}.
$$
At $q_0$, this cubic-in-$h_0$ Borromean trace difference equals $+0.028265$
($|\mathrm{tr}(P_\Lambda V^3)| / |\mathrm{tr}(P_{\Sigma^0} V^3)| = 1.02875$),
lifting the weight-only degeneracy without fitted parameters while
under-predicting the observed $76.959\;\mathrm{MeV}$ ($6.90\%$) gap at
$31.53\;\mathrm{MeV}$ ($-59.0\%$), whereas the single-crossing ratio $q_0 =
1.10998$ over-predicts at $122.70\;\mathrm{MeV}$ ($+59.4\%$).

## What the framework supplies

The decomposition above, and everything drawn from it, is conditional on
$N = 3$.  The framework's single-fibre construction gives $\dim V = 2$, at
which the Schur--Weyl row cap removes the singlet entirely and there is no
octet to carry a weight diagram --- a proved obstruction, not an approximation
([Proposition](#prop:schur-weyl-eightfold)).  No construction here supplies
$N = 3$, and no parameter is fitted to the empirical hadron masses: what is
established is that weight-only formulas are excluded structurally, while the
internal $H_3(q_0)$ diquark sub-projectors split $\Lambda$ from $\Sigma^0$ at
order $(q_0 - q_0^{-1})^3$ without closing the quantitative $77\;\mathrm{MeV}$
scale.
