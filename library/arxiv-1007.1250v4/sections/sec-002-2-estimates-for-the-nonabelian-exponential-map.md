---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-002-2-estimates-for-the-nonabelian-exponential-map
section_title: "Estimates for the Nonabelian Exponential Map"
section_number: 2
pages: 25-35
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.969
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec:expon}


\subsection{The Exponential Map}
\indent{Nonabelian exponential map}
We need some preliminary results on the exponential maps of Lie groups.
Let $G$ be a (finite dimensional) Lie group over $\R$, with Lie
algebra $\mfrak{g} = \opn{Lie}(G)$. The exponential map
\[ \opn{exp}_G : \mfrak{g} \to G  \]
is an analytic map, satisfying
$\opn{exp}_G(0) = 1$ and $\exp(-\alpha) = \exp(\alpha)^{-1}$. The
exponential map is a diffeomorphism near
$0 \in \mfrak{g}$. Namely there is an open neighborhood $U_0(\g)$ of $0$
in $\g$, such that $V_0(G) := \opn{exp}_G(U_0(\g))$ is open in $G$,
and $\opn{exp}_G : U_0(\g) \to V_0(G)$ is a diffeomorphism.
Let $\log_G : V_0(G) \to U_0(\g)$ be the inverse of $\exp_G$. We call such
$V_0(G)$ an {\em open neighborhood of $1$ in $G$ on which $\log_G$ is
defined}. See \cite[Sections 2.10]{Va} for details.

The exponential map is functorial. Namely given a map 
$\phi : G \to H$ of Lie groups, the diagram
\[ \UseTips \xymatrix @C=7ex @R=5ex {
\opn{Lie}(G)
\ar[r]^{\opn{\ \ exp}_G}
\ar[d]_{\opn{Lie}(\phi)}
& 
G
\ar[d]^{\phi}
\\
\opn{Lie}(H)
\ar[r]^{\opn{\ \ exp}_H}
& 
H
} \]
is commutative.

When there is no danger of confusion we write $\exp$ and $\log$ instead of 
$\opn{exp}_G$ and $\log_G$, respectively.

The product in $G$ is denoted by $\cdot$, and the Lie bracket in $\g$ is
denoted by $[-,-]$. Given a finite sequence
$(g_1, \ldots, g_m)$ of elements in the group $G$, we write
\begin{equation} \label{eqn:6}
\prod_{i = 1}^m \, g_i := g_1 \cdot g_2 \cdots g_m \in G \ .
\end{equation}

It is a basic fact that if 
 $\alpha_1, \ldots, \alpha_m \in \g$
are {\em commuting} elements, then 
\[ \prod_{i=1}^m\, \opn{exp}(\alpha_i) = 
\exp \Bigl( \bosum_{i=1}^m \, \alpha_i \Bigr) . \]
The next theorem lists several estimates for the discrepancy when the elements
do not necessarily commute. 

\begin{thm} \label{thm:6}
Let $G$ be a Lie group, with Lie algebra $\g$. Let $V_0(G)$ be an  open
neighborhood of $1$ in $G$ on which $\log$ is well-defined, and
let $\norm{-}$ be a euclidean norm on $\g$. 
Then there are real constants $\epsilon_0(G)$ and $c_0(G)$ with the following
properties:
\begin{enumerate}
\rmitem{i} $0 < \epsilon_0(G) \leq 1$ and $0 \leq c_0(G)$.

\rmitem{ii} Let $\alpha_1, \ldots, \alpha_m \in \g$ be such that
$\sum_{i = 1}^m\, \norm{\alpha_i} < \epsilon_0(G)$.
Then
\[ \prod_{i=1}^m\, \opn{exp}(\alpha_i) \in V_0(G) ,  \]
\[ \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) } 
\leq c_0(G) \cdot \sum\nolimits_{i=1}^m \norm{\alpha_i} \]
and
\[ \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) -
\sum\nolimits_{i=1}^m \alpha_i } 
\leq c_0(G) \cdot \bigl( \sum\nolimits_{i=1}^m \norm{\alpha_i} \bigr)^2 . \]

\rmitem{iii} Let $\alpha_1, \alpha_2 \in \g$ be such that
$\norm{\alpha_1} + \norm{\alpha_2} < \epsilon_0(G)$. 
Then
\[  \norm{ [\alpha_1, \alpha_2] } \leq
c_0(G) \cdot \norm{\alpha_1} \cdot \norm{\alpha_2} , \]
\[ \begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\alpha_1) \cdot 
\opn{exp}(\alpha_2) \bigr) -  
( \alpha_1 + \alpha_2 + \smfrac{1}{2}[\alpha_1, \alpha_2] ) } \\
& \qquad 
\leq c_0(G) \cdot \norm{\alpha_1} \cdot \norm{\alpha_2} \cdot 
\bigl( \norm{\alpha_1} + \norm{\alpha_2} \bigr) .
\end{aligned} \]
and
\[ \begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\alpha_1) \cdot 
\opn{exp}(\alpha_2) \cdot \opn{exp}(\alpha_1)^{-1} \cdot
\opn{exp}(\alpha_2)^{-1} \bigr) -  
[\alpha_1, \alpha_2] } \\
& \qquad 
\leq c_{0}(G) \cdot \norm{\alpha_1} \cdot \norm{\alpha_2} \cdot 
\bigl( \norm{\alpha_1} + \norm{\alpha_2} \bigr) .
\end{aligned} \]

