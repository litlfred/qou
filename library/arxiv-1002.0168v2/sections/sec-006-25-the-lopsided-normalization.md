---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Introduction"
section_id: sec-006-25-the-lopsided-normalization
section_title: "The lopsided normalization"
section_number: 2.5
pages: 9-10
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.992
doc_brief: "Non-cyclotomic fusion categories Introduction — Etingof, Nikshych and Ostrik ask in [7, §2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
[]{#sec:lopsided label="sec:lopsided"} In an irreducible shaded planar algebra $\cP$ over a field $k$, the shaded inside and shaded outside circles each evaluate to a scalar multiple of the empty diagram. These multiples are called the shaded and unshaded moduli. The product of the two moduli is called the index of $\cP$.

If the two moduli are equal, we say the planar algebra is spherical. (In particular, because in this section we are assuming irreducibility, this condition implies the usual notion of a planar algebra being spherical.) If the shaded modulus is equal to one, we say the planar algebra is lopsided, and the unshaded modulus is the index.

Any irreducible shaded planar algebra $\cP$ over $\Complex$ is part of a family $\left\{\cP_x\right\}_{x \in \Complex}$ of planar algebras with $\cP_1 = \cP$, and $\cP_x$ given by changing the action of the planar operad by a factor of $x^k$, where $k$ is the signed count of critical points in the strands which are shaded above and unshaded below (minima counting positively, maxima counting negatively). The index is constant across this family, but the shaded and unshaded moduli scale by $x$ and $x^{-1}$.

It may be that the planar algebra $\cP_x$ has a rational form over a field $k$ for certain $x$, but not all $x$. In particular, given a planar algebra $\cC$ over $k$ with unshaded modulus $x \in k$, then $\cC_{x^{-1}}$ is a lopsided planar algebra over $k(x)=k$. On the other hand, given a lopsided planar algebra $\cC$ over $k$ with index $D \in k$ the corresponding spherical planar algebra $\cC_{\sqrt{D}}$ is in general only defined over $k(\sqrt{D})$. The fact that the field of definition may need to increase to ensure being spherical but does not need to increase to ensure being lopsided should encourage you to prefer lopsided planar algebras over spherical planar algebras. (It's also natural from a subfactor perspective: $B$ as an $A-B$ bimodule has left-dimension the index and right-dimension $1$.)

Any element $v \in \cP_{n,\pm}$ has a left trace and a right trace, satisfying $$\begin{aligned}
\operatorname{tr}_{L}\left(v\right) & =
    \begin{cases}
        \operatorname{tr}_{R}\left(v\right) & \text{if $n$ is even} \\
        \frac{d_{\mp}}{d_{\pm}} \operatorname{tr}_{R}\left(v\right) & \text{if $n$ is odd}
    \end{cases}
\end{aligned}$$ where $d_+$ is the unshaded modulus and $d_-$ is the shaded modulus. When $\cP$ is spherical, the left and right traces coincide. We will sometimes refer to the trace of an idempotent as its dimension, and if a side is not specified we always intend the right trace.

::: example
The two strand Jones-Wenzl idempotents in lopsided Temperley-Lieb are $$\begin{aligned}
\begin{tikzpicture}[baseline=-1ex]
\node[fill=white, draw, rectangle] (left) at (0,0) {$\JW{2}$};
\begin{pgfonlayer}{background} 
\path[fill=black!20]
    ($(left.240)+(0,-0.5)$) -- ($(left.120)+(0,0.5)$) -- ($(left.60)+(0,0.5)$) -- ($(left.300)+(0,-0.5)$);
\draw ($(left.240)+(0,-0.5)$) -- ($(left.120)+(0,0.5)$);
\draw  ($(left.60)+(0,0.5)$) -- ($(left.300)+(0,-0.5)$);
\end{pgfonlayer}
\end{tikzpicture}
& = 
\begin{tikzpicture}[baseline=-1ex]
\clip (-0.75,-0.8) rectangle (0.75,0.8);
\path[fill=black!20]
     (-0.5,-0.8) -- (-0.5,0.8) -- (0.5,0.8) -- (0.5,-0.8);
\draw (-0.5,-0.8) -- (-0.5,0.8);
\draw  (0.5,0.8) -- (0.5,-0.8);
\end{tikzpicture}
 - 
\begin{tikzpicture}[baseline=-1ex]
\clip (-0.75,-0.8) rectangle (0.75,0.8);
\path[draw, fill=black!20]
     (-0.5,-0.8) .. controls ++(0,0.7) and ++(0,0.7) .. (0.5,-0.8);
\path[draw, fill=black!20]
     (-0.5,0.8) .. controls ++(0,-0.7) and ++(0,-0.7) .. (0.5,0.8);
\end{tikzpicture}
\displaybreak[1] \\
\intertext{and}
\begin{tikzpicture}[baseline=-1ex]
\node[fill=white, draw, rectangle] (left) at (0,0) {$\JW{2}$};
\begin{pgfonlayer}{background} 
\path[fill=black!20] (-0.75,-0.8) rectangle (0.75,0.8);
\path[fill=white]
    ($(left.240)+(0,-0.5)$) -- ($(left.120)+(0,0.5)$) -- ($(left.60)+(0,0.5)$) -- ($(left.300)+(0,-0.5)$);
\draw ($(left.240)+(0,-0.5)$) -- ($(left.120)+(0,0.5)$);
\draw  ($(left.60)+(0,0.5)$) -- ($(left.300)+(0,-0.5)$);
\end{pgfonlayer}
\end{tikzpicture}
& = 
\begin{tikzpicture}[baseline=-1ex]
\path[fill=black!20] (-0.75,-0.8) rectangle (0.75,0.8);
\path[fill=white]
     (-0.5,-0.8) -- (-0.5,0.8) -- (0.5,0.8) -- (0.5,-0.8);
\draw (-0.5,-0.8) -- (-0.5,0.8);
\draw  (0.5,0.8) -- (0.5,-0.8);
\end{tikzpicture}
 -  \frac{1}{[2]^2}
\begin{tikzpicture}[baseline=-1ex]
\path[fill=black!20] (-0.75,-0.8) rectangle (0.75,0.8);
\path[draw, fill=white]
     (-0.5,-0.8) .. controls ++(0,0.7) and ++(0,0.7) .. (0.5,-0.8);
\path[draw, fill=white]
     (-0.5,0.8) .. controls ++(0,-0.7) and ++(0,-0.7) .. (0.5,0.8);
\end{tikzpicture}
\end{aligned}$$
:::

::: example
Consider an irreducible shaded planar algebra $\cP$ with index $D$. Choose $q$ so $q+q^{-1} = \sqrt{D}$. If $\cP$ is spherical then the dimensions of the Jones-Wenzl idempotents are given by $$\begin{aligned}
\operatorname{tr}_{R}\left(\JW{n} \in \cP_{n,\pm}\right) & = [n+1]_q \in \Rational(\sqrt{D}) \\
\intertext{while when $\cP$ is lopsided they are}
\operatorname{tr}_{R}\left(\JW{n} \in \cP_{n,+}\right) & =
    \begin{cases}
        \frac{[n+1]_q}{[2]_q} & \text{if $n$ is odd} \\
        [n+1]_q & \text{if $n$ is even}
    \end{cases}
    \\
    & \in \Rational(D) \displaybreak[1] \\
\operatorname{tr}_{R}\left(\JW{n} \in \cP_{n,-}\right) & =
    \begin{cases}
        [2]_q [n+1]_q & \text{if $n$ is odd} \\
        [n+1]_q & \text{if $n$ is even}
    \end{cases}
    \\
    & \in \Rational(D)
\end{aligned}$$
:::
