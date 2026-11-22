---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-005-24-multivariate-analogues-of-the-hko-and-hb-theo
section_title: "Multivariate analogues of the HKO and HB Theorems."
section_number: 2.4
pages: 6-8
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.938
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
By analogy with the univariate HB Theorem, polynomials
$f,g\in\RR[\x]$ are said to be in \emph{proper position}, denoted by
$f\ll g$, when $g+\i f\in\Stab[\x]$.  (As will be seen, this implies
that $f,g\in\StabR[\x]$.)  Thus, the multivariate analogue of
Hermite-Biehler is a \underline{definition}, not a theorem.

\begin{prop}[Lemma 1.8 and Remark 1.3 of \cite{BB5}]
Let $f,g\in\CC[\x]$.\\
\textup{(a)}\ If $f,g\in\RR[\x]$ then $f \ll g$
if and only if $g+yf\in\StabR[\x,y]$.\\
\textup{(b)}\ If $0\not\equiv f\in\Stab[\x]$ then
$g+yf\in\Stab[\x,y]$ if and only if for all $\z\in\HH^m$,
$$
\Im\left(\frac{g(\z)}{f(\z)}\right)\geq 0.
$$
\end{prop}
\begin{proof}
If $g+yf\in\StabR[\x,y]$ then $g+\i f\in\Stab[\x]$, by specialization.  
Conversely, assume that $h=g+\i f\in\Stab[\x]$ with $f,g\in\RR[\x]$,
and let $z=a+\i b$ with $a,b\in\RR$ and $b>0$.  By Lemma 2.3, for all
$\a,\b\in\RR^{m}$ with $\b>\zero$ we have $h(\a+\b t)\in\Stab[t]$.
By HB, $\fhat(t)=f(\a+\b t)$ and $\ghat(t)=g(\a+\b t)$ are
such that $\fhat\ll \ghat$.  By HKO, $c\fhat+d\ghat\in\StabR[t]$
for all $c,d\in\RR$.  By HKO again, the roots of
$b\fhat$ and of $\ghat+a\fhat$ are interlaced.  Since
$W[b\fhat,\ghat+a\fhat] = b W[\fhat,\ghat]\leq 0$ on $\RR$,
it follows that $b\fhat\ll \ghat+a\fhat$.  Finally, by HB again,
$\ghat + (a+\i b)\fhat\in\Stab[t]$.  Since this holds for all
$\a,\b\in\RR^{m}$ with $\b>\zero$, Lemma 2.3 implies that
$g+(a+\i b)f\in\Stab[\x]$.  Since this holds for all
$a,b\in\RR$ with $b>0$, $g+yf\in\Stab[\x,y]$.  This proves part (a).

For part (b), first let $g+yf$ be stable. By specialization, $g$ is also stable.
If $g\equiv 0$ then there is nothing
to prove.  Otherwise, consider any $\z\in\HH^{m}$, so that $f(\z)\neq 0$ and
$g(\z)\neq 0$.  There is a unique solution $z\in\CC$ to $g(\z)+zf(\z)=0$,
and since $g+yf$ is stable, $\Im(z)\leq 0$.  Hence,
$\Im(g(\z)/f(\z))=\Im(-z)\geq 0$.  This argument can be reversed to prove
the converse implication.
\end{proof}

\begin{exercise}[Corollary 2.4 of \cite{BB4}]
$\Stab[\x]=\{g + \i f:\ f,g\in \StabR[\x]\ \mathrm{and}\ f\ll g\}$.
\end{exercise}

Here is the multivariate HKO Theorem of Borcea and Br\"and\'en.

\begin{theorem}[Theorem 1.6 of \cite{BB4}]
Let $f,g\in\RR[\x]$.  Then $af+bg\in\StabR[\x]$ for all $a,b\in\RR$
if and only if $f,g\in\StabR[\x]$ and either $f\ll g$ or $g\ll f$.
\end{theorem}
\begin{proof}
First assume that $f\ll g$, and let $a,b\in\RR$ with $b>0$.
By Proposition 2.7(a), $g+yf\in\StabR[\x,y]$.  By scaling and specialization,
$bg+(a+\i)f \in\Stab[\x]$.  By Proposition 2.7(a) again, $f\ll (af+bg)$.  Thus
$af+bg\in\StabR[\x]$ for all $a,b\in\RR$.  The case that $g\ll f$ is 
similar.

Conversely, assume that $af+bg\in\StabR[\x]$ for all $a,b\in\RR$.
Let $\a,\b\in\RR^{m}$ with $\b>\zero$, and let $\fhat(t)=f(\a+\b t)$ and
$\ghat(t)=g(\a+\b t)$.  By Lemma 2.3, $a\fhat +b\ghat\in\StabR[t]$
for all $a,b\in\RR$.  By HKO, for each
$\a,\b\in\RR^{m}$ with $\b>\zero$, either $\fhat\ll \ghat$
or $\ghat\ll\fhat$.  

