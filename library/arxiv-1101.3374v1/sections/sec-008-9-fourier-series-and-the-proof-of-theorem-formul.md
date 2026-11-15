---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-008-9-fourier-series-and-the-proof-of-theorem-formul
section_title: "Fourier series and the Proof of Theorem ??, formula (3)"
section_number: 9
pages: 48-56
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.942
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
[]{#sec:B' label="sec:B'"}

-.2in -.2in

In the proofs of formulas (1) and (2) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, we needed to find a 1-form $\alpha$ on $T^3$ whose exterior derivative is the exact 2-form $\omega_L$ associated with the three-component link $L$ in $S^3$. We asserted that we can choose $\alpha=\delta(\varphi* \omega_L)$, where $\varphi$ is the fundamental solution of the scalar Laplacian on $T^3$. Furthermore, we asserted that this choice of $\alpha$ is canonical in the sense that it has the smallest $L^2$ norm among all possible choices. We justify these assertions in this section and lay the groundwork for the proof of formula (3) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} by studying the calculus of differential forms on $T^3=(\mathbb R/2\pi\mathbb Z)^3$ in terms of their Fourier series.

We will prove the following two results:

::: proposition
[]{#prop:fs label="prop:fs"} **  The fundamental solution of the scalar Laplacian on the\
$3$-torus $T^3 = (\mathbb R/2\pi\mathbb Z)^3$ is given by the formula $$\varphi(\textup{\bf x}) \ = \
{1\over 8\pi^3}\sum_{\textup{\bf n}\ne{\bf 0}}
e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}} / |\textup{\bf n}|^2.$$ The function $\varphi$ is $C^\infty$ at all points $\textup{\bf x}\in T^3$ except ${\bf 0}$, where it becomes infinite.**
:::

::: proposition
[]{#prop:alp label="prop:alp"} **If $\omega$ is any exact differential form on $T^3$ with $C^\infty$ coefficients, then $$\alpha \ = \ \delta(\varphi* \omega)$$ is a $C^\infty$ differential form satisfying $d\alpha=\omega$. Furthermore, if $d\widetilde\alpha=\omega$ as well, then $|\alpha|_{L^2}\le|\widetilde\alpha|_{L^2}$, with equality if and only if $\widetilde\alpha=\alpha$.**
:::

Before diving into calculations, we pause for some words of explanation: We write $\Omega^k(T^3)$ for the space of $C^\infty$ $k$-forms on $T^3$. With $d$ as the exterior differentiation operator taking $\Omega^k(T^3)$ to $\Omega^{k+1}(T^3)$, and $\delta$ the co-differentiation map adjoint to $d$ in the $L^2$ sense, the Laplacian of a $k$-form $\alpha$ is $$\Delta\alpha \ = \ (d\delta+\delta d)\alpha.$$ This definition gives us the "geometer's sign convention" for the Laplacian on functions (0-forms): $$\Delta f \ = \  -\left({\partial^2 f\over\partial x_1^2}+{\partial^2 f\over\partial x_2^2} +
{\partial^2 f\over\partial x_3^2}\right).$$

The *fundamental solution of the scalar Laplacian is a function $\varphi$, convolution with which "inverts" the Laplacian to the extent that this is possible. On $T^3$, only functions that integrate to zero are in the range of the Laplacian, and so "the" fundamental solution of $\Delta$ on $T^3$ is the function $\varphi$ which satisfies $$\int_{T^3}\varphi\,d\!\mathop{\rm vol}\nolimits\ = \  0
\qquad\textup{and}\qquad 
\Delta(\varphi * f) \ = \ f$$ for all $f\in C^\infty(T^3)$ such that $\displaystyle{\int_{T^3}f\,d\!\mathop{\rm vol}\nolimits=0}$.*

Even though we have expressed $\varphi$ in terms of complex exponentials, the value of $\varphi$ is real for real values of $\textup{\bf x}$ because of the symmetry of the coefficients.

Figure [1](#fig:fundsol){reference-type="ref" reference="fig:fundsol"} shows the graph of the corresponding fundamental solution $$\varphi(\textup{\bf x}) \ = \
{1\over 4\pi^2}\sum_{\textup{\bf n}\ne{\bf 0}} e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}} /  |\textup{\bf n}|^2$$ of the scalar Laplacian on the 2-torus $S^1 \times S^1$, summed for $|\textup{\bf n}| \leq 10$, and displayed over the range $[-3\pi,3\pi]\times[-3\pi,3\pi]$.

