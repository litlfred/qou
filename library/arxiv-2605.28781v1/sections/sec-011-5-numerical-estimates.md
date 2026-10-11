---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-011-5-numerical-estimates
section_title: "Numerical estimates"
section_number: 5
pages: 11-12
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.895
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
[]{#sec-numerical label="sec-numerical"} We have not tried to keep track of explicit constants in the proofs above, since these would obscure the main ideas of the proof, and the calculations become quite messy. In this section we sketch what a quantified version of the construction would give, yielding in particular $c\geq 0.00000087$. We have not made any attempt to change the structure of the argument, even slightly, to optimize the constants. Doing so would likely yield a better value, although we expect a $c$ obtained by any variant of this kind of argument to be very small.

An earlier version of our argument constructed a field with small split primes, as in the disproof of the unit distance conjecture described in [@ABGLSSTWW2026UnitDistance], and considered elements divisible only by these ideals instead of units. To our surprise, the existence of small split primes turned out to be completely unnecessary, resulting in the simplified version presented here, but it is likely that an optimized version would include these primes.

We first state variants of our lemmas with all the different constants appearing named, and then give explicit values for these constants, before stating a version of the main result for these constants, and then finally giving an explicit value for the main result.

1.  In Lemma [\[lem-regbound\]](#lem-regbound){reference-type="ref" reference="lem-regbound"} we have $$R_K \leq c_1^{-d}\Delta_K.$$

2.  In Theorem [\[th-tower\]](#th-tower){reference-type="ref" reference="th-tower"} we have $\Delta_K\leq C_2^d$.

3.  In Lemma [\[lem-ball\]](#lem-ball){reference-type="ref" reference="lem-ball"} $$X^d\Delta_K^{-1/2}\leq \lvert B^+(X)\rvert\leq (2X+1)^d.$$

4.  In Lemma [\[lem-unitsep\]](#lem-unitsep){reference-type="ref" reference="lem-unitsep"} $u\in \{\pm 1\}$ whenever $\lvert \sigma_i(u)\rvert\in [\tfrac{1}{1+c_3},1+c_3]$.

5.  In Lemma [\[lem-ball-mult\]](#lem-ball-mult){reference-type="ref" reference="lem-ball-mult"} $$(1-o(1))^dY^{d-1}R_K^{-1}\leq \lvert B^\times(Y)\rvert\leq 10(C_4Y+1)^{d-1}.$$

For example, following the proofs given above we can take $$c_1\geq 3.819,\quad C_2\leq 857.57, \quad c_3\geq 0.618,\quad\textrm{and}\quad C_4\leq 4.16.$$ The values of most of the constants here are immediate from the proofs presented above. The constant $C_2$ is sometimes called Martinet's constant (see [@HaMa01]). Hajir, Maire, and Ramakrishna [@hajir2021shafarevich §3.3.3] proved that we can take $C_2 \leq 857.57$.

For the rest of this sketch we will use the notation $\lesssim$ and $\gtrsim$ to hide losses of $(1+o(1))^d$ (which are inconsequential since we can take $d$ arbitrarily large). In general, our construction leads to $$(c_1/C_2)^dY^{d}\lesssim\mathopen{}\left| G\mathclose{}\right|\leq \mathopen{}\left| GG\mathclose{}\right|\lesssim(2C_4Y+1)^{d}$$ and, with $\epsilon= \tfrac{c_3}{2+c_3}$ (which is permissible provided $X$ is an integer), $$\mathopen{}\left| P\mathclose{}\right|\gtrsim(\epsilon C_2^{-1/2})^dX^d.$$ By discarding elements of $P$ and $G$ if necessary, we can assume that the lower bounds on $\mathopen{}\left| G\mathclose{}\right|$ and $\mathopen{}\left| P\mathclose{}\right|$ are attained, and $$(c_1\epsilon C_2^{-3/2})^d(XY)^d\lesssim\mathopen{}\left| A\mathclose{}\right|.$$ Now $$\mathopen{}\left| AA\mathclose{}\right|\lesssim\mathopen{}\left( \frac{C_2^2(2C_4Y+1)}{c_1^2Y^2} \mathclose{}\right)^d\mathopen{}\left| A\mathclose{}\right|^2$$ and $$\begin{align*}
\mathopen{}\left| A+A\mathclose{}\right|
&\lesssim(4(1+\epsilon)Xe^Y+1)^d\\
&\lesssim\mathopen{}\left( \frac{(4(1+\epsilon)Xe^Y+1)C_2^3}{c_1^2\epsilon^2X^2Y^2} \mathclose{}\right)^d\mathopen{}\left| A\mathclose{}\right|^2.
\end{align*}$$ For example, with the constant choices above we have $$\mathopen{}\left| AA\mathclose{}\right|\lesssim\mathopen{}\left( \frac{419531}{Y}+\frac{50425}{Y^2} \mathclose{}\right)^d\mathopen{}\left| A\mathclose{}\right|^2$$ and $$\mathopen{}\left| A+A\mathclose{}\right|\lesssim\mathopen{}\left( \frac{3836812879}{XY^2}e^Y+\frac{776017933}{X^2Y^2} \mathclose{}\right)^d\mathopen{}\left| A\mathclose{}\right|^2,$$ while $$\mathopen{}\left| A\mathclose{}\right|\gtrsim(0.000035XY)^d.$$ A rough approximation to the optimal choice is to take $X=\lfloor e^{1140402}\rfloor$ and $Y=1140402$, which leads to arbitrarily large $A\subset \mathbb{R}$ with $$\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\leq \mathopen{}\left| A\mathclose{}\right|^{2-0.00000087}.$$
