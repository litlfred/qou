---
doc_id: 250906388v1
doc_title: "Preliminary Draft Manuscript Chapter 8"
section_id: sec-002-82-simple-additive-weighting-saw
section_title: "Simple Additive Weighting (SAW)"
section_number: 8.2
pages: 2-5
source_pdf: 2509.06388v1.pdf
source_sha256: 48123c8812890b17
toc_source: inferred
doc_brief: "Preliminary Draft Manuscript Chapter 8 — This chapter describes selected aggregation-type multi-criteria decision-making (MCDM) methods that convert an alternatives-criteria matrix (ACM) into a"
---
Section 8.3 
Multiplicative Exponent Weighting (MEW) 
Section 8.4 
Analytic Hierarchy Process (AHP) 
Section 8.5 
Analytic Network Process (ANP) 
Section 8.6 
Complex Proportional Assessment (COPRAS) 
Section 8.7 
Multi-Objective Optimization on the basis of Ratio Analysis (MOORA) 
Section 8.8 
Faire Un Choix Adéquat (FUCA) 
Section 8.9 
Weighted Aggregated Sum Product Assessment (WASPAS) 
Section 8.10 Summary 
Our Microsoft Excel based program, EMCDM, described in Chapter 10, includes SAW, 
COPRAS, MOORA, and FUCA methods. 
The learning outcomes of this chapter are: (1) Describe the principles and algorithms of 
aggregation-type MCDM methods covered; (2) Apply any of these methods to ACM of an 
application; and (3) Select one or more aggregation-type MCDM methods for solving MCDM 
problems. 
Unless otherwise stated, the notation used throughout this chapter are as follows: 
• 
𝑖∈{1,2, … , 𝑚} and 𝑗∈{1,2, … , 𝑛}, where 𝑚 is the number of rows (i.e., alternatives) 
and 𝑛 is the number of columns (i.e., criteria) in the ACM.  
• 
𝑓𝑖𝑗 is the value of the 𝑗𝑡ℎ criterion for the 𝑖𝑡ℎ alternative in the original ACM. 
• 
𝐹𝑖𝑗 is the normalized value of 𝑓𝑖𝑗. 
• 
𝑤𝑗 is the weight assigned to the 𝑗𝑡ℎ criterion, and ∑
𝑤𝑗
𝑛
𝑗=1
= 1. 
• 
𝑣𝑖𝑗 is the value of the 𝑗𝑡ℎ criterion for the 𝑖𝑡ℎ alternative in the weighted normalized 
ACM. 
Additionally, the ACM presented in Table 8.1 is employed to walk through the steps of the 
aggregation-type MCDM methods covered in this chapter. This ACM is made up of 4 
Preliminary Draft Manuscript 
 
8-3 
 
alternatives (i.e., 𝑚= 4 and 𝑖∈{1, 2, 3, 4}) and 3 criteria (i.e., 𝑛= 3 and 𝑗∈{1, 2, 3}). Out of 
the 3 criteria (C1, C2, and C3), C1 and C2 are benefit criteria to be maximized, while C3 is a 
cost criterion to be minimized. For illustration, the 3 criteria are assigned weights as: 𝑤1 = 0.25, 
𝑤2 = 0.33, and 𝑤3 = 0.42. All the 4 alternatives (A1, A2, A3, and A4) are non-dominated, 
which means that the improvement in one criterion will inevitably result in degradation in at 
least one other criterion (Wang et al., 2023). 
Table 8.1: ACM employed for illustration of aggregation-type MCDM methods (C1 and C2 for 
maximization; C3 for minimization). 
Alternatives 
C1 (Max) 
C2 (Max) 
C3 (Min) 
A1 
0.93 
600 
8.25 
A2 
0.51 
700 
6.33 
A3 
0.77 
500 
3.16 
A4 
0.82 
400 
2.98 
Weight 
0.25 
0.33 
0.42 
 
