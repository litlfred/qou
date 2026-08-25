---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-042-35-integral-representation-as-we-are-going-to-co
section_title: "Integral representation. As we are going to consider the functions in (82) when"
section_number: 3.5
pages: 33-34
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
N → +∞, we re-introduce now the hidden dependence on N in the notations, thus letting
(uN )N := ((u0,N, u1,N, u2,N ))N be a sequence of triples of quantum shape parameters on ∆ 0
as in Section 2.3. Contrary to the more general situation con sidered in Section 2.4, here we
assume that uN
k,N is constant. Thus, as in (34) we write
(84) uk,N = exp(lk,N ), lk,N := 1
N (Log(uk) +πiak) +πiak,ak ∈ Z.
Using the formula (54) one can write (83) as
(85) Σ N (u0,N, u1,N ) = 1 + 1
ˆSN (l0,N )
N −1∑
β=1
e
2πi
N β2−l1,Nβ ˆSN (l0,N + 2βiπ/N ).
Note that for β ∈ Z we have el1,Nβ = e(l1,N +2iπk)β for any k ∈ Z, so the formula (85) is
invariant under translation of l1,N by 2iπ. In fact, because the QHI solely depend on the
quantum shape parameters uk,N and vk,N , by adding even integers to a0 or a1 if necessary
we can assume that in the above formula we have
(86) ∀N, I(l0,N ) ∈] − 2π, 0] , I(l1,N ) ∈]0, 2π].
Recall that the poles of ˆSN (z) are the points z = 2iπ + 2piπ/N, p ∈ N, the simple poles
being those with p ∈ { 0,...,N − 1} (see (53)). On another hand the poles of coth( Nz/ 2)
34 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
are the points z = 2iπβ/N , β ∈ Z, and they are all simple poles, with residue 2 /N. Because
I(l0,N ) ⊂] − 2π, 0], it follows that the function
φ : z ↦→ˆSN (l0,N +z) coth(Nz
2 )N
2
is meromorphic in the half-space {I(z) < 2π}, and has poles zβ := 2iπβ/N where β ∈ Z,
β ≤N − 1. These poles are simple, and Res( φ,zβ) = ˆSN (l0,N + 2βiπ/N ).
Let CN be the boundary of a rectangle with counter clockwise orient ation, sides parallel to
the real and imaginary axes, containing the segment i[ 2π
N, 2π − 2π
N ] in its interior, and close
to it so that we have constants ε> 0 and s−
N,s +
N ∈]0, 2π
N [ satisfying
(87) CN ⊂ {|R(z)| ≤ ε} ∩ {s−
N ≤ I(z) ≤ 2π −s+
N }.
See Figure 6. An immediate application of Cauchy’s residue t heorem gives:
Lemma 3.11. Assuming (86) and (87), we have
(88) Σ N (u0,N, u1,N ) = 1 + 1
ˆSN (l0,N )
N
4iπ
∫
CN
e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 )dz.
