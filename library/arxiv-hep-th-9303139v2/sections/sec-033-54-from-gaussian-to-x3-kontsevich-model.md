---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-033-54-from-gaussian-to-x3-kontsevich-model
section_title: "From Gaussian to $X^3$ Kontsevich model"
section_number: 5.4
pages: 134-138
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
We shall now abandon these complicated matters and give a simple illustration
of how the things can work, if expressed in the adequate terms. Namely, as
alternative to the sophisticated procedure, involving explicit
switch to Kazakov
variables and the study of limits of Ward-identites (loop equations), we shall
just use the equivalence of the discrete 1-matrix model and Gaussian
Kontsevich model, proved in the section 3.8 above in order to take the
continuum limit just of this simplest Kontsevich model. This procedure,
suggested in ref.\cite{Toda}  appears
to be just a kind of a standard eveluation of the integral in the large
$N$-limit by the steepest descent method. It is important here that GKM is not
sensitive to the size of the matrix $n$ in Kontsevich integral, therefore this
limit, when expressed in terms of GKM, has nothing to do with the infinitely
large matrices.

Relation to be proved below is
\be
\lim_{d.s.\hbox{ }N\rightarrow \infty }{\cal F}_{\{\hat V\}} =
{\cal F}^2_{\{V\}},
\label{coligako}
\ee
where $\hat V(X) = \frac{1}{2}X^2 - N\log X$ and $V(X) = \frac{1}{3}X^3$.

Very naively, what happens as $N \rightarrow \infty$ is that in the Kontsevich
integral,
\be
\int dX \exp {\rm tr}\left(-\frac{1}{2}X^2 + N\log X + \Lambda X\right)
\ee
a stationary point arises at $X = X_0$, such that
\be
X_0 = \frac{N}{X_0} + \Lambda.
\ee
Expansion of this action in powers of $\tilde X = \gamma^{-1} (X - X_0)$ comes
entirely from the logarithmic piece:
\be
S - S_0 &= \frac{\gamma^2}{2}\tilde X^2 - N\left( \log\left(1 + \frac{\gamma
\tilde X}{X_0}\right) - \frac{\tilde X}{X_0}\right) = \nn \\
&= \frac{\gamma^2}{2}\left( 1 + \frac{N}{X_0^2}\right) \tilde X^2
+ \sum_{k\geq 3} \frac{N}{k}\left(-\gamma\frac{\tilde X}{X_0}\right)^k.
\label{actexpan}
\ee
In the continuum limit $\gamma$ should be adjusted in such a way, that
quadratic term is finite, i.e.
${\gamma \sim \left( 1 + \frac{N}{X_0^2}\right)^{-1/2}}$.
Now, if $\Lambda$ remains finite as $N \rightarrow \infty$, $X_0 \sim
\sqrt{N}$,
$\gamma \sim 1$ and all the terms with $k\geq 3$ in the sum are damped as
$\gamma^kNX_0^{-k} \sim N^{1-\frac{k}{2}}$. This is the naive continuum limit.
However, it is clear, that one can usually ask $\Lambda$ to behave more
adequately - blow up together with growth of $N$ -  and fine tune the way in
which it tends to infinity so that at last the first term with $k=3$ also
survives. For this purpose $\Lambda$ and thus $X_0$ should scale in such a
way, that both quantites
$\displaystyle{\gamma^2\left( 1 + \frac{N}{X_0^2}\right)}$ and
$\displaystyle{\frac{N\gamma^3}{X_0^3}}$ remain finite. This requirement in the
case of the latter expression means that
$\gamma \sim X_0N^{-1/3}$ and then
\be
\gamma^2\left( 1 + \frac{N}{X_0^2}\right) \sim \frac{N + X_0^2}{N^{2/3}}.
\nn
\ee
This is never finite, unless $N + X_0^2 \rightarrow 0$ as $N \rightarrow
\infty$. This in turn implies that $X_0 \sim i\sqrt{N}$ and
$\Lambda \rightarrow 2X_0 \sim  2i\sqrt{N}$ should be pure imaginary. One can
also check that the terms with $k>3$ in the sum (\ref{actexpan}) all tend to
zero in this specific limit. Thus we are left with a model which has only
cubic and quadratic terms in the action. By simple shift of variables
quadratic term can be changed for a linear one and we get a description of the
theory in the vicinity of the stationary point in terms of an $X^3$-Kontsevich
model.

