---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-008-51-2-linear-maps-from-spans-of-groupoids
section_title: "2-Linear Maps from Spans of Groupoids"
section_number: 5.1
pages: 22-24
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
---
in Figure 2, we can apply the functor [ −, V ect] to the span diagram (7). This
functor is contravariant, so we get a cospan:
(70) [ X, V ect]
[A1, V ect]
s∗
/d56/d56/d113/d113/d113/d113/d113/d113/d113/d113/d113/d113/d113
[A2, V ect]
t∗
/d102/d102/d77 /d77 /d77 /d77 /d77 /d77 /d77 /d77 /d77 /d77 /d77
We now recall that the pullbacks s∗ and t∗ have adjoints: this is a direct con-
sequence of Theorem 4.2.1. This reveals how to transport a V ect-presheaf on A1
along this cospan. In fact, it gives two 2-linear maps, which are adjo int. Thinking
2-VECTOR SPACES AND GROUPOIDS 23
of the span as a morphism in Span( FinGpd) from A1 to A2, we ﬁnd a correspond-
ing 2-linear map (though the adjoint is equally well deﬁned). We ﬁrst d o a pullback
along s, giving a V ect-presheaf on X. Then we use the adjoint map t∗. So we have
the following:
Deﬁnition 5.1.1. For a span of groupoids X : A1→ A2 in Span(FinGpd) deﬁne
the 2-linear map:
(71) t∗◦ s∗ : [A1, V ect]−→ [A2, V ect]
Now, by Theorem 4.2.1, both s∗ and t∗ are 2-linear maps, so the composite t∗◦s∗
is also a 2-linear map.
Remark 5.1.2. We can think of the pullback-pushforward construction as giving—
in the language of quantum ﬁeld theory—a “sum over histories” for e volving a 2-
vector. Each 2-vector in [ A1, V ect] picks out a vector space for each object of A1.
The 2-linear map we have described tells us how to evolve this 2-vecto r along a span.
First we consider the pullback to [ X, V ect], which gives us a 2-vector consisting of
all assignments of vector spaces to objects of X which project to the chosen one
in A1. Each of these objects could be considered a “history” of the 2-v ector along
the span. We then “push forward” this assignment to A2, which involves a colimit.
This is more general than a sum, though so one could describe this as a “colimit
of histories”. It takes into account the symmetries between individ ual “histories”
(i.e. morphisms in X).
So, given a span X : A1→ A2, we can write Λ( X) in terms of its eﬀect on a
V ect-presheaf G on A1, which, at any object a2∈ A2 gives:
(72) Λ( X)(G)(a2) = (
⨁
[x]|t(x)∼=a2
C[Aut(a2)]⊗C[Aut(x)] G(s(x)))
by exactly the same reasoning as in Section 4.3.
It is sometimes useful—particularly when we look at composition of spa ns—to
break up the direct sum into the contributions from diﬀerent objec ts of A1, like
this:
(73) Λ( X)(G)(a2) =
⨁
[a1]∈A1
(
⨁
[x]
s(x)∼=a1
t(x)∼=a2
C[Aut(a2)]⊗C[Aut(x)] G(a1))
Moreover, there is a convenient way to write down the components of the 2-linear
map associated to a span, which is given by Frobenius reciprocity.
Proposition 5.1.3. Given basis elements (a1, W1)∈ Λ( A1) and (a2, W2)∈ Λ( A2),
the matrix elements are:
(74) Λ( X)(a1,W1),(a2,W2)≃
⨁
[x]
homRep(Aut(x))[s∗(W1), t∗(W2)]
Here, the direct sum is taken over equivalence classes [ x] in the essential preimage
of ( a1, a2): that is, objects of X mapping to a1 and a2. For each [ x], the functors
s and t deﬁne homomorphisms
(75) sx : Aut(x)→ Aut(s(x))
and
(76) tx : Aut(x)→ Aut(t(x))
24 JEFFREY C. MORTON
, which deﬁne the induced representations. We think of the terms o f the direct sum
as “lying over” the objects x.
So using the adjoint 2-linear map
(77) t∗ : Λ( X)→ Λ( A2)
to push forward a 2-vector s∗F : X→ V ect to one on A2, the above is also, by
Frobenius reciprocity:
(78)
⨁
[x]
homRep(Aut(a2))[(tx)∗◦ (sx)∗W1, W2]
By Schur’s lemma, this says:
(79) Λ( X)(a1, W1) =
⨁
[x]
(tx)∗◦ (sx)∗(a1, W1)
since the components of Λ( X)(a1, W1) count the number of copies of W2 in the
pushforward of W1. (In the remainder of this paper, we will suppress the subscripts
and denote sx by s and tx by t when the context makes clear that we mean the
induced group homomorphism.)
So in fact, Λ( X)(a1, W1) is a direct sum of irreducible 2-vectors in Λ( A2), given
as a sum over x∈ X restricting to a1, a2 of the induced representations along each
restriction map.
