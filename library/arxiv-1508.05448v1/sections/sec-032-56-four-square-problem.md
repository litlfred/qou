---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-032-56-four-square-problem
section_title: "Four Square Problem"
section_number: 5.6
pages: 115-122
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.984
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
We would now like to give an idea as to how the $q$-Stirling's formula arises in the problem of bounding the fluctuations of the length of the longest increasing subsequence in a Mallows random permutation. This work is ongoing, but an important step is discussed in this section. A random permutation (Mallows or otherwise), can be viewed as a set of points in a rectangle, in the following way:

Consider $n$ points $(x_i, y_i)$ in the rectangle $[0,1]\times [0,1]$ in $\mathbb{R}^2$ with all coordinates distinct. The set of points specifies a permutation $\pi\in S_n$ by the rule: \"The point with the $i$th smallest $y$ coordinate has the $\pi(i)$th smallest $x$-coordinate\". Hence, given a set of points in a box, we can obtain a permutation from these points. Depending on how the points are distributed in the box, we can obtain permutations with different distributions. As an example, if the points are uniformly distributed in the box, we obtain a uniform random permutation.

To begin to bound the fluctuation of a Mallows random permutation, we assume that we have $n$ points in the unit square distributed so that they give a Mallows random permutation. We then divide the square into a large number of small subsquares. If the size of each subsquare is small enough, the points in the subsquare will be approximately uniformly distributed. We then hope to couple our model to a model of Deuschel and Zeitouni [@DZ] to bound the fluctuations.

<figure id="fig:FourSquare">
<div class="center">
<p><span class="math display">$$\begin{tikzpicture}
\draw
(-2,-2)--(-2,2)--(2,2)--(2,-2)--(-2,-2);
\draw
(0,-2)--(0,2);
\draw
(-2,0)--(2,0); 
\node at (-1,-1) {$R_{11}$};
\node at (-1,1) {$R_{21}$};
\node at (1,-1) {$R_{12}$};
\node at (1,1) {$R_{22}$};
\end{tikzpicture}$$</span></p>
</div>
<figcaption>An example of a decomposition of <span class="math inline">[0,1]<sup>2</sup></span> into four rectangles <span class="math inline"><em>R</em><sub>11</sub>, <em>R</em><sub>12</sub>, <em>R</em><sub>21</sub>, <em>R</em><sub>22</sub></span>.</figcaption>
</figure>

