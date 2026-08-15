---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-018-42-projection-on-functions-on-young-diagrams-of
section_title: "Projection on functions on Young diagrams of size n"
section_number: 4.2
pages: 32-37
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
⋆ is a
subalgebra of the algebra of functions on all Young diagrams. The latter has a natu-
ral projection map ϕn onto F(Yn, Q), the algebra of functions on Young diagrams
of size n. As Jack symmetric functions Jλ form a basis of the symmetric func-
tion ring, the functions (θµ)µ⊢n form a basis of F(Yn, Q) (see [Fér12, Proposition
4.1]).
We consider the structure constants cµ,ν;π of F(Yn, Q) with basis (θµ)µ⊢n, that
is the numbers uniquely deﬁned by:
(18) θµ(λ) · θν(λ) =
∑
π⊢n
cµ,ν;π θπ(λ) for all λ ⊢ n.
Note that cµ,ν;π depends on α, but, according to our convention, we omit the su-
perscript, when it does not bring any confusion. It is import ant to keep in mind
that the c’s are indexed by triples of partitions of the same size, while the g’s are
indexed by any triple of partitions.
It turns out that the quantities cµ,ν;π can be expressed in terms of the quantities
gµ,ν;τ . To explain that, for any partitionµ, let ˜µ denotes the partition obtained from
µ by erasing all parts equal to 1. Fix two partitions µ and ν of the same integer n;
then
Ch˜µ · Ch˜ν =
∑
τ
g˜µ,˜ν;τ Chτ .
But using the deﬁnition of Ch from Section 1.4.1, this implies that, for all λ ⊢ n,
one has:
α− |µ|−ℓ(µ)
2 z˜µ θµ(λ) · α− |ν|−ℓ(ν)
2 z˜ν θν(λ)
=
∑
τ,
|τ |≤n
g˜µ,˜ν;τ α
|τ |−ℓ(τ )
2 zτ
(n − |τ | + m1(τ )
m1(τ )
)
θτ 1n−|τ |(λ).
Every partition τ with |τ | ≤ n can be written uniquely as ˜π1i where π is a partition
of n and i ≤ m1(π). Denoting
d(µ, ν; π) := |µ| − ℓ(µ) + |ν| − ℓ(ν) − (|π| − ℓ(π)),
one has
θµ(λ) · θν(λ) = αd(µ,ν;π)/2
z˜µz˜ν
∑
π⊢n

 ∑
