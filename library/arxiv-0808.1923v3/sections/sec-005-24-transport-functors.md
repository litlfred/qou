---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-005-24-transport-functors
section_title: "Transport Functors"
section_number: 2.4
pages: 10-11
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
The second tool we need for Section 3 is the concept of a transpor t functor. Transport functors are
an axiomatic formulation of connections in ﬁbre bundles – they are th e one-dimensional analogue of
transport 2-functors, the axiomatic formulation of connections on non-abelian gerbes we are aiming at
in the present article. We have introduced and discussed transpor t functors in [SW09].
From a general perspective, the deﬁnition of a “transport n-functor” is supposed to rely on a
recursive principle in the sense that it uses transport ( n − 1)-functors. This is one reason to recall
the deﬁnition of a transport functor. The other reason is to highlig ht the analogy between the two
deﬁnitions, which might be helpful to notice:
(a) Instead of the path 2-groupoid P2(X), we are looking at the path groupoid P1(X), obtained by
just taking objects and 1-morphisms of P2(X). A transport functor is a certain functor
F : P1(X) /d47/d47 T ,
for some target category T : it assigns objects in T – the “ﬁbres” – to the points of X, and
morphisms in T – the “parallel transport maps” – to paths in X.
– 10 –
(b) In order to say which functors are transport functors we ne ed a Lie groupoid Gr and a functor
i : Gr /d47/d47 T . A local i-trivialization of F is a surjective submersion π : Y /d47/d47 X, a functor
triv : P1(Y ) /d47/d47 Gr, and a natural equivalence
P1(Y )
π∗ /d47/d47
triv
/d15/d15
P1(X)
t tttttt
/d118/d126 tttttttt F
/d15/d15
Gr i
/d47/d47T .
(c) Associated to a local trivialization is a descent object : it is a pair (triv ,g ) consisting of the functor
triv : P1(Y ) /d47/d47 Gr and of a natural equivalence
g :π∗
1trivi /d47/d47 π∗
2trivi
satisfying a cocycle condition.
