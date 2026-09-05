---
doc_id: arxiv-0707.3799v3
doc_title: "EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION"
section_id: sec-010-22-roman-bezrukavnikov-and-michael-finkelberg
section_title: "ROMAN BEZRUKAVNIKOV AND MICHAEL FINKELBERG"
section_number: 22
pages: 22-24
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
doc_brief: "EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION — 16 sections: ROMAN BEZRUKAVNIKOV AND MICHAEL FI; ROMAN BEZRUKAVNIKOV AND MICHAEL FI; ROMAN BEZRUKAVNIKOV AND MICHAEL FI"
---
Forl= 0,1,...,nwe introduce a new vectors l
i such thates l
i = 0, ands l
i≡e l(m−1⊗
vi−2l) moduloU ℏ⟨si+2,si+4,...,s n⟩(evidently,s l
i is proportional tosi =s 0
i wheni−2l≥
−n; otherwise,s l
i is not defined). Consider the following collection of equalities:
el(m−1⊗v−n) =
nX
i=−n+2l
ℏl(x+(i−1)ℏ)−1(x+(i−2)ℏ)−1...

x+ i−n+ 2l
2 ℏ
−1
f
n−2l+i
2 sl
i
Then then-th equality is obvious, while thel+1-st equality is equivalent to thel-th one
by applyingeto both sides. Thus the desired equality (forl= 0) follows by descending
induction inl.□
6.Topology vs Algebra
6.1.Comparison of Kostant functor with equivariant cohomology.Recall that
tis identified with ˇt∗.
Theorem 6.a) ForV∈Rep( ˇG)there is a unique isomorphism ofO(t/W×t/W×A 1)-
modulesη V :H •
GO⋊Gm(GrG,S(V))≃ϕ(V)such that(π,Id,Id) ∗ηV preserves the
canonical filtrations and induces the identity isomorphism of the associated graded
gr(π,Id,Id) ∗H•
GO⋊Gm(GrG,S(V)) = (Id,π,Id) ∗
L
λ O(Γλ)⊗ λV=gr(π,Id,Id) ∗ϕ(V).
b) ForV 1,V 2∈Rep( ˇG)the composition
H•
GO⋊Gm(GrG,S(V 1))⋆H •
GO⋊Gm(GrG,S(V 2))
topω−1
V1,V2
−−−−−−→H•
GO⋊Gm(GrG,S(V 1⊗V 2))
ηV1⊗V2
−−−−→ϕ(V1⊗V 2)
algωV1,V2
−−−−−−→ϕ(V1)⋆ϕ(V 2)
equalsη V1∗ηV2 (notations of 3.5 and 4.6).
Proof: a) We have
(π,Id,Id)∗H•
GO⋊Gm(GrG,S(V))⊗ O(t×A1) k(t×A 1) =
gr(π,Id,Id) ∗H•
GO⋊Gm(GrG,S(V))⊗ O(t×A1) k(t×A 1) =
 M
