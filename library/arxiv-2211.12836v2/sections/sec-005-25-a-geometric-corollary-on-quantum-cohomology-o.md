---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-005-25-a-geometric-corollary-on-quantum-cohomology-o
section_title: "A geometric corollary on quantum cohomology of the Grassmannian"
section_number: 2.5
pages: 11-13
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
Bk,n and its convolution algebra are related to various other ﬁelds, out of which we singled out two
main ones: the Wess-Zumino-Witten models of type Ak−1 at level n, which is a particular model
of conformal ﬁeld theory, and the quantum cohomology of the Grassmannian Gk,n, which counts
rational curves with target space the space of k-dimensional vector subspaces of Cn. Those two
concepts are actually related [24, 25, 35]. Let us ﬁrst brieﬂy sketch the second one (see Appendix
A for a more detailed introduction).
Denote by Gk,n the space of k-dimensional vector subspaces of Cn. This space is a compact
manifold of dimension k(n−k) and even a projective variety, and thus we can study it from a
cohomological perspective (which roughly amounts to counts the number of 𝓁-dimensional holes in
Gk,n, 0 ≤ 𝓁≤ k(n−k)). For any ﬂag W = 0 ⊂ W1⊂···⊂ Wn = Cn there exists a natural
decomposition of Gk,n into cells ΩW
I ,I ∈Bk,n, where
ΩW
I ={V ∈Gk,n, dim(V∩Wn−Ii)≥i, 1≤i≤k},
and ΩW
I is a closed manifold of Gk,n of dimension⟨I⟩−⟨ I0⟩ called Schubert variety. An important
property of the family {ΩW
I ,I ∈ Bk,n} is that a generic submanifold M of Gk,n is completely
characterized up to homotopy by
{#(M∩ ΩW
I ), dim ΩW
I + dimM = dimGk,n},
see [23]. We are interested in the set of maps from P1(C) to Gk,n whose values at generic points
are restricted to lie on some submanifolds of Gk,n. Let Hol(Gk,n) be the set of rational maps from
P1(C) to Gk,n. We deﬁne the degree deg f of f∈Hol(Gk,n) as
degf = #{z∈ P1(C),f (z)∩H⁄=∅, H ∈Gn−k−1,n generic}.
We should understand deg f as the number of singular points of f (as the number of poles of
a rational function, which actually corresponds to the special case k = 1, n = 2, see Appendix
12 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
A). For d≥ 0, let us write Hold(Gk,n) as the space of elements of Hol(Gk,n) of degree d. Up
to some compactiﬁcation, we can again give to Hold(Gk,n) the structure of a projective variety
of dimension k(n−k) +dn. The enumerative problem related to the quantum cohomology is to
count elements of Hold(Gk,n) having prescribed singular points. Namely, ﬁx a0,...,a m+1 generic
points of P1(C) and M0,...,M m+1 m + 1 generic sub-manifolds of Cn of respective dimension
1≤d0,...,d m+1≤k(n−k). Set
Md,a0,...,am+1
M0,...,Mm+1 :={f∈Hold(Gk,n),f (ai)∈Mi, 0≤i≤m + 1}.
In general,Md,a0,...,am+1
M0,...,Mm+1 is non empty only if∑m+1
i=0 di≤ dimHold(Gk,n) =k(n−k) +dn and then
the resulting manifoldMd,a0,...,am+1
M0,...,Mm+1 has dimensionk(n−k) +dn−∑m+1
i=0 di. In the particular case
wherek(n−k)+dn =∑m+1
i=0 di,Md,a0,...,am+1
M0,...,Mm+1 is generically a discrete manifold, which can be shown
to be ﬁnite (see Section A). We address in this section the problem of counting # Md,a0,...,am+1
M0,...,Mm+1 in
the case k(n−k) +dn =∑m+1
i=0 di when there is a large number of constraints Mi. To this end, for
M a submanifold of dimension d of Gk,n, let us decompose the homology class [ M]∈Hd(Gk,n) of
M on the basis
{[
ΩW
I
]
,I ∈Bk,n
}
as
[M] =
∑
I∈Bk,n,⟨I⟩=d+⟨I0⟩
cM
I
[
ΩW
I
]
.
We then deﬁne the quantum dimension of M as
(5) qDim(M) =
∑
I∈Bk,n,⟨I⟩=d+⟨I0⟩
cM
I SI(ξn(I0)),
where SI(⃗ u) is the evaluation at ( eiu1,...,e iuk) of the Schur function associated to the partition
λI = (I1− (k− 1),...,I k) (see Appendix A for more details on Schur functions), and write pM
I =
cM
I SI(ξn(I0))
qDimM for I∈Bk,n, so that ∑
I∈Bk,npM
I = 1 by (5). Then, introduce for a = 2, 3 the statistic
‖M‖a = 1
qDim(M)
∑
I∈Bk,n,⟨I⟩=d+⟨I0⟩
pM
I
k∑
j=1
(Ij− (d +⟨I0⟩)/k)a.
In the following statement, we write Ic for the dual conﬁguration Ic = (n− 1−Ik+1−j)1≤j≤k of
I∈Bk,n.
Corollary 2.7. LetM0,M 1,...,M m+1 be generic sub-manifolds of Gk,n having respective dimen-
sion d0,...,d m+1 and d≥ 0 such that ∑m+1
i=0 di =k(n−k) +dn. Then, for generic a0,...,a m+1∈
P1(C) and setting xn
I =R
−
∑m
i=1di
kn
[ξn(I)] and yn
I′ =ξn((I′)c)
#Md,a0,...,am+1
M0,...,Mm+1 = V (ξn(I0))2∏m+1
i=0 qDim(Mi)
nk−1

 ∑
I,I′∈Bk,n
pM0
I pMm+1
I′ KSU (k)
γt0 (xn
I,yn
I′) +O
( 1
n
)
,
where γ =
k[( 1
m
∑m
i=1‖Mi‖2)−⟨I0⟩2]
k2−1 , t0 = (2π)2m
n2 and O(·) depends on k, m
n2 and
( 1
m
∑m
i=1‖Mi‖a
)
,
a = 2, 3.
Similarly to the previous local limit theorem, the latter result is non trivial only when m is of
order n2 or larger. In the particular case where M0 = ΩW0
I and Mm+1 = ΩWm+1
I′ for some generic
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 13
ﬂags W0,Wm+1, the latter corollary yields for d such that∑m+1
i=0 di−dn−k(n−k) = 0
#Md,a0,...,am+1
M1,...,Mm =|V (ξn(I))V (ξn(I′))|∏m+1
i=0 qDim(Mi)
nk−1
(
KSU (k),γ
m
n2
(xI,yI′) +O
( 1
n
))
.
