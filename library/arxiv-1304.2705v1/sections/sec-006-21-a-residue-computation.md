---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-006-21-a-residue-computation
section_title: "A residue computation"
section_number: 2.1
pages: 6-8
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 0.889
---
\lbl{sub.residue}

To relate the state-integral $\calI_{A,B}$ to a sum, we will apply the
residue theorem on a semicircle $\gamma_R$ with center $0$ and radius $R$,
oriented counterclockwise in the upper half-plane:
$$
\psdraw{gammaR}{1in}
$$
Then, we will take the limit $R \to \infty$. To compute the residue
of the integrand, we need to expand $\Phi_b(x)$ near the pole 
$$
x_{m,n}=c_b + i b m + i b^{-1} n
$$ for natural numbers $m$ and $n$. Let
\begin{align}
\lbl{eq.phi}
\phi_m(x) &= \frac{(q^{m+1} e^{x};q)_\infty}{(q^{m+1};q)_\infty}
\\
\lbl{eq.tphi}
\ti \phi_n(x) &=\frac{(\tq;\tq)_\infty}{(\tq e^{x};\tq)_\infty}
\frac{(\tq^{-1};\tq^{-1})_n}{(\tq^{-1} e^{x};\tq^{-1})_n} 
\end{align}

\begin{lemma}
\lbl{lem.expandPhi}
We have:
\begin{equation}
\lbl{eq.expandPhi}
\Phi_b(x+x_{m,n}) = \frac{(q;q)_\infty}{(\tq;\tq)_\infty}
\frac{1}{(q;q)_m}
\frac{1}{(\tq^{-1};\tq^{-1})_n} \frac{\phi_m(2 \pi b x)
\, \ti \phi_n(2 \pi b^{-1} x)}{1-e^{2 \pi b^{-1}x}} \,. 
\end{equation}
\end{lemma}

\begin{proof}
Equation~\eqref{fad} implies the functional equations
\begin{align*}
\frac{\Phi_b(x+c_b+ib)}{\Phi_b(x+c_b)} &= \frac{1}{1-q e^{2 \pi b x}} 

\\
\frac{\Phi_b(x+c_b+ib^{-1})}{\Phi_b(x+c_b)} &= 
\frac{1}{1-\tq^{-1} e^{2 \pi b^{-1} x}} 

\end{align*}
which give 
\begin{align*}
\Phi_b(x+ x_{m,n})&=\Phi_b(x+c_b) 
\frac{1}{(q e^{2 \pi b x};q)_m}
\frac{1}{(\tq^{-1} e^{2 \pi b^{-1} x};\tq^{-1})_n} \\
\Phi_b(x+c_b)&=\frac{1}{1-e^{2 \pi b^{-1}x}} 
\frac{(q e^{2 \pi b x};q)_\infty}{(\tq e^{2 \pi b^{-1} x};\tq)_\infty} \,.
\end{align*}
Thus,
\begin{align*}
\Phi_b(x+x_{m,n})&=
\frac{(q;q)_\infty}{(\tq;\tq)_\infty}
\frac{1}{(q;q)_m}
\frac{1}{(\tq^{-1};\tq^{-1})_n} \cdot \\
& \frac{1}{1-e^{2 \pi b^{-1}x}}
\frac{(q e^{2 \pi b x};q)_\infty}{(q;q)_\infty}
\frac{(\tq;\tq)_\infty}{(\tq e^{2 \pi b^{-1} x};\tq)_\infty}
\frac{(q;q)_m}{(q e^{2 \pi b x};q)_m}
\frac{(\tq^{-1};\tq^{-1})_n}{(\tq^{-1} e^{2 \pi b^{-1} x};\tq^{-1})_n} 
\\
&=
\frac{(q;q)_\infty}{(\tq;\tq)_\infty}
\frac{1}{(q;q)_m}
\frac{1}{(\tq^{-1};\tq^{-1})_n} \cdot \\
& \frac{1}{1-e^{2 \pi b^{-1}x}}
\frac{(q^{m+1} e^{2 \pi b x};q)_\infty}{(q^{m+1};q)_\infty}
\frac{(\tq;\tq)_\infty}{(\tq e^{2 \pi b^{-1} x};\tq)_\infty}
\frac{(\tq^{-1};\tq^{-1})_n}{(\tq^{-1} e^{2 \pi b^{-1} x};\tq^{-1})_n}
\end{align*}
The result follows.
\end{proof}
The decoupling of $(m,n)$ in the quadratic form comes as follows:
since $A,m,n$ are integers, $e^{A \pi i m n}=1$ and a computation gives
$$

e^{-A \pi i (x+ x_{n,m})^2}=
i^A \left(\frac{q}{\tq}\right)^{\frac{A}{8}} 
t^A_m(q) \, \ti t^A_n(\tq) e^{- A \pi i x^2 +2 A \pi x 
\left(b (m+\frac{1}{2}) + b^{-1} (n+\frac{1}{2})\right)}
$$
where
$$
t^A_m(q) = (-1)^{A m} q^{A \frac{m(m+1)}{2}}, \qquad
\ti t^A_n(\tq) = (-1)^{A n} \tq^{-A \frac{n(n+1)}{2}} \,.
$$
The Dedekind function $\eta(\tau)=q^{1/24}(q;q)_\infty$ (with $q=e^{2\pi i\tau}$)
satisfies the modular equation 
$\eta(-\tau^{-1})=\sqrt{-i\tau}\eta(\tau)$ \cite{Andrews}.
It follows that 
\begin{equation}
\lbl{eq.etaf}
\frac{(q;q)_\infty}{(\tq;\tq)_\infty}=e^{\frac{\pi i}{4}} 
\left(\frac{\tq}{q}\right)^{\frac{1}{24}} b^{-1} \,.
\end{equation}
After we set $w=x/(2\pi)$, the above discussion implies that
\begin{equation}
\lbl{eq.III}
\calI_{A,B}(b)=\left(\frac{\tq}{q}\right)^{\frac{B-3A}{24}} 
e^{\pi i \frac{B+2(A+1)}{4}} \sum_{m,n=0}^\infty  \left(\Res_{w=0} F_{A,B,m,n}(w)\right)
 \frac{t^A_m(q)}{(q;q)_m^B}
