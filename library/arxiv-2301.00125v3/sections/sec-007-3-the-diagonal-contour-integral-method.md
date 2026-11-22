---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem"
section_id: sec-007-3-the-diagonal-contour-integral-method
section_title: "The diagonal (contour integral) method"
section_number: 3
pages: 8-12
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.833
latex_coverage_ratio: 1.0
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem — Given a uniform random permutation π ∈Sn, let Zn,k be equal to the number of increasing"
---
\label{sec:PinskyDiagonal}

We now apply the diagonal method, based on a complex  contour integral.
Firstly, we obtain
\begin{equation}
\label{eq:alphaIntegral}
	\oint_{\mathcal{C}(0;1)} \beta\left(w\, ,\ x\xi\, ,\ \frac{y}{\xi}\right)\, \frac{d\xi}{2\pi i \xi}\, =\, \alpha(w,xy)\, ,
\end{equation}
for sufficiently small $x$, $y$ and $w$.
To state it again with the detailed formula, we have
\begin{equation}
\label{eq:alphaIntegralOneHalf}
	\alpha(w,xy)\,  =\,
\oint_{\mathcal{C}(0;1)}  \frac{1}{\left(\left(1-\left(x \xi+y \xi^{-1}\right)\right)^2-4xy\right)^{1/2}-w}\, \cdot \frac{d\xi}{2\pi i \xi}\, .
\end{equation}
For simplicity, we will specialize this to $y=x$. That gives
\begin{equation}
\label{eq:alphaIntegralThreeFourths}
	\alpha(w,x^2)\,  =\,
\oint_{\mathcal{C}(0;1)}  \frac{1}{\left(\left(1-x\cdot\left(\xi+\xi^{-1}\right)\right)^2-4x^2\right)^{1/2}-w}\, \cdot \frac{d\xi}{2\pi i \xi}\, .
\end{equation}
This may then be further simplified as 
\begin{equation}
\label{eq:alphaIntegralFourFifths}
	\alpha(w,x^2)\,  =\,
\oint_{\mathcal{C}(0;1)}  \frac{1}{\Big(\big(1-x\cdot (\xi+2+\xi^{-1})\big)\big(1-x\cdot (\xi-2+\xi^{-1})\big)\Big)^{1/2}-w}\, \cdot \frac{d\xi}{2\pi i \xi}\, .
\end{equation}
We will do a contour integral for $\xi$ as in Figure \ref{fig:contour},
which requires analytically continuing this function from $\xi \in \mathcal{C}(0;1)$.
The argument of the square-root in equation (\ref{eq:alphaIntegralFourFifths}) is closely connected
to the quartic function of $\xi$
\begin{equation}
\label{eq:calQ1Def}
\begin{split}
	\mathcal{Q}_1(x;\xi)\, 
	&=\, \big(\xi - x\cdot(\xi^2+1)\big)^2-4x^2\xi^2\\ 
	&=\, \big(x \cdot(\xi^2+1) - (1+2x)\xi\big)\big(x \cdot(\xi^2+1) - (1-2x)\xi\big)\, .
\end{split}
\end{equation}
More precisely, we can rewrite equation (\ref{eq:alphaIntegralFourFifths}) as
\begin{equation}
\label{eq:alphaIntegralFiveSixths}
	\alpha(w,x^2)\,  =\,
\oint_{\mathcal{C}(0;1)}  \frac{1}{\big(\mathcal{Q}_1(x;\xi)/\xi^2\big)^{1/2}-w}\, \cdot \frac{d\xi}{2\pi i \xi}\, ,
\end{equation}
because, for $\xi \neq 0$ we have
\begin{equation}
\label{eq:sqrtArgument}
	\big(1-x\cdot (\xi+2+\xi^{-1})\big)\big(1-x\cdot (\xi-2+\xi^{-1})\big)\, 
	=\, \frac{\mathcal{Q}_1(x;\xi)}{\xi^2}\, .
\end{equation}
We will want to rationalize the denominator of the integrand. Therefore, let us also introduce
another quartic function of $\xi$, 
\begin{equation}
\label{eq:calQ2Def}
\begin{split}
	\mathcal{Q}_2(x,w;\xi)\, 
	&=\, \mathcal{Q}_1(x;\xi)-w^2 \xi^2\\
	&=\, \big(\xi - x\cdot(\xi^2+1)\big)^2-(4x^2+w^2)\xi^2\, .