\rmitem{iv} Let 
$\alpha_1, \ldots, \alpha_m, \beta_1, \ldots, \beta_m \in \g$ be
such that
\[ \sum_{i = 1}^m\, (\norm{\alpha_i} + \norm{\beta_i}) < \epsilon_0(G) \, . \]
Then
\[ \begin{aligned}
& \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i + \beta_i) \bigr) -
\opn{log} \bigl(   \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) -
\sum\nolimits_{i=1}^m \beta_i } \\
& \qquad 
\leq c_0(G) \cdot \bigl( \sum\nolimits_{i=1}^m (\norm{\alpha_i}  +
\norm{\beta_i}) \bigr) \cdot 
\bigl( \sum\nolimits_{i=1}^m \norm{\beta_i} \bigr) .
\end{aligned} \]
and
\[ \begin{aligned}
& \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i + \beta_i) \bigr) -
\opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) } \\
& \qquad 
\leq c_0(G) \cdot 
\bigl( \sum\nolimits_{i=1}^m \norm{\beta_i} \bigr) \, .
\end{aligned} \]

\rmitem{v} Let $\alpha_1, \ldots, \beta_m$ be as in property \tup{(iv)},
and assume moreover that $[\alpha_i, \alpha_j] \lb = 0$ for all $i, j$. 
Then
\[ \begin{aligned}
& \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i + \beta_i) \bigr) -
\sum\nolimits_{i=1}^m (\alpha_i + \beta_i) } \\
& \qquad 
\leq c_0(G) \cdot \bigl( \sum\nolimits_{i=1}^m (\norm{\alpha_i}  +
\norm{\beta_i}) \bigr) \cdot 
\bigl( \sum\nolimits_{i=1}^m \norm{\beta_i} \bigr) .
\end{aligned} \]
\end{enumerate}
\end{thm}

The theorem is proved at the end of Subsection \ref{subsec:touches}, after
some preparations. 

The constants $c_0(G)$ and $\epsilon_0(G)$ are called a {\em commutativity
constant} and a {\em convergence radius} for $G$ respectively. (If $G$ is
abelian one can take $c_0(G) = 0$.)


\subsection{The CBH Theorem}
\label{subsec:CBH}
\index{CBH Theorem}
There is an element $F(x, y)$ in the completed free Lie algebra over 
$\mbb{Q}$ in the variables $x, y$, called the {\em Hausdorff series}.  See
\cite[Sections II.6 and II.7]{Bo}, where the letter $H$ is used instead of $F$. 
For any $i,j \geq 0$ let us denote by $F_{i, j}(x, y)$ the homogeneous
component of $F(x, y)$ of degree $i$ in $x$ and degree $j$ in $y$. So 
\[ F(x, y) =  \sum_{i, j \geq 0} F_{i, j}(x, y) ץ \]

Now consider a Lie group $G$ as before, with Lie algebra $\g$. Choose a
euclidean norm $\norm{-}$ on the vector space $\g$. 
Given elements $\alpha, \beta \in \g$ we can evaluate
$F_{i, j}(x, y)$ on them, obtaining an element
$F_{i, j}(\alpha, \beta) \in \g$. 

The {\em Campbell-Baker-Hausdorff Theorem} says that 
there is an open neighborhood $U_1$ of $0$ in $\g$ 
(its size depending on the norm) such that the series
$F(\alpha, \beta)$ converges absolutely and uniformly for 
$\alpha, \beta \in U_1$, and moreover 
\begin{equation} \label{eqn:87}
\exp \bigl( F(\alpha, \beta) \bigr) = 
\exp(\alpha) \cdot \exp(\beta) .
\end{equation}

This assertion is not explicit in the book \cite{Bo}; it
requires combining various scattered results in Sections II.7 and III.4
of \cite{Bo}. An explicit statement of the CBH Theorem is 
\cite[Theorem 2.15.4]{Va}. However the treatment of the structure of the
Hausdorff series is not sufficiently detailed in \cite{Va}. 

For a positive number $r$ we denote by $U(r)$ the open ball of radius $r$ and
center $0$ in $\g$, and by $\ol{U}(r)$ its closure (the closed ball). 

\begin{lem} \label{lem:35}
There are constants $\epsilon_1$ and $c_1$, such that
$0 < \epsilon_1$,
$U(\epsilon_1 ) \subset U_1$, $0 \leq c_1$, and for every 
$\alpha, \beta \in U(\epsilon_1)$ the inequality
\[ \Norm{ F(\alpha, \beta) - 
(\alpha + \beta + \smfrac{1}{2} [x,y]) } 
\leq c_1 \cdot \norm{\alpha} \cdot 
\norm{\beta} \cdot (\norm{\alpha} + \norm{\beta})  \]
holds.
\end{lem}

\begin{proof}
Let us denote by 
$f_{i, j}$ the norm of the bi-homogeneous function 
\[ F_{i, j} : \g \times \g \to \g . \]
Namely
\[ f_{i, j} := \sup \, \{ \norm{F_{i, j}(\alpha, \beta)} \mid 
\norm{\alpha}, \norm{\beta} \leq 1 \} . \]
So for any $\alpha, \beta \in \g$ one has
\[ \norm{F_{i, j}(\alpha, \beta)} \leq 
f_{i, j} \cdot \norm{\alpha}^i \cdot \norm{\beta}^j . \]
In \cite[Section II.7.2]{Bo} it is shown that there is a positive
number $\epsilon_1$, such that the series 
$\sum_{i, j \geq 0} f_{i,j} \epsilon_1^{i+j}$
converges (to a finite sum). 
By shrinking $\epsilon_1$ if necessary, we may assume that
$\ol{U}(\epsilon_1 ) \subset U_1$.

