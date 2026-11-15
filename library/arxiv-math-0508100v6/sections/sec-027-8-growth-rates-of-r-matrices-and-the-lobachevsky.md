---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-027-8-growth-rates-of-r-matrices-and-the-lobachevsky
section_title: "Growth rates of R-matrices and the Lobachevsky function"
section_number: 8
pages: 18-19
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.982
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sec.hypgeom}



\subsection{The Lobachevsky function}
\lbl{sub.estimates}

In Section \ref{sec.boundsJones} we got a simple but crude estimate
for the $l^1$-norm of the $R$-matrices, which  are  a ratio of five
quantum factorials. In this largely independent section we will give
 refined (and optimal) estimates for the growth rate of the
$R$-matrices. These estimates reveal the close relationship between
hyperbolic geometry and the asymptotics of the quantum factorials.


Recall that  the {\em Lobachevsky function} is given by
$$
\La(z)=-\int_0^z \log|2 \sin x| dx = \frac{1}{2} \sum_{n=1}^\infty
\frac{\sin(2 n z)}{n^2}
$$
The Lobachevsky function is an odd, periodic function with period
$\pi$. Its graph for $z \in [0, \pi]$ is:
$$
\psdraw{lobachevsky}{2.5in}
$$


\begin{definition}
\lbl{eq.ev}
If $f(q) \in \BZ[q^{\pm 1/4}]$, let us denote by $\ev_n(f)$
the {\em evaluation} of $f$ at $q^{1/4}=e^{\pi i/(2n)}$.
\end{definition}
For $0\le k\le n$ we have
$$
\ev_n|\{k\}| =|e^{k\pi i/n}   -  e^{-k\pi i/n}| = 2\sin (k \pi/n),
$$
hence,
$$
\log (\ev_n|(\{j\}!|)|) = \sum_{k=1}^{j} \log|2\sin (k \pi/n)|,
$$
which is very closely related to a Riemann sum of the integral in
the definition of the Lobachevsky function. It is not surprising to
have the following.

\begin{proposition}
\lbl{lem.1}
For every $\a \in (0,1)$ we have:
$$
\log\left|\ev_n (\{ \lfloor \a n \rfloor \}!)\right|=

-\frac{n}{\pi} \La(\pi \a) +O(\log n).
$$
Here $O(\log n)$ is a term which is bounded by $C \log n$ for some
constant $C$ {\em independent} of $\a$.
\end{proposition}

\begin{remark}
\lbl{rem.subleading}
The proof reveals an asymptotic expansion of the form:
$$
\ev_n (\{ \lfloor \a n \rfloor \}!) \sim n^{\theta}
\exp\left(-\frac{n}{\pi} \La(\pi \a) \right)\left(C_0 + \frac{C_1}{n} +
\frac{C_2}{n^2} + \dots\right)
$$
for explicitly computable constants $C_i$ and $\theta$.
\end{remark}



\begin{proof}
Recall the {\em Euler-MacLaurin summation formula},
with error term (see for example, \cite[Chpt. 8]{O}):
$$
\sum_{k=a}^b f(k)=\int_a^b f(x) dx + \frac{1}{2} f(a) +
\frac{1}{2} f(b) +
\sum_{k=1}^{m-1} \frac{B_{2k}}{(2k)!}( f^{(2k-1)}(b)-f^{(2k-1)}(a) )
+ R_m(a,b,f)
$$
where $B_k$ is the $k$th {\em Bernoulli number} and the error term has an
estimate
$$
|R_m(a,b,f)| \leq (2-2^{1-2m}) \frac{|B_{2m}|}{(2m)!}
\int_a^b |f^{(2m)}(x)| dx.
$$

Applying the above formula  for $m=1$ to $f(x)=\log(2 \sin
x\pi/n)$, we have:
\begin{eqnarray*}
\log(\prod_{k=1}^{\lfloor \a n \rfloor } 2\sin (k \pi/n)) & = &
\frac{1}{2} (f(1)+f(\lfloor \a n \rfloor ))+
\int_1^{\lfloor \a n \rfloor } \log(2\sin (t \pi/n)) dt
+R_1(1,\lfloor \a n \rfloor,f) \\
& = &  \frac{1}{2} (f(1)+f( \a n )+
\int_1^{\a n } \log(2\sin (t \pi/n)) dt
+R_1(1,\lfloor \a n \rfloor,f) + \e(\a,n) \\
& = & \frac{1}{2} (f(1)+f(\a n))+ \frac{n}{\pi}  \int_{\pi/n}^{\pi
\a} \log|2 \sin (  u)| u +R_1(1,\lfloor \a n \rfloor, f) +\e(\a,n)
\\
& = & \frac{1}{2} (f(1)+f(\a n))+ \frac{n}{\pi} \left(-\La(\pi \a) +
\La(\frac{\pi}{n}) \right) + R_1(1,\lfloor \a n \rfloor, f) +
\e(\a,n).
\end{eqnarray*}
Here $\e(\a,n)$ comes from adjusting the boundary of integration and
satisfies $|\e(\a,n) | = O(1)$. Note that
$$
\frac{1}{2} |f(1)+f(\a n)| = O( \log n).
$$
Moreover,
$f''(x)=\frac{\pi^2}{n^2} (\csc(\pi x/n))^2 >0$. Hence

$$
\int_1^{\lfloor \al n\rfloor} |f''(x)| dx
=\int_1^{\lfloor \al n\rfloor} f''(x) dx \le \int_1^{\al n} f''(x) dx
= \frac{\pi}{n} \left( \cot(\al \pi) - \cot\left(\frac{\pi}{n}\right)\right).
$$

It follows easily that
$$
|R_1(1,\lfloor \a n \rfloor, f)| = O(1).
$$
Furthermore, using L'Hospital's rule,
one can see  that
$$
\frac{n}{\pi} \left|\La(\frac{\pi}{n})\right| = O( \log n).
$$
The result follows.






\end{proof}


\begin{corollary} For every $\a \in (0,1)$  and any fixed number $d$ we have:
$$
\log\left|\ev_n (\{ \lfloor \a n  +d \rfloor \}!)\right|=

-\frac{n}{\pi} \La(\pi \a) +O(\log n).
$$
\label{87}
\end{corollary}

\begin{proof}
There is $\ve >0$ such that for big enough $n$, we
have $\ve \le x/n \le 1-\ve$ for every integer $x$ between $\lfloor
\a n \rfloor$ and $\lfloor \a n  +d \rfloor$. For such $x$, we have
$ 0< 2 \sin \ve \pi   < 2\sin (x\pi/n)  < 2$, and hence there is a
constant $M$ such that $|\log 2\sin (x\pi/n) | < M$. There are at most
$|d|+1$ such values of $x$. Hence the difference  between
$\log\left|\ev_n (\{ \lfloor \a n  +d \rfloor \}!)\right|$ and $
\log\left|\ev_n (\{ \lfloor \a n \rfloor \}!)\right|$ by absolute
value is less than $(|d|+1) M$, a constant. The result follows.
\end{proof}