0≤i≤m1(π)
g˜µ,˜ν;˜π1i · z˜π · i! ·
(n − |˜π|
i
) 
 θπ(λ).
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 33
As this holds for all partitions λ of n, by deﬁnition of structure constants, we have:
(19) cµ,ν;π = αd(µ,ν;π)/2
z˜µz˜ν
∑
0≤i≤m1(π)
g˜µ,˜ν;˜π1i · z˜π · i! ·
(n − |˜π|
i
)
.
Using Theorem 1.4 with deg3, we know that g˜µ,˜ν;˜π1i is a polynomial of degree at
most d(µ, ν; π) − i. We have thus proved the following result:
Proposition 4.1. Let µ, ν and π be three partitions without parts equal to1. Then,
α−d(µ,ν;π)/2cµ1n−|µ|,ν1n−|ν|;π1n−|π| is a polynomial in n and γ with rational coefﬁ-
cients, of total degree at most d(µ, ν; π).
Moreover, seen as a polynomial inγ, it has the same parity as d(µ, ν; π).
Corollary 4.2. The quantity cµ1n−|µ|,ν1n−|ν|;π1n−|π| is a polynomial in n and α.
Moreover, it has degree at most d(µ, ν; π) in n and at most d(µ, ν; π) in α (the
total degree may be bigger).
Applications of these statements are given in next section a s well as in appen-
dix B.
5. S PECIAL VALUES OF α AND POLYNOMIAL INTERPOLATION
5.1. Case α = 1 : symmetric group algebra. In the case α = 1 , the structure
constants considered in the previous section are linked wit h the symmetric group
algebra. Let Sn denote the symmetric group of size n, i.e. the group of permu-
tations of the set [n] := {1, . . . , n}. Recall that the cycle-type of a permutation
σ ∈ Sn is the integer partition µ ⊢ n obtained by sorting the lengths of the cycles
of σ. We consider the group algebra Q[Sn] of Sn over the rational ﬁeld Q. Its
center Z(Q[Sn]) is spanned linearly by the conjugacy classes, that is the elements
Cµ =
∑
σ∈Sn,
cycle-type(σ)=µ
σ.
By a classical result of Frobenius (see [Fro00] or [Mac95, (I,7.8)]), for any λ ⊢ n,
Trρλ(Cµ)
dimension of ρλ = θ(1)
µ (λ),
where ρλ is the irreducible representation of the symmetric group associated to the
Young diagram λ. In other words: θ(1)
µ is the image of Cµ by the abstract Fourier
transform, which is an algebra morphism. Hence, the structu re constants of the
algebra Z(Q[Sn]) with the basis (Cµ)µ⊢n coincide with c(1)
µ,ν;π.
These structure constants have been widely studied in the last ﬁfty years in alge-
bra and combinatorics (they count some families of graphs embedded in orientable
surfaces). A famous result in this topic is due to Farahat and Higman [FH59, The-
orem 2.2]: the quantity c(1)
µ1n−|µ|,ν1n−|ν|;π1n−|π| is a polynomial in n. Note that this
is a consequence of Proposition 4.1.
34 M. DOŁ ˛ EGA AND V . FÉRAY
Besides, structure constants of the center of Z(Q[Sn]) have a well-known and
obvious combinatorial interpretation.
Lemma 5.1. Let µ, ν and π be three partitions of the same integer n. Fix a per-
mutation σ of cycle-type π. Then c(1)
µ,ν;π is the number of pairs of permutations
(σ1, σ2), such that σ1 has cycle-type µ, σ2 has cycle-type ν and σ1 · σ2 = σ.
This can be used to computec(1)
µ,ν;π in some particular cases, which will be useful
later.
Lemma 5.2. We have the following identities:
(1) c(1)
µ,ν;1n = 0 for any µ ⁄= ν;
(2) c(1)
(k1n),(k1n);(1k+n) =
(k+n
k
)
(k − 1)!.
Proof. Consider the ﬁrst item. The only permutationπ of cycle type(1n) is σ = id.
Hence, the condition σ1 · σ2 = σ corresponds to σ2 = σ−1
1 and in particular σ1 and
σ2 must have the same cycle-type.
Consider now the second item. As before, we must chooseσ = id. As σ2 = σ−1
1
has always the same cycle-type as σ1, the coefﬁcient c(1)
(k1n),(k1n);(1k+n) is simply
the number of permutations of k + n of type (k1n). This is well-known [Sag01,
equation (1.2)] to be
(k + n)!
z(k1n)
=
(k + n
k
)
(k − 1)!. □
Remark. The quantities g(1)
µ,ν;π also have a direct combinatorial interpretation in
terms of partial permutations, see [IK99].
5.2. Case α = 2 : Hecke algebra of (S2n, Hn). An analogous interpretation of
the structure constants exists in the case α = 2 . We explain it here, following the
development given in [GJ96b].
We can view the elements of the symmetric group S2n as permutations of the
following set: {1, ¯
1, . . . , n,¯n}. A subgroup formed by permutations σ such that
σ(i) = σ(i) for i ∈ {1, . . . , n},
where by convention ¯j = j, is called hyperoctahedral groupand is denoted by Hn.
We consider the subalgebra Q[Hn\S2n/Hn] < Q[S2n] of the elements invariant
by multiplication on the left or on the right by any element of Hn; in other words
x ∈ Q[Hn\S2n/Hn]
def
⇐ ⇒ hxh′ = x for all h, h′ ∈ Hn.
A non-trivial result is that this algebra is commutative.
The equivalence classes for the relationx ∼ hxh′ (for x ∈ S2n and h, h′ ∈ Hn)
are called double-cosets. They are naturally indexed by partitions ofn, see [Mac95,
(VII,2)]. We denote by C(2)
µ ∈ Q[Hn\S2n/Hn] the sum of all elements in the dou-
ble coset corresponding to µ. The family (C(2)
µ )µ⊢n is a basis of Q[Hn\S2n/Hn].
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 35
One can show (see [GJ96b, Equation (3) and (5)]) that there exist some orthog-
onal idempotents Eλ such that:
C(2)
µ = 2 nn!
∑
λ⊢n
θ(2)
µ (λ) Eλ,
and one has
C(2)
µ · C (2)
ν = (2nn!)2∑
λ⊢n
θ(2)
µ (λ) θ(2)
ν (λ) Eλ
= (2nn!)2∑
π⊢n
∑
λ⊢n
c(2)
µ,ν;π θ(2)
π (λ) Eλ = (2nn!)
∑
π⊢n
c(2)
µ,ν;π C(2)
π .
Hence, the structure constants hµ,ν;π of the algebra Q[Hn\S2n/Hn] for the basis
(C(2)
µ )µ⊢n are, up to a factor 2nn!, the same as the ones of the algebra F(Yn, Q)
with the basis (θ(2)
µ )µ⊢n.
In particular, Proposition 4.1 implies the following, result, which is an analog of
Farahet and Higman’s result [FH59] (a combinatorial proof o f the polynomiality
has recently been given by O. Tout in [Tou13]).
Proposition 5.3. Let µ, ν and π be partitions without parts equal to 1. The renor-
malized structure constant of the algebra Q[Hn\S2n/Hn]
hµ1n−|µ|,ν1n−|ν|;π1n−|π|
n! 2n √
2
d(µ,ν,π)
is a polynomial in n of degree at most d(µ, ν, π). Moreover, its coefﬁcient of
nd(µ,ν,π) is the same as in c(1)
µ1n−|µ|,ν1n−|ν|;π1n−|π|. In particular,
• when |µ| − ℓ(µ) + |ν| − ℓ(ν) = |π| − ℓ(π), one has
hµ1n−|µ|,ν1n−|ν|;π1n−|π|
n! 2n = c(1)
µ1n−|µ|,ν1n−|ν|;π1n−|π|
and this quantity is independent of n ;
• when |µ| − ℓ(µ) + |ν| − ℓ(ν) = |π| − ℓ(π) − 1,
hµ1n−|µ|,ν1n−|ν|;π1n−|π|
n! 2n
is independent of n.
Proof. The claim that the renormalized structure constant mention ed above is a
polynomial and the bound on its degree follow from Proposition 4.1 specialized to
α = 2. The dominant coefﬁcient is a polynomial in γ of degree 0, so it is the same
for γ ∈ {0, −1/
√
2}, that is α ∈ {1, 2}. The ﬁrst item follows immediately.
In the second item, we consider the case d(µ, ν, π) = 1 . So,
hµ1n−|µ|,ν1n−|ν|;π1n−|π|
n! 2n √
2
36 M. DOŁ ˛ EGA AND V . FÉRAY
is an afﬁne function of n with the same linear coefﬁcient as c(1)
µ1n−|µ|,ν1n−|ν|;π1n−|π|.
But the latter is identically equal to0. Indeed, the fact that the sign of permutations
is a group morphism implies that
c(1)
µ1n−|µ|,ν1n−|ν|;π1n−|π| = 0
whenever d(µ, ν; π) is odd. □
Besides, Goulden and Jackson [GJ96b] described the coefﬁcients hµ,ν;π combi-
natorially. Let FS be the set of all (perfect) matchings on a set S, that is partitions
of S in pairs. When S is the set {1, 2 . . . ,2n}, we also denote FS by Fn.
For F1, F2 ∈ F S, let G(F1, F2) be the multigraph with vertex-set S whose
edges are formed by the pairs in F1, . . . , Fk. Because of the natural bicoloration of
the edges, the connected components of G(F1, F2) are cycles of even length. Let
the list of their lengths in weakly decreasing order be (2θ1, 2θ2, . . .) = 2 θ, and
deﬁne Λ by Λ( F1, F2) = θ.
Lemma 5.4 ([GJ96b, Lemma 2.2.]). Let F1, F2 be two ﬁxed matchings in Fn such
that Λ( F1, F2) = π, where π ⊢ n. Then, for any µ, ν ⊢ n we have
hµ,ν;π = 2nn!|{F3 ∈ Fn : Λ( F1, F3) = µ, Λ( F2, F3) = ν}|.
In particular
c(2)
µ,ν;π = |{F3 ∈ F n : Λ( F1, F3) = µ, Λ( F2, F3) = ν}|.
From this lemma one can evaluate some special cases of struct ure constants
which will be helpful in the next subsection.
Lemma 5.5. We have the following identities:
(1) c(2)
µ,ν;1n = 0 for any µ ⁄= ν;
(2) c(2)
(k1n),(k1n);(1k+n) =
(k+n
k
)
2k−1(k − 1)!.
Proof. The ﬁrst item is immediate from Lemma 5.4, since wheneverF1 and F2 are
matchings such that Λ( F1, F2) = 1 n then clearly F1 = F2.
Let F1, F2 be two ﬁxed matchings such that Λ( F1, F2) = (1 k+n) (hence F1 =
F2). We are looking for the number of matchings F3 such that Λ( F1, F3) =
Λ( F2, F3) = ( k1n). Of course, as F1 = F2, it is the number of matchings F3
with Λ( F1, F3) = ( k1n). This number does not depend on F1. Using [F ´S11,
Lemma 2.4], we know that the numbers of pairs (F, F3) with Λ( F, F3) = ( k1n) is
given by
(2n + 2k)!
z(k1n)2n+1 .
As there are (2n+2k)!
2n+k(n+k)! matchings in Fn+k, that is possible values for F , for a
ﬁxed F1, the number of matchings F3 with Λ( F1, F3) = ( k1n) is
2n+k(n + k)!
z(k1n)2n+1 =
(k + n
k
)
2k−1(k − 1)!. □
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 37