Now in \cite[Section II.6.4]{Bo} it is proved that 
\[ F_{1,0}(x, y) = x, \ F_{0, 1}(x, y) = y, \
F_{1, 1}(x,y) = \smfrac{1}{2} [x,y] \]
and 
\[ F_{i, 0}(x,y) = F_{0, j}(x,y) = 0 \ \ \text{for} \ \ i, j \neq 1 . \]
Thus for $\alpha, \beta \in U(\epsilon_1)$ we have
\[  F(\alpha, \beta) - (\alpha + \beta + \smfrac{1}{2} [x,y]) = 
\sum\limits_{(i, j) \in I} F_{i, j}(\alpha, \beta) , \]
where
\[ I := \{ (i, j) \mid i, j \geq 1 \ \text{and} \ i + j \geq 3 \} . \]

Now if $(i, j) \in I$ and $0 \leq a, b \leq \epsilon_1$, then 
\[ a^i b^j \leq a b (a+b) \cdot \epsilon_1^{i + j -3} . \]
Therefore for $\alpha, \beta \in U(\epsilon_1)$, with
$a := \norm{\alpha}$ and $b := \norm{\beta}$, we have the estimate
\[ \begin{aligned}
& \Norm{ \sum\limits_{(i, j) \in I} F_{i, j}(\alpha, \beta) }
\leq \sum\limits_{(i, j) \in I} \Norm{ F_{i, j}(\alpha, \beta) } \\
& \qquad \leq \sum\limits_{(i, j) \in I} f_{i,j} \cdot a^i \cdot b^j
\leq a b (a+b) \cdot \epsilon_1^{-3} \cdot  
\sum\limits_{(i, j) \in I} f_{i,j} \cdot \epsilon_1^{i+j} \, .
\end{aligned} \]
Taking the number
\[ c_1 := \epsilon_1^{-3} \cdot  
\sum\limits_{(i, j) \in I} f_{i,j} \cdot \epsilon_1^{i+j} \]
does the trick.
\end{proof}


\subsection{Calculations with a Few Elements}
We continue with the chosen open set $V_0(G) \subset G$ and norm $\norm{-}$ on
the Lie algebra $\g$.
In this subsection we translate the estimate for the CBH series to estimates on
$\exp$ and $\log$.
Recall our notation: $U(r)$ is the open ball of positive radius $r$ in $\g$, and
$\ol{U}(r)$ is the closed ball.

\begin{lem} \label{lem11}
There exist constants $\epsilon_2, c_2 \in \R$ such that 
\[ 0< \epsilon_2 \leq 1 \ \ \text{and} \ \ 1 \leq c_2 , \]
and such the following formulas hold for every 
$\alpha, \beta \in U(\epsilon_2)$.
\begin{eqnarray} \label{eqn:82}
\opn{exp}(\alpha) \cdot \opn{exp}(\beta) \in V_0(G) , \\
\label{eqn:86}
\norm{\, [\alpha, \beta]\, } \leq
c_{2} \cdot \norm{\alpha} \cdot \norm{\beta} \, ,
\end{eqnarray}
and
\begin{equation} \label{eqn:83}
\begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\alpha) \cdot 
\opn{exp}(\beta) \bigr) -  
( \alpha + \beta + \smfrac{1}{2}[\alpha, \beta] ) } \\
& \qquad
\leq c_{2} \cdot \norm{\alpha} \cdot \norm{\beta} \cdot 
\bigl( \norm{\alpha} + \norm{\beta} \bigr) \, .
\end{aligned}
\end{equation}
\end{lem}

\begin{proof}
The existence of a positive $\epsilon_2$ making formula (\ref{eqn:82}) true
is easy (due to continuity). We can assume 
$\epsilon_2 \leq \min (1, \epsilon_1)$.

The existence of a number $c_2$ making inequality (\ref{eqn:86}) valid is also
easy, because the function
$\norm{\, [\alpha, \beta]\, }$ is bilinear and $\g$ is finite dimensional. 
We can assume that $c_2 \geq \max(1, c_1)$. 

Finally, the validity of formula (\ref{eqn:83}) comes from Lemma \ref{lem:35}
and the CBH formula (\ref{eqn:87}).
\end{proof}

\begin{lem} \label{lem:33}
There is a real number $c_3$ such that $c_3 \geq c_2$, and for any 
$\alpha_1, \alpha_2, \beta_1, \beta_2 \in \g$ satisfying
$\norm{\alpha_i} + \norm{\beta_i} < \epsilon_2$ the inequality 

\begin{equation} \label{eqn:84}
\begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\alpha_1 + \beta_1) \cdot 
\opn{exp}(\alpha_2 + \beta_2) \bigr) -  
\opn{log} \bigl( \opn{exp}(\alpha_1) \cdot 
\opn{exp}(\alpha_2) \bigr) } \\
& \qquad \leq c_{3} \cdot (\norm{\beta_1} + \norm{\beta_2} ) .
\end{aligned} 
\end{equation}
holds.
\end{lem}

