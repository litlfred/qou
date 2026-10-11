---
doc_id: 250906388v1
doc_title: "Preliminary Draft Manuscript Chapter 8"
section_id: sec-004-84-analytic-hierarchy-process-ahp
section_title: "Analytic Hierarchy Process (AHP)"
section_number: 8.4
pages: 6-19
source_pdf: 2509.06388v1.pdf
source_sha256: 48123c8812890b17
toc_source: inferred
doc_brief: "Preliminary Draft Manuscript Chapter 8 — This chapter describes selected aggregation-type multi-criteria decision-making (MCDM) methods that convert an alternatives-criteria matrix (ACM) into a"
---
Preliminary Draft Manuscript 
 
8-7 
 
The AHP method, originally developed by Saaty (1977, 1990), is based on decision-makers’ 
subjective pairwise comparisons. To facilitate this, Saaty’s fundamental 1–9 scale (Table 8.4) 
is typically employed. The AHP method begins by constructing a decision hierarchy, 
organizing the overall goal, 𝑛 criteria, and 𝑚 alternatives into a structured model, as illustrated 
in Figure 8.1. Decision-makers then perform subjective pairwise comparisons to assess the 
relative importance among each pair of criteria using Saaty’s 1–9 scale. These comparisons 
are compiled into an 𝑛× 𝑛 pairwise comparison matrix. Following this, the eigenvalue method 
is used to find the priority eigenvector from the matrix, which then determines the criteria 
weights (Saaty, 1990). Instead of the eigenvalue method, there is a simpler approximation 
technique (based on sum normalization of the pairwise comparison matrix) to calculate the 
criteria weights, which is adopted in many applications (e.g., Teknomo, 2006; Karim & 
Karmaker, 2016; Wang et al., 2020). The procedure for determining criteria weights follows 
the same steps outlined in the AHP section of Chapter 6. If the criteria weights have already 
been explicitly predefined by decision-makers, this step may be omitted. Note that 
determination of criteria weights by the AHP method does not require ACM. 
 
Figure 8.1: Illustration of the AHP decision hierarchy of Goal, Criteria and Alternatives in top, 
middle and bottom levels 
 
Table 8.4: Saaty’s 1–9 pairwise comparison scale. 
Scale 
Compare between events x and y 
1 
Equal importance of x against y 
3 
Moderate importance of x against y 
Preliminary Draft Manuscript 
 
8-8 
 
5 
Essential or strong importance of x against y 
7 
Very strong importance of x against y 
9 
Extreme importance of x against y 
2, 4, 6, 8 
Intermediate value between adjacent scales 
Any decimal within [1, 9], 
e.g., 2.3 and 5.1 
Finer scale 
Reciprocals, e.g., 1/3 
and 1/7 
If event x has one of the above numbers assigned to it 
when compared with event y, then y has the reciprocal 
value when compared with x. 
 
In addition to determining the criteria weights, it is crucial to recognize that the AHP method 
can be directly utilized for decision-making (i.e., act as an MCDM method). For this, the 
conventional procedure is that decision-makers conduct subjective pairwise comparisons 
among alternatives with respect to each criterion, leading to 𝑛 number of 𝑚× 𝑚 pairwise 
comparison matrices. According to the original AHP method (Saaty, 1990), these pairwise 
comparisons among alternatives are purely subjective, sourced directly from the judgments of 
the decision-makers. For each 𝑚× 𝑚 pairwise comparison matrix, AHP calculates the local 
priority vector (sized 𝑚× 1) for alternatives with respect to the corresponding criterion using 
the eigenvalue method, analogous to the calculation of criteria weights at the beginning. 
Notably, a typical ACM containing objective quantitative data on different measurement scales 
(e.g., Table 8.1), rather than the subjective pairwise comparisons using Saaty’s 1–9 scale, is 
neither required nor immediately compatible with the AHP acting as an MCDM method. 
However, mapping the objective quantitative data (e.g., Table 8.1) to Saaty’s 1–9 scale and 
constructing 𝑛 number of 𝑚× 𝑚 pairwise comparison matrices, is feasible (Si et al., 2016). 
Subsequently, AHP iterates through all 𝑛 criteria, calculates, and amalgamates these local 
priority vectors (𝑚× 1) into a local priority matrix (𝑚× 𝑛), in which each row indicates the 
priority of an alternative with respect to all 𝑛 criteria. This 𝑚× 𝑛 local priority matrix is then 
multiplied by the 𝑛× 1 criteria weights vector (previously calculated by AHP or predefined by 
decision-makers), resulting in an 𝑚× 1 vector representing the global priorities of all 
alternatives. The alternative with the highest global priority value is top-ranked and 
recommended to decision-makers.  
The main procedural steps of the AHP method are summarized below. For completeness, we 
will go through the full AHP steps along with numerical calculations, starting with determining 
criteria weights, followed by calculating the local priority vectors of alternatives with respect to 
Preliminary Draft Manuscript 
 