8.2 
Simple Additive Weighting (SAW) 
The SAW method, also known as the weighted sum method (WSM), described in 
MacCrimmon (1968), is one of the most fundamental and simple methods in MCDM. It is 
based on the principle that the top-ranked alternative is the one with the highest weighted sum 
of normalized criteria values (Nabavi et al., 2023), after converting minimization or cost criteria 
into maximization or benefit type. The method assumes that the criteria are compensatory, 
which means that a lower score in one criterion can be offset by a higher score in another. 
The steps in SAW are as follows. 
Step 1. Normalize the original ACM with 𝑚 rows (i.e., alternatives) and 𝑛 columns (i.e., 
criteria) by using the Max normalization method. For a maximization criterion, the normalized 
value, 𝐹𝑖𝑗 is obtained as: 
𝐹𝑖𝑗=
𝑓𝑖𝑗
𝑚𝑎𝑥
𝑘∈{1,2,...,𝑚}𝑓𝑘𝑗
 
(8.1)  
For a minimization criterion, the normalized value, 𝐹𝑖𝑗 is obtained as: 
𝐹𝑖𝑗=
𝑚𝑖𝑛
𝑘∈{1,2,...,𝑚}𝑓𝑘𝑗
𝑓𝑖𝑗
 
(8.2)  
The above normalization ensures that all minimization criteria are converted to maximization 
type, indicating that a higher 𝐹𝑖𝑗 always indicates a better performance (Nabavi et al., 2024). 
Preliminary Draft Manuscript 
 
8-4 
 
Numerical Calculations (using ACM from Table 8.1): 
For instance, for 𝑖= 1 and 𝑗= 2: 
𝐹12 = 600
700 = 0.8571 
Similar calculations are performed for all other values in the ACM across the 4 alternatives 
and 3 criteria. The complete results, forming the normalized ACM, are shown in Table 8.2. 
Table 8.2: Normalized ACM for SAW walkthrough. 
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
 
Step 2. Construct the weighted normalized ACM by multiplying each normalized criterion 
value by its corresponding weight 𝑤𝑗.  
𝑣𝑖𝑗= 𝐹𝑖𝑗× 𝑤𝑗 
(8.3)  
Numerical Calculations: 
For instance, for 𝑖= 1 and 𝑗= 2: 
𝑣12 = 𝐹12 × 𝑤2 = 0.8571 × 0.33 = 0.2829 
Likewise, calculations are carried out for all other values in the normalized ACM, using their 
respective assigned weights. The results, which constitute the weighted normalized ACM, 
are displayed in Table 8.3. 
Table 8.3: Weighted normalized ACM for SAW walkthrough. 
Alternatives 
C1 
C2 
C3 
A1 
0.2500 
0.2829 
0.1517 
A2 
0.1371 
0.3300 
0.1977 
A3 
0.2070 
0.2357 
0.3961 
A4 
0.2204 
0.1886 
0.4200 
 
Step 3. Compute the performance score (𝑃𝑖) for each alternative, which is obtained by 
summing its weighted normalized values. 
Preliminary Draft Manuscript 
 
8-5 
 
𝑃𝑖= ∑𝑣𝑖𝑗
𝑛
𝑗=1
 
(8.4)  
Finally, the alternatives are ranked in descending order of 𝑃𝑖, with the highest value indicating 
the top-ranked alternative and recommended to the decision-maker. 
Numerical Calculations: 
For instance, for 𝑖= 1: 
𝑃1 = ∑𝑣1𝑗
3
𝑗=1
= 0.2500 + 0.2829 + 0.1517 = 0.6846 
Similarly, the performance scores of all alternatives are calculated as 𝑃1 = 0.6846, 𝑃2 =
0.6648, 𝑃3 = 0.8388, and 𝑃4 = 0.8290. Accordingly, the ranking is A3 ≻ A4 ≻ A1 ≻ A2, with 
A3 being the top-ranked alternative by SAW. 
 
The advantages of SAW are as follows. (1) It is one of the simplest MCDM methods, requiring 
only the sum of the normalized weighted criteria values, which makes it very straightforward 
to understand and implement (Wang et al., 2022). (2) Its computational procedure is relatively 
transparent, allowing decision-makers to easily observe how each criterion and weight 
contributes to the overall score. (3) Due to its simplicity, it can be readily applied in many fields, 
such as engineering, project selection, and resource allocation, where a quick ranking of 
alternatives is needed.  
The limitations of SAW are as follows. (1) Similar to other MCDM methods, rank reversal can 
occur if new alternatives are added or existing ones are removed, potentially affecting the 
stability of the ranking results. (2) It treats all performance values additively; high performance 
on one criterion is possible to completely compensate for low performance on another, which 
might be undesirable in certain decision-making scenarios. 
8.3