![Fundamental solution of the scalar Laplacian on $S^1 \times S^1$](FigFundSolDennis.pdf){#fig:fundsol height="260pt"}

With respect to the $L^2$ inner product $$\langle f,g\rangle \ = \  \int_{T^3}f(\textup{\bf x})\,\overline{g(\textup{\bf x})}\,d\textup{\bf x}\,,$$ the set of complex exponentials $\{e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}} \ | \ \textup{\bf n}\in\mathbb Z^3\}$ is an orthogonal set, and for all $\textup{\bf n}$, we have $\langle e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}},e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\rangle = 8\pi^3$.

Any function $f$ in $L^2(T^3)$ can be expanded into a Fourier series $$f\ \sim \ \sum_{\textup{\bf n}\in\mathbb Z^3} c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}$$ where $$c_\textup{\bf n}\ = \ {1\over 8\pi^3}\langle f,e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\rangle \ = \  {1\over 8\pi^3}\int_{T^3} f(\textup{\bf x})\,e^{-i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,d\textup{\bf x}.$$ Moreover, by Plancharel's theorem, the $L^2(T^3)$-norm of $f$ is equal to the $\ell^2$-norm of the sequence of coefficients: $$|f|_{L^2} \ = \  \int_{T^3}|f(x)|^2\,d\textup{\bf x}\ = \  \sum_{\textup{\bf n}\in\mathbb Z^3} 8\pi^3|c_\textup{\bf n}|^2.$$ This shows that the function $\varphi$ of Proposition [\[prop:fs\]](#prop:fs){reference-type="ref" reference="prop:fs"} is in $L^2(T^3)$, since $|c_\textup{\bf n}|^2$ is of order $1/|\textup{\bf n}|^4$, while the number of lattice points at distance $|\textup{\bf n}|$ from ${\bf 0}$ is of order $|\textup{\bf n}|^2$.

Because the range of the scalar Laplacian is the (closed) subspace of functions $f$ for which $$\int_{T^3} f(\textup{\bf x})\,d\textup{\bf x}\ = \ 0\,,$$ we will denote this subspace of $L^2(T^3)$ by $L^2_0(T^3)$, and similarly for other function spaces, where a zero subscript will indicate that all functions in the space have average value zero. In terms of Fourier coefficients, $f\in L^2_0(T^3)$ if and only if the Fourier coefficient $c_{\bf 0}=c_{(0,0,0)}=0$.

For functions $f$ and $g$ in $C^\infty(T^3)$, their ***convolution*** $f*g$ is defined by $$\left(\vphantom{x^2}f*g\right)(\textup{\bf x})\ = \ \int_{T^3}f(\textup{\bf y})\,g(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf y}\,,$$ and also lies in $C^\infty(T^3)$. One checks easily that $e^{i\textup{\bf m}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}*e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}} = 0$ if $\textup{\bf m}\neq \textup{\bf n}$, and $$e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}*e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\ = \ 8\pi^3 e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}.$$ Therefore, if $f$ and $g$ have Fourier series $\sum c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}$ and $\sum d_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}$ respectively, then the Fourier series of $f*g$ is $$8\pi^3\sum_{\textup{\bf n}\in\mathbb Z^3}c_{\textup{\bf n}}d_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}.$$

From this it follows that the operation of convolution satisfies $f*g=g*f$ and $(f*g)*h=f*(g*h)$ whenever all the convolutions are defined. Furthermore, $${\partial\over \partial x_k}(f*g)\ = \ {\partial f\over \partial x_k}*g \ = \  f*{\partial g\over \partial x_k}.$$

