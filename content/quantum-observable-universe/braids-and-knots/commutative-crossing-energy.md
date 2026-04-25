**Remark (commutative-limit reading of crossing energy).**
The crossing-energy formula
([crossing energy](#def:crossing-energy)) assigns a positive crossing
the weight $q$ and a negative crossing $-q^{-1}$, so each crossing
contributes the eigenvalue difference $q - q^{-1}$ to the net Skein
weight.  In the strictly commutative limit
([commutative QOU](#def:commutative-qou)) this difference vanishes
identically: $q \to 1$ forces $q - q^{-1} \to 0$ and the per-crossing
weight collapses.

This degeneracy is *not* the end of the story.  Writing
$q = e^{i\theta}$ on the unit circle of the complex plane recasts the
crossing weight as

$$
  q - q^{-1}  =  2i \sin\theta,
$$

so the **commutative-limit crossing weight is a pure imaginary $2i\sin\theta$**.
The factor of $i$ is forced by the geometry of the $\mathrm{U}(1)$
phase tube ([prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)):
the orbit-space interval $\theta \in [0, \pi]$ has scalar fixed points
at the two poles $\theta = 0, \pi$ (zero crossing weight) and a free
$S^1$-fibre over the interior (the "traveling part" of the interval).
The quarter-turn point $\theta = \pi/2$, where $q = i$ exactly, is
the midpoint of the traveling part and the location of maximum
crossing weight $|2i\sin(\pi/2)| = 2$.

**Travel speed reading.**  In this picture
$\sin\theta$ is the *speed of travel* along the interior of the
orbit interval: zero at the boundary poles, maximal at the midpoint,
and sign-changing under the orientation reversal $\theta \mapsto -\theta$
(equivalently $q \leftrightarrow q^{-1}$, the involution
exchanging $L_+$ and $L_-$).  The Hecke energy of the
non-commutative theory is the algebraic analogue of this speed; in
the commutative limit only the imaginary travel-speed $i\sin\theta$
survives.

**Branch-phase localisation.**  By
[rem:u1-phase-tube](#rem:u1-phase-tube), the five branch points
$\zeta_5^{k}$ of the hyperelliptic quintic
([hyperelliptic quintic](#def:hyperelliptic-quintic)) pick out five
preferred phase values $\varphi_k = 2\pi k/5$ on the $\mathrm{U}(1)$
tube.  At these phases the commutative crossing weight takes only
two distinct magnitudes,

$$
  2\lvert\sin(2\pi/5)\rvert  \approx 1.902,
  \qquad
  2\lvert\sin(4\pi/5)\rvert  \approx 1.176,
$$

with the golden-ratio identity $\sin(2\pi/5)/\sin(4\pi/5) = \varphi$
(where $\varphi = (1+\sqrt{5})/2$).  These are the only two
"speeds" available to commutative-limit crossings localised at the
$\mathbb{Z}_5$-orbit on the curve.

**Falsifiability witness — light-isotope mass-tower ratios.**  The
recent computation `tr-m-plus-tower-and-log` in
`folio-assistant/computations/` evaluates the multi-brane mass
$\mathfrak{m}_{\mathrm{cat}} = \lvert\mathrm{tr}_M(\beta)\rvert + \sum_n \hbar_q^{2n}\,\mathrm{tower}^{(n)}$
against AME binding energies for the three lightest non-trivial
nuclei.  The derived/observed ratio overshoots by a factor of
$3$ to $4$, indicating a missing scalar prefactor.  The
isospin-corrected (Coulomb-removed) ratios collapse to two values
that match sums over the two distinct branch-phase magnitudes
above:

| Atom | $A$ | strong-force ratio | branch-phase prediction | error |
|------|-----|--------------------|------------------------|-------|
| $\mathrm{D}$  $({}^2\mathrm{H})$ | 2 | $\approx 3.052$ | $2\lvert\sin(2\pi/5)\rvert + 2\lvert\sin(4\pi/5)\rvert \approx 3.078$ | $+0.84\%$ |
| $\mathrm{T}$ = ${}^3\mathrm{He}_{\mathrm{Coulomb-corr}}$ | 3 | $\approx 3.477$ | $3 \cdot 2\lvert\sin(4\pi/5)\rvert \approx 3.527$ | $+1.44\%$ |

Removing the well-known $\approx 0.76\;\mathrm{MeV}$ Coulomb energy
of ${}^3\mathrm{He}$ collapses the two $A = 3$ ratios to a single
value $3.4767$ that agrees with the tritium ratio $3.4764$ to
$0.014\%$, consistent with isospin symmetry of the strong-force
binding (Wigner-energy convention as in \cite{satula1997}).

**Status.**  This is a *suggestive partial fit*, not a derivation:
the magnitudes, ordering, and golden-ratio relations align with the
branch-phase reading at the percent level, but the per-nucleon
scaling between $A = 2$ and $A = 3$ has not been derived from first
principles.  The match motivates promoting the commutative-limit
crossing weight $2i\sin\theta$ to a structural object on equal
footing with the Hecke weight $q - q^{-1}$ at $q = q_0$, but a clean
derivation requires understanding why the $A = 3$ sum picks out
three copies of the inner phase $\sin(4\pi/5)$ while the $A = 2$
sum picks out one of each.

**No anyons here.**  As in
[rem:u1-phase-tube](#rem:u1-phase-tube), the commutative limit is
disjoint from the root-of-unity specialisation; the $i$ here is the
quarter-turn complex structure on a single phase tube, not a
fractional spin.
