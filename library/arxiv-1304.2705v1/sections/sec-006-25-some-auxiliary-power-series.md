---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-006-25-some-auxiliary-power-series
section_title: "Some auxiliary power series"
section_number: 2.5
pages: 10-13
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
text_source: latex
latex_prose_ratio: 0.602
latex_coverage_ratio: 0.817
---
\lbl{sub.aux}

Consider the auxiliary series 

\begin{equation}
\lbl{eq.ax}
\frac{1}{a e^x-1}=\sum_{n=0}^\infty p_n(a) x^n
\end{equation}
where 
$$
p_n(a)=- \frac{a}{n! (1-a)^{n+1}} \sum_{m=0}^{n-1} A_{n,m} a^m
\qquad p_0(a)=-\frac{1}{1-a}
$$
and $A_{n,m}$ are {\em Euler triangular numbers} (sequence
{\tt A008292} in the online encyclopedia of integer sequences
\cite{OEIS}) that satisfy the recursion
$$
A_{n,m}=(n-m)A_{n-1,m-1}+(m+1)A_{n-1,m}
$$
and also given by the sum
$$
A_{n,m}=\sum_{k=0}^m (-1)^k \binom{n+1}{k} (m+1-k)^n \,.
$$
For a detailed discussion on this subject, see \cite{FS}.
A table of the first few numbers $A_{n,m}$ is given by

\begin{center}
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|} \hline
{$n\setminus m$} & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8  \\ \hline
1 &	1 &        &       &	&  & & & & \\ \hline
2 &	1 &	1  & & & & & & & \\ \hline
3 &	1 &	4  &	1 & & & & & & \\ \hline
4 &	1 &	11 &	11 &	1 & & & & & \\ \hline
5 &	1 &	26 &	66 &	26 &	1 & & & & \\ \hline
6 &	1 &	57 &	302 &	302 &	57 &	1 & & & \\ \hline
7 &	1 &	120 &	1191 &	2416 &	1191 & 	120 &	1 & & \\ \hline		
8 &	1 &	247 &	4293 &	15619 &	15619 &	4293 &	247 &	1 & \\ 
\hline		
9 &	1 &	502 &	14608 &	88234 &	156190 &88234 &	14608 &	502 & 1
\\ \hline
\end{tabular}
\end{center}

\begin{lemma}
\lbl{lem.E1}
For $l \geq 1$, we have:
\begin{equation}
\lbl{eq.qb}
\frac{d^l}{dx^l}\log(1-q^k e^{bx})|_{x=0}=b^l p_{l-1}(q^k) + b \, \delta_{l,1}
\end{equation}
\end{lemma}

\begin{proof}
It follows from
$$
\frac{d}{dx}\log(1-q^k e^{bx})=b\left(1+\frac{1}{q^ke^{bx}-1}\right)
$$
and Equation \eqref{eq.ax}.
\end{proof}

For positive natural numbers $l$, $r$ with $l \geq r$ and $m$ consider the 
$q$-series $E^{(m)}_{l,r}(q)$ defined by
\begin{align}
\lbl{eq.Elrm}
E_{l,r}^{(m)}(q)&=\sum_{k=m+1}^\infty \frac{q^{k r}}{(1-q^k)^l}
\end{align}

\begin{lemma}
\lbl{lem.E2}
\rm{(a)} We have
\begin{equation}
\lbl{eq.Ea}
E_{l,r}^{(m)}(q)= \sum_{s=r}^\infty a_{l,s} \frac{q^{s(m+1)}}{1-q^s}
\end{equation}
where
$$
\frac{x^r}{(1-x)^l} = \sum_{s=r}^\infty a_{l,s} x^s 
$$
\rm{(b)} It follows that
\begin{equation}
\lbl{eq.Eb}
\sum_{r=0}^{l-1} A_{l-1,r} E^{(m)}_{l,r+1}(q) = E^{(m)}_l(q)
\end{equation}
\end{lemma}