\begin{proof}
Given $\alpha \in \ol{U}(\epsilon_2)$ we have a smooth
(in fact analytic) function
$f_{\alpha} : U(\epsilon_2) \to \g$ defined by
\[ f_{\alpha}(\beta) := \log 
\bigl( \opn{exp}(\alpha) \cdot \opn{exp}(\beta) \bigr) . \]
Let $\g^*$ be the dual space of $\g$, and let 
$\d_{\beta} f_{\alpha} \in \g^*$
be the derivative of $f_{\alpha}$ at $\beta$. 
Then Taylor expansion of $f_{\alpha}$ around $\beta$ gives us
\begin{equation} \label{eqn15}
f_{\alpha}(\beta + \gamma) = f_{\alpha}(\beta) +
(\d_{\beta} f_{\alpha})(\gamma) +
(\opn{R}_{\beta}^{\geq 2} f_{\alpha})(\gamma)
\end{equation}
for any $\gamma \in \ol{U}(\epsilon_2)$. 
Here $\opn{R}_{\beta}^{\geq 2} f_{\alpha}$ is just the remainder, in other
words the higher order part of the Taylor expansion. 
The linear term 
$(\d_{\beta} f_{\alpha})(\gamma)$ 
can be estimated by
\[ \norm{ (\d_{\beta} f_{\alpha})(\gamma)  } \leq
a_1 \cdot \norm{\gamma}  \]
for a suitable positive number $a_1$. 
The remainder $(\opn{R}_{\beta}^{\geq 2} f_{\alpha})(\gamma)$ can be
estimated by
\[ \norm{ (\opn{R}_{\beta}^{\geq 2} f_{\alpha})(\gamma) } 
\leq a_2 \cdot \norm{\gamma}^2  \]
for some positive number $a_2$. 

These inequalities tell us that if 
$\alpha, \beta, \gamma \in U(\epsilon_2)$ then 
\begin{equation} \label{eqn17}
\begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\alpha) \cdot 
\opn{exp}(\beta + \gamma) \bigr) -  
\opn{log} \bigl( \opn{exp}(\alpha) \cdot 
\opn{exp}(\beta) \bigr) } \\
& \qquad
= \Norm{ \opn{log} \bigl( f_{\alpha}(\beta + \gamma) \bigr) -  
\opn{log} \bigl( f_{\alpha}(\beta) \bigr) } \\
& \qquad
\leq a_1 \cdot \norm{\gamma} + a_2 \cdot \norm{\gamma}^2
\leq (a_1 + a_2) \cdot \norm{\gamma} . 
\end{aligned} 
\end{equation}

In a similar way we look at the function 
$g_{\beta}(\alpha) := f_{\alpha}(\beta)$, 
and we obtain constants $b_1, b_2$ such that
\begin{equation}  \label{eqn18}
\Norm{ \opn{log} \bigl( \opn{exp}(\alpha + \gamma) \cdot 
\opn{exp}(\beta) \bigr) -  
\opn{log} \bigl( \opn{exp}(\alpha) \cdot 
\opn{exp}(\beta) \bigr) } 
\leq (b_1 + b_2) \cdot \norm{\gamma} .
\end{equation}

Therefore by taking
\[ c_3 := \max \{ c_2, a_1 + a_1, b_1 + b_2  \} \]
all conditions are satisfied.
\end{proof}

\begin{lem} \label{lem16}
There exists a constant $c_4 \geq c_3$ such that the following inequalities
hold for any $\alpha, \beta \in \g$ satisfying
$\norm{\alpha}, \norm{\beta} < \epsilon_2$.
\[ \Norm{ \opn{log} \bigl( \opn{exp}(\alpha) \cdot 
\opn{exp}(\beta) \bigr) -  ( \alpha + \beta ) } \leq
c_{4} \cdot \norm{\alpha} \cdot \norm{\beta} \]
and
\[ \Norm{ \opn{log} \bigl( \opn{exp}(\alpha) \cdot \opn{exp}(\beta) \bigr) }
\leq \norm{\alpha} + \norm{\beta} +
c_{4} \cdot \norm{\alpha} \cdot \norm{\beta} \, . \]
\end{lem}

\begin{proof}
{}From Lemma \ref{lem11} and the triangle inequality we get
\[ \begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\alpha) \cdot 
\opn{exp}(\beta) \bigr) -  
( \alpha + \beta ) } \\
& \qquad \leq c_{2} \cdot \norm{\alpha} \cdot \norm{\beta} \cdot 
\bigl( \norm{\alpha} + \norm{\beta} \bigr)  +
\smfrac{1}{2} c_2 \cdot \norm{\alpha} \cdot \norm{\beta} \\
& \qquad \leq 3 c_2  \cdot \norm{\alpha} \cdot \norm{\beta} \, .  
\end{aligned} \]
This proves the first inequality, with
$c_4 := \max (c_3, 3 c_2)$.
The second inequality is an immediate consequence.
\end{proof}


\subsection{Calculations with Many Elements}
Let us define
\begin{equation} \label{eqn:101}
\epsilon_4 :=  \smfrac{1}{12} c_4^{-1} \cdot \epsilon_2 \, . 
\end{equation}