8-9 
 
each criterion, and finally aggregating the results to rank the alternatives. In the following, 
Steps 1 to 3 are for the criteria weights, and Steps 4 and 5 are for ranking the alternatives. 
Step 1. Construct the 𝑛× 𝑛 pairwise comparison matrix for 𝑛 criteria as follows. 
𝐌𝐀=
[
 
 
 
 
𝑎11
𝑎12
𝑎13
…
𝑎1𝑛
𝑎21
𝑎22
𝑎23
…
𝑎2𝑛
𝑎31
𝑎32
𝑎33
…
𝑎3𝑛
⋮
⋮
⋮
⋱
⋮
𝑎𝑛1
𝑎𝑛2
𝑎𝑛3
…
𝑎𝑛𝑛]
 
 
 
 
 
(8.6) 
• 
Here, 𝑖, 𝑗∈{1,2, … , 𝑛}, each entry 𝑎𝑖𝑗 represents the relative importance of criterion 𝑖 
compared to criterion 𝑗 by using Saaty’s 1–9 scale (in Table 8.4). 
• 
The leading diagonal entries (𝑎11, 𝑎22, 𝑎33, … , 𝑎𝑛𝑛) of this matrix are always equal to 
unity, that is, the relative importance of a criterion compared to itself is always 1. 
• 
The following equation always holds true (i.e., entries below the leading diagonal are 
the reciprocals of the corresponding entries above it), as per the last row of Table 8.4.  
𝑎𝑖𝑗= 1
𝑎𝑗𝑖
 
(8.7) 
• 
For instance, if we consider that the relative importance of criterion 1 versus criterion 
2 is moderate (i.e., 𝑎12 = 3), then relative importance criterion 2 to criterion 1 is its 
reciprocal (i.e., 𝑎21 = 1 3
⁄ ). Thus, only 
𝑛(𝑛−1)
2
 comparisons are needed to populate half 
of the matrix, with values of the other half obtained through simple reciprocals. 
Numerical Calculations: 
Instead of using the predefined weights presented in the last row of Table 8.1, suppose that 
the decision-maker provides the following subjective assessments for the 3 criteria (C1, C2, 
and C3) using Saaty’s 1–9 scale: 
• 
C1 is moderately more important than C2 (i.e., 𝑎12 = 3 and 𝑎21 = 1 3
⁄ ), meaning C1 
is 3 times as important as C2, while C2 holds only 1/3 the importance of C1. 
• 
C1 is strongly more important than C3 (i.e., 𝑎13 = 5 and 𝑎31 = 1 5
⁄ ). 
• 
C2 is rated between moderate and strong in importance relative to C3 (i.e., 𝑎23 = 4 
and 𝑎32 = 1 4
⁄ ). 
Based on these assessments, the 3 × 3 pairwise comparison matrix is as follows: 
𝐌𝐀= [
𝑎11
𝑎12
𝑎13
𝑎21
𝑎22
𝑎23
𝑎31
𝑎32
𝑎33
] = [
1
3
5
1 3
⁄
1
4
1 5
⁄
1 4
⁄
1
] 
 
Preliminary Draft Manuscript 
 
8-10 
 
