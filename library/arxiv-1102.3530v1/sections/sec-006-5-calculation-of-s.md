---
doc_id: arxiv-1102.3530v1
doc_title: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion"
section_id: sec-006-5-calculation-of-s
section_title: "Calculation of S"
section_number: 5
pages: 12-34
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
doc_brief: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight"
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.927
---
\label{sec:S_gamma}
In this section we first show the analyticity of $S_{\gamma}$ and then calculate its special values.
\begin{lem}\label{lem:analyticity}
If a complex number $\gamma$ has the positive real part, then $S_{\gamma}(z)$ is an analytic function in $\{z\in\C\mid|\Re(z)|<\pi+\Re(\gamma)\}$.
\end{lem}
\begin{proof}
Put
\begin{equation*}
  L_{\gamma}(t)
  :=
    \frac{e^{zt}}{t\sinh(\pi t)\sinh(\gamma t)}.
\end{equation*}
We will show that the improper integrals $\int_{R}^{\infty}L_{\gamma}t\,dt$ and $\int_{-\infty}^{R}L_{\gamma}t\,dt$ converge.
\par
Putting $z:=x+\sqrt{-1}y$ and $\gamma:=a+\sqrt{-1}b$ for real numbers $x,y,a,b$ with $a>0$ we have
\begin{equation*}
  \Re(L_{\gamma}(t))
  =
  \frac
  {-2e^{xt}\bigl(\cosh(at)\sin(bt)\sin(ty)+\sinh(at)\cos(bt)\cos(yt)\bigr)}
  {t\sinh(\pi t)\bigl(\cos(2bt)-\cosh(2at)\bigr)}
\end{equation*}
and
\begin{equation*}
  \Im(L_{\gamma}(t))
  =
  \frac
  {2e^{xt}\bigl(\cosh(at)\sin(bt)\cos(ty)-\sinh(at)\cos(bt)\sin(yt)\bigr)}
  {t\sinh(\pi t)\bigl(\cos(2bt)-\cosh(2at)\bigr)}
\end{equation*}
for $t\in\R$.
\par
If $t$ is positive and sufficiently large we have
\begin{equation*}
\begin{split}
  |\Re(L_{\gamma}(t))|
  &\le
  \frac{2e^{xt}e^{at}}{t\sinh(\pi t)(\cosh(2at)-1)}
  \\
  &=
  \frac{8e^{(x-\pi-a)t}}{t(1-e^{-2\pi t})(1+e^{-4at}-2e^{-2at})}
\end{split}
\end{equation*}
and similarly we have
\begin{equation*}
  |\Im(L_{\gamma}(t))|
  \le
  \frac{8e^{(x-\pi-a)t}}{t(1-e^{-2\pi t})(1+e^{-4at}-2e^{-2at})}.
\end{equation*}
Therefore the integral $\int_{R}^{\infty}L_{\gamma}t\,dt$ converges since $x<\pi+a$.
\par
If $t$ is negative and $|t|$ is sufficiently large we have
\begin{equation*}
\begin{split}
  |\Re(L_{\gamma}(t))|
  &\le
  \frac{2e^{(x-a)t}}{t\sinh(\pi t)(\cosh(2at)-1)}
  \\
  &=
  \frac{8e^{(x+\pi+a)t}}{t(e^{2\pi t}-1)(e^{4at}+1-2e^{2at})}
\end{split}
\end{equation*}
and similarly we have
\begin{equation*}
  |\Im(L_{\gamma}(t))|
  \le
  \frac{8e^{(x+\pi+a)t}}{t(e^{2\pi t}-1)(e^{4at}+1-2e^{2at})}.
\end{equation*}
Therefore the integral $\int_{-\infty}^{R}L_{\gamma}t\,dt$ converges since $x>-\pi-a$.
\end{proof}
Next we prove Lemma~\ref{lem:S_gamma}.
\begin{proof}[Proof of Lemma~\ref{lem:S_gamma}]
By the definition we have
\begin{equation*}
\begin{split}
  &\frac{S_{\gamma}(-\pi-\sqrt{-1}u+\gamma)}{S_{\gamma}(\pi-\sqrt{-1}u-\gamma)}
  \\
  =&
  \exp
  \left(
    \frac{1}{4}
    \int_{C_R}
    \left(
      \frac{e^{(-\pi-\sqrt{-1}u+\gamma)t}}{\sinh(\pi t)\sinh(\gamma t)}
      -
      \frac{e^{(\pi-\sqrt{-1}u-\gamma)t}}{\sinh(\pi t)\sinh(\gamma t)}
    \right)
    \frac{dt}{t}
  \right)
  \\
  =&
  \exp
  \left(
    \frac{1}{2}
    \int_{C_R}
    e^{-\sqrt{-1}ut}
    \frac{\sinh(-\pi t+\gamma t)}{\sinh(\pi t)\sinh(\gamma t)}
    \frac{dt}{t}
  \right)
  \\
  =&
  \exp
  \left(
    \frac{1}{2}
    \int_{C_R}
    \frac{e^{-\sqrt{-1}ut}\coth(\pi t)}{t}
    \,dt
    -
    \frac{1}{2}
    \int_{C_R}
    \frac{e^{-\sqrt{-1}ut}\coth(\gamma t)}{t}
    \,dt
  \right).
