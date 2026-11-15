---
doc_id: arxiv-math-0405126v1
doc_title: "ASYMPTOTIC BEHAVIORS OF THE COLORED JONES POLYNOMIALS OF A TORUS KNOT"
section_id: sec-001-2-proof
section_title: "Proof"
section_number: 2
pages: 2-5
source_pdf: 0405126v1.pdf
source_sha256: 713498dbe80f7319
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.894
doc_brief: "ASYMPTOTIC BEHAVIORS OF THE COLORED JONES POLYNOMIALS OF A TORUS KNOT — We study the asymptotic behaviors of the colored Jones polyno- mials of torus knots. Contrary to the works by R. Kashaev, O."
---
When $t=e^{2\pi{r}\sqrt{-1}/N}$ for $r\in\mathbb{C}\setminus{\mathbb{Z}}$, $J_N\left(T(a,b);e^{2\pi{r}\sqrt{-1}/N}\right)$ can be given by the following integral form [@Kashaev/Tirkkonen:ZAPNS200 Lemma 1]. $$J_N\left(T(a,b),e^{2\pi{r}\sqrt{-1}/N}\right)
  =
  \Phi_{a,b,r}(N)
  \int_{C}
  e^{Nf_{a,b,r}(z)}
  \tau_{a,b}(z)
  dz.$$ Here $$\begin{aligned}
  \Phi_{a,b,r}(N)
  &:=g_{a,b,r}\sqrt{N}
     e^{-\left(ab\left(N^2-1\right)+a/b+b/a\right)\pi{r}\sqrt{-1}/(2N)}
  \\
  &\text{
    with
      $g_{a,b,r}
       :=
       \frac{\sqrt{ab}}
            {2\pi\sqrt{2r}
            e^{\pi\sqrt{-1}/4}\sinh\left(\pi{r}\sqrt{-1}\right)}$},
  \\[3mm]
  f_{a,b,r}(z)
  &:=
  ab\left(z-\frac{z^2}{2\pi{r}\sqrt{-1}}\right),
  \\[3mm]
  \tau_{a,b}(z)
  &:=
  \frac{2\sinh(az)\sinh(bz)}{\sinh(abz)},
\end{aligned}$$ and $C$ is the line $$\label{eq:C}
  C:=\{se^{\varphi\sqrt{-1}}\mid{s}\in\mathbb{R}\}$$ with $\operatorname{Re}\left(r\sqrt{-1}e^{-2\varphi\sqrt{-1}}\right)>0$. (We will choose $\varphi$ later.)

Let $\mathcal{P}$ be the set of the poles of $\tau_{a,b}(z)$, that is , we put $$\mathcal{P}
  :=
  \left\{\frac{k\pi\sqrt{-1}}{ab} \big| k\in\mathbb{Z},a\nmid k,b\nmid k\right\}.$$ We will show that the result follows if $r\notin\mathbb{R}$, $\operatorname{Re}{r}>0$, and $|r|>\frac{1}{ab}$.

Put $\theta:=\arg{r}$ ($-\pi/2<\theta<\pi/2$) so that $r=|r|e^{\theta\sqrt{-1}}$. Put also $\varphi:=\theta/2+\pi/4$ in [\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"}. Note that $\operatorname{Re}\left(r\sqrt{-1}e^{-2\varphi\sqrt{-1}}\right)=\operatorname{Re}|r|>0$ and that $0<\varphi<\pi/2$.

Let ${C'}$ be the line parallel to $C$ that passes through the point $\pi{r}\sqrt{-1}$. (We change $C'$ slightly near $\mathcal{P}$ to avoid poles of $\tau_{a,b}(z)$ if necessary.) For a positive number $R$, let $D_{+}$ ($D_{-}$, respectively) be the segment of the line $\operatorname{Re}{z}=R$ ($\operatorname{Re}{z}=-R$, respectively) between $C$ and $C'$ oriented upward (downward, respectively). We see that $C'$ and $D_{\pm}$ are parameterized as follows. $$\begin{split}
  C'
  &=
  \left\{
    se^{(\theta/2+\pi/4)\sqrt{-1}}+\pi{r}\sqrt{-1}
    \Bigm|
    s\in\mathbb{R}
  \right\},
  \\
  D_{\pm}
  &=
  \left\{
    \vphantom{\bigr)}
    \pm{R}+s\sqrt{-1}
    \bigm|
    \pm{R}\tan\left(\theta/2+\pi/4\right)
    \le{s}
    \le
    \pm{R}\tan\left(\theta/2+\pi/4\right)
    +
    \pi|r|h(\theta)
  \right\},
