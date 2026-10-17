---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-019-44-the-limit-in-case-a
section_title: "The limit in case (a)"
section_number: 4.4
pages: 39-41
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.942
---
\label{sub:SPM:a} Recall \eqref{l0inftymars25}-\eqref{l1inftymars25} and \eqref{defL+-modif}-\eqref{notInjui25}. In case (a) we have $\bl_{0,\infty}=-2i\pi$ and $\bl_{1,\infty}=i\pi$, so
\begin{equation}\label{defL+-modifcasea}
\left\lbrace
	\begin{array}{ll}
		f_-(z)= \mathcal{L}_-(z;-2i\pi,i\pi) := {\rm Li}_2(e^{z})+z^2 - i\pi z,& 
		\\
		f_+(z) = \mathcal{L}_+(z;-2i\pi,i\pi) := {\rm Li}_2(e^{z})+z^2 +i\pi  z.
		\end{array}\right.
\end{equation}

We will prove, using Proposition \ref{prop:SPM:PV} for $I_{n,-}$, that
\begin{equation}\label{asyIjui25}
\lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert I_{n,-} \right \vert = \dfrac{1}{2} {\rm Vol}(M)
  \ \ \text{and} \ \ 
I_{n,+} = O_{N\ra \infty}(1). 
\end{equation}
By Lemma \ref{lem:PM:SE} this will imply asymptotics of linear combinations of $I_{n,-}$ and $I_{n,+}$, such as
\begin{equation}\label{asyIjui25b}
\lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert I_{n,-} \pm I_{n,+} \right \vert = \dfrac{1}{2} {\rm Vol}(M).
\end{equation}


\subsubsection{Case (a), integral $I_{n,-}$}\label{sub:a:-}
Let us prove that $\lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert I_{n,-} \right \vert = \dfrac{1}{2} {\rm Vol}(M)$.


First we show that $f_-(z)=  {\rm Li}_2(e^{z})+z^2 - i\pi z$ and $\textstyle z_0:= {i \frac{\pi}{3}}$ satisfy the properties of Proposition \ref{prop:SPM:PV} for the contour $\lambda=i[\eta,2\pi-\eta']$, where $\eta,\eta' \in(0,1)$.

We have $\partial_z {\rm Li}_2(z) = -\Log(1-z)/z$, so $\partial_z {\rm Li}_2(e^{z}) = -\Log(1-e^{z})e^{-z}.e^{z}= -\Log(1-e^{z})$, and therefore
$$(f_-)'(z)= 2z -\Log(1-e^{z}) - i \pi,\ \text{and}\ (f_-)''(z)= 2 + \frac{e^z}{1-e^z}= 1 + \frac{1}{1-e^z}.$$ 
It follows $(f_-)'(z_0)=  (2i\pi/3)  -\Log(1-e^{i\pi/3}) - i \pi= (-i \pi/3) - \Log(e^{-i \frac{\pi}{3}})=0$, which checks (i). Also $(f_-)''(z_0)= 1 + (1-e^{i \frac{\pi}{3}})^{-1}=1+e^{i \frac{\pi}{3}} \neq 0$, which checks (ii).

Let us check property (iii). We parametrize the contour $\lambda=i[\eta,2\pi-\eta']$ by $z=i t$, where $t \in [\eta,2\pi-\eta']$. Let us prove that $[0,2\pi] \ni t \mapsto \Im(f_-)(it)$ has a strict maximum at $\textstyle\frac{\pi}{3}$.

Recall (\cite{Z}) that
\begin{equation}\label{BWdilogmars25}
\forall y \in \C, \ \mathfrak{I}({\rm Li}_2(y))   = -\arg(1-y)\Log\vert y\vert + D(y),
\end{equation}
where $\arg$ is the branch of the argument with values in $]-\pi,\pi]$, and $D(y)$ is the Bloch-Wigner dilogarithm, which computes the algebraic volume of an oriented hyperbolic ideal tetrahedron with cross--ratio modulus $y$. Hence we have
$$\Im(f_-)(it) = \Im\left ({\rm Li}_2(e^{it})+(it)^2 - i\pi it\right )
=\Im\left ({\rm Li}_2(e^{it})\right ) = D(e^{it})= {\rm Cl}_2(t),$$
where ${\rm Cl}_2$ is Clausen's function \eqref{Clausenf}. Since it achieves its strict local maxima at the points $\pi/3 + 2\pi n$, $n\in \mz$, (iii) follows.

