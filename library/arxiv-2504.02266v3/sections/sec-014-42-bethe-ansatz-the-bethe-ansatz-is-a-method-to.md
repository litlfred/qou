---
doc_id: arxiv-2504.02266v3
doc_title: "Knizhnik-Zamolodchikov equations in Deligne categories"
section_id: sec-014-42-bethe-ansatz-the-bethe-ansatz-is-a-method-to
section_title: "Bethe ansatz. The Bethe ansatz is a method to find joint eigenvectors of the Gaudin"
section_number: 4.2
pages: 13-13
source_pdf: 2504.02266v3.pdf
source_sha256: a12193f740b6ee53
toc_source: inferred
---
Hamiltonians 𝐻𝑖= ∑︀
𝑗̸=𝑖
Ω𝑖𝑗
𝑧𝑖−𝑧𝑗which appear on the right-hand side of the KZ equations.
One obtains such eigenvectors from the integral representations of solutions to KZ equa-
tions by taking the limit ℏ→0 and using the steepest descend method, see [22].
More precisely, for any non-degenerate critical point of the function
exp
(︃
ℏ
𝑚
∑︁
𝑖=1
(𝑧𝑐(𝑖) −𝑧𝑐(𝑖)+1)𝑡𝑖
)︃
Φ−ℏ
(4.19)
the value of the differential form 𝜔from (4.10) at this point is a joint eigenvector, see
[22]. Such eigenvectors are called the Bethe vectors.
The critical set of this function has not been analyzed yet. It not clear if the critical
points of this function are non-degenerate and if their number is big enough so that the
corresponding Bethe vectors diagonalize the Gaudin Hamiltonians.
Nevertheless, we may still prove that the joint spectrum of the Gaudin Hamiltonians
is simple.
Proposition 4.6. The common spectrum of the Gaudin hamiltonians 𝐻𝑖on
HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚)
(4.20)
is simple for generic 𝑡, 𝑧𝑖.
Proof. The simplicity of the spectrum is a Zariski open condition on parameters 𝑡, 𝑧𝑖, so
it is sufficient for us to prove it for a special 𝑡and generic 𝑧𝑖. The latter can be proved
by taking a sufficiently large integer 𝑡. In this case we have isomorphisms (3.6), (3.8)
and (3.27), so the space (4.20) can be identified with the space Sing(Λ∙(𝑉⊗𝑊)𝛾,𝛽) of all
gl(𝑉)-singular vectors of gl(𝑉) ⊕gl(𝑊) weight space (𝛾, 𝛽) in Λ∙(𝑉⊗𝑊). However, it
follows from [21] that for generic 𝑧𝑖Gaudin hamiltonians 𝐻𝑖separate the Bethe vectors
basis in Sing(Λ∙(𝑉⊗𝑊)𝛾,𝛽), thus we have the proposition.
□
Remark 4.7. It follows from this proposition that the Gaudin hamiltonians 𝐻𝑖generically
(i.e. for generic 𝑧𝑖, 𝑡) generate the image of the Bethe algebra from [16] in the space
End(HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚)).
(4.21)
