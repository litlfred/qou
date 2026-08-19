---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-vector Fields on Quaternionic Flag Manifolds"
section_id: sec-005-3-quatrisson-and-tetraplectic-structures
section_title: "Quatrisson and tetraplectic structures"
section_number: 3
pages: 4-6
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
doc_brief: "Geometry of Four-vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-ve ctor ﬁelds on quaternionic ﬂag manifolds, which geometrically determ ine"
---
Recall that a symplectic manifold is a manifold equipped with a closed non -
degenerate 2-form. We also recall that a Poisson manifold is a manifo ld equipped
with a bi-vector ﬁeld that induces a Lie algebra structure on the spa ce of smooth
functions, compatible with the commutative product of functions v ia the Leibniz
rule. In the case of quaternionic ﬂags, we make use of the following s tructures
which reﬂect the underlying geometry:
Deﬁnition 3.1 [6] Let X be a real orientable manifold of dimension 4m. A
tetraplectic structure on X is a four-form, ψ satisfying:
1) ψ is closed (dψ = 0)
2) ψm is a volume form
We call the pair (X,ψ ) a tetraplectic manifold . A map φ : (X,ψ )→ (X ′,ψ ′) is
called tetraplectic if φ∗ψ′ =ψ. If, in addition, φ is a diﬀeomorphism, then we
call φ a tetraplectomorphism.
Example. Let ψ be an Sp(2)-invariant volume form on S4. Then ( HP1,ψ) is
a teraplectic manifold. In fact, in [6] the construction of invariant t etraplectic
structures on all quaternionic ﬂag manifolds was given. ©
One can deﬁne a standard Poisson structure on a manifold by giving a bi-vector
ﬁeld whose the Schouten bracket with itself is zero. However, in ord er to reﬂect
the geometry of our situation we will make use of 4-vector ﬁelds, fo r which we
recall the following [17]:
Proposition 3.2 Denoting ⋀ iχ(M ) the space of i-vector ﬁelds on M , there
exists a unique bracket, called the Schouten bracket:
[·,·] :
p⋀
χ(M )×
q⋀
χ(M )→
p+q−1⋀
χ(M )
which extends the usual Lie bracket of vector ﬁelds and is an R-linear operation
satisfying the following identities:
1) [ P,Q ] = (−1)pq[Q,P ] (Anti-Symmetry)
2) [ P,Q∧R] = [P,Q ]∧R + (−1)pq+qQ∧ [P,R ] (Leibniz)
3) ( −1)p(r−1)[P, [Q,R ]] + (−1)q(p−1)[Q, [R,P ]]
+(−1)r(q−1)[R, [P,Q ]] = 0 (Jacobi)
We recall that in [1] the authors use the vanishing of the Schouten b racket of ap-
vector ﬁeld ξ with itself, [ξ,ξ ] = 0, to deﬁne the Generalized Poisson Structures
(GPS). For etymologic-semantic reasons, we give the following deﬁn ition:
Deﬁnition 3.3 LetM be a manifold, and let ξ be a 4-vector ﬁeld on M satis-
fying [ξ,ξ ] = 0 . We call ξ a quatrisson structure on M and the pair (M,ξ ) a
quatrisson manifold .
Quatrisson structures and H-ﬂags 5
Deﬁnition 3.4 For two quatrisson manifolds ( X, ξ) and ( X ′,ξ′) a map φ :
X → X ′ is called a quatrisson map if for any quadruple of functions fi ∈
C∞(X ′), 1≤i≤ 4 the following identity holds:
ξ(dφ∗f1∧dφ∗f2∧dφ∗f3∧dφ∗f4) = φ∗ξ′(df1∧df2∧df3∧df4).
i.e. φ∗(ξ) = ξ′.
Deﬁnition 3.5 Let ξ be a 4-vector ﬁeld on a 4m-dimensional manifold, M .
Then we call ξ non-degenerate if ξ∧m is a nowhere vanishing 4m-vector ﬁeld.
If ξ is a non-degenerate vector ﬁeld on M , then ξ induces a surjection⋀ 3 T∗
xM → TxM for all x∈ M , obtained by contraction with ξ. If ( M,ξ )
is quatrisson, we deﬁne the rank of ξ at x∈M as the dimension of the image
of this map. One can see that a quatrisson structure ξ onM is non-degenerate
if the rank of ξ at any point of M is equal to the dimension of M .
Lemma 3.6 Letting (M,ξ ) be as above, the rank of ξ at any x∈M is divisible
by 4.
Proof. This is an easy exercise in multi-linear algebra for the reader. ✷
Deﬁnition 3.7 Let M be a manifold equipped with a 4-vector ﬁeld ξ. We say
that a smooth 4l-dimensional submanifold, L, is a tetraplectic leaf in M if:
1) ξ comes from ⋀ 4χ(L) at all points of L
2) ξ is non-degenerate on L
3) L is not properly included in any other such submanifold of M
4) the four-form, ψ, given by iψξm =ξm−1, deﬁnes a
tetraplectic structure on M .
To each triple of functions f =(f1, f2, f3), we can associate a “hamiltonian”
vector ﬁeld Xf given by ι(df1∧df2∧df3)ξ. Then we get the characteristic
distribution of M . Unlike in the Poisson case, we cannot expect in general
that (M,ξ ) is stratiﬁed as a union of smooth tetraplectic leaves, even if ξ is
quatrisson, see Example 8 in [7]. However, the particular case of this result for
quaternionic ﬂag manifolds will follow later.
Example. Let Fn be a quaternionic ﬂag manifold considered as a tetraplectic
manifold with an Sp(n)-invariant 4-form ψ [6]. The corresponding 4-vector
ﬁeld, χ, deﬁned by iχ (ψm) = ψm−1, is quatrisson and Sp(n)-invariant. We
refer to χ as the invariant quatrisson structure of Fn.©
4 Quatrisson structures on HP 1.
For our ﬂag manifolds, we construct a Bruhat quatrisson structu re explicitly by
analogy to the Poisson case as in [11] or [15]. We begin by deﬁning a quat risson
4-vector ﬁeld, κ, on Sp(2), which we show descends to the quotient Σ \Sp(2).