\end{split}
\end{equation*}
We will calculate the integral $\int_{C_R}e^{-\sqrt{-1}ut}\coth(\kappa t)/t\,dt$ for a complex number $\kappa$ with $\Re(\kappa)>0$ and $\Im(\kappa)\le0$.
\par
Put $\kappa:=\alpha-\beta\sqrt{-1}$ with $\alpha>0$ and $\beta\ge0$.
For a positive number $r$, let $U_1$ be the segment connecting $r$ and $r+r'\beta/\alpha-r'\sqrt{-1}$, $U_2$ be the segment connecting $r+r'\beta/\alpha-r'\sqrt{-1}$ and $-r+r'\beta/\alpha-r'\sqrt{-1}$, and $U_3$ be the segment connecting $-r+r'\beta/\alpha-r'\sqrt{-1}$ and $-r$ with $r':=(n+1/2)\pi\alpha/|\kappa|^2$, where $n:=\lfloor{r|\kappa|^2/(\pi\alpha)}\rfloor$.
Here $\lfloor{x}\rfloor$ is the largest integer that does not exceed $x$.
Note that $r-\pi\alpha/(2|\kappa|^2)<r'\le r+\pi\alpha/(2|\kappa|^2)$.
We use $r'$ instead of $r$ just to avoid the poles of $\coth(\kappa t)$.
Then we have
\begin{equation*}
\begin{split}
  &\left|
    \int_{U_1}
    \frac{e^{-\sqrt{-1}ut}}{t}
    \coth(\kappa t)
    \,dt
  \right|
  \\
  \le&
  \int_{0}^{r'}
  \left|
    \frac{e^{-\sqrt{-1}u(r+s\beta/\alpha-s\sqrt{-1})}}
         {r+s\beta/\alpha-s\sqrt{-1}}
  \right|
  \left|
    \coth\bigl((\alpha-\beta\sqrt{-1})(r+s\beta/\alpha-s\sqrt{-1})\bigr)
  \right|
  \,ds
  \\
  \le&
  \frac{1}{r}
  \int_{0}^{r'}
  e^{-us}
  \left|
    \coth\bigl(r\alpha-\sqrt{-1}(s\alpha+r\beta+s\beta^2/\alpha)\bigr)
  \right|
  \,ds
  \\
  \le&
  \frac{1}{r}
  \int_{0}^{r'}
  e^{-us}
  \,ds
  \\
  =&
  \frac{1}{ur}
  (1-e^{-ur'})
  \xrightarrow{r\to\infty}0.
\end{split}
\end{equation*}
Similarly we have
\begin{equation*}
\begin{split}
  &\left|
    \int_{U_3}
    \frac{e^{-\sqrt{-1}ut}}{t}
    \coth(\kappa t)
    \,dt
  \right|
  \\
  \le&
  \int_{0}^{r'}
  \left|
    \frac{e^{-\sqrt{-1}u(-r+s\beta/\alpha-s\sqrt{-1})}}
         {-r+s\beta/\alpha-s\sqrt{-1}}
  \right|
  \left|
    \cosh\bigl((\alpha-\beta\sqrt{-1})(-r+s\beta/\alpha-s\sqrt{-1})\bigr)
  \right|
  \,ds
  \\
  \le&
  \frac{|\kappa|}{r\alpha}
  \int_{0}^{r'}
  e^{-us}
  \left|
    \cosh\bigl(-r\alpha-\sqrt{-1}(s\alpha-r\beta+s\beta^2/\alpha)\bigr)
  \right|
  \,ds
  \\
  \le&
  \frac{|\kappa|}{ur\alpha}
  (1-e^{-ur'})
  \xrightarrow{r\to\infty}0.
\end{split}
\end{equation*}
We also have
\begin{equation*}
\begin{split}
  &\left|
    \int_{U_2}
    \frac{e^{-\sqrt{-1}ut}}{t}
    \coth(\kappa t)
    \,dt
  \right|
  \\
  \le&
  \int_{-r}^{r}
  \left|
    \frac{e^{-\sqrt{-1}u(s+r'\beta/\alpha-r'\sqrt{-1})}}
         {s+r'\beta/\alpha-r'\sqrt{-1}}
  \right|
  \left|
    \coth\bigl((\alpha-\beta\sqrt{-1})(s+r'\beta/\alpha-r'\sqrt{-1})\bigr)
  \right|
  \,ds
  \\
  \le&
  \frac{e^{-ur'}}{r'}
  \int_{-r}^{r}
  \left|
   \coth\bigl(s\alpha-\sqrt{-1}(r'\alpha+s\beta+r'\beta^2/\alpha)\bigr)
  \right|
  \,ds
  \\
  =&
  \frac{e^{-ur'}}{r'}
  \int_{-r}^{r}
  \left|
   \coth
   \left(
     s\alpha-\sqrt{-1}\bigl((n+1/2)\pi+s\beta\bigr)
   \right)
  \right|
  \,ds
  \\
  =&
  \frac{e^{-ur'}}{r'}
  \int_{-r}^{r}
  \left|
    \tanh\bigl(\kappa s\bigr)
  \right|
  \,ds
  \\
  &\text{($\delta:=\max_{-1\le s\le1}|\tanh(\kappa s)|>0$)}
  \\
  \le&
  \frac{e^{-ur'}}{r'}
  \left(
    2\delta
    +
    \int_{-r}^{-1}
    \frac{|e^{\kappa s}-e^{-\kappa s}|}{|e^{\kappa s}+e^{-\kappa s}|}
    \,ds
    +
    \int_{1}^{r}
    \frac{|e^{\kappa s}-e^{-\kappa s}|}{|e^{\kappa s}+e^{-\kappa s}|}
    \,ds
  \right)
  \\
  \le&
  \frac{e^{-ur'}}{r'}
  \left(
    2\delta
    +
    \int_{-r}^{-1}
    \frac{|e^{\kappa s}|+|e^{-\kappa s}|}
         {\bigl||e^{\kappa s}|-|e^{-\kappa s}|\bigr|}
    \,ds
    +
    \int_{1}^{r}
    \frac{|e^{\kappa s}|+|e^{-\kappa s}|}
         {\bigl||e^{\kappa s}|-|e^{-\kappa s}|\bigr|}
    \,ds
  \right)
  \\
  =&
  \frac{2e^{-ur'}}{r'}
  \left(
    \delta
    +
    \int_{1}^{r}|\coth(\alpha s)|\,ds
  \right)
  \\
  =&
  \frac{2e^{-ur'}}{r'}
  \left(
    \delta
    +
    \frac{\log(\sinh(\alpha r))-\log(\sinh(\alpha))}{\alpha}
  \right)
  \xrightarrow{r\to\infty}0.
\end{split}
\end{equation*}
Therefore we have
\begin{equation*}
\begin{split}
  \int_{C_R}\frac{e^{-\sqrt{-1}ut}}{t}\coth(\kappa t)\,dt
  &=
  2\pi\sqrt{-1}
  \sum_{l=1}^{\infty}
  \Res
  \left(
    \frac{e^{-\sqrt{-1}ut}}{t}\coth(\kappa t);
    t=\frac{l\pi\sqrt{-1}}{\kappa}
  \right)
  \\
  &=
  2\pi\sqrt{-1}
  \sum_{l=1}^{\infty}
  \frac{e^{lu\pi/\kappa}}{l\pi\sqrt{-1}}
  \\
  &=
  -2\log(1-e^{u\pi/\kappa})
\end{split}
\end{equation*}
and so we have
\begin{equation*}
  \frac{S_{\gamma}(-\pi-\sqrt{-1}u+\gamma)}{S_{\gamma}(\pi-\sqrt{-1}u-\gamma)}
  =
  \frac{1-e^{u\pi/\gamma}}{1-e^u}.
\end{equation*}
\end{proof}


\section{Proof of Proposition~\ref{prop:4.7}}
\label{sec:prop:4.7}
In this section we follow \cite[Appendix~A]{Andersen/Hansen:JKNOT2006} to show Proposition~\ref{prop:4.7}.
\par
From \cite[\S~4.1]{Andersen/Hansen:JKNOT2006} we have the following integral expression for $|\Re(z)|<\pi$, or $|\Re(z)|=\pi$ and $\Im(z)\ge0$:
\begin{equation*}
  \frac{1}{2\sqrt{-1}}
  \Li_2(-e^{\sqrt{-1}z})
  =
  \frac{1}{4}
  \int_{C_R}\frac{e^{zt}}{t^2\sinh(\pi t)}\,dt.
\end{equation*}
Therefore we have
\begin{equation*}
\begin{split}
  S_{\gamma}(z)
  &=
  \exp
  \left(
    \frac{1}{2\sqrt{-1}\gamma}
    \Li_2(-e^{\sqrt{-1}z})
    +
    I_{\gamma}(z)
  \right)
  \\
  &=
  \exp
  \left(
    \frac{N}{\xi}
    \Li_2(-e^{\sqrt{-1}z})
    +
    I_{\gamma}(z)
  \right),
\end{split}
\end{equation*}
where
\begin{equation*}
  I_{\gamma}(z)
  :=
  \frac{1}{4}
  \int_{C_R}\frac{e^{zt}}{t\sinh(\pi t)}
  \left(
    \frac{1}{\sinh(\gamma t)}-\frac{1}{\gamma t}
  \right)
  \,dt
\end{equation*}
(see \cite[Equation~(4.2)]{Andersen/Hansen:JKNOT2006}).
Note that $I_{\gamma}(z)$ is defined for $z$ with $|\Re(z)|\le\pi$ (\cite[Appendix~A]{Andersen/Hansen:JKNOT2006}).
\par
Then we have from \eqref{eq:g_N_def}
\begin{equation}\label{eq:g_N}
\begin{split}
  &g_N(z)
  \\
  =&
  \exp
  \left(
    \frac{N}{\xi}
    \left(
      \Li_2(-e^{\sqrt{-1}\pi+u-\xi z})
      -
      \Li_2(-e^{-\sqrt{-1}\pi+u+\xi z})
    \right)
    -Nuz
  \right)
  \\
  &\times
  \exp
  \left(
    I_{\gamma}(\pi-\sqrt{-1}u+\sqrt{-1}\xi z)
    -
    I_{\gamma}(-\pi-\sqrt{-1}u-\sqrt{-1}\xi z)
  \right)
  \\
  =&
  \exp\bigl(N\Phi(z)\bigr)
  \exp
  \bigl(
    I_{\gamma}(\pi-\sqrt{-1}u+\sqrt{-1}\xi z)
    -
    I_{\gamma}(-\pi-\sqrt{-1}u-\sqrt{-1}\xi z)
  \bigr).
\end{split}
\end{equation}
\par
We first give an estimation for $|I_{\gamma}(z)|$.
\begin{lem}[see Lemma~3 in \cite{Andersen/Hansen:JKNOT2006}]\label{lem:Lemma3}
If $|\Re(z)|<\pi$, then we have
\begin{equation*}
  |I_{\gamma}(z)|
  \le
  A
  \left(
    \frac{1}{\pi-\Re(z)}+\frac{1}{\pi+\Re(z)}
  \right)
  |\gamma|
  +
  B
  \left(
    1+e^{-\Im(z)R}
  \right)
  |\gamma|
\end{equation*}
If $|\Re(z)|\le\pi$, then we have
\begin{equation*}
  |I_{\gamma}(z)|
  \le
  2A+B(1+e^{-\Im(z)R})|\gamma|.
\end{equation*}
\end{lem}
\begin{proof}
We follow \cite[Appendix~A]{Andersen/Hansen:JKNOT2006}.
\par
Put
\begin{equation*}
  \psi(w)
  :=
  \frac{1}{\sinh(w)}-\frac{1}{w},
\end{equation*}
which is holomorphic in the open disk $D_0(\pi)$ with center $0$ and radius $\pi$.
Note that
\begin{equation}\label{eq:psi}
  \psi(w)
  =
  \frac{w-\sinh(w)}{w\sinh(w)}
  =
  -w
  \frac{h(w)}{k(w)}
\end{equation}
for entire functions $h(w)$ and $k(w)$ with
\begin{align*}
  h(w)&=\sum_{j=0}^{\infty}\frac{w^{2j}}{(2j+3)!}
  \intertext{and}
  k(w)&=\sum_{j=0}^{\infty}\frac{w^{2j}}{(2j+1)!}
\end{align*}
when $|w|<\pi$.
Therefore there exists $\delta>0$ such that $\min_{|w|\le\delta}|\psi(w)/w|=D>0$ since $\lim_{w\to0}\psi(w)/w=1/6$.
\par
Put $C_{\delta}:=[-\delta/|\gamma|,-R]\cup\Omega_R\cup[R,\delta/|\gamma|]$.
Consider the following integrals $I_0(z)$ and $I_1(z)$ so that $I_{\gamma}(z)=I_0(z)+I_1(z)$:
\begin{align*}
  I_0(z)
  &:=
  \frac{1}{4}
  \int_{C_{\delta}}
  \frac{\exp(zt)}{t\sinh(\pi t)}\psi(\gamma t)
  \,dt,
  \\
  I_1(z)
  &:=
  \frac{1}{4}
  \int_{-\infty}^{-\delta/|\gamma|}
  \frac{\exp(zt)}{t\sinh(\pi t)}\psi(\gamma t)
  \,dt
  +
  \frac{1}{4}
  \int_{\delta/|\gamma|}^{\infty}
  \frac{\exp(zt)}{t\sinh(\pi t)}\psi(\gamma t)
  \,dt.
\end{align*}
Since $\lim_{w\to\infty}w\psi(w)=0$, $\psi(w)$ has poles at $w=m\pi\sqrt{-1}$ ($m=\pm1,\pm2,\dots$), and $\Im(\gamma)\ne0$, we have $|\gamma t\psi(\gamma t)|\le E$ for a positive number $E$.
Note that $E$ depends only on the argument of $\gamma$ and so only on $\xi=\gamma\times 2\sqrt{-1}N$.
So we have
\begin{equation*}
  |\psi(\gamma t)|
  \le
  \frac{E}{|\gamma t|}
\end{equation*}
for any $t$.
Therefore we can apply the argument (replacing $\gamma$ there with $|\gamma|/E$ and $a$ with $\delta/|\gamma|$) in \cite[Page~532]{Andersen/Hansen:JKNOT2006} to conclude
\begin{equation*}
  |I_1(z)|
  \le
  \frac{E}{\delta\left(1-e^{-2\pi|\delta|/|\gamma|}\right)}
\end{equation*}
if $|\Re(z)|\le\pi$ and
\begin{equation*}
  |I_1(z)|
  \le
  \frac{E|\gamma|}
       {2\delta^2\left(1-e^{-2\pi\delta/|\gamma|}\right)}
  \left(
    \frac{e^{-(\pi-\Re(z))\delta/|\gamma|)}}{\pi-\Re(z)}
    +
    \frac{e^{-(\pi+\Re(z))\delta/|\gamma|)}}{\pi+\Re(z)}
  \right)
\end{equation*}
if $|\Re(z)|<\pi$.
\par
\begin{comment}
If $t\in {C'}_{R}$, then $|\gamma t|\le\delta$ and so we have $|\psi(\gamma t)|\le D|\gamma||t|$.
So we have
\begin{equation*}
  |I_0(z)|
  \le
  \frac{|\gamma|}{4}
  \int_{C_{\delta}}
  \left|
    \frac{\exp(zt)}{\sinh(\pi t)}
  \right|\,dt.
\end{equation*}
\par
\end{comment}
Next we estimate $I_0(z)$.
Let $M(z,R)$ be the maximum of $\left|\frac{e^{z t}}{t\sinh(\pi t)}\psi(\gamma t)\right|$ for $t\in\Omega_R$.
Then we have
\begin{equation*}
  \left|
    \int_{\Omega_R}
    \frac{\exp(zt)}{t\sinh(\pi t)}\psi(\gamma t)
    \,dt
  \right|
  \le
  \pi R M(z,R).
\end{equation*}
\par
From \eqref{eq:psi} we have
\begin{equation*}
\begin{split}
  M(z,R)
  &=
  \max_{t\in\Omega_R}
  \left|\frac{e^{z t}}{t\sinh(\pi t)}\psi(\gamma t)\right|
  \\
  &=
  \max_{t\in\Omega_R}
  |\gamma|
  \left|\frac{e^{z t}}{\sinh(\pi t)}\right|
  \left|\frac{h(\gamma t)}{k(\gamma t)}\right|
\end{split}
\end{equation*}
since $|\gamma t|=|\gamma|R<\pi$ when $t\in\Omega_R$ and $R<1$.
Then putting $L(R):=\max_{t\in\Omega_R}|h(z)/k(z)|$ and $N(z,R):=\max_{t\in\Omega_R}\left|e^{zt}/(e^{\pi t}-e^{-\pi t})\right|$ we can apply the argument in \cite[Page~533]{Andersen/Hansen:JKNOT2006} to have the following estimation.
\begin{equation*}
  \left|
    \frac{1}{4}
    \int_{\Omega_R}
    \frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
  \right|
  \le
  |\gamma|B(1+e^{-\Im(z)R})
\end{equation*}
for a constant $B$ (depending only on $R$).
\par
Now we will estimate the rest of $I_0(z)$.
We have
\begin{equation*}
\begin{split}
  &\left|
    \int_{-\delta/|\gamma|}^{-R}\frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
    +
    \int_{R}^{\delta/|\gamma|}\frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
  \right|
  \\
  \le&
  \int_{-\delta/|\gamma}^{-R}
  \frac{e^{\Re(z)t}}{|t||\sinh(\pi t)|}|\psi(\gamma t)|\,dt
  +
  \int_{R}^{\delta/|\gamma}
  \frac{e^{\Re(z)t}}{|t||\sinh(\pi t)|}|\psi(\gamma t)|\,dt
  \\
  =&
  \int_{R}^{\delta/|\gamma}
  \frac{e^{\Re(z)t}+e^{-\Re(z)t}}{t\sinh(\pi t)}
  |\psi(\gamma t)|\,dt
  \\
  =&
  2|\gamma|
  \int_{R}^{\delta/|\gamma}
  \frac{e^{\Re(z)t}+e^{-\Re(z)t}}{e^{\pi t}-e^{-\pi t}}
  \left|\frac{\psi(\gamma t)}{\gamma t}\right|\,dt.
\end{split}
\end{equation*}
Since $\psi(w)/w$ is continuous in $D_0(\pi)$ and $\lim_{w\to0}\psi(w)/w=1/6$, there exists $\delta>0$ such that $\min_{|w|<\delta}|\psi(w)/w|=D>0$.
Therefore if $a<\delta/|\gamma|$, then $|\gamma t|\le|\gamma|a<\delta$ in the integral and so we have
\begin{equation*}
\begin{split}
  &\left|
    \int_{-\delta/|\gamma|}^{-R}
    \frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
    +
    \int_{R}^{\delta/|\gamma|}
    \frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
  \right|
  \\
  \le&
  2|\gamma|D
  \int_{R}^{\delta/|\gamma|}
  \frac{e^{\Re(z)t}+e^{-\Re(z)t}}{e^{\pi t}-e^{-\pi t}}
  \,dt
  \\
  \le&
  \frac{2|\gamma|D}{1-e^{-2\pi R}}
  \int_{R}^{a}(e^{-(\pi-\Re(z))t}+e^{-(\pi+\Re(z))t})
  \,dt.
\end{split}
\end{equation*}
Then from the argument in \cite[Page~533]{Andersen/Hansen:JKNOT2006} we have
\begin{equation*}
\begin{split}
  &\left|
    \int_{-\delta/|\gamma|}^{-R}
    \frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
    +
    \int_{R}^{\delta/|\gamma|}
    \frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
  \right|
  \\
  \le&
  \frac{4\delta D}{1-e^{-2\pi R}}
\end{split}
\end{equation*}
when $|\Re(z)|\le\pi$, and
\begin{equation*}
\begin{split}
  &\left|
    \int_{-\delta/|\gamma|}^{-R}
    \frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
    +
    \int_{R}^{\delta/|\gamma|}
    \frac{e^{zt}}{t\sinh(\pi t)}\psi(\gamma t)\,dt
  \right|
  \\
  \le&
  \frac{2|\gamma|D}{(1-e^{-2\pi R})}
  \left(
    \frac{1-e^{-(\pi-\Re(z))\delta/|\gamma|}}{\pi-\Re(z)}
    +
    \frac{1-e^{-(\pi+\Re(z))\delta/|\gamma|}}{\pi+\Re(z)}
  \right)
\end{split}
\end{equation*}
when $|\Re(z)|<\pi$.
\par
Therefore if $|\Re(z)|\le\pi$, we have
\begin{equation*}
\begin{split}
  I_{\gamma}(z)
  &\le
  \frac{E}{\delta\left(1-e^{-2\pi|\delta|/|\gamma|}\right)}
  +
  |\gamma|B\left(1+e^{\Im(z)R}\right)
  +
  \frac{\delta D}{1-e^{-2\pi R}}
  \\
  &\le
  \frac{1}{1-e^{-2\pi R}}\left(\frac{E}{\delta}+\delta D\right)
  +
  |\gamma|B\left(1+e^{\Im(z)R}\right)
\end{split}
\end{equation*}
since $\delta/|\gamma|\ge R$.
If $|\Re(z)|<\pi$ we also have
\begin{equation*}
\begin{split}
  &|I_{\gamma}(z)|
  \\
  \le&
  \frac{E|\gamma|}
       {2\delta^2\left(1-e^{-2\pi\delta/|\gamma|}\right)}
  \left(
    \frac{e^{-(\pi-\Re(z))\delta/|\gamma|)}}{\pi-\Re(z)}
    +
    \frac{e^{-(\pi+\Re(z))\delta/|\gamma|)}}{\pi+\Re(z)}
  \right)
  \\
  &+
  \frac{|\gamma|D}{2(1-e^{-2\pi R})}
  \left(
    \frac{1-e^{-(\pi-\Re(z))\delta/|\gamma|}}{\pi-\Re(z)}
    +
    \frac{1-e^{-(\pi+\Re(z))\delta/|\gamma|}}{\pi+\Re(z)}
  \right)
  \\
  &+
  |\gamma|B\left(1+e^{\Im(z)R}\right)
  \\
  \le&
  |\gamma|
  \left(
    \frac{1}{\pi-\Re(z)}+\frac{1}{\pi+\Re(z)}
  \right)
  \frac{1}{1-e^{-2\pi R}}
  \left(\frac{E}{2\delta^2}+\frac{D}{2}\right)+
  |\gamma|B\left(1+e^{\Im(z)R}\right).
\end{split}
\end{equation*}
\par
The lemma follows by putting
\begin{equation*}
  A
  :=
  \frac{1}{1-e^{-2\pi R}}
  \times
  \max
  \left\{
    \left(\frac{E}{2\delta}+\frac{\delta D}{2}\right),
    \left(\frac{E}{2\delta^2}+\frac{D}{2}\right)
  \right\}.
\end{equation*}
\end{proof}

Now we prove Proposition~\ref{prop:4.7}.
\par
First note that since $g_N(x)$ has no poles inside $C_{+}(\varepsilon)\cup C_{-}(\varepsilon)$, we can assume that $\varepsilon=0$ without changing the sum, that is,
\begin{equation*}
\begin{split}
  &\int_{C_{+}(\varepsilon)}(\tan(N\pi x)-\sqrt{-1})g_N(x)\,dx
  +
  \int_{C_{-}(\varepsilon)}(\tan(N\pi x)+\sqrt{-1})g_N(x)\,dx
  \\
  =&
  \int_{C_{+}(0)}(\tan(N\pi x)-\sqrt{-1})g_N(x)\,dx
  +
  \int_{C_{-}(0)}(\tan(N\pi x)+\sqrt{-1})g_N(x)\,dx
\end{split}
\end{equation*}
We decompose $C_{+}(0)$ into $C_{+,1}\cup C_{+,2}\cup C_{+,3}$, where $C_{+,1}$ connects $0$ and $-u/(2\pi)+\sqrt{-1}$, $C_{+,2}$ connects $-u/(2\pi)+\sqrt{-1}$ and $1-u/(2\pi)+\sqrt{-1}$, and $C_{+,3}$ connects $1-u/(2\pi)+\sqrt{-1}$ and $1$.
Similarly we also decompose $C_{-}(0)$ in to $C_{-,1}\cup C_{-,2}\cup C_{-,3}$, where $C_{-,1}$ connects $0$ and $u/(2\pi)-\sqrt{-1}$, $C_{-,2}$ connects $u/(2\pi)-\sqrt{-1}$ and $1+u/(2\pi)-\sqrt{-1}$, and $C_{-,3}$ connects $1+u/(2\pi)-\sqrt{-1}$ and $-1$.
Let $I_{\pm,i}(N)$ be the integral of $\bigl(\tan(N\pi x)-\sqrt{-1}\bigr)g_N(x)$ along $C_{\pm,i}$ ($i=1,2,3$).
We will show that $|I_{\pm,i}(N)|$ is bounded from above by $K_{\pm,i}/N$ for a positive constant $K_{\pm,i}$ independent of $N$.
\par
We will give the following estimations for $I_{\pm,i}(N)$.

\begin{equation}\label{eq:I_{+,1}}
  |I_{+,1}(N)|<\frac{K_{+,1}}{N}.
\end{equation}
\begin{equation}\label{eq:I_{+,2}}
  |I_{+,2}(N)|<\frac{K_{+,2}}{N}.
\end{equation}
\begin{equation}\label{eq:I_{+,3}}
  |I_{+,3}(N)|<\frac{K_{+,3}}{N}.
\end{equation}
\begin{equation}\label{eq:I_{-,1}}
  |I_{-,1}(N)|<\frac{K_{-,1}}{N}.
\end{equation}
\begin{equation}\label{eq:I_{-,2}}
  |I_{-,2}(N)|<\frac{K_{-,2}}{N}.
\end{equation}
\begin{equation}\label{eq:I_{-,3}}
  |I_{-,3}(N)|<\frac{K_{-,3}}{N}.
\end{equation}

\begin{proof}[Proof of \eqref{eq:I_{+,1}}]
We first estimate $|\tan(N\pi (-u/(2\pi)+\sqrt{-1})t)-\sqrt{-1}|$.
We have
\begin{equation*}
\begin{split}
  &
  |\tan(N\pi (-u/(2\pi)+\sqrt{-1})t))-\sqrt{-1}|
  \\
  =&
  \left|
    \frac{2e^{-Nut\sqrt{-1}/2-N\pi t)}}
         {e^{-Nut\sqrt{-1}/2-N\pi t)}+e^{Nut\sqrt{-1}/2+N\pi t)}}
  \right|
  \\
  =&
  \frac{2e^{-2N\pi t}}
  {\left|e^{-Nut\sqrt{-1}-2N\pi t}+1\right|}.
\end{split}
\end{equation*}
Since the denominator is bigger than $1$ if $Nut<\pi/2$ we have
\begin{equation*}
  |\tan(N\pi (-u/(2\pi)+\sqrt{-1})t))-\sqrt{-1}|
  <
  2e^{-2N\pi t}
\end{equation*}
when $t<\pi/(2Nu)$.
If $t\ge\pi/(2Nu)$, then the denominator is bigger than equal to $1-e^{-2N\pi t}$.
So we have
\begin{equation*}
  |\tan(N\pi (-u/(2\pi)+\sqrt{-1})t))-\sqrt{-1}|
  \le
  \frac{2e^{-2N\pi t}}{1-e^{-2N\pi t}}
  \le
  \frac{2e^{-2N\pi t}}{1-e^{-\pi^2/u}}
\end{equation*}
when $t\ge\pi/(2Nu)$.
Therefore for any $0\le t\le 1$ we have
\begin{equation}\label{eq:I_{+,1}tan}
  |\tan(N\pi (-u/(2\pi)+\sqrt{-1})t)-\sqrt{-1}|
  <
  \frac{2e^{-2N\pi t}}{1-e^{-\pi^2/u}}.
\end{equation}
\par
So we have
\begin{equation}\label{eq:I_{+,1}integral}
  \left|I_{+,1}(N)\right|
  \le
  \frac{2}{1-e^{-\pi^2/u}}
  \int_{0}^{1}
  e^{-2N\pi t}
  \left|
    g_N\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t\right)
  \right|
  \,dt.
\end{equation}
\par
We estimate $|g_N((-u/(2\pi)+\sqrt{-1})t)|$.
\par
Since the function $g_N$ is not well-defined on the segment $(-u/(2\pi)+\sqrt{-1})t$ (Figure~\ref{fig:contour}), we need to consider the segment $(-u/(2\pi)+\sqrt{-1})t+\varepsilon)$ ($0\le t\le1$) instead for small $\varepsilon$.
(See the argument in \cite[Page~534]{Andersen/Hansen:JKNOT2006}.)
\par
From \eqref{eq:g_N} we have
\begin{equation*}
\begin{split}
  &g_{N}\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \exp
  \left[
    N\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \right]
  \\
  &
  \times
  \exp
  \left[
    I_{\gamma}
    \left(
      \pi-\sqrt{-1}u-\sqrt{-1}\frac{|\xi|^2t}{2\pi}+\sqrt{-1}\varepsilon\xi
    \right)
  \right.
  \\
  &\phantom{\times\exp\bigl[}
  \left.
    -
    I_{\gamma}
    \left(
      -\pi-\sqrt{-1}u+\sqrt{-1}\frac{|\xi|^2t}{2\pi}-\sqrt{-1}\varepsilon\xi
    \right)
  \right].
\end{split}
\end{equation*}
\par
From Lemma~\ref{lem:Lemma3}, there exist $A>0$ and $B>0$ such that $|I_{\gamma}(z)|\le 2A+B|\gamma|(1+e^{-\Im(z)R})$.
So we have
\begin{equation}\label{eq:I_{+,1}Phi}
\begin{split}
  &
  \left|
    g_{N}\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \right|
  \\
  \le&
  \exp
  \left[
    N\Re\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \right]
  \frac{\exp\left(2A+B|\gamma|(1+e^{(u+|\xi|^2t/(2\pi)-\varepsilon u)R}\right)}
       {\exp\left(2A+B|\gamma|(1+e^{(u-|\xi|^2t/(2\pi)+\varepsilon u)R}\right)}
  \\
  \le&
  \exp
  \left[
    N\Re\Phi\left(\left(-\frac{ut}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \right]
  \exp\left(2A+B|\gamma|(1+e^{(u+|\xi|^2/(2\pi)-\varepsilon u)R}\right)
\end{split}
\end{equation}
for $0\le t\le1$.
\par
Now we want to estimate $\Re\Phi\bigl((-ut/(2\pi)+\sqrt{-1})t+\varepsilon\bigr)$.
\par
From the definition we have
\begin{multline*}
  \Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u+|\xi|^2t/(2\pi)-\varepsilon\xi})
    -
    \Li_2(e^{u-|\xi|^2t/(2\pi)+\varepsilon\xi})
  \right)
  +\frac{u^2t}{2\pi}-\sqrt{-1}ut-\varepsilon u.
\end{multline*}
Since we may assume that $\Re(u+|\xi|^2t/(2\pi)-\xi\varepsilon)=(1-\varepsilon)u+|\xi|^2t/(2\pi)>0$, there are two cases to consider; the case where $u-|\xi|^2t/(2\pi)<0$ and the case where $u-|\xi|^2t/(2\pi)\ge0$.
\par
If $|z|>1$, it is convenient to replace $\Li_2(z)$ with $\Li_2(z^{-1})$ using the following well-known formula.
\begin{equation}\label{eq:dilog}
  \Li_2(z)+\Li_2(z^{-1})
  =
  -\frac{\pi^2}{6}-\frac{1}{2}\bigl(\log(-z)\bigr)^2,
\end{equation}
where we choose a branch of $\log(-z)$ so that $-\pi<\Im\log(-z)<\pi$.
\begin{itemize}
\item The case where $u-|\xi|^2t/(2\pi)<0$.
We choose $\varepsilon$ small enough so that $u-|\xi|^2t/(2\pi)+\varepsilon u<0$.
From \eqref{eq:dilog} we have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(\vphantom{
          \left(u+\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\sqrt{-1}\pi\right)^2}
    -
    \Li_2(e^{-u-|\xi|^2t/(2\pi)+\varepsilon\xi})
    -
    \Li_2(e^{u-|\xi|^2t/(2\pi)+\varepsilon\xi})
  \right.
  \\
  &
  \left.\quad
    -\frac{\pi^2}{6}
    -\frac{1}{2}
    \left(
      u+\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\sqrt{-1}\pi
    \right)^2
  \right)
  \\
  &+\frac{u^2t}{2\pi}-\sqrt{-1}ut-\varepsilon u
  \\
  =&
  \frac{1}{\xi}
  \left(
    -
    \Li_2(e^{u-|\xi|^2t/(2\pi)+\xi\varepsilon})
    -
    \Li_2(e^{u-|\xi|^2t/(2\pi)+\xi\varepsilon})
  \right)
  \\
  &-\frac{\pi^2}{6\xi}
  -\frac{1}{2\xi}
  \left(
    u+\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\sqrt{-1}\pi
  \right)^2
  \\
  &+\frac{u^2t}{2\pi}-\sqrt{-1}ut-\varepsilon u,
\end{split}
\end{equation*}
where in the first equality we choose the sign of $\sqrt{-1}\pi$ so that $\Im(u+|\xi|^2t/(2\pi)-\varepsilon\xi+\pi\sqrt{-1})=-\varepsilon u+\pi$ is between $-\pi$ and $\pi$.
Since the dilogarithm function $\Li(z)$ is analytic when $\Re(z)<1$, we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    -
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
    -
    \Li_2(e^{u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &-\frac{\pi^2}{6\xi}
  -\frac{1}{2\xi}
  \left(
    u+\frac{|\xi|^2t}{2\pi}+\sqrt{-1}\pi
  \right)^2
  +\frac{u^2t}{2\pi}-\sqrt{-1}ut.
\end{split}
\end{equation*}
Since $\Li_2(z)$ is real when $z$ is real and $z<1$, we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Re\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  -\frac{u}{|\xi|^2}
  \left(
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &-\frac{u\pi^2}{6|\xi|^2}
  -\frac{u}{2|\xi|^2}
  \left(
    u+\frac{|\xi|^2t}{2\pi}
  \right)^2
  +
  \frac{u\pi^2}{2|\xi|^2}
  -
  \frac{4\pi(u+|\xi|^2t/(2\pi))\pi}{2|\xi|^2}
  +\frac{u^2t}{2\pi}
  \\
  =&
  -\frac{u}{|\xi|^2}
  \left(
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &-\frac{5u\pi^2}{6|\xi|^2}
  -\frac{u^3}{2|\xi|^2}
  -\frac{u|\xi|^2t^2}{8\pi^2}
  -\pi t
  \\
  <&0
\end{split}
\end{equation*}
if $u>0$.
\item The case where $u-|\xi|^2t/(2\pi)\ge0$.
In this case we have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \vphantom{\left(\frac{|\xi|^2t}{2\pi}\right)^2}
    -
    \Li_2(e^{-u-|\xi|^2t/(2\pi)+\varepsilon\xi})
    +
    \Li_2(e^{-u+|\xi|^2t/(2\pi)-\varepsilon\xi})
  \right.
  \\
  &\left.\quad
    -\frac{1}{2}
    \left(
      u+\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\pi\sqrt{-1}
    \right)^2
    +\frac{1}{2}
    \left(
      u-\frac{|\xi|^2t}{2\pi}+\varepsilon\xi-\pi\sqrt{-1}
    \right)^2
  \right)
  \\
  &+
  \frac{u^2t}{2\pi}-\sqrt{-1}ut-u\varepsilon
  \\
  =&
  \frac{1}{\xi}
  \left(
    \vphantom{\left(\frac{|\xi|^2t}{2\pi}\right)^2}
    -
    \Li_2(e^{-u-|\xi|^2t/(2\pi)+\varepsilon\xi})
    +
    \Li_2(e^{-u+|\xi|^2t/(2\pi)-\varepsilon\xi})
  \right)
  \\
  &
  -\frac{2u}{\xi}
  \left(
    \frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\pi\sqrt{-1}
  \right)
  +
  \frac{u^2t}{2\pi}-\sqrt{-1}ut-u\varepsilon
\end{split}
\end{equation*}
and so we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Re\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    -
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-u+|\xi|^2t/(2\pi)})
  \right)
  \\
  &
  -\Re
  \left(
    \frac{2u}{\xi}
    \left(
      \frac{|\xi|^2t}{2\pi}+\pi\sqrt{-1}
    \right)
  \right)
  +
  \frac{u^2t}{2\pi}  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    -
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-u+|\xi|^2t/(2\pi)})
  \right)
  -\frac{4\pi^2u}{|\xi|^2}-\frac{u^2t}{2\pi}
  \\
  <&0
\end{split}
\end{equation*}
if $u>0$.
\end{itemize}
Therefore for any $t$ we have $\Re\Phi\bigl((-u/(2\pi)+\sqrt{-1})t+\varepsilon\bigr)\le0$ for small $\varepsilon>0$.
\par
So from \eqref{eq:I_{+,1}integral} and \eqref{eq:I_{+,1}Phi} we have
\begin{equation*}
\begin{split}
  \left|I_{+,1}(N)\right|
  &\le
  \frac{2}{1-e^{-\pi^2/u}}
  \exp\left(2A+B|\gamma|(1+e^{(u+|\xi|^2/(2\pi)-\varepsilon u)R}\right)
  \int_{0}^{1}e^{-2N\pi t}\,dt
  \\
  &=
  \frac{1-e^{-2N\pi}}{N\pi(1-e^{-\pi^2/u})}
  \exp\left(2A+B|\gamma|(1+e^{(u+|\xi|^2/(2\pi))R}\right)
  \\
  &<
  \frac{K_{+,1}}{N}
\end{split}
\end{equation*}
for a positive constant $K_{+,1}$.
\end{proof}

\begin{proof}[Proof of \eqref{eq:I_{-,1}}]
Since $\tan$ is an odd function we have from \eqref{eq:I_{+,1}tan}
\begin{equation}\label{eq:I_{-,1}tan}
  |\tan\bigl(N\pi(u/(2\pi)-\sqrt{-1})t\bigr)+\sqrt{-1}|
  <
  \frac{2e^{-2N\pi t}}{1-e^{-\pi^2/u}}
\end{equation}
for any $0\le t\le 1$.
\par
So we have
\begin{equation}\label{eq:I_{-,1}integral}
  \left|I_{-,1}(N)\right|
  \le
  \frac{2}{1-e^{-\pi^2/u}}
  \int_{0}^{1}
  e^{-2N\pi t}
  \left|
    g_N\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t\right)
  \right|
  \,dt.
\end{equation}
\par
We estimate $|g_N((u/(2\pi)-\sqrt{-1})t)|$.
\par
As in the case of $I_{+,1}$ we need to calculate $g_N(g_N((u/(2\pi)-\sqrt{-1})t)+\varepsilon)$.
\par
From \eqref{eq:g_N} we have
\begin{equation*}
\begin{split}
  &g_{N}\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \exp
  \left[
    N\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \right]
  \\
  &
  \times
  \exp
  \left[
    I_{\gamma}
    \left(
      \pi-\sqrt{-1}u+\sqrt{-1}\frac{|\xi|^2t}{2\pi}+\sqrt{-1}\varepsilon\xi
    \right)
  \right.
  \\
  &\phantom{\times\exp\bigl[}
  \left.
    -
    I_{\gamma}
    \left(
      -\pi-\sqrt{-1}u-\sqrt{-1}\frac{|\xi|^2t}{2\pi}-\sqrt{-1}\varepsilon\xi
    \right)
  \right].
\end{split}
\end{equation*}
\par
From Lemma~\ref{lem:Lemma3}, there exist $A>0$ and $B>0$ such that $|I_{\gamma}(z)|\le 2A+B|\gamma|(1+e^{-\Im(z)R})$.
So we have
\begin{equation}\label{eq:I_{-,1}Phi}
\begin{split}
  &
  \left|
    g_{N}\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \right|
  \\
  \le&
  \exp
  \left[
    N\Re\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \right]
  \frac{\exp\left(2A+B|\gamma|(1+e^{(u-|\xi|^2t/(2\pi)-\varepsilon u)R}\right)}
       {\exp\left(2A+B|\gamma|(1+e^{(u+|\xi|^2t/(2\pi)+\varepsilon u)R}\right)}
  \\
  \le&
  \exp
  \left[
    N\Re\Phi\left(\left(\frac{ut}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \right]
  \exp\left(2A+B|\gamma|(1+e^{(u-|\xi|^2/(2\pi)-\varepsilon u)R}\right)
\end{split}
\end{equation}
for $0\le t\le1$.
\par
Now we want to estimate $\Re\Phi\bigl((ut/(2\pi)-\sqrt{-1})t+\varepsilon\bigr)$.
\par
From the definition we have
\begin{multline*}
  \Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u-|\xi|^2t/(2\pi)-\varepsilon\xi})
    -
    \Li_2(e^{u+|\xi|^2t/(2\pi)+\varepsilon\xi})
  \right)
  -\frac{u^2t}{2\pi}+\sqrt{-1}ut-\varepsilon u.
\end{multline*}
Since $\Re(u+|\xi|^2t/(2\pi)+\varepsilon\xi)=(1+\varepsilon)u+|\xi|^2t/(2\pi)>0$, there are two cases to consider; the case where $u-|\xi|^2t/(2\pi)<0$ and the case where $u-|\xi|^2t/(2\pi)\ge0$.
\begin{itemize}
\item The case where $u-|\xi|^2t/(2\pi)\le0$.
In this case we have $u-|\xi|^2t/(2\pi)-\varepsilon u<0$.
From \eqref{eq:dilog} we have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(\vphantom{
          \left(u+\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\sqrt{-1}\pi\right)^2}
    \Li_2(e^{u-|\xi|^2t/(2\pi)-\varepsilon\xi})
    +
    \Li_2(e^{-u-|\xi|^2t/(2\pi)-\varepsilon\xi})
  \right.
  \\
  &
  \left.\quad
    +\frac{\pi^2}{6}
    +\frac{1}{2}
    \left(
      u+\frac{|\xi|^2t}{2\pi}+\varepsilon\xi-\sqrt{-1}\pi
    \right)^2
  \right)
  \\
  &-\frac{u^2t}{2\pi}+\sqrt{-1}ut-\varepsilon u
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u-|\xi|^2t/(2\pi)-\xi\varepsilon})
    +
    \Li_2(e^{-u-|\xi|^2t/(2\pi)-\xi\varepsilon})
  \right)
  \\
  &+\frac{\pi^2}{6\xi}
  +\frac{1}{2\xi}
  \left(
    u+\frac{|\xi|^2t}{2\pi}+\varepsilon\xi-\sqrt{-1}\pi
  \right)^2
  \\
  &-\frac{u^2t}{2\pi}+\sqrt{-1}ut-\varepsilon u.
\end{split}
\end{equation*}
Therefore we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &+\frac{\pi^2}{6\xi}
  +\frac{1}{2\xi}
  \left(
    u+\frac{|\xi|^2t}{2\pi}-\sqrt{-1}\pi
  \right)^2
  \\
  &-\frac{u^2t}{2\pi}+\sqrt{-1}ut
\end{split}
\end{equation*}
and so
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Re\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    \Li_2(e^{u-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &+\frac{u\pi^2}{6|\xi|^2}
  +\frac{u}{2|\xi|^2}
  \left(
    u+\frac{|\xi|^2t}{2\pi}
  \right)^2
  -
  \frac{u\pi^2}{2|\xi|^2}
  -
  \frac{4\pi(u+|\xi|^2t/(2\pi))\pi}{2|\xi|^2}
  -\frac{u^2t}{2\pi}
  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    \Li_2(e^{u-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &-\frac{7u\pi^2}{3|\xi|^2}
  +\frac{u^3}{2|\xi|^2}
  +\frac{u|\xi|^2t^2}{8\pi^2}
  -\pi t
  \\
  =&
  -2\frac{u\pi^2}{|\xi|^2}
  +\frac{u^3}{2|\xi|^2}
  +\frac{u|\xi|^2t^2}{8\pi^2}
  -\pi t
\end{split}
\end{equation*}
since $\Li_2(z)\le\pi^2/6$ for $0<z\le1$.
We can easily prove
\begin{equation*}
  -2\frac{u\pi^2}{|\xi|^2}
  +\frac{u^3}{2|\xi|^2}
  +\frac{u|\xi|^2t^2}{8\pi^2}
  -\pi t
  <
  \pi t
\end{equation*}
when $0<u<1$ and $2u\pi/|\xi|^2\le t\le1$.
So we have
\begin{equation*}
  \lim_{\varepsilon\searrow0}
  \Re\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  <\pi t
\end{equation*}
in this case.
\item The case where $u-|\xi|^2t/(2\pi)>0$.
We choose $\varepsilon$ so that $u-|\xi|^2t/(2\pi)-\varepsilon u>0$.
In this case we have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \vphantom{\left(\frac{|\xi|^2t}{2\pi}\right)^2}
    -
    \Li_2(e^{-u+|\xi|^2t/(2\pi)+\varepsilon\xi})
    +
    \Li_2(e^{-u-|\xi|^2t/(2\pi)-\varepsilon\xi})
  \right.
  \\
  &\left.\quad
    -\frac{1}{2}
    \left(
      u-\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\pi\sqrt{-1}
    \right)^2
    +\frac{1}{2}
    \left(
      -u-\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\pi\sqrt{-1}
    \right)^2
  \right)
  \\
  &-
  \frac{u^2t}{2\pi}+\sqrt{-1}ut-\varepsilon u
\end{split}
\end{equation*}
and so we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Re\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+\varepsilon\right)
  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    -
    \Li_2(e^{-u+|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-u-|\xi|^2t/(2\pi)})
  \right)
  +\frac{u^2t}{2\pi}-\frac{4u\pi^2}{|\xi|^2}
  \\
  <&
  \frac{u^2t}{2\pi}-\frac{23u\pi^2}{6|\xi|^2}
  <0
\end{split}
\end{equation*}
if $0<u<1$ and $0\le t<2u\pi/|\xi|^2$.
\end{itemize}
Therefore for any $0\le t\le1$ we have $\Re\Phi\bigl((u/(2\pi)-\sqrt{-1})t+\varepsilon\bigr)\le\pi t$ for small $\varepsilon>0$.
\par
So from \eqref{eq:I_{-,1}integral} and \eqref{eq:I_{-,1}Phi} we have
\begin{equation*}
\begin{split}
  \left|I_{-,1}(N)\right|
  &\le
  \frac{2}{1-e^{-\pi^2/u}}
  \exp\left(2A+B|\gamma|(1+e^{(u-|\xi|^2/(2\pi))R}\right)
  \int_{0}^{1}e^{-N\pi t}\,dt
  \\
  &=
  \frac{2(1-e^{-N\pi})}{N(1-e^{-\pi^2/u})}
  \exp\left(2A+B|\gamma|(1+e^{(u-|\xi|^2/(2\pi))R}\right)
  \\
  &<
  \frac{K_{-,1}}{N}
\end{split}
\end{equation*}
for a positive constant $K_{-,1}$.
\end{proof}

\begin{proof}[Proof of \eqref{eq:I_{+,3}}]
Since $\tan$ has period $\pi$ we have
\begin{equation}\label{eq:tan_I+3}
  |\tan(N\pi (-u/(2\pi)+\sqrt{-1})t)-\sqrt{-1}|
  <
  \frac{2e^{-2N\pi t}}{1-e^{-\pi^2/u}}
\end{equation}
from \eqref{eq:I_{+,1}tan}
\par
From \eqref{eq:tan_I+3} we have
\begin{equation}\label{eq:I_{+,3}integral}
  \left|I_{+,3}(N)\right|
  \le
  \frac{2}{1-e^{-\pi^2/u}}
  \int_{0}^{1}
  e^{-2N\pi t}
  \left|
    g_N\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1\right)
  \right|
  \,dt.
\end{equation}
\par
As in the case of $I_{+,1}(N)$ we consider the integral on the segment $(-u/(2\pi)+\sqrt{-1})t+1-\varepsilon$ ($0\le t\le1$) for small $\varepsilon$.
\par
We estimate $\Phi\bigl((-u/(2\pi)+\sqrt{-1})t+1-\varepsilon\bigr)$.
We have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u+|\xi|^2t/(2\pi)-(1-\varepsilon)\xi})
    -
    \Li_2(e^{u-|\xi|^2t/(2\pi)+(1-\varepsilon)\xi})
  \right)
  \\
  &+\frac{u^2t}{2\pi}-\sqrt{-1}ut-(1-\varepsilon)u.
\end{split}
\end{equation*}
Since we may assume that $\Re(u+|\xi|^2t/(2\pi)-(1-\varepsilon)\xi)=\varepsilon u+|\xi|^2t/(2\pi)>0$, there are two cases to consider; the case where $2u-|\xi|^2t/(2\pi)\le0$ and the case where $2u-|\xi|^2t/(2\pi)>0$.
\begin{itemize}
\item $2u-|\xi|^2t/(2\pi)\le0$.
In this case, since $u-|\xi|^2t/(2\pi)+(1-\varepsilon)u<0$, from \eqref{eq:dilog} we have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
  \vphantom{
    \left(
      u+\frac{|\xi|^2t}{2\pi}-(1-\varepsilon)\xi+\pi\sqrt{-1}
    \right)^2}
    -
    \Li_2(e^{-u-|\xi|^2t/(2\pi)+(1-\varepsilon)\xi})
    -
    \Li_2(e^{u-|\xi|^2t/(2\pi)+(1-\varepsilon)\xi})
  \right.
  \\
  &
  \quad
  \left.
    -\frac{\pi^2}{6}
    -\frac{1}{2}
    \left(
      u+\frac{|\xi|^2t}{2\pi}-(1-\varepsilon)\xi+\pi\sqrt{-1}
    \right)^2
  \right)
  \\
  &+\frac{u^2t}{2\pi}-\sqrt{-1}ut-(1-\varepsilon)u
\end{split}
\end{equation*}
Since the dilogarithm function $\Li(z)$ is analytic when $\Re(z)<1$, we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    -
    \Li_2(e^{-|\xi|^2t/(2\pi)})
    -
    \Li_2(e^{2u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &-\frac{\pi^2}{6\xi}
  -\frac{1}{2\xi}
  \left(
    \frac{|\xi|^2t}{2\pi}-\pi\sqrt{-1}
  \right)^2
  \\
  &+\frac{u^2t}{2\pi}-\sqrt{-1}ut-u.
\end{split}
\end{equation*}
So we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Re\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  -\frac{u}{|\xi|^2}
  \left(
    \Re\Li_2(e^{-|\xi|^2t/(2\pi)})
    +
    \Re\Li_2(e^{2u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &-\frac{u\pi^2}{6|\xi|^2}
  -\frac{u}{2|\xi|^2}
   \frac{|\xi|^4t^2}{4\pi^2}
  +
  \frac{u\pi^2}{2|\xi|^2}
  -
  \frac{4\pi|\xi|^2t/(2\pi)\pi}{2|\xi|^2}
  +
  \frac{u^2t}{2\pi}
  -u
  \\
  =&
  -\frac{u}{|\xi|^2}
  \left(
    \Re\Li_2(e^{-|\xi|^2t/(2\pi)})
    +
    \Re\Li_2(e^{2u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &+\frac{u\pi^2}{3|\xi|^2}
  -\frac{u|\xi|^2t^2}{8\pi^2}
  -\pi t
  +\frac{u^2t}{2\pi}
  -u
  \le0.
\end{split}
\end{equation*}
The last inequality follows since $\frac{u\pi^2}{3|\xi|^2}
  -\frac{u|\xi|^2t^2}{8\pi^2}
  -\pi t
  +\frac{u^2t}{2\pi}
  -u$,
is a quadratic function with respect to $u$ with non-positive maximum.
\item $2u-|\xi|^2t/(2\pi)>0$.
In this case we may choose $\varepsilon$ small so that $u-|\xi|^2t/(2\pi)+(1-\varepsilon)u>0$.
Then we have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \vphantom{\left(\frac{|\xi|^2t}{2\pi}\right)^2}
    -
    \Li_2(e^{-u-|\xi|^2t/(2\pi)+(1-\varepsilon)\xi})
    +
    \Li_2(e^{-u+|\xi|^2t/(2\pi)-(1-\varepsilon)\xi})
  \right.
  \\
  &\left.
    -\frac{1}{2}
    \left(
      u+\frac{|\xi|^2t}{2\pi}-(1-\varepsilon)\xi+\pi\sqrt{-1}
    \right)^2
    +\frac{1}{2}
    \left(
      u-\frac{|\xi|^2t}{2\pi}+(1-\varepsilon)\xi-\pi\sqrt{-1}
    \right)^2
  \right)
  \\
  &+
  \frac{u^2t}{2\pi}-\sqrt{-1}ut-(1-\varepsilon)u
\end{split}
\end{equation*}
and so we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Re\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    -
    \Li_2(e^{-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-2u+|\xi|^2t/(2\pi)})
  \right)
  +\frac{2u^3}{|\xi|^2}
  -\frac{u^2t}{2\pi}
  +\frac{4\pi^2u}{|\xi|^2}
  -u.
\end{split}
\end{equation*}
Putting $s:=|\xi|^2t/(2\pi)$ and consider the function
\begin{equation*}
\begin{split}
  f(u,s)
  &:=
  -
  \Li_2(e^{-s})
  +
  \Li_2(e^{-2u+s})
  +2u^2
  -us
  +4\pi^2
  -|\xi|^2
  -\frac{2\pi^2s}{u}
  \\
  &=
  -
  \Li_2(e^{-s})
  +
  \Li_2(e^{-2u+s})
  +u^2
  -us-\frac{2\pi^2s}{u}
\end{split}
\end{equation*}
so that
\begin{equation*}
  \frac{u}{|\xi|^2}f\left(u,\frac{|\xi|^2t}{2\pi}\right)
  =
  \lim_{\varepsilon\searrow0}
  \Re\Phi\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1-\varepsilon\right)
  -\pi t.
\end{equation*}
\end{itemize}
\par
We will show $f(u,s)\le0$ for $0\le s<2u\le2$.
\par
We have
\begin{equation*}
  \exp\left[-\frac{\partial\,f(u,t)}{\partial\,t}\right]
  =
  2e^{2\pi^2/u}
  \left(
    \cosh(u)-\cosh(s-u)
  \right).
\end{equation*}
Therefore it can be shown that for fixed $u$, $f(u,s)$ is increasing for $0\le s<u-\arccosh(\cosh(u)-\exp(-2\pi^2/u)/2)$, decreasing for $u-\arccosh(\cosh(u)-\exp(-2\pi^2/u)/2)<s<u+\arccosh(\cosh(u)-\exp(-2\pi^2/u)/2)$, and increasing for $u+\arccosh(\cosh(u)-\exp(-2\pi^2/u)/2)<s<u$.
Since a graph of $f\bigl(u,u-\arccosh(\cosh(u)-\exp(-2\pi^2/u)/2)\bigr)$ looks as Figure~\ref{fig:graph} and
\begin{equation*}
  f(u,2u)
  =
  -\frac{23\pi^2}{6}
  -u^2
  -\Li_2(e^{-2u})
  <0,
\end{equation*}
we see $f(u,s)\le0$.
\begin{figure}[h]
  \includegraphics[scale=0.7]{graph.eps}
  \caption{A graph of $f\bigl(u,u-\arccosh(\cosh(u)-\exp(-4\pi^2/u)/2)\bigr)$.}
  \label{fig:graph}
\end{figure}
\par
Therefore we finally have
\begin{equation*}
\begin{split}
  |I_{+,3}(N)|
  &<
  \frac{2}{1-e^{-\pi^2/u}}
  \exp\left(2A+B(1+e^{(u+|\xi|^2/(2\pi))R})|\gamma|\right)
  \int_{4\pi u/|\xi|^2}^{1}
  e^{-2N\pi t}\,dt
  \\
  &=
  \frac{e^{-8N\pi^2u/|\xi|^2}-e^{-2N\pi}}{N\pi(1-e^{-\pi^2/u})}
  \exp\left(2A+B(1+e^{(u+|\xi|^2/(2\pi))R})|\gamma|\right)
  \\
  &<
  \frac{K_{+,3}}{N}
\end{split}
\end{equation*}
for a positive constant $K_{+,3}$.
\end{proof}

\begin{proof}[Proof of \eqref{eq:I_{-,3}}]
Since $\tan$ has period $\pi$ we have
\begin{equation}\label{eq:tan_I-3}
  |\tan(N\pi((u/(2\pi)-\sqrt{-1})t+1)+\sqrt{-1}|
  <
  \frac{2e^{-2N\pi t}}{1-e^{-\pi^2/u}}
\end{equation}
from \eqref{eq:I_{+,1}tan}
\par
From \eqref{eq:tan_I-3} we have
\begin{equation}\label{eq:I_{-,3}integral}
  \left|I_{-,3}(N)\right|
  \le
  \frac{2}{1-e^{-\pi^2/u}}
  \int_{0}^{1}
  e^{-2N\pi t}
  \left|
    g_N\left(\left(-\frac{u}{2\pi}+\sqrt{-1}\right)t+1\right)
  \right|
  \,dt.
\end{equation}
\par
As in the case of $I_{+,1}(N)$ we consider the integral on the segment $(u/(2\pi)-\sqrt{-1})t+1-\varepsilon$ ($0\le t\le1$) for small $\varepsilon$.
\par
We estimate $\Phi\bigl((u/(2\pi)-\sqrt{-1})t+1-\varepsilon\bigr)$.
We have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u-|\xi|^2t/(2\pi)-(1-\varepsilon)\xi})
    -
    \Li_2(e^{u+|\xi|^2t/(2\pi)+(1-\varepsilon)\xi})
  \right)
  \\
  &-\frac{u^2t}{2\pi}+\sqrt{-1}ut-(1-\varepsilon)u.
\end{split}
\end{equation*}
We will calculate $\lim_{\varepsilon\searrow0}\Phi\bigl((u/(2\pi)-\sqrt{-1})t+1-\varepsilon\bigr)$.
\par
Note that $\Re(u+|\xi|^2t/(2\pi)+(1-\varepsilon)\xi)=2u+|\xi|^2t/(2\pi)-\varepsilon u>0$ for small $\varepsilon$.
Since $\Re(u-|\xi|^2t/(2\pi)-(1-\varepsilon)\xi)=-|\xi|^2t/(2\pi)+\varepsilon u$, if $t>0$ we assume that $\Re(u-|\xi|^2t/(2\pi)-(1-\varepsilon)\xi)<0$.
Therefore we assume that $t>0$.
\par
In this case from \eqref{eq:dilog} we have
\begin{equation*}
\begin{split}
  &\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{-|\xi|^2t/(2\pi)+\varepsilon\xi})
    +
    \Li_2(e^{-2u-|\xi|^2t/(2\pi)+\varepsilon\xi})
  \right)
  \\
  &
  +\frac{\pi^2}{6\xi}
  +\frac{1}{2\xi}
  \left(
    2u+\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\pi\sqrt{-1}
  \right)^2
  \\
  &-\frac{u^2t}{2\pi}+\sqrt{-1}ut-(1-\varepsilon)u
\end{split}
\end{equation*}
and
\begin{equation*}
\begin{split}
  &\Re\Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{-|\xi|^2t/(2\pi)+\varepsilon\xi})
    +
    \Li_2(e^{-2u-|\xi|^2t/(2\pi)+\varepsilon\xi})
  \right)
  \\
  &
  +\frac{\pi^2}{6\xi}
  +\frac{1}{2\xi}
  \left(
    2u+\frac{|\xi|^2t}{2\pi}-\varepsilon\xi+\pi\sqrt{-1}
  \right)^2
  \\
  &-\frac{u^2t}{2\pi}+\sqrt{-1}ut-(1-\varepsilon)u.
\end{split}
\end{equation*}
So we have
\begin{equation*}
\begin{split}
  &\lim_{\varepsilon\searrow0}
  \Phi\left(\left(\frac{u}{2\pi}-\sqrt{-1}\right)t+1-\varepsilon\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-2u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &
  +\frac{\pi^2}{6\xi}
  +\frac{1}{2\xi}
  \left(
    2u+\frac{|\xi|^2t}{2\pi}+\pi\sqrt{-1}
  \right)^2
  \\
  &-\frac{u^2t}{2\pi}+\sqrt{-1}ut-u
  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    \Li_2(e^{-|\xi|^2t/(2\pi)})
    +
    \Li_2(e^{-2u-|\xi|^2t/(2\pi)})
  \right)
  \\
  &+\frac{u\pi^2}{6|\xi|^2}
  +
  \frac{u}{2|\xi|^2}
  \left(
    2u+\frac{|\xi|^2t}{2\pi}
  \right)^2
  -
  \frac{u\pi^2}{2|\xi|^2}
  +
  \frac{4\pi^2}{2|\xi|^2}
  \left(
    2u+\frac{|\xi|^2t}{2\pi}
  \right)
  -
  \frac{u^2t}{2\pi}
  -u
  \\
  \le
  &\frac{11u\pi^2}{3|\xi|^2}
  +\frac{2u^3}{|\xi|^2}
  +\frac{u|\xi|^2t^2}{8\pi^2}
  +\pi t
  +\frac{u^2t}{2\pi}
  -u
  <\frac{3}{2}\pi t
\end{split}
\end{equation*}
if $0<u<1$ and $0<t\le1$.
\par
Therefore we finally have
\begin{equation*}
\begin{split}
  |I_{-,3}(N)|
  &<
  \frac{2}{1-e^{-\pi^2/u}}
  \exp\left(2A+B(1+e^{(u+|\xi|^2/(2\pi))R})|\gamma|\right)
  \int_{0}^{1}
  e^{-N\pi t/2}
  \,dt
  \\
  &=
  \frac{4(1-e^{-N\pi/2})}{N\pi(1-e^{-\pi^2/u)}}
  \exp\left(2A+B(1+e^{(u+|\xi|^2/(2\pi))R})|\gamma|\right)
  \\
  &<
  \frac{K_{-,3}}{N}
\end{split}
\end{equation*}
for a positive constant $K_{-,3}$.
\end{proof}

\begin{proof}[Proof of \eqref{eq:I_{+,2}}]
From \cite[Equation~(4.6)]{Andersen/Hansen:JKNOT2006} we have
\begin{equation*}
  |I_{+,2}(N)|
  \le
  4e^{-2\pi N}
  \int_{\varepsilon}^{1-\varepsilon}|g_N(-u/(2\pi)+\sqrt{-1}+t)|\,dt.
\end{equation*}
From \eqref{eq:g_N} we have
\begin{multline*}
  |g_N(-u/(2\pi)+\sqrt{-1}+t)|
  \\
  \le
  \exp\bigl(N\Re(\Phi(-u/(2\pi)+\sqrt{-1}+t))\bigr)
  \exp\bigl(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)})\bigr).
