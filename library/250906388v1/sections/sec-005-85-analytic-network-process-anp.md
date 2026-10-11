---
doc_id: 250906388v1
doc_title: "Preliminary Draft Manuscript Chapter 8"
section_id: sec-005-85-analytic-network-process-anp
section_title: "Analytic Network Process (ANP)"
section_number: 8.5
pages: 19-26
source_pdf: 2509.06388v1.pdf
source_sha256: 48123c8812890b17
toc_source: inferred
doc_brief: "Preliminary Draft Manuscript Chapter 8 — This chapter describes selected aggregation-type multi-criteria decision-making (MCDM) methods that convert an alternatives-criteria matrix (ACM) into a"
---
The ANP method, developed by Saaty (1996, 1999), is a generalization and an advanced 
version of the AHP method described in Section 8.4. This more advanced method emphasizes 
that everything is interconnected to everything else, with a continuous flow of influence among 
all 
elements. 
ANP 
accommodates 
complex 
decision-making 
scenarios 
involving 
interdependencies and feedback among criteria and alternatives. Unlike AHP, which 
structures decision problems strictly into hierarchical layers with unidirectional influences, ANP 
uses networks, allowing mutual dependence among elements and bidirectional relationships. 
Therefore, ANP effectively addresses decision-making complexities, such as criteria 
influencing alternatives and alternatives simultaneously impacting the criteria themselves. 
The fundamental difference between AHP and ANP is that the latter replaces the strict 
hierarchical structure with a more generalized network structure comprising clusters (e.g., 
criteria clusters and alternatives clusters) and nodes (e.g., individual criterion and alternative). 
These clusters and nodes can have inner dependencies (within the same cluster) and outer 
dependencies (across different clusters), creating loops and feedback. The steps for applying 
ANP are detailed as follows: 
Step 1. Construct the ANP network structure. For clarity of illustration, we will use a simplified 
example to walk through the ANP process. Suppose a company needs to select one of the 2 
alternative designs (𝐴1, 𝐴2) based on 3 criteria (𝐶1: Cost, 𝐶2: Technical Feasibility, 𝐶3: Market 
Risk). Decision-makers recognize some interdependence among these criteria and feedback 
from the alternatives to the criteria. 
Thus, we have the following nodes: 
• 
{𝐺} — single node for goal in the goal cluster. 
• 
{𝐶1, 𝐶2, 𝐶3} — 3 criteria nodes in the criteria cluster. 
• 
{𝐴1, 𝐴2} — 2 alternatives nodes in the alternatives cluster. 
Suppose the network of influences, as illustrated in Figure 8.3, is as follows: 
• 
𝐺 influences all criteria (𝐶1, 𝐶2, 𝐶3); this does not differ from that of AHP. 
• 
𝐶1 influences {𝐶2, 𝐶3} (e.g., a higher cost can correlate with higher technical feasibility 
and lower market risk). 
𝐶2 influences {𝐶1, 𝐶3} 
Preliminary Draft Manuscript 
 
8-20 
 
𝐶3 influences {𝐶1, 𝐶2} 
• 
Each criterion (𝐶1, 𝐶2, 𝐶3) influences the alternatives (𝐴1, 𝐴2); this does not differ from 
that of AHP. 
• 
Each alternative (𝐴1, 𝐴2) influences both 𝐶2 and 𝐶3 in a feedback loop. For example, 
each alternative, if implemented, might affect technical feasibility and market risk in the 
longer term. For instance, a more innovative design 𝐴1 may push the company to 
adopt advanced technology solutions, raising the overall technical feasibility in the long 
run; and simultaneously reduce future market risk by aligning the product with 
emerging trends. 
• 
If a node influences both the criteria and alternatives clusters, we assume its impact 
on the alternatives cluster is always 3 times as important as its impact on the criteria 
cluster. In other words, the particular node devotes 75% of its influence to the 
alternatives and 25% to the criteria. 
 
Figure 8.3: ANP representation for the simplified decision-making problem; dashed arrows 
indicate inner dependencies within the Criteria cluster; solid arrows represent outer 
dependencies across the Goal, Criteria, and Alternatives clusters. Note that some arrows 
are bi-directional whereas the others (e.g., from Criteria 1 to Alternatives 1 and 2) are in one 
direction only.  
Step 2. Construct pairwise comparison matrices among the nodes and determine local 
priorities. 
Using the simplified example, we now go node by node, identifying each parent node and 
performing the standard pairwise comparisons (as in AHP) among the child nodes under each 
parent, to find how strongly each parent influences its child nodes. 
➢ Under the Goal node (𝑮): 
Preliminary Draft Manuscript 
 