\frac{\ti t^A_n(\tq)}{(\tq^{-1};\tq^{-1})_n^B} \,,
\end{equation}
where
\begin{equation}
\lbl{eq.FABmn}
F_{A,B,m,n}(w) =
e^{\frac{A}{4 \pi i} w^2 + A w \left(b( m+ \frac{1}{2}) 
+b^{-1}( n+ \frac{1}{2}) \right)} 
\left( \frac{ \phi_m(b w) \, \ti \phi_n(b^{-1} w) }{b(1-e^{b^{-1}w})}\right)^B 
\,.
\end{equation}


\subsection{The Taylor series of $\phi_m(x)$ and $\ti\phi_n(x)$}
\lbl{sub.identify}

In this section we express the Taylor series of $\phi_m(x)$ and $\ti\phi_n(x)$
in terms of the $q$-series $E^{(m)}_l(q)$ and $\ti E^{(m)}_l(\tq)$
defined by:
\begin{subequations}
\begin{align}
\lbl{eq.Elm}
E_l^{(m)}(q)&=\sum_{s=1}^\infty \frac{s^{l-1} q^{s(m+1)}}{1-q^s} =
\la \d_l(x^m) \ra
\\
\lbl{eq.Etlm}
\ti E_l^{(n)}(\tq)&=
\begin{cases}
-n + E_1^{(n)}(\tq) & \text{if $l=1$} \\
E_l^{(n)}(\tq)  & \text{if $l>1$ is odd} \\
2 E_l^{(0)}(\tq) -E_l^{(n)}(\tq) & \text{if $l>1$ is even} 
\end{cases}
\end{align}
\end{subequations}

\begin{proposition}
\lbl{prop.phiexp}
We have:
\begin{subequations}
\begin{align}
\lbl{eq.minfinity}
\phi_m(x) 
&= \exp\left(-\sum_{l=1}^\infty \frac{1}{l!} E^{(m)}_l(q) x^l
\right) 
\\
\lbl{eq.ninfinity}
\ti \phi_n(x) 
&= \exp\left(\sum_{l=1}^\infty \frac{1}{l!} \ti E^{(m)}_l(\tq) x^l
\right) \,.
\end{align}
\end{subequations}
\end{proposition}
The proof of this proposition is given in Section \ref{sub.prop.phiexp}.
The first few terms in Equations \eqref{eq.minfinity}-\eqref{eq.minfinity}
are given by:
{\tiny
\begin{subequations}
\begin{align}
\lbl{eq.minfinity.terms}
\phi_m(x) 
&= \exp\left(-E^{(m)}_1 x - \frac{1}{2} E^{(m)}_2 x^2 - \frac{1}{6} E^{(m)}_3 x^3 
- \frac{1}{24} E^{(m)}_4 x^4 -\dots \right) 
\\
\notag &= 1 - E^{(m)}_1 x + \frac{1}{2} (E^{(m)2}_1 - E^{(m)}_2) x^2 + 
\frac{1}{6} (-E^{(m)3}_1 + 3 E^{(m)}_1 E^{(m)}_2 - E^{(m)}_3) x^3 + \\ &
\frac{1}{24} (E^{(m)4}_1 - 6 E^{(m)2}_1 E^{(m)}_2 + 3 E^{(m)2}_2 + 
    4 E^{(m)}_1 E^{(m)}_3 - E^{(m)}_4 )x^4 +\dots
\\
\lbl{eq.ninfinity.terms}
\ti \phi_n(x) 
&= \exp\left( \ti E^{(n)}_1 x + \frac{1}{2} \ti E^{(n)}_2 x^2 
+ \frac{1}{6} \ti E^{(n)}_3 x^3 
+ \frac{1}{24} \ti E^{(n)}_4 x^4 -\dots \right) 
\\
\notag &= 1 + \ti E^{(n)}_1 x 
+ \frac{1}{2} (\ti E^{(n)2}_1 + \ti E^{(n)}_2) x^2 + 
\frac{1}{6} (\ti E^{(n)3}_1 + 3 \ti E^{(n)}_1 \ti E^{(n)}_2 + \ti E^{(n)}_3) 
x^3 + \\ &
\frac{1}{24} (\ti E^{(n)4}_1 + 6 \ti E^{(n)2}_1 \ti E^{(n)}_2 + 3 \ti E^{(n)2}_2 + 
    4 \ti E^{(n)}_1 \ti E^{(n)}_3 + \ti E^{(n)}_4 ) x^4 +\dots
\end{align}
\end{subequations}
}
where $E^{(m)}_l=E^{(m)}_l(q)$ and $\ti E^{(m)}_l=\ti E^{(m)}_l(\tq)$.
