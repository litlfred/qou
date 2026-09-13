---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-024-41-leclercs-conjecture-the-following-theorem-is
section_title: "Leclerc’s conjecture. The following theorem is a part of Leclerc’s conjecture"
section_number: 4.1
pages: 32-35
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
stated in the introduction.
Theorem 4.1.1. Let M and N be simple modules. We assume that M is real. Then
we have the equalities in the Grothendieck group K(R-gmod):
(i) [M ◦N] = [M ∇N] + ∑
k[Sk]
with simple modules Sk such that Λ(M,Sk)< Λ(M,M ∇N) = Λ( M,N ),
(ii) [M ◦N] = [M ∆ N] + ∑
k[Sk]
with simple modules Sk such that Λ(Sk,M )< Λ(M ∆ N,M ) = Λ( N,M ),
(iii) [N ◦M] = [N ∇M] + ∑
k[Sk]
with simple modules Sk such that Λ(Sk,M )< Λ(N ∇M,M ) = Λ( N,M ),
(iv) [N ◦M] = [N ∆ M] + ∑
k[Sk]
with simple modules Sk such that Λ(M,Sk)< Λ(M,N ∆ M) = Λ( M,N ).
In particular, M ∇N as well as M ∆ N appears only once in the Jordan-H¨ older series
of M ◦N in R-mod.
The following result is an immediate consequence of this theorem.
Corollary 4.1.2. Let M and N be simple modules. We assume that one of them
is real. Assume that M and N do not commute, Then we have the equality in the
Grothendieck group K(R-gmod)
[M ◦N] = [M ∇N] + [M ∆ N] +
∑
k
[Sk]
with simple modules Sk. Moreover we have
(i) If M is real, then we have Λ(M,M ∆ N)< Λ(M,N ), Λ(M ∇N,M )< Λ(N,M )
and Λ(M,Sk)< Λ(M,N ), Λ(Sk,M )< Λ(N,M ).
(ii) If N is real, then we have Λ(N,M ∇N) < Λ(N,M ), Λ(M ∆ N,N ) < Λ(M,N )
and Λ(N,Sk)< Λ(N,M ), Λ(Sk,N )< Λ(M,N ).
Proof of Theorem 4.1.1. We shall prove only (i). The other statements are proved
similarly.
M ◦N =K0 ⊃K1 ⊃ · · · ⊃ Kℓ ⊃Kℓ+1 = 0.
Then we haveK0/K1 ≃M ∇N. Let us consider the renormalized R-matrix Rren
Mz,M ◦N =
(M ◦Rren
Mz,N ) ◦ (Rren
Mz,M ◦N)
Mz ◦M ◦N
Rren
Mz ,M ◦N
/d47/d47M ◦Mz ◦N
M ◦Rren
Mz ,N /d47/d47M ◦N ◦Mz.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 33
Then Rren
Mz,M ◦N sends Mz ◦Kk to Kk ◦Mz for any k. Hence evaluating the above
diagram at z = 0, we obtain
M ◦M ◦N
M ◦rM,N /d47/d47M ◦N ◦M
M ◦K1 /d47/d47/d63/d31
/d79/d79
K1 ◦M.
/d63/d31
/d79/d79
Since Im( rM,N : M ◦N → N ◦M) ≃ (M ◦N)/K1, we have rM,N (K1) = 0. Hence,
Rren
Mz,M ◦N sends Mz ◦ K1 to (K1 ◦ Mz) ∩ z
(
(M ◦ N) ◦ Mz
)
= z(K1 ◦ Mz). Thus
z−1Rren
Mz,M ◦N |Mz◦K1 is well deﬁned. Then it sends Mz ◦Kk toKk ◦Mz fork ≥ 1. Thus
we obtain an R-matrix
z−1Rren
Mz,M ◦N |Mz◦(Kk/Kk+1) : Mz ◦ (Kk/Kk+1) → (Kk/Kk+1) ◦Mz for 1 ≤k ≤ℓ.
Hence we have
Rren
Mz,Kk/Kk+1 =z−skz−1Rren
Mz,M ◦N |Mz◦(Kk/Kk+1)
for some sk ∈ Z≥0. Since the homogeneous degree of Rren
Mz,M ◦N is Λ( M,M ◦N) =
Λ(M,N ), we obtain
Λ(M,Kk/Kk+1) = Λ( M,N ) − 2(1 +sk)< Λ(M,N ).
□
Recall that the isomorphism classes of self-dual simple modules in R-gmod are pa-
rameterized by the crystal basis B(∞) ([ 28]). The following theorem is an application
of the above theorem.
Theorem 4.1.3. Letφ be an element of the Grothendieck group K(R-gmod) given by
φ =
∑
b∈B(∞)
ab[Lb],
where Lb is the self-dual simple module corresponding to b ∈ B(∞) and ab ∈ Z[q±1].
LetA be a real simple module in R-gmod. Assume that we have an equality
φ[A] = ql[A]φ
in K(R-gmod) for some l ∈ Z. Then A commutes with Lb and
l = Λ(A,Lb)
for every b ∈B(∞) such that ab ⁄= 0.
Proof. Note that we have
φ[A] =
∑
b
ab[Lb ◦A] =
∑
b
ab([Lb ∇A] +
∑
k
[Sb,k]) and
34 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
ql[A]φ =ql
∑
b
ab[A ◦Lb] = ql
∑
b
ab(qΛ(Lb,A)[Lb ∇A] +
∑
k
[Sb,k]),
for some simple modules Sb,k and Sb,k satisfying
Λ(Sb,k,A )< Λ(Lb,A ) and Λ( Sb,k,A )< Λ(Lb,A )
by Theorem 4.1.1.
We may assume that {b ∈B(∞) |ab ⁄= 0} ⁄= ∅. Set
t := max {Λ(Lb,A ) |ab ⁄= 0}.
By taking the classes of self-dual simple modules S with Λ(S,A ) = t in the expansions
of φ[A] and ql[A]φ, we obtain
∑
Λ(Lb,A)=t
ab[Lb ∇A] =
∑
Λ(Lb,A)=t
qlabqΛ(Lb,A)[Lb ∇A].
In particular, we have t = −l.
Set
t′ := max {Λ(A,Lb) |ab ⁄= 0}.
Then, by a similar argument we have t′ =l.
It follows that
0 = t +t′ ≥ Λ(Lb,A ) + Λ(A,Lb) ≥ 0
for every b such that ab ⁄= 0. Hence A and Lb commute.
Since∑
ab qΛ(A,Lb)[A ◦Lb] =
∑
ab[Lb ◦A] = φ[A] = ql[A]φ =ql
∑
ab[A ◦Lb],
we have
l = Λ(A,Lb)
for any b such that ab ⁄= 0, as desired. □
Corollary 4.1.4. LetM and N be simple modules. Assume that one of them is real.
If [M] and [N] q-commute (i.e., [M][N] = qn[N][M] for some n ∈ Z), then M and N
commute. In particular, M ◦N is simple.
The following corollary is an immediate consequence of the corollary ab ove and
Theorem 2.1.4.
Corollary 4.1.5. Assume that the generalized Cartan matrix A is symmetric and that
b1,b 2 ∈B(∞) satisfy the conditions :
(i) one of Gup(b1)2 and Gup(b2)2 is a member of the upper global basis up to a power
of q,
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 35
(ii) Gup(b1) and Gup(b2) q-commute.
Then their product Gup(b1)Gup(b2) is a member of the upper global basis of U −
q (g) up
to a power of q.
