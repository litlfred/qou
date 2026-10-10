---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-018-26-the-right-adjoint-action
section_title: "The right adjoint action"
section_number: 2.6
pages: 9-10
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
module R(M ) [Mo, Deﬁnition 3.4.1(2)], which we shall often denote by M ′ (see
also [FT, HK1]), is M as a k-vector space, with right A-action given by
m · a =
∑
S(a2)ma1
for all a ∈ A and m ∈ M . Below we shall want to combine twisting with the right
adjoint action, producing right modules of the form ( σAτ )′ which will be crucial in
our calculation of Hochschild homology. Parallel results to those sta ted in (2.2),
(2.3) and (2.4) can be derived for R(−). We shall omit most of the statements.
The following lemma will be used later. For π ∈ G(A◦), we write kπ for the
corresponding right A-module A/ ker π.
Lemma. Let A be a Hopf algebra, let π, φ ∈ G(A◦) and let σ ∈ Autk-alg(A). Let
M be an A-bimodule. From (b) to (e) we assume S is bijective. In (d) and (e)
we assume that the left integral of A exists. In (b) to (e) we identify the spaces of
homomorphisms with vector subspaces of M or A as appropriate.
(a) kσ
π ∼= kπσ .
(b) HomAop (k, (S−2
M σ)′) = Z σ
A(M ).
(c) HomAop (kφ∗π, (M Ξ[ φ])′) = Hom Aop(kπ, (M )′). As a consequence,
HomAop(kφ∗π, (S−2
AσΞ[ φ])′) = Hom Aop (kπ, (S−2
Aσ)′).
(d) HomAop (
∫ l, (S−2
Aσ)′) = Z(Aσξ−1
). That is,
HomAop(
∫ l, (Aσ)′) = Z(AS−2σ ξ −1
) ∼= Z(AS−2ξ−1σ).
(e) HomAop (
∫ l
, (S−2
Aξ)′) = Z(A) = Hom Aop(
∫ l
, (ξ−1S−2
A)′).
Proof. (a) follows from the deﬁnitions.
(b) By Lemma 2.3(a) we may assume σ = id A. The right A-action on ( S−2
M )′
is then given by
m · a =
∑
S−1(a2)ma1
10 K.A. BROWN AND J.J. ZHANG
for all m ∈ M and a ∈ A, and so we need to prove that
HomAop(k, (S−2
M )′) = Z(M ).
The proof of Lemma 2.4(a) can be modiﬁed and we leave the details to t he reader.
(c) We may, in a similar way to the proof of (b), identify both the spac es of
maps in question with subspaces of the k-vector space M . The rest of the proof is
straightforward.
The second assertion follows by taking M = S−2
Aσ.
(d) As a right module,
∫ l
is by deﬁnition isomorphic to kπ0 . So from (c) with
π = π0 and φ = π−1
0 , together with (b) with A for M , we see that
HomAop(
∫ l, (S−2
Aσ)′) = Z σ
A(A).
The ﬁrst isomorphism in (d) now follows from Lemma 2.3(a). The secon d isomor-
phism in (d) follows from the ﬁrst after we observe that ( Aσ)′ ∼= (S−2
AS−2σ)′, which
is clear from (2.3.1).
(e) In view of (2.3.2), this is a special case of (d). □
