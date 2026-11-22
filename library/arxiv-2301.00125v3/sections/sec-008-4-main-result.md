---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem"
section_id: sec-008-4-main-result
section_title: "Main result"
section_number: 4
pages: 12-16
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 1.0
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem — Given a uniform random permutation π ∈Sn, let Zn,k be equal to the number of increasing"
---
\label{sec:Main}
Using equations (\ref{eq:Q2factorization}) and (\ref{eq:alphaIntegralSevenEighths}), we know
\begin{equation}
\label{eq:alphaIntegralSevenEights}
	\alpha(w,x^2)\,  =\,
\oint_{\mathcal{C}(0;1)}  \frac{w\cdot \xi+\widetilde{g}(x;\xi)}
{x^2\cdot \big(\xi  - \mathcal{A}_1(x,w)\big)\big(\xi-\mathcal{A}_2(x,w)\big)\big(\xi-b_1(x,w)\big)\big(\xi-b_2(x,w)\big)}\, 
\cdot \frac{d\xi}{2\pi i}\, .
\end{equation}
We will deform the contour from $\mathcal{C}(0;1)$ into the open disk $\mathcal{U}(0;1)$ shrinking to contours around the poles
$\mathcal{A}_1(x,w)$ and $\mathcal{A}_2(x,w)$ and also around the
branch cut $[c_1(x),c_2(x)]$ as in Figure \ref{fig:Deformation}.
\begin{lemma}
\label{lem:residue1}
For $x,w \in (0,\infty)$ satisying $4x+w^2<1$ we have
\begin{equation}
	\alpha(w,x^2)\, =\, \mathcal{A}_1(x,w) + \mathcal{A}_2(x,w)\, ,
\end{equation}
for the function $\mathcal{A}_1(x,w)$ given by the residue theorem
\begin{equation}
\label{eq:A1formula}
\begin{split}
	\mathcal{A}_1(x,w)\, &=\, \frac{w\cdot a_1(x,w)+\widetilde{g}\big(x;a_1(x,w)\big)}
{x^2\cdot \big(a_1(x,w)-a_2(x,w)\big)\big(a_1(x,w)-b_1(x,w)\big)\big(a_1(x,w)-b_2(x,w)\big)}\\[5pt]
&\qquad
+\frac{w\cdot a_2(x,w)+\widetilde{g}\big(x;a_2(x,w)\big)}
{x^2\cdot \big(a_2(x,w)-a_1(x,w)\big)\big(a_2(x,w)-b_1(x,w)\big)\big(a_2(x,w)-b_2(x,w)\big)}\, ,
\end{split}
\end{equation}
and for the function $\mathcal{A}_2(x,w)$ given by the integral
\begin{equation}
\label{eq:A2formula}
	\mathcal{A}_2(x,w)\, =\, \frac{1}{\pi}\cdot \int_{c_1(x)}^{c_2(x)} \mathcal{I}_2(x,w;r)\, dr\, ,
\end{equation}
where
\begin{equation}
	\forall r \in [c_1(x),c_2(x)]\, ,\ \text{ we have }\ \mathcal{I}_2(x,w;r)\, =\, \frac{i\cdot \widetilde{g}_{+}(x;r)-i\cdot \widetilde{g}_-(x;r)}
	{2\mathcal{Q}_2(x,w;r)}\, , 
\end{equation}
for the functions $\widetilde{g}_+(x;\cdot)$ and $\widetilde{g}_-(x;\cdot)$ defined such that
\begin{equation}
	\forall r \in [c_1(x),c_2(x)]\, ,\ \text{ we have }\ \widetilde{g}_{\pm}(x;r)\, =\, \lim_{\epsilon \to 0^+} \widetilde{g}(x;r\pm i \epsilon)\, .
\end{equation}
\end{lemma}
This lemma is elementary and will be proved in Appendix \ref{sec:residue}.
Note that since $w\cdot \xi/\mathcal{Q}_2(x,\xi)$ is analytic for $\xi$ in a neighborhood
of $[c_1(x),c_2(x)]$, its contribution to the integral along $\Gamma_3(\delta)$ vanishes.
See Figure \ref{fig:Deformation}.
That is why it is not included in $\mathcal{I}_2(x,w;r)$.

