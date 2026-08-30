---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic ﬁelds"
section_id: sec-008-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 11-14
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magne tic ﬁelds is presented."
---
The authors gratefully acknowledge ﬁnancial support from Volksw agen Foundation
and helpful discussions with Mitchell A. Berger.
Appendix A. Equivalence of boundary conditions
We prove for a simply connected volume V the equivalence of the boundary conditions
B · n|∂V = 0 and A × n|∂V = 0.
First note that A × n|∂V = 0 implies B · n|∂V = 0: Locally on the boundary we
can write n = ∇β, where β(x) is a scalar function deﬁned such that β(x) = β0 deﬁnes
the boundary ∂V . Thus A × n|∂V = 0 implies A|∂V = α∇β for some α(x). Then
B|∂V = ∇α × ∇β and therefore B · n|∂V = 0.
To prove the reverse we start with an arbitrary vector potential A which
will in general have a non-vanishing component A|| tangential to the surface ∂V .
We can express A|| as a one-form α deﬁned only on ∂V . Then the assumption
B · n|∂V = ( ∇ × A||) · n = 0 written in diﬀerential forms reads dα = 0 on ∂V .
FromV being simply connected it follows that ∂V has the same homotopy type as
Third-order topological invariant 12
the two-sphere S2. But since the cohomology vector space H 1(S2;IR) = 0, all closed
one-forms are exact. Therefore there exists a scalar function ψ on ∂V such that
α = dψ. This in turn implies that a gauge exists such that A|||∂V = 0 and thus
A × n|∂V = 0.
Appendix B. Gauge invariance of the third-order invariant H (3)
We now prove that the integral invariant (19) is unchanged under a ll gauge
transformations Ai → Ai′
= Ai + ∇φi for i = 1 , 2, 3, which obey the following
two conditions: First we require
∇ · Gi = ∇ · Gi′
= 0, (B.1)
where as before we deﬁne Gi = Aj × Ak and Gi′
= Aj ′
× Ak′
for cyclic indices i,j,k .
Second, the gauge transformations must respect the boundary condition
Ai × n|∂V = Ai′
× n|∂V = 0, (B.2)
where n is a normal vector to the boundary ∂V of the integration volume V .
It is easily checked that a general gauge transformation that leav es the condition
∇ · Gi = 0 unchanged for i = 1, 2, 3 has to be a simultaneous gauge transformation of
all three ﬁelds. Substituting Ai + ∇φi for Ai our invariant of equation (19) changes
according to
H (3) →H (3)′
=
∫
V
(A1 + ∇φ1) · [(A2 + ∇φ2) × (A3 + ∇φ3)] d3x (B.3)
=
∫
V
A1 · (A2 × A3) d3x
+
∫
V
[
∇φ1 · (A2 × A3) + ∇φ2 · (A3 × A1) + ∇φ3 · (A1 × A2)
]
d3x
+
∫
V
[
A1 · (∇φ2 × ∇φ3) + A2 · (∇φ3 × ∇φ1) + A3 · (∇φ1 × ∇φ2)
]
d3x
+
∫
V
∇φ1 · (∇φ2 × ∇φ3) d3x.
We have to show that for gauge transformations respecting equa tions (B.1) and (B.2),
H (3)′
=H (3), i.e. the sum of the last three integrals in equation (B.4) has to vanish .
We can rewrite the ﬁrst integral as∫
V
∇φi · Gi d3x =
∫
∂V
φiGi · n d2x −
∫
V
φi(∇ · Gi) d3x = 0,
which vanishes since Ai × n|∂V = 0 implies Gi · n|∂V = 0. To show that the second
integral vanishes we use the identities
∇φ2 × ∇φ3 = ∇ × (φ2∇φ3) = −∇ × (φ3∇φ2) (B.4)
= 1
2 ∇ × (φ2∇φ3 −φ3∇φ2) (B.5)
and
∇ · G1′
− ∇ · G1 = ∇φ3 · B2 − ∇φ2 · B3,
Third-order topological invariant 13
as well as expressions obtained by cyclic permutations of the indices (1, 2, 3).
Substituting the ﬁrst identity into the second integral we obtain∫
V
[
A1 · ( 1
2 ∇ × (φ2∇φ3 −φ3∇φ2)) + (1, 2, 3) cyclic
]
d3x
= − 1
2
∫
∂V
[
(A1 × (φ2∇φ3 −φ3∇φ2)) · n + (1, 2, 3) cyclic
]
d2x
+ 1
2
∫
V
[
(∇ × A1) · (φ2∇φ3 −φ3∇φ2) + (1, 2, 3) cyclic
]
d3x
= + 1
2
∫
V
[
φ1(B3∇φ2 − B2∇φ3) + (1, 2, 3) cyclic
]
d3x
= − 1
2
∫
V
[
φ1(∇ · G1′
− ∇ · G1) + (1, 2, 3) cyclic
]
d3x
= 0 .
The surface integral vanishes due to condition (B.2) and the last vo lume integral due
to condition (B.1). Finally we can see that the third integral vanishes by substituting
equation (B.5) for the term ∇φ2 × ∇φ3
∫
V
∇φ1 · (∇φ2 × ∇φ3) d3x = 1
2
∫
V
(∇φ1 · ∇ × (φ2∇φ3 −φ3∇φ2)) d3x
= 1
2
∫
∂V
(φ2∇φ3 −φ3∇φ2) × ∇φ1 · n d2x
= 0.
In the last step we used that due to condition (B.2) the gradients ∇φ1, ∇φ2 and ∇φ3
have to be parallel to n. This completes the proof.
Appendix C. Equivalence of the link integrals for disjunct ﬂ ux tubes
The equivalence of the third-order link integrals as given by Monasty rsky and Sasorov
(1987), Berger (1990) and Ruzmaikin and Akhmetiev (1994) for th ree disjunct
and mutually unlinked ﬂux tubes Ui with the integral (19) is shown as follows.
Monastyrsky and Sasorov gave an integral which corresponds to the Massey triple
product and reads in vector notation:∫
∂U 1
(A1×F1−A3×F3) d2x, with ∇ × F1 = G1 := A2 × A3, for 1,2,3 cyclic. (C.1)
The integration is taken over the surface of tube U1. Cyclic permutations of indices
in (C.1) yield equivalent expressions. Note that the Gi in this representation are
evaluated only outside the tubes Ui where ∇ · Gi = 0 for any gauge. To convert this
integral into a volume integral over the whole space, one has to eva luate Gi and Fi
on Ui and therefore encounters the problem of ∇ · (Aj × Ak)|Ui ⁄= 0 for an arbitrary
gauge. To overcome this problem Berger deﬁned Gi within the ﬂux tubes as
Gi :=