\end{split}
\end{equation}
If we assume that $x$ and $w$ are both in $[0,\infty)$, then we may rewrite this as 
\begin{equation}
\label{eq:calQ2Def2}
	\mathcal{Q}_2(x,w;\xi)\, 
	=\, \left(x \cdot(\xi^2+1) - \left(1+\sqrt{4x^2+w^2}\right)\xi\right)
	\left(x \cdot(\xi^2+1) - \left(1-\sqrt{4x^2+w^2}\right)\xi\right)\, .
\end{equation}
Now we will begin to simplify the polynomials $\mathcal{Q}_2(x;\cdot)$ and $\mathcal{Q}_2(x,w;\cdot)$.
First we may a quick definition to set notation.
\begin{definition}
Let $\mathcal{U}(z_0;r)$ denote the open unit disk in the complex plane $\{z\, :\, |z-z_0|<r\}$.
Let $\overline{\mathcal{U}}(z_0;r)$ denote its closure $\{z\, :\, |z-z_0|\leq r\}$.
\end{definition}
The following four lemmas will be proved in in Appendix \ref{sec:quadratic}. They all rely on the quadratic formula
for roots of 1-variable quadratic equations.
\begin{figure}
\begin{center}
\begin{tikzpicture}[xscale=1.5,yscale=1.5]
	\draw[very thick,->] (-2.5,0) -- (5,0);
	\draw[very thick,->] (0,-2.5) -- (0,2.5);
	\draw[line width=0.3cm, black!75!white, opacity=0.5] (0.75,0) -- (1.5,0);
	\foreach \t in {0.65,0.7,0.75,...,1.6}{
		\draw[thin] (\t,-0.1) -- (\t,0.1);}
	\fill[black!75!white, opacity=0.5] (0.75,0) -- (0.75,0.1) arc (90:270:0.1cm) -- cycle;
	\fill[black!75!white, opacity=0.5] (1.5,0) -- (1.5,0.1) arc (90:-90:0.1cm) -- cycle;
	\draw (0.65,0.1) -- (0.65,-0.1) node[below] {\small $c_1$};
	\draw (1.6,0.1) -- (1.6,-0.1) node[below] {\small $c_2$};
	\draw (0,0) circle (2cm);
	\fill (0.45,0) circle (2pt) node[above=1pt] {\small $a_1$};
	\fill (1.8,0) circle (2pt) node[above=1pt] {\small $a_2$};
	\begin{scope}[xshift=2.5cm]
	\draw[line width=0.3cm, black!75!white, opacity=0.5] (0.75,0) -- (1.5,0);
	\foreach \t in {0.65,0.7,0.75,...,1.6}{
		\draw[thin] (\t,-0.1) -- (\t,0.1);}
	\fill[black!75!white, opacity=0.5] (0.75,0) -- (0.75,0.1) arc (90:270:0.1cm) -- cycle;
	\fill[black!75!white, opacity=0.5] (1.5,0) -- (1.5,0.1) arc (90:-90:0.1cm) -- cycle;
	\draw (0.65,0.1) -- (0.65,-0.1) node[below] {\small $d_1$};
	\draw (1.6,0.1) -- (1.6,-0.1) node[below] {\small $d_2$};
	\fill (0.35,0) circle (2pt) node[above=1pt] {\small $b_1$};
	\fill (1.9,0) circle (2pt) node[above=1pt] {\small $b_2$};
	\end{scope}

	\draw (45:2cm) node[rotate=135] {\small $\boldsymbol{>}$};
\end{tikzpicture}
\caption{\textsl{A schematic picture -- it is not to scale but it does accurately depict the order of points -- for the branch cuts and poles of the integral in (\ref{eq:alphaIntegralSevenEighths}).
The configuration of points and branch cuts is shown assuming $u,t \in (0,1)$ are sufficiently small.
The poles are at $a_1(x,w)$, $a_2(x,w)$, $b_1(x,w)$ and $b_2(x,w)$.
The branch cuts are the intervals $[c_1(x),c_2(x)]$ and $[d_1(x),d_2(x)]$.
\label{fig:contour}
}}
\end{center}
\end{figure}
\begin{lemma}
\label{lem:calQ1roots}
Suppose that we have a number $x \in (0,1/4)$. Then, defining
\begin{equation}
\begin{split}
	c_1(x)\, &=\, \frac{1+2x-\sqrt{1+4x}}{2x}\, ,\qquad c_2(x)\, =\, \frac{1-2x-\sqrt{1-4x}}{2x}\, ,\\[5pt]
	d_1(x)\, &=\, \frac{1-2x+\sqrt{1-4x}}{2x}\, ,\qquad d_2(x)\, =\, \frac{1+2x+\sqrt{1+4x}}{2x}\, ,
