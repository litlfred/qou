---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-Body Systems in Lattice Effective Field Theory"
section_id: sec-015-the-reduced-symmetry-of-so3z
section_title: "The reduced symmetry of SO(3,Z)"
section_number: null
pages: 29-30
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
toc_source: outline
doc_brief: "Few-Body Systems in Lattice Effective Field Theory — 62 sections: Front matter; Introduction and Motivation; The standard model of particle phy"
---
respectively. As we see in Fig. 3.1 the continuum result and the continuum-regularized one are both
attractive albeit the latter one vanishes for small lattice spacings. This is in line with eﬀective ﬁeld theory,
where all short-range physics is absorbed in contact interaction terms. All lattice realizations show a very
good agreement for distances larger than 3.5 fm, while the trigonometric ones show a repulsive behavior
between 0 fm and 3 fm. This is partially compensated by some contributions which are very negative, e.g.
at a distance of 2 fm for a lattice spacing of 0.98 fm. The exact discretization results are in a very good
agreement with the continuum calculation. We see of course that for lattice spacings smaller than 1.0 fm,
the exact discretization solution is far oﬀfrom the continuum-regularized solution. This means that we
can use the one-pion-exchange potential without extra regulator only in systems with lattice spacings
larger than ∼1 fm. Otherwise, the contact interaction contributions become unnaturally large, and may
not be able to compensate the OPE contribution.
−10
−8
−6
−4
−2
0
2
4
0
1
2
3
4
5
V
1S 0
OPEP [MeV]
r [fm]
V
1S 0
OPEP(r)
V
1S 0
OPEP(r) · flong−range(r)
a = 1.97 fm, impr.0
a = 1.97 fm, impr.1
a = 1.97 fm, exact
a = 1.32 fm, impr.0
a = 1.32 fm, impr.1
a = 1.32 fm, exact
a = 0.98 fm, impr.0
a = 0.98 fm, impr.1
a = 0.98 fm, exact
Figure 3.1: 1S 0 one-pion-exchange potential for various lattice discretization schemes and continuum solutions
with and without position space regularization.
3.2 The reduced symmetry of SO(3, Z)
As argued in Subsec. 2.2.1, the continuum SO(3) symmetry has an inﬁnite number of irreducible
representations and each irreducible representation is identiﬁed with the angular momentum j. This makes
the identiﬁcation straightforward, as each partial wave is directly linked to an irreducible representation
with quantum number j. In fact, this is not possible anymore in a cubic ﬁnite volume. Due to the cubic
symmetry, rotations are only allowed for a discrete and ﬁnite number of values, namely multiplicities of
π/2. E. g., the π/2 rotation around the z-axes is given by the operator,
Rˆz
π
2

= exp

−iπ
2 jz

.
(3.7)
Rotations around the x- and y-axes are deﬁned accordingly with respect to jx, jy. From Eq. (3.7) it is
clear that also the quantum number jz is not a good quantum number anymore, but only jz modulo 4.
23
Chapter 3 Nuclear Lattice Eﬀective Field Theory
The reduced symmetry group is SO(3, Z), which is a ﬁnite group consisting of the representations A1, T1,
E, T2, and A2 [79]. The properties of the representation are summarized in Tab. 3.1.
Rep
dimensionality
jz
Example
A1
1
0 mod 4
Y0,0
T1
3
0,1,3 mod 4
{Y1,1, Y1,0, Y1,−1}
E
2
0,2 mod 4
{Y2,0,
Y2,−2+Y2,2
√
2
}
T2
3
1,2,3 mod 4
{Y2,1,
Y2,−2+Y2,2
√
2
, Y2,−1}
A2
1
2 mod 4
Y3,2−Y3,−2
√
2
Table 3.1: Spherical harmonics for various representations [79].
j
irrep
0
A1
1
T1
2
E ⊕T2
3
A2 ⊕T1 ⊕T2
4
A1 ⊕E ⊕T1 ⊕T2
5
E ⊕T1 ⊕T1 ⊕T2
6
A1 ⊕A2 ⊕E ⊕T1 ⊕T2 ⊕T2
Table 3.2: Irreducible representations for angular momentum j ≤6 [79].
The mapping from SO(3) irreducible representations according to their angular momentum j to the
irreducible representations of SO(3, Z) is shown in Tab. 3.2. There is a one-to-one mapping for systems
with angular momenta zero and one. The situation becomes diﬃcult by including higher angular momenta
and as such higher partial waves. Firstly, the partial waves begin to decompose into parts belonging
to diﬀerent representations. Hence, a formalism must be used that puts together the diﬀerent pieces of
diﬀerent representations to restore the rotational invariant state where the angular momentum is a good
quantum number, see for example in [80, 81]. Additionaly, a representation like the T1 exist for j = 1 and
j = 3, linking the coupled channels 3S 1 −3 D1 and 3D3 −3 G3. Such a mixing is unphysical and should
be removed from the data. This eﬀect has been investigated in Refs. [82, 83] and it is removed by adding
all possible rotational symmetry breaking operators in the theory.
