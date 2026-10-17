---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-007-23-the-connection-with-the-differential-operator
section_title: "The connection with the differential operators l and '0365l"
section_number: 2.3
pages: 8-10
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.848
latex_coverage_ratio: 0.757
---
In this section we connect the series $E^{(m)}_l(q)$ and $\ti E^{(m)}_l(\tq)$
with the action of the differential operators $\d_l$ and $\ti\d_l$ on
a series $F(x)$ and $\ti F(\ti x)$ respectively.
Consider formal power series 
$$
F(x)=\sum_{m=0}^\infty t(m) x^m \qquad 
\ti F(\ti x)=\sum_{m=0}^\infty \ti t(m) \ti x^m \,.
$$

\begin{lemma}
\lbl{lem.dconnect}
We have:
\begin{align}
\lbl{eq.daction}
\sum_{m=0}^\infty \left( \prod_{j=1}^r E^{(m)}_{l_j}(q) \right) t(m) &=
\la \prod_{j=1}^r \d_{l_j} F \ra \\
\lbl{eq.ddaction}
\sum_{m=0}^\infty m^r t(m) &= \la \d^r F \ra
\end{align}
and 
\begin{align}
\lbl{eq.tdaction}
\sum_{n=0}^\infty \left( \prod_{j=1}^r \ti E^{(n)}_{l_j}(\tq) \right) \ti t(n) &=
\la \prod_{j=1}^r \ti \d_{l_j} \ti F \ra \\
\lbl{eq.tddaction}
\sum_{n=0}^\infty n^r \ti t(n) &= \la \ti d^r \ti F \ra \,.
\end{align}
\end{lemma}

\begin{proof}
For a positive natural number $l$ we have:
\begin{align*}
\sum_{m=0}^\infty E^{(m)}_l(q) t(m) &=\sum_{m=0}^\infty \la \d_l(x^m) \ra t(m)
=\Big\la \d_l(\sum_{m=0}^\infty t(m) x^m) \Big\ra = \la \d_l F \ra \,.
\end{align*}
Moreover, for positive natural numbers $l,l'$ we have:
\begin{align*}
\sum_{m=0}^\infty E^{(m)}_l(q) E^{(m)}_{l'}(q)
t(m) &=\sum_{m=0}^\infty \la \d_l(x^m) \ra \la \d_{l'}(x^m) \ra t(m)
\\
& 
=\Big\la \d_l\left( \sum_{m=0}^\infty \la \d_{l'}(x^m) \ra t(m) x^m \right) 
\Big\ra \,.
\end{align*}
Now,
\begin{align*}
\la \d_{l'}(x^m) \ra t(m) x^m &=
\sum_{s=1}^\infty \frac{s^{l'-1} q^s}{1-q^s} q^{sm}  t(m) x^m=\d_{l'}(x^m)t(m)
\end{align*}
and summing up over $m$, we obtain that
$$
\sum_{m=0}^\infty \la \d_{l'}(x^m) \ra t(m) x^m  = \d_{l'} F(q,x) \,.
$$
It follows that
$$
\sum_{m=0}^\infty E^{(m)}_l(q) E^{(m)}_{l'}(q) t(m) = \la \d_l \d_{l'} F \ra \,.
$$
The general case of Equation \eqref{eq.daction} follows by induction on $r$.
Equation \eqref{eq.ddaction} is obvious. 
\end{proof}
