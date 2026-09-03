---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-006-33-classification-of-fiber-functors
section_title: "Classification of fiber functors"
section_number: 3.3
pages: 11-12
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
---
Theorem 3.6.LetGact on a finite tensor categoryC. Fiber functors onC G are in
bijection with conjugacy classes of pairs(H,M)such that:
(1)H≤G;
(2)Mis anH-equivariantC-module category whose underlyingC-module category
is indecomposable, exact, and semisimple;
(3)Hacts transitively onIrr(M);
(4)for some, equivalently every, simpleX∈M, the class[α X]∈H 2(StH(X),k×)
is nondegenerate.
Proof.By Proposition 3.1, a fiber functor onC G determines an exactC G-module
categoryNof rank one. In particular,Nis indecomposable and semisimple. Propo-
sition 2.2 gives a subgroupH⊆Gand anH-equivariantC-module categoryM, with
indecomposable exact underlyingC-module category, such thatN ≃MH. SinceH
is finite and|H|is invertible ink, Tambara’s semisimplicity theorem [Tam01, Propo-
sition 5.2] implies thatMis semisimple. Corollary 3.5 then gives transitivity of the
action onIrr(M)and nondegeneracy of the stabilizer cocycle.
Conversely, let(H,M)satisfy the conditions in the statement. Part (1) of Propo-
sition 2.2 shows thatMH is an exactCG-module category. SinceMis semisimple,
items (3)–(4) and Corollary 3.5 imply thatMH has rank one. Proposition 3.1 there-
fore produces a fiber functor onCG.
Finally, Theorem 2.4 says that two such pairs yield equivalentCG-module cate-
gories, and hence equivalent fiber functors, exactly when they are conjugate. This
proves both directions and the asserted bijection.□
12 C. GALINDO, C. GALLEGO, AND Y. MORALES
Corollary 3.7.Assume thatH 2(L,k×) = 0for every subgroupL≤G. Then fiber
functors onC G are classified by conjugacy classes of pairs(H,M)satisfying items
(1)–(2)of Theorem 3.6 and such thatHacts freely and transitively onIrr(M). This
applies in particular when every subgroup ofGis cyclic, hence whenGis cyclic.
Proof.Under the hypothesis, every stabilizer cocycle is cohomologically trivial. Its
twisted group algebra is therefore an ordinary group algebra, which is simple overk
exactly when the stabilizer is trivial. Theorem 3.6 gives the result.□
4.Fiber functors for the Hopf algebrasH p
We apply Theorem 3.6 to Nikshych’sC2-equivariantizations of Tambara–Yamagami
categories [Nik08].
