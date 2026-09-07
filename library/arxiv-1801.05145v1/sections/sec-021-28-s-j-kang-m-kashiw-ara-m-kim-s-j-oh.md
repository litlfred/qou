---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-021-28-s-j-kang-m-kashiw-ara-m-kim-s-j-oh
section_title: "S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH"
section_number: 28
pages: 28-30
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
The following is a dual form of the preceding proposition.
Proposition 3.2.15. LetM be a real simple module. Let N be a module with a simple
head. If the following diagram
M ◦N
rM,N /d47/d47
/d15/d15
/d15/d15
N ◦M
/d15/d15
/d15/d15
M ◦ hd(N)
rM,hd(N ) /d47/d47hd(N) ◦M
commutes up to a non-zero constant multiple, then M ∇ hd(N) is equal to the simple
head of M ◦N.
Proposition 3.2.16. Let L, M and N be simple modules. We assume that L is real
and one of M and N is real.
(i) If Λ(L,M ∇N) = Λ( L,M ) + Λ(L,N ), then L ◦M ◦N has a simple head and
N ◦M ◦L has a simple socle.
(ii) If Λ(M ∇N,L ) = Λ( M,L ) + Λ(N,L ), then M ◦N ◦L has a simple head and
L ◦N ◦M has a simple socle.
(iii) If d(L,M ∇N) = d(L,M ) +d(L,N ), then L◦M ◦N andM ◦N ◦L have simple
heads, and N ◦M ◦L and L ◦N ◦M have simple socles.
Proof. (i) Denote k = Λ(L,M ∇N) = Λ( L,M ) + Λ(M,N ) and m = Λ(M,N ). Then
the diagram
L ◦M ◦N
rL,M ◦N /d47/d47
/d15/d15
/d15/d15
q−kM ◦N ◦L
/d15/d15
/d15/d15
L ◦ (M ∇N)
rL,M ∇N /d47/d47
/d15/d15
/d15/d15
q−k(M ∇N) ◦L
/d15/d15
/d15/d15
q−mL ◦N ◦M
rL,N ◦M /d47/d47q−k−mN ◦M ◦L
commutes. Hence Proposition 3.2.14 and Proposition 3.2.15 imply that L ◦M ◦N has
a simple head and N ◦M ◦L has a simple socle. (ii) are proved similarly.
(iii) If d(L,M ∇N) = d(L,M )+d(L,N ), then we have Λ(L,M ∇N) = Λ( L,M )+Λ(L,N )
and Λ(M ∇N,L ) = Λ( M,L ) + Λ(N,L ) by Proposition 3.2.8. Thus the statements in
(iii) follow from (i) and (ii). □
Proposition 3.2.17. Let M and N be simple modules. Assume that one of them is
real and d(M,N ) = 1 . Then we have an exact sequence
0 →M ∆ N →M ◦N →M ∇N → 0.
In particular, M ◦N has length 2.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 29
Proof. In the course of the proof, we ignore the grading.
SetX =Mz ◦N andY =N ◦Mz. By Rren
N,Mz : Y ֌X let us regard Y as a submodule
ofX. By the condition, we have Rren
N,Mz ◦Rren
Mz,N =z idX up to a constant multiple (see
Lemma 3.2.1 (ii)), and hence we have
zX ⊂Y ⊂X.
We have an exact sequence
0 − − →Y
zX − − →X
zX − − →X
Y − − →0.
Since
M ◦N ≃ X
zX ։ X
Y ֌ z−1Y
Y ≃N ◦M,
we have X
Y ≃M ∇N by Proposition 3.2.9. Similarly,
N ◦M ≃ Y
zY ։ Y
zX ֌ X
zX ≃M ◦N
implies that Y
zX ≃M ∆ N by Proposition 3.2.9. □
Lemma 3.2.18. Let M and N be simple modules. Assume that one of them is real.
If there is an exact sequence
0 →qmX − − →M ◦N − − →qnY − − →0
for self-dual simple modules X, Y and integers m, n, then we have
d(M,N ) = m −n.
Proof. We may assume that M andN are self-dual without loss of generality. Then we
haven = −~Λ(M,N ). Since qmX ≃qΛ(N,M )N ∇M ≃qΛ(N,M )−~Λ(N,M )(
q ~Λ(N,M )N ∇M
)
,
we have m = Λ(N,M ) − ~Λ(N,M ). Thus we obtain
m −n = Λ(N,M ) − ~Λ(N,M ) + ~Λ(M,N ) = d(M,N ).
□
Lemma 3.2.19. Let M and N be simple modules. Assume that one of them is real.
If the equation
[M][N] = qm[X] +qn[Y ]
holds in K(R-gmod) for self-dual simple modules X, Y and integers m, n such that
m ≥n, then we have
(i) d(M,N ) = m −n> 0,
(ii) there exists an exact sequence
0 − − →qmX − − →M ◦N − − →qnY − − →0,