We can now apply Proposition \ref{prop:SPM:PV}
and conclude that
 $$\lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert \int_{[i\eta,2i\pi-i\eta']}  e^{n(-i) f_{-}(z)} dz \right \vert 
 = \Im (f_-)(z_0) = D\left (e^{i\frac{\pi}{3}}\right )
 = \dfrac{1}{2} {\rm Vol}(M),$$
as the volume of the figure-eight knot complement is well-known to be twice the volume of a regular ideal tetrahedron, with angles $\textstyle \frac{\pi}{3}$.

Finally, consider the decomposition
\begin{align*}
	I_{n,-} &=  \int_{i[s_N^-,2\pi-s_N^+]}  e^{n(-i) f_{-}(z)} dz\\
	&=
	\int_{i[ s_N^-,\eta ]}  e^{n(-i) f_{-}(z)} dz
	+\int_{i[\eta,2\pi-\eta']}  e^{n(-i) f_{-}(z)} dz
	+\int_{i[2\pi-\eta',2\pi- s_N^+]}  e^{n(-i) f_{-}(z)} dz.
\end{align*}
By  the results of Section \ref{sub:small:vert:int}, an immediate triangle inequality shows that
the first and third integrals are $O_{n\to\infty}(\exp(n K))$ where $K>0$ is a value of ${\rm Cl}_2(t)$ outside of its strict maximum, and thus $ K<{\rm Vol}(M)/2$. Hence
 $$\lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert I_{n,-} \right \vert 
= \dfrac{1}{2} {\rm Vol}(M).$$



\subsubsection{Case (a), integral $I_{n,+}$}\label{sec:case(a)In+}
Let us prove that $I_{n,+} = O_{N\ra \infty}(1)$.

One can easily compute that the function $f_+(z)=  {\rm Li}_2(e^{z})+z^2 +i\pi  z$ admits a unique critical point at $\textstyle z=-i \frac{\pi}{3}$ (on which $\Im f_+ |_{i\R}$  has a minimum, not a maximum), but we will not use this.


We deform the contour $i[s_N^-,2\pi-s_N^+]$. Let $x$ be a large negative real number, and define $C^\infty$ as the path from $is_N^-$ to $2i\pi -is_N^+$ formed by the concatenation of the open oriented intervals $C_{s_N^-}:=i(s_N^-,0)$, $C^\infty_0:=(0,x)\subset \mr_-$, $C^\infty_x:=x+ i(0,2\pi)$, $C^\infty_{2\pi}:=(x,0)+i2\pi$, and $C'_{s_N^+}:=(2i\pi,2i\pi-is_N^+)$ (see Figure \ref{fig:contour:a:+}). Since $C^\infty$ and $i[s_N^-,2\pi-s_N^+]$ are homotopic relatively to their endpoints we have 
\begin{equation}\label{defneg}
	I_{n,+} = \int_{C^\infty} e^{\frac{N}{2\pi i}\mathcal{L}_+(z;-2\pi i,\pi i)}dz.
\end{equation}
\begin{figure}[!h]
\begin{tikzpicture}
\draw[color=lightgray,->] (-5,0)--(2,0);
\draw[color=lightgray,->] (0,-2)--(0,4);
\draw (-4,-.05) node {\Huge $\cdot$};
\draw (-4,-.25) node {$x$};
\draw (-4,-.05+2) node {\Huge $\cdot$};
\draw (-4,+.25+2) node {$x+2i\pi$};
\draw (+.025,-.05) node {\Huge $\cdot$};
\draw (+.25,-.25) node {$0$};
\draw (+.025,.4-.05) node {\Huge $\cdot$};
\draw (+.5,.4) node {$is_N^-$};
\draw (+.025,2-.4-.05) node {\Huge $\cdot$};
\draw (+1,2-.4) node {$2i\pi-is_N^+$};
\draw (+.025,2-.05) node {\Huge $\cdot$};
\draw (+.25+.2,2) node {$2i \pi$};
\draw[color=blue,thick] (0,0)--(-4,0);
\draw[color=blue] (-2,0-.3) node {$C^\infty_0$};
\draw[color=blue] (-2,0-.3-.5) node {$\Im(f_+)<0$};
\draw[color=blue,thick] (0,0+2)--(-4,0+2);
\draw[color=blue] (-2,0+2+.3) node {$C^\infty_{2\pi}$};
\draw[color=blue] (-2,0+2+.3+.5) node {$\Im(f_+)<0$};
\draw[color=blue,thick] (-4,0)--(-4,2);
\draw[color=blue] (-4-.5,1.2) node {$C^\infty_x$};
\draw[color=blue] (-4-1,.7) node {$\Im(f_+)<0$};
\draw[color=blue,thick] (0,2)--(0,2-.4);
\draw[color=blue] (-.5,1.6) node {$C'_{s_N^+}$};
\draw[color=red,thick] (0,0)--(0,.4);
\draw[color=red] (-.5,.4) node {$C_{s_N^-}$};
\end{tikzpicture}
\caption{The deformed contour $C^\infty=C_{s_N^-} \cup C^\infty_0 \cup C^\infty_x \cup C^\infty_{2\pi} \cup C'_{s_N^+}$ (blue parts are where $\Im(f_+)<0$ and the red part is where $\Im(f_+)$ is positive but very small)
	}\label{fig:contour:a:+}
\end{figure}


From the formula $f_+(z)=\mathcal{L}_+(z;-2\pi i,\pi i) = {\rm Li}_2(e^{z})+z^2+\pi iz$ we compute
$$\Im(f_+(z))= \Im({\rm Li}_2(e^{z}))+2 \Re(z)\Im(z) + \pi \Re(z).$$

For $z \in C_0^\infty \subset \R_-$ we thus have $\Im(f_+(z))= \Im({\rm Li}_2(e^{z}))+ \pi \Re(z)= \pi \Re(z)<0$ since $\Re(z)<0$ and the dilogarithm of a real number $<1$ is real.

For $z \in C_{2\pi}^\infty \subset \R_-+ i2\pi$ we have $\Im(f_+(z))= \Im({\rm Li}_2(e^{z}))+5\pi\Re(z)=5\pi\Re(z) <0$ since again $\Re(z)<0$ and the dilogarithm of  $e^z \in \exp(]-\infty;0[ + 2i \pi) \subset \R\setminus ]1;+\infty[$ is real.

For $z=x+it \in C^\infty_x$ we have $\Im(f_+(x+it))= \Im({\rm Li}_2(e^{x+it}))+2 x t + \pi x.$ Moreover ${\rm Li}_2(y)\sim y$ as $y\ra 0$ in $\mc$, and 
 therefore there exists $x_0 <0$ such that
  for every $t\in [0,2\pi]$ and $x\leq x_0$ we have
  $\textstyle |{\rm Li}_2(e^{x+it})|<\frac{1}{2}$.
  Hence, taking for instance $x \leqslant x_0-1$, for every $t\in [0,2\pi]$ we have
$$\Im(f_+(x+it))= \Im({\rm Li}_2(e^{x+it}))+2 x t + \pi x
\leqslant \dfrac{1}{2} + \pi(-1) <0.
$$
We conclude that for $|x|$ large enough, $\Im(f_+)<0$ on the contour $C^\infty_x$.

Now we remark that, having fixed for example $x=x_0-1<0$, and denoting by $\gamma\colon [0,1]\to \mc$ a parametrization of the path $C^\infty_0 \cup C^\infty_x \cup C^\infty_{2\pi} $, we have
\begin{align*}
	\left \vert \int_{C^\infty} e^{\frac{N}{2\pi i}f_+(z)}dz\right \vert
& \leqslant \int_{0}^1 |e^{\frac{N}{2\pi i}f_+(\gamma(t))} \gamma'(t)|dt \\
& \leqslant \int_{0}^1 e^{\frac{N}{2\pi}\Im f_+(\gamma(t))} |\gamma'(t)| dt\\
& \leqslant \int_{0}^1 e^{\frac{N}{2\pi}0}|\gamma'(t)| dt=2|x|+2\pi = O_{N\ra \infty}(1).
\end{align*}

Finally, the remaining two integrals on the small vertical contours $C_{s_N^-}, C'_{s_N^+}$ are also $O_{N\ra \infty}(1)$ from the conclusions of Section \ref{sub:small:vert:int}. Hence $I_{n,+} = O_{N\ra \infty}(1)$.
