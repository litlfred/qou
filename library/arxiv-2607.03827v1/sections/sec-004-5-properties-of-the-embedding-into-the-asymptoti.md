---
doc_id: arxiv-2607.03827v1
doc_title: "AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS"
section_id: sec-004-5-properties-of-the-embedding-into-the-asymptoti
section_title: "Properties of the embedding into the asymptotic algebra"
section_number: 5
pages: 17-22
source_pdf: 2607.03827v1.pdf
source_sha256: 965d69603381942a
doc_brief: "AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS — The theory of affine cellular algebrasAis extended to incorporate their asymptotic algebras ˆA, clarifying unexpected differences between classical"
---
In this section we will provide further information related with the embedding into the asymptotic
algebra by considering the restriction functor associated to the embeddingA→bA. Moreover we will
derive a geometric property of the embedding. This enhances in particular Theorems B and C.
Throughout this section,Ais an affine cellular algebra with cell chain{Ji : 1≤i≤n}as in (10) and
cell data(Bi,σi,∆i,ψ (i),αi)as in (11), withd i = rankBi(∆i), such that no determinantdet(ψ(i))is a
zero-divisor inBi and such that the embeddingΘ :A→bAinto its asymptotic algebrabA= bAn×···× bA1,
with bAk =M dk(Bk), is given by (15), i.e.Θ(a) = (Θn(a),...,Θ 1(a)), for alla∈A. Then, fora∈J ′
k,
we haveΘk =α k(a)ψ(k), wherea=a+J k−1. The embeddingΘinduces a restriction functor
F: bA−Mod→A−Mod,
where forX∈ bA−Modthe additive groupXbecomes a leftA-moduleF(X)by letting
(20)a·x:= Θ(a)x,∀a∈A, x∈X.
All components bAk =M dk(Bk)are unital algebras, with identityI dk. The identity element of bAis
(Idn,...,I d1). We will identify elementsa∈ bAk with the elementaIdk = (0,···,a,···,0)∈ bAand any
left bA-moduleXdecomposes intoX=X n×···×X 1, whereXk = bAIdkX= bAkXis a left bAk-module.
Hence, any element ofXcan be uniquely written asx= (x n,...,x 1)withx i∈X i and theA-action
ofa∈Aonx∈F(X)is given bya·x= Θ(a)x= (Θ n(a)xn,...,Θ 1(a)x1). Moreover, for bA-modules
XandY,Hom bA(X,Y) = Qn
k=1 Hom bAk
(Xk,Yk).Recall that by definition of an affine cellular algebra
A= Ln
i=1J′
i ask-module, whereJ i =L
j≤iJ′
j.
Lemma 13.Let1≤k,l≤nand assume thatJ k/Jk−1 is idempotent. The following statements hold
for an bAk-moduleXand an bAl-moduleY.
(1)J ′
k·X=X.
(2)Hom A(F(X),F(Y)) = 0, ifk <l.
(3)Hom A(F(X),F(Y)) = Hom bA(X,Y), ifk=l.
Proof.Note, that theA-action onXis completely determined byΘ k, i.e.a·x= Θ(a)x= Θ k(a)x,
for anya∈Aandx∈X, because bAiX= 0, fori̸=k. Moreover, sinceJ k/Jk−1 is idempotent,
bAkψ(k)bAk = bAk holds.
(1) Using (14), we haveJ′
k·X= Θ k(J′
k)bAkX= bAkψ(k)bAkX= bAkX=X.
(2) Letf:F(X)→F(Y)beA-linear. By (1) andΘ l(J′
k) = 0, forl>k:
f(X) =f(J ′
k·X) =J ′
k·f(X)⊆J ′
k·Y= Θ l(J′
k)Y= 0.
(3) We always haveHombA(X,Y)⊆Hom A(F(X),F(Y)). Assumek=land letf:F(X)→F(Y)
beA-linear. We need to show thatfis bA-linear. Sinceα k(Jk/Jk−1) = bAk, for anyy∈ bAk, there
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 18
exists˜y∈J ′
k such thatΘk(˜y) =αk(˜y)ψ(k) =yψ (k).In particular,a(˜y·z) =ayψ (k)z=fay·z, for any
a,y,z∈ bAk. Furthermore, sincebAkψ(k)bAk = bAk, there exist elementsyi,zi∈ bAk, such that
(21)I dk =
tX
i=1
yiψ(k)zi =
tX
i=1
˜yi·zi.
Thus, any elementa∈ bAk can be written asa= Pt
i=1fayi·zi. Then, forx∈X:
f(ax) =f
 tX
