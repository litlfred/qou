---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-009-iii-standard-information-about-the-biotsavart-op
section_title: "STANDARD INFORMATION ABOUT THE BIOT–SAVART OPERATOR"
section_number: III
pages: 8-12
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
A. The basic facts
Given a smooth vector ﬁeld V on V, the vector potential A(V) for BS( V) is deﬁned by the
formula,
A~V!~y!5~1/4p! E
V
V~x!/uy2xu d~volx!. ~3.1!
Here is the classically known information about the Biot–Savart operator and its vector
potential. Note that some of the assertions below hold for any vector ﬁeld VeVF(V), while others
need the more restrictive assumption that V is divergence-free and tangent to the boundary of V,
in other words, that V lies in the subspace K ~V! of ﬂuid knots.
Standard Information: Let V be a compact domain in 3-space with smooth boundary ]V.
Let V be a smooth vector ﬁeld deﬁned on V. Then
(1) BS(V) and A(V) are well-deﬁned on all of 3-space, that is, the improper integrals deﬁning
them converge everywhere;
(2) BS(V) and A(V) are of class C ‘ on V, and on the closure V8 of R32V. BS( V) is continuous
on R 3, but its derivatives typically suffer jump discontinuities as one crosses ]V. A(V) is of
class C 1 on R3, but its second derivatives typically suffer jump discontinuities as one crosses
]V;
(3) DA(V)52 Vi n V and DA(V)50 in V8, where D is the vector Laplacian;
(4) „ 3A(V)5BS(V) on R 3;
(5) If V eK(V), then A(V) is divergence-free on R 3;
(6) „BS(V)50 in V and in V8;
(7) If V eK(V), then „ 3BS(V)5Vi n V and „ 3BS(V)50 in V8;
(8) If V eK(V), then *CBS(V)ds 50 for all closed curves C on ]V which bound in R 3 2V;
(9) In general,A (V) decays at ‘ like 1/r and BS(V) decays at ‘ like 1/r2; however, if V eK(V),
then A(V) decays at ‘ like 1/r2 and BS(V) decays at ‘ like 1/r3.
Proofs of most of these basic facts can be found throughout the physics literature ~see, for
example, Grifﬁths 46!, with the exception of item ~9!, which we prove in the Appendix. Item ~7!
contains the ﬁrst half of Theorem A; we will prove that immediately, since it affects the rest of the
paper.
B. Proof of 7

The argument to follow begins as in Grifﬁths, 46 pp. 215–217, but is then modiﬁed to suit our
purpose.
To prove ~7!, we assume that V is a ﬂuid knot, and must show that
882 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
„ y3BS~V!~y!5V~y!, when yeV,
50, when yeV8.
From now on, we will use the shorthand notation $V(y)i n V /0 i n V8%, or simply $V(y)/0%,
to express these two outcomes.
The above assertion will follow immediately from the next proposition, which will then serve
as a springboard to the rest of the paper.
Proposition 1:
„ y3BS~V!~y!5$V~y! in V /0 i n V8%1~1/4p!„ y E
V
~„ xV~x!! /uy2xu d~volx!
2~1/4p!„ y E
]V
V~x!n/uy2xu d~areax!.
If V is divergence-free, then the second term on the right-hand side vanishes; if V is tangent
to the boundary of V, then the third term on the right-hand side vanishes. If both hold, that is, if
V is a ﬂuid knot, then we get item ~7!.
We can view the statement of Proposition 1 as Maxwell’s equation,
„ 3B5J1]E/]t, ~3.2!
as follows.
Let V represent a current distribution throughout the domain V. At time t50, let the volume
charge density r throughout V and the surface charge density s along ]V both be zero. Then set
r52 ~„"V!t throughout V, ~3.3!
and
s5~V"n!t along ]V. ~3.4!
Equation ~3.3! for the volume charge density r is forced on us by the continuity equation,
„"V52 ]r /]t. ~3.5!
Likewise, Eq. ~3.4! for the surface charge density s is forced on us by a version of the continuity
equation appropriate to the boundary of our domain. The current V is simply carrying charge from
locations within V and on its boundary to other such locations. Thus the surface charge density
given by ~3.4! has a time rate of change equal to the ﬂux density of the current V through the
boundary ]V.
Now the volume charge throughout V gives rise to a time varying electric ﬁeld
Er~y,t!5F~1/4p!„ y E
V
~„ x"V~x!! /uy2xu d~volx!Gt, ~3.6!
and the surface charge along ]V gives rise to a time varying electric ﬁeld,
Es~y,t!5F2~1/4p!„ y E
]V
V~x!"n~x!/uy2xu d~areax!Gt, ~3.7!
both ﬁelds extending throughout 3-space.
The total electric ﬁeld
E~y,t!5Er~y,t!1Es~y,t! ~3.8!
883J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
has a time rate of change
]E/]t5]Er /]t1]Es /]t5Er81Es8 . ~3.9!
With this notation, the equation of Proposition 1 condenses to
„ 3BS~V!5$V /0 %1Er81Es8 , ~3.10!
which is just Maxwell’s Eq. ~3.2!. Proving Proposition 1 conﬁrms these interpretations.
Proof of Proposition 1: We must evaluate
„ y3BS~V!~y!5„ y3~1/4p! E
V
V~x!3~y2x!/uy2xu3 d~volx!
5~1/4p! E
V
„ y3$V~x!3~y2x!/u~y2x!u3% d~volx!. ~3.11!
We will need the following formula from vector calculus:
„ 3~A3B!5~B„ !A2~A„ !B1A~„B!2B~„A!. ~3.12!
Applying this formula to the integrand, we get
„ y3$V~x!3~y2x!/uy2xu3%
5~y2x!/uy2xu3„ y)V~x!2~V~x!„ y!~~ y2x!/uy2xu3