This argument will not be presented here. For now, we will simply look at the division of the unit square into four subrectangles to illustrate the use of the $q$-Stirling's formula. Suppose that we divide the unit square into four rectanges, which we refer to as $R_{11}, \; R_{12},\; R_{21},\;  R_{22}$. See figure [1](#fig:FourSquare){reference-type="ref" reference="fig:FourSquare"}. Assuming that we have $n$ total points in the square, let $n_{11}$ denote the number of points in $R_{11}$, $n_{12}$ denote the number of points in $R_{12}$, and so on. We then have $n_{11}+n_{12}+n_{21}+n_{22}=n$. Denote the area of rectange $R_{ij}$ as $p_{ij}$. Consider the distribution of the points $(x_1,y_1), (x_2,y_2),\dots, (x_n, y_n)$ in the square. If the points are distributed uniformly (i.e. if $q=1$), then the probability of the event $$\cap_{i,j=1}^n \{\# \{k:(X_k,Y_k)\in R_{ij}=n_{ij}\}\}$$ is given by the usual multinomial formula $$\label{com1}
\frac{n!}{n_{11}!n_{12}!n_{21}!n_{22}!} p_{11}^{n_{11}}p_{12}^{n_{12}}p_{21}^{n_{21}}p_{22}^{n_{22}}$$ For $0<q<1$ and $q\not = 1$ (in other words, a Mallows random permutation), the correct probability is obtained by multiplying the above expression by the factor $$\label{com2}
q^{n_{12} n_{21}}\,
\frac{[n_{11}+n_{12}]![n_{11}+n_{21}]![n_{12}+n_{22}]![n_{21}+n_{22}]!}
{(n_{11}+n_{12})!(n_{11}+n_{21})!(n_{12}+n_{22})!(n_{21}+n_{22})!}
\cdot \frac{(n_{11})!(n_{12})!(n_{21})!(n_{22})!}{[n_{11}]![n_{12}]![n_{21}]![n_{22}]!}
\cdot \frac{n!}{[n]!}\, .$$ where $[a]!$ denotes the $q$ factorial as defined earlier. Combining [\[com1\]](#com1){reference-type="ref" reference="com1"} and [\[com2\]](#com2){reference-type="ref" reference="com2"} and using the notation $\{n\}!:=[n]!/n!$, we have $$\begin{gathered}
\label{4square}
\mathbb{P}\left(\cap_{i,j=1}^n \{\# \{k:(X_k,Y_k)\in R_{ij}=n_{ij}\}\right)= \\
\frac{n!}{\prod_{i,j=1}^2 (n_{ij})!}\left(\prod_{i,j=1}^2 p_{ij}^{n_{ij}}\right) \, 
\frac{\{n_{11}+n_{12}\}!\{n_{11}+n_{21}\}!\{n_{12}+n_{22}\}!\{n_{21}+n_{22}\}!}
{\{n_{11}\}!\{n_{12}\}!\{n_{21}\}!\{n_{22}\}!\{n_{11}+n_{12}+n_{21}+n_{22}\}!}\,q^{n_{21}n_{12}} 
\end{gathered}$$ This formula is somewhat involved, but it is explicit. By applying the $q$-Stirling's formula, we can obtain the exact asymptotics for the probability distribution in the limit $n\rightarrow\infty$, with $q=e^{-\beta/n}$.

Recall that Stirling's formula says that $$n!\sim e^{n\ln n-n}\sqrt{2\pi n}$$ and the $q$-Stirling's formula states that for $q=e^{-\beta/n}$, $$\ln\left(\frac{[n]!}{n!}\right)=nA(\beta)+B(\beta)+R_n(\beta)$$ where $$A(\beta)=\int_0^1\ln\left(\frac{1-e^{-\beta x}}{\beta x}\right) dx$$ $$B(\beta)=\frac{\beta}{2}+\frac{1}{2}\ln\left(\frac{1-e^{-\beta x}}{\beta x}\right)$$ and $R_n(\beta)$ is a remainder term which goes to zero as $n\rightarrow\infty$. Before we can apply these asymptotics to equation [\[4square\]](#4square){reference-type="ref" reference="4square"}, we need a preliminary lemma.

::: lem
For $q=e^{-\beta/n}$, $$\ln(\{n_{ij}\}!)=n_{ij} A\left(\frac{n_{ij}}{n}\, \beta\right) + B\left(\frac{n_{ij}}{n}\, \beta\right) + R_{n_{ij}}\left(\frac{n_{ij}}{n}\, \beta\right)\,$$
:::

This lemma is easily proved using the $q$-Stirling's formula and rewriting $q$ as $q=e^{-\beta '/n_{ij}}$, where $\beta '=\frac{n_{ij}\beta}{n}$.

To break down the asymptotics of [\[4square\]](#4square){reference-type="ref" reference="4square"} a bit, let $$W_q = \frac{\{n_{11}+n_{12}\}!\{n_{11}+n_{21}\}!\{n_{12}+n_{22}\}!\{n_{21}+n_{22}\}!}
{\{n_{11}\}!\{n_{12}\}!\{n_{21}\}!\{n_{22}\}!\{n_{11}+n_{12}+n_{21}+n_{22}\}!}\,q^{n_{21}n_{12}}$$ In addition, let $\nu_{ij}=\frac{n_{ij}}{n}$. For this analysis, we will assume that all $\nu_{ij}$ are order $1$, so that we are not letting any of the squares be too small. If this is the case, we can make the approximation $$\ln\{n_{ij}\}!\approx n\nu_{ij}A(\beta v_{ij})$$ Using this assumption, we have the following lemma

::: lem
For $\nu_{11}, \nu_{12}, \nu_{21}, \nu_{22}>0$, we have $$\begin{gathered}
\lim_{n\rightarrow\infty} \frac{1}{n}\ln(W_q)= -\beta \nu_{12} \nu_{21} + (\nu_{11}+\nu_{12}) A(\beta[\nu_{11}+\nu_{12}]) 
+ (\nu_{11}+\nu_{21}) A(\beta[\nu_{11}+\nu_{21}])\\
\qquad + (\nu_{12}+\nu_{22}) A(\beta[\nu_{12}+\nu_{22}])
+ (\nu_{21}+\nu_{22}) A(\beta[\nu_{21}+\nu_{22}])\\
\qquad - \nu_{11} A(\beta \nu_{11})
- \nu_{12} A(\beta \nu_{12})
- \nu_{21} A(\beta \nu_{21})
- \nu_{22} A(\beta \nu_{22})
- A(\beta)
\end{gathered}$$
:::

::: proof
*Proof.* By definition, $$\lim_{n\rightarrow\infty}\frac{1}{n}\ln(W_q)$$ $$=\lim_{n\rightarrow\infty} \frac{1}{n}\ln\left(q^{\nu_{12}n\nu_{21}n}\frac{\{\nu_{11}n+\nu_{12}n\}!\{\nu_{11}n+\nu_{21}n\}!\{\nu_{12}n+\nu_{22}n\}!\{\nu_{21}n+\nu_{22}n\}!}{\{\nu_{11}n\}!\{\nu_{12}n\}!\{\nu_{21}n\}!\{\nu_{22}\}!\{\nu_{11}n+\nu_{12}n+\nu_{21}n+\nu_{22}n\}!}\right)$$ Using the $q$-Stirling formula and the previous lemma, we get $$\begin{gathered}
=\lim_{n\rightarrow\infty}\frac{1}{n}( \ln\left(q^{\nu_{12}n\nu_{21}n}
\right)+ (\nu_{11}n+\nu_{12}n)A(\beta(\nu_{11}+\nu_{12}))+\dots + (\nu_{21}n+\nu_{22}n)A(\beta(\nu_{21}+\nu_{22})) \\
-\nu_{11}nA(\beta\nu_{11})-\nu_{12}nA(\beta\nu_{12})-\nu_{21}nA(\beta nu_{21})-\nu_{22}nA(\beta \nu_{22}) \\
-(\nu_{11}n+\nu_{12}n+\nu_{21}n+\nu_{22}n)A(\beta(\nu_{11}+\nu_{12}+\nu_{21}+\nu_{22})) )
\end{gathered}$$ Distributing the $n$ and taking the limit immediately gives us what we need except for the first and last terms. Consider just $$\lim_{n\rightarrow\infty}\ln(q^{\nu_{12}n\nu_{21}n})$$ Since $q=e^{-\beta/n}$, this is $$=\lim_{n\rightarrow\infty}\frac{1}{n}e^{-\beta(\nu_{12}n\nu_{21})}$$ $$=\frac{1}{n}(-\beta\nu_{12}n\nu_{21})=-\beta\nu_{12}\nu_{21}$$ This gives us the first term in our lemma. The last term is equal to $$\lim_{n\rightarrow\infty}\frac{1}{n}(\nu_{11}n+\nu_{12}n+\nu_{21}n+\nu_{22}n)A(\beta(\nu_{11}+\nu_{12}+\nu_{21}+\nu_{22}))$$ $$=\lim_{n\rightarrow\infty}(\nu_{11}+\nu_{12}+\nu_{21}+\nu_{22})A(\beta(\nu_{11}+\nu_{12}+\nu_{21}+\nu_{22}))$$ $$=A(\beta)$$ since $\sum_{i,j=1}^2\nu_{ij}=1$. Putting all terms together proves the lemma. ◻
:::

It is worth noting that the asymptotics for $$\frac{1}{n}\ln W_q$$ given by this lemma give us an equation analogous (and very similar) to equation (6) in [@starrWal].

Combining these asymptotics with the asymptotics for $$\frac{n!}{\prod_{i,j=1}^2 (n_{ij})!}\left(\prod_{i,j=1}^2 p_{ij}^{n_{ij}}\right)$$ gives $$\mathbb{P}\left(\cap_{i,j=1}^n \{\# \{k:(X_k,Y_k)\in R_{ij}=n_{ij}\}\right)=\frac{\sqrt{2\pi n}}{\prod_{i,j=1}^2 \sqrt{2\pi n_{ij}}}e^{\tilde{A}}$$ where $$\begin{gathered}
\tilde{A}=n(\ln(n)-\sum_{i,j=1}^n\nu_{ij}\ln(n_{ij}) \\ -\beta \nu_{12} \nu_{21} + (\nu_{11}+\nu_{12}) A(\beta[\nu_{11}+\nu_{12}]) 
+ (\nu_{11}+\nu_{21}) A(\beta[\nu_{11}+\nu_{21}])\\
\qquad + (\nu_{12}+\nu_{22}) A(\beta[\nu_{12}+\nu_{22}])
+ (\nu_{21}+\nu_{22}) A(\beta[\nu_{21}+\nu_{22}])\\
\qquad - \nu_{11} A(\beta \nu_{11})
- \nu_{12} A(\beta \nu_{12})
- \nu_{21} A(\beta \nu_{21})
- \nu_{22} A(\beta \nu_{22})
\end{gathered}$$
