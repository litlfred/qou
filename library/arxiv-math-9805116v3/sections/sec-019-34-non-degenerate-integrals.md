---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-019-34-non-degenerate-integrals
section_title: "Non-degenerate integrals"
section_number: 3.4
pages: 22-29
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
Until now we have not been able to decide whether the WHM Theor em of Subsection 3.2
implies the existence of non-degenerate integrals, as it do es in case of Hopf algebras. In the
present subsection we will show that the existence of non-de generate integrals in the WHA ˆA
is equivalent to the existence of non-degenerate functiona ls on A, i.e. that A is a Frobenius
algebra. As a byproduct we obtain that the class of Frobenius WHAs is selfdual.
The space IR of right integrals can be viewed as a K-module, as a left AL-module ALIR
by left multiplication, and as a left A-module AIR since it is a left ideal of A. From the latter
point of view AIR is the dual of the trivial right A-module, AIR ∼= Hom ( ˆAL
A,AA), by a twisted
version of Lemma 3.3. As a K-module IR has ˆIL as its K-dual, ˆIL ∼= Hom (K IR, KK) the
isomorphism being given by the restriction of the canonical pairing (see Corollary 3.10). The
next Lemma shows that ˆIL is also the AL-dual of IR with right AL-module structure precisely
the one needed in Example 3.8, i.e. λ ·xL =S(xL)⇀λ .
Lemma 3.14 The AL-valued bilinear form
( , )AL : IR × ˆIL → AL , (r,λ )AL =λ⇀r (3.32)
22
provides an isomorphism of right AL-modules
(ˆIL)AL
→ Hom (ALIR, ALAL) , λ ↦→(r ↦→(r,λ )AL ) , (3.33)
i.e. (ˆIL)AL
is the AL-dual of ALIR.
Proof: At ﬁrst verify the following properties of the AL-valued bilinear form.
(xL ·r,λ )AL = xL(r,λ )AL (3.34a)
(r,λ ·xL)AL = ( r,λ )ALxL (3.34b)
(r,λ )AL = 0 ∀r ∈ IR ⇒ λ = 0 (3.34c)
The ﬁrst two are simple WHA identities. The third one follows from the relation ε((r,λ )AL ) =
⟨λ,r ⟩and from non-degeneracy of the canonical pairing ⟨, ⟩on ˆIL × IR (Corollary 3.10). Now
properties (a) and (b) tell us that λ ↦→(.,λ )AL is indeed the required AL-module map and (c)
ensures that it is injective. In order to show that it is surje ctive it is suﬃcient to ﬁnd ﬁnite
sets of elements {ra} in IR and {λa} in ˆIL such that
∑
a
(r,λa)AL ra = r ∀r ∈ IR . (3.35)
For if such elements exist then any f ∈ Hom (ALIR, ALAL) can be written as f =∑
aλa ·f (ra).
As a matter of fact
f (r) = f (
∑
a
(r,λa)AL ·ra) =
∑
a
(r,λa)AL f (ra) = (r,
∑
a
λa ·f (ra))AL
for all r ∈ IR. Now we claim that a pair of dual bases {ra} of IR and {λa} of ˆIL, in the sense
of K-duality, i.e. ⟨λa,rb⟩=δab, also satisﬁes (3.35). As a matter of fact for λ ∈ ˆIL we have
⟨λ,
∑
a
(λa⇀r )ra⟩=ε(
∑
a
(λa⇀r )(λ⇀ra)) =
∑
a
⟨λa,r (λ⇀ra)⟩=
=
∑
a
⟨λa,r (S(ra)↼ ˆS−1(λ))⟩=
∑
a
⟨λa
(1),r ⟩ ⟨ˆS−1(λ)λa
(2),S (ra)⟩=
=
∑
a
⟨λλa
(1),r ⟩ ⟨λa
(2),S (ra)⟩= ⟨λ
[ ∑
a
S(ra)⇀λa
]
, r⟩= ⟨λ,r ⟩
where in the last equality (3.21) has been used. Q.e.d.
Notice that Eqn(3.35) means that ALIR is ﬁnitely generated projective 3. Therefore by a
general result (see e.g. [5])
ˆIL ⊗
AL
IR ∼= End ALIR . (3.36)
On the other hand the isomorphism α of the WHM Theorem, if restricted to ˆIL ⊗
AL
IR, yields
an isomorphism onto ˆAL. Thus we have the composition
E: AL − → ˆAL α−1
− →ˆIL ⊗
AL
IR − →End ALIR (3.37)
3Although this is clear from the fact that AL is semisimple, constructing the concrete bases λa, r a was not
in vain since it will help to compute the commutant in (3.38).
23
of isomorphisms. Evaluating it explicitely we obtain
r · E (xL) = r ·

