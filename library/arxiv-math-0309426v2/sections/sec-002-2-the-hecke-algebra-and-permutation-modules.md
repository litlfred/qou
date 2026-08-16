---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-002-2-the-hecke-algebra-and-permutation-modules
section_title: "The Hecke algebra and permutation modules"
section_number: 2
pages: 1-3
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
Fix a positive integer n and let Sn be the symmetric group of degree n.
Let R be a commutative domain and let q be an invertible element in R.
2000 Mathematics Subject Classiﬁcation. 20C08, 20G05, 33D80.
Key words and phrases. Specht modules, elementary divisors, hook partitions.
1
2 MATTHIAS K ¨UNZER AND ANDREW MATHAS
The Iwahori–Hecke algebra of Sn with parameter q is the unital associative
algebra H with generators T1,T 2,...,T n−1 and relations
(Ti −q)(Ti + 1) = 0 for 1 ≤i<n,
TiTj = TjTi for 1 ≤i<j − 1<n − 1,
TiTi+1Ti = Ti+1TiTi+1 for 1 ≤i<n − 1.
Let ri = (i,i + 1), for i = 1, 2,...,n − 1. Then {r1,r 2,...,r n−1} generate Sn
(as a Coxeter group). If w ∈ Sn then w =ri1 · · ·rik for some ij with 1 ≤ ij < n.
The word w =ri1...r ik is reduced if k is minimal; in this case we say that w has
length k and we deﬁne ℓ(w) = k.
If ri1...r ik is reduced then we set Tw =Ti1 · · ·Tik . Then Tw is independent of
the choice of reduced expression for w; see, for example, [ 10, 1.11]. Furthermore,
H is free as an R–module with basis {Tw |w ∈ Sn }.
A composition µ of n is a sequence of non–negative integers ( µ1,µ 2,... ) that
sum to n. If, in addition, µ1 ≥µ2 ≥... , then µ is a partition of n.
Letµ be a composition of n and let Sµ be the associated Young subgroup. Then
H (Sµ) = ⟨Tw |w ∈ Sµ ⟩ is a subalgebra of H . Given a (right) H (Sµ)–moduleV ,
we deﬁne the induced H –module
IndH
H (Sµ )(V ) = V ⊗H (Sµ ) H .
Let Dµ = {d ∈ Sn |ℓ(dri)>ℓ (d) for all ri ∈ Sµ } be the set of distinguished right
coset representatives of Sµ in Sn. Then, as an R-module,
IndH
H (Sµ )(V ) ∼
=
⨁
d∈Dµ
V ⊗Td
by [ 2, Theorem 2.7].
Let xµ = ∑
w∈Sµ Tw. Then Twxµ =xµTw =qℓ(w)xµ for all w ∈ Sµ. The trivial
representation of H (Sµ) is the free R–module 1µ =Rxµ.
Letyµ = ∑
w∈Sµ (−q)−ℓ(w)Tw. Then Twyµ =yµTw = (−1)ℓ(w)yµ for all w ∈ Sµ.
The sign representation of H (Sµ) is the free R–module Eµ =Ryµ.
For any compositionµ we deﬁne the permutation module M (µ) = Ind H
H (Sµ )(1µ) ∼
=
xµH . Then M (µ) is free as anR–module of rank [ Sn : Sµ] with basis {xµTd |d ∈ Dµ }.
The H –action on M (µ) is determined by
xµTdTi =





qxµTd, if ℓ(dri)>ℓ (d) and dri ⁄∈ Dµ,
xµTdri, if ℓ(dri)>ℓ (d) and dri ∈ Dµ,
qxµTdri + (q − 1)xµTd, otherwise.
Note that if ℓ(dri)<ℓ (d) then dri ∈ Dµ.
Let ∗ : H − →H be the R–linear map on H determined by T ∗
w =Tw−1, for all
w ∈ Sn. This deﬁnes an R-algebra anti–automorphism on H of order 2.
The module M (µ) carries a symmetric bilinear form ⟨, ⟩µ given by
⟨xµTa,xµTb⟩µ =
{
qℓ(a), if a =b,
0, otherwise,
fora,b ∈ Dµ. It follows from the formulae above that the form ⟨, ⟩µ is associative
in the sense that
⟨xh,y ⟩µ = ⟨x,yh ∗⟩µ
for all x,y ∈M (µ) and all h ∈ H .
