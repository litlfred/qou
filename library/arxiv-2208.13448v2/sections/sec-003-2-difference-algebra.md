---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-003-2-difference-algebra
section_title: "Difference algebra"
section_number: 2
pages: 3-7
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
2.1. Galois groups. In this section, we make a short overview of the Galois theory of linear
diﬀerence equations. For more details on what follows, we ref er to [ VdPS97, Chapter 1].
A diﬀerence ring is a commutative ring R equipped with an automorphism φ : R → R.
We denote by CR := {c ∈ R|φ(c) = c}, the constants of the diﬀerence ring ( R, φ). A
diﬀerence ideal I of a diﬀerence ring ( R, φ) is an ideal such that φ(I) ⊂ I. If R is a ﬁeld,
we call ( R, φ) a diﬀerence ﬁeld. In this case, CR is a ﬁeld, the ﬁeld of constants. With an
abuse of notations, we will often denote by R the diﬀerence ring ( R, φ).
Throughout this paper, we assume that (k, φ) is a diﬀerence ﬁeld such that its ﬁeld of
constants Ck is algebraically closed.
4 THOMAS DREYFUS AND MARINA POULET
If we consider a diﬀerence system
(2.1) φ(Y ) = AY, with A ∈ GLn (k) ,
according to [ VdPS97, Section 1.1], there exists a diﬀerence ring extension ( L, φ) of ( k, φ)
such that:
• there exists a fundamental matrix of solutions of ( 2.1) with entries in L, that is,
a matrix U ∈ GLn (L) such that φ (U ) = AU ;
• L is generated as a k-algebra by the entries of U and det (U )−1;
• the only diﬀerence ideals of L are {0} and L.
A diﬀerence ring L which satisﬁes these conditions is called a Picard-Vessiot ring for the
system ( 2.1) over k. It is unique up to isomorphisms of diﬀerence rings over k. We have
the following property: CL = Ck.
The diﬀerence Galois group G of ( 2.1) over k is the group of k-linear automorphisms
of L commuting with φ, that is,
G := {σ ∈ Aut(L/k) | σ ◦ φ = φ ◦ σ} .
For any fundamental matrix U ∈ GLn(L), an easy computation shows that U −1σ(U ) ∈
GLn(CL) = GL n(Ck) for all σ ∈ G. By [ VdPS97, Theorem 1.13], the faithful
representation
ρ : G → GLn(Ck)
σ ↦→ U −1σ(U )
identiﬁes G with a linear algebraic subgroup G ⊂ GLn(Ck). If we take another
fundamental matrix of solutions V , we ﬁnd an algebraic group that is conjugated to
the ﬁrst one. In this paper, by “computation of the diﬀerence G alois group G” , we mean
“computation of an algebraic subgroup of GL n (Ck) conjugated to ρ(G)” , thus we work up
to conjugations. Abusing notations, we will still denote by G the image of the diﬀerence
Galois group under the above representation.
We denote by k
⟨
φ, φ−1⟩
the ¨Ore algebra of noncommutative Laurent polynomials with
coeﬃcients in k such that φf = φ(f )φ for all f ∈ k. We consider the diﬀerence equation
(2.2) Ly = 0, where L :=
n∑
i=0
aiφi ∈ k ⟨φ⟩ with a0an ⁄= 0 ,
that is, a0y + · · · + anφn(y) = 0 with ai ∈ k and a0an ⁄= 0. We transform the diﬀerence
equation ( 2.2) into the diﬀerence system
φ(Y ) = ALY, where AL =


1
. . .
1
−a0/an . . . −an−1/an


