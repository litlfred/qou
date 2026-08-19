---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-007-35-a-problem-of-signs
section_title: "A problem of signs"
section_number: 3.5
pages: 17-19
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
We must now confront a pesky but important detail.
There is an ambiguity in (3.7): the generators F andJ are well deﬁned only up to
c-number shifts. As a result, the index Ω
′
(L℘,ϑ, ¯a) suﬀers from some potential ambiguity
(which even depends on℘). We can partially ﬁx this ambiguity by requiring thatΩ
′
(L℘,ϑ, ¯a)
is real, but this still leaves the possibility of an integer shift of F orJ . Such a shift
would reverse the sign of Ω
′
(L℘,ϑ, ¯a). So, a priori , we would expect that we need some
additional data in order to ﬁx Ω
′
(L℘,ϑ, ¯a) uniquely. A similar ambiguity aﬄicts the 2d-4d
BPS degeneracies µ(¯a): the deﬁnition (3.6) depends on the choice of generator F , and
changing this choice can change µ(¯a) by a sign.
There is no diﬃculty in ﬁxing these ambiguities locally in any particular corner of
parameter space. In this paper, though, we will mainly be concerned with phenomena which
occur when parameters are varied, sometimes over long distances in parameter space. It is
therefore desirable to have a global way of ﬁxing these sign ambiguities, which is consistent
with all of the physical constraints, and ideally one that does not depend on any arbitrary
choices. We have found such a rule, which we now describe. It would be desirable to give
a ﬁrst-principles derivation of this rule from the physics of the (2 , 0) theory S[g] in six
dimensions.
Figure 5. Two tangent directions at z determined by a ﬁnite web N: ˜z1 points “into” the ﬁnite
web while ˜z2 points “away.”
It will be useful to keep track of a bit more information about the ﬁnite webs N
representing 2d-4d BPS states. For any real surface S, let ˜S denote the circle bundle of
tangent directions to S. For z∈S we will let ˜z denote a lift of z to ˜S, that is, a choice of
tangent direction at z. Any smooth path ℘ on S carries a natural tangent direction ﬁeld
14See [21, 40–42] for a description of the halo approach to wall-crossing.
– 15 –
and hence has a canonical lift to a path ˜ ℘ on ˜S; we will use this lift often. There is a
distinguished class H∈H1(˜Σ; Z), represented by a path which winds once around a ﬁber
of ˜Σ (the choice of ﬁber does not matter).
By smoothing out the junctions slightly, we can deformNΣ into a ﬁnite union ofsmooth
paths on Σ, which thus has a canonical lift to a path N˜Σ on ˜Σ. Let ˜z1 and ˜z2 denote the
tangent directions to C at z shown in Figure 5. Let ˜z(i)
1 be the lift of ˜z1 to the i-th sheet
of ˜Σ, and similarly deﬁne ˜z(j)
2 . The path N˜Σ then has
∂N ˜Σ = ˜z(j)
2 − ˜z(i)
1 . (3.10)
Let ˜Γ(˜z1, ˜z2) denote the set of relative homology classes on ˜Σ obeying (3.10), modulo shifts
by the class 2H. ˜Γ(˜z1, ˜z2) is a principal Z/2Z-bundle over Γ(z1,z 2), with the Z/2Z action
given by adding H. The relative homology class [ N˜Σ]∈ ˜Γ(˜z1, ˜z2) thus keeps track of one
extra Z/2Z worth of information beyond that in [ NΣ]∈ Γ(z,z ). There can be diﬀerent
open ﬁnite BPS webs N carrying the same charge [ NΣ] but with diﬀerent lifts [ N˜Σ]; see
Figure 6 for an example.
(12)
12
23
(23)
31
(12)
12
23
(23)
31
12
23
Figure 6. Two open ﬁnite BPS webs N on the same patch ofC, drawn displaced from one another
for clarity. These two webs carry the same charge [ NΣ] but have diﬀerent lifts [ N˜Σ]. Informally,
one can say that the lifts of these two webs “diﬀer by one unit of winding.”
Now we can explain our proposal for how the sign of µ behaves. Given a charge
¯a∈ Γ(z,z ), µ(¯a) is not well deﬁned (although it is well deﬁned up to sign). In order to
make it well deﬁned, we propose that we must choose a class a∈ ˜Γ(˜z1, ˜z2) which projects
to ¯a. Having done so, there should be a way of ﬁxing the ambiguity of F to obtain a well
deﬁned BPS degeneracy, which we call µ(a). Two choices a,a′ diﬀer by a winding number
w(a,a′); the corresponding µ should obey
µ(a)/µ(a′) = (−1)w(a,a′). (3.11)
(Of course, knowing |µ(a)| for all a and knowing (3.11) is still not enough by itself to
determine µ. Later in this paper we will ﬁx one more convention, in (4.7), after which we
will be able to calculate µ(a) for all a.)
A similar discussion applies to Ω
′
(L℘,ϑ, ¯a), but with the extra complication that now
we have to discuss both the dependence on the path ℘ and on the charge ¯a. First suppose
we ﬁx the path ℘ from z1 to z2, with initial tangent vector ˜z1 and ﬁnal tangent vector
– 16 –
˜z2. Then we propose that the situation is strictly parallel to our discussion of µ above:
the degeneracies Ω
′
(L℘,ϑ, ¯a) are not well deﬁned (although they are well deﬁned up to
sign), and what is really deﬁned is an integer Ω
′
(L℘,ϑ,a ), where a∈ ˜Γ(˜z1, ˜z2) is a lift of
¯a∈ Γ(z1,z 2). The dependence on the choice of lift is given by
Ω
′
(L℘,ϑ,a )/Ω
′
(L℘,ϑ,a′) = (−1)w(a,a′). (3.12)
Now let us also consider the dependence on ℘. Recall from §3.3 that the line defect
L℘,ϑ depends only on the homotopy class of the path ℘. Nevertheless, the prescription for
ﬁxing the sign of Ω
′
(L℘,ϑ,a ) can depend on more information than just the homotopy class.
We propose that the sign actually depends on the homotopy class of the lift of ℘ from C
to the bundle of tangent directions ˜C. For two paths ℘, ℘′ whose lifts to ˜C have the same
initial and ﬁnal endpoints, there is a mod-2 winding number w(℘,℘′) (deﬁned similarly to
the winding number we considered above for paths on Σ). We propose that for such paths
we have
Ω
′
(L℘,ϑ,a )/Ω
′
(L℘′,ϑ,a ) = (−1)w(℘,℘′). (3.13)
We summarize this proposal by saying that the framed 2d-4d BPS degeneracies of the
interface L℘,ϑ are not quite homotopy invariants of ℘, but rather are “twisted homotopy
invariants” of℘.
