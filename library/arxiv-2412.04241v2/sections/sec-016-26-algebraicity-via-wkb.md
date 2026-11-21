---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-016-26-algebraicity-via-wkb
section_title: "Algebraicity via WKB"
section_number: 2.6
pages: 33-35
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.885
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.WKB}

In this section we outline an independent proof of Lemma~\ref{lem.PhiA} of
Section~\ref{sub.FGI} using instead of formal Gaussian integration, the unique
solution to the system of
linear $q$-difference equations~\eqref{PhiAshift}. This is essentially the WKB
method~\cite{Bender} for linear $q$-difference equations~\cite{GG:qdiff}, which
writes the first derivative of a new function as a
differential polynomial of known functions. In general, integrating will produce
non-algebraic functions, but with some care one can overcome and solve this
vanishing residue problem. Calculations similar to those of this section were done in
unpublished work of Masha Vlasenko.

Rather than explain this method for the general case, we do so for the
case of $1 \times 1$ integer matrices $A$. Consider the power series $z=z(t)$ defined
by
\be
1-z\=tz^A
\ee
and
\be
X\=\frac{z-1}{(1-A)z+A}
\=
\begin{pmatrix}
1 & -1\\
1-A & A
\end{pmatrix}
\cdot
z\,,
\ee
so that 
\be\label{eq:XZrel}
z\=\frac{AX+1}{(A-1)X+1}
\=
\begin{pmatrix}
A & 1\\
A-1 & 1
\end{pmatrix}
\cdot
X \,.
\ee
Then notice that for $\Delta=X(AX+1)((A-1)X+1)$ we have
\be
t\frac{d}{dt} \= \Delta\frac{d}{dX} \,, \qquad
X \= \frac{t}{z}\frac{dz}{dt}\,.
\ee














This implies that
\be
\label{eq:logz}
\exp\Big(h t\frac{d}{dt}\Big)\log(z(t))-\log(z(t))-Xh \inn
X(AX+1)((A-1)X+1)\BQ[X][\![h]\!]\,.
\ee
Suppose that $F(t;q)\in\BQ(\!(h)\!)[\![t]\!]$ is the unique solution to the equation
\be
  F(t;h)-F(e^{h}t;h)\=tF(e^{Ah}t;h)\,,
\ee
and their exists $c_k(t)\in\BQ[\![t]\!]$ so that $F(t;h)$ satisfies the following
ansatz
\be
F(t;h) \= \exp\Big(\sum_{k=-1}^{\infty}c_k(t)h^{k}\Big)\,.
\ee
We will prove that such $c_k$ exist and that for $k>0$ they are algebraic functions.
In order to do this we consider the quotient
\be\label{eq:bkdef}
G(t;h) \= \frac{F(e^h t;h)}{F(t;h)}
\;=:\; z(t)\exp\Big(\sum_{k=1}^{\infty}b_k(t)h^k\Big)\,.
\ee
The functional equations of $F$ and $z$ imply that $G$ satisfies the equation
\be
\label{eq:funeqG}
\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}
\Big(\frac{z(t)-G(t;h)}{1-z(t)}\Big)^k
\= \log\Big(1+\frac{z(t)-G(t;h)}{1-z(t)}\Big)
\= \sum_{j=0}^{A-1}\log\Big(\frac{G(e^{jh}t;h)}{z(t)}\Big)\,.
\ee
This implies that
\be
\label{eq:b1}
-\frac{z(t)}{1-z(t)}b_{1}(t) \= Ab_{1}(t)+\frac{1}{2}A(A-1)X
\ee
and
\be\label{eq:b1andb2}
\frac{1}{2}\Big(\frac{z(t)}{1-z(t)}b_{1}(t)\Big)^2-\frac{z(t)}{1-z(t)}
\Big(b_{2}(t)+\frac{b_{1}(t)^2}{2}\Big)
\= Ab_{2}(t)+\sum_{j=0}^{A-1}\Big(jt\frac{d}{dt}\Big)\big(X(t)+b_1(t)\big)\,.
\ee
We have the following lemma.

\begin{lemma}
The coefficients $b_{k}(t)$ defined by equation~\eqref{eq:bkdef} exists and satisfy
the properties:
\be
b_{1}(t) \= \frac{A(A-1)}{2}X^2\,,
\quad\text{and for }k\in\BZ_{>1}\quad b_{k}(t)\inn X\Delta\BQ[X]\,.
\ee
\end{lemma}

