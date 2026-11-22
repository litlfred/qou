---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-016-62-the-gns-construction
section_title: "The GNS construction"
section_number: 6.2
pages: 40-43
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
The GNS construction
Thus uniqueness of the trace implies factoriality. This suggests another in-
teresting way to construct a type II1 factor. If A = M2(C), A is embedded
in A ⊗A as diagonal matrices: a ,→a ⊗1. Iterate this procedure to form an
increasing sequence An of *-algebras with A1 = A and An+1 = An ⊗A, and
consider the *-algebra A∞= ∪nAn which could also be called ⊗∞
alg,n=1An. If
we normalise the matrix trace on all matrix algebras so that tr(1) = 1 then
tr(a ⊗1) = tr(a) so that tr deﬁnes a positive faithful normalised trace on
A∞. Elements of A∞can be thought of as linear combinations of tensors
of the form a1 ⊗a2 ⊗a3 ⊗· · · ⊗1 ⊗1 ⊗1 ⊗· · · , on which the trace is just
the product of the traces of the ai’s. We now turn A∞into a von Neumann
algebra.
Deﬁne an inner product on A∞by ⟨x, y⟩= tr(y∗x). Then A∞is a pre-
Hilbert space and let H be its completion. Note that Mn(C) is a von Neu-
mann algebra so tr(y∗x∗xy) ≤||x||2tr(y∗y). This means that the operator
Lx on A∞, Lx(y) = xy, satisﬁes ||Lx(ξ)|| ≤||x|| · ||ξ|| (where ||x|| is the
operator norm of the matrix x and ||ξ|| is the Hilbert space norm of ξ) and
so extends uniquely to a bounded operator also written Lx on H. One checks
that (Lx)∗= Lx∗so x →Lx deﬁnes a faithful (=injective) representation of
the *-algebra A∞on H . Let M be the von Neumann algebra on H generated
by the Lx and identify A∞with a subalgebra of M.
The trace on A∞is deﬁned by tr(a) = ⟨aξ, ξ⟩where ξ is the element
1 ∈A∞considered as a vector in H. So tr extends to a trace on M which is
ultraweakly continuous, positive and normalised. It is also unique with these
properties by the uniqueness of the trace on the ultraweakly dense subalgebra
A∞of M. If we can show that tr is faithful on M then it follows that M is a
type II1 factor. It is important to note that this does not follow simply from
the faithfulness of tr on A. In fact it is true but we need to do something to
prove it.
When we showed that Lx was bounded, the same calculation, with tr(ab) =
tr(ba), would have shown that Rx, right multiplication by x, is also bounded.
Associativity shows that Lx and Ry commute on A∞, hence on H. Thus M
commutes with Ry for each y ∈A∞.
Now we can show faithfulness: if
40
tr(x∗x) = 0 for x ∈M then for each a ∈A∞we have
||x(a)||2 = ||xRa(ξ)||2 = ||Rax(ξ)||2 ≤||Ra||2||xξ||2 = ||Ra||2tr(x∗x) = 0.
Since A∞is dense, this means x = 0. So tr is faithful on M which is thus a
type II1 factor.
Exercise 6.2.1. Let Fn be the Fibonacci numbers.
Show that there is a
unique (up to you to ﬁgure out in what sense) unital embedding of MFn(C)⊕
MFn+1(C) inside MFn+1(C) ⊕MFn+2(C) for n ≥3. Thus one may form the
*-algebra
F∞= ∪∞
n=1MFn(C) ⊕MFn+1(C).
Show that there is a unique C∗-norm and unique positive trace on F∞so we
may repeat the procedure above to obtain another type II1 factor.
Many points are raised by this example. The easiest to deal with are
the properties of the vector ξ which played a prominent role. We used both
Mξ = H and M ′ξ = H.
Deﬁnition 6.2.2. Let M be a von Neumann algebra on H. A vector ξ ∈H is
called cyclic for M if Mξ = H and separating for M if
(xξ = 0) ⇒(x = 0)
for all x ∈M.
Proposition 6.2.3. With notation as above, ξ is cyclic for M iﬀξ is sepa-
rating for M ′.
Proof. (⇒) Exercise—in fact done in the discussion of A∞above.
(⇐) Let p be the projection onto the closure of Mξ. Then p ∈M ′. But
(1 −p)ξ = 0 so p = 1.
The construction of M from A∞is a special case of what is known
as the GNS construction (Gelfand-Naimark-Segal).
Given a positive lin-
ear functional φ satisfying φ(a∗) = φ(a) on a *-algebra A we let Nφ be
{x ∈A : φ(x∗x) = 0}. We also deﬁne a sesquilinear form ⟨, ⟩φ on A by
⟨x, y⟩φ = φ(y∗x). This form is positive semideﬁnite but this is enough for the
Cauchy-Schwartz inequality to hold so that N is the same as {x : ⟨x, y⟩φ =
0
∀y ∈A} so that N is a subspace and ⟨, ⟩φ deﬁnes a pre-Hilbert space
structure on the quotient A/N. Under favourable circumstances, left mul-
tiplication by x, Lx deﬁnes a bounded linear operator on it.
Favourable
circumstances are provided by C∗-algebras.
Exercise 6.2.4. If φ is a linear functional on a C∗-algebra satisfying φ(a∗a) ≥
0 show that φ(a∗) = φ(a). Moreover if A is unital show that φ is norm-
continuous and in fact ||φ|| = φ(1).
41
Remark 6.2.5. It is a standard elementary fact in C∗-algebras that one may
always adjoin an identity to a C∗-algebra.
Proposition 6.2.6. If A is a unital C∗-algebra and φ : A →C is a positive
linear functional then
φ(y∗x∗xy) ≤||x||2φ(y∗y)
Proof. Let ˜φ(a) = φ(y∗ay). Then ˜φ is positive so by the exercise ˜φ(x∗x) ≤
||x||2 ˜φ(1).
It follows immediately that, given a positive linear functional φ on a unital
C∗-algebra, each x ∈A determines a bounded linear operator πφ(x) on the
Hilbert space Hφ of the GNS construction via left multiplication: πφ(x)(y) =
xy.
Moreover ||πφ(x)|| ≤||x|| and πφ(x∗) = πφ(x)∗since ⟨πφ(x)y, z⟩=
φ(z∗xy) = ⟨y, πφ(x∗)z⟩. Note that φ(x) = ⟨πφ(x)1, 1⟩.
To sum up we have the following:
Deﬁnition 6.2.7. If A is a C∗-algebra and φ is a positive linear functional
on A, the Hilbert space of the GNS construction is written Hφ and the rep-
resentation πφ by left multiplication is called the GNS representation.
Proposition 6.2.8. If A is a C∗-algebra on H and ξ ∈H, deﬁne ωξ(a) =
⟨aξ, ξ⟩. Then ωξ is a positive linear functional and a 7→aξ deﬁnes a unitary
u : Hωξ →Aξ such that uπωξ(a)u∗= a.
Proof. Obvious.
If A is actually a von Neumann algebra, πφ(A) will not in general be one
on Hφ. This diﬃculty will be resolved in the next section.
42
Chapter 7
Normality, complete additivity.