\end{split}
\end{equation}
we have
\begin{equation}
\label{eq:calQ1roots}
	\mathcal{Q}_1(x;\xi)\, =\, x^2 \big(\xi  - c_1(x)\big)\big(\xi-c_2(x)\big)\big(\xi-d_1(x)\big)\big(\xi-d_2(x)\big)\, .
\end{equation}
\end{lemma}
Note in particular that
\begin{equation}
\label{eq:Q1inversive}
	c_1(x)\cdot d_2(x)\, =\, c_2(x) \cdot d_1(x)\, =\, 1\, ,
\end{equation}
which can also be seen since they are the roots of the self-inversive quadratic polynomials of $\xi$ in the ultimate formula
in (\ref{eq:calQ1Def}). 
\begin{lemma}
\label{lem:calQ2roots}
Suppose that we have a number $x \in (0,1/4)$ and another number $w$ satisfying
\begin{equation}
	0\, \leq\, w\, \leq\, \sqrt{1-4x}\, .
\end{equation}
Then, defining
\begin{equation}
\begin{split}
	a_1(x,w)\, &=\, \frac{1+\sqrt{4x^2+w^2}-\sqrt{1+w^2+2\sqrt{4x^2+w^2}}}{2x}\, ,\\[5pt]
	a_2(x,w)\, &=\, \frac{1-\sqrt{4x^2+w^2}-\sqrt{1+w^2-2\sqrt{4x^2+w^2}}}{2x}\, ,\\[5pt]
	b_1(x,w)\, &=\, \frac{1-\sqrt{4x^2+w^2}+\sqrt{1+w^2-2\sqrt{4x^2+w^2}}}{2x}\, ,\\[5pt]
	b_2(x,w)\, &=\, \frac{1+\sqrt{4x^2+w^2}+\sqrt{1+w^2+2\sqrt{4x^2+w^2}}}{2x}\, ,
\end{split}
\end{equation}
we have
\begin{equation}
\label{eq:Q2factorization}
	\mathcal{Q}_2(x,w;\xi)\, =\, x^2\cdot \big(\xi  - a_1(x,w)\big)\big(\xi-a_2(x,w)\big)\big(\xi-b_1(x,w)\big)\big(\xi-b_2(x,w)\big)\, .
\end{equation}
\end{lemma}
Of course,
we also have
\begin{equation}
\label{eq:Q2inversive}
	a_1(x,w)\cdot b_2(x,w)\, =\, a_2(x,w) \cdot b_1(x,w)\, =\, 1\, ,
\end{equation}
because these are the roots of the self-inversive quadratic polynomials of $\xi$ 
in (\ref{eq:calQ2Def}). 
Let us note the following ordering of the roots for the two quartic equations,
as in Figure \ref{fig:contour}.
\begin{lemma}
\label{lem:rootsOrder}
If we have $x \in (0,1/4)$ and $w \in (0,\sqrt{1-4x})$ then we have
\begin{equation}
	0<a_1(x,w)<c_1(x)<c_2(x)<a_2(x,w)<1<b_1(x,w)<d_1(x)<d_2(x)<b_2(x,w)\, .
\end{equation}
\end{lemma}
\begin{figure}
\begin{center}
\begin{tikzpicture}[xscale=5,yscale=5]
	\draw[very thick,->] (-0.5,0) -- (2.5,0);
	\draw[very thick,->] (0,-0.5) -- (0,0.5);
	\foreach \t in {0.65,0.7,0.75,...,1.6}{
		\draw[thin] (\t,-0.05) -- (\t,0.05);}
	\draw (0.65,0.1) -- (0.65,-0.1) node[below] {\small $c_1$};
	\draw (0.65,-0.1) -- (1.6,-0.1);
	\draw (1.125,-0.1) node[rotate=0] {\scriptsize $\boldsymbol{>}$};
	\draw (1.6,0.1) -- (1.6,-0.1) node[below] {\small $c_2$};
	\draw (1.6,0.1) -- (0.65,0.1);
	\draw (1.125,0.1) node[rotate=0] {\scriptsize $\boldsymbol{<}$};
	\fill (0.45,0) circle (1pt) node[above=12pt] {\small $a_1$};
	\draw (0.45,0) circle (0.1cm);
	\draw (0.45,-0.175) node[] {$\Gamma_1(\delta)$};
	\draw (0.45,0) +(45:0.1cm) node[rotate=135] {\scriptsize $\boldsymbol{>}$};
	\fill (1.8,0) circle (1pt) node[above=12pt] {\small $a_2$};
	\draw (1.8,0) circle (0.1cm);
	\draw (1.8,-0.175) node[] {$\Gamma_2(\delta)$};
	\draw (1.8,0) +(45:0.1cm) node[rotate=135] {\scriptsize $\boldsymbol{>}$};
	\draw (1.125,-0.25) node[] {$\Gamma_3(\delta)$};