Note that $\mathcal{A}_1(x,w)$ and $\mathcal{A}_2(x,w)$ are roots of $\mathcal{Q}_2(x,w;\xi)$ which is 
$\mathcal{Q}_1(x;\xi)-w^2 \xi^2$ as in (\ref{eq:calQ2Def}) and (\ref{eq:Q2factorization}). 
But $\big(\widetilde{g}(x;\xi)\big)^2 = \mathcal{Q}_1(x;\xi)$ 
by (\ref{eq:fDef}) and (\ref{eq:signCheck}).
Therefore, $w\cdot a_j(x,w)+\widetilde{g}(x;a_j(x,w))$ may be simplified for $j=1,2$
in the formula for $\mathcal{A}_1(x,w)$.
\begin{lemma} For $x,w \in (0,\infty)$ satisfying $4x+w^2<1$ we have
\begin{equation}
\label{eq:A1formula2}
\begin{split}
	\mathcal{A}_1(x,w)\, &=\, \frac{2w\cdot a_1(x,w)}
{x^2\cdot \big(a_1(x,w)-a_2(x,w)\big)\big(a_1(x,w)-b_1(x,w)\big)\big(a_1(x,w)-b_2(x,w)\big)}\\[5pt]
&\qquad
+\frac{2w\cdot a_2(x,w)}
{x^2\cdot \big(a_2(x,w)-a_1(x,w)\big)\big(a_2(x,w)-b_1(x,w)\big)\big(a_2(x,w)-b_2(x,w)\big)}\, ,
\end{split}
\end{equation}
or simplifying
\begin{equation}
\label{eq:A1formula3}
	a_1(x,w)\, =\, \frac{2w\cdot \big(b_1(x,w)\cdot b_2(x,w) - a_1(x,w) \cdot a_2(x,w)\big)}
{x^2\prod_{j=1}^{2} \prod_{k=1}^{2} \big(b_j(x,w)-a_k(x,w)\big)}\, .
\end{equation}
\end{lemma}
We will prove this lemma in Appendix \ref{sec:residue}.
Recall from equation (\ref{eq:Q2inversive}) that $b_2(x,w) = 1/a_1(x,w)$ and $b_1(x,w)=1/a_2(x,w)$.
From this one may simplify a bit more.
\begin{lemma} For $x,w \in (0,\infty)$ satisfying $4x+w^2<1$ we have
\begin{equation}
\label{eq:A1formula4}
\begin{split}
	\mathcal{A}_1(x,w)\, =\, \frac{2w\cdot a_1(x,w) \cdot a_2(x,w) \Big(1+ a_1(x,w) \cdot a_2(x,w)\Big)}
{x^2 \cdot\Big(1-a_1(x,w)\cdot a_2(x,w)\Big) \Big(1-\big(a_1(x,w)\big)^2\Big)
\Big(1-\big(a_2(x,w)\big)^2\Big)}\, .
\end{split}
\end{equation}
\end{lemma}
\begin{figure}
\begin{center}
\begin{tikzpicture}[xscale=4,yscale=4]
	\draw[dashed] (2,0) arc (0:15:2cm);
	\draw[dashed] (2,0) arc (0:-15:2cm);
	\draw[very thick,->] (-0.5,0) -- (2.5,0);
	\draw[very thick,->] (0,-0.675) -- (0,0.675);
	\draw (0.65,0.1) -- (0.65,-0.1) node[below] {\small $c_1$};
	\draw (1.6,0.1) -- (1.6,-0.1) node[below] {\small $c_2$};
	\draw (0.65,0) -- (1,0.5) -- (1.6,0);
	\draw (1,0.5) node[] {$\bullet$};
	\draw[] (0.65,0) +(0:0.2cm) arc (0:55:0.2cm);
	\draw (0.65,0) +(47.5:0.2cm) node[rotate=-45] {\small $<$};
	\draw[] (1.6,0) +(0:0.2cm) arc (0:140:0.2cm);
	\draw (1.6,0) +(135:0.2cm) node[rotate=45] {\small $<$};
	\draw[dotted] (1,0) -- (1,0.5);
	\draw (1,0.5) node[above] {$\xi = r + i \epsilon$};
	\draw (0.65,0) +(0:0.2cm) node[above left] {\small $\theta_1$};
	\draw (1.6,0) +(0:0.2cm) node[above left] {\small $\theta_2$};
