---
doc_id: arxiv-0705.1468v1
doc_title: "Knots in the Skyrme-Faddeev model Paul Sutcliffe"
section_id: sec-001-the-skyrme-faddeev-model-and-low-charge-solitons
section_title: "The Skyrme-Faddeev model and low charge solitons"
section_number: null
pages: 3-7
source_pdf: 0705.1468v1.pdf
source_sha256: 4ff578cb3657e4a4
doc_brief: "Knots in the Skyrme-Faddeev model Paul Sutcliffe — The Skyrme-Faddeev model is a modiﬁed sigma model in three-d imensional space, which has string-like topological solitons classiﬁed by th e"
---
The Skyrme-Faddeev model involves a map φ : R3 ↦→S2, which is realized as a real three-
component vector φ = (φ1, φ2, φ3), of unit length, φ · φ = 1. As this paper is concerned only
with static solutions then the model can be deﬁned by its ener gy
E = 1
32π2
√
2
∫
∂iφ · ∂iφ + 1
2(∂iφ × ∂jφ ) · (∂iφ × ∂jφ ) d3x, (2.1)
where the normalization is chosen for later convenience. Th e ﬁrst term in the energy is
that of the usual O(3) sigma model and the second is a Skyrme term, required to pr ovide a
balance under scaling and hence allow solitons with a ﬁnite n on-zero size.
Finite energy boundary conditions require that the ﬁeld ten ds to a constant value at
spatial inﬁnity, which is chosen to be φ (∞) = (0 , 0, 1) = e3. This boundary condition com-
pactiﬁes space to S3, so that the ﬁeld becomes a map φ : S3 ↦→S2. Such maps are classiﬁed
by π3(S2) = Z, so there is an integer-valued topological charge Q, the Hopf charge, which
gives the soliton number. Unlike most theories with topolog ical solitons, the topological
charge is not a winding number or degree of a mapping. Rather, it has a geometrical inter-
pretation as a linking number of ﬁeld lines, as follows. Gene rically, the preimage of a point
on the target two-sphere is a closed loop (or a collection of c losed loops) in the three-sphere
domain obtained from the compactiﬁcation of R3. Two loops obtained as the preimages of
any two distinct points on the target two-sphere are linked e xactly Q times, where Q is the
Hopf charge.
The Hopf charge can be written as the integral over the three- sphere domain of a charge
density, but this density is non-local in the ﬁeld φ , as the following construction demon-
strates. Let ω denote the area two-form on the target two-sphere and let F = φ ∗ω be its
pull-back under φ to the domain three-sphere. The triviality of the second coh omology
group of the three-sphere implies that F is an exact two-form, say F = dA. The Hopf charge
is then given by integrating the Chern-Simons three-form ov er the three-sphere as
Q = 1
4π2
∫
S3
F ∧ A. (2.2)
The energy bound
E ≥ c Q3/ 4, where c =
( 3
16
) 3/ 8
≈ 0.534 (2.3)
has been proved [12, 9], and it is known that the fractional po wer is optimal [10], though it is
expected that the above value of the constant c is not. Motivated by a study of the Skyrme-
Faddeev model on a three-sphere with a ﬁnite radius, togethe r with an analogy with the
Skyrme model, Ward has conjectured [13] that the above energ y bound holds with the value
c = 1 (hence the choice of normalization factor for the energy i n (2.1)), but this has not been
proven. As discussed shortly, the current energy values kno wn for low charge solitons are in
good agreement with Ward’s conjectured energy bound, and la ter it will be demonstrated
that the energies for higher charge solitons are too.
3
The simplest examples of Hopf solitons are axially symmetri c and their qualitative fea-
tures may be described as follows. First, consider the model (2.1) deﬁned in two-dimensional
space, so that the boundary conditions now result in a compac tiﬁcation of space from R2 to
S2. The ﬁeld is then a map φ : S2 ↦→S2 and is classiﬁed by an integer m ∈ Z = π2(S2), which
is the usual winding number familiar from the O(3) sigma model itself. Strictly speaking,
in order to have two-dimensional solitons with a ﬁnite size i n this model then a potential
term must also be included, upon which the two-dimensional s olitons are known as baby
Skyrmions [11], but this aspect is not crucial for the discus sion here. Returning to the
three-dimensional model, then a toroidal ﬁeld conﬁguratio n can be formed by embedding
the two-dimensional soliton in the normal slice to a circle i n space. The two-dimensional
soliton has an internal phase and this can be rotated through an angle 2 πn, as it travels
around the circle once, where n ∈ Z counts the number of twists. A ﬁeld conﬁguration of
this type has Hopf charge Q = nm, and it will be denoted by An,m , so the ﬁrst subscript
labels the number of twists and the second is the winding numb er of the two-dimensional
soliton forming the loop.
The minimal energy Q = 1 soliton is of the type A1, 1 and has been studied numerically by
a number of authors [6, 5, 1, 7, 14] using diﬀerent algorithms . Taken together, these results
suggest that the charge one soliton has an energy of around E = 1 .21, and this is part of
a general pattern where the minimal energy soliton exceeds W ard’s conjectured bound by
around 20%. The numerical computations reported in this paper produce a charge one energy
of E = 1.204, and hence appear to underestimate the energy by an amount of t he order of 1%.
For low charge solitons this accuracy could be improved by in creasing the resolution of the
numerical grid, but it is computationally too expensive to i ncrease the resolution for all the
large number of simulations reported here for large charges . Moreover, although the energy
is a slight underestimate for a given soliton solution, the r elative energies between two given
solutions are much more accurate than this (changing grid re solutions and sizes suggests an
accuracy of around 0 .1%) and it is more important to preserve the relative energie s than the
absolute energy of any single solution.
The details of the numerical computations are similar to tho se of Ref.[1], and full details
of the related numerical code used to study Skyrmions can be f ound in Ref.[2]. Brieﬂy, a ﬁnite
diﬀerence scheme is employed with a lattice spacing ∆ x = 0 .1 on a grid containing (151) 3
lattice points, with the ﬁeld ﬁxed to the vacuum value φ = e3 on the boundary of the grid;
this is preferable to other methods of dealing with the ﬁnite volume simulation domain, such
as the one used in Ref.[1] which led to a more substantial unde restimate of energies, though
again relative energies had a high accuracy. The energy mini mization algorithm proceeds by
evolving second order in time dynamics and periodically rem oving kinetic energy from the
system whenever the potential energy of the system begins to increase. It is based on the
approach employed in Ref.[1], but is computationally more e ﬃcient since the second order
dynamics is derived from the kinetic term of the sigma model o nly, rather than the full
kinetic term determined from the Lorentz invariant Lagrang ian associated with the energy
(2.1). This subtle diﬀerence leads to a more eﬃcient algorit hm since the leading term in the
evolution equations is now diagonal, so a costly matrix inve rsion can be avoided.
4
A sensible deﬁnition of the position of a soliton is to identi fy where the ﬁeld is as far
as possible from the vacuum ﬁeld. A Hopf soliton is therefore string-like, since the soliton’s
position is deﬁned to be the closed loop (or collection of loo ps) corresponding to the preimage
of the point φ = −e3 = (0 , 0, −1), which is antipodal to the vacuum value on the target
two-sphere. To visualize a ﬁeld conﬁguration this position curve is plotted, though for clarity
a tube around this position is displayed, given by an isosurf ace of the form φ3 = −1 + ν,
where generally the value ν = 0.2 is chosen. If a pictorial representation of the Hopf charge
is also required then a second preimage curve can also be plot ted (again as a tube), and
the linking number of these two curves inspected. There is no natural choice for this second
preimage value ( e3 is not a very useful choice) and in this paper when a second pre image
curve is displayed it corresponds to the point φ = ( √2µ − µ2, 0, −1 + µ) where µ = 0 .1. In
what follows this curve will be referred to as the linking cur ve, and since µ is relatively small
then the linking curve remains reasonably close to the posit ion curve, making it fairly easy
to inspect the linking number.
In Figure 1 the position (light tube) and linking (dark tube) curves are displayed for
the known lowest energy solitons with Hopf charges from one t o seven. Given the large
number of numerical simulations performed by diﬀerent grou ps it seems reasonably certain
that these are the minimal energy solitons for these charges . The energies of these solutions
will be discussed later, and as mentioned above they are gene rally around 20% above Ward’s
conjectured bound, but for now it is the structure of the solu tions that is of primary interest,
and this is reviewed below.
The solutions with charges one and two are both axially symme tric, and are of the type
A1, 1 and A2, 1 respectively [5, 6], with one and two twists of the linking cu rve around the
position curve clearly visible. There is a solution of the fo rm A1, 2 [13, 14, 7] but it has
an energy around 13% above that of the minimal charge two soli ton. This solution has
the interpretation of two Q = 1 solitons stacked one above the other, preserving the axia l
symmetry.
The charge three soliton is basically of the type A3, 1 but the axial symmetry is broken as
the position curve is bent [1], so it will be denoted by ~A3, 1 to emphasize that the structure
is deformed. There is an axial solution of the type An, 1 for any integer n, but for n > 2 this
solution is unstable to a coiling instability [1]; a well-kn own phenomenon in other settings
such as twisted elastic rods. The Q = 4 soliton is of the type A2, 2, [8, 13], and may be
thought of as two Q = 2 solitons stacked one above the other. For both Q = 4 and Q = 5
there are also bent solutions [1], similar to the charge thre e soliton, and therefore denoted
~A4, 1 and ~A5, 1, but unlike the Q = 3 case, both these solutions are only local energy minima,
with energies around 2% and 4% above the global minimum, resp ectively. The minimal
energy charge ﬁve soliton provides the ﬁrst example of a link , that is, a solution in which
the position curve contains two or more disconnected compon ents. It consists of a charge
one soliton and a charge two soliton which are linked once [8] , with the result that each of
these solitons gains an additional unit of linking number to make a total of ﬁve. To denote a
link of this type the notation L1, 1
1, 2 will be used, where the subscripts label the charges of the
components of the links and the superscript above each subsc ript counts the extra linking
5
Figure 1: The position (light tube) and linking (dark tube) c urves for the known lowest
energy solitons with Hopf charges 1 ≤ Q ≤ 7.
number of that component, due to its linking with the others. Hence the total charge is the
sum of the subscripts plus superscripts. The charge six soli ton is similar to that of charge
ﬁve, but now both components of the link have charge two [1], s o using the above notation
it is written as L1, 1
2, 2.
Finally, the charge seven soliton is the ﬁrst (and so far only ) example of a knot [1]. The
position curve is a trefoil knot, which has a self-linking or crossing number of three (the
crossing number of a knot is not an invariant and its use in thi s paper refers to the minimal
crossing number over all presentations). An examination of the linking curve in Figure 1
conﬁrms that it twists around the position curve four times a s the knot is traversed, so the
Hopf charge is indeed seven, being the sum of the crossing num ber plus the number of twists.
Any ﬁeld conﬁguration of a trefoil knot will be denoted by K3, 2, which refers to the fact that
the trefoil knot is also the (3 , 2)-torus knot (see the following section for more informati on
regarding torus knots). Note that this notation does not dis play the Hopf charge of the
conﬁguration, which is determined by the twist number as wel l as the crossing number, but
this should not cause any confusion in what follows. Of cours e, for knots and links, as well
as for unknot conﬁgurations, the precise conformation of th e position curve is important in
determining the energy, not just its topological type, but i ts knotted or linked structure is
an important feature in classifying the solution. Thus, for example, the Q = 7 trefoil knot
displayed in Figure 1 is not as symmetric as its typical knot t heory presentation, and it is
signiﬁcant that the energy is lowered by breaking the possib le cyclic C3 symmetry.
Having reviewed the known results for low charge solitons an d introduced the notation
used to label their structural type, it is time to turn to the m ain questions addressed in
this paper. Given the variety of solutions which appear, eve n at low charges, it is diﬃcult
to make a conﬁdent prediction of the kind of behaviour that mi ght arise at higher charges.
6
In particular, an interesting open question is whether more knot solitons appear at higher
charge, and if so what types of knots arise and are they local o r global minima? It could
have been the case that the charge seven trefoil knot was the o nly knot soliton, though in
this paper it will be shown that this is far from true. Also, it would be useful to have at least
a qualitative understanding of the fact that Q = 7 is the lowest charge at which a knot ﬁrst
appears, and desirable to be able to estimate the charges at w hich other knots might exist.
In this section it has been mentioned brieﬂy that at each char ge there are often local
minima in addition to the global minimum, and it is expected t hat the number of local
minima generally increases with the charge. As noted in the i ntroduction, these local minima
can have large capture basins, making it diﬃcult to fully exp lore the space of solutions. For
any relaxation computation this makes the choice of initial conditions a crucial issue. In
particular, it is not obvious how to construct a variety of re asonably low-energy initial
ﬁeld conﬁgurations for all Hopf charges. One family of conﬁg urations are the axial ﬁelds
An, 1, which are all unstable for n > 2. However, even for charges as low as four, initial
conditions which use small perturbations of these unstable solutions get trapped in local
minima. One successful approach for low charges involves co nstructing links by hand [7, 8],
using a numerical cut-and-paste technique where various nu merical ﬁeld conﬁgurations are
sewn together in diﬀerent parts of the simulation grid to cre ate a linked ﬁeld with a given
Hopf charge. Although this approach was the ﬁrst method to su ccessfully yield the global
minima at charges four and ﬁve, it becomes more cumbersome fo r larger charges and is not
applicable for creating knot initial conditions; it is also not very elegant mathematically, but
this is perhaps not a serious criticism. Another set of initi al conditions that have been used
[8] are based on the ﬁelds An,m , with m > 1, though these ﬁelds tend to have relatively
large energies and therefore require quite long simulation times (except for the low charge
examples of A1, 2 and A2, 2). In the following section an analytic ansatz is presented tha t yields
reasonable ﬁeld conﬁgurations for a variety of charges and d escribes all torus knots plus a
wide range of links, in addition to ﬁelds of the type An,m . The key ingredient of the ansatz
involves a rational map from the three-sphere into the compl ex projective line. The ansatz
allows the construction of initial conditions correspondi ng to a variety of locations in ﬁeld
conﬁguration space; in particular, conﬁgurations can be cr eated which are reasonably close
to suspected local energy minima. This approach substantia lly reduces the computational
eﬀort required to explore the energy landscape and makes it f easible to study knots and links
for quite large charges.
