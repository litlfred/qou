---
doc_id: arxiv-hep-th-9609174v2
doc_title: "arXiv:hep-th/9609174v2 23 Sep 1996"
section_id: sec-007-4-conclusion-and-speculation
section_title: "Conclusion and speculation"
section_number: 4
pages: 15-18
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.859
doc_brief: "arXiv:hep-th/9609174v2 23 Sep 1996 — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom matrices in the microscopic limit."
---
\noindent
In the present work we have proven two theorems
concerning the asymptotic behavior of orthogonal polynomials 
for a broad class of measures. 
They show a remarkable asymptotic universality 
near the origin, a relation previously only known for the classical
orthogonal polynomials of generalized Laguerre and Jacobi type \cite{Sze}. 
Furthermore, we have used this highly universal behavior 
to prove universality
conjectures regarding the spectral densities and their
$s$-point correlators in the microscopic limit.

\vspace{12pt}\noindent
All of these proofs refer to the zero-dimensional matrix model 
language alone. 
And, as we have emphasized in the Introduction, 
the assumption that this universality
can be applied to full $d$-dimensional quantum gauge theories
with fermionic fields is {\em a priori} very far from obvious.
Of course, our matrix model universality theorems are
interesting in their own right. But from a particle physics perspective
the real focus should be on the application of 
these theorems to the Dirac operator spectrum \cite{V93}.

\vspace{12pt}\noindent
How could we imagine the link between random matrix models and gauge
theories established in this connection? 
Consider a Euclidean
four-dimensional 
${\rm SU}(N_c)$ 
gauge theory coupled to $N_f$ light fermions in, say, 
the fundamental representation. Assume that 
$N_f$ is small enough to
allow for the conventional scenario of 
spontaneous chiral symmetry breaking.
Let us simply call such a theory ``QCD''. 
Its partition function can
be written formally as
\begin{equation}
Z_{\rm QCD}=
\int \frac{{\cal D}A_\mu}{\rm (Gauge)}
\prod_{f=1}^{N_f}{\cal D}\bar{\psi}_f{\cal D}\psi_f
\,\e^{-S[A]-\int\bar{\psi}_f ({\rm i} D\!\llap{/}+m_f)\psi_f} ~, 
\end{equation}
where $S[A]$ is the gauge field part of the action. 
Consider the theory in a finite volume $V_4$. 
Let us now seek a
low-energy effective description of this theory.
One way is the chiral Lagrangian ($\chi$L) approach,
which in this case introduces considerable simplification due to the
suppression of all derivative terms 
(since one is interested only in the
very soft modes) \cite{LS}. 
Here the chiral condensate at zero mass,
$\langle \bar{\psi}\psi\rangle \equiv \Sigma$ is by
construction assumed to be non-vanishing.
Below is a schematic picture of how one could imagine 
random matrix theory to fit into this framework:
\[
\begin{array}{ccc}
Z_{\rm QCD}=
\int \frac{{\cal D}A_\mu}{\rm (Gauge)}
\,\e^{-S[A]}\,\prod_f\det ({\rm i} D\!\llap{/}+m_f)
&
\stackrel{\mbox{(b)}}{\longrightarrow}&
Z_{\chi{\rm UE}}=\int \d M\,\e^{-NV(M)}\,\prod_f\det
(M+m_f)\\
\ & \ & \ \\
\downarrow \mbox{(a)}&
\ &
\mbox{(c)}
\downarrow 
\\
\ & \ & \ \\
Z_{\chi {\rm L}}=\int_{{\rm SU}(N_f)} \d U\,
\e^{N\Sigma\,{\rm tr}\,{m} U \, \e^{{\rm i}\frac{\theta}{N_f}}+c.c.}&
\stackrel{\mbox{(d)}}{\longleftarrow} &
Z_{\chi{\rm GUE}}=\int \d M\,\e^{-N\Sigma^2\,{\rm tr}\,M^2}
\,\prod_f \det(M+m_f)
\end{array}
\]

\vspace{12pt}\noindent
This link (a)
is, however, based on the 
global symmetry breaking pattern
${\rm SU}(N_f)_{\rm L}\times{\rm SU}(N_f)_{\rm R}
\rightarrow{\rm SU}(N_f)_{\rm V}$ alone 
and thus by no means
refers to the microscopic theory.

\vspace{12pt}\noindent
Let us now consider a different route (b)-(c)-(d):
suppose we start with QCD in a finite volume, 
and with a sharp ultraviolet cut-off. 
(One would like to think of conventional lattice regularizations,
were it not for the known difficulties of defining massless fermionic
degrees of freedom in that case.)
Consider the formal change of integration variables
from the gauge field $A_{\mu}(x)$ to the Dirac operator
${\rm i} D\!\llap{/}=A\!\llap{/}(x)+{\rm i} \partial\!\llap{/}~
\equiv M$
itself (b).
Since $V_4$ is the size of the matrix $M$, we write $N=V_4$.
Although we can hardly imagine computing the Jacobian $J$ of
this transformation
the resulting partition function would formally look like the
random matrix model above,
with $V(M)=S[A(M)]-\log J(M)$.
Once phrased in a matrix model language, we can apply our Theorem 1
to substitute the uncomputable $V(M)$ by
another simple measure, say that of the Gaussian unitary ensemble (GUE)
with $V(M)=\Sigma^2\,{\rm tr}\,M^2$.
This GUE can be shown to be expressible as
the zero-dimensional chiral Lagrangian 
in the microscopic limit (d) \cite{V93}.
If the relation (b) between
a properly regularized version of QCD
and a particular random matrix model
were not still very formal and weakly established, 
the diagram would otherwise close itself full circle. 
The diagram above at least serves as an intuitive picture 
outlining the logical routes
between the different formulations, and the r\^{o}le played by our
universality theorems proposed in this connection.\\

\vspace{12pt}\noindent
{\large {\bf Acknowledgements}}\\

\noindent
P.H.D.~would like to thank J.~Verbaarschot for an early discussion, 
and P.~Nevai and W.~Van Assche for e-mail correspondences.
G.A.~wishes to thank the Niels Bohr Institute
for its warm hospitality while this work
was being started.
The work of S.N.~is supported by 
JSPS Postdoctoral Fellowships for Research Abroad.

\newpage
