---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-022-30-s-j-kang-m-kashiw-ara-m-kim-s-j-oh
section_title: "S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH"
section_number: 30
pages: 30-31
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
(iii) qmX is the socle of M ◦N and qnY is the head of M ◦N.
Proof. First note that d(M,N ) > 0 since M ◦N is not simple. By the assumption,
there exists either an exact sequence
0 − − →qmX − − →M ◦N − − →qnY − − →0,
or
0 − − →qnY − − →M ◦N − − →qmX − − →0.
The second sequence cannot exist by Lemma 3.2.18 because d(M,N ) = n −m ≤ 0.
Hence the ﬁrst sequence exists, and the assertion (iii) follows from Theorem 2.2.4. □
Proposition 3.2.20. Let X,Y,M and N be simple R-modules. Assume that there is
an exact sequence
0 →X →M ◦N →Y → 0,
X ◦N and Y ◦N are simple and X ◦N ⁄≃Y ◦N as ungraded modules. Then N is a
real simple module.
Proof. Assume that N is not real. Then N ◦N is reducible and we have rN,N ⁄=c idN◦N
for any c ∈ k by [15, Corollary 3.3]. Note that N ◦N is of length 2, because M ◦N ◦N
is of length 2.
Let S be a simple submodule of N ◦N. Consider an exact sequence
0 − − →X ◦N − − →M ◦N ◦N − − →Y ◦N − − →0.
Then we have
(X ◦N) ∩ (M ◦S) = 0.(3.2)
Indeed, if ( X ◦ N) ⊂ (M ◦ S), then there exists a submodule Z of N such that
X ⊂ M ◦Z and Z ◦N ⊂ S by [ 15, Lemma 3.1]. It contradicts the simplicity of N.
Thus ( 3.2) holds.
Note that ( 3.2) implies
M ◦S ≃Y ◦N
since Y ◦N is simple.
(a) Assume ﬁrst that N ◦N is semisimple so that N ◦N = S ⊕S′ for some simple
submoduleS′ ofN ◦N. Then M ◦S ≃Y ◦N ≃M ◦S′. Hence M ◦S ≃X ◦N ≃M ◦S′.
Therefore we obtain X ◦N ≃Y ◦N, which is a contradiction.
(b) Assume that N ◦ N is not semisimple so that S is a unique non-zero proper
submodule of N ◦N and (N ◦N)/S is a unique non-zero proper quotient of N ◦N.
Without loss of generality, we may assume that k is algebraically closed ([ 21, Corollay
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 31
3.19]). Let x ∈ k be an eigenvalue of rN,N . Since rN,N ⁄∈k idN◦N , we have 0 ⊊
Im(rN,N −x idN◦N ) ⊊ N ◦N. It follows that
S = Im(rN,N −x idN◦N ) ≃ (N ◦N)/S,
and hence we have an exact sequence
0 − − →M ◦S − − →M ◦N ◦N − − →M ◦
(
(N ◦N)/S
)
− − →0.
Since M ◦N ◦N is of length 2, we have
X ◦N ≃M ◦S ≃M ◦
(
(N ◦N)/S
)
≃Y ◦N,
which is a contradiction. □
Corollary 3.2.21. Let X,Y,N be simple R-modules and let M be a real simple R-
module. If we have an exact sequence
0 →X →M ◦N →Y → 0
and if X ◦N and Y ◦N are simple, then N is a real simple module.
Proof. Since M is real and M ◦N is not simple, X is not isomorphic to Y as an
ungraded module by Lemma 3.2.3 (iv). It follows that X ◦N is not isomorphic to
Y ◦N, because K(R-gmod) is a domain so that [ X ◦N] = qm[Y ◦N] for some m ∈ Z
implies [X] = qm[Y ]. Now the assertion follows from Proposition 3.2.20. □
Lemma 3.2.22. Let {Mi}1≤i≤n and {Ni}1≤i≤n be a pair of commuting families of real
simple modules. We assume that
(a) {Mi ∇Ni}1≤i≤n is a commuting family of real simple modules,
(b) Mi ∇Ni commutes with Nj for any 1 ≤i,j ≤n.
Then we have
(◦1≤i≤nMi) ∇ (◦1≤j≤nNj) ≃ ◦1≤i≤n(Mi ∇Ni) up to a grading shift.
Proof. Since ◦1≤i≤n(Mi∇Ni) is simple, it is enough to give an epimorphism ( ◦1≤i≤nMi)◦
(◦1≤j≤nNj) ։ ◦1≤i≤n(Mi ∇Ni). We shall show it by induction on n. For n >0, we
have
(◦1≤i≤nMi) ◦ (◦1≤j≤nNj) ≃ (◦1≤i≤n−1Mi) ◦Mn ◦Nn ◦ (◦1≤j≤n−1Nj)
։ (◦1≤i≤n−1Mi) ◦ (Mn ∇Nn) ◦ (◦1≤j≤n−1Nj)
≃ (◦1≤i≤n−1Mi) ◦ (◦1≤j≤n−1Nj) ◦ (Mn ∇Nn)
։ (◦1≤i≤n−1(Mi ∇Ni)) ◦ (Mn ∇Nn),
as desired. □
