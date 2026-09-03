---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-007-markov-traces-via-jucys-murphy-elements
section_title: "Markov traces via Jucys-Murphy elements."
section_number: null
pages: 5-9
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — WegiveasimpleconstructionofMarkovtracesforIwahori-Heckealgebrasassociated with infinite series of crystallographic Coxeter groups."
---
Definition 3.1.1. LetR be a commutativeA-algebra. A family (ϕn) ofA-linear
functionals ϕn :H(Xn), where X is A−1,B or D and n∈ Z≥1 (n∈ Z≥2 in typeD) is
called a Markov trace if there are elementsµ,ρ∈R such that the following conditions
are satisfied.
5
(M1). ϕn is a trace function, i.e.ϕn(hh′) = ϕn(h′h). This property is a generalization
of the first Markov move from the theory of link invariants.
Recall the embeddingι =ιn−1 :H(Xn−1)→H (Xn) defined in Section 2.4. The
functionals ϕn−1 and ϕn, n≥ 2 must satisfy
(U1). ϕn(ι(h)) = ρϕn−1(h). This property is a generalization of a rule for removing an
unlinked circle in the theory of link invariants.
(M2). ϕn(ι(h)tn) = µϕn−1(h). This property is a generalization of the second Markov
move from the theory of link invariants.
Notethatif (ϕn)isaMarkovtracewithconstants ρ,µ, then, forarbitraryλ1,λ 2∈R ,
(λ1λn
2ϕn) is again a Markov trace with constantsλ2ρ,λ 2µ.
Remark 3.1.2.We exclude smalln in our definition of the Markov trace because some
special treatment is needed for the embeddingsB0→ B1,D 0→ D1→ D2. For the
geometric traces these properties are extended to smalln, see Section 3.3.
Definition 3.1.3. Assume that the involutionv7→v−1 is extended toR. We say that
an elementz∈H (W,S )⊗AR represents a functionalϕ :H(W,S )→R ifϕ(h) =⟨z,h⟩
for anyh∈H (W,S ). It is easy to see thatϕ satisfies the property (M1) if and only if
z is in the center ofH(W,S ). In this case we writeϕ = trz.
LetR =A(a) and leta =a−1. Define
ζn =
nY
i=1
(1 +a−1JX
i ),ζ 0 = 1,
an element inH(Xn) when X = A−1,B or D. By Corollary 2.5.3, elements ζn are
central in the corresponding Iwahori-Hecke algebras. We prove
Theorem 3.1.4. The family of functionals (trζn) is a Markov trace with constants
ρ = 1 +a,µ =v−v−1.
Proof. We first check the property (U1). We have
⟨ζn,ι (h)⟩ =⟨ζn−1(1 +a−1JX
n ),ι (h)⟩ =⟨ζn−1,ι (h)⟩ +a⟨ζn−1JX
n ,ι (h)⟩.
Applying Proposition 2.4.2 twice — recall thatJX
n = S(Xn)−1S(Xn−1) — we get the
equality⟨ζn−1JX
n ,ι (h)⟩ =⟨ζn−1,ι (h)⟩ and (U1) follows.
We now check the property (M2). We have
(1) ⟨ζn,ι (h)tn⟩ =⟨ζn−1(1 +a−1JX
n ),ι (h)tn⟩ =⟨ζn−1,ι (h)tn⟩ +a⟨ζn−1JX
n ,ι (h)tn⟩ =
=⟨ζn−1,ι (h)t−1
n ⟩ + (v−v−1)⟨ζn−1,ι (h)⟩ +a⟨ζn−1JX
n ,ι (h)tn⟩.
From Corollary 2.3.2, we get that⟨ζn−1,ι (h)t−1
n ⟩ = 0.
For the third summand in the last expression in (1), applying Proposition 2.4.2, we
have
⟨ζn−1JX
n ,ι (h)tn⟩ =⟨ι(h)tn,ζn−1S(Xn−1)⟩ = 0,
with the last equality again following from Corollary 2.3.2. We obtain (M2).
Remark 3.1.5. We will show below that, in typesA and B (but not in typeD), the
traces trζn coincide with the traces coming from geometry. See Section 3.3.
6
3.2 General Markov traces in typesB,D. In typeA, the classical result of Jones
and Ocneanu [Jon87] says that a Markov trace with given constantsρ,µ is defined
uniquely up to an overall scaling. Thus, Theorem 3.1.4 gives a general description of a
Markov trace in typeA.
In typesB,D, the general description of Markov traces was obtained by Geck and
Lambropoulou [GL97], [Gec98]. We recall their results.
Forn≥ 1, define the elements
Tn =tn−1...t 1t0t−1
1 ...t −1
n−1∈H (Bn),n≥ 2,T 1 =t0,
and
Un =tn−1...t ′
1t−1
1 ...t −1
n−1∈H (Dn),n≥ 2,U 1 = 1.
Theorem 3.2.1([GL97], [Gec98]). LetR =A(a,y 1,...,y n,... ), with infinite number
of variable yk. There is a unique Markov trace (trX
n,(y•)), where X is B or D, with
values inR, with constantsρ = 1 +a,µ =v−v−1, normalization trX
n,(y•)(1) = (1 +a)n
and additional properties:
(B). trB
n,(y•)(T1T2...T n) =yn, n≥ 1, in typeB.
(D). trD
2n,(y•)(U1U2...U 2n) =y2n, n≥ 1, in typeD.
Any Markov trace with the chosenρ,µ and normalization is of this form. Moreover,
every such Markov trace in typeD is obtained by restriction from the Markov trace on
Hv,1(Bn) (see Section 2.5).
We will be interested in a particular case of these traces whenyn is of the form
yn = yn. Let from now onR = A(y) and denote by trX
n,y the Markov trace from
Theorem 3.2.1 withyn = yn for alln≥ 1. Extend the bar involution toR, formally
writing y — we assume that such an extension exists under any specialization ofy we
will use. To simplify the formulas, we adopt the notationα =v−v−1,α 0 =v0−v−1
0 .
Define the elements
βn(y) =
nY
i=1
(1 + (y +α0)jB
i +a−1JB
i )∈H v,v0(Bn)⊗AR.
By Corollary 2.5.3, the element βn(y) is central inHv,v0(Bn)⊗AR. We have the
following
Theorem 3.2.2. The equality trB
n,y = trβn(y) holds.
The property in Theorem 3.2.1 (B) follows from the more general property (compare
[GL97, Proposition 4.5]).
Proposition 3.2.3. For anyh∈H (Bn−1), we havetrβn(y)(ι(h)Tn) =ytrβn−1(y)(h).
Proof. We will use the following lemma, verified by a direct computation.
Lemma 3.2.4. (a). We haveT−1
n =Tn−α0.
(b). The elementsTn,T−1
n satisfy
Tn∈ spanA⟨tw,w∈W (Bn)\W (Bn−1)⟩
and
T−1
n ∈ spanA⟨t−1
w ,w∈W (Bn)\W (Bn−1)⟩.
7
(c). The element (jB
n )−1Tn satisfies
(jB
n )−1Tn− 1∈ spanA⟨t−1
w ,w∈W (Bn)\W (Bn−1)⟩.
To simplify the formulas, introduce the notationy′ =y−α0,y′ =y +α0. We have
⟨βn(y),ι (h)Tn⟩ =⟨βn−1(y),ι (h)Tn⟩ +y′⟨βn−1(y)jB
n,ι (h)Tn⟩ +a⟨βn−1(y)JB
n,ι (h)Tn⟩.
Let us examine the summands on the right-hand side of this equation one by one.
We will rutinely use the Corollary 2.3.2. For the first summand, we have, by Lemma
3.2.4 (a), (b),
⟨βn−1(y),ι (h)Tn⟩ =⟨βn−1(y),ι (h)T−1
n ⟩ +α0⟨βn−1(y),ι (h)⟩ =α0⟨βn−1(y),ι (h)⟩.
For the second summand, first note thatjB
n is in the centralizer ofH(Xn−1) inH(Xn).
It follows that
y′⟨βn−1(y)jB
n,ι (h)Tn⟩ =y′⟨βn−1(y),ι (h)(jB
n )−1Tn⟩.
Thus we have, by Lemma 3.2.4 (c),
y′⟨βn−1(y),ι (h)(jB
n )−1Tn⟩ =y′⟨βn−1(y),ι (h)⟩.
For the third summand, by Proposition 2.4.2 and Lemma 3.2.4 (b), we have
a⟨βn−1(y)JB
n,ι (h)Tn⟩ =⟨ι(h)Tn,βn−1(y)S(Bn−1)⟩ = 0.
Collecting all three summands together, we get
⟨βn(y),ι (h)Tn⟩ = (α0 +y′)⟨βn−1(y),ι (h)⟩ =y⟨βn−1(y),ι (h)⟩,
which completes the proof.
Proof of Theorem 3.2.2.It remains to check the properties (U1) and (M2). Note that
jB
n =tc,jB
nt−1
n =tc′ for c,c′∈W (Bn)\W (Bn−1). It follows from Corollary 2.3.2, that,
for anyh∈H (Bn−1) we have
⟨(y +α0)βn−1jB
n,ι (h)⟩ = 0 =⟨(y +α0)βn−1jB
n,ι (h)tn⟩,
which reduces the proof to the proof of Theorem 3.1.4.
From Theorems 3.2.1 and 3.2.2 we get the following description of a Markov trace
trD
n,y.
Corollary 3.2.5. Let
Pn(x1,...,x n;y) =
nY
i=1
(1 +yxi +a−1x2
i ),
a symmetric polynomial in variables(xi) overR. WritePn =P +
n +P−
n , a sum of even
and odd monomial degree parts. Letδn(y) =P +
n (jD
1 ,...,j D
n ;y). Then trD
n,y = trδn(y).
8
Proof. Recall that the tracetrD
n,(y•) is obtained by restriction oftrB
n,(y•) along the em-
bedding ιD→B :H(Dn)→H v,1(Bn), so that we have
trD
n,y(h) =⟨βn(y),ιD→B(h)⟩ =⟨P (jB
1 ,...,j B
n ;y),ιD→B(h)⟩.
It remains to observe that for all i we have jD
i = t0jB
i , and so every even degree
monomial injB
i is equal to the same monomial injD
i , sincet2
0 = 1 inHv,1(Bn) and t0
commutes withjB
i for alli; and that every odd degree monomial injB
i is orthogonal to
ιD→B(h) with respect to⟨,⟩. This completes the proof of the Corollary.
We have the following analogue of Proposition 3.2.3 in typeD.
Proposition 3.2.6. Forn≥ 1 and anyh∈H (D2n−2), we have
trD
2n,y(ι◦ι(h)U2n−1U2n) =y2trD
2n−2,y(h).
Proof. Note that we haveιD→B(Uk) =Tkt0, and so
trD
2n,y(ι◦ι(h)U2n−1U2n) = trB
2n,y(ι◦ι(h)T2n−1t0T2nt0).
Using the property (M1) and Proposition 3.2.3 twice, we get the result.