\begin{proof}
For (a), interchange $k$ and $s$ summation:
$$
E^{(m)}_{l,r}(q) = \sum_{k=m+1}^\infty \sum_{s=r}^\infty a_{l,s} q^{sk} =
\sum_{s=r}^\infty  \sum_{k=m+1}^\infty a_{l,s} q^{sk} =
\sum_{s=r}^\infty q^{(m+1)s} \sum_{k=0}^\infty a_{l,s} q^{sk} = 
\sum_{s=r}^\infty a_{l,s} \frac{q^{(m+1)s}}{1-q^s}
$$
(b) follows from (a) and the fact that
$$
\frac{\sum_{r=0}^{l-1} A_{l-1,r} x^r}{(1-x)^l}=
\sum_{s=1}^\infty s^{l-1} x^s \,.
$$
\end{proof}

\begin{lemma}
\lbl{lem.E3}
We have:
\begin{align}
\lbl{eq.minfinity2}
\phi_m(x) 
&= \exp\left(
-\sum_{l=1}^\infty \frac{1}{l!} \sum_{r=0}^{l-1} A_{l-1,r} E^{(m)}_{l,r+1}(q) x^l
\right) 
\end{align}
\end{lemma}

\begin{proof}
It follows from Lemma \ref{lem.E1} combined with 
$$
\log (\phi_m(x))= \log\left(
\frac{(q^{m+1} e^{x};q)_\infty}{(q^{m+1};q)_\infty} \right)
= \sum_{l=m+1}^\infty \left( \log(1-q^l e^{x}) -\log(1-q^l) \right)
$$
\end{proof}


\subsection{Proof of Proposition \ref{prop.phiexp}}
\lbl{sub.prop.phiexp}

Part (a) of Proposition \ref{prop.phiexp} follows from Lemma \ref{lem.E2}
and Lemma \ref{lem.E3}. For part (b), we will use the series
$$
E_l^{[m]}(q) =\sum_{s=1}^\infty \frac{s^{k-1} q^{s(m+1)}}{1-q^s} 
$$
Using 
\begin{align*}
\log ( \ti \phi_n(x)) &= 
\log\left( \frac{(\tq;\tq)_\infty}{(\tq e^{x};\tq)_\infty}\right)+
\log\left(
\frac{(\tq^{-1};\tq^{-1})_n}{(\tq^{-1} e^{x};\tq^{-1})_n} \right)  
\end{align*}
and the proof of part (a) of Proposition \ref{prop.phiexp}, it follows that
\begin{align*}
\log ( \ti \phi_n(x)) &= 
\log\left( \frac{(\tq;\tq)_\infty}{(\tq e^{x};\tq)_\infty}\right)+
\log\left(
\frac{(\tq^{-1};\tq^{-1})_n}{(\tq^{-1} e^{x};\tq^{-1})_n} \right) \\
& = 
\sum_{l=1}^\infty \frac{1}{l!} \sum_{r=0}^{l-1} A_{l-1,r} E^{(0)}_{l,r+1}(\tq) x^l 
+
\sum_{l=1}^\infty \frac{1}{l!} \sum_{r=0}^{l-1} A_{l-1,r} E^{[n]}_{l,r+1}(\tq^{-1}) x^l 
\\
& = \sum_{l=1}^\infty \frac{1}{l!} \sum_{r=0}^{l-1} A_{l-1,r} 
\left(E^{(0)}_{l,r+1}(\tq) + E^{[n]}_{l,r+1}(\tq^{-1}) \right) x^l
\end{align*}
where
\begin{equation}
\lbl{eq.E[n]}
E_{l,r}^{[n]}(q)=\sum_{k=1}^n \frac{q^{k r}}{(1-q^k)^l} \,.
\end{equation}
Let
\begin{equation}
\lbl{eq.tiE}
\ti E^{(n)}_{l,r}(\tq) =  
\begin{cases}
-n + E^{(n)}_{1,1}(\tq) & \text{if $l=r=1$} \\
E^{(n)}_{l,r}(\tq)   & \text{if $l>1$ is odd} \\
2 E^{(0)}_{l,r}(\tq) - E^{(n)}_{l,r}(\tq) & \text{if $l>1$ is even} 
\end{cases}
\end{equation}
We claim that 
\begin{equation}
\lbl{eq.lemE1}
E^{(0)}_{l,r}(\tq) + E^{[n]}_{l,l-r}(\tq^{-1}) =\ti E^{(n)}_{l,r}(\tq)
\end{equation}
for $l>r \geq 1$ and
\begin{equation}
\lbl{eq.lemE2}
E^{(0)}_{1,1}(\tq) + E^{[n]}_{1,1}(\tq^{-1})=\ti E^{(n)}_{1,1}(\tq)
\end{equation}
Assuming Equations \eqref{eq.lemE1} and \eqref{eq.lemE2}, it follows
that
\begin{align*}
\log ( \ti \phi_n(x)) &= 
\sum_{l=1}^\infty \frac{1}{l!} \sum_{r=0}^{l-1} A_{l-1,r} 
\ti E^{(n)}_{l,r+1}(\tq) x^l \\
&= \sum_{l=1}^\infty \frac{1}{l!} \ti E^{(n)}_l(\tq) x^l
\end{align*}
where the last step follows from part (b) of Lemma \ref{lem.E2}.

