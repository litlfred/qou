---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-100-4-abelian-periods-as-algebraic-integrals-47
section_title: "ABELIAN PERIODS AS ALGEBRAIC INTEGRALS. 47"
section_number: 4
pages: 51-52
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
Note that another choice of ( ... ,ζ pn,... , 1) changes (2iπ)p by multipli-
cation by a unit in Zp. Similarly, up to addition of an element of (2 iπ)pZp,
Log z depends only on z(0); it is sometimes simply denoted by Log z(0).
By choosing a double embedding of Q into C and Qp, one obtains
a canonical element (2 iπ)p, attached to the sequence ( ... ,e 2iπ/pn
,... , 1).
Similarly, if z(0) ∈ Q, then Log z(0) is well-deﬁned up to addition of an
element of (2iπ)pZ.
4.4. Colmez’ construction of abelian p-adic periods.
Let A be an abelian variety deﬁned over a p-adic local ﬁeld K. The
Fontaine-Messingp-adic period pairing is a pairing
∫ (p)
: H 1
dR(A)⊗Tp(A
K )−→ B+
dR
whereTp(A
K ) = lim←−Ker([pn] : AK→AK ) is the Tate module (a Zp-module
of rank 2 dim A with Gal(K/K )-action).
We present Colmez’ construction, which is parallel to 4.1.
Let ω be a diﬀerential form on A of second kind, and F 3
ω the function
on A3 determined as in 4.1. Then:
Proposition 4.4.1 ([Co92, 4.1]) . There exists a locally meromorphic func-
tion Fω on A(BdR), unique up to constant, such that:
(1) dFω =ω.
(2) Fω(z1 +z2 +z3)−Fω(z1 +z2)−Fω(z1 +z3) +Fω(z1) = F 3
ω (z1,z 2,z 3).
(3) If ω =dF , then Fω =F .
Moreover, if α : A1 → A2 is a morphism of abelian varieties and ω is a
diﬀerential form of second kind on A2, then Fα∗ω =α∗Fω.
Note that the function Fω is not multivalued; this fact comes from the
following lemma speciﬁc to the p-adic case:
Lemma 4.4.2 ([Co91, 4.3]) . For any neighborhoodV of 0 inA(B+
dR), there
exists an open subgroup U of A(B+
dR) contained in V such that A(B+
dR)/U is
a torsion group.
Take a proper model A of A overOK. Let γ = (··· ,u n,··· ,u 2,u 1 =
0)∈ Tp(A
K ) with each un ∈ A(OCp), and choose an ∈ A(B+
dR) so that
neither an nor an +Aˆun is close to a pole of ω. For suitable liftings ˆun∈
A(B+
dR) of un (i.e. θ(ˆun) = un), the following holds.
Theorem 4.4.3 ([Co91, 5.2]) . The limit
∮ (p)
γ
ω := lim
n→∞
pn(
Fω(an)−Fω(an +Aˆun)
)
48 I. ANALYTIC ASPECTS OF p-ADIC PERIODS.
converges to an element in B+
dR, and it deﬁnes a non degenerate bilinear
pairing
∮ (p)
: H 1
dR(A)⊗ Tp(A
K)−→ B+
dR,
compatible with the Galois action and the ﬁltrations.
Remark 4.4.4. On composing the period pairing
∫ (p) with θ, one gets a
bilinear map H 1
dR(A)⊗Tp(A
K )−→ Cp which sends Ω 1(A)⊂ H1
dR(A) to
