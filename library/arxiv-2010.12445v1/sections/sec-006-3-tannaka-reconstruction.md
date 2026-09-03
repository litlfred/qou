---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-006-3-tannaka-reconstruction
section_title: "Tannaka Reconstruction"
section_number: 3
pages: 14-18
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect"
---
The goal of this section is to introduce the stack of ﬁber func tors and prove Theorem A. We
will work over a base ring R and denote by A a general R-algebra.
Deﬁnition 3.1. Let X be a quasi-compact ﬁber category over R, C ⊆ VectX a monoidal
subcategory and A an R-algebra. We deﬁne SMex R(C,A ) as the category of contravariant, R-
linear and strong monoidal functors Γ : C → ModA such that, for all geometric points Spec k − →
SpecA, Γ ⊗Ak are left exact in the sense of 1.3.
Let Y be another ﬁbered category over R. A functor C − →VectY is said a ﬁber functor if it
is a covariant, R-linear and strong monoidal functor which is right exact in t he sense of 1.4. We
denote by Fib X , C(Y) the category of ﬁber functors C → Vect(Y).
We deﬁne Fib X , C as the ﬁber category (not necessarily in groupoids) over R whose ﬁber over
an R-algebra A is Fib X , C(SpecA) and we call PC the functor
(3.1) PC : X − → FibX , C, (SpecA
s
− − → X) ↦− →(s∗ : C − →VectA)
The ﬁbered category Fib X , C is called the stack of ﬁber functors.
We will prove the following result and, in particular, Theor em A.
Theorem 3.2. Let X be a quasi-compact fpqc stack over R with quasi-aﬃne diagonal, A be an
R-algebra and C ⊆ VectX be a monoidal subcategory with duals that generates QCoh X . Then
the functors
(Spec AΓ , C − → X) (Γ : C − →ModA)
X (A) SMexR(C,A )
(s : SpecA − → X) ((s∗
|C)∨ : C − →VectA)
are well deﬁned and quasi-inverses of each other. In particular t he functor PC : X − → FibX , C is
an equivalence of stacks.
An immediate corollary and generalization of Theorem 3.2 is the following.
Corollary 3.3. Let X be a quasi-compact fpqc stack over R with quasi-aﬃne diagonal, C ⊆
VectX be a monoidal subcategory with duals that generates QCoh X and Y be a ﬁbered category
over R. Then the functor
Hom(Y, X ) − →FibX , C(Y), (Y
f
− − → X) ↦− →f ∗
|C : C − →Vect(Y)
is an equivalence of categories.
Proof. The map in the statement is obtained applying Hom (Y, −) to the functor PC : X − →
FibX , C, which is an equivalence by 3.2. □
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 15
Remark 3.4. Let R = k be a ﬁeld, X = ∆ be an aﬃne gerbe over k and C = Vect(∆) , which
is a k-Tannakian category. The stack of ﬁber functor Π C → Aﬀ /k usually associated with C is
deﬁned as
Π C(A) = {k-linear, exact and strong monoidal functors C → Vect(A)}
Sometimes it is also required that those functors are faithf ul. In any case, by [ Del90, Cor 2.10]
all those notions coincide and Π C = Fib∆ , C. Classical Tannaka’s reconstruction states that the
functor PC : ∆ → Π C = Fib∆ , C is an equivalence. On the other hand C = Vect(∆) generates
QCoh(∆) (see [ Del90, Corollary 3.9]), so that Theorem 3.2 can be seen of a generalization of
classical Tannaka’s reconstruction.
Remark 3.5. Even though we keep choosing a base ring R, the ﬁbered category Fib X , C →
Aﬀ /R → Aﬀ does not depend on this choice: we may have chosen R = Z orR = H0(OX ). Indeed
if A is an R-algebra and Γ : C → Mod(A) is an R-linear functor, then H 0(OX ) = End(OX ) →
End(A) = A makesA into a H 0(OX )-algebra and Γ into an H 0(OX ) linear functor.
Lemma 3.6. Let X be a quasi-compact ﬁbered category over R, C ⊆ VectX be a monoidal
subcategory with duals, Γ : C → Vect(A) be a contravariant, R-linear and strong monoidal functor
and set A = AΓ , C, f : Y = Spec A → X . Then
Ω A
E ≃ H0((f ∗E)∨)
and the map
Γ E ⊗A OY → (f ∗E)∨
induced by Γ → Ω A is surjective.
Proof. Set π : XA → X for the projection. We have monoidal isomorphisms
Ω A
E = Hom(π ∗E, A ) ≃ Hom(E,f ∗OY ) ≃ Hom(f ∗E, OY ) = H0((f ∗E)∨)
In particular we obtain a monoidal natural transformation Γ → Ω A = H0((f ∗−)∨) and therefore
a commutative diagram
Γ E ⊗ Γ E ∨ H0(f ∗E ∨) ⊗ H0(f ∗E)
Γ E⊗E ∨ H0(f ∗(E ⊗ E ∨)∨)
ω
Consider the evaluation e : E ⊗ E ∨ → O X , which is a map in C because C has duals. The
morphism H 0(f ∗O∨
X ) → H0(f ∗(E ⊗ E ∨)∨) maps 1 to an element that we denote by ψ . After the
usual identiﬁcations E ⊗ E ∨ ≃ End(E), the map ω become the evaluation
ω : H0(f ∗E) ⊗ HomY (f ∗E, OY ) − →EndY (f ∗E), ω (x ⊗φ)(y) = xφ(y)
while ψ become id f ∗E .
By hypothesis the vertical map on the left in the above diagra m is an isomorphism. By
functoriality, there exist x1,...,x n ∈ H0(f ∗E),φ 1,...,φ n ∈ Hom(f ∗E, OX ), coming respectively
from Γ E ∨ and Γ E , such that id f ∗E =ω (∑
ixi ⊗φ i). This implies that the map On
Y − →f ∗E given
by the global sections x1,...,x n is surjective. Since this map factors through Γ E ∨ ⊗A OY →f ∗E
by construction, this ends the proof. □
Lemma 3.7. Let X be a quasi-compact ﬁbered category over R and C ⊆ VectX be a monoidal
subcategory. If Γ ∈ SMexR(C,A ) and E ′ β
− → E → 0 or E ′′ α
− − → E′ β
− − → E →0 is a ﬁnite test
sequence in C then
0 → Γ E → Γ E ′ → Coker(Γ β ) → 0 and 0 → Coker(Γ β ) → Γ E ′′ → Coker(Γ α ) → 0
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 16
are short exact sequences of vector bundles over A.
In particular Γ , as well as any base change Γ ⊗AB for an A-algebraB, are left exact. Moreover
Γ ⊗AB ∈ SMexR(C,B ).
Proof. By [Aut19, Tag 046Y] if M →N is a map of vector bundles over A and, for all p ∈ SpecA,
the map M ⊗Ak(p) →N ⊗Ak(p) is injective then M →N is injective and N/M is ﬂat. As N/M
is ﬁnitely presented we can moreover conclude that N/M is a vector bundle. Applying this on
the map Γ E → Γ E ′ we obtain the ﬁrst exact sequence and that Coker (Γ β ) is locally free. Here
we use the deﬁnition of SMex, which also tell us that γ : Coker(Γ β ) → Γ E ′′ is injective on the
geometric point. Again we can conclude that this map is injec tive and that Coker (γ) is a vector
bundle. As Coker (γ) = Coker(Γ α ) this concludes the proof. □
By deﬁnition SMex R(C, −) is a stack (not necessarily in groupoids) over Aﬀ /R . The next
result tells us that this stack is just Fib X , C.
Proposition 3.8. Let X be a quasi-compact ﬁbered category over R and C ⊆ VectX be a
monoidal subcategory. Then
FibX , C → SMexR(C, −), Γ ↦− →Γ ∨
is an equivalence of stacks over Aﬀ /R .
Proof. If Γ : C → Vect(A) is a covariant (resp. contravariant), R-linear and strong monoidal
functor then Γ ∨ : C → Vect(A) is a contraviariant (resp. covariant) R-linear functor which
moreover has a strong monoidal structure. Moreover if B is an A-algebra we have
HomA(Γ E,A ) ⊗AB ≃ HomB(Γ E ⊗AB,B )
because Γ E ∈ Vect(A).
If Γ ∈ SMexR(C,A ) then Γ ∨ ∈ FibX , C(A) thanks to 3.7. Conversely assume Γ ∈ FibX , C(A).
We must show that (Γ ⊗Ak)∨ ≃ Γ ∨ ⊗Ak is left exact for all geometric points Spec k → SpecA.
As Γ ⊗Ak ∈ FibX , C(k) we can assume that A is a ﬁeld. The functor Γ ∨ : C → Vect(A) is left
exact because Γ is exact on all ﬁnite test sequences and the dual of a right exa ct sequence is
again exact. □
Proof. (of Theorem 3.2). The last claim follows from 3.8. Set π : XA → X for the projection.
Composing by π we obtain an equivalence XA(A) → X (A). Since X and therefore XA have aﬃne
diagonal by 2.9, all morphisms Spec A − → X, XA are aﬃne. Therefore the functor XA(A) − →
QAlg(XA) which maps t : SpecA − → XA to t∗OA is fully faithful. By 1.6 and the fact that
Ω t∗OA
E = HomXA(π ∗E,t ∗OA) ≃ HomX (E,s ∗OA) ≃ (s∗E)∨ for t ∈ X A(A), E ∈ C
where s = πt : SpecA → X we can conclude that the functor X (A) − →SMexR(C,A ), s ↦− →
(s∗
|C)∨ is well deﬁned and fully faithful.
Set A = AΓ , C ∈ QAlg(XA). We must show that, given Γ ∈ SMexR(C,A ), the composition
p : Spec A − → XA − →SpecA is an isomorphism. Set Y = Spec A and f : Y − → X for the
structure morphism. We want to apply 2.2 on p : Y − →SpecA.
Notice that, since f : Y → X is aﬃne, Y is quasi-compact and has aﬃne diagonal. Moreover
by 1.6 and 3.6 we have monoidal isomorphisms
Γ E ≃ Ω A
E ≃ H0((f ∗E)∨)
In particular, since Γ is a strong monoidal functor, the isomorphism A → Γ OX yields the iso-
morphism A − →H0(A ).
Let Spec k − →SpecA be a geometric point and set g : Xk − → XA for the base change map.
We have Y ×Ak ≃ Spec(g∗A ), while by [ Ton20, Prop 2.14] we have g∗A ≃ AΓ ⊗Ak, C. Since Γ ⊗Ak
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 17
is also left exact by hypothesis, by 1.6 we get Γ ⊗Ak ≃ Ω AΓ ⊗A k,C . Thus Γ OX ⊗Ak =A ⊗Ak ≃k
implies that Ω
AΓ ⊗A k,C
OX ≃k and therefore AΓ ⊗Ak, C ⁄= 0, that is Y × Ak ⁄= ∅.
It remains to show that {OY } generates QCoh Y. Since Y
f
− − → Xis aﬃne, f ∗C generates
QCoh Y by 2.4. On the other hand every sheaf f ∗E is generated by global sections thanks to 3.6.
In conclusion Y is pseudo-aﬃne and, by 2.2, the map p : Y → SpecA is an isomorphism. □
4. Pseudo-Affine shea ves revisited
In this section we give an alternative characterization of p seudo-aﬃne sheaves, which will be
used when studying the ﬁber category Fib X , C.
Lemma 4.1. Letπ : X → Aﬀ /R be a ﬁbered category over R, T∗ be a bounded above complex of
locally free sheaves on X and denote by Ul, for l ∈ Z, the locus in X where T∗ is exact in degrees
greater than l, that is
Ul(A) = {ξ: SpecA → X | ξ∗T∗ is exact in degrees greater than l} ⊆ X (A)
Then Ul → X is a quasi-compact open immersion.
Proof. Since T∗ is bounded above we have Ul = X for l ≫ 0. It is therefore enough to show
that Ul−1 → U l is a quasi-compact open immersion. In particular we can assu me X aﬃne and
Ul = X , that is assume T∗ exact in degrees greater than l. Set E = Ker(Tl → T l+1) and consider
the complex
0 → E → T l → T l+1 → · · ·
By construction this complex is exact. Since all the Tl are locally free it follows that E is locally
free as well and that this complex remains exact after any pul lback. We can therefore conclude
that Ul−1 is the locus where the map
Tl−1 → Ker(Tl → T l+1) = E
is surjective. In particular Ul−1 is a subﬁbered category of X . Going Zariski locally we can
assume Tl−1 and E free of rank m and n. In this case the locus Ul is the locus where
Λ nTl−1 → Λ nE = det E ≃ B
is surjective. But this is the complement of the zero locus de ﬁned by the above matrix, which is
a quasi-compact open subset of Spec B. □
Theorem 4.2. An intersection of quasi-compact open subschemes (thought o f as sheaves) of an
aﬃne scheme is pseudo-aﬃne. Conversely if U is a pseudo-aﬃne stack then it is (equivalent to) a
sheaf and it is the intersection of the quasi-compact open sub schemes of Spec H0(OU ) containing
it.
Proof. Let X = SpecB be an aﬃne scheme, {Ui}i∈I be a set of quasi-compact open subsets of
X and set U = ∩iUi. If i ∈ I the subscheme Ui is the complement of the zero locus of ﬁnitely
many elements of B and thus there exists a free B-moduleEi and a map φ i : Ei − →B such that
Ui is the locus where φ i is surjective. Let Vi : Aﬀ /B → (Sets) be the functor
Vi(A) = {s ∈Ei ⊗BA | φ i(s) = 1 }
It is easy to check that Vi is aﬃne, the map Vi → SpecB factors through Ui and that Vi →Ui
is locally (Kerφ i)|Ui → Ui. In particular Vi → SpecB is ﬂat. Now set V = ∏
iVi : Aﬀ /B − →
(Sets), that is
V (A) = {(si)i∈I | si ∈Ei ⊗BA and φ i(si) = 1 }
The schemeV is aﬃne, the map V − →SpecB is ﬂat, factors through U andV − →U is surjective
(as functors). Moreover if Spec A − →U is any map then V ×U A = V ×X A over A because
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 18
U − →X = SpecB is a monomorphism. It follows that V → U is aﬃne and faithfully ﬂat, in
particular an fpqc covering. Thus U is quasi-compact and U − →X is a ﬂat monomorphism.
The result then follows from 2.2.
Now assume that U is a pseudo-aﬃne stack. By 2.2 we know that p : U → SpecB, B =
H0(OU ), is a ﬂat monomorphism. Denote by Z the intersection of all quasi-compact open
subsets of Spec B containingU and set C = {OU }. In particular U ⊆Z.
Given a map α : SpecA − → SpecB factoring through Z we have to show that is factors
throughU . Consider α ∗
|C : C → Vect(A), which is a covariant strong monoidal functor. We show
that α ∗
|C ∈ FibU, C(A). By deﬁnition, if T∗ : Om
U → O q
U → 0 or T∗ : On
U − → Om
U − → Oq
U − →0
is an exact sequence on U , we must show that α ∗
|C is exact on T∗. The sequence T∗ deﬁnes a
complex W∗ of free A-modules, namely W∗ = H0(T∗), and the locus W in Spec A where W∗ is
exact is quasi-compact, open and contains U (see 4.1). Thus Z ⊆W , the sequence W∗ become
exact on Z and therefore α ∗ maintains its exactness, as required.
Since U is pseudo-aﬃne and α ∗
|C ∈ FibU, C(A), by 3.2 there exists s : SpecA → U and an
isomorphism s∗
|C ≃ α ∗
|C in Fib U, C(A). On the other hand, since B = H0(OU ), the restriction
{OSpec B} → C = {OU } is an equivalence and therefore Fib U, C(A) → FibSpec B, {OSpec B } is fully
faithful. By 3.2 applied on Spec B we can conclude that α : SpecA → SpecB and Spec A
s
− − →
U → SpecB coincides as required. □
Example 4.3. We show an example of a pseudo-aﬃne sheaf which is not quasi-a ﬃne. Let B
be a noetherian normal domain with dimB ≥ 2 and inﬁnitely many primes p with htp = 2. For
instance B = k[x,y ] for a ﬁeld k. Let I = {p ∈ SpecB | htp ≥ 2} and Up = SpecB −V (p)
for p ∈ I. Set U = ⋂
p∈IUp. The sheaf U is pseudo-aﬃne by 4.2 and we are going to show
that it is not quasi-aﬃne. Assume by contradiction that this is true. We identify the points
of the topological space of U with the ones of its image in Spec B. Remember that a map
SpecC − →SpecB factors through U if and only if pC =C for all p ∈I. Given q ∈ SpecB and
k(q) ⊆L an extension of ﬁelds, we have that Spec L − →SpecB factors through U if and only if
pL =L ∀p ∈I ⇐ ⇒pk(q) = k(q) ∀p ∈I ⇐ ⇒pBq =Bq ∀p ∈I ⇐ ⇒ htq ≤ 1
This tells us that U = {q ∈ SpecB | htq ≤ 1} and that, for all q ∈U , Spec Bq factors through
U . So, if q ∈U , The map U ×BBq − →SpecBq is a monomorphism with a section and therefore
an isomorphism. In particular OU,q =Bq. If V = SpecA ⊆U is an open subset and q ∈ SpecA
is a minimal prime, then Aq = Bq has dimension 0 and therefore q must be the generic point
of Spec B. Thus U is irreducible and, since the local rings of U are all domains, integral. In
particular
H0(OU ) =
⋂
q∈U
OU,q =
⋂
q∈Spec B | ht q≤1
Bq =B
where the last equality follows from the fact that B is normal. Since U is quasi-aﬃne, it follows
that it is an open subset of Spec B. So Z = SpecB −U has a ﬁnite number of generic points
and all p ∈ SpecB with htp = 2 have to be generic points, contradicting our assumptions.