If $\fhat\ll \ghat$ for all $\a,\b\in\RR^{m}$ with $\b>\zero$, then
by HB, $\ghat + \i \fhat \in\Stab[t]$ for all
$\a,\b\in\RR^{m}$ with $\b>\zero$.  Thus $g + \i f\in\Stab[\x]$ by
Lemma 2.3, which is to say that $f\ll g$ (by definition).  Similarly, if
$\ghat\ll \fhat$ for all $\a,\b\in\RR^{m}$ with $\b>\zero$ then $g\ll 
f$.

It remains to consider the case that
$f(\a_{0}+\b_{0} t) \ll g(\a_{0}+\b_{0} t)$ for 
some $\a_{0},\b_{0}\in\RR^{m}$ with $\b_{0}>\zero$, and 
$g(\a_{1}+\b_{1} t) \ll f(\a_{1}+\b_{1} t)$ for 
another $\a_{1},\b_{1}\in\RR^{m}$ with $\b_{1}>\zero$.
For $0\leq\lambda\leq 1$, let
$\a_{\lambda} = (1-\lambda)\a_{0}+\lambda\a_{1}$ and 
$\b_{\lambda} = (1-\lambda)\b_{0}+\lambda\b_{1}$.
Since roots of polynomials move continuously as the coefficients 
are varied continuously, there is a value $0\leq \lambda\leq 1$ for 
which both $f(\a_{\lambda}+\b_{\lambda} t) \ll g(\a_{\lambda}+\b_{\lambda} t)$
and $g(\a_{\lambda}+\b_{\lambda} t) \ll f(\a_{\lambda}+\b_{\lambda} t)$.
From Exercise 2.6, it follows that
$cf(\a_{\lambda}+\b_{\lambda} t) = dg(\a_{\lambda}+\b_{\lambda} t)$
for some $c,d\in\RR$ not both zero.  Now $h=cf-dg\in\Stab[\x]$ by hypothesis,
and since $h(\a_{\lambda}+\b_{\lambda} t)\equiv 0$ identically, it follows 
that $h(\a_{\lambda}+\i\b_{\lambda})=0$.  Since $\b_{\lambda}>\zero$ 
and $h$ is stable, this implies that $h\equiv 0$, so that $cf=dg$ in $\Stab[\x]$.
In this case, both $f\ll g$ and $g\ll f$ hold.
\end{proof}

For $f,g\in\CC[\x]$ and $i\in[m]$, let
$\Wr_i[f,g] = \partial_i f \cdot g - f \cdot \partial_i g$
be the \emph{$i$-th Wronskian} of the pair $(f,g)$.
\begin{coro}[Theorem 1.9 of \cite{BB5}]
Let $f,g\in\RR[\x]$.  The following are equivalent:\\
\textup{(a)}\ $g+\i f$ is stable in $\Stab[\x]$, that is $f\ll g$;\\
\textup{(b)}\ $g+ y f$ is real stable in $\StabR[\x,y]$;\\
\textup{(c)}\ $af+bg\in\StabR[\x]$ for all $a,b\in\RR$, and
$\Wr_i[f,g](\a)\leq 0$ for all $i\in[m]$ and $\a\in\RR^m$.
\end{coro}
\begin{proof}
Proposition 2.7(a) shows that (a) and (b) are equivalent.

If (a) holds then Theorem 2.9 implies that $af+bg\in\StabR[\x]$ for all
$a,b\in\RR$.  To prove the rest of (c), let $i\in[m]$ and $\a\in\RR^m$,
and let $\delta_i\in\RR^m$ be the unit vector with a one in the $i$-th position.
Since $f\ll g$, for any $\b\in\RR^m$ with $\b>\zero$ we have
$f(\a+(\b+\delta_i)t) \ll g(\a+(\b+\delta_i)t)$ in $\StabR[t]$, from
Proposition 2.7(a) and Lemma 2.3.  By the Wronskian condition for univariate
polynomials in proper position,
$$
\Wr[f(\a+(\b+\delta_i)t),g(\a+(\b+\delta_i)t)]\leq 0
$$
for all $t\in\RR$.  Taking the limit as $\b\goesto\zero$ and evaluating
at $t=0$ yields
$$
\Wr_i[f,g](\a) = \Wr[f(\a+\delta_i t),g(\a+\delta_i t)]|_{t=0}\leq 0,
$$
by continuity.  Thus (a) implies (c).

