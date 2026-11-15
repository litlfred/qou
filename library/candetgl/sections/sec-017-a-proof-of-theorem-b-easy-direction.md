---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-017-a-proof-of-theorem-b-easy-direction
section_title: "Proof of Theorem B, easy direction"
section_number: A
pages: 16-18
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
toc_source: inferred
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 27 sections: Front matter; INTRODUCTION; PRELIMINARIES"
---
Recall the statement:
Theorem B: The kernel of the Biot–Savart operator is precisely the space of gradient vector
ﬁelds which are orthogonal to the boundary of V.
The easy direction is to assume that V is a gradient vector ﬁeld which is orthogonal to the
boundary of V ~equivalently, that Ve HG%GG!, and then conclude that BS(V)50. We will do
that here, and will actually show that BS(V)50 throughout all of 3-space, rather than just in V.
We begin with the following lemma, which is stated without proof on p. 60 of Grifﬁths.46
Lemma 1: Let V be a smooth vector ﬁeld on the domain V, and let n denote the outward
pointing unit normal vector ﬁeld to ]V. Then,
E
V¹3V d~vol!52E
]VV3n d~area!.
Proof: Start with the Divergence Theorem,
E
V¹•Vd~vol!5E
]VV•n d~area!.
Then replace V by V3C, where C is any constant vector,
E
V¹•~V3C! d~vol!5E
]V~V3C!•n d~area!.
Writing ¹•(V 3C)5(¹3V)•C and moving C outside the integral, the left-hand side becomes
C•E
V¹3V d~vol!.
Writing (V 3C)•n52(V3n)•C and again moving C outside the integral, the right-hand side
becomes
2C•E
]VV3n d~area!.
Since the left- and right-hand sides are equal for all C, we must have
890
J. Math. Phys., Vol. 42, No. 2, February 2001
Cantarella, DeTurck, and Gluck
E
V¹3V d~vol!52E
]VV3n d~area!,
proving the lemma.
Suppose now that V5¹w is a gradient vector ﬁeld on V which is orthogonal to the boundary,
which means that w is constant on each component ]Vi of ]V. We must show that BS(V)50.
Begin with the formula for the Biot–Savart operator,
BS~V!~y!5~1/4p!E
VV~x!3~y2x!/uy2xu3 d~volx!.
~5.1!
Fix y, and let W5(y2x)/uy2xu3. Then,
BS~V!5~1/4p!E
V~¹w!3W d~vol!.
~5.2!
Now consider the vector ﬁeld wW on V and take its curl,
¹3~wW!5~¹w! 3W1w~¹3W!5~¹w!3W,
~5.3!
since ¹3W50. Thus
BS~V!5~1/4p!E
V¹3~wW! d~vol!.
~5.4!
We would like to use the preceding lemma to replace the right-hand side of this formula by
the expression
2~1/4p!E
]V~wW! 3n d~area!.
~5.5!
But the vector ﬁeld wW does not quite ﬁt the hypothesis of the lemma, since it has an isolated
singularity at the point y ~which we can assume is in the interior of V!. However, this singularity
is ‘‘radial;’’ if we surround it by a small sphere, the vector ﬁeld wW will be orthogonal to the
sphere, and so the integral *(wW)3n d~area! over this small sphere will be zero. It follows
immediately that the lemma can be applied in this case, in spite of the singularity.
We do so, and continue
BS~V!52~1/4p!E
]V~wW!3n d~area!
52~1/4p!(
i wiE
]Vi
W3n d~area!,
~5.6!
where wi is the constant value of w on ]Vi .
Now we claim that, for each i,
E
]Vi
W3n d~area! 50.
~5.7!
To see this, let Vi be the compact domain in 3-space bounded by ]Vi . Then, using the lemma
once again,
891
J. Math. Phys., Vol. 42, No. 2, February 2001
The Biot–Savart operator
E
]Vi
W3n d~area!56E
Vi
¹3W d~vol!
~5.8!
with the 1 or 2 sign chosen according as n points into or out of Vi . In any case, ¹3W50, so
the integral vanishes.
Thus BS(V)50 throughout 3-space.
