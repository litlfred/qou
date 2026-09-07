---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-020-26-s-j-kang-m-kashiw-ara-m-kim-s-j-oh
section_title: "S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH"
section_number: 26
pages: 26-28
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
Conversely, assume (ii). Then, Rren
Lz,M ◦N |Lz◦(Kk/Kk+1) and Rren
Lz,Kk/Kk+1
have the same
homogeneous degree, and hence they should coincide. It implies tha t f |L◦(Kk/Kk+1) =
rL,Kk/Kk+1
is an isomorphism for any k. Therefore f = (M ◦ rL,N ) ◦ (rL,M ◦N) is an
isomorphism, which implies that rL,N and rL,M are isomorphisms. Thus we obtain (i).
Similarly, (i) and (iii) are equivalent. □
Lemma 3.2.11. Let L, M and N be simple modules. We assume that L is real and
commutes with M. Then the diagram
L ◦ (M ◦N)
rL,M ◦N /d47/d47
/d15/d15
(M ◦N) ◦L
/d15/d15
L ◦ (M ∇N)
rL,M ∇N /d47/d47(M ∇N) ◦L
commutes.
Proof. Otherwise the composition
L ◦M ◦N
∼
rL,M ◦N
/d47/d47
M ◦L ◦N M ◦rL,N
/d47/d47M ◦N ◦L /d47/d47(M ∇N) ◦L
vanishes by Proposition 3.2.8. Hence we have
M ◦ Im(rL,N ) ⊂ Ker(M ◦N →M ∇N) ◦L.
Hence, by Lemma 2.2.3, there exists a submodule K of N such that
Im(rL,N ) ⊂K ◦L and M ◦K ⊂ Ker(M ◦N →M ∇N).
The ﬁrst inclusion implies K ⁄= 0 and the second implies K ⁄= N, which contradicts
the simplicity of N. □
The following lemma can be proved similarly.
Lemma 3.2.12. Let L, M and N be simple modules. We assume that L is real and
commutes with N. Then the diagram
(M ◦N) ◦L
rM ◦N,L /d47/d47
/d15/d15
L ◦ (M ◦N)
/d15/d15
(M ∇N) ◦L
rM ∇N,L /d47/d47L ◦ (M ∇N)
commutes.
The following proposition follows from Lemma 3.2.11 and Lemma 3.2.12.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 27
Proposition 3.2.13. Let L, M and N be simple modules. Assume that L is real.
Then we have:
(i) If L and M commute, then
Λ(L,M ∇N) = Λ( L,M ) + Λ(L,N ).
(ii) If L and N commute, then
Λ(M ∇N,L ) = Λ( M,L ) + Λ(N,L ).
Proposition 3.2.14. Let M be a real simple module and let N be a module with a
simple socle. If the following diagram
soc(N) ◦M
rsoc(N ),M /d47/d47
/d15/d15
/d15/d15
M ◦ soc(N)
/d15/d15
/d15/d15
N ◦M
rN,M /d47/d47M ◦N
commutes up to a non-zero constant multiple, then soc
(
M ◦ soc(N)
)
is equal to the
socle of M ◦N. In particular, M ◦N has a simple socle.
Proof. LetS be an arbitrary simple submodule of M ◦N. Then we have the following
commutative diagram:
S ◦Mz
RS◦Mz /d47/d47
/d15/d15
/d15/d15
Mz ◦S
/d15/d15
/d15/d15
M ◦N ◦Mz
RM ◦N,Mz /d47/d47M ◦M ◦N.
By multiplying z−m, where m be the order of zero of RM◦N,M , and specializing at
z = 0, we have a commutative diagram (up to a constant multiple):
S ◦M /d47/d47
/d15/d15
/d15/d15
M ◦S
/d15/d15
/d15/d15
M ◦N ◦M
M ◦rN,M /d47/d47M ◦M ◦N.
Here, we use the fact that rM◦N,M = ( rM,M ◦N) ◦ (M ◦ rN,M ) from Lemma 3.1.5
and the fact that rM,M is equal to id M◦M up to a non-zero constant multiple, because
M is a real simple module.
It follows that S ◦M ⊂M ◦ (rN,M )−1(S). Hence there exists a submodule K of N
such that S ⊂M ◦K and K ◦M ⊂ (rN,M )−1(S) by Lemma 2.2.3. Hence K ⁄= 0 and
soc(N) ⊂K by the assumption. Hence rN,M
(
soc(N) ◦M
)
⊂ rN,M
(
K ◦M
)
⊂S. Since
rN,M
(
soc(N) ◦M
)
is non-zero by the assumption, we have rN,M
(
soc(N) ◦M
)
= S.
Thus we obtain the desired result. □
