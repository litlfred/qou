---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-008-51-moments-of-young-diagrams-and-conserved-charg
section_title: "Moments of Young diagrams and conserved charges"
section_number: 5.1
pages: 18-19
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 1.0
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
Following \cite{Jevicki:1993qn} one can define an infinite sequence of conserved commuting quantities 

\ben
H_n = \frac{1}{2\pi} \int dh\ d\theta\ \omega(h,\theta) \ h^n.
\een

Using the Poisson bracket (\ref{eq:poisson}) one can show that 

\ben
\{H_m,H_n\} = 0.
\een

Also, using the equations of motion (\ref{eq:boundeq}) one can show that 
\ben
\frac{d H_n}{dt} =0. 
\een

Existence of infinite number of conserved charges makes the system integrable. This is a generic feature of one matrix model and indicates that the theory is exactly solvable.

These conserved charges are related to moments of Young diagrams defined in \cite{Kerov1}. The matrix model techniques can be used to calculate the moments of automodel diagrams. Using the definitions (\ref{eq:hdistribution}), one can show that

\ben
H_n = \int dh \ u(h)\ h^n.
\een

One can define a generating function for these moments

\ben
H(h) = \int\ dh' \frac{u(h')}{h-h'} = \sum_{n=0}^\infty \frac{H_n}{h^{n+1}}.
\een

Using the expression for the resolvent (\ref{eq:Hw}) and the relation between $h$ and $w$ (\ref{eq:hwrelation}), one can show that

\ben
H_n = \sum_{i_1,\cdots, i_n \geq 1} \frac{\lambda^{i_1+\cdots +\i_n-n}}{i_1\cdots i_n} p_{i_1+\cdots+i_n}
\een

where $p_n$s are the moments associated with $H(w)$,

\be
H(w) = \sum_{n=0}^\infty \frac{p_n}{w^{n+1}}.
\ee

Since we know the exact expression for $H(w)$, one can easily find the $p_n$s from it's asymptotic expansion. In the limit $\lambda\ra 0$, we get 

\ben
H_n=p_n.
\een

Thus, we have an explicit formula to compute the moments of the asymptotic automodel diagrams.
