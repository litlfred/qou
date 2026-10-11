---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-017-42-the-saddle-point-method
section_title: "The saddle-point method"
section_number: 4.2
pages: 37-39
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.908
---
\label{sub:SPM:PV} Let $\lambda$ denote a piecewise continuously differentiable path contained in an open
set $\Delta \subset \mathbb{C}$, and let $z \mapsto g(z)$ and $z \mapsto f(z)$ denote two holomorphic functions on $\Delta$.
We consider the asymptotics of the integral
\begin{equation}\label{intIndec25}
I_n := \int_{\lambda} g(z) e^{n (-i) f(z)} dz\quad , \ n\to +\infty.
\end{equation}
Let us recall a concise version of the one-dimensional saddle point method theorem (see also \cite{O'Sul}). Note that usually the condition (iii) below is written as a maximum of the real part of the potential function. Here we consider $n(-i)f(z)$ instead of $nf(z)$, so we look for a maximum of the imaginary part instead (this is mostly in order to work with ${\rm Li}_2$ instead of $i{\rm Li}_2$ in the following sections).

\begin{prop}[\cite{PV}, Section 2]\label{prop:SPM:PV} Assume there exists an interior point $z_0 \in \lambda$ such that 
	\begin{enumerate}[label=(\roman*)]
\item $f'(z_0)=0$,
\item $f''(z_0) \neq 0$,
\item $\Im f(z) < \Im f(z_0)$ for all $z \neq z_0$ on the closure of $\lambda$ in $\mathbb{C}\cup\{\infty\}$,
	\end{enumerate}
and $g(z_0)\neq 0$. Then we have:
$$ I_n = \dfrac{\sqrt{2\pi}}{\sqrt{n}} e^{i \theta} g(z_0) \dfrac{1}{\sqrt{|f''(z_0)|}}
e^{n (-i) f(z_0)} \left ( 1+ o_{n \to \infty}(1) \right ),
$$
for some explicit $\theta \in \mathbb{R}$. In particular 
$$ \lim_{n\ra +\infty}  \dfrac{1}{n}\Log \left \vert I_n \right \vert = \Im f(z_0).
$$
\end{prop}

In the following sections we will use this result to study the integrals $I_{\pm,N}(\bl_{0,\infty},\bl_{1,\infty})$ in \eqref{I+} for the particular values $\bl_{0,\infty}=-2i \pi$ and $\bl_{1,\infty}\in \{i \pi,2i\pi\}$ obtained in Section \ref{loglimmars25}. Therefore we set $$n:=\frac{N}{2\pi}$$
(as usual with $N\geq 3$ odd); $g$ will be the constant map equal to $1$, and $f$ one of the following two functions, introduced in \eqref{defL+-}:
\begin{equation}\label{defL+-modif}
	f(z) = \left\lbrace
	\begin{array}{ll}
		f_-(z):= \mathcal{L}_-(z;\bl_{0,\infty},\bl_{1,\infty}) := {\rm Li}_2(e^{\bl_{0,\infty} + z})+z^2- \bl_{1,\infty} z& 
		\\
		f_+(z) := \mathcal{L}_+(z;\bl_{0,\infty},\bl_{1,\infty}) := {\rm Li}_2(e^{\bl_{0,\infty} + z})+z^2 -(\bl_{1,\infty}-2i\pi) z . 
		\end{array}\right.
\end{equation}
With these notations, and for $\textstyle s_N^-,s_N^+\in ]0,\frac{2\pi}{N}[$, we are going to describe some asymptotics of the integrals
\begin{equation}\label{notInjui25} I_{n,\pm} :=  \int_{i[s_N^-,2\pi-s_N^+]}  e^{n(-i) f_{\pm}(z)} dz.
\end{equation}
Note that the endpoints $s_N^-,s_N^+$ of the contour are moving to $0$ or $2\pi i$ as $N\rightarrow +\infty$, which lie on branch cuts of the functions $f_\pm$. Eventually, our analysis will be achieved by taking $s_N^-$ not too small, namely (see the end of Section \ref{smallIsN})
\begin{equation}\label{sNvalue}
s_N^- := \alpha \frac{\pi}{N},\ \alpha\in ]0,1[.
\end{equation}
We begin in Section \ref{sub:small:vert:int} with the asymptotics of integrals along small contours in $i\mr$, near $0$ or $2i\pi$. These asymptotics will be used several times in the following sections.


\subsection{Asymptotics of integrals $\textstyle \int e^{\scriptscriptstyle{\frac{N}{2\pi} {\rm Cl}_2(t)}}dt$ }\label{sub:small:vert:int}


\subsubsection{Along $[\pi,2\pi]+2k\pi$, $k\in \mz$.}\label{smallpijuil25}

Recall that Clausen's function
\begin{equation}\label{Clausenf} {\rm Cl}_2(t) = -\int_0^t \Log\vert 2\sin(t/2)\vert dt
\end{equation}
is $2\pi$-periodic and odd (\cite{Z}). Therefore it is enough to make our analysis over $[-\pi,0]$. Since ${\rm Cl}'_2(t)= -\Log\vert 2\sin(t/2)\vert$ for all $t \notin 2\pi \Z$, we have ${\rm Cl}''_2(t)= -\cot(t/2)/2$ for the same $t$, which implies that the Clausen function is convex on $[-\pi,0]$. It vanishes at $-\pi$ and $0$, is negative on $]-\pi,0[$, and has a strict minimum ${\rm Cl}_2\left (-\pi/3\right )= -1.10149...$ that we will denote $-m$.

Since the graph of a convex function lies under its chords, it follows
$${\rm Cl}_2(t)\leqslant -\dfrac{3 m}{2\pi}t-\dfrac{3m}{2}\ \text{for\ all}\ t \in \left [-\pi,-\frac{\pi}{3}\right ], \ \text{and}\ 
{\rm Cl}_2(t)\leqslant \dfrac{3 m}{\pi}t \ \text{for\ all}\ t \in \left [-\frac{\pi}{3},0\right ].$$

Hence we can compute the upper bound:
\begin{align*}
0 < \int_{-\pi}^0 e^{\frac{N}{2\pi} {\rm Cl}_2(t)}dt 
&= \int_{-\pi}^{-\pi/3} e^{\frac{N}{2\pi} {\rm Cl}_2(t)}dt 
+\int_{-\pi/3}^0 e^{\frac{N}{2\pi} {\rm Cl}_2(t)}dt \\
&\leqslant \int_{-\pi}^{-\pi/3} e^{\frac{N}{2\pi} \left (-\frac{3 m}{2\pi}t-\frac{3m}{2}\right )}dt 
+\int_{-\pi/3}^0 e^{\frac{N}{2\pi} \frac{3 m}{\pi}t}dt \\
&= 
e^{-\frac{3Nm}{4\pi}}
\frac{(-4)\pi^2}{3 m N}
\left (e^{\frac{Nm}{4\pi}}- e^{\frac{3Nm}{4\pi}}\right )
+ \frac{2\pi^2}{3 m N}\left (1- e^{-\frac{Nm}{2\pi}}\right )\\
&= \frac{2\pi^2}{ m N}\left (1+o_{N\to \infty}(1)\right )\\
&= o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ).
\end{align*}

Since $e^{\frac{N}{2\pi} {\rm Cl}_2}\geqslant 0$, this generalizes to
$$\int_{I} e^{\frac{N}{2\pi} {\rm Cl}_2(t)}dt= o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right )$$
for any sub-part $I$ of $[-\pi,0]$ or $[\pi,2\pi]
$.


