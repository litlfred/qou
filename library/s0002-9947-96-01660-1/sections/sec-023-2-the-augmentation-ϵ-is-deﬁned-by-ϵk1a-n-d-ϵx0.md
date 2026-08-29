---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: sec-023-2-the-augmentation-ϵ-is-deﬁned-by-ϵk1a-n-d-ϵx0
section_title: "The augmentation, ϵ, is deﬁned by ϵ(K)=1a n d ϵ(X)=0 ,"
section_number: 2
pages: 23-25
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
doc_brief: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state"
---
3. The antipode, γ, is deﬁned by γ(K)= K−1 and γ(X)= −sX.
The element w =K2 satisﬁes the conditions
∆(w)= w⊗w,
ϵ(w)=1 ,
γ(w)= w−1,
γ2(b)= wbw−1 for all b∈B.
The trace condition is not satisﬁed since B has 4r one dimensional representa-
tions withX =0a n dK a4r-th root of unity, and it is clear that the trace condition
is not satisﬁed in these representations.
Example 6.6. Not all spherical Hopf algebras are modular Hopf algebras in the
sense of [17]. For example, the group algebra of a ﬁnite group over a ﬁeld of
characteristic 0, or more generally, any cocommutative, involutory, semisimple Hopf
algebra, is spherical and not modular.
Also, not all spherical Hopf algebras are ribbon Hopf algebras. The dual of the
group algebra of a non-commutative ﬁnite group can be made a spherical Hopf
algebra. However, the representation ring is non-commutative, and so the Hopf
algebra cannot be quasi-triangular.
The next proposition gives the application of spherical Hopf algebras to state
sum models.
Proposition 6.7. The category of representations of a spherical Hopf algebra, A,
is equivalent to a canonical strict spherical category.
In this category, the objects are lists of left A-modules and the morphisms A-
linear maps of the modules formed by tensor product over the list. The trace
4020 JOHN W. BARRETT AND BRUCE W. WESTBURY
trL of an endomorphism θ of a left A-module is the matrix trace of θw.T h e f u l l
construction is given in [3].
Some extra conditions are required to give invariants of manifolds. The ﬁrst way
this can be achieved uses the same data as the construction of invariants given in
[11].
Proposition 6.8. Let A be a ﬁnite dimensional involutory Hopf algebra over an
algebraically closed ﬁeld of characteristic 0. Then A determines a 3-manifold in-
variant.
Proof. The Hopf algebra A gives a spherical Hopf algebra by taking w =1 . I nt h i s
case the quantum trace is just the matrix trace. The algebra A is semisimple by
[12]. Hence the category of ﬁnite dimensional left A-modules is a spherical category
which satisﬁes the hypotheses of Theorem 5.1.
In general, the construction of the non-degenerate quotient is another way of
attaining the semisimple condition. The following proposition is proved in [3].
Proposition 6.9. Let A be a spherical Hopf algebra over an algebraically closed
ﬁeld. Then the non-degenerate quotient of the spherical category of ﬁnitely generated
left A-modules is semisimple.
A corollary to the proof of this proposition is that the nondegenerate quotient of
any spherical subcategory of the category of left A-modules which is closed under
taking direct summands is a semisimple spherical category. Thus, in order to con-
struct a manifold invariant, it is suﬃcient to construct such spherical subcategories
which are ﬁnite and have non-zero dimension.
Let A be a ﬁnite dimensional spherical Hopf algebra. If A is semisimple as an
algebra, then it is clear that the non-degenerate quotient of the category of left A-
modules satisﬁes all the hypotheses of Theorem 5.1 except possibly the condition
that K = 0. In the following discussion we assume that A is not semisimple. In
this case the set of isomorphism classes of simple objects in the non-degenerate
quotient may well be inﬁnite. This may come about since each A-module V that
satisﬁes End
A(V )∼=F and which has non-zero quantum dimension gives a simple
object in the quotient. The condition that End A(V )∼=F is much weaker than the
condition that V is irreducible. Although it is possible for inequivalent modules to
give equivalent simple objects in the quotient, there is no apparent reason for the
set of simple objects in the quotient to be ﬁnite, in general.
Hence in order to construct a manifold invariant from a spherical Hopf algebra
A which is not semisimple it is necessary to ﬁnd a proper spherical subcategory
of the category of left A-modules such that the non-degenerate quotient is ﬁnite
and has non-zero dimension. A subcategory of a spherical category is a spherical
subcategory if and only if it is closed under addition, tensor product and taking
duals.
The category of left A-modules has a proper spherical subcategory, namely the
category of projective left A-modules. This category is spherical, since it is closed
under tensor product and is closed under taking duals by [13]. However, the next
proposition is a negative result which shows that this spherical subcategory cannot
be used to construct manifold invariants.
Proposition 6.10. LetA be a ﬁnite dimensional pivotal Hopf algebra which is not
semisimple. Then every projective A-module has zero quantum dimension.
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 4021
Proof. If A is any Hopf algebra, then the linear functional
a↦→ tr(x↦→γ−2(xa))
is a right co-integral. If A is not a semisimple algebra this is identically zero [12,
Proposition 2.4]; and so if A satisﬁes the hypotheses of the proposition then, for
all a∈ A,t r (x↦→ w−1xaw) = 0. Now choose a primitive idempotent π and put
a =πω−1.T h i sg i v e s
0=t r (x↦→w−1xπ)=d i mq(Aπ),
which shows that every indecomposable projective A-module has zero quantum
dimension.
Examples of spherical Hopf algebras which are not semisimple are quantised
enveloping algebras at roots of unity. The following theorem shows that each of
these examples gives a manifold invariant. This theorem is proved in [1] for odd
roots of unity and in [2] in general. The main steps of the argument follow.
Theorem 6.11. Let A be a quantised enveloping algebra of a ﬁnite dimensional
semisimple Lie algebra at a root of unity. Assume that the order, k, of the quantum
parameterq is at least the Coxeter number of the Lie algebra. Then the category of
tilting modules is spherical and the non-degenerate quotient is ﬁnite with non-zero
dimension, satisfying the hypotheses of Theorem 5.1.
Proof. It follows from the deﬁnition that the category of tilting modules is closed
under taking duals and direct summands. The set of tilting modules is also closed
under tensor product. The isomorphism classes of indecomposable tilting modules
are indexed by the dominant weights, and the quantum dimension is zero unless the
dominant weight lies in the interior of the fundamental alcove. In particular this
shows that the set of isomorphism classes of simple objects in the non-degenerate
quotient is ﬁnite. Each tilting module corresponding to a dominant weight in the
interior of the fundamental alcove is a Weyl module (as well as being irreducible),
and so the quantum dimension is given by the Kac formula. The quantum dimension
of the dual is given by substituting q
−1 for q in this formula. Since dim q(V )=
dimq(V∗) for anyV andq has unit modulus, it follows that each quantum dimension
is real. Hence the dimension K is a sum of positive real numbers. The condition
that k is greater than or equal to the Coxeter number ensures that there is at
least one dominant weight in the interior of the fundamental alcove, and so K is
non-zero.