\begin{lem} \label{lem17}
Let $\alpha_1, \ldots, \alpha_m \in \g$ be such that
$\sum_{i = 1}^m\, \norm{\alpha_i} < \epsilon_4$.
Then the relation and inequalities below hold:
\begin{equation} \label{eqn:90}
\prod_{i=1}^m\, \opn{exp}(\alpha_i) \in V_0(G) ,
\end{equation}
\begin{equation} \label{eqn:91}
\Norm{ \opn{log} \bigl( \prod\nolimits_{i=1}^m
\opn{exp}(\alpha_i) \bigr) } \leq 
\smfrac{3}{2} \sum_{i = 1}^m\, \norm{\alpha_i} 
\end{equation}
and
\begin{equation} \label{eqn:92}
\Norm{ \opn{log} \bigl( \prod\nolimits_{i=1}^m
\opn{exp}(\alpha_i) \bigr) - \sum\nolimits_{i=1}^m \alpha_i } \leq
c_4 \cdot \bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)^2 \, .
\end{equation}
\end{lem}

\begin{proof}
Recall that $\epsilon_2 \leq 1$ and $c_4 \geq 1$.

For $m = 1$ all is clear. Take $m = 2$. Then since
$\norm{\alpha_i} < \epsilon_2$ we have 
\[ \opn{exp}(\alpha_1) \cdot \opn{exp}(\alpha_2) \in V_0(G) \]
by Lemma \ref{lem11}. Next, since
$\norm{\alpha_1} \leq \smfrac{1}{6} c_4^{-1}$, it follows that
\[ c_4 \cdot \norm{\alpha_1} \cdot \norm{\alpha_2} \leq 
\smfrac{1}{6}  \norm{\alpha_2} \, . \]
{}From this and Lemma \ref{lem16} we see that
\[ \Norm{ \opn{exp}(\alpha_1) \cdot \opn{exp}(\alpha_2) } \leq 
\norm{\alpha_1} + \norm{\alpha_2} + c_4 \cdot \norm{\alpha_1} \cdot
\norm{\alpha_2} 
\leq \smfrac{3}{2} \cdot (\norm{\alpha_1} + \norm{\alpha_2}) \, . \]
Hence (\ref{eqn:91}) holds for $m = 2$.
Again using Lemma \ref{lem16}  we have
\[ \begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\alpha_1) \cdot 
\opn{exp}(\alpha_2) \bigr) -  
( \alpha_1 + \alpha_2 ) } \\
& \qquad \leq
c_{4} \cdot \norm{\alpha_1} \cdot \norm{\alpha_2} 
\leq c_{4} \cdot (\norm{\alpha_1} + \norm{\alpha_2})^2 .
\end{aligned}  \]
This finishes the case $m = 2$.

Now assume the assertions are true for $m \geq 2$, and consider 
$\alpha_1, \ldots, \lb \alpha_{m+1} \in \g$ such that
$\sum_{i = 1}^{m+1}\, \norm{\alpha_i} < \epsilon_4$.
Define
\[ \beta := \opn{log} \bigl( \prod\nolimits_{i=1}^{m}
\opn{exp}(\alpha_i) \bigr)  , \]
so that
\[ \prod_{i=1}^{m+1} \opn{exp}(\alpha_i) =
\opn{exp}(\beta) \cdot \opn{exp}(\alpha_{m+1}) . \]
By the induction hypothesis, i.e.\ inequality (\ref{eqn:91}) for $m$,
we have
\begin{equation} \label{eqn:93}
\norm{\beta} \leq \smfrac{3}{2} \sum_{i = 1}^m\, \norm{\alpha_i}
\leq
\smfrac{3}{2} \sum_{i = 1}^{m+1}\, \norm{\alpha_i}
\leq \smfrac{3}{2} \cdot \smfrac{1}{6}  c_4^{-1} \cdot \epsilon_2 =
\smfrac{1}{4} c_4^{-1} \cdot \epsilon_2 \, .
\end{equation}
This implies 
$\norm{\beta} < \epsilon_2$. Since we also have 
$\norm{\alpha_{m+1}} < \epsilon_2$, Lemma  \ref{lem11} says that
\[ \opn{exp}(\beta) \cdot \opn{exp}(\alpha_{m+1}) \in V_0(G) . \]
This verifies (\ref{eqn:90}) for $m+1$.

Using Lemma \ref{lem11} again we see that 
\[ \Norm{ \opn{log} \bigl( \opn{exp}(\beta) \cdot
\opn{exp}(\alpha_{m+1})
\bigr) } \leq 
\norm{\beta} + \norm{\alpha_{m+1}} + 
c_4 \cdot \norm{\beta} \cdot \norm{\alpha_{m+1}} \, . \]
Because we also have the inequality
$c_4 \cdot \norm{\beta} \leq \smfrac{1}{2}$, 
we conclude that
\[ \norm{\beta} + \norm{\alpha_{m+1}} + 
c_4 \cdot \norm{\beta} \cdot \norm{\alpha_{m+1}} \leq
\smfrac{3}{2} \cdot \norm{\beta} + \smfrac{3}{2} \cdot \norm{\alpha_{m+1}} \leq
\smfrac{3}{2} \cdot \sum_{i = 1}^{m+1}\, \norm{\alpha_i} \, . \]
Thus inequality (\ref{eqn:91}) holds for $m+1$.