To prove that (c) implies (b), let $\a,\b\in\RR^m$ with $\b=(b_1,...,b_m)>\zero$,
and let $a,b\in\RR$ with $b>0$.  By Lemma 2.3, to show that  $g+ y f
\in\StabR[\x,y]$ it suffices to show that
$g(\a+\b t) + (a+\i b) f(\a+\b t) \in\Stab[t]$.  From (c) it follows that
$p=g + a f $ and $q=bf$ are such that $\alpha p +\beta q \in \StabR[\x]$
for all $\alpha,\beta\in\RR$.  By Theorem 2.9, either $p\ll q $ or $q\ll p$.
Now
\showon
\Wr[q(\a+\b t),p(\a+\b t)]
&=&
b \Wr[f(\a+\b t),g(\a+\b t)] \\
&=&
b\sum_{i=1}^m b_i \Wr_i[f,g](\a+\b t) \leq 0,
\showoff
by the Wronskian condition in part (c).  Thus $q(\a+\b t)\ll p(\a +\b t)$,
so that $p(\a+\b t)+\i q(\a +\b t)\in\Stab[t]$.  Since $p+\i q = g + (a+\i b)
f$, this shows that (c) implies (b).
\end{proof}

\begin{exercise}[Corollary 1.10 of \cite{BB5}]
Let $f,g\in\StabR[\x]$ be real stable.  Then $f \ll g$ and $g\ll f$
if and only if $cf=dg$ for some $c,d\in\RR$ not both zero.
\end{exercise}

\begin{prop}[Lemma 3.2 of \cite{BB5}]
Let $V$ be a $\KK$-vector subspace of $\KK[\x]$, with either $\KK=\RR$
or $\KK=\CC$.\\
\textup{(a)}\ If $\KK=\RR$ and $V\subseteq\StabR[\x]$ then $\dim_\RR V \leq
2$.\\
\textup{(b)}\ If $\KK=\CC$ and $V\subseteq\Stab[\x]$ then $\dim_\CC V \leq 1$.
\end{prop}
\begin{proof}
For part (a), suppose to the contrary that $f,g,h\in V$ are linearly
independent over $\RR$ (and hence not identically zero).  By Theorem 2.9,
either $f\ll g$ or $g\ll f$, and similarly for the other pairs $\{f,h\}$ and
$\{g,h\}$.  Renaming these polynomials as necessary, we may assume that
$f\ll h$ and $h\ll g$.  Now, for all $\lambda\in[0,1]$ let $p_\lambda =
(1-\lambda)f+\lambda g$, and note that each $p_{\lambda}\not\equiv 0$.
By Theorem 2.9, for each $\lambda\in[0,1]$ either
$h\ll p_\lambda$ or $p_\lambda \ll h$.  Since $p_0=f\ll h$
and $h\ll g=p_1$, by continuity of the roots of $\{p_\lambda:\
\lambda\in[0,1]\}$ there is a $\lambda\in[0,1]$ such that $h\ll p_\lambda$
and $p_\lambda\ll h$.  But then, by Exercise 2.11, either $\{f,g\}$ is
linearly dependent or $h$ is in the span of $\{f,g\}$, contradicting the
supposition.

For part (b), let $\Re(V)=\{\Re(h):\ h\in V\}$.  Then $\Re(V)$ is a
real subspace of $\StabR[\x]$, so that $\dim_\RR \Re(V)\leq 2$ by part (a).
If $\dim_\RR \Re(V) \leq 1$ then $\dim_\CC V \leq 1$.  In the remaining
case let $\{p,q\}$ be a basis of $\Re(V)$ with $f=p+\i q\in V$.
By Corollary 2.10,  $\Wr_i[q,p](\a)\leq 0$ for all $i\in[m]$ and $\a\in\RR^m$.
Since $p$ and $q$ are not linearly dependent, there is an index $k\in[m]$
such that $\Wr_k[q,p]\not\equiv 0$.

Consider any $g\in V$.  There are reals $a,b,c,d\in\RR$ such that
$$
g = (ap+bq) + \i (cp + dq).
$$
Since $g$ is stable,
$\Wr_k[cp+dq,ap+bq](\a) = (ad-bc)\Wr_k[q,p](\a)\leq 0$
for all $\a\in\RR^m$.  Since $\Wr_k[q,p]\not\equiv 0$, it follows that
$ad-bc\geq 0$.  Now, for any $v,w\in\RR$, $g+(v+\i w)f$ is in $V$.
Since 
$$
g+(v+\i w)f = (a+v)p+(b-w)q +\i((c+w)p+(d+v)q),
$$
this argument shows that $H = (a+v)(d+v) - (b-w)(c+w)\geq 0$
for all $v,w\in\RR$.  But
$$
4H = (2v+a+d)^2 + (2w+c-b)^2 - (a-d)^2 - (b+c)^2,
$$
so that $H\geq 0$ for all $v,w\in\RR$ if and only if $a=d$ and $b=-c$.
This implies that $g=(a+\i c)f$, so that $\dim_\CC V = 1$.
\end{proof}
