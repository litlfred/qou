---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-017-erdős-741-i
section_title: "Erdős #741-(i)"
section_number: null
pages: 35-37
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Question. Let 𝐴⊆ℕbe such that 𝐴+ 𝐴has positive upper density. Can one always decompose
𝐴= 𝐴1 ⊔𝐴2 such that 𝐴1 + 𝐴1 and 𝐴2 + 𝐴2 both have positive upper density?
Proof. We show that the answer is yes. We use an alternating block partition. Given a rapidly
35
Advancing Mathematics Research with AI-Driven Formal Proof Search
growing sequence 𝑀0 < 𝑀1 < 𝑀2 < · · · , we define
𝐴1 = 𝐴∩
Ø
𝑘
(𝑀2𝑘, 𝑀2𝑘+1],
𝐴2 = 𝐴\ 𝐴1.
In odd-indexed intervals (𝑀2𝑘, 𝑀2𝑘+1], all elements of 𝐴belong to 𝐴1; in even-indexed inter-
vals (𝑀2𝑘+1, 𝑀2𝑘+2], they all belong to 𝐴2. The sequence 𝑀is chosen to grow fast enough
that each block dwarfs all previous ones. We split into two cases.
Case 1: 𝐴has positive upper density. There exist a constant 𝑐> 0 and a strictly in-
creasing sequence of scales along which |𝐴∩[1, 𝑁]| ≥𝑐· 𝑁. Using a dependent-choice
argument, we extract a rapidly growing sequence 𝑀𝑘such that for each 𝑘:
• |𝐴∩[1, 𝑀𝑘+1]| ≥𝑐· 𝑀𝑘+1 (density is retained at the next scale),
• |𝐴∩[1, 𝑀𝑘]| ≤𝑐
4 · 𝑀𝑘+1 (the “past” is negligible relative to the “future”).
Because each new block contains all the “fresh” elements of 𝐴, looking at scale 𝑀2𝑘+1 shows
that 𝐴1 has positive upper density, and looking at scale 𝑀2𝑘+2 shows the same for 𝐴2. A
short argument then lifts this: if a set has positive upper density, so does its sumset with itself.
Case 2: 𝐴has zero upper density but 𝐴+ 𝐴has positive upper density. This is the
harder case, since 𝐴is too sparse to guarantee positive density for the parts directly. Instead,
we argue about the sumsets themselves. Since 𝐴+ 𝐴has positive upper density, there exist
𝑐> 0 and a sequence of scales along which |(𝐴+ 𝐴) ∩[1, 𝑁]| ≥𝑐· 𝑁. Since 𝐴has zero
upper density, |𝐴∩[1, 𝑁]| = 𝑜(𝑁), so for any fixed 𝐾there are arbitrarily large 𝑁where
(𝐾+ 1) · |𝐴∩[1, 𝑁]| ≤𝑐
4 · 𝑁. By dependent choice, we extract a rapidly growing 𝑀𝑘such that
for each 𝑘:
• |(𝐴+ 𝐴) ∩[1, 𝑀𝑘+1]| ≥𝑐· 𝑀𝑘+1,
• (𝑀𝑘+ 1) · |𝐴∩[1, 𝑀𝑘+1]| ≤𝑐
4 · 𝑀𝑘+1.
The key ingredient is a combinatorial sumset bound: if 𝐴= 𝐴1 ∪𝐴2 and every element of 𝐴2
in [1, 𝑁] is at most 𝐾, then
|(𝐴+ 𝐴) ∩[1, 𝑁]| ≤|(𝐴1 + 𝐴1) ∩[1, 𝑁]| + (𝐾+ 1) · |𝐴∩[1, 𝑁]|.
The idea is that any sum involving an element of 𝐴2 has one summand bounded by 𝐾, giving
at most (𝐾+ 1) · |𝐴∩[1, 𝑁]| such sums. Applying this bound at alternating scales:
• At scale 𝑁= 𝑀2𝑘+1: all elements of 𝐴2 in [1, 𝑁] lie below 𝑀2𝑘, so the bound with
𝐾= 𝑀2𝑘gives |(𝐴1 + 𝐴1) ∩[1, 𝑁]| ≥3𝑐
4 · 𝑁.
• At scale 𝑁= 𝑀2𝑘+2: symmetrically, all elements of 𝐴1 in [1, 𝑁] lie below 𝑀2𝑘+1, giving
|(𝐴2 + 𝐴2) ∩[1, 𝑁]| ≥3𝑐
4 · 𝑁.
Since these bounds hold for infinitely many 𝑁, both sumsets have positive upper density. □
The agent also initially disproved a strict “natural density” formulation of this problem
(where the density must exist as a limit), which served as a diagnostic for the correct
36
Advancing Mathematics Research with AI-Driven Formal Proof Search
interpretation of Erdős’ original phrasing. Following Thomas Bloom’s observation that Erdős
likely meant “positive upper density,” the formulation was amended and the agent resolved
the corrected version as described above. The Lean proof for the upper density variant is
available at https://github.com/google-deepmind/alphaproof-nexus-results
/blob/main/APNOutputs/ErdosProblems/erdos_741.parts.i.lean.
