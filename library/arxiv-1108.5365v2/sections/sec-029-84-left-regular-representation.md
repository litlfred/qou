---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-029-84-left-regular-representation
section_title: "Left regular representation"
section_number: 8.4
pages: 82-85
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual"
---
Now we apply the pairing to the left corepresentation (7.61).
Theorem 8.11. The representation of Uq(gl(2, R)) is equivalent to
∫
R
∫ ⊕
R+
Pλ,s2/2|Sb(Q + 2iλ)|2dλds2⊗L2(R,dt 2),
where the representation space Pλ,s2/2 =L2(R,ds 1) is deﬁned in Theorem 8.6.
Proof. Recall that we have to multiply the expression by Gb(Q+iα)Gb(Q+iτ )
(1−q2)ib−1 (α +τ ) under
the pairing. Also since the resulting expression is analytic in α,τ on the lower half
plane, by taking α,τ to 0,−ib we mean the analytic continuation from R to the
corresponding point, while respecting the contour of σ.
The pairing of K0 and K is then given by τ = 0,α = 0. The factor
Gb(−iσ)Gb(−iα +iσ)
Gb(Q +iτ ) Gb(Q +iα)Gb(Q +iτ )
becomes δ(σ) which means we also set σ = 0. Hence we obtain
K0·f (s1,t 1)g(s2,t 2) = f (s1,t 1)g(s2,t 2)e− πb
2 s2, (8.13)
K·f (s1,t 1)g(s2,t 2) = f (s1,t 1)g(s2,t 2)eπbs1. (8.14)
The pairing of E is given by τ =−ib and α = 0, so that again σ = 0 and is
given by
E·f (s1,t 1)g(s2,t 2) = −iq1/2f (s1−ib,t 1)g(s2,t 2)e2πbs1+πbs2e−πbs1− πb
2 s2
1−q2
= −iq1/2f (s1−ib,t 1)g(s2,t 2)eπbs1+ πb
2 s2
1−q2 ,
or simply
E = i
q−q−1e
πb
2 s2eπbs1+2πbps1. (8.15)
Finally the pairing of F is given by τ = 0,α =−ib. By Corollary 3.11 we have
Gb(−iσ)Gb(−iα +iσ)
Gb(Q +iτ ) Gb(Q +iα)Gb(Q +iτ )
= e−πiσ2−πQσGb(iσ−b)Gb(Q +b)
Gb(Q +iσ)
= −q2δ(σ)−q2δ(σ +ib),
82
so that we obtain
F·f (s1,t 1)g(s2,t 2) = iq−1/2 −q2
1−q2eπbs1− πb
2 s2
(
e2πb(t1−s1)f (s1 +ib,t 1 +ib)g(s2,t 2)
+f (s1 +ib,t 1)g(s2,t 2) Gb( Q
2 +is1−it1)Gb( Q
2 +is1 +it1)
Gb( Q
2 +is1−it1−b)Gb( Q
2 +is1 +it1−b)
)
.
Using Gb(ix)
Gb(ix−b) = (1−e2πib(ix−b)), we expand the expression:
F = iq1/2e− πb
2 s2
q−q−1
(
e−πb(s1−2t1)e−2πb(pt1 +ps1 )+
(1 +q−1e−2πb(s1−t1))(1 +q−1e2πb(−s1−t1))e2πbs1e−2πbps1
)
= ie− πb
2 s2
q−q−1
(
e−πb(2ps1 −s1) +e−πb(2ps1 +3s1) + (e2πbt1 +e−2πbt1 +e−2πb(pt1 −t1))e−πb(2ps1 +s1)
)
,
so that under multiplication by e−πit2
1 which changes pt1↦→pt1 +t1, we get
F = ie− πb
2 s2
q−q−1
(
e−πb(2ps1 −s1) +e−πb(2ps1 +3s1) + Ce−πb(2ps1 +s1)
)
, (8.16)
where C depending only on t1 is the operator deﬁned in the previous section.
Therefore under the unitary transformation Φ deﬁned previously , the representation
is equivalent to
K0 = e
πb
2 s2,
K = eπbs1,
E = i
q−q−1e
πb
2 s2eπbs1+2πbps1,
F = ie− πb
2 s2
q−q−1
(
e−πb(2ps1 −s1) +e−πb(2ps1 +3s1) + (e2πbλ +e−2πbλ)e−πb(2ps1 +s1)
)
,
where the measure dµ(λ) is now |Sb(Q + 2iλ)|2dλ.
Motivated from the expression of the corepresentation, we multip ly the space by
Gb( Q
2 +is1−iλ)−1, and in eﬀect changes the action of e2πbps1 to (1+qe−2πbs1+2πbλ)e2πbps1 .
The action of E and F then become:
E = i
q−q−1e
πb
2 s2 (eπbs1+2πbps1 +e−πbs1+2πbλ+2πbps1 ),
F = i
q−q−1e− πb
2 s2 (eπbs1−2πbps1 +e−πbs1−2πbλ−2πbps1 ).
83
Now we make the following changes of variables (unitary transforma tions):
◦s1↦→−s1 : ps1↦→−ps1,
◦eπis1λ : ps1↦→ps1− λ
2, p λ− s1
2,
◦e− πi
2 s1s2 : ps1↦→ps1− s2
4 , p s2↦→ps2− s1
4.
In other words, the transformation:
f (s1,t 1)g(λ,t 2)↦→f (−s1,t 1)g(λ,t 2)e
πi
2 s1(2λ−s2).
Then the representation (denoted by Pλ,t1 ) becomes:
K0 = e
πb
2 s2,
K = e−πbs1,
E = i
q−q−1 (eπb(−2ps1 −s1+λ) +eπb(−2ps1 +s1−λ))
= i
q−q−1 (q1/2eπb(s1−λ) +q−1/2e−πb(s1−λ))e−2πbps1
= [ Q
2b− i
b (s1−λ)]qe−2πbps1,
F = i
q−q−1 (eπb(2ps1 −s1−λ) +eπb(2ps1 +s1+λ))
= i
q−q−1 (q−1/2eπb(s1+λ) +q1/2e−πb(s1+λ))e2πbps1
= [ Q
2b + i
b (s1 +λ)]qe2πbps1.
Remark 8.12. We note that there is a freedom of choice in multiplication by Gb
in the above action. In fact this precisely says that
Pλ,t ≃ P −λ,t (8.17)
f (x) ↦→ Gb( Q
2 +iλ−ix)
Gb( Q
2−iλ−ix)
f (x) (8.18)
as observed in [32].
Since the pairing is non-degenerate, we obtain the following importan t realiza-
tion of the multiplicative unitary W:
84
Corollary 8.13. As a corepresentation on L2(R), W is equivalent to
W =
∫
R
∫ ⊕
R+
T λ,t/2dµ(λ)dt, (8.19)
wheredµ(λ) =|Sb(Q + 2iλ)|2dλ.
This is a generalization of Podle´ s-Woronowicz’s deﬁnition [30] of a multiplicative
unitary for a compact group
u =
∑
α∈ ˆG
⊕
uα, (8.20)
where ˆG is the set of all (ﬁnite dimensional) irreducible unitary representatio n of
G, and
uα :Vα↦→Vα⊗G
is the irreducible corepresentation on some ﬁnite dimensional vecto r space Vα. In
particular, this deﬁnes the multiplicative unitary in a coordinate free canonical way.
Furthermore, by applying the transformations that was done in th e proof of
Theorem 8.11 to the expression (7.61), and comparing the result wit h the expression
of T λ,t/2 given in (7.31), we recover the “6-9 relation” of Gb that is ﬁrst observed
by Volkov [44]. See Section 9 for further details.
