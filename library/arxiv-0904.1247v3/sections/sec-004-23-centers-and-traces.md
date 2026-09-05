---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-004-23-centers-and-traces
section_title: "Centers and traces"
section_number: 2.3
pages: 18-20
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
algebra objects in closed symmetric monoidal ∞-categories, following [BFN] to which we refer for
more details. This is an ∞-categorical version of the approach to topological Hochschild ho mology
developed in [EKMM, Sh].
LetS be a closed symmetric monoidal ∞-category, and A∈S an associative algebra object.
Then we have internal hom objects [L2, 6.1], and given A⊗Aop-modules M,N , we can consider
the A⊗Aop-linear morphism object HomA⊗Aop(M,N )∈S . Likewise, given left and right A⊗Aop
modules M,N ∈S we have a pairing M⊗A⊗Aop N∈S deﬁned by the two-sided bar construction
[L2, 4.3.4] over A⊗Aop.
18
Deﬁnition 2.10. Let A be an associative algebra object in a closed symmetric monoi dal ∞-
categoryS, and B an A-bimodule inS.
(1) The Hochschild cohomology (or derived center) Z(A) = HH ∗(A)∈S is the endomorphism
objectEndA⊗Aop(A) of A as an A-bimodule. More generally, the Hochschild cohomology of
the bimodule B is
HH∗(A,B ) = Hom A⊗Aop(A,B ).
(2) The Hochschild homology (or derived trace) Tr(A) = HH ∗(A) ∈ Sis the pairing object
A⊗A⊗AopA of A with itself as an A-bimodule. More generally, the Hochschild homology of
the bimodule B is
HH∗(A,B ) = A⊗A⊗AopB.
Example 2.11. TakingB =MA⊗ AN for a left A-module AN and a right A-module MA, we ﬁnd
the relative tensor product
HH∗(A,M A⊗ AN ) = M⊗AN,
while taking B = Hom( AM, AN ) the Hom object in S between two left A-modules M,N , we ﬁnd
the A-module Hom
HH∗(A, Hom(AM, AN )) = Hom A(M,N ).
In general, the center Z( A) is again an associative algebra object in S. Furthermore, Z(A) comes
with a canonical central morphism
z : Z(A) /d47/d47A F ✤ /d47/d47F (1A)
while the trace Tr( A) comes with a canonical trace morphism
tr :A /d47/d47 Tr(A)
coequalizing left and right multiplication.
2.3.1. Cyclic bar construction. For an associative algebra object A in a symmetric monoidal ∞-
categoryS, there is a natural simplicial object Ncyc
∗ (A) and cosimplicial object N∗
cyc(A) such that
the geometric realization colim Ncyc
∗ (A) calculates HH ∗(A) = Tr(A) and the totalization lim N∗
cyc(A)
calculates HH ∗(A) = Z(A).
We construct the simplicial object Ncyc
∗ (A) and cosimplicial object N∗
cyc(A) as follows. The
A-bimodule A has a canonical free simplicial resolution C∗(A) as an A-bimodule with terms
Cn(A)≃A⊗n+2
It is deﬁned using the usual formalism of cotriple resolutions as in [BFN ]. The face maps come from
the multiplication on A, and the degeneracies from the unit of A. The A-bimodule structure is the
obvious action on the left and right extreme factors.
Now recall that the trace HH ∗(A,B ) is deﬁned by the pairing A⊗A⊗Aop B. Since the tensor
product commutes with colimits, in particular geometric realizations, we calculate
HH∗(A,B ) = A⊗A⊗AopB≃|C∗(A)|⊗ A⊗AopB≃|B⊗A⊗AopC∗(A)|.
Thus the geometric realization of C∗(A)⊗A⊗AopB calculates the trace HH ∗(A,B ).
We write Ncyc
∗ (A) for the simplicial object A⊗A⊗Aop C∗(A) and refer to it as the Hochschild
simplicial object. We can evaluate the terms of the Hochschild simplicia l object
Ncyc
n (A) = A⊗A⊗AopCn(A)≃A⊗A⊗AopA⊗n+2≃A⊗n+1
In particular, there are equivalences Ncyc
0 (A)≃ A and Ncyc
1 (A)≃ A⊗A, and the two simplicial
maps A⊗A→A are the multiplication and the opposite multiplication of A.
Similarly, recall that the center HH ∗(A,B ) is deﬁned by the hom object HomA⊗Aop(A,B ). Since
morphisms take colimits in the domain to limits, in particular geometric re alizations to totalizations,
we calculate
HH∗(A,B ) =HomA⊗Aop(A,B )≃HomA⊗Aop(|C∗(A)|,B )≃ limHomA⊗Aop(C∗(A),B )
19
Thus the totalization of HomA⊗Aop(C∗(A),B ) calculates the center HH ∗(A,B ).
We write N∗
cyc(A) for the cosimplicial objectHomA⊗Aop(C∗(A),A ) and refer to it as the Hochschild
cosimplicial object. As before, we can evaluate the terms of the Ho chschild cosimplicial object
Nn
cyc(A) =HomA⊗Aop(Cn(A),A )≃HomA⊗Aop(A⊗n+2,A )≃Hom(A⊗n,A ).
In particular, there are equivalences N0
cyc(A)≃A and N1
cyc(A)≃H om(A,A ), and the two cosim-
plicial maps A→Hom(A,A ) are induced by the left and right multiplication of A.
2.3.2. Transposed Hochschild object. Let us now suppose that A∈S is dualizable, with dual A′. In
that case the simplicial object C∗(A) deﬁnes a dual cosimplicial object C∗(A)t with cosimplices
Cn(A)t≃A′⊗n+2
and face and degeneracies given as the transposes of those of C∗(A). In this case, we can describe
the center of a bimodule as a colimit
HH∗(A,B ) ≃ limHomA⊗Aop(C∗(A),B )
≃ |C∗(A)′⊗A⊗AopB|
