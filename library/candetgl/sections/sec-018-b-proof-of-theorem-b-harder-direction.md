---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-018-b-proof-of-theorem-b-harder-direction
section_title: "Proof of Theorem B, harder direction"
section_number: B
pages: 18-21
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
toc_source: inferred
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 27 sections: Front matter; INTRODUCTION; PRELIMINARIES"
---
The heart of the argument is the following energy estimate.
Proposition 2: Let V be a compact domain with smooth boundary in 3-space, and V a smooth
divergence-free vector ﬁeld deﬁned in V. Let Es8 be the electrostatic ﬁeld due to the charge
distribution s(x)5V(x)•n(x) along ]V. Then,
E
3-spaceuEs8u2 d~vol!<E
VuVu2 d~vol!.
That is, the energy of the electrostatic ﬁeld Es8 throughout all of 3-space is bounded from above
by the energy of the original ﬁeld V in V.
When V is not required to be divergence-free, the energy of the ﬁeld Es8 can be made
arbitrarily large, while keeping the energy of V itself as small as desired: make V(x)•n(x) large
along ]V, and then quickly taper V off to zero throughout most of V.
Proof of Proposition 2: Given a divergence-free vector ﬁeld V, we can subtract from V its
orthogonal projection into the space K(V)5FK%HK of ﬂuid knots. This will leave the corre-
sponding electrostatic ﬁeld Es8 unchanged, while at worst decreasing the energy in V.
So in proving the proposition, there is no loss in generality in assuming that V is already
orthogonal to this subspace, and hence a gradient vector ﬁeld...as well as being divergence-free.
Thus we can write
V5¹w with Dw50.
~5.9!
Likewise,
Es8~y!52¹yc~y!,
~5.10!
where
c~y!5~1/4p!E
xe]VV~x!•n~x!/ux2yu d~areax!.
~5.11!
Lemma 2: E
3-spaceuEs8u2d~vol!5E
]Vc]w/]nd~area!.
Proof of Lemma 2: This is a standard result in electrostatics; see Grifﬁths46 pp. 94–95. For
convenience, we give the argument here.
Since the surface charge distribution s along ]V is given by
s~x!5V~x!•n~x!5~¹w~x!!•n~x!5~]w/]n!~x!,
~5.12!
we can rewrite the equation to be proved as
E
3-spaceuEs8u2 d~vol!5E
]Vcs d~area!.
~5.13!
892
J. Math. Phys., Vol. 42, No. 2, February 2001
Cantarella, DeTurck, and Gluck
This more clearly displays the relation of the integrand on the right-hand side to the ﬁeld Es8 ; the
function s is the surface charge distribution along ]V which gives rise to the ﬁeld Es8 , while the
function c is the electrostatic potential for Es8 , that is, Es852¹c.
The proof is a little easier to express if we replace the surface charge distribution s by a
volume charge distribution r in a small neighborhood N(]V) of ]V, and let Er852¹c
be the resulting electrostatic ﬁeld, because in this situation we can write ¹•Er5r.
With this understanding, we must show that
E
3-spaceuEr8u2 d~vol!5E
N~]V!cr d~vol!.
~5.14!
To prove this, rewrite the integral on the right-hand side as
E
N~]V!c~¹•Er8! d~vol!.
~5.15!
Next,
¹•~cEr8! 5~¹c!•Er81c~¹•Er8!52uEr8u21c~¹•Er8!.
~5.16!
Hence
E
N~]V!cr d~vol!5E
N~]V!c~¹•Er8! d~vol!
5E
N~]V!¹•~cEr8! d~vol!1E
N~]V!uEr8u2 d~vol!.
~5.17!
If, in the integral on the left-hand side above, we replace the neighborhood N(]V) by any
larger domain, call it V*, the value of the integral will not change because r50 outside N(]V).
And the equation above will still hold if we replace N(]V) by V* in each of the three integrals,
E
V*
cr d~vol!5E
V*
¹•~cEr8! d~vol!1E
V*uEr8u2 d~vol!.
~5.18!
Apply the divergence theorem to the ﬁrst integral on the right-hand side, so that we now have
E
V*
cr d~vol!5E
]V*
~cEr8!•n d~area!1E
V*uEr8u2 d~vol!.
~5.19!
Visualize the domain V* growing larger and larger, with its boundary receding towards
inﬁnity. Then c decays like 1/r, while Er8 decays like 1/r2 and the area of ]V* grows like r2.
Thus the value of the ﬁrst integral on the right-hand side decays like 1/r, and so goes to zero in
the limit. Hence
E
N~]V!cr d~vol!5E
3-spaceuEr8u2 d~vol!,
~5.20!
the desired result for volume charge distributions.
If we compress the neighborhood N(]V) towards the surface ]V, the above result for volume
charge distributions will tend to the corresponding result for surface charge distributions,
E
]Vcs d~area!5E
3-spaceuEs8u2 d~vol!,
~5.21!
and the lemma is proved.
893
J. Math. Phys., Vol. 42, No. 2, February 2001
The Biot–Savart operator
Completion of the proof of Proposition 2: Now we recall Green’s ﬁrst identity.
Let A5c¹w. Then
¹•A5¹•~c¹w!5¹c•¹w1cDw5¹c•¹w,
~5.22!
since Dw50.
Thus,
E
V2Es8•V d~vol!5E
V¹c•¹w d~vol!5E
V¹•A d~vol!5E
]VA•n d~area!
5E
]Vc¹w•n d~area!5E
]Vc]w/]n d~area!5E
3-spaceuEs8u2 d~vol!,
~5.23!
by the lemma.
Hence,
E
3-spaceuEs8u2 d~vol!5E
V2Es8•Vd~vol!
<SE
VuEs8u2 d~vol!D
1/2SE
VuVu2 d~vol!D
1/2
<SE
3-spaceuEs8u2 d~vol!D
1/2SE
VuVu2 d~vol!D
1/2
,
~5.24!
and therefore
E
3-spaceuEs8u2 d~vol!<E
VuVu2 d~vol!,
~5.25!
as claimed, ﬁnishing the proof of Proposition 2.
Completion of the proof of Theorem B: In the previous section, we showed that HG%GG, the
space of gradient vector ﬁelds which are orthogonal to the boundary of V, lies within the kernel
of the Biot–Savart operator BS:VF(V)→VF(V).
Now we must show that there is nothing else in the kernel.
We will do this by assuming that V is orthogonal to GG ~equivalently, is divergence-free! and
that BS(V)50, and will show that V must lie in HG.
First we observe that, under these assumptions, V must be a gradient vector ﬁeld.
To see this, consider the Maxwell equation in V,
¹y3BS~V!~y!5V~y!2~1/4p!¹yE
xe]VV~x!•n~x!/ux2yu d~areax!,
~5.26!
written in the form appropriate for any divergence-free vector ﬁeld V.
If V had a nonzero component in the subspace FK%HK of ﬂuid knots, then that component
would persist when we computed ¹3BS(V), since the Maxwell equation tells us that
¹3BS(V) differs from V by a gradient vector ﬁeld. It follows that no such V could possibly be
in the kernel of BS.
So we can assume that V is a gradient vector ﬁeld, and write V5¹w. Since V is orthogonal
to GG, the function w must be harmonic. To show that V lies in HG, we must show that the
function w is constant on each component of ]V.
To start on this, note that the second term on the right-hand side in the Maxwell equation
above is the electrostatic ﬁeld Es8(y), and write that equation more succinctly as
894
J. Math. Phys., Vol. 42, No. 2, February 2001
Cantarella, DeTurck, and Gluck
¹3BS~V!5V1Es8 .
~5.27!
Now if BS(V)50, then Es852V in V.
It follows that Es8 must be identically zero outside V because, by Proposition 2, it simply has
no more energy.
This, in turn, implies that the electrostatic potential function c for the ﬁeld Es8 must be
constant on each component of ]V.
But the three equations,
Es8 52¹c
~everywhere!,
~5.28!
V5¹w
~inside V!,
~5.29!
Es8 52V
~inside V!,
~5.30!
tell us that
¹w 5¹c
~inside V!,
~5.31!
and hence that
w 5c 1 some constant
~5.32!
on each component of V, where the constant may depend on the component.
Thus w inherits from c the property of being constant on each component of ]V, and hence
V5¹w must lie in HG, the desired conclusion.
This completes the proof of Theorem B.
In fact, we have actually proved a bit more.
Theorem B8: The kernel of ¹3BS, the composition of the curl and Biot–Savart operators, is
also the space of gradient vector ﬁelds which are orthogonal to the boundary of V.
This follows, with no further argument, because the only way we used the hypothesis that
BS(V)50 in this section was to set ¹3BS(V)50 on the left-hand side of the Maxwell equation
~5.27!.
