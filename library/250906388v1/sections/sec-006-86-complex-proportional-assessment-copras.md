---
doc_id: 250906388v1
doc_title: "Preliminary Draft Manuscript Chapter 8"
section_id: sec-006-86-complex-proportional-assessment-copras
section_title: "Complex Proportional Assessment (COPRAS)"
section_number: 8.6
pages: 26-29
source_pdf: 2509.06388v1.pdf
source_sha256: 48123c8812890b17
toc_source: inferred
doc_brief: "Preliminary Draft Manuscript Chapter 8 — This chapter describes selected aggregation-type multi-criteria decision-making (MCDM) methods that convert an alternatives-criteria matrix (ACM) into a"
---
The COPRAS method, proposed by Zavadskas et al. (1994), is another aggregation-type 
MCDM method. It employs a systematic approach to rank alternatives based on their relative 
importance. After constructing the weighted normalized ACM, COPRAS calculates the sum of 
weighted normalized values for all maximization criteria and the sum of weighted normalized 
Preliminary Draft Manuscript 
 
8-27 
 
values for all minimization criteria, for each alternative. These two sums are then aggregated 
using the method’s specific equations (Zavadskas et al., 1994) to determine each alternative’s 
performance score. The alternative with the highest performance score is top-ranked. 
Step 1. Normalize the original ACM with m rows (i.e., alternatives) and n columns (i.e., criteria) 
using Sum normalization method. 
𝐹𝑖𝑗=
𝑓𝑖𝑗
∑
𝑓𝑘𝑗
𝑚
𝑘=1
 
(8.18)  
Numerical Calculations (using ACM from Table 8.1): 
For instance, for 𝑖= 1 and 𝑗= 2: 
𝐹12 =
𝑓12
∑
𝑓𝑘2
𝑚
𝑘=1
=
600
600 + 700 + 500 + 400 = 0.2727 
Similar calculations are performed for all other values in the ACM across the 4 alternatives 
and 3 criteria. The complete results, forming the normalized ACM, are shown in Table 8.12. 
Table 8.12: Normalized ACM for COPRAS walkthrough. 
Alternatives 
C1 
C2 
C3 
A1 
0.3069 
0.2727 
0.3982 
A2 
0.1683 
0.3182 
0.3055 
A3 
0.2541 
0.2273 
0.1525 
A4 
0.2706 
0.1818 
0.1438 
 
Step 2. Construct the weighted normalized ACM by multiplying the values of each criterion 
with its assigned weight, 𝑤𝑗. 
𝑣𝑖𝑗= 𝐹𝑖𝑗× 𝑤𝑗 
(8.19)  
Numerical Calculations: 
For instance, for 𝑖= 1 and 𝑗= 2: 
𝑣12 = 𝐹12 × 𝑤2 = 0.2727 × 0.33 = 0.0900 
Likewise, calculations are carried out for all other values in the normalized ACM, using their 
respective assigned weights. The results, which constitute the weighted normalized ACM, 
are displayed in Table 8.13. 
Table 8.13: Weighted normalized ACM for COPRAS walkthrough. 
Alternatives 
C1 
C2 
C3 
A1 
0.0767 
0.0900 
0.1672 
Preliminary Draft Manuscript 
 
8-28 
 
A2 
0.0421 
0.1050 
0.1283 
A3 
0.0635 
0.0750 
0.0641 
A4 
0.0677 
0.0600 
0.0604 
 
Step 3. For each alternative, calculate the sums of weighted normalized values for both 
maximization and minimization criteria, 𝑆𝑖+ and 𝑆𝑖−, separately. 
𝑆𝑖+ = ∑𝑣𝑖𝑗
𝑔
𝑗=1
 
(8.20)  
𝑆𝑖−= ∑𝑣𝑖𝑗
𝑛
𝑗=𝑔+1
 
