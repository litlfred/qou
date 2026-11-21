---
doc_id: arxiv-1208.2521v1
doc_title: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS"
section_id: page-009
section_title: "Page 9"
section_number: null
pages: 9-9
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
toc_source: undetermined
doc_brief: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS
9
(diﬀerent from Rahman’s proposal in [13, (1.13)]) and with the replacement of
f(qk), g(qn) by qkf(qk), qng(qn) this becomes
(3.4)











g(qn) =
∞
X
k=−∞
q2k Jα(qk+n; q2) f(qk),
f(qk) =
∞
X
n=−∞
q2n Jα(qk+n; q2) g(qn).
Now observe that
Jα((1 −q)z; q2) = (1 + q)−α zα
Γq2(α + 1)
1φ1(0; q2α+2; q2, (1 −q2)2 (qz/(1 + q))2)
converges, for q ↑1, to the Bessel function
Jα(z) =
2−α zα
Γ(α + 1) 0F1(−; α + 1; −z2/4),
where we used Proposition A.2 and the fact that
(1 −q2)α (q2α+2; q2)∞
(q2; q2)∞
=
1
Γq2(α + 1) −→
1
Γ(α + 1)
as q ↑1, cf. Andrews [1, Appendix A], Koornwinder [11, Appendix B]. We can
apply this to (3.4) when we let q ↑1 under the side condition that log(1−q)
log q
∈2Z.
For such q we can replace qk, qn in (3.4) by (1 −q)1/2qk, (1 −q)1/2qn, and next
f((1 −q)1/2qk), g((1 −q)1/2qn) by f(qk), g(qn). With the q-integral notation
Z ∞
0
h(z) dqz := (1 −q)
∞
X
j=−∞
h(qj) qj,
(3.4) then takes the form







g(λ) =
Z ∞
0
f(x) Jα((1 −q)λx; q2) x dqx,
f(x) =
Z ∞
0
g(λ) Jα((1 −q)λx; q2) λ dqλ,
where λ in the ﬁrst identity and x in the second identity take the values qn, n ∈Z.
For q ↑1 we obtain, at least formally, the Hankel transform pair







g(λ) =
Z ∞
0
f(x) Jα(λx) x dx,
f(x) =
Z ∞
0
g(λ) Jα(λx) λ dλ,
