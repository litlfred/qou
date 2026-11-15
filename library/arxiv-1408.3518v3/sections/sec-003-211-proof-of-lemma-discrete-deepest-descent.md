---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond"
section_id: sec-003-211-proof-of-lemma-discrete-deepest-descent
section_title: "Proof of Lemma ??: Discrete deepest descent."
section_number: 2.1.1
pages: 9-9
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
toc_source: outline
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond — 13 sections: Front matter; Introduction.; Our Contributions"
---
We observe that
0 > c⊺(xmin −xk) = c⊺X
αigi =
X
αic⊺gi ≥−(2n −2)∆
where ∆> 0 is the largest value of −αc⊺z over all z ∈G(A) and integer α > 0 for which xk + αz is
feasible. Rewriting this, we get
∆≥c⊺(xk −xmin)
2n −2
.
Now let αz be the discrete deepest-descent augmentation applied to xk, leading to xk+1 := xk +αz.
Then we get ∆= −αc⊺z and
c⊺(xk −xk+1) = −αc⊺z = ∆≥c⊺(xk −xmin)
2n −2
.
Thus, we have a factor of β = 1/(2n −2) of objective-function decrease at each augmentation,
leading to the desired polynomial number of augmentations via Lemma 3 taking ǫ = 1. In this case,
we get the number of augmentations bounded by (4n −4) log(c⊺(x0 −xmin))).