It remains to prove Equations \eqref{eq.lemE1} and \eqref{eq.lemE2}.
Equation \eqref{eq.lemE1} follows from the definition of $\ti E^{(n)}_{1,1}(\tq)$
and 
\begin{align*}
E^{(0)}_{l,r}(\tq) + E^{[n]}_{l,l-r}(\tq^{-1}) &=
\sum_{k=1}^\infty \frac{\tq^{kr}}{(1-\tq^k)^l} +
\sum_{k=1}^n \frac{\tq^{-k(l-r)}}{(1-\tq^{-k})^l}
\\ &
= \sum_{k=1}^\infty \frac{\tq^{kr}}{(1-\tq^k)^l} + (-1)^l
\sum_{k=1}^n  \frac{\tq^{kr}}{(1-\tq^k)^l}
\\ &
= (1+(-1)^l) \sum_{k=1}^n  \frac{\tq^{kr}}{(1-\tq^k)^l} +
\sum_{k=n+1}^\infty \frac{\tq^{kr}}{(1-\tq^k)^l}
\end{align*}
Equation \eqref{eq.lemE2} follows from
\begin{align*}
E^{(0)}_{1,1}(\tq) + E^{[n]}_{1,1}(\tq^{-1}) &= \sum_{k=1}^\infty 
\frac{\tq^k}{1-\tq^k} + \sum_{k=1}^n \frac{\tq^{-k}}{1-\tq^{-k}} \\
&=
\sum_{k=1}^\infty 
\frac{1-1+\tq^k}{1-\tq^k} -\sum_{k=1}^n \frac{1}{1-\tq^k}
= -n + \sum_{k=n+1}^\infty 
\frac{\tq^k}{1-\tq^k}
\end{align*}
This completes the proof of Proposition \ref{prop.phiexp}.
\qed


\subsection{Proof of Lemma \ref{lem.thm2}}
\lbl{sub.lem2}

Part (a) of Lemma \ref{lem.thm2} follows from the definition of $F_{A,B}$
and $\ti F_{A,B}$.

Part (b) follows from an application of Zeilberger's creative telescoping 
\cite{Z91}. To apply the method, define
$$
t(m,x)=\frac{(-1)^{A m} q^{A \frac{m(m+1)}{2}}}{(q)^B_m} x^m
$$
Then, observe that $t$ satisfies the recursions with respect to $m$
and $x$:
$$
(1-q^{m+1})^B t(m+1,x)= (-1)^A q^{A(m+1)} t(m,x) \qquad t(m,qx)=q^m t(m,x) \,.
$$
Now, we eliminate $q^m$ from the above equations as follows. The second
equation implies that $t(m+1,q^j x)=q^{j(m+1)} t(m+1,x)$. Expanding the
first equation, it follows that
$$
\sum_{j=0}^B (-1)^j \binom{B}{j} t(m+1,q^jx)=(-1)^A q^A x t(m,q^A x)
$$ 
Summing for $m \geq 0$ implies (b).
\qed

\begin{proof}(of Corollary \ref{cor.omega})
The admissibility of $F$ in the sense of Kontsevich-Soibelman,
follows from \cite[Sec.6.1]{KS} and \cite[Thm.9]{KS}. Given this,
the Nahm Equation \eqref{eq.FABnahm} for $\omega$ follows easily from 
part (b) of Lemma \ref{lem.thm2}.
\end{proof}
