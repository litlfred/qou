---
doc_id: arxiv-math-0612592v1
doc_title: "Analytic q -diﬀerence equations"
section_id: sec-001-first-examples-of-q-difference-equations
section_title: "First examples of q-difference equations"
section_number: null
pages: 3-5
source_pdf: 0612592v1.pdf
source_sha256: a5d29fa15a0b74ff
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.959
doc_brief: "Analytic q -diﬀerence equations — 7 sections: Front matter; Difference equations in general; First examples of q-difference equ"
---
This exposition is concerned with the difference field $K=\mathbb{C}(\{z\})$, i.e., the field of convergent Laurent series over $\mathbb{C}$, provided with the automorphism $\phi$ given by $\phi (z)=qz$, where $q$ is a fixed complex number satisfying $0<|q|<1$. In order to define $\phi$ on the algebraic closure $K_\infty =\cup _{n\geq 1} K_n$, with $K_n:=\mathbb{C}(\{z^{1/n}\})$, of $K$ we choose a $\tau \in \mathbb{C}$ with $\Im (\tau )>0$ such that $q=e^{2\pi i \tau}$. Define $q^\lambda$ for $\lambda \in \mathbb{Q}$ (or any $\lambda \in \mathbb{C}$) as $e^{2\pi i\lambda \tau}$. Then the action of $\phi$ on $K_\infty$ is given by $\phi (z^\lambda)=q^\lambda z^\lambda$. The action of $\phi$ on $\widehat{K}=\mathbb{C}((z))$, i.e., the field of the formal Laurent series, and on its algebraic closure $\widehat{K}_\infty =\cup _{n\geq 1}\widehat{K}_n$, with $\widehat{K}_n:=\mathbb{C}((z^{1/n}))$, is defined in a similar way.

Some $q$-difference rings $F=(F,\phi )$ will be considered, namely $\mathbb{C}[z,z^{-1}]$ and $O$, the ring of the holomorphic functions on $\mathbb{C}^*$. A difference module $M=(M,\Phi )$ over a $q$-difference ring $F$ will be a *free* $F$-module of finite rank provided with a bijective additive map $\Phi :M\rightarrow M$ such that $\Phi (f\cdot m)=\phi (f)\cdot \Phi (m)$ for $f\in F,\ m\in M$.

::: examples
$\ $\
(a) $Ke, \Phi (e)=ce,\ c\in \mathbb{ C}^*$. There exists a solution ($\neq 0$) in $K$ $\Leftrightarrow \ c\in q^{\mathbb{Z}}$. Indeed, $\Phi (z^te)=cq^tz^te$. If $c\in q^{\mathbb{Z}}$, then the Picard-Vessiot ring is $K$ itself and the difference Galois group is $\{1\}$.

There exists a solution ($\neq 0$) in $K_n$ $\Leftrightarrow$ $c\in q^{\frac{1}{n}\mathbb{Z}}$. If $c\in q^{\frac{1}{n}\mathbb{Z}}$ with $n$ minimal, then $K_n$ is the Picard-Vessiot ring and the difference Galois group is $\mu _n:=\{a\in \mathbb{C}|\ a^n=1\}$.

In the remaining case, the Picard-Vessiot ring is $K[X,X^{-1}]$ with the action of $\phi$ given by $\phi (X)=c^{-1}X$. The difference Galois group is $\mathbb{G}_m:=\mathbb{C}^*$. It consists of the automorphisms $\sigma$ given by $\sigma (X)=aX$ (for any $a\in \mathbb{C}^*$). We will use the symbol $e(c)$ for this $X$. It can be given an interpretation as multivalued function $z^b$ for a $b$ with $q^b=c^{-1}$.

\(b\) The difference module $U_n:=Ke_1+\cdots +Ke_n$ with $\Phi$ given by the matrix $$\left[\begin{array}{cccc}1&1& &\\ 
                            &1&1 &\\
                            &&&1\\
                            &&& 1 \end{array}\right]$$

is called *unipotent of length $n$*. The Picard-Vessiot ring is $K[X]$, with $\phi (X )=X +1$. The difference Galois group is $\mathbb{G}_a:=\mathbb{C}$. The elements $\sigma$ of this group have the form $\sigma (X )=X +a$ (any $a\in \mathbb{C}$). We will use the symbol $\ell$ for this $X$. It has an interpretation as multivalued function $\frac{\log z}{2\pi i \tau}$. For $n=2$ one easily verifies that the solution space has $\mathbb{C}$-basis $\{e_1-\ell e_2,\ e_2\}$. $\square$
:::

A difference module $M$ over $K$ is called *regular singular* if $M$ has a basis $e_1,\dots ,e_m$ such that $\mathbb{C}\{z\}e_1+\cdots +\mathbb{C}\{z\}e_m$ is invariant under $\Phi$ and $\Phi ^{-1}$.

::: theorem
The following are equivalent\
(i) $M$ regular singular.\
(ii) $M=K\otimes _{\mathbb{C}}W$, $\dim _{\mathbb{C}}W < \infty$ and $\Phi (f\otimes w)=\phi (f)\otimes A(w)$ for some $A\in {\rm GL}(W)$. Moreover, there is a unique $A$ such that every eigenvalue $c$ satisfies $|q|<|c|\leq 1$.\
(iii) $M$ is obtained by $\oplus ,\otimes$ from the examples in 2.1.
:::

The difference module $(Ke,\ \Phi e=(-z)e)$ is the basic example of an *irregular singular* difference module. Its Picard-Vessiot ring is $K[X,X^{-1}]$ with $\phi (X)=(-z)^{-1}X$. The difference Galois group is $\mathbb{G}_m$. We will use the symbol $e(-z)$ for this $X$. It has the interpretation $\Theta (z):=\sum _{n\in \bf Z}q^{n(n-1)/2}(-z)^n$ because of the well known formula $(-z)\Theta (qz)=\Theta (z)$.
