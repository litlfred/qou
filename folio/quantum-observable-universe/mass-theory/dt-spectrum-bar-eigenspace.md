**Proposition.** *Let $(\mathfrak{d}^+, \mathfrak{d}^-) = (4, 3)$ be the ordered
pair of certified $q\to0$ Stokes constants of the figure-eight's chiral partner
$5_2$ (the $(96)$/$(97)$ factorization constants of $S^+(0)$, $S^-(0)$; both
integer, GGM eq 98). Under the chirality involution $\tau$ — the $q\mapsto q^{-1}$
mirror swap $(\mathfrak{d}^+,\mathfrak{d}^-)\mapsto(\mathfrak{d}^-,\mathfrak{d}^+)$
— the pair carries a faithful $\mathbb{Z}/2$ grading into a bar-even and a bar-odd
part,*

$$
  \mathrm{even} = \mathfrak{d}^+ + \mathfrak{d}^- = 7 \quad(\tau\text{-fixed}),
  \qquad
  \mathrm{odd} = \mathfrak{d}^+ - \mathfrak{d}^- = 1 \quad(\tau\text{-negated}),
$$

*with faithful reconstruction $2\mathfrak{d}^\pm = \mathrm{even} \pm
\mathrm{odd}$. The bar-odd part is nonzero, so no $\tau$-symmetric scalar recovers
the ordered datum; for the amphichiral $4_1$ the bar-odd part vanishes and the
spectrum degenerates to a single constant.*

This is the base brick (milestone M0) of the categorical Route C for the
figure-eight monodromy datum $A_\omega$. The
[scalar exclusion](#conj:stokes-dt-bps-bridge) — no single-valued Wedderburn
Euler characteristic, recursion order, block count, or A-polynomial $L$-degree
equals the $5_2$ DT datum — is a *negative* statement. The bar-eigenspace
decomposition converts it into a *positive* one: the DT count is not a number but
a $\mathbb{Z}/2$-graded (bar-even $\oplus$ bar-odd) object, of which a scalar is
the $\tau$-trivial shadow. "No scalar serves the datum" is exactly "the bar-odd
part is nonzero", which for the chiral $5_2$ it is ($=1$) and for the amphichiral
$4_1$ it is not ($=0$).

The grading is the $q\mapsto q^{-1}$ bar-involution that runs through the whole
even/odd programme; the chirality-refined, set-valued count the exclusion forces is
therefore the categorification of that involution's eigenspaces, not a generic
cohomological-Hall computation. Milestone M2 supplies a *structural
characterization* of the putative closed-sector BPS spectrum — **not** a
construction of it: taking the certified eq-(98) constants as Donaldson–Thomas
invariants (conditional on the DT/BPS bridge `conj:stokes-dt-bps-bridge`), every
Borel ray is distinct, so the Davison–Meinhardt plethystic log is trivial and
$\dim \mathrm{BPS}_d = |\Omega_d|$ with no superpotential and no motivic
$q$-correction — the spectrum would be *abelian*, which is why $A_\omega$ and the
whole Stokes tower are integers rather than Poincaré polynomials
(`QOU.QBeta.AomegaM2BPSCohomology`).
This does **not** build the closed-sector quiver-with-potential $(Q,W)$ (Milestone
M1, still unwritten), does not compute a cohomology from a category, and does not
derive $A_\omega$: the count is *imported* (conditional on the bridge above), and
what M2 adds is only that its BPS realization would carry no hidden motivic
multiplicity. The Hecke-to-BPS bridge (M3) that would *derive* rather than *import*
the count stays open; this proposition fixes only the structural target. The onward identification of $A_\omega$ with the
bar-odd decay leak $S$ has no literature support and is not derivable; it is not
carried here.

## Status

Proved over the integers, with no archimedean structure: the certified matrices $S_0^{\pm}$; the two-element split of the DT spectrum; the bar swap and that it is an involution; the eigenspace laws (the bar-even pair is fixed, the bar-odd pair is negated); the faithful reconstruction from the bar grading; that the $5_2$ DT pair is chiral, with grading $(7,1)$; and that a symmetric scalar cannot detect the chirality.