8-21 
 
Since 𝐺 influences all criteria (𝐶1, 𝐶2, 𝐶3): 
- 
Parent: 𝐺 
- 
Children: {𝐶1, 𝐶2, 𝐶3} 
Suppose the subjective assessment using Saaty's 1–9 scale are as follows: 
- 
𝐶1 and 𝐶2 are treated equally important (ratio 1:1) 
- 
𝐶3 is twice as important as 𝐶1, and also twice as important as 𝐶2 (ratios 2:1) 
Hence, the 3 × 3 pairwise comparison matrix of the 3 criteria under 𝐺 is constructed as 
follows: 
𝑀𝐺→(𝐶1,𝐶2,𝐶3) = (
1
1
0.5
1
1
0.5
2
2
1.0
) 
Same as the calculations in Step 2 of AHP, eigenvalue method is employed to determine the 
principal eigenvalue (𝜆max) and normalized principal eigenvector (i.e., criteria priorities or 
weights). Using WolframAlpha, 𝜆max is found to be 3.0. The corresponding criteria weights are 
as follows: 
𝑤𝐺→𝐶1 = 0.25, 𝑤𝐺→𝐶2 = 0.25, 𝑤𝐺→𝐶3 = 0.50. 
For brevity, the consistency ratio check is omitted here. Its computation follows the exact same 
procedure as in Step 3 of AHP. 
➢ Under the Criterion 1 node (𝑪𝟏): 
Since 𝐶1 influences both {𝐶2, 𝐶3} and (𝐴1, 𝐴2): 
- 
Parent: 𝐶1 
- 
Children: {𝐶2, 𝐶3, 𝐴1, 𝐴2} 
Besides, as aforementioned, when a node influences both the criteria and alternatives 
clusters, it devotes 75% of its influence to the alternatives and 25% to the criteria.  
Now, inside {𝐶2, 𝐶3} pairwise comparison, 𝐶2 is one-half as important as 𝐶3 (ratio 1:2). The 
comparison matrix is as follows: 
𝑀𝐶1→(𝐶2,𝐶3) = (1
1/2
2
1 ) 
For this matrix, 𝜆max = 2. The corresponding priorities are 0.3333 and 0.6667 for 𝐶2 and 𝐶3, 
respectively. Given that 𝐶1 allocates 25% of its influence to criteria cluster, weights are: 
𝑤𝐶1→𝐶2 = 0.3333 × 0.25 = 0.0833 
Preliminary Draft Manuscript 
 
8-22 
 
𝑤𝐶1→𝐶3 = 0.6667 × 0.25 = 0.1667 
Analogously, inside {𝐴1, 𝐴2} pairwise comparison, 𝐴1 is 3 times as important as 𝐴2 (ratio 3:1). 
The comparison matrix is as follows: 
𝑀𝐶1→(𝐴1,𝐴2) = ( 1
3
1/3
1) 
For this matrix, 𝜆max = 2. The corresponding priorities are 0.75 and 0.25 for 𝐴1 and 𝐴2 , 
respectively. Given that 𝐶1 allocates 75% of its influence to the alternatives cluster, weights 
are: 
𝑤𝐶1→𝐴1 = 0.75 × 0.75 = 0.5625 
𝑤𝐶1→𝐴2 = 0.25 × 0.75 = 0.1875 
➢ Under the Criterion 2 node (𝑪𝟐): 
The calculations under 𝐶2 are similar to those under 𝐶1; for brevity, only the key points and 
numbers are presented. 
𝐶2 influences both {𝐶1, 𝐶3} and (𝐴1, 𝐴2): 
- 
Parent: 𝐶2 
- 
Children: {𝐶1, 𝐶3, 𝐴1, 𝐴2} 
Inside {𝐶1, 𝐶3}, 𝐶1 is treated equally as important as 𝐶3 (ratio 1:1). The corresponding priorities 
are 0.25 each. Considering 25% of parent’s influence to criteria cluster, weights are: 
𝑤𝐶2→𝐶1 = 0.25 × 0.25 = 0.125 
𝑤𝐶2→𝐶3 = 0.25 × 0.25 = 0.125 
Inside {𝐴1, 𝐴2}, 𝐴1 is one-half as important as 𝐴2 (ratio 1:2). The corresponding priorities are 
0.3333 and 0.6667 for 𝐴1 and 𝐴2, respectively. Considering 75% of parent’s influence to the 
alternatives cluster, weights are: 
𝑤𝐶2→𝐴1 = 0.3333 × 0.75 = 0.25 
𝑤𝐶2→𝐴2 = 0.6667 × 0.75 = 0.50 
➢ Under the Criterion 3 node (𝑪𝟑): 
Again, for conciseness, only the key points and numbers under 𝐶3 are presented. 
- 
Parent: 𝐶3 
- 
Children: {𝐶1, 𝐶2, 𝐴1, 𝐴2}. 
Inside {𝐶1, 𝐶2}, 𝐶1 is 3 times as important as 𝐶3 (ratio 3:1). The corresponding priorities are 
0.75 and 0.25 for 𝐶1 and 𝐶2. Considering 25% of parent’s influence to criteria cluster, weights 
are: 
𝑤𝐶3→𝐶1 = 0.75 × 0.25 = 0.1875 
Preliminary Draft Manuscript 
 