\end{tikzpicture}
\caption{\textsl{Consideration of the phase of the function,  $\widetilde{g}(x;\xi) = \sqrt{\mathcal{Q}_1(x;\xi)}$, for $\xi=r+i\epsilon$
with $c_1(x)\leq r\leq c_2(x)$.
If we write $\widetilde{g}(x;\xi)$ as $e^{i \varphi} R$ for $R \geq 0$ and $\varphi \in \R$
then by ``phase'' we mean $e^{i\varphi}$. For $r \in \R \setminus \{c_1(x),c_2(x),d_1(x),d_2(x)\}$, and taking 
$\xi = r + i\delta$ the phase $e^{i\varphi}$
converges to a number $\Omega_+(r) \in \{1,i,-1,-i\}$ in the $\delta \to 0^+$ limit. Similarly for the limit of the phase from the lower half-plane $\Omega_-(r)$.
\label{fig:sqrtNew2}
}}
\end{center}
\end{figure}
This elementary lemma will also be proved in Appendix \ref{sec:residue}.

\begin{lemma}
\label{lem:calA2penultimate}
For $x,w \in (0,\infty)$ satisfying $4x+w^2<1$, it is the case that
\begin{equation}
	\forall r \in [c_1(x),c_2(x)]\, ,\ \text{ we have }\	\pm i \cdot \widetilde{g}_{\pm}(x,r)\,
	=\, -\sqrt{-\mathcal{Q}_1(x;r)}\, ,
\end{equation}
where note that $\mathcal{Q}_1(x;r)\leq 0$ for all $r \in [c_1(x),c_2(x)]$. In particular 
\begin{equation}
\label{eq:A2formula2}
	\mathcal{A}_2(x,w)\, =\, \frac{1}{\pi}\, \int_{c_1(x)}^{c_2(x)} \frac{\sqrt{-\mathcal{Q}_1(x;r)}}{-\mathcal{Q}_2(x,w;r)}\, dr\, ,
\end{equation}
where also  $\mathcal{Q}_2(x,w;r)<0$
for $r \in [c_1(x),c_2(x)]$, since $a_1(x,r)<c_1(x)<c_2(x)<a_2(x,r)$.
\end{lemma}
We will give the details of the proof in Appendix \ref{sec:residue}. But we may indicate the key to the calculation by referring to
Figure \ref{fig:sqrtNew2}.
Recall from equation (\ref{eq:calQ1roots}) and (\ref{eq:gDefinition}) that $\widetilde{g}(x;\cdot)$ is an 
analytic continuations of $\sqrt{\mathcal{Q}_1(x,\cdot)}$. 
More precisely, we had a function $f(x;\cdot)$ defined on $\mathcal{D}_2(x)$
such that $f(x;\xi) = \sqrt{\mathcal{Q}_1(x;\xi)/\xi^2}$.
Then $\widetilde{g}(x;\cdot)$ is defined on the region $\mathcal{D}_4(x)$ and $\widetilde{g}(x;\xi) = \xi\cdot f(x;\xi)$ on $\mathcal{D}_2(x)$  (which is a subset of $\mathcal{D}_4(x)$).
It is easy to see that
\begin{equation}
	\forall r \in [c_1(x),c_2(x)]\, ,\ \text{ we have } \lim_{\epsilon \to 0^+} \left|\widetilde{g}(x;r+i\epsilon)\right|\,
	=\, 	\lim_{\epsilon \to 0^+} \left|\widetilde{g}(x;r-i\epsilon)\right|\,
	=\, \sqrt{-\mathcal{Q}_1(x;r)}\, ,
