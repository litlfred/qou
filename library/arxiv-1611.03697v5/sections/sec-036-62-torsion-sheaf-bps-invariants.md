---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-036-62-torsion-sheaf-bps-invariants
section_title: "Torsion sheaf BPS invariants"
section_number: 6.2
pages: 30-31
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.973
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Let $\cA=\Coh_{\leq 1}(X)$ denote the abelian category of coherent sheaves on $X$ supported in dimension $\leq 1$.  Any  sheaf $E\in \cA$ has a Chern character $\ch(E)\in H^*(X,\bZ)$, which via Poincar{\'e} duality we can view as an element
\[\ch(E)=(\beta,n)\in \Gamma=H_2(X,\bZ)\oplus \bZ.\]
We note that for any objects $E_1,E_2$ of $\cA$, the Riemann-Roch theorem tells us that
\[\chi(E_1,E_2)=\sum_{i\in \bZ} (-1)^i \dim_\bC \Ext^i_X(E_1,E_2)=\int_X \ch(E_1)^{\dual}\ch(F)\td(X) =0,\]
because the intersection number of any two curves on a threefold is zero. We therefore take $\<-,-\>$ to be the zero form  on  $\Gamma$. We define a central charge
$Z\colon \Gamma\to \bC$ via the formula \[Z(\beta,n)=2\pi(\beta\cdot \omega_\bC-n),\]
where $\omega_\bC=B+i\omega\in H^2(X,\bC)$ is a complexified K{\"a}hler class.
The assumption that $\omega$ is  K{\"a}hler  ensures that for any nonzero object $E\in \cA$ the complex number $Z(E)\in \bC$ lies in the semi-closed upper half-plane
\[\bar{\cH}= \{z=r\exp(i\pi \phi): r\in \bR_{>0}\text{ and }0<\phi\leq 1\}\subset \bC^*.\]

It follows that $Z$  defines a stability condition on the abelian category $\cA$.
 
For each class $\gamma\in \Gamma$ there is an associated BPS invariant
$\Omega(\gamma)\in \bQ$  first constructed by Joyce and Song (\cite{JS}, see particularly Sections 6.3--6.4). They  are defined using moduli stacks of semistable objects in $\cA$, and should not be confused with the ideal sheaf curve-counting invariants appearing in the famous MNOP conjectures \cite{MNOP}.  Joyce and Song prove that the numbers $\Omega(\gamma)$  are independent of the complexified K{\"a}hler class $\omega_\bC$. This is to be expected, since wall-crossing is trivial when the form $\<-,-\>$ vanishes: see Remark \ref{abelian} below.

A direct calculation \cite[Section 6.3]{JS} shows that
 \begin{equation}\label{montreux}\Omega(0,n)=-\chi(X),\qquad n\in \bZ\setminus\{0\}.\end{equation}
It is expected \cite[Conjecture 6.20]{JS} that when $\beta>0$ is a positive curve class
\begin{equation}
\label{lausanne}
\Omega(\pm \beta,n)=\GV(0,\beta),\end{equation}
and, in particular, is independent of $n$.  We shall assume this in what follows.
 We emphasise that the higher genus Gopakumar-Vafa invariants are invisible from the point-of-view of the  torsion sheaf invariants $\Omega(\gamma)$.
