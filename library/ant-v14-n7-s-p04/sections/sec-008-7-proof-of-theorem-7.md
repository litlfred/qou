---
doc_id: ant-v14-n7-s-p04
doc_title: "Elliptic curves over totally real cubic ﬁelds are modular"
section_id: sec-008-7-proof-of-theorem-7
section_title: "Proof of Theorem 7"
section_number: 7
pages: 8-9
source_pdf: ant-v14-n7-s-p04.pdf
source_sha256: 6abd838a4c933311
doc_brief: "Elliptic curves over totally real cubic fields are modular — 10 sections: Introduction; Images mod 3, 5, 7 and modularity; Modular curves"
---
In this section we prove Theorem 7 thereby completing the proof of Theorem 2. Recall X= X(b5, ns7).
Write X(3) for the third symmetric power of X. We shall prove the following result which immediately
implies Theorem 7.
Proposition 7.1. X(3)(Q)={ c0, c∞}.
Proof. Let x∈ X(3)(Q). By Lemma 6.3 we have (1−w5)[x− c∞]= 𝓁·[ c0− c∞] for some𝓁∈ Z/7Z.
Asw5(c∞)= c0 we may rewrite this as
(x−w5(x))∼ k·(c0− c∞)
for some k∈{− 3,..., 3}. We write xF3, c0,F3, c∞,F3∈ X(3)(F3) for the reductions of x, c0, c∞ modulo 3
respectively. It follows that
(y−w5(y))∼ k·(c0,F3− c∞,F3) (3)
where y= xF3. Using our model D we enumerated X(3)(F3); this has precisely 40 elements. For each
y∈ X(3)(F3) and for each k=− 3,..., 3 we tested the relation (3) and found that it holds only fory= c0,F3
and k= 1 and for y= c∞,F3 and k=− 1. We therefore deduce that xF3= c0,F3 or c∞,F3. We would like to
conclude that x= c0 or c∞. As w5 swaps c0 and c∞ and also their mod 3 reductions, we may suppose
that xF3= c∞. Letµ: X(3)→ J be given by z↦→[ z− c∞] and t: J→ A be simply t=w5− 1. Since
xF3= c∞,F3, the point (t◦µ)(x)∈ A(Q) belongs to the kernel of reduction A(Q)→ A(F3). However
as A(Q) is torsion, this kernel of reduction is trivial [Katz 1981, Appendix]. Thus (t◦µ)(x)= 0. To
conclude that x= c∞ it is now enough to check that t◦µ is a formal immersion at c∞,F3, and for this we
shall use the formal immersion criterion due to Derickx, Kamienny, Stein and Stoll [Derickx et al. 2017,
Proposition 3.7].
WriteX∼=J for the 6-dimensional space of 1-forms on X/F3. We would like to write down the
4-dimensional subspace t∗(A). We easily do this since it is precisely that−1-eigenspace ofw∗
5 acting
onX, and we know the action of w5 on our model D from which can write down the corresponding
action on the 1-forms. Let ω1,...,ω 4 be an F3-basis for t∗(A). To check the formal immersion
criterion of Derickx et al. at c∞,F3 we need to check that a certain 4× 3 matrix deﬁned in [Derickx
et al. 2017, Proposition 3.7], which we denote by M, has rank 3. As 3 is inert in Q(ζ7)+, we have
c∞,F3= P1+ P2+ P3, where Pi∈ X(F27) are distinct. This slightly simpliﬁes the description of the
matrix M. Let u j∈ F27(X) be a uniformizing element for Pj. Thenωi/du j is a regular function at Pj
and we may evaluate(ωi/du j)(Pj)∈ F27. That matrix is simply
M=((ωi/du j)(Pj))i=1,2,3,4; j=1,2,3.
We computed M and checked that it has rank 3 as required. This completes the proof. □
Elliptic curves over totally real cubic ﬁelds are modular 1799
