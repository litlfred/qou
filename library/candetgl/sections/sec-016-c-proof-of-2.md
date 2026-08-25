---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-016-c-proof-of-2
section_title: "Proof of 2"
section_number: C
pages: 25-29
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
To prove that the Biot–Savart operator is compact, we use two standard facts from functional
analysis. First is the fact that for any compact domain V,i f f(x) is continuous on R3, then the
integral operator
~Tf f !~y!5 E
V
f~y2x! f~x! d~volx! ~7.9!
deﬁnes a compact operator on L2(V); see Zimmer, 48 Theorem 3.1.5 on p. 53. It is stated there
only for operators on scalar-valued functions, but the extension to vector-valued ones, using the
deﬁnition given in Lemma 9.3, is trivial.
Second is the fact that the norm-limit of compact operators is compact; see Zimmer,
48 Lemma
3.1.3 on p. 52.
Now let
fN~x!5H
N2/4p if uxu<1/N
1/~4puxu2! if uxu>1/N. ~7.10!
Note that fN is a continuous function, and that
NV~f02fN!5maxy E
V
uw0~y2x! 2wN~y2x!u d~volx!
<~1/4p! E
uxu<1/N
~~ 1/uxu2!2N2! d~volx!
<~1/4p! E
uxu<1/N
~1/uxu2! d~volx!51/N. ~7.11!
By the ﬁrst functional analysis fact, TfN is a compact operator from VF(V)t o VF(V). By our
Lemma, we see that as TfN converges in norm to Tf0, the Biot–Savart operator, as N!‘ . Using
the second functional analysis fact, we conclude that BS: VF(V)!VF(V) is a compact operator.
This completes the proof of part ~2!.
D. Proof of 3

It is easy to see why the Biot–Savart operator is self-adjoint.
Suppose that V1 and V2 are smooth vector ﬁelds deﬁned on V. Then
899J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
^V1 ,BS~V2!&5 E
V
V1~y!BS~V2!~y! d~voly!
5 E
V
V1~y!F~1/4p! E
V
V2~x!3~y2x!/uy2xu3 d~volx!Gd~voly!
5~1/4p! E
V3V
V1~y!3V2~x!~y2x!/uy2xu3 d~volx! d~voly!
5~1/4p! E
V3V
V2~x!3V1~y!~x2y!/ux2yu3 d~voly! d~volx!
5^V2 ,BS~V1!&. ~7.12!
It is a straightforward exercise to check that these improper integrals are all convergent.
Thus BS:VF( V)!VF(V) is a self-adjoint operator, and therefore remains self-adjoint when
extended to the L2 completion VF(V)o fV F ~V!.
Theorem D is proved.
APPENDIX: THE DECAY RATE OF A V
 AND BSV
 AT INFINITY
