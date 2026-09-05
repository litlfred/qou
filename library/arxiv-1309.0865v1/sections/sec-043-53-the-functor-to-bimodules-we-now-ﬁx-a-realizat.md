---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-043-53-the-functor-to-bimodules-we-now-ﬁx-a-realizat
section_title: "The functor to bimodules. We now ﬁx a realization where Demazure Surjec-"
section_number: 5.3
pages: 45-53
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
tivity holds. This ensures that ∆ s ∈R ⊗RsR is well-deﬁned (see section 3.3).
Deﬁnition 5.12. Let F be the k-linear monoidal functor from D to BSBim deﬁned as
follows. The object x is sent toBx. The images of the dots and trivalent vertices were
given in the introduction, and correspond to the four struct ure maps of a Frobenius
extension. In the introduction, one of the dots was sent to 1 ↦→1
2(αs ⊗ 1 + 1⊗αs), but
this should be 1 ↦→∆ s in general; whenever 1
2 exists, these two expressions are equal.
The bimodule image of the 2m-valent vertex is given explicitly in [Elib], though in a
convoluted and not particularly useful form.
Claim 5.13. This deﬁnition gives a well-deﬁned functor.
Proof. Previous papers have done most of the work for this claim. The polynomial
relations are obvious. Any other relation involving only a s ubset of colors can be
checked in the category DS′, whereS′ is the appropriate subset. Most of the relations
(including the isotopy relations) involve at most 2 colors, and the dihedral case was
checked in [Elib]. It remains to check the relations arising from rank 3 parabolics.
The case of A3 andA1 ×I2(m) form = 2, 3 was done already in [EK], where general
typeA was completed. The check for A1 ×I2(m) for other m <∞ exactly parallels
the proof for m = 2, 3 in [EK], and is essentially trivial.
46 BEN ELIAS AND GEORDIE WILLIAMSON
The case of B3 was checked by computer. The case of H3 can be checked by com-
puter, once the appropriate relation is found. The computer check used a localization
technique, which we will discuss in the section after next. □
5.4. Localization.
Deﬁnition 5.14. Let DQ denote the localization of D at Q, which is to say that we
allow boxes labelled by f ∈Q in the leftmost region, and require that they multiply
as in Q. Let FQ denote the functor DQ → BSBimQ which extends F under base
change.
Because of arguments akin to Lemma 3.20, this is the same as th e category which
allows boxes labelled byf ∈Q in any region, and allows f ∈Qs to slide across a line
coloreds.
The bimoduleBs is equipped with short exact sequences (3.4) and (3.5) which split
after localization to Q. Each short exact sequence “splits” the other, in the sense t hat
following one map from (3.4) and then one map from (3.5) gives an endomorphism
ofQ or of Qs which is multiplication by αs, and is therefore invertible. Two of the
maps we have already seen: they are the bottom and top boundar y dot. We seek a
calculus which mixes Soergel bimodules and standard bimodu les, and which con-
tains the other two maps. We might draw them as follows.
(5.18) f ⊗g ↦→f ⊗g =fs (g) ⊗ 1 1 ⊗ 1 ↦→δ ⊗ 1 − 1 ⊗δ
Deﬁnition 5.15. Let Kar(DQ) (temporarily abusive notation) denote the non-cyclic(!)
biadjoint monoidal category generated on top of DQ as follows. Add new objects Qs
for eachs ∈S, called reﬂection indices , whose identity morphisms we draw as dashed
lines of the same color as s. Thus an object of Kar (DQ) will have objects which are
sequences of normal indices and reﬂection indices. We typic ally disambiguate by
writing Bx,Q for a sequence of normal indices and Qx for a sequence of reﬂection
indices. Allow an additional kind of vertex of degree +1, a bivalent vertex with one
solids edge and one dashed s edge. We also allow dashed cups and caps. Finally ,
impose these new relations:
(5.19) =
(5.20) = −
(5.21) = =
SOERGEL CALCULUS 47
(5.22)
=
= − −
=
=
The reader can check that these relations are consistent wit h (5.18). Note that we
can deﬁne this category over R instead ofQ if desired, or even in the absence of De-
mazure Surjectivity . The remainder of this section will inv estigate Kar(DQ) further,
and prove the following theorem.
Theorem 5.16. Assume Demazure Surjectivity. This diagrammatic category is equivalent
to the Karoubi envelope of DQ. It is also equivalent to Dstd
Q , and to StdBimQ.
Unfortunately , Kar(DQ) is not cyclic! It is worse than that the rotation of one bi-
valent vertex is not the other. The bivalent vertex itself is not invariant under 360
degree twisting, being off by a sign. Any morphism with an eve n number of biva-
lent vertices will be cyclic (i.e. invariant under 360 degre e twists), but this still does
not imply that twisting by 180 degrees is equal to rotation by 180 degrees, because
bivalent vertices do not behave this way consistently . An example can be seen below
in (5.26). At least different representatives of the same is otopy class only differ by a
sign.
Remark 5.17. If one is familiar with the geometric underpinning of Soerge l bimod-
ules, then it should not be terribly off-putting that these m aps are not cyclic. One
expects cyclicity whenever one analyzes convolution betwe en perverse sheaves, be-
cause the procedure of taking the biadjoint of a sheaf is a fun ctor. Soergel bimodules
are the equivariant (derived) global sections of the semisi mple perverse sheaves on
the ﬂag variety , and taking global sections is a well-behave d functor on this semisim-
ple category , so that cyclicity happens to be preserved. How ever, taking global sec-
tions of non-semisimple sheaves tends to forget structure, and break the compatibil-
ity with the biadjunction functor. If one more appropriatel y models non-semisimple
perverse sheaves as complexes of semisimple sheaves, then t hese complexes will be
biadjoint in a cyclic way .
For instance, the standard bimodule Rs corresponds to two different, mutually bi-
adjoint perverse sheaves: the shriek and the star extension of the constant sheaf on P1
minus a point. These two different perverse sheaves have two different resolutions
in terms of semisimple perverse sheaves, and these descend t o (3.4) and (3.5). The
two complexes of Soergel bimodules which are quasi-isomorp hic toRs are biadjoint
in a cyclic way . The bimodule Rs itself is self-biadjoint. However, the compatibility
between these two biadjunction structures is broken.
We call an isotopy class of graphs as above mixed graphs. A mixed graph only rep-
resents a morphism in Kar(DQ) up to sign. A mixed graph has some solid edges and
some dashed edges. A mixed graph without any dashed edges is a Soergel graph or
48 BEN ELIAS AND GEORDIE WILLIAMSON
solid graph, and a mixed graph without any solid edges is a standard graph or dashed
graph (we will expand what counts as a dashed graph soon). (Isotopy classes of)
solid graphs and dashed graphs do unambiguously represent a morphism, without
any sign issues, because they have no bivalent vertices.
Now let us do some calculations. Using (5.19) and (5.20), one can easily produce
the following equalities after multiplication by αs. Since we’re working over Q, we
may divide by αs.
(5.23) = 0 = 0
Remark 5.18. If deﬁning this diagrammatic category over R instead ofQ, one should
add (5.23) to the list of relations.
The new bivalent vertices give rise to an idempotent
1
αs , which is comple-
mentary to the idempotent 1
αs
which already existed in DQ. Therefore, Bs,Q ∼=
Qs(1) ⊕Q(1). (We include the gradings for those who wish to use the homoge neous
fraction ﬁeld rather than the full fraction ﬁeld. Remember t hatQ ∼=Q(2) so that the
grading lives in /CI /2 /CI .) By convention we tend to include 1
αs
in the projection map,
rather than the inclusion map.
(5.24) = +
1
αs
1
αs
We can take a line and either “break” it or “dash” it. How very v iolent!
Claim 5.19. The reﬂection indices behave like standard modules with res pect to polynomials.
In other words, we have (4.1).
Proof. Place a polynomial f on the left side of the diagrams in (5.19). Use the poly-
nomial forcing rules to force f through the solid line in the middle. Any term where
the line breaks is zero by (5.23). The remaining term has s(f ) on the right hand side
instead. Dividing by αs gives the desired equality . □
Claim 5.20. The dashed cups and caps are redundant, being equal to the fol lowing maps.
The only relations necessary are (5.19) and (5.20).
(5.25) =
= 1
αs
1
αs
Proof. Equation (5.25) follows from (5.19) by adding a cap or cup and using (5.22).
Conversely , if we only use (5.25) as a deﬁnition of the dashed cups and caps, it is a
simple calculation to check (5.22) and (5.21). We give a samp le computation here.
SOERGEL CALCULUS 49
= −
0
=
−
= −=
1
αs1
αs
1
αs
1
αs
□
Fix a category C speciﬁed with generators and relations, an object M ∈ C , and
an idempotent e ∈ End(M). Let C(M,e ) denote the partial idempotent completion
which formally adds the image of e as a new object. Let us call this new object X.
It is easy to give a presentation of C(M,e ) by generators and relations. One adds a
new objectX and two new generators, a map ι : X →M and a mapπ : M →X. One
adds two new relations, which state that ιπ = e ∈ End(M) andπι = /BD ∈ End(X).
This presentation clearly gives a category C(M,e ) equipped with a fully faithful map
C → C (M,e ) which has all the desired properties. If the image of e is already an
object in C then X will be isomorphic to it. Similarly , if we wish to adjoin a set
of new summands {Xβ}, we need only add inclusions {ιβ} and projections {πβ}
with the relations above for each β. Similar statements can be made about monoidal
categories with monoidal presentations, graded categorie s etc.
Now it is clear that Kar (DQ) is the category obtained from DQ by adjoining the
complements of Q inBs,Q, for each s. The bivalent vertices are the new maps ι and
π, and the two relations on ι and π correspond to (5.19) and (5.20). To show that
Kar(DQ) is the Karoubi envelope of DQ, it is enough to show that Kar (DQ) is idem-
potent complete. Because each Bs,Q decomposes into Qs and the monoidal identity ,
it is clear that any object in DQ is isomorphic to a direct sum of sequences consisting
solely of reﬂection indices. Thus we need only show that any s equence consisting of
reﬂection indices represents an indecomposable object. Th is will be implied once we
show that this diagrammatic category is equivalent to Dstd
Q .
We do some more computations in preparation for the proof of t his equivalence.
Suppose that one takes a 2m-valent vertex and placesm consecutive bivalent vertices
on it (say , on bottom).
If one places a dot on top of this diagram, we get 0. This is because we can use
(5.7) to replace the 2m-valent vertex with the Jones-Wenzl morphism, and the Jones -
Wenzl morphism must have a dot on one of the bottom exits. This dot will then hit
the bivalent vertex, yielding zero by (5.23). However, each line on top decomposes
into two idempotents as in (5.24), and only the dashed idempo tent survives. Thus if
there are everm consecutive bivalent vertices on a 2m-valent vertex, we may as well
assume that all 2m are present.
If we place 2m bivalent vertices around a 2m-valent vertex, we get a morphism of
degree 2m. In order to get a morphism of degree 0 we should divide by a polynomial.
In other words, half the bivalent vertices should be inclusi ons and half projections,
50 BEN ELIAS AND GEORDIE WILLIAMSON
and one half should be paired with 1
αs
. So consider the following diagram with m
strands.
This is a reduced expression for w0, the longest element of Ws,t. Using (5.19), we
get a sequence of vertical dashed lines, with αs to the left of each line colored s. If we
pull all these polynomials to the far left region using (4.1) , we get ρs,t, the product of
allm positive roots corresponding to reﬂections in ⟨s,t ⟩ (for a deﬁnition of positive
roots in a dihedral group, see [Elib]). Note that w0 sends the set of positive roots to
the set of negative roots, so that w0(ρ) = ( −1)mρ.
A simple calculation using (5.22) shows that
(5.26) = (−1)m
Therefore
(5.27) =
1
ρ 1
ρ
Thus the RHS of (5.27) is a degree 0 map which is cyclic, and is a perfect candidate
for the 2m-valent vertex in Dstd
Q .
Deﬁnition 5.21. Let Std denote the functor from Dstd
Q to Kar (DQ) deﬁned herein,
called the standardization functor . On objects, it sends a sequence of indices to the
corresponding sequence of reﬂection indices. On morphisms , it sends caps and cups
to dashed caps and cups, and it sends the 2m-valent vertex to the morphism in (5.27).
We draw the image of the 2m-valent vertex in Dstd
Q as a dashed 2m-valent vertex.
From the above, it should be easy to check that
(5.28) =
Proposition 5.22. The functor Std is well-deﬁned, and is an equivalence of categories.
SOERGEL CALCULUS 51
This proposition implies all of Theorem 5.16 except for the c onnection to StdBim.
We have already showed that Std is essentially surjective, because Kar (DQ) is addi-
tively generated by reﬂection indices. We need to check that Std is well-deﬁned, full
and faithful.
Proof that Std is well-deﬁned. We have already checked the isotopy relations inStdBim,
because of (5.21) and (5.27). We have also checked polynomia l-sliding. Relation (4.3)
follows as below (we used δ = αs
2 , but any δ will work).
= =
(
+
(
=
(
+
(
−
= − = − =
1
2
1
21
αs
1
αs
1
α2s
1
α2s
1
α2s
1
α2s
The proof of (4.2) is easy , and we leave it as an exercise.
The proofs of (4.4) and the three color relations all follow f rom the same method.
Take relations (5.16) and the three color relations in D, and place a bivalent ver-
tex below every strand on bottom. Doing so will kill any diagr am with a bottom
boundary dot, including all the non-identity diagrams in th e Jones-Wenzl projec-
tor in (5.16), and all the lower terms in the H3 relation (5.12). We ignore all those
terms. For any diagram composed entirely out of 2m-valent vertices for various m,
we can use (5.28) to pull the “dashed-ness” from bottom to top , until the entire di-
agram is dashed except with bivalent vertices at the top. The result is precisely the
corresponding relation in Dstd, with bivalent vertices on top. Bivalent vertices are
invertible, so this checks the relation. □
Now we can apply any relations in Dstd to dashed diagrams in Kar (DQ).
We see that surrounding a 2m-valent vertex with bivalent vertices yields (up to
polynomial) the dashed version of the map. However, there ca n be no dashed ver-
sion of the dot or the trivalent vertex, since there are no map s between standard
bimodules when they do not express the same element of W . Unsurprisingly , sur-
rounding a dot or a trivalent vertex with bivalent vertices i s zero. For the dot this is
(5.23). It is not too hard to show that
=
Therefore
52 BEN ELIAS AND GEORDIE WILLIAMSON
(5.29) = = = 0
Lemma 5.23. Every morphism in Kar (DQ) is a linear combination of graphs for which:
• The only dots appearing are boundary dots.
• There is a single polynomial in the leftmost region, and no ot her connected compo-
nents without boundary.
• There are no trivalent vertices.
• There are no solid 2m-valent vertices, only dashed 2m-valent vertices.
Proof. Consider a diagram in Kar(DQ). One can use (5.24) to either break or dash any
edge. The reduction goes as follows:
(1) Counting regions separated by a dashed line as a single area, we can assume
there is a single area. This can be done by taking a solid line w hich separates
two areas and either breaking it or dashing it.
(2) We can assume that every 2m-valent vertex appears only in its dashed ver-
sion. If there are any solid 2m-valent vertices, break or dash one of its edges.
If broken, one can use (5.7) to remove the 2m-valent vertex. If dashed, now
break or dash the next edge. Eventually we can assume every ed ge is dashed,
any thus can replace the 2m-valent vertex with its dashed version (up to mul-
tiplication by a polynomial in some region).
(3) We can assume there are no trivalent vertices. If there ar e any trivalent ver-
tices, break or dash one of its edges. If broken, one can use (5 .4) to remove the
trivalent vertex. If dashed, now break or dash the next edge. One of the three
edges must be broken, or the result is zero by (5.29).
(4) We can assume there are no dots except for boundary dots. A ny dot not
connected to the boundary must be connected to another dot (and so becomes
a box), or to bivalent vertex (and so becomes zero).
(5) Any remaining solid line can only run into the boundary or into a bivalent
vertex (it can not form a circle, for this would create a secon d area). Any
solid line meeting two bivalent vertices can be removed by (5 .19), yielding a
continuous dashed line (up to a polynomial). Thus any connec ted component
without boundary is either a box or is a purely dashed diagram .
(6) We can assume all boxes are in the leftmost region. This is because there is a
single area, and we can slide polynomials through dashed lin es using (4.1).
Thus the polynomials merge into a single box.
(7) Any remaining closed component can be removed. This uses the fact that
closed diagrams in Dstd reduce to the empty diagram.
□
Corollary 5.24. Std is full.
SOERGEL CALCULUS 53
Proof. Apply the reduction of the lemma to a map between reﬂection in dices. There
can be no boundary dots. A solid edge can not connect to anythi ng except a bivalent
vertex any more. Thus every solid edge can be removed with (5. 19) (at the cost of
adding a polynomial). Any map with only dashed edges is clear ly in the image of
Std. □
We can deﬁne a functor Kar (DQ) →StdBim extending F . This functor acts on bi-
valent vertices as in (5.18). Clearly this functor intertwi nes Std and Fstd. Since Fstd is
an equivalence, this would imply that Std is faithful, and is therefore an equivalence.
This concludes the proof of Proposition 5.22 and Theorem 5.1 6
In the next section we construct a quasi-inverse for Std, giving a proof that Std is
faithful without needing the functor F to bimodules.
