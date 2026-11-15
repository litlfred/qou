---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-016-erdős-138-differences-variant
section_title: "Erdős #138, Differences Variant"
section_number: null
pages: 35-35
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Question. Let the van der Waerden number 𝑊(𝑘) be such that whenever 𝑁≥𝑊(𝑘) and
{1, . . . , 𝑁} is 2-coloured there must exist a monochromatic 𝑘-term arithmetic progression. Is
it true that 𝑊(𝑘+ 1) −𝑊(𝑘) →∞?
Proof. We will show that 𝑊(𝑘+ 1) ≥𝑊(𝑘) + 𝑘, which establishes that 𝑊(𝑘+ 1) −𝑊(𝑘) →∞.
Given a 2-coloring of the first 𝑊(𝑘) −1 integers without a monochromatic 𝑘-AP, we can
extend it by 𝑘further elements without creating a monochromatic (𝑘+ 1)-AP by proceeding
greedily. Adding new elements one by one, suppose we have validly colored up to 𝑀(where
𝑀< 𝑊(𝑘) −1 + 𝑘); we simply color 𝑀+ 1 red if doing so doesn’t create a red (𝑘+ 1)-AP, and
blue otherwise.
The only way this algorithm could result in an invalid coloring is if both choices are
blocked, meaning there is already a red 𝑘-AP with some step size 𝑑𝑅and a blue 𝑘-AP with
some step size 𝑑𝐵such that the (𝑘+1)-th element for both progressions lands exactly on 𝑀+1.
But this is impossible. Because our original interval up to 𝑊(𝑘) −1 has no monochromatic
𝑘-APs, these progressions must contain at least one newly added element, which bounds their
step sizes to 𝑑𝑅, 𝑑𝐵≤𝑘−1. Hence, if we step backward 𝑑𝐵times along the red progression
and 𝑑𝑅times along the blue progression, both calculations land exactly on the positive integer
𝑀+ 1 −𝑑𝑅𝑑𝐵, meaning this single point would have to be simultaneously colored red and
blue, which is a contradiction.
□
We originally communicated the result in https://www.erdosproblems.com/foru
m/thread/138#post-5314, and share the Lean proof at https://github.com/googl
e-deepmind/alphaproof-nexus-results/blob/main/APNOutputs/ErdosProbl
ems/erdos_138.variants.difference.lean. In the discussion at the ErdosProblems
site, Thomas Bloom pointed out that the obvious generalization of this argument gives
𝑊(𝑘+ 1, 𝑙+ 1) ≥𝑊(𝑘, 𝑙) + min(𝑘, 𝑙), and asked what this kind of argument can prove for the
𝑟-color variant 𝑊𝑟(𝑘).
