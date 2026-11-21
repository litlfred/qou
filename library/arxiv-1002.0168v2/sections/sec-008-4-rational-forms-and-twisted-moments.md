---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Introduction"
section_id: sec-008-4-rational-forms-and-twisted-moments
section_title: "Rational forms and twisted moments"
section_number: 4
pages: 14-17
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.984
doc_brief: "Non-cyclotomic fusion categories Introduction — Etingof, Nikshych and Ostrik ask in [7, §2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
[]{#sec:noncyclotomic label="sec:noncyclotomic"}

The goal of this section is to prove the "only if\" direction of Thereom [\[thm:detailed\]](#thm:detailed){reference-type="ref" reference="thm:detailed"} parts [\[pa:dualprojs\]](#pa:dualprojs){reference-type="ref" reference="pa:dualprojs"} and [\[pa:principalprojs\]](#pa:principalprojs){reference-type="ref" reference="pa:principalprojs"} and as an immediate corollary Theorem [\[thm:noncyclotomic\]](#thm:noncyclotomic){reference-type="ref" reference="thm:noncyclotomic"}.

First we prove part [\[pa:dualprojs\]](#pa:dualprojs){reference-type="ref" reference="pa:dualprojs"}. Suppose $\cH_k^d$ is a complete rational from of $\cH^d$. The absolute value squared of the dimension of any object in $\cH^d$ must lie in $k$, by [@MR2183279 §2.1] (we take the absolute value squared because this does not depend on having a pivotal structure over $k$). Hence $|D_\ell |^2 \in k$, but $\Rational(D_\ell) = \Rational(|D_\ell^2|)$ in our cases.

Now we turn our attention to the main result, part [\[pa:principalprojs\]](#pa:principalprojs){reference-type="ref" reference="pa:principalprojs"}. Again our approach is to find an invariant which does not depend on the rational form and see that it generates $\Rational(\lambda_\ell)$. A key observation in [@0902.1294; @0909.4099] is that the whole structure of the Haagerup and extended Haagerup planar algebras can be recovered from the "moments\" and "twisted moments\" of a generator $S$. The moments are just the diagrammatic traces of the powers of $S$, while the twisted moments are the diagrammatic traces of the powers of $\rho^{\frac{1}{2}}(S)$ where $\rho^{\frac{1}{2}}$ is the 'one-click' rotation. Since $\rho^{\frac{1}{2}}$ changes the shading, it only makes sense in the shaded planar algebra, rather than the even part. Nonetheless we show in this section how to construct normalized twisted moments of an element $R$ in a shaded planar algebra which are invariants of the even part. In particular, if $\cC_K$ is the even part of a $3$-supertransitive shaded planar algebra, $R$ is a $\Rational$-linear combination of projections in $\cC_K$ and if $\cC_k$ is a complete rational form of $\cC_K$ over $k$, then $k$ must contain the normalized third twisted moment of $R$.

In order to define the twisted moments we need to define several morphisms. Suppose that $\cC_k$ is a split fusion category over $k$ with an object $Y$ such that $\Hom{}{Y\tensor Y \tensor Y}{1}$ is $1$-dimensional (this is assured if $\cK_k$ is the even part of a 3-supertransitive planar algebra) and $R$ is a $\Rational$-linear combination of simple projections in $\End{Y^{\otimes m}}$ for some $m$. Later, we will specialize to the category $\cC_k = \cH_\ell^p$, the object $Y=\JW{2}$, and the morphism $$R = \frac{1}{\lambda_\ell} S = \frac{1}{2}(P-Q) \in \End{{\JW{2}}^{\tensor n/2}}.$$ Choose nonzero elements $B$, $B'$, $T$, and $T'$ in the $1$-dimensional spaces $\Hom{}{Y \otimes Y}{1}$, $\Hom{}{1}{Y \otimes Y}$, $\Hom{}{Y \otimes Y \otimes Y}{1}$, and $\Hom{}{1}{Y \otimes Y \otimes Y}$ respectively. We can build morphisms $B_{Y^{\otimes 2i}}: Y^{\otimes 2i} \rightarrow 1$ and $B_{Y^{\otimes 2i}}: 1 \rightarrow Y^{\otimes 2i}$ by composing appropriately many copies of $B$ or $B'$. For example, $B_{Y^{\otimes 4}} =  B \circ (1 \otimes B \otimes 1)$.

::: defn
Define the theta symbol $\Theta\in k$ by $T \circ T'$, and the circle $C \in k$ by $B \circ B'$. Using the usual string notation, with a string labeled by $Y$, we have: $$\begin{array}{ccc}\Theta(T, T') =\inputtikz{theta} & \text{and} & C(B, B') = \inputtikz{circle}\end{array}$$
:::

Let a thick line denote $m-1$ copies of a thin line (i.e. the object $Y^{\otimes m-1}$).

::: defn
Define $\widehat{M}_3(R; B, B', T, T') \in k$, the unnormalized third twisted moment of a morphism $R \in \End{Y^{\otimes m}}$, by the value of the following composition $$\begin{aligned}
\widehat{M}_3(R; B, B', T, T') & =  
    B_{Y^{\otimes 2m-2}} \circ (\mathrm{id}_{Y^{\otimes m-1}} \otimes T \otimes \mathrm{id}_{Y^{\otimes m-1}}   ) \circ \\
    &\qquad \circ (R \tensor \mathrm{id}_{Y^{\otimes m+1}}) \circ  (\mathrm{id}_{Y} \otimes R \otimes \mathrm{id}_{Y^{\otimes m}}   ) \circ \\ & \qquad \qquad\circ (\mathrm{id}_{Y^{\otimes 2}} \otimes R \otimes \mathrm{id}_{Y^{\otimes m-1}}   ) \circ (T' \tensor B'_{Y^{\otimes 2m-2}}) \displaybreak[1]
\\ 
& = 
\begin{tikzpicture}
[
    baseline=10ex,
    R/.style={rectangle,draw,minimum width=40pt},
    O/.style={rectangle,draw,minimum width=30pt},
]

\foreach \i / \xc / \yc in {1/0/0, 2/-0.7/1.25, 3/-1.4/2.5}
{
    \node[R](R\i) at (\xc,\yc)  {$R$};
}

\begin{scope}[every node/.style={O}]
    \node(B) at (1,5.2){$B$};
    \node(B') at (1,-1.5) {$B'$};
    \node(T) at (0.5,3.7) {$T$};
    \node(T') at (-1.4,-1.5) {$T'$};
\end{scope}

\newcommand{\upwardsarrow}[3][]{
 \draw[->,#1] #2 ..controls ++(0,0.5) and ++(0,-0.5) .. #3;
}
\foreach \i / \j in {1/2,2/3}
{
    \upwardsarrow[very thick] {(R\i.135)} {(R\j.-45)}
    
}

\upwardsarrow[very thick] {(B'.45)}{(B.-45)};
\upwardsarrow[very thick] {(R3.135)}{(B.225)};
\upwardsarrow[very thick] {(B'.135)}{(R1.-45)};

\foreach \i / \theta in {1/-45,2/-90,3/-135}
{
    \upwardsarrow {(R\i.45)} {(T.\theta)};
}

\foreach \i / \theta in {1/45,2/90,3/135}
{
    \upwardsarrow {(T'.\theta)} {(R\i.-135)};
}
\end{tikzpicture}
\end{aligned}$$

Define the normalized third twisted moment by $$M_3(R) = \frac{\widehat{M}_3(R; B, B', T, T')}{\Theta(T, T') C(B, B')^{m-1}}.$$
:::

::: lem
$M_3(R)$ does not depend on the choice of $B$, $B'$, $T$, and $T'$.
:::

::: proof
*Proof.* Each of $B$, $B'$, $T$, and $T'$ are well-defined up to a choice of scalar. Each of $\Theta$, $C$, and $\widehat{M}_3(R)$ are homogoenous with respect to these rescalings, and it is easy to see that $M_3(R)$ is degree $0$ with respect to each of these rescalings. ◻
:::

::: thm
If $\cC_k$ is a split rational form for $\cH_\ell^p(\Complex)$ over a field $k$, then $\lambda_\ell \in k$.
:::

::: proof
*Proof.* Let $Y$ be the simple object of $\cC_k$ corresponding to the object $\JW{2}$ of $\cH_\ell^p(\Complex)$. Let $R = \frac{1}{2}(P-Q) = \frac{1}{\lambda_\ell} S \in \End{Y^{\otimes 2 \ell + 2}}$. The morphism $R$ makes sense in $\cC_k$ because $\cC_k$ is split. Consider the scalar $M_3(R) \in k$. Since this scalar does not depend on any choices, we can compute it in $\cH_\ell^p(\Complex)$ using the following obvious choices: $$\begin{aligned}
B & =\inputtikz{Bexpanded} & B' & = \inputtikz{Bprimeexpanded} \displaybreak[1]\\
T & =\inputtikz{Texpanded} & T' & = \inputtikz{Tprimeexpanded}. 
\end{aligned}$$ Since $S$ is uncappable, any $\JW{2}$ connected to an $S$ can be replaced with the identity. Thus with the above choices the unnormalized third twisted moment $\widehat{M}_3(R)$ is given by $$\begin{aligned}
\widehat{M}_3(R) =
\begin{tikzpicture}
[
    baseline=10ex,
    R/.style={rectangle,draw,minimum width=30pt},
]
\clip (2,-1.2) rectangle (-2.2,4.5);

\foreach \i / \xc / \yc in {1/0/0, 2/-0.7/1.25, 3/-1.4/2.5}
{
    \node[R](R\i) at (\xc,\yc)  {$R$};
    \foreach \n/\q in {1/30, 2/70, 3/110, 4/150} {
        \coordinate(R\i\n) at (R\i.\q);
    }
    \foreach \n/\q in {5/210, 6/250, 7/290, 8/330} {
        \coordinate(R\i\n) at (R\i.\q);
    }
}
\draw[fill=black!20] (R14) -- (R27) -- (R28) -- (R13);
\draw[fill=black!20] (R24) -- (R37) -- (R38) -- (R23);
\newcommand{\rr}{0.8}
\newcommand{\oa}{2.5}
\newcommand{\ob}{0.6}
\newcommand{\stf}{1.4}
\draw[fill=black!20] (R34) .. controls ++ ($2*\stf*(0,\rr)$) and ++ ($2*\stf*(0,\rr)$) .. ($(R34)+(\oa,0)+(0.8,0)$) -- ($(R17)+(\ob,0)+(0.8,0)$) .. controls ++ ($-\stf*(0,\rr)$) and ++ ($-\stf*(0,\rr)$)  .. (R17) -- (R18) .. controls ++ (0,-\rr)  and ++ (0,-\rr) .. ($(R18)+(\ob,0)$) -- ($(R33)+(\oa,0)$)  .. controls ++ (0,2*\rr) and ++(0,2*\rr) .. (R33);
\draw[fill=black!20] (R32) .. controls ++ ($\stf*(0,\rr)$) and ++ ($4*\stf*(0,\rr)$) .. (R11) -- (R12)  .. controls ++ (0,2*\rr) and ++ (0,\rr) .. (R21) -- (R22)  .. controls ++ (0,2*\rr) and ++ (0,\rr) .. (R31);
\draw[fill=black!20] (R16) .. controls ++ ($\stf*(0,-\rr)$) and ++ ($4*\stf*(0,-\rr)$) .. (R35) -- (R36)  .. controls ++ (0,-2*\rr) and ++ (0,-\rr) .. (R25) -- (R26)  .. controls ++ (0,-2*\rr) and ++ (0,-\rr) .. (R15);
    \node at ($(R1.180)+(-0.1,0)$) {$\star$};
    \node at ($(R2.180)+(-0.1,0)$) {$\star$};
    \node at ($(R3.180)+(-0.1,0)$) {$\star$};
\end{tikzpicture}
& = \frac{1}{[2]^2 \lambda_\ell^3} \inputtikz{twistedTTT} \\
& = \frac{1}{[2]^2 \lambda_\ell^3} \tr{\rho^{\frac{1}{2}}(S)^3}
\end{aligned}$$

hence the name "third twisted moment.\" (In the equation above, we don't literally mean equality of these diagrams; they live in different vector spaces. Instead, we mean that each diagram is the same multiple of the appropriate empty diagram.) The value of this moment can be easily computed using the formula for the square of $\rho^{\frac{1}{2}}(S)$ in Equation [\[eq:rhoS2\]](#eq:rhoS2){reference-type="eqref" reference="eq:rhoS2"}: $$\begin{aligned}
 \frac{1}{[2]^2 \lambda_\ell^3} \tr{\rho^{\frac{1}{2}}(S)^3} 
    & = \frac{1}{[2]^2 \lambda_\ell^3} \tr{(\check{r}-1) \rho^{1/2}(S)^2 + \check{r} \rho^{1/2}(S)} \displaybreak[1] \\
    & = \frac{1}{[2]^2 \lambda_\ell^3} \check{r} (\check{r}-1) [n+1]  \displaybreak[1] \\
    & = \lambda_\ell [2]^2(1-\check{r}^{-1})[n+1] \displaybreak[1] \\
    & = \lambda_\ell [2]^2 \frac{[2n+2]}{[n+2]}.
\end{aligned}$$ (In the last step we used the identity $([n+2]-[n])[n+1] = [2n+2]$.)

We have $\Theta  = [5] + 1$ and $C  = [3]$ and thus $$\begin{aligned}
M_3(R) & =\lambda_\ell  \frac{[2n+2]}{[n+2]} \frac{[2]^2}{\left([5]+1\right) [3]^{2\ell+1}}.
\end{aligned}$$

Finally, since $M_3(R) \in k$, and $\frac{[2n+2]}{[n+2]} \frac{[2]^2}{\left([5]+1\right) [3]^{2\ell+1}} \in k$ since odd quantum numbers lie in $\Rational(D_\ell)$, $[2]^2 = [3]+1$ can be written as a sum of odd quantum numbers, and ratios of even quantum numbers (in particular $\frac{[2n+2]}{[n+2]}$) lie in $\Rational(D_\ell)$, we conclude that $\lambda_\ell \in k$. ◻
:::
