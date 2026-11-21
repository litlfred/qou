---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem"
section_id: sec-006-2-pinskys-combinatorial-second-moment-formula
section_title: "Pinsky's combinatorial second moment formula"
section_number: 2
pages: 5-8
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.98
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem — Given a uniform random permutation π ∈Sn, let Zn,k be equal to the number of increasing"
---
{
In his paper \cite{Pinsky1}, Pinsky calculated
\begin{equation}
	\mathbf{E}\left[Z_{n,k}^2\right]\, =\, \sum_{i=0}^{k}A(k-i,i)\, B(n,2k-i),
\end{equation}
where for any $N,j \in \{0,1,\dots\}$, we have
\begin{equation}
	B(N,j)\, =\, \binom{N}{j} \cdot \frac{1}{j!}\, ,
\end{equation}
and 
\begin{equation}
	A(N,j)\, =\, \sum_{\substack{\ell_0,\dots,\ell_j \in \{0,1,\dots\}\\ \ell_0+\dots+\ell_j=N}}\
	\sum_{\substack{m_0,\dots,m_j \in \{0,1,\dots\}\\ m_0+\dots+m_j=N}}\
	\prod_{r=0}^{j} \left(\binom{\ell_r+m_r}{\ell_r,m_r}\right)^2\, .
\end{equation}
See Pinsky's Proposition 2. We will not reproduce his proof, but we mention that his argument is elegant.


Let us define the new quantity
\begin{equation}
	K(L,M,j)\, =\, \sum_{\substack{\ell_0,\dots,\ell_j \in \{0,1,\dots\}\\ \ell_0+\dots+\ell_j=L}}\
	\sum_{\substack{m_0,\dots,m_j \in \{0,1,\dots\}\\ m_0+\dots+m_j=M}}\
	\prod_{r=0}^{j} \left(\binom{\ell_r+m_r}{\ell_r,m_r}\right)^2\, .
\end{equation}
Then we have $A(N,j) = K(N,N,j)$.
Let us define the generating function
\begin{equation}
	\kappa(w,x,y)\, =\, \sum_{j=0}^{\infty} \sum_{L=0}^{\infty} \sum_{M=0}^{\infty} w^j x^L y^M K(L,M,j)\, ,
\end{equation}
for  $x,y,w \in \C$.
Then for $w,x,y \in [0,\infty)$, we have
\begin{equation}
\label{eq:betaSecondFormula}
	\kappa(w,x,y)\, =\, \sum_{j=0}^{\infty}  w^j \left(\sum_{\ell=0}^{\infty}\ \sum_{m=0}^{\infty} x^{\ell} y^{m} \left(\binom{\ell+m}{\ell,m}\right)^2\right)^{j+1}\, ,
\end{equation}
by the Tonelli theorem. (See for example, Section 2.5 of Folland \cite{Folland}.) So the left-hand-side
diverges if and only if the right-hand-side diverges. If neither diverges, the numerical equality 
is valid.
Also, if neither diverges for a choice of $x=x_1$, $y=y_1$, $w=w_1$ for $x_1,y_1,w_1 \in [0,\infty)$, then for any complex numbers $x,y,w \in \C$ such that 
$|x|\leq x_1$, $|y|\leq y_1$ and $|z|\leq z_1$, the two sides of (\ref{eq:betaSecondFormula}) are convergent 
and there is equality of the two sides  by Fubini's theorem.
Given $|x|,|y| \in [0,1/4)$, let us define
\begin{equation}
\label{eq:gamma2def}
	\varkappa^{(2)}(x,y)\, =\, \sum_{\ell=0}^{\infty} \sum_{m=0}^{\infty} x^\ell y^m \left(\binom{\ell+m}{\ell,m}\right)^2\, ,
\end{equation}
so that, according to (\ref{eq:betaSecondFormula}),
\begin{equation}
\label{eq:betaSecondFormula2}
	\kappa(w,x,y)\, =\, \sum_{j=0}^{\infty}  w^j \left(\varkappa^{(2)}(x,y)\right)^{j+1}\, .
\end{equation}
The reason we have denoted the function in (\ref{eq:gamma2def}) as $\varkappa^{(2)}$, with the superscript index $2$, is that
it bears a relation to a more famous generating function, which we call $\varkappa^{(1)}$:
\begin{equation}
	\forall x,y \in \left[0\, ,\ 1/2\right)\, ,\ \text{ we define }\ \varkappa^{(1)}(x,y)\, =\, \sum_{\ell,m=0}^{\infty} \binom{\ell+m}{\ell,m} x^{\ell} y^m\, ,
\end{equation}
using the multinomial notation for the binomial coefficient 
$\binom{\ell+m}{\ell,m} = \frac{(\ell+m)!}{\ell!\, m!}$.
We have 
\begin{equation}
	\varkappa^{(1)}(x,y)\, =\, \sum_{n=0}^{\infty} (x+y)^n\, =\, \frac{1}{1-(x+y)}\, .
\end{equation}
The function that we have called $\varkappa^{(1)}$ is among the first examples in many textbooks on generating functions. See, for example, Pemantle and Wilson's Example 2.2.2 in \cite{PemantleWilson}.

The relation between $\varkappa^{(1)}$ and $\varkappa^{(2)}$ is as follows.
Taking the product of $\varkappa^{(1)}(x,y)$ and $\varkappa^{(1)}(u,v)$ and then multiplying $x$ by $\xi$ and $u$ by $\xi^{-1}$,
and multiplying $y$ by $\zeta$ and $v$ by $\zeta^{-1}$,  we have
\begin{equation}
	\varkappa^{(1)}(x\xi,y\zeta) \cdot \varkappa^{(1)}\left(\frac{u}{\xi}\, ,\ \frac{v}{\zeta}\right)\, =\, \sum_{\ell,m,k,n=0}^{\infty} \binom{\ell+m}{\ell,m} \binom{k+n}{k,n}
	x^\ell y^m u^k v^n \xi^{\ell-k} \zeta^{m-n}\, .
\end{equation}
Therefore, integrating over unit circles, 
and using the residue method:
\begin{equation}
\label{eq:gamma2contour}
	\varkappa^{(2)}(xu,yv)\, =\, \oint_{\mathcal{C}(0;1)} \oint_{\mathcal{C}(0;1)} \varkappa^{(1)}(x\xi,y\zeta) \cdot \varkappa^{(1)}\left(\frac{u}{\xi}\, ,\ \frac{v}{\zeta}\right)\, \frac{d\xi}{2\pi i \xi}\, \cdot
	\frac{d\zeta}{2\pi i \zeta}\, .
\end{equation}
\begin{definition}
Let $\mathcal{C}(z_0;r)$ denote the circle in the complex plane $\{z\, :\, |z-z_0|=r\}$,
which may be parametrized as $z = z_0 + r e^{i\theta}$ for $-\pi<\theta\leq \pi$.
\end{definition}
One can perform the integral to calculate the following.
\begin{figure}
\begin{center}
\begin{tikzpicture}[xscale=1.5,yscale=1.5]
	\draw[very thick,->] (-2.5,0) -- (2.5,0);
	\draw[very thick,->] (0,-2.5) -- (0,2.5);
	\foreach \t in {-2.5,-2.375,-2.25,...,-0.25}{
		\draw[thin] (\t,-0.1) -- +(0.25,0.2);}
	\draw[thin] (-0.125,-0.1) -- (0,0);
	\draw[thin] (-2.5,0) -- (-2.375,0.1);
	\draw (-2.5,0.1) -- (0,0.1) arc (90:-90:0.1cm) --  (-2.5,-0.1);
	\fill[black!75!white, opacity=0.5] (-2.5,0.1) -- (0,0.1) arc (90:-90:0.1cm) --  (-2.5,-0.1) -- cycle;
	\draw[<->] (-175:2cm) arc (-175:175:2cm);
	\draw (1,0.75) node[] {$z=r e^{i\theta}$};
	\draw (3,1) node[] {$r>0$ and};
	\draw (3,0.5) node[] {$-\pi<\theta<\pi$};
	\draw (2.75,-1.25) node[] {$\sqrt{z}=\sqrt{r}\, e^{i\theta/2}$};
	\draw (3.5,-1.25) node[right] {$=\exp((1/2) \log(z))$};



















\end{tikzpicture}
\caption{\textsl{Schematic for the standard square-root function on the open domain of $\C$ with branch cut along the non-positive
real axis: $\mathcal{D}_1 = \{r e^{i\theta}\, :\, r>0\, ,\ -\pi<\theta<\pi\}$. For $z \in \mathcal{D}_1$
we use the formula
$\sqrt{z} = \exp((1/2) \int_0^1 (z-1)(1+t(z-1))^{-1}\, dt)$. \label{fig:sqrt}
}}
\end{center}
\end{figure}
\begin{lemma}
\label{lem:gamma2}
Given $|x|,|y| \in [0,1/4)$, 
the series in (\ref{eq:gamma2def}) converges and 
\begin{equation}
\label{eq:gamma2formula}
	\varkappa^{(2)}(x,y)\, =\, \left(\sqrt{\left(1-\left(x+y\right)\right)^2 - 4 xy}\right)^{-1}\, .
\end{equation}
\end{lemma}
\begin{remark}
\label{rem:sqrt}
In our paper,
we use the standard branch cut for the natural logarithm along the non-positive
real axis. So the domain is $\mathcal{D}_1 = \{r e^{i\theta}\, :\, r>0\, ,\ -\pi<\theta<\pi\}$
and for each $z \in \mathcal{D}_1$, the formula is 
$\log(z) = \int_0^1 (z-1)(1+(z-1)t)^{-1}\, dt$. Then, for each $z \in \mathcal{D}_1$, we use $\sqrt{z} = \exp((1/2) \log(z))$.
See Figure \ref{fig:sqrt} for the schematic.
In the decomposition of $x=r e^{i\theta}$, we refer to the term $e^{i\theta}$ as the ``phase.''
Some complex analysis textbooks call this the argument as in Section 3.4 of \cite{Ahlfors}.
But we reserve the term ``argument'' for the input of other functions. 
For example, given a term of the form $\sqrt{f(x)}$ we will refer to $f(x)$ as the ``argument of the square-root function.''
\end{remark}

The result of the calculation in the lemma is an instance related to the fact that the diagonal of a rational bivariate generating function
is an algebraic univariate generating function. (And it is generically not rational.)
This is proved in Section 2.4 of Pemantle and Wilson,
credited to Furstenberg and to Hautus and Klarner.

The residue method may be used to derive formulas such as this, when they are unknown.
This is opposed to proof methods for conjectural formulas, which are sometimes more automatic, such as induction.
For this example, we do the contour integral as an exercise in Appendix \ref{sec:gamma2}.
But once the formula is ``known,'' whether or not it is {\em proved},
there are often simpler combinatorial methods that prove the formula.
The methods are often simpler because they bypass the need for contour integrals.
Here we present such an alternative proof.

\begin{proofof}{\bf Proof of Lemma \ref{lem:gamma2}:}
Let the right-hand-side of equation (\ref{eq:gamma2formula}) be denoted by $g^{(2)}(x,y)$. Then we may rewrite
\begin{equation}
	g^{(2)}(x,y)\, =\, \frac{1}{1-(x+y)}\, \left(1- \frac{4xy}{\left(1-(x+y)\right)^2}\right)^{-1/2}\, .
\end{equation}
Therefore, by Newton's version of the binomial theorem, this gives
\begin{align}
	g^{(2)}(x,y)\, &=\, \frac{1}{1-(x+y)}\, \sum_{n=0}^{\infty} \frac{(-1/2)_n}{n!} \frac{(-1)^n 4^n x^n y^n}{\left(1-(x+y)\right)^{2n}}\\
	&=\, \sum_{n,k=0}^{\infty} \frac{(-1/2)_n}{n!} \cdot \frac{(-2n-1)_k}{k!} (-1)^{n+k} 4^n x^n y^n (x+y)^k\, ,
\end{align}
where the Pochhammer symbol, falling factorial, is 
\begin{equation}
\label{eq:PochhammerFallingFactorial}
	(z)_n\, =\, z(z-1)(z-2)\cdots (z-n+1)\, =\, \prod_{k=0}^{n-1} (z-k)\, .
\end{equation}
Then, by the regular binomial formula, we have
\begin{equation}
	g^{(2)}(x,y)\, 
	=\, \sum_{n,k=0}^{\infty} \sum_{j=0}^{k} \frac{(-1/2)_n}{n!} \cdot \frac{(-2n-1)_k}{k!} \binom{k}{j} (-1)^{n+k} 4^n x^{n+j} y^{n+k-j}\, .
\end{equation}
Therefore, the lemma will be proved if we check that
\begin{equation}
\label{eq:LeftMostBridge}
	\sum_{n=0}^{\infty} \frac{(-1/2)_n}{n!} \cdot \frac{(-2n-1)_k}{k!} \binom{k}{j} (-1)^{n+k} 4^n \Bigg|_{\substack{j=\ell-n\\k-j=m-n}}\,
	=\, \left(\binom{\ell+m}{\ell,m}\right)^2\, ,
\end{equation}
for each $\ell,m \in \{0,1,\dots\}$.
But using well-known combinatorial formulas for the Pochhammer symbols of $-1/2$ and of negative integers, which we review in Appendix \ref{sec:Poc}, this is equivalent to checking
the multinomial identity:
\begin{equation}
\label{eq:gamma2combinatorial}
	\sum_{n=0}^{\infty} \binom{\ell+m}{n,n,\ell-n,m-n}\, =\, \left(\binom{\ell+m}{\ell,m}\right)^2\, .
\end{equation}
(We use the standard convention that if one of the indices in the subscript of a binomial or multinomial coefficient is outside the range
of $0$ to the superscript index, then that coefficient equals 0 by definition.)
Equation (\ref{eq:gamma2combinatorial}) may be proved as follows.
The key is to use {\em distinguishable permutations}.

Draw $\ell+m$ black dots on the number line from $1$ to $\ell+m$. Above each dot place a circle with either the top or bottom shaded in, such that if 
$a$ is the subset of those $r\in\{1,\dots,\ell+m\}$
whose circle above it has the top half shaded, then $|a|=\ell$ and $|a^{\complement}|=m$.
Below each black dot, place a circle with either the left or right shaded in, such that if $\mathcal{B}$ is the set of 
those $r\in\{1,\dots,\ell+m\}$
whose circle below it has the left half shaded, then $|\mathcal{B}|=m$ and $|\mathcal{B}^{\complement}|=\ell$.
We show a particular example of this mapping in the following displayed equation:
\begin{equation}
\label{eq:CombinatorialExample}
\begin{minipage}{13cm}	\begin{tikzpicture}[xscale=0.95,yscale=0.95]
		\draw[very thick,->] (0.5,0) -- (5.5,0);
		\foreach \i in {1,...,5}{
			\fill (\i,0) circle (3pt);}
		\foreach \i in {1,3,5}{
			\draw (\i,0.5) circle (3pt);
			\fill (\i,0.5) -- +(0:3pt) arc (0:180:3pt) -- cycle;}
		\foreach \i in {2,4}{
			\draw (\i,0.5) circle (3pt);
			\fill (\i,0.5) -- +(180:3pt) arc (180:360:3pt) -- cycle;}
		\foreach \i in {2,3,4}{
			\draw (\i,-0.5) circle (3pt);
			\fill (\i,-0.5) -- +(-90:3pt) arc (-90:90:3pt) -- cycle;}
		\foreach \i in {1,5}{
			\draw (\i,-0.5) circle (3pt);
			\fill (\i,-0.5) -- +(90:3pt) arc (90:270:3pt) -- cycle;}
	\begin{scope}[xshift=8.5cm]
		\draw[very thick,->] (0.5,0) -- (5.5,0);
		\foreach \i in {1,...,5}{
			\fill (\i,0) circle (3pt);}
		\foreach \i in {1,5}{
			\draw (\i,0.5) circle (3pt);
			\fill (\i,0.5) -- +(90:3pt) arc (90:180:3pt) -- cycle;}
		\foreach \i in {2,4}{
			\draw (\i,0.5) circle (3pt);
			\fill (\i,0.5) -- +(270:3pt) arc (270:360:3pt) -- cycle;}
		\foreach \i in {3}{
			\draw (\i,0.5) circle (3pt);
			\fill (\i,0.5) -- +(0:3pt) arc (0:90:3pt) -- cycle;}
	\end{scope}
	\draw[decorate, decoration={coil, aspect=0}, -stealth'] (6.5,0) -- (8,0);
	\end{tikzpicture}
\end{minipage}
\end{equation}
Then, if we let $n = |a\cap \mathcal{B}|$ we have $|a \cap \mathcal{B}^{\complement}|=\ell-n$
and $|a^{\complement} \cap \mathcal{B}|=m-n$, as well. Therefore, $|a^{\complement}\cap\mathcal{B}^{\complement}|$
is equal to $\ell+m-|a\cap \mathcal{B}|-|a \cap \mathcal{B}^{\complement}|-|a^{\complement} \cap \mathcal{B}|$,
which is $n$. The number of ways of choosing one quadrant to shade in -- (top,left), (top,right), (bottom,left), (bottom,right)  --
with a prescribed number of each $n$, $\ell-n$, $m-n$, $n$ is $N(\ell,m,n)$ where
\begin{equation}
	N(\ell,m,n)\ =\, \binom{\ell+m}{n,\ell-n,m-n,n}\, .
\end{equation}
Summing over all choices of $n$ gives all possibilities for choosing the two sets $a$ and $\mathcal{B}$.
Since they are chosen independently, that is equal to $\widetilde{N}(\ell,m) \widetilde{N}(\ell,m)$ where 
$\widetilde{N}(\ell,m)$ is the number of ways of choosing a set of cardinality $\ell$ as a subset of a larger set of cardinality
$\ell+m$, which is
\begin{equation}
\widetilde{N}(\ell,m)\, =\, \binom{\ell+m}{\ell,m}\, .
\end{equation}
Since we have proved that $\sum_{n} N(\ell,m,n)$ is equal to $\widetilde{N}(\ell,m) \widetilde{N}(\ell,m)$, this  proves equation (\ref{eq:gamma2combinatorial}).
\end{proofof}
\begin{remark}
\label{rem:Pinsky1}
The picture as in (\ref{eq:CombinatorialExample}) could have been made clearer if we had used multiple colors, as we did in a first draft of our preprint. But
we wished to obtain another picture which could be more easily printed in black-and-white. The combinatorial object is the same as one that was already
in Pinsky's paper in the first step of his proof of Lemma 2 \cite{Pinsky1}.
\end{remark}

Because of Lemma \ref{lem:gamma2} and equation (\ref{eq:betaSecondFormula}), we have
\begin{equation}
\label{eq:beta}
	\kappa(w,x,y)\, =\, \frac{\varkappa^{(2)}(x,y)}{1-w \cdot \varkappa^{(2)}(x,y)}\, =\, \frac{1}{\left(\left(1-\left(x+y\right)\right)^2-4xy\right)^{1/2}-w}\, .
\end{equation}
Now define another generating function
\begin{equation}
	\alpha(w,z)\, =\, \sum_{j,N=0}^{\infty} w^j z^N A(N,j)\, =\, \sum_{j,N=0}^{\infty} w^j z^N B(N,N,j)\, ,
\end{equation}
which is the generating function for the combinatorial numbers we want, $A(N,j)$
for $N,j \in \{0,1,\dots\}$.

}
