---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-001-maximal-tori-in-classical-groups
section_title: "Maximal tori in classical groups"
section_number: 2
pages: 2-5
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
---
In this section we establish the existence of regular semisimple ℓ-singular elements in suitable tori of
classical groups of Lie type. This will be a main ingredient in the proof of the vanishing Theorem 1.
Moreover, we formulate a criterion for collections of maximal tori of simple algebraic groups not to be
contained in a common proper reductive subgroup.
2.1. Weyl groups and maximal tori in symplectic and orthogonal groups. For a prime power
q and K = Fq we consider the natural representation of G = Sp2n (K) on V = K 2n (case Cn ) and of
G = SO2n+1 (K) on V = K 2n+1 , and a Steinberg morphism F on G with fixed point group GF = Sp2n (q),
respectively GF = SO2n+1 (q). With respect to an appropriate choice of basis of V we can assume (see
[13, Exmp. 6.7]) that the subgroup T of diagonal matrices forms an F -stable maximal torus of G, its
−1
−1
−1
elements have the form diag(t1 , . . . , tn , t−1
n , . . . , t1 ), respectively diag(t1 , . . . , tn , 1, tn , . . . , t1 ), and F
acts by raising the diagonal entries to their q-th power. The Weyl group W acts on T by its natural
permutation action on the diagonal entries. More precisely, W is isomorphic to the wreath product
C2 ≀ Sn , where the cyclic groups of order 2 interchange the entries {ti , t−1
i }, i = 1, . . . , n, while the
symmetric group permutes the n pairs {ti , ti−1 }. See [5, Chap. 15] for more details.
The GF -conjugacy classes of F -stable maximal tori of G are parameterised by the conjugacy classes
of W . An element t ∈ T is conjugate to an element t′ ∈ GF if w F (t) = t for some w ∈ W . Then t′ lies


MURNAGHAN–NAKAYAMA RULE FOR UNIPOTENT CHARACTERS

3

in an F -stable maximal torus parameterised by the class of w. Such an element t′ is regular semisimple
if w is unique.
The conjugacy classes of W are parameterised by pairs of partitions (λ, µ) ⊢ n of n as follows: If
w ∈ W permutes entries of a regular diagonal element as above, then a cycle containing entries ti and t−1
i
for some i is of even length 2µj and contributes a part µj to µ. Otherwise a cycle of length λj permutes
some diagonal entries and there is another cycle of the same length permuting the inverse diagonal entries
in the same way; this contributes a part λj to λ.
We can embed an even dimensional orthogonal group G = SO2n (K) (type Dn ) into G̃ = SO2n+1 (K)
such that it is stable under the Steinberg morphism of G̃ and its fixed points are GF = SO+
2n (q). There
−
′
F′
is a second Steinberg morphism F on G leading to the twisted groups G = SO2n (q). The Weyl group
W of G is a subgroup of index 2 in the Weyl group W̃ of G̃, consisting of the conjugacy classes of W̃
whose parameter (λ, µ) has an even number of parts in µ. If µ is empty in (λ, µ) and λ has only even
parts then the corresponding class in W̃ splits into two classes in W , called degenerate classes. The
twisted Steinberg morphism F ′ acts on W like conjugation by the short root generator of W̃ . This way
the F ′ -conjugacy classes of W can be parameterised by the conjugacy classes of W̃ whose parameter
(λ, µ) has an odd number of parts in µ. Since G and G̃ have the same rank, maximal tori of G are also
maximal tori of G̃.
Let (λ, µ) = ((λ1 , . . . , λr ), (µ1 , . . . , µs )) ⊢ n. Then the order of the corresponding maximal torus TF
in GF is
s
r
Y
Y
(q λi − 1) (q µi + 1)
|TF | =
i=1

i=1