\end{equation}
because $\mathcal{Q}_1(x;r)\leq 0$ for all $r \in [c_1(x),c_2(x)]$.
So all that remain is to determine the phase, meaning $\widetilde{g}_{\pm}(x;r)/|\widetilde{g}_{\pm}(x;r)|$.
Let us call that $\Omega_{\pm}(x;r)$. Then as in Figure 5, we may see that $\Omega_{\pm}(x;r) = \pm i$, mainly because
in the product of the four square roots, exactly one has an argument which is ``approximately negative,'' being such that the phase of the argument of that square root is equal to:
$e^{i (\pi - \delta)}$ for $\xi=r+i\epsilon$,
and $e^{-i(\pi-\delta)}$ for $\xi = r-i\epsilon$, where the quantity $\delta$
is such that $\delta \to 0^+$ when $\epsilon \to 0^+$.
Taking the square-roots we get  $\Omega_{\pm}(x;r) = \pm i$.
We give more careful details in Appendix \ref{sec:residue}.

Note that the integral equation (\ref{eq:A2formula2}) is an elliptic integral:  $\mathcal{A}_2(x,w)$ can be put into the form
\begin{equation}
\label{eq:A2formula2}
\begin{split}
&\hspace{-1cm}
	\frac{1}{\pi}\cdot \int_{c_1(x)}^{c_2(x)} \frac{x\cdot \sqrt{r-c_1(x)}\, \cdot \sqrt{c_2(x)-r}\,
\cdot \sqrt{d_1(x)-r}\, \cdot \sqrt{d_2(x)-r}}{-\mathcal{Q}_2(x,w;r)}\, dr\\[3pt]
&\hspace{2cm} =\,  \int_{c_1(x)}^{c_2(x)} \frac{\mathcal{R}(x,w;r)}{\sqrt{r-c_1(x)}\, \cdot \sqrt{c_2(x)-r}\,
\cdot \sqrt{d_1(x)-r}\, \cdot \sqrt{d_2(x)-r}}\, dr\, ,
\end{split}
\end{equation}
where $\mathcal{R}(x,w;\cdot) : \C \to \C \cup \{\infty\}$ is a rational (meromorphic function), and we note that the 
denominator on the left-hand-side is the square-root of a quartic function.
But for the Legendre normal form for elliptic integrals, we prefer to use a linear fractional transformation
to transform to a quartic of the form
\begin{equation}
\label{eq:quarticNormalForm}
(1-r^2)(1-k^2 r^2)\, =\, k^2 \cdot (r-1)(r+1)(r-k^{-1})(r+k^{-1})\, ,
\end{equation}
for some number $k \in (0,1)$.
In other words, for the normal form, the roots of the quartic should come in pairs which are additive inverses.
For $\mathcal{Q}_1(x,w;r)$, the roots come in pairs which are multiplicative reciprocals (\ref{eq:Q1inversive}).

To reduce an elliptic integral to normal form one generally applies one or more
linear fractional transfomations $L(r) = (ar+b)/(cr+d)$, for example with $ad-bc=1$
and $a,b,c,d \in \R$ having inverse $L^{-1}(s) = (ds-b)/(-cs+a)$, using a substitution $r=L^{-1}(s)$.
This is a good type of transformation for such a problem.
Precomposing with $L^{-1}$ has good properties for rational functions.
Such a mapping also takes the quartic function inside the square-root to another quartic function, 
modulo multiplying by an even power of the denominator $(-cs+a)$.
It should be mentioned that $dr=dL^{-1}(s)$ also produces an even power of $(-cx+a)$.

Therefore we note, that within the family of linear fractional transformations there is one (and its inverse)
which intertwines between pairs of numbers which are multiplicative reciprocals
and pairs of numbers which are additive inverses.
It is 
\begin{equation}
\label{eq:calLdef}
	\mathcal{L}(z)\, =\, \frac{z-1}{z+1}\, ,\ \text{ with }\ \mathcal{L}^{-1}(\xi)\, =\, \frac{1+\xi}{1-\xi}\, .
\end{equation}
This satisfies $\mathcal{L}(1/z) = -\mathcal{L}(z)$ and $\mathcal{L}(-z)=1/\mathcal{L}(z)$.
After performing this transformation and rescaling, we do replace the quartic $\mathcal{Q}_1(x;r)$
by the normal form of (\ref{eq:quarticNormalForm}), with
\begin{equation}
	k^2\, =\, \big(K_1(x)\big)^2\, ,\ \text{ where }\ K_1(x)\, =\, \sqrt{1-4x^2}\, .
