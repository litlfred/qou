---
doc_id: generalised-markov-traces-and-jucys-murphy-element
doc_title: "Glasgow Mathematical Journal (2026), 1–10"
section_id: sec-009-general-markov-traces-in-types-b-d
section_title: "General Markov traces in types B, D"
section_number: null
pages: 6-8
source_pdf: Generalised_Markov_traces_and_Jucys-Murphy_element.pdf
source_sha256: 9246e10a44d0b4aa
toc_source: outline
doc_brief: "Glasgow Mathematical Journal (2026), 1–10 — We give a simple construction of Markov traces for Iwahori–Hecke algebras associated with the crystallographic Coxeter groups of types An, Bn and Dn."
---
In type A, the classical result of Jones and Ocneanu [10] says that a Markov trace with given constants
ρ, μ is deﬁned uniquely up to an overall scaling. Thus, Theorem 3.1.4 gives a general description of a
Markov trace in type A.
In types B, D, the general description of Markov traces was obtained by Geck and Lambropoulou
[3, 5]. We recall their results.
For n ≥1, deﬁne the elements
Tn = tn−1 . . . t1t0t−1
1 . . . t−1
n−1 ∈H(Bn), n ≥2, T1 = t0,
and
Un = tn−1 . . . t1′t−1
1 . . . t−1
n−1 ∈H(Dn), n ≥2, U1 = 1.
Theorem 3.2.1 ([3, 5]). Let R = A(a, y1, . . . , yn, . . . ), with inﬁnite number of variables yk. There is a
unique Markov trace (trX
n,(y•)), where X is B or D, with values in R, with constants ρ = 1 + a, μ = v −v−1,
normalisation trX
n,(y•)(1) = (1 + a)n and additional properties:
(B) trB
n,(y•)(T1T2 . . . Tn) = yn, n ≥1, in type B.
(D) trD
2n,(y•)(U1U2 . . . U2n) = y2n, n ≥1, in type D.
Any Markov trace with the chosen ρ, μ and normalisation is of this form. Moreover, every such
Markov trace in type D is obtained by restriction from the Markov trace on Hv,1(Bn) (see Section 2.5).
We will be interested in a particular case of these traces when yn is of the form yn = yn. Let from
now on R = A(y) and denote by trX
n,y the Markov trace from Theorem 3.2.1 with yn = yn for all n ≥1.
Extend the bar involution to R, formally writing y — we assume that such an extension exists under
any specialisation of y we will use. To simplify the formulas, we adopt the notation α = v −v−1, α0 =
v0 −v−1
0 . Deﬁne the elements
βn(y) =
n
i=1
(1 + (y + α0)jB
i + a−1JB
i ) ∈Hv,v0(Bn) ⊗A R.
By Corollary 2.5.3, the element βn(y) is central in Hv,v0(Bn) ⊗A R. We have the following
Theorem 3.2.2 The equality trB
n,y = trβn(y) holds.
We will use the following lemma, veriﬁed by a direct computation.
Lemma 3.2.3.
(a) We have T−1
n = Tn −α0.
(b) The elements Tn, T−1
n
satisfy
Tn ∈spanA⟨tw, w ∈W(Bn)\W(Bn−1)⟩
and
T−1
n ∈spanA⟨t−1
w , w ∈W(Bn)\W(Bn−1)⟩.
(c) The element (jB
n)−1Tn satisﬁes
(jB
n)−1Tn −1 ∈spanA⟨t−1
w , w ∈W(Bn)\W(Bn−1)⟩.
The property in Theorem 3.2.1 (B) follows from the more general property (compare [5, Proposition
4.5]).
Proposition 3.2.4. For any h ∈H(Bn−1), we have trβn(y)(ι(h)Tn) = ytrβn−1(y)(h).
Proof. To simplify the formulas, introduce the notation y′ = y −α0, y′ = y + α0. We have
⟨βn(y), ι(h)Tn⟩= ⟨βn−1(y), ι(h)Tn⟩+ y′⟨βn−1(y)jB
n, ι(h)Tn⟩+ a⟨βn−1(y)JB
n , ι(h)Tn⟩.
Let us examine the summands on the right-hand side of this equation one by one. We will routinely use
Corollary 2.3.2. For the ﬁrst summand, we have, by Lemma 3.2.3 (a), (b),
⟨βn−1(y), ι(h)Tn⟩= ⟨βn−1(y), ι(h)T−1
n ⟩+ α0⟨βn−1(y), ι(h)⟩= α0⟨βn−1(y), ι(h)⟩.
For the second summand, ﬁrst note that jB
n is in the centraliser of H(Bn−1) in H(Bn). It follows that
y′⟨βn−1(y)jB
n, ι(h)Tn⟩= y′⟨βn−1(y), ι(h)(jB
n)−1Tn⟩.
Thus, we have, by Lemma 3.2.3 (c),
y′⟨βn−1(y), ι(h)(jB
n)−1Tn⟩= y′⟨βn−1(y), ι(h)⟩.
For the third summand, by Proposition 2.4.2 and Lemma 3.2.3 (b), we have
a⟨βn−1(y)JB
n , ι(h)Tn⟩= ⟨ι(h)Tn, βn−1(y)S(Bn−1)⟩= 0.
Collecting all three summands together, we get
⟨βn(y), ι(h)Tn⟩= (α0 + y′)⟨βn−1(y), ι(h)⟩= y⟨βn−1(y), ι(h)⟩,
which completes the proof.
Proof of Theorem 3.2.2. It remains to check the properties (U1) and (M2). Note that the deﬁning
expression (1) for jB
n is reduced as a word in generators ti and ends in tn−1, so jB
n = tc, jB
nt−1
n−1 = tc′ for some
8
Kostiantyn Tolmachov and Heorhii Zhylinskyi
c, c′ ∈W(Bn)\W(Bn−1). It follows from Corollary 2.3.2 that, for any h ∈H(Bn−1) we have
⟨(y + α0)βn−1jB
n, ι(h)⟩= 0 = ⟨(y + α0)βn−1jB
n, ι(h)tn−1⟩,
which reduces the proof to the proof of Theorem 3.1.4.
From Theorems 3.2.1 and 3.2.2, we get the following description of a Markov trace trD
n,y.
Corollary 3.2.5. Let
Pn(x1, . . . , xn; y) =
n
i=1
(1 + yxi + a−1x2
i ),
a symmetric polynomial in the variables (xi) over R. Write Pn = P+
n + P−
n , a sum of even and odd
monomial degree parts. Let δn(y) = P+
n (jD
1 , . . . , jD
n ; y). Then trD
n,y = trδn(y).
Proof.
Recall that the trace trD
n,(y•) is obtained by restriction of trB
n,(y•) along the embedding
ιD→B : H(Dn) →Hv,1(Bn), so that we have
trD
n,y(h) = ⟨βn(y), ιD→B(h)⟩= ⟨Pn(jB
1, . . . , jB
n; y), ιD→B(h)⟩.
It remains to observe that for all i we have jD
i = t0jB
i , and so every even degree monomial in jB
i is equal
to the same monomial in jD
i , since t2
0 = 1 in Hv,1(Bn) and t0 commutes with jB
i for all i; and that every
odd degree monomial in jB
i is orthogonal to ιD→B(h) with respect to ⟨, ⟩. This completes the proof of the
Corollary.
We have the following analogue of Proposition 3.2.4 in type D.
Proposition 3.2.6. For n ≥1 and any h ∈H(D2n−2), we have
trD
2n,y(ι ◦ι(h)U2n−1U2n) = y2trD
2n−2,y(h).
Proof. Note that we have ιD→B(Uk) = t0Tk, and so
trD
2n,y(ι ◦ι(h)U2n−1U2n) = trB
2n,y(ι ◦ι(h)t0T2n−1t0T2n).
Using the property (M1) and Proposition 3.2.4 twice, we get the result.
