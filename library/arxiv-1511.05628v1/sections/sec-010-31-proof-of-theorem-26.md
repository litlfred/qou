---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-010-31-proof-of-theorem-26
section_title: "Proof of Theorem 2.6"
section_number: 3.1
pages: 12-14
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
is well-deﬁned over the set ( Z/kZ)N. This was observed in [GZ] and uses the fact that θk is
a solution to the Neumann-Zagier equations.
Lemma 3.1. [GZ] The summation in Equation (12) is k-periodic.
Proof. We need to show that
am+kej(θ) =am(θ).
This follows from the deﬁnition of am(θ) given in Equation (10), the fact that z is a solution
to the Neumann-Zagier equations, and Lemma 3.3 for the cyclic dilogarithm. □
To prove Theorem 2.6, recall the Galois extensionFG,k/Fk, and the elementam(θ) ofFG,k.
Let σj denote the j-th generator of the Galois group from Equation (9), and let
(30) ϵj(θ) =aej(θ)−1.
The next lemma was observed in [GZ].
Lemma 3.2. [GZ] For all m we have:
(31) am(σjθ)
am+ej(θ) =ϵj(θ).
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY 13
Proof. It suﬃces to show that the left hand side of the above equation is independent of m,
since the right hand side is the value at m = 0. To prove this claim, we compute
am(σjθ)
am+ej(θ) = e±πiB−1ν·m
e±πiB−1ν·(m+ej)· ζ
1
2(mT B−1Am±B−1ν·m)
ζ
1
2 ((m+ej)T B−1A(m+ej)±B−1ν·(m+ej))·
N∏
i=1
(σjθi)−(B−1Am)i
θ
−(B−1A(m+ej))i
i
·
N∏
i=1
(ζθ−1
i ;ζ)mi+δi,j
(ζσjθ−1
i ;ζ)mi
.
We focus on the m-dependent part of each of the 4 fractions. Obviously,
e±πiB−1ν·m
e±πiB−1ν·(m+ej) = (term independent of m) .
Next,
ζ
1
2(mT B−1Am±B−1ν·m)
ζ
1
2 ((m+ej)T B−1A(m+ej)±B−1ν·(m+ej)) =ζ−(B−1Am)j× (term independent of m).
Splitting the product of the third fraction to the case when j⁄= i and the case when j = i
implies that
N∏
i=1
(σjθi)−(B−1Am)i
θ
−(B−1A(m+ej))i
i
=ζ(B−1Am)j× (term independent of m) .
Using the identity
(ζθ−1
j ;ζ)mj+1
(ζ2θ−1
j ;ζ)mj
= 1−ζθ−1
j ,
and splitting the product of the fourth fraction to the case when j⁄= i and the case when
j =i implies that
(ζθ−1
i ;ζ)mi+δi,j
(ζσjθ−1
i ;ζ)mi
= (term independent of m) .
This completes the proof of the lemma. □
Using the fact that the sum is m-periodic it follows that
(32) σj

 ∑
m∈(Z/kZ)N
am(θ)

 =ej(θ)
∑
m∈(Z/kZ)N
am(θ).
Suppose that f(m,θ ) is a rational function of θ with the property that
(33) f(m,σjθ) =f(m +ej,θ )
for all j = 1,...,N and all m. Then, it follows that for all m we have
am(σjθ)f(m,σjθ) =ϵj(θ)am+ej(θ)f(m +ej,θ ).
14 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
Summing up, we obtain that
(34) σj

 ∑
m∈(Z/kZ)N
am(θ)f(m,θ )

 =ϵj(θ)
∑
m∈(Z/kZ)N
am(θ)f(m,θ ).
Equations (32) and (34) and the fact that FG,k/Fk is a Galois extension imply that if f
satisﬁes Equation (33), then Av(f(−,θ ))∈Fk.
Now observe that the vertex weights of the Feynman diagrams are Q(ζ)-linear combina-
tions of values of the polylogarithm Li l(ζmi+sθ−1
i ) for l < 0. Since the polylogarithm is a
rational function, andζmiθ−1
i satisﬁes Equation (33) for alli andj, Theorem 2.6 follows. □
