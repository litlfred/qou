---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-006-acknowledgements
section_title: "Acknowledgements"
section_number: null
pages: 6-12
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.965
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
The authors would like to thank Jorgen Andersen, Sergei Gukov, Rinat Kashaev, Maxim Kontsevich, Pavel Putrov and Matthias Storzer for enlightening conversations. S.G. wishes to thank the University of Geneva for their hospitality during his visit in the summer of 2021. The work of J.G. has been supported in part by the NCCR 51NF40-182902 "The Mathematics of Physics" (SwissMAP). The work of M.M. has been supported in part by the ERC-SyG project "Recursive and Exact New Quantum Theory\" (ReNewQuantum), which received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation program, grant agreement No. 810573. The work of C.W. has been supported by the Max-Planck-Gesellschaft.

# The $\mathbf{4}_1$ knot {#sec.41}

## A $2 \times 2$ matrix of $q$-series {#sub.41q2}

In this section we recall in detail what is known about the resurgence of the two asymptotic series of the $\mathbf{4}_1$ knot, labeled by the geometric and the complex-conjugate flat connections. As explained in the introduction, the answer is determined by a $2 \times 2$ matrix of $q$-series which was discovered in a long story and in several stages in a series of papers [@GZ:qseries; @GK:qseries; @GGM:resurgent; @GGM:peacock]. A detailed description of the numerical discoveries and coincidences is given in [@GZ:qseries] and will not be repeated here. In that paper, the following pair of $q$-series $G^{(j)}(q)$ for $j=0,1$ was introduced and studied by the first author and Zagier [@GZ:qseries] $$\label{G01}
\begin{aligned}
G^{(0)}(q) &=
\sum_{n\geq0}(-1)^{n}\frac{q^{n(n+1)/2}}{(q;q)_{n}^{2}} \\
G^{(1)}(q) &=
\sum_{n\geq0}\left(n+\frac{1}{2}-2E_{1}^{(n)}(q)\right)(-1)^{n}
\frac{q^{n(n+1)/2}}{(q;q)_{n}^{2}} 
\end{aligned}$$ where $$\label{Ek}
E_{k}^{(n)}(q) = \sum_{s=1}^{\infty}s^{k-1}\frac{q^{s(n+1)}}{1-q^{s}} \,.$$ These series were found to be connected to the $\mathbf{4}_1$ knot in at least two ways, discussed in detail in [@GZ:qseries]. On the one hand, they express bilinearly the Andersen-Kashaev state-integral [@GK:qseries] and the total 3D-index of Dimofte-Gaiotto-Gukov [@DGG2]. On the other hand, their radial asymptotics as $q=e^{2\pi {\rm i}\tau} \to 1$ (where $\tau$ is in a ray in the upper half-plane) is a linear combination of the two asymptotic series $\Phi^{(\sigma_1)}(\tau)$ and $\Phi^{(\sigma_2)}(\tau)$ of the Kashaev invariant, where $\sigma_1$ is the geometric representation of the fundamental group of the knot complement and $\sigma_2$ is the complex conjugate. The resurgence of the factorially divergent asymptotic series $\Phi^{(\sigma_1)}(\tau)$ and $\Phi^{(\sigma_2)}(\tau)$, including a complete description of the Stokes automorphism and the Borel resummation was given by the first three authors in [@GGM:resurgent]. Surprisingly, the Stokes matrices were expressed bilinearly in terms of a $2 \times 2$ matrix of explicit descendant $q$-series whose definition we now give. Consider the linear $q$-difference equation $$\label{41rec}
f_m(q) + (q^{m+1}-2) f_{m+1}(q) + f_{m+2}(q) = 0 \qquad (m \in \mathbbm Z) \,.$$ In [@GGM:resurgent] it was shown that it has a