\subsubsection{Along $[0,s_N^-]$} \label{smallIsN} The Clausen function is positive and increasing on $[0,\pi/3]$, so to get an upper bound it is enough to discuss the asymptotical behaviour of the constant integral 
$$\int_{[0, s_N^-]} e^{\frac{N}{2\pi} {\rm Cl}_2(s_N^-)} = s_N^- \cdot e^{\frac{N}{2\pi} {\rm Cl}_2(s_N^-)}. $$ 
We want to prove that $s_N^- \cdot e^{\frac{N}{2\pi} {\rm Cl}_2(s_N^-)} = o_{N \to \infty}\left ( \frac{1}{\sqrt{N}}\right )$.

Recall that $\textstyle s_N^-\in ]0,\frac{2\pi}{N}[$. For all $x\in (0,1)$ we have
$$ \frac{x}{2} < x-\frac{x}{3} < x - \frac{x^3}{3} < \sin(x) < x.$$
Thus, for any $N\geqslant 7$ and any $t\in (0,s_N^-]$ we have
$$ \frac{t}{2} = \frac{2(\frac{t}{2})}{2} < 2 \sin\left (\frac{t}{2}\right )< 2\left (\frac{t}{2}\right ) = t,$$
and therefore $\Log(t)-\Log(2) < \Log \left (2 \sin\left (t/2\right )\right ) < \Log(t)$. By integrating the opposite of this inequality, we obtain for all $t \in (0,s_N^-]$,
$$t -t\Log(t) <  {\rm Cl}_2(t) < \Log(2) t + t - t \Log(t).$$
(This notably implies that ${\rm Cl}_2(t) \sim_{t \to 0^+} -t\Log(t)$ but we will use the more precise double inequality in what follows.) By evaluating the previous double inequality at $t=s_N^-$ we get
$$-s_N\Log(s_N^-) <  {\rm Cl}_2(s_N^-) < \Log(2) s_N^- + s_N^- - s_N^- \Log(s_N^-)$$
and thus 
$$ s_N^- \cdot e^{\frac{N}{2\pi} {\rm Cl}_2(s_N^-)} <  s_N^-\cdot e^{\frac{N}{2\pi}s_N\left (\Log(2)+1-\Log(s_N^-)\right )}.$$
In particular, if $s_N^-=\alpha \frac{\pi}{N}$, where $\alpha \in ]0,1[$, then we get
$$ s_N^- \cdot e^{\frac{N}{2\pi} {\rm Cl}_2(s_N^-)} <  \alpha \frac{\pi}{N} \cdot e^{\frac{\alpha}{2}\left (\Log(2)+1+\Log(N) - \Log(\pi)-\Log(\alpha)\right )}= \dfrac{\text{Constant}}{N^{1-\frac{\alpha}{2}}}=o_{N\to \infty}\left (\frac{1}{\sqrt{N}}\right ).$$
