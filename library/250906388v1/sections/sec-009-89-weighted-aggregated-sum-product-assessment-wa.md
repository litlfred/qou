---
doc_id: 250906388v1
doc_title: "Preliminary Draft Manuscript Chapter 8"
section_id: sec-009-89-weighted-aggregated-sum-product-assessment-wa
section_title: "Weighted Aggregated Sum Product Assessment (WASPAS)"
section_number: 8.9
pages: 33-34
source_pdf: 2509.06388v1.pdf
source_sha256: 48123c8812890b17
toc_source: inferred
doc_brief: "Preliminary Draft Manuscript Chapter 8 — This chapter describes selected aggregation-type multi-criteria decision-making (MCDM) methods that convert an alternatives-criteria matrix (ACM) into a"
---
The WASPAS method, introduced in Zavadskas et al. (2012), is a hybrid MCDM approach 
that combines both the SAW and MEW methods in its algorithm. It calculates a composite 
performance score for each alternative by blending the additive results from SAW with the 
multiplicative results from MEW. By integrating these two different perspectives, WASPAS 
aims to leverage the strengths of each method while mitigating their individual shortcomings. 
The procedure of the WASPAS method consists of the following steps. 
Step 1. Normalize the original ACM with 𝑚 rows (i.e., alternatives) and 𝑛 columns (i.e., 
criteria) by using Max normalization. This step is the same as the Step 1 of the SAW and 
MEWS methods (Sections 8.2 and 8.3). For the sake of brevity, the normalization equations 
and numerical calculations (same as Table 8.2) are not repeated here. 
Preliminary Draft Manuscript 
 
8-34 
 
Step 2. Calculate the performance score (𝑃𝑖) for each alternative by integrating additive (as in 
the SAW method) and multiplicative (as in the MEW method) components, as follows. The 
alternative with the largest 𝑃𝑖 is top-ranked and recommended to the decision-maker. 
𝑃𝑖= 𝜆∑𝐹𝑖𝑗𝑤𝑗
𝑛
𝑗=1
+ (1 −𝜆) ∏𝐹𝑖𝑗
𝑤𝑗
𝑛
𝑗=1
 
(8.27) 
Here, 𝜆∈[0, 1] is a parameter that balances between the additive and multiplicative 
components. When 𝜆= 1, WASPAS reduces to a purely additive approach (i.e., SAW). When 
𝜆= 0, it simplifies to a fully multiplicative approach (i.e., MEW). Intermediate 𝜆 values allow a 
flexible combination of both approaches. Commonly, 𝜆= 0.5 is chosen to give equal priority 
to both SAW and MEW components. 
Numerical Calculations: 
For instance, for 𝑖= 1 and 𝜆= 0.5, using the normalized criteria values in Table 8.2: 
𝑃1 = 0.5 ∑𝐹1𝑗𝑤𝑗
3
𝑗=1
+ 0.5 ∏𝐹1𝑗
𝑤𝑗
3
𝑗=1
 
= 0.5(1 × 0.25 + 0.8571 × 0.33 + 0.3612 × 0.42) + 0.5(10.25 × 0.85710.33 × 0.36120.42) 
= 0.6521 
Similarly, the performance scores for all alternatives are calculated as 𝑃1 = 0.6521, 𝑃2 =
0.6460, 𝑃3 = 0.8358, 𝑃4 = 0.8173. Accordingly, the ranking is A3 ≻ A4 ≻ A1 ≻ A2, with A3 
being the top-ranked alternative by WASPAS. 
 
The advantages of WASPAS are as follows. (1) It involves straightforward calculations, 
making it easy to implement and computationally efficient. (2) By integrating SAW and MEW, 
WASPAS takes advantage of each method’s strengths: the SAW part helps maintain clarity 
and proportional scaling, while the MEW part ensures no single criterion is completely 
overshadowed by extremely high values in others.  
The limitations of WASPAS are as follows. (1) The final ranking can be affected by the choice 
of 𝜆 value, which itself becomes an additional decision-making challenge. (2) If a criterion 
value is zero or extremely small for an alternative, the multiplicative component can 
excessively penalize it. (3) Similar to other MCDM methods, the addition or removal of 
alternatives can affect rankings, potentially leading to rank reversals.