\end{tikzpicture}
\caption{\textsl{A schematic of the contours after deformation as used in the proof of Lemma \ref{lem:residue1}. The  positively oriented circular contours 
$\Gamma_1(\delta)$ and $\Gamma_2(\delta)$ are of radius $\delta$, centered at the poles $a_1(x,w)$
and $a_2(x,w)$. The branch cut along the real axis interval from $c_1(x)$ to $c_2(x)$ is enclosed by
the contour $\Gamma_3(\delta)$ which is the rectangle traversing the vertices: $c_1(x)-i\delta$, $c_2(x)-i\delta$, $c_2(x)+i\delta$ 
and $c_1(x)+i\delta$, in that order.
\label{fig:Deformation}
}}
\end{center}
\end{figure}
Let us introduce an analytic continuation of the function from (\ref{eq:sqrtArgument}),
$\left(\left(1-x\xi-x\xi^{-1}\right)-4x^2\right)^{1/2}$.
\begin{lemma}
\label{lem:sqrtContinuation}
Assume we have $x \in (0,1/4)$. Define the domain $\mathcal{D}_2(x)$ as 
\begin{equation}
	\mathcal{D}_2(x)\, =\, \mathcal{U}(0;d_1(x)) \setminus \overline{\mathcal{U}}(0;c_1(x))\, .
\end{equation}
Then for all $\xi \in \mathcal{D}_2(x)$, we have $\mathcal{Q}_1(x;\xi)/\xi^2$ is in $\mathcal{D}_1$
from Remark \ref{rem:sqrt}.
So, defining the function,
\begin{equation}
f(x;\cdot) : \mathcal{D}_2(x) \to \C\, ,
\end{equation}
by the formula
\begin{equation}
\label{eq:fDef}
	f(x;\xi)\, =\, \sqrt{\mathcal{Q}_2(x;\xi)/\xi^2}\, =\, \big(\left(1 - x \cdot ( \xi +\xi^{-1})\right)^2-4x^2\big)^{1/2}\, ,
\end{equation}
we have that $f(x;\cdot)$ is analytic.
\end{lemma}
We will prove Lemmas \ref{lem:calQ1roots}, \ref{lem:calQ2roots}, \ref{lem:rootsOrder} 
and \ref{lem:sqrtContinuation} in Appendix \ref{sec:quadratic}.
They are all elementary, and essentially follow by applying the quadratic formula.

We want to deform the contour from the integral in (\ref{eq:alphaIntegralFiveSixths})
as in Figure \ref{fig:Deformation}.
For equation (\ref{eq:alphaIntegralFiveSixths}) we rationalize the denominator.
From equation (\ref{eq:calQ2Def2}) and Lemma \ref{lem:sqrtContinuation}, we may 
rewrite that equation as
\begin{equation}
\label{eq:alphaIntegralSixSevenths}
	\alpha(w,x^2)\,  =\,
\oint_{\mathcal{C}(0;1)}  \frac{\xi\cdot f(x;\xi)+w\cdot \xi}
	{\mathcal{Q}_2(x,w;\xi)}\, \cdot \frac{d\xi}{2\pi i}\, .
\end{equation}
We multiplied numerator and denominator of the first fraction by $\xi^2$,
and then canceled one power from the numerator with the $\xi$ that had been
in the denominator of $d\xi/(2\pi i \xi)$, which is now absent.

To deform this as in as in Figure \ref{fig:Deformation},
we need a more optimal analytic continuation of the function $f(x;\cdot)$.
We start with the domain as in the right-hand picture in Figure \ref{fig:sqrtNew}.
\begin{lemma}
\label{lem:sqrtContinuationB}
Assume we have $x \in (0,1/4)$. Define the domain $\mathcal{D}_3(x)$ as 
\begin{equation}
	\mathcal{D}_3(x)\, =\, \C \setminus \big((-\infty,c_2(x)] \cup [d_1(x),\infty)\big)\, .
