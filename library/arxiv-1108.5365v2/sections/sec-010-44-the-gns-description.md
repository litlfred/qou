---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-010-44-the-gns-description
section_title: "The GNS description"
section_number: 4.4
pages: 28-31
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
The GNS representation enables us to bring the quantum plane into t he Hilbert
space level, where the algebra is realized as operators on certain Hilb ert space.
This Hilbert space is nothing but the space of “ L2 functions on the quantum
plane”, which gives the necessary background later to describe th e L2 functions
on GL+
q (2, R) using the quantum double construction. This will allow us to state
the main theorem (Theorem 8.15) on the decomposition of L2(GL+
q (2, R)) into the
fundamental principal series representations of Uq~q(gl(2, R)) with certain Plancherel
measure.
Now equipped with the left invariant Haar functional h, we can describe com-
pletely the GNS representation of A using h as the weight.
Theorem 4.9. LetH =L2(R× R) be the completion of L2(R)⊗W equipped with
the inner product
⟨f,g⟩ =
∫
R
∫
R
g(s,t + iQ
2 )f (s,t + iQ
2 )dsdt, (4.28)
and the L2 norm
‖f‖2 =
∫∫
|f (s,t + iQ
2 )|2dsdt. (4.29)
28
Then the GNS map is simply given by
Λ
( ∫
R+i0
∫
R
f (s,t )Aib−1sBib−1tdsdt
)
=f (s,t ). (4.30)
In particular, the Haar functional is a faithful weight.
The action π is given by the multiplication of A on itself:
π(a)Λ(b) := Λ( ab), a,b ∈A. (4.31)
First of all, let us note that A is closed under *:
Proposition 4.10. The conjugation map T is given by
T (f ) = f (−s,−t)e2πist, (4.32)
where we denote by f (z) := f (z).
We observe that f (−s,−t)e2πist still satisﬁes all the analytic properties required
to be an element of A: it is entire analytic in s, meromorphic in t with possible
poles at t =−inb−imb−1, etc. see Deﬁnition 4.2.
Proof.
( ∫
R+i0
∫
R
f (s,t )Aib−1sBib−1tdsdt
) ∗
=
∫
R+i0
∫
R
f (s,t )B−ib−1tA−ib−1sdsdt
=
∫
R−i0
∫
R
f (s,t)B−ib−1tA−ib−1sdsdt
=
∫
R−i0
∫
R
f (s,t)e2πistA−ib−1sB−ib−1tdsdt
=
∫
R+i0
∫
R
f (−s,−t)e2πistAib−1sBib−1tdsdt
=
∫
R+i0
∫
R
f (−s,−t)e2πistAib−1sBib−1tdsdt.
Next we describe the product in terms of f (s,t ):
Proposition 4.11. The product of two elements in A is given by:
(f·g)(s,t ) =
∫
C
∫
R
f (s−s′,t−t′)g(s′,t ′)e2πis′(t−t′)ds′dt′ (4.33)
i.e. a twisted convolution. Here C is the contour that, with possible poles, goes
belowt′ =t and above t′ = 0.
29
Proof.
( ∫
R+i0
∫
R
f (s,t )Aib−1sBib−1tdsdt
)( ∫
R+i0
∫
R
g(s′,t ′)Aib−1s′
Bib−1t′
ds′dt′
)
=
∫
R+i0
∫
R
∫
R+i0
∫
R
f (s,t )g(s′,t ′)e2πis′tAib−1(s+s′)Bib−1(t+t′)ds′dt′dsdt
=
∫
R+i0
∫
R
( ∫
C
∫
R
f (s−s′,t−t′)g(s′,t ′)e2πis′(t−t′)ds′dt′
)
Aib−1sBib−1tdsdt,
where in the last step, the shift in t will push the contour of t′ to go below t′ =t.
Proof of Theorem 4.9. Using the formula for the Haar functional, and the deﬁnition
of the GNS inner product, we have
⟨f,g⟩ = h(g∗f )
= h(g(−s,−t)e2πist·f (s,t ))
= h
( ∫
R+i0
∫
R
g(s′−s,t ′−t)e2πi(s−s′)(t−t′)f (s′,t ′)e2πis′(t−t′)ds′dt′
)
= h
( ∫
R+i0
∫
R
g(s′−s,t ′−t)f (s′,t ′)e2πis(t−t′)ds′dt′
)
=
∫
R+i0
∫
R
g(s′,t ′−iQ)f (s′,t ′)ds′dt′
=
∫
R
∫
R
g(s′,t ′− iQ
2 )f (s′,t ′ + iQ
2 )ds′dt′
=
∫
R
∫
R
g(s′,t ′ + iQ
2 )f (s′,t ′ + iQ
2 )ds′dt′,
where in the second to last line, we do a shift in the contour of t by iQ
2 by holo-
morphicity.
Finally we read oﬀ the representation π ofA on the functions f (s,t )∈H :
Proposition 4.12. The representation π :A֒B (H) is given by
π(A) = e−2πbps, π (B) = e2πbse−2πbpt, (4.34)
whereps = 1
2πi
∂
∂s , so that e2πbps·f (s) = f (s−ib). Similarly for pt.
Proof. A acts on f (s,t ) by:
Aib−1s′
∫∫
f (s,t )Aib−1sBib−1tdsdt
=
∫∫
f (s,t )Aib−1(s+s′)Bib−1tdsdt
=
∫∫
f (s−s′,t )Aib−1sBib−1tdsdt.
30
Hence Aib−1s′
·f (s,t ) = f (s−s′,t ), or A =e−2πbps.
Similarly,
Bib−1t′
∫∫
f (s,t )Aib−1sBib−1tdsdt
=
∫∫
f (s,t )e2πist′
Aib−1sBib−1(t+t′)dsdt
=
∫∫
f (s,t−t′)e2πist′
Aib−1sBib−1tdsdt.
Hence Bib−1t′
·f (s,t ) = e2πist′
f (s,t−t′), or B =e2πbse−2πbpt.
We will take this Hilbert space H as our canonical choice, when we introduce
right measure and the dual space.
