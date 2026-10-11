---
doc_id: arxiv-2504.18825v2
doc_title: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications"
section_id: sec-007-appendix-a-an-alternative-proof-of-corollary-63
section_title: "Appendix A. An alternative proof of Corollary 6.3"
section_number: null
pages: 49-51
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
toc_source: outline
doc_brief: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications — We establish a Murnaghan–Nakayama rule for the irreducible characters of the cyclotomic Hecke algebra Hm,n(q, u) on Shoji’s"
---
In this appendix, we present an alternative proof of Corollary 6.3 based on the Regev
formula for the Hecke algebra of type A. To proceed with this, we elaborate on the associ-
ation between the irreducible characters of the cyclotomic Hecke algebra and those of the
Hecke algebra of type A.
For a m-multimatrix M ∈Mm(µ), recall that
ci(M) := (m(1)
1,i , · · · , m(1)
l(µ(1)),i, m(2)
1,i , · · · , m(2)
l(µ(2)),i, · · · , m(m)
1,i , · · · , m(m)
l(µ(m)),i).
and −→c i(M) is the partition obtained by rearranging ci(M).
Lemma A.1. Let ψλ be the irreducible character of the Hecke algebra in type A indexed
by λ. Suppose λ, µ are two multipartitions of n. Then we have
χλ
µ =
X
M
uM(q −q−1)#M−l(µ)
m
Y
i=1
ψλ(i)
−
→c i(M),
(A.1)
summed over all m-multimatrices M such that the j-th row sum of M (r) equals µ(r)
j
and
|ci(M)| = |λ(i)|.
Proof. This can be derived by the following calculations.
χλ
µ = ⟨qµ, sλ⟩⊗
=
*
qn
(q −q−1)l(µ)
X
M
uMqM(x; q−2), sλ
+
⊗
(by (8.8))
50
NAIHUAN JING AND NING LIU
=
X
M
uM(q −q−1)#M−l(µ)
* m
Y
i=1
q|ci(M)|
(q −q−1)l(ci(M))qci(M)(x(i); q−2),
m
Y
i=1
sλ(i)(x(i))
+
⊗
=
X
M
uM(q −q−1)#M−l(µ)
m
Y
i=1

q|ci(M)|
(q −q−1)l(ci(M))qci(M)(x(i); q−2), sλ(i)(x(i))

=
X
M
uM(q −q−1)#M−l(µ)
m
Y
i=1
ψλ(i)
−
→c i(M).
□
Lemma A.2. ([JL22, Theorem 3.1],[Zha19, Theorem B]) The Regev formula for the Hecke
algebra in type A states that
X
λ⊢|µ|
λ hook
ψλ
µ = 2l(µ)−1
l(µ)
Y
i=1
[µi]−q−2.
(A.2)
Now we are ready to provide an alternative proof of Corollary 6.3.
Proof of Corollary 6.3.
X
λ⊢|µ|
λ(i) hook
2L(λ)χλ
µ
=
X
λ⊢|µ|
λ(i) hook
2L(λ) X
M
uM(q −q−1)#M−l(µ)
m
Y
i=1
ψλ(i)
−
→
ci (M)
(by (A.1))
=
X
M
uM(q −q−1)#M−l(µ)
X
λ⊢|µ|
λ(i) hook, |λ(i)|=|ci(M)|
2L(λ)
m
Y
i=1
ψλ(i)
−
→
ci (M)
=
X
M
uM(q −q−1)#M−l(µ)
m
Y
i=1
21−δ|ci(M)|,0
X
ρ⊢|ci(M)|
ρ hook
ψρ
−
→
ci (M)
=
X
M
uM(q −q−1)#M−l(µ)
m
Y
i=1
21−δ|ci(M)|,0







2 l(−
→
ci (M))−1
m
Y
r=1
l(µ(r))
Y
j=1
[m(r)
ji ]−q−2,
if |ci(M)| > 0,
1,
if |ci(M)| = 0,
(by (A.2))
=
X
M
uM(q −q−1)#M−l(µ)2#M
Y
m(r)
ij ∈M
[m(r)
ij ]−q−2.
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
51
In the last step, we used the identity
m
X
i=1
l(−→
ci (M)) = #M.
This completes the proof.
□