i=1
fayi·zix
!
=
tX
i=1
fayi·f(z ix) =
tX
i=1
a˜yi·f(z ix) =af
 tX
i=1
˜yi·zix
!
=af(x).
Hencefis bAk-linear and alsobA-linear, since bAiX= 0, fori̸=k.□
A module is said to betorsionlessprovided it can be embedded into a projective (free) module.
Lemma 14.Let1≤l < k≤m,Xa bAk-module andYa torsionless bAl-module. Ifdet(ψ (l))is a not
a zero-divisor inBl, thenHomA(F(X),F(Y)) = 0.
Proof.Sincedet(ψ (l))is a not a zero-divisor inBl,ann P (ψ(l)) = 0, for any freebAl-moduleP= bA(I)
l . In
particular,ann Y (ψ(l)) = 0, for any torsionlessbAl-moduleY.
Letf∈Hom A(F(X),F(Y)). Thenψ (l)f(X)⊆J ′
l·f(X) =f(J ′
l·X) =f(Θ k(J′
l)X) = 0, since
Θk(J′
l) = 0asl<k. Thus,f(X)⊆ann Y (ψ(l)) = 0andf= 0.□
LetT( bA)denote the class of torsionless leftbA-modules. The restriction functorF:T( bA)→A−Mod
is fully faithful on this subcategory.
Theorem 15(Theorem B).LetAbe an affine cellular algebra with an affine cell chain such that all
occurring affine cell ideals are idempotent and no determinant of their respective swich matrix is a zero-
divisor. Then the embeddingΘ :A→ bAinduces a fully faithful restriction functorF:T( bA)→A−Mod,
between torsionlessbA-modules andA-modules.
Proof.LetX= Qn
i=1Xi andY= Qn
i=1Yi be any torsionless bA-modules. AsJ k/Jk−1 is idempotent,
HomA(F(Xk),F(Y l)) = 0for allk < l, by Lemma 13. By Lemma 14,Hom A(F(Xk),F(Y l)) = 0for
k>l. Furthermore,Hom A(F(Xk),F(Y k) = Hom bA(Xk,Yk), for allk, by Lemma 13. Therefore,
HomA(F(X),F(Y)) =
nM
k,l=1
HomA(F(Xk),F(Y l)) =
nM
k=1
Hom bA(Xk,Yk) = Hom bA(X,Y).
□
In the second part of this section we will compare the primitive spectrum of an affine cellular algebra
with the primitive spectrum of its asymptotic algebra. In [2] Baum and Nistor determined the periodic
cyclic homology of the Iwahori-Hecke algebraHq at a proper root of unityq. Their method is based
on a general result, which states that a map calledweakly spectrum preserving morphismof finite type
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 19
algebras induces an isomorphism in periodic cyclic homology. Furthermore, they showed that Lusztig’s
embeddingϕ q :H q →J, of the Iwahori–Hecke algebraH q into Lusztig’s asymptotic algebraJis
weakly spectrum preserving. Here we will show that the embedding of an affine cellular algebra into its
asymptotic algebra is weakly spectrum preserving if and only if all affine cell ideals appearing in the
affine cell chain of the algebra are idempotent ideals (not necessarily generated by idempotent elements).
LetRbe a ring and denote byPrim(R)the set of (left) primitive ideals ofR, where an idealPis
called left primitive if it is the annihilator of a simple leftR-module. Over a not necessarily unital ring
R, a moduleVis said to be simple ifRV̸= 0andRv=Vfor allv∈V\{0}.
Definition 16([2]).Ak-algebra homomorphismΘ :R→Sbetween two (not necessarily unital)
k-algebrasRandSis calledspectrum preservingif for anyP∈Prim(S),Θ −1(P)is contained in a
unique primitive ideal ofRand the resulting mapΘ∗ : Prim(S)→Prim(R)is a bijection.
GivenBan affine commutativek-algebra,n≥1andψ∈M n(B), we denote, as above, the swich
algebra(M n(B),ψ)by ^Mn(B). The map
φ: ^Mn(B)→M n(B), x7→φ(x) =xψ
is a homomorphism of (not necessarily unital)k-algebras. We will examine, whenφis spectrum preserv-
ing. A description of simple ^Mn(B)-modules in terms of the simpleMn(B)-modules has been obtained
in [18, Theorem 3.10] and will allow us to obtain the following correspondence between the primitive
spectra of the two rings under the hypothesis that^Mn(B)is idempotent. The correspondence from [18]
is revised in the proof of the following proposition for the sake of completeness.
Note that by [18, Proposition 3.8], any leftM n(B)-moduleVcarries a natural structure of left
^Mn(B)-module, by defining
˜a·v:=φ(a)v=aψv,∀˜a∈ ^Mn(B), v∈V.
We denote this left ^Mn(B)-module structure onVbyV φ.
Proposition 17.LetBbe an affinekalgebra,ψ∈M n(B)and ^Mn(B) = (Mn(B),ψ). Assume ^Mn(B)
is idempotent. There is a one-to-one correspondence between the primitive spectrum ofMn(B)and the
one of ^Mn(B)given by
φ∗ : Prim(Mn(B))−→Prim( ^Mn(B))
P→ {X∈M n(B) :ψXψ∈P}
Proof.LetP∈Prim(M n(B)). ThenPis a maximal ideal ofM n(B)andP=M n(m)for somema
maximal ideal ofB.
LetVbe a simpleM n(B)-module such thatP= ann Mn(B)(V). As above,V φ is a ^Mn(B)-module.
Note thatann Vφ(In) = annV (ψ)is an ^Mn(B)-submodule ofV φ and considerV φ/annVφ(In). IfV φ =
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 20
annVφ(In), thenψV= 0. As ^Mn(B)is idempotent,M n(B)ψMn(B) =M n(B). AsVis a simple
Mn(B)-module, it would follow thatV=M n(B)V=M n(B)ψV= 0, a contradiction. Therefore
Vφ̸= annVφ(In). Also ^Mn(B)(Vφ/annVφ(In))̸= 0. Now takeWan ^Mn(B)-submodule ofV φ properly
containingann Vφ(In)andw∈W\ann Vφ(In).We have thatM n(B)ψw̸= 0is aM n(B)-submodule of
V, henceM n(B)ψw=VandV φ =V=M n(B)ψw= ^Mn(B)·w⊆W. Hence
Vφ/annVφ(In)
is a simple ^Mn(B)-module and
ann ^Mn(B)
 
Vφ/annVφ(In)

={X∈M n(B) :Xψv∈ann Vφ(In),∀v∈V}
={X∈M n(B) :ψXψv= 0,∀v∈V}.
Therefore
(22)ann ^Mn(B)
 
Vφ/annVφ(In)

={X∈M n(B) :ψXψ∈P}
is a primitive ideal of^Mn(B).
LetQ∈Prim( ^Mn(B)andEa simple left ^Mn(B)-module such thatQ= ann ^Mn(B)(E). Consider the
left ^Mn(B)-module structureMn(B)φ onM n(B). AsEis simple,E= ^Mn(B)efor anye∈E\{0}. As
in [18, Proposition 3.10] considerq:M n(B)φ→Esuch thatq(r) = ˜re. Recall, that the product in
^Mn(B)is defined as˜a˜b= gaψb, for any˜a,˜b∈ ^Mn(B). Given˜a∈ ^Mn(B),b∈M n(B)
˜aq(b) = ˜a(˜be) = (˜a˜b)e= (gaψb)e=q(aψb) =q(˜a·b).
Soqis a ^Mn(B)-epimorphism and asEis simple,Ker(q)is a maximal ^Mn(B)-submodule ofM n(B)φ.
LetZbe the centre ofM n(B)and considerZKer(q)that containsKer(q). Note that
˜a·(zx) =aψzx=z(˜a·x)∈ZKer(q),∀a∈M n(B),z∈Z,x∈Ker(q).
HenceZKer(q)is an ^Mn(B)-submodule ofMn(B)φ that contains the maximal submoduleKer(q). Thus
Ker(q) =ZKer(q)orZKer(q) =M n(B). AssumeZKer(q) =M n(B), then
E=q(M n(B)) =q( ^Mn(B)·M n(B)) =q(M n(B)ψZKer(q)) = ^Mn(B)Zq(Ker(q)) = 0
a contradiction. Therefore,Ker(q) =ZKer(q)andKer(q)is aZ-module, as well asE ∼=Mn(B)/Ker(q).
As aZ-module,Eis finitely generated and for everym∈MaxSpec(Z),mEis an ^Mn(B)-module, so
mE= 0ormE=E. IfmE=Efor allm∈MaxSpec(Z)using localisation and Nakayama’s Lemma, we
would haveE= 0[1, Proposition 3.8]. Hence there ism, a maximal ideal ofZ=Z(M n(B))∼=B, such
thatmE= 0. ThusM n(m)⊆Ker(q)andqinduces aZ-epimorphismq ′ :M n(B)/Mn(m)−→E. Also
q′ is a ^Mn(B)-homomorphism from(Mn(B)/Mn(m))φ toE. Note thatmunder the above conditions is
unique.
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 21
As anM n(B)-module,M n(B)/Mn(m)∼= V1⊕···⊕V n a direct sum of copies of a simpleMn(B)-
modules with annihilatorMn(m). Sinceq ′̸= 0, there isi∈{1,...,n}such thatq ′(Vi)̸= 0. For such
ani,Ker(q ′|(Vi)φ) = ann (Vi)φ(In), indeed ifx∈Ker(q ′)∩(V i)φ andψx̸= 0,M n(B)ψx=V i, forVi is
a simpleM n(B)-module, and so ^Mn(B)x= (V i)φ andq ′((Vi)φ) =q ′( ^Mn(B)x) = ^Mn(B)q′(x) = 0, a
contradiction. ThusKer(q ′)∩V i⊆ann (Vi)φ(In). Ifx∈V i is such thatψx= 0then ^Mn(B)q′(x) =
q′( ^Mn(B)x) =q ′(Mn(B)ψx) = 0. SinceEis a simple ^Mn(B)-module, ifq(x)̸= 0, ^Mn(B)q(x)would
beE, hencex∈Ker(q ′). It follows that, as an ^Mn(B)-module,Eis isomorphic to(V i)φ/ann(Vi)φ(In),
so by (22)
Q= ann ^Mn(B)(E) = ann ^Mn(B)((Vi)φ/ann(Vi)φ(In)) ={X∈M n(B) :ψXψ∈M n(m)}.
LetP 1,P 2 be distinct elements ofPrim(M n(B)). SinceP 1,P 2 are maximal ideals,P 1 +P 2 =
Mn(B). AsP 1 ⊆φ ∗(P1)andP 2 ⊆φ ∗(P2), ifφ ∗(P1) =φ ∗(P2),M n(B) =P 1 +P 2 ⊆φ ∗(P1)and
ψMn(B)ψ⊆P 1. By hypothesis ^Mn(B)is idempotent, soM n(B)ψMn(B) =M n(B)andM n(B) =
Mn(B)ψMn(B)ψMn(B)⊆P 1 a contradiction, soφ∗ is injective.□
Proposition 18.The ring homomorphismφ: ^Mn(B)→M n(B)is spectrum preserving if and only if
^Mn(B)is idempotent.
Proof.Assume first that ^Mn(B)is not idempotent. It follows by [5, Proposition 2.5(6)] that there is a
maximal idealmofBcontaining the ideal generated by all entries ofψ. ConsideringM n(m), maximal
ideal ofM n(B), hence primitive, it follows thatφ( ^Mn(B)) =M n(B)ψ⊆M n(m), or in other words,
φ−1(Mn(m)) = ^Mn(B). Thus,φ −1(Mn(m))is not contained in any primitive ideal of ^Mn(B)andφ
cannot be spectrum preserving, proving the only if part of the statement.
Assumenowthat ^Mn(B)isidempotent, takeP∈Prim(M n(B))andconsiderthebijectionφ ∗ between
Prim(Mn(B))andPrim( ^Mn(B)), as in Proposition 17. By definition
P⊆φ −1(P) ={X∈M n(B) :Xψ⊆P}⊆φ ∗(P).
We need to show thatφ∗(P)is the unique primitive ideal containingφ−1(P). Suppose there exists a
primitive idealQ∈Prim( ^Mn(B)), such thatφ−1(P)⊆Q. By Proposition 17,Q=φ ∗(P1), for some
P1∈Prim(M n(B)). In particular,P 1⊆φ −1(P1)⊆Q. Hence,P+P 1⊆φ −1(P) +φ −1(P1)⊆Q.
IfP̸=P 1, then as both are maximal ideals,P+P 1 =M n(B)and henceQ=M n(B), which is a
contradiction. Thusφ∗(P)is the only primitive ideal that containsφ−1(P).□
Definition 19([2]).A morphismΘ :R→Sofk-algebras is calledweakly spectrum preservingif, and
only if, there exist increasing filtrations0 =J0⊂J 1⊂···⊂J n =Rand0 =I 0⊂I 1⊂···⊂I n =S
of two-sided ideals such thatΘ(Ji)⊆I i and the induced morphismsJi/Ji−1→I i/Ii−1 are spectrum
preserving.
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 22
LetAbe an affine cellular algebraAwith cell chain0 =J 0 ⊂J 1 ⊂ ··· ⊂Jn =A, such that
each affine cell idealJ k/Jk−1 has cell datum(B k,σk,∆k,ψ (k),αk), i.e.J k/Jk−1 ∼= ∆k⊗Bk ∆′
k ∼= 
Mdk(Bk),ψ (k)
asA-bimodules, whered k = rank Bk(∆k). LetI k = bAn×···× bAk. Suppose no
determinantdet(ψ (k))is a zero-divisor, then by Theorem 10,Θis an embedding ofAinto its asymptotic
algebra bA=M dn(Bn)×···×M d1(B1). Using Proposition 18 we conclude
Theorem 20(Theorem C).LetAbe an affine cellular algebra with no determinantdet(ψ (i))being a
zero-divisor. Then the embeddingΘ :A→ bAis weakly spectrum preserving if and only if all affine cell
idealsJ i/Ji−1 are idempotent.
Now, [2, Theorem 9] implies invariance of periodic cyclic homology under a general assumption in
[2].
Corollary 21.LetAbe an affine cellular algebra with no determinantdet(ψ (i))being a zero-divisor
and allJ i/Ji−1 being idempotent. IfAis a finitely generated algebra over an affineC-algebra, then the
embeddingΘinduces an isomorphism of periodic cyclic homology.
In [2], algebras with these properties are called finite type algebras. Iwahori-Hecke algebras satisfy
this conditions, and in [2] the periodic cyclic homology of Iwahori Hecke algebras with parameter not
being zero and not a proper root of unity is determined by using the embeddingΘinto the asymptotic
algebra and its property of being weakly spectrum preserving. Cellular structures are not used in [2].
Corollary 21 also applies to Brauer algebras and more generally diagram algebras that are cellular in
the sense of [7] over an affine ground ring that is aC-algebra.
