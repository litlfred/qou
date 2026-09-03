---
doc_id: arxiv-1007.2335v1
doc_title: "Hopf solitons in the Nicole model"
section_id: sec-002-4-numerical-results
section_title: "Numerical results"
section_number: 4
pages: 7-10
source_pdf: 1007.2335v1.pdf
source_sha256: a55d544d1740523f
doc_brief: "Hopf solitons in the Nicole model — The Nicole model is a conformal ﬁeld theory in three-dimensi onal space."
---
In this section we present the results of numerical computations o f Hopf solitons using
the volume-preserving ﬂow algorithm, with initial conditions constru cted as in the previous
section. The simulation region Ω consists of the cube |xi| ≤ 75 with spatial derivatives
approximated by fourth-order accurate ﬁnite diﬀerences using a lattice spacing ∆ x = 1. The
ﬂow is evolved using an explicit method with timestep ∆ t = 0. 1 and is terminated once the
energy has stabilized at a constant value.
In the continuum theory in Euclidean space the energy of a given solu tion is invariant
under a spatial rescaling. The simulation lattice and ﬁnite region Ω mea n that the energy is
not independent of the volume V, but for a reasonable range of V we ﬁnd that there is only a
weak variation of the energy. The results of varying V suggest that our quoted energies should
be accurate to around one percent. In situations where there ar e two diﬀerent solutions with
the same value of Q, then comparisons of energies are made using similar volumes. Genera lly
the proﬁle function g(r) is taken to have a simple linear form, with a cutoﬀ to ensure that
the boundary condition is satisﬁed. Varying the cutoﬀ allows diﬀeren t values of V to be
investigated, and the results are found to be consistent within the errors mentioned above,
of around one percent.
As a ﬁrst test the A1, 1 solution with Q = 1 is computed using initial conditions (3.2)
with a simple linear proﬁle function. The energy is calculated to be E = 1. 000, which agrees
with the exact solution to three decimal places. This accuracy is bey ond that expected in
general. Figure 1.1 displays the position curve for this Q = 1 soliton. For clarity, a tube
around the position is displayed by plotting an isosurface where φ 3 is slightly greater than
−1. The stability of this solution has been conﬁrmed by applying pertur bations and also
by using initial conditions in which a squashing perturbation is applied to break the axial
symmetry of the A1, 1 rational map constructed ﬁeld. Under the volume-preserving ﬂow the
axial symmetry is restored and the same solution is recovered.
7
Figure 1: Position curves for the known lowest energy solitons with H opf charges 1 ≤ Q ≤ 8.
The situation is similar for the Q = 2 solution of type A2, 1, which is shown in Figure 1.2
and has been constructed using initial conditions (3.3) with ( n, m ) = (2 , 1). This solution
is found to be stable under perturbations that break the axial sym metry and its energy is
computed to be E = 1. 794. This is expected to be the same solution as found using toroidal
coordinates, though our energy is 3% lower than that reported in [1 0]. This diﬀerence is
slightly more than that expected from studying variations of the vo lume V. A comparison of
our results for axially symmetric solutions with larger values of Q reveals a better agreement
with the toroidal computations in [10], so the origin of the unusually lar ge disagreement in
the case of Q = 2 remains unclear. We have also computed a solution of the type A1, 2 and
conﬁrmed the results of [10], that this solution has an energy great er than that of the type
A2, 1. This result agrees with the similar situation in the Skyrme-Faddeev mo del.
In the Skyrme-Faddeev model the axially symmetric Q = 3 solution of type A3, 1 is
unstable to a perturbation that breaks the axial symmetry [4] to f orm a twisted ring. The
notation ~A3, 1 is used to denote the type of this solution, to indicate that it has the same
topological type as A3, 1 but that the axial symmetry is broken. We have conﬁrmed that
a similar situation occurs in the Nicole model by ﬁrst constructing the A3, 1 solution, using
initial conditions (3.3) with ( n, m ) = (3 , 1), and then applying a non-axial perturbation. The
resulting twisted ring solution is displayed in Figure 1.3 and its energy is lis ted in Table 1,
together with the energies of all the minimal energy solutions found for 1 ≤ Q ≤ 8.
In the Skyrme-Faddeev model the minimal energy soliton with Q = 4 is axially symmetric
and is of the type A2, 2 [5]. A solution of this type has been constructed in the Nicole model
using toroidal coordinates [10]. We have computed this solution, usin g initial conditions
(3.3) with ( n, m ) = (2 , 2), but found that, in constrast to the Skyrme-Faddeev model, this
solution is unstable to perturbations that break the axial symmetr y. Such a perturbation
leads to the linked solution displayed in Figure 1.4, which is of the type L1, 1
1, 1. We have also
conﬁrmed that the same solution is obtained by starting with the initia l conditions (3.5)
8
Q Type E E/Q 3/ 4
1 A1, 1 1.000 1.000
2 A2, 1 1.794 1.067
3 ~A3, 1 2.535 1.112
4 L1, 1
1, 1 3.156 1.116
5 L1, 1
1, 2 3.739 1.118
6 L1, 1
2, 2 4.339 1.132
7 K3, 2 4.843 1.125
8 L2, 2
2, 2 5.297 1.114
Table 1: Energies and types of the known minimal energy solitons with 1 ≤ Q ≤ 8.
 0.98
 1
 1.02
 1.04
 1.06
 1.08
 1.1
 1.12
 1.14
 0  1  2  3  4  5  6  7  8  9
E/Q3/4
Q
Figure 2: The ratio of the energy E to the conjectured bound Q3/ 4 for the known minimal
energy solitons with 1 ≤ Q ≤ 8.
with n = 1. The energy of this solution can be found in Table 1.
Solitons with Q = 5 , 6, 7, 8 have been constructed using a variety of initial conditions
for each Q, including perturbed axial ﬁelds, links and knots. The resulting minima l energy
solitons for each Q are displayed in Figure 1 and their energies and types are listed in Table 1.
For Q = 5, 6 the solitons are links and have the same type as in the Skyrme-Fadd eev model.
For Q = 7 the soliton is a trefoil knot and again this agrees with the result of the Skyrme-
Faddeev model. For Q = 8 the soliton is a link of type L2, 2
2, 2. In the Skyrme-Faddeev model
the minimal energy soliton with Q = 8 is also a link, but it has the diﬀerent type L1, 1
3, 3. In
the Skyrme-Faddeev model initial conditions of the type L2, 2
2, 2 develop reconnections during
the energy minimization process and this produces the minimal energ y link L1, 1
3, 3 [6].
In the Skyrme-Faddeev model it has been shown [16] that a lower bo und on the energy
exists of the form E ≥ k Q
3
4 , where k is a known constant. To date, a similar lower bound
9
has not been proved for the Nicole model: see [10] for a discussion o f the technical diﬃculties
in adapting the proof in [16] to the Nicole model. A conjectured lower b ound for the Nicole
model is E ≥ Q
3
4 , where the constant has been set to unity, as this is the largest pos sible
value consistent with the energy of the explicit Q = 1 solution. In the ﬁnal column of Table 1
we list the ratio of the energy to this conjectured bound and plot th is ratio in Figure 2. It
is clear that our numerical results are consistent with the conject ured bound. Furthermore,
for Q > 2 the excess above the bound appears to settle down to a value aro und 12% , which
suggests that the solutions we have found are good candidates fo r the global energy minima
for these values of Q.
