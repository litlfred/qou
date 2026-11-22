---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-024-42-a-rank-one-admissible-series
section_title: "A rank one admissible series"
section_number: 4.2
pages: 48-51
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.856
latex_coverage_ratio: 0.939
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.F3}

$q$-hypergeometric series give admissible series that are easy to analyse. We
illustrate this with the example of the $1 \times 1$ matrix $A=(3)$ in~\eqref{FAdef}

\be
\label{Fexdef}
F(t,q) \= \sum_{k=0}^\infty \frac{(-1)^k q^{3 k(k+1)/2}}{(q;q)_k} t^k
\inn \BQ(q)[\![t]\!] \,.
\ee



It satisfies the linear $q$-difference equation 

\be
\label{Frec}
F(t,q) - F(q t,q) + q^3 t F(q^3 t,q) \= 0 \,.
\ee

The DT invariant of~\eqref{logF} $c_{n,i}$ is non-zero only for
$3n+1 \leq i \leq n^2+n+1$ (and exceptionally, for $c_{1,3}=1$) and satisfy the
positivity $c_{n,i} \in \BN$. The first few values of $c_{n,i}$ are given by

\be
\label{DTvalues}
\begin{array}{|r|c|} \hline
  n &  c_{n,i}, \,\, i=3n+1,\dots,n^2+n+1 \\ \hline

  2 & 1 \\ 
  3 & 1, 1, 0, 1 \\ 
  4 & 1, 1, 2, 1, 2, 1, 1, 0, 1 \\ 
  5 & 1, 2, 3, 4, 4, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 1 \\ 
  6 & 1, 2, 5, 7, 11, 11, 15, 13, 15, 13, 14, 10, 12, 8, 8, 6, 6, 3, 4, 2, 
2, 1, 1, 0, 1 \\ \hline
\end{array}
\ee
Despite appearances in low degrees, the DT invariants grow fast exponentially.
For example,
\be
c_{20,142} \= 44549701024 \,. 
\ee
The WKB expansion (see e.g.,~\cite{Bender}) of the solution $F(t,q)$
of~\eqref{Frec} allows one to compute the leading asymptotics of $\Phitof_1(t,x)$
in terms of the power series $z(t)$ and $V(t)$ defined by
\be
\label{z3}
1 - z  \= - t z^3, \qquad z(0)\=1\,,
\ee
where
\be
\label{zfew3}
z(t) \= 1 + t + 3 t^2 + 12 t^3 + 55 t^4 + 273 t^5 + 1428 t^6 + 7752 t^7 + 
 43263 t^8 + 246675 t^9 + O(t^{10}) 
\ee
and
\be
\label{V3}
\begin{aligned}
V(t) \= & -\Li_2(1-z(t)) -\frac{3}{2} (\log(z(t)))^2
\\
\= & t + \frac{5}{4} t^2 + \frac{28}{9} t^3 + \frac{165}{16} t^4 + \frac{1001}{25} t^5
+ \frac{1547}{9} t^6 + \frac{38760}{49} t^7 + \frac{245157}{64} t^8
+ O(t^9) \,. 
\end{aligned}
\ee



Using the auxiliary function 
\be
\label{delta3}
\begin{aligned}
\delta(t) & \=  -2t-\frac{t}{1-z(t)} \\
& \=1 - 5 t - 3 t^2 - 10 t^3 - 42 t^4 - 198 t^5 - 1001 t^6
- 5304 t^7 - 29070 t^8 + \dots 
\inn \BZ[\![t]\!]
\end{aligned}
\ee
and setting $q=1+x$ and abbreviating $V(t)$, $\delta(t)$ and $z(t)$ by $V$, $\delta$
and $z$, respectively, we obtain the first few coefficients of $\Phitof_1(t,x)$ as
follows:
\be
\label{Phi1tx3}
\begin{aligned}
&\widehat{\Phitof}_1(t,x) \= e^{\tfrac{V}{x}} \frac{1}{\sqrt{\delta}} \Big(1 +
\frac{1}{24 \delta^3}
((308 t^3 - 74 t^2) z^2 + (234 t^3 - 74 t^2) z + (216 t^3 - 382 t^2 + 74 t)) x
\\
&
+\frac{1}{1152\delta^6}(
(748116 t^6 - 893688 t^5 + 281084 t^4 - 19924 t^3 - 1104 t^2) z^2
\\ &  + (397872 t^6 - 685624 t^5 + 257848 t^4 - 21028 t^3 - 1104 t^2) z
\\ &  + (186624 t^6 - 1252224 t^5 + 1127196 t^4 - 303216 t^3 + 18820 t^2 + 1104 t))
  x^2 + O(x^3) \Big) \,.
