---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-006-25-example-of-calculation
section_title: "Example of calculation"
section_number: 2.5
pages: 10-16
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.961
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
[]{#subsec:calculation label="subsec:calculation"}

Put $\beta:=\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$. Its closure $E$ is a knot called the figure-eight knot (Figure [\[fig:braid_presentation\]](#fig:braid_presentation){reference-type="ref" reference="fig:braid_presentation"}). We will calculate $J_N(E;q)$.

Instead of calculating $\operatorname{Tr}_1(\operatorname{Tr}_2(\operatorname{Tr}_3(\Phi(\beta)\mu^{\otimes3})))\in\mathbb{C}$, we will calculate $\operatorname{Tr}_2(\operatorname{Tr}_3(\Phi(\beta)(\operatorname{Id}\otimes\mu\otimes\mu)))\in\operatorname{End}(V)$, which is a scalar multiple by Schur's lemma (for a proof see [@Kirby/Melvin:INVEM1991 Lemma 3.9]). See Figure [1](#fig:tangle){reference-type="ref" reference="fig:tangle"}.

<figure id="fig:tangle">
<p><embed src="tangle_small.eps" /> <embed src="tangle_R_small.eps" /></p>
<figcaption>We close all the strings except for the first one.</figcaption>
</figure>

Then $\operatorname{Tr}_1(\operatorname{Tr}_2(\operatorname{Tr}_3(\Phi(\beta)\mu^{\otimes3})))$ coincides with the trace of $\mu$ times the scalar $S$. Since $$\begin{split}
  T_{(R,\mu,q^{(N^2-1)/4},1)}(\beta)
  &=
  q^{-w(\beta)(N^2-1)/4}\operatorname{Tr}_1(\operatorname{Tr}_2(\operatorname{Tr}_3(\Phi(\beta)\mu^{\otimes3})))
  \\
  &=
  q^{-w(\beta)(N^2-1)/4}\operatorname{Tr}_1(S\operatorname{Id}_V)
  \\
  &=
  q^{-w(\beta)(N^2-1)/4}\sum_{i=0}^{N-1}S\, q^{(2i-N+1)/2}
  \\
  &=
  q^{-w(\beta)(N^2-1)/4}\frac{\{N\}}{\{1\}}S,
\end{split}$$ we have $J_N(L;q)=q^{-w(\beta)(N^2-1)/4}S=S$.

We need an explicit formula for the inverse of the $R$-matrix, which is given by $$\label{eq:R_inverse}
\begin{split}
  (R^{-1})^{ij}_{kl}
  =&
  \sum_{m=0}^{\min(N-1-i,j)}
  \delta_{l,i-m}\delta_{k,j+m}
  \frac{\{k\}!\{N-1-l\}!}{\{j\}!\{m\}!\{N-1-i\}!}
  \\
  &\times
  (-1)^{m}q^{-\bigl(i-(N-1)/2\bigr)\bigl(j-(N-1)/2\bigr)-m(i-j)/2+m(m+1)/4}.
\end{split}$$

To calculate the scalar $S$, draw a diagram for the braid $\beta$ and close it except for the first string (Figure [2](#fig:R0){reference-type="ref" reference="fig:R0"}).

![Draw the braid $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ and close it except for the left-most one.](fig8_R0_small.eps){#fig:R0}

Fix a basis $\{e_0,e_1,\dots,e_{N-1}\}$ of $\mathbb{C}^N$.

Label each arc with a non-negative integer $i$ less than $N$, which corresponds to a basis element $e_i$, where our braid diagram is divided into arcs by crossings so that at each crossing four arcs meet. Since the homomorphism $\operatorname{Tr}_2(\operatorname{Tr}_1(\Phi(\beta)\otimes2))$ is a scalar multiple, we choose any basis for the first (top-left) arc of Figure [2](#fig:R0){reference-type="ref" reference="fig:R0"} and calculate the scalar. For simplicity we choose $e_{N-1}$ and so we label the first arc with $N-1$ (Figure [3](#fig:R1){reference-type="ref" reference="fig:R1"}).

![Label the first (top-left) arc with $N-1$.](fig8_R1_small.eps){#fig:R1}

Recall that we will associate the $R$-matrix or its inverse with each crossing as follows.

::: center
$\Rightarrow$ $R^{ij}_{kl}$  , $\Rightarrow$ $(R^{-1})^{ij}_{kl}$
:::

Therefore we will label the other arcs following the following two rules:

1.  At a positive crossing, the top-left label is less than or equal to the bottom-right label, the top-right label is greater than or equal to the bottom-left label, and their differences coincide (see [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"}).

    ::: center
    $: i+j=k+l$, $l\ge i$, $k\le j$,
    :::

2.  At a negative crossing, the top-left label is greater than or equal to the bottm-right label, the top-right label is less than or equal to the bottm-left label, and their differences coincide (see [\[eq:R_inverse\]](#eq:R_inverse){reference-type="eqref" reference="eq:R_inverse"}).

    ::: center
    $: i+j=k+l$, $l\le i$, $k\ge j$.
    :::

From Rule (i), the next arc should be labeled with $N-1$, and the difference at the top crossing is $0$ (Figure [4](#fig:R2){reference-type="ref" reference="fig:R2"}). This is why we chose $N-1$ for the label of the first arc.

![The label of the next arc should be $N-1$, and the difference at the top crossing is $0$](fig8_R2_small.eps){#fig:R2}

Label the top-right arc with $i$ with $0\le i\le N-1$ (Figure [5](#fig:R3){reference-type="ref" reference="fig:R3"}).

![Label the top-right arc with $i$ ($0\le i\le N-1$).](fig8_R3_small.eps){#fig:R3}

The label of the left-middle arc should be $i$ since the difference at the top crossing is $0$.

![The label of the left-middle arc should be $i$ since the difference at the top crossing is $0$.](fig8_R4_small.eps){#fig:R4}

Label the arcs indicated in Figure [7](#fig:R6){reference-type="ref" reference="fig:R6"} with $j$ and $k$ with $0\le j\le N-1$ and $0\le k\le N-1$. Then the difference at the second top crossing is $N-k-1$. Therefore the arc between the second top crossing and the second bottom crossing should be labeled with $N-k+j-1$ from Rule (ii) (Figure [8](#fig:R7){reference-type="ref" reference="fig:R7"}). Since the label should be less than $N$, we have $j-k\le0$.

![Choose $j$ and $k$. Then the difference at the second top crossing is $N-k-1$.](fig8_R6_small.eps){#fig:R6}

![The label of the arc between the second top arc and the second bottom arc should be $N-k+j-1$. Note that $j-k\le0$.](fig8_R7_small.eps){#fig:R7}

Look at the bottom-most crossing and apply Rule (ii). We see that $i\ge k$ and the difference at the bottom-most crossing is $i-k$. So the label of the arc between the second bottom crossing and the bottom-most crossing is $i+j-k$ (Figure [9](#fig:R8){reference-type="ref" reference="fig:R8"}). We also see that the label of the bottom-most arc is $N-1$ as we expected.

![The label of the arc between the second bottom crossing and the bottom-most crossing should be $i+j-k$. Note that $j-k\ge0$](fig8_R8_small.eps){#fig:R8}

However from Rule (i) we have $j-k\ge0$ and so $k=j$. Therefore we finally have the labeling as indicated in Figure [10](#fig:R9){reference-type="ref" reference="fig:R9"}.

![The label $k$ should coincide with $i$.](fig8_R9_small.eps){#fig:R9}

Now we can calculate the colored Jones polynomial. We have $$\begin{split}
  J_N(E;q)
  &=
  \sum_{i\ge j}
  R^{N-1,i}_{i,N-1}\,
  (R^{-1})^{N-1,j}_{N-1,j}\,
  R^{i,N-1}_{N-1,i}\,
  (R^  {-1})^{i,j}_{i,j}\,
  \mu^{j}_{j}\,
  \mu^{i}_{i}
  \\
  &=
  \sum_{i\ge j}
  (-1)^{N-1+i}
  \frac{\{N-1\}!\{i\}!\{N-1-j\}!}{(\{j\}!)^2\{i-j\}!\{N-1-i\}!}
  \\
  &\phantom{=\sum_{i\ge j}}\times q^{(-i-i^2-2ij-2j^2+3N+6Ni+2Nj-3N^2)/4}.
\end{split}$$

In this formula we need two summations. To get a formula involving only one summation we regard the figure-eight knot $E$ as the closure of a tangle as shown in Figure [11](#fig:fig8_calc){reference-type="ref" reference="fig:fig8_calc"}.

![The figure-eight knot can also regarded as the closure of a $(1,1)$-tangle.](fig8_calc_small.eps){#fig:fig8_calc}

In this case we need to put $\mu$ at each local minimum where the arc goes from left to right, and $\mu^{-1}$ at each local maximum where the arc goes from right to left. See [@Kirby/Melvin:INVEM1991 Theorem 3.6] for details.

From Figure [1](#fig:tangle){reference-type="ref" reference="fig:tangle"}, we have $$\begin{split}
  &J_N(E;q)
  \\
  =&
  \sum_{\stackrel{0\le i\le N-1,0\le j\le N-1}{0\le i+j\le N-1}}
  R^{i,0}_{0,i}\,
  (R^{-1})^{i,j}_{i+j,0}\,
  R^{0,i+j}_{i,j}\,
  (R^  {-1})^{j,0}_{0,j}\,
  (\mu^{-1})^{i}_{i}\,
  \mu^{j}_{j}
  \\
  =&
  \sum_{\stackrel{0\le i\le N-1,0\le j\le N-1}{0\le i+j\le N-1}}
  (-1)^i
  \frac{\{i+j\}!\{N-1\}!}{\{i\}!\{j\}!\{N-1-i-j\}!}
  q^{-(N-1)i/2+(N-1)j/2-i^2/4+j^2/4-3i/4+3j/4}.
\end{split}$$ Putting $k:=i+j$, we have $$J_N(E;q)
  =
  \sum_{k=0}^{N-1}
  \frac{\{N-1\}!}{\{N-1-k\}!}q^{k^2/4+Nk/2+k/4}
  \left(
    \sum_{i=0}^{k}(-1)^i
    \frac{\{k\}!}{\{i\}!\{k-i\}!}
    q^{-Ni-ik/2-i/2}
  \right).$$ Using the formula (see [@Murakami/Murakami:ACTAM12001 Lemma 3.2]) $$\sum_{i=0}^{k}(-1)^iq^{li/2}\frac{\{k\}!}{\{i\}!\{k-i\}!}
  =
  \prod_{g=1}^{k}(1-q^{(l+k+1)/2-g}),$$ we have the following simple formula with only one summand, which is due to Habiro and Lê (I learned this method from Lê). $$\label{eq:fig8_single}
  J_N(E;q)
  =
  \frac{1}{\{N\}}
  \sum_{k=0}^{N-1}\frac{\{N+k\}!}{\{N-1-k\}!}.$$