\end{split}$$ where $h(\theta):=\cos\theta+\sin\theta\tan(\theta/2+\pi/4)$ Note that $C'$ crosses the imaginary axis at $\pi|r|h(\theta)\sqrt{-1}$.

Then by the residue theorem $$\begin{split}
  &
  \int_{\overline{C}}
  e^{Nf_{a,b,r}(z)}\tau_{a,b}(z)\,dz
  \\
  &\quad
  =
  \int_{\overline{C'}}
  e^{Nf_{a,b,r(z)}}\tau_{a,b}(z)\,dz
  +
  \sum_{k}
  \operatorname{Res}
  \left(
    e^{Nf_{a,b,r}(z)}\tau_{a,b}(z);z=k\pi\sqrt{-1}/(ab)
  \right)
  \\
  &\quad\quad
  -\int_{D_+}
  e^{Nf_{a,b,r}(z)}\tau_{a,b}(z)\,dz
  -\int_{D_-}
  e^{Nf_{a,b,r}(z)}\tau_{a,b}(z)\,dz,
\end{split}$$ where $\operatorname{Res}(F(z);z=\zeta)$ is the residue of $F(z)$ around $z=\zeta$, $\overline{C}$ ($\overline{C'}$, respectively) is the segment in $C$ (${C'}$, respectively) bounded by $D_{\pm}$ oriented from left to right, and $k$ runs over integers that are not multiples of $a$ or $b$ such that $k\pi\sqrt{-1}/ab$ is between $C$ and $C'$, that is, $0<k<ab|r|h(\theta)$.

Since it is not hard to see that on $D_{\pm}$ $$\left|e^{Nf_{a,b,r}(z)}\right|
  <
  e^{abN\left(c_2R^2+c_1R+c_0\right)}$$ for some $c_i$ with $c_2<0$ if $R$ is sufficiently large, and that $$\begin{split}
  \left|\tau_{a,b}(z)\right|
  &=
  \frac{\left|\left(e^{az}-e^{-az}\right)
              \left(e^{bz}-e^{-bz}\right)\right|}
       {\left|e^{abz}-e^{-abz}\right|}
  \\
  &\le
  \frac{\left|e^{(a+b)z}\right|
        +
        \left|e^{(a-b)z}\right|
        +
        \left|e^{(b-a)z}\right|
        +
        \left|e^{-(a+b)z}\right|}
       {\bigl|\left|e^{abz}\right|-\left|e^{-abz}\right|\bigr|}
  \\
  &=
  \frac{e^{\pm(a+b)R}
        +
        e^{\pm(a-b)R}
        +
        e^{\pm(b-a)R}
        +
        e^{\mp(a+b)R}}
       {\left|e^{\pm{abR}}-e^{\mp{abR}}\right|},
\end{split}$$ the integrals on $D_{\pm}$ vanish when $R\to\infty$. Therefore we have $$\begin{gathered}
  \int_{C}
  e^{Nf_{a,b,r}(z)}\tau_{a,b}(z)\,dz
  \\
  =
  \int_{C'}
  e^{Nf_{a,b,r}(z)}\tau_{a,b}(z)\,dz
  +
  \sum_{k}
  \operatorname{Res}
  \left(
    e^{Nf_{a,b,r}(z)}\tau_{a,b}(z);z=k\pi\sqrt{-1}/(ab)
  \right).
\end{gathered}$$

We will apply the saddle point method (or the method of steepest descent) to know the asymptotic behavior of the integral on $C'$. See for example [@Marsden/Hoffman:Complex_Analysis Theorem 7.2.9]. On $C'$ we have $$f_{a,b,r}\left(se^{(\theta/2+\pi/4)\sqrt{-1}}+\pi{r}\sqrt{-1}\right)
  =
  -\frac{s^2}{2\pi|r|}+\frac{\pi{r}\sqrt{-1}}{2}.$$ So $\operatorname{Im}{f_{a,b,r}(z)}$ is constant on $C'$ and $\operatorname{Re}{f_{a,b,r}(z)}$ takes its unique maximum at $z=\pi{r}\sqrt{-1}$ (when $s=0$) on $C'$. (Note that this is also true if we change $C'$ slightly near a pole of $\tau_{a,b}$.) Therefore from the saddle point method we have $$\begin{split}
  &
  \int_{C'}
  e^{Nf_{a,b,r}(z)}\tau_{a,b}(z)\,dz
  \\
  &\quad\underset{N\to\infty}{\sim}
  \frac{\sqrt{2\pi}\tau_{a,b}(\pi{r}\sqrt{-1})}
       {\sqrt{N}\sqrt{-d^2f_{a,b,r}(z)/dz^2\big|_{z=\pi{r}\sqrt{-1}}}}
  e^{Nf_{a,b,r}(\pi{r}\sqrt{-1})}
  \\
  &=
  \pi\sqrt{\frac{2r}{abN}}e^{\pi\sqrt{-1}/4}
  \tau_{a,b}(\pi{r}\sqrt{-1})
  e^{Nab\pi{r}\sqrt{-1}/2}.
\end{split}$$ We also have $$\begin{split}
  &
  \operatorname{Res}
  \left(
    e^{Nf_{a,b,r}(z)}\tau_{a,b}(z);z=k\pi\sqrt{-1}/(ab)
  \right)
  \\
  &\quad=
  e^{Nk\pi\sqrt{-1}\left(1-\frac{k}{2abr}\right)}
  \operatorname{Res}\left(\tau_{a,b}(z);z=k\pi\sqrt{-1}/(ab)\right)
  \\
  &\quad=
  (-1)^k
  \frac{2\sinh(k\pi\sqrt{-1}/a)\sinh(k\pi\sqrt{-1}/b)}{ab}
  e^{Nk\pi\sqrt{-1}\left(1-\frac{k}{2abr}\right)}.
\end{split}$$

Therefore we have $$\label{eq:asymptotic}
\begin{split}
  &\int_{C}
  e^{Nf_{a,b,r}(z)}\tau_{a,b}(z)\,dz
  \\
  &\quad\underset{N\to\infty}{\sim}
  \pi\sqrt{\frac{2r}{abN}}e^{\pi\sqrt{-1}/4}
  \tau_{a,b}(\pi{r}\sqrt{-1})
  e^{Nab\pi{r}\sqrt{-1}/2}
  \\
  &\quad\phantom{\underset{N\to\infty}{\sim}}
  +
  \sum_{k}
  (-1)^k
  \frac{2\sinh(k\pi\sqrt{-1}/a)\sinh(k\pi\sqrt{-1}/b)}{ab}
  e^{Nk\pi\sqrt{-1}\left(1-\frac{k}{2abr}\right)}.
\end{split}$$

Now we want to know the biggest real part of the exponents in [\[eq:asymptotic\]](#eq:asymptotic){reference-type="eqref" reference="eq:asymptotic"}. We have $$\begin{split}
  &
  \max
  \left\{
    \operatorname{Re}\left(\frac{ab\pi{r}\sqrt{-1}}{2}\right),
    \max_{k}{\operatorname{Re}\left(k\pi\sqrt{-1}\left(1-\frac{k}{2abr}\right)\right)}
  \right\}
  \\
  &\quad=
  \max
  \left\{
    -\frac{ab\pi\operatorname{Im}{r}}{2},
    \max_{k}{\frac{-k^2\pi\operatorname{Im}{r}}{2ab|r|^2}}
  \right\}
  \\
  &\quad=
  \begin{cases}
    \displaystyle
    \frac{\pi\operatorname{Im}{r}}{2ab}\max_{k}
    \left\{
      -a^2b^2,-\frac{k^2}{|r|^2}
    \right\}
    &\qquad\text{if $\operatorname{Im}{r}>0$}
    \\[5mm]
    \displaystyle
    -\frac{\pi\operatorname{Im}{r}}{2ab}\max_{k}
    \left\{
      a^2b^2,\frac{k^2}{|r|^2}
    \right\}
    &\qquad\text{if $\operatorname{Im}{r}<0$}
  \end{cases}.
\end{split}$$ Since $1<h(\theta)$ when $0<\theta<\pi/2$, $|r|>1/(ab)$, and $k$ runs over positive integers less than $ab|r|h(\theta)>1$, we have $$\max_{k}\left\{-a^2b^2,-\frac{k^2}{|r|^2}\right\}
  =
  -\frac{1}{|r|^2}$$ if $\operatorname{Im}{r}>0$. Since $0<h(\theta)<1$ when $-\pi/2<\theta<0$, $0<k<ab|r|h(\theta)<ab|r|$. So we have $$\max_{k}\left\{a^2b^2,\frac{k^2}{|r|^2}\right\}
  =
  a^2b^2$$ if $\operatorname{Im}{r}<0$.

Therefore if $\operatorname{Im}{r}<0$ $$\int_{C}
  e^{Nf_{a,b,r(z)}}\tau_{a,b}(z)dz
  \underset{N\to\infty}{\sim}
  \pi\sqrt{\frac{2r}{abN}}e^{\pi\sqrt{-1}/4}
  \tau_{a,b}(\pi{r}\sqrt{-1})
  e^{Nab\pi{r}\sqrt{-1}/2}$$ and if $\operatorname{Im}{r}>0$ $$\int_{C}
  e^{Nf_{a,b,r}(z)}\tau_{a,b}(z)\,dz
  \\
  \underset{N\to\infty}{\sim}
  -
  \frac{2\sinh(\pi\sqrt{-1}/a)\sinh(\pi\sqrt{-1}/b)}{ab}
  e^{N\pi\sqrt{-1}\left(1-\frac{1}{2abr}\right)}.$$ Since $$\Phi_{a,b,r}(N)
  \underset{N\to\infty}{\sim}
  g_{a,b,r}\sqrt{N}e^{-Nabr\pi\sqrt{-1}/2},$$ we have $$\begin{gathered}
  J_N\bigr(T(a,b);e^{2\pi{r}\sqrt{-1}}\bigr)
  \\
  \underset{N\to\infty}{\sim}
  -
  \frac{2\sinh(\pi\sqrt{-1}/a)\sinh(\pi\sqrt{-1}/b)g_{a,b,r}}{ab}
  \sqrt{N}
  e^{N\pi\sqrt{-1}\bigl(1-abr/2-1/(2abr)\bigr)}
\end{gathered}$$ if $\operatorname{Im}{r}>0$ and $$J_N\bigr(T(a,b);e^{2\pi{r}\sqrt{-1}}\bigr)
  \underset{N\to\infty}{\sim}
  \frac{\sinh(ar\pi\sqrt{-1})\sinh(br\pi\sqrt{-1})}
       {\sinh(abr\pi\sqrt{-1})\sinh(r\pi\sqrt{-1})}$$ if $\operatorname{Im}{r}<0$.

Since the Alexander polynomial $\Delta\bigl(T(a,b);t\bigr)$ of $T(a,b)$ is $\frac{(t^{ab/2}-t^{-ab/2})(t^{1/2}-t^{-1/2})}
      {(t^{a/2}-t^{-a/2})(t^{b/2}-t^{-b/2})}$ (see for example [@Lickorish:1997 Page 119]), we have $$\lim_{N\to\infty}J_N\left(T(a,b);e^{2\pi{r}\sqrt{-1}/N}\right)
  =
  \frac{1}{\Delta\left(T(a,b);e^{2\pi{r}\sqrt{-1}}\right)}$$ if $\operatorname{Im}{r}<0$. If $\operatorname{Im}{r}>0$ we have $$\lim_{N\to\infty}
  \frac{\log{J_N\left(T(a,b);e^{2\pi{r}\sqrt{-1}/N}\right)}}{N}
  =
  \left(1-\dfrac{1}{2abr}-\dfrac{abr}{2}\right)\pi\sqrt{-1}.$$ This completes the proof of Theorem [\[thm\]](#thm){reference-type="ref" reference="thm"}.
