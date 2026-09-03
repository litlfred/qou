---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-014-34-v-olume-and-the-chernsimons-invariant-now-we
section_title: "V olume and the Chern–Simons invariant. Now we know that u de-"
section_number: 3.4
pages: 20-23
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
doc_brief: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS — In this paper we give an introduction to the volume conjectur e and its generalizations."
---
ﬁnes a representation (with some ambiguity) of π 1(S3 \ E) at SL(2; C). In this
subsection we calculate the corresponding volume and Chern –Simons invariant.
(i) When u is close to 0.
In this case the parameter u deﬁnes an (incomplete) hyperbolic structure on
S3 \ E, and as described in Subsection 1.3, if u and v(u) satisfy p u + q v(u) =
2π √ − 1 with coprime integers p and q, then we can construct a closed three-
manifold Eu. In [50] we proved that Conjecture 2.3 holds in this case. Not e that
since H(0) = Vol( E)√ − 1, which is the original volume conjecture 2.1 for the
ﬁgure-eight knot, ˜f (u) deﬁned by H(u) coincides with the f function appearing
in (1.2) and (1.3).
Example 3.5. As an example let us consider the case where u is real, and study
H(u) and the corresponding representation.
Remark 3.6. In this example we do not mind whether the sequence
log
(
JN
(
E; exp
(
(u + 2π
√
− 1)/N
)))
/N
really converges or not.
First we assume that − arccosh(3/ 2) < u < arccosh(3/ 2). Note that arccosh(3 / 2)
= 0. 9624236501 . . . .
Since |x − √ − 1
√
1 − x2|= 1 when |x|⩽ 1 and 1 / 2 ⩽ cosh(u) − 1/ 2 < 1 for
real u with |u|⩽ arccosh(3/ 2), we see that ϕ (u) is purely imaginary. Then from
(3.10) we have
H(u) = Li 2(e−ϕ (u)−u) − Li2(e−ϕ (u)−u) + uϕ (u)
and so H(u) is purely imaginary, where z is the complex conjugate of z. We can
also see that v(u) is also purely imaginary from (3.12).
Let us consider the corresponding volume function:
Vol(Eu) := Im H(u) − π Re(u) − 1
2 Re(u) Im
(
v(u)
)
.
See Figures 7 and 8 for graphs of Im H(u) and Vol( Eu) respectively. Note
that
Vol(E0) = Im H(0) = 2 . 0298832128 . . . ,
which is the volume of S3 \ E with the complete hyperbolic structure. Note also
that
Im H(arccosh(3/ 2)) = 2 π arccosh(3/ 2) = 6 . 0470861377 . . .
and
Vol
(
E± arccosh(3/ 2)
)
= 0
since ϕ (arccosh(3/ 2)) = 2 π √ − 1.
If we choose uq so that v(uq) = 2 π √ − 1/q for a positive integer q, then Euq is
the cone-manifold with cone-angle 2 π/q whose underlying manifold is obtained
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 239
Figure 7. Graph of Im H(u) for − arccosh(3/ 2) ⩽ u ⩽ arccosh(3/ 2)
Figure 8. Graph of the volume function Vol( Eu) for
− arccosh(3/ 2) ⩽ u ⩽ arccosh(3/ 2)
from the 0-surgery along the ﬁgure-eight knot (the singular set is the core of
the surgery). This is because it corresponds to the generali zed Dehn surgery of
coeﬃcient (0 , q ), since 0 × uq + q × v(uq) = 2 π √ − 1 [54, Chapter 4]. Note that
even though q is not an integer, Vol( Euq ) is still the volume of the corresponding
incomplete hyperbolic manifold.
See [20] for geometric structures of the Euq . In that paper, H. Hilden, M. Lozano,
and J.M. Montesinos-Amilibia also observed that when q = 1, that is, when
u = ± arccosh(3/ 2), the corresponding manifold is just the 0-surgery and has a
Sol-geometry. They also calculated Vol( Euq ) with q = 2, 3, . . . , 81 [20, p. 559].
Next we consider the case where u is real and |u|> arccosh(3/ 2). In this case
Im v(u) = 2 π √ − 1 since Im ϕ (u) = 2 π √ − 1.
240 HITOSHI MURAKAMI
If we put p = − Re v(u)/u , q = 1, s = 0 and r = − 1, then p u+q v(u) = 2 π √ − 1
and ps − qr = 1. (For a while we do not mind whether p is an integer or not. See
Remark 3.7 below.) Assuming that this would give a genuine ma nifold, we have
from (1.4) and (2.3)
Vol(Eu)+
√
− 1 CS(Mu)−
{
Vol(E) +
√
− 1 CS(E)
}
≡ H(u)√ − 1 − H(0)√ − 1 − 3
2 πu − uv(u)
4√ − 1
(mod π 2√
− 1Z).
Since H(0) = √ − 1 Vol(E) and CS( E) = 0 from the amphicheirality of E (that
is, the ﬁgure-eight knot is equivalent to its mirror image), we have
Vol(Eu) = Im H(u) − 2πu = 0
and
CS(Eu) ≡ − Re H(u) + 1
4 u Re v(u) (mod π 2Z),
since Im ϕ (u) = 2 π if |u|> arccosh(3/ 2).
Figure 9. Graph of the CS( Mu)/ (2π 2) for ⩽ arccosh(3/ 2) < u < 10
Remark 3.7. Here we show some calculations by using Mathematica and Snap Pea.
See Figure 9.
If eu satisﬁes the equation
x6 − 4x4 − 7x3 − 4x2 + 1 = 0
(u = 0 . 9839865622 . . . ), then u + v(u) = 2 π √ − 1 and so this corresponds to the
(1, 1)-surgery along E. Moreover we have CS(Eu)
2π √ − 1 = 0 . 01190476190 . . . = 1
84 ,
which coincides with the calculation by SnapPea. Note that Eu in this case is
the Brieskorn homology sphere Σ(2 , 3, 7), which is a Seifert ﬁbered space over the
sphere with three singular ﬁbers. (See for example [31, Prob lem 1.77].)
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 241
If u = log
(
1 +
√
5
2 +
√ √
5 + 1
2
)
= 1. 061275062 . . . , then 2 u + v(u) = 2 π √ − 1
and so this corresponds to the (2 , 1)-surgery along E. We also have CS(Eu)
2π 2 =
0. 025 = 1
40 , which coincides with the calculation by SnapPea. In this ca se Eu is
the Brieskorn homology sphere Σ(2 , 4, 5).
If u = log
(
1
2 +
√
2 + 1
2
√
5 + 4
√
2
)
= 1. 265948638 . . . , then 3u+v(u) = 2 π √ − 1,
and so this corresponds to the (3 , 1)-surgery along E. We also have CS(Eu)
2π 2 =
0. 041666666667 . . . = 1
24, which coincides with the calculation by SnapPea. In
this case Eu is Σ(3 , 3, 4).
Note that from Figure 9 it seems that
lim
u→∞
CS(Eu)
2π 2 = 1
12 ,
which would be the Chern–Simons invariant of E∞ that corresponds to the (4 , 1)-
surgery of the ﬁgure-eight knot.
(ii) When θ is real and |θ |> arccosh(3/ 2).
In this case ˜H(u − 2π √ − 1) is real and so Im v(u) = − 2π . Therefore formulas
for Vol(Eu) and CS( Eu) similar to the case where u is real and |u|> arccosh(3/ 2)
hold.
Remark 3.8. Note that
Re H(u) = Re ˜H(u − 2π
√
− 1)
but Im H(u) and Im ˜H(u − 2π √ − 1) are diﬀerent. In fact Im ˜H(u − 2π √ − 1) = 0
but Im H(u) = 2 πu for − arccosh(3/ 2) < u < arccosh(3/ 2). This means that if
|Re u|/greaterorequalslantarccosh(3/ 2), then the cases where Im u = 0 and Im u = − 2π √ − 1 give
diﬀerent limits but the same Vol and CS. As observed in Exampl e 3.5, this would
correspond to cone-manifold whose underlying manifold is t he 0-surgery along E.