basis of solutions $G^{(j)}_m(q)$ for $j=1,2$ given by [^1] $$\label{Gm01}
\begin{aligned}
G_{m}^{(0)}(q) &=
\sum_{n\geq0}(-1)^{n}\frac{q^{n(n+1)/2}}{(q;q)_{n}^{2}}q^{mn}\\
G_{m}^{(1)}(q) &=
\sum_{n\geq0}\left(n+m+\frac{1}{2}-2E_{1}^{(n)}(q)\right)(-1)^{n}
\frac{q^{n(n+1)/2}}{(q;q)_{n}^{2}}q^{mn}
\end{aligned}$$ where $E_{k}^{(n)}(q)$ are as in Equation [\[Ek\]](#Ek){reference-type="eqref" reference="Ek"}. Note that $G_0^{(j)}(q)=G^{(j)}(q)$, and that $G^{(j)}_m(q) \in \mathbbm Z((q))$ are Laurent series in $q$ (with finitely many negative powers of $q$), meromorphic on $|q|<1$ with only possible pole at $q=0$. We will extend them to analytic functions on $|q| \neq 1$ by $$G_m^{(j)}(q^{-1}) = (-1)^{i}G^{(j)}_{-m}(q),\qquad j=0,1.
  \label{eq:Gmj-cn}$$ The $2 \times 2$ matrix is given by $\mathbf J^\mathrm{red}(q) = \mathbf J^\mathrm{red}_{-1}(q) \bigl(\smallmatrix 0&-2\\1&-1\endsmallmatrix\bigr)$ where $$\label{Jqred}
\mathbf J^\mathrm{red}_{m}(q) =
\begin{pmatrix}
G_{m}^{(1)}(q) & G_{m+1}^{(1)}(q)\\
G_{m}^{(0)}(q) & G_{m+1}^{(0)}(q)\\
\end{pmatrix}$$ coincides with the transpose of the matrix $W_m(q)$ of [@GGM:peacock Eqn.(48)] after interchanging of the two rows. A complete description of the resurgent structure of the series $\Phi^{(\sigma_j)}(\tau)$ for $j=0,1$, of their Borel resummation and their expression in terms of a $2 \times 2$ matrix of state-integrals (with one distinguished entry being the Andersen--Kashaev state-integral [@AK]) was given in [@GGM:resurgent; @GGM:peacock].

## A $3 \times 3$ matrix of $q$-series {#sub.41q3}

In this section we define the promised $3 \times 3$ matrix of $q$-series $\mathbf J^\mathrm{red}_{m}(q)$ and give several algebraic properties thereof. In his forthcoming thesis, the fourth author introduced the series $G^{(2)}(q)$ $$\label{G2}
G^{(2)}(q) =
\sum_{n\geq0}\left(\frac{1}{2}\left(n+\frac{1}{2}-2E_{1}^{(n)}(q)\right)^2
  -E_{2}^{(n)}(q)
  -\frac{1}{24}E_{2}(q)\right)(-1)^{n}\frac{q^{n(n+1)/2}}{(q;q)_{n}^{2}}$$ which is the coefficient of $\varepsilon^2$ in the $\varepsilon$-deformed $q$-series $$\label{G41epsilon}
G(q,\varepsilon)= e^{-\varepsilon^{2}\frac{E_{2}(q)}{24}}
\sum_{n=0}^{\infty}(-1)^{n}\frac{q^{n(n+1)/2}e^{(n+1/2)\varepsilon}}{(qe^{\varepsilon};q)_{n}^{2}}
    = 
    \sum_{k=0}^{\infty}G^{(k)}(q)\varepsilon^{k}$$ which appears in [@GZ:qseries]. Here, $E_2(q)=1-24E_2^{(0)}(q)$. Adding the descendant variable $m \in \mathbbm Z$, leads to the $q$-series $$\label{Gm2}
G_{m}^{(2)}(q) =
\sum_{n\geq0}\left(\frac{1}{2}\left(n+m+\frac{1}{2}-2E_{1}^{(n)}(q)\right)^2
  -E_{2}^{(n)}(q)
  -\frac{1}{24}E_{2}(q)\right)(-1)^{n}\frac{q^{n(n+1)/2}}{(q;q)_{n}^{2}}q^{mn}$$ As in the case of $G_{m}^{(j)}(q)$ for $j=0,1$, it is a meromorphic function on $|q|<1$ with only possible pole at $q=0$, and extends to an analytic function on $|q|>1$ satisfying [\[eq:Gmj-cn\]](#eq:Gmj-cn){reference-type="eqref" reference="eq:Gmj-cn"} with $j=2$.

The sequence $G_{m}^{(2)}(q)$ is a solution of the inhomogenous equation obtained by replacing the right hand side of [\[41rec\]](#41rec){reference-type="eqref" reference="41rec"} by $1$. This follows easily by using creative telescoping of the theory of $q$-holonomic functions implemented by Koutschan [@Koutschan:holofunctions].

We can assemble the three sequences of $q$-series into a matrix $$\label{Jq}
\mathbf J_{m}(q) =
\begin{pmatrix}
1 & G_{m}^{(2)}(q) & G_{m+1}^{(2)}(q)\\
0 & G_{m}^{(1)}(q) & G_{m+1}^{(1)}(q)\\
0 & G_{m}^{(0)}(q) & G_{m+1}^{(0)}(q)\\
\end{pmatrix}$$ whose bottom-right $2 \times 2$ matrix is $\mathbf J^\mathrm{red}_{m}(q)$. The next theorem summarises the properties of $\mathbf J_{m}(q)$.

::: theorem
[]{#thm.41bJ1 label="thm.41bJ1"} The matrix $\mathbf J_{m}(q)$ is a fundamental solution to the linear $q$-difference equation $$\label{41Jqrec}
\mathbf J_{m+1}(q) = \mathbf J_{m}(q) A(q^m,q), \qquad A(q^m,q)=
\begin{pmatrix}
1 & 0 & 1\\
0 & 0 & -1\\
0 & 1 & 2-q^{m+1}\\
\end{pmatrix} \,,$$ has $\det(\mathbf J_m(q))=-1$ and satisfies the analytic extension $$\label{Jmqq}  
  \mathbf J_m(q^{-1}) =
  \begin{pmatrix}
    1&0&0\\
    0&-1&0\\
    0&0&1
  \end{pmatrix} \mathbf J_{-m-1}(q)
  \begin{pmatrix}
    1&0&0\\
    0&0&1\\
    0&1&0
  \end{pmatrix} \,.$$
:::

::: proof
*Proof.* Equation [\[41Jqrec\]](#41Jqrec){reference-type="eqref" reference="41Jqrec"} follows from the fact the last two rows of $\mathbf J_m(q)$ are solutions of the $q$-difference equation [\[41rec\]](#41rec){reference-type="eqref" reference="41rec"} and the first is a solution of the corresponding inhomogenous equation. Moreover, the block form of $\mathbf J_m(q)$ implies that $\det(\mathbf J_m(q))=\det(\mathbf J^\mathrm{red}_m(q))=-1$ where the last equality follows from [@GGM:resurgent eq. (14)]. Equation [\[Jmqq\]](#Jmqq){reference-type="eqref" reference="Jmqq"} follows from the fact that all three sequences of $q$-series satisfy [\[eq:Gmj-cn\]](#eq:Gmj-cn){reference-type="eqref" reference="eq:Gmj-cn"}. ◻
:::

We now give the inverse matrix of $\mathbf J_m(q)$ in terms of Appell-Lerch like sums. The latter appear curiously in the mock modular forms and the meromorphic Jacobi forms of Zwegers [@Zwegers:thesis], and in [@DMZ:blackholes].

::: theorem
[]{#thm.41bJ2 label="thm.41bJ2"} We have $$\label{Jqinv}
\mathbf J_{m}(q)^{-1} =
\begin{pmatrix}
1 & L_{m}^{(0)}(q) & -L_{m}^{(1)}(q)     \\
0 & -G_{m+1}^{(0)}(q) & G_{m+1}^{(1)}(q) \\
0 & G_{m}^{(0)}(q) & -G_{m}^{(1)}(q)
\end{pmatrix}$$ for the $q$-series $L_m^{(j)}(q)$ ($j=0,1$) defined by $$\label{L12}
\begin{aligned}
L^{(0)}_{m}(q) &=
G_{m+1}^{(0)}(q)G_{m}^{(2)}(q)-G_{m}^{(0)}(q)G_{m+1}^{(2)}(q)
\\
L_{m}^{(1)}(q) &=
G_{m+1}^{(1)}(q)G_{m}^{(2)}(q)-G_{m}^{(1)}(q)G^{(2)}_{m+1}(q) \,.
\end{aligned}$$ The $q$-series $L_m^{(j)}(q)$ are expressed in terms of Appell-Lerch type sums: $$\label{Lm}
  \begin{aligned}
L^{(0)}_{m}(q) &=
2E_{1}^{(0)}(q)-1-m+
\sum_{n=1}^{\infty}(-1)^{n}\frac{q^{n(n+1)/2}}{(q;q)_{n}^{2}}\frac{q^{mn+n}}{1-q^{n}}
\\
L_{m}^{(1)}(q) &=
-\frac{3}{8}-2E_{1}^{(0)}(q)^{2}+2E_{1}^{(0)}(q)-E_{2}^{(0)}(q)
-\frac{1}{24}E_{2}(q)+2mE_{1}^{(0)}(q)-m-\frac{m^{2}}{2}
\\
&+\sum_{n=1}^{\infty}(-1)^{n}\frac{q^{n(n+1)/2}}{(q)_{n}^{2}}
\frac{q^{mn+n}}{1-q^{n}}\left(n+m+\frac{1}{2}-2E^{(n)}_{1}(q)+\frac{1}{1-q^{n}}\right)
\,.
\end{aligned}$$
:::

::: proof
*Proof.* Since $\mathbf J^\mathrm{red}_{m}(q)$ is a $2 \times 2$ matrix with determinant $-1$, it follows that the inverse matrix $\mathbf J_{m}(q)^{-1}$ is given by [\[Jqinv\]](#Jqinv){reference-type="eqref" reference="Jqinv"} for the $q$-series $L_m^{(j)}(q)$ ($j=0,1$) given by [\[L12\]](#L12){reference-type="eqref" reference="L12"}.

Observe that $A(q^m,q)$ has first column $(1,0,0)^t$, first row $(1,0,1)$, and the remaining part is a companion matrix. It follows that its inverse matrix has first column $(1,0,0)^t$ and first row $(1,1,0)$. This, together with [\[41Jqrec\]](#41Jqrec){reference-type="eqref" reference="41Jqrec"} implies that

$$\mathbf J_{m+1}(q)^{-1} = A(q^m,q)^{-1} \mathbf J_{m}(q)^{-1} =
\begin{pmatrix}
1 & 1 & 0\\
0 & 2-q^{m+1} & 1\\
0 & -1 & 0\\
\end{pmatrix}
\mathbf J_{m}(q)^{-1} \,.$$ It follows that $L_m^{(j)}(q)$ satisfy the first order inhomogeneous linear $q$-difference equation

$$L^{(j)}_{m-1}(q)-L^{(j)}_{m}(q) =
G_{m}^{(j)}(q)  \qquad (j=0,1) \,.$$ Let $\mathcal L^{(0)}_m(q)$ denote the right hand side of the top Equation [\[Lm\]](#Lm){reference-type="eqref" reference="Lm"}. Then we have $$\mathcal L^{(0)}_{m-1}(q)-\mathcal L^{(0)}_{m}(q)
=
1+\sum_{n=1}^{\infty}(-1)^{n}\frac{q^{n(n+1)/2}}{(q)_{n}^{2}}\frac{q^{mn}-q^{mn+n}}{1-q^{n}}
=
G_{m}^{(0)}(q).$$ Therefore $\mathcal L^{(0)}_{m}(q)-L_{m}^{(0)}(q)$ is independent of $m$. Moreover, $\lim_{m \to \infty} \mathcal L^{(0)}_{m}(q)-L_{m}^{(0)}(q)=0$. The top part of Equation [\[Lm\]](#Lm){reference-type="eqref" reference="Lm"} follows.

Likewise, let $\mathcal L^{(1)}_m(q)$ denote the right hand side of the bottom part of Equation [\[Lm\]](#Lm){reference-type="eqref" reference="Lm"}. Then we have

$$\begin{aligned}
\mathcal L^{(1)}_{m-1}(q)-\mathcal L^{(1)}_{m}(q)
=&
\sum_{n=1}^{\infty}(-1)^{n}\frac{q^{n(n+1)/2}}{(q)_{n}^{2}}
\frac{q^{mn}-q^{mn+n}}{1-q^{n}}\left(n+m+\frac{1}{2}
  -2E^{(n)}_{1}(q)+\frac{1}{1-q^{n}}\right)\\
&-\sum_{n=1}^{\infty}(-1)^{n}\frac{q^{n(n+1)/2}}{(q)_{n}^{2}}
\frac{q^{mn}}{1-q^{n}}+m+\frac{1}{2}-2E^{(0)}_{1}(q)\\
=&\:
G^{(1)}_{m}(q) \,.
\end{aligned}$$ Therefore $\mathcal L^{(1)}_{m}(q)-L^{(1)}_{m}(q)$ is independent of $m$. Moreover, $\lim_{m \to \infty} \mathcal L^{(1)}_{m}(q)-L_{m}^{(1)}(q)=0$. Equation [\[Lm\]](#Lm){reference-type="eqref" reference="Lm"} follows. ◻
:::

## The $\Phi^{(\sigma_0)}(\tau)$ asymptotic series {#sub.413Phi}

The $\mathbf{4}_1$ knot has three asymptotic series $\Phi^{(\sigma_j)}(\tau)$ for $j=0,1,2$ corresponding to the trivial flat connection $\sigma_0$, the geometric flat connection $\sigma_1$ and its complex conjugate $\sigma_2$. The asymptotic series $\Phi^{(\sigma_j)}(\tau)$ for $j=1,2$ are defined in terms of perturbation theory of a state-integral [@DG] and can be computed via formal Gaussian integration in a way that was explained in detail in [@GGM:resurgent] and in [@GZ:kashaev] and will not be repeated here. They have the form $$\Phi^{(\sigma_j)}(\tau) = e^{\tfrac{V(\sigma_j)}{2\pi{\rm i}\tau}}

  \varphi^{(\sigma_j)}(\tau)
  ,\quad j=1,2,$$ where $$V(\sigma_1) = -V(\sigma_2) = {\rm i}\text{Vol}(\mathbf{4}_1)
  = {\rm i}2\text{Im} \mathrm{Li}_2({\rm e}^{{\rm i}\pi/3}) = {\rm i}2.029883\ldots,$$ with $\text{Vol}(\mathbf{4}_1)$ being the hyperbolic volume of $S^3\backslash \mathbf{4}_1$, and $\varphi^{(\sigma_1)}(\tau/(2\pi{\rm i}))$ is a power series with algebraic coefficients with first few terms $$\varphi^{(\sigma_1)}(\tfrac{\tau}{2\pi{\rm i}})
  = 3^{-1/4}\left(
    1+\frac{11\tau}{72\sqrt{-3}}
    +\frac{697\tau^2}{2(72\sqrt{-3})^2}+\ldots\right)$$ (a total of 280 terms have been computed), while $\varphi^{(\sigma_2)}(\tau) = {\rm i}\varphi^{(\sigma_1)}(-\tau)$.

We now discuss the new series $\varphi^{(\sigma_0)}(\tau) \in \mathbbm Q[[\tau]]$ corresponding to the zero volume $V(\sigma_0)=0$ trivial flat connection. This series can be defined and computed (for any knot) using either the colored Jones polynomial or the Kashaev invariant. Let us recall how this works.

Let $J_n(q) \in \mathbbm Z[q^{\pm 1}]$ denotes the Jones polynomial colored by the $n$-dimensional irreducible representation of $\mathfrak{sl}_2$, and normalised to $1$ at the unknot. Setting $q=e^h$, one obtains a power series in $h$, whose coefficient of $h^k$ is a polynomial in $n$ of degree at most $k$. In other words, we have $$\label{Jnq}
J_n(e^h) = \sum_{i=0}^\infty \sum_{j=0}^i a_{i,j} n^j h^i \in \mathbbm Q[[n,h]]$$ where $a_{i,j}$ depends on the knot and, as the knot varies, defines a Vassiliev invariant of type (i.e., degree) $i$ [@Bar-Natan]. Then, the perturbative series $\varphi^{(\sigma_0)}(\tau)$ is given by $$\label{phi0h}
\varphi^{(\sigma_0)}(\tau) = \sum_{i=0}^\infty a_{i,0} \tau^i \,.$$ With this definition, to compute the coefficient of $\tau^k$ in $\varphi^{(\sigma_0)}(\tau)$, one needs to compute the first $k$ colored Jones polynomials $J_n(e^h)$ for $k =1, \dots, n$ up to $O(h^{k+1})$, polynomially interpolate and extract the coefficient $a_{k,0}$. An efficient computation of the colored Jones polynomial is possible if one knows a recursion relation with respect to $n$ (such a relation always exists [@GL]) together with some initial conditions. This gives a polynomial time algorithm to compute $J_n(e^h)+O(h^{k+1})$.

An alternative method is the so-called loop expansion of the colored Jones polynomial $$\label{Jnqloop}
J_n(e^h) = \sum_{\ell=0}^\infty \frac{P_\ell(x)}{\Delta(x)^{2\ell+1}} h^\ell \in
\mathbbm Z[x^{\pm 1}, \Delta(x)^{-1}][[h]]$$ where $x=q^n=e^{n h}$ and $\Delta(x) \in \mathbbm Z[x^{\pm 1}]$ is the Alexander polynomial of the knot. This expansion was introduced by Rozansky [@Rozansky:bureau] (see also Kricker [@Kricker] and [@GK:noncommutative]) and it is related to the Vassiliev power series expansion [\[Jnq\]](#Jnq){reference-type="eqref" reference="Jnq"} by $$\label{Jnqresum}
\sum_{k=0}^\infty a_{\ell+k,k} h^k= \frac{P_\ell(e^h)}{\Delta(e^h)^{2\ell+1}} \,.$$ Then the perturbative series $\varphi^{(\sigma_0)}(\tau)$ is given in terms of the loop expansion by

$$\label{phi0hloop}
\varphi^{(\sigma_0)}(\tau) = \sum_{\ell=0}^\infty P_\ell(1) h^\ell$$

as follows from the above equations together with the fact that $\Delta(1)=1$.

A third method uses a theorem of Habiro [@Habiro:sl2; @Habiro:WRT] which lifts the Kashaev invariant of a knot to an element of the Habiro ring $\widehat{\mathbbm Z[q]} = \varprojlim \;\Bbb Z[q]/((q;q)_n)$. There is a canonical ring homomorphism $\widehat{\mathbbm Z[q]} \to \mathbbm Z[[h]]$ defined by $q \mapsto e^h$, which sends $(q;q)_n$ to $(-1)^n h^n + O(h^{n+1})$ and the image of the lifted element of the Habiro ring under this homomorphism equals to the series $\varphi^{(\sigma_0)}(h)$. For the case of the $\mathbf{4}_1$ knot, the corresponding element of the Habiro ring is given by $$\label{hab41}
\sum_{n=0}^\infty (q;q)_n (q^{-1};q^{-1})_n$$ and its expansion when $q=e^h$ gives the power series with first few terms $$\varphi^{(\sigma_0)}
  (\tfrac{\tau}{2\pi{\rm i}})=
  1-\tau^2+\frac{47}{12}\tau^4+\ldots.$$

We end this section with a comment. Going back to the case of a general knot, it was shown in [@GK:desc] that the colored Jones polynomial is equivalent (in the sense of knot invariants) to a descendant sequence of colored Jones polynomials and of Kashaev invariants (indexed by the integers) which is $q$-holonomic. These descendant Kashaev invariants play a key role in extending matrices of periodic functions whose rows and columns are indexed by nonrtivial flat connections to a matrix that includes the trivial flat connection. This is explained in detail in [@GZ:kashaev].

[^1]: $G_m^{(1)}(q)$ defined here is one half of $G^1_m(q)$ in [@GGM:resurgent].
