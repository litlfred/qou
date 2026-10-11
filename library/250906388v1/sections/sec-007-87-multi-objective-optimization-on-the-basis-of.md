---
doc_id: 250906388v1
doc_title: "Preliminary Draft Manuscript Chapter 8"
section_id: sec-007-87-multi-objective-optimization-on-the-basis-of
section_title: "Multi-Objective Optimization on the basis of Ratio Analysis (MOORA)"
section_number: 8.7
pages: 29-31
source_pdf: 2509.06388v1.pdf
source_sha256: 48123c8812890b17
toc_source: inferred
doc_brief: "Preliminary Draft Manuscript Chapter 8 — This chapter describes selected aggregation-type multi-criteria decision-making (MCDM) methods that convert an alternatives-criteria matrix (ACM) into a"
---
The MOORA method, introduced by Brauers and Zavadskas (2006), is extensively applied in 
various fields for MCDM. After constructing the weighted normalized ACM, the performance 
score for each alternative is calculated by subtracting the aggregate of minimization criteria 
values from the aggregate of maximization criteria values. The alternative that has a larger 
Preliminary Draft Manuscript 
 
8-30 
 
performance score is ranked higher. The MOORA method follows a structured sequence of 
the following steps. 
Step 1. Normalize the original ACM with 𝑚 rows (i.e., alternatives) and 𝑛 columns (i.e., 
criteria) by Vector normalization method. 
𝐹𝑖𝑗=
𝑓𝑖𝑗
√∑
𝑓𝑘𝑗
2
𝑚
𝑘=1
 
(8.23) 
Numerical Calculations (using ACM from Table 8.1): 
For instance, for 𝑖= 1 and 𝑗= 2: 
𝐹12 =
𝑓12
√∑
𝑓𝑘2
2
𝑚
𝑘=1
=
600
√6002 + 7002 + 5002 + 4002 = 0.5345 
Similar calculations are performed for all other values in the ACM across the 4 alternatives 
and 3 criteria. The complete results, forming the normalized ACM, are shown in Table 8.15. 
Table 8.15: Normalized ACM for MOORA walkthrough. 
Alternatives 
C1 
C2 
C3 
A1 
0.6015 
0.5345 
0.7321 
A2 
0.3299 
0.6236 
0.5617 
A3 
0.4980 
0.4454 
0.2804 
A4 
0.5304 
0.3563 
0.2644 
 
Step 2. Construct the weighted normalized ACM by multiplying the values of each criterion 
with its assigned weight, 𝑤𝑗. 
𝑣𝑖𝑗= 𝐹𝑖𝑗× 𝑤𝑗 
(8.24)  
Numerical Calculations: 
For instance, for 𝑖= 1 and 𝑗= 2: 
𝑣12 = 𝐹12 × 𝑤2 = 0.5345 × 0.33 = 0.1764 
Likewise, calculations are carried out for all other values in the normalized ACM, using their 
respective assigned weights. The results, which constitute the weighted normalized ACM, 
are displayed in Table 8.16. 
Table 8.16: Weighted normalized ACM for MOORA walkthrough. 
Alternatives 
C1 
C2 
C3 
A1 
0.1504 
0.1764 
0.3075 
Preliminary Draft Manuscript 
 
8-31 
 
A2 
0.0825 
0.2058 
0.2359 
A3 
0.1245 
0.1470 
0.1178 
A4 
0.1326 
0.1176 
0.1111 
 
Step 3. Compute the performance score (𝑃𝑖) of each alternative as follows. 
𝑃𝑖= ∑
𝑣𝑖𝑗
𝑔
𝑗=1
−∑
𝑣𝑖𝑗
𝑛
𝑗=𝑔+1
 
(8.25)  
Here, significance of 𝑔 is the same as that in COPRAS method, meaning that 𝑔 is the number 
of maximization criteria, which can be arranged in the first 𝑔 columns of the weighted 
normalized ACM. The minimization criteria are in columns 𝑔+ 1 to 𝑛.  The alternative with the 
largest 𝑃𝑖 is top-ranked and recommended to the decision-maker. The performance score in 
Eq. 8.25 is somewhat simpler than that in COPRAS method (Eq. 8.22). 
Numerical Calculations: 
There are 2 maximization criteria, hence 𝑔= 2. For instance, for 𝑖= 1: 
𝑃1 = ∑
𝑣1𝑗
2
𝑗=1
−∑
𝑣1𝑗
3
𝑗=2+1
= 0.1504 + 0.1764 −0.3075 = 0.0193 
Similarly, the performance scores for all alternatives are calculated as 𝑃1 = 0.0193, 𝑃2 =
0.0523, 𝑃3 = 0.1537, 𝑃4 = 0.1391. Accordingly, the ranking is A3 ≻ A4 ≻ A2 ≻ A1, with A3 
being the top-ranked alternative by MOORA. Note that some or all 𝑃𝑖 can be negative (e.g., 
if all/majority of criteria are minimization type). 
 
The advantages of MOORA are as follows. (1) It employs a straightforward mathematical 
formulation where the performance of each alternative is determined by summing weighted 
benefit criteria and then subtracting weighted cost criteria, making it easy to interpret. (2) The 
steps are relatively simple, which allows for efficient implementation across a wide variety of 
decision-making contexts. 
The limitations of MOORA are as follows. (1) Similar to COPRAS, a single high or low value 
in one criterion can disproportionately influence the final performance score, which may be 
undesirable for decisions requiring a balanced performance across all criteria. (2) As with other 
MCDM methods, the addition or removal of alternatives may cause rank reversal. 
8.8