For $u\in C^\infty(T^3)$, with $$u(\textup{\bf x})\ = \ \sum_{\textup{\bf n}\in\mathbb Z^3} b_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,,$$ we have $$\Delta u(\textup{\bf x})\ = \ \sum_{\textup{\bf n}\neq{\bf 0}}|\textup{\bf n}|^2b_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}.$$ Because the $(0,0,0)$-coefficient of $\Delta u$ is zero, this shows why in order to solve $\Delta u=f$ we must restrict $f$ to be in $C^\infty_0(T^3)$. And for $f\in C^\infty_0(T^3)$, with $$f(\textup{\bf x})\ = \ \sum_{\textup{\bf n}\neq{\bf 0}}c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}},$$ the unique solution $u\in C^\infty_0(T^3)$ of $\Delta u=f$ has $b_{\textup{\bf n}}= c_\textup{\bf n}/|\textup{\bf n}|^2$, and so, since $$\varphi(\textup{\bf x})\ = \ \frac{1}{8\pi^3}\sum_{\textup{\bf n}\ne{\bf 0}}{e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}}/{|\textup{\bf n}|^2}\,,$$ we conclude that $u=\varphi * f$. This completes the proof of Proposition [\[prop:fs\]](#prop:fs){reference-type="ref" reference="prop:fs"} except for the assertion about the smoothness of $\varphi$ away from its singularity, which follows from well-known local regularity theorems for elliptic partial differential equations (see, for example, Folland [@Folland], Theorem 6.33).

To prove Proposition [\[prop:alp\]](#prop:alp){reference-type="ref" reference="prop:alp"}, we express the calculus of differential forms on $T^3$ in terms of Fourier series. Except for the fundamental solution $\varphi$ of the (scalar) Laplacian on $T^3$, we will assume all functions and forms are $C^\infty$.

We continue to express functions (0-forms) as Fourier series: for $\textup{\bf x}=(s,t,u)$ and $\textup{\bf n}=(n_1,n_2,n_3)$, we write $$f(\textup{\bf x}) \ = \ \sum_{\textup{\bf n}\in\mathbb Z^3}c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\ \in\ \Omega^0(T^3).$$ Likewise, we employ the notation described in the introduction and express 1-forms using $\textup{\bf c}_{\textup{\bf n}}=(c_\textup{\bf n}^{s},c_\textup{\bf n}^{t},c_\textup{\bf n}^{u})$ and $d\textup{\bf x}=(ds,dt,du)$. We write $$\alpha(\textup{\bf x}) \ = \ \sum_{\textup{\bf n}\in\mathbb Z^3}\textup{\bf c}_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}d\textup{\bf x}\ \in\ \Omega^1(T^3).$$ With $\star d\textup{\bf x}=(dt\wedge du,du\wedge ds,ds\wedge dt)$ as before, we can express a 2-form as $$\beta(\textup{\bf x}) \ = \ \sum_{\textup{\bf n}\in\mathbb Z^3}\textup{\bf c}_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}\ \in\ \Omega^2(T^3).$$ Finally, with $dV=ds\wedge dt\wedge du$, a 3-form can be written as $$\gamma(\textup{\bf x}) \ = \ \sum_{n\in\mathbb Z^3}c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}dV\ \in\ \Omega^3(T^3).$$

It is straightforward to express both the exterior derivative $d$ and the codifferential $\delta$ in terms of Fourier coefficients. With $f$, $\alpha$, $\beta$ and $\gamma$ as above, we have $$\begin{array}{lll}
\displaystyle{df \ = \ \sum ic_{\textup{\bf n}}\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}d\textup{\bf x}} &
\mbox{\rm\ and\ } & \delta f \ = \ 0,\\[0.3cm]
\displaystyle{d\alpha \ = \ \sum i\textup{\bf n}\times \textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}} &
\mbox{\rm\ and\ } & \displaystyle{\delta\alpha \ = \ -\sum i\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}},\\[0.3cm]
\displaystyle{d\beta \ = \ \sum i\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}dV} &
\mbox{\rm\ and\ } & \displaystyle{\delta\beta \ = \ \sum i\textup{\bf n}\times\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}
\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}d\textup{\bf x},}\\[0.3cm]
d\gamma \ = \ 0 & \mbox{\rm\ and\ } & 
\displaystyle{\delta\gamma \ = \ -\sum ic_\textup{\bf n}\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}}.
\end{array}$$ Thus, exterior differentiation and co-differentiation are expressed in terms of vector algebraic operations on the Fourier coefficients. From these expressions, we conclude the following about the kernel and image of $d$ and $\delta$:

-   For 0-forms, $$\begin{aligned}
    \ker d &\ = \ \{f \ | \ c_\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }
    \ c_{\bf 0}
    \ \mbox{\rm is arbitrary}\} \ \ \ \\[0.2cm]
    \mathrm{im\,}d\, &\ = \  \{0\} \\[0.2cm]
    \ker \delta &\ = \  \{\mbox{\rm all}\ f\} \\[0.2cm]
    \mathrm{im\,}\delta\, &\ = \  \{f \ | \ c_{\bf 0}=0\}
    \end{aligned}$$

