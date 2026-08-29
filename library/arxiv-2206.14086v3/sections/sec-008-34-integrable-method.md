---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-008-34-integrable-method
section_title: "Integrable method"
section_number: 3.4
pages: 6-7
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
The above theorems were obtained by explicitly computing the ﬁnite-time distribution function and then
taking the large limit of the formula. In particular, for the TASEP, the ﬁnite-time formula is given by the
Fredholm determinant of an operator. After suitable scaling and conjugation, the operator converges to the
so-called Airy operator, the Fredholm determinant of which is the Tracy-Widom distribution.
Johansson obtained the ﬁnite-time distribution formula for TASEP using a combinatorial interpretation
similar to the longest increasing subsequence problem and connecting to the so-called Schur measure [69]. The
Schur measure on integer partitions is deﬁned in terms of the Schur function and contains many parameters.
The one-point distribution of the TASEP arises by taking a special limit of the parameters.
A diﬀerent proof computes the transition probabilities of the TASEP explicitly and then takes an ap-
propriate sum over the conﬁguration space to obtain the ﬁnite-time distribution. To ﬁnd the transition
probabilities, we solve the Kolmogorov forward equation, which is a linear diﬀerential equation with non-
constant coeﬃcients due to the exclusion property of the particles.
This equation was solved explicitly
in [80] by applying the coordinate Bethe ansatz method from mathematical physics [46,84], which consists
of changing the Kolmogorov equation to a linear diﬀerential equation with constant coeﬃcients (the free
evolution equation) but with complicated boundary conditions. Taking the sum of transition probabilities
over particular conﬁgurations is more technical, and this part was done in [67,75] to re-derive the result of
Johansson.
Both methods, which are algebraic and exact, are signiﬁcantly extended to prove a one-point KPZ limit
theorem for many other models. The following is the list of some of such integrable (exactly solvable) models.
Of course, the list and references are far from exhaustive.
6
• Interacting particle systems: PushASEP, ASEP, q-TASEP, q-Hahn ASEP [18,27,28,88].
• Random growth models: KPZ equation, stochastic heat equation [4,24].
• DLPP and directed polymers: O’Connell–Yor semi-discrete polymer, log Gamma polymer [23,26,68].
The underlying algebraic structures of these integrable models are generalized greatly by Macdonald
processes [22] and the stochastic six vertex model [25,35]. They are umbrella models with many parameters
whose specializations produce the above models. Though many, these integrable models are still isolated
examples. For instance, DLPP with general random variables, other than exponential and geometric random
variables, does not seem to be integrable. See Section 9 for some comments for non-integrable models.
4