\end{multline*}
\par
Now estimate $\Re(\Phi(-u/(2\pi)+\sqrt{-1}+t))$.
We have
\begin{equation*}
\begin{split}
  &\Phi\left(-\frac{u}{2\pi}+\sqrt{-1}+t\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u+|\xi|^2/(2\pi)-\xi t})
    -
    \Li_2(e^{u-|\xi|^2/(2\pi)+\xi t})
  \right)
  +\frac{u^2}{2\pi}-\sqrt{-1}u-ut.
\end{split}
\end{equation*}
Since $\Re(u+|\xi|^2/(2\pi)-\xi t)=u(1-t)+|\xi|^2/(2\pi)>0$ and $\Re(u-|\xi|^2/(2\pi)+\xi t)=u(1+t)-|\xi|^2/(2\pi)\le0$, we have
\begin{equation*}
\begin{split}
  &\Phi\left(-\frac{u}{2\pi}+\sqrt{-1}+t\right)
  \\
  =&
  -\frac{1}{\xi}
  \left(
    \Li_2(e^{u+|\xi|^2/(2\pi)-\xi t})
    +
    \Li_2(e^{u-|\xi|^2/(2\pi)+\xi t})
  \right)
  \\
  &
  -\frac{\pi^2}{6\xi}
  -\frac{1}{2\xi}
  \left(
    u+\frac{|\xi|^2}{2\pi}-(u+2\pi\sqrt{-1})t+\pi\sqrt{-1}
  \right)^2
  +\frac{u^2}{2\pi}-\sqrt{-1}u-ut
