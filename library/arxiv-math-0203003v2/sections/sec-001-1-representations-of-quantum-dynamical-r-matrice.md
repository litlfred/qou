---
doc_id: arxiv-math-0203003v2
doc_title: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002"
section_id: sec-001-1-representations-of-quantum-dynamical-r-matrice
section_title: "Representations of Quantum Dynamical R-Matrices with Spectral Parameters"
section_number: 1
pages: 2-4
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.966
doc_brief: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002 — 8 sections: Front matter; Introduction; Representations of Quantum Dynamic"
---
Let $\mathfrak{a}$ be a finite dimensional abelian Lie algebra over , $V$ be a finite dimensional semisimple $\mathfrak{a}$-module, and $\gamma \in \text{$\mathbb{C}$}^*$. The quantum dynamical Yang-Baxter equation with spectral parameter and step $\gamma$ is $$\begin{aligned}
\notag
R^{12}(u_1-u_2,\lambda-\gamma h^{(3)}) R^{13}(u_1-u_3,\lambda) R^{23}(u_2-u_3,\lambda-\gamma h^{(1)})\\ \label{eq:qdybs}
= R^{23}(u_2-u_3,\lambda) R^{13}(u_1-u_3,\lambda-\gamma h^{(2)}) R^{12}(u_1-u_2,\lambda)
\end{aligned}$$ with respect to a meromorphic function $R:\text{$\mathbb{C}$}\times\mathfrak{a}^* \to \text{End}_{\mathfrak{a}}(V\otimes V)$. The notation $h^{(i)}$ means that, for example, $R^{12}(u_1-u_2,\lambda-\gamma h^{(3)})(v_1\otimes v_2\otimes v_3) = \big(R(u_1-u_2,\lambda-\gamma\mu)(v_1\otimes v_2)\big)\otimes v_3$ if $v_3$ has weight $\mu$. A function $R$ is called a quantum dynamical R-matrix if it is a generically invertible solution of [\[eq:qdybs\]](#eq:qdybs){reference-type="eqref" reference="eq:qdybs"}.

Given a quantum dynamical R-matrix $R:\text{$\mathbb{C}$}\times\mathfrak{a}^* \to \text{End}_{\mathfrak{a}}(V\otimes V)$, we denote by $\text{\bf Rep}_{\text{f}}(R)$ the category of meromorphic finite dimensional representations of $R$. This category was first defined in [@Fel94a; @Fel94b]. It consists of pairs $(W,L_{W})$ where $W$ is a semisimple finite dimensional $\mathfrak{a}$-module and $L_{W}$ is a meromorphic function $$L_{W} : \text{$\mathbb{C}$} \times \mathfrak{a}^* \to \text{End}_{\mathfrak{a}}(V\otimes W)$$ such that $L_{W}(u,\lambda)$ is (generically) invertible and satisfies $$\begin{aligned}
\notag
R^{12}(u_1-u_2,\lambda-\gamma h^{(3)}) L_{W}^{13}(u_1-u_3,\lambda) L_{W}^{23}(u_2-u_3,\lambda-\gamma h^{(1)})\\ \label{eq:Ldef}
= L_{W}^{23}(u_2-u_3,\lambda) L_{W}^{13}(u_1-u_3,\lambda-\gamma h^{(2)}) R^{12}(u_1-u_2,\lambda)
\end{aligned}$$ in $\text{End}_{\mathfrak{a}}(V\otimes V\otimes W)$. If $(W,L_{W})$ and $(U,L_{U})$ are two representations, a morphism between them is a meromorphic function $f:\mathfrak{a}^* \to \text{Hom}_{\mathfrak{a}}(W,U)$ such that $$\label{eq:morpdef}
\big(1\otimes f(\lambda)\big)L_{W}(u,\lambda) = L_{U}(u,\lambda)\big(1\otimes f(\lambda - \gamma h^{(1)})\big)$$ Thus, the category $\text{\bf Rep}_{\text{f}}(R)$ is linear over the field $M_V$ of meromorphic functions on $\mathfrak{a}^*$ periodic under the lattice spanned by the weights of $V$.

::: ex
[]{#ex:bex label="ex:bex"} Let $R: \text{$\mathbb{C}$}\times \mathfrak{a}^* \to \text{End}_{\mathfrak{a}}(V\otimes V)$ be a quantum dynamical R-matrix.

1.  []{#ex:trep label="ex:trep"} Let $W$ be any vector space and let $\mathfrak{a}$ act trivially on $W$. Then $(W,1)$, where $1$ denotes the constant function $1\in \text{End}_{\mathfrak{a}}(V\otimes W)$, is a representation of $R$ called the trivial representation associated to $W$.

2.  $(V,R)$ is a representation of $R$ called the basic representation.

3.  []{#ex:isorep label="ex:isorep"} If $(W,L_{W})$ is a representation of $R$, $f:\mathfrak{a}^* \to \text{End}_{\mathfrak{a}}(W)$ is generically invertible and $L_{W}^f = \big(1\otimes f(\lambda)^{-1}\big)L_{W}(u,\lambda)\big(1\otimes f(\lambda -\gamma h^{(1)})\big)$ then $(W,L_{W}^{f})$ is also a representation. It is clear that $f$ provides an isomorphism from $(W,L^f_W)$ to $(W,L_W)$.
:::

::: ex
[]{#ex:felder label="ex:felder"} Let $\mathfrak{a}$ be an abelian $n$-dimensional Lie algebra and $V$ be a semisimple $n$-dimensional $\mathfrak{a}$-module whose weights form a basis for $\mathfrak{a}^*$ (in other words, $\mathfrak{a}$ is the usual Cartan subalgebra of $\mathfrak{gl}_n$ acting naturally on $V=\text{$\mathbb{C}$}^n$). Quantum dynamical R-matrices for such $\mathfrak{a}$ and $V$ are said to be of $\mathfrak{gl}_n$ type [@EtVa98; @EtVa99]. They have the form $$R(u,\lambda) = \sum_{m,l}  \alpha_{m,l}(u,\lambda) E_{m,m}\otimes E_{l,l} + \sum_{m\neq l} \beta_{m,l}(u,\lambda) E_{l,m}\otimes E_{m,l}$$ The main example is the elliptic quantum dynamical R-matrix found by Felder [@Fel94a; @Fel94b] $$R_{\tau,\gamma}^{ell}(u,\lambda) = \sum_{m} E_{m,m}\otimes E_{m,m} + \sum_{m\neq l} \alpha(u,\lambda_{m,l}) E_{m,m}\otimes E_{l,l} + \beta(u,\lambda_{m,l}) E_{l,m}\otimes E_{m,l}$$ with $$\alpha(u,\lambda) = \frac{\vartheta_1(\lambda+\gamma;\tau)}{\vartheta_1(\lambda;\tau)} \frac{\vartheta_1(u;\tau)}{\vartheta_1(u-\gamma;\tau)}\quad\quad \beta(u,\lambda) = \frac{\vartheta_1(\gamma;\tau)}{\vartheta_1(\lambda;\tau)} \frac{\vartheta_1(u-\lambda;\tau)}{\vartheta_1(u-\gamma;\tau)}$$ where $\lambda_{m,l} = \lambda_m - \lambda_l$, and $\vartheta_1$ is the standard first theta function. Felder also proposed to associate to $R^{ell}_{\tau,\gamma}$ an elliptic quantum group $E_{\tau,\gamma/2}({\mathfrak{g}l}_n)$, whose category of finite dimensional representations is $\text{\bf Rep}_{\text{f}}(R^{ell}_{\tau,\gamma})$.
:::

Let $R: \text{$\mathbb{C}$}\times \mathfrak{a}^* \to \text{End}_{\mathfrak{a}}(V\otimes V)$ be a quantum dynamical R-matrix. The category $\text{\bf Rep}_{\text{f}}(R)$ can be endowed with a tensor product functor given by $(W,L_{W})\odot (U,L_{U}) = (W\otimes U,L_{W\odot U})$ where $$L_{W\odot U}(u,\lambda) = L_{W}^{12}(u,\lambda-\gamma h^{(3)})L_{U}^{13}(u,\lambda)$$ on objects and $$f\odot g(\lambda) = f(\lambda-\gamma h^{(2)})\otimes g(\lambda)$$ on morphisms. One easily checks that the first formula defines a representation, and the second one a morphism of representations. Thus, $\odot$ is a bifunctor. Moreover, it is easy to see that it defines a structure of a tensor category on $\text{\bf Rep}_{\text{f}}(R)$, with unit object being the trivial representation $(\text{$\mathbb{C}$},1)$.
