---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-013-24-palm-measures-of-determinantal-point-processe
section_title: "Palm measures of determinantal point processes"
section_number: 2.4
pages: 10-11
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.988
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
[]{#secpalm label="secpalm"} We here give a probabilistic interpretation of Christoffel deformations of orthogonal polynomial ensembles in the case when the points $u_1,...,u_k$ belong to the support of the measure $\omega$. We first recall the basics on Palm distributions of a general point process $\mathbb{P}$ on a discrete space $E$, see for instance [@daley-verejones], [@shiraitakahashi] or [@bufetovquasisymmetries] and references therein for a more general treatment.

::: defi
Let $\mathbb{P}$ be a point process on the discrete set $E$. For pairwise distinct points $u_1,...,u_k \in E$ such that $\mathbb{P}(u_1,...,u_k  \in X) >0$, the *Palm measure* $\hat{\mathbb{P}}^{u_1,...,u_k}$ of $\mathbb{P}$ at $u_1,...,u_k$ is the point process $\mathbb{P}$ on $E$ conditionned to have particles at $u_1,...,u_k$, $$\begin{aligned}
\hat{\mathbb{P}}^{u_1,...,u_k} ( \mathcal{B} )= \frac{\mathbb{P}(\mathcal{B}\cap \{u_1,...,u_k  \in X \})}{\mathbb{P}(u_1,...,u_k  \in X) },
\end{aligned}$$ for any borel set $\mathcal{B} \subset \mathrm{Conf}(E)$. The *reduced Palm measure* $\mathbb{P}^{u_1,...,u_k}$ is then defined as the pushforward of the Palm measure $\hat{\mathbb{P}}^{u_1,...,u_k}$ under the map $$\begin{aligned}
\mathrm{Conf}(E) & \rightarrow \mathrm{Conf}(E)\\
X & \mapsto X \setminus \{u_1,...,u_k \}.
\end{aligned}$$
:::

In particular, if the point process $\mathbb{P}$ has $N + k$ particles, i.e. $\mathbb{P}( |X| = N+k) =1$, then its reduced Palm measure $\mathbb{P}^{u_1,\dots, u_k}$ has $N$ particles.\
We also recall the following Proposition from [@shiraitakahashi].

::: prop
[]{#propcvpalm label="propcvpalm"} If $\mathbb{P}$ is a determinantal point process with kernel $K$ such that $\mathbb{P}(u_1,...,u_k  \in X) >0$, then, its reduced Palm measure at $u_1,...,u_k$ is a determinantal point process with kernel $$\begin{aligned}
K^{u_1,...,u_k}(x,y)= \left( \det(K(u_i,u_j)\right)_{1 \leq i,j \leq k}^{-1} \det \begin{pmatrix}
K(x,y) & K(x,u_1) &\dots & K(x,u_k) \\
K(u_1,y) &K(u_1,u_1) & \dots & K(u_1,u_k) \\
\vdots & & \ddots & \vdots \\
K(u_k,y) & \dots & \dots& K(u_k,u_k)
\end{pmatrix}.
\end{aligned}$$ acting on $l^2(E )$.
:::

We now consider a measure $\omega$ as before, with an infinite support lying in a discrete countable subset $E$ of $\mathbb{R}$. For $n \in \mathbb{N}$, we denote by $\mathbb{P}_n$ the corresponding orthogonal polynomial ensemble. Let $u_1,...,u_k \in \text{supp}(\omega)$ be pairwise distinct, and, as before, denote by $\mathbb{P}_n^k$ the Christoffel deformation of $\mathbb{P}_n$ at $u_1,...,u_k$. The next Proposition formally establishes the fact that the study of Christoffel deformations of orthogonal polynomial ensembles contains the study of their Palm measures.

::: prop
[]{#proppalm label="proppalm"} For any natural $N \in \mathbb{N}$, we have the equality between point processes $$\begin{aligned}
\mathbb{P}_{N+k}^{u_1,...,u_k}=\mathbb{P}_N^k.
\end{aligned}$$
:::

::: proof
*Proof.* We know from [@shiraitakahashi] (see also [@bufetovquasisymmetries]) that, for a determinantal point process with a kernel that is a kernel of an orthogonal projection onto a closed subspace $L \subset l^2(E)$, its reduced Palm measure at points $u_1,...,u_k$ is a determinantal point process with the kernel of orthogonal projection onto $$\begin{aligned}
L^k:= \{f \in L, \hspace{0.1cm} f(u_1)=...=f(u_k)=0 \}.
\end{aligned}$$ Specializing this fact to the subspace $$\begin{aligned}
L:= \{ \sqrt{\omega(x)}p(x), \hspace{0.1cm} p \in \mathbb{R}_{N+k-1}[x] \},
\end{aligned}$$ one obtains the statement of the Proposition. ◻
:::
