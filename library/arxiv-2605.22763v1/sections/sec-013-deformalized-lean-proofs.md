---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-013-deformalized-lean-proofs
section_title: "Deformalized Lean Proofs"
section_number: null
pages: 30-31
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Advancing Mathematics Research with AI-Driven Formal Proof Search
The LLM cost for each agent was computed as follows:
𝑡𝑜𝑡𝑎𝑙𝑐𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡= 𝑖𝑛𝑝𝑢𝑡∗𝑝𝑖𝑛𝑝𝑢𝑡+ 𝑐𝑎𝑐ℎ𝑒𝑟𝑒𝑎𝑑∗𝑝𝑐𝑎𝑐ℎ𝑒+ 𝑜𝑢𝑡𝑝𝑢𝑡∗𝑝𝑜𝑢𝑡𝑝𝑢𝑡,
𝑡𝑜𝑡𝑎𝑙= 𝑡𝑜𝑡𝑎𝑙𝑠𝑘𝑒𝑡𝑐ℎ𝑒𝑟+ 𝑡𝑜𝑡𝑎𝑙𝑟𝑎𝑡𝑒𝑟
where 𝑖𝑛𝑝𝑢𝑡includes user prompt, agent session prefix, thoughts and tool calls outputs and
excludes cached tokens, 𝑐𝑎𝑐ℎ𝑒𝑟𝑒𝑎𝑑accounts for the input tokens read from cache and 𝑜𝑢𝑡𝑝𝑢𝑡
includes model output and thoughts. 𝑝is the corresponding standard price per token as per
https://ai.google.dev/gemini-api/docs/pricing. Note that for all agent price
estimates, we applied the rate for prompts of 200k tokens or fewer.
B.4. Deformalized Lean Proofs
Next, we give deformalized versions of the Lean proofs discovered by our full-featured Agent
(D).
Erdős #12-(i)
First, we give the proof of the first question under Erdős problem #12, as classified on the
ErdosProblems site (https://www.erdosproblems.com).
Theorem (i). There is an infinite set 𝐴⊆ℕsatisfying that there are no distinct 𝑎, 𝑏, 𝑐∈𝐴
with 𝑎< 𝑏, 𝑐satisfying 𝑎|𝑏+ 𝑐and
lim inf
𝑁→∞
|𝐴∩{1, . . . , 𝑁}|
𝑁1/2
> 0.
Proof. We will construct a sequence of "blocks" that individually cannot contain such 𝑎, 𝑏, 𝑐,
and with a careful choice of parameters, their union forms the desired set. By precisely
controlling the growth and modular residues of these blocks, we ensure the set remains
dense enough to satisfy the lim inf condition while avoiding all forbidden divisibility relations.
Let 𝑓: ℕ→ℕbe defined by 𝑓(0) = 0 and 𝑓(𝑛) = 3 𝑓(⌊𝑛/2⌋) + (𝑛mod 2). The func-
tion 𝑓takes a number represented in base 2 and outputs the number given by the same
representation but read in base 3. In particular, the base 3 representation of 𝑓(𝑛) will contain
only 0s and 1s. For this reason, 𝑓(𝑎) + 𝑓(𝑏) = 2 𝑓(𝑐) implies 𝑎= 𝑏= 𝑐, ensuring the sequence
( 𝑓(𝑛))𝑛∈ℕcontains no 3-APs.
Next, let 𝐹𝑖be the 𝑖-th odd prime, and write 𝑀𝑖= Î
𝑗<𝑖𝐹𝑗and 𝑉𝑖= 𝐹𝑖𝑀𝑖. By Bertrand’s
postulate, we have 𝐹𝑖≤2𝑖+2. By the Chinese Remainder Theorem, for each 𝑖, let 𝐶𝑖< 𝑉𝑖be
the unique integer such that 𝐶𝑖≡0 (mod 𝐹𝑖) and 𝐶𝑖≡1 (mod 𝑀𝑖).
Now we define the parameters for the blocks (𝐵𝑖). Let
• 𝑌𝑖= 3(𝑖+20)3 be the exponential bounding scale to control the distance between blocks.
• 𝑃𝑖= 10𝑉𝑖𝑌𝑖+ 𝐶𝑖be the starting coordinate of block 𝑖.
• 𝑋𝑖= ⌊√
𝑃𝑖+1⌋be the element capacity of block 𝑖. Note that the capacity of 𝐵𝑖is directly
tied to the starting point of the next block 𝐵𝑖+1.
30
Advancing Mathematics Research with AI-Driven Formal Proof Search
Formally, define 𝐵𝑖= {𝑃𝑖+ 𝑉𝑖𝑓(𝑦) | 𝑦< 𝑋𝑖}. The purpose of 𝑌𝑖is to keep the blocks relatively
narrow while ensuring they are well-spaced. Note that if 𝑦< 2𝑘, then 𝑓(𝑦) < 3𝑘. Letting
𝑘= (𝑖+ 20)3, we want to guarantee that for any 𝑦< 𝑋𝑖, we have 𝑓(𝑦) < 𝑌𝑖= 3𝑘. To do this, it
suffices to show 𝑋𝑖≤√
𝑃𝑖+1 < 2𝑘, which is equivalent to 𝑃𝑖+1 ≤4𝑘.
Observe that 𝑃𝑖+1 ≤11𝑉𝑖+1𝑌𝑖+1 ≤11 · 2(𝑖+4)2 · 3(𝑖+21)3, following from the bound on 𝐹𝑖.
This is asymptotically strictly smaller than 4𝑘= 4(𝑖+20)3. By adding the shift of 20, the
inequality 11 · 2(𝑖+4)2 · 3(𝑖+21)3 ≤4(𝑖+20)3 holds universally for all 𝑖≥1.
Set 𝐴= Ð
𝑖∈ℕ𝐵𝑖. Clearly, 𝐴is an infinite set. Suppose, for the sake of contradiction, that there
exist distinct 𝑎, 𝑏, 𝑐∈𝐴with 𝑎< 𝑏, 𝑐such that 𝑎| (𝑏+ 𝑐). Let 𝑎∈𝐵𝑖. We analyze two cases:
• (Case 1: Cross-block) Suppose at least one of 𝑏, 𝑐is not in 𝐵𝑖. Without loss of generality,
assume 𝑏∈𝐵𝑗for some 𝑗> 𝑖(since 𝑏> 𝑎). Since 𝑎∈𝐵𝑖, we have 𝑎≡0 (mod 𝐹𝑖), and
thus 𝑏+ 𝑐≡0 (mod 𝐹𝑖) by the divisibility condition. However, by our CRT construction,
𝑏≡1 (mod 𝐹𝑖). The element 𝑐must belong to some block 𝐵𝑚with 𝑚≥𝑖, so 𝑐≡0
(mod 𝐹𝑖) (if 𝑚= 𝑖) or 𝑐≡1 (mod 𝐹𝑖) (if 𝑚> 𝑖). Therefore, 𝑏+ 𝑐≡1 (mod 𝐹𝑖) or
𝑏+ 𝑐≡2 (mod 𝐹𝑖). Since 𝐹𝑖≥3, this directly contradicts 𝑏+ 𝑐≡0 (mod 𝐹𝑖).
• (Case 2: Same block) Suppose 𝑏, 𝑐∈𝐵𝑖. They must be tightly clustered around 𝑃𝑖.
Because 𝑦< 𝑋𝑖, we have 𝑓(𝑦) < 𝑌𝑖. The maximum "noise" added to any block element is
𝑉𝑖𝑌𝑖. Since 𝑃𝑖> 10𝑉𝑖𝑌𝑖, any 𝑥∈𝐵𝑖must satisfy 𝑥∈[𝑃𝑖, 1.1𝑃𝑖]. The divisibility condition
𝑎| (𝑏+ 𝑐) implies 𝑚𝑎= 𝑏+ 𝑐for some integer 𝑚. Because 𝑏+ 𝑐∈[2𝑃𝑖, 2.2𝑃𝑖] and
𝑎∈[𝑃𝑖, 1.1𝑃𝑖], it must be that 𝑚= 2, implying 2𝑎= 𝑏+ 𝑐.
Writing the elements as 𝑎= 𝑃𝑖+ 𝑉𝑖𝑓(𝑎′), 𝑏= 𝑃𝑖+ 𝑉𝑖𝑓(𝑏′), and 𝑐= 𝑃𝑖+ 𝑉𝑖𝑓(𝑐′), substitution and
cancellation yield 2 𝑓(𝑎′) = 𝑓(𝑏′) + 𝑓(𝑐′). This is impossible for distinct 𝑎′, 𝑏′, 𝑐′ because the
image of 𝑓avoids 3-APs, contradicting the assumption that 𝑎, 𝑏, 𝑐are distinct.
Finally, we show that 𝐶(𝑁) = |𝐴∩{1, . . . , 𝑁}| ≥𝑐
√
𝑁for some constant 𝑐> 0. We split
into two cases:
1. 𝑁falls in the gap between 𝐵𝑖and 𝐵𝑖+1; precisely, 𝑃𝑖+ 𝑉𝑖𝑌𝑖≤𝑁< 𝑃𝑖+1. Here, 𝐶(𝑁)
counts at least all elements in 𝐵𝑖, meaning 𝐶(𝑁) ≥𝑋𝑖= ⌊√
𝑃𝑖+1⌋. Since 𝑁≤𝑃𝑖+1, we
have
√
𝑁≤√
𝑃𝑖+1. Thus, 𝐶(𝑁)
√
𝑁≥⌊√𝑃𝑖+1⌋
√𝑃𝑖+1 ≈1.
2. 𝑁is inside the block 𝐵𝑖; precisely, 𝑃𝑖≤𝑁< 𝑃𝑖+ 𝑉𝑖𝑌𝑖. A pessimistic lower bound counts
only the elements up to the previous block, giving 𝐶(𝑁) ≥𝑋𝑖−1 = ⌊√
𝑃𝑖⌋. Observe that
𝑉𝑖𝑌𝑖≤0.1𝑃𝑖, so 𝑁≤1.1𝑃𝑖< 2𝑃𝑖. Consequently, √
𝑃𝑖>
√︁
𝑁/2, which implies 𝐶(𝑁)
√
𝑁≥
1
√
2.
In both cases, lim inf𝑁→∞
𝐶(𝑁)
𝑁1/2 ≥
1
√
2 > 0.
□
