---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-006-25-q-commuting-operators
section_title: "q-commuting operators"
section_number: 2.5
pages: 15-16
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.96
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:pre:qcom}
Throughout the paper, we will consider positive operators $A,B$ satisfying $AB=q^2BA$ for $q=e^{\pi ib^2}, |q|=1$. 

We will realize the operators using the canonical pair $A=e^{2\pi bx}, B=e^{2\pi bp}$ where $p=\frac{1}{2\pi i}\frac{d}{dx}$. Then it is well-known that 
\begin{Prop} Both $A,B$ are positive unbounded operators on $L^2(\R)$ and they are essentially self-adjoint. The domain for $A$ is given by 
\Eq{\cD_A=\{f(x)\in L^2(\R): e^{2\pi bx}f(x) \in L^2(\R)\}}
and the domain for $B$ is given by the Fourier transform of $\cD_A$.
\end{Prop}
Hence we can apply functional calculus and obtain various functions in $A$ and $B$. In particular, for any function defined on $x>0\in\R$ such that $|f(x)|=1$, $f(A)$ will be a unitary operator.

In this paper, we will be using a dense subspace $\cW\sub L^2(\R)$ introduced in \cite{Gon, Sch}.
\begin{Def}\label{WDef}The dense subspace $\cW\sub L^2(\R)$ is the linear span of functions of the form
\Eq{e^{-\a x^2+\b x}P(x),} where $\a,\b\in\C$ with $Re(\a)>0$, and $P(x)$ is a polynomial in $x$.
\end{Def}

Then it is known \cite{Sch} that $\cW$ forms a core for both $A$ and $B$ and it is also stable under Fourier transform. It is obvious that these functions have analytic continuation to the whole complex plane, and they have rapid decay along the real direction. All the operators in the remaining sections will first be defined on $\cW$ and extended by continuity to all of $L^2(\R)$ or its natural domain if the operator is unbounded.

We will also use the notion 
\Eq{\label{WxW}\cW\hat{\ox}\cW\sub L^2(\R\x \R, dsdt),}
where the extra exponent $e^{\c st},\c\in\C$ is allowed.

For convenience, we describe some computations involving $A$ and $B$, and similarly for the operators $\hat{A}$ and $\hat{B}$ with the opposite commutation relations.
\begin{Lem} \label{qqcom} For $AB=q^2BA$, $\hat{A}\hat{B}=q^{-2}\hat{B}\hat{A}$, both $q\inv BA\inv$ and $q\hat{B}\hat{A}\inv$ are positive self-adjoint operators. By the Baker-Campbell-Hausdorff formula
\Eq{e^{2\pi bx}e^{2\pi bp} = e^{2\pi b(x+p)}e^{(2\pi b)^2[x,p]/2}=q e^{2\pi b(x+p)},}
we deduce for example
\Eq{q\inv BA\inv = q\inv e^{2\pi bp}e^{-2\pi bx} = e^{2\pi b(p-x)}.}
Hence we can describe
\Eq{(q\inv BA\inv)^{ib\inv \t} = e^{\pi i\t^2}B^{ib\inv \t}A^{-ib\inv \t}=e^{-\pi i\t^2}A^{-ib\inv \t}B^{ib\inv \t},}
\Eq{(q \hat{B}\hat{A}\inv)^{ib\inv \t} =e^{\pi i\t^2}\hat{A}^{-ib\inv \t}\hat{B}^{ib\inv \t}= e^{-\pi i\t^2}\hat{B}^{ib\inv \t}\hat{A}^{-ib\inv \t}.}
Furthermore we have commutation relations of the form
\Eq{\label{comW1} (B\ox 1) e^{\frac{i}{2\pi b^2}\log A\inv\ox \log \hat{A}} = e^{\frac{i}{2\pi b^2}\log A\inv\ox \log \hat{A}} (B\ox \hat{A}\inv),}
\Eq{\label{comW2} (1\ox \hat{B}) e^{\frac{i}{2\pi b^2}\log A\inv\ox \log \hat{A}} = e^{\frac{i}{2\pi b^2}\log A\inv\ox \log \hat{A}} (A\ox \hat{B}),}
and similar variants.
\end{Lem}