λ
(Id,π,Id)∗O(Γλ)⊗ λV
!
⊗O(t×A1) k(t×A 1) =
gr(π,Id,Id) ∗ϕ(V)⊗ O(t×A1) k(t×A 1) = (π,Id,Id)∗ϕ(V)⊗ O(t×A1) k(t×A 1).
Thus we have to identify (π,Id,Id) ∗H•
GO⋊Gm(GrG,S(V)) with the naturalW-action
on it, and (π,Id,Id) ∗ϕ(V) with the naturalW-action on it, as twoO(t×t/W×A 1)-
submodules of (L
λ(Id,π,Id)∗O(Γλ)⊗ λV)⊗ O(t×A1) k(t×A 1). First we will show that
theW-action on ( L
λ(Id,π,Id)∗O(Γλ)⊗ λV)⊗ O(t×A1) k(t×A 1) arising from its iden-
tification with (π,Id,Id) ∗H•
GO⋊Gm(GrG,S(V))⊗ O(t×A1) k(t×A 1) coincides with the
W-action arising from the identification with (π,Id,Id) ∗ϕ(V)⊗ O(t×A1) k(t×A 1).
Letαbe a simple root,s α∈Wthe corresponding simple reflection, and (e α,hα,fα)
the correspondingsl 2-triple in ˇg. Letv∈ λVbe a vector such thatf αv= 0. Then
EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION 23
hαv=λ(h α)v, andλ(h α) is a nonpositive integer. We consider the following vector in
(L
λ(Id,π,Id)∗O(Γλ)⊗ λV)⊗ O(t×A1) k(t×A 1)∋p α(v) :=
−λ(hα)X
k=0
(hα+(2k−1+λ(hα))ℏ)−1(hα+(2k−2+λ(hα))ℏ)−1...(h α+(k+λ(hα))ℏ)−11λ+kα⊗ek
αv
where 1µ is the constant function 1 on (Id,π,Id)Γ µ.
It follows from the computation in rank 1 (Lemma 12), and the transitivity equa-
tion (8) of subsection 4.5 (applied to the case where ˇLis a subminimal Levi containing
just one positive rootα, and ˇL′ = ˇT) thatp α(v) iss α-invariant (with respect to the
action arising from the identification with (π,Id,Id) ∗ϕ(V)⊗ O(t×A1) k(t×A 1)), and
Mα :=Pv∈ λVfα
λ O(t×A 1)pα(v) contains (π,Id,Id) ∗ϕ(V).
On the other hand, it follows from the computation in rank 1 (equation (7) of
subsection 5.2), and the transitivity equation (3) of subsection 3.4 (applied to the
case where ˇLis a subminimal Levi containing just one positive rootα, and ˇL′ = ˇT)
thatp α(v) iss α-invariant (with respect to the action arising from the identification
with (π,Id,Id) ∗H•
GO⋊Gm(GrG,S(V))⊗ O(t×A1) k(t×A 1)), andM α = Pv∈ λVfα
λ O(t×
A1)pα(v) contains (π,Id,Id) ∗H•
GO⋊Gm(GrG,S(V)). It follows that the twoW-actions
on (L
λ(Id,π,Id)∗O(Γλ)⊗ λV)⊗ O(t×A1) k(t×A 1) coincide. In particular, we have
defined unambiguously aW-action on ( L
λ(Id,π,Id)∗O(Γλ)⊗ λV)⊗ O(t×A1) k(t×A 1).
Now we claim that (π,Id,Id)∗ϕ(V) = Tαsimple
w∈W w(Mα) = (π,Id,Id)∗H•
GO⋊Gm(GrG,S(V)).
In effect, note that if (Id,π,Id)Γ ν∩(Id,π,Id)Γ µ has codimension 1 in (Id,π,Id)Γ ν
(and in (Id,π,Id)Γ µ as well), then necessarilyµ=ν+kβfor certain integer
k, and certain positive rootβ(not necessarily a simple root). Let us choose
w∈Wsuch thatα:=w −1(β) is a simple root. Thenw −1(µ) =w −1(ν) +kα.
Since we know that any section inM α extends through the generic point of
(Id,π,Id)Γ w−1(µ)∩(Id,π,Id)Γ w−1(µ)+kα, we conclude that any section inw(M α)
extends through the generic point of (Id,π,Id)Γ µ ∩(Id,π,Id)Γ ν. It follows
that any section in Tαsimple
w∈W w(Mα) is regular off a codimension 2 subvari-
ety. Since both (π,Id,Id) ∗ϕ(V) and (π,Id,Id) ∗H•
GO⋊Gm(GrG,S(V)) are flat
O(t×A 1)-modules coinciding with Tαsimple
w∈W w(Mα) generically, we conclude that
(π,Id,Id)∗ϕ(V) = Tαsimple
w∈W w(Mα) = (π,Id,Id) ∗H•
GO⋊Gm(GrG,S(V)). This completes
the proof of the a).
b) follows by comparing Propositions 1 and 2.□
6.2.Cohomology is fully faithful.The following property of the cohomology func-
tor will play an important role in the proof of the main results. LetIC(resp. fIC) denote
the full subcategory of semisimple complexes inD GO⋊Gm(Gr) (resp.D GO(Gr)).
Lemma 13.a) The functorH •
GO⋊Gm :IC→Coh Gm(N(ˇt∗/W) 2∆)is a full imbedding.
b) The functorH •
GO : fIC→Coh Gm(T(ˇt∗/W))is a full imbedding.
Proofis due to V. Ginzburg, see [17]. We prove a), and the proof of b) is identical.
ForV 1,V 2 ∈Rep( ˇG) we have Ext •
GO⋊Gm(S(V1),S(V 2)) = Ext •
G×Gm(S(V1),S(V 2)).
