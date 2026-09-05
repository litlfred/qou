---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-057-12-sheaves-on-the-hilbert-scheme
section_title: "Sheaves on the Hilbert scheme"
section_number: 12
pages: 66-67
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
In this section we explain how for a word β of generators of the braid group Brn one can construct a
two-periodic complex Cβ of quasi-coherent sheaves on the space Xℓ with the property that its homology
is supported on a version of the Steinberg-like variety St ℓ that covers the nested Hilbert Scheme Hilb 1,n of
n-points on C2. We show later that Bℓ×G-invariant part H ∗(Cβ) is related to the isotopy invariant of the
link L(β). First let us remind a deﬁnition of the nested Hilbert scheme.
66
12.1. Nested Hilbert scheme: deﬁnitions and notations. Direct deﬁnition of the scheme Hilb 1,n is
the moduli space of the sequences of the ideals I1⊂···⊂ In⊂ C[x,y ] such that dim C[x,y ]/Ik = k. We
are also interested in the subvariety Hilb L
1,n which consists of the sequence like above with extra condition
supp(Ik−1/Ik) is a point on the line L ={y = 0}.
We can also think of a point on Hilb 1,n as quotient sequence
C[x,y ]/In→ C[x,y ]/In−1→···→ C[x,y ]/I1.
Let us use notation Vk = C[x,y ]/Ik. If we choose a basis {vi}i=1,...,n of Vn such that ⟨v1,...,v k⟩ = Vk
then the operators of multiplication by x and y become upper triangular in this basis. Let us denote these
operators by X,Y . Let us also notice that the fact that Vk are obtained as a quotient of C[x,y ] implies that
there is a special vector in u∈Vn which is the image of 1 ∈ C[x,y ]. Thus on the level of points we obtained
identiﬁcation of Hilb 1,n with the quotient of the variety
CV st
b×b ={(X,Y )∈ b|[X,Y ] = 0 and exists u such that C[X,Y ]u =V}
by the group B. Respectively, to obtain a model for Hilb L
1,n one need to impose the condition Y ∈ n
The tricky part of the previous description is the fact that we take quotient by the group B which is not a
reductive group. Thus to reveal the scheme theoretic structur e of the quotient CV st
b×b/B one could consider
slightly diﬀerent model for Hilb 1,n which we describe below. Let us deﬁne ˜C⊂ Fl× gln× gln which consists
of the triples ( V•,X,Y ) satisfying the following conditions:
XV i⊂Vi, YV i⊂Vi, [X,Y ] = 0.
There is a natural action of GL(n) on ˜C and analogously to the argument in [33] one can show that the
semi-stable locus ˜Css of the action is exactly the locus where there is a vector u such that C[X,Y ]u =Vn.
Thus on the set theoretic level we established the isomorphism betw eenCV st
b×b/B and ˜Css/GLn. Lastly, let
us notice that the quotient ˜Css/GLn has a natural scheme structure due to GIT theory [32].
