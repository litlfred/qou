---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond"
section_id: sec-007-221-proof-of-lemma-for-discrete-deepest-descent
section_title: "Proof of Lemma ?? for Discrete deepest descent."
section_number: 2.2.1
pages: 11-12
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
toc_source: outline
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond — 13 sections: Front matter; Introduction.; Our Contributions"
---
We observe that
0 > c⊺(xmin −xk) = c⊺X
αigi =
X
αic⊺gi ≥−n∆
where ∆> 0 is the largest value of −αc⊺z over all z ∈C(A) and α > 0 for which xk +αz is feasible.
Rewriting this, we get
∆≥c⊺(xk −xmin)
n
.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
12
Now let αz be the discrete deepest-descent augmentation applied to xk, leading to xk+1 := xk +αz.
Then we get ∆= −αc⊺z and
c⊺(xk −xk+1) = −αc⊺z = ∆≥c⊺(xk −xmin)
n
.
Thus, we have a factor of β = 1/n of objective-function value decrease at each augmentation. Apply-
ing Lemma 3 with ǫ = 1/δ then yields a solution ¯x with |c⊺(¯x−xmin)| < 1/δ within 2n log(δ c⊺(x0 −
xmin))) many augmentations. Due to the deﬁnition of δ as the least common multiple of all subde-
terminants of A, any vertex with an objective value of at most c⊺¯x must be optimal. As explained
right before the statement of Theorem 1, such a vertex can be found from ¯x in at most n additional
augmentations. Finally, note that once the discrete deepest-descent augmentation makes progress
in objective value less than ǫ/(2n −2), we have
|c⊺(xk −xmin)| =
X
|αic⊺gi| < (2n −2) · ǫ/(2n −2) = ǫ.
Hence, we can decide eﬀectively when we should stop making discrete deepest-descent augmenta-
tions and should rather ﬁnd a nearby vertex.