8-23 
 
𝑤𝐶3→𝐶2 = 0.25 × 0.25 = 0.0625 
Inside {𝐴1, 𝐴2}, 𝐴1 is twice as important as 𝐴2 (ratio 2:1). The corresponding priorities are 
0.6667 and 0.3333 for 𝐴1 and 𝐴2, respectively. Considering 75% of parent’s influence to the 
alternatives cluster, weights are: 
𝑤𝐶3→𝐴1 = 0.6667 × 0.75 = 0.50 
𝑤𝐶3→𝐴2 = 0.3333 × 0.75 = 0.25 
➢ Under the Alternative 1 node (𝐴1): 
Since 𝐴1 influences both 𝐶2 and 𝐶3 in a feedback loop: 
- 
Parent: 𝐴1 
- 
Children: {𝐶2, 𝐶3}. 
Inside {𝐶1, 𝐶2}, suppose ratio of 𝐶2:𝐶3 = 1: 2, thus: 
𝑤𝐴1→𝐶2 = 0.3333 
𝑤𝐴1→𝐶3 = 0.6667 
 
➢ Under the Alternative 2 node (𝐴2): 
Since 𝐴2 influences both 𝐶2 and 𝐶3 in a feedback loop: 
- 
Parent: 𝐴2 
- 
Children: {𝐶2, 𝐶3}. 
Inside {𝐶1, 𝐶2}, suppose ratio of 𝐶2:𝐶3 = 1: 1, thus: 
𝑤𝐴2→𝐶2 = 0.50 
𝑤𝐴2→𝐶3 = 0.50 
Step 3. Construct the weighted supermatrix (𝐖). 
The weighted supermatrix is formed by consolidating all the results from the previous step. It 
is termed “super’ because it incorporates all the nodes and their influences in the ANP 
network. In this supermatrix, as shown in Table 8.10 each column header represents a parent 
node; the entries in each column indicate the influence of the parent node on its child nodes; 
for node pairs that were not compared in the previous step, simply assign a value of 0. 
Table 8.10: ANP weighted supermatrix (𝐖). 
Preliminary Draft Manuscript 
 
8-24 
 
 
𝐺 
𝐶1 
𝐶2 
𝐶3 
𝐴1 
𝐴2 
𝐺 
0 
0 
0 
0 
0 
0 
𝐶1 
0.25 
0 
0.125 
0.1875 
0 
0 
𝐶2 
0.25 
0.0833 
0 
0.0625 
0.3333 
0.50 
𝐶3 
0.50 
0.1667 
0.125 
0 
0.6667 
0.50 
𝐴1 
0 
0.5625 
0.25 
0.50 
0 
0 
𝐴2 
0 
0.1875 
0.50 
0.25 
0 
0 
 