Aj × Ak − Φ (j)kBj on Uj,
Aj × Ak + Φ (k)j Bk on Uk,
Aj × Ak else,
withi,j,k cyclic and ∇Φ (i)j = Aj|Ui.(C.2)
The resulting volume integral∫
V
B1 ·
(
F1 − Φ (1)2A3
)
d3x (C.3)
Third-order topological invariant 14
is equivalent to (C.1), as shown in Berger (1990). Using the same con struction with
potentials Φ (i)j Ruzmaikin and Akhmetiev (1994) have rewritten (C.3) in a more
symmetric form.
Now, instead of using the additional potentials Φ (i)j , we can just as well use the
special gauge
Ai → ˜Ai := Ai − ∇Φ (j)i − ∇Φ (k)i ,
which implies ˜Ai|Uj = 0 for i ⁄= j. In other words, the corresponding new ˜Φ (i)j are
set to zero and deﬁnition (C.2) implies condition (i) of the Theorem in se ction 3.
Furthermore, suppressing tildes, (C.3) turns into
∫
V
B1 × F1 d3x =
∫
V
A1 × G1 d3x +
∫
∂V
(A1 × F1) · n d2x
=
∫
V
A1 × G1 d3x +
∫
∂V
(n × A1) · F1 d2x
=
∫
V
A1 × G1 d3x , (C.4)
which ﬁnally shows the equivalence of the integrals (C.1) and (19) for the case of three
pairwise unlinked ﬂux tubes.
