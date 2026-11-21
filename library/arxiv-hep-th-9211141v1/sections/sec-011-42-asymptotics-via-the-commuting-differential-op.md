---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-011-42-asymptotics-via-the-commuting-differential-op
section_title: "Asymptotics via the Commuting Differential Operator"
section_number: 4.2
pages: 19-21
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
[]{#subsec:asy_diffop label="subsec:asy_diffop"} We begin with the integral identity $$K(x,y)=\int_0^\infty A(x+z) A(y+z)\, dz \, .
\label{K_identity}$$ This appears in [@clarkson_mcleod1] but we give a simple proof here. Think of ([\[partial_K\]](#partial_K){reference-type="ref" reference="partial_K"}) as a differential equation for the "unknown" function $K(x,y)$. Since $$\left({\partial\over\partial x}+{\partial\over \partial y}\right)
A(x+z) A(y+z) = {\partial\over\partial z} A(x+z) A(y+z)$$ one solution is the right side of ([\[K_identity\]](#K_identity){reference-type="ref" reference="K_identity"}) and, of course, another solution is the Airy kernel $K(x,y)$. The difference is therefore of the form $\varphi(x-y)$ for some function $\varphi$. Since both sides of ([\[K_identity\]](#K_identity){reference-type="ref" reference="K_identity"}) tend to zero as $x$ and $y$ tend to $+\infty$ independently, we must have $\varphi\equiv 0$.

Rewriting ([\[K_identity\]](#K_identity){reference-type="ref" reference="K_identity"}) as $$K(x,y) = \int_s^\infty A(x+z-s) A(z+y-s) \, dz$$ shows that $K$ as an operator on $(s,\infty)$ is the square of the operator with kernel $A(x+y-s)$.

Integration by parts shows that an integral operator with kernel $L(x,y)$ on $(s,\infty)$ commutes with a differential operator $${d\over dx} \alpha(x) {d\over dx} + \beta(x)$$ if $\alpha(s)=0$ and if $$\alpha(y) {\partial^2L\over \partial y^2} + \alpha^\prime(y)
{\partial L\over \partial y} + \beta(y) L =
\alpha(x) {\partial^2 L\over \partial x^2} + \alpha^\prime(x)
{\partial L\over \partial x}+\beta(x) L \, .$$ (Of course we also require, in the end, appropriate vanishing at $\infty$.)  If we set $L(x,y)=A(x+y-s)$ and use the fact $A^{\prime\prime}(x)=xA(x)$ we can easily check that a solution is given by $$\alpha(x)=x-s, \ \ \ \beta(x)=-x(x-s)$$ and so we obtain the commuting differential operator ([\[L_operator\]](#L_operator){reference-type="ref" reference="L_operator"}).

Here is an outline of how ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}) is found. If we let $f_1$, $f_2, \cdots$ denote the eigenfunctions of $L$ then the logarithmic derivative of each $\lambda_i$ (thought of as a function of $s$) is expressible very simply in terms of the corresponding $f_i$. The asymptotics of these eigenfunctions, and so of the logarithmic derivative, is established by WKB techniques. Integrating, and using the fact that each $\lambda_i\rightarrow 1$ as $s\rightarrow -\infty$, gives ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}). The WKB argument we give is quite heuristic although it could very likely be made rigorous.

We make a preliminary change of variables, replacing $x$ by $x+s$ (so that $L$ acts on $(0,\infty)$) and $s$ by $-2t$. The eigenvalue problem can then be written as $$\left(x f^\prime(x)\right)^\prime +\left(\mu-(x-t)^2\right)f(x)=0
\label{eig_eqn1}$$ or in the equivalent form $$x g^{\prime\prime}(x) +\left\lbrack \mu - (x-t)^2 +{1\over 4x}
\right\rbrack g(x)=0\, , \ \ \ \left(g(x)=\sqrt{x} f(x)\right)
\label{eig_eqn2}$$ The eigenvalues satisfy $0<\mu_0<\mu_1<\cdots$ and oscillation considerations applied to ([\[eig_eqn2\]](#eig_eqn2){reference-type="ref" reference="eig_eqn2"}) show that $\mu_i={\rm O}(t^{1/2})$, for each $i$ as $t\rightarrow\infty$. So we think of $\mu$ in our equations as ${\rm O}(t^{1/2})$, we normalize our eigenfunctions so that $f(0)=1$, and proceed to find asymptotics for large $t$.
