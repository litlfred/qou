---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-021-a3-quantum-cohomology-ring-of-the-grassmannian
section_title: "A.3. Quantum cohomology ring of the Grassmannian"
section_number: null
pages: 62-64
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
of Gk,n is an enrichment of H∗(Gk,n) that counts more broadly maps from P1(C) to Gk,n with
prescribed values at speciﬁc points rather than intersection of subvarieties of Gk,n. Refer to [5, 6]
for a general introduction to the small quantum cohomology. Note that one can generally deﬁne
two quantum cohomologies for a given projective variety: the big quantum cohomology and the
small one. In this paper we will only be interested in the small quantum cohomology which is much
easier to handle, and we will simply drop the term small in the sequel (see [33] for an introduction
to the big quantum cohomology). Denote by Hol(Gk,n) the set of rational maps from P1(C) to
Gk,n. We deﬁne the degree of a map f∈Hol(Gk,n) as
degf = #f−1
(
ΩW
(1)
)
,
and we can show this is independent of a generic choice of W . We denote by Hold(Gk,n) the
space of rational maps from P1(C) to Gk,n of degree d. The latter is a quasi-projective variety
(i.e, an open subset of a projective variety) of dimension k(n−k) +dn whose closure yields a
projective variety Hold(Gk,n). Note that other compactiﬁcations of Hold(Gk,n) can be achieved
with better smoothness, see [5]. The choice of compactiﬁcation will not play any role here, since we
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 63
will study intersection of subvarieties of Hold(Gk,n) which are generically located in Hold(Gk,n).
Fora∈ P1(C), λ∈ Λk,n and W∈ W, denote by VW
a,λ the subvariety
VW
a,λ =
{
f∈Hold(Gk,n), f(a)∈ ΩW
λ
}
.
Then, VW
a,λ is a subvariety of Hold(Gk,n) of dimension nd +k(n−k)−⟨λ⟩.
Deﬁnition A.2 ([5]). The quantum cohomology ring QH(Gk,n) is the vector space C[q]⊗H∗(Gk,n)
with the multiplication
(62) ( qkσλ)· (qk′
σµ) =qk+k′ ∑
d≥0,ν∈Λk,n
⟨λ,µ,ν c⟩dqdσν,
where⟨λ,µ,ν c⟩d = 0 if⟨λ⟩ +⟨µ⟩ +⟨νc⟩⁄ =k(n−k) +nd, and otherwise
⟨λ,µ,ν⟩d = #
(
VW
0,λ∩VW′
1,µ ∩VW′′
∞,ν
)
.
Remark that d = 0 corresponds to constant maps on Gk,n and we recover with ⟨λ,µ,ν c⟩0 the
intersection numbers given in the previous paragraph. The fact that the multiplication is indeed
an associative product on C[q]⊗H∗(Gk,n) is a highly nontrivial property. This associativity is
however crucial for enumerative properties of the quantum cohomology ring. Indeed, for any
p≥ 2,λ 1,...,λ p∈ Λk,n, then we have in QH(Gk,n)
(63) σλ1...σ λp =
∑
d≥0,λc
p+1∈Λk,n
⟨λ1,...,λ p+1⟩dqdσλc
p+1,
where⟨λ1,...,λ p+1⟩d = 0 if∑p+1
i=1⟨λi⟩⁄ =k(n−k) +dn and otherwise
⟨λ1,...,λ p+1⟩d = #
(p+1⋂
i=1
VWi
ai,λi
)
,
where a1,...,a p+1 are p + 1 generic points of P1(C) and W1,...,W p+1 are (p + 1) generic ﬂags in
W.
The algebraic structure of QH(Gk,n) has been investigated by several authors [5, 6, 15]. This
algebraic study culminated with the combinatorial description of the coeﬃcients⟨λ,µ,ν c⟩d in [15] in
terms of puzzles of the 2-steps ﬂag manifold (see also [14] for a reﬁned version). For our probabilistic
purpose, one of the most important descriptions of QH(Gk,n) is given by its algebraic presentation
QH(Gk,n)≃Sym[x1,...,x k]/⟨hi = 0,i =n−k + 1,...n − 1⟩
through the map σλ↦→sλ,q ↦→ (−1)k+1hn. This algebraic presentation can be further simpliﬁed,
see [47], as
Sym[x1,...,x k]/⟨hi = 0,i =n−k + 1,...n − 1,hn = (−1)k+1q⟩
=Sym[x1,...,x k]/⟨(x1,...,x k) =q1/k(
eit1,...e itk
)
,⃗t∈Tk,n⟩,
and then q = (−1)k+1xn
i for all 1 ≤ i≤ n. Note that the relation between both presentations of
QH(Gk,n) is not trivial.
Example A.3. Let us resume Example A.1 for k = 1, where G1,n+1 = Pn(C). Then, a rational
map h from P1(C) to Pn(C) is given by n + 1 homogeneous polynomials f1(x,y ),...,f n+1(x,y )
of same degree which don’t have any common zero. Denote by d the degree of the polynomials
fj, 1≤j≤n. Up to a generic choice of basis (e1,...,e n+1) of Pn(C), one can assume that all fj
have nonzero coeﬃcient for the monomialyd and that furthermorefn+1(0, 1)⁄= 0. Let W be the ﬂag
given by the basis (e1,...,e n+1), with Wi = Vect⟨e1,...,e i⟩. Recall then from Example A.1 that
64 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
ΩW
(1) ={[x1,...,x n, 0], (xi)1≤i≤n∈ Cn\{ 0}}. Hence, h−1(ΩW
(1)) ={[x,y ]∈ P1(C), fn+1(x,y ) = 0}.
By the choice of a generic basis, fn+1(0, 1)⁄= 0 and thus (0, 1)⁄∈ h−1(ΩW
(1)). Then, on the open
chart{x⁄= 0}, the maps h is given by
h : (1,y )↦→ [f1(1,y ),...,f n+1(1,y )],
where each fj(1,y ) are univariate polynomials of degree d. Hence,
h−1(ΩW
(1))∩{x⁄= 0} ={[1,y ], fn+1(1,y ) = 0}.
Sincefn+1(1,y ) is a degree d polynomial, the latter equation has exactly d solutions, and ﬁnally
#h−1
(
ΩW
(1)
)
=d.
Hence, we see that in the simplest case k = 1 , the degree of a holomorphic map coincides with
the algebraic degree of the map from P1(C) to Pn(C). The ring QH(G1,n+1) is then the ring of
univariate polynomials C[x], with the map σk↦→xk for 1≤k≤n and q↦→xn+1.
In the simplest case n = 1 , we can even recover a classical result. Let x1,...,x 2p+1 and
y1,...,y 2p+1 be generic elements of P(C). Each yi∈ P1(C) deﬁnes a ﬂag in C2 given by Wi ={0⊂
yi⊂ C2}. Moreover, saying that a map h∈ Hol(P1(C), P1(C)) satisﬁes f(xi) = yi exactly means
that f(xi)∈ ΩWi
(1). By (63),
σ2p
(1) =
∑
d≥0,λc
2p+1∈R1,2
2p+|λ2p+1|=2d+1
#

ΩW2p+1
λ2p+1 ∩
⋂
1≤i≤2p
VWi
xi,(1)

qdσλc
2p+1,
and by the latter description of QH(G1,2),
σ2p
(1) =qp.
Hence, the only non zero terms arise for d =p, and then λ2p+1 = (1). We deduce that there is a
unique rational map of degree p such that f(xi) =yi for generic{xi,yi}1≤i≤2p+1∈ P1(C).
