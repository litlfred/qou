---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-005-22-main-result
section_title: "Main result"
section_number: 2.2
pages: 16-17
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "On q-summation and confluence — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
The formulas above suggest the convergence of the q-Laplace transform
Lqφ to the classical Laplace transform Ldφ (in the direction d ∈ (0, 2π)):
(2.2) Ld(φ)(x) =
∫ ∞eid
0
φ(ξ)e− ξ
xdξ,
where φ is supposed to be holomorphic in a neighborhood of ξ = 0 and to
be analytically continued in an open sector {| argξ −d|<ϵ } with at most
an exponential growth at inﬁnity.
Theorem 2.6. — Let y(q,x ) = ∑
n/greaterorequalslant0yn(q)xn+1 ∈xC[[x]] be a family
of formal power series, with q ∈ (η, 1], for some η ∈ (0, 1). We suppose
that the yn(q)’s are continuous functions of q and that the family φ(q,ξ ) =
Bqy(q,x ) ∈ C{ξ} is solution of a family of equations over P1
C, fuchsian and
non resonant at ∞, in the sense of Assumption 2.7 below.
Letd ∈ [0, 2π) be such thatφ(1,ξ ) is holomorphic on a domain containing
the half line [0,e id∞). Then for any x ∈V := {| argx −d|< π
2 } we have
lim
q→1−
y(q,x ) = Ld(
φ(1,ξ )
)
,
the convergence being uniform on any compact of V .
Notice that y(q,x ) = Lqφ(q,ξ ), so that the result above is actually a re-
sult about the conﬂuence of q-summation. Moreoverφ(q,ξ ) is meromorphic
over C∗ and its poles are contained in a ﬁnite set of lines passing through
the origin. Also for φ(1,ξ ) there are only a ﬁnite numbers of direction d
that are forbidden: the anti-Stokes directions.
Assumption 2.7. — We suppose that:
(1) The series φ(1,ξ ) is solution of a diﬀerential equation N1φ(1,ξ ) =∑µ
i=0Ai(1,ξ )δiφ(1,ξ ) = 0 , where δ =ξ d
dξ , Ai(1,ξ ) ∈ C[ξ], and the
operator N1 is fuchsian at 0 and ∞. Moreover we suppose that the
exponents of N1φ(1,ξ ) = 0 at ∞ are non resonant.
TOME 59 (2009), F ASCICULE 1
362 Lucia DI VIZIO & Changgui ZHANG
(2) The series φ(q,ξ ) = Bqy(q,x ), q ∈ (0, 1), are solutions of a linear
q-diﬀerence operator Nqφ(q,ξ ) =∑µ
i=0Ai(q,ξ )δi
qφ(q,ξ ) = 0 , where
δq =ξdq, Ai(q,ξ ) ∈ C[ξ], and Nq is fuchsian at 0 and ∞(4) .
(3) The Newton-Ramis polygons of Nq coincide for any q ∈ (η, 1], and
the coeﬃcients Ai(q,ξ ) tends uniformly to Ai(1,ξ ) whenq → 1, on
any compact of P1
C. This implies in particular that for q suﬃciently
closed to 1, the exponents of Nq at ∞ are non resonant.
(4) For anyq suﬃciently closed to 1 there exists a constant gauge trans-
formation C(q) ∈Glµ(C) such that the constant term at ∞ of the
matrix
C(q)−1


0 1 0
... . . .
0 0 1
− A0(q,x)
Aµ(q,x) − A1(q,x)
Aµ(q,x) ... − Aµ−1(q,x)
Aµ(q,x)


C(q)
is in the Jordan normal form. We suppose that for q ∈ (η, 1] the
entries of the matrix C(q) are continuous functions of q and that
the form of the Jordan blocks is independent of q.
