---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-010-24-the-euler-maclaurin-formula
section_title: "The Euler-Maclaurin Formula"
section_number: 2.4
pages: 34-36
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.977
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
The Euler-Maclaurin formula is a formula which enables us to make a connection between a sum and its corresponding integral, provided the function is sufficiently smooth. Before we can state the formula, we need a few preliminary definitions and notation. Let $\lfloor x\rfloor$ denote the greatest integer function, so that $\lfloor x\rfloor$ returns the greatest integer less than or equal to $x$. For $s=1,2,\dots$, let $B_s(x)$ denote the Bernoulli polynomials. The generating function for the Bernoulli polynomials is as follows: $$\frac{te^{xt}}{e^t-1}=\sum_{s=0}^{\infty} B_s(x)\frac{t^s}{s!}$$ For $s\geq 1$, we will let $B_s:=B_s(0)$. These $B_s$ are called the Bernoulli numbers. The first few Bernouli numbers are given by $B_1 = -1⁄2,\; B_2 = 1⁄6,\; B_3 = 0 ,\; B_4 = −1⁄30, \;B_5 = 0\;, B_6 = 1⁄42$. See [@AndrewsAskeyRoy] for more details and alternative definitions. We now have everything that we need to state the Euler-Maclaurin formula.

::: thm
Suppose $f$ has continuous derivatives up to order $s$. Then $$\begin{gathered}
\sum_{m+1}^n f(x)=\int_m^n f(x) dx+\sum_{i=1}^s(-1)^i\frac{B_i}{i!}(f^{(i-1)}(n)-f^{(i-1)}(m)) \\ +\frac{(-1)^{i-1}}{i!}\int_m^n B_s(x-\lfloor x\rfloor)f^{(i)}(x) dx
\end{gathered}$$
:::

Notice that this formula allows a sum to be estimated by its corresponding integral (or an integral by its sum), and gives an exact formula for the error in using this estimation. In many applications, this error term can at least be bounded, if not computed exactly. The proof of the formula involves successively performing integration by parts, which gives a sequence of periodic functions relating to the Bernoulli polynomials. For a proof, see [@AndrewsAskeyRoy]. We will use a similar method of proof to prove a $q$-deformed version of Stirling's formula in a later section.

# Random Operator Compressions