-   For 1-forms, $$\begin{aligned}
    \ker d &\ = \  \{\alpha \ | \ \textup{\bf c}_\textup{\bf n}=\lambda_\textup{\bf n}\textup{\bf n}\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\textup{\bf c}_{\bf 0}
    \ \mbox{\rm is arbitrary}\} \\[0.2cm] 
    \mathrm{im\,}d\, &\ = \  \{\alpha \ | \ \textup{\bf c}_\textup{\bf n}=\lambda_\textup{\bf n}\textup{\bf n}\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},\ \textup{\bf c}_{\bf 0}={\bf 0}\} \\[0.2cm]
    \ker \delta &\ = \  \{\alpha \ | \ \textup{\bf c}_\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\textup{\bf c}_{\bf 0}\ \mbox{\rm is arbitrary}\} \\[0cm]

    \mathrm{im\,}\delta\, &\ = \  \{\alpha \ | \ \textup{\bf c}_\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf n}=0\ \mbox{\rm for}
    \ \textup{\bf n}\ne{\bf 0},\ \textup{\bf c}_{\bf 0}={\bf 0}\}
    \end{aligned}$$

-   For 2-forms, $$\begin{aligned}
    \ker d &\ = \  \{\beta \ | \ \textup{\bf c}_\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\textup{\bf c}_{\bf 0}
    \ \mbox{\rm is arbitrary}\} \\[0.01cm]
    \mathrm{im\,}d\, &\ = \  \{\beta \ | \ \textup{\bf c}_\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},\ \textup{\bf c}_{\bf 0}={\bf 0}\} \\[0cm]
    \ker \delta &\ = \  \{\beta \ | \ \textup{\bf c}_\textup{\bf n}=\lambda_\textup{\bf n}\textup{\bf n}\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\textup{\bf c}_{\bf 0}\ \mbox{\rm is arbitrary}\} \\[0cm]
    \mathrm{im\,}\delta\, &\ = \  \{\beta \ | \ \textup{\bf c}_\textup{\bf n}=\lambda_\textup{\bf n}\textup{\bf n}\ \mbox{\rm for}
    \ \textup{\bf n}\ne{\bf 0},\ \textup{\bf c}_{\bf 0}={\bf 0}\}
    \end{aligned}$$

-   For 3-forms, $$\begin{aligned}
    \ker d&\ = \ \{\mbox{\rm all}\ \gamma\}\\[0.15cm]
    \mathrm{im\,}d\, &\ = \  \{\gamma \ | \ c_{\bf 0}=0\} \\[0.2cm]
    \ker \delta &\ = \  \{\gamma \ | \ c_\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\ c_{\bf 0}
    \ \mbox{\rm is arbitrary}\} \\[0.1cm]
    \mathrm{im\,}\delta\, &\ = \ \{0\}
    \end{aligned}$$

Therefore $\mathrm{im\,}d\subset\ker d$ and $\mathrm{im\,}\delta\subset\ker\delta$, and the following orthogonal (with respect to the $L^2$ inner product) decompositions hold: $$\Omega^k(T^3)\ = \ \ker\delta\oplus\mathrm{im\,}d \ = \ \mathrm{im\,}\delta\oplus\ker d$$ for $k=0,\ldots,3$. The $k$-forms in $\ker d\cap\ker\delta$ are the forms whose Fourier series contain only constant terms. These are called *harmonic $k$-forms because they are in the kernel of the Laplacian $\Delta=d\delta+\delta d$, so we write $\mathop{\rm Har}\nolimits^k(T^3)=\ker d\cap\ker\delta$. We then have the Hodge decomposition $$\Omega^k(T^3)\ = \ \mathrm{im\,}\delta\oplus\mathop{\rm Har}\nolimits^k(T^3)\oplus \mathrm{im\,}d.$$ The Laplacian $\Delta\colon\Omega^k(T^3)\to\Omega^k(T^3)$ preserves this Hodge decomposition, taking $\mathrm{im\,}\delta$ bijectively to itself, killing $\mathop{\rm Har}\nolimits^k(T^3)$, and taking $\mathrm{im\,}d$ bijectively to itself.*

We must show that if $\omega$ is any $C^\infty$ exact differential $k$-form on $T^3$, then the $(k-1)$-form $\alpha=\delta(\varphi*\omega)$ is $C^\infty$ and satisfies $d\alpha=\omega$, and that if $d\widetilde\alpha=\omega$ as well, then $|\alpha|_{L^2}
\le|\widetilde\alpha|_{L^2}$, with equality if and only if $\widetilde\alpha=\alpha$.

Because it is the case we use in Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, we will carry this out specifically for 2-forms. The proofs for 1-forms and 3-forms are essentially the same.