Step 4. Compute the limit supermatrix (𝐖∞) as follows: 
𝐖∞= lim
𝑘→∞𝐖𝑘 
(8.17)  
As seen, the limit supermatrix is obtained by raising the weighted supermatrix to powers until 
convergence. This can be computed by repeatedly multiplying the weighted supermatrix by 
itself until it stabilizes. In essence, the limit supermatrix represents the long‐run steady‐state 
priorities in a network of feedback influences. Each column of the supermatrix tells us how a 
particular parent node distributes its influence among its child nodes. By raising the 
supermatrix to higher and higher powers, it is essentially simulating infinitely many rounds of 
mutual influence among the nodes. Once the matrix powers stabilize (converge), it indicates 
a steady-state distribution of influence. The entries in the columns of the resulting 𝐖∞, as 
shown in Table 8.11, can be interpreted as the overall priorities of each node under its parent 
node. In this example, all columns eventually converge to the same values; however, this may 
not be the case in all applications. 
Table 8.11: ANP limit supermatrix (𝐖∞). 
 
𝐺 
𝐶1 
𝐶2 
𝐶3 
𝐴1 
𝐴2 
𝐺 
0 
0 
0 
0 
0 
0 
𝐶1 
0.0797 
0.0797 
0.0797 
0.0797 
0.0797 
0.0797 
𝐶2 
0.1991 
0.1991 
0.1991 
0.1991 
0.1991 
0.1991 
𝐶3 
0.2926 
0.2926 
0.2926 
0.2926 
0.2926 
0.2926 
𝐴1 
0.2409 
0.2409 
0.2409 
0.2409 
0.2409 
0.2409 
𝐴2 
0.1876 
0.1876 
0.1876 
0.1876 
0.1876 
0.1876 
 
Next, from 𝐖∞, we extract the global priority scores for alternatives, 𝐴1:0.2409 and 
𝐴2: 0.1876, under the goal node 𝐺. After applying sum normalization, the normalized global 
priority score for 𝐴1 is 0.5622(= 0.2409/(0.2409 + 0.1876) and for 𝐴2 is 0.4378 (= 0.1876/
Preliminary Draft Manuscript 
 
8-25 
 
(0.2409 + 0.1876) . Therefore, alternative 𝐴1 is ranked higher and recommended for 
implementation. 
Alternatively, we can also use SuperDecisions to solve this problem. Figure 8.4(a) presents 
the weighted supermatrix (𝐖) calculated by SuperDecisions. Figure 8.4(b) displays the limit 
supermatrix (𝐖∞). Figure 8.4(c) shows the normalized global priority scores. All these results 
tally with our previous calculations. The original SuperDecisions file for this ANP model can 
be downloaded from our shared folder in Google Drive:  
https://drive.google.com/drive/folders/18ynIwnKaCRsptwBCrMIFVOlV9Mu_A7qM?usp=shari
ng 
 
Figure 8.4(a): Screenshot of the weighted supermatrix (𝐖) from SuperDecisions for ANP. 
 
 
Figure 8.4(b): Screenshot of the limit supermatrix (𝐖∞) from SuperDecisions for ANP. 
Preliminary Draft Manuscript 
 
8-26 
 
 
Figure 8.4(c): Screenshot of the normalized global priority scores from SuperDecisions for 
ANP. 
The advantages of ANP are as follows. (1) ANP is designed to handle interdependent criteria 
and alternatives by allowing feedback loops and reciprocal influences, thereby providing a 
more realistic representation of complex decision problems that are not strictly hierarchical. 
(2) The network-based model facilitates a deeper understanding of how changes to one 
criterion can impact others, leading to comprehensive insights that might not emerge from 
linear approaches. (3) By breaking down interrelationships into pairwise comparisons, ANP 
uses subjective judgments while preserving logical consistency to a reasonable extent. (4) 
Because it captures the nuanced interplay among factors, ANP can be particularly beneficial 
in situations where multiple variables are intertwined, and traditional methods struggle to 
capture those interdependencies. 
The limitations of ANP are as follows. (1) ANP’s feedback-driven structure can be challenging 
to explain to stakeholders who are unfamiliar with the method, potentially hindering consensus 
or agreement. (2) The method generally requires specialized software (e.g., SuperDecisions, 
AhpAnpLib Python library) and a solid grasp of the underlying theory, which can be a barrier 
in terms of both cost and the learning curve for practitioners. (3) Verification and interpretation 
of results can be complex, given the myriad loops and interconnections; isolating the impact 
of individual criteria becomes less straightforward than in hierarchical models. (4) For simpler 
decision problems where criteria and alternatives are relatively independent, ANP may be 
excessive, since more familiar and less resource-intensive methods (e.g., AHP) can often 
suffice while providing similar outcomes. 
8.6
