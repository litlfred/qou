---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-029-83-the-maximum-of-the-growth-rate-of-the-r-matri
section_title: "The maximum of the growth rate of the R-matrix"
section_number: 8.3
pages: 21-22
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.955
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
In this section we determine the maximum of $r_\pm(\a,\b,\k)$.

\begin{proposition}
\lbl{prop.R}
{\rm (a)}
With $\a,\b,\k$ satisfying \eqref{eq.abk}, $r_+(\a,\b,\k)$ achieves
maximum when $\a=3/4, \b=1/4$, and $\k=1/2$. Moreover
$$
r_+(3/4,1/4,1/2)=\frac{v_8}{2 \pi},
$$
where
$$
v_8=8 \La(\pi/4) \approx 3.6638623767088760602 \dots
$$
is the volume of the regular hyperbolic ideal octahedron.
\newline
{\rm (b)}
Similarly,  $r_-(\a,\b,\k)$ reaches maximum when $\a=1/4, \b=3/4$,
and $k=1/2$; and its maximum value is the same as that of
$r_+(\a,\b,\k)$.
\end{proposition}

Thus, asymptotically, the winning configuration is given by:
$$
\psdraw{winningR}{1in}
$$


\begin{proof}
It is enough to consider the case of $r_+$. The result
for $r_-$ follows from \eqref{62}. Let $\d = \a -\k$, we have
$$
r_+(\a,\b,\k) = -\La(\pi(\b+\k)) +
\La(\pi\b)+\La(\pi\k)-\La(\pi(\d+ \k))+\La(\pi(\d)),
$$
with domain $ 0\le \b,\d,\k$, and $ \b+\k \le 1, \d+\k \le 1$. Note
the symmetry between $\b$ and $\d$.

Using $\La'(x) = - \log(2\sin x)$ for $ 0 <x < \pi$, one can easily
show that the function $-\La(\pi(\b+\k)) + \La(\pi\b)$, for a fixed
$\k \in [0,1]$, achieves maximum at $ \b = (1-\k)/2$. It follows
that the maximum of $r_+(\a,\b,\k)$ is the same as the maximum of

$$
g(\k):= 2(-\La(\pi(\b+\k)) + \La(\pi\b)) + \La(\pi\k),
$$
with $ \b = (1-\k)/2$. The domain for $g$ is $\k \in [0,1]$. Using
the derivative of $g$ it is easy to show that $g$ achieves maximum
when $\k=1/2$. In this case $\a=3/4, \b=1/4$.
\end{proof}

\begin{remark}
Another proof is to use part (b) of Proposition \ref{prop.R+limit} and
the fact that the volume of an ideal octahedron is maximized at a regular
ideal octahedron; see \cite{Ra}.
\end{remark}


\begin{lemma}
\lbl{lem.2circles}
If $z,w$ are complex numbers that satisfy $|z|=|w|=1$ and $|1-z|=|1-w|$,
then $z=w^{\pm 1}$.
\end{lemma}

\begin{proof}
Let us define
$$
C_{u_0,r}:=\{ u \in \BC \,\, | \,\, |u-u_0|=r>0 \}.
$$
Then $C_{u_0,r}$ is a circle with center $u_0$ and radius $r$. Fixing $w$, it
follows that $z \in C_{0,1} \cap C_{1,|1-w|}$. The intersection of two circles
is two points, and since $w$ and $w^{-1}=\bar{w}$ both lie in the intersection,
the result follows.
\end{proof}
