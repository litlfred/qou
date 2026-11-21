---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-032-751-conditions-on-the-eigenvalues
section_title: "Conditions on the eigenvalues"
section_number: 7.5.1
pages: 53-55
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.971
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Using just norms clearly weakens the conditions considerably,
and so one would like to identify the Burau eigenvalues directly.
However, the relations between the $X_i$ do not allow to recover 
by simple algebraic means the individual traces from $P$. 

Using Squier's unitarity, there is an analytic way to recover
the Burau trace of 4-braids (at least for generic $t$ and
up to finite indeterminacy). Since by the previous remarks
the use of $P$ is not essential, we will describe the
procedure given $\Dl$, $V$ and $e$. This gives the most
significant practical enhancement to the above 4-braid tests.

In the following we fix a 4-braid $\bt$ of exponent sum $e$, whose
closure link has Jones polynomial $V$ and Alexander polynomial $\Dl$.
We let $t$ be a unit norm complex number with non-negative real part.

We use that
\[
\tr \psi_3\wedge \psi_3 = (-t)^{e/2}\ol{\tr \psi_3(-t)^{-e/2}}\,.
\]
Then we have
\[
\Dl(t)\,=\,\frac{1-t}{1-t^4}\,\left(-\frac{1}{\sqrt{t}}\right)^{e-3}
\cdot\,\left[ 1-\tr \psi_3 + (-t)^{e/2}\ol{\tr \psi_3(-t)^{-e/2}}-
(-t)^e\,\right]\,.
\]
So, with $i=\sqrt{-1}$,
\[
\dl\,:=-\frac{1}{2i}(-t)^{-e/2}
\left[ \Dl(t)\frac{1-t^4}{1-t}\left(-\frac{1}{\sqrt{t}}\right)^{3-e}
-1 + (-t)^e\,\right]
\]
is a real number. Now when $\lm_{1,2,3}$ are the eigenvalues of
$\psi_3(\bt)$, we have
\begin{eqnarray*}
A & = & \lm_1+\lm_2+\lm_3\,=\,(-t)^{e/2}(y+i\dl) \\
B & = & \lm_1\lm_2+\lm_1\lm_3+\lm_2\lm_3\,=\,(-t)^{e/2}(y-i\dl) \\
C & = & \lm_1\lm_2\lm_3\,=\,(-t)^e\,.
\end{eqnarray*}
Here $y$ is a real number we do not know, and we try to determine.
Since $|\lm_k|=1$, we have
as before $|A|\le 3$ and $|B|\le 3$. So the range
for $y$ is $[-y_0,y_0]$ with $y_0=\sqrt{9-\dl^2}$.
(If $|\dl|>3$ we are done as before.) Then
\[
\tr\psi_3\,\in\,[(-t)^{e/2}(-y_0+i\dl),\, (-t)^{e/2}(y_0+i\dl)]\,,
\]
with the interval understood lying in $\bC$.
Let $\psi_-$ and $\psi_+$ be the endpoints of this interval.

Now one can restrict the interval $[-y_0,y_0]$ for $y$ using the
Jones polynomial as follows.

Let $\rho\,:=(-t)^{-e/2}\tr\bar\psi_2\in [-2,2]$. The restriction
to the given range follows because $J^{[3]}$ (see the proof of
proposition \reference{p4.1}) is also definite when
$J^{[4]}$ is. From \eqref{Vf} we have
\[
\tr \psi_3\,=\,\frac{1-t^2}{t(1-t^3)}\,\left[\,
V(t)\,\left(-\frac{1}{\sqrt{t}}\right)^{e-3}-\frac{1-t^5}{1-t^2}
-\frac{t^2}{1+t}(-t)^{e/2}\cdot \rho\,\right]\,=:\,\tl\psi(\rho)\,,
\]
so
\[
\tl\psi(\rho)=\frac{1-t^2}{t(1-t^3)}\left [
V(t)\,\left(\frac{-1}{\sqrt{t}}\right)^{e-3}-
\frac{1-t^5}{1-t^2}\right] -\frac{\rho}{1+2\Re t}(-t)^{e/2}\,.
\]
(Just for the purpose of defining $\tl\psi$, we should regard here
$\rho$ as a formal parameter, rather than as a concrete value.)

Let $\tl\psi(\pm 2)=:\tl\psi_\pm$. Since $1+2\Re t>0$, we have
$\Re((-t)^{-e/2}\tl\psi_+)>\Re((-t)^{-e/2}\tl\psi_-)$.

Then $[\tl\psi_-,\tl\psi_+]\subset \bC$ is an interval
of the same slope as $[\psi_-,\psi_+]$, so we check if they overlap.

Let
\[
\tl y_{\pm}= (-t)^{-e/2}\tl\psi_\pm -i\delta.
\]

Then for a consistent restriction on $\tr \psi_3$ the following holds:
\begin{enumerate}
\item $\tl y_{\pm}$ are real
\item $ \tl y_+\tl y_-\le 0$ or $\min(\tl y_\pm^2+\delta^2)\le 9$.
\end{enumerate}

Potentially these conditions may be violated, but in
practice they seem always to hold. (We have not elaborated on why
this is so, though it may be worth understanding.) Then at least,
we consider 
\begin{eqn}\label{qw0}
y\in [-y_0,y_0]\cap [\tl y_-,\tl y_+]\,.
\end{eqn}

We have now the cubic
\[
x^3 +ax^2 +bx +c \,:=\,x^3-A x^2+B x-C \,=\,0\,.
\]
One solution is obtained by Cardano's formula
\begin{eqn}\label{qw}
\lm_1\,=\,-\frac{a}{3}
-\frac{\sqrt[3]{2}(-a^2+3b)}{3\Gm} + \frac{\Gm}{3\sqrt[3]{2}}\,,
\end{eqn}
where 
\begin{eqn}\label{Gm}
\Gm=\sqrt[3]{
  -2a^3 + 9ab - 27c + 
  \sqrt{
    27\,\left( -a^2b^2 + 4b^3 + 4a^3c -18abc + 27c^2
    \right)
  }
}\,.
\end{eqn}
We must have that $|\lm_1|=1$. Then we must check $|\lm_{2,3}|=1$.
For this their exact determination is not necessary.
We have $\lm_2+\lm_3=A-\lm_1$ and $\lm_2\lm_3=C/\lm_1$.
In order $|\lm_{2,3}|=1$, we must have
\[
\lm_2+\lm_3=c\cdot \sqrt{\lm_2\lm_3}\,,
\]
with $c\in [-2,2]$, so $A-\lm_1=c\sqrt{C/\lm_1}$, which is
equivalent to
\begin{eqn}\label{qw2}
\frac{(A-\lm_1)^2\lm_1}{C}\,\in\,[0,4]\,.
\end{eqn}
