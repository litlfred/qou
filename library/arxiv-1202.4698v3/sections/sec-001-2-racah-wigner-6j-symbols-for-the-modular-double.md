---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-001-2-racah-wigner-6j-symbols-for-the-modular-double
section_title: "Racah-Wigner 6j symbols for the modular double"
section_number: 2
pages: 2-5
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
2.1 Self-dual representations of Uq(sl(2, R)) and the modular double
We will be considering the Hopf-algebraUq(sl(2, R)) which has generatorsE,F andK subject
to the usual relations. This algebra has a one-parameter family of representations Pα
Eα ≡πα(E) := e+πbx coshπb(p −s)
sinπb2 e+πbx,
Fα ≡πα(F ) := e−πbx coshπb(p +s)
sinπb2 e−πbx,
Kα ≡πα(K) := e−πbp, (2.1)
3
where p and x are operators acting on functions f (x) as pf (x) = (2πi)−1 ∂
∂xf (x) and xf (x) =
xf (x), respectively. In the deﬁnitions (2.1) we are parameterizi ngq asq =eπib2
, and write the
parameterα asα = Q/2 + is. There is a maximal dense subspace Pα ⊂ L2(R) on which all
polynomials formed out of Eα, Fα and Kα are well-deﬁned [BT2, Appendix B].
These representations are distinguished by a remarkable se lf-duality property: They are au-
tomatically representations of the quantum group U˜q(sl(2, R)), where ˜q = eπi/b2
ifq = eπib2
.
These representations are generated from operators ˜Eα, ˜Fα and ˜Kα which are deﬁned by formu-
lae obtained from those in (2.1) by replacing b → b−1. The subspace Pα is simultaneously a
maximal domain for the polynomial functions of ˜Eα, ˜Fα and ˜Kα [BT2, Appendix B].
This phenomenon was observed independently in [PT1] and in [F99]. It is closely related to
the fact that Eα, Fα and Kα are positive self-adjoint generators which allows one to construct
˜Eα, ˜Fα and ˜Kα as E1/b2
α F1/b2
α , K1/b2
α [BT1].
It was proposed in [PT1, BT1] to construct a noncompact quantum group which has as com-
plete set of tempered representations the self-dual representations Pα. It’s gradually becoming
clear how to realize this suggestion precisely. Relevant st eps in this direction were taken in
[BT1] by deﬁning co-product, R-operator and Haar-measure of such a quantum group. Further
important progress in this direction was recently made in [I p]. Following [F99], we will in the
following call this noncompact quantum group the modular double of Uq(sl(2, R)).
2.2 Normalized Clebsch-Gordan coefﬁcients for the modular double
The Clebsch-Gordan maps Cα3
α2,α1 : Pα2 ⊗ Pα1 → P α3 were constructed in [PT2]. The deﬁning
intertwining property is
Cα3
α2,α1 · (πα2 ⊗πα1)(∆(X)) = πα3 · Cα3
α2,α1. (2.2)
In [PT2] it was found that the Cα3
α2,α1 can be represented as integral operators of the form
(Cα3
α2,α1ψ)(x3) =
∫
R2
dx1dx2
(α3
x3 | α2
x2
α1
x1
)
bψ(x2,x 1), (2.3)
The intertwining property (2.2) will be satisﬁed if we take
(α3
x3 | α2
x2
α1
x1
)
=
(α3
x3 | α2
x2
α1
x1
)an
b , with
(α3
x3 | α2
x2
α1
x1
)an
b =e−πi(∆ α 3 −∆ α 1 −∆ α 2 )/2D− i
2 (α1+α2+α3−Q)
(
x2 −x1 − i α3
2
)
(2.4)
×D− i
2 (Q+α2−α3−α1)
(
x2 −x3 − i α1
2
)
D− i
2 (Q+α1−α3−α2)
(
x3 −x1 − i α2
2
)
.
In (2.4) we are using the notations ∆ α =α(Q −α) withQ =b +b−1 and
Diα(x) = Sb(Q/2 − ix +α)
Sb(Q/2 − ix −α). (2.5)
4
Sb(x) is the so-called double Sine-function which is closely related to the functions called quan-
tum dilogarithm in [FK2] hyperbolic gamma function in [Ru], and quantum exponential func-
tion in [Wo]. Deﬁnition and relevant properties are recalled in Appendix A.
One should note, however, that our deﬁnition of the 3j coefﬁcients (2.4) is not canonical, we
might equally well use
(α3
x3 | α2
x2
α1
x1
)′
b in (2.3), with
(α3
x3 | α2
x2
α1
x1
)′
b :=M(α3,α 2,α 1)
(α3
x3 | α2
x2
α1
x1
)an
b . (2.6)
This will satisfy (2.2) for arbitrary functionsM(α3,α 2,α 1). A natural choice forM(α3,α 2,α 1)
can be determined by requiring the Weyl-invariance of the Cl ebsch-Gordan maps. In order to
formulate this requirement, we will need the intertwining operator Rα : Pα → P Q−α which can
be represented explicitly as integral operator [PT2]
(Rαf )(x) := Sb(2α)
∫
R
dx′ D−iα(x −x′)f (x). (2.7)
We may now require that
Cα3
α2,α1 · (1 ⊗ RQ−α1) = Cα3
α2,Q−α1,
Cα3
α2,α1 · (RQ−α2 ⊗ 1) = Cα3
Q−α2,α1,
Rα3 · Cα3
α2,α1 = CQ−α3
α2,α1 . (2.8)
We claim that (2.8) is satisﬁed if we chooseM(α3,α 2,α 1) as
M(α3,α 2,α 1) = (2.9)
=
(
Sb(2Q −α1 −α2 −α3)Sb(Q −α1 −α2 +α3)Sb(α1 +α3 −α2)Sb(α2 +α3 −α1)
)− 1
2.
To prove this claim let us consider, for example, the ﬁrst of t he equations in (2.8), which
would follow from the identity
Sb(2 ¯α1)
∫
R
dx′
1
(α3
x3 | α2
x2
α1
x′
1
)an
b D−i¯α1(x′
1 −x1) = ξ
(α3
x3 | α2
x2
¯α1
x1
)an
b , (2.10)
where we use abbreviation ¯α =Q −α andξ =Sb(α2 +α3 −α1)Sb(2Q −α1 −α2 −α3). This
identity can easily be rewritten in the form [BT1, Equation (A.34)] in which it is recognized as
the famous star-triangle relation, see e.g. [BMS1]. Proofs can be found in [K2, V]. It can also
be derived easily from the so-called elliptic beta-integral [S01] following the strategy discussed
in Appendix B.
We will denote the Clebsch-Gordan coefﬁcients deﬁned by (2.6) with functionM(α3,α 2,α 1)
given in (2.9) as
(α3
x3 | α2
x2
α1
x1
)
b. We would like to stress that both
(α3
x3 | α2
x2
α1
x1
)an
b and
(α3
x3 | α2
x2
α1
x1
)
b
have their virtues. While
(α3
x3 | α2
x2
α1
x1
)
b has more natural symmetry properties, the virtue of(α3
x3 | α2
x2
α1
x1
)an
b is to have nice analytic properties in all of its variables.
5
