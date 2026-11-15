---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-014-26-perverse-multiplier
section_title: "Perverse multiplier"
section_number: 2.6
pages: 44-46
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
We now introduce the notion of a multiplier. This will play an important
role in our proof of theorem 1.1, indeed the theorem essentially amounts
to the statement that any perverse sheaf on a complex abelian variety is a
multiplier. In this section Λ need not be algebraically closed, but we assume
as always that axioms (D1) – (D4) from section 2.3 hold.
Let N be a full subcategory of D satisfying the stability axiom (N1). We
then deﬁne an N-multiplier to be an object K ∈D such that for all r ∈N0 and
all n̸ = 0 the subquotients of pHn((K ⊕K∨)∗r) all lie in N. The relevance of
this notion for theorem 1.1 is clear from
LEMMA 2.11. For P ∈P the following holds.
(a) If the subcategory N satisﬁes the twisting axiom (N2) and if P is
an N-multiplier, then H•(X,Pχ) is concentrated in degree zero for
most characters χ.
(b) Conversely, suppose that N satisﬁes the acyclicity axiom (N3) and
that the hard Lefschetz axiom (D5) holds. Then P is an N-multiplier
if H•(X,P) is concentrated in degree zero.
Proof. (a) Put g = dim(X). The perverse decomposition axiom (D3)
shows that
P∗(g+1) =
M
m∈Z
Pm[m]
for suitable
Pm ∈P.
2.6. Perverse multiplier
37
By assumption P is an N-multiplier, hence Pm ∈N for all m̸ = 0. Via the
twisting axiom (N2) it follows that for most characters χ and all n ∈Z,
Hn(X,P∗(g+1)
χ
) = Hn(X,(P0)χ).
The right hand side vanishes for |n| > g since rat(P0)χ is perverse. But for
the left hand side we have
H•(X,P∗(g+1)
χ
) = (H•(X,Pχ))⊗(g+1)
by proposition 2.1 and since H•(X,−) is a tensor functor by the K¨unneth
theorem. So the above vanishing statement for |n| > g implies that H•(X,Pχ)
is concentrated in degree zero.
(b) Put Q = (P ⊕P∨)∗r for any r ∈N. Since hypercohomology is a
tensor functor by the K¨unneth theorem, with H•(X,Pχ) also H•(X,Q) is
concentrated in degree zero. Using the hard Lefschetz axiom (D5), one
then deduces that for all n̸ = 0 one has H•(X, pHn(Q)) = 0 so that by (N3)
the subcategory N contains pHn(Q). Since this holds for arbitrary r ∈N, it
follows that P is an N-multiplier.
□
In view of part (a) of the lemma, to prove theorem 1.1 we want to show
that for a suitable subcategory N every object of P is an N-multiplier. For
this we will argue by contradiction, using the following
LEMMA 2.12. Suppose that N satisﬁes the stability axiom (N1) and the
Euler axiom (N4), that D satisﬁes all axioms (D1) – (D5) and that P ∈P is
not an N-multiplier. Then for some r ∈N the convolution power
(P∗P∨)∗r = (P∗P∨)∗···∗(P∗P∨)
admits a direct summand of the form 1[2i](i) with an integer i̸ = 0.
Proof. If P is not an N-multiplier, we can ﬁnd integers a,b ∈N such
that P∗a ∗(P∨)∗b admits a direct summand Q[i] for some i̸ = 0 and some
simple object Q ∈P which is not in N. By the hard Lefschetz axiom (D5)
then Q[−i](−i) is a direct summand of P∗a ∗(P∨)∗b as well. It then follows
that also the dual Q∨[i](i) is a direct summand of P∗b ∗(P∨)∗a. Altogether
then the convolution product Q[i]∗Q∨[i](i) = Q∗Q∨[2i](i) will be a direct
summand of (P∗P∨)∗r for the exponent r = a+b.
It remains to show that 1 is a direct summand of Q ∗Q∨. For this note
that the trace map tr(Q) : 1 −→Q ∗Q∨∼= Q∨∗Q −→1 is non-zero since
we have χ(Q)̸ = 0 by axiom (N4). Now tr(Q) factors over pH0(Q ∗Q∨),
indeed HomD(P, pτ>0P) = HomD(pτ<0P,P) = 0. So tr(Q) exhibits 1 as a
retract of pH0(Q∗Q∨) in the abelian category P, and we are done.
□
38
Chapter 2 – Proof of the vanishing theorem(s)
