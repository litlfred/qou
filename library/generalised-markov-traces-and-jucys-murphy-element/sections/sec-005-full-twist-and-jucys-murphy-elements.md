---
doc_id: generalised-markov-traces-and-jucys-murphy-element
doc_title: "Glasgow Mathematical Journal (2026), 1–10"
section_id: sec-005-full-twist-and-jucys-murphy-elements
section_title: "`Full twist' and Jucys-Murphy elements"
section_number: null
pages: 3-4
source_pdf: Generalised_Markov_traces_and_Jucys-Murphy_element.pdf
source_sha256: 9246e10a44d0b4aa
toc_source: outline
doc_brief: "Glasgow Mathematical Journal (2026), 1–10 — We give a simple construction of Markov traces for Iwahori–Hecke algebras associated with the crystallographic Coxeter groups of types An, Bn and Dn."
---
Assume that (W, S) is of ﬁnite type. Let w0 stand for the longest element in W with respect to the Bruhat
length. Let S(W, S) = t−2
w0 ∈H(W, S). In classical types, we will write S(Xn) ∈H(Xn), when X is A, B or
D, or simply S when the type is clear from the context.
The following proposition is also standard:
Proposition 2.4.1. The element S(W, S) is central in H(W, S).
We will need the following ‘Serre property’ of the operator of multiplication by S(W, S).
Proposition 2.4.2. For any h1, h2 ∈H(W, S), we have the identity
⟨h1, S(W, S)h2⟩= ⟨h2, h1⟩.
Proof. By Proposition 2.3.1 (b), it is enough to prove the statement for h1 = t−1
w1 , h2 = tw2 for arbitrary
w1, w2 ∈W. We have, by Proposition 2.3.1 (c),
⟨t−1
w1 , S(W, S)tw2⟩= ⟨tw0t−1
w1 , t−1
w0 tw2⟩= ⟨tw0w−1
1 , t−1
w−1
2 w0⟩
= δw0w−1
1 ,w0w2 = δw1,w−1
2 = ⟨tw2, t−1
w1 ⟩.
This completes the proof.
4
Kostiantyn Tolmachov and Heorhii Zhylinskyi
We have the natural embedding ιn : H(Xn) →H(Xn+1), where X is A, B or D, induced by the embed-
ding of the sets of labels of the Coxeter diagram. Using these embeddings, an element of H(Xn) can be
considered as an element of H(Xm) for m > n.
Deﬁnition 2.4.3. For n ≥2, let JX
n = S(Xn)−1 · S(Xn−1) when X is A−1, B or D. We let JA
1 = 1, JB
1 = t2
0,
JD
1 = 1. We call these elements Jucys–Murphy elements of ﬁnite Hecke algebras in classical types.
We have the following corollary of Proposition 2.4.1.
Corollary 2.4.4. For X equal to A−1, B or D, elements JX
k commute with each other when considered
lying in the same Iwahori–Hecke algebra via the embedding described above. The element JX
n lies in the
centraliser of H(Xn−1) in H(Xn).
Remark 2.4.5. The elements JA
k are sometimes called multiplicative Jucys–Murphy elements in the
Iwahori–Hecke algebra of type A. There seems to be no agreement in the literature on which elements to
call the Jucys–Murphy elements in other types. We chose our convention because under it the deﬁnition
of the Jucys–Murphy element is uniform in all types, but elements jX
k for X = B, D deﬁned below arguably
also deserve the name.