\end{equation}
Then the path of integration is the interval between two of the roots of (\ref{eq:quarticNormalForm}),
$1$ and $1/k$. 
We do want the path of integration to be an invterval joining two of the roots of (\ref{eq:quarticNormalForm})
to get a complete elliptic integral, which is a bit simpler than the incomplete integrals.
Unfortunately, for the Legendre normal form of an elliptic integral, it is preferred that the 
path of integration is between the pair of roots $-1$ and $1$ (instead of between the pair $1$ and $1/k$). 
So, we use another linear fractional transformation to permute the roots cyclically, while also changing $k$
from $K_1(x)$ to another value. 
The linear fractional transformation is
\begin{equation}
	\Lambda(k;z)\, =\, \frac{\left(k^{-1/2}+1\right)\left(z-k^{-1/2}\right)}
{\left(k^{-1/2}-1\right)\left(z+k^{-1/2}\right)}\, ,\ \text{ with }\
	\Lambda^{-1}(k;\xi)\, =\, k^{-1/2}\, \cdot \frac{k^{-1/2}+1+\left(k^{-1/2}-1\right)\xi}
{k^{-1/2}+1-\left(k^{-1/2}-1\right)\xi}\, ,
\end{equation}
which has the property
\begin{equation}
	\Lambda(k;k^{-1})\, =\, 1\, ,\ \Lambda(k;1)\, =\, -1\, ,\ 
	\Lambda(k;-1)\, =\, -1/\mathcal{J}(k)\ \text{ and }\
	\Lambda(k;-k^{-1})\, =\, 1/\mathcal{J}(k)\, ,
\end{equation}
for the involution $\mathcal{J} : (0,1) \to (0,1)$ given by
\begin{equation}
	\mathcal{J}(k)\, =\, (1-k^{1/2})^2/(1+k^{1/2})^2\, .
\end{equation}
It may be worthwhile to note that $\mathcal{J}$ is a decreasing function on $(0,1)$ with fixed point $(\sqrt{2}-1)^2$.

After performing the second linear fractional transformation using
$\Lambda(K_1(x);\cdot)$ and $\Lambda^{-1}(K_1(x);\cdot)$,
we do obtain another elliptic integral with the quartic of the form of (\ref{eq:quarticNormalForm})
now with
\begin{equation}
	k^2\, =\, (K_2(x))^2\, ,\ \text{ where }\ K_2(x)\, =\,\mathcal{J}(K_1(x))\,
	=\, \left(\frac{1-(1-4x^2)^{1/4}}{1+(1-4x^2)^{1/4}}\right)^2\, .
\end{equation}
And the path of integration is the interval from $-1$ to $1$, as desired.










































































































\begin{theorem}
\label{thm:rewrite}
As usual, denote the complete elliptic integral of the first kind as 
\begin{equation}
\label{eq:FirstKind}
	K(k)\, =\, \int_0^1 \frac{1}{\sqrt{(1-t^2)(1-k^2t^2)}}\, dt\, ,
\end{equation}
and let the complete elliptic integral of the third kind be
\begin{equation}
	\Pi(k;\lambda)\, =\, \int_0^1 \frac{1}{\sqrt{(1-t^2)(1-k^2 t^2)}}\cdot \frac{1}{1-\lambda t}\, dt\, .
\end{equation}
Then we have that $\mathcal{A}_2(x,w)$ can be written as a linear combination of terms of the form
$\phi_i(x,w) \Pi(\psi_i(x,w))$ (with at most 4 terms) where each $\phi_i$ and $\psi_i$ are algebraic
expressions.
Hence the generating function $\alpha(w,z)$ is an expression involving algebraic functions
and a linear combination of several $\Pi$-functions, viewed as a vector over the field of algebraic functions
(other than the identically zero function).
\end{theorem}

