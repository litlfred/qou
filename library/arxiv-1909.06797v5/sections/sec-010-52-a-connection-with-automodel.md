---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-010-52-a-connection-with-automodel
section_title: "A connection with automodel"
section_number: 5.2
pages: 18-19
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.839
latex_coverage_ratio: 1.0
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
To make a precise connection between automodel class and the above solution, we need to set up a dictionary between the variables defined in $(u,v)$ plane and $(h,x)$ plane. The relation between \emph{French} notation and \emph{English} notation is $Y=n\ \tand \ X=x$. We use the following transformation between $(n,x)$ and $(u,v)$ so that 
$u=v=2$ point is mapped to $n=1, x=0$

\ben
\begin{split}
	\frac u2 &= n-x \\
	\frac v2 &= n+x.
\end{split}
\een

Using this mapping one can show that the Young diagram distribution function (\ref{eq:uhdef}) is related to $v'(u)$ in the following way

\be
\label{eq:Ivanov-our-map}
u(h) = \frac12 -\frac12 v'(u) \quad \with \quad u=2(h-1).
\ee 

One can also check that the terminal diagram (\ref{eq:terminaluh}) is exactly same as the limit shape defined in (\ref{eq:kerovfunction}). Thus we see that the Young diagram density $u(h)$ is related to \emph{charge} $\sigma(u)$ defined in (\ref{eq:youngcharge}) by $u(h) = - \sigma'(u)$. The resolvent (\ref{eq:resolventsym}) for this symmetric solution is same as the moment generating function for charges (\ref{eq:momgenfunc}).

We also observe that the symmetric distributions (\ref{eq:uhsym}) for $0<\xi<1/2$ satisfies,

\be\label{eq:automodeluh}
\dow_\xi u(h,\xi) +\frac{h-1}{\xi} \dow_hu(h,\xi)=0.
\ee

Since for this branch we have $\xi^2=k'$, the above equation can be written as,

\be\label{eq:automodeluh2}
\dow_{k'} u(h,k')+\frac{h-1}{2k'} \dow_h u(h,k') =0.
\ee

Thus we see that the Young diagram density satisfies the automodel equation\footnote{Please note the difference in notation. Here $u$ is Young diagram density and $h$ is hook number.} (\ref{eq:automodeleqnsigma}) with $k'$ playing the role of automodel time $t$. This is natural to expect that the renormalised box number $k'$ plays the role of growth parameter $t$ in Kerov's paper \cite{Kerov1}. Hence we conclude that the no-gap phase of GWW model (\ref{eq:cZ}) or  (\ref{eq:cZ2}), in the limit of large box number, captures the Plancherel growth of Young diagrams and the dominating Young diagrams belong to the automodel class of Kerov.
