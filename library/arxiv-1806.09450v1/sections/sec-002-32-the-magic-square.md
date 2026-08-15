---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-002-32-the-magic-square
section_title: "The magic square"
section_number: 3.2
pages: 8-10
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
Equivalent constructions of the Lie algebras en with n = 6, 7, 8 have been pro-
posed by Freudenthal and Tits around 1958, with improved formulations pub-
lished later. In the summary below we follow [BS], as well as [B] where more
references to the early work can be found.
Let K be a real composition algebra and J a real Jordan algebra with unit 1 I
and with an inner product satisfying⟨X,Y ◦Z⟩ =⟨X◦Y,Z⟩ (2.10). Let further
K0 andJ0 be the subspaces of K andJ orthogonal to the unit element. Denote
by∗ the product in J0 obtained from the Jordan product projected back to J0:
X∗Y =X◦Y− 1
n⟨X,Y⟩ 1 I where n =⟨1 I, 1 I⟩ = tr 1 I (3.12)
(the notation being chosen to ﬁt the case J =Hn(K′)). Tits deﬁnes (in 1966) a
Lie algebra structure on the vector space
T (K,J ) = Der (K) ˙+ Der (J) ˙+ K0⊗J0 (3.13)
by setting
[x⊗X,y⊗Y ] = 1
n⟨X,Y⟩Dx,y−⟨x,y⟩[LX,LY ] + [x,y ]⊗X∗Y (3.14)
where x,y ∈ K0, X,Y ∈ J0 and the square brackets in the right hand side
denote commutators in K0 and End (J);Dx,y is the derivation in K0 deﬁned by
(2.4). Tits proves that the brackets (3.14) deﬁne a Lie algebra structure using
the identity
nX 3− (trX 3) 1 I = (trX 2)X for X∈J0, J =Hn(K′) (3.15)
(for K′ = O, n≤ 3). Tits obtains the magic square of Lie algebras by viewing
T (K,J ) forJ =H3(K′) as a Lie algebraL(K, K′) depending on two composition
algebras K and K′:
L(K, K′) =T (K,H 3(K′)). (3.16)
For the Lie algebras of compact real forms one thus obtains the following sym-
metric table:
8
K\ K′ R C H O
R so (3) su (3) sp (6) f4
C su (3) su (3)⊕u(3) su (6) e6
H sp (6) su (6) so (12) e7
O f4 e6 e7 e8
T able 1. Magic square of Lie algebras L(K, K′) (sp (6) being the
rank 3 unitary symplectic Lie algebra).
Following Tits construction the symmetry of the square comes as a surprise.
In fact, it has been predicted in a non-rigorous visionary 1956 paper of the
Russian mathematician and historian of science Boris Rosenfeld who proposed
to view E6,E 7,E 8 as isometry groups of projective planes over the algebras
K⊗ O for K = C, H, O, respectively, just as F4 is the isometry group of P2(O)
= P2(R⊗ O) (see [B] for references and for a more detailed discussion; Rosenfeld
provides a later expositon of his views in Chapter VII of [R]). The realization
of this idea has problems since K⊗ O is not a division algebra except for K =
R. A construction of the exceptional Lie algebras generalizing (3.11), however,
does exist with Der (K)⊕ Der (O) instead of Der (O) and sa3(O) substituted by
sa3(K⊗ O). This is Vinberg’s (1966) approach to constructing L(K, K′), that
is manifestly symmetric with respect to the two algebras K and K′. The Lie
brackets in L(K, K′) are given as follows.
(i) Der ( K) and Der (K′) are commuting Lie subalgebras of L(K, K′).
(ii) The bracket of D∈ Der (K)⊕ Der (K′) with X ∈ sa3(K⊗ K′) is given
by applying D to every entry of the matrix X using the natural action of
Der (K) and Der (K′) as derivations on K⊗ K′.
(iii) Given X,Y ∈sa3(K⊗ K′), we set
[X,Y ] = [X,Y ]0 + 1
3
3∑
i,j=1
Dxij,yij. (3.17)
Here [X,Y ]0 is the traceless part of the 3 × 3 matrix [X,Y ], and given
x,y ∈ K⊗ K′, we deﬁne Dx,y ∈ Der (K)⊕ Der (K′) as real bilinear in
a,b∈ K, a′,b′∈ K′ such that
Da⊗a′b⊗b′ =⟨a′,b′⟩Da,b +⟨a,b⟩Da′,b′ (3.18)
where a,b∈ K, a′,b′∈ K′, and Da,b, Da′,b′ are deﬁned as in Eq. (2.4).
For the equivalence of Tits’ and Vinberg’s constructions of the magic square
and for its triality construction we refer to [B, BS].
9
