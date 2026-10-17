---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-020-45-the-limit-in-case-b
section_title: "The limit in case (b)"
section_number: 4.5
pages: 41-47
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.959
doc_brief: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement — We compute the real part of the semi-classical limit of the sequence of quantum hyperbolic invariants (QHI) of"
---
\label{sub:SPM:b}
For case (b) we have $\bl_{0,\infty}=-2i\pi$ and $\bl_{1,\infty}=2i\pi$. Hence
\begin{equation}\label{defL+-modifcaseb}
	\left\lbrace
	\begin{array}{ll}
		f_-(z)= \mathcal{L}_-(z;-2i\pi,2i\pi) := {\rm Li}_2(e^{z})+z^2 - 2i\pi z,& 
		\\
		f_+(z) = \mathcal{L}_+(z;-2i\pi,2i\pi) := {\rm Li}_2(e^{z})+z^2.& 
	\end{array}\right.
\end{equation}

We will again use Proposition \ref{prop:SPM:PV} to prove that $I_{n,-}$ and $I_{n,+}$ are 
of the form
\begin{equation}\label{asyIjui25c}
I_{n,-} = \dfrac{\text{Constant}_-}{\sqrt{N}}(e^{i r_+ N}+o_{N\to\infty}(1)), \ \
I_{n,+} = \dfrac{\text{Constant}_+}{\sqrt{N}}(e^{i r_- N}+o_{N\to\infty}(1)),
\end{equation}
where $\text{Constant}_-$ and $\text{Constant}_+$ are distinct non-zero complex numbers and $r_+,r_-\in \R$ are distinct as well (see \eqref{Cst+},\eqref{Cst-}).
In particular, this will imply that, e.g.,
\begin{equation}\label{asyIjui25d}
\lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert I_{n,-} \right \vert =
\lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert I_{n,+} \right \vert = 
\lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert I_{n,-} \pm I_{n,+} \right \vert = 0.
\end{equation}


\subsubsection{Case (b), integral $I_{n,+}$}\label{sub:b:+:perron}
Let us study the asymptotics of $I_{n,+}=  \int_{i[s_N^-,2\pi-s_N^+]}  e^{\frac{N}{2i\pi} f_{+}(z)} dz$.

From the formula $f_+(z)=\mathcal{L}_+(z;-2\pi i,2\pi i) = {\rm Li}_2(e^{z})+z^2$
we compute
\begin{align*}\Im(f_+(z))&= \Im({\rm Li}_2(e^{z}))+2 \Re(z)\Im(z),\\
(f_+)'(z)& =2z- \Log(1-e^z),\\
(f_+)''(z)& =2 + \dfrac{e^z}{1-e^z} = 1 + \dfrac{1}{1-e^z},\\
f_+(x+it)& = {\rm Li}_2(e^{x+it})+(x+it)^2 ,\\
\dfrac{\partial}{\partial x} \Im (f_+(x+it)) & = \Im \left (\dfrac{\partial}{\partial x}f_+(x+it)\right ) = 2t - \Im \left (\Log(1-e^{x+it})\right )
= 2t - \arg\left (1-e^{x+it}\right ),\\
\dfrac{\partial}{\partial t} \Im (f_+(x+it)) & = \Im \left (\dfrac{\partial}{\partial t}f_+(x+it)\right ) = 2x - \Re \left (\Log(1-e^{x+it})\right )
= 2x - \Log \vert 1-e^{x+it} \vert.
\end{align*}
One can easily compute that $(f_+)'(z_0)=0$ if and only if 
$$z_0 = a:= \Log ((-1+\sqrt{5})/{2}) \approx -0.48.$$
We will deform the contour $i[s_N^-,2\pi-s_N^+]$ (in blue in Figure \ref{fig:contour:b:+:perron}) to a new contour $C'$ (in dotted blue in Figure \ref{fig:contour:b:+:perron}) on which $\Im(f_+)$ is negative everywhere but in the point $a$ where  $\Im(f_+)(a)=0$ and on the small subcontour $[0,is_N]$ where it is nonnegative. Let us prove this is possible.