\end{aligned}
\ee
In general, the coefficient of $x^k$ in $\Phitof_1(t,x) e^{-\tfrac{V(t)}{x}}
\delta^{\frac{1}{2} + 3k}$ is in $\BQ[t,z]$, where $z$ satisfies~\eqref{z3}.

Recall the symmetrisation $G(t,q)$ and $F^\sym(t,q)$ from equation~\eqref{GSdef}.
equation~\eqref{Frec} implies that $G$ satisfies a non-linear (Ricatti type)
$q$-difference equation 

\be
\label{Grec}
1-G(t,q) +q^3 t \, G(t,q) \, G(q t,q) \, G(q^2 t,q)  \= 0 \,.
\ee
It follows from this that the limit $\lim_{q \to 1} G(tq,q) = z(t)$ exists and
satisfies the algebraic equation~\eqref{z3}. Equation~\eqref{GS2} gives
the factorisation
\be
\label{gexp}
z(t) \= \prod_{n \geq 1} 
(1-t^n)^{-n \sum_{i \in \BZ} \, c_{n,i}}
\ee
which proves that the exponent of $1-t^n$ in the above product expansion
is divisible by $n$. 
This is an application of~\cite{KS:cohomological}, where one may think of the
polynomials $L_n(q)$ as a categorification of the integers $n \, c_{n,i}$. 

The symmetrised series $F^\sym(t,q)$ was not considered previously in
the literature. It is easy to show that it satisfies a sixth order linear
$q$-difference equation, which we omit.


Below, we will treat the series $G(t,q)$ and $F^\sym(t,q)$ on the same footing.

We now illustrate a remarkable aspect of the series $G(t,q)$ and $F^\sym(t,q)$,
namely their $(q-1)$-expansion. It is clear that they both lie in the
completed ring $\BZ[\![t]\!][\![q-1]\!]$ but more is true. The
expansion~\eqref{Phi1tx3} contains a volume prefactor that cancels, as well
as universal denominators for each power of $x$, which also cancel, so that what
remains are series in $\BZ[t^{\pm 1},z,1/\delta]$. Explicitly, we can write $G(t,q)$ 
\be
\label{Gexp}
G(t,1+x) \= \sum_{k \geq 0} g_k(t) x^k
\ee
and then it follows from~\eqref{Grec} and induction that $g_0=z$ and 
$\delta^{3k} g_k \in \BZ[t^{\pm 1}, z]$, e.g., 



\be
\label{gvals3}
\begin{aligned}
g_0 \= & z\,,
\\
\delta^3 g_1 \= & (15 t^3 - 3 t^2) z^2 + (18 t^3 - 3 t^2) z + (-18 t^2 + 3 t)\,,
\\
\delta^6 g_2 \= & (711 t^6 - 708 t^5 + 107 t^4 + 17 t^3 - 3 t^2) z^2
+ (405 t^6 - 586 t^5 + 115 t^4 + 14 t^3 - 3 t^2) z
\\ & + (-1176 t^5 + 828 t^4 - 96 t^3 - 20 t^2 + 3 t)\,,
\\
\delta^{9} g_3 \= &
(26325 t^9 - 69399 t^8 + 32035 t^7 + 6234 t^6 - 6470 t^5 + 1259 t^4 - 69 t^3 - t^2) z^2
\\ &
+ (9720 t^9 - 47322 t^8 + 29899 t^7 + 2658 t^6 - 5430 t^5 + 1187 t^4 - 70 t^3 - t^2) z
\\ &
+ (-56187 t^8 + 95787 t^7 - 32141 t^6 - 10699 t^5 + 7584 t^4 - 1330 t^3 + 68 t^2 + t)
\,.


\end{aligned}
\ee

\noindent
Likewise, we have
\be
\label{Fsymexp}
F^\sym(t,1+x) \= \sum_{k \geq 0} f^\sym_k(t) x^k\,,
\ee
where $\delta^{3k+1} f^\sym_k \in \BZ[t^{\pm 1}, z]$, with the first few
values given by 

\be
\label{fsymvals3}
\begin{aligned}
\delta f^\sym_0 \= & 1\,,
\\
\delta^4 f^\sym_1 \= & 0\,,
\\
\delta^7 f^\sym_2 \= &
(39 t^6 - 109 t^5 - 18 t^4 + 34 t^3 - 5 t^2) z^2
+ (9 t^6 - 85 t^5 + t^4 + 29 t^3 - 5 t^2) z
\\ & + (-96 t^5 + 124 t^4 + 42 t^3 - 39 t^2 + 5 t)\,,
\\
\delta^{10} f^\sym_3 \= &
(1296 t^9 - 9183 t^8 + 7230 t^7 + 1604 t^6 - 2730 t^5 + 858 t^4 - 109 t^3 + 5 t^2) z^2
\\ &
+ (243 t^9 - 5328 t^8 + 6310 t^7 + 415 t^6 - 2139 t^5 + 764 t^4 - 104 t^3 + 5 t^2) z
\\ &
+ (-3969 t^8 + 14304 t^7 - 7635 t^6 - 3231 t^5 + 3405 t^4 - 957 t^3 + 114 t^2 - 5 t)
\,.






