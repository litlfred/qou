---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-068-1-let-µ-be-a-composition-lµ-n-consider-the-set
section_title: "Let µ be a composition, l(µ) = n. Consider the set"
section_number: 1
pages: 76-77
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
M (µ) =
{
w =a1a2··· a|µ|| ak∈ [1,n ], #{i| ai =j} =µj
}
.
Let us deﬁne the number of inversions for a word w as
inv(w) =
∑
1≤i<j≤|µ|
χ(ai>a j).
i) Prove
∑
w∈M (µ)
qinv(w) =
[
|µ|
µ1,...µ n
]
q
. (P. MacMahon, 1914)
ii) Given w∈M (µ), let wij be the subword of w formed by deleting all letters am such
thatam⁄=i orj. For example, if w = 2411213144321∈M (5, 3, 2, 3) then w12 = 21121121,
w13 = 1113131, w14 = 41111441, w23 = 22332, w24 = 242442, w34 = 43443.
The Z-index (Zeilberger’s index) of w is deﬁned to be the sum of the major indices of
all 2-letter subwords, wij, of w. That is
Z(w) =
∑
1≤i<j≤n
Maj(wij).
Dilogarithm identities 77
Analogously, let us introduce the ~Z-index of w as follows
~Z(w) =
∑
1≤i<j≤n
~Maj(wij)−n(µ).
For our example, inv( w) = 29, Maj( w) = 47, ~Maj(w)− n(µ) = 59 − 15 = 44,
Z(w) = 12 + 10 + 8 + 4 + 7 + 5 = 46, ~Z(w) = 19 + 13 + 23 + 11 + 8 + 8 − 15 = 67.
Prove
∑
w∈M (µ)
qZ(w) =
[
|µ|
µ1,...,µ n
]
q
. (D. Zeilberger, D. Bressoud, 1985)
iii) Give a combinatorial proof of equidistribution for the sta tistics
inv, Maj and Z.
Further details and proofs one can ﬁnd in [Bre3], [ZB], [Gre] and [Han].
2. (Tensor product multiplicities and Bethe’s ansatz equatio ns).
Let µ(j) = (µ(j)
1 ≥···≥ µ(j)
n ≥ 0), 1≤j≤N , and λ be the highest weights and Vµ(j) ,
Vλ be the corresponding irreducible ﬁnite dimensional repres entations of the Lie algebra
gln.
Conjecture 5. The tensor product multiplicity
MultVλ (Vµ(1)⊗···⊗ Vλ(N ) )
is equal to the number of solutions to the following system of algebraic equations on vari-
ables v1 ={v1,1,...,v 1,m1}, v2 ={v2,1,...,v 2,m2}, ... , vn ={vn,1,...,v n,mn} (we assume
that v0 =vn+1 =φ)
N∏
j=1
vk−λ(j)
k i
vk−λ(j)
k+1i
=
∏
vk−1
vk−vk−1 +i/2
vk−vk−1−i/2
∏
v′
k⁄=vk
vk−v′
k−i
vk−v′
k +i
∏
vk+1
vv−vk+1 +i/2
vk−vk+1−i/2.
Herei =√−1. The number of equations and that of variables are the same an d are equal
tom1 +··· +mn. The relation between the weights λ andµ(1),...,µ (N) and the composition
m = (m1,m 2,...,m n) is the following
2mk−mk−1−mk+1 =
∑
l≥k+1



N∑
j=1
µ(j)
l −λl


.
