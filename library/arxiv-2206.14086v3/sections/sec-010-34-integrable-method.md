---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-010-34-integrable-method
section_title: "Integrable method"
section_number: 3.4
pages: 6-7
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 1.0
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
[]{#sec:integrablemethod label="sec:integrablemethod"}

The above theorems were obtained by explicitly computing the finite-time distribution function and then taking the large limit of the formula. In particular, for the TASEP, the finite-time formula is given by the Fredholm determinant of an operator. After suitable scaling and conjugation, the operator converges to the so-called Airy operator, the Fredholm determinant of which is the Tracy-Widom distribution.

Johansson obtained the finite-time distribution formula for TASEP using a combinatorial interpretation similar to the longest increasing subsequence problem and connecting to the so-called Schur measure [@Okounkov01]. The Schur measure on integer partitions is defined in terms of the Schur function and contains many parameters. The one-point distribution of the TASEP arises by taking a special limit of the parameters.

A different proof computes the transition probabilities of the TASEP explicitly and then takes an appropriate sum over the configuration space to obtain the finite-time distribution.

To find the transition probabilities, we solve the Kolmogorov forward equation, which is a linear differential equation with non-constant coefficients due to the exclusion property of the particles. This equation was solved explicitly in [@Schutz97] by applying the coordinate Bethe ansatz method from mathematical physics [@Gaudin14; @Sutherland04], which consists of changing the Kolmogorov equation to a linear differential equation with constant coefficients (the free evolution equation) but with complicated boundary conditions. Taking the sum of transition probabilities over particular configurations is more technical, and this part was done in [@Nagao-Sasamoto04; @Rakos-Schutz05] to re-derive the result of Johansson.

Both methods, which are algebraic and exact, are significantly extended to prove a one-point KPZ limit theorem for many other models. The following is the list of some of such integrable (exactly solvable) models. Of course, the list and references are far from exhaustive.

-   Interacting particle systems: PushASEP, ASEP, $q$-TASEP, $q$-Hahn ASEP [@Borodin-Ferrari08; @Tracy-Widom09; @Borodin-Ferrari14; @Barraquand-Corwin16].

-   Random growth models: KPZ equation, stochastic heat equation [@Amir-Corwin-Quastel11; @Borodin-Corwin-Ferrari-Veto15].

-   DLPP and directed polymers: O'Connell--Yor semi-discrete polymer, log Gamma polymer [@{O'Connell12}; @Borodin-Corwin-Remenik13; @Borodin-Corwin-Ferrari14].

The underlying algebraic structures of these integrable models are generalized greatly by Macdonald processes [@Borodin-Corwin13] and the stochastic six vertex model [@Borodin-Corwin-Gorin16; @Corwin-Petrov16]. They are umbrella models with many parameters whose specializations produce the above models. Though many, these integrable models are still isolated examples. For instance, DLPP with general random variables, other than exponential and geometric random variables, does not seem to be integrable.

See Section [\[sec:univ\]](#sec:univ){reference-type="ref" reference="sec:univ"} for some comments for non-integrable models.
