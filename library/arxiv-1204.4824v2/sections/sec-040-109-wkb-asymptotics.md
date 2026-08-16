---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-040-109-wkb-asymptotics
section_title: "WKB asymptotics"
section_number: 10.9
pages: 72-74
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
So far in this section we have been considering the map Ψ W associated to an arbitrary
spectral networkW. These maps have especially interesting asymptotic properties if we
chooseW to be the particular network Wϑ which we studied in the rest of the paper. In
this section we brieﬂy explain this point. (We will gloss over the role of the twisting in this
section, and use spin structures to pass freely between twisted and untwisted connections.)
Equip C with a complex structure. Suppose given a GL(K) Higgs bundle overC, i.e.
a triple (V, ¯∂,ϕ ) whereV is a complex vector bundle of rank K, ¯∂ a holomorphic structure
onV , and ϕ a meromorphic End(V )-valued 1-form, with poles at the punctures on C. Let
Σ be the spectral cover determined by ϕ,
Σ ={det(ϕ−λ) = 0}⊂ T∗C. (10.30)
Now assume that Σ is smooth (this is the case for genericϕ.) Then we have a corresponding
spectral line bundle over Σ,
L = ker(ϕ−λ), (10.31)
and the Higgs bundle (V, ¯∂,ϕ ) is the pushforward of (L,λ ).35
Now, given a Higgs bundle there is a corresponding solution of Hitchin’s equations
[16, 56–59]. In [5] we proposed a new method for constructing that solution. The key
ingredient is a set of integral equations written in§5.6 of [5]. The equations are determined
by the data of:
• the Higgs bundle (V, ¯∂,ϕ ),
• the BPS degeneraciesµ andω, which (as we have explained in§§4,5,6) are computed
from the spectral networksWϑ determined by Σ,
• a real parameter R> 0.
35The passage from ( V, ¯∂,ϕ ) to L is often called abelianization and has been exploited heavily in the
study of “nonabelian theta functions”; see e.g. [55] where it was introduced, and [50] for a very precise
description of the abelianization map in the more general setting of an arbitrary Lie groupG. Abelianization
for Higgs bundles is simpler than for ﬂat connections in one important respect: for Higgs bundles the
monodromy around branch points causes no problem and no spectral network is needed. There is thus only
one abelianization map for Higgs bundles, in contrast to the various Ψ W we found in this paper for ﬂat
connections.
– 70 –
These equations are expected to have a unique solution for large enoughR (constructed
e.g. by iteration). The solution produces a family of ﬂat connections ∇(ζ) in V , together
with a family of ﬂat connections ∇ab(ζ) inL, and a family of isomorphisms
g(ζ) : ΨWϑ=argζ(L,∇ab(ζ))→ (V,∇(ζ)). (10.32)
The integral equations give some control over the analytic structure and ζ → 0,∞
asymptotic behavior of g(ζ) and∇ab(ζ). From this we deduce that the family ∇(ζ) is of
the form
∇(ζ) =Rζ−1ϕ +D +Rζ ¯ϕ, (10.33)
where D is a connection in V , unitary with respect to some Hermitian metric h in V
(“harmonic metric”), and ¯ϕ is the adjoint of ϕ in the metric h. The fact that ∇(ζ) is
ﬂat for all ζ∈ C× is equivalent to the statement that ( V,ϕ,D, ¯ϕ) constitute a solution of
Hitchin’s equations on C. (The natural conjecture is that it is the unique such solution
corresponding to the given Higgs bundle (V, ¯∂,ϕ )). So the integral equations are a machine
for producing solutions to Hitchin’s equations.
In addition, the integral equations give some more interesting asymptotic information.
This information is most naturally formulated in terms of the objects
Ya(ζ) =Xa(∇ab(ζ))∈ Hom(V˜z1,V ˜z2). (10.34)
If we think of Ya(ζ) as a function of ˜ z2 then it is ﬂat with respect to the connection
∇(ζ), except when z2 meets the network Wϑ=argζ: when z2 crosses the S-walls,Ya(ζ)
jumps discontinuously. Analogous remarks hold for the dependence of Ya on ˜z1. From the
integral equations we learn that the ζ→ 0 asymptotics ofYa(ζ) are given by
Ya(ζ)∼ exp
[
πR
ζZ¯a
]
. (10.35)
Indeed, we can say something a bit stronger: suppose that we deﬁne a new section Yϑ
a (ζ)
by analytic continuation ofYa(ζ) from the locus arg ζ = ϑ. In this case, we have the
asymptotics
Yϑ
a (ζ)∼ exp
[
πR
ζZ¯a
]
, (10.36)
so long as ζ → 0 while remaining in the half-plane Hϑ centered on the ray arg ζ = ϑ.
This is rather sharp asymptotic information about the ﬂat sections of the family of ﬂat
connections∇(ζ).
Our way of describing this asymptotic information is perhaps a bit unfamiliar, so
let us relate it to something better known: the WKB analysis of 1-parameter families of
diﬀerential equations. The ﬂatness equation ∇(ζ)s = 0 takes the general form
[
ζ d
dz + (Rϕ +ζ(··· ))
]
s = 0. (10.37)
The WKB analysis of this equation involves studying formal solutions of the form
s(i)
fo (ζ) = exp
[
1
ζ
∞∑
n=0
S(i)
n ζn
] ∞∑
n=0
T (i)
n ζn (10.38)
– 71 –
where eachS(i)
n is a function andT (i)
n is a section ofV . One important diﬃculty in the WKB
method is that these solutions really are only formal: the series (10.38) typically has zero
radius of convergence. So one should interpret (10.38) as an asymptotic series. It is then
natural to ask, are there actual ∇(ζ)-ﬂat sections s(i)(ζ) which have these asymptotics?
Our discussion in this section provides the answer: such sections do indeed exist, in
the following sense. Fix a phase ϑ, a basepoint ˜z1∈ ˜C′
Wϑ, and basis vectors e(i)∈L (i)
˜z1 .
Then letting ˜℘ be a path in ˜C′
Wϑ from ˜z1 to ˜z, we can deﬁne
s(i)(ζ) =e(i)Yϑ
˜℘(i)(ζ). (10.39)
s(i)(ζ) is a solution of∇(ζ)s(i)(ζ) = 0, and (10.36) implies thats(i) indeed has an asymptotic
expansion of the form (10.38), as ζ → 0 in the half-plane Hϑ. So, in each connected
component of ˜C′
Wϑ, we have a basis of ∇(ζ)-ﬂat sections which have the asymptotics
predicted by WKB, as ζ→ 0 in Hϑ. As we move from one component of ˜C′
Wϑ to another,
these bases change. Thus the walls of Wϑ have an interpretation as Stokes lines.
Finally, we should say that some of the structures which appeared in this paper have
appeared before in the WKB literature (although we arrived at them independently.) In
the case K = 2, our constructions here and in [3] seem to be closely related to a line
of development pursued by Voros and others (e.g. [18, 19, 60, 61]). For K > 2, the
phenomenon that new Stokes lines can be born at intersections between old ones was
apparently ﬁrst noticed in [62], and has been followed up in a few works since then; we
note in particular the reference [20], which contains examples of Stokes diagrams in the case
K = 3 which look identical to our Wϑ. What we have here called joints are there called
virtual turning points . There are also results of Simpson on asymptotics of monodromy
which seem likely to be related to ours, e.g. [63, 64]. We have not understood the precise
relation.
