---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-019-24-s-j-kang-m-kashiw-ara-m-kim-s-j-oh
section_title: "S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH"
section_number: 24
pages: 24-26
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
(ii) If Λ(M,N 1)< Λ(M,N 2), then the composition
M ◦N1
M ◦f
− − − →M ◦N2
rM,N2
− − − − →N2 ◦M
vanishes.
(iii) If Λ(M,N 1)> Λ(M,N 2), then the composition
M ◦N1
rM,N1
− − − − →N1 ◦M
f ◦M
− − − →N2 ◦M
vanishes.
(iv) If f is surjective, then we have
Λ(M,N 1) ≥ Λ(M,N 2) and Λ(N1,M ) ≥ Λ(N2,M )
If f is injective, then we have
Λ(M,N 1) ≤ Λ(M,N 2) and Λ(N1,M ) ≤ Λ(N2,M )
Proof. Let si be the order of zero of RMz,Ni for i = 1, 2. Then we have Λ( M,N 1) −
Λ(M,N 2) = 2(s2 −s1).
Set m := min{s1,s 2}. Then the following diagram is commutative:
Mz ◦N1
z−mRMz ,N1 /d47/d47
Mz◦f
/d15/d15
N1 ◦Mz
f◦Mz
/d15/d15
Mz ◦N2
z−mRMz ,N2 /d47/d47N2 ◦Mz.
(i) If s1 = s2, then by specializing z = 0 in the above diagram, we obtain the
commutativity of the diagram in (i).
(ii) If s1 >s 2, then we have
z−mRMz,N1 =zs1−m(
z−s1RMz,N1
)
so that z−mRMz,N1|z=0 vanishes. Hence we have
rM,N2
◦ (M ◦f ) = z−mRMz,N2|z=0 ◦ (M ◦f ) = 0,
as desired. In particular, f is not surjective.
(iii) Similarly, if s1 <s 2, then we have ( f ◦M) ◦ rM,N1
= 0, and f is not injective.
(iv) The statements for Λ( M,N 1) and Λ( M,N 2) follow from (ii) and (iii). The other
statements can be shown in a similar way. □
Proposition 3.2.9. LetM and N be simple modules. We assume that one of them is
real. Then we have
HomR-mod(M ◦N,N ◦M) = k rM,N.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 25
Proof. Since the other case can be proved similarly, we assume that M is real. Let
f : M ◦N → N ◦M be a morphism. Note that we have rM,M ◦N = M ◦ rM,N and
rM,N ◦M = rM,N ◦M by Lemma 3.1.5 (ii) and by the fact that rM,M = idM◦M up a
constant multiple. Thus, by Proposition 3.2.8, we have a commutative diagram (up to
a constant multiple)
M ◦M ◦N
M ◦rM,N /d47/d47
M ◦f
/d15/d15
M ◦N ◦M
f ◦M
/d15/d15
M ◦N ◦M
rM,N ◦M
/d47/d47N ◦M ◦M
Hence we have
M ◦ Im(rM,N ) ⊂f −1(
Im(rM,N )
)
◦M.
Hence there exists a submodule K of N such that Im( rM,N ) ⊂K ◦M and M ◦K ⊂
f −1(
Im(rM,N )
)
by Lemma 2.2.3. Since K ⁄= 0, we have K = N. Hence f (M ◦N) ⊂
Im(rM,N ), which means that f factors as M ◦N → soc(N ◦M) ֌N ◦M. It remains
to remark that Hom R-mod
(
M ◦N, soc(N ◦M)
)
= k rM,N . □
Proposition 3.2.10. LetL, M and N be simple modules. Then we have
Λ(L,S ) ≤ Λ(L,M ) + Λ(L,N ), Λ(S,L ) ≤ Λ(M,L ) + Λ(N,L ) and
d(S,L ) ≤ d(M,L ) + d(N,L )(3.1)
for any subquotient S of M ◦N. Moreover, when L is real, the following conditions
are equivalent.
(i) L commutes with M and N.
(ii) Any simple subquotient S of M ◦N commutes with L and satisﬁes Λ(L,S ) =
Λ(L,M ) + Λ(L,N ).
(iii) Any simple subquotient S of M ◦N commutes with L and satisﬁes Λ(S,L ) =
Λ(M,L ) + Λ(N,L ).
Proof. The inequalities (
3.1) are consequences of Proposition 3.2.8. Let us show the
equivalence of (i)–(iii).
LetM ◦N =K0 ⊃K1 ⊃ · · · ⊃ Kℓ ⊃Kℓ+1 = 0 be a Jordan-H¨ older series ofM ◦N.
Then the renormalized R-matrix Rren
Lz,M ◦N = (M ◦Rren
Lz,N ) ◦ (Rren
Lz,M ◦N) :Lz ◦M ◦N →
M ◦N ◦Lz is homogeneous of degree Λ( L,M ) + Λ( L,N ) and it sends Lz ◦Kk to
Kk ◦Lz for any k ∈ Z. Hence f := rL,M ◦N =Rren
Lz,M ◦N |z=0 sends L ◦Kk to Kk ◦L.
First assume (i). Then f is an isomorphism. Hence f |L◦Kk : L ◦Kk → Kk ◦L is
injective. By comparing their dimension, f |L◦Kk is an isomorphism, Hence f |L◦(Kk/Kk+1)
is an isomorphism of homogeneous degree Λ( L,M ) + Λ(L,N ). Hence we obtain (ii).
