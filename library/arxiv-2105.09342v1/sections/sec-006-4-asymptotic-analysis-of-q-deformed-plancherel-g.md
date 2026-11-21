---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-006-4-asymptotic-analysis-of-q-deformed-plancherel-g
section_title: "Asymptotic analysis of q-deformed Plancherel growth of second kind"
section_number: 4
pages: 15-17
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.987
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
\label{subsec:qdkind1}


In this section, we discuss the growth process controlled by the \qd probability measure considered in \cite{Strahov07}, given by \eqref{eq:Strahov-qPlancherel}. The partition function \eqref{q-partition} can be written as
\begin{equation}\label{eq:PF_Strahov}
Z_q=\sum_{k=1}^{\infty}\sum_{\lambda_k} \exp[S_{eff}(h_i)]e^{-\frac{\ln q}{6}N(N-1)(N-2)}
\end{equation}
where the effective action is given by (see \ref{app:calculationofZ})
\begin{equation}
\label{eff-S}
\begin{aligned}
S_{eff}(h_i) = k\ln t(1-q) +k\ln k -k & + \sum_{ i\neq j} \frac{1}{2} \ln |h_i-h_j|-\sum_{i} (h_i \ln h_i -h_i) \\
& + \sum_{ i\neq j}  \frac{1}{2}\ln |q^{h_j}-q^{h_i}| -\sum_{i=1}^{N} \sum_{j=1}^{h_i} \ln (1-q^j).
\end{aligned}
\end{equation}
In the continuum limit, the effective action takes the form
\begin{equation}
\begin{aligned}
S_{eff}[h(x)]&=N^2\left[k'\ln t(1-q)N+k' \ln k' -k'-\int_0^1 dx\ (h(x)\ln h(x)-h(x))\right.\\
&\hspace*{-1.7cm}\left.+\frac{1}{2}\int_0^1 dx \Xint-_{0}^{1} dy \left(\ln |q^{Nh(x)}-q^{Nh(y)}|
+\ln|h(x)-h(y)|\right)-\int_0^1 dx \int_0^{h(x)}dy\ \ln(1-q^{Ny})\right].
\end{aligned}
\end{equation}
In the double scaling limit (\ref{eq:doublescalling}), the dominant contribution to the partition function comes from the configurations satisfying the saddle point equation
\begin{equation}
\label{fulleom}
\Xint-_{h_{L}}^{h_{U}} dh' u(h')\left[\coth \frac{\lambda(h-h')}{2}+\frac{2}{\lambda(h-h')}\right]=1+\frac{2}{\lambda}\ln \frac{h(1-e^{-\lambda h})}{t\lambda k'}
\end{equation}
where $[h_L,h_U]$ denotes the support of $u(h)$. Our goal is to find a solution of (\ref{fulleom}) for $\lambda\neq 0$.\\
In order to solve the saddle point equation (\ref{fulleom}), we take the following ansatz for $u(h)$
\begin{equation}
\label{eq:u_ansatz}
u(h)=
\begin{cases}
1 &\mbox{for}\ 0\leq h\leq a \\
\tilde{u}(h) &\mbox{for}\  a\leq h\leq b.
\end{cases}
\end{equation}
The equation of motion \eqref{fulleom} takes the form
\begin{equation}
\label{eom2}
\Xint-_{a}^{b} dh'\ \tilde{u}(h')\left[\coth \frac{\lambda(h-h')}{2}+\frac{2}{\lambda(h-h')}\right]=1-a+\frac{2}{\lambda}\ln \left[\frac{(h-a)(1-e^{-\lambda (h-a)})}{\lambda \xi^2}\right].
\end{equation}
The kernel in the above integral equation is nontrivial. It is difficult to do a change of variable which brings the kernel to a standard form. However, the $\coth$ part of the kernel has the same singular structure as that of the second part. We therefore expand the $\coth$ part in powers of $\lambda$ and separate out the singular part. The derivation is given in \ref{app:strahov}. To find $\tilde{u}(h)$, we again define a resolvent function as in \eqref{eq:def_resolvent}. We provide the explicit calculations for the resolvent in \ref{app:strahov}. Here, we present the final answer.

