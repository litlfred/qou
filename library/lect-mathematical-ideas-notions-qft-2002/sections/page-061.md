---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-061
section_title: "Page 61"
pages: 61-61
pdf_page: 61
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 61

9. FERMIONIC INTEGRALS

9.1. Bosons and fermions. In physics there exist two kinds of particles — bosons
and fermions. So far we have dealt with bosons only, but many important par-
ticles are fermions: e.g., electron, proton, etc. Thus it is important to adapt our
techniques to the fermionic case.

In quantum theory, the difference between bosons and fermions is as follows: if
the space of states of a single particle is H then the space of states of the system of
k such particles is S*H for bosons and A*H for fermions. In classical theory, this
means that the space of states of a bosonic particle is a usual real vector space (or
more generally a manifold), while for a fermionic particle it is an odd vector space.
Mathematically “odd” means that the ring of smooth functions on this space (i.e.
the ring of classical observables) is an exterior algebra (unlike the case of a usual,
even space, for which the ring of polynomial functions is a symmeteric algebra).

More generally, one may consider systems of classical particles or fields some
of which are bosonic and some fermionic. In this case, the space of states will be
a supervector space, ie. the direct sum of an even and an odd space (or, more
generally, a supermanifold — a notion we will define below).

When such a theory is quantized using the path integral approach, one has to
integrate functions over supermanifolds. Thus, we should learn to integrate over
supermanifolds and then generalize to this case our Feynman diagram techniques.
This is what we do in this section.

9.2. Supervector spaces. Let k be a field of characteristic zero. A supervector
space (or shortly, superspace) over k is just a Z/2-graded vector space: V = Vo ©
V,. If VY = k” and V¥, = k™ then V is denoted by k”!. The notions of a
homomorphism, direct sum, tensor product, dual space for supervector spaces are
defined in the same way as for Z/2-graded vector spaces. In other words, the tensor
category of supervector spaces is the same as that of Z/2-graded vector spaces.

However, the notions of a supervector space and a Z/2-graded vector space are
not the same. The difference is as follows. The category of vector (and hence Z/2-
graded vector) spaces has an additional symmetry structure, which is the standard
isomorphism V @ W > W ®V (given by v ®w > w ®v). This isomorphism allows
one to define symmetric powers S™V, exterior powers AV, etc. For supervector
spaces, there is also a symmetry V ® W > W ®V, but it is defined differently.
Namely, v ® w goes to (—1)""w @v, v € Vn,w € Vn (m,n € {0,1}). In other
words, it is the same as usual except that if v,w are odd then v @w > -—w ® v.
As a result, we can define the superspaces SV and A™V for a superspace V, but
they are not the same as the symmetric and exterior powers in the usual sense. For
example, if V is purely odd (V = V,), then SV is the exterior m-th power of V,
and A™V is the m-th symmetric power of V (purely even for even m and purely
odd for odd m).

For a superspace V, let IIV be the same space with opposite parity, i.e. (IIV); =
Vi_-i, 2 = 0,1. With this notation, the equalities explained in the previous para-
graph can be written as: S™V =TI™(A™TV), A™V = II" (S™TIV).

Let V = W © V be a finite dimensional superspace. Define the algebra of
polynomial functions on V, O(V), to be the algebra SV* (where symmetric powers
are taken in the super sense). Thus, O(V) = SV> ® AV,*, where Vo and Vy are
regarded as usual spaces. More explicitly, if 71,...,¢%, are linear coordinates on Vo,
