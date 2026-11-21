---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-012-33-proof-of-proposition-212-and-properties-of-mo
section_title: "Proof of Proposition 2.12 and properties of modular categories"
section_number: 3.3
pages: 12-13
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.98
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
It is well known (see \cite{BaKi}) that the matrix $T$ is diagonal
with eigenvalues being roots of unity. So we only need to show that 
the S-matrix is unitary. The entries $s_{ij}$ of the S-matrix are known to 
satisfy $s_{ij}=s_{ji}$, and $\sum_j s_{i^*j}s_{jl}=\delta_{il}$ 
(\cite{BaKi}). So it suffices to show that $s_{i^*j}=\overline{s_{ij}}$. 

Recall that $s_{j0}=\pm \dim(V_j)/\sqrt{D}$, where $D$ is the global dimension of 
the category. So $s_{j0}$ is a real number. 
Further, by the Verlinde formula (\cite[3.1]{BaKi}), 
if $\mathbf v_m$ is the $m$-th column of $S$ then 
$$
N_i\mathbf v_m=\frac{s_{im}}{s_{0m}}\mathbf v_m, 
$$
for all $i$. Let $\mathbf v_m^*$ denote the row 
vector, Hermitian adjoint to $\mathbf v_m$. 
Then 
$$
\mathbf v_m^*N_i\mathbf v_m=\frac{s_{im}}{s_{0m}}|\mathbf v_m|^2.
$$
One the other hand, since $N_i^T=N_{i^*}$, and $N_i$ is real, we have
$$
\mathbf v_m^*N_i\mathbf v_m=(N_i^T\mathbf v_m)^*\mathbf v_m=(N_{i^*}\mathbf v_m)^*\mathbf v_m=
(\frac{s_{i^*m}}{s_{0m}}\mathbf v_m)^*\mathbf v_m=
\frac{\overline{s_{i^*m}}}{s_{0m}}|\mathbf v_m|^2.
$$
Since $|\mathbf v_m|^2\ne 0$, the statement is proved. 

\begin{remark}
An important property of modular categories is 

\begin{proposition}\label{moddivi} (\cite{EG4}, Lemma 1.2) The dimension 
of every simple object of a modular category divides 
$\sqrt{D}$, where $D$ is the global dimension 
of the category. 
\end{proposition} 

This implies that in a ribbon category, dimensions of objects 
divide the global dimension (this is seen by taking the Drinfeld center 
and using Theorem \ref{dualcat} and 
the well known fact that the Drinfeld center of 
a braided category contains the original category). This fact is useful 
in classification of modular categories (See section 8).  
\end{remark}

In conclusion of this subsection let us give a simple application 
of Theorem \ref{posi} to modular categories. 

Let $c\in {\mathbb C}/8{\mathbb Z}$ be the Virasoro central
charge of a modular category $\mC$, defined by the relation 
$(ST)^3=e^{2\pi ic/8}S^2$ 
(see \cite{BaKi}), and $D$ be the global dimension of 
$\mC$. Let $f: (-\infty,1]\to [1,\infty)$ be the inverse function to 
the monotonely decreasing function $g(x)=(3-x)\sqrt{x}/2$. 

\begin{proposition} One has
$$
D\ge f({\rm sign}(s_{00})\cos(\pi c/4))
$$
\end{proposition}

\begin{remark} The number $s_{00}$ equals $\pm 1/\sqrt{D}$.\end{remark}

\begin{proof} We need to show that
$$
{\rm sign}(s_{00})\cos(\pi c/4)\ge (3-D)\sqrt{D}/2
$$
To prove this, recall \cite{BaKi} that the number $e^{\pi ic/4}$ can be
expressed via a Gaussian sum:
$$
{\rm sign}(s_{00})e^{\pi i c/4}=\sum |X_i|^2\theta_i/\sqrt{D}, 
$$
where $\theta_i$ are the twists. 
This means that 
$$
{\rm sign}(s_{00})e^{\pi i c/4}-D^{-1/2}=
\sum_{i\ne 0} |X_i|^2\theta_i/\sqrt{D}. 
$$
Taking squared absolute values of both sides, and using that $|\theta_i|=1$, 
and $|X_i|^2>0$ (by Theorem \ref{posi}), we get 
$$
|{\rm sign}(s_{00})
e^{\pi ic/4}-D^{-1/2}|^2\le (\sum_{i\ne 0}|X_i|^2)^2/D=\frac{(D-1)^2}{D}.
$$
After simplifications, this yields the desired inequality.
\end{proof}

\begin{remark} Sometimes this inequality sharp. For example,  
for $c=\pm 2/5,\pm 22/5$, it yields an estimate 
$D\ge (5-\sqrt{5})/2$, 
which becomes an equality for 
the well known Yang-Lee category 
($c=-22/5$, see \cite{DMS}) and three its Galois images.
The same is true for $c=\pm 14/5,\pm 34/5$, in which case the estimate is 
$D\ge (5+\sqrt{5})/2$ (it is attained at 
four Galois images of the Yang-Lee category). 
Also, it goes without saying that the inequality 
is sharp for $c=0$, where it becomes an equality for the trivial category. 
\end{remark}

These considerations inspire the following questions.

{\bf Questions.} Does there exist a sequence of 
nontrivial fusion categories over $\CC$ 
for which the global dimensions tend to $1$? Does there 
exist such a sequence with a bounded  number of simple objects?
Is the set of global dimensions of fusion categories over $\CC$ 
a discrete subset of $\mathbb R$? 

We expect that the answer to the first question is ``no'', i.e. the point $1$ 
of the set of possible dimensions of fusion categories is an isolated point
(``categorical property T''). 



\begin{section}{Weak Hopf algebras and their integrals}

Below we collect the definition and basic properties of
weak Hopf algebras.