\begin{eqnarray} 
\label{resolvent-exact}
\begin{split}
 H(h) = \ln \frac{h}{\xi} & + \ln \frac{\sqrt{b}-\sqrt{a}}{\sqrt{b}+\sqrt{a}}+\ln \frac{h + \sqrt{a b} - \sqrt{(h-a)(h-b)}}{h-\sqrt{a b} + \sqrt{(h-a)(h-b)}} + \frac{\lambda}{4}(1-a)+\sum_{k=1}^{\infty} A_{k}^{(1)}\sqrt{\frac{(h-a)}{(h-b)}} \\ & + \sum_{k=1}^{\infty}A_{k}^{(2)}\frac{_2F_1(1,\frac{1}{2}+k,2+k,\frac{a-b}{a-h})}{\sqrt{(h-a)(h-b)}}+\sum_{k=1}^{\infty}\sum_{n=0}^{2k-1}A_{k,n}^{(1)}\sqrt{\frac{(h-a)}{(h-b)}} \\ & + \sum_{k=1}^{\infty}\sum_{n=0}^{2k-1}A_{k,n}^{(2)}\frac{_2F_1(1,\frac{1}{2}+n,2+n,\frac{a-b}{a-h})}{\sqrt{(h-a)(h-b)}}       
\end{split}
\end{eqnarray}

where $A_k$'s are given by equation (\ref{eq:Aks}). Different moments, $\mathfrak{h}_n$ (defined in \eqref{shifted-moment}) appear on the right hand side of this expression, which are a priori not known. Hence, the saddle point equation has to be solved recursively. However, if we calculate the resolvent order by order in $\lambda$, the moments start appearing only at order $\lambda^2$. The result up to order $\lambda$ is given by

\begin{equation}
\label{resolvent-approx}
\begin{aligned}
 H(h)&=\ln \frac{h}{\xi}+\ln \frac{\sqrt{b}-\sqrt{a}}{\sqrt{b}+\sqrt{a}}+\ln \frac{h+\sqrt{ab}-\sqrt{(h-a)(h-b)}}{h-\sqrt{ab}+\sqrt{(h-a)(h-b)}}+\frac{\lambda}{4}(1-h)\\&\hspace{1cm} + \frac{\lambda\sqrt{(h-a)(h-b)}}{4}.
\end{aligned}
\end{equation}

The support of $\tilde{u}(h)$ can be found from the asymptotic behaviour of the resolvent. Up to first order in $\lambda$, we get

\begin{eqnarray}
a = 1-2\xi +\lambda\frac{\xi^{2}}{2},\quad
b = 1+2\xi +\lambda\frac{\xi^{2}}{2}.
\end{eqnarray}

and the Young diagram density is given by

\begin{equation}\label{eq:tildeuhstrahov}
\tilde{u}(h)=\frac{1}{\pi}\cos^{-1}\Big(\frac{2h-a-b}{b-a}\Big)-\frac{\lambda\sqrt{(h-a)(b-h)}}{4\pi}.
\end{equation}

Since $a\geq 0$, the above solution is valid for 

\be\label{eq:xilimitstrahov}
0<\xi\leq \frac12 +\frac{\lambda}{16}.
\ee

$\tilde u(h)$ given by (\ref{eq:tildeuhstrahov}) describes the automodel class of \cite{Kerov1} corrected up to first order in $\lambda$. It is easy to check from equations (\ref{q-automodel-D}) and (\ref{eq:tildeuhstrahov}) that the order $\lambda$ correction to automodel density in both the cases is same apart from a factor of half. The reason behind this is the appearance of $\text{dim}\lambda_k$ in (\ref{eq:Strahov-qPlancherel}). 

The limit shape corresponds to the upper limit of $\xi$ given in (\ref{eq:xilimitstrahov}). We plot the limit shape in a rotated coordinate system (see \cite{Chattopadhyay:2019pkl} for coordinate transformation) in fig \ref{fig:strahov-ls}. It is clear that the symmetric property of the distribution \cite{Chattopadhyay:2019pkl} is lost under \qq deformation. 

\begin{figure}[H]
	\begin{center}
		\includegraphics[scale=0.4]{strahov-ls.pdf}
		\caption{The limit shape for a $q$-deformed ($\lambda=0.97$) Plancherel growth process (green curve) and its $q\rightarrow 1$ ($\lambda\rightarrow 0$) limit (orange curve) for comparison.}
		\label{fig:strahov-ls}
	\end{center}
\end{figure}

Thus, we see that both the measures (\ref{eq:Strahov-qPlancherel} and \ref{eq:qmeasure2}) qualitatively give the similar asymptotic behaviour up to order $\lambda$. However, we emphasise that (\ref{q-automodel-D}) is exact in $\lambda$.
