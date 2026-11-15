---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-022-erdős-152
section_title: "Erdős #152"
section_number: null
pages: 41-42
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Theorem. For a Sidon set 𝐴⊂ℕof size 𝑛, let 𝐼(𝐴+ 𝐴) count the isolated elements of the
sumset — those 𝑠∈𝐴+ 𝐴with 𝑠± 1 ∉𝐴+ 𝐴. Define 𝑓(𝑛) as the minimum of 𝐼(𝐴+ 𝐴) over all
Sidon sets of size 𝑛. Then 𝑓(𝑛) ≥(𝑛2 −100𝑛−16)/16, so in particular 𝑓(𝑛) →∞.
Proof. The proof establishes, for every Sidon set 𝐴of size 𝑛:
16 · 𝐼(𝐴+ 𝐴) + 100𝑛+ 16 ≥𝑛2.
(★)
Let 𝐷= {𝑎−𝑏: 𝑎, 𝑏∈𝐴} denote the difference set and 𝑆= 𝐴+ 𝐴the sumset. For
any set 𝑋⊆ℤ, let 𝑁𝑘(𝑋) := |𝑥∈𝑋: 𝑥+ 𝑘∈𝑋| be the number of pairs at distance 𝑘,
𝑉2(𝑋) := |𝑥∈𝑋: 𝑥± 1 ∈𝑋| be the number of interior points, and 𝐼(𝑋) be the isolated points .
Let 𝑋⊂ℤ. We will employ the following three facts:
1. 𝐼(𝑋) + 2𝑁1(𝑋) = |𝑋| + 𝑉2(𝑋), by partitioning elements by neighbor count.
2. 4𝑁1(𝑋) + 𝑁3(𝑋) ≤3|𝑋| +2𝑁2(𝑋), which follows from writing 𝑁𝑘(𝑥) = Í
𝑥∈ℤ1𝑋(𝑥)1𝑋(𝑥+
𝑘) and a pointwise check of the indicator function 1𝑋across all 4-point windows
(𝑥, 𝑥+ 1, 𝑥+ 2, 𝑥+ 3); that is, summing the local inequality 1𝑋(𝑥) + 1𝑋(𝑥+ 1) + 1𝑋(𝑥+
2) + 1𝑋(𝑥)1𝑋(𝑥+ 2) + 1𝑋(𝑥+ 1)1𝑋(𝑥+ 3) ≥1𝑋(𝑥)1𝑋(𝑥+ 1) + 21𝑋(𝑥+ 1)1𝑋(𝑥+ 2) +
1𝑋(𝑥+ 2)1𝑋(𝑥+ 3) + 1𝑋(𝑥)1𝑋(𝑥+ 3) and then summing over all 𝑥∈ℤ.
3. 2𝑁2(𝑋) ≤𝑁3(𝑋) + 2𝑉2(𝑋) + 2𝐼(𝑋). Consider each pair (𝑥, 𝑥+ 2) ∈𝑋2 and we proceed
by cases on 𝑥+ 1. Let 𝐺= {𝑥∈𝑋| 𝑥+ 1 ∉𝑋∧𝑥+ 2 ∈𝑋}. If 𝑥+ 1 ∈𝑋, then the pair is
counted exactly by 𝑉2, so 𝑁2(𝑋) = 𝑉2(𝑋) + |𝐺|. If 𝑥+ 1 ∉𝑋, then
• If 𝑥−1 ∈𝑋, then (𝑥−1, 𝑥+ 2) is a pair counted in 𝑁3(𝑋).
• If 𝑥+ 3 ∈𝑋, then (𝑥, 𝑥+ 3) is a pair counted in 𝑁3(𝑋).
41
Advancing Mathematics Research with AI-Driven Formal Proof Search
• If 𝑥−1 ∉𝑋, then 𝑥is an isolated point in 𝐼(𝑋), and if 𝑥+ 3 ∉𝑋, then 𝑥+ 2 is an
isolated point in 𝐼(𝑋).
Since each 𝑁3 pair can be counted by two different gaps, while isolated points are
distinct in this construction, we have 2|𝐺| ≤𝑁3(𝑋) + 2𝐼(𝑋).
Next, for each 𝑘≥1, count quadruples (𝑎, 𝑏, 𝑐, 𝑑) ∈𝐴4 with 𝑎+ 𝑏+ 𝑘= 𝑐+ 𝑑. Rewriting as
𝑎−𝑐= 𝑑−𝑏−𝑘and partitioning by 𝛿= 𝑎−𝑐yields the following two quadruple transfer
bounds:
1. The cases 𝛿= 0 and 𝛿= −𝑘each contribute ≤|𝐴| (one coordinate determines the rest).
For any 𝛿∉{0, −𝑘}, the Sidon property ensures that there is at most one pair (𝑎, 𝑐)
with 𝑎−𝑐= 𝛿and at most one pair (𝑑, 𝑏) with 𝑑−𝑏= 𝛿+ 𝑘. Consequently, each gap of
size 𝑘in 𝐷identifies exactly one quadruple. Thus |quad𝑘| ≤𝑁𝑘(𝐷) + 2𝑛.
2. Each "good" element 𝑠∈𝑆with 𝑠+ 𝑘∈𝑆(excluding ≤2𝑛doubles of the form 2𝑎)
produces ≥4 quadruples, giving 4𝑁𝑘(𝑆) ≤|quad𝑘| + 8𝑛.
Combining these bounds shows that 𝑁𝑘(𝐷) and 𝑁𝑘(𝑆) are related up to 𝑂(𝑛) error. Apply-
ing fact (2) to 𝐷= 𝐴−𝐴gives
4𝑁1(𝐷) + 𝑁3(𝐷) ≤3|𝐷| + 2𝑁2(𝐷)
and then substitute the above two quadruple transfer bounds for 𝑘= 1, 2, 3 and collecting
all 𝑂(𝑛) terms gives
16𝑁1(𝑆) + 4𝑁3(𝑆) ≤3|𝐷| + 8𝑁2(𝑆) + 100𝑛
Then, using fact (3) on 𝑆we obtain
16𝑁1(𝑆) + 4𝑁3(𝑆) ≤3|𝐷| + (4𝑁3(𝑆) + 8𝑉2(𝑆) + 8𝐼(𝑆)) + 100𝑛
and notice that the 4𝑁3(𝑆) terms cancel. Then applying fact (1) we obtain
(8|𝑆| + 8𝑉2(𝑆) −8𝐼(𝑆)) ≤3|𝐷| + 8𝑉2(𝑆) + 8𝐼(𝑆) + 100𝑛
and see that the 8𝑉2(𝑆) terms now cancel, leaving
16𝐼(𝑆) + 100𝑛≥8|𝑆| −3|𝐷|.
The standard Sidon estimates |𝑆| ≥𝑛2/2 and |𝐷| ≤𝑛2 then give 16𝐼(𝑆)+100𝑛≥4𝑛2−3𝑛2 = 𝑛2,
accounting for a boundary correction of +16 at zero yields (★).
□
We include the Lean proof at https://github.com/google-deepmind/alphapro
of-nexus-results/blob/main/APNOutputs/ErdosProblems/erdos_152.lean.