\end{aligned}
\ee

But a further surprise is awaiting us when we expand $G(t,q)$ and $F^\sym(t,q)$
at $q=\z_m+x$. As expected, we now get series in
$\BZ[\z_m][t^{\pm 1},z,1/\delta][\![x]\!]$. But these series glue, after applying
$p$-Frobenius. Concretely, if we specialise $t=1$, then we obtain
\be\label{eq:ex.fsym.admis1}
F^\sym(1,1+x) \= \frac{1}{\delta} + (- 59 z^2 - 51 z + 36) \frac{x^2}{\delta^7} +
(- 1029 z^2 + 166 z + 2026) \frac{x^3}{\delta^{10}} + O(x^4) \,,
\ee
where $z$ satisfies the cubic equation $1-z+z^3=0$ and
$\delta=-2-1/(1-z)=-z^2-z-2$, an algebraic integer of norm $-23$. $z$ generates
a cubic field $F=\BQ(z)$ of discriminant $-23$. Let $R=\BZ[z,1/23]$.

The specialisation $F^\sym(1,q)\in \BZ[z,\frac{1}{23}][\![q-1]\!]$ and
$G(1,q)$ lie in $\calH_{\BZ[z,1/23]}$ and its field of fractions, respectively.
This illustrates part (a) of Corollary~\ref{cor.3} of Section~\ref{sub.results}.

These are elements of the Habiro ring of the \'etale map
\be
\label{Hetale}
\BZ[t^{\pm 1},1/\delta] \to \BZ[t^{\pm 1},1/\delta][z]/(1-z + t z^3) \,.
\ee

When $m=1$ and $A$ is a $1 \times 1$ matrix, the power series $z(t)=z_A(t)$,
$V(t)=V_A(t)$ and $\delta(t)=\delta_A(t)$ have coefficients polynomials in $A$.
Indeed, the unique power series $z(t)=z_A(t)$ 
\be
\label{gAdef}
1-z\=(-1)^A t z^A, \qquad z(0)\=1 \,.
\ee
has coefficients integer-valued polynomials of $A$ (for integer $A$), with the
first few given by
\be
\label{fewgt}
z(t) \= 1- (-1)^{A} t + A t^2 - \frac{1}{2}(-1)^{A} A(3A-1) t^3 + O(t^4) \,.

\ee
This, together with 
\begin{align*}
z(t) & \= \lim_{q \to 1} \frac{F(tq,q)}{F(t,q)} \= \lim_{q \to 1}
\exp\Big(-\sum_{n, \ell \geq 1} \sum_{i \in \BZ} \frac{L_n(q^\ell)}{\ell(1-q^\ell)}
(q^{\ell n}-1) t^{\ell n} \Big)
\\
& \= \exp\big( \sum_{n \geq 1} n L_n(1) \Li_1(t^n) \big)
\= \exp\big( t \partial_t \sum_{n \geq 1} L_n(1) \Li_2(t^n) \big)
\= \exp\big( t \partial_t V(t) \big)\,,
\end{align*}
implies that $V(t)$ satisfies 
\be 
\label{g2V}
\begin{aligned}
V(t) 
& \= -\Li_2(1-z(t)) - \frac{A}{2} (\log(z(t)))^2 \inn \BQ[\![t]\!],
\qquad V(0)\=0 \\
& \= -(-1)^A t -\frac{2A-1}{4} t^2 + (-1)^A \frac{(3A-1)(3A-2)}{18} t^3
+ O(t^4) \,.
\end{aligned}
\ee
Finally,
\be
\label{deltadef}
\begin{aligned}
\delta(t) & \= (-1)^A \Big( (A-1)t + \frac{t}{1-z(t)} \Big) \inn \BZ[\![t]\!],
\qquad \delta(0)\=1 \\
& \=
1 - (-1)^A (2A-1) t + \frac{A(A-1)}{2} t^2 + (-1)^A \frac{(2A-1)A(A-1)}{3} t^3
+ O(t^4) \,.
\end{aligned}
\ee






The rest of the coefficients of the unique zero-slope solution $F_A(t,q)$
of~\eqref{FArec} can be computed inductively as was illustrated in the beginning
of this section with the example of~$A=3$.
