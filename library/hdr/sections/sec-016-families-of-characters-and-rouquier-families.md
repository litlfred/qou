---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-016-families-of-characters-and-rouquier-families
section_title: "Families of characters and Rouquier families"
section_number: null
pages: 35-36
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "Hecke algebras, generalisations and representation theory — 27 sections: Algebras of Finite Type; Blocks; Symmetrising forms and Schur eleme"
---
The Rouquier families for cyclotomic Hecke algebras associated with the complex reﬂection group
G(l, 1,n ), that is, cyclotomic Ariki–Koike algebras, have been ﬁrst determined by Brou´ e and Kim [BrKi],
but it turned out that their results were only true in the case where l is a power of a prime number.
In [Ch3], we gave the correct families for any l, using the property of semicontinuity explained in the
previous chapter. In fact, we discovered that the Rouquier families for G(l, 1,n ) are determined by the
families of characters of Weyl groups of type B.
Letr,r 0,r 1,...,r l∈ Z. If r⁄= 0, set mi :=ri/r for all i = 0,...,l − 1 and m := (m0,...,m l−1)∈ Ql.
Let u be an indeterminate. Let
ϕ : Z[q±1,Q±1
0 ,...,Q ±1
l−1]→ Z[u±1]
be the cyclotomic specialisation deﬁned by
ϕ(q) =ur and ϕ(Qi) =ζi
luri.
Then we have the following result due to Brou´ e and Kim [BrKi].
Proposition 4.5 Let λ, µ∈P (l,n ) and assume that r⁄= 0. If Eλ and Eµ are in the same Rouquier
family, then Contcλ = Contc µ with respect to the weight system m. The converse is true when l is a
power of a prime number.
Now, using the form of the Schur elements, we obtain that the essential hyperplanes forG(l, 1,n ) are:
• kr +rs−rt = 0 for all−n<k<n if ζs
l−ζt
l is not a unit in Z[ζl].
32
• r = 0.
Remark 4.6 Note that, according to Theorem 3.10, the Rouquier families do not depend on the actual
values of the ri’s and r, but only on the essential hyperplanes to which they belong. Therefore, as long
as r⁄= 0, we can always restrict to the case r = 1.
It is obvious from the form of the Schur elements that the Rouquier families associated with no
essential hyperplane are all trivial. We now have the following two results about the Rouquier families
associated with the essential hyperplanes described above [Ch3, Propositions 3.15, 3.16, 3.17]:
Proposition 4.7 Let λ, µ∈P (l,n ). The following are equivalent :
(1) Eλ andEµ are in the same Rouquier family associated with the essential hyperplane kr +rs−rt = 0.
(2) λ(i) = µ(i) for all i /∈{ s,t} and Contc(λ(s),λ(t)) = Contc(µ(s),µ(t)) with respect to the weight system
(0,k ).
(3) λ(i) = µ(i) for all i /∈{ s,t} and Contc(λ(s),λ(t)) = Contc(µ(s),µ(t)) with respect to the weight system
(ms,mt).
(4) λ(i) = µ(i) for all i /∈ {s,t} and E(λ(s),λ(t)), E(µ(s),µ(t)) are in the same Rouquier family of the
cyclotomic Ariki–Koike algebra of type B|λ(s)|+|λ(t)| obtained via the specialisation :
q↦→ur,Q 0↦→urs,Q 1↦→−urt
Proposition 4.8 Let λ, µ∈P (l,n ). Then Eλ and Eµ are in the same Rouquier family associated with
the essential hyperplane r = 0 if and only if |λ(i)| =|µ(i)| for all i = 0,...,l − 1.
Using the above results, we managed to prove that the functions a and A are constant on Rouquier
families (for r⁄= 0, this was already a known consequence of Proposition 4.5). We also created the
program RBAK.g, available on my webpage [Ch-web], which allows the computation of the Rouquier
families for any cyclotomic Ariki–Koike algebra on GAP3.
Finally, the results above allowed for the correct determination of the Rouquier families of the cyclo-
tomic Hecke algebras associated with the complex reﬂection groups G(l,p,n ), with the use of Cliﬀord
theory, in the cases where n> 2, or n = 2 and p is odd [Ch5].