∑
ij
S2(bi)⇀ (βiβj(ˆ1↼xL)) ⊗ bj

 =r ·

∑
j
ˆL(βj(ˆ1↼xL)) ⊗bj

 =
= r · (
∑
a
λa ⊗S(xL)ra) =
∑
a
(r,λa)ALS(xL)ra =
= S(xL)r ∀r ∈ IR, xL ∈AL . (3.38)
This proves our next
Proposition 3.15 The left modules ALIR and ARIR are faithful and the endomorphism alge-
bra of ALIR consists of left multiplications with elements of AR. Therefore
End ALIR ∼= AL , as algebras. (3.39)
The set SecAL of equivalence classes of simple left AL-modules will be called the sectors
of AL. For a ∈ S ecAL let Va be a simple module from the class a and let Da = End Va
be the corresponding division algebra. Then by the Wedderbu rn structure theorem AL ∼=
⊕aMna(Da). Let ma denote the multiplicity of Va in the semisimple module ALIR. Then
End ALIR ∼= ⊕aMma (Da) which is, by the Proposition, isomorphic to AL. This is possible only
if there is a permutation
˜: SecAL → SecAL, such that n˜a =ma and D˜a = Da . (3.40)
This means that IR, as an AL-End ALIR bimodule, can be identiﬁed with a direct sum of
matrices,
ALIR ∼= ⊕a Mat (na ×ma, Da) . (3.41)
This allows us to compute its K-dimension and apply the Cauchy-Schwarz inequality to obta in
the bound
dimK IR =
∑
a
(dimK Da)nama ≤
∑
a
(dimK Da)n2
a = dim KAL . (3.42)
Equality holds here iﬀ ma =na,a ∈ SecAL, i.e. iﬀ ALIR ∼= ALAL. Now we are ready to prove
the following
Theorem 3.16 LetA be a WHA over the ﬁeld K. Then the following conditions are equiva-
lent.
i) A is a Frobenius algebra;
ii) dimK IR = dim K AL;
iii) Non-degenerate integrals exist in A;
iv) ˆA is a Frobenius algebra.
Proof: (i)⇒(ii) If AA ∼= A ˆA then their invariants I(AA) = IL and I(A ˆA) = ˆAL, respectively
(see Scholium 3.5), are isomorphic as K-spaces. (ii)⇒(iii) As we have seen above the K-space
isomorphism of IR and AL implies that ALIR is isomorphic to the left regular module ALAL.
Since the latter is cyclic, there exists a cyclic vector r ∈ ALIR. Thus l := S(r) is cyclic in
24
(IL) ˆAL
. As a matter of fact IL = S(IR) = S(ALr) = lAR = ˆS( ˆAL)⇀l . Now interchanging
the roles of A and ˆA in the WHM Theorem
A =α(IL ⊗
ˆAL
ˆA) = ˆS( ˆA)⇀ IL = ˆS( ˆA)⇀ ( ˆS( ˆAL)⇀l ) = ˆA⇀l ,
hencel is a non-degenerate left integral in A. (iii)⇒(iv) is obvious since l is a non-degenerate
functional on ˆA. (iv)⇒(i) Repeat the arguments above from (i) to (iv) with A replaced by
ˆA. Q.e.d.
Weak Hopf algebras satisfying any one of the conditions of th e above Theorem will be called
Frobenius WHAs. Note that since semisimple algebras are Frobenius, in a sem isimple WHA
there exist both normalized and non-degenerate integrals, although there may be no integral
sharing both properties. 4
As an immediate consequence of the above considerations we h ave
Scholium 3.17 The following properties for l ∈ IL (r ∈ IR) are equivalent:
i) l (r) is non-degenerate;
ii) l is separating for IL
AL,R (r is separating for AL,R IR );
iii) l is cyclic for IL
AL,R (r is cyclic for AL,R IR).
In a Frobenius WHA A the group of invertible elements AR
× of AR acts on the set IL
∗ (A)
of non-degenerate left integrals transitively and freely. Similar statement holds for the non-
degenerate right integrals IR
∗ ,
IL
∗ =lAR
× , IR
∗ =AL
×r (3.43)
for any l ∈ IL
∗ and r ∈ IR
∗ . Similar relation for the dual integrals shows that there ar e one-
to-one correspondences between non-degenerate integrals of A and of ˆA. The Theorem below
selects a distinguished ”natural” one-to-one corresponde nce.
Theorem 3.18 LetA be a WHA and l ∈ IL(A) be a left integral. If there exists a λ ∈ ˆA such
that λ⇀l = 1 then it is unique, it is a left integral in ˆA, and both l and λ are non-degenerate.
Moreoverl⇀λ = ˆ1. Such a pair (l,λ ) will be called a dual pair of left integrals.
Similarly, elements r ∈ IR
∗ and λ ∈ ˆIL
∗ are in one-to-one correspondence by either one of
the equivalent relations λ⇀r = 1 or λ↼r = ˆ1.
Proof: By Lemma 3.2.d) if l is a left integral such that λ⇀l = 1 then 5 lR ◦λL =S. Since
S is invertible, both lR and λL are invertible, i.e. l and λ are non-degenerate and λ is unique.
To show that λ ∈ IL( ˆA)
ϕλ⇀l = ϕ⇀ 1 = ˆ⊓L(ϕ)λ⇀l , ϕ ∈ ˆA
4As an example consider M2(Z Z2), the semisimple algebra of two by two matrices over the ﬁeld of mod2
residue classes. Fix a set of matrix units {eij} and introduce the coproduct ∆( eij): = eij ⊗ eij. Then we have
two normalized left integrals lj =
∑
i eij for j = 1, 2 neither of which is non-degenerate. The only non-degenera te
left integral is l = l1 + l2 for which however ⊓L(l) = 0.
5Here we use the standard notations fL, fR: A → ˆA deﬁned by fL(x) := f ↼ x and fR(x) := x ⇀ f for any
f ∈ ˆA.
25
suﬃces since lR is a bijection. It remains to show that l⇀λ = ˆ1 which eventually justiﬁes the
term ”dual” left integral. For l ∈ IL(A) and λ ∈ ˆA we have
λ⇀l = 1 ⇔ xl(1)⟨λ,l (2)⟩=x x ∈A
⇔ ⟨ λ,xl (2)⟩S−1(l(1)) = x x ∈A
⇒ ⟨ l⇀λ,x ⟩=ε(x) x ∈A
⇔ l⇀λ = ˆ1
The duality between ˆIL and IR follows from the above duality between ˆIL and IL by
passing from A to Aop. The other two twisted versions of the Theorem are not spelle d out
explicitely. They can also be obtained by applying the antip ode to the above relations. Q.e.d.
Recall that the quasibasis of a non-degenerate functional f onA is an element ∑
iai ⊗bi ∈
A ⊗A such that (cf. [23])
∑
i
f (xai)bi =x =
∑
i
aif (bix), x ∈A . (3.44)
(If K is a ﬁeld then this just means that {bi} is a K-basis of A and {ai} is its dual basis
w.r.t. f .) In other words ∑
iai ⊗bi is simply the expression ∑
if −1
R (βi) ⊗bi of the inverse of
fR:A → ˆA as an element of A ⊗A. The index of f is then deﬁned by Index f :=∑
iaibi which
belongs to Center A. Now let ( l,λ ) be a dual pair of left integrals. Then the quasibasis of λ is
l(2) ⊗S−1(l(1)) and
Indexλ =S−1 ◦ ⊓L(l) ∈ZR . (3.45)
In particular a non-degenerate left integral l is normalized if and only if its dual has index 1.
3.5 2-sided non-degenerate integrals
The space of 2-sided integrals I(A) := IL(A) ∩ IR(A) in a weak Hopf algebra A is a possibly
zero subalgebra of A. The assumption I(A) ⁄= 0 is independent of the assumption IL
∗ (A) ⁄= ∅
since already Hopf algebras provide examples [21] for IL
∗ (A) ⁄= 0 and I(A) = 0. In this
Subsection we will make the stronger assumption I∗(A) := IL
∗ (A) ∩ I (A) ⁄= ∅ and study some
of the consequences. The main result will be ﬁnding a criteri on for a WHA to be a symmetric
algebra.
At ﬁrst we observe that if a non-degenerate 2-sided integral j exists then the subspace of
2-sided integrals is obtained from j by the action of the central subalgebra ZR =AR ∩CenterA,
I =jZ R, I∗ =jZ R
× for any j ∈ I∗ . (3.46)
As a matter of fact if i ∈ I theni is a left integral therefore there exists an xR ∈ AR such that
i = jxR. Thus for all y ∈ A we have jxR ⊓R (y) = jxRy = j ⊓R (xRy). Since j is separating
for the right AR-action, xR ⊓R (y) = ⊓R(xRy). Therefore
xRS(y) = xRS(y(1))y(2)S(y(3)) = S(y(1))xRy(2)S(y(3)) = S(1(1)y)xR1(2) =S(y)xR
hence xR is central.
Next we recall some facts about ”modular automorphisms”. Le t A be a ﬁnite dimensional
Frobenius algebra over a ﬁeld K and let f :A →K be a non-degenerate functional. Then the
modular automorphism of f is deﬁned to be the unique θf ∈ AutA such that
f (xy) = f (yθf (x)) , x,y, ∈A . (3.47)
26
It is worth to give two other equivalent deﬁnitions of θ:
f↼x = θf (x)⇀f , x ∈A (3.48)
or simply
θf = f −1
R ◦fL . (3.49)
Since any two non-degenerate functionals f and g are related by g =x⇀f , with x ∈A×, the
equivalence class θA := [θf ] of θf modulo inner automorphisms is independent of the choice of
f . If A is a WHA which is Frobenius then one may ask the question wheth er θA = [S2].
Deﬁnition 3.19 A non-degenerate functional f :A →K over a WHA A is called a q-trace if
θf =S2.
In the term ”q-trace” the letter ”q” has no individual meanin g. One may as well read it as
”skew trace” although we do not denie that our motivation cam e from the theory of q-deformed
Hopf algebras.
Lemma 3.20 In a WHA A let l be a non-degenerate left integral. Then S(l) = l if and only
if its dual left integral λ is a q-trace.
Proof: θλ =S2 is equivalent to that the quasibasis of λ satisﬁes
l(2) ⊗S−1(l(1)) = S(l(1)) ⊗l(2) . (3.50)
Applying S to the second tensor factor we obtain ∆( l) = ∆( S(l)) which yields l =S(l) by the
existence of a counit. Q.e.d.
Lemma 3.21 If non-degenerate 2-sided integrals exist then all 2-sided integralsi ∈ I (A) are
S-invariant, S(i) = i.
Proof: If we can show only that the non-degenerate 2-sided integra ls are S-invariant then we
are ready since j =S(j) ∈ I ∗ implies S(jzR) = S(zR)j =zRj =jzR for all zR ∈ZR.
So let j ∈ I ∗. Then S(j) ∈ I ∗ thus there exists an invertible z ∈ZR such that S(j) = jz.
Let λ be the dual of j as a left integral. Then for arbitrary x ∈A and for zL =S−1(z−1)
zLS(x) = zL(λ↼x )⇀j = (λ↼x )⇀zLj = (λ↼x )⇀S −1(j)
S2(x)z−1 = j↼ ˆS−1(λ↼x ) = jL ◦ ˆS−1 ◦λL(x) = λ−1
R ◦λL(x) =
= θλ(x)
Therefore z−1 =θλ(1) = 1 and j is S-invariant. Q.e.d.
Theorem 3.22 The WHA A overK is a symmetric algebra if and only if it has non-degenerate
2-sided integrals and the square of the antipode is an inner a utomorphism.
Proof: Let A be a symmetric WHA, and τ ∈ ˆA be a non-degenerate trace. Then there
exists a unique i ∈A such that i⇀τ = ˆ1 = τ↼i . We claim that i is a 2-sided integral. As a
matter of fact
xi⇀τ = x⇀ ˆ1 = ⊓L(x)⇀ ˆ1 = ⊓L(x)i⇀τ
τ↼ix = ˆ1↼x = ˆ1↼ ⊓R(x) = τ↼i ⊓R (x)
27
so by non-degeneracy of τ , i ∈ I . This integral i is also non-degenerate: For any xR ∈ AR
one has ixR⇀τ = i⇀τ↼x R = ˆ1↼xR, hence i is separating for IL
AR so non-degenerate by
Scholium 3.17.
The innerness of S2 in a symmetric algebra follows if we can construct a non-dege nerate
functional on A the modular automorphism of which is S2. By Lemma 3.21 i isS-invariant so
by Lemma 3.20 χ, the dual left integral to i, is such a non-degenerate q-trace.
Conversely, let S2 = Ad g with some g ∈A× and i ∈ I ∗. Denoting the dual left integral of
i byχ again, g−1⇀χ is a non-degenerate trace. Q.e.d.
We close this Subsection with a result arising from assuming the existence of non-degenerate
2-sided integrals in both A and ˆA. Although the arising structure is reminiscent to that of th e
”distinguished grouplike element” in Hopf algebra theory i t is not a generalization of that.
Proposition 3.23 Let A be a WHA and assume that both I∗(A) and I∗( ˆA) are non-empty.
ThenS4 is inner and the square of θA is the identity in Out A. Moreover and more explicitely,
for ˆh ∈ I ∗( ˆA) there exist invertible elements aL ∈AL andαL ∈ ˆAL such that, with the notations
aR =S(aL) and αR = ˆS(αL), we have
AdaLa−1
R
= S4 (3.51)
AdaLaR = θ2
ˆh (3.52)
aLa−1
R ⇀ψ↼a La−1
R = αLαRψα−1
R α−1
L , ψ ∈ ˆA . (3.53)
Proof: Choose h ∈ I ∗(A) and ˆh ∈ I ∗( ˆA) and let λ be the dual of h and l be that of ˆh, as left
integrals. Deﬁne
aL = ˆh⇀h , α L =h⇀ ˆh . (3.54)
Then
ˆ1↼aL = ⟨ˆ1(1)ˆh,h ⟩ˆ1(2) = ⟨ˆh(1),h ⟩ˆh(2) ˆS(ˆh(3)) = ˆ⊓L(ˆh↼h ) = ˆS(ˆh↼h ) = αL (3.55)
and introducing aR and αR as above
laL =l↼αR =l↼ (ˆh↼h ) = h(l↼ ˆh) = h( ˆS2(ˆh)⇀l ) = h (3.56)
where q-trace property of l and ˆS-invariance of ˆh have been used. Similarly,
αR⇀l = h = laR (3.57)
aR⇀λ = ˆh = λαR (3.58)
λ↼aR = ˆh = λαL. (3.59)
Non-degeneracy of ˆh and h now imply invertibility of aL, aR, αL, and αR. Hence Eq(3.53)
readily follows.
We can now compute the modular automorphism of ˆh using the information θλ =S2.
ˆh↼x =aR⇀λ↼x =aRθλ(x)⇀λ ⇒ θˆh = AdaR ◦S2 (3.60)
Computing ˆS(ˆh↼x ) in two diﬀerent ways
ˆS(ˆh↼x ) = S−1(x)⇀ ˆh = ˆh↼θ −1
ˆh (S−1(x))
= ˆS(θˆh(x)⇀ ˆh) = ˆh↼S −1(θˆh(x))
28
yields
S−1 ◦θˆh =θ−1
ˆh ◦S−1 (3.61)
and ﬁnally
AdaL ◦S−2 = θˆh = Ad aR ◦S2 (3.62)
from which (3.51) and (3.52) follow immediately. Q.e.d.
