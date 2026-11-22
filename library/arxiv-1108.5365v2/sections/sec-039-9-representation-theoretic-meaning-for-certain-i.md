---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-039-9-representation-theoretic-meaning-for-certain-i
section_title: "Representation theoretic meaning for certain integral transforms"
section_number: 9
pages: 88-89
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.966
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:meaning}
In this section, we state without proof certain integral transformations of $G_b$ that arise in the calculations of certain representation relations.
\begin{Prop} The pentagon equation $W_{23}W_{12}=W_{12}W_{13}W_{23}$ is equivalent to the 4-5 relation (Lemma \ref{45})
\Eq{\frac{G_b(\a)G_b(\b)G_b(\c)}{G_b(\a+\c)G_b(\b+\c)}=\int_C d\t e^{-2\pi \c\t}\frac{G_b(\a+i\t)G_b(\b+i\t)}{G_b(\a+\b+\c+i\t)G_b(Q+i\t)}.}
By a change of variables and using the reflection formula, it can be rewritten as
\Eq{\frac{G_b(\a+\c)G_b(\b+\c)G_b(\a)G_b(\b)}{G_b(\a+\b+\c)}=\int_C d\t e^{-2\pi i(\b+i\t)(\a+i\t)}G_b(\a+i\t)G_b(\b+i\t)G_b(\c-i\t)G_b(-i\t).}
Scaling all the variables by $b$ and taking the limit $b\to 0$ by applying Theorem \ref{classicallimit}, we recover precisely Barnes' first lemma:
\Eq{\frac{\G(a+c)\G(b+c)\G(a)\G(b)}{\G(a+b+c)}=\frac{1}{2\pi }\int_C\G(a+i\t)\G(b+i\t)\G(c-i\t)\G(-i\t) d\t} in the special case for $d=0$.
\end{Prop}

Next, as noted in Section \ref{sec:regular:left}, by comparing $\bW_m=\iint^{\o+} T^{\l,t/2} dt d\mu(\l)$ as corepresentation, we obtain the following relation that is first observed by Volkov \cite{Vo}:
\begin{Prop}\label{69}
The 6-9 relation for $G_b(x)$ can be written as
\begin{eqnarray}
&&\int_C e^{-2\pi \t (\d-i\t)} \frac{G_b(\a+i\t)G_b(\b+i\t)G_b(\c+i\t)G_b(\d-i\t)G_b(-i\t)}{G_b(\a+\b+\c+\d+i\t)} d\t\nonumber\\
&=&\frac{G_b(\a)G_b(\b)G_b(\c)G_b(\a+\d)G_b(\b+\d)G_b(\c+\d)}{G_b(\a+\b+\d)G_b(\a+\c+\d)G_b(\b+\c+\d)},
\end{eqnarray}where the contour goes along $\R$ and separates the increasing and decreasing sequence of poles. By the asymptotic properties of $G_b$, the integral converges for any choice of parameters.

Again by scaling all the variables by $b$ and applying Theorem \ref{classicallimit}, we recover Barnes' second lemma:
\begin{eqnarray}
&&\int_C \frac{\G(a+i\t)\G(b+i\t)\G(c+i\t)\G(d-i\t)\G(-i\t)}{\G(a+b+c+d+i\t)}d\t\nonumber\\
&=&\frac{\G(a)\G(b)\G(c)\G(a+d)\G(b+d)\G(c+d)}{\G(a+b+d)\G(a+c+d)\G(b+c+d)},
\end{eqnarray}
which in turn is a generalization of Pfaff-Saalsch\"{u}tz's sum
\Eq{\sum_{j\geq 0} \frac{(n+m+l+k-j)!}{(m-j)!(l-j)!(k-j)!(n+j)!j!}=\frac{(n+m+l)!(n+m+k)!(n+l+k)!}{m!l!k!(n+m)!(n+l)!(n+k)!}.}
\end{Prop}

Finally, in \cite{WZ} an alternative description of the multiplicative unitary lying instead in $\cA\ox \cA$ is defined to be (slightly modified to fit our definition):
\Eq{V=g_b(B\inv\ox q\inv BA\inv)e^{\frac{i}{2\pi b^2}\log (qAB\inv)\ox \log A\inv},}
so that
\Eq{V(x\ox 1)V^* = \D(x).}
On comparing
\Eq{W^*(1\ox x)W = \D(x) = V(x\ox 1)V^*}
as operators on $\cH\ox\cH$, we obtain a new relation involving $G_b(x)$, which is essentially the same as the relation in \cite[Theorem 5.6.7]{VdB} in the case $n=1$:
\begin{Prop}\label{32} The 3-2 relation is given by
\Eq{\int_C G_b(\a+i\t)G_b(\b-i\t)G_b(\c-i\t)e^{-2\pi i(\b-i\t)(\c-i\t)}d\t = G_b(\a+\c)G_b(\a+\b),}
where the contour goes along $\R$ and separates the poles for $i\t$ and $-i\t$. By the asymptotic properties for $G_b$, the integral converges for $Re(\a-\b-\c)<\frac{Q}{2}$.
\end{Prop}

\addcontentsline{toc}{section}{References}
