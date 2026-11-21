---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-018-erdős-741-ii
section_title: "Erdős #741-(ii)"
section_number: null
pages: 37-37
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Question. Is there a basis 𝐴of order 2 such that if 𝐴= 𝐴1 ⊔𝐴2 then 𝐴1 + 𝐴1 and 𝐴2 + 𝐴2
cannot both have bounded gaps?
Proof. We show that the answer is yes by constructing a pathological basis 𝐴with “forbidden
zones” that force any partition to create arbitrarily large gaps in at least one component
sumset.
Step 1: The construction. Choose a sequence of rapidly growing scales 𝑃𝑘= 100𝑘. For each
𝑘≥1, define a forbidden zone 𝑍𝑘, which is a broad interval of integers running roughly
from 11
2 𝑃𝑘to 11𝑃𝑘+ 𝑘. In the middle of this zone, we leave a single “oasis” — an isolated
element 𝑥𝑘= 10𝑃𝑘. The set 𝐴consists of all natural numbers that avoid every forbidden
zone, together with the oases 𝑥𝑘. In visual terms, 𝐴is made of clumps of consecutive integers
separated by large empty gaps, each containing a single survivor 𝑥𝑘.
Step 2: 𝐴∪{0} is a basis of order 2. We must show every natural number 𝑛can be
written as 𝑎+ 𝑏with 𝑎, 𝑏∈𝐴∪{0}:
• If 𝑛∉𝑍𝑘for any 𝑘, then 𝑛∈𝐴and we use 𝑛+ 0 = 𝑛.
• If 𝑛∈𝑍𝑘and 𝑛lies in the lower half of 𝑍𝑘, we use ⌊𝑛/2⌋+ ⌈𝑛/2⌉. Because 𝑛is small
enough, neither half lands in 𝑍𝑘, and both are large enough to avoid the previous zone
𝑍𝑘−1.
• If 𝑛∈𝑍𝑘and 𝑛lies in the upper half, we use the oasis: 𝑛= 𝑥𝑘+ (𝑛−𝑥𝑘). The difference
𝑛−𝑥𝑘is small enough that it falls safely before the forbidden zone 𝑍𝑘.
Step 3: No syndetic partition exists. Suppose 𝐴= 𝐴1 ⊔𝐴2. Consider a target sum
𝑚∈[11𝑃𝑘, 11𝑃𝑘+ 𝑘]. To write 𝑚= 𝑢+ 𝑣with 𝑢, 𝑣∈𝐴, the algebra forces the larger operand
𝑣to land inside the forbidden range [ 11
2 𝑃𝑘, 11𝑃𝑘+ 𝑘]. But the only element of 𝐴in this range
is 𝑥𝑘. Therefore, representing any sum in [11𝑃𝑘, 11𝑃𝑘+ 𝑘] requires 𝑥𝑘.
By the pigeonhole principle, 𝑥𝑘belongs to exactly one partition component, say 𝐴1. Then
𝐴1 + 𝐴1 can cover the interval [11𝑃𝑘, 11𝑃𝑘+ 𝑘] using 𝑥𝑘, but 𝐴2 + 𝐴2 is completely locked out
— it cannot represent any element in that interval. This leaves a gap of length 𝑘in 𝐴2 + 𝐴2.
Since 𝑘can be made arbitrarily large, the gaps in one component’s sumset are unbounded,
proving it is impossible to partition 𝐴so that both sumsets have bounded gaps.
□
The Lean proof for part (ii) is available at https://github.com/google-deepmind/