\end{split}
\end{equation*}
from \eqref{eq:dilog}.
Therefore we have
\begin{equation*}
\begin{split}
  &\Re\Phi\left(-\frac{u}{2\pi}+\sqrt{-1}+t\right)
  \\
  =&
  -\frac{u}{|\xi|^2}
  \left(
    \Re\Li_2(e^{u+|\xi|^2/(2\pi)-\xi t})
    +
    \Re\Li_2(e^{u-|\xi|^2/(2\pi)+\xi t})
  \right)
  \\
  &-\frac{2\pi}{|\xi|^2}
  \left(
    \Im\Li_2(e^{u+|\xi|^2/(2\pi)-\xi t})
    +
    \Im\Li_2(e^{u-|\xi|^2/(2\pi)+\xi t})
  \right)
  \\
  &
  +(2t-1)\pi
  -\frac{1}{2}(t^2+1)u
  +\frac{u^2t}{2\pi}
  -\frac{u^3}{8\pi^2}
  +\frac{\pi^2u}{3|\xi|^2}
  \\
  \le&
  -\frac{u}{|\xi|^2}
  \left(
    \Re\Li_2(e^{u+|\xi|^2/(2\pi)-\xi t})
    +
    \Re\Li_2(e^{u-|\xi|^2/(2\pi)+\xi t})
  \right)
  \\
  &-\frac{2\pi}{|\xi|^2}
  \left(
    \Im\Li_2(e^{u+|\xi|^2/(2\pi)-\xi t})
    +
    \Im\Li_2(e^{u-|\xi|^2/(2\pi)+\xi t})
  \right)
  \\
  &+(2t-1)\pi.