In item ~9! in our list of standard information from Sec. III A, we asserted that in general,
A(V) decays at ‘ like 1/r and that BS( V) decays at ‘ like 1/r2. In the special case that VeK(V),
we asserted that A( V) decays at ‘ like 1/r2 and that BS( V) decays at ‘ like 1/r3.
We give the proofs here.
The deﬁning formula for the vector potential,
A
~V!~y!5~1/4p! E
V
V~x!/uy2xu d~volx!, ~A1!
expresses an inverse ﬁrst power law, with integration over a compact region V. It follows imme-
diately that A( V) decays at inﬁnity at least as fast as 1/ r.
When we say that A( V) decays at inﬁnity at least as fast as 1/r, we mean that the product
uA(V)( y)uu yu has a ﬁnite upper bound on R3, and likewise for corresponding expressions used
below.
The Biot–Savart formula,
BS~V!~y!5~1/4p! E
V
V~x!3~y2x!/uy2xu3 d~volx!, ~A2!
expresses an inverse square law, with integration over a compact region V. Again it follows
immediately that BS( V) decays at inﬁnity at least as fast as 1/ r2.
The proof of the faster decay rates when Ve K(V) will be divided into two lemmas.
Lemma 4: The following are equivalent:
(1) A(V) decays at inﬁnity at least as fast as 1/r2;
(2) BS(V) decays at inﬁnity at least as fast as 1/r3;
(3) *VVd(vol) 50.
Proof:
It is an easy exercise to check that conditions ~1! and ~2! each imply ~3!. For example, when
uyu is very large, we have
900 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
uyuA~V!~y!’ ~1/4p! E
V
V~x! d~volx!. ~A3!
If the integral of V is not zero, then uyu2uA(V)( y)u certainly blows up at ‘. Thus condition ~1!
implies condition ~3!, and likewise, ~2! implies ~3!.
Suppose now that condition ~3! holds. Then,
uyu2A~V!~y!5~1/4p! E
V
uyu2V~x!/uy2xu d~volx!
5~1/4p! E
V
uyu2V~x!/uy2xu d~volx!2~1/4p! E
V
uyuV~x! d~volx!
5~1/4p! E
V
$~uy2/uy2xu!2uyu%V~x! d~volx!, ~A4!
where the integral added on the right-hand side is zero thanks to condition ~3!.
Now,
$~uyu2/uy2xu!2uyu%5$uyu/uy2xu%$uyu2uy2xu%.
The ﬁrst factor on the right-hand side approaches 1 as y!‘ because V is bounded. The second
factor on the right-hand side is <uxu, and hence also bounded. Thus
$~uyu2/uy2xu!2uyu%
is bounded as y!‘ .
Since *VuV(x)ud(volx) is certainly bounded, it follows that uyu2uA(V)( y)u is bounded, and
hence that A( V) decays at ‘ at least as fast as 1/ r2. Thus condition ~3! implies condition ~1!,a s
claimed.
Again suppose that condition ~3! holds. Then
uyu3 BS~V!~y!5~1/4p! E
V
V~x!3~y2x!uyu3/uy2xu3 d~volx!
5~1/4p! E
V
V~x!3~y2x!uyu3/uy2xu3 d~volx!2~1/4p! E
V
V~x! 3y d~volx!
5~1/4p! E
V
V~x!3$~~ y2x!uyu3/uy2xu3!2y% d~volx!, ~A5!
where again the integral added on the right-hand side is zero because of condition ~3!. Continuing,
$~~ y2x!uyu3/uy2xu3!2y%5$y~uyu32uy2xu3!/uy2xu3%2$xuyu3/uy2xu3%.
Processing the ﬁrst term on the right-hand side,
$y~uyu32uy2xu3!/uy2xu3%5$y/uy2xu%$ uyu2uy2xu%$ ~uyu21uyuu y2xu1uy2xu2!/uy2xu2%.
The ﬁrst factor on the right-hand side of this last equation is bounded as y!‘ because V is
bounded. The second factor on the right-hand side is <uxu, and hence is also bounded. The third
factor on the right-hand side approaches the value 3 as y!‘ , and hence is also bounded. It
follows that
$y~uyu32uy2xu3!/uy2xu3%
901J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
is bounded as y!‘ .
Now the term
$xuyu3/uy2xu3%
is certainly bounded as y!‘ , and so we conclude that
$~~ y2x!uyu3/uy2xu3!2y%
is also bounded as y!‘ . From this it follows that
uyu3 BS~V!~y!
is bounded for all y, and hence that BS( V)( y) decays at ‘ at least as fast as 1/ r3. Thus condition
~3! implies condition ~2!.
This completes the proof of Lemma 4.
Lemma 5: *VV(x)d(volx)50 for all V in FK%HK%HG%GG, but this relation determines a
codimension-three subspace of CG.
Proof:
We begin with the proof that *VV(x)d(volx)50 for all VeFK%HK5K(V).
The argument will be coordinate-wise, so that we can deal with scalar-valued integrals instead
of vector-valued ones. So let us write the typical point of V as x5(x1 ,x2 ,x3), and then write
V(x)5(V1(x), V2(x), V3(x)).
Then
„~x1V!5~„ x1!V1x1~„V!5~„ x1!V5V1 , ~A6!
since V is divergence-free.
Hence,
E
V
V1~x! d~volx!5 E
V
„~x1V! d~volx!5 E
]V
x1Vn d~area!50, ~A7!
because V is tangent to ]V.
Of course the same argument holds for V2 and V3 , so we conclude that
E
V
V~x! d~volx!50, ~A8!
as claimed.
Now we prove that *VV(x) d(vol x)50 for all Ve HG%GG.
Write V5„ w with w constant on each component of ]V.
We claim that
E
V
V d~vol!5 E
V
„ w d~vol!5 E
]V
wn d~area!. ~A9!
We see this as follows:
Let C be any constant vector. Then,
„~wC!5~„ w!C1w~„C!5~„ w!C. ~A10!
Hence
902 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
S E
V
„ w d~vol!DC5 E
V
~„ w!C d~vol!
5 E
V
„~wC! d~vol!
5 E
]V
~wC!n d~area!
5S E
]V
wn d~area!DC. ~A11!
Since this is true for all constant vectors C, we must have
E
V
„ w d~vol!5 E
]V
wn d~area!, ~A12!
as claimed.
Now suppose that
]V5]V1ł ﬂł ]Vk ~A13!
is the decomposition of ]V into its connected components, and let wi denote the constant value of
the function w on the boundary component ]Vi . Then
E
V
V d~vol!5 E
V
„ w d~vol!5 E
]V
wn d~area!5(
i
wi E
]Vi
n d~area!50, ~A14!
because *n d(area) over any closed surface in 3-space is always zero.
This completes the proof that *VV(x) d(vol x)50 for all Ve HG%GG.
The observation that this relation determines a codimension-three subspace of CG follows
directly from the fact that the three constant vector ﬁelds xˆ, yˆ, and zˆ are curly gradients, com-
pleting the proof of Lemma 5.
Clearly, Lemmas 4 and 5 imply the faster decay rates of A( V) and BS( V) when Ve K(V),
completing our argument.
