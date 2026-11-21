---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond"
section_id: sec-004-212-proof-of-part-a-of-theorem-discrete-dantzig
section_title: "Proof of part (a) of Theorem ??: Discrete Dantzig descent."
section_number: 2.1.2
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
αic⊺gi ≥−∆0
X
αi ≥−(2n −2)∆0αmax,
where this time ∆0 > 0 denotes the greatest value of −c⊺z over all z ∈G(A) for which xk +z is still
feasible and where αmax = max{αi }. Rewriting this, we get
∆0 ≥c⊺(xk −xmin)
(2n −2)αmax
.
Now let αz be the discrete Dantzig-descent augmentation applied to xk, leading to xk+1 := xk +αz.
Then we get
c⊺(xk −xk+1) = −αc⊺z = α∆0 ≥∆0 ≥c⊺(xk −xmin)
(2n −2)αmax
≥c⊺(x0 −xmin)
(2n −2)γ
,
where γ is the maximum entry in any feasible integer solution (or, equivalently, in any vertex of PI).
Thus, we have a factor of β = 1/((2n −2)γ) of objective-function decrease at each augmentation
leading to the desired polynomial number of augmentations via Lemma 3 taking ǫ = 1. In this case
we get the number of augmentations bounded by (4n −4)γ log(c⊺(x0 −xmin)))