\end{split}
\end{equation*}
For $0<r<1$ and $0<\theta<2\pi$ we have
\begin{equation*}
\begin{split}
  \Re\Li_2(re^{\sqrt{-1}\theta})
  &=
  -\frac{1}{2}
  \int_{0}^{r}
  \frac{\log(1-2s\cos\theta+s^2)}{s}\,ds
  \ge
  -\frac{1}{2}
  \int_{0}^{r}
  \frac{\log(1+2s+s^2)}{s}\,ds
  \\
  &=
  -\int_{0}^{r}\frac{\log(1+s)}{s}\,ds
  \ge
  -\int_{0}^{1}\frac{\log(1+s)}{s}\,ds
  =
  \Li_2(-1)
  =
  -\frac{\pi^2}{12}.
\end{split}
\end{equation*}
We also have
\begin{equation*}
  \Im\Li_2(re^{\sqrt{-1}\theta})
  =
  -\int_{0}^{r}
  \frac{\arg(1-se^{\sqrt{-1}\theta})}{s}\,ds.
\end{equation*}
If $0<\theta\le\pi$ the right hand side is non-negative.
If $\pi<\theta<2\pi$ we have
\begin{equation*}
\begin{split}
  \Im\Li_2(re^{\sqrt{-1}\theta})
  &=
  -\int_{0}^{1}\frac{\arg(1-se^{\sqrt{-1}\theta})}{s}\,ds
  +
  \int_{r}^{1}
  \frac{\arg(1-se^{\sqrt{-1}\theta})}{s}\,ds
  \\
  &=
  \Im\Li_2(e^{\sqrt{-1}\theta})
  +
  \int_{r}^{1}
  \frac{\arg(1-se^{\sqrt{-1}\theta})}{s}\,ds.
