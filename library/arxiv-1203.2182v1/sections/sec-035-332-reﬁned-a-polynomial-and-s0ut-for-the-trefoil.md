---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-035-332-reﬁned-a-polynomial-and-s0ut-for-the-trefoil
section_title: "Reﬁned A-polynomial and S0(u,t ) for the trefoil"
section_number: 3.3.2
pages: 40-41
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
The next example is naturally the trefoil knot T 2,3 = 31. First, let us discuss the structure
of its reﬁned A-polynomial and the associated free energy S0(u,t ) from the viewpoint of the
quantum A-polynomial given in (3.134). The reﬁned A-polynomial can be determined by
setting q = 1 in (3.134):
Aref
T 2,3(x,y ;t) =y2 − 1 −xt2 +x3t5 +x4t6 + 2x2t2(t + 1)
1 +xt3 y + (x − 1)x3t4
1 +xt3 = 0 . (3.160)
We stress that for generic values of t this form does not factorize, as the discriminant
∆ =
(1 +x2t3
1 +xt3
) 2(
1 − 2t2x + (4t2 + 2t3 +t4)x2 + 2t5x3 +t6x4)
is not a complete square. This means that the abelian branch – represented by a factor y − 1
in the classical, unreﬁned A-polynomial – is “mixed” in together with the non-abelian br anch
for generic values oft ⁄= −1. Indeed, the value t = −1 is very special because the discriminant
factorizes
∆(t=−1) = (1 + x3)2,
and, as a result, the A-polynomial also factorizes
Aref
T 2,3(x,y ;t = −1) = ( y − 1)(y +x3). (3.161)
– 39 –
In the latter expression, y − 1 represents the abelian branch, while the “interesting” fa ctor
y +x3 is what sometimes referred to as the reduced A-polynomial for the trefoil knot. We see
that for generic values of t such a factorization does not occur, and the “character vari ety”
Aref(x,y ;t) = 0 is irreducible, with only one component. For t = −1 it becomes reducible
and splits into two (or, in general, several) components.
Once we found the reﬁned curve, we can easily compute S0(u,t ) =
∫
logy dx
x using (2.7).
For the trefoil knot there is no compact expression for this i ntegral, but one can write it as a
Taylor series in (t + 1). Namely, by solving the quadratic equation Aref
T 2,3(x,y ;t) = 0, we ﬁnd
y = 1 −xt2 +x3t5 +x4t6 + 2x2t2(t + 1)
2(1 +xt3) − 1
2
√
∆ =
= −x3 + (t + 1)x3 (x − 2)(3x2 − 2x + 2)
(x − 1)(1 −x +x2) + O
(
(t + 1)2)
(3.162)
The ﬁrst term −x3 corresponds to the non-abelian branch in (3.161). Then, exp anding the
integrand logy dx
x in powers of ( t + 1) and integrating term by term we ﬁnd the following
structure
