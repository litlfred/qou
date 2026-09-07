---
doc_id: arxiv-math-0611521v1
doc_title: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0611521v1.pdf
source_sha256: 65fcd77b7b0a208e
doc_brief: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP — We describe an explicit construction of galoisian Stokes op erators for irregular linear q-difference equations."
---
In this paper we return to the local analytic classiﬁcation o f q-difference modules. In [22] we gave such a
classiﬁcation in Birkhoff style [2, 3], using normal forms a nd index theorems. In [28] (cf. also [21], [23])
appears a classiﬁcation using non abelian cohomology of she aves on an elliptic curve. Here our aim is to
give a classiﬁcation based upon a “fundamental group” and it s ﬁnite dimensional representations, in the
style of the Riemann-Hilbert correspondence. At the abstra ct level there exists such a classiﬁcation: the
fundamental group is the tannakian Galois group of the tanna kian category of our q-modules, but we want
more information: our ﬁnal aim is to get a smaller fundamental group (as small as possible !) which is
Zariski dense in the tannakian Galois group and to describe i t explicitly. (As a byproduct, we shall get a
complete description of the tannakian Galois group itself. ) It is important to notice that the tannakian Ga-
lois group is an algebraic object but that the construction of the smaller group is based upon transcendental
techniques (topology and complex analysis).
This program is only partially achieved in this paper: even if we have the main ingredients, part of the work
remains conjectural. As in the differential case, the const ruction of the fundamental group is a Russian-
dolls construction using semi-direct products (heuristically, going from interior to exterior, each new “slice
of inﬁnitesimal neighborhood” of the origin (each “scale”) corresponds to an invariant subgroup in a new
semi-direct product). At the end there is a fascinating parallel between the differential and the q-difference
case. However, it has been impossible (for us) to mimick the d ifferential approach (essentially based upon
the concept of solutions); instead, we shall follow a new path. Before the descriptio n of our approach and
of our results in the q-difference case, let us recall, without proof, what happen s in the differential case (in
∗Institut de France (Acad´ emie des Sciences)
†Laboratoire Emile Picard, CNRS UMR 5580, U.F.R. M.I.G., 118, route de Narbonne, 31062 Toulouse CEDEX 4
1
this case the “fundamental group” is the wild fundamental group introduced by the ﬁrst author). We shall
not use these results but we need them at the heuristic level i n order to develop our q-analogies, therefore
we shall insist on the underlying geometric ideas.
We shall use tannakian categories as an essential tool (cf. [5], [30], 6, page 67). First recall some basic
facts. Assume E is a neutral tannakian category, with ﬁber functor ω (to the category of C-vector spaces),
then Aut⊗(ω) has a structure of complex pro-algebraic afﬁne group scheme; we shall call it the tannakian
group of the tannakian category E. The category E is isomorphic to the category of ﬁnite dimensional rep-
resentations of Aut⊗(ω) (by deﬁnition, such a representation factors through a representation of one of the
algebraic quotients). Conversely, if G is a complex pro-algebraic group, its category of complex re presen-
tations RepC(G) is a neutral tannakian category with a natural ﬁber functor ( the obvious forgetful functor)
ω G and G = Aut⊗(ω G,RepC(G)); the complex space aut⊗(ω G,RepC(G)) of Lie-like⊗-endomorphisms of
the ﬁber functor ω G is the Lie-algebra of Aut⊗(ω G,RepC(G)).
Assuming that Γ is a ﬁnitely generated group, a pro-algebraic completion of Γ is, by deﬁnition, a uni-
versal pair (ιal,Γal) where ιal : Γ→ Γal is a group homomorphism from Γ to a pro-algebraic group Γal.
It is unique up to an isomorphism of proalgebraic groups. A ﬁn ite dimensional representation of Γ clearly
factors through a proalgebraic completion of Γ. We can get a pro-algebraic completion of Γ from the
tannakian mechanism: RepC(Γ) is a neutral tannakian category with a natural ﬁber functor ( the obvious
forgetful functor) ω, and the group G = Aut⊗(ω,RepC(Γ)) is a pro-algebraic completion of Γ. The groups
Γ and G have the same representations, more precisely the natural h omomorphism of groups Γ→ G in-
duces an isomorphism of tannakian categories: RepC(G)→ RepC(Γ). We shall encounter below similar
situations associated to different classiﬁcation problem s (in a little more general setting: Γ will not be in
general a ﬁnitely generated group).
The ﬁrst example (our baby example) is the category of local m eromorphic regular-singular connections,
or equivalently the category D(0)
f of regular singular D-modules, where D = C({z})[d/dz] (C({z}) is the
ﬁeld of fractions of C{z}). A meromorphic connection is equivalent to an equivalence class of differential
systems ∆A : dY
dx = AY up to the gauge-equivalence: ∆A∼ ∆B if and only if there exists P∈ Gln(C({z}))
such that B = P−1AP−P−1dP/dx. We consider the fundamental groupπ1(D∗,d) of a germ at zero of punc-
tured disk, pointed on a germ of direction d. We choose a generator γ(a one turn loop in the positive sense)
and we get an isomorphism Z→ π1(D∗,d), n↦→γn. Then, by a very simple application of the Riemann-
Hilbert correspondance, our category D(0)
f is equivalent (via themonodromy representation) to the category
of ﬁnite dimensional representations of the fundamental group π1(D∗,d). A D-module M corresponds to a
representation ρM of π1(D∗,d).
We can apply the tannakian machinery to the groupΓ = Z (or equivalently toΓ = π1(D∗,d)). Then our cate-
gory D(0)
f is equivalent to the category of representations ofπ1(D∗,d): a D-module M “is” a representation
ρM of the topological fundamental group π1(D∗,d), it is also equivalent to the category of representations
of the pro-algebraic completion π⊗
