---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-011-iv-proof-of-theorem-a
section_title: "PROOF OF THEOREM A"
section_number: IV
pages: 13-15
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
Recall the statement:
Theorem A: The equation „ 3BS (V)5V holds in V if and only if V is divergence-free and
tangent to the boundary of V.
The condition that V be divergence-free and tangent to the boundary of V can also be written
as VeK(V)5FK%HK, the subspace of ﬂuid knots. For the same effort, we will also get
Addendum to Theorem A: The equation „ 3BS (V)50 holds in the closure V8 of R32V if
and only if V eFK % HK % HG % GG .
This condition on V is equivalent to V being orthogonal to the subspace CG of curly gradients
in VF~V!. Then we will prove.
Corollary to Theorem A: The vector potential A (V) is divergence-free if and only if V is
divergence-free and tangent to the boundary of V.
A. Proof of Theorem A
Half of Theorem A has already appeared as item ~7! in our list of Standard Information, and
was proved in Sec. III B, namely, if VeK(V)5FK%HK, then „ 3BS(V)5V in V.
By contrast, if Ve HG%GG, then it would be impossible for „ 3BS(V) to equal V in V
unless V50, since we know from the Hodge Decomposition Theorem that the image of curl is
FK%HK%CG.
It remains to show that if V is in CG, then „ 3BS(V) can never equal V in V unless V50.
The proof will be based on the Maxwell equation,
„ y3BS~V!~y!5$V~y! in V /0 i n V8%2~1/4p!„ y E
xe]V
V~x!n~x!/ux2yu d~areax!.
~4.1!
Following our discussion in Sec. III B, we can write the second term on the right-hand side of
this equation as
Es8~y!52 ~1/4p!„ y E
xe]V
V~x!n~x!/ux2yu d~areax!. ~4.2!
Although Es8 is the time rate of change of the electrostatic ﬁeld Es , it is also the same as the
electrostatic ﬁeld due to a charge density s(x)5V(x)n(x) along ]V, and so we can treat it as
though it were an electrostatic ﬁeld.
We write
Es8~y!52 „ yc~y!, ~4.3!
887J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
where
c~y!5~1/4p! E
xe]V
V~x!n~x!/ux2yu d~areax!. ~4.4!
Although we have in general been writing our gradient ﬁelds with a plus sign, as in the equation
V5„ w, we write electrostatic ﬁelds with a minus sign, Es852 „ c, to follow standard conven-
tion.
While the electrostatic potential function c for a surface charge distribution s is continuous,
the electrostatic ﬁeld Es8 will in general have a jump discontinuity as we cross the surface.
Nevertheless, we have „Es850i n V and „Es850i n V8.
We claim that if V is a nonzero vector ﬁeld in CG, then Es8 cannot be identically zero in V.
Recall the deﬁnition of the subspace CG of curly gradients. A smooth vector ﬁeld V deﬁned
on V is in CG if and only if V5„ w, where w is a harmonic function on V, and where the ﬂux of
V through each component of ]V is zero. That is, for each component ]Vi of ]V, we have
E
]Vi
V~x!n~x! d~areax!5 E
]Vi
s~x! d~areax!50. ~4.5!
In other words, the total charge on each component of ]V is zero.
Suppose now that Es850i n V. We must show that V50.
First we will show that Es850i n V8, the closure of R32V.
The hypothesis that Es850 inside V tells us that c must be constant on each component ]Vi
of ]V85]V.
Now we consider the ﬁeld cEs8 in V8, and compute its divergence ~a standard trick in
electrostatics!,
„~cEs8!5~„ c!Es81c~„Es8!52 Es8Es852 uEs8u2. ~4.6!
Hence,
E
V8
uEs8u2 d~vol!52 E
V8
„~cEs8! d~vol!52 E
]V8
cEs8n8d~area!, ~4.7!
where n8 is the unit outward-pointing normal vector to V8, so that n852 n.
Using the divergence theorem in V8 requires a comment, since one of its components is
unbounded. That unbounded component should really be approximated by a bounded domain with
one boundary component out near inﬁnity. The ﬂux of cEs8 through this boundary component
goes to zero as it recedes towards inﬁnity, because the area grows like r2, while the ﬁeld Es8
decays like 1/ r2 and the potential c decays like 1/ r.
With that said, we continue,
E
V8
uEs8u2 d~vol!52 E
]V8
cEs8n8d~area!52 (
i
ci E
]Vi
Es8n8d~area!, ~4.8!
since c is constant, say with value ci , on each component ]Vi of the boundary.
Now, by Gauss’ Law,
E
]Vi
Es8n8d~area!56 total charge ‘‘inside’’ ]Vi
56 (
some j
E
]V j
s~x! d~areax!50, ~4.9!
888 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
because the total charge on each component ]Vj of ]V is zero ~see Fig. 1 !.
Thus, *V8uEs8u2d~vol!50, and hence Es8[0i n V8.
Now we have Es8[0i n V and also in V8. Then Gauss’s Law, applied to the typical ‘‘pill
box’’ neighborhood of a point on ]V, implies that the surface charge distribution s is identically
zero ~see Fig. 2 !.
Since s(x)5V(x)n(x), this imples that V is tangent to the boundary of V, and hence
VPK(V). But K( V)øCG50, so V50.
This completes the proof of Theorem A.
B. Proof of Addendum to Theorem A
We know that if V lies in K( V)5FK%HK, then „ 3BS(V)50i n V8, according to item ~7!
in our list of Standard Information from Sec. III A.