\end{split}
\end{equation*}
The second integral is positive and $\Im\Li_2(e^{\sqrt{-1}\theta})$ is bigger than or equal to $-\Im\Li_2(\exp(\sqrt{-1}\pi/3))=-1.01494\ldots$.
\par
Therefore we have
\begin{equation*}
  \Re\Phi\left(-\frac{u}{2\pi}+\sqrt{-1}+t\right)
  \le
  \frac{\pi^2u}{6|\xi|^2}
  +
  \frac{2\pi\Im\Li_2(e^{\sqrt{-1}\pi/3})}{|\xi|^2}
  +(2t-1)\pi
\end{equation*}
So we have
\begin{equation*}
\begin{split}
  &|I_{+,2}(N)|
  \\
  \le&
  4\exp(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)}))
  e^{-3\pi N}
  \\
  &\times
  \exp
  \left[
  N
  \left(
    \frac{\pi^2u}{6|\xi|^2}
    +
    \frac{2\pi\Im\Li_2(e^{\sqrt{-1}\pi/3})}{|\xi|^2}
  \right)
  \right]
  \int_{0}^{1}e^{2N\pi t}\,dt
  \\
  =&
  \frac{2(1-e^{-2\pi N})}{\pi N}
  \exp(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)}))
  \\
  &\times
  \exp
  \left[
  \pi N
  \left(
    \frac{\pi u}{6|\xi|^2}
    +
    \frac{2\Im\Li_2(e^{\sqrt{-1}\pi/3})}{|\xi|^2}
    -1
  \right)
  \right]
  \\
  <&
  \frac{2}{\pi N}
  \exp(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)}))
  \\
  <&
  \frac{K_{+,2}}{N}
