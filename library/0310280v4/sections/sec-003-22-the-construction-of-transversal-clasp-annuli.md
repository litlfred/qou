---
doc_id: 0310280v4
doc_title: "Stabilization in the braid groups II: Transversal simplicity of knots"
section_id: sec-003-22-the-construction-of-transversal-clasp-annuli
section_title: "The construction of transversal clasp annuli"
section_number: 2.2
pages: 8-13
source_pdf: 0310280v4.pdf
source_sha256: 1e146ee4ebc157f2
doc_brief: "Stabilization in the braid groups II: Transversal simplicity of knots — 9 sections: Introduction and description of re; The MTWS and transversal isotopies; Block-strand diagrams, templates a"
---
The goal in this subsection and the two that follow it is to state and prove a modiﬁed
version of Theorem 1 which holds in the transversal setting. The proof of the MTWS
in [6] began with the construction of a ‘clasp annulus’. We were given closed braids
X+ and X− which represent the same topological knot typeX . The goal was to ﬁnd
an isotopy from X+→ X− through closed braids, which would give us moves that
change the closed braid, but were non-increasing on braid index. It was proved in
Section 2.1 of [6], that the trace of the isotopy from X+ to X− could be assumed to be
a clasp annulus, that is a topological annulus PA∼= S1× [0, 1] with boundary and an
immersion e : PA−→ CA⊂R3 such that:
• The boundary of CA is X+− X−. The self-intersection set of CA is the
union of clasp arcs {γ1,··· ,γ k} ⊂ CAsuch that, for each γj, we have
e−1(γj) = γj
+∪γj
−⊂ PA. Also, γj
ϵ has an endpoint on e−1(Xϵ), ϵ =±. In
particular, there are no ribbon arcs or other more complicated self-intersections.
We refer to PAas the pre-image annulus (cf Section 2.1, [6]). The motion of pushing
X+ across CAto X− corresponds to an isotopy in R3. The clasp annulus CAcan be
positioned with respect to the braid structure ( H, A) so as to have a ‘braid foliation’
(see Section 2.3 below), that encodes a Markov tower for the pair (X+, X−). We called
this our basic construction.
In this subsection we adapt the same ideas, but now in the setting of the standard contact
structure and transversal isotopies in R3, and construct our transversal clasp annulus.
The construction here was motivated by, but does not depend on, that in [6].
We will need to make repeated use of two results which are well-known to workers
in low dimensional contact topology. In [2], Bennequin proved that a transversal link
in the standard contact structure of R3 could be modiﬁed by transversal isotopy to a
Geometry &Topology 10 (2006)
Stabilization in the braid groups II 1433
transversal link which is in braid position with respect to the z–axis. In fact, it is easy
to see that Bennequin’s original argument generalizes to the following statement.
Lemma 1 (The Bennequin Trick) Let Γ⊂ R3 be an oriented differentiable graph that
is transversal to the standard contact structureξ of R3. Let e⊂ Γ be an edge having
a local parameterization function f (t) : [0, 1]→ R3 where f (t) = (ρ(t),θ (t), z(t)). If
dθ
dt is not positive for all t then there exists a transversal isotopy of Γ which is the
identity everywhere except on a small neighborhood of e such that for a resulting
parameterization ˆf (t) = (ˆρ(t), ˆθ(t),ˆz(t)) we have dbθ
dt being everywhere positive.
The Bennequin trick is analogous to the Alexander trick, which was used in Section
2.1 of [6]. It essentially allows us to put a transversal graph into braid position, ie,
Γ∩ A =∅ and dθ
dt > 0 for every edge in Γ. The Bennequin trick will be used in
conjunction with a result of Eliashberg, which allows us to extend a transversal isotopy
of links to an isotopy of the ambient space R3, with its standard tight contact structure.
Lemma 2 (Eliashberg’s isotopy extension lemma [8]) Letϕt : X→ R3, t∈ [0, 1]
be an transversal isotopy of a transversal link in the standard contact structure ξ. Then
there exists a contact isotopy αt : (R3,ξ )→ (R3,ξ ), t∈ [0, 1], with α0 = id such that
αt◦ϕ0 =ϕt for t∈ [0, 1].
With the help of these two lemmas we will now develop the construction of Section 2.1
of [6] in the contact structure setting. Figure 5 may be helpful.
Given a pair ( TX+, TX−) with TX+, TX−∈TX and [ TX+]top, [TX−]top∈B (X ),
TA is an associated transversal clasp annulus if for PA∼= S1× [0, 1], there exists
an immersion e : PA−→ TA⊂ R3, with the oriented boundary of TA being
TX+− TX−, such that:
(a) The self-intersection set of the immersed annulus TA is the union of clasp arcs
{γ1,··· ,γ k}⊂ TA such that, for eachγj, we have e−1(γj) =γj
+∪γj
−. Also,
γj
ϵ has an endpoint on e−1(TXϵ), ϵ=±.
(b) The characteristic foliation of TA (which comes from integrating ξ in TA)
is trivial. That is, when viewing the pre-image of a leaf of the characteristic
foliation in PA, it is a single arc having one endpoint on e−1(TX+) and one
endpoint on e−1(TX−).
(c) The clasp arcs {γ1,··· ,γ k} are transversal arcs in the contact structure. In
particular, the arcsγi
+,γ i
−⊂ PAare transverse to the pre-image of the charac-
teristic foliation of TA. See Figure 5(b) for an example. Each clasp arc is also
in braid position, ie, transverse to each ﬁber Hθ of the braid structure H on R3.
Here we assume that the braid axis is the z axis.
Geometry &Topology 10 (2006)
1434 Joan S Birman and William W Menasco
(d) There exists a disjoint set of extension arcs of the clasp arcs (Figure 5(c)),
{g1
ϵ,··· , gk
ϵ, ϵ=±}⊂ PA, such that for each i = 1,..., k the union gi
ϵ∪γϵ
is an continuous edgepath in PA that is transverse to the trivial foliation of
PAand has its two endpoints on e−1(TXϵ). Each extension arc is also in braid
position.
(e) There exists a braid TX0⊂{TA\ (∪1≤i≤kγi∪∪ 1≤i≤k(gi
+∪ gi
−))} such that
[TX0]top∈B (X ) and [ TX0]top is a preferred longitude of both [TX+]top (in the
absence of [TX−]top) and [TX−]top (in the absence of [TX+]top).
(f) The graph
TX+∪ TX−∪ TX0∪ (∪1≤i≤kγi)∪ (∪1≤i≤ke(gi
+))∪ (∪1≤i≤ke(gi
−))
is in braid position with respect to the z–axis.
(g) The collection of edgepaths {(gi
+∪γi
+), (gi
−∪γi
−), i = 1,..., k}⊂ PA is
staggered. That is, there exists a set of leaves {s1,··· , sl}⊂ PA in the pre-
image of the characteristic foliation that are disjoint from the gi
±∪γi
± edgepaths,
1≤ i≤ k, such that each component of PA\ (∪1≤j≤lsj) is a disc containing at
most a single edgepath from the set{(gi
+∪γi
+), (gi
−∪γi
−), i = 1,..., k}.
We now use The Bennequin Trick (Lemma 1) and the Eliashberg Lemma (Lemma 2)
to establish that for any such pair (TX+, TX−) there always exists a transversal clasp
annulus.
Proposition 1 Given any pair of transversal closed braids (TX+, TX−) of the same
transversal knot type, there exists an associated transversal clasp annulus TA with
∂TA = TX+− TX−.
Proof We start by partitioning R3 along the plane z = 0, and denote the upper-half
space by R3
+ and the lower-half space by R3
−. We position TX− so that it is a transverse
braid in R3
−. Let TX′∈TX be an oriented closed braid that is a preferred longitude
of TX−. We can visualize TX′ being in R3
−, in braid position, and close to TX− with
TX′− TX− the boundary of an embedded annulusA′ in the lower half-space R3
− whose
characteristic foliation is trivial. In Figure 5(a) we see two fragments of A′. Note
thatA′ is oriented by the orientation on its boundary curves, so that we are looking at
its negative side. The knots TX′ and TX− will be geometrically linked, except in the
special case whenTX is the unknot. Let TX0⊂A′ be a core curve of the annulus.
Clearly TX0 is also a preferred longitude of TX− and TX′.
Now we think of a regular projection of the link TX−⊔ TX′ onto the plane z = 0.
Viewing this projection from the R3
+ side, at any crossing of TX− and TX′, whenever
Geometry &Topology 10 (2006)
Stabilization in the braid groups II 1435
TX
TX
TX
TX
TX
TX
TX0
TX0
TX0
TX0
TX0
TX0
TX−
TX−
TX−
TX−
TX−
TX−
crossing
(a) (b)
(c)
γj
sj
sj+1
sj′ +1
sj′γj
− gi
−
γj
+ gi
+
Figure 5: (a) Fragments of the embedded annulus A′ , trivially foliated, with ∂A′ =
TX ′−TX − . (b) The immersed annulus A′′ , with ∂A′′ =TX ′′−TX − . (c) The
preimage of A′′ . (Changing the label TX′′ to TX+ , sketch (c) can also be interpreted as
illustrating the preimage of TA.)
TX′ goes under TX− we modify it by an isotopy of TX′, changing the crossing. (We
do not change any of the crossings between TX′ and TX0.) We would like to do
this ‘unlinking’ transversally, and for that we use a method which was used by Nancy
Wrinkle in her thesis [16]. She notes:
⋆ Let Cρ be a cylinder of radiusρ in R3 whose axis is parallel to the z–axis and is
foliated by parallel Legendrian arcs of slope−ρ2. Then an isotopy of subarcs of
a transverse braid which lies on the surface of Cρ, and is slid vertically along the
Legendrian leaves, is a transverse isotopy.
So, let p = pi∈ R2 be a double point in the projected image of TX−∪ TX′ onto R2,
let p′
i be its preimage on TX′ and letαi be a neighborhood of p′
i on TX′. For each i the
points pi and p′
i share the sameρ coordinateρi, so they lie on the cylinder Cρi . Choose
a leaf of the characteristic foliation of Cρi that passes through pi and shift the point p′
i a
little bit until it also lies on the leaf. Then slide αi (keeping its endpoints ﬁxed) to an
arcβi, thereby changing the crossing in TX−∪ TX′. Let TX′′ be the transverse knot
that results from repeating this procedure at each undercrossing of TX′, replacing each
αi byβi.
Geometry &Topology 10 (2006)
1436 Joan S Birman and William W Menasco
Our unlinking isotopy will create clasp intersections inA′ as shown in Figure 5. We
can assume that the clasp arcs are in braid position. We call the resulting annulusA′′.
Its boundary will be TX′′− TX−. The characteristic foliation onA′′ is still trivial and
the image of extension arcs can be easily chosen in A′′. Moreover, a set of leaves
in the characteristic foliation can readily chosen to demonstrate that the edgepath of
clasps and their extension are staggered. (See Figure 5.) Notice that TX′′ and TX−
are geometrically unlinked. So we can modify TX′′ by transversal isotopy so that it is
contained in R3
+. This transversal isotopy will also correspond to a braid isotopy in
the complement of the z–axis, which is the braid axis. Finally, notice that for the pair
(X′′, TX−), the annulusA′′ is a transversal clasp annulus.
By Lemma 1 we know that closed oriented braids in R3 having the z–axis as their
braid axis are transversally isotopic to transversal closed braids. We consider a pair
(TX+, TX−) such that [ TX+]top∈B (X ), [ TX−]top∈B min(X ) and TX+, TX−∈TX .
The main result in [15] tells us that there is a transversal Markov tower for the pair of
transversal knots (TX+, TX−). That is, the transversal isotopy may be assumed to be
via a sequence of transverse closed braids, say:
(2) TX+ = TX1→ TX2→···→ TXr = TX−,
such that each TXj+1 is obtained from TXj by braid isotopy and a positive stabilization
or destabilization. Negative stabilizations and destabilizations do not occur.
Without loss of generality, we can assume that this isotopy is restricted to R3
+, ie, it is
the identity on R3
−. By Lemma 2 our transversal isotopy via the Markov tower extends
to a contact isotopy Ψ0 : (R3,ξ )→ (R3,ξ ), which ﬁxes R3
− and, thus TX−. This is
the starting point for our transversal clasp annulus. We initially let TA0 = Ψ0(A′′).
The boundary of TA0 will then be Ψ0(TX′′− TX−) = TX+− TX−. Note that since
Ψ0 is a contact isotopy the characteristic foliation of TA0 will be trivial, since the
foliation onA′′ was trivial. Moreover, the fact that the clasp arc and their extensions
are transverse and staggered in this trivial foliation is preserved by Ψ0. But, we
are not yet done. Although TX+ and TX− are in braid position, we cannot be sure
that TX0 remains in braid position under Ψ0, nor do we know the positioning of the
clasp arcs{γ1,··· ,γ k}, nor the image under the immersion of the extension arcs
{e(g1
+), e(g1
−),··· , e(gk
+), e(gk
−)}. However, if they are not in braid position, we can
apply the Bennequin trick (Lemma 1) to place them in braid position via a transversal
isotopy of the graph
TX+∪ TX−∪ TX0∪ (∪1≤i≤kγi)∪ (∪1≤i≤ke(gi
+))∪ (∪1≤i≤ke(gi
−))
which is the identity on TX+ and TX−. Appealing again to Lemma 2, we extend this
transversal isotopy to a contact isotopy Ψ1 : (R3,ξ )→ (R3,ξ ). Our needed transversal
Geometry &Topology 10 (2006)
Stabilization in the braid groups II 1437
annulus associated with the pair (TX+, TX−) will be TA = Ψ1(TA0) = Ψ1◦ Ψ0(A′′).
Again, the triviality of the characteristic foliation of A′′ is preserved under contact
isotopies. The fact that clasp arcs and their extensions are staggered remains true under
Ψ1. And, by construction TA satisﬁes the other conditions of a transversal clasp
annulus.
