---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-011-35-dimensions
section_title: "Dimensions"
section_number: 3.5
pages: 21-23
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.817
latex_coverage_ratio: 0.898
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
[]{#dim label="dim"} In this section we study a hook length formula which gives the dimension of indecomposable objects in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$. Let us start by defining the hook length formula.

::: definition
[]{#hookpoly label="hookpoly"} The *hook length* of a fixed box in a Young diagram $\lambda$ is the number of boxes in $\lambda$ which are either directly below or directly to the right of the fixed box, counting the fixed box itself once. Given a Young diagram $\lambda$ let $P_\lambda$ denote the unique polynomial such that $$P_\lambda(d)=\frac{d!}{\prod(\text{hook lengths of }\lambda(d))}$$ for every integer $d\geq2|\lambda|$.
:::

::: example
Let $\lambda=\includegraphics[bb= 0 4 16 1]{diss49.pdf}$ and suppose $d\geq 10$ is an integer. In the following picture each box of $\lambda(d)$ is labeled by its hook length. $$\includegraphics{diss50.pdf}$$ Thus $P_\lambda(d)=\frac{d!}{24(d-3)(d-4)(d-6)(d-8)!}=\frac{1}{24}d(d-1)(d-2)(d-5)(d-7)$.$\rotatebox{45}{$\Box$}$
:::

First, we show how $P_\lambda$ is related to the indecomposable object in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ corresponding to $\lambda$.

::: proposition
[]{#gendimen label="gendimen"} $\dim_{\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)}L(\lambda)=P_\lambda(T)$ for any Young diagram $\lambda$.
:::

::: proof
*Proof.* Fix a Young diagram $\lambda$. Let $K'=F(T)$ and suppose $\varepsilon\in K'P_{|\lambda|}(T)$ is a primitive idempotent with $L(\lambda)=([|\lambda|], \varepsilon)$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K')$. Applying Proposition [\[fieldex\]](#fieldex){reference-type="ref" reference="fieldex"} to the field extension $K'\subset K$ shows $L(\lambda)=([|\lambda|], \varepsilon)$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ too. Thus $\dim_{\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)}L(\lambda)=\text{tr}\,(\varepsilon)$ is a rational function in $T$. Now, by Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(4) and Proposition [\[Findy\]](#Findy){reference-type="ref" reference="Findy"} we can find an integer $N$ so that $\operatorname{Lift}_d(L(\lambda))=L(\lambda)$ and $\mathcal{F}:\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)\to \operatorname{Rep}(S_d; F)$ has $\mathcal{F}(L(\lambda))=L_{\lambda(d)}$ for all integers $d>N$. Hence, if $d>N$ is an integer, we have $$\begin{array}{rll}
P_\lambda(d)\hspace{-.1in} & = \dim_{\operatorname{Rep}(S_d; F)}L_{\lambda(d)} & \text{(see e.g. \cite[4.12]{MR1153249})}\\
 & =\dim_{\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)}L(\lambda) & \text{(since tensor functors preserve dimension)}\\
 & =(\dim_{\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)}L(\lambda))|_{T=d}  & \text{(by Proposition \ref{Liftprop}(2))}
\end{array}$$ Hence, $\dim_{\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)}L(\lambda)$ (a rational function in $T$) agrees with $P_\lambda(T)$ (a polynomial in $T$) for infinitely many values of $T$ . Hence they must always agree. ◻
:::

Next, we wish to determine the roots of $P_\lambda$. The following combinatorics will be useful toward that endeavor.

::: definition
Given a Young diagram $\lambda$ and an integer $d\geq2|\lambda|$, create the *$(\lambda, d)$ grid marking* as follows: Start with a grid of $(|\lambda|+1)\times (d-|\lambda|)$ black boxes. Place the Young diagram $\lambda(d)$ (with white boxes) atop the grid so that the upper left corner of $\lambda(d)$ is atop the upper left corner of the grid. Now place the numbers $0,\ldots, d-1$ into the boxes of the grid using the following rules:

-   Begin by placing the number 0 in the lower left box of the grid.

-   If the number $i$ is in a black box, place $i+1$ into the box directly above $i$.

-   If the number $i$ is in a white box, place $i+1$ into the box directly to the right of $i$.

Label the rows of the grid $0,\ldots, |\lambda|$ (from top to bottom) and the columns of the grid $1,\ldots, d-|\lambda|$ (from left to right).
:::

::: example
Set $\lambda=(4, 3, 1, 1, 0,\ldots)$ and $d=25$. Below is the $\lambda$-marking of the $10\times 16$ grid. $$~\hspace{.75in}\includegraphics{diss51.pdf}\hspace{.7in}\rotatebox{45}{$\Box$}$$
:::

The following proposition records the properties of the $(\lambda, d)$ grid marking which will be useful for determining the roots of $P_\lambda$.

::: proposition
[]{#grid label="grid"} The $(\lambda, d)$ grid marking has the following properties:

1.  If $\includegraphics[bb= 0 4 12 1]{diss52.pdf}$ appears in the $i$th row, then $k=|\lambda|+\lambda_i-i$.

2.  If $\includegraphics[bb= 0 4 12 1]{diss53.pdf}$ appears in the $i$th column, then $d-k$ is the hook length of the row $0$, column $i$ box in $\lambda(d)$.
:::

::: proof
*Proof.* (1) If $\includegraphics[bb= 0 4 12 1]{diss52.pdf}$ appears in the $i$th row, then $\includegraphics[bb= 0 4 12 1]{diss52.pdf}$ must be in column $\mu_i+1$. Hence $k$ is the number of up/right moves it takes to get from the lower left corner to the upper right corner in a $(|\lambda|-i)\times(\lambda_i+1)$ grid. The result follows.

\(2\) Let $c_i$ denote the number of boxes in the $i$th column of $\lambda$. Notice there are $c_i$ boxes below, and $d-|\lambda|-i$ boxes to the right of the row $0$, column $i$ box in $\lambda(d)$. Hence the hook length of that box is $d-|\lambda|-i+c_i+1$. On the other hand, if $\includegraphics[bb= 0 4 12 1]{diss53.pdf}$ appears in the $i$th column, then $\includegraphics[bb= 0 4 12 1]{diss53.pdf}$ must be in row $c_i$. Hence $k$ is the number of up/right moves it takes to get from the lower left corner to the upper right corner in a $(|\lambda|-c_i)\times i$ grid. Thus $k=|\lambda|-c_i+i-1$. ◻
:::

Using Proposition [\[grid\]](#grid){reference-type="ref" reference="grid"}, we can determine all the roots of the polynomial $P_\lambda$.

::: proposition
[]{#roots label="roots"} $P_\lambda$ is a degree $|\lambda|$ polynomial with $|\lambda|$ distinct, integer roots given by $|\lambda|+\lambda_i-i$ for each $i=1,\ldots,|\lambda|$.
:::

::: proof
*Proof.* Suppose $d$ is an integer with $d>2|\lambda|$. It follows from Definition [\[hookpoly\]](#hookpoly){reference-type="ref" reference="hookpoly"} that the roots of $P_\lambda$ are exactly the integers $0\leq k<d$ such that $d-k$ is not a hook length of a box in the top row of $\lambda(d)$. By Proposition [\[grid\]](#grid){reference-type="ref" reference="grid"}(2), those are exactly the values of $k$ for which $\includegraphics[bb= 0 4 12 1]{diss52.pdf}$ appears in the $(\lambda, d)$ grid marking. The result now follows from Proposition [\[grid\]](#grid){reference-type="ref" reference="grid"}(1). ◻
:::
