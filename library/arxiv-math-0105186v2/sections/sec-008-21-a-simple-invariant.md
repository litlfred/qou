---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-008-21-a-simple-invariant
section_title: "A simple invariant"
section_number: 2.1
pages: 22-24
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
Let (E2n+2,π ) be an exact Lefschetz ﬁbration over S. A Lagrangian boundary
condition is an (n+1)-dimensional submanifold Q⊂E|∂S which is disjoint from
∂hE and such that π|Q :Q→∂S is a submersion, together with κQ∈ Ω 1(∂S )
and KQ∈ C∞(Q, R), satisfying Θ |Q = π∗κQ +dKQ. This implies that each
Qz =Q∩Ez,z∈∂S , is an exact Lagrangian submanifold of Ez, with function
KQ|Qz (one could consider a more general situation in which the con dition on
π|Q is dropped, so that the Qz could have singularities; but we will not do that).
From Lemma 1.3 one sees that parallel transport along ∂S carries the Qz into
each other, in the ordinary sense of the word; this holds in th e “exact” sense,
that is to say as exact Lagrangian submanifolds, iﬀ κQ = 0. Note also that if
one equips E with a symplectic form Ω + π∗β as in Lemma 1.5, Q itself becomes
a Lagrangian submanifold. The aim of this section is to intro duce, in the case
where S is compact with ∂S⁄=∅, a Gromov-type invariant
Φ 1(E,π,Q )∈H∗(Qζ; Z/2),
where ζ is some point of ∂S . In a nutshell, this is the cycle represented by the
values at ζ of pseudo-holomorphic sections of E with boundary in Q.
To begin, we remind the reader of a class of almost complex str uctures suit-
able for exact symplectic manifolds. The Liouville vector ﬁ eld N on such a
manifold, iNω =θ, deﬁnes a collar R−×֒→M . Let σ be the function on
a neighbourhood of ∂M whose composition with R−×֒→M is projection
to the R− factor. An ω-compatible almost complex J is called convex near the
boundary if θ◦J = d(eσ) near ∂M . This implies d(d(eσ)◦J) = −ω, which
serves to control the behaviour of J-holomorphic curves. It is well-known that
the space of these J is contractible (in particular, nonempty).
22
Given an exact Lefschetz ﬁbration ( E,π ), one can consider the Liouville
vector ﬁeld on each ﬁbre, and this gives rise to a function σ on a neighbourhood
of ∂hE in E. Choose a complex structure j on the base S (whenever we do
that, now or later, j is assumed to be positively oriented and equal to j0 in
some neighbourhood of Scrit). An almost complex structure J on E is called
compatible relative to j if
(i) J =J0 in a neighbourhood of Ecrit;
(ii) Dπ◦J =j◦Dπ;
(iii) Ω( ·,J·)|TEv
x is symmetric and positive deﬁnite for any x∈E;
(iv) in a neighbourhood of ∂hE,J(TEh) = TEh and Θ ◦J =d(eσ).
To see more concretely the meaning of these conditions, take x /∈Ecrit and split
TEx =TEh
x⊕TEv
x∼=TSz⊕TEv
x,z =π(x). One can then write
Jx =
(jz 0
Jvh
x Jvv
x
)
(2.1)
where Jvv
x ∈ End(TEv
x) is a complex structure compatible with Ω |TEv
x, and
Jvh
x ∈ Hom(TSz,TE v
x) is C-antilinear with respect to j and Jvv . This is a
reformulation of (ii), (iii). An immediate consequence is t he following result,
which sharpens Lemma 1.5:
Lemma 2.1. LetJ be compatible relative to j. Then for any suﬃciently posi-
tive β∈ Ω 2(S), Ω + π∗β tames J.
Because of the lack of antisymmetry in (2.1), J will not be compatible with
Ω + π∗β in the ordinary sense of the word, unless Jvh = 0; we will return
to this more restricted class of almost complex structures i n the next section.
Continuing with the analysis of the conditions above, suppo se now that x∈E
is suﬃciently close to ∂hE. More precisely, we require that σ(x) is deﬁned and
that (iv) applies. There is then a further splitting
TEv
x∼= RN⊕ RR⊕ (ker Θ ∩ kerdσ∩TEv
x), (2.2)
where N is the Liouville vector ﬁeld and R is the Hamiltonian vector ﬁeld of
eσ|Ez. The two parts of (iv) say that Jvh
x = 0 and that with respect to (2.2),
Jvv
x =


0 −1 0
1 0 0
0 0 ∗

. (2.3)
The pointwise analysis which we have just carried out can be r ecast in terms of
sections of ﬁbre bundles, and one sees then that the space J(E,π,j ) of almost
complex structures which are compatible relative to j is contractible.
Suppose now that we have a Lagrangian boundary condition Q. The theory of
pseudo-holomorphic sections with boundary in Q ﬁts into a familiar framework
23
of inﬁnite-dimensional manifolds and maps. We will now revi ew this, on a formal
level, that is to say using C∞ spaces and without assuming that S is compact.
In that sense, J(E,π,j ) is an inﬁnite-dimensional manifold; its tangent space at
J consists of sections Y ∈C∞(End(TE )) which are zero near Ecrit and can be
written, in parallel with (2.1), as
Yx =
( 0 0
Yvh
x Yvv
x
)
(2.4)
withYvv
x an inﬁnitesimal deformation of the compatible complex stru ctureJvv
x ,
and Yvv
x Jvh
x +Jvv
x Yvh
x =−Yvh
x jz. There is a further requirement about Y
near ∂hE, the linearization of (iv), which we leave to the reader to wr ite
down. The space B of sections u : S → E satisfying u(∂S ) ⊂ Q is also
an inﬁnite-dimensional manifold, with T Bu ={X ∈ C∞(u∗TEv) : Xz ∈
T (Qz) for all z∈∂S}; note that u∗TEv→S is really a vector bundle, since u
as a smooth section of π avoidsEcrit. Consider the inﬁnite-dimensional vector
bundle E→ B× J(E,π,j ) whose ﬁbre at ( u,J ) is Ω 0,1(u∗TEv), the space of
(0, 1)-forms on ( S,j ) with values in u∗(TEv,J|TEv). It has a canonical sec-
tion ¯∂univ(u,J ) = 1