and TF contains cyclic subgroups of orders q λi − 1 and q µi + 1 for all i.
2.2. Regular semisimple elements. We need to know that certain maximal tori contain regular elements. As before, let q be a prime power. For a prime ℓ not dividing q we denote by dℓ (q) the order of q
modulo ℓ, that is the smallest d ≥ 1 with ℓ | (q d − 1). If d is even then we have ℓ | (q d/2 + 1). With these
definitions, ℓ | (q k − 1) if and only if d | k, and for even d we have ℓ | (q k + 1) if and only if k is an odd
multiple of d/2.
Lemma 2.1. Let G be a simple simply-connected classical group of type Bn , Cn or Dn defined over the
finite field Fq with corresponding Steinberg morphism F .
Let (λ, µ) = ((λ1 , . . . , λr ), (µ1 , . . . , µs )) be a pair of partitions of n, and T a corresponding F -stable
maximal torus of G. Then TF contains regular elements if one of the following conditions is fulfilled.
(1) q > 3, λ1 < λ2 < . . . < λr and µ1 < µ2 < . . . < µs ;
(2) q ∈ {2, 3}, λ1 < λ2 < . . . < λr , µ1 < µ2 < . . . < µs , all λi 6= 2, and if G is of type Bn or Cn
then also all λi 6= 1; or
(3) G is of type Dn , 2 < λ1 < λ2 < . . . < λr and 1 = µ1 = µ2 < µ3 < . . . < µs .
Proof. (a) We use the natural representations of G̃ = Sp2n (K) and G̃ = SO2n+1 (K) with the natural
Steinberg morphism that raises matrix entries to their q-th power, and we consider SO±
2n (q) as subgroups
of SO2n+1 (K).
We have described the maximal torus T of diagonal elements in G̃ in Section 2.1. The connected
◦
(t) of t ∈ T equals T if and only if α(t) = 1 for all roots α of G with respect to T.
centraliser CG̃
These roots are explicitly given in [5, Chap. 15] (for types Cn and Dn , but type Bn is very similar): It is
enough to describe a set of positive roots. Their values on t = diag(t1 , t2 , . . . , tn , tn−1 , . . . , t−1
1 ) respectively
−1
)
are
t = diag(t1 , t2 , . . . , tn , 1, t−1
,
.
.
.
,
t
n
1
(Types Bn , Cn , Dn ) α(t) = ti t−1
and α(t) = ti tj for 1 ≤ i < j ≤ n,
j
(Type Bn only) α(t) = ti for 1 ≤ i ≤ n,


4

FRANK LÜBECK AND GUNTER MALLE

(Type Cn only) α(t) = t2i for 1 ≤ i ≤ n.
◦
So, CG̃
(t) = T if and only if for all 1 ≤ i < j ≤ n we have ti 6= tj and ti 6= t−1
j , and in type Bn we
also have ti 6= 1 for 1 ≤ i ≤ n, and in type Cn we also have ti 6= ±1 for 1 ≤ i ≤ n.
(b) In type Cn we have G = G̃, while in types Bn and Dn the groups SO2n+1 (K) and SO2n (K) are
not simply-connected. But there are isogenies from the simply-connected coverings G = Spinm (K) →
SOm (K) = G̃. If q is even, that is char(K) = 2, then this map has a trivial kernel and induces
±
isomorphisms Spin±
m (q) → SOm (q). For odd q the kernel is a central subgroup of order 2, and the image
±
of the induced map Spinm (q) → SO±
m (q) of the finite groups has index 2.
To show the existence of regular elements in tori of type (λ, µ) we construct a t ∈ T such that w F (t) = t
◦
for some w ∈ W in the class (λ, µ) and CG̃
(t) = T. In cases Bn and Dn and odd q this t will be a square of
wF
another element in T
such that in all cases t has a preimage in a corresponding twisted maximal torus
of the simply-connected group G. This preimage is regular because centralisers of semisimple elements
in a simply-connected group are connected.
(c) Now let (λ, µ) = ((λ1 , . . . , λr ), (µ1 , . . . , µs )) ⊢ n be a pair of partitions. We construct t ∈ T by
describing the entries t1 , . . . , tn ∈ K.
First assume that G is of type Cn or that q is even.
λi −1
For 1 ≤ i ≤ r let ai ∈ Fqλi be of order q λi − 1 and use ai , aqi , . . . , aiq
as entries of t (note that
aqi

λi

= ai ).

For 1 ≤ j ≤ s let bj ∈ Fq2µj be of order q µj + 1 and use bj , bqj , . . . , bjq

µj −1

as entries of t (note that then

µj
bqj = b−1
j ).

If G is of type Bn or Dn and q is odd, we use as t the square of the element just described (so ai is of
order 12 (q λi − 1) and bj is of order 21 (q µj + 1)).
It is clear from this construction that the Steinberg morphism F of Sp2n (K), respectively SO2n+1 (K)
permutes the entries of t such that this can be reversed by an element w ∈ W of cycle type (λ, µ), so
t = w F (t).
(d) We next discuss when t fails to be regular. Let λi , µj > 0 with q λi − 1 = q µj + 1. Then µj < λi
and the assumption is equivalent to q µj (q λi −µj − 1) = 2. It follows that q = 2, µj = 1 and λi = 2.
(e) Let k ∈ Z, 0 < k < λi and assume (q λi − 1) | (q k ∓ 1). Then q λi − 1 ≤ q k ∓ 1, which holds if and
only if q k (q λi −k − 1) ≤ 0 or 2, respectively. This is only possible for q = 2, k = 1 and λi = 2. Similarly,
for odd q the condition 21 (q λi − 1) | (q k ∓ 1) implies q = 3, k = 1 and λi = 2.
Now let k ∈ Z, 0 < k < µj . A similar argument as above shows that for all q we have (q µj +1) ∤ (q k ∓1)
and for odd q we also have 12 (q µj + 1) ∤ (q k ∓ 1).
(f) Now we prove assertions (1) and (2) of the statement by showing that in those cases the element
t ∈ T constructed in (c) does not lie in the kernel of any root.
First note that the ai (1 ≤ i ≤ r) and bj (1 ≤ j ≤ s) have pairwise different orders. This follows
from (d) since for q = 2 we assume that all λi 6= 2.
λi −1
According to (a) we need to show that for 1 ≤ i ≤ r any of the entries (ai , aqi , . . . , aiq
) are not equal
or inverse to each other, and similarly for the (bj , bqj , . . . , bjq

µj −1

). Since the map x 7→ xq permutes these
k

entries of t and their inverses it suffices to show that for 0 < k < λi we have aqi 6= a±1
(equivalently
i
k

k

aqi ∓1 6= 1), and similarly for the bj . Now aqi ∓1 = 1 implies (q λi − 1) | (q k ∓ 1) or 12 (q λi − 1) | (q k ∓ 1),
respectively. Using (e) this implies λi = 2 and q ∈ {2, 3}, contradicting the assumptions.
k
Similarly, step (e) shows that we always have bqj 6= b±1
for 0 < k < µj .
j
For type Cn we also have to show that a2i 6= 1 (1 ≤ i ≤ r) and b2j 6= 1 (1 ≤ j ≤ s). This holds because
a2i = 1, i.e., (q λi − 1) | 2, implies λi = 1 and q ∈ {2, 3}, contradicting the assumption. Note that always
q µi + 1 > 2.


MURNAGHAN–NAKAYAMA RULE FOR UNIPOTENT CHARACTERS

5

For type Bn we also have to show that ai 6= 1 (1 ≤ i ≤ r) and bj 6= 1 (1 ≤ j ≤ s). This follows as
q λi − 1 = 1 implies q = 2 and λi = 1, while 12 (q λi − 1) = 1 implies q = 3 and λi = 1 for odd q, and as
always q µj + 1 > 1.
(g) The argument for statement (3) is very similar. A suitable element t can be defined as before,
except that for µ1 = 1 we choose b1 = 1. Then the entry for µ2 = 1 has order q + 1 for even q or 21 (q + 1)
for odd q which is always larger than 1.

Remark 2.2. Let G be a connected reductive group with Steinberg morphism F and T an F -stable
maximal torus of G. Let ℓ be a prime dividing |TF |. If TF contains a regular element then TF also
contains an ℓ-singular regular element.
Proof. Let t ∈ TF be an ℓ-regular (that is of order prime to ℓ) regular element and u ∈ TF be any
element of order ℓ. Then tu has order ℓ|t| and some power of tu equals t, hence tu is also regular.

2.3. Maximal connected reductive subgroups. The following lemma will allow us to decide if a
collection of classes of maximal tori of a classical group has representatives inside the centraliser of a
semisimple element:
Lemma 2.3. Let G be a simple algebraic group of classical type Bn , Cn (with n ≥ 2) or Dn (with n ≥ 4)
with Frobenius endomorphism F such that GF is a classical group. Let Λ be a set of pairs of partitions
(λ, µ) ⊢ n. Assume the following:
(1) there is no 1 ≤ k ≤ n − 1 such that all (λ, µ) ∈ Λ are of the form (λ1 , µ1 ) ⊔ (λ2 , µ2 ) (that is λ
contains the parts from λ1 and λ2 and similarly for µ) with (λ1 , µ1 ) ⊢ k;
(2) the greatest common divisor of all parts of all (λ, µ) ∈ Λ is 1; and
(3) if G is of type Bn , then there exist pairs (λ, µ) ∈ Λ for which µ has an odd number of parts, and
for which µ has an even number of parts.
If s ∈ GF is semisimple such that CG (s) contains maximal tori of G corresponding to all (λ, µ) ∈ Λ then
s is central.
Proof. The types of maximal tori are insensitive to isogeny types, so we may assume that G is a classical
◦
matrix group Sp(V ) or SO(V ). Let s ∈ GF be a non-central semisimple element. Then H := CG
(s) fixes
each eigenspace of s on V . Since s is non-central it has at least two different eigenvalues. Since s is F stable, the eigenspaces of s are permuted under the action of F . First assume that the set of eigenspaces
forms one orbit, of length f > 1 say, under the action of F . Then H is a central product of isomorphic
classical groups, HF is an extension field subgroup and hence its maximal tori have parameters all parts
of which are divisible by f , contradicting (2).
So there are at least two F -orbits of eigenspaces. Let V1 < V be an F -stable sum of eigenspaces of
minimal possible dimension. Then either V1 ∩ V1⊥ 6= 0 or V1 is non-degenerate and V = V1 ⊥ V1⊥ . The
stabilisers of totally singular spaces are contained in maximal parabolic subgroups [13, Prop. 12.13], but
these only have tori of types as excluded by (1). Else, H is contained in the stabiliser of V1 ⊥ V1⊥ , a
central product of classical groups. The latter are of types Ca + Cb , respectively Ba + Db or Da + Db with
a + b = n, a, b > 0 for G of type Cn , respectively Bn , Dn . Then the parameters of F -stable maximal
tori of H are of the form excluded by (1) of the lemma, for k = a, unless G is of type Bn and V1 is
1-dimensional, when H could be of type Dn . In that case, the number of parts in the second entry of the
parameters of F -stable maximal tori of H all have a fixed parity (namely even for HF untwisted, and
odd for HF twisted). This is excluded by (3).

