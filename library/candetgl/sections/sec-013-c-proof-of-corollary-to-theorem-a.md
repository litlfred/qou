---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-013-c-proof-of-corollary-to-theorem-a
section_title: "Proof of Corollary to Theorem A"
section_number: C
pages: 15-21
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
If V is divergence-free and tangent to the boundary of V, then we already know from item ~5!
in the list of Standard Information that the vector potential A(V) is divergence-free.
Recall, also from that list, items
~3!D A(V)52 V, and
~4!„ 3A(V)5BS(V) for all V
e VF(V).
Now take the second derivative formula,
„ 3~„ 3W!5„ ~„W!2DW ~4.10!
for any vector ﬁeld W, and rewrite it with A( V) in place of W,
FIG. 1. Components of the domain V and of its complement, V8.
FIG. 2. A typical ‘‘pill box’’ neighborhood of a point on ]V.
889J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
„ 3~„ 3A~V!! 5„ ~„"A~V!! 2DA~V!. ~4.11!
Using items ~3! and ~4! above, substitute BS( V) for „ 3A(V) on the left-hand side, and V for
2DA(V) on the right-hand side, to get
„ 3BS~V!5„ ~„"A~V!! 1V. ~4.12!
If A( V) is divergence-free, then we get
„ 3BS~V!5V inside V, ~4.13!
which by Theorem A implies that Ve K(V).
We conclude that A( V) is divergence-free if and only if Ve K(V), which is exactly the
assertion of the Corollary.
V. PROOF OF THEOREM B
A. Proof of Theorem B, easy direction
Recall the statement:
Theorem B: The kernel of the Biot –Savart operator is precisely the space of gradient vector
ﬁelds which are orthogonal to the boundary of V.
The easy direction is to assume that V is a gradient vector ﬁeld which is orthogonal to the
boundary of V~ equivalently, that Ve HG%GG!, and then conclude that BS( V)50. We will do
that here, and will actually show that BS( V)50 throughout all of 3-space, rather than just in V.
We begin with the following lemma, which is stated without proof on p. 60 of Grifﬁths. 46
Lemma 1: Let V be a smooth vector ﬁeld on the domain V, and let n denote the outward
pointing unit normal vector ﬁeld to ]V. Then,
E
V
„ 3V d~vol!52 E
]V
V3n d~area!.
Proof: Start with the Divergence Theorem,
E
V
„Vd~vol!5 E
]V
Vn d~area!.
Then replace V by V3C, where C is any constant vector,
E
V
„~V3C! d~vol!5 E
]V
~V3C!n d~area!.
Writing „(V 3C)5(„ 3V)C and moving C outside the integral, the left-hand side becomes
C E
V
„ 3V d~vol!.
Writing ( V 3C)n52 (V3n)C and again moving C outside the integral, the right-hand side
becomes
2C E
]V
V3n d~area!.
Since the left- and right-hand sides are equal for all C, we must have
890 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
E
V
„ 3V d~vol!52 E
]V
V3n d~area!,
proving the lemma.
Suppose now that V5„ w is a gradient vector ﬁeld on V which is orthogonal to the boundary,
which means that w is constant on each component ]Vi of ]V. We must show that BS( V)50.
Begin with the formula for the Biot–Savart operator,
BS~V!~y!5~1/4p! E
V
V~x!3~y2x!/uy2xu3 d~volx!. ~5.1!
Fix y, and let W5(y2x)/ uy2xu3. Then,
BS~V!5~1/4p! E
V
~„ w!3W d~vol!. ~5.2!
Now consider the vector ﬁeld wW on V and take its curl,
„ 3~wW!5~„ w! 3W1w~„ 3W!5~„ w!3W, ~5.3!
since „ 3W50. Thus
BS~V!5~1/4p! E
V
„ 3~wW! d~vol!. ~5.4!
We would like to use the preceding lemma to replace the right-hand side of this formula by
the expression
2~1/4p! E
]V
~wW! 3n d~area!. ~5.5!
But the vector ﬁeld wW does not quite ﬁt the hypothesis of the lemma, since it has an isolated
singularity at the point y ~which we can assume is in the interior of V!. However, this singularity
is ‘‘radial;’’ if we surround it by a small sphere, the vector ﬁeld wW will be orthogonal to the
sphere, and so the integral *(wW)3n d~area! over this small sphere will be zero. It follows
immediately that the lemma can be applied in this case, in spite of the singularity.
We do so, and continue
BS~V!52 ~1/4p! E
]V
~wW!3n d~area!
52 ~1/4p!(
i
wi E
]Vi
W3n d~area!, ~5.6!
where wi is the constant value of w on ]Vi .
Now we claim that, for each i,
E
]Vi
W3n d~area! 50. ~5.7!
To see this, let Vi be the compact domain in 3-space bounded by ]Vi . Then, using the lemma
once again,
891J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
E
]Vi
W3n d~area!56 E
Vi
„ 3W d~vol! ~5.8!
with the 1 or 2 sign chosen according as n points into or out of Vi . In any case, „ 3W50, so
the integral vanishes.
Thus BS( V)50 throughout 3-space.
B. Proof of Theorem B, harder direction
The heart of the argument is the following energy estimate.
Proposition 2: Let V be a compact domain with smooth boundary in 3-space, and V a smooth
divergence-free vector ﬁeld deﬁned in V. Let E s8 be the electrostatic ﬁeld due to the charge
distribution s(x)5V(x)n(x) along ]V. Then,
E
3-space
uEs8u2 d~vol!< E
V
uVu2 d~vol!.
That is, the energy of the electrostatic ﬁeld E s8 throughout all of 3-space is bounded from above
by the energy of the original ﬁeld V in V.
When V is not required to be divergence-free, the energy of the ﬁeld Es8 can be made
arbitrarily large, while keeping the energy of V itself as small as desired: make V(x)n(x) large
along ]V, and then quickly taper V off to zero throughout most of V.
Proof of Proposition 2: Given a divergence-free vector ﬁeld V, we can subtract from V its
orthogonal projection into the space K( V)5FK%HK of ﬂuid knots. This will leave the corre-
sponding electrostatic ﬁeld Es8 unchanged, while at worst decreasing the energy in V.
So in proving the proposition, there is no loss in generality in assuming that V is already
orthogonal to this subspace, and hence a gradient vector ﬁeld...as well as being divergence-free.
Thus we can write
V5„
w with Dw50. ~5.9!
Likewise,
Es8~y!52 „ yc~y!, ~5.10!
where
c~y!5~1/4p! E
xe]V
V~x!n~x!/ux2yu d~areax!. ~5.11!
Lemma 2: E
3-space
uEs8u2d~vol!5 E
]V
c]w /]nd~area!.
Proof of Lemma 2: This is a standard result in electrostatics; see Grifﬁths 46 pp. 94–95. For
convenience, we give the argument here.
Since the surface charge distribution s along ]V is given by
s~x!5V~x!n~x!5~„ w~x!!n~x!5~]w /]n!~x!, ~5.12!
we can rewrite the equation to be proved as
E
3-space
uEs8u2 d~vol!5 E
]V
cs d~area!. ~5.13!
892 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
This more clearly displays the relation of the integrand on the right-hand side to the ﬁeld Es8 ; the
function s is the surface charge distribution along ]V which gives rise to the ﬁeld Es8 , while the
function c is the electrostatic potential for Es8 , that is, Es852 „ c.
The proof is a little easier to express if we replace the surface charge distribution s by a
volume charge distribution r in a small neighborhood N(]V)o f ]V, and let Er852 „ c
be the resulting electrostatic ﬁeld, because in this situation we can write „Er5r.
With this understanding, we must show that
E
3-space
uEr8u2 d~vol!5 E
N~]V!
cr d~vol!. ~5.14!
To prove this, rewrite the integral on the right-hand side as
E
N~]V!
c~„Er8! d~vol!. ~5.15!
Next,
„~cEr8! 5~„ c!Er81c~„Er8!52 uEr8u21c~„Er8!. ~5.16!
Hence
E
N~]V!
cr d~vol!5 E
N~]V!
c~„Er8! d~vol!
5 E
N~]V!
„~cEr8! d~vol!1 E
N~]V!
uEr8u2 d~vol!. ~5.17!
If, in the integral on the left-hand side above, we replace the neighborhood N(]V) by any
larger domain, call it V*, the value of the integral will not change because r50 outside N(]V).
And the equation above will still hold if we replace N(]V)b y V* in each of the three integrals,
E
V*
cr d~vol!5 E
V*
„~cEr8! d~vol!1 E
V*
uEr8u2 d~vol!. ~5.18!
Apply the divergence theorem to the ﬁrst integral on the right-hand side, so that we now have
E
V*
cr d~vol!5 E
]V*
~cEr8!n d~area!1 E
V*
uEr8u2 d~vol!. ~5.19!
Visualize the domain V* growing larger and larger, with its boundary receding towards
inﬁnity. Then c decays like 1/ r, while Er8 decays like 1/ r2 and the area of ]V* grows like r2.
Thus the value of the ﬁrst integral on the right-hand side decays like 1/ r, and so goes to zero in
the limit. Hence
E
N~]V!
cr d~vol!5 E
3-space
uEr8u2 d~vol!, ~5.20!
the desired result for volume charge distributions.
If we compress the neighborhood N(]V) towards the surface ]V, the above result for volume
charge distributions will tend to the corresponding result for surface charge distributions,
E
]V
cs d~area!5 E
3-space
uEs8u2 d~vol!, ~5.21!
and the lemma is proved.
893J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
Completion of the proof of Proposition 2: Now we recall Green’s ﬁrst identity.
Let A5c„ w. Then
„A5„~c„ w!5„ c„ w1cDw5„ c„ w, ~5.22!
since Dw50.
Thus,
E
V
2Es8V d~vol!5 E
V
„ c„ w d~vol!5 E
V
„A d~vol!5 E
]V
An d~area!
5 E
]V
c„ wn d~area!5 E
]V
c]w /]n d~area!5 E
3-space
uEs8u2 d~vol!, ~5.23!
by the lemma.
Hence,
E
3-space
uEs8u2 d~vol!5 E
V
2Es8Vd~vol!
<S E
V
uEs8u2 d~vol!D
1/2
S E
V
uVu2 d~vol!D
1/2
<S E
3-space
uEs8u2 d~vol!D
1/2
S E
V
uVu2 d~vol!D
1/2
, ~5.24!
and therefore
E
3-space
uEs8u2 d~vol!< E
V
uVu2 d~vol!, ~5.25!
as claimed, ﬁnishing the proof of Proposition 2.
Completion of the proof of Theorem B: In the previous section, we showed that HG %GG, the
space of gradient vector ﬁelds which are orthogonal to the boundary of V, lies within the kernel
of the Biot–Savart operator BS:VF( V)!VF(V).
Now we must show that there is nothing else in the kernel.
We will do this by assuming that V is orthogonal to GG ~equivalently, is divergence-free! and
that BS( V)50, and will show that V must lie in HG.
First we observe that, under these assumptions, V must be a gradient vector ﬁeld.
To see this, consider the Maxwell equation in V,
„
y3BS~V!~y!5V~y!2~1/4p!„ y E
xe]V
V~x!n~x!/ux2yu d~areax!, ~5.26!
written in the form appropriate for any divergence-free vector ﬁeld V.
If V had a nonzero component in the subspace FK %HK of ﬂuid knots, then that component
would persist when we computed „ 3BS(V), since the Maxwell equation tells us that
„ 3BS(V) differs from V by a gradient vector ﬁeld. It follows that no such V could possibly be
in the kernel of BS.
So we can assume that V is a gradient vector ﬁeld, and write V5„ w. Since V is orthogonal
to GG, the function w must be harmonic. To show that V lies in HG, we must show that the
function w is constant on each component of ]V.
To start on this, note that the second term on the right-hand side in the Maxwell equation
above is the electrostatic ﬁeld Es8(y), and write that equation more succinctly as
894 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
„ 3BS~V!5V1Es8 . ~5.27!
Now if BS( V)50, then Es852 V in V.
It follows that Es8 must be identically zero outside V because, by Proposition 2, it simply has
no more energy.
This, in turn, implies that the electrostatic potential function c for the ﬁeld Es8 must be
constant on each component of ]V.
But the three equations,
Es8 52 „ c ~everywhere!, ~5.28!
V5„ w ~inside V!, ~5.29!
Es8 52 V ~inside V!, ~5.30!
tell us that
„ w 5„ c ~inside V!, ~5.31!
and hence that
w 5c 1 some constant ~5.32!
on each component of V, where the constant may depend on the component.
Thus w inherits from c the property of being constant on each component of ]V, and hence
V5„ w must lie in HG, the desired conclusion.
This completes the proof of Theorem B.
In fact, we have actually proved a bit more.
Theorem B
8: The kernel of „ 3BS , the composition of the curl and Biot –Savart operators, is
also the space of gradient vector ﬁelds which are orthogonal to the boundary of V.
This follows, with no further argument, because the only way we used the hypothesis that
BS(V)50 in this section was to set „ 3BS(V)50 on the left-hand side of the Maxwell equation
~5.27!.