In practice things are a little more complicated, because also reduction to
even-times should be taken into account. However, this does not really add too
many new problems. We need that only even times
${t_{2k} = {1\over 2k} {\rm tr}{1\over \Lambda ^{2k}}}$
remain non-vanishing, while all the odd times  ${t_{2k+1} = {1\over
2k+1} {\rm tr}{1\over \Lambda ^{2k+1}} = 0}$.
This obviously implies that the matrix $\Lambda$ should be of block form:
\be
\Lambda = \left(
\begin{array}{cc}
{\cal M} & 0\\0 & -{\cal M}
\end{array}\right)
\ee
and, therefore, the matrix integration variable is also naturally decomposed
into block form:
\be
X = \left(
\begin{array}{cc}
{\cal X} & {\cal Z}\\{\cal Z} & {\cal Y}
\end{array}
\right) .
\ee
Then
\be
\new
\begin{array}{c}
{\cal F}_{\{\hat V=X^2/2-N\log X\}}
= \int d{\cal X}d{\cal Y}d^2{\cal Z}\ \\
{\rm det} ({\cal X}{\cal Y}-\bar {\cal Z}
{1\over {\cal Y}}{\cal Z}{\cal Y})^N
e^{-{\rm tr}\{|{\cal Z}|^2+{\cal X}^2/2+{\cal Y}^2/2-{\cal M}{\cal X}+
{\cal M}{\cal Y}\}}.
\end{array}
\ee
To take the limit $N \rightarrow \infty $, one should assume certain scaling
behaviour of ${\cal X}$, ${\cal Y}$ and ${\cal Z}$. Moreover, our previous
naive consideration gave us some feeling of the
{\it fine tuned} scaling behaviour can look like. So we take
\be
\new
\begin{array}{c}
{\cal X} = \gamma (i\beta I + x), \\
{\cal Y} = \gamma (-i\beta I + y),      \\
{\cal Z} = \gamma \zeta , \\
{\cal M} = \gamma ^{-1}(i\alpha I + m)
\end{array}
\ee
with some large real $\alpha $, $\beta $ and $\gamma $. If expressed through
these variables, the action becomes:
\be
\new
\begin{array}{c}
{\rm tr}\left(|{\cal Z}|^2 + {\cal X}^2/2 + {\cal Y}^2/2 - {\cal M}{\cal X} +
{\cal M}{\cal Y} - N\log ({\cal X}{\cal Y} - \bar {\cal Z}{1\over
{\cal Y}}{\cal Z}{\cal Y})\right) = \\
= \gamma ^2{\rm tr}\left(\frac{1}{2}(i\beta I + x)^2 +
{1\over 2}{\rm tr}(i\beta I -y)^2 + |z|^2\right) - \\
- {\rm tr}(i\alpha I + m)(2i\beta I + x - y) - \\
- N{\rm tr} \log \ \beta ^2\gamma ^2\left(1 - i {x-y\over \beta } +
{xy\over \beta ^2} - {|\zeta |^2\over \beta ^2}(1 + {\cal O}(1/\beta ))\right)
=
\end{array}
\ee
$$
= [2\alpha \beta  - \beta ^2\gamma ^2 - 2N\ \log \ \beta \gamma ] {\rm tr}\ I -
2i\beta \ {\rm tr}\ m +
\eqno{(A)}
$$
$$
+ i\left(\beta \gamma ^2 - \alpha  + {N\over \beta }\right)
({\rm tr}\ x - {\rm tr}\ y) +
{1\over 2}\left(\gamma ^2 - {N\over \beta ^2}\right)
({\rm tr}\ x^2 + {\rm tr}\ y^2) +
\eqno{(B)}
$$
$$
+ \left(\gamma ^2 + {N\over \beta ^2}\right) {\rm tr} |\zeta |^2 -
\eqno{(C)}
$$
$$
- {\rm tr}\ mx + {\rm tr}\ my + {iN\over 3\beta ^3}{\rm tr}(x^3 - y^3) +
\eqno{(D)}
$$
$$
+ {\cal O}(N/\beta ^4) + {\cal O}\left(|\zeta |^2 {N\over \beta ^3}\right).
\eqno{(E)}
$$
We want to adjust the scaling behaviour of $\alpha $, $\beta $ and $\gamma $
in
such a way that only the terms in the line $(D)$ survive. This goal is
achieved
in several steps.

The line ({\it A}) describes normalization of functional integral, it does not
contain $x$ and $y$. Thus, it is not of interest for us at the moment.

Two terms in the line $(B)$ are eliminated by adjustment of $\alpha $ and
$\gamma $:
\be
\gamma ^2 = {N\over \beta ^2}\hbox{ , }  \alpha  = {2N\over \beta }\hbox{ .}
\ee
As we shall see soon,  $\gamma ^2 = N/\beta ^2$ is large in the limit of
$N\rightarrow \infty $ . Thus, the term $(C)$ implies that the fluctuations of
$\zeta $-field are severely suppressed, and this is what makes the terms of
the
second type in the line $(E)$ negligible. More general, this is the reason for
the integral  $Z_{\{\hat V\}}$
to split into a product of two independent integrals leading to the square
of partition function in the limit $N\rightarrow \infty $ (this splitting is
evident as, if ${\cal Z}$ can be neglected, the only mixing term
$\displaystyle{\log \det
\left(
\begin{array}{cc}
{\cal X} & {\cal Z}\\{\cal Z} & {\cal Y}
\end{array}
\right)} $  turns into  $\log {\cal X}{\cal Y} = \log {\cal X} +
\log {\cal Y}$).

Thus, we remain with a single free parameter $\beta $ which can be adjusted so
that
\be
{\beta ^3\over N}\rightarrow {\rm const}\ \ \
\hbox{   as }\ \ \ N\rightarrow \infty \nn \\
(i.e\hbox{. }  \beta  \sim  N^{1/3},\ \gamma^2 \ \sim N^{1/3},\ \alpha \sim
N^{2/3}  ),
\ee
making the terms in the last line $(E)$ vanishing and the third term in the
line $(D)$ finite.

This proves the statement (\ref{coligako}) in a rather straightforward way.
Unfortunately no generalization of this procedure for other discrete models is
found so far, the main problem beeing identification of GKM-type realizations
of other (for example, conformal) discrete matrix models.

\
