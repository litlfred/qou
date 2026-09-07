---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-058-101-chevalley-and-kashiwara-operators-let-us-rec
section_title: "Chevalley and Kashiwara operators. Let us recall the deﬁnition of several"
section_number: 10.1
pages: 75-80
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
functors on modules over KLR algebras which are used to categorif yU −
q (g)∨
Z[q±1].
Deﬁnition 10.1.1. Letβ ∈ Q+.
(i) Fori ∈I and 1 ≤a ≤ |β|, set
ea(i) =
∑
ν∈I β,νa=i
e(ν) ∈R(β).
(ii) We take conventions:
EiM =e1(i)M,
E∗
iM =e|β|(i)M,
which are functors from R(β)-gmod to R(β −αi)-gmod.
(iii) For a simple module M, we set
εi(M) = max {n ∈ Z≥0 |En
iM ⁄= 0},
ε∗
i (M) = max {n ∈ Z≥0 |E∗n
i M ⁄= 0},
~FiM =qεi(M )
i L(i) ∇M,
~F ∗
iM =q
ε∗
i (M )
i M ∇L(i),
~EiM =q1−εi(M )
i soc(EiM) ≃qεi(M )−1
i hd(EiM),
˜E∗
iM =q
1−ε∗
i (M )
i soc(E∗
iM) ≃q
ε∗
i (M )−1
i hd(E∗
iM),
˜E max
i M = ˜Eεi(M )
i M and ˜E∗ max
i M = ˜E
∗ε∗
i (M )
i M.
76 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
(iv) Fori ∈I and n ∈ Z≥0, we set
L(in) = qn(n−1)/2
i L(i) ◦ · · · ◦L(i)/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
n
.
HereL(i) denotes the R(αi)-moduleR(αi)/R(αi)x1. Then L(in) is a self-dual real
simple R(nαi)-module.
Note that, under the isomorphism in Theorem 2.1.2, the functors Ei and E∗
i cor-
respond to the linear operators ei and e∗
i on Aq(n)Z[q±1] = ι(U −
q (g)∨
Z[q±1]) ⊂ Aq(n),
respectively. Note also that, for a simple R(β)-module S, we have ˜Ei ~FiS ≃ S, and
~Fi ˜EiS ≃S if εi(M)> 0.
In the course of proving the following propositions, we use the follow ing notations.
Qi,j(xa,xa+1,xa+2) := Qi,j(xa,xa+1) −Qi,j(xa+2,xa+1)
xa −xa+2
.(10.1)
Then we have
τa+1τaτa+1 −τaτa+1τa =
∑
i,j∈I
Qi,j(xa,xa+1,xa+2)ea(i)ea+1(j)ea+2(i).
Proposition 10.1.2. Let β ∈ Q+ with n = |β|. Assume that an R(β)-module
M satisﬁes EiM = 0 . Then the left R(αi)-module homomorphism R(αi) ⊗M − →
q(αi,β)M ◦R(αi) given by
e(i) ⊗u ↦− →τ1 · · ·τn(u ⊗e(i))(10.2)
extends uniquely to an (R(αi +β),R (αi))-bilinear homomorphism
R(αi) ◦M − →q(αi,β)M ◦R(αi)(10.3)
Proof. (i) First note that, for 1 ≤a ≤n,
(10.4) τ1 · · ·τa−1ea(i)τa+1 · · ·τn
(
u ⊗e(i)
)
=τa+1 · · ·τn
(
e1(i)τ1 · · ·τa−1(u ⊗e(i))
)
= 0
since EiM = 0.
(ii) In order to see that (
10.3) is a well-deﬁned R(αi +β)-linear homomorphism, it is
enough to show that ( 10.2) is R(β)-linear.
(a) Commutation with xa ∈R(β) (1 ≤a ≤n): We have
xa+1τ1 · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τa−1xa+1τa · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τa−1
(
τaxa +ea(i)
)
τa+1 · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τnxa
(
u ⊗e(i)
)
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 77
by ( 10.4).
(b) Commutation with τa ∈R(β) (1 ≤a<n ): We have
τa+1τ1 · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τa−1(τa+1τaτa+1)τa+2 · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τa−1
(
τaτa+1τa +
∑
j
Qi,j(xa,xa+1,xa+2)ea(i)ea+1(j)
)
τa+2 · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τnτa
(
u ⊗e(i)
)
+
∑
j
τ1 · · ·τa−1Qi,j(xa,xa+1,xa+2)ea(i)ea+1(j)τa+2 · · ·τn
(
u ⊗e(i)
)
.
The last term vanishes because EiM = 0 implies
τ1 · · ·τa−1f (xa,xa+1)g(xa+2)ea(i)τa+2 · · ·τn
(
u ⊗e(i)
)
=g(xa+2)τa+2 · · ·τne1(i)τ1 · · ·τa−1f (xa,xa+1)
(
u ⊗e(i)
)
= 0
for any polynomial f (xa,xa+1) and g(xa+2).
(iii) Now let us show that ( 10.3) is right R(αi)-linear. By ( 10.4), we have
τ1 · · ·τa−1xaτa · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τa−1
(
τaxa+1 −ea(i)
)
τa+1 · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τaxa+1τa+1 · · ·τn
(
u ⊗e(i)
)
for 1 ≤a ≤n. Therefore we have
x1τ1 · · ·τn
(
u ⊗e(i)
)
=τ1 · · ·τnxn+1
(
u ⊗e(i)
)
=τ1 · · ·τn
(
u ⊗e(i)x1
)
. □
Recall that for m,n ∈ Z≥0, we denote by w[m,n ] the element of Sm+n deﬁned by
w[m,n ](k) =
{
k +n if 1 ≤k ≤m,
k −m if m<k ≤m +n.(10.5)
Set τw[m,n] := τi1 · · ·τir , where si1 · · ·sir is a reduced expression of w[m,n ]. Note that
τw[m,n] does not depend on the choice of reduced expression ([
14, Corollary 1.4.3]).
Proposition 10.1.3. LetM ∈R(β)-gmod and N ∈R(γ)-gmod, and set m = |β| and
n = |γ|. If EiM = 0 for any i ∈ supp(γ), then
v ⊗u ↦− →τw[m,n](u ⊗v)
gives a well-deﬁned R(β +γ)-linear homomorphism N ◦M − →q(β,γ )M ◦N.
Proof. The proceeding proposition implies that
v ⊗u ↦− →τw[m,n](u ⊗v) for u ∈M,v ∈R(γ)
gives a well-deﬁned R(β +γ)-linear homomorphism R(γ) ◦M →M ◦R(γ). Hence it
is enough to show that it is right R(γ)-linear. Since we know that it commutes with
78 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
the right multiplication of xk, it is enough to show that it commutes with the right
multiplication of τk. For this, we may assume that n = 2 and k = 1. Set γ =αi +αj.
Thus we have reduced the problem to the equality
τ1(τ2τ1) · · ·(τm+1τm)
(
u ⊗e(i) ⊗e(j)
)
= (τ2τ1) · · · (τm+1τm)τm+1
(
u ⊗e(i) ⊗e(j)
)
for u ∈M, which is a consequence of
(τ2τ1) · · ·(τaτa−1)τa(τa+1τa) · · ·(τm+1τm)
(
u ⊗e(i) ⊗e(j)
)
= (τ2τ1) · · · (τa+1τa)τa+1(τa+2τa+1) · · ·(τm+1τm)
(
u ⊗e(i) ⊗e(j)
)
for 1 ≤a ≤m. Note that
τa(τa+1τa) · · ·(τm+1τm)
(
u ⊗e(i) ⊗e(j)
)
=τa(τa+1τa)ea+1(i)ea+2(j)(τa+2τa+1) · · ·(τm+1τm)
(
u ⊗e(i) ⊗e(j)
)
and
τa(τa+1τa)ea+1(i)ea+2(j)
= (τa+1τa)τa+1ea+1(i)ea+2(j) −
Qji(xa,xa+1,xa+2)ea(j)ea+1(i)ea+2(j).
Hence it is enough to show
(τ2τ1) · · · (τaτa−1)Qj,i(xa,xa+1,xa+2)ea(j)
(τa+2τa+1) · · ·(τm+1τm)
(
u ⊗e(i) ⊗e(j)
)
= 0.
This follows from
(τ2τ1) · · ·(τaτa−1)f (xa)g(xa+1,xa+2)ea(j)(τa+2τa+1) · · · (τm+1τm)
(
u ⊗e(i) ⊗e(j)
)
= (τ2 · · ·τa)(τ1 · · ·τa−1)f (xa)g(xa+1,xa+2)ea(j)
(τa+2τa+1) · · ·(τm+1τm)
(
u ⊗e(i) ⊗e(j)
)
= (τ2 · · ·τa)g(xa+1,xa+2)(τa+2τa+1) · · · (τm+1τm)
e1(j)(τ1 · · ·τa−1)f (xa)
(
u ⊗e(i) ⊗e(j)
)
= 0
for 1 ≤a ≤m and f (xa) ∈ k[xa], g(xa+1,xa+2) ∈ k[xa+1,xa+2]. □
Let P (in) be a projective cover of L(in). Deﬁne the functor
E(n)
i :R(β)-Mod →R(β −nαi)-Mod
by
E(n)
i (M) := P (in)ψ ⊗
R(nαi)
En
iM,
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 79
where P (in)ψ denotes the right R(nαi)-module obtained from the left R(β)-module
P (in) via the anti-automorphism ψ. We deﬁne the functor E∗ (n)
i in a similar way.
Note that
En
i ≃ [n]i!E(n)
i .
Corollary 10.1.4. Let R be a symmetric KLR algebra. Let i ∈ I and M a simple
module. Then we have
~Λ
(
L(i),M
)
=εi(M),
Λ
(
L(i),M
)
= 2εi(M) + ⟨hi, wt(M)⟩ =εi(M) +ϕi(M).
Proof. Set n = εi(M) and M0 = E(n)
i (M). Then the preceding proposition implies
Λ(L(i),M 0) =
(
αi, wt(M0)
)
. Hence we have ~Λ(L(i),M 0) = 0, which implies
~Λ(L(i),M ) = ~Λ(L(i),L (in) ◦M0) = ~Λ
(
L(i),L (in)
)
+ ~Λ(L(i),M 0) = n.
□
Proposition 10.1.5. LetM, N be modules and m,n ∈ Z≥0.
(i) If Em+1
i M = 0 and En+1
i N = 0, then we have
E(m+n)
i (M ◦N) ≃qmn+n⟨hi,wt(M )⟩E(m)
i M ◦E(n)
i N.
(ii) If E∗m+1
i M = 0 and E∗n+1
i N = 0, then we have
E∗ (m+n)
i (M ◦N) ≃qmn+m⟨hi,wt(N )⟩E∗ (m)
i M ◦E∗ (n)
i N.
Proof. Our assertions follow from the shuﬄe lemma ([ 21, Lemma 2.20]). □
The following corollaries are immediate consequences of Proposition 10.1.5.
Corollary 10.1.6. Leti ∈I and let M be a real simple module. Then ˜E max
i M is also
real simple.
Corollary 10.1.7. Let i ∈ I and let M be a simple module with εi(M) = m . Then
we have ˜Em
i M ≃E(m)
i M.
Proposition 10.1.8. LetM and N be simple modules. We assume that one of them
is real. If εi(M ∇N) = εi(M), then we have an isomorphism in R-gmod
~E max
i (M ∇N) ≃ ( ~E max
i M) ∇N.
Similarly, if ε∗
i (N ∇M) = ε∗
i (M), then we have
~E∗max
i (N ∇M) ≃ (N ∇ ~E∗max
i M).
80 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Proof. Set n = εi(M ∇N) = εi(M) and M0 = ~E max
i M. Then M0 or N is real. Now
we have
L(in) ⊗M0 ⊗N ֌En
i (M ∇N) ≃L(in) ⊗ ~E max
i (M ∇N),
which induces a non-zero map M0 ⊗N → ~E max
i (M ∇N). Hence we have a surjective
map
M0 ◦N ։ ~E max
i (M ∇N).
Since M0 or N is real by Corollary
10.1.6, M0 ◦N has a simple head and we obtain
the desired result. A similar proof works for the second statement . □
