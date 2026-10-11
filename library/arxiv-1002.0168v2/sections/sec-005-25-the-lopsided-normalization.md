---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder"
section_id: sec-005-25-the-lopsided-normalization
section_title: "The lopsided normalization"
section_number: 2.5
pages: 9-14
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
doc_brief: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder — Etingof, Nikshych and Ostrik ask in [ 7,§2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.965
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

# The shaded planar algebras $\cH_0$ and $\cH_1$ {#sec:construction}

The goal of this section is to prove Theorem [\[thm:detailed\]](#thm:detailed){reference-type="ref" reference="thm:detailed"} part [\[pa:construct\]](#pa:construct){reference-type="ref" reference="pa:construct"} and the "if\" direction of parts [\[pa:dualprojs\]](#pa:dualprojs){reference-type="ref" reference="pa:dualprojs"} and [\[pa:principalprojs\]](#pa:principalprojs){reference-type="ref" reference="pa:principalprojs"}. Thus we explicitly construct certain rational forms and determine when they are complete. These constructions all follow quickly from the generators and relations presentation of the 'Haagerup subfactor planar algebra' $\cH_0$ (from [@0902.1294]) and of the 'extended Haagerup subfactor planar algebra' $\cH_1$ (from [@0909.4099]). We modify these previous constructions slightly by using the lopsided normalization for cups and caps instead of the spherical one. Furthermore, we have rescaled the generator: our $S$ is $\lambda_\ell$ times the $S$ of [@0909.4099; @0902.1294]. (Both of these modifications were made in order to simplify the numbers that appear in the definition so that they lie in a smaller field.)

Let $\ell=0$ or $1$, and let $n=4\ell+4$. Choose $q$ so $q+q^{-1}=\sqrt{D_\ell}$, and define the quantum integers as usual by $[m]=\frac{q^m - q^{-m}}{q-q^{-1}} \in \Integer[\sqrt{D_\ell}]$ (so in particular, $[2] = \sqrt{D_\ell}$). If $m$ is odd then $[m] \in \Rational(D_\ell)$. If $m$ is even, then $[2][m] = [m+1]+[m-1]\in \Rational(D_\ell)$, and also any ratio of two even quantum integers lies in $\Rational(D_\ell)$. We will write $\check{r} = \frac{[n+2]}{[n]} \in \Rational(D_\ell)$ throughout. (This number is the ratio of Perron-Frobenius dimensions of the two vertices past the branch point on the dual principal graph. The corresponding ratio on the principal graph is just $1$.)

Define $\lambda_\ell = [2]^{-1}\sqrt{-\check{r}}$ (these are the same as the explicit numbers given in the introduction) and note that $\lambda_\ell^2 = - \frac{[n+2]}{[2]^2[n]} \in \Rational(D_\ell)$.

Since $\lambda_\ell^2$ is not rational, and the degrees $[\Rational(D_\ell):\Rational]$ are prime, it follows that $\Rational(D_\ell) = \Rational(\lambda_\ell^2)$, and in particular $\Rational(D_\ell) \subset \Rational(\lambda_\ell) \subset \Complex$.

::: defn
[]{#def:pa label="def:pa"} Let $k$ be any field $\Rational(D_\ell) \subset k \subset \Complex$. Let $\cQ_\ell(k)$ be the shaded planar algebra over $k$ generated by a single $n$-box $S \in \cQ_\ell(k)_{n,+}$ subject to relations (1)-(6) below.

1.  The lopsided moduli are $1$ and $D_\ell$. That is, the shaded circle is $1$ and the unshaded circle is $D_\ell$.

2.  $\rho(S)=-S$,

3.  $S$ is uncappable,

4.  $S^2 = \lambda_\ell^2 \JW{n}$,

5.  $$\begin{aligned}
        \scalebox{0.8}{\inputtikz{relations/A}}
                & =  [2] [n]
        \scalebox{0.8}{\inputtikz{relations/B}},
        
    \end{aligned}$$

6.  and $$\begin{aligned}
        \scalebox{0.8}{\inputtikz{relations/C}} 
                 = \frac{1}{\lambda_\ell^2} \frac{1}{[n+1]} \frac{[2n+4]}{[n+2]}
            \scalebox{0.8}{\inputtikz{relations/D}}.
        
    \end{aligned}$$
:::

The planar algebra $\cQ_\ell(k)$ isn't nondegenerate, and hence doesn't yield semisimple tensor categories. We apply the usual semisimplification procedure.

::: defn
Let $\cH_\ell(k)$ be $\cQ_\ell(k) / \cN_\ell(k)$, where $\cN_\ell(k)$ is the ideal of negligible morphisms in $\cQ_\ell(k)$.
:::

::: thm
$\cH_\ell(\Complex)$ is a unitary irreducible planar algebra with principal graph pair $\cH_\ell$. Hence, the tensor categories $\cH_\ell^p(k)$ and $\cH_\ell^d(k)$ are fusion categories.
:::

::: proof
*Proof.* The first statement follows immediately from [@0902.1294 Theorem 5.5] (for $\ell=0$) and from [@0909.4099 Theorem 3.10] (for $\ell=1$). Unitarity implies that $\cH_\ell^p(\Complex)$ and $\cH_\ell^d(\Complex)$ are semisimple, and hence $\cH_\ell^p(k)$ and $\cH_\ell^d(k)$ are semisimple also (since nonsemisimplicity is preserved under base extension). These categories are fusion because the principal graphs are finite. ◻
:::

::: thm
All the minimal idempotents in $\cH_\ell(\Complex)$ (corresponding to the vertices of the principal graph) in fact lie inside $\cH_\ell(\Rational(\lambda_\ell))$. All of the minimal idempotents in the even part of the dual principal graph lie inside $\cH_\ell(\Rational(D_\ell))$.
:::

::: proof
*Proof.* We give explicit formulas for all the idempotents, in Lemmas [\[lem:idempotents1\]](#lem:idempotents1){reference-type="ref" reference="lem:idempotents1"}, [\[lem:idempotents2\]](#lem:idempotents2){reference-type="ref" reference="lem:idempotents2"} and [\[lem:idempotents3\]](#lem:idempotents3){reference-type="ref" reference="lem:idempotents3"}, which occupy the rest of this section. Our naming conventions for the idempotents are shown in Figure [1](#fig:naming){reference-type="ref" reference="fig:naming"}. ◻
:::

<figure id="fig:naming">
<p><span class="math display">$$\begin{tikzpicture}[baseline=-1mm, scale=.7]
    \draw (0,0) -- (7,0);
    \draw (7,0)--(7.7,.7)--(9.7,.7);
    \draw (7,0)--(7.7,-.7)--(9.7,-.7);

    \filldraw              (0,0) node [above] {$1$} circle (1mm);
    \filldraw [fill=white] (1,0) node [above] {$X$} circle (1mm);
    \filldraw              (2,0) node [above] {$\JW{2}$}  circle (1mm);
    \filldraw [fill=white] (3,0) node [above] {$\JW{3}$}  circle (1mm);
    \filldraw              (4,0) node [above] {$\JW{4}$}  circle (1mm);
    \filldraw [fill=white] (5,0) node [above] {$\JW{5}$}  circle (1mm);
    \filldraw              (6,0) node [above] {$\JW{6}$}  circle (1mm);
    \filldraw [fill=white] (7,0) node [above] {$\JW{7}$}  circle (1mm);
    
    
    \filldraw              (7.7,.7) node [above] {$P$}  circle (1mm);
    \filldraw [fill=white] (8.7,.7) node [above] {$P'$}  circle (1mm);
    \filldraw              (9.7,.7) node [above] {$P''$}  circle (1mm);
    \filldraw              (7.7,-.7) node [above] {$Q$}  circle (1mm);
    \filldraw [fill=white] (8.7,-.7) node [above] {$Q'$}  circle (1mm);
    \filldraw              (9.7,-.7) node [above] {$Q''$}  circle (1mm);
\end{tikzpicture}$$</span></p>
<p><span class="math display">$$\begin{tikzpicture}[baseline=-1mm, scale=.7]
    \draw (0,0) -- (7,0);
    \draw (7,0)--(7.7,.7);
    \draw (7,0)--(7.7,-.7);
    \draw (7.7,.7)--(8.4,1.4);
    \draw (7.7,.7)--(8.4,0);

    \filldraw              (0,0) node [above] {$1$} circle (1mm);
    \filldraw [fill=white] (1,0) node [above] {$X^*$} circle (1mm);
    \filldraw              (2,0) node [above] {$\JW{2}$}  circle (1mm);
    \filldraw [fill=white] (3,0) node [above] {$\JW{3}$}  circle (1mm);
    \filldraw              (4,0) node [above] {$\JW{4}$}  circle (1mm);
    \filldraw [fill=white] (5,0) node [above] {$\JW{5}$}  circle (1mm);
    \filldraw              (6,0) node [above] {$\JW{6}$}  circle (1mm);
    \filldraw [fill=white] (7,0) node [above] {$\JW{7}$}  circle (1mm);
    
    
    \filldraw              (7.7,.7) node [above] {$B$}  circle (1mm);
    \filldraw              (7.7,-.7) node [below] {$A$}  circle (1mm);
    \filldraw [fill=white] (8.4,1.4) node [above] {$C$}  circle (1mm);
    \filldraw [fill=white] (8.4,0) node [below] {$D$}  circle (1mm);
\end{tikzpicture}$$</span></p>
<figcaption>The names for the minimal idempotents in <span class="math inline">$\cH_1(\Complex)$</span>. Even vertices are shown as filled circles, and odd vertices are shown as hollow circles. The convention for <span class="math inline">$\cH_0(\Complex)$</span> is the same but with fewer <span class="math inline">$\JW{i}$</span>.</figcaption>
</figure>

::: lem
[]{#lem:S2 label="lem:S2"} The 'one-click' rotation $\rho^{1/2}(S)$, which is an element of $\cH_\ell(k)_{n,-}$, satisfies $$\begin{aligned}
\rho^{1/2}(S)^2 & = -i [2] \lambda_\ell (\check{r}^{1/2} - \check{r}^{-1/2}) \rho^{1/2}(S) - [2]^2 \lambda_\ell^2 \JW{n} \notag \\
    & =  (\check{r}-1) \rho^{1/2}(S) + \check{r} \JW{n}. \label{eq:rhoS2}
\end{aligned}$$
:::

::: proof
*Proof.* Take the formula for $\rho^{1/2}(S)^2$ appearing in [@0909.4099 Theorem 3.9],

and recall that the $S$ there is $\lambda_\ell^{-1}$ times our generator $S$, and that since we are working in the lopsided planar algebra, there is an additional factor of $[2]^{-1}$ with each occurrence of $\rho^{1/2}$. This factor arises because in the notation of §[\[sec:lopsided\]](#sec:lopsided){reference-type="ref" reference="sec:lopsided"}, if the planar algebras from [@0902.1294; @0909.4099] are denoted $\cP$, we're looking at $\cP_{\sqrt{D_\ell}}$, and $\rho^{1/2}$ has a single critical point shaded above, which is a maximum. Thus we obtain $$[2]^{-2} \lambda_\ell^{-2} \rho^{1/2}(S)^2 = - [2]^{-1} \lambda_\ell^{-1} \omega^{1/2} r^{1/2} (\check{r}^{1/2} - \check{r}^{-1/2})\rho^{1/2}(S) + \omega^{-1} r \JW{n}$$ and after setting $r=1$, $\omega = -1$, using the formula for $\lambda_\ell$ and rearranging, this becomes the desired formula. ◻
:::

::: lem
[]{#lem:idempotents1 label="lem:idempotents1"} The idempotents $P$, $Q$, $A$ and $B$ in $\cH_\ell^p$ and $\cH_\ell^d$ are given by $$\begin{aligned}
P & = \frac{1}{2}\left(\JW{n} + \frac{1}{\lambda_\ell}S\right) \label{eq:P} \\
Q & = \frac{1}{2}\left(\JW{n} - \frac{1}{\lambda_\ell}S\right) \label{eq:Q} \\
A & = \frac{1}{\check{r}+1}\left(\JW{n}  + \rho^{1/2}(S)\right) \label{eq:A} \\
B & = \frac{1}{\check{r}+1}\left(\check{r} \JW{n} - \rho^{1/2}(S)\right) \label{eq:B}
\end{aligned}$$
:::

::: proof
*Proof.* The formulas certainly define idempotents, according to the formulas in Lemma [\[lem:S2\]](#lem:S2){reference-type="ref" reference="lem:S2"} and in Definition [\[def:pa\]](#def:pa){reference-type="ref" reference="def:pa"}. Since $\frac{1}{2}\left(\JW{n} + \frac{1}{\lambda_\ell}S\right)+\frac{1}{2}\left(\JW{n} - \frac{1}{\lambda_\ell}S\right) = \JW{n}$, we know these formulas for $P$ and $Q$ actually define the corresponding idempotents. Note the symmetry between $P$ and $Q$: rescaling $S$ by $-1$ interchanges the formulas for the idempotents. Since $\frac{1}{\check{r}+1}\left(\JW{n}  + \rho^{1/2}(S)\right) + \frac{1}{\check{r}+1}\left(\check{r} \JW{n} - \rho^{1/2}(S)\right) = \JW{n}$, these formulas are indeed the idempotents $A$ and $B$; you can check which is which by taking the trace. ◻
:::

::: lem
[]{#lem:idempotents2 label="lem:idempotents2"} The remaining idempotents on the principal graph are given by $$\begin{aligned}
P' & = P \tensor X - \frac{2[n]}{[2][n+1]} \left((P \tensor X) \circ e_n \circ (P \tensor X)\right) \label{eq:P'} \displaybreak[1]\\
Q' & = Q \tensor X - \frac{2[n]}{[2][n+1]} \left((Q \tensor X) \circ e_n \circ (Q \tensor X)\right) \label{eq:Q'} \displaybreak[1] \\
P'' & = P' \tensor X^* -  \frac{[2][n+1]}{[n+2]-[n]} \left((P' \tensor X^*) \circ e_{n+1} \circ (P' \tensor X^*)\right) \label{eq:P''} \displaybreak[1] \\
\intertext{and}
Q'' & = Q' \tensor X^* -  \frac{[2][n+1]}{[n+2]-[n]} \left((Q' \tensor X^*) \circ e_{n+1} \circ (Q' \tensor X^*)\right).  \label{eq:Q''} 
\end{aligned}$$
:::

::: proof
*Proof.* We know from the principal graph that $P \tensor X \iso \JW{n-1} \directSum P'$ We claim that the second term in the right hand side of Equation [\[eq:P\'\]](#eq:P'){reference-type="eqref" reference="eq:P'"} is the projection onto $\JW{n-1}$, and so the difference is exactly $P'$. In fact, if the second term is a projection at all it must be equivalent to $\JW{n-1}$ as it factors through $n-1$ strands. The partial trace of $P$ is $$\ptr{P} = \frac{[2][n+1]}{2[n]} \JW{n-1}$$ and an easy calculation gives the result. An identical argument for $Q$ instead of $P$ gives Equation [\[eq:Q\'\]](#eq:Q'){reference-type="eqref" reference="eq:Q'"}.

Equations [\[eq:P\'\'\]](#eq:P''){reference-type="eqref" reference="eq:P''"} and [\[eq:Q\'\'\]](#eq:Q''){reference-type="eqref" reference="eq:Q''"} follow similarly. We use that fact that $P' \tensor X^* \iso P \directSum P''$, and calculate $$\ptr{P'} = \left(1-\frac{2[n]}{[2][n+1]}\right) P = \frac{[n+2]-[n]}{[2][n+1]} P$$ from Equation [\[eq:P\'\]](#eq:P'){reference-type="eqref" reference="eq:P'"}. Computing the square of the second term in Equation [\[eq:P\'\'\]](#eq:P''){reference-type="eqref" reference="eq:P''"} confirms that it is a projection, and gives the result. The analogous considerations for $Q'$ instead of $P'$ give Equation [\[eq:Q\'\'\]](#eq:Q''){reference-type="eqref" reference="eq:Q''"}. ◻
:::

::: lem
[]{#lem:idempotents3 label="lem:idempotents3"} The idempotents $C$ and $D$ on the dual principal graph are given by $$\begin{aligned}
C & = \rho^{n/2}(P') \label{eq:C} \\
\intertext{and}
D & = \rho^{n/2}(Q'). \label{eq:D}
\end{aligned}$$
:::

::: proof
*Proof.* The idempotents $C$ and $P'$ are dual, as are $D$ and $Q'$. ◻
:::

The coefficients appearing in Equations [\[eq:P\]](#eq:P){reference-type="eqref" reference="eq:P"} and [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} lie in $\Rational(\lambda_\ell)$ while the coefficients in Equations [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"} through [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"} all lie in $\Rational(D_\ell)$.

This planar algebra gives a possibly incomplete rational form for both even parts over $\Rational(D_\ell)$. Since all of the projections in the dual even part lie in $\Rational(D_\ell)$ we have constructed a complete rational form for the dual even part in $\Rational(D_\ell)$. Finally, since all of the projections in the principal even part lie in $\Rational(\lambda_\ell)$ we have a complete rational form for the principal even part over $\Rational(\lambda_\ell)$.