\begin{proof}
Firstly, $b_{1}(t)$ can be explicitly computed using~\eqref{eq:XZrel}~and~\eqref{eq:b1}.
Next we notice that
\be
-\frac{zb_{1}(t)}{1-z} \= \frac{(A-1)A}{2}X(AX+1)\inn X\BQ[X]
\ee
and
\be
-\frac{zb_{1}(t)^2}{1-z} - \Big(-\frac{zb_{1}(t)}{1-z}\Big)^2
\= \frac{(A-1)^2A^2}{4}X^2(AX+1)((A-1)X+1) \inn X\Delta\BQ[X]\,.
\ee
By induction on $k$, we see that for $k\in\BZ_{>0}$ we have
\be
\label{eq:indb1}
-\frac{zb_{1}(t)^k}{1-z} - \Big(-\frac{zb_{1}(t)}{1-z}\Big)^k
\inn X\Delta\BQ[X]\,.
\ee

















Already this and equation~\eqref{eq:b1andb2} implies that
$b_{2}(t)\in X\Delta\BQ[X]$. By induction, suppose that for some $K>2$
we have that $b_{k}(t)\in X\Delta\BQ[X]$ for all $k<K$. Then we
see that
\be
\frac{1-G(t)}{1-z(t)}\quad\in\quad
\frac{1-z(t)\exp(b_{1}(t)h)}{1-z(t)} + \frac{-z(t)b_{K}(t)h^K}{1-z(t)}
+ h^2 X\Delta\BQ[X,h] + \mathrm{O}(h^{K+1})\,,
\ee
and therefore
\be
\begin{small}
\begin{aligned}
\log\Big(\frac{1-G(t)}{1-z(t)}\Big)
\inn \log\Big(\frac{1-z(t)\exp(b_{1}(t)h)}{1-z(t)}\Big)
- \frac{z(t)b_{K}(t)h^K}{1-z(t)} + h X\Delta\BQ[X,h]
+ \mathrm{O}(h^{K+1})\,.
\end{aligned}
\end{small}
\ee
From equation~\eqref{eq:indb1}, we see that
\be
\frac{1-z(t)\exp(b_{1}(t)h)}{1-z(t)} \inn
\exp\Big(\frac{-z(t)b_{1}(t)h}{1-z(t)}\Big)+h X\Delta\BQ[X,h]\,,
\ee
and so
\be
\log\Big(\frac{1-z(t)\exp(b_{1}(t)h)}{1-z(t)}\Big)
\inn \frac{-z(t)b_{1}(t)h}{1-z(t)} +h X\Delta\BQ[X,h]\,.
\ee
Together with the fact that $zX^2(1-z)^{-1}=-X-AX^2\in X\BZ[X]$
and the functional equation~\eqref{eq:funeqG} of $G$, this gives a relation
for $b_{K}(t)$ of the form
\be
\frac{-z(t)b_{K}(t)}{1-z(t)} -Ab_{K}(t) \= X^{-1}b_{K}(t) \inn \Delta\BQ[X]\,.
\ee
This completes the proof.
\end{proof}
This lemma can now be used to determine the properties of the coefficients of $F(t;h)$.

\begin{corollary}
The coefficients $c_{k}(t)$ in the function $F(t;h)$ exists and for $k\in\BZ_{>0}$
\be
c_{k}(t)\inn X\BQ[X]\,.
\ee
\end{corollary}

\begin{proof}
Notice that
\be
\frac{1}{\exp(h t\frac{d}{dt})-1}\log(G(t;h))
\= \sum_{k=0}^{\infty}\frac{B_k}{k!}(h t\frac{d}{dt})^{k-1}\log(G(t;h))
\= \log(F(t;h))\,.
\ee
Therefore, we see that to compute the coefficient $c_{k}(t)$ we need to integrate
$b_{k+1}(t)$ with the initial condition $c_{k}(0)=0$. We see that
\be
\int b_{k+1}(t)\frac{dt}{t} \= \int b_{k+1}(t)\frac{dX}{\Delta} \inn X\BQ[X]\,,
\ee
since $\Delta^{-1}b_{k+1}(t)\in X\BQ[X]$.
\end{proof}