1V~x!„ y~~ y2x!/uy2xu3!2~~ y2x!/uy2xu3!~„ yV~x!! . ~3.13!
The ﬁrst and last terms on the right-hand side are zero, because they involve differentiation with
respect to y of V(x), which depends only on x. Thus,
„ y3$V~x!3~y2x!/uy2xu3%5V~x!„ y~~ y2x!/uy2xu3!2~V~x!„ y!~~ y2x!/uy2xu3!.
~3.14!
In the ﬁrst term on the right-hand side, the second factor
„ y~~ y2x!/uy2xu3! ~3.15!
is the divergence of the well known ‘‘inverse square central ﬁeld.’’ Using spherical coordinates
centered at x, this can be written as
„rˆ/r25~1/r2!~]/]r!~r2~1/r2!! 50, ~3.16!
away from the origin.
But the integral of „rˆ/r2 over any ball centered at the origin, when converted to a surface
integral via the divergence theorem, is clearly 4 p,
E
ball
„rˆ/r2 d~vol!5 E
sphere
~rˆ/r2!n d~area!54p. ~3.17!
Thus,
„rˆ/r254pd3~r!, ~3.18!
where d3(r) is the three-dimensional delta function; equivalently,
884 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
„ y"~~ y2x!/uy2xu3!54pd3~y2x!. ~3.19!
Hence,
~1/4p! E
V
V~x!„ y"~~ y2x!/uy2xu3! d~volx!5~1/4p! E
V
V~x!4pd3~y2x! d~volx!
5V~y! in V /0 i n V8. ~3.20!
Thus far, we have proved that
„ y3BS~V!~y!5$V~y! /0 %2~1/4p! E
V
~V~x!"„ y!~~ y2x!/uy2xu3! d~volx!. ~3.21!
Now we focus on the second term on the right-hand side and must show that
2~1/4p! E
V
~V~x!"„ y!~~ y2x!/uy2xu3! d~volx!
5~1/4p!„ y E
V
~„ x"V~x!! /uy2xu d~volx!
2~1/4p!„ y E
]V
V~x!"n/uy2xu d~areax!. ~3.22!
We begin by writing each of the three terms in ~3.22! in the form
6~1/4p!„ y E
V
~something! d~volx!. ~3.23!
Starting with the left-hand side of ~3.22!, we claim that its integrand can be rewritten as
~V~x!"„ y!~~ y2x!/uy2xu3!5„ y~V~x!"~y2x!/uy2xu3!. ~3.24!
To see this, we need the formula from vector calculus,
„ ~V"W!5V3~„ 3W!1W3~„ 3V!1~V"„ !W1~W"„ !V. ~3.25!
We use this with „ 5„ y , V5V(x), and W5(y2x)/ uy2xu3. Three of the four terms on the
right-hand side of ~3.25! will then be zero; the ﬁrst is zero because „ y3W50; the second is zero
because „ y3V(x)50; the fourth is zero because ( W"„ y)V(x)50. Thus „ y(V"W)5(V"„ y)W,
which is exactly our claim.
The ﬁrst term on the right-hand side of ~3.22! is already in the desired form.
The second term on the right-hand side of ~3.22! can be rewritten as
E
]V
V~x!"n/uy2xu d~areax!5 E
V
„ x"~V~x!/uy2xu! d~volx!, ~3.26!
thanks to the divergence theorem.
Now that all the terms in ~3.22! have been rewritten in the desired form, we claim that the
integrands on both sides are equal, namely, that
2V~x!"~y2x!/uy2xu35~„ x"V~x!! /uy2xu2„ x"~V~x!/uy2xu!. ~3.27!
This is an immediate consequence of the formula
885J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
„"~ fA !5~„ f !"A1 f~„"A!, ~3.28!
and the proof of Proposition 1 is complete.
