---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-025-63-the-corepresentation-space
section_title: "The corepresentation space"
section_number: 6.3
pages: 51-53
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.939
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:Trans:corep}
Recall that $W$ satisfies the pentagon equation and the coaction axiom \eqref{DW}. In a more familiar form we see that $W'=W_{21}:=\S W \S \in M(\hat{\cA}\ox \cA)$ satisfies
\Eq{(1\ox \D)W' = W_{12}'W_{13}'.}
Hence if we treat $W'$ as an element in $M(\cB(\cH)\ox \cA)$ instead, we obtain the \emph{left regular corepresentation}
\begin{eqnarray} \Pi: \cH &\to& \cH \ox M(\cA)\nonumber\\
f&\mapsto& W'(f\ox 1)
\end{eqnarray}
which satisfies 
\Eq{ (1\ox \D)\circ \Pi = (\Pi \ox 1)\circ \Pi.}

This corepresentation picture is useful when we study the corepresentation of the quantum double. Therefore we introduce the transformation from $\cH$ to $\cH_{corep}$ so that $\hat{\cA}$ acts canonically. Similarly, by considering $\hat{W}$, we also describe the transformation so that $\cA$ acts canonically on $\hat{\cH}$.
\begin{Def} We define the transformation $\cT_{co}:\cH\to\cH_{corep}$ by
\begin{eqnarray} 
\cT_{co}: f(s,t)&\mapsto& f(-s,s-t+\frac{iQ}{2})G_b(\frac{Q}{2}-is+it)\inv,\\
\cT_{co}\inv: f(s,t)&\mapsto& f(-s,-t-s+\frac{iQ}{2})G_b(-it).
\end{eqnarray}

Similarly, we define the transformation $\hat{\cT}_{co}:\hat{\cH}\to\hat{\cH}_{corep}$ by
\begin{eqnarray}
\hat{\cT}_{co}:\hat{f}(s,t)&\mapsto& f(-s,s-t+\frac{iQ}{2})G_b(\frac{Q}{2}+is-it)e^{2\pi is(s-t+\frac{iQ}{2}),}\\
\hat{\cT}_{co}\inv:\hat{f}(s,t)&\mapsto&f(-s,-t-s+\frac{iQ}{2})e^{2\pi ist}G_b(Q+it)\inv.
\end{eqnarray}
\end{Def}

\begin{Prop} Under the transformation $\cT_{co}$, the action of $\hat{\cA}$ on $\cH_{corep}$ is given by
\Eq{\hat{A}=e^{-2\pi bs},\tab \hat{B}=e^{2\pi bp_s}.}
Under the transformation $\hat{\cT}_{co}$, the action of $\cA$ on $\hat{\cH}_{corep}$ is given by
\Eq{A=e^{2\pi bs},\tab B=e^{2\pi bp_s}.}
Furthermore, the $L^2$ measure on $\cH_{corep}$ and $\hat{\cH}_{corep}$ becomes the standard Lebesgue measure.
\end{Prop}
\begin{proof} It suffices to see that the transformations can be written as
\Eq{\cT_{co}=(t\mapsto t-s)\circ (-s,-t)\circ (t\mapsto t+\frac{iQ}{2}) \circ G_b(-it)\inv,}
\Eq{\hat{\cT}_{co}=(t\mapsto t-s)\circ (-s,-t)\circ (t\mapsto t+\frac{iQ}{2}) \circ G_b(Q+it)e^{-2\pi ist},}
followed by applying the transformation rules.
\end{proof}

This choice allows us to reproduce the representation from the pairing between $\cA$ and $\hat{\cA}$ given by the corepresentation associated to the multiplicative unitary.

\begin{Prop} The left regular corepresentation associated to $W'$ on $\cA$ is given by
\Eq{f(s,t)\mapsto \int_{\R+i0} \frac{f(s+\t,t)}{G_b(Q+i\t)}B^{ib\inv\t} A^{ib\inv s}d\t .}
\end{Prop}
\begin{Rem} Note that the left regular corepresentation is related to the left ``fundamental" representation
\Eq{\label{qplanecorep}\int f(s)x^{b\inv (-\frac{Q}{2}+is)}ds\mapsto \left(\int f(s)(xA+B)^{b\inv (-\frac{Q}{2}+is)}ds\right)\d^{-\frac{1}{2}},}
i.e.
\Eq{f(s)\mapsto \int f(s+\t)\frac{G_b(-i\t)G_b(\frac{Q}{2}-is)}{G_b(\frac{Q}{2}-i\t-is)}A^{ib\inv s-\frac{Q}{2b}}B^{ib\inv \t}A^{\frac{Q}{2b}}d\t}
$$=\int f(s+\t)\frac{G_b(\frac{Q}{2}+is+i\t)}{G_b(Q+i\t)G_b(\frac{Q}{2}+is)}B^{ib\inv \t}A^{ib\inv s}d\t$$
by multiplication by $G_b(\frac{Q}{2}+is)\inv$. Here $\d=A^{-\frac{Q}{b}}$ is the modular element.
\end{Rem}

\begin{Prop}\label{Bqaction} Under the pairing $\<1\ox \cA_q^*, W'(f\ox 1)\>$, the left regular representation of the quantum plane algebra $\cB_q=\cA_q^*$ is given by the canonical action
\Eq{X=e^{2\pi bs},\tab Y=e^{2\pi b(p_s+s)}.}
Similarly we can define the action of its modular double counterpart
\Eq{\til[X]=e^{2\pi b\inv s},\tab \til[Y]=e^{2\pi b\inv (p_s+s)},}
so that it extends to a representation of the modular double $\cB_{q\til[q]}$. Under a unitary transform by multiplication by $e^{\pi is^2}$ on $\cH_{corep}$, the action becomes the canonical action of $\cB_{q\til[q]}$.
\end{Prop}
\begin{proof}
It follows directly from Proposition \ref{lamda} since $\l$ is the identity map, hence the elements of $\hat{\cA}$ are sent to the corresponding actions. Now the formula follows from the definition $X=\hat{A}\inv, Y=q\hat{B}\hat{A}\inv$.
\end{proof}

Similarly the corepresentation associated to $\hat{W}'$ is given by
\Eq{f(s)\mapsto \int f(s+\t)G_b(-i\t)\hat{B}^{ib\inv \t}\hat{A}^{ib\inv s}d\t.}

For completeness, by composing $\cT_{co}$ with $\cT\inv$, we obtain the transformation $\cS:\cH_{rep}\to\cH_{corep}$
\begin{Prop}\label{Strans}The transformation $\cS:\cH_{rep}\to \cH_{corep}$ is given by
\begin{eqnarray}
\cS: f(s,t) &\mapsto&\int_\R f(\a-s, \a-t)G_b(\frac{Q}{2}-is+it)\inv e^{2\pi i(\a-s)s} d\a,\\
\cS\inv: f(s,t)&\mapsto& \int_\R f(\a-s,\a-t)G_b(\frac{Q}{2}+is-it) e^{-2\pi i(\a-s)s} d\a.
\end{eqnarray}

Similarly we define the corresponding transformation for $\cA$ using $\hat{\cS}:\hat{\cH}_{rep}\to\hat{\cH}_{corep}$ by
\begin{eqnarray}
\hat{\cS}: \hat{f}(s,t)&\mapsto& \int_\R f(\a-s,\a-t)G_b(\frac{Q}{2}+is-it)e^{-2\pi i(\a-s)s}d\a,\\
\hat{\cS}\inv: \hat{f}(s,t)&\mapsto& \int_\R f(\a-s,\a-t)G_b(\frac{Q}{2}-is+it)\inv e^{2\pi i(\a-s)s}d\a.
\end{eqnarray}
\end{Prop}
