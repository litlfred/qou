---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-034-82-the-principal-series-representation
section_title: "The principal series representation"
section_number: 8.2
pages: 77-79
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.971
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:regular:principal}
By taking the pairing above with the fundamental corepresentation defined in Section \ref{sec:double:matrix}, we obtain:
\begin{Thm}\label{fundrep} The fundamental corepresentation $T^{\l,t}$ corresponds to the representation $\cP_{\l,t}$, called the \emph{principal series representation}, given on $L^2(\R,ds)$ by:
\begin{eqnarray*}
K_0 &=& e^{\pi bt},\\
K&=&e^{-\pi bs},\\
E &=&[\frac{Q}{2b}-\frac{i}{b}(s-\l)]_q e^{-2\pi bp_{s}},\\
F &=&[\frac{Q}{2b}+\frac{i}{b}(s+\l)]_q e^{2\pi bp_{s}},\\
\end{eqnarray*}
where $[n]_q=\frac{q^n-q^{-n}}{q-q\inv}$. The operators are all positive essentially self-adjoint.
\end{Thm}
\begin{proof}
Recall that we choose $c=-iq^{1/2}$ in the pairing.  Recall also that we have to multiply the expressions by $\frac{G_b(Q+i\a)G_b(Q+i\t)}{(1-q^2)^{ib\inv (\a+\t)}}$. From the expression \eqref{fundcorep} we obtain for $K_0$ and $K$ that $\t=\a=0$. The factor becomes $\dis\lim_{\a\to0}G_b(-i\a)G_b(Q+i\a)=1$ and the rest becomes
\begin{eqnarray*} 
K_0:f(s)&\mapsto&f(s)\cdot (q^{-1/2})^{ib\inv(t-s)}(q^{-1/2})^{ib\inv(t+s)}\\
&=&e^{\pi bt}f(s),\\
K:f(s)&\mapsto&f(s)\cdot (q^{-1/2})^{ib\inv(t-s)}(q^{1/2})^{ib\inv(t+s)}\\
&=&e^{-\pi bs}f(s).\\
\end{eqnarray*}
For $E$, we have $\t=-ib,\a=0$ so that the factor $\dis\lim_{\a\to0}G_b(-i\a)G_b(Q+i\a)=1$ as well, and we obtain
\begin{eqnarray*}
E:f(s)&\mapsto&\frac{-iq^{1/2}f(s+ib)}{1-q^2}\frac{G_b(\frac{Q}{2}-is+i\l+b)}{G_b(\frac{Q}{2}-is+i\l)}e^{\pi \l b-2\pi bs+\pi bt}\cdot (q^{ib\inv(t-s)})\\
&=&\frac{iq^{-1/2}}{q-q\inv} (1-e^{2\pi i b(\frac{Q}{2}-is+i\l)})e^{\pi b(\l-s)} f(s+ib)\\
&=&\frac{i}{q-q\inv}(q^{1/2}e^{\pi b(s-\l)}+q^{-1/2}e^{-\pi b(s-\l)}) f(s+ib)\\
&=&[\frac{Q}{2b}-\frac{i}{b}(s-\l)]_q f(s+ib).
\end{eqnarray*}
Finally, for $F$ we have $\a=-ib,\t=0$, the factor $\dis\lim_{\a\to-ib}G_b(-i\a)G_b(Q+i\a)=-q^2$, and we obtain
\begin{eqnarray*}
F:f(s)&\mapsto&\frac{iq^{-1/2}(-q^2)f(s-ib)}{1-q^2}\frac{G_b(\frac{Q}{2}-is-i\l)}{G_b(\frac{Q}{2}-is-i\l-b)}e^{-\pi \l b+\pi bt}\cdot (q^{ib\inv(t+s)})\\
&=&\frac{iq^{1/2}}{q-q\inv} (1-e^{2\pi i b(\frac{Q}{2}-is-i\l-b)})e^{-\pi b(\l+s)} f(s-ib)\\
&=&\frac{i}{q-q\inv}(q^{-1/2}e^{\pi b(s+\l)}+q^{1/2}e^{-\pi b(s+\l)}) f(s-ib)\\
&=&[\frac{Q}{2b}+\frac{i}{b}(s+\l)]_q f(s-ib).
\end{eqnarray*}
Since $\frac{i}{q-q\inv}=\frac{1}{2\sin(\pi b^2)}>0$, we immediately see that the operators are positive. We note that the expression for $E$ can be rewritten as
\Eq{E=\frac{i}{q-q\inv} (e^{\pi b(s-\l-p_s)}+e^{\pi b(\l-s-p_s)}),}
where the summand $q^2$-commutes. Hence using Proposition \ref{x+p}, it is unitary equivalent to $e^{\pi b(s-\l-p_s)}$ which in turn is equivalent to $e^{-\pi b(p_s+\l)}$ by multiplication by $e^{-\pi is^2}$. Hence it is essentially self-adjoint. Similar analysis applies to $F$, hence all operators are positive essentially self-adjoint.
\end{proof}

\begin{Rem} We note that by restricting to $U_q(\sl(2,\R))$, this is precisely (the Fourier transform of) the continuous series representation $\cP_{s}$ obtained in \cite{BT} given by
\begin{eqnarray*}
K\d_k&=&e^{-\pi bk}\d_k,\\
E_s\d_k&=&[\frac{Q}{2b}-\frac{i}{b}(k-s)]_q \d_{k+ib},\\
F_s\d_k&=&[\frac{Q}{2b}+\frac{i}{b}(k+s)]_q\d_{k-ib}\\
\end{eqnarray*}
under the correspondences $s\corr k, \l\corr s$.
\end{Rem}
