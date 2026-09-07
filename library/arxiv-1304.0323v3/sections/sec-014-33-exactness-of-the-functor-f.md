---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS"
section_id: sec-014-33-exactness-of-the-functor-f
section_title: "Exactness of the functor F"
section_number: 3.3
pages: 33-36
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
proving our main theorem.
Proposition 3.3.1 ([
23, Corollary 2.9], [ 31, Theorem 4.6]) . If the quiver associated
with RJ is of ﬁnite type A,D,E , then RJ (β) has a ﬁnite global dimension for every
β∈ Q+.
Proposition 3.3.2. Let A→ B be a homomorphism of algebras. We assume the
following conditions:
(a) B is a ﬁnitely generated projective A-module,
(b) HomA(B,A ) is a projective B-module,
(c) the global dimension of B is ﬁnite.
Then we have:
(i) any B-module projective over A is projective over B,
(ii) any B-module ﬂat over A is ﬂat over B.
Proof. Since the proof is similar, we give only the proof of (ii).
Let us denote by ﬂat . dimAM the ﬂat dimension of an A-module M. Then we have
ﬂat. dimA(M)≤ ﬂat. dimB(M)
for any B-module M, because Tor A
k (N,M )≃ TorB
k (N⊗AB,M ) for any Aopp-module
N and k∈ Z by (a).
34 S.-J. KANG, M. KASHIW ARA, M. KIM
By (b), Hom A(B,A )⊗AL is a ﬂat B-module if L is a ﬂat A-module. Indeed,
the functor X⊗B HomA(B,A ) is exact in X ∈ Mod(Bopp) and hence the functor
X⊗B HomA(B,A )⊗AL is also exact in X.
On the other hand, for any A-module L, the canonical B-module homomorphism
HomA(B,A )⊗
A
L→ HomA(B,L ), f ⊗s↦−→(B∋b↦→f (b)s)
is an isomorphism by (a). Hence we conclude that Hom A(B,L ) is a ﬂat B-module for
any ﬂat A-module L. It immediately implies that
ﬂat. dimB
(
HomA(B,L )
)
≤ ﬂat. dimA(L) for any A-module L.
Now, letM be a B-module. Then there exists a canonical B-module homomorphism
ϕM : M→ HomA(B,M )
given by ϕM (x)(b) = bx. It is evidently injective.
In order to prove the proposition, it is enough to show the following s tatement for
anyd≥ 0:
for any B-module M, ﬂat. dimA(M)≤d implies ﬂat. dimB(M)≤d.
We shall show it by the descending induction on d. If d≫ 0, it is a consequence of (c).
Let M be a B-module with ﬂat . dimA(M)≤d. We have an exact sequence
0→M
ϕM
−−→HomA(B,M )→N→ 0.
Then
ﬂat. dimA
(
HomA(B,M )
)
≤ ﬂat. dimB
(
HomA(B,M )
)
≤ ﬂat. dimA(M)≤d.
Hence we have ﬂat . dimAN≤d + 1, which implies that ﬂat . dimB(N)≤d + 1 by the
induction hypothesis. Finally, we conclude that ﬂat . dimB(M)≤d. Thus the induction
proceeds. □
Theorem 3.3.3. If the quiver associated with RJ is of ﬁnite type A,D,E , then the
functorFβ is exact for every β∈ Q+.
Proof. Let us apply Proposition 3.3.2 withA = Popp
β andB =RJ (β)opp. The conditions
(a) and (b) are well-known, and (c) is nothing but Proposition
3.3.1. Therefore, ˆV⊗β
is a ﬂat RJ (β)opp-module since it is a ﬂat Popp
β -module. □
4. Quantum affine algebra U′
q(ˆslN ) and the category CJ
In this section, we investigate the tensor category structure of CˆslN
(N≥ 2) via its
vector representation using the method introduced in the previou s section. In the case
of g = ˆslN , we have I ={0, 1,...,N − 1} and
(αi,αj) = 2δi,j−δ(i≡j + 1 mod N)−δ(i≡j− 1 mod N).
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 35
The base ﬁeld k is C(q).
4.1. R-matrix for V (̟1) of U′
q(ˆslN ). Let V :=V (̟1) be the fundamental represen-
tation of U′
q(ˆslN ) of fundamental weight ̟1. Then V =
N⨁
k=1
kuk with the action
ei(uk) = δ(k≡i + 1 mod N )ui,
fi(uk) = δ(k≡i mod N)ui+1,
Kiuk = qδ(k≡i mod N )−δ(k≡i+1 mod N )uk.
Here u0 =uN .
The normalized R-matrix
R =Rnorm
V (̟1),V (̟1) : Vz⊗Vz′→Vz′⊗Vz
is explicitly given by
R((ui)z⊗(uj)z′)
=



(1−q2)z′δ(i>j)zδ(i<j)
z′−q2z (ui)z′⊗(uj)z + q(z′−z)
z′−q2z (uj)z′⊗(ui)z if i⁄=j,
(ui)z′⊗(ui)z if i =j.
(4.1.1)
It shows that dV,V (z′/z) = z′/z−q2.
LetS ={V}, J = Z and let X : J→ k× be the map given by X(j) = q2j. Then we
have
dij =δ(j =i + 1) for i,j∈J.(4.1.2)
Then, for i,j∈J, we have
(αi,αj) =





−1 if i−j =±1,
2 if i =j,
0 otherwise,
and
Qij(u,v ) =





±(u−v) if j =i± 1,
0 if i =j,
1 otherwise.
Therefore the corresponding Khovanov-Lauda-Rouquier algebr aR =RJ is of type A∞.
We take
PJ = ⨁
a∈Z
Zǫa
as the weight lattice with ( ǫa,ǫb) = δa,b. The root lattice QJ = ⨁
i∈J
Zαi is embedded
intoPJ byαi =ǫi−ǫi+1. We write as usual Q+
J for ⨁
i∈J
Z≥0αi.
36 S.-J. KANG, M. KASHIW ARA, M. KIM
Note that, for β∈ Q+
J and ν∈Jβ, we have
(τa+1τaτa+1−τaτa+1τa)e(ν) =
{
±e(ν) if νa =νa+2 =νa+1∓ 1,
0 otherwise.
Also, we have
Pij(u,v ) = (u−v)δ(j=i+1)ci,j(u,v ).
We will choose ci,j(u,v ) satisfying (
3.1.1) later in Theorem 4.6.5. Recall that the
functor
F : ⨁
β∈Q+
J
Modgr(R(β))→ Mod(U′
q(ˆslN ))
deﬁned in (
3.2.1) is exact (Theorem 3.3.3).