Step 2. Compute the priority vector (i.e., criteria weights in this step), using the eigenvalue 
method by solving the following equation. 
𝐌𝐀 𝐰∗= 𝜆max 𝐰∗ 
(8.8) 
Here, 𝜆max is the largest eigenvalue (known as the principal eigenvalue) of the pairwise 
comparison matrix, and 𝐰∗ is the corresponding principal eigenvector. The entries of this 
principal eigenvector are then normalized to sum to 1, yielding the criteria weights in this step, 
as follows. 
𝑤𝑗=
𝑤𝑗
∗
∑
𝑤𝑘
∗
𝑛
𝑘=1
,  𝑗= 1,2, … , 𝑛 
(8.9) 
Here, 𝑤𝑗
∗ and 𝑤𝑘
∗ represent the 𝑗𝑡ℎ and 𝑘𝑡ℎ entries of the principal eigenvector 𝐰∗, 
respectively, while 𝑤𝑗 denotes the final weight of criterion 𝑗. 
Numerical Calculations: 
Solve the following equation using computational tools such as WolframAlpha 
(https://www.wolframalpha.com/input?i=eigenvalue+calculator) or Python code: 
[
1
3
5
1 3
⁄
1
4
1 5
⁄
1 4
⁄
1
] 𝐰∗= 𝜆max𝐰∗ 
Use of WolframAlpha gives the principal eigenvalue 𝜆max = 3.086 and the corresponding 
principal eigenvector 𝐰∗= [
6.6943
2.9876
1
]. Note that when using different computational tools, the 
computed principal eigenvector may be scaled by a constant factor. 
Next, apply sum normalization to the principal eigenvector to derive the weights of the 3 
criteria (C1, C2, and C3), as follows. 
𝑤1 =
𝑤1
∗
∑
𝑤𝑘
∗
3
𝑘=1
=
6.6943
6.6943 + 2.9876 + 1 = 0.6267 
𝑤2 =
𝑤2
∗
∑
𝑤𝑘
∗
3
𝑘=1
=
2.9876
6.6943 + 2.9876 + 1 = 0.2797 
𝑤3 =
𝑤3
∗
∑
𝑤𝑘
∗
3
𝑘=1
=
1
6.6943 + 2.9876 + 1 = 0.0936 
As expected, these weights very much depend on the values given by decision-makers, for 
pairwise comparison of criteria. Further, the above weights are different from the arbitrarily 
assumed weight values in Table 8.1. 
 
Preliminary Draft Manuscript 
 
8-11 
 
Step 3. Check the consistency of the pairwise comparison matrix of 𝑛 criteria by calculating 
its consistency ratio (𝐶𝑅). 
𝐶𝐼= 𝜆𝑚𝑎𝑥−𝑛
𝑛−1
,  𝐶𝑅= 𝐶𝐼
𝑅𝐼 
(8.10) 
Here, 𝐶𝐼 is the consistency index, and 𝑅𝐼 (shown in Table 8.5) is the random 𝐶𝐼 value 
provided by Saaty (1990), who computed it by averaging the 𝐶𝐼 values from numerous 
randomly generated 𝑛× 𝑛 reciprocal matrices using Saaty’s 1–9 scale. If 𝐶𝑅≤0.1 , 
consistency is considered acceptable. If not, decision-makers should review and revise their 
given values for pairwise comparison of criteria. 
In addition, for a perfectly consistent pairwise comparison matrix (where each comparison 𝑎𝑖𝑗 
between criterion 𝑖 and criterion 𝑗 exactly equals the ratio of their resulting weights 𝑤𝑖𝑤𝑗
⁄
, 
which also implies that the transitive property holds, i.e., 𝑎𝑖𝑗𝑎𝑗𝑘= 𝑎𝑖𝑘 for all criteria 𝑖, 𝑗, and 𝑘), 
Saaty (1990) proved that the largest eigenvalue of this matrix is equal to the number of criteria, 
i.e., 𝜆max = 𝑛. 
Note on consistency analysis: Since we are dealing with human judgment for pairwise 
comparison matrix, it is inherently subjective and may sometimes be vague or inconsistent. 
For example, if a decision-maker prefers criterion 1 over criterion 2, and criterion 2 over 
criterion 3, then logically, he or she should prefer criterion 1 over criterion 3. This logical 
principle is known as the transitive property. However, in practice, due to cognitive biases or 
judgmental inconsistencies, decision-makers may unknowingly violate this property to some 
extent. 
Table 8.5: Saaty’s 𝑅𝐼 values; for 𝑛> 10, see Podvezko (2009). 
𝑛 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
𝑅𝐼 
0 
0 
0.58 
0.90 
1.12 
1.24 
1.32 
1.41 
1.45 
1.49 
 
Numerical Calculations: 
In this example, with 𝑛= 3, refer to Table 8.5 and find the corresponding 𝑅𝐼= 0.58. 
𝐶𝐼= 𝜆max −𝑛
𝑛−1
= 3.086 −3
3 −1
= 0.0429 
𝐶𝑅= 𝐶𝐼
𝑅𝐼= 0.0429
0.58
= 0.074 
Since the calculated 𝐶𝑅 satisfies 𝐶𝑅≤0.1, the decision-maker’s subjective assessments 
for the 3 criteria are considered consistent and acceptable. 
Preliminary Draft Manuscript 
 
8-12 
 
 
After obtaining the criteria weights, the following steps are for ranking the alternatives by the 
AHP method. 
Step 4. Determine local priority scores of alternatives under each criterion, denoted as 𝑣𝑖𝑗 with 
𝑖∈{1,2, . . . , 𝑚} and 𝑗∈{1,2, . . . , 𝑛}.  
With respect to each of the 𝑛 criteria, a separate pairwise comparison matrix (size 𝑚× 𝑚) is 
constructed, comparing all pairs of 𝑚 alternatives, which essentially follows the same 
procedure as described in Steps 1 to 3 including consistency analysis. For example, the 
decision-maker assesses alternative 1 against alternative 2 under the first criterion and 
assigns a relative importance value using Saaty’s 1–9 scale. This process is repeated for all 
pairs of 𝑚 alternatives under each criterion. Once the 𝑛 number of 𝑚× 𝑚 pairwise 
comparison matrices are established, the local priority vectors (representing the relative 
priorities of alternatives for each criterion) are computed using the eigenvalue method as in 
Step 2. 
At this stage, if the decision-maker does not have an ACM (such as Table 8.1) based on 
objective measurement data, they can continue to rely entirely on their subjective judgments, 
as in Step 1, to construct all pairwise comparison matrices for alternatives under each criterion 
(e.g., A1 is moderately more important/better than A4 under C1; A3 is strongly more 
important/better than A2 under C3).  
If an ACM based on objective measurement data is available, since it is not directly compatible 
with the conventional AHP process that relies on Saaty’s 1–9 scale, the decision-maker needs 
to first map the objective data into Saaty’s 1–9 scale (Si et al., 2016). This is done either 
through subjective assessment, leveraging the decision-maker’s domain knowledge to inspect 
the ACM and assign pairwise comparison values of alternatives under each criterion using the 
1–9 scale, or by applying mathematical mapping techniques. After this mapping, the decision-
maker constructs the pairwise comparison matrices for alternatives for each criterion. One 
commonly used mathematical mapping technique is the logarithmic transformation, whose 
steps are outlined below. 
Firstly, normalize the original ACM with 𝑚 rows (i.e., alternatives) and 𝑛 columns (i.e., criteria) 
by using the Max normalization method.  
For a maximization criterion, the normalized value 𝐹𝑖𝑗 is obtained as: 
𝐹𝑖𝑗=
𝑓𝑖𝑗
𝑚𝑎𝑥
𝑘∈{1,2,...,𝑚}𝑓𝑘𝑗
 
(8.11)  
For a minimization criterion, the normalized value 𝐹𝑖𝑗 is obtained as: 
Preliminary Draft Manuscript 
 
8-13 
 
𝐹𝑖𝑗=
𝑚𝑖𝑛
𝑘∈{1,2,...,𝑚}𝑓𝑘𝑗
𝑓𝑖𝑗
 
(8.12)  
The above normalization transforms all minimization criteria to maximization type (i.e., a higher 
𝐹𝑖𝑗 always indicates a better performance). 
Next, for each criterion 𝑗, determine the largest ratio (𝑟𝑚𝑎𝑥,𝑗) and smallest ratio (𝑟𝑚𝑖𝑛,𝑗) after 
comparing each alternative’s normalized value with the minimum 𝐹𝑖𝑗 in that criterion: 
𝑟𝑚𝑎𝑥,𝑗=
𝑚𝑎𝑥
𝑖
𝐹𝑖𝑗
𝑚𝑖𝑛
𝑖
𝐹𝑖𝑗
,  𝑖∈{1,2, . . . , 𝑚} 𝑎𝑛𝑑 𝑗∈{1,2, . . . , 𝑛}  
(8.13)  
𝑟𝑚𝑖𝑛,𝑗=
𝑚𝑖𝑛
𝑖
𝐹𝑖𝑗
𝑚𝑖𝑛
𝑖
𝐹𝑖𝑗
= 1,  𝑖∈{1,2, . . . , 𝑚} 𝑎𝑛𝑑 𝑗∈{1,2, . . . , 𝑛} 
(8.14)  
Here, 𝑟𝑚𝑖𝑛,𝑗 always equals 1 because it is the ratio of minimum 𝐹𝑖𝑗 to itself. 
Then, for each criterion 𝑗, the pairwise comparison between alternative 𝑖 and 𝑘 (i.e., 𝑎𝑖𝑘) is 
mapped into Saaty’s 1–9 scale by using the logarithmic transformation as follows: 
When 𝐹𝑖𝑗≥𝐹𝑘𝑗,      𝑎𝑖𝑘=
𝑙𝑛(𝐹𝑖𝑗
𝐹𝑘𝑗) −𝑙𝑛(𝑟𝑚𝑖𝑛,𝑗)
𝑙𝑛(𝑟𝑚𝑎𝑥,𝑗) −𝑙𝑛(𝑟𝑚𝑖𝑛,𝑗) × (9 −1) + 1,  𝑖, 𝑘∈{1,2, . . . , 𝑚} 
(8.15)  
For cases of 𝐹𝑖𝑗< 𝐹𝑘𝑗 when comparing 𝐹𝑖𝑗 over 𝐹𝑘𝑗, its pairwise comparison value 𝑎𝑖𝑘 is 
obtained through simple reciprocal of the comparison of 𝐹𝑘𝑗 over 𝐹𝑖𝑗, since 𝑎𝑖𝑘=
1
𝑎𝑘𝑖.  
The reason logarithmic transformation is commonly used in this context is that Saaty’s 1–9 
scale is meant to convey a ratio of importance (1 means equal, 3 means moderate, 9 means 
extreme, etc.). A logarithmic transformation preserves these multiplicative (ratio) relationships. 
For example, comparing 𝐹𝑖𝑗= 0.2 and 𝐹𝑘𝑗= 0.1, their ratio 
𝐹𝑖𝑗
𝐹𝑘𝑗 is 2, thus 𝑙𝑛(
𝐹𝑖𝑗
𝐹𝑘𝑗) = 0.693; 
similarly, comparing 𝐹𝑖𝑗= 0.9 and 𝐹𝑘𝑗= 0.45, their ratio 
𝐹𝑖𝑗
𝐹𝑘𝑗 is also 2 and 𝑙𝑛(
𝐹𝑖𝑗
𝐹𝑘𝑗) = 0.693. 
Since both comparisons yield the same logarithmic value, the pairwise comparison value 𝑎𝑖𝑘 
remains the same in both cases. 
Once the pairwise comparison matrices for all alternatives under each criterion are 
constructed, the eigenvalue method equation from Step 2 can be re-used to compute the local 
priority scores (𝑣𝑖𝑗), which are derived by applying the sum normalization to the obtained 
principal eigenvector. In addition, the equation from Step 3 is re-used to calculate the 
consistency ratios of the matrices. 
Numerical Calculations (using ACM from Table 8.1): 
Preliminary Draft Manuscript 
 
8-14 
 
Apply Max normalization method, the original ACM is normalized and shown in Table 8.6. 
Table 8.6: Normalized ACM for AHP walkthrough. 
Alternatives 
C1 
C2 
C3 
A1 
1 
0.8571 
0.3612 
A2 
0.5484 
1 
0.4708 
A3 
0.8280 
0.7143 
0.9430 
A4 
0.8817 
0.5714 
1 
 
For instance, for 𝑗= 1: 
𝑟𝑚𝑎𝑥,1 =
𝑚𝑎𝑥
𝑖
𝐹𝑖1
𝑚𝑖𝑛
𝑖
𝐹𝑖1
=
1
0.5484 = 1.8235 
𝑟𝑚𝑖𝑛,1 =
𝑚𝑖𝑛
𝑖
𝐹𝑖1
𝑚𝑖𝑛
𝑖
𝐹𝑖1
= 1 
Next, under 𝑗= 1, let us compare A1’s normalized value (𝐹11) over A3’s normalized value 
(𝐹31), and perform logarithmic transformation: 
𝑎13 =
𝑙𝑛(𝐹11
𝐹31) −𝑙𝑛(𝑟𝑚𝑖𝑛,1)
𝑙𝑛(𝑟𝑚𝑎𝑥,1) −𝑙𝑛(𝑟𝑚𝑖𝑛,1) × (9 −1) + 1 
=
𝑙𝑛(
1
0.8280) −𝑙𝑛(1)
𝑙𝑛(1.8235) −𝑙𝑛(1) × (9 −1) + 1 
= 3.5140 
Symmetrically, we can obtain that 𝑎31 =
1
𝑎13 =
1
3.5140 = 0.2846.  
Likewise, the complete pairwise comparisons for all 4 alternatives under C1 are computed 
and presented in the first 5 columns of Table 8.7. The last column of Table 8.7 displays the 
calculated local priority scores (𝑣𝑖1) for alternatives under C1, solved using the eigenvalue 
method described in Step 2. Additionally, the consistency ratio, 𝐶𝑅 is computed as 0.0427 
(within acceptable threshold), obtained using the equation in Step 3. 
Table 8.7: Pairwise comparison matrix for alternatives under C1. 
 
A1 
A2 
A3 
A4 
Local priority 
score (𝑣𝑖1) 
A1 
1 
9.0000 
3.5140 
2.6762 
0.5296 
A2 
0.1111 
1 
0.1542 
0.1365 
0.0388 
A3 
0.2846 
6.4860 
1 
0.5441 
0.1741 
A4 
0.3737 
7.3238 
1.8378 
1 
0.2575 
Preliminary Draft Manuscript 
 
8-15 
 
 
For the remaining criteria (C2 and C3), similar calculations are performed to construct the 
pairwise comparison matrices for alternatives under each of them and compute the 
corresponding local priority scores (𝑣𝑖2 and 𝑣𝑖3) for alternatives, as presented in Table 8.8 
and Table 8.9, respectively; the CR values are found to be 0.0677 and 0.0389, respectively, 
both within the acceptable threshold. 
Table 8.8: Pairwise comparison matrix for alternatives under C2. 
 
A1 
A2 
A3 
A4 
Local priority 
score (𝑣𝑖2) 
A1 
1 
0.3121 
3.6051 
6.7958 
0.2675 
A2 
3.2042 
1 
5.8093 
9.0000 
0.5831 
A3 
0.2774 
0.1721 
1 
4.1907 
0.1086 
A4 
0.1471 
0.1111 
0.2386 
1 
0.0409 
 
Table 8.9: Pairwise comparison matrix for alternatives under C3. 
 
A1 
A2 
A3 
A4 
Local priority 
score (𝑣𝑖3) 
A1 
1 
0.3245 
0.1171 
0.1111 
0.0407 
A2 
3.0812 
1 
0.1548 
0.1445 
0.0825 
A3 
8.5392 
6.4580 
1 
0.6846 
0.3908 
A4 
9.0000 
6.9188 
1.4608 
1 
0.4859 
 
Step 5. Aggregate the local priority scores using the criteria weights calculated in Step 2, to 
determine the global priority scores (𝑃𝑖) for alternatives, as follows: 
𝑃𝑖= ∑𝑤𝑗
𝑛
𝑗=1
𝑣𝑖𝑗,  𝑖∈{1,2, . . . , 𝑚} 
(8.16)  
The alternatives are ranked based on the 𝑃𝑖 values, where the alternative with the highest 𝑃𝑖 
value is top-ranked. 
Numerical Calculations: 
For instance, for 𝑖= 1 and using the criteria weights computed in Step 2: 
𝑃1 = ∑𝑤𝑗
3
𝑗=1
𝑣1𝑗= 0.6267 × 0.5296 + 0.2797 × 0.2675 + 0.09 × 0.0936 = 0.4105 
Preliminary Draft Manuscript 
 
8-16 
 
Similarly, the performance scores for all alternatives are calculated as 𝑃1 = 0.4105, 𝑃2 =
0.1951, 𝑃3 = 0.1761, 𝑃4 = 0.2183. Accordingly, the ranking is A1 ≻ A4 ≻ A2 ≻ A3, with A1 
being the top-ranked alternative by AHP. 
 
Alternatively, we can utilize SuperDecisions, a specialized software that has AHP and Analytic 
Network Process (ANP) implemented, to assist us in solving the foregoing numerical example. 
SuperDecisions (downloadable from https://superdecisions.com/) is a free educational 
software developed by the team of the creator of the methods, Professor Thomas Saaty. To 
begin, we construct the AHP model with the 3 hierarchical levels (namely, L1-Goal, L2-Criteria, 
and L3-Alternatives) within the interface of the software, as illustrated in Figure 8.2(a). Next, 
we input the pairwise comparison matrix for the 3 criteria (from the Numerical Calculations 
part of Step 1) and the pairwise comparison matrices for the 4 alternatives under each of the 
3 criteria (from the first 5 columns of Table 8.7, 8.8, and 8.9) into SuperDecisions.  
The software then calculates the criteria weights and the local priorities of alternatives under 
each criterion. These results, highlighted in the red boxes of Figure 8.2(b), match the values 
we previously computed manually. Readers can ignore all the other values reported in Figure 
8.2(b) for now; they will understand their meanings in the subsequent ANP section. Finally, 
SuperDecisions determines the global priority scores of the alternatives, presented in Figure 
8.2(c), which also align with our previous calculations. The original SuperDecisions file for this 
AHP model can be downloaded from our shared folder in Google Drive:  
https://drive.google.com/drive/folders/18ynIwnKaCRsptwBCrMIFVOlV9Mu_A7qM?usp=shari
ng 
Preliminary Draft Manuscript 
 
8-17 
 
 
Figure 8.2(a): AHP representation in SuperDecisions software 
 
 
Figure 8.2(b): Criteria weights and local priorities of alternatives for each criterion inside red 
boxes; a screenshot from SuperDecisions for AHP. 
Preliminary Draft Manuscript 
 
8-18 
 
 
 
Figure 8.2(c): Global priorities of alternatives; a screenshot from SuperDecisions for AHP. 
Additional Comment: If an ACM based on objective measurement data is available (e.g., 
Table 8.1), apart from what Step 4 describes for mapping objective data into Saaty’s 1–9 scale 
either through subjectively assessing the ACM or mathematical transformation, another 
straightforward approach is to directly utilize the ACM as is and adopt a hybrid approach 
combining AHP with other MCDM methods (e.g., SAW, MEW) for ranking alternatives. In this 
hybrid approach, AHP is used only to determine criteria weights subjectively, while the 
objective ACM provides the evaluation data for alternatives, which are then ranked using the 
MCDM method (e.g., SAW, MEW). This approach, also commonly adopted in the literature 
(Zaidan et al., 2015; Suartini et al., 2023), bypasses the need for mapping onto Saaty’s 1–9 
scale and leverages objective quantitative values directly. 
The advantages of AHP are as follows. (1) It provides a systematic approach to decompose 
complex decision problems into hierarchical levels, beginning from the overall goal, moving 
down to criteria, and finally to the alternatives. (2) The use of pairwise comparisons allows 
subjective and qualitative judgments to be included explicitly in the decision-making process 
while preserving a measure of logical consistency through the consistency ratio. (3) By 
breaking down the comparisons at each hierarchical level, AHP helps the decision-maker 
focus on smaller, more manageable pairs, which can reduce cognitive overload compared to 
simultaneously considering all criteria and alternatives. (3) Due to its intuitive nature and well-
established methodology, AHP is widely adopted and/or hybridized with other methods across 
a broad range of decision-making contexts, including engineering design, project selection, 
policymaking, and resource allocation, among others. 
The limitations of AHP are as follows. (1) It heavily depends on the subjective judgments of 
decision-makers, which can introduce biases or inconsistencies, especially when dealing with 
large comparison matrices. (2) The use of Saaty’s 1–9 scale, while straightforward, can reduce 
fidelity for nuanced differences, mapping a more granular measurement scale onto these 
discrete intervals may oversimplify actual distinctions among criteria or alternatives. (3) Rank 
reversal (a common limitation of many MCDM methods) can occur if new alternatives are 
Preliminary Draft Manuscript 
 
8-19 
 
added or existing ones are removed, since this can alter the relative priorities derived from the 
pairwise comparison matrices of alternatives. (4) As the number of criteria and alternatives 
grows, the required pairwise comparisons increase exponentially, resulting in greater 
computational effort and higher cognitive demand on the part of decision-makers. 
8.5
