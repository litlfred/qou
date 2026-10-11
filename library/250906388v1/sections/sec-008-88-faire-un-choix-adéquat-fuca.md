---
doc_id: 250906388v1
doc_title: "Preliminary Draft Manuscript Chapter 8"
section_id: sec-008-88-faire-un-choix-adéquat-fuca
section_title: "Faire Un Choix Adéquat (FUCA)"
section_number: 8.8
pages: 31-33
source_pdf: 2509.06388v1.pdf
source_sha256: 48123c8812890b17
toc_source: inferred
doc_brief: "Preliminary Draft Manuscript Chapter 8 — This chapter describes selected aggregation-type multi-criteria decision-making (MCDM) methods that convert an alternatives-criteria matrix (ACM) into a"
---
FUCA is the French acronym for "Faire Un Choix Adéquat", which translates to "Make an 
Adequate Choice". The FUCA method, proposed by Fernando et al. (2011), determines the 
Preliminary Draft Manuscript 
 
8-32 
 
best alternative based on rank aggregation. It works by assigning ranks to alternatives with 
respect to each criterion and then computing a weighted sum of these ranks. The alternative 
with the smallest aggregated rank is top-ranked and recommended to the decision-maker 
(Wang & Rangaiah, 2017). Thus, no normalization of criteria values is required. 
Step 1. Rank the alternatives for each criterion. Each alternative is assigned a rank with 
respect to every criterion, denoted as 𝑟𝑖𝑗, based on its performance under that criterion, as 
follows: 
• 
Rank 1 is assigned to the best alternative. 
• 
Rank 2 is assigned to the next best alternative. 
• 
…. 
• 
Rank 𝑚 (where 𝑚 is the number of alternatives) is assigned to the worst alternative.  
The ranking assignment depends on whether the criterion is of a benefit or cost type. For 
benefit criteria (maximization), the best alternative is the one with the highest value, receiving 
rank 1, while the worst receives rank 𝑚. Conversely, for cost criteria (minimization), the best 
alternative is the one with the lowest value, receiving rank 1, while the worst receives rank 𝑚. 
Numerical Calculations (using ACM from Table 8.1): 
For instance, for 𝑖= 2 and 𝑗= 1, by inspecting Table 8.1, we can easily find the rank of A2 
under C1 is: 𝑟21 = 4. Similar rankings are performed for all other values in the ACM across 
the 4 alternatives and 3 criteria. The complete results are shown in Table 8.17. 
Table 8.17: Rank of alternatives under each criterion for FUCA walkthrough. 
Alternatives 
C1 
C2 
C3 
A1 
1 
2 
4 
A2 
4 
1 
3 
A3 
3 
3 
2 
A4 
2 
4 
1 
 
Step 2. Compute the aggregated ranks. Once the rankings under each criterion are assigned, 
a weighted rank summation of all criteria (𝑅𝑖) is performed for each alternative. 
𝑅𝑖= ∑(𝑟𝑖𝑗× 𝑤𝑗)
𝑛
𝑗=1
 
(8.26)  
The alternative with the smallest 𝑅𝑖 is top-ranked and recommended to the decision-maker. 
Preliminary Draft Manuscript 
 
8-33 
 
Numerical Calculations: 
For instance, for 𝑖= 4: 
𝑅4 = ∑(𝑟4𝑗× 𝑤𝑗)
3
𝑗=1
= 2 × 0.25 + 4 × 0.33 + 1 × 0.42 = 2.24 
Similarly, the aggregated ranks for all alternatives are calculated as 𝑅1 = 2.59, 𝑅2 = 2.59, 
𝑅3 = 2.58, 𝑃4 = 2.24. Accordingly, the ranking is A4 ≻ A3 ≻ A1 = A2, with A4 being the top-
ranked alternative by FUCA. Note that 𝑅𝑖 can have the same value for 2 or more 
alternatives. 
 
The advantages of FUCA are as follows. (1) It is easy to understand and implement, requiring 
only ranking assignments and simple weighted summation calculations. (2) Since FUCA ranks 
alternatives directly instead of normalizing numerical values for each criterion, it eliminates the 
dependence of ranking on the normalization method. This helps avoid issues such as possibly 
drastic changes in normalized values when ACM is updated. (3) FUCA is less sensitive to 
extreme values as it considers only rankings and not absolute magnitudes. 
The limitations of FUCA are as follows. (1) Since FUCA relies solely on ranks, it does not 
account for the actual differences between alternative performances. A small difference in 
criteria values may be treated the same as a large difference (i.e., in terms of ranking 
difference). (2) In cases where multiple alternatives have the same criterion value, additional 
tie-breaking rules must be defined, which can introduce subjectivity. (3) FUCA is still 
susceptible to rank reversal when new alternatives are introduced or existing ones are 
removed, as the reassignment of ranks for each criterion may alter the relative positioning of 
alternatives. 
8.9
