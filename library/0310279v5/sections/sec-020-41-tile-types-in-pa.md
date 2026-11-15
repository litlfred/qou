---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-020-41-tile-types-in-pa
section_title: "Tile types in PA"
section_number: 4.1
pages: 39-45
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
Tile types in PA
Our work begins with the two closed braid representatives X+ and X−of X . Our
basic construction in Section 2 gave us the immersed annulus CA = A+ ∪A−and the
clasp arcs. We begin by studying the braid foliations of the two annuli. The key point
which will allow us to apply the machinery of Section 3 is that each is embedded. The
really new feature is the presence of the clasp arcs. We ﬁrst make the clasp arc as nice
as possible (we change them to ‘tabs’). After that we will remove ‘short clasp arcs’,
ie ones which do not pass through any singular leaves. Then we will create ‘normal
neighborhoods’ about the doubly modiﬁed clasp arcs, which will isolate them from the
rest of CA. Our device for isolating them is to introduce lots of inessential b–arcs,
which will give us the freedom we need to modify the clasp arcs when we need to do so.
In this section we are interested in the foliation of A+ and A−which are induced by
intersections of these annuli with the half-planes of our braid structure. The closed
braids X+, X0, X−are all oriented so that they point in the direction of increasing θ at
each point of intersection with an Hθ. We choose an orientation on the annulus A+ in
such a way that it induces the given orientation on its boundary component X+. Notice
that this means that the orientation on X0 does not agree with that induced by the chosen
orientation on A+. Similarly, we choose an orientation on the annulus A−in such a
way that it induces the given orientation on its boundary component X0, which implies
that the orientation on X−does not agree with that induced by the chosen orientation
on A−.
As in the situation of Seifert surfaces, the foliation may be assumed to be radial in a
neighborhood of each point of A∩A± (see Figure 15(a)) and transverse to the boundary
in a neighborhood of ∂A± (Figure 15(b)). The braid axis A pierces A± from either
Geometry & Topology 10 (2006)
452
Joan S Birman and William W Menasco
the negative or the positive side at each pierce point, and we have indicated this by
attaching positive or negative signs to the pierce points on A±. As before, leaves in the
foliation are singular if they contain a singularity of the foliation, otherwise they are
non-singular. The singularities may be assumed to be ﬁnite in number and to occur on
distinct ﬁbers of H.
We now show that, as in the situation of Seifert surfaces, we may assume that there
are no leaves in the foliation of CA = A+ ∪A−which are simple closed curves. See
Figure 28. There are new issues to settle. The ﬁrst question we ask is whether a simple
closed curve c could intersect both A+ and A−? Assume that the homoclinic loop
determined by c is innermost in Hθ, and also innermost in the foliation of CA. Then
c bounds a disc on A+ ∪A−which is foliated by simple closed curves, so it would
intersect X0 twice if it intersects it at all. This would force a tangency between X0 and
a ﬁber of H, but X0 is in braid position, so this cannot happen. Therefore any leaf in
the foliation which is a simple closed curve must lie in the interior of Aϵ, ϵ = + or −.
Next, for simplicity assume that the foliation of A+ contains the homoclinic loop c
and refer to Figure 28. Our leaf c bounds a disc ∆θ in the ﬁber Hθ which contains c.
See Figure 28(a). (If c is homologically nontrivial in A+ then, since it bounds a disc in
Hθ, X+ would have a component that was the unknot.) If c is not intersected by any
clasp arcs then we can apply the argument of Section 3 (see Figure 16). Since both ∆θ
and ∆c are embedded their union ∆θ ∪c ∆c is an embedded 2–sphere.
Now consider a clasp arc that intersects c. Since clasp arcs are transverse to the foliation
of CA, any clasp arc that intersects c intersects it exactly once. Thus, any clasp arc that
intersects c must have a puncture endpoint in ∆c, where X−intersects A+. (Referring
to Figure 28(a), the gray braid strands represent X−.) Since any braid that enters
the 2–sphere ∆θ ∪c ∆c must puncture ∆θ, and can only exit by puncturing ∆c, we
conclude that only X−can intersect ∆θ.
Next, we consider the intersection of ∆θ ∩(A+ ∪A−) ⊂∆θ. In principle, this
intersection set can contain three types of arcs/curves: arcs that have an endpoint on
both X−and c; arcs that have both endpoints on c; and simple closed curves. Notice
that there can be no arcs that have both endpoints on X−because this would violate
the orientation of X−. Since we are assuming that c is innermost for the moment we
ignore the issue of simple closed curves. Referring to Figure 28(b) notice that for
every puncture point in ∆c there is a point on c that is an intersection with a clasp
arc. But, also for every puncture point of X−with ∆c there must be a puncture point
of X−with ∆θ. So the second type of arc of intersection—having both endpoints on
c—cannot occur. If we then perform the surgery illustrated in Figure 28(a), we see
that this corresponds to a truncation of the clasp arcs. That is, this surgery on a simple
closed curve in the homoclinic leaf replaces the immersed annulus with a new immersed
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
453
∆0
∆c
surgery + isotopy
surgery + isotopy
(a)
(b)
Figure 28: The elimination of a homoclinic singularity and associated simple closed curves,
in the presence of clasp arcs. Sketch (a) is the geometric realization. Sketch (b) shows the
preimage in PA.
Geometry & Topology 10 (2006)
454
Joan S Birman and William W Menasco
surface which is union of an annulus and a 2–sphere, where the latter can be discarded.
It replaces a clasp intersection with a clasp intersection and ribbon intersection on the
discarded 2–sphere. Afterwards, clasp intersections are still in braid position. This
surgery eliminates at least one saddle singularity (and, possibly some points of CA∩A).
Reiterating this procedure we will arrive at a point where the foliation of CA has no
leaves that are simple closed curves, except in one situation.
The situation where we will not be able to perform the surgery illustrated in Figure 28
is when the homoclinic point involves a singularity between an s–arc (see Figure 29)
and a simple closed curve where the disc ∆θ contains the endpoints of the resulting
singular leaf which are in X+ and X−. However, we can alter the foliation of CA in the
following manner to eliminate the leaf c. Let γϵ be any clasp arc that has an endpoint
e−ϵ ⊂∆c. Let α ⊂CA be an arc that starts at e−ϵ and ends at Xϵ such that int(α)
does not intersect any clasp arcs. It is convenient to take the support of α to be in a
union of ∆c and a regular neighborhood of the homoclinic singular leaf; and it can be
assumed that α is transverse to the foliation of CA except at a single point in ∆c near
e−ϵ. We now perform Alexander’s braid trick on α to make α ∪γϵ transverse to H.
In the resulting new foliation of CA the path α ∪γϵ cannot intersect any leaf that is a
simple closed curve for reasons of orientation. It is easily seen that once the homoclinic
point is eliminated for γϵ it will be eliminated for all clasp arcs that intersect ∆c. No
new homoclinic points are introduced.
Finally, if c is not innermost and ∆θ ∩(A+ ∪A−) ⊂∆θ does contain other simple
closed curves, we can achieve the assumption that c is innermost by ﬁrst performing
a surgery which is similar to that illustrated in Figure 28 on all of the simple closed
curves in ∆θ, starting with the innermost. Such surgeries may or may not eliminate any
saddle singularities, but they will create center points in the foliation. But, then we can
perform the surgery to eliminate the homoclinic saddle singularity on c.
We have learned that we may assume that every leaf is an arc. The situation is a little
bit more complicated than it was in the case of Seifert surfaces. Consult Figure 29.
There are now 5 possible types of non-singular arcs in the foliation of A+ and A−:
(i) arcs which have both endpoints at vertices (type b); (ii) arcs which have exactly
one endpoint at a positive vertex (type a+); (iii) arcs which have exactly one endpoint
at a negative vertex (type a−); (iv) arcs which have one endpoint on one boundary
component and the other on the opposite boundary component (type s); and (v) arcs
which have both endpoints on the same boundary component. As for type (v), the exact
argument that we used in the case of Seifert surfaces applies, because X+, X0, X−are
all closed braids, so type (v) does not occur.
Remark 4.1.1 With regard to Figure 29 we may need to reinterpret the boundary
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
455
+
+
-
-
type a−
type a+
type b
type s
X−
X+
Figure 29: Non-singular leaves in the foliation of A+ ∪A−, as viewed in the preimage of CA
components, temporarily, as (X+, X0) or (X0, X−) instead of (X+, X−). This ambiguity
will be removed shortly. See Remark 4.3.1 below.
♦
The annulus A+ ∪A−is said to be trivially foliated or trivial if it is foliated without
clasp arcs and the leaves in its foliation are all s–arcs.
An exhaustive list of the singularities which could, in principle, occur in the foliation
of A+ and A−are types a+a+, a+b, a+s, a+a−, a−a−, a−b, a−s, sb, ss, and bb,
where the notation is consistent with that used in Section 3. However, we have:
Lemma 4.1.1 Singularities of type ss do not occur in either A+ or A−.
Proof There is an oriented ﬂow on A+ ∪A−that is transverse to the foliation. In
particular, we have arranged that the foliation is transverse to the boundary in small
neighborhoods of X+ and X−, so that the ﬂow will be parallel to the boundary and
oriented to agree with the orientations on X+ and X−, both of which are oriented closed
braids. On the other hand, the fact that every singularity in the foliation is a saddle point
implies that every singularity in the associated ﬂow is hyperbolic. Suppose that there
was a singularity of type ss at polar angle 0. Then, for an arbitrarily small negative
polar angle −ϵ there must be a pair of type s non-singular leaves s1, s2 moving toward
one another on a collision course. However, a type s leaf separates the annulus and as
we just noted the ﬂow near the two endpoints of both s1 and s2 is in the direction of the
orientation of X+ and X−. It is then impossible for the images of s1 and s2 in the ﬂow
to approach one-another, as the ﬂow evolves.
Lemma 4.1.2 If a singularity of type a−a−or a−s occurs, then the associated singular
leaf is always intersected by a clasp arc.
Proof Suppose that a singularity of either type a−a−or a−s occurs, and that no clasp
arc intersects the associated singular leaf. See Figure 30. Notice that there is an arc,
α, contained in the singular leaf which has both of its endpoints on X−and which,
Geometry & Topology 10 (2006)
456
Joan S Birman and William W Menasco
α
β
Figure 30: Type a−a−and a−s singularities do not occur
together with one of the two subarcs β of X−\ (X−∩∂α) forms a simple closed curve
C which bounds a disc D ⊂A−. Since C bounds a disc it represents the unknot. Now
observe that if we perturb the endpoints of α slightly along X−we may change α to an
arc α′ which is transverse to ﬁbers of H. Thus, after an arbitrarily small perturbation,
we may change C to C′ = α′ ∪β, where C′ is a closed braid and where β ⊂X−is
a subarc of the closed braid X−. Let b be the braid index of C′. The fact that C′ is
everywhere transverse to ﬁbers of H guarantees that b ≥1. But then, we may reduce
the braid index of X−by at least one without changing its knot type by replacing β
by α′. However that is impossible because by hypothesis the braid index of X−is
minimal.
+
+
+
+
+
+
+
-
-
-
-
-
-
+
-
-
+
+
a+a+
a+b
a+s
a−a+
a−a−
a−b
a−s
sb
bb
Figure 31: Possible tile types in the foliation of A+ ∪A−. The black (resp. grey) arcs always
represent subarcs of X+ (resp. X−), with one exception: when we construct the tabs we will be
working in A−and X0 will enter the picture as a (dotted) grey arc.
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
457
