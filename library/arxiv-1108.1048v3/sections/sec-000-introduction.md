---
doc_id: arxiv-1108.1048v3
doc_title: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 1108.1048v3.pdf
source_sha256: 6f2b83450ba923d0
doc_brief: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS — We give an explicit construction of irreducible modules ove r Khovanov-Lauda- Rouquier algebras R and their"
---
The Khovanov-Lauda-Rouquier algebras (KLR algebras) were introduced independently by
Khovanov-Lauda [19, 20] and Rouquier [26] to give a categori ﬁcation of quantum groups. Let
Uq(g) be the quantum group associated with a symmetrizable Carta n datum, and let R be
the corresponding KLR algebra. For a dominant integral weig ht λ of Uq(g), the algebra
R has a special quotient Rλ corresponding to λ, which is called the cyclotomic Khovanov-
Lauda-Rouquier algebra (cyclotomic KLR algebra ) of weight λ. It was conjectured that the
cyclotomic quotient Rλ gives a categoriﬁcation of the irreducible highest weight Uq(g)-module
V (λ). This was shown for type A in [1, 2, 4]. In [12], Kang and Kashiwara proved this
conjecture for all symmetrizable Cartan data. Webster [27] has announced a categoriﬁcation
of tensor products of highest weight modules. In a recent pap er, Kang, Oh and Park [14]
extended the study of KLR algebras to provide a categoriﬁcat ion of quantum generalized
Kac-Moody algebras and their crystals. Moreover, Kang, Kas hiwara and Oh [13] proved the
2000 Mathematics Subject Classiﬁcation. 05E10, 16D60, 17B67, 81R10.
Key words and phrases. adapted strings, crystal bases, Khovanov-Lauda-Rouquier algebras.
1 This work was supported by KRF Grant # 2007-341-C00001.
2 This work was supported by NRF Grant # 2010-0010753.
3 This work was supported by NRF Grant # 2010-0019516.
4 This work was supported by BK21 Mathematical Sciences Divis ion.
1
2 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PAR K
cyclotomic categoriﬁcation conjecture for irreducible hi ghest weight modules over quantum
generalized Kac-Moody algebras.
For symmetrizable Cartan data, the set B(∞) (resp. B(λ)) of isomorphism classes of ﬁnite-
dimensional irreducible graded modules over R (resp. Rλ) can be given a crystal structure,
and Lauda and Vazirani [22] have shown that there exist cryst al isomorphisms B(∞) ∼− →
B(∞) and B(λ) ∼− →B(λ), where B(∞) (resp. B(λ)) is the crystal of U −
q (g) (resp. V (λ)).
Kleshchev and Ram [21] gave a construction of irreducible gr aded R-modules for all ﬁnite
types by using the combinatorics of Lyndon words to construc t irreducible R-modules as the
irreducible heads of the induced modules of the outer tensor products of cuspidal modules .
In this approach, the action of Kashiwara operators on the cr ystal of irreducible modules is
hidden in the combinatorics of Lyndon words. Hill, Melvin an d Mondragon [7] completed
the classiﬁcation of irreducible R-modules begun by Kleshchev and Ram by determining the
cuspidal modules. Recently, McNamara [25] investigated th is approach using PBW basis
theory and computed the global dimension of R for ﬁnite type. However, it remains an open
problem to construct irreducible graded Rλ-modules. For ﬁnite and aﬃne type A, results in
[1, 3, 10] tell us that the algebra Rλ has a cellular basis, which yields irreducible modules by
using the cellular basis techniques introduced in [6].
In this paper, we give an explicit construction of all irredu cible graded modules over R and
Rλ for KLR algebras of ﬁnite classical type as the irreducible h eads of certain induced mod-
ules. This generalizes the type An result in [15] to all ﬁnite classical types. Our constructio n
diﬀers from the one given by Kleshchev and Ram and is based on th e theory of crystal bases.
As a result, the action of the Kashiwara operators is an integ ral part of the construction.
Here is a brief description of our work. Let ( A, P, Π , P∨, Π ∨) be a symmetrizable Cartan
datum. Let I be the index set of the simple roots, and let n = |I|. Set I(n+1) = I and take
I(k) (k = 1, . . . , n) to be subsets of I such that I(k) ⊂ I(k+1) and |I(k)| = k for all k. Let Bk
be the crystal obtained from B(∞) by forgetting the i-arrows for i /∈ I(k). For v ∈ B(∞), let
u0 = v and let uk be the highest weight vector of the connected component of Bk containing
v for k = 1, . . . , n. Then, there exists a sequence ik of elements in I such that uk−1 = ˜fikuk,
where ˜fik is a product of the Kashiwara operators corresponding to the terms in the sequence
ik. For k = 1, . . . , n, deﬁne
Nk(v) = ˜fik1,
where 1 is the trivial for the KLR algebra R(0) := C. In Proposition 1.10, we prove for
any symmetrizable Cartan datum that hd Ind(N1(v) ⊠ · · · ⊠ Nn(v)) is an irreducible graded
R-module and that the map Φ : B(∞) − →B(∞) deﬁned by
(0.1) Φ( v) = hd Ind (N1(v) ⊠ · · · ⊠ Nn(v)) for v ∈ B(∞)
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 3
is a crystal isomorphism.
When A is of ﬁnite type, the modules Nk(v) can be given a more explicit description in
terms of the Kashiwara operators ˜fi via the adapted strings introduced by Littelmann in [24].
For this, we choose a special expression w0 = rs1 · · ·rsn of the longest element w0 in the Weyl
group W . Here the sk are sequences of indices in I (see Table 1). Using the description of
adapted strings given in [24], we prove for v ∈ B(∞) that
Nk(v) = ˜f a(v)k
sk 1,
where a(v) is the adapted string of v with respect to this expression for w0, and a(v)k is the
subsequence of a(v) deﬁned by (2.3) (see Proposition 2.3 below).
Our main result is an explicit construction of the irreducib le graded modules over the KLR
algebras R and Rλ of ﬁnite classical type An, Bn, Cn, Dn in terms of adapted strings. Let S
(resp. S λ) be the set of adapted strings of B(∞) (resp. B(λ)) given in Proposition 3.1, and
let B be the crystal of the irreducible module V (Λ n) labeled by the fundamental weight Λ n
if A is of type An (resp. V (Λ 1) if A is of type Bn, Cn, Dn). For a, b ∈ B with a ≻ b, using
the structure of the crystal B, in (3.3) we associate to a, b an irreducible graded module
∆ (a,b). The modules ∆ (a,b) are 1- or 2-dimensional, and in general they are not the cuspidal
modules found in [7, 21]. Using the description of S (resp. S λ), we deﬁne for v ∈ B(∞) (resp.
v ∈ B(λ)) the module ∆( a(v); k) to be the outer tensor product of modules ∆ (a,b) as in (3.5).
Then, it follows from Lemma 4.3 that
(0.2) Nk(v) = hd Ind∆( a(v); k) for k = 1, . . . , n.
The description of the irreducible modules in (0.1) works fo r all symmetrizable Cartan
data. It follows from (0.1) and (0.2) that the irreducible mo dules for the KLR algebras of
ﬁnite classical type can be obtained from taking the outer te nsor product of heads of induced
modules, inducing, then taking the head of the induced modul e. But this unduly complicated
process can be simpliﬁed. Indeed, we prove for the module ∆( a(v)) := ∆( a(v); 1) ⊠ · · · ⊠
∆( a(v); n) that hd Ind∆( a(v)) is irreducible for v ∈ B(∞) (resp. v ∈ B(λ)) for all ﬁnite
classical types and that the maps
Ψ : B(∞) − →B(∞) given by Ψ( v) = hd Ind ∆( a(v)) for v ∈ B(∞),
Ψ λ :B(λ) − →B(λ) given by Ψ λ(v) = hd Ind ∆( a(v)) for v ∈ B(λ)
are crystal isomorphisms (Theorem 3.2). Using that fact, we show for the ﬁnite classical
types that
A = {hd Ind∆( a) | a ∈ S} and
Aλ = {hd Ind∆( a) | a ∈ S λ},
4 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PAR K
as a ranges over the adapted strings, provide complete lists of a ll the irreducible graded
modules over R and Rλ, respectively, up to isomorphism and grading shift (Coroll ary 3.3).
Our paper is organized as follows. Section 1 contains a brief review of crystal bases and
KLR algebras associated with any symmetrizable Cartan datu m. This section culminates
with the proof of the crystal isomorphism Φ : B(∞) − →B(∞) in (0.1). Section 2 specializes
to the case of ﬁnite type, ﬁrst reviewing Littelmann’s resul t (see [24]) on adapted stings and
then giving an explicit description of the modules Nk(v) for all ﬁnite types via adapted stings.
Combining this description with the deﬁnition of Nk(v), we obtain an expression for Nk(v)
in terms of Kashiwara operators.
In Section 3, we restrict to the case of ﬁnite classical types . We ﬁrst deﬁne the modules
