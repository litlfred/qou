---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-001-11-state-integrals-and-their-q-series
section_title: "State-integrals and their q-series"
section_number: 1.1
pages: 1-4
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.776
---
\lbl{sub.intro}

Multi-dimensional state integrals of products of Faddeev's quantum 
dilogarithm appear in abundance in Quantum Topology, and were studied among 
others by Hikami~\cite{Hi}, Dimofte--Gukov--Lennels--Zagier~\cite{DGLZ}, Andersen--Kashaev~\cite{AK}, and 
Kashaev--Luo--Vartanov \cite{KLV}. It is well-known to the experts 
that such state-integrals can be written as finite sums of products of pairs 
of $q$-series and $\tq$-series. The reason for this is a factorized structure 
of Faddeev's quantum dilogarithm, the structure of the set of its poles, 
and the specific form of exponential factors of the integrand of the 
state-integrals, while its derivation is based on an application of the 
residue theorem. Instead of formulating a general theorem for 
multi-dimensional integrals which obscures the principle, we will give a 
detailed proof for the case of a family of 1-dimensional integrals 
and illustrate it with some concrete examples taken from \cite{AK,KLV}. 

To state our results, recall that
{\em Faddeev's quantum dilogarithm function} $\Phi_b(x)$ is given by 
\cite{Faddeev}
\begin{equation}\lbl{fad}
\Phi_b(x)
=\frac{(e^{2 \pi b (x+c_b)};q)_\infty}{
(e^{2 \pi b^{-1} (x-c_b)};\tq)_\infty} \,,
\end{equation}
where
$$
q=e^{2 \pi i b^2}, \qquad 
\tq=e^{-2 \pi i b^{-2}}, \qquad
c_b=\frac{i}{2}(b+b^{-1}), \qquad \Im(b^2) >0. 
$$
Remarkably, this function admits an extension to all values of $b$ with 
$b^2\not\in\mathbb{R}_{\le 0}$. $\Phi_b(x)$ is a meromorphic function of $x$ with
$$
\text{poles:} \,\,\, c_b + i \BN b + i \BN b^{-1},
\qquad
\text{zeros:} \,\, -c_b - i \BN b - i \BN b^{-1} \,.
$$ 
The functional equation
$$
\Phi_b(x) \Phi_b(-x)=e^{\pi i x^2} \Phi_b(0)^2, 
\qquad
\Phi_b(0)=q^{\frac{1}{24}} \tq^{-\frac{1}{24}}
$$
allows us to move $\Phi_b(x)$ from the denominator to the numerator
of the integrand of a state-integral. 

For natural numbers $A,B$ with 
$B > A > 0$, we consider the absolutely convergent integral 
$$
\calI_{A,B}(b)=\int_{\BR + i \epsilon} \Phi_b(x)^B e^{-A \pi i x^2} dx
$$
with small positive $\epsilon$. The condition $B > A > 0$ ensures not only 
the convergence
of $\calI_{A,B}(b)$ for $\Im(b^2) >0$, but also the convergence of the 
$q$-series and the $\tq$-series (for $|q|, |\tq|<1$) that appear in 
Theorem \ref{thm.1} below.

To express the above state-integral in terms of series, consider the 
generating series
\begin{equation}
\lbl{eq.FABqx}
F_{A,B}(q,x)=\sum_{m=0}^\infty 
\frac{(-1)^{A m} q^{A \frac{m(m+1)}{2}}}{(q)^B_m}
x^m, \qquad
\ti F_{A,B}(q,x) = F_{B-A,B}(q,x) \,.
\end{equation}
Consider the operators $\d$ and $\d_k$ (for $k$ a positive natural number)
which act on the space of functions of $x$ as follows
\begin{equation}
\lbl{eq.dd}
(\d F)(x)=x \pt_x F(x), \qquad
(\d_k F)(x)=\sum_{s=1}^\infty \frac{s^{k-1} q^s}{1-q^s} F(q^sx) \,.
\end{equation}
Likewise, there are operators $\ti\d$ and $\ti\d_k$ which act on the space 
of functions of $\ti x$ and with $q$ replaced by $\tq$. It is easy to see 
that any two of the operators 
$\d$, $\d_k$, $\ti \d$, $\ti \d_k$ commute and they freely generate 
over $\BQ$ a commutative ring $\calD \otimes \ti\calD$, 
where 
$$
\calD=\BQ[\d,\d_1,\d_2,\dots], \qquad
\ti \calD=\BQ[\ti \d,\ti \d_1,\ti \d_2,\dots] \,.
$$ 
Let 
$$
\calD_b=\calD[(2 \pi i)^{-1},b^{\pm 1},e_2,e_4,e_6,\dots], \qquad
\ti \calD_b=\ti\calD[(2 \pi i)^{-1},b^{\pm 1},e_2,e_4,e_6,\dots] \,,
$$
where $e_l=e_l(\tq)=
\ti\d_l(1) \in \BZ[[\tq]]$.
Consider the following {\em operator valued polynomial}:

\begin{equation}
\lbl{eq.PAB}
P_{A,B} = \Res_{w=0}  \left( e^{\frac{1}{4 \pi i} w^2 + A w(b(\d + \frac{1}{2})+
b^{-1}(\ti\d + \frac{1}{2}))} \right)^A
\left(\frac{\phi(b w,\d_\bullet) \ti\phi(b^{-1} w,\ti\d_\bullet)}{b(1-e^{b^{-1}w})} \right)^B \in
\calD_b \otimes \ti \calD_b \,,
\end{equation}
where
\begin{subequations}
\begin{align}
\lbl{eq.phid}
\phi(w,\d_\bullet) 
& = \exp\left(-\sum_{l=1}^\infty \frac{\d_l}{l!} w^l
\right)
\\ 
\lbl{eq.phitd}
\ti \phi(w,\ti \d_\bullet) 
& = \exp(-\ti\d w) \exp\left(2 \sum_{l=\text{even}>0} 
e_l(\tq) \frac{w^l}{l!}\right)
\exp\left(-\sum_{l=1}^\infty \frac{\ti \d_l}{l!} (-w)^l
\right) \,.
\end{align}
\end{subequations}
For a series $F(x,\ti x)$, we define:
\begin{equation}
\lbl{eq.CT}
\la F(x, \ti x) \ra = F(1,1) \,.
\end{equation} 


\begin{theorem}
\lbl{thm.1}
We have:
\begin{equation}
\lbl{eq.thm1}
\calI_{A,B}(b) = \left(\frac{\tq}{q}\right)^{\frac{B-3A}{24}} 
e^{\pi i \frac{B+2(A+1)}{4}}
\Big\la P_{A,B}  \left( F_{A,B}(q,x) \ti F_{A,B}(\tq,\ti x) \right) \Big\ra \,.
\end{equation}
\end{theorem}


\begin{corollary}
\lbl{cor.1}
Writing $P_{A,B}=\sum_k p_k P_k$ (a finite sum), for
$p_k \in \calD_b$ and $P_k \in \ti \calD_b $, it follows that
\begin{equation}
\lbl{eq.cor1}
\calI_{A,B}(b) = \left(\frac{\tq}{q}\right)^{\frac{B-3A}{24}} 
e^{\pi i \frac{B+2(A+1)}{4}} \sum_k g_k(q) G_k(\tq)
\end{equation}
where
\begin{equation}
\lbl{eq.gp}
g_k(q) = \la p_k F_{A,B} \ra,
\qquad
G_k(\tq) = \la P_k \ti F_{A,B} \ra \,.
\end{equation}
\end{corollary}

\begin{remark}
\lbl{rem.1}
The left hand side of Equation \eqref{eq.cor1} has analytic continuation 
to the cut plane $\BC\setminus\{b^2 \, | \, b^2 <0\}$ whereas each of 
the series $g_k$ and $G_k$ is only well-defined in the upper-half plane 
$\{b^2 \, | \Im(b^2) >0 \}$.
\end{remark}

\begin{remark}
\lbl{rem.degPAB}
$P_{A,B}$, as a polynomial in the variables $e_2,e_4,\dots$ has degree
$B-1$, where the degree of $e_l$ is $l$. $P_{A,B}$ as a Laurent polynomial
in $b$ has $b$-monomials of degrees in $\{-B+1,-B+3,\dots,B-3,B-1\}$.
\end{remark}