\end{split}
\end{equation*}
for a positive constant $K_{+,2}$.
Here we use the inequality
\begin{equation*}
  \frac{\pi u}{6|\xi|^2}
  +
  \frac{2\Im\Li_2(e^{\sqrt{-1}\pi/3})}{|\xi|^2}
  -1
  <
  \frac{\pi}{6}
  +\frac{1.01494\ldots}{2\pi^2}
  -1
  <0.
\end{equation*}
\end{proof}

\begin{proof}[Proof of \eqref{eq:I_{-,2}}]
From \cite[Equation~(4.6)]{Andersen/Hansen:JKNOT2006} we have
\begin{equation*}
  |I_{-,2}(N)|
  \le
  4e^{-2\pi N}
  \int_{\varepsilon}^{1-\varepsilon}|g_N(u/(2\pi)-\sqrt{-1}+t)|\,dt.
\end{equation*}
From \eqref{eq:g_N} we have
\begin{multline*}
  |g_N(u/(2\pi)-\sqrt{-1}+t)|
  \\
  \le
  \exp\bigl(N\Re(\Phi(u/(2\pi)-\sqrt{-1}+t))\bigr)
  \exp\bigl(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)})\bigr).
\end{multline*}
\par
Now estimate $\Re(\Phi(u/(2\pi)-\sqrt{-1}+t))$.
We have
\begin{equation*}
\begin{split}
  &\Phi\left(\frac{u}{2\pi}-\sqrt{-1}+t\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u-|\xi|^2/(2\pi)-\xi t})
    -
    \Li_2(e^{u+|\xi|^2/(2\pi)+\xi t})
  \right)
  -\frac{u^2}{2\pi}+\sqrt{-1}u-ut.
\end{split}
\end{equation*}
Since $\Re(u-|\xi|^2/(2\pi)-\xi t)=u(1-t)-|\xi|^2/(2\pi)<0$ and $\Re(u+|\xi|^2/(2\pi)+\xi t)=u(1+t)+|\xi|^2/(2\pi)>0$, we have
\begin{equation*}
\begin{split}
  &\Phi\left(\frac{u}{2\pi}-\sqrt{-1}+t\right)
  \\
  =&
  \frac{1}{\xi}
  \left(
    \Li_2(e^{u-|\xi|^2/(2\pi)-\xi t})
    +
    \Li_2(e^{-u-|\xi|^2/(2\pi)-\xi t})
  \right)
  \\
  &
  +\frac{\pi^2}{6\xi}
  +\frac{1}{2\xi}
  \left(
    u+\frac{|\xi|^2}{2\pi}+(u+2\pi\sqrt{-1})t-\pi\sqrt{-1}
  \right)^2
  -\frac{u^2}{2\pi}+\sqrt{-1}u-ut
\end{split}
\end{equation*}
from \eqref{eq:dilog}.
Therefore we have
\begin{equation*}
\begin{split}
  &\Re\Phi\left(\frac{u}{2\pi}-\sqrt{-1}+t\right)
  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    \Re\Li_2(e^{u-|\xi|^2/(2\pi)-\xi t})
    +
    \Re\Li_2(e^{-u-|\xi|^2/(2\pi)-\xi t})
  \right)
  \\
  &
  +
  \frac{2\pi}{|\xi|^2}
  \left(
    \Im\Li_2(e^{u-|\xi|^2/(2\pi)-\xi t})
    +
    \Im\Li_2(e^{-u-|\xi|^2/(2\pi)-\xi t})
  \right)
  \\
  &
  +\frac{u\pi^2}{6|\xi|^2}-\frac{u^2}{2\pi}-ut
  \\
  &
  +\frac{u}{2|\xi|^2}
  \left(
    \left(
    u+\frac{|\xi|^2}{2\pi}+ut
    \right)^2
    -
    \pi^2(2t-1)^2
  \right)
  \\
  &
  +
  \frac{4\pi}{2|\xi|^2}
  \pi(2t-1)
  \left(
    u+\frac{|\xi|^2}{2\pi}+ut
  \right)
  \\
  =&
  \frac{u}{|\xi|^2}
  \left(
    \Re\Li_2(e^{u-|\xi|^2/(2\pi)-\xi t})
    +
    \Re\Li_2(e^{-u-|\xi|^2/(2\pi)-\xi t})
  \right)
  \\
  &
  +
  \frac{2\pi}{|\xi|^2}
  \left(
    \Im\Li_2(e^{u-|\xi|^2/(2\pi)-\xi t})
    +
    \Im\Li_2(e^{-u-|\xi|^2/(2\pi)-\xi t})
  \right)
  \\
  &
  +\frac{ut^2}{2}
  +\frac{|\xi|^2t}{2\pi}
  -\frac{7u\pi^2}{3|\xi|^2}
  +\frac{u^3}{2|\xi|^2}
  +\frac{u|\xi|^2}{8\pi^2}
  -\pi.
\end{split}
\end{equation*}
For $0<r<1$ and $0<\theta<2\pi$ we have
\begin{equation*}
\begin{split}
  \Re\Li_2(re^{\sqrt{-1}\theta})
  &=
  -\frac{1}{2}
  \int_{0}^{r}
  \frac{\log(1-2s\cos\theta+s^2)}{s}\,ds
  \le
  -\frac{1}{2}
  \int_{0}^{r}
  \frac{\log(1-2s+s^2)}{s}\,ds
  \\
  &=
  -\int_{0}^{r}\frac{\log(1-s)}{s}\,ds
  \le
  -\int_{0}^{1}\frac{\log(1-s)}{s}\,ds
  =
  \Li_2(1)
  =
  \frac{\pi^2}{6}.
\end{split}
\end{equation*}
We also have
\begin{equation*}
\begin{split}
  \Im\Li_2(re^{\sqrt{-1}\theta})
  &=
  -\int_{0}^{r}
  \frac{\arg(1-se^{\sqrt{-1}\theta})}{s}\,ds
  \\
  &=
  -\int_{0}^{1}\frac{\arg(1-se^{\sqrt{-1}\theta})}{s}\,ds
  +
  \int_{r}^{1}
  \frac{\arg(1-se^{\sqrt{-1}\theta})}{s}\,ds
  \\
  &\le
  \Im\Li_2(e^{\sqrt{-1}\theta})
  \le
  \Im\Li_2(e^{\sqrt{-1}\pi/3})
  =
  1.01494\dots.
\end{split}
\end{equation*}
when $0\le\theta\le\pi$.
Since $\Im\Li_2(re^{\sqrt{-1}\theta})=-\Im\Li_2(re^{\sqrt{-1}(\theta-\pi)})$ when $\pi<\theta\le2\pi$, we have
\begin{equation*}
\begin{split}
  &\Re\Phi\left(\frac{u}{2\pi}-\sqrt{-1}+t\right)
  \\
  =&
  \frac{4\pi}{|\xi|^2}\Im\Li_2(e^{\sqrt{-1}\pi/3})
  +\frac{ut^2}{2}
  +\frac{|\xi|^2t}{2\pi}
  -2\frac{u\pi^2}{|\xi|^2}
  +\frac{u^3}{2|\xi|^2}
  +\frac{u|\xi|^2}{8\pi^2}
  -\pi
  \\
  &\quad\text{(since $0<t<1$ and $0<u<\pi/2$)}.
  \\
  <&
  \frac{|\xi|^2t}{2\pi}
  +\frac{1}{\pi}\Im\Li_2(e^{\sqrt{-1}\pi/3})
  +\frac{\pi}{2}
  -\frac{4\pi}{17}
  +\frac{\pi}{64}
  +\frac{17\pi}{64}
  -\pi
  \\
  \le&
  \frac{|\xi|^2t}{2\pi}
  +
  \frac{1}{\pi}\Im\Li_2(e^{\sqrt{-1}\pi/3})
  -\frac{247}{544}\pi.
\end{split}
\end{equation*}
when $u<\pi/2$.
\par
So we have
\begin{equation*}
\begin{split}
  &|I_{-,2}(N)|
  \\
  <&
  4e^{(\Im\Li_2(e^{\sqrt{-1}\pi/3})/\pi-247\pi/544-2\pi)N}
  \exp\bigl(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)})\bigr)
  \\
  &\times
  \lim_{\varepsilon\searrow0}
  \int_{\varepsilon}^{1-\varepsilon}e^{N|\xi|^2t/(2\pi)}\,dt
  \\
  =&
  4e^{(\Im\Li_2(e^{\sqrt{-1}\pi/3})/\pi-247\pi/544-2\pi)N}
  \exp\bigl(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)})\bigr)
  \\
  &\times
  \frac{2\pi}{N|\xi|^2}(e^{N|\xi|^2/(2\pi)}-1)
  \\
  =&
  \frac{8\pi\exp\bigl(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)})\bigr)}{N|\xi|^2}
  \\
  &\times
  \left(
    e^{(\Im\Li_2(e^{\sqrt{-1}\pi/3})/\pi-247\pi/544-2\pi+|\xi|^2/(2\pi))N}
  \right.
  \\
  &\phantom{\times}\qquad
  \left.
    -
    e^{(\Im\Li_2(e^{\sqrt{-1}\pi/3})/\pi-247\pi/544-2\pi)N}
  \right)
  \\
  <&
  \frac{8\pi\exp\bigl(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)})\bigr)}{N|\xi|^2}
  \\
  &\times
  \left(
    e^{(\Im\Li_2(e^{\sqrt{-1}\pi/3})/\pi-179\pi/544)N}
    -
    e^{(\Im\Li_2(e^{\sqrt{-1}\pi/3})/\pi-247\pi/544-2\pi)N}
  \right)
  \\
  <&
  \frac{8\pi\exp\bigl(4A+2|\gamma|(1+e^{R(u+u^2/(2\pi)+2\pi)})\bigr)}{N|\xi|^2}
  \\
  <&
  \frac{K_{-,2}}{N}
\end{split}
\end{equation*}
for a positive constant $K_{-,2}$, since $\Im\Li_2(e^{\sqrt{-1}\pi/3})/\pi-179\pi/544=-0.710657\dots$.
\end{proof}


