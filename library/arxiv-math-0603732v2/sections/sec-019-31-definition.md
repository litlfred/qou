---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-019-31-definition
section_title: "Definition"
section_number: 3.1
pages: 9-10
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
---
also [FT, HK1]), is M as a k-vector space, with right A-action given by
m · a =
X
S(a2)ma1
for all a ∈A and m ∈M. Below we shall want to combine twisting with the right
adjoint action, producing right modules of the form (σAτ)′ which will be crucial in
our calculation of Hochschild homology. Parallel results to those stated in (2.2),
(2.3) and (2.4) can be derived for R(−). We shall omit most of the statements.
The following lemma will be used later.
For π ∈G(A◦), we write kπ for the
corresponding right A-module A/ ker π.
Lemma. Let A be a Hopf algebra, let π, φ ∈G(A◦) and let σ ∈Autk-alg(A). Let
M be an A-bimodule. From (b) to (e) we assume S is bijective. In (d) and (e)
we assume that the left integral of A exists. In (b) to (e) we identify the spaces of
homomorphisms with vector subspaces of M or A as appropriate.
(a) kσ
π ∼= kπσ.
(b) HomAop(k, (S−2M σ)′) = Zσ
A(M).
(c) HomAop(kφ∗π, (M Ξ[φ])′) = HomAop(kπ, (M)′). As a consequence,
HomAop(kφ∗π, (S−2AσΞ[φ])′) = HomAop(kπ, (S−2Aσ)′).
(d) HomAop(
R l, (S−2Aσ)′) = Z(Aσξ−1). That is,
HomAop(
R l, (Aσ)′) = Z(AS−2σ ξ−1) ∼= Z(AS−2ξ−1σ).
(e) HomAop(
R l, (S−2Aξ)′) = Z(A) = HomAop(
R l, (ξ−1S−2A)′).
Proof. (a) follows from the deﬁnitions.
(b) By Lemma 2.3(a) we may assume σ = idA. The right A-action on (S−2M)′
is then given by
m · a =
X
S−1(a2)ma1
10
K.A. BROWN AND J.J. ZHANG
for all m ∈M and a ∈A, and so we need to prove that
HomAop(k, (S−2M)′) = Z(M).
The proof of Lemma 2.4(a) can be modiﬁed and we leave the details to the reader.
(c) We may, in a similar way to the proof of (b), identify both the spaces of
maps in question with subspaces of the k-vector space M. The rest of the proof is
straightforward.
The second assertion follows by taking M = S−2Aσ.
(d) As a right module,
R l is by deﬁnition isomorphic to kπ0. So from (c) with
π = π0 and φ = π−1
0 , together with (b) with A for M, we see that
HomAop(
R l, (S−2Aσ)′)
=
Zσ
A(A).
The ﬁrst isomorphism in (d) now follows from Lemma 2.3(a). The second isomor-
phism in (d) follows from the ﬁrst after we observe that (Aσ)′ ∼= (S−2AS−2σ)′, which
is clear from (2.3.1).
(e) In view of (2.3.2), this is a special case of (d).
□