According to Lemma \ref{lem16} we have
\[ \Norm{ \opn{log} \bigl( \opn{exp}(\beta) \cdot
\opn{exp}(\alpha_{m+1}) 
\bigr) - (\beta + \alpha_{m+1}) } \leq 
c_4 \cdot \norm{\beta} \cdot \norm{\alpha_{m+1}} . \]
The induction assumption for inequality (\ref{eqn:92}) says that
\[ \Norm{ \beta - \sum\nolimits_{i=1}^m \alpha_i } \leq 
c_4 \cdot \bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)^2 \, . \]
Combining these with the inequality (\ref{eqn:93}) we obtain
\[ \begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\beta) \cdot
\opn{exp}(\alpha_{m+1}) 
\bigr) -  \sum\nolimits_{i=1}^{m+1} \alpha_i } \\
& \quad \leq 
\Norm{ \opn{log} \bigl( \opn{exp}(\beta) \cdot
\opn{exp}(\alpha_{m+1}) 
\bigr) - (\beta + \alpha_{m+1}) } \\
& \quad \quad +
\Norm{ (\beta + \alpha_{m+1}) - \sum\nolimits_{i=1}^{m+1} \alpha_i } \\
& \quad \leq c_4 \cdot \norm{\beta} \cdot \norm{\alpha_{m+1}} +
c_4 \cdot \bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)^2 \\
& \quad \leq c_4 \cdot \Bigl(
\bigl( \smfrac{3}{2} \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)
\cdot \norm{\alpha_{m+1}} + 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)^2 \Bigr)  \\
& \quad \leq c_4 \cdot 
\bigl( \sum\nolimits_{i = 1}^{m+1}\, \norm{\alpha_i} \bigr)^2 \, .
\end{aligned} \]
This proves (\ref{eqn:92}).
\end{proof}

\begin{lem} \label{lem18}
Let 
$\alpha_1, \ldots, \alpha_m, \beta_1, \ldots, \beta_m \in \g$ be
such that
\[ \sum_{i = 1}^m\, \bigl( \norm{\alpha_i} + \norm{\beta_i} \bigr)
< \epsilon_4 \, . \]
Then
\[ \begin{aligned}
& \Norm{ \opn{log} \Bigl( \prod\nolimits_{i=1}^m
\bigl( \exp(\alpha_i) \cdot \exp(\beta_i) \bigr) \Bigr) \\
& \qquad \qquad -
\opn{log} \Bigl( \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i)
\bigr)
\cdot \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\beta_i) \bigr) \Bigr) }
\\
& \qquad \leq 4 c_4^2 \cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr) \cdot  
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\beta_i} \bigr) 
\end{aligned} \]
and
\[ \begin{aligned}
& \Norm{ \opn{log} \bigl( \prod\nolimits_{i=1}^m
\opn{exp}(\alpha_i + \beta_i) \bigr) -
\opn{log} \Bigl( \prod\nolimits_{i=1}^m
\bigl( \exp(\alpha_i) \cdot \exp(\beta_i) \bigr) \Bigr) } \\
& \qquad \leq 2 c_4^2 \cdot \sum\nolimits_{i = 1}^m\, 
\norm{\alpha_i} \cdot \norm{\beta_i} .
\end{aligned} \]
\end{lem}

\begin{proof}
For the first inequality we note that for any $i,j$ one has
\[ \begin{aligned}
& \Norm{ \log \bigl( \exp(\beta_j) \cdot \exp(\alpha_i) \bigr) - 
\log \bigl( \exp(\alpha_i) \cdot \exp(\beta_j) \bigr) } \\
& \qquad \leq 2 c_2 \cdot \norm{\alpha_i} \cdot \norm{\beta_j} \cdot
\bigl( \norm{\alpha_i} + \norm{\beta_j} \bigr) +
c_2 \cdot \norm{\alpha_i} \cdot \norm{\beta_j} \\
& \qquad \leq 2 c_2 \cdot \norm{\alpha_i} \cdot \norm{\beta_j} .
\end{aligned} \]
This is due to Lemma \ref{lem11}.
Now for our inequality we have to move all the $\exp(\beta_j)$ in the
product across all the $\exp(\alpha_i)$. According Lemma \ref{lem:33} the
``cost'' of each such move is at most
$2 c_3 \cdot 2 c_2 \cdot \norm{\alpha_i} \cdot \norm{\beta_j}$.
So the total ``cost'' is at most
\[ \sum\nolimits_{i, j = 1}^m\, 2 c_3 \cdot 
2 c_2 \cdot \norm{\alpha_i} \cdot \norm{\beta_j} =
4 c_2 c_3 \cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr) \cdot  
\bigl( \sum\nolimits_{j = 1}^m\, \norm{\beta_j} \bigr) . \]
Since $c_4 \geq c_2, c_3$ this proves the first inequality.

For the second inequality we note that, due to Lemma \ref{lem16}, we
have
\[ \Norm{ \log \bigl( \exp(\alpha_i + \beta_i) \bigr) -
\log \bigl( \exp(\alpha_i) \cdot \exp(\beta_i) \bigr) } 
\leq c_4 \cdot \norm{\alpha_i} \cdot \norm{\beta_i}  . \]
Since we have to make such a change for every $i$, according to
Lemma \ref{lem:33} the total ``cost'' is at most
$2 c_3 c_4 \cdot \sum\nolimits_{i = 1}^m\, 
\norm{\alpha_i} \cdot \norm{\beta_i}$.
\end{proof}