\section{Proof of Proposition~\ref{prop:4.9}}\label{sec:prop:4.9}
In this section we again follow \cite{{Andersen/Hansen:JKNOT2006}} to prove Proposition~\ref{prop:4.9}.
From \eqref{eq:g_N} we have
\begin{equation*}
  \int_{p(\varepsilon)}g_N(w)\,dw
  =
  \int_{p(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw
  +
  \int_{p(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)h_{\gamma}(w)\,dw
\end{equation*}
for any path in the parallelogram bounded by $C_+(\varepsilon)\cup C_-(\varepsilon)$ connecting $\varepsilon$ and $1-\varepsilon$, where
\begin{equation*}
  h_{\gamma}(w)
  :=
  \exp
  \left(
    I_{\gamma}(\pi-\sqrt{-1}u+\sqrt{-1}\xi w)
    -
    I_{\gamma}(-\pi-\sqrt{-1}u-\sqrt{-1}\xi w)
  \right)
  -1.
\end{equation*}
Note that $h_{\gamma}(w)$ is defined for $w$ with $0<\Im(\xi w)<2\pi$, that is, for $w$ between the two parallel thick lines depicted in Figure~\ref{fig:contour}.
\par
Then we have
\begin{equation}\label{eq:max}
\begin{split}
  &\left|
    \int_{p(\varepsilon)}g_N(w)\,dw
    -
    \int_{p(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw
  \right|
  \\
  \le&
  \int_{p(\varepsilon)}\left|\exp\big(N\Phi(w)\bigr)h_{\gamma}(w)\right|\,dw
  \\
  \le&
  \max_{w\in p(\varepsilon)}\left\{\exp\bigl(N\Re\Phi(w)\bigr)\right\}
  \int_{p(\varepsilon)}|h_{\gamma}(w)|\,dw
  \\
  =&
  \max_{w\in p(\varepsilon)}\left\{\exp\bigl(N\Re\Phi(w)\bigr)\right\}
  \int_{\varepsilon}^{1-\varepsilon}|h_{\gamma}(w)|\,dw
  \\
  \le&
  \max_{w\in p(\varepsilon)}\left\{\exp\bigl(N\Re\Phi(w)\bigr)\right\}
  \int_{0}^{1}|h_{\gamma}(w)|\,dw.
\end{split}
\end{equation}
Here we use the analyticity of $h_{\gamma}$ in the equality.
\par
By the definition of $h_{\gamma}$ we have
\begin{equation}\label{eq:h_gamma}
  h_{\gamma}(t)
  =
  \sum_{n=1}^{\infty}
  \frac{1}{n!}
  \left(
    I_{\gamma}(\pi-\sqrt{-1}u+\sqrt{-1}\xi t)
    -
    I_{\gamma}(-\pi-\sqrt{-1}u-\sqrt{-1}\xi t)
  \right)^n.
\end{equation}
From Lemma~\ref{lem:Lemma3}, for $0<t<1$ we have
\begin{equation*}
  \left|
    I_{\gamma}(\pi-\sqrt{-1}u+\sqrt{-1}\xi t)
  \right|
  \le
  A|\gamma|
  \left(
    \frac{1}{2\pi t}+\frac{1}{2\pi-2\pi t}
  \right)
  +
  B|\gamma|
  \left(
    1+e^{(u-ut)R}
  \right)
\end{equation*}
and
\begin{equation*}
  \left|
    I_{\gamma}(-\pi-\sqrt{-1}u-\sqrt{-1}\xi w)
  \right|
  \le
  A|\gamma|
  \left(
    \frac{1}{2\pi-2\pi t}+\frac{1}{2\pi t}
  \right)
  +
  B|\gamma|
  \left(
    1+e^{(u+ut)R}
  \right),
\end{equation*}
and so we have
\begin{equation*}
\begin{split}
  &\left|
    I_{\gamma}(\pi-\sqrt{-1}u+2\pi t)
    -
    I_{\gamma}(-\pi-\sqrt{-1}u-2\pi t)
  \right|
  \\
  \le&
  \frac{A|\gamma|}{\pi}
  \left(
    \frac{1}{1-t}+\frac{1}{t}
  \right)
  +
  B|\gamma|
  \left(
    2+e^{(1+t)uR}+e^{(1-t)uR}
  \right)
  \\
  \le&
  |\gamma|\left(A'f(t)+B'\right)
\end{split}
\end{equation*}
for some positive constants $A'$ and $B'$, where we put $f(t):=1/t+1/(1-t)$.
Since $f(t)\ge4$ for $0<t<1$ we have
\begin{equation}\label{eq:I_gamma}
\begin{split}
  &\left|
    I_{\gamma}(\pi-\sqrt{-1}u+\sqrt{-1}\xi w)
    -
    I_{\gamma}(-\pi-\sqrt{-1}u-\sqrt{-1}\xi w)
  \right|
  \\
  \le&
  |\gamma|\left(A'f(t)+B'\frac{f(t)}{4}\right)
  \\
  =&
  A''|\gamma|f(t),
\end{split}
\end{equation}
where $A'':=A'+B'/4$.
\par
From the argument in \cite[P.~537]{Andersen/Hansen:JKNOT2006} we have
\begin{equation*}
  \int_{|\gamma|}^{1-|\gamma|}f(t)^n\,dt
  \le
  2^{2n+1}\int_{|\gamma|}^{1/2}\frac{dt}{t^n}
\end{equation*}
for $n\ge1$.
Since $|\gamma|=|\xi|/(2N)$ we have
\begin{equation*}
  \int_{|\gamma|}^{1/2}\frac{dt}{t}
  =
  \log{N}-\log|\xi|
  \le
  \log{N}
\end{equation*}
and
\begin{equation*}
  \int_{|\gamma|}^{1/2}\frac{dt}{t^n}
  =
  \frac{1}{n-1}
  \left(
    \frac{1}{|\gamma|^{n-1}}-2^{n-1}
  \right)
  \le
  \frac{1}{(n-1)|\gamma|^{n-1}}.
\end{equation*}
for $n\ge2$.
\par
Therefore from \eqref{eq:h_gamma} and \eqref{eq:I_gamma} we have
\begin{equation*}
\begin{split}
  \int_{|\gamma|}^{1-|\gamma|}|h_{\gamma}(t)|\,dt
  &\le
  \sum_{n=1}^{\infty}
  \frac{1}{n!}(A'')^n|\gamma|^n
  \int_{|\gamma|}^{1-|\gamma|}f(t)^n\,dt
  \\
  &\le
  2|\gamma|
  \left(
    4A''\log{N}
    +
    \sum_{n=2}^{\infty}
    \frac{(4A'')^n}{(n-1)n!}
  \right)
  \\
  &\le
  \frac{|\xi|}{N}
  \left(
    4A''\log{N}
    +
    \exp(4A'')-4A''-1
  \right)
  \\
  &\le
  \frac{K'\log{N}}{N}
\end{split}
\end{equation*}
for a positive constant $K'$ if $N$ is sufficiently large.
\par
For $0\le t\le1$, we also have from Lemma~\ref{lem:Lemma3}
\begin{equation*}
\begin{split}
  &\left|
    I_{\gamma}(\pi-\sqrt{-1}u+2\pi t)
    -
    I_{\gamma}(-\pi-\sqrt{-1}u-2\pi t)
  \right|
  \\
  \le&
  4A
  +
  B|\gamma|
  \left(
    2+e^{(1+t)uR}+e^{(1-t)uR}
  \right).
\end{split}
\end{equation*}
Since $|\gamma|=|\xi|/(2N)$, we have
\begin{equation*}
  |h_{\gamma}(t)|
  \le
  \exp
  \left(
    4A
    +
    \frac{B'|\xi|}{2N}
  \right).
\end{equation*}
So we have
\begin{equation*}
  \int_{0}^{|\gamma|}|h_{\gamma}(t)|\,dt
  \le
  \frac{|\xi|}{2N}
  \exp
  \left(
    4A
    +
    \frac{B'|\xi|}{2N}
  \right)
  \le
  \frac{K''}{N}
\end{equation*}
and
\begin{equation*}
  \int_{1-|\gamma|}^{1}|h_{\gamma}(t)|\,dt
  \le
  \frac{|\xi|}{2N}
  \exp
  \left(
    4A
    +
    \frac{B'|\xi|}{2N}
  \right)
  \le
  \frac{K'''}{N}
\end{equation*}
for positive constants $K''$ and $K'''$.
\par
Therefore we have
\begin{equation*}
  \int_{0}^{1}|h_{\gamma}(t)|\,dt
  \le
  \frac{K'\log{N}}{N}+\frac{K''}{N}+\frac{K'''}{N}
  \le
  \frac{K_2\log{N}}{N}
\end{equation*}
for a positive constant $K_2$.
Now from \eqref{eq:max} we finally have
\begin{equation*}
  \left|
    \int_{p(\varepsilon)}g_N(w)\,dw
    -
    \int_{p(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw
  \right|
  \le
  \frac{K_2\log{N}}{N}
  \max_{w\in p(\varepsilon)}\left\{\exp\bigl(N\Re\Phi(w)\bigr)\right\},
\end{equation*}
proving Proposition~\ref{prop:4.9}.


\section{Proof of Lemma~\ref{lem:Phi_0}}
\label{sec:Phi_0}
We will show that $\xi\Phi(w_0)$ is purely imaginary with positive imaginary part.
Then since $\xi$ is in the first quadrant, $\Phi(w_0)$ is in also in the first quadrant and so $\Re\Phi(w_0)>0$.
\par
Since $\varphi(u)$ is purely imaginary (Remark~\ref{rem:varphi}), we have $\Li_2(e^{u-\varphi(u)})=\overline{\Li_2(e^{u+\varphi(u)})}$.
Therefore from \eqref{eq:Phi_0} and \eqref{eq:dilog} we have
\begin{equation*}
\begin{split}
  \Im(\xi\Phi(w_0))
  &=
  -2\Im\Li_2(e^{u+\varphi(u)})-u\Im\tilde{\varphi}(u)
  \\
  &=
  2\Im\Li_2(e^{-u-\varphi(u)})
  +\Im\bigl(u+\varphi(u)+\pi\sqrt{-1}\bigr)^2
  -u\Im\tilde{\varphi}(u)
  \\
  &=
  2\Im\Li_2(e^{-u-\varphi(u)})
  +u\varphi(u).
\end{split}
\end{equation*}
So we have
\begin{equation*}
\begin{split}
  &\frac{d\,\Im(\xi\Phi(w_0))}{d\,u}
  \\
  =&
  2\Im
  \left(
    \log(1-e^{-u-\varphi(u)})
    \left(
      1
      +
      \sqrt{-1}\frac{d\,\Im\varphi(u)}{d\,u}
    \right)
  \right)
  +\Im\varphi(u)
  +u\frac{d\,\Im\varphi(u)}{d\,u}
  \\
  =&
  \frac{d\,\Im\varphi(u)}{d\,u}
  \left(
    2\log|1-e^{-u-\varphi(u)}|+u
  \right)
  +2\arg(1-e^{-u-\varphi(u)})
  +\Im\varphi(u)
  \\
  =&
  \frac{d\,\Im\varphi(u)}{d\,u}
  \log\Bigl((1-e^{-u-\varphi(u)})(1-e^{-u+\varphi(u)})e^u\Bigr)
  +2\arg(1-e^{-u-\varphi(u)})
  +\Im\varphi(u)
  \\
  =&
  \frac{d\,\Im\varphi(u)}{d\,u}
  \log(e^u+e^{-u}-e^{\varphi(u)}-e^{-\varphi(u)})
  +2\arg(1-e^{-u-\varphi(u)})
  +\Im\varphi(u)
  \\
  =&
  2\arg(1-e^{-u-\varphi(u)})
  +\Im\varphi(u)
  <0
\end{split}
\end{equation*}
since $-\pi/3<\Im\varphi(u)<0$.
\par
Since $\varphi(0)=-\pi\sqrt{-1}/3$ and $\varphi\Bigl(\log\bigl((3+\sqrt{5})/2\bigr)\Bigr)=0$, we have
\begin{equation*}
  \xi\Phi(w_0)
  =
  \begin{cases}
    2\Im\Li_2\left(e^{\pi\sqrt{-1}/3}\right)=1.01494\ldots
    &\quad\text{($u=0$)},
    \\
    2\Im\Li_2\left(\frac{2}{3+\sqrt{5}}\right)=0
    &\quad\text{($u=\log\bigl((3+\sqrt{5})/2\bigr)$)}.
  \end{cases}
\end{equation*}
Therefore $\Im(\xi\Phi(w_0))>0$ for $0<u<\log\bigl((3+\sqrt{5})/2\bigr)$, completing the proof of Lemma~\ref{lem:Phi_0}.