For a 2-form $$\beta\ = \ \sum_{\textup{\bf n}\in\mathbb Z^3}\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}\,,$$ its Laplacian is given by $$\Delta\beta\ = \ \sum_{\textup{\bf n}\ne{\bf 0}}|\textup{\bf n}|^2\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}.$$ We can use convolution with the fundamental solution $\varphi$ of the scalar Laplacian to express the Green's operator, $$\mathop{\rm Gr}\nolimits(\beta)\ = \ \varphi* \beta \ = \  \sum_{\textup{\bf n}\ne {\bf 0}}{\textup{\bf c}_\textup{\bf n}\over|\textup{\bf n}|^2}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}.$$ Clearly the Laplacian $\Delta$ and the Green's operator are inverses of one another when applied to 2-forms $\beta$ with $\textup{\bf c}_{\bf 0}={\bf 0}$, equivalently, to 2-forms $\beta$ orthogonal to $\mathop{\rm Har}\nolimits^2(T^3)$.

To prove Proposition [\[prop:alp\]](#prop:alp){reference-type="ref" reference="prop:alp"}, assume that $\beta$ is exact, that is, $\beta\in\mathrm{im\,}d$. Then $\mathop{\rm Gr}\nolimits(\beta)$ is also exact, hence certainly closed, and therefore $$\beta\ = \ \Delta\mathop{\rm Gr}\nolimits(\beta)\ = \ (d\delta+\delta d)\mathop{\rm Gr}\nolimits(\beta)\ = \ d\delta\mathop{\rm Gr}\nolimits(\beta)\ = \ d\delta(\varphi*\beta).$$ Thus $\alpha=\delta(\varphi*\beta)$ satisfies $d\alpha=\beta$.

If $\widetilde\alpha$ is any other 2-form satisfying $d\widetilde\alpha=\beta$, then $\widetilde\alpha$ differs from $\alpha$ by some closed 2-form, which must be $L^2$-orthogonal to $\alpha$ since $\alpha\in\mathrm{im\,}\delta$. Thus, $|\alpha|_{L^2}\le|\widetilde\alpha|_{L^2}$ by the Pythagorean theorem.

Since the Fourier coefficients of a $C^\infty$ 2-form decrease faster than any negative power of $|\textup{\bf n}|$, we have that $\mathop{\rm Gr}\nolimits(\beta)$ and $\delta\mathop{\rm Gr}\nolimits(\beta)$ will be $C^\infty$ if $\beta$ is. This completes the proof of Proposition [\[prop:alp\]](#prop:alp){reference-type="ref" reference="prop:alp"}.

This formula expresses Milnor's invariant $\mu(L)$ in terms of the Fourier coefficients of $\omega_L$: $$\mu(L)\ = \ 8\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{\textup{\bf a}_\textup{\bf n}\times\textup{\bf b}_\textup{\bf n}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}}{|\textup{\bf n}|^2}$$ where $$\omega_L\ = \ \sum_{\textup{\bf n}\ne{\bf 0}}\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\star d\textup{\bf x}$$ with $\textup{\bf c}_\textup{\bf n}=\textup{\bf a}_\textup{\bf n}+i\textup{\bf b}_\textup{\bf n}$ and with $\textup{\bf a}_\textup{\bf n}$ and $\textup{\bf b}_\textup{\bf n}$ real.

The formula for $\omega_L$ is summed over $\textup{\bf n}\ne{\bf 0}$ because the hypothesis of pairwise linking numbers zero is equivalent to the vanishing of the harmonic component of $\omega_L$, which in turn is equivalent to the vanishing of its Fourier coefficient $\textup{\bf c}_{\bf 0}$.

We begin with formula (1) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} for $\mu(L)$: $$\mu(L)\ = \ {1\over 2}\int_{T^3}\delta(\varphi*\omega_L)\wedge\omega_L.$$ We have $$\varphi*\omega_L\ = \ \sum_{\textup{\bf n}\ne{\bf 0}}\frac{\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}}{|\textup{\bf n}|^2}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\star d\textup{\bf x}\,,$$ and hence, from our table of derivatives and co-derivatives in terms of Fourier series, $$\delta(\varphi*\omega_L)\ = \ \sum_{\textup{\bf n}\ne{\bf 0}} \frac{(\textup{\bf n}\times\textup{\bf c}_\textup{\bf n})\,i\,e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}}{|\textup{\bf n}|^2}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,d\textup{\bf x}.$$ To compute $\delta(\varphi*\omega_L)\wedge\omega_L$, we use the fact that if $\textup{\bf v}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,d\textup{\bf x}$ is a 1-form and $\textup{\bf w}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\! \star \!d\textup{\bf x}$ is a 2-form, then $$(\textup{\bf v}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,d\textup{\bf x})\wedge(\textup{\bf w}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\! \star\!d\textup{\bf x})\ = \ (\textup{\bf v}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf w})\,dV.$$ Thus $$\delta(\varphi*\omega_L)\wedge\omega_L\ = \ \sum_{\textup{\bf m}\ne{\bf 0}}\sum_{\textup{\bf n}\ne{\bf 0}}
\frac{(\textup{\bf n}\times\textup{\bf c}_\textup{\bf n})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf c}_\textup{\bf m}\,ie^{i(\textup{\bf m}+\textup{\bf n})\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}}{|\textup{\bf n}|^2}\,dV.$$ When we insert this double sum into the integral $\mu(L)={1\over 2}\int_{T^3}\delta(\varphi*\omega_L)\wedge\omega_L,$ most of the terms in the summation will integrate to zero, leaving only the terms where $\textup{\bf m}+\textup{\bf n}={\bf 0}$. In those cases, $e^{i(\textup{\bf m}+\textup{\bf n})\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}=e^0=1$ integrates to $8\pi^3$, the volume of $T^3$.