\begin{lem} \label{lem:36}
There exists a constant $c_5$ such that 
$c_5 \geq \max( c_4, \smfrac{3}{2} )$, 
and for every   
$\alpha_1, \ldots, \alpha_m, \beta_1, \ldots, \beta_m \in \g$ 
satisfying
\[ \sum_{i = 1}^m\, \bigl( \norm{\alpha_i} + \norm{\beta_i} \bigr)
< \epsilon_4 \]
one has:
\begin{equation} \label{eqn:94}
\begin{aligned}
& \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i + \beta_i) \bigr) -
\opn{log} \bigl(   \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) -
\sum\nolimits_{i=1}^m \beta_i } \\
& \qquad 
\leq c_5 \cdot \bigl( \sum\nolimits_{i=1}^m (\norm{\alpha_i}  +
\norm{\beta_i}) \bigr) \cdot 
\bigl( \sum\nolimits_{i=1}^m \norm{\beta_i} \bigr) 
\end{aligned} 
\end{equation}
and
\begin{equation} \label{eqn:95}
\begin{aligned}
& \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i + \beta_i) \bigr) -
\opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) } \\
& \qquad 
\leq c_5 \cdot 
\bigl( \sum\nolimits_{i=1}^m \norm{\beta_i} \bigr) \, .
\end{aligned} 
\end{equation}
If moreover $[\alpha_i, \alpha_j] = 0$ for all $i, j$, then
\begin{equation} \label{eqn:96}
\begin{aligned}
& \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i + \beta_i) \bigr) -
\sum\nolimits_{i=1}^m (\alpha_i + \beta_i) } \\
& \qquad 
\leq c_5 \cdot \bigl( \sum\nolimits_{i=1}^m (\norm{\alpha_i}  +
\norm{\beta_i}) \bigr) \cdot 
\bigl( \sum\nolimits_{i=1}^m \norm{\beta_i} \bigr) .
\end{aligned} 
\end{equation}
\end{lem}

\begin{proof}
According to Lemma \ref{lem18} we have
\begin{equation} \label{eqn:97}
\begin{aligned}
& \Norm{ \opn{log} \bigl( \prod\nolimits_{i=1}^m
\opn{exp}(\alpha_i + \beta_i) \bigr) -
\opn{log} \Bigl( \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i)
\bigr)
\cdot \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\beta_i) \bigr) \Bigr) }
\\
& \qquad
\leq 2 c_4^2 \cdot 
\sum_{i = 1}^m\, \norm{\alpha_i} \cdot \norm{\beta_i} \, . 
\end{aligned}
\end{equation}
By Lemma \ref{lem17} we know that 
\begin{equation} \label{eqn:98}
\Norm{ \opn{log} \bigl( \prod\nolimits_{i=1}^m
\opn{exp}(\beta_i) \bigr) - \sum\nolimits_{i=1}^m \beta_i } \leq
c_4 \cdot \bigl( \sum\nolimits_{i = 1}^m\, \norm{\beta_i} \bigr)^2 \, .
\end{equation}
Combining Lemmas \ref{lem16} and \ref{lem17} we get
\begin{equation} \label{eqn:99}
\begin{aligned}
& \Norm{ 
\opn{log} \Bigl( \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i)
\bigr)
\cdot \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\beta_i) \bigr) \Bigr) \\
& \qquad \qquad  -
\Bigl( \opn{log} \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) +
\opn{log} \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\beta_i) \bigr)
\Bigr) } \\
& \qquad \leq c_4 \cdot 
\Norm{ \opn{log} \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) }
\cdot 
\Norm{ \opn{log} \bigl( \prod\nolimits_{i=1}^m \opn{exp}(\beta_i) \bigr) } \\
& \qquad \leq c_4 \cdot 
\bigl( \smfrac{3}{2} \, \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)
\cdot 
\bigl( \smfrac{3}{2} \, \sum\nolimits_{i = 1}^m\, \norm{\beta_i} \bigr) \\
& \qquad = \smfrac{9}{4} c_4 \cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)
\cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\beta_i} \bigr) \, . 
\end{aligned}
\end{equation}
Putting all these together we obtain the inequality
\begin{equation} \label{eqn:100}
\begin{aligned}
& \Norm{ \opn{log} 
\bigl( \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i + \beta_i) \bigr) -
\opn{log} \bigl(   \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) -
\sum\nolimits_{i=1}^m \beta_i } \\
& \qquad 
\leq 2 c_4^2 \cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)
\cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\beta_i} \bigr) \\
& \qquad \qquad + 
 \smfrac{9}{4} c_4^2 \cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\alpha_i} \bigr)
\cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\beta_i} \bigr) \\
& \qquad \qquad +
c_4 \cdot 
\bigl( \sum\nolimits_{i = 1}^m\, \norm{\beta_i} \bigr)^2 \\
& \qquad 
\leq 6 c_4^2  
\cdot \bigl( \sum\nolimits_{i=1}^m (\norm{\alpha_i}  +
\norm{\beta_i}) \bigr) \cdot 
\bigl( \sum\nolimits_{i=1}^m \norm{\beta_i} \bigr) \, . 
\end{aligned} 
\end{equation}
This proves inequality (\ref{eqn:94}) with
$c_5 := 7 c_4^2$.

Inequality (\ref{eqn:95}) follows easily from (\ref{eqn:100}), once we notice
that
\[ 6 c_4^2  
\cdot \bigl( \sum\nolimits_{i=1}^m (\norm{\alpha_i}  +
\norm{\beta_i}) \bigr) \leq 
6 c_4^2 \cdot 2 \epsilon_3 \leq c_4 \, . \]
When $[\alpha_i, \alpha_j] = 0$ for all $i, j$ we have
\[ \opn{log} \bigl(   \prod\nolimits_{i=1}^m \opn{exp}(\alpha_i) \bigr) =
\sum\nolimits_{i = 1}^m\, \alpha_i . \]
So inequality (\ref{eqn:95}) holds.
\end{proof}