is the companion matrix associated with L. By deﬁnition, the diﬀerence Galois group of
(2.2) is the diﬀerence Galois group of the system [ AL].
The change of variables Z := T Y , T ∈ GLn(k), transforms the system φY = AY with
A ∈ GLn(k) into φZ = BZ where B := φ(T )AT −1 ∈ GLn(k). Let A, B ∈ GLn(k).
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 5
We will say that [ A] and [ B] are equivalent over k if there exists T ∈ GLn(k) such that
B = φ(T )AT −1.
In what follows, we assume moreover that the ﬁeld k satisﬁes:
• k is a C1-ﬁeld, that is every non-constant homogeneous polynomial P over k has
a nontrivial zero provided that the number of its variables i s more than its degree;
• k is the only ﬁnite algebraic diﬀerence ﬁeld extension of k.
All the above mentioned examples (S,Q,M,E) satisfy these tw o conditions, see [ Hen97,
Hen98, DR15, Roq18]. Note that in the q-diﬀerence case, the ﬁeld ( C(z), φ) is a diﬀerence
ﬁeld but there are nontrivial ﬁnite algebraic diﬀerence ﬁeld extensions. For instance
C(z1/2)|C(z) is of degree two and we may extend φ on it with φ(z1/2) = q1/2z1/2. This is
the reason why we consider C(z1/∗) instead of C(z) in that setting. Similar considerations
occur in the elliptic case.
We recall that C := Ck is by hypothesis algebraically closed and the characterist ic
of k is zero. The following statement will be crucial in what foll ows. See [ VdPS97,
Propositions 1.20 and 1.21], see also [ DR15, Theorem 2.4].
Theorem 2.1. Let G ⊂ GLn(C) be the diﬀerence Galois group over (k, φ) of (2.1). Then,
the following properties hold:
• G/G0 is ﬁnite and cyclic, where G0 is the identity component of G;
• there exists B ∈ G(k) such that (2.1) is equivalent to φY = BY over k.
Let ~G be an algebraic subgroup of GLn(C) such that A ∈ ~G(k). The following properties
hold:
• G is conjugate to a subgroup of ~G;
• any minimal element in the set of algebraic subgroups ~H of ~G for which there
exists T ∈ GLn(k) such that φ(T )AT −1 ∈ ~H(k) is conjugate to G;
• G is conjugate to ~G if and only if, for any T ∈ ~G(k) and for any proper algebraic
subgroup ~H of ~G, one has that φ(T )AT −1 /∈ ~H(k).
In practice, to compute the diﬀerence Galois group, we are goi ng to compute a gauge
transformation such that the transformed system lies in G(k). This leads to the following
deﬁnition.
Deﬁnition 2.2. Let G ⊂ GLn(C) be the diﬀerence Galois group over (k, φ) of the system
(2.1). We say that the system (2.1) is in reduced form (or reduced) when A ∈ G(k).
Given a diﬀerence system φ(Y ) = AY and an integer ℓ /greaterorequalslant1, we can iterate it:
(2.3) φℓ(Y ) = A[ℓ]Y, where A[ℓ] = φℓ−1(A) × · · · × A .
Let G[ℓ] be the diﬀerence Galois group of the system ( 2.3). The following lemma may
be deduced from the proof [ DHR21, Proposition 4.6] in the particular case where the
parametric operator is the identity, and is proved in [ ADH21, Proposition 4.10]. It
compares the Galois groups G[ℓ], ℓ /greaterorequalslant1.
Lemma 2.3. For all ℓ /greaterorequalslant1, G[ℓ] has the same connected component of the identity as G.
Furthermore, there exists ℓ0 /greaterorequalslant1, such that G[ℓ0] is the connected component of the identity
of G.
6 THOMAS DREYFUS AND MARINA POULET
2.2. Factorisations of diﬀerence operators. In this subsection, we focus on the reducible
diﬀerence operators and make the relation with the reducible Galois groups and the Riccati
equation. Let G be an algebraic subgroup of GL n(C). We say that G is reducible if there
exists a non trivial vector subspace V of C n such that for all σ ∈ G, σ(V ) ⊂ V . We say
that G is irreducible otherwise.
The following lemma relates the irreducibility of the diﬀere nce Galois group with the
factorisation of the diﬀerence operator, see [ ADH21, Lemma 4.4].
Lemma 2.4. Let G ⊂ GLn(C) be the diﬀerence Galois group of (2.1). Then, G is reducible
with a nontrivial invariant space of dimension 0 < m < n , if and only if there exists
T ∈ GLn(k), A1 ∈ GLm(k), and A2, A3 matrices of convenient size, such that
φ(T )AT −1 =
(
A1 A2
0 A3
)
.
If we consider the diﬀerence system [AL] attached to (2.2), then its diﬀerence Galois group
is reducible with A1 ∈ GLm(k) if and only if L admits a nontrivial right factor of order
m.
Thus, to determine whether G is irreducible or not, we have to determine whether the
diﬀerence operator L deﬁned in ( 2.2) admits a nontrivial right factor or not. For right
factors of order one, we have the following criterion.
Lemma 2.5 (Lemma 2 in [ ABPS21]). Let L be the diﬀerence operator deﬁned in (2.2). The
operator of order one φ − α is a right factor of L if and only if
n∑
i=0
ai
i−1∏
j=0
φj(α) = 0 .
Although the above equation, called the Riccati equation, i s nonlinear it might be solved
in some situations we are going to describe later.
When L has order two, it admits a nontrivial factor if and only if it a dmits a nontrivial
right factor of order one.
When L has order three, it admits a nontrivial factor if and only if i t admits a nontrivial
factor of order one. The latter may be either a right or a left f actor. Let us see how
we can pass from left factor to right factor. We deﬁne the dual M ∨ of an operator
M =∑ n
i=m aiφi ∈ k
⟨
φ, φ−1⟩
by
M ∨ :=
n∑
i=m
φ−i(ai)φ−i.
By linearity, if M1, M2 ∈ k
⟨
φ, φ−1⟩
, we can check that
(M1M2)∨ = M ∨
2 M ∨
1 .
Hence, an operator has a left factor of order one if and only if its dual has a right factor
of order one. So we will focus on right factors of order one.
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 7
Remark 2.6. Assume n > 1 and that L admits a right factor of order one so let us write
L as ~L(φ − α) where α ∈ k and ~L ∈ k
⟨
φ, φ−1⟩
has order n − 1. Let y1 be a solution of
Ly = 0 such that φ(y1) ⁄= αy1 and let y2 := φ(y1) − αy1. By construction y2 ⁄= 0 is a
solution of ~Ly = 0. If Y :=
(
y1, y2, . . . , φn−2(y2)
)t then φ(Y ) = ~AY where
~A :=


α 1 0 · · · 0
0
... A~L
0

 .
Thus, the companion system associated with Ly = 0 is equivalent to the system [~A].
Furthermore, A~L is a companion matrix associated with ~L.
