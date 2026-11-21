---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-028-33-dg-rings-and-modules
section_title: "DG Rings and Modules"
section_number: 3.3
pages: 59-62
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
are in place.
Deﬁnition 3.3.1. A DG central K-ring is a graded central K-ring A = L
i∈Z Ai
(see Deﬁnition 3.1.11), together with a K-linear homomorphism dA : A →A of
degree 1, called the diﬀerential, satisfying the equation dA ◦dA = 0, and the graded
Leibniz rule
dA(a·b) = dA(a)·b + (−1)i·a·dA(b)
for all a ∈Ai and b ∈Aj.
We sometimes write d instead of dA.
Deﬁnition 3.3.2. Let A and B be DG central K-rings. A homomorphism of DG
central K-rings f : A →B is a graded central K-ring homomorphism that commutes
with the diﬀerentials of A and B. The resulting category is denoted by DGRng/c K.
Central K-rings are viewed as DG central K-rings concentrated in degree 0
(and with trivial diﬀerentials). Thus the category Rng/c K is a full subcategory
of DGRng/c K.
Convention 3.3.3. To simplify terminology, we usually write “DG ring” instead
of “DG central K-ring”.
Deﬁnition 3.3.4. A DG ring A is called weakly commutative, strongly commu-
tative, nonpositive or commutative if it is so, respectively, as a graded ring (after
forgetting the diﬀerential), in the sense of Deﬁnition 3.1.22.
The corresponding full subcategories of DGRng/c K are DGRngwc/K, DGRngsc/K,
DGRng≤0/c K and DGRng≤0
sc /K.
When K = Z we can write DGRng := DGRng/c Z, etc.
Here are few examples of DG rings. First a silly example.
Example 3.3.5. Let A be a graded ring. Then A, with the zero diﬀerential, is a
DG ring.
59
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Example 3.3.6. Let X be a diﬀerentiable (i.e. of type C∞) manifold over K :=
R. The de Rham complex A of X is a DG R-ring, with the wedge product and
the exterior diﬀerential.
See [75, Section 2.9.7] for details.
This is a strongly
commutative DG ring, in the sense of Deﬁnition 3.3.4. However, it is almost never
nonpositive.
The next example is the algebraic analogue of the previous one.
Example 3.3.7. Let C be a commutative K-ring. Then the algebraic de Rham
complex A := ΩC/K = L
p≥0 Ωp
C/K is a DG K-ring. It is a strongly commutative
DG ring, and it is almost never nonpositive. See [46, Exercise 16.15] or [105, Section
25] for details.
Example 3.3.8. Let M be a DG K-module.
Consider the DG K-module
EndK(M) := HomK(M, M) from Deﬁnition 3.2.3(2).
Composition of endomor-
phisms is an associative multiplication on EndK(M) that respects the grading, and
the graded Leibniz rule holds. We see that EndK(M) is a DG K-ring. It is usually
neither weakly commutative nor nonpositive.
Example 3.3.9. Let C be a commutative ring and let c ∈C be an element. The
Koszul complex of c is the DG C-module K(C; c) deﬁned as follows. In degree 0
we let K0(C; c) := C. In degree −1, K−1(C; c) is a free C-module of rank 1, with
basis element x. All other homogeneous components are trivial. The diﬀerential
d is determined by what it does to the basis element x ∈K−1(C; c), and we let
d(x) := c ∈K0(C; c).
We want to make K(C; c) into a strongly commutative DG ring (in the sense
of Deﬁnition 3.3.4). Since x is an odd element, we must deﬁne the graded ring
structure by K(C; c) := C ⊗K[x], where K[x] is the strongly commutative graded
polynomial ring from Example 3.1.23, on the graded set X = X−1 := {x}; i.e.
x2 = 0.
Example 3.3.10. Let A and B be DG rings. The graded ring A⊗B from Deﬁnition
3.1.21, with the diﬀerential from Deﬁnition 3.2.3(1), is a DG ring.
Example 3.3.11. Let C be a commutative ring and let c = (c1, . . . , cn) be a
sequence of elements in C. By combining Examples 3.3.9 and 3.3.10 we obtain the
Koszul complex
K(C; c) := K(C; c1) ⊗C · · · ⊗C K(C; cn).
This is a strongly commutative DG C-ring.
Remark 3.3.12. In the book [46, Section 17, Exercises] there are a few variants
of the Koszul complex. Note that in most of the classical literature (including [46]
and [105]), the multiplicative structure of K(C; c) has been ignored.
Deﬁnition 3.3.13. Let A be a DG ring. The opposite DG ring Aop is the same
DG K-module as A, but the multiplication ·op of Aop is the multiplication · of A,
reversed and twisted by signs: a ·op b := (−1)i·j ·b·a for a ∈Ai and b ∈Aj.
Exercise 3.3.14. Verify that Aop is a DG ring.
Note that A is weakly commutative iﬀA = Aop.
Remark 3.3.15. In algebraic topology and homotopy theory it is customary to use
lower indices for DG rings (and to call them DG algebras). In other words, they use
homological grading, as opposed to our cohomological grading. Thus our nonpositive
DG ring A = L
i≤0 Ai becomes a nonnegative graded algebra A = L
i≥0 Ai in their
language.
60
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Another notion that is common in homotopy theory is that of a connective DG
algebra; this is a DG ring A = L
i∈Z Ai whose homology H(A) = L
i∈Z Hi(A) is
nonnegative. In our cohomological language, the analogue would be a coconnec-
tive DG ring, that is a DG ring A whose cohomology H(A) = L
i∈Z Hi(A) is a
nonpositive graded ring. Cf. Exercise 3.3.20 below.
If A is a coconnective DG ring, then its smart truncation A′ := smt≤0(A), in
the sense of Deﬁnition 7.3.6, is a nonpositive DG ring, and the inclusion A′ →A is
a quasi-isomorphism.
Deﬁnition 3.3.16. Let A be a DG ring. A DG left A-module is a graded left
A-module M = L
i∈Z M i, together with a K-linear homomorphism dM : M →M
of degree 1, called the diﬀerential, satisfying dM ◦dM = 0 and
dM(a·m) = dA(a)·m + (−1)i·a·dM(m)
for a ∈Ai and m ∈M j.
DG right A-modules are deﬁned likewise, but we won’t deal with them much.
This is because DG right A-modules are DG left modules over the opposite DG
ring Aop. More precisely, if M is a DG right A-module, then the formula a·m :=
(−1)i·j ·m·a, for a ∈Ai and m ∈M j, makes M into a DG left Aop-module.
As implied by Convention 1.2.4(5), all DG modules are by default DG left mod-
ules.
Proposition 3.3.17. Let A be a DG K-ring, and let M be a DG K-module.
(1) Suppose f : A →EndK(M) is a DG K-ring homomorphism.
Then the
formula a·m := f(a)(m), for a ∈Ai and m ∈M j, makes M into a DG
A-module.
(2) Conversely, every DG A-module structure on M, that’s compatible with the
DG K-module structure, arises in this way from a DG K-ring homomor-
phism f : A →EndK(M).
Exercise 3.3.18. Prove this proposition.
Deﬁnition 3.3.19. Let M and N be DG A-modules. A strict homomorphism of
DG A-modules φ : M →N is a strict homomorphism of DG K-modules (Deﬁ-
nition 3.2.2) that respects the action of A. The resulting category is denoted by
DGModstr A, or by the short notation Cstr(A).
The category Cstr(A) is abelian. See Proposition 3.8.6 for a more general state-
ment.
Exercise 3.3.20. Let A be a DG ring.
Show that the the module of cocycles
Z(A) := L
i∈Z Zi(A) is a graded subring of A, and the module of coboundaries
B(A) := L
i∈Z Bi(A) is a two-sided graded ideal of Z(A). Conclude that the coho-
mology module H(A) := L
i∈Z Hi(A) is a graded ring.
Let f : A →B be a homomorphism of DG rings. Show that H(f) : H(A) →H(B)
is a graded ring homomorphism.
Exercise 3.3.21. Let A be a DG ring. Given a DG A-module M, show that its
cohomology H(M) is a graded H(A)-module. If φ : M →N is a homomorphism in
Cstr(A), then H(φ) : H(M) →H(N) is a homomorphism in Gstr(H(A)). Conclude
that
(3.3.22)
H : Cstr(A) →Gstr(H(A))
is a linear functor.
61
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Deﬁnition 3.3.23. Let A be a DG K-ring, let M be a right DG A-module, and
let N be a left DG A-module. By Lemma 3.1.30, M ⊗A N is a graded K-module.
We make it into a DG K-module with the diﬀerential from Deﬁnition 3.2.3(1).
Deﬁnition 3.3.24. Let A be a DG K-ring, and let M and N be left DG A-
modules. The graded K-module HomA(M, N) from Deﬁnition 3.1.31 is made into
a DG K-module with the diﬀerential from Deﬁnition 3.2.3(2).
Generalizing formula (3.2.7), for DG A-modules M and N there is equality
HomCstr(A)(M, N) = Z0 HomA(M, N)

.
Proposition 3.3.25. Let A be a DG ring.
(1) The category Cstr(A) has products. Given a collection {Mx}x∈X of DG A-
modules, their product M = Q
x∈X Mx in Cstr(A) is M := L
i∈Z M i, where
M i := Q
x∈X M i
x.
(2) The category Cstr(A) has direct sums. Given a collection {Mx}x∈X of DG
A-modules, their direct sum M = L
x∈X Mx in Cstr(A) is M := L
i∈Z M i,
where M i := L
x∈X M i
x.
(3) The functor H from (3.3.22) commutes with all products and direct sums.
Exercise 3.3.26. Prove this proposition.
