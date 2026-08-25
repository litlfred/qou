---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-011-43-the-spectral-network-w
section_title: "The spectral network W"
section_number: 4.3
pages: 20-23
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Our next aim is to explain how F (℘,ϑ ) can actually be computed. As it turns out, the
answer depends crucially on how ℘ meets a certain codimension-1 locus Wϑ⊂ C, which
we call a spectral network.
We say that a pointz∈C supports those charges ¯a∈ Γ(z,z ) for whichZ¯a(z)/eiϑ∈ R−.
DeﬁneWϑ to be the set of z∈C such that z supports some ¯a∈ Γ(z,z ) with µ(a)⁄= 0 (for
either lift a of ¯a).
Wϑ is a codimension-1 network on C, the union of segments which we call S-walls.
TheS-walls can end at branch points or at special points which we call joints, and can also
– 18 –
asymptote to the punctures of C. We will assume that along any S-wall, a generic point
supports exactly one charge ¯a.
There are two ways in which this genericity could be violated. One is for ϑ to be non-
generic: in that case some S-walls will support both a charge ¯a∈ Γij(z,z ) and a charge
¯b∈ Γji(z,z ). This phenomenon is crucial for our story and will be analyzed in§6. For now,
however, we are assuming ϑ generic, so we explicitly exclude this possibility. The second
way in which genericity could be violated is less common: it might happen accidentally
that e.g. λi−λj =λk−λl on a whole patch of C. In this case a single wall could support
both a charge ¯a∈ Γij(z,z ) and ¯b∈ Γkl(z,z ). If i,j,k,l are all distinct, all our discussion
in this section has a straightforward extension to that case; if they are not all distinct the
situation is more subtle. In any case, from now on we assume that a generic point along
anS-wall supports exactly one charge ¯a.
In this case, all points of any single S-wall support “the same” charge ¯a, in the sense
that if z, z′ are generic points on a common wall, the natural parallel transport along the
wall takes the charge ¯a∈ Γ(z,z ) supported at z into the charge ¯a′∈ Γ(z′,z′) supported
at z′. If we choose a charge a∈ ˜Γ(˜z, ˜z) lifting ¯a as discussed in §3.5, then the parallel
transport also takes a to an a′∈ ˜Γ(˜z′, ˜z′) lifting ¯a′.
Now recall the soliton degeneracies µ(a)∈ Z, which are deﬁned for any a∈ ˜Γ(˜z, ˜z),
so long as z ∈ C does not lie on a wall of marginal stability. 15 µ(a) does not depend
on the parameter ϑ, and its deﬁnition does not involve the spectral network Wϑ. In our
computation ofF (℘,ϑ ) below, though, we will ﬁnd that theµ(a) which are really important
are the ones where ¯a∈ Γ(z,z ) is supported at z — or said otherwise, we will be mainly
interested in evaluating µ(a) along theS-walls supporting ¯a. We will also ﬁnd below that
µ(a) is constant along eachS-wall supporting ¯a; with this in mind we immediately simplify
our notation by letting µ(a,p ) denote the constant value of µ(a) along a wall p supporting
¯a.
4.4 Computing F (℘,ϑ )
Now we can describe how F (℘,ϑ ) is computed. The recipe we will summarize here follows
from the 2d-4d wall-crossing formula of [5].
The simplest situation occurs when ℘ does not crossWϑ anywhere. Deﬁne
D(℘) =
K∑
i=1
X℘(i), (4.5)
where the ℘(i) are the canonical lifts of ℘ to the K sheets of ˜Σ. Then if ℘∩W ϑ =∅ we
have simply
F (℘,ϑ ) =D(℘). (4.6)
In other words, interfaces corresponding to short enough paths ℘ on C just support K
framed BPS states, one for each vacuum of the surface operator.
15To reduce potential confusion we emphasize that the walls of marginal stability are not the same thing
as theS-walls.
– 19 –
The more interesting question is how to compute F (℘) if ℘ does cross Wϑ. Because
of the composition property (4.4), it is enough to answer this question in the case where ℘
crossesWϑ exactly once.
So suppose ℘ crossesWϑ at a point z supporting a charge ¯a∈ Γij(z,z ). In this case
℘ is divided into two subpaths ℘+ and℘−, which we deform slightly to obtain ℘′
+ and℘′
−
as shown in Figure 8. Then we have 16
ij ij
Figure 8. A path ℘ crossing anS-wall is locally divided into two pieces℘±. We deform ℘± slightly
to paths ℘′
±, so that the ﬁnal tangent vector of ℘′
+ and the initial tangent vector of ℘′
− point along
theS-wall, in opposite directions. The paths ℘′
± are shown slightly displaced from the wall for
clarity.
F (℘,ϑ ) =D(℘) +D(℘′
+)(µ(a)Xa)D(℘′
−). (4.7)
The second term is the interesting one: it says that when ℘ crossesWϑ, F (℘,ϑ ) includes
paths which are segments of lifts of ℘ combined with “detours” along the lifts of BPS
solitons. (The point of our deformation from ℘± to℘′
± here was to arrange that the second
term makes sense, i.e. that D(℘′
+) andD(℘′
−) can be concatenated with the soliton charge
a.)
For later convenience, we introduce a second notation for (4.7). Let ˜ z denote the
tangent vector to ℘ at z. Let t1 be the shortest arc running from ˜z to the initial point of
a, in the ﬁber of ˜Σ overz. Similarly, let t2 be the shortest arc running from the ﬁnal point
of a to ˜z, in the ﬁber of ˜Σ over z; and deﬁne
a˜z =t1 +a +t2. (4.8)
Note that t1,t 2 are well-deﬁned because the intersection of ℘ andWϑ is assumed to be
transverse. With this deﬁnition (4.7) can be rewritten as
F (℘,ϑ ) =D(℘+)(1 +µ(a)Xa˜z)D(℘−). (4.9)
The formula (4.9) can be interpreted as a kind of wall-crossing formula for the framed
2d-4d BPS spectrum: it implies that when an endpoint of the path ℘ is moved across an
S-wall,F (℘,ϑ ) jumps by multiplication with a factor (1 + µ(a)Xa˜z). This is the way that
this formula appeared in [5].
16The factorµ(a)Xa appearing in (4.7) is independent of the choice of lift a of ¯a, because of (3.11), (4.1).
– 20 –
5 The spectral network Wϑ at ﬁxed ϑ
In§4 we have given a recipe for computing the generating functions F (℘,ϑ ). The recipe
depends on the data of the spectral network Wϑ and the framed 2d-4d BPS degeneracies
µ(·,p ) along each wall p ofWϑ. To make this recipe explicit, then, we need to be able to
determineWϑ and µ. In this section we explain how this can be done.
Throughout this section we continue to assume thatϑ is generic, in the sense explained
in§3.3.
