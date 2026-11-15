---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-009-34-length-spectrum-of-the-fricke-macbeath-surfac
section_title: "Length spectrum of the Fricke-Macbeath surface"
section_number: 3.4
pages: 19-21
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.989
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
In Vogeler's study [@Vogeler2003], an in-depth analysis of closed geodesics on Hurwitz surfaces is presented, with a special focus on the length spectrum of Hurwitz surfaces of low genera. Of particular relevance to us, Vogeler offers an exhaustive table [@Vogeler2003 Table C.2] enumerating the short primitive closed geodesics on the Fricke-Macbeath surface, along with their corresponding lengths and multiplicities. This table comprehensively covers geodesics with lengths below 14.49 [@Vogeler2003 p. 57]. For those interested on understanding the method used, refer to [@Vogeler2003 Section 2.3].

In order to compute the multiplicity of $\la_1$ for the Fricke-Macbeath surface using the Selberg trace formula, we need the conjugacy classes of the two shortest lengths as input data. The shortest classes have an approximate length of $5.796298891$, while the next shortest classes are about $8.303943294$ in length.

To employ interval arithmetic in the trace formula, we need a precise error bound for these lengths. To convert an entry from [@Vogeler2003 Table C.2] into a conjugacy class of $\Gamma$, one can follow these steps:

-   A proper label for a geodesic is a sequence consisting of the letters $R$ and $L$. The sequence begins with either one or two $R$'s, followed by one or two $L$'s, and continues in this alternating pattern. Further details can be found in [@Vogeler2003 p. 19].

-   This proper label can be converted into a code. A code in the table is a sequence of 1's and 2's. Each number in this sequence denotes the count of consecutive $R$'s or $L$'s. As an illustration, the code $(1 1 2 2)$ translates to the proper label $RLRRLL$. This encoding is described in [@Vogeler2003 p. 23].

-   Now, one should substitute the letter $R$ with the expression $a^{-1}b$ and the letter $L$ with $b$. This transformation yields a word consisting of $a$ and $b$. The process is explained in [@Vogeler2003 p. 32].

-   Lastly, with the aid of [\[eq:matrixA\]](#eq:matrixA){reference-type="eqref" reference="eq:matrixA"} and [\[eq:matrixB\]](#eq:matrixB){reference-type="eqref" reference="eq:matrixB"}, an exact matrix representation can be obtained for this word in $a$ and $b$.

Consider the first entry with code $(1222)$ and $n=2$ in [@Vogeler2003 Table C.2]. The code $(1222)$ which translates to the proper label $(RLLRRLL)$, and since $n = 2$, this label repeats twice: $$(RLLRRLL)(RLLRRLL).$$ The geodesic with this label corresponds to the conjugacy class of $\Gamma$ containing $$\begin{aligned}
\gamma
&= (a^{-1}b^3a^{-1}ba^{-1}b^3)(a^{-1}b^3a^{-1}ba^{-1}b^3) \\
&= \gamma_{15} \text{, as checked in } \eqref{eq:gamma15}.
\end{aligned}$$ Let $z_0$ be half the trace of $\gamma$, whose minimal polynomial is $1-x-9 x^2+x^3$. We can easily check that $$z_0 \in (9.09783467903, 9.09783467905).$$ The length of $\gamma$ is $\ell(\gamma) = 2 \arccosh(z_0) = 5.796298891\dots$. This length is significant as it represents the shortest geodesic length on the Fricke-Macbeath surface $\X$. This shortest geodesic length, also termed the *systole* and denoted by $\sys(\X)$, is defined as: $$\sys(\X) = \min \{ \ell(\gamma) : \{\gamma\} \in \calC(\Gamma) \}.$$

Similarly, the geodesic labeled by the code $(11111112)$ with $n=2$ corresponds to a conjugacy class with length $2 \arccosh(z_1) = 8.303943294\dots$ with $z_1$ having minimal polynomial $-1-25 x-31 x^2+x^3$. We can easily check that $$z_1 \in (31.78746324455, 31.78746324457).$$

Finally, note that the multiplicity of a geodesic listed in Vogeler's table should be doubled when we are counting the number of corresponding conjugacy classes. This adjustment is necessary because the table enumerates unoriented geodesics; see [@Vogeler2003 Definition 9].

The preceding discussion can be summarized in the following proposition:

::: prop
[]{#prop:shortgeo label="prop:shortgeo"} Let $z_0$ and $z_1$ be the above algebraic numbers. The conjugacy classes with the minimum length in $\calC(\Gamma)$ has length $2\arccosh(z_0)$, and there are 252 classes. There are 504 conjugacy classes that are the second shortest, each with a length $2\arccosh(z_1)$.
:::

The precise intervals within which $z_0$ and $z_1$ lie, as well as the above multiplicities play a crucial role in the computations utilizing the Selberg trace formula with interval arithmetic.