We construct $C'$ in six parts:
\begin{itemize}
\item $C'_1$ is vertical, going from $i s_N^-$ to $0$.
\item $C'_2$ is vertical, going from $0$ to $-i \eta$.
\item $C'_3$ is almost horizontal, going from $-i \eta$ to $a$.
\item $C'_4$ is vertical, going from $a$ to $a+2i\pi-i\eta'$.
\item $C'_5$ is horizontal, going from $a+2i\pi-i\eta'$ to $2i\pi-i\eta'$.
\item $C'_6$ is vertical, going from $2i\pi-i\eta'$ to $2i\pi-is_N^+$.
\end{itemize}


\begin{figure}[!h]
	\begin{tikzpicture}
		
		\draw[black,fill=gray!50,opacity=0.5, ] (0,0) circle (2ex); 		
		\draw[black,fill=gray!50,opacity=0.5, ] (-.6,0) circle (2.5ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-1.2,0) circle (3ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-1.8,0) circle (3.2ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-2.4,0) circle (3ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-2.9,0) circle (2.7ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-3.4,0) circle (1.9ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-3.65,0) circle (1.4ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-4,0) circle (2ex);
		
		
		\draw[red] (-.5,.8) node {$\Im f_+ >0$};
		\draw[red] (-.5,-.95) node {$\Im f_+ <0$};		
		\draw[red] (-4.5,-1.2) node {$\Im f_+ >0$};		
		\draw[red] (-4,2) node {$\Im f_+ <0$};		
		
		\draw[color=black,->] (-5,0)--(4,0);		
		\draw[color=black,->] (0,-2)--(0,5);
		
		\draw[color=violet , very thick ] (0,0)--(4,0);		
		\draw[color=violet ] (2,.3) node {Cut};
		
		\draw[color=violet , very thick ] (0,0+4)--(4,0+4);		
		\draw[color=violet ] (2,.3+4) node {Cut};		
		
		
		\draw (-4-.35,-.3) node {$a$};
		\draw[red,fill=red] (-4,0) circle (.5ex); 
		\draw (-4,+.25+4-.65) node {\small \color{blue} $a+2i\pi-i\eta'$};
		\draw[blue,fill=blue] (-4,4-.7) circle (.3ex); 		
		
		\draw (+.25+.2,-.25) node {$0$};
		\draw[red,fill=red] (0,2) circle (.5ex); 
		\draw (+.25+.2,0.3) node {\color{blue}$i s_N^-$};
		\draw[blue,fill=blue] (0,.3) circle (.5ex); 		
		\draw (+.25+.2,2-.25) node {$i \pi$};
		\draw[red,fill=red] (0,4) circle (.5ex); 
		\draw (-.9,4-.3) node {\small \color{blue}$2i\pi - i s_N^+$};
		\draw[blue,fill=blue] (0,4-.3) circle (.5ex); 		
		\draw (-.8,4-.95) node {\small \color{blue}$2i\pi - i \eta'$};
		\draw[blue,fill=blue] (0,4-.7) circle (.4ex); 		
		\draw (+.25+.2,4+.25) node {$2i \pi$};
		\draw[color=red,very thick] (0,0)--(-5,0);
		
		
		\draw[color=blue,very thick,dashed] (0,0+4-.7)--(-4,0+4-.7);
		
		
		\draw[color=blue,very thick,dashed ] (-4,0)--(-4,4-.7);
		
		
		\draw[color=blue,thick] (0,0)--(0,4);
		\draw[color=red, very thick, dashed] (-4,0) ..controls +(0,-.5) and +(-1,1).. (0,-2);
		\draw[color=red,very thick, dashed] (-4,0) ..controls +(0,.5) and +(-1,-1).. (0,2);
		\draw[color=red,very thick, dashed] (0,2) ..controls +(1,1) and +(1,-.5).. (0,4);
		\draw[color=red, very thick,dashed] (0,4) ..controls +(-1,.5) and +(1,-.5).. (-1,4.5);
		
		\draw[color=blue , very thick, dashed] (-4,0) ..controls +(0.5,-.3) and +(-.5,0).. (0,-.2);
		\draw[blue,fill=blue] (0,-.2) circle (.4ex); 
		\draw (+.2,-0.5) node {\color{blue}$-i \eta $};		
		
		\draw[red,fill=red] (0,0) circle (.5ex); 
		
		
	\end{tikzpicture}
	\caption{The deformed contour (in dashed blue) through zones where $\Im f_+<0$ and the point $a$ (in red) where $\Im f_+=0$.}\label{fig:contour:b:+:perron}
\end{figure}

First,  $\Im(f_+)$ is zero on the half-line $(-\infty,0]$ since ${\rm Li}_2$ takes real values on $[0,1]$. Moreover,  $\Im(f_+)(z)$ vanishes at $z=2i\pi$ (and also at $z=i\pi$ but we will not use this). The set of points where $\Im(f_+)$ vanishes is drawn in red in Figure \ref{fig:contour:b:+:perron}; the red dotted line's general form was computed via \textit{Mathematica}, but we will not use its exact position in our arguments.
\smallskip

\underline{Defining $C'_1$, and asymptotics:} We define $C'_1:=[0,i s_N^-]$ oriented downwards. Recall that for all $t\in \R$ and $z:=it$ we have $\Im({\rm Li}_2(e^z))={\rm Cl}_2(t)$, thus $\Im(f_+(it))={\rm Cl}_2(t)$. From Section \ref{smallIsN} we have:
$$ \int_{C'_1} e^{\frac{N}{2 i \pi}f_+(z)}dz =
\int_{0}^{s_N^-} e^{\frac{N}{2 \pi}\Im(f_+(it))}dt=
\int_{0}^{s_N^-}e^{\frac{N}{2 \pi}{\rm Cl}_2(t)}dt = O_{N\to \infty}\left (\frac{1}{N^{1-\frac{\alpha}{2}}}\right ) = o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ).$$

\underline{Defining $C'_2$, and asymptotics:} We define $C'_2:=[-i\eta,0]$ oriented downwards. From Section \ref{smallpijuil25}, since $[-\eta,0] \subset [-\pi,0]$ we have:
$$ \left |\int_{C'_2} e^{\frac{N}{2 i \pi}f_+(z)}dz\right | \leqslant
\int_{-\eta}^{0} e^{\frac{N}{2 \pi}\Im(f_+(it))}dt=
\int_{-\eta}^{0}e^{\frac{N}{2 \pi}{\rm Cl}_2(t)}dt = o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ).$$

\underline{Defining $C'_3$:}
The critical point $z=a$ of $f_+$ is simple, since $(f_+)''(z)$ only vanishes at $z=\Log(2)$. Thus, by standard complex analysis, there is a disk neighbourhood $D_a$ of $a$ (drawn as a grey disk) split into four zones by two transverse level lines where $\Im(f_+)=0$, and $\Im(f_+)$ is alternatively positive and negative in these four zones by circling around $a$. We already know that one level line is the horizontal line (drawn in full red), thus the other level line (part of the dotted red curve) crosses transversely this horizontal line.

Now, for any point $x \in (a,0]$ we have
$$\dfrac{\partial}{\partial t} \Im (f_+(x+it))\vert_{t=0} =  2x - \Log \vert 1-e^{x} \vert
=  2x - \Log (1-e^{x} )>0,$$
by definition of $a$ and the fact that
$ 2x - \Log \vert 1-e^{x} \vert>0 \Leftrightarrow (e^x)^2+(e^x)-1>0$.
Hence, $\Im(f_+)$ is increasing on every small enough vertical line (oriented upwards) above every $x\in(a,0]$. This confirms that a negative zone for $\Im(f_+)$ is below the red horizontal line and a positive zone is above it.

We can now define the part $C'_3$ of the new contour $C'$ (in Figure \ref{fig:contour:b:+:perron} this is the part which is between $-i\eta$ and $a$, oriented from right to left, where the value of $\eta>0$ will be decided in what follows). For any $x \in (a,0]$, define a small enough disk $D_x$ around $x$ so that the real line cuts $D_x$ into two half-disks, where $\Im(f_+)$ is negative on the bottom half-disk and positive on the upper half-disk. Such a small disk exists since $\textstyle \frac{\partial}{\partial t} \Im (f_+(x+it))\vert_{t=0}>0$.

The union $\textstyle D_a \cup \bigcup_{a<x \leqslant 0} D_x$ covers the compact set $[a,0]$, so there is a finite family of points $x_0=a<x_1<x_2<\ldots<x_p=0$ such that $\textstyle D_a \cup \bigcup_{1 \leqslant i \leqslant p} D_{x_i}$ covers $[a,0]$. Take $\eta>0$ small enough to be smaller than the radius of $D_{x_p}=D_0$.
 We can now define the part $C'_3$ as a smooth curve going from $-i\eta$ to $a$ while remaining in all bottom half-disks; it can even be chosen outside of $D_a$ as an horizontal line of imaginary part $-\eta$ (thus higher than the opposite of half the minimum of all radii of $D_{x_i}$), and smoothed out afterwards.

\smallskip

\underline{Defining $C'_4$:}
We define $C'_4:= [a,a+2i\pi-i\eta']$, oriented upwards. Let us prove that $\Im(f_+)<0$ on the vertical line $(a,a+2i\pi]$.
To do this we look for all $t \in (0,2\pi)$ at the real derivative
$$\dfrac{\partial}{\partial t} \Im (f_+(a+it))
=  2a - \Log \vert 1-e^{a+it} \vert
=  \Log (1-e^{a}) - \Log \vert 1-e^{a+it} \vert.
$$
We remark that this quantity is negative for all $t \in (0,2\pi)$, by a simple geometric argument: $1-e^a$ is the distance between $1$ and $e^a \in (0,1)$, which is smaller than the distance $\vert 1-e^{a+it} \vert$ between $1$ and any other point $e^{a+it}$ of the  circle of center $0$ and radius $e^a$ (since $1$ lives outside of the closed disk $\bar{D}(0,e^a)$). Hence, $\Im(f_+)$ decreases on $[a,a+2i\pi]$ oriented upwards, and thus $\Im(f_+)<0$ on the vertical line $(a,a+2i\pi]$.
\smallskip

\underline{Asymptotics on $C'_3 \cup C'_4$:}
From what precedes, we have  all the tools to apply the saddle point method (see Section \ref{sub:SPM:PV}) on the contour $\lambda=C'_3\cup C'_4$ for $g(z)=1, f(z)=f_+(z)$ and $z_0=a$. Since $N = 2\pi n$, we obtain:
$$ \int_{C'_3\cup C'_4} e^{\frac{N}{2 i \pi}f_+(z)}dz = \dfrac{{2\pi}}{\sqrt{N}} e^{i \theta}\cdot 1 \cdot \dfrac{1}{\sqrt{|f_+''(a)|}}
e^{\frac{N}{2i\pi} f_+(a)} \left ( 1+ o_{N \to \infty}(1) \right ).$$
For the curious reader, we remark that (\cite{Z}) $${\rm Li}_2(e^a)={\rm Li}_2\left (\frac{\sqrt{5}-1}{2}\right )= \frac{\pi^2}{10}-\Log^2\left (\frac{\sqrt{5}+1}{2}\right ),$$
and thus $f_+(a)={\rm Li}_2(e^a) +a^2$ has the unexpectedly simple expression
$\textstyle f_+(a)= \frac{\pi^2}{10} $. For our purposes, we only need to know that this is a real number, i.e. $\Im(f_+(a))=0$ which we knew already.

Moreover, $(f_+)''(a)=1+\frac{1}{1-e^a}= \frac{5+\sqrt{5}}{2}$. Hence we have
$$ \int_{C'_3\cup C'_4} e^{\frac{N}{2 i \pi}f_+(z)}dz = \dfrac{\text{Constant}_+}{\sqrt{N}}(e^{i r_+ N}+o_{N\to\infty}(1)),$$
where $\text{Constant}_+ \in \C^*$ has modulus $2\pi \left (\frac{5+\sqrt{5}}{2}\right )^{-\frac{1}{2}}=3.303...$ and $r_+=-\frac{\pi}{20} \in \R$.
\smallskip

\underline{Defining $C'_5$, and asymptotics:} We define $C'_5:=[a+2i\pi-i\eta',2i\pi-i\eta']$ oriented from left to right.
Since $\partial_x \Im (f_+(x+it)) = 2t - \arg\left (1-e^{x+it}\right )$ for all $x+it$ in the domain of definition of $f_+$, and since $\arg$ lies in $(-\pi,\pi]$, we deduce that for any fixed $t>\pi/2$ the function $\left (x\mapsto \Im (f_+(x+it))\right )$ is strictly increasing on the horizontal line of altitude $t$ oriented from left to right.

In particular for $t=2\pi - \eta'$, $\Im (f_+)$ is maximal on $C'_5$ at its right endpoint $2i\pi-i\eta'$ where it takes the value ${\rm Cl}_2(2\pi-\eta')<0$.
Hence 
$$ \left |\int_{C'_5} e^{\frac{N}{2 i \pi}f_+(z)}dz\right | \leqslant
|a|e^{\frac{N}{2 \pi}{\rm Cl}_2(2\pi-\eta')} = o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ).$$


\underline{Defining $C'_6$, and asymptotics:} We define $C'_6:=i[2\pi-\eta',2\pi-s_N^+]$ oriented upwards. From Section \ref{sub:small:vert:int}, since $[2\pi-\eta',2\pi-s_N^+] \subset [\pi,2\pi]$ we have:
$$ \left |\int_{C'_6} e^{\frac{N}{2 i \pi}f_+(z)}dz\right | \leqslant
\int_{2\pi-\eta'}^{2\pi-s_N^+} e^{\frac{N}{2 \pi}\Im(f_+(it))}dt=
\int_{2\pi-\eta'}^{2\pi-s_N^+} e^{\frac{N}{2 \pi}{\rm Cl}_2(t)}dt = o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ).$$


This concludes the construction of the new contour $C'$, and by summing the integrals on each part, we obtain
$$ I_{n,+}=\int_{C'} e^{\frac{N}{2 i \pi}f_+(z)}dz = \dfrac{\text{Constant}_+}{\sqrt{N}}(e^{i r_+ N}+o_{N\to\infty}(1)),$$
where
\begin{equation}\label{Cst+}
\vert \mathrm{Constant}_+ \vert  = 2\pi \left (\frac{5+\sqrt{5}}{2}\right )^{-\frac{1}{2}}=3.303...,\ r_+=-\frac{\pi}{20}\in \R.
\end{equation} 


\subsubsection{Case (b), integral $I_{n,-}$}\label{sec:bIn-janv26} From the formula $f_-(z)=\mathcal{L}_-(z;-2\pi i,2i\pi) = {\rm Li}_2(e^{z})+z^2 -2i\pi z$ we compute
\begin{align*}\Im(f_-(z))&= \Im({\rm Li}_2(e^{z}))+2 \Re(z)\Im(z)-2\pi\Re(z),\\
(f_-)'(z)&=2z- \Log(1-e^z)-2i\pi,\\
(f_-)''(z)& =2 + \dfrac{e^z}{1-e^z} = 1 + \dfrac{1}{1-e^z},\\
f_-(x+it)&= {\rm Li}_2(e^{x+it})+(x+it)^2 -2i\pi(x+it),\\
\dfrac{\partial}{\partial x} \Im (f_-(x+it)) & = \Im \left (\dfrac{\partial}{\partial x}f_-(x+it)\right ) = 2(t-\pi) - \Im \left (\Log(1-e^{x+it})\right )
\\ &= 2(t-\pi) - \arg\left (1-e^{x+it}\right ),\\
\dfrac{\partial}{\partial t} \Im (f_-(x+it)) & = \Im \left (\dfrac{\partial}{\partial t}f_-(x+it)\right ) = 2x- \Re \left (\Log(1-e^{x+it})\right )
= 2x - \Log \vert 1-e^{x+it} \vert.
\end{align*}
One can easily compute that $(f_-)'(z_0)=0$ if and only if $$z_0 = b+i\pi:= \Log((1+\sqrt{5})/2)+i\pi \approx 0.48+i\pi.$$

As in the previous section, we will deform the contour $i[s_N^-,2\pi-s_N^+]$ (in blue in Figure \ref{fig:contourC':b:+}) to a new contour $C'$ (in dotted blue in Figure \ref{fig:contourC':b:+}). In Figure \ref{fig:contourC':b:+}, red dots and lines are points where one can easily prove that $\Im(f_-)=0$, and the red dotted curve is suggested by \textit{Mathematica}.

We construct $C'$ in five parts:
\begin{itemize}
	\item $C'_1$ is horizontal, going from $i s_N^-$ to $1+is_N^-$.
	\item $C'_2$ is vertical, going from $1+is_N^-$ to $1+i(\pi-\epsilon)$, where $\epsilon>0$ is small enough.
	\item $C'_3$ is almost horizontal, going from $1+i(\pi-\epsilon)$ to the saddle point $b+i\pi$.
	\item $C'_4$ is almost horizontal, going from the saddle point $b+i\pi$ to $i(\pi+\epsilon)$.
	\item $C'_5$ is vertical, going from $i(\pi+\epsilon)$ to $2i\pi-is_N^+$.
\end{itemize}

\begin{figure}[!h]
	\begin{tikzpicture}
	\begin{scope}[xshift=4cm,yshift=2cm]
		\draw[black,fill=gray!50,opacity=0.5, ] (0,0) circle (2ex); 		
		\draw[black,fill=gray!50,opacity=0.5, ] (-.6,0) circle (2.5ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-1.2,0) circle (3ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-1.8,0) circle (3.2ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-2.4,0) circle (3ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-2.9,0) circle (2.7ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-3.4,0) circle (1.9ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-3.65,0) circle (1.4ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-4,0) circle (2ex);
	\end{scope}	


		\draw[red] (1,3) node {$\Im f_- <0$};		
		\draw[red] (3.2,1.2) node {$\Im f_- <0$};				
		\draw[red] (3,3) node {$\Im f_- >0$};		
		\draw[red] (1,1) node {$\Im f_- >0$};				







		\draw[color=black,->] (-2,0)--(8,0);		
		\draw[color=black,->] (0,-2)--(0,5);
		
		\draw[color=violet , very thick ] (0,0)--(8,0);		
		\draw[color=violet ] (2,-.3) node {Cut};
		
		\draw[color=violet , very thick ] (0,0+4)--(8,0+4);		
		\draw[color=violet ] (2,.3+4) node {Cut};		
		
		
		\draw (2.25+.75,2+.3) node {$b+i\pi$};
		\draw[red,fill=red] (2.25,2) circle (.5ex); 


		
		\draw (+.25+.2,-.25) node {$0$};
		\draw[red,fill=red] (0,2) circle (.5ex); 
		\draw (-.25-.2,0.3) node {\color{blue}$i s_N^-$};
		\draw[blue,fill=blue] (0,.3) circle (.5ex); 		
		
		
		\draw (-.25-.2,2-.25) node {$i \pi$};
		\draw[red,fill=red] (0,4) circle (.5ex); 
		\draw (-.9,4-.3) node {\small \color{blue}$2i\pi - i s_N^+$};
		\draw[blue,fill=blue] (0,4-.3) circle (.5ex); 		


		\draw (+.25+.2,4+.25) node {$2i \pi$};
		\draw[color=red,very thick] (0,2)--(8,2);
		
		

		
		

		
		
		\draw[color=blue,thick] (0,0)--(0,4);
		\draw[color=red, very thick, dashed] (0,0) ..controls +(3,0) and +(3,0).. (0,4);

	


		
		\draw[red,fill=red] (0,0) circle (.5ex); 
		
		\draw[color=blue,very thick,dashed] (0,0.3)--(4,.3);
		
		\draw (4+.9,0.3) node {\color{blue}$1+i s_N^-$};
		\draw[blue,fill=blue] (4,.3) circle (.5ex); 	

		\draw[color=blue,very thick,dashed] (4,.3)--(4,2-.15);		
		\draw[blue,fill=blue] (4,2-.15) circle (.3ex); 			
		\draw (4+1.1,2-.3) node {\color{blue}\small $1+i (\pi-\epsilon)$};		
		\draw[color=blue,very thick,dashed] (4,2-.15)--(2.4,2-.15)--(2.15,2.15)--(0,2.15);		
		\draw[blue,fill=blue] (0,2+.15) circle (.3ex); 					
		\draw (-.95,2+.3) node {\color{blue}\small $i (\pi+\epsilon)$};		
		
	\end{tikzpicture}
	\caption{The deformed contour $C'$}\label{fig:contourC':b:+}	
\end{figure}
\smallskip

\underline{Asymptotics on $C'_1$:} On the horizontal line of altitude $s_N^-$, for all $x\geqslant 0$, we have
$$\dfrac{\partial}{\partial x} \Im (f_-(x+is_N^-)) = 2s_N^--2\pi - \arg\left (1-e^{x+is_N^-}\right )<-\frac{\pi}{2},$$
where the last inequality comes from $|\arg|\leqslant \pi$ and the fact that $s_N^-$ is small. Thus for all  $x> 0$ we have
$$\Im (f_-(x+is_N^-)) < \Im (f_-(0+is_N^-))- \frac{\pi}{2}x = {\rm Cl}_2(s_N^-)-\frac{\pi}{2}x.$$
Since ${\rm Cl}_2(s_N^-)< {\rm Cl}_2(\pi/3) \approx 1.10149$, it follows that for all $x \geqslant 1$ we have $\Im (f_-(x+is_N^-))\leqslant 
\Im (f_-(1+is_N^-))< 0$. Moreover, on $C'_1=[is_N^-,1+is_N^-]$ we have:
\begin{align*}
 \left |\int_{C'_1} e^{\frac{N}{2 i \pi}f_-(z)}dz\right | 
 &\leqslant
\int_0^{1}e^{\frac{N}{2  \pi}\Im (f_-(x+is_N^-))}dx\\
&\leqslant  \int_0^{1}e^{\frac{N}{2  \pi}\left ({\rm Cl}_2(s_N^-)-\frac{\pi}{2}x\right )}dx\\
&= e^{\frac{N}{2  \pi}{\rm Cl}_2(s_N^-)} \cdot  \int_0^{1}e^{\frac{N}{2 
		 \pi}\left (-\frac{\pi}{2}x\right )}dx \\
	 &= e^{\frac{N}{2  \pi}{\rm Cl}_2(s_N^-)} \cdot 
	 \dfrac{4}{N}\left (1-e^{-\frac{N}{4}}\right )\\
&=o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ),\end{align*}
where the last asymptotics comes from $s_N^- e^{\frac{N}{2\pi}{\rm Cl}_2(s_N^-)}=
o_{N\to \infty}(1/\sqrt{N})$ established in Section \ref{smallIsN}.
\smallskip

\underline{Asymptotics on $C'_3 \cup C'_4$:} We proceed similarly as we did in the previous section for $C'_3$, constructing this time two almost horizontal curves $C'_3, C'_4$, going respectively from $1+i\pi-i\epsilon$ to $b+i\pi$ and from $b+i\pi$ to $i\pi+i\epsilon$. For this we construct a small disk $D_x$ around each point $x+i\pi$ of $[i\pi,1+i\pi]$, where $\Im(f_-)$ is negative on the bottom half-disk and
positive on the upper half-disk if $x>b$, and conversely if $x<b$. This is possible, because for any $x\geqslant0$ the vertical derivative at $x+i\pi$ is
$$\dfrac{\partial}{\partial t} \Im (f_-(x+it)) \vert_{t=\pi}
= 2x - \Log \vert 1-e^{x+i\pi} \vert=2x-\Log(1+e^x).$$
The reader will recognize the golden ratio, and agree that $2x-\Log(1+e^x)<0$ for $x \in [0,b)$ and $2x-\Log(1+e^x)>0$ for $x>b$. This justifies the location of the zones of signs of $\Im(f_-)$ in Figure \ref{fig:contourC':b:+} (the {\it valleys} and the {\it hills} of $f_-$ at $b$), whence the construction of the disks $D_x$. By compacity we can reduce to a finite family of such disks which cover $[i\pi,1+i\pi]$; they are drawn in grey in Figure \ref{fig:contourC':b:+}. Then we define $\epsilon>0$ small enough to be smaller than the radii of all grey disks.

Finally, in order to apply the saddle point method of Proposition \ref{prop:SPM:PV} for the contour $\lambda=C'_3\cup C'_4$, with $g=1$, $f=f_-$, and $z_0=b+i\pi$, we only need to check that $f''(z_0) \neq 0$. We have 
$$(f_-)''(b+i\pi)=1+\frac{1}{1-e^{b+i\pi}}= 1+ \frac{1}{1+\frac{1+\sqrt{5}}{2}}=\frac{5-\sqrt{5}}{2} =1.38... \neq 0$$ so we are good to go. For the sake of completeness, we can compute $f_-(b+i\pi) = 9\pi^2/10$, once again from the special values of the dilogarithm. Hence we get
$$ \int_{C'_3\cup C'_4} e^{\frac{N}{2 i \pi}f_-(z)}dz = \dfrac{\text{Constant}_-}{\sqrt{N}}(e^{i r_- N}+o_{N\to\infty}(1)),$$
where $\text{Constant}_- \in \C^*$ has modulus $2\pi \left (\frac{5-\sqrt{5}}{2}\right )^{-\frac{1}{2}}=5.34...$ and $r_-=-\frac{9 \pi}{20} \in \R$.
\smallskip

\underline{Asymptotics on $C'_2$:} Now that $\epsilon>0$ has been fixed, we define $C'_2$ as the vertical contour from $1+is_N^-$ to $1+i\pi-i\epsilon$.
To see that $\Im(f_-)$ is strictly increasing on $C'_2$ going upwards, one can for example prove that the vertical derivative is positive:
$$\dfrac{\partial}{\partial t} \Im (f_-(x+it)) \vert_{x=1}
= 2 - \Log \vert 1-e^{1+it} \vert \geqslant 2-\Log(1+e)>0,$$
where the last inequality stems from the fact that $1>b$. Hence the negative number $\Im \left (f_-\left (1+i\pi-i\epsilon\right )\right )$ is an upper bound for $\Im(f_-)$ on $C'_2$, and
$$ \left |\int_{C'_2} e^{\frac{N}{2 i \pi}f_-(z)}dz\right | \leqslant
\pi \cdot e^{\frac{N}{2 \pi}\Im \left (f_-\left (c+i\pi-i\epsilon\right )\right )} = o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ).$$

\underline{Asymptotics on $C'_5$:} We define $C'_5:=i[\pi+\epsilon,2\pi-s_N^+]$, oriented upwards. From Section \ref{sub:small:vert:int}, since $i[\pi+\epsilon,2\pi-s_N^+] \subset [\pi,2\pi]$, we have:
$$ \left |\int_{C'_5} e^{\frac{N}{2 i \pi}f_-(z)}dz\right | \leqslant
\int_{\pi+\epsilon}^{2\pi-s_N^+} e^{\frac{N}{2 \pi}\Im(f_-(it))}dt=
\int_{\pi+\epsilon}^{2\pi-s_N^+} e^{\frac{N}{2 \pi}{\rm Cl}_2(t)}dt = o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ).$$


This concludes the construction of the new contour $C'$, and by summing the integrals on each part, we obtain
$$ I_{n,-}=\int_{C'} e^{\frac{N}{2 i \pi}f_-(z)}dz = \dfrac{\text{Constant}_-}{\sqrt{N}}(e^{i r_- N}+o_{N\to\infty}(1)),$$
where
\begin{equation}\label{Cst-}
\vert \mathrm{Constant}_- \vert = 2\pi \left (\frac{5-\sqrt{5}}{2}\right )^{-\frac{1}{2}}=5.34..., \ r_-=-\frac{9 \pi}{20} \in \R.
\end{equation}
