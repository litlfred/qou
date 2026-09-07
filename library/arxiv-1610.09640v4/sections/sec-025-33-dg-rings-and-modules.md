---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-025-33-dg-rings-and-modules
section_title: "DG Rings and Modules"
section_number: 3.3
pages: 59-62
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
are in place.
Deﬁnition 3.3.1.A DG centralK-ring is a graded centralK-ring A =⨁
i∈ZAi
(see Deﬁnition 3.1.11), together with aK-linear homomorphism dA : A→A of
degree 1, called thediﬀerential, satisfying the equationdA◦dA = 0, and the graded
Leibniz rule
dA(a·b) = dA(a)·b + (−1)i·a·dA(b)
for alla∈Ai and b∈Aj.
We sometimes writed instead of dA.
Deﬁnition 3.3.2.Let A and B be DG centralK-rings. A homomorphism of DG
centralK-ringsf :A→B isagradedcentral K-ringhomomorphismthatcommutes
with the diﬀerentials ofA andB. The resulting category is denoted byDGRng/cK.
Central K-rings are viewed as DG central K-rings concentrated in degree 0
(and with trivial diﬀerentials). Thus the categoryRng/cK is a full subcategory
of DGRng/cK.
Convention 3.3.3. To simplify terminology, we usually write “DG ring” instead
of “DG centralK-ring”.
Deﬁnition 3.3.4.A DG ringA is called weakly commutative, strongly commu-
tative, nonpositive or commutative if it is so, respectively, as a graded ring (after
forgetting the diﬀerential), in the sense of Deﬁnition 3.1.22.
The corresponding full subcategories ofDGRng/cKare DGRngwc/K, DGRngsc/K,
DGRng≤0/cK and DGRng≤0
sc /K.
WhenK =Z we can writeDGRng := DGRng/cZ, etc.
Here are few examples of DG rings. First a silly example.
Example 3.3.5. Let A be a graded ring. ThenA, with the zero diﬀerential, is a
DG ring.
59
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Example 3.3.6. Let X be a diﬀerentiable (i.e. of typeC∞) manifold overK :=
R. The de Rham complexA of X is a DGR-ring, with the wedge product and
the exterior diﬀerential. See [75, Section 2.9.7] for details. This is a strongly
commutative DG ring, in the sense of Deﬁnition 3.3.4. However, it is almost never
nonpositive.
The next example is the algebraic analogue of the previous one.
Example 3.3.7. Let C be a commutativeK-ring. Then the algebraic de Rham
complex A := ΩC/K =⨁
p≥0 Ωp
C/K is a DGK-ring. It is a strongly commutative
DG ring, and it is almost never nonpositive. See [46, Exercise 16.15] or [105, Section
25] for details.
Example 3.3.8. Let M be a DG K-module. Consider the DG K-module
EndK(M) := Hom K(M,M ) from Deﬁnition 3.2.3(2). Composition of endomor-
phisms is an associative multiplication onEndK(M) that respects the grading, and
the graded Leibniz rule holds. We see thatEndK(M) is a DGK-ring. It is usually
neither weakly commutative nor nonpositive.
Example 3.3.9. Let C be a commutative ring and letc∈C be an element. The
Koszul complexof c is the DGC-module K(C;c) deﬁned as follows. In degree0
we let K0(C;c) := C. In degree−1, K−1(C;c) is a freeC-module of rank1, with
basis elementx. All other homogeneous components are trivial. The diﬀerential
d is determined by what it does to the basis elementx∈K−1(C;c), and we let
d(x) :=c∈K0(C;c).
We want to makeK(C;c) into a strongly commutative DG ring (in the sense
of Deﬁnition 3.3.4). Sincex is an odd element, we must deﬁne the graded ring
structure by K(C;c) := C⊗K[x], whereK[x] is the strongly commutative graded
polynomial ring from Example 3.1.23, on the graded setX = X−1 :={x}; i.e.
x2 = 0.
Example3.3.10. LetAandB beDGrings. Thegradedring A⊗B fromDeﬁnition
3.1.21, with the diﬀerential from Deﬁnition 3.2.3(1), is a DG ring.
Example 3.3.11. Let C be a commutative ring and letc = (c1,...,cn) be a
sequence of elements inC. By combining Examples 3.3.9 and 3.3.10 we obtain the
Koszul complex
K(C;c) := K(C;c1)⊗C···⊗C K(C;cn).
This is a strongly commutative DGC-ring.
Remark 3.3.12. In the book [46, Section 17, Exercises] there are a few variants
of the Koszul complex. Note that in most of the classical literature (including [46]
and [105]), the multiplicative structure ofK(C;c) has been ignored.
Deﬁnition 3.3.13.Let A be a DG ring. Theopposite DG ringAop is the same
DGK-module asA, but the multiplication·op of Aop is the multiplication·of A,
reversed and twisted by signs:a·opb := (−1)i·j·b·a for a∈Ai and b∈Aj.
Exercise 3.3.14. Verify thatAop is a DG ring.
Note thatA is weakly commutative iﬀA =Aop.
Remark 3.3.15.In algebraic topology and homotopy theory it is customary to use
lower indices for DG rings (and to call them DG algebras). In other words, they use
homological grading, asopposedtoourcohomologicalgrading. Thusournonpositive
DG ringA =⨁
i≤0Ai becomes a nonnegative graded algebraA =⨁
i≥0Ai in their
language.
60
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Another notion that is common in homotopy theory is that of aconnective DG
algebra; this is a DG ringA =⨁
i∈ZAi whose homology H(A) = ⨁
i∈Z Hi(A) is
nonnegative. In our cohomological language, the analogue would be acoconnec-
tive DG ring, that is a DG ringA whose cohomology H(A) = ⨁
i∈Z Hi(A) is a
nonpositive graded ring. Cf. Exercise 3.3.20 below.
If A is a coconnective DG ring, then its smart truncationA′:= smt≤0(A), in
the sense of Deﬁnition 7.3.6, is a nonpositive DG ring, and the inclusionA′→A is
a quasi-isomorphism.
Deﬁnition 3.3.16.Let A be a DG ring. A DG left A-module is a graded left
A-module M =⨁
i∈ZMi, together with aK-linear homomorphism dM :M→M
of degree 1, called the diﬀerential, satisfyingdM◦dM = 0 and
dM(a·m) = dA(a)·m + (−1)i·a·dM(m)
for a∈Ai and m∈Mj.
DG rightA-modules are deﬁned likewise, but we won’t deal with them much.
This is because DG rightA-modules are DG left modules over the opposite DG
ring Aop. More precisely, ifM is a DG rightA-module, then the formulaa·m :=
(−1)i·j·m·a, fora∈Ai and m∈Mj, makesM into a DG leftAop-module.
As implied by Convention 1.2.4(5), all DG modules are by default DG left mod-
ules.
Proposition 3.3.17. LetA be a DGK-ring, and letM be a DGK-module.
(1) Suppose f : A→EndK(M) is a DG K-ring homomorphism. Then the
formula a·m := f(a)(m), for a∈Ai and m∈Mj, makes M into a DG
A-module.
(2) Conversely, every DGA-module structure onM, that’s compatible with the
DG K-module structure, arises in this way from a DGK-ring homomor-
phism f :A→EndK(M).
Exercise 3.3.18. Prove this proposition.
Deﬁnition 3.3.19.Let M and N be DGA-modules. A strict homomorphism of
DG A-modules φ: M →N is a strict homomorphism of DGK-modules (Deﬁ-
nition 3.2.2) that respects the action ofA. The resulting category is denoted by
DGModstrA, or by the short notationCstr(A).
The category Cstr(A) is abelian. See Proposition 3.8.6 for a more general state-
ment.
Exercise 3.3.20. Let A be a DG ring. Show that the the module of cocycles
Z(A) := ⨁
i∈Z Zi(A) is a graded subring ofA, and the module of coboundaries
B(A) :=⨁
i∈Z Bi(A) is a two-sided graded ideal ofZ(A). Conclude that the coho-
mology module H(A) :=⨁
i∈Z Hi(A) is a graded ring.
Letf :A→B beahomomorphismofDGrings. Showthat H(f) : H(A)→H(B)
is a graded ring homomorphism.
Exercise 3.3.21. Let A be a DG ring. Given a DGA-module M, show that its
cohomology H(M) is a gradedH(A)-module. Ifφ:M→N is a homomorphism in
Cstr(A), then H(φ) : H(M)→H(N) is a homomorphism inGstr(H(A)). Conclude
that
(3.3.22) H : Cstr(A)→Gstr(H(A))
is a linear functor.
61
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 3.3.23.Let A be a DGK-ring, letM be a right DGA-module, and
let N be a left DGA-module. By Lemma 3.1.30,M⊗AN is a gradedK-module.
We make it into a DGK-module with the diﬀerential from Deﬁnition 3.2.3(1).
Deﬁnition 3.3.24.Let A be a DG K-ring, and let M and N be left DG A-
modules. The gradedK-module HomA(M,N ) from Deﬁnition 3.1.31 is made into
a DGK-module with the diﬀerential from Deﬁnition 3.2.3(2).
Generalizing formula (3.2.7), for DGA-modules M and N there is equality
HomCstr(A)(M,N ) = Z0(
HomA(M,N )
{
.
Proposition 3.3.25. LetA be a DG ring.
(1) The categoryCstr(A) has products. Given a collection{Mx}x∈X of DGA-
modules, their productM =∏
x∈XMx in Cstr(A) isM :=⨁
i∈ZMi, where
Mi :=∏
x∈XMi
x.
(2) The category Cstr(A) has direct sums. Given a collection{Mx}x∈X of DG
A-modules, their direct sumM =⨁
x∈XMx in Cstr(A) is M :=⨁
i∈ZMi,
whereMi :=⨁
x∈XMi
x.
(3) The functor H from (3.3.22) commutes with all products and direct sums.
Exercise 3.3.26. Prove this proposition.
