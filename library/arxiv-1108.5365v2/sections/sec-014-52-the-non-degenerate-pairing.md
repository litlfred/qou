---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-014-52-the-non-degenerate-pairing
section_title: "The non-degenerate pairing"
section_number: 5.2
pages: 41-44
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
Recall that a Hopf pairing between two Hopf algebras A andA∗ is a non-degenerate
pairing such that
⟨a,xy⟩ =⟨∆( a),x⊗y⟩, ⟨ab,x⟩ =⟨a⊗b, ∆( x)⟩. (5.19)
for a,b∈A,x,y ∈A ∗. (In this paper we will not consider counit and antipode in
the pairing.)
In the current setting, we have the pairing between Aq andA∗
q from the compact
case:
⟨A,X⟩ =q−2, ⟨B,X⟩ = 0,
⟨A,Y⟩ = 0, ⟨B,Y⟩ =c∈ C,
where c is any complex number.
The pairings between A,B and ˆA =X −1, ˆB =q−1YX −1 are given by
⟨A, ˆA⟩ =q2, ⟨B, ˆA⟩ = 0,
⟨A, ˆB⟩ = 0, ⟨B, ˆB⟩ =cq :=c′.
We will choose c′ = 1. From this it is extended to
⟨BmAn, ˆA⟩ =q2nδm0, ⟨BmAn, ˆB⟩ =δm1,
and then to
⟨BmAn, ˆBm′
ˆAn′
⟩ =q2n′(n+m)[m]q!δmm′,
where [m]q! := [ m]q[m− 1]q...[1]q is the q-factorial, and [ m]q = qm−q−m
q−q−1 is the
q-number.
From the analogy between the quantum dilogarithm Gb and the Γ q function
established in [14], we prove the following theorem:
Theorem 5.7. The Hopf pairing between A andA∗≃ ˆAcop is given by
⟨
∫∫
g(s,t )Bib−1tAib−1sdsdt,
∫∫
ˆf (s,t ) ˆBib−1t ˆAib−1sdsdt⟩
=
∫∫∫
g(s,t ) ˆf (s′,t )Gb(Q +it)e−2πis′(s+t)ds′dsdt (5.20)
⟨
∫∫
g(s,t )Aib−1sBib−1tdsdt,
∫∫
ˆf (s,t ) ˆBib−1t ˆAib−1sdsdt⟩
=
∫∫∫
g(s,t ) ˆf (s′,t )Gb(Q +it)e−2πis′(s+t)e−2πistds′dsdt, (5.21)
41
or using the Mellin transformed picture (see Remark 4.3):
⟨
∫
f (t)Bib−1tg(logA)dt,
∫∫
ˆf (s,t ) ˆBib−1t ˆAib−1sdsdt⟩
=
∫∫
g(−2πbs′) ˆf (s′,t )f (t)Gb(Q +it)e−2πits′
ds′dt (5.22)
⟨
∫
g(logA)f (t)Bib−1tdt,
∫∫
ˆf (s,t ) ˆBib−1t ˆAib−1sdsdt⟩
=
∫∫
g(−2πb(s′ +t)) ˆf (s′,t )f (t)Gb(Q +it)e−2πits′
ds′dt. (5.23)
Here the Hopf pairing between two C∗-algebra are deﬁned by naturally extending the
pairing in the deﬁning relations (5.19) to a pairing between the multiplier algebras
M (A⊗A ) and M (A∗⊗A ∗).
Proof. It suﬃces to show that
⟨f, ˆgˆh⟩ =⟨∆( f ), ˆg⊗ ˆh⟩. (5.24)
The other relations are similar by duality. We will prove the ﬁrst form ( 5.21). For
simplicity we omit all the integrations after the pairing. Every variable is to be
integrated.
LHS = ⟨f (s,t ),
∫∫
ˆg(s−s′,t−t′)ˆh(s′,t ′)e2πi(s−s′)t′
ds′dt′⟩
= f (s,t )ˆg(s′′−s′,t−t′)ˆh(s′,t ′)e2πi(s′′−s′)t′
Gb(Q +it)e−2πis′′(s+t)e−2πist
= f (s,t )ˆg(s′′−s′,t−t′)ˆh(s′,t ′)Gb(Q +it)e2πi(s′′−s′)t′
e−2πis′′(s+t)e−2πist,
RHS = ⟨f (s1,t 1 +t2)Gb(−it1)Gb(−it2)
Gb(−it1−it2)) δ(s2,s 1 +t1), ˆg(s1,t 1)ˆh(s2,t 2)⟩
= f (s1,t 1 +t2)Gb(−it1)Gb(−it2)
Gb(−it1−it2) Gb(Q +it1)Gb(Q +it2)δ(s2,s 1 +t1)
ˆg(s′
1,t 1)ˆh(s′
2,t 2)e−2πis′
1(s1+t1)e−2πis′
2(s2+t2)e−2πis1t1e−2πis2t2
= f (s1,t 1 +t2)ˆg(s′
1,t 1)ˆh(s′
2,t 2)Gb(Q +it1 +it2)e−2πis′
2t2e−2πis1(t1+t2)e−2πi(s1+t1)(s′
1+s′
2),
where we used the reﬂection properties (3.10) of the Gb function:
Gb(−is)Gb(−it)
Gb(−is−it) = Gb(Q +is +it)e2πist
Gb(Q +is)Gb(Q +it). (5.25)
Now shifting t1↦→t1−t2,s ′
1↦→s′
1−s′
2, we obtain
= f (s1,t 1)ˆg(s′
1−s′
2,t 1−t2)ˆh(s′
2,t 2)Gb(Q +it1)e−2πis′
2t2e−2πis1t1e−2πis′
1(s1+t1−t2)
= f (s1,t 1)ˆg(s′
1−s′
2,t 1−t2)ˆh(s′
2,t 2)Gb(Q +it1)e2πi(s′
1−s′
2)t2e−2πis′
1(s1+t1)e−2πis1t1.
42
Hence we see that the expression is equal on renaming s1 =s,t 1 =t,s ′
1 =s′′,s ′
2 =s′
and t2 =t′.
With the pairing established, we can prove the density condition need ed in order
forA to be a locally compact quantum group.
Theorem 5.8. We have
A = span{(ω⊗ 1)∆( a)|ω∈A ∗,a∈A} closure (5.26)
= span{(1⊗ω)∆( a)|ω∈A ∗,a∈A} closure. (5.27)
Proof. We will prove that (ω⊗ 1)∆( a) is dense in 1 ⊗A , while the other statement
is similar. Let us write
ω =
∫∫
ˆf (s,t ) ˆBib−1t ˆAib−1sdsdt∈A ∗
a =
∫∫
g(s,t )Aib−1sBib−1tdsdt∈A.
Using Proposition 4.4, the required pairing is (here we understood th at it is an
element in 1⊗A with coordinatess2,t 2, and that all integrations converge absolutely
with the appropriate contours):
⟨g(s1,t 1 +t2)Gb(−it1)Gb(−it2)
Gb(−i(t1 +t2)) δ(s2,s 1 +t1), ˆf (s,t )⟩
=
∫∫∫
ˆf (s′,t 1)g(s1,t 1 +t2)Gb(−it1)Gb(−it2)
Gb(−i(t1 +t2)) Gb(Q +it1)δ(s2,s 1 +t1)e−2πis′(s1+t1)ds′ds1dt1
=
∫∫
ˆf (s′,t 1)g(s2−t1,t 1 +t2) Gb(−it2)
Gb(−i(t1 +t2))e−2πis′s2eπit2
1−πt1Qds′dt1.
Now if we choose ˆf (s′,t 1) = ˆf1(s′) ˆf2(t1), the integration over s′ is just the Fourier
transform ˆF1(s2) of ˆf1(s′), and we get
=
∫
ˆF1(s2) ˆf2(t1)g(s2−t1,t 1 +t2) Gb(−it2)Gb(−i(t1 +t2))eπit2
1−πt1Qdt1.
Finally we can choose any nice approximation of identity for ˆf2(t1)−→δ(t1), then
in the limit we obtain simply
−→ ˆF1(s2)g(s2,t 2),
which is then obviously all of 1 ⊗A for diﬀerent choices of ˆF and g.Corollary 5.9. A is a locally compact quantum group in the sense of [24, 25].
43