Thus $$\begin{aligned}
\mu(L)&\ = \ 4\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{i(\textup{\bf n}\times\textup{\bf c}_\textup{\bf n})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf c}_{-\textup{\bf n}}}{|\textup{\bf n}|^2} \\
&\ = \ 4\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{i(\textup{\bf c}_\textup{\bf n}\times\textup{\bf c}_{-\textup{\bf n}})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}}{|\textup{\bf n}|^2}
\end{aligned}$$ and it remains to simplify this last series.

Since $\textup{\bf c}_\textup{\bf n}=\textup{\bf a}_\textup{\bf n}+i\textup{\bf b}_\textup{\bf n}$ and since $\omega_L$ is real-valued, we have $\textup{\bf c}_{-\textup{\bf n}} = \overline\textup{\bf c}_\textup{\bf n} = \textup{\bf a}_\textup{\bf n}-i\textup{\bf b}_\textup{\bf n}.$ Hence $$\textup{\bf c}_\textup{\bf n}\times\textup{\bf c}_{-\textup{\bf n}}\ = \ (\textup{\bf a}_\textup{\bf n}+i\textup{\bf b}_\textup{\bf n})\times(\textup{\bf a}_\textup{\bf n}-i\textup{\bf b}_\textup{\bf n})\ = \ 
-2i\,\textup{\bf a}_\textup{\bf n}\times\textup{\bf b}_\textup{\bf n},$$ and therefore $$\begin{aligned}
\mu(L)&\ = \ 4\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{i(\textup{\bf c}_\textup{\bf n}\times\textup{\bf c}_{-\textup{\bf n}})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}}{|\textup{\bf n}|^2}\\
&\ = \ 8\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{(\textup{\bf a}_\textup{\bf n}\times\textup{\bf b}_\textup{\bf n})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}}{|\textup{\bf n}|^2}\,,
\end{aligned}$$ completing the proof of formula (3) and, with it, that of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}.

We used Maple and Matlab to calculate an approximation to Milnor's $\mu$-invariant for the three-component link $L$ in $S^3$ given by $$\aligned
x(s)&\ = \ [\textstyle{4\over 5}\sin s,\cos s,\textstyle{3\over 5}\sin s,0], \\
y(t)&\ = \ [\textstyle{4\over 5}\sin t,0,\cos t,\textstyle{3\over 5}\sin t], \\
z(u)&\ = \ [\textstyle{4\over 5}\sin u,\textstyle{3\over 5}\sin u,0,\cos u],
\endaligned$$ for $s\in[0,2\pi]$, $t\in[0,2\pi]$ and $u\in[0,2\pi]$, which is a concrete realization of the Borromean rings with $\mu=-1$.

![Borromean rings](FigBorRafal.pdf){#fig:bor height="130pt"}

Maple gave the (long, ugly) formula for $\omega_L$ obtained from Proposition [\[prop:char\]](#prop:char){reference-type="ref" reference="prop:char"}, and we used Matlab to calculate approximations to its Fourier coefficients $\textup{\bf c}_\textup{\bf n}$ for divisions of the $s$, $t$ and $u$ intervals into 60 subintervals and for $\textup{\bf n}\in[-15,15]^3$. The approximation of $\mu$ we obtained in this way was $-0.97$.
