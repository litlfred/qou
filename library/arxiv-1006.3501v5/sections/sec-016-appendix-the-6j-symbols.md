---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-016-appendix-the-6j-symbols
section_title: "Appendix. The 6j-symbols"
section_number: null
pages: 69-70
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
The tensors known under the awkward name 6j-symbols (see Example 3.3) play a
special role in this theory because only these tensors are needed f or the computation
of the state sum of Section 6.3 on special skeletons of 3-manifolds. We outline the
basic properties of the 6j-symbols associated with a spherical pre-fusion category C.
Pick a 6-tuple T = (i,ε i,j,ε j,k,ε k,l,ε l,m,ε m,n,ε n) of signed objects of C. Let Γ T
be the C-colored graph in S2 obtained from the graph Γ ⊂ S2 in Example 3.3 by
reversing the orientation on all edges colored by x∈{ i,j,k,l,m,n } with εx =−.
Then ⏐⏐⏐⏐
iε i jε j kε k
lε l mε m nε n
⏐⏐⏐⏐ = FC(Γ T )∈H(Γ T )∗,
is the 6j-symbol determined by T . Here H(Γ T ) is the (non-ordered) tensor product
of the modulesH(m,ε m,i,−εi,n,−εn),H(j,ε j,i,ε i,k,−εk),H(n,ε n,j,−εj,l,−εl),
and H(l,ε l,k,ε k,m,−εm). In particular,
⏐⏐⏐⏐
i+ j+ k+
l+ m+ n+
⏐⏐⏐⏐ = FC(Γ).
The isotopy invariance of FC implies that the 6j-symbols have the symmetries of
an oriented tetrahedron. For example,
⏐⏐⏐⏐
i+ j+ k+
l+ m+ n+
⏐⏐⏐⏐ =
⏐⏐⏐⏐
j+ k− i−
m+ n+ l+
⏐⏐⏐⏐ =
⏐⏐⏐⏐
k+ l+ m+
n− i+ j−
⏐⏐⏐⏐.
Giveni,j,k ∈ Ob(C) and signs ε,µ,ν , we have a canonical (non-degenerate) pair-
ingH(iε,jµ,kν )⊗H(k(−ν),j (−µ),i (−ε))→ k, see Sections 2.4 and 3.1. This form
is denoted ωiε,jµ,kν and the corresponding tensor contraction is denoted ∗iε,jµ,kν .
70 V. TURAEV AND A. VIRELIZIER
Theorem 15.2 (The Biedenharn-Elliott identity) . LetI be a representative set of
simple objects in C. For any a,b,c,i,j,k,l,m,n ∈ Ob(C),
∑
z∈I
dim(z) ∗m∓,k±,z±∗c∓,j∓,z±∗b±,i∓,z±
( ⏐⏐⏐⏐
i± z∓ b±
m± n± k±
⏐⏐⏐⏐⊗
⏐⏐⏐⏐
z± j∓ c±
l± m± k±
⏐⏐⏐⏐⊗
⊗
⏐⏐⏐⏐
i± j∓ a∓
c∓ b± z∓
⏐⏐⏐⏐
)
=∗a∓,n∓,l±
( ⏐⏐⏐⏐
i± j∓ a∓
l± n± k±
⏐⏐⏐⏐⊗
⏐⏐⏐⏐
n± l∓ a∓
c∓ b± m∓
⏐⏐⏐⏐
)
.
Proof. Note that the signs of all the objects in this formula may be chosen in de-
pendently from each other. For the upper choice of all the signs, t he graphical
proof is given in Figure 10 (for the opposite choice of some of the sign s, reverse the
orientation of the corresponding edges). Figure 10 presents colo redC-graphs in S2;
the equality means the equality of their FC-invariants. The ﬁrst equality is obtained
by applying Lemma 4.2(d) twice (along the dotted lines) and then Lemm a 4.2(c).
The second equality follows from the invariance of FC under isotopies of the graph
in S2. The last equality follows from Lemma 4.2(d). □
∑
z∈I
dim(z)
PSfrag replacements
i
i z z
z
a
b
b kk c
c
lm m
j
j
n
=
PSfrag replacements
i
z
a
b
k
c
l
m
j
n
=
PSfrag replacements
i
z
a
b
k
c
lm
j
n =
PSfrag replacements
i
z
a
a
b
k
c
l
l
m
j
n
n
Figure 10. Proof of the Biedenharn-Elliot identity
Theorem 15.3 (The orthonormality relation) . For any objects i,k,l,m,m ′,n ofC
such that m,m ′ are simple and for any I as above,
dim(m)
∑
z∈I
dim(z)∗z±,i±,k∓∗z±,n∓,l±
( ⏐⏐⏐⏐
i± z± k±
l± m± n±
⏐⏐⏐⏐⊗
⏐⏐⏐⏐
z∓ i∓ k∓
m′± l± n±
⏐⏐⏐⏐
)
=δm,m′ ωm∓,n±,i±⊗ωl∓,m±,k∓.
The proof is given in Figure 11.
