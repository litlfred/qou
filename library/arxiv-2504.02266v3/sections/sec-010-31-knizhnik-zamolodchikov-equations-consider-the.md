---
doc_id: arxiv-2504.02266v3
doc_title: "Knizhnik-Zamolodchikov equations in Deligne categories"
section_id: sec-010-31-knizhnik-zamolodchikov-equations-consider-the
section_title: "Knizhnik-Zamolodchikov equations. Consider the category Rep(𝐺𝐿𝑡) for a com-"
section_number: 3.1
pages: 5-6
source_pdf: 2504.02266v3.pdf
source_sha256: a12193f740b6ee53
toc_source: inferred
---
plex 𝑡. For integer 𝑚, 𝑛≥0 we may consider the Casimir operators
Ω𝑖𝑗: 𝑉*⊗𝑛⊗𝑉⊗𝑚→𝑉*⊗𝑛⊗𝑉⊗𝑚,
Ω𝑖𝑗= Ω𝑗𝑖
(3.1)
which act in 𝑖, 𝑗tensor components via a flip if 𝑖, 𝑗≤𝑛or 𝑖, 𝑗> 𝑛, and via −coev ∘ev
for other 𝑖, 𝑗. Here, ev: 𝑉⊗𝑉* →1 and coev: 1 →𝑉⊗𝑉* are the evaluation and
coevaluation maps.
We define the Knizhnik-Zamolodchikov connection on the base space
{(𝑧1, . . . , 𝑧𝑛+𝑚) ∈C𝑛+𝑚|𝑧𝑖̸ = 𝑧𝑗for 𝑖̸ = 𝑗}
(3.2)
with values in HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚)
∇𝐾𝑍(ℏ) = 𝑑−ℏ
∑︁
𝑖<𝑗
𝑑𝑧𝑖−𝑑𝑧𝑗
𝑧𝑖−𝑧𝑗
Ω𝑖𝑗,
(3.3)
where ℏ∈C and the action of Ω𝑖𝑗on 𝑉*⊗𝑛⊗𝑉⊗𝑚is extended to endomorphisms of
HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚). We may assume |𝜆| + 𝑛= |𝜇| + 𝑚, otherwise
HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚) = 0.
(3.4)
6
P. Etingof ⋆, I. Motorin*, A. Varchenko♢, and I. Zhu†
Example 3.1 ([15]). In the case when 𝜆, 𝜇= 0 and 𝑚= 𝑛we can describe Ω𝑖𝑗explicitly:
note that HomRep(𝐺𝐿𝑡)(1, 𝑉*⊗𝑚⊗𝑉⊗𝑚) = C[𝑆𝑚], so for 1 ≤𝑖< 𝑗≤2𝑚and 𝜎∈𝑆𝑚we
have
Ω𝑖𝑗𝜎=
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎩
(𝑖, 𝑗) ∘𝜎,
𝑖, 𝑗≤𝑚
𝜎∘(𝑖−𝑚, 𝑗−𝑚),
𝑖, 𝑗> 𝑚
−𝑡𝜎,
𝜎(𝑗−𝑚) = 𝑖, 𝑖≤𝑚< 𝑗
−(𝑖, 𝜎(𝑗−𝑚)) ∘𝜎,
𝜎(𝑗−𝑚)̸ = 𝑖, 𝑖≤𝑚< 𝑗
(3.5)
Since the vector space of homomorphisms HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚) has the same
dimension for all non-integer and all large enough integer 𝑡= dim 𝑉, it is sufficient for us
to consider the setup for gl𝑡, 𝑡∈N - for large 𝑡we have an isomorphism
𝐹: HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚)
∼−→Homgl𝑡(𝑉𝜆,𝜇, 𝑉*⊗𝑛⊗𝑉⊗𝑚).
(3.6)
Here 𝑉𝜆,𝜇is the irreducible gl𝑡representation of highest weight
(𝜆1, 𝜆2, . . . , 0, . . . , 0, . . . , −𝜇2, −𝜇1),
(3.7)
where the first coordinates are the coordinates of 𝜆, the last coordinates are the coordi-
nates of −𝜇, and the coordinates in between are all zeros.
For large positive integer 𝑡we also have
Homgl𝑡(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚) ∼= Homgl𝑡(𝑉𝜆,𝜇⊗(Λ𝑡𝑉)⊗𝑛, (Λ𝑡−1𝑉)⊗𝑛⊗𝑉⊗𝑚).
(3.8)
