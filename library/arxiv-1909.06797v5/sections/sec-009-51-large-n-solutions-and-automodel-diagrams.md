---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-009-51-large-n-solutions-and-automodel-diagrams
section_title: "Large N solutions and automodel diagrams"
section_number: 5.1
pages: 16-18
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.994
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
\label{sec:largeNphases}

All possible large $N$ solutions of (\ref{eq:saddeq2}) were discussed in \cite{duttagopakumar} and it was observed that (\ref{eq:saddeq2}) admits two possible solutions. However, here we look at the problem more carefully keeping the symmetry of the growth process in mind. From the Plancherel measure (\ref{eq:Plancherelmeasure2}) we see that at any level $k$, two Young diagrams related to each other by transposition, have same probability $\cP(\lambda_k)$. Therefore the large $N$ solution of (\ref{eq:saddeq2}) must be invariant under transposition. Young diagrams, symmetric under transposition, are called rectangular diagrams \cite{Kerov1,Hora:2237389}.

Following \cite{duttagopakumar}, we can take the following ansatz for $u(h)$ to get a rectangular Young diagram 

\ben \label{eq:uhsym}
\begin{split}\label{eq:sym-ansatz}
	u(h) = \bigg\{ {1 \qquad \hspace{.16cm}  h\in [0,p) \atop
	 \tilde u(h) \quad h\in (p,q].}
\end{split}
\een
To solve the saddle point equation we define a resolvent

\ben\label{eq:Hresolvent}
H(h) = \int_{h_L}^{h_U} \frac{u(h')dh'}{h-h'}.
\een

After a little algebra, we find that the resolvent $H(h)$ is given by \cite{duttagopakumar}

\ben \label{eq:resolventsym}
H(z)= \ln\lB\frac{h \left(h-1 -\sqrt{(h-1)^2-4 \xi ^2}\right)}{2 \xi ^2}\rB.
\een

The resolvent is same as the moment generating function for the rectangular diagrams defined in (\ref{eq:momgenfunc}) \cite{Kerov1}. The resolvent has a branch cut in the complex $h$ plane. Young diagram density is given by the discontinuity of $H(h)$ about the branch cut

\be\label{eq:sym-answer}
\tilde u(h) = \frac1\pi \cos^{-1} \lB  \frac{h-1}{2\xi}\rB, \quad \for\quad p\leq h\leq q.
\ee

The supports $p$ and $q$ are given by,

\be
p=1-2\xi, \quad q=1+2\xi.
\ee

This particular class of solution exists subject to the following condition

\be
k'=\xi^2.
\ee

Since $p\geq 0$, this solution is valid for $0\leq\xi\leq 1/2$. From the definition of $\xi$ ($\xi^2 = z k'$) we also see that this solution exists for 

\ben
\text{either} \quad \xi =k'=0 \quad \text{or} \quad z=1.
\een

The case $\xi=k'=0$ is trivial. This means there is no box in the Young diagram. The non-trivial solution corresponds to $z=1$ (i.e. fugacity is one and hence zero chemical potential). It is easy to check that the Young diagram is invariant under transposition. The height of the first column can be calculated from equation (\ref{eq:hook2}) and is given by $2\xi$ which is similar to the length of the first row. Also the function $\tilde u(h)$ is symmetric about body diagonal. A typical Young diagram for this class is depicted in figure \ref{fig:YD-english-automodel}.

\begin{figure}[h]
	\begin{center}
		\includegraphics[width=5cm,height=5cm]{YDEnglish.png}
		\caption{A Young diagram in English notation for automodel class ($0<\xi<1/2$).}
		\label{fig:YD-english-automodel}
	\end{center}
\end{figure}

In this phase the renormalised number of boxes (i.e. $k'$) in a Young diagram grows from $k'=0$ to $k'= 1/4$ as $\xi$ changes from $0$ to $1/2$. For any value of $\xi$ between $0$ and $1/2$ the dominant Young diagram is always symmetric under transposition and hence a rectangular diagram. The limiting value $\xi=1/2$ (GWW transition point) corresponds to the distribution

\be\label{eq:terminaluh}
\tilde{u}(h) =\frac1\pi \cos^{-1}(h-1).
\ee

This terminal distribution is same as the universal curve or the limit shape obtained by \cite{LogShe,VerKer77}. Hence we see that the limit shape Young diagram corresponds to GWW transition point in matrix model side. 

We calculate Plancherel measure (\ref{eq:Plancherelmeasure2}) for this dominant diagram. Following \cite{duttagopakumar}, the Plancherel measure  in large $N$ limit is given by

\be
\frac1{N^2}\ln \cP_{\lambda_k} = \int_{0}^{q} dh^{} u(h)  \ \Xint-_0^q dh' u(h') \ln|h-h'| -2 \int_0^q u(h) h \ln h \ dh  +k'+1+k'\ln k'.
\ee

Evaluating the right hand side for symmetric solutions (\ref{eq:sym-ansatz}) and (\ref{eq:sym-answer}) we get

\be
\cP_{\lambda_k} = 1 +O\lb 1/N\rb.
\ee


Thus we see that in the large $k$ (or large $N$) limit the symmetric solution (\ref{eq:sym-ansatz}, \ref{eq:sym-answer}) is the maximum probable solution. Probability of having other diagrams is suppressed by powers of $N$. This gives an alternate proof of \emph{limit shape} theorem of Vershik-Kerov and Logan-Shepp result \cite{VerKer77,LogShe}.

The partition function (\ref{eq:GCPF3}) admits another phase. The dominant diagrams in that phase are not self-transpose. See \ref{app:asymetricsol} for details. Growth of such diagrams are different than that studied in section \ref{sec:plancherel}.
