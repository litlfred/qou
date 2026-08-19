---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-036-105-dimension-counts
section_title: "Dimension counts"
section_number: 10.5
pages: 67-68
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Now let us compare the dimensions of the moduli spaces related by Ψ W.
First we consider M(C,GL (K); m). This space can be represented as the space of
GL(K, C) matrices A1,...,A gC, B1,...,B gC, C1,...,C s, subject to some relations: ﬁrst,
the eigenvalues of the Cn are ﬁxed; second, we impose
∏
i
[Ai,Bi]
∏
n
Cn = 1; (10.21)
third, we divide out by overall conjugation. The condition on the eigenvalues of the Cn
eliminatesKs degrees of freedom. The equation (10.21) imposes only K2− 1 independent
conditions: if ∏
n detCn ⁄= 1 there are no solutions, but if ∏
n detCn = 1, while there
are solutions, the determinant equation is redundant. Similarly, the center of the gauge
group acts trivially, so the quotient by the gauge group reduces the dimension by K2− 1.
Altogether we get
dimCM(C,GL (K); m) = (2gC +s)K2−Ks− 2(K2− 1). (10.22)
31Here and below, we use the freedom to ﬁx a gauge so that we consider only variations δα which vanish
near the punctures. This makes the integral (10.18) convergent, despite the fact that the connections we
consider are singular.
– 65 –
On the other hand, using the Riemann-Hurwitz relation
dimCM(Σ,GL (1); m) = 2gΣ =K(2gC− 2) +B + 2, (10.23)
where B is the branching number (which is simply the number of branch points, since we
assume all branch points are simple.) It follows that
dimCM(C,GL (K); m)− dimCM(Σ,GL (1); m) = (K2−K)(2gC +s− 2)−B. (10.24)
Since ΨW is symplectic it is in particular locally injective, so the quantity in (10.24) must be
nonnegative. We thus get a topological restriction on the branching number of a branched
cover Σ→C of degree K admitting a spectral network:
B≤ (K2−K)(2gC +s− 2). (10.25)
If this bound is saturated, ΨW is a local symplectomorphism. Note that this does happen
for the spectral curves (2.1), to which the spectral networks Wϑ are subordinate.
Equation (10.25) is a purely topological statement. It says that there cannot be too
many branch points in a spectral network. It would be interesting to give a more direct
topological proof of this assertion.
In the case where (10.25) is saturated and ΨW is a covering map, we have constructed
not only a local isomorphism between M(C) and M(Σ), but also a local identiﬁcation
between (π∗L,π∗∇ab) and ( ˆE,∇). We can use this to tie up a loose end from §6.5. Letting
(L,∇) vary we get a universal bundle π∗(L) over M(Σ)×C. Restricting this to some
point ˜z∈ ˜C gives a line bundle over M(Σ), which we call π∗(L)˜z. Similarly we have a
universal bundle ˆE˜z overC.32 Now let A(Σ) be the algebra of global rational sections of
End(π∗(L)˜z) (i.e. the algebra of sections over the generic point), and similarly A(C) the
algebra of global rational sections of End( ˆE˜z). A(Σ) is a central simple algebra of degree
K overR(M(Σ)), the ﬁeld of rational functions on M(Σ), and similarly A(C) is a central
simple algebra of degree K overR(M(C)). Our nonabelianization construction gives an
embedding ofA(C) inA(Σ) and a compatible embedding ofR(M(C)) inR(M(Σ)). Now,
we have just shown that this embedding realizes M(Σ) as a cover ofM(C). It follows
thatR(M(Σ)) is a ﬁnite extension ofR(M(C)) (since it is an extension and the two have
the same dimension, hence the same transcendence degree over C, and are both ﬁnitely
generated). Thus the group Aut(R(M(Σ)) :R(M(C))) is ﬁnite. But now it follows by
dimension counting that Aut(A(Σ) :A(C)) is also ﬁnite.
