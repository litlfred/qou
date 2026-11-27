---
doc_id: arxiv-1711.09011v1
doc_title: "Quantum groups and braid groups as fundamental symmetries"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 1711.09011v1.pdf
source_sha256: d046698777f38634
toc_source: inferred
doc_brief: "Quantum groups and braid groups as fundamental symmetries — 12 sections: Front matter; Introduction; The Helon model"
---
Quantum groups (which are algebras rather than groups) provide a generalization of the fa-
miliar symmetry concepts encoded in Lie groups. Such quantum groups are deformations on Hopf
algebras and depend on a deformation parameter q with the value q = 1 returning the undeformed
universal enveloping algebra. First formalized by Jimbo [1] and Drinfeld [2] as a class of Hopf al-
gebras, quantum groups have found many applications in theoretical physics, see [3, 4, 5, 6, 7, 8, 9]
and references therein. Likewise, the (Artin) braid groups are an extension of the symmetric groups
in which the square of group generators need no longer be equal to the identity. A braid may be
thoughts of as an intertwining of strands between two rows of n points, one set above the other.
In 2005, Bilson-Thompson [10] proposed the Helon model in which the Standard Model (SM)
elementary particles are identiﬁed as braidings of three ribbons with two crossings. With the ad-
ditional structure that each ribbon can be twisted (interpreted physically as electric charge) these
braids, satisfying certain conditions, map precisely to the ﬁrst generation fermions of the SM. The
original model has since been expanded into a complete scheme for the identiﬁcation of the SM
fermions and weak vector bosons for an unlimited series of generations [11, 12, 13]. This topolog-
ical model ﬁts naturally into the context of Loop Quantum Gravity (LQG) which uses spin network
graphs with edges labelled by representations of SU(2). Instead labelling the edges by representa-
tions of the quantum group SUq(2) introduces a cosmological constant and requires that the edges
be thickened to ribbons [29].
Kauffman and Lomonaco have demonstrated, in what they call the Clifford Braiding Theorem,
that particular elements of Clifford algebras form representations of (circular) braid groups [ 14].
Clifford (or geometric) algebras have found many applications in physics [ 15, 16, 17, 18] and
they are also closely related to the four normed division algebras (NDAs), the reals R, complex
numbers C, (non-commutative) quaternionsH, and (non-associative) octonionsO. One may expect
therefore that the NDAs to admit representations of particular braid groups. This is interesting
because in 2015 Furey showed that most spacetime and internal symmetries of the SM may be
derived starting from only the NDAs acting on themselves [ 19]. In particular, generalized ideals
of the complex quaternions give all the SM representations of the Lorentz group whereas those
of the complex octonions mirror the behaviour of a single generation of quarks and leptons under
unbroken SU(3)c and U(1)em.
The main idea presented here is that using the Clifford Braiding Theorem of Kauffman and
Lomonaco it is possible to investigate the braid content of the description of SM symmetries based
on the NDAs and compare it to the braided structures found in the Helon model. Remarkably,
we ﬁnd that the braid groups representations admitted by the complex numbers and quaternions
are precisely those braid groups present in the Helon model. Further work to investigate the con-
nections between the two models, in particular the role of the octonions and the braid group they
represent, is ongoing.
In section 2 we review a recent attempt at taking a quantum group as the broken ﬂavour sym-
metry for hadrons. Following a review of the Helon model in section 3 and the NDAs in section
4, we then use the Clifford braiding theorem to ﬁnd the braid group representation admitted by the
normed division algebras in section5. In section 6 we demonstrate that the braid groups represented
by the NDAs are precisely those that appear in the Helon model.
1
Quantum groups and braid groups Niels G. Gresnigt
2. Quantum group SUq(3) as a ﬂavour symmetry
In this section we review recent attempts at taking a quantum group as a fundamental ﬂavour
symmetry. The use of the classical SU(3) group as a ﬂavour symmetry gives rise to mass relations
between the multiplets of the octet and decuplet baryons [20, 21]. The Gell-mann-Okubo formula
for octet baryons and the Okubo formula for decuplet baryons are
N + Ξ = 3
2 Λ + 1
2 Σ, (2.1)
and
Ω− ∆ = 3(Ξ∗− Σ∗), (2.2)
respectively.
Gavrilik considered the use of the quantum groupSUq(3) as a ﬂavour symmetry to obtain gen-
eralized baryon mass formulas [22, 23, 24, 25]. For suitable values of the deformation parameter q
(taken to be a root of unity), the obtained mass formulas are accurate enough that mass differences
within baryon multiples, due to electromagnetic mass contributions, can no longer be ignored. Ac-
counting for these electromagnetic mass contribution by using the general QCD parametrization
scheme of Morpurgo [26], Gresnigt [27] derived the following generalized mass formulas for the
octet baryons:
p + 2[3]q
3[2]q
Ξ0 +
( 1
[2]q− 1− 2[3]q
3[2]q
)
Ξ− = [3]q
[2]q
Λ− [3]q
3[2]q
Σ0 +
( 1
[2]q− 1− 2[3]q
3[2]q
)
Σ− + Σ+, (2.3)
where
[N]q = qN− q−N
q− q−1 , (2.4)
is a q-number, and q can in general be real or complex. Equation ( 2.3) is only valid for the case
where q = qn = eiθ8 = e
iπ
n for integer n. The best ﬁt to experimental data occurs when n = 7, in
which case equation (2.3) simpliﬁes to:
p + (2Ξ0 + Ξ−)
3([2]q7− 1) = Λ
[2]q7− 1 + (Σ−− Σ0)
3([2]q7− 1) + Σ+. (2.5)
Similarly, the Okubo formula for decuplet baryons becomes:
Ω−− ∆− = ([2]q + 1)(Ξ∗−− Σ∗−), (2.6)
with the best ﬁt occurring when q = qn = eiθ10 = e
iπ
21 . With the values of q so chosen, the errors of
these mass relations are only 0.02% and 0.08% respectively; a factor of 20 reduction compared to
the standard Gell-mann-Okubo mass formulas. These results are summarised in table 1.
Additionally, the use of a quantum group as a ﬂavour symmetry suggest an explicit formula
for the Cabibbo angle, taken to be π
14, in terms of the deformation parameter q and spin parity JP
of the baryons [22, 27, 28]
θC =−iJP lnq. (2.7)
2
Quantum groups and braid groups Niels G. Gresnigt
GMO formula (2.1) Equation ( 2.5)
LHS (MeV) 2257.2 2582.0
RHS (Mev) 2270.1 2582.6
Error (%) 12.9 0.6
Okubo formula (2.2) Equation ( 2.6)
LHS (MeV) 440.5 440.5
RHS (Mev) 446.5 440.2
Error (%) 6.0 0.3
Table 1: Decuplet baryon mass formula.
