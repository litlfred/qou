---
doc_id: arxiv-math-0611521v1
doc_title: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP"
section_id: sec-006-21-general-facts
section_title: "General facts"
section_number: 2.1
pages: 8-10
source_pdf: 0611521v1.pdf
source_sha256: 65fcd77b7b0a208e
doc_brief: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP — We describe an explicit construction of galoisian Stokes op erators for irregular linear q-difference equations."
---
Notations, general conventions. We ﬁx q∈ C such that|q| > 1. We then deﬁne the automorphism σq on
various rings, ﬁelds or spaces of functions by putting σq f (z) = f (qz). This holds in particular for the ring
C{z} of convergent power series and its ﬁeld of fractionsC({z}), the ring C[[z]] of formal power series and
its ﬁeld of fractions C((z)), the ring O(C∗,0) of holomorphic germs and the ﬁeldM (C∗,0) of meromorphic
germs in the punctured neighborhood of 0, the ring O(C∗) of holomorphic functions and the ﬁeld M (C∗)
of meromorphic functions on C∗; this also holds for all modules or spaces of vectors or matrices over these
rings and ﬁelds. For any such ring (resp. ﬁeld) R, the σq-invariants elements make up the subring (resp.
8
subﬁeld) Rσq of constants. The ﬁeld of constants of M (C∗,0) and that of M (C∗) can be identiﬁed with a
ﬁeld of elliptic functions, the ﬁeld M (Eq) of meromorphic functions over the complex torus Eq = C∗/qZ.
We shall write a = π(a)∈ Eq for the image of a∈ C∗ by the natural projection π : C∗→ Eq, and [a;q] =
aqZ = π−1(a)⊂ C∗ for the preimage of a in C∗, a discrete q-spiral. These notations extend to subsets
A⊂ C∗: A = π(A)⊂ Eq and [A;q] = AqZ = π−1(A)⊂ C∗.
Categories. Let K denote any one of the forementioned ﬁelds of functions. Then , we write Dq,K =
K
⟨
σ,σ−1⟩
for the ¨Ore algebra of non commutative Laurent polynomials characterized by the relationσ.f =
σq( f ).σ. We now deﬁne the category of q-difference modules in three clearly equivalent ways:
Di f f Mod(K,σq) = {(E,Φ ) / E a K-vector space of ﬁnite rank ,Φ : E→ E a σq-linear map}
= {(Kn,Φ A) / A∈ GLn(K),Φ A(X) = A−1σqX}
= { ﬁnite length left Dq,K-modules}.
For instance, a morphism from MA = (Kn,Φ A) to MB = (Kn,Φ B), where A∈ GLn(K) and B∈ GLp(K), is
a F∈ Mp,n(K) such that (σq)FA = BF. Then, Di f f Mod(K,σq) is a C-linear abelian rigid tensor category,
hence a tannakian category. Moreover, all objects in Di f f Mod(K,σq) have the form Dq,K/Dq,KP. In the
case of K = C({z}), the category Di f f Mod(K,σq) will be written E (0) (for “equations near 0”).
Vector bundles and ﬁber functors. To any module MA in E (0), one can associate a holomorphic vector
bundle FA over Eq:
FA = (C∗,0)× Cn
(z,X)∼ (qz,A(z)X)→ (C∗,0)
z∼ qz = Eq.
This is the usual construction from equivariant bundles exc ept that the germ (C∗,0) is only endowed with
the action of the semigroup q−N instead of a group; correspondingly, the projection map is not a covering.
The pullback ˜FA = π∗(FA) over the open Riemann surface C∗ is the trivial bundle C∗× Cn, but with
an equivariant action by qZ. The OEq-module of sections of FA (also written FA) is the sheaf over Eq
deﬁned by: FA(V ) ={solutions of σqX = AX holomorphic over π−1(V )}. ¿From these two descriptions,
the following is immediate:
Proposition 2.1 This gives an exact faithful ⊗-functor M A↝ FA from E (0) to the category Fib (Eq) of
holomorphic vector bundles. Taking the ﬁber of ˜FA at a∈ C∗ yields a ﬁber functor ω (0)
a on E (0) over C.
Newton polygon. Any q-difference module M over C({z}) or C((z)), can be given a Newton polygon
N(M) at 0, or, equivalently, a Newton function rM sending the slope 1 µ∈ S(M)⊂ Q to its multiplicity
rM(µ)∈ N∗ (and the µ out of the support S(M) to 0).
For instance, theq-difference operator L = qzσ2− (1 +z)σ +1∈ Dq,K gives rise to theq-difference equation
qzσ2
q f− (1 + z)σq f + f = 0, of which the so-called Tschakaloff series ∑ n≥0 qn(n−1)/2zn is a solution (it is a
natural q-analogue of the Euler series). By vectorisation, this equa tion gives rise to the system σqX = AX,
where A =
(
z−1 z−1
0 1
)
, and to the module M = MA. The latter is isomorphic to Dq,K/Dq,K ˆL, where
ˆL = σ2− (z + 1)σ + z = (σ− z)(σ− 1) is the dual operator of L. We respectively attach to σ− z and σ− 1
the slopes−1 and 0 and take S(M) ={−1,0}, with multiplicities rM(−1) = rM(0) = 1.
1It should be noted that the slopes deﬁned and used in the present paper are the opposites of the slopes deﬁned in previous papers.
9