\subsection{Final Touches} \label{subsec:touches}

\begin{lem} \label{lem:34}
There is a real number $c_6$ such that $c_6 \geq c_5$, and for any 
$\alpha, \beta \in \g$ with
$\norm{\alpha}, \norm{\beta} < \epsilon_4$ the inequality

\begin{equation} \label{eqn:85}
\begin{aligned}
& \Norm{ \opn{log} \bigl( \opn{exp}(\alpha) \cdot 
\opn{exp}(\beta) \cdot \opn{exp}(\alpha)^{-1} \cdot
\opn{exp}(\beta)^{-1} \bigr) -  
[\alpha, \beta] } \\
& \hspace{10ex}
\leq c_{6} \cdot \norm{\alpha} \cdot \norm{\beta} \cdot 
\bigl( \norm{\alpha} + \norm{\beta} \bigr) .
\end{aligned} 
\end{equation}
holds.
\end{lem}

\begin{proof}
Let's write
\[ a := \opn{exp}(\alpha), \quad b := \opn{exp}(\beta) , \]
\[ \gamma^+ := \alpha + \beta + \smfrac{1}{2} [\alpha, \beta], \quad
\gamma^- := -\alpha - \beta + \smfrac{1}{2} [\alpha, \beta], \]
\[ \delta^+ := \log(a \cdot b) - \gamma^+, \quad
\delta^- := \log(a^{-1} \cdot b^{-1})  - \gamma^- .  \]
According to Lemma \ref{lem11} we have
\[ \norm{\delta^+}, \norm{\delta^-} \leq 
c_{2} \cdot \norm{\alpha} \cdot \norm{\beta} \cdot 
\bigl( \norm{\alpha} + \norm{\beta} \bigr) \,  \]
and
\[ \norm{\gamma^+}, \norm{\gamma^-} \leq 
\norm{\alpha} + \norm{\beta} +
\smfrac{1}{2} c_{2} \cdot \norm{\alpha} \cdot \norm{\beta}
\leq (1 + c_2)(\norm{\alpha} + \norm{\beta}) \ . \]


Now
\[ a \cdot b = \exp (\gamma^+ + \delta^+) \]
and
\[ a^{-1} \cdot b^{-1} = \exp (\gamma^- + \delta^-) . \]
So by Lemma \ref{lem:33} we have
\[ \begin{aligned}
& \Norm{ \opn{log} \bigl( (a \cdot b) \cdot (a^{-1} \cdot b^{-1}) \bigr)
- \opn{log} \bigl( \exp (\gamma^+) \cdot \exp (\gamma^-) \bigr) } \\
& \qquad \leq c_{3} \cdot (\norm{\delta^+} + \norm{\delta^-} ) \\
& \qquad \leq 2 c_2 c_3 
\cdot \norm{\alpha} \cdot \norm{\beta}
\cdot \bigl( \norm{\alpha} + \norm{\beta} \bigr) \, .
\end{aligned}  \]

On the other hand, since $\alpha + \beta$ and $-\alpha - \beta$ commute,
by formula (\ref{eqn:96}) in Lemma \ref{lem:36} we have 
\[ \begin{aligned}
& \Norm{ \opn{log} \bigl( \exp (\gamma^+) \cdot \exp (\gamma^-) \bigr) -
[\alpha, \beta] } \\
& \qquad = 
\Norm{ \opn{log} 
\bigl( \exp((\alpha + \beta) + \smfrac{1}{2} [\alpha, \beta]) \cdot 
\exp((-\alpha - \beta) + \smfrac{1}{2} [\alpha, \beta]) \bigr) \\
& \qquad \qquad - \bigl( (\alpha + \beta) + \smfrac{1}{2} [\alpha, \beta] +
(-\alpha - \beta) + \smfrac{1}{2} [\alpha, \beta] \bigr) } \\
& \qquad \leq c_5 \cdot \bigl( 2 \cdot \norm{\alpha} + 
2 \cdot \norm{\beta} + \norm{ [\alpha, \beta] } \bigr) \cdot 
\bigl( \norm{ [\alpha, \beta] } \bigr) \\
& \qquad \leq c_5 \cdot (2 + c_2 \cdot \epsilon_4) \cdot c_2 
\cdot \norm{\alpha} \cdot \norm{\beta}
\cdot \bigl( \norm{\alpha} + \norm{\beta} \bigr) \, . 
\end{aligned} \]
In the last inequality we used
\[  \norm{ [\alpha, \beta] } \leq c_2 \cdot \norm{\alpha} \cdot \norm{\beta} 
\leq c_2 \cdot \epsilon_4 \cdot \norm{\beta} \, . \]
Therefore (\ref{eqn:85}) holds with 
\[ c_6 := 2 c_2 c_3 + c_5 \cdot (2 + c_2 \epsilon_4) \cdot c_2 \, . \]
\end{proof}

\begin{proof}[Proof of Theorem \tup{\ref{thm:6}}]
Take
$c_0(G) := c_6$ and $\epsilon_0(G) := \epsilon_4$.
Since $\epsilon_4 \leq \epsilon_2$ and
\[ c_6 \geq c_5 \geq \max( c_4, \smfrac{3}{2} ) 
\geq c_4 \geq c_3 \geq c_2 \, , \]
the assertions of the theorem 
are contained on Lemmas \ref{lem11}, \ref{lem17}, \ref{lem:36}
and \ref{lem:34}.  
\end{proof}









\cleardoublepage
