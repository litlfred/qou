---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-032-94-path-lifting
section_title: "Path lifting"
section_number: 9.4
pages: 59-61
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
In§§4-5 we studied at great length the generating functions F (℘,ϑ ) of framed 2d-4d BPS
degeneracies. Let us set aside the physical meaning of these functions for a moment and
just think of them as some interesting mathematical objects. We found in§4.4 thatF (℘,ϑ )
could be completely constructed from the datum of the spectral networkWϑ together with
its soliton content. One of the main motivations of our deﬁnition of spectral network is
that, given any spectral network, we can make a very similar construction. In this section
we describe that construction. For notational convenience we consider only the case of
a nondegenerate spectral network, but what we write has an obvious extension to the
degenerate case.
We will be rather brief since everything is parallel to what we did in §4.4. However,
we slightly modify §4.4, in two respects. First, with an eye toward future applications,
– 57 –
instead of homology classes of open paths on ˜Σ, we will keep track of homotopy classes.
This turns out to be no more diﬃcult. We will generally denote the homotopy objects
with a bold letter to distinguish them from their homology cousins. Second, instead of
considering smooth paths ℘ in C and using their canonical lift to ˜C, it will be convenient
to work with arbitrary paths ˜℘ on ˜C from the beginning. This will involve lifting many
objects from C to ˜C or from Σ to ˜Σ; we always use a tilde to denote the lifted objects.
For any homotopy class a of open paths on ˜Σ, we introduce a corresponding formal
variable Xa, subject to the relation that if a and a′ project to the same homotopy class on
Σ then we have
Xa/Xa′ = (−1)w(a,a′). (9.3)
Now, given a spectral network W, let ˜W be the preimage of W on ˜C. Given a path ˜℘ on
˜C whose endpoints are not on ˜W, we are going to deﬁne a formal sum of these variables,
with integer coeﬃcients:
F( ˜℘,W) =
∑
a
Ω
′
( ˜℘,W, a)Xa. (9.4)
(In§4.1 we met a similar expansion for which the coeﬃcients Ω
′
were interpreted as framed
2d-4d BPS degeneracies. In the more general setting of this section, we do not know what
the physical interpretation of Ω
′
should be.)
The assignment F(·,W) will obey two important properties:
• For two concatenatable paths ˜℘, ˜℘′ on ˜C,
F( ˜℘ ˜℘′,W) = F( ˜℘,W)F( ˜℘′,W). (9.5)
• If ˜℘ and ˜℘′ are two paths on ˜C which project to the same homotopy class on C,
F( ˜℘,W) = (−1)w( ˜℘, ˜℘′)F( ˜℘′,W). (9.6)
(In particular, if ˜℘ and ˜℘′ are homotopic, then F( ˜℘,W) = F( ˜℘′,W).)
Given any path ˜℘ on ˜C′ we ﬁrst deﬁne
D( ˜℘) =
K∑
i=1
X ˜℘(i). (9.7)
where ˜℘(i) is the open path given by lifting the initial point of ˜℘ to the i-th sheet and then
using the canonical connection on ˜Σ→ ˜C to lift the path. For any ˜℘ which does not cross
˜W we have simply
F( ˜℘, ˜W) = D( ˜℘). (9.8)
For any ˜℘ which crosses ˜W exactly once at a wall pc, we have
F( ˜℘, ˜W) = D( ˜℘+)
(
1 +
∑
ν∈Sc
Xa(ν, ˜℘)
)
D( ˜℘−), (9.9)
where a(ν, ˜℘) is a particular lift of the soliton sν to ˜Σ, described in the next paragraph.
– 58 –
Let ℘ be the projection of ˜℘ to C. Let z be the point of intersection between ℘ and
W. Let ˜z be the point of ˜℘ lying overz, dividing ˜℘ into ˜℘+ ˜℘−. Let o+ be a tangent vector
at z oriented alongW, and o− a tangent vector at z oriented oppositely to W. Let A+
be some path from ˜z to o+ in the circle ﬁber ˜Cz, and A− a path from o− to ˜z in ˜Cz. The
concatenation A = A− +A+ is thus a path from o− to its antipode o+ in ˜Cz; we ﬁx our
choices of A± so that A is homotopic to a simple arc which covers half of ˜Cz, and this arc
includes the tangent vector ℘′(z). Each soliton sν(z) has a canonical lift to a smooth path
˜sν(z) on ˜Σ from o(i)
+ to o(j)
− . The path a(ν, ˜℘) on ˜Σ from ˜z(i) to ˜z(j) is deﬁned by
a(ν, ˜℘) =A(i)
+ + ˜sν(z) +A(j)
− . (9.10)
Finally, to deﬁne F( ˜℘,W) for an arbitrary path ˜℘ on ˜C whose endpoints are not on
˜W, we perturb ˜℘ slightly so that its intersections with ˜W are all transverse, break it into
pieces which meet ˜W at most once, and use (9.8), (9.9) and the composition property (9.5).
Our construction makes the composition property (9.5) manifest. The same arguments
given in§5.6 apply to our current construction and show the twisted homotopy invariance
(9.6).
The path-lifting rule F will be put to some mathematical use in §10 below. As men-
tioned in§1, we are hopeful that it will also have some interesting physical applications,
as well as connections to upcoming work of Goncharov and Kontsevich.
10 Coordinates for moduli of ﬂat connections
In this last section we discuss a mathematical application of spectral networks. Given a
spectral networkW subordinate to a K-fold covering Σ→C, we will construct a map
ΨW :M(Σ,GL (1); m)→M F (C,GL (K); m) (10.1)
whereM(Σ,GL (1); m) is a moduli space of twisted ﬂat GL(1)-connections∇ab on Σ and
MF (C,GL (K); m) is a moduli space of twisted ﬂat GL(K)-connections∇ onC, decorated
by some “ﬂag data” as we explain below. This map is a local symplectomorphism, and
conjecturally 1-1 onto its image.
Roughly speaking, ∇ = ΨW(∇ab) is obtained by a two-step process. We ﬁrst push
forward the GL(1) connection∇ab from Σ to C. This gives a ﬂat GL(K) connection on
the complement of the branch locus in C, which is everywhere diagonal. This connection
however cannot be extended over the branch points, because it has monodromy around
them. To deal with this problem we cut C into pieces along the network W, and then
reglue the connection with a nontrivial (and non-diagonal) transition function, controlled
by the soliton content ofW. This process eliminates the monodromy around branch points,
while not introducing unwanted monodromy anywhere else. We call this construction