We note that occasionally leading theoretical physicists make contributions to algebra and number theory
by determining certain physical quantities in terms of algebraic or number theoretic expressions.
For example, Boos, Korepin, Nishiyama and Shiroishi found that certain correlation functions of the XXZ ground
state (for the quantum spin chain) are expressible in terms of rational linear combinations of the products of
$\ln(2)$ and factors of the Riemann zeta functions $\zeta$ evaluated at the first $n$ odd positive integers
\cite{KorepinEtAl}.
Our main theorem may be viewed as following their model.

The following is an {important remark.}
\begin{remark}
\label{rem:PinskySRW}
In \cite{Pinsky1}, Ross Pinsky proved the combinatorial fact
\begin{equation}
\label{eq:Pinsky2}
	\frac{A(N,j)}{\binom{2N}{N}\binom{2N}{N}}\, =\, 
	\sum_{\substack{t_1,\dots,t_j \in \Z\\0\leq t_1\leq\dots\leq t_j\leq 2N}} 
\mathbf{P}\big( U_{t_1}=\dots=U_{t_j}=0\, \big|\, U_{2N}=V_{2N}=0\big)\, ,
\end{equation}
where $(U_t,V_t)$ performs the standard $d=2$ dimensional SRW starting from $(0,0)$.
See his equation 4.2 in the first part of his proof of his Lemma 2.
\end{remark}

The standard $d=2$ dimensional SRW is such that $(U_{t+1}-U_t,V_{t+1}-V_t)$ are iid increments equally likely
to be any of the four elements from $\{(1,0),(0,1),(-1,0),(0,-1)\}$.
The transformation that Pinsky gives in his paper is $(X_t,Y_t) = (U_t+V_t,U_t-V_t)$,
so that $X_t$ and $Y_t$ independently perform $d=1$ dimensional SRWs.
Then it is seen that $\mathbf{P}(U_{2N}=V_{2N}=0)=2^{-4N} \binom{2N}{N}\binom{2N}{N}$. Therefore, Pinsky's formula (\ref{eq:Pinsky2}) can be rewritten as
\begin{equation}
\label{eq:PrePolya}
	2^{-4N} A(N,j)\, =\, \sum_{\substack{t_1,\dots,t_j \in \Z\\0<t_1<\dots<t_j<2N}} 
\mathbf{P}\big( U_{t_1}=\dots=U_{t_j}=0\ \text{ and }\ U_{2N}=V_{2N}=0\big)\, ,
\end{equation}
This is also related to P\'olya's $d=2$ dimensional result.
We point to McKean's textbook, in which he discusses
P\'olya's result in Section 4.3, \cite{McKean}. 
That is more accessible than P\'olya's original \cite{Polya}.
The precise formula of P\'olya is the following
\begin{equation}
	\sum_{N=0}^{\infty} \mathbf{P}(U_{2N}=V_{2N}=0) z^N\, =\, \frac{1}{\pi}\, K(z)\, ,
\end{equation}
for $|z|<1$, where $K(z)$ is as in (\ref{eq:FirstKind}).
Let us perform a consistency check for our main formulas by 
noting that when $w=0$ we have $\mathcal{A}_1(x,w)=\mathcal{A}_1(x,0)=0$ due to formula 
(\ref{eq:A2formula2}).
But in Lemma \ref{lem:calA2penultimate}, if we send $w \to 0$, we have 
\begin{equation}
-\mathcal{Q}_2(x,w;r)\, =\, 
-\mathcal{Q}_2(x,0;r)\, =\, -\mathcal{Q}_1(x;r)\, .
\end{equation}
But then, by Lemma \ref{lem:residue1}, we have
\begin{equation}
	\alpha(0,x^2)\, =\, 0 + \mathcal{A}_2(x,0)\, =\, \frac{1}{ \pi x}\, \int_{c_1(x)}^{c_2(x)} 
\frac{1}{\sqrt{\big(r-c_1(x)\big)\big(c_2(x)-r\big)\big(\frac{1}{c_1(x)}-r\big)\big(\frac{1}{c_2(x)}-r\big)}}\, dr\, .
\end{equation}
Using the methods of Appendix \ref{sec:Elliptic}, this can be seen to give the desired specialization $\alpha(x,w=0)=K(x)/\pi$.