\end{equation}
Then define the  function
\begin{equation}
g(x,\cdot) : \mathcal{D}_3(x) \to \C\, ,
\end{equation}
by the formula
\begin{equation}
\label{eq:gDefinition}
	g(x;\xi)\, =\, x\, \cdot \sqrt{\xi-c_1(x)}\, \cdot \sqrt{\xi-c_2(x)}\,
\cdot \sqrt{d_1(x)-\xi}\, \cdot \sqrt{d_2(x)-\xi}\, ,
\end{equation}
where the square-root is as in Remark \ref{rem:sqrt}.
Then $g(x;\cdot)$ is analytic and 
\begin{equation}
\label{eq:gEQUALSf}
	\forall \xi \in \mathcal{D}_2(x)\cap \mathcal{D}_3(x)= \big(\mathcal{U}(0;d_1(x))\setminus \overline{\mathcal{U}}(0;c_1(x))\big)
	\setminus [-d_1(x),-c_1(x)]\, ,\
	\text{ we have }\ g(x;\xi)\, =\, \xi\cdot f(x;\xi)\, . 
\end{equation}
\end{lemma}



\begin{lemma}
\label{lem:sqrtContinuationC}
Assume we have $x \in (0,1/4)$. Define the domain $\mathcal{D}_4(x)$ as 
\begin{equation}
	\mathcal{D}_4(x)\, =\, \C \setminus \big([c_1(x),c_2(x)]\cup[d_1(x),d_2(x)]\big)\, .
\end{equation}
Then define the  function
\begin{equation}
\label{eq:tildegDef1}
	\widetilde{g}(x;\cdot) : \mathcal{D}_4(x) \to \C\, ,
\end{equation}
such that
\begin{equation}
\label{eq:tildegDef2}
	\forall \xi \in \mathcal{D}_3(x) = \Big(\C \setminus \big((-\infty,c_2(x)] \cup [d_1(x),\infty)\big)\Big)\, ,\ \text{ we have }\
	\widetilde{g}(x;\xi)\, =\, g(x;\xi)\, ,
\end{equation}
and
\begin{equation}
\label{eq:tildegDef3}
\forall \xi \in (-\infty,c_1(x)) \cup (d_2(x),\infty)\, ,\ 
\text{ we have }\ \widetilde{g}(x;\xi)\, =\, \lim_{\substack{\zeta \to \xi\\ \zeta \in  \C \setminus \R}}
 g(x;\zeta)\, .
\end{equation}
Then $\widetilde{g}(x;\cdot)$ is analytic and 
\begin{equation}
\label{eq:signCheck}
	\forall \xi \in \mathcal{D}_2(x)\, ,\
	\text{ we have }\ \widetilde{g}(x;\xi)\, =\, \xi \cdot f(x;\xi)\, .
\end{equation}
\end{lemma}

\begin{figure}
\begin{center}
\begin{tikzpicture}[xscale=1,yscale=1]
	\draw[very thick,->] (-2.5,0) -- (5,0);
	\draw[very thick,->] (0,-2.5) -- (0,2.5);
	\draw[line width=0.2cm, black!75!white, opacity=0.5] (0.75,0) -- (1.5,0);
	\foreach \t in {0.65,0.7,0.75,...,1.6}{
		\draw[thin] (\t,-0.1) -- (\t,0.1);}
	\fill[black!75!white, opacity=0.5] (0.75,0) -- (0.75,0.1) arc (90:270:0.1cm) -- cycle;
	\fill[black!75!white, opacity=0.5] (1.5,0) -- (1.5,0.1) arc (90:-90:0.1cm) -- cycle;
	\draw (0.65,0.1) -- (0.65,-0.1) node[below] {\small $c_1$};
	\draw (1.6,0.1) -- (1.6,-0.1) node[below] {\small $c_2$};
	\draw[dashed] (0,0) circle (2cm);
	\begin{scope}[xshift=2.5cm]
	\draw[line width=0.2cm, black!75!white, opacity=0.5] (0.75,0) -- (1.5,0);
	\foreach \t in {0.65,0.7,0.75,...,1.6}{
		\draw[thin] (\t,-0.1) -- (\t,0.1);}
	\fill[black!75!white, opacity=0.5] (0.75,0) -- (0.75,0.1) arc (90:270:0.1cm) -- cycle;
	\fill[black!75!white, opacity=0.5] (1.5,0) -- (1.5,0.1) arc (90:-90:0.1cm) -- cycle;
	\draw (0.65,0.1) -- (0.65,-0.1) node[below] {\small $d_1$};
	\draw (1.6,0.1) -- (1.6,-0.1) node[below] {\small $d_2$};
	\end{scope}