(8.21) 
Here, 𝑔 is the number of maximization criteria, which can be arranged in the first 𝑔 columns 
of the weighted normalized ACM. The minimization criteria are in columns 𝑔+ 1 to 𝑛. If all 
criteria are for maximization, then 𝑔= 𝑛; whereas 𝑔= 0 when all criteria are for minimization. 
Numerical Calculations: 
There are 2 maximization criteria, hence 𝑔= 2.  
For instance, for 𝑖= 1: 
𝑆1+ = ∑𝑣1𝑗
2
𝑗=1
= 𝑣11 + 𝑣12 = 0.0767 + 0.0900 = 0.1667 
𝑆1−= ∑𝑣1𝑗
3
𝑗=2+1
= 𝑣13 = 0.1672 
After calculating the 𝑆𝑖+ and 𝑆𝑖− of each alternative, the results are tabulated in the first 3 
columns of Table 8.14. 
Table 8.14: Weighted normalized ACM for COPRAS walkthrough. 
Alternatives 
𝑆𝑖+ 
𝑆𝑖− 
𝑃𝑖 
A1 
0.1667 
0.1672 
0.2214 
A2 
0.1471 
0.1283 
0.2183 
A3 
0.1385 
0.0641 
0.2813 
A4 
0.1277 
0.0604 
0.2790 
 
Step 4. Compute the performance score (𝑃𝑖) of each alternative as follows. 
Preliminary Draft Manuscript 
 
8-29 
 
𝑃𝑖=
{
  
 
  
 𝑆𝑖+ +
∑
𝑆𝑘−
𝑚
𝑘=1
𝑆𝑖−∑
1
𝑆𝑘−
𝑚
𝑘=1
,
if both maximization and minimization criteria exist
𝑆𝑖+,
if only maximization criteria exist
∑
𝑆𝑘−
𝑚
𝑘=1
𝑆𝑖−∑
1
𝑆𝑘−
𝑚
𝑘=1
,
if only minimization criteria exist
 
(8.22)  
In the above equation, both ∑
𝑆𝑘−
𝑚
𝑘=1
 and ∑
1
𝑆𝑘−
𝑚
𝑘=1
 are invariant across the performance score 
(𝑃𝑖) calculations for each alternative 𝑖, and so the term 
∑
𝑆𝑘−
𝑚
𝑘=1
𝑆𝑖−∑
1
𝑆𝑘−
𝑚
𝑘=1
 can be considered as a 
scaled 𝑆𝑖− value. Further, a smaller 𝑆𝑖− leads to a higher 𝑃𝑖 value. The alternative with the 
largest 𝑃𝑖 is top-ranked and recommended to the decision-maker. 
Numerical Calculations: 
For instance, for 𝑖= 1, since both maximization and minimization criteria exist: 
𝑃1 = 𝑆1+ +
∑
𝑆𝑘−
𝑚
𝑘=1
𝑆1−∑
1
𝑆𝑘−
𝑚
𝑘=1
= 0.1667 +
0.1672 + 0.1283 + 0.0641 + 0.0604
0.1672 (
1
0.1672 +
1
0.1283 +
1
0.0641 +
1
0.0604)
= 0.2214 
Similarly, performance scores for all alternatives are calculated and given in the last column 
of Table 8.14. Accordingly, the ranking is A3 ≻ A4 ≻ A1 ≻ A2, with A3 being the top-ranked 
alternative by COPRAS. 
 
The advantages of COPRAS are as follows. (1) COPRAS explicitly separates benefit (to be 
maximized) and cost (to be minimized) criteria, making it intuitive for decision-makers to see 
how each criterion contributes to or detracts from the final performance score of an alternative. 
(2) COPRAS has been successfully adopted in many applications (Stefano et al., 2015). 
The limitations of COPRAS are as follows. (1) Because the final performance score is largely 
driven by the sum of weighted normalized values, exceptionally high (or low) performance on 
one criterion may greatly overshadow moderate performance on other criteria, which may not 
be desirable in some applications. (2) As with other MCDM methods, the addition or removal 
of alternatives may cause rank reversal. 
8.7