\begin{scope}[xshift=8cm,xscale=0.875,yscale=0.875]
	\draw[dashed] (0,0) circle (2cm);
	\draw[very thick,->] (-2.5,0) -- (6.75,0);
	\draw[very thick,->] (0,-2.5) -- (0,2.5);
	\draw (0.65,0.1) -- (0.65,-0.1) node[below] {\small $c_1$};
	\fill[black!25!white,opacity=0.375] (-2.5,0.1) -- (0.65,0.1) -- (0.65,-0.1) -- (-2.5,-0.1) -- cycle;
	\draw[<->,thin] (-2.5,0.1) -- (0.65,0.1) -- (0.65,-0.1) -- (-2.5,-0.1);
	\draw (1.6,0.1) -- (1.6,-0.1) node[below] {\small $c_2$};
	\fill[black!25!white,opacity=0.375] (-2.5,0.2) -- (1.6,0.2) -- (1.6,-0.2) -- (-2.5,-0.2) -- cycle;
	\draw[<->,thin] (-2.5,0.2) -- (1.6,0.2) -- (1.6,-0.2) -- (-2.5,-0.2);
	\begin{scope}[xshift=2.5cm]
	\draw (1.6,0.1) -- (1.6,-0.1) node[below] {\small $d_2$};
	\fill[black!25!white,opacity=0.375] (4.25,0.1) -- (1.6,0.1) -- (1.6,-0.1) -- (4.25,-0.1) -- cycle;
	\draw[<->,thin] (4.25,0.1) -- (1.6,0.1) -- (1.6,-0.1) -- (4.25,-0.1);
	\draw (0.65,0.1) -- (0.65,-0.1) node[below] {\small $d_1$};
	\fill[black!25!white,opacity=0.375] (4.25,0.2) -- (0.65,0.2) -- (0.65,-0.2) -- (4.25,-0.2) -- cycle;
	\draw[<->,thin] (4.25,0.2) -- (0.65,0.2) -- (0.65,-0.2) -- (4.25,-0.2);
	\end{scope}
\end{scope}
\end{tikzpicture}
\caption{\textsl{The branch cuts for the function $\widetilde{g}(x;\cdot)$ are shown on the left,
which is an analytic continuation of the function $f(x;\xi)=\sqrt{\mathcal{Q}_1(\xi)/\xi^2}$
defined in a neighborhood of $\mathcal{C}(0;1)$.
In the figure on the right we show the {\em a priori} overlapping branch-cuts of the original
analytic continuation $g(x;\cdot)$.
\label{fig:sqrtNew}
}}
\end{center}
\end{figure}
The domain for the function $\widetilde{g}(x;\cdot)$ is as in the left-hand picture in Figure \ref{fig:sqrtNew}.


We prove Lemmas \ref{lem:sqrtContinuationB} and \ref{lem:sqrtContinuationC} in 
Appendix \ref{sec:Deform}.
Then equation (\ref{eq:alphaIntegralSixSevenths}) may be rewritten as 
\begin{equation}
\label{eq:alphaIntegralSevenEighths}
	\alpha(w,x^2)\,  =\,
\oint_{\mathcal{C}(0;1)}  \frac{\widetilde{g}(x;\xi)+w\cdot \xi}
	{\mathcal{Q}_2(x,w;\xi)}\, \cdot \frac{d\xi}{2\pi i}\, ,
\end{equation}
where the roots of $\mathcal{Q}_2(x,w;\cdot)$ are $a_1(x;w)$, $a_2(x;w)$, $b_1(x;w)$ and $b_2(x;w)$,
and where the domain of $\widetilde{g}(x;\cdot)$ is all of $\C$ except for the union 
of the two intervals $[c_1(x),c_2(x)]$ and $[d_1(x),d_2(x)]$.
Thus we obtain the region  as in Figure \ref{fig:contour}.
This is the region where we may deform the contour $\mathcal{C}(0;1)$.
