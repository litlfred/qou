---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-020-41-christoffel-deformations-of-the-z-measures
section_title: "Christoffel deformations of the z-measures"
section_number: 4.1
pages: 18-25
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
The $z$-measures on partitions were introduced and extensively studied by Borodin and Olshanski in a series of papers, see e.g. [@bodist], [@bogamma], [@bomeixner] and [@bomarkov] and references therein. We first briefly explain their construcion. The $z$-measures are defined on the set $\mathbb{Y}$ of all partitions by: $$\begin{aligned}
M_{z,z',\xi}(\lambda)=(1-\xi)^{zz'}\xi^{|\lambda|}(z)_\lambda(z')_\lambda \left(\frac{\dim(\lambda)}{|\lambda|!}\right)^2.
\end{aligned}$$ They depend on three complex parameters, $z$, $z'$ and $\xi$ and they are in general complex measures. The following choices ensure that it is a probability measure (see e.g. [@bomeixner] Proposition 1.2 for a proof). First of all, the parameter $\xi$ is real and lies in the open unit interval $(0,1)$. Next, we distinguish three cases:

1.  The parameters $z$ and $z'$ are conjugate to each other.

2.  The parameters $z$ and $z'$ are both real and belong to the same interval $(m,m+1)$ where $m \in \mathbb{Z}$.

3.  One of the parameter, say $z$, is a non-zero integer, while the other has the same sign and satisfy $|z'|>|z|-1$.

If $z$ and $z'$ satisfy one of these three conditions, we say that they are *admissible* parameters. The Christoffel defomations of the $z$-measure are then defined as follows:

::: defi
Let $z$, $z'$ be admissible parameters and $M_{z,z',\xi}$ the corresponding $z$-measure. Let $u_1$,\...,$u_k$, $v_1$,\...,$v_k \in\mathbb{C}$ be $2k$ complex numbers which satisfy: $$\begin{aligned}
\prod_{i=1}^k(x-u_i+z)(x-v_i+z') > 0
\end{aligned}$$ for any $x \in \mathbb{Z}$. We define the Christoffel deformation of $M_{z,z',\xi}$ by: $$\begin{aligned}
 \label{defzmeas}
M_{z,z',\xi}^k(\lambda)=C\prod_{j=1}^{l(\lambda)}\prod_{i=1}^k(\lambda_j-j-u_i+z)(\lambda_j-j-v_i+z')M_{z,z'\xi}(\lambda),
\end{aligned}$$ where $C$ is the normalisation constant chosen such that $M_{z,z',\xi}^k$ is a probability measure.
:::

We first have to focus on the degenerate case. For simplicity, we assume that $z=N$ is a positive integer and $z' > z-1$. The $z$-measure $M_{z,z'\xi}$ is then supported on the subset of Young diagrams of length less than or equal to $N$, and we map $\mathbb{Y}$ on $\text{Conf}(\mathbb{N}) \subset \text{Conf}(\mathbb{Z})$ via $$\begin{aligned}
\lambda \mapsto \mathfrak{S}_N(\lambda):=\{ \lambda_i-i+N, \hspace{0.1cm} i=1,...,N \}.
\end{aligned}$$ The pushforward of the $z$-measure $M_{z,z'\xi}$ under $\mathfrak{S}_N$ is then the $N$-th Meixner ensemble (see e.g. [@bomeixner], Proposition 1.4), i.e. the $N$-th orthogonal ensemble with weight $$\begin{aligned}
\omega_{\beta,\xi}(x)=\frac{(\beta)_x \xi^x}{x!},
\end{aligned}$$ where $\beta = z'-z+1>0$. The corresponding orthogonal polynomials are the Meixner polynomials defined by: $$\begin{aligned}
M_n(x;\beta,\xi)= \left._2F_1\right.(-n,-x;\beta;1-1/\xi) , \hspace{0.1cm} n \in \mathbb{N}.
\end{aligned}$$ Their leading coefficient $c_n$ and their squared norm $h_n$ are given by $$\begin{aligned}
c_n= \frac{\left(1-\frac{1}{\xi}\right)^n}{n!(\beta)_n} \hspace{0.1cm} , \quad h_n = \frac{n!}{\xi^n (1-\xi)^\beta (\beta)_n}.
\end{aligned}$$ We now choose $k$ real numbers $u_1,...,u_k \in \mathbb{R}\setminus \mathbb{N}$ which are not integers, and set $v_i=u_i+\beta-1$. We thus have: $$\begin{aligned}
\prod_{j=1}^{l(\lambda)}\prod_{i=1}^k(\lambda_j-j-u_i+z)(\lambda_j-j-v_i+z')=\prod_{x \in \mathfrak{S}_N(\lambda)}\prod_{j=1}^k(x-u_i)^2
\end{aligned}$$ from which we deduce that the pushforward of $M_{z,z',\xi}^k$ under $\mathfrak{S}_N$ is the Christoffel deformation of the $N$-th Meixner ensemble at points $u_1,...,u_k$ as defined in definition [\[maindef\]](#maindef){reference-type="ref" reference="maindef"}. As a consequence, it defines a determinantal point process with an explicit kernel given by Proposition [\[propkernelcharlier\]](#propkernelcharlier){reference-type="ref" reference="propkernelcharlier"}. We now prepare a similar statement for other choices of admissible parameters $z$ and $z'$. For this aim, we will reproduce the analytic continuation argument developed in [@bomeixner] and [@bomarkov], although the simplifications we need are less obvious. We will note: $\mathbb{Z}'=\mathbb{Z}+1/2$ the set of proper half integers. For $a \in \mathbb{Z}'$, $x \in \mathbb{Z}'$ and $z$ and $z'$ admissible parameters *that are not* in the degenerate case, we define: $$\label{defpsi} \begin{split}
\psi_a(x;z,&z',\xi):= \left( \frac{\Gamma(x+z+1/2) \Gamma(x+z'+1/2)}{\Gamma(z-a+1/2) \Gamma(z'-a+1/2)} \right)^{1/2} \xi^{1/2(x+a)} (1-\xi)^{1/2(z+z')-a} \\
&\times \frac{\left._2F_1\right.\left(-z+a+1/2,-z'+a+1/2;x+a+1;\frac{\xi}{\xi-1}\right)}{\Gamma(x+a+1)}.
\end{split}$$ Observe that these functions are symmetric in $z,z'$. We now recall the following integral representation, which is due to Borodin-Olshanski (see [@bomeixner], Proposition 2.3): $$\label{intreppsi} \begin{split}
\psi_a(x;z,z',\xi)&= \left( \frac{\Gamma(x+z+1/2)\Gamma(x+z'+1/2)}{\Gamma(z-a+1/2)\Gamma(z'-a+1/2)}\right)^{1/2} \frac{\Gamma(z'-a+1/2)}{\Gamma(z'+x+1/2)}(1-\xi)^{\frac{z'-z+1}{2}}\\
&\times\frac{1}{2i\pi} \oint (1- \sqrt{\xi}\omega)^{-z'+a-1/2} \left(1- \frac{\sqrt{\xi}}{\omega}\right)^{z-a-1/2}\omega^{-x-a}\frac{d\omega}{\omega}.
\end{split}$$ Observe that it is now not obvious that such an expression is symmetric in $z,z'$, i.e. none of its factor is symmetric in $z,z'$, but since expression ([\[defpsi\]](#defpsi){reference-type="ref" reference="defpsi"}) is, it has to be symmetric in $z,z'$. We will also need the following Proposition, relating the functions $\psi_a$ to Meixner polynomials, which comes from Borodin and Olshanski ([@bomeixner], Proposition 2.8).

::: prop
[]{#propbopsimeixner label="propbopsimeixner"} Suppose $z=N \in \mathbb{N}$ and $z'=N+\beta-1$. Suppose that: $$\begin{aligned}
\tilde{x}:=x+N-1/2 \in \mathbb{N}, \quad \quad n:=N-a-1/2 \in \mathbb{N},
\end{aligned}$$ are non-negative integers. Then, $\psi_a(x;z,z',\xi)$ is well defined and we have: $$\begin{aligned}
\psi_a(x;z,z',\xi) =\sqrt{\frac{\omega_{\beta,\xi}(\tilde{x})}{h_n}} M_n(\tilde{x};\beta,\xi).
\end{aligned}$$
:::

In what follows, we will sometimes omit the dependance on the parameters $z$, $z'$ and $\xi$ when the context is clear. The first Theorem of this section states that, for any pair of admissible parameters $(z,z')$, the modified $z$-measure given by formula ([\[defzmeas\]](#defzmeas){reference-type="ref" reference="defzmeas"}) gives rise to a determinantal point process with an explicit kernel expressed through the functions $\psi_a$ and their derivatives.

::: thm
[]{#thmzmeas label="thmzmeas"}For any admissible parameters $z$ and $z'$ which are not in the degenerate case, and any $u_i \in \mathbb{R}$, $v_i=u_i+z'-z-1/2$, the pushforward of the measure $M_{z,z',\xi}^k$ under the map $$\begin{aligned}
\mathfrak{S} : \lambda \mapsto \{\lambda_i-i+1/2\} \in \text{Conf}(\mathbb{Z}'),
\end{aligned}$$ is a determinantal point process on $\mathbb{Z}'$. Its correlation kernel is given by: $$\label{kernelmodifiedzmeas}
K_{z,z',\xi}^k(x,y):=\frac{C_{z,z',k}}{\prod_{i=1}^{k}|(x-u_i)(y-u_i)|}\frac{B_{k,0}(x;z,z',\xi)B_{k,1}(y;z,z',\xi)-B_{k,0}(y;z,z',\xi)B_{k,1}(x;z,z',\xi)}{D_k(z,z',\xi)^2(x-y)},$$ with $$\begin{aligned}
B_{k,p}(x)&= \begin{vmatrix}
 \psi_{-1/2+p}(u_1) & \psi_{-3/2+p}(u_1) & \dots & \psi_{-1/2-2k+p}(u_1) \\
 \vdots &   & \ddots & \vdots \\
 \psi_{-1/2+p}(u_k) & \dots & \dots & \psi_{-1/2-2k+p}(u_k) \\
 \psi'_{-1/2+p}(u_1) & \dots & \dots & \psi'_{-1/2-2k+p}(u_1) \\
 \vdots  & \ddots &  & \vdots \\
 \psi'_{-1/2+p}(u_k) & \dots & \dots & \psi'_{-1/2-2k+p}(u_k) \\
 \psi_{-1/2+p}(x) & \dots & \dots & \psi_{-1/2-2k+p}(x)
\end{vmatrix}, \quad p=0,1 \hspace{0.1cm}, \\
\\
D_k&=\begin{vmatrix}
 \psi_{-1/2}(u_1) & \psi_{-3/2}(u_1) &\dots& \psi_{1/2-2k}(u_1) \\
  \vdots & & \ddots & \vdots \\
 \psi_{-1/2}(u_k) & \dots & \dots & \psi_{1/2-2k}(u_k) \\
 \psi'_{-1/2}(u_1) & \dots & \dots & \psi'_{1/2-2k}(u_1) \\
 \vdots & \ddots &  & \dots \\
 \psi'_{-1/2}(u_k) & \dots & \dots & \psi'_{1/2-2k}(u_k) \\
\end{vmatrix}, \\
\intertext{and}
C_{z,z',k}&=\left(\frac{\xi}{\xi-1}\right)^{1+2k} \frac{\Gamma(z+2k+1)}{\Gamma(z)}\frac{\Gamma(z'+2k)}{\Gamma(z'-1)}.
\end{aligned}$$
:::

::: proof
*Proof.* The proof requires some steps. We first establish in step 1 that the statement of the Theorem holds for the degenerate series case. This fact is precisely formulated in Lemma [\[lemmestep1\]](#lemmestep1){reference-type="ref" reference="lemmestep1"} below. In step 2, we prove that quantities of interest involving the modified $z$-measures have an analytic in $\xi$ (and thus in $\sqrt{\xi}$), with polynomial coefficients in $(z,z')$, for all values of the admissible parameters. In step 3, we prove that a modification of the kernel also have an analytic expansion in $\sqrt{\xi}$ with polynomials coefficients in $(z,z')$. We here use the integral reprensentations of the functions $\psi_a$. We conclude the proof in the final step.\

#### **Step 1.**

Assume that $z=N \in \mathbb{N}$ and $z'=N+\beta-1$, and: $$\begin{aligned}
\tilde{x}:=x+N-1/2, \quad \tilde{y}:=y+N-1/2 \quad \quad \tilde{u}_i \in \mathbb{R}, \quad \tilde{v}_i=\tilde{u}_i+\beta-1, \quad i=1,...,k .
\end{aligned}$$ Then, by means of Propositions [\[propkernelcharlier\]](#propkernelcharlier){reference-type="ref" reference="propkernelcharlier"} and [\[propbopsimeixner\]](#propbopsimeixner){reference-type="ref" reference="propbopsimeixner"}, and computations similar to those performed at the beginning of the proof of Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"}, formula ([\[kernelmodifiedzmeas\]](#kernelmodifiedzmeas){reference-type="ref" reference="kernelmodifiedzmeas"}) makes sense and holds with: $$\begin{aligned}
\tilde{u}_i=u_i+N-1/2.
\end{aligned}$$ Indeed, the factor $C_{z,z',k}$ comes from the ratio $\frac{c_{N-1}}{c_{N+2k}}$ appearing in Proposition [\[propkernelcharlier\]](#propkernelcharlier){reference-type="ref" reference="propkernelcharlier"}, while the expressions for $A_k$, $B_k$ and $D_k$ are obtained from Proposition [\[propkernelcharlier\]](#propkernelcharlier){reference-type="ref" reference="propkernelcharlier"} after performing operations similar to those in the proof of Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"}: the polynomials $M_n$ are replaced by the functions $\psi_a$ thanks to homogeneity, and their derivatives $M_n'$ are replaced by $\psi_a'$ by operations on rows. We resume this fact in the following Lemma:

::: lem
[]{#lemmestep1 label="lemmestep1"} Suppose that $z = N \in \mathbb{N}$ is a positive integer, $\beta >0$ is a positive number and that $z' = N +\beta - 1$. Let $\tilde{u}_1,...,\tilde{u}_k \in \mathbb{R}$ be $k$ real numbers, and set: $$\begin{aligned}
\tilde{v}_i=\tilde{u}_i + \beta - 1, \quad i=1,...,k.
\end{aligned}$$ Let $M_{z,z',\xi}^k$ be the Christoffel deformation of the $z$-measure $M_{z,z',\xi}$ defined by ([\[defzmeas\]](#defzmeas){reference-type="ref" reference="defzmeas"}), with $u_i$ (resp. $v_i$) replaced by $\tilde{u}_i$ (resp. $\tilde{v}_i$). We then have, for every $n \in \mathbb{N}$ and every $\{\tilde{x}_1,...,\tilde{x}_n \} \subset \mathbb{N}$: $$\begin{aligned}
M_{z,z',\xi}^k \left( \{x_1,...,x_n \} \subset \mathfrak{S}(\lambda) \right)=M_{z,z',\xi}^k \left( \{\tilde{x}_1,...,\tilde{x}_n \} \subset \mathfrak{S}_N(\lambda) \right)=\det \left( K_{z,z',\xi}^k(x_i,x_j) \right)_{i,j=1}^n
\end{aligned}$$ where $K_{z,z',\xi}^k$ is defined by ([\[kernelmodifiedzmeas\]](#kernelmodifiedzmeas){reference-type="ref" reference="kernelmodifiedzmeas"}) and: $$\begin{aligned}
x_j &= \tilde{x}_j -N +1/2, \quad j=1,...,n
\intertext{and}
u_i &= \tilde{u}_i -N + 1/2, \quad i=1,...,k.
\end{aligned}$$
:::

#### **Step 2.** 

For any values of the parameters $z$ and $z'$, and for any $n \in \mathbb{N}$, and any $\{x_1,..,x_n\} \subset \mathbb{Z}'$, Borodin and Olshanski ([@bomeixner], Proposition 3.9) show that the quantity: $$\begin{aligned}
M_{z,z',\xi} \left( \{x_1,...,x_n \} \subset \mathfrak{S}(\lambda) \right),
\end{aligned}$$ as a function of $\xi$, can be expanded in series around zero, and its coefficients are polynomials in $(z,z')$. As an immediate consequence, we also have that, viewed as a function of $\xi$, the quantity: $$\begin{aligned}
M_{z,z',\xi}^k \left( \{x_1,...,x_n \} \subset \mathfrak{S}(\lambda) \right)
\end{aligned}$$ has an analytic expansion around zero with coefficients that are polynomials in $(z,z')$.\
\

#### **Step 3**

We will prove that the same statement holds for a slight modification of the kernel $K_{z,z',\xi}(x,y)$. We first assume that $z$ and $z'$ are admissible parameters not in the degenerate series case. Following [@bomeixner] (or [@bomarkov]), we define: $$\begin{aligned}
 \label{def:functfzz'}
f_{z,z'}(x)=\frac{\Gamma(x+z'+1/2)}{\sqrt{\Gamma(x+z+1/2)\Gamma(x+z'+1/2)}}
\end{aligned}$$ where $x \in \mathbb{Z}'$. By the assumptions on $z$ and $z'$, this function is well defined. Indeed, the Gamma functions are well defined and the fact that: $$\begin{aligned}
\Gamma(x+z+1/2)\Gamma(x+z'+1/2) >0
\end{aligned}$$ allows to define the square root. We also assume that $u_1,...u_k$ are such that $f_{z,z'}(x)$ is well defined for $x \in \{u_1,...,u_k \}$. Observe that interchanging $z$ and $z'$ corresponds to turning $f$ into $1/f$. We will also use the notation: $$\begin{aligned}
I_a(x;z,z',\xi)=\frac{1}{2i\pi}\oint (1- \sqrt{\xi}\omega)^{-z'+a-1/2} \left(1- \frac{\sqrt{\xi}}{\omega}\right)^{z-a-1/2}\omega^{-x-a}\frac{d\omega}{\omega}
\end{aligned}$$ for any $a \in \mathbb{Z}'$ and $x \in \mathbb{Z}' \cup \{u_1,...u_k \}$. By means of the integral representation ([\[intreppsi\]](#intreppsi){reference-type="ref" reference="intreppsi"}), we can decompose: $$\begin{aligned}
 \label{v1}
\psi_a(x;z,z',\xi)=(1-\xi)^{\frac{z-z'+1}{2}}\frac{f_{z,z'}(x)}{f_{z,z'}(-a)}I_a(x;z,z',\xi)
\end{aligned}$$ Since the initial definition ([\[defpsi\]](#defpsi){reference-type="ref" reference="defpsi"}) is symmetric in $(z,z')$, we can also write: $$\begin{aligned}
 \label{v2}
\psi_a(x;z,z',\xi)=(1-\xi)^{\frac{z'-z+1}{2}}\frac{f_{z,z'}(-a)}{f_{z,z'}(x)}I_a(x;z',z,\xi),
\end{aligned}$$ Similarly, we have for the derivatives: $$\begin{aligned}
\label{v1'}
\psi_a'(x;z,z',\xi)-\frac{f'_{z,z'}(x)}{f_{z,z'}(x)}\psi_a(x;z,z',\xi)=(1-\xi)^{\frac{z-z'+1}{2}} \frac{f_{z,z'}(x)}{f_{z,z'}(-a)}I_a'(x;z,z',\xi)
\end{aligned}$$ and: $$\begin{aligned}
\label{v2'}
\psi_a'(x;z,z',\xi)+\frac{f'_{z,z'}(x)}{f_{z,z'}(x)}\psi_a(x;z,z',\xi)=(1-\xi)^{\frac{z'-z+1}{2}}\frac{f_{z,z'}(-a)}{f_{z,z'}(x)}I_a'(x;z',z,\xi).
\end{aligned}$$ Observe that the integrals $I_a$ and their derivatives $I_a'$ have an analytic expansion in $\sqrt{\xi}$ with coefficients polynomial in $(z,z')$. We thus want to get rid of the factors involving $f_{z,z'}$ and $f_{z',z}$ appearing in formula ([\[kernelmodifiedzmeas\]](#kernelmodifiedzmeas){reference-type="ref" reference="kernelmodifiedzmeas"}) through the functions $\psi_a$. We begin with the constant factor $D_k^2$. By ([\[v1\]](#v1){reference-type="ref" reference="v1"}) and ([\[v1\'\]](#v1'){reference-type="ref" reference="v1'"}) and their multiplicative structure, we can write $$\begin{gathered}
D_k=(1-\xi)^{k(z'-z+1)}\left(\prod_{i=1}^k f_{z,z'}(u_i)\right)^2 \left( \prod_{i=1}^{2k}f_{z,z'}(-1/2-i+1) \right)^{-1}\\
\times \det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k}}   \\
\left( I_{-1/2-j+1}'(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k}}
\end{pmatrix}.
\end{gathered}$$ But using ([\[v2\]](#v2){reference-type="ref" reference="v2"}) and ([\[v2\'\]](#v2'){reference-type="ref" reference="v2'"}), we see that $D_k$ can also be expressed in the following way $$\begin{gathered}
D_k=(1-\xi)^{k(z-z'+1)}\left(\prod_{i=1}^k f_{z,z'}(u_i)\right)^{-2} \left( \prod_{i=1}^{2k}f_{z,z'}(-1/2-i+1) \right)\\
\times \det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k}}   \\
\left( I_{-1/2-j+1}'(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k}}
\end{pmatrix}.
\end{gathered}$$ Thus, writing the determinants $D_k$ in $D_k^2$ in these two different ways leads to: $$\begin{aligned}
 D_k^2=(1-\xi)^{2k}\det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k}}   \\
\left( I_{-1/2-j+1}'(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k}}
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k}}   \\
\left( I_{-1/2-j+1}'(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k}}
\end{pmatrix}.
\end{aligned}$$ For the products $B_{k,0}(x)B_{k,1}(y)$ and $B_{k,1}(x)B_{k,0}(y)$, we also write the functions $\psi_a$ and $\psi_a'$ in two different ways, but now, we have to take care of the \"boundary factors\", i.e. the factors that are not shared by both determinants. For instance, we have $$\begin{gathered}
B_{k,0}(x)B_{k,1}(y)=(1-\xi)^{2k+1}\frac{f_{z,z'}(x)}{f_{z,z'}(y)} \frac{f_{z,z'}(1/2)}{f_{z,z'}(-1/2-2k)} \\
\times \det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}   \\
\left( I_{-1/2-j+1}'(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}\\
\left(I_{-1/2-j+1}(x;z,z',\xi)\right)_{j=1,..2k+1}
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{1/2-j+1}(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}   \\
\left( I_{1/2-j+1}'(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}\\
\left(I_{1/2-j+1}(y;z',z,\xi)\right)_{j=1,...,2k+1}
\end{pmatrix},
\end{gathered}$$ and $$\begin{gathered}
B_{k,0}(y)B_{k,1}(x)=(1-\xi)^{2k+1}\frac{f_{z,z'}(x)}{f_{z,z'}(y)}\frac{f_{z,z'}(-1/2-2k)}{f_{z,z'}(1/2)}\\
\times \det\begin{pmatrix}
\left( I_{1/2-j+1}(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}   \\
\left( I_{1/2-j+1}'(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}\\
\left(I_{1/2-j+1}(x;z,z',\xi)\right)_{j=1,..2k+1}
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}   \\
\left( I_{-1/2-j+1}'(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}\\
\left(I_{-1/2-j+1}(y;z',z,\xi)\right)_{j=1,...,2k+1}
\end{pmatrix}.
\end{gathered}$$ This gives $$\begin{aligned}
B&_{k,0}(x)B_{k,1}(y)-B_{k,0}(y)B_{k,1}(x)=(1-\xi)^{2k+1}\frac{f_{z,z'}(x)}{f_{z,z'}(y)}\\
&\times\left( \frac{f_{z,z'}(1/2)}{f_{z,z'}(-1/2-2k)}\det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}   \\
\left( I_{-1/2-j+1}'(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}\\
\left(I_{-1/2-j+1}(x;z,z',\xi)\right)_{j=1,..2k+1}
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{1/2-j+1}(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}   \\
\left( I_{1/2-j+1}'(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}\\
\left(I_{1/2-j+1}(y;z',z,\xi)\right)_{j=1,...,2k+1}
\end{pmatrix} \right. \\
&\left. - \frac{f_{z,z'}(-1/2-2k)}{f_{z,z'}(1/2)} \det\begin{pmatrix}
\left( I_{1/2-j+1}(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}   \\
\left( I_{1/2-j+1}'(u_i;z,z',\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}\\
\left(I_{1/2-j+1}(x;z,z',\xi)\right)_{j=1,..2k+1}
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}   \\
\left( I_{-1/2-j+1}'(u_i;z',z,\xi) \right)_{\substack{i=1,...,k \\ j=1,...,2k+1}}\\
\left(I_{-1/2-j+1}(y;z',z,\xi)\right)_{j=1,...,2k+1}
\end{pmatrix} \right) \\
\\
&=\frac{(1-\xi)^{2k+1}}{\sqrt{(z'+1)z'...(z'-2k-1)(z+1)z...(z-2k-1)}} \frac{f_{z,z'}(x)}{f_{z,z'}(y)} \\
&\times \left( (z'+1)z'...(z'-2k-1) \det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z,z',\xi) \right)  \\
\left( I_{-1/2-j+1}'(u_i;z,z',\xi) \right)\\
\left(I_{-1/2-j+1}(x;z,z',\xi)\right)
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{1/2-j+1}(u_i;z',z,\xi) \right)   \\
\left( I_{1/2-j+1}'(u_i;z',z,\xi) \right)\\
\left(I_{1/2-j+1}(y;z',z,\xi)\right)
\end{pmatrix} \right.\\
& \left. - (z+1)z...(z-2k-1) \det\begin{pmatrix}
\left( I_{1/2-j+1}(u_i;z,z',\xi) \right)   \\
\left( I_{1/2-j+1}'(u_i;z,z',\xi) \right)\\
\left(I_{1/2-j+1}(x;z,z',\xi)\right)
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z',z,\xi) \right)   \\
\left( I_{-1/2-j+1}'(u_i;z',z,\xi) \right)\\
\left(I_{-1/2-j+1}(y;z',z,\xi)\right)
\end{pmatrix}  \right),
\end{aligned}$$ where we used: $$\begin{aligned}
\frac{a}{b}C+\frac{b}{a}D=\frac{a^2C+b^2D}{ab}
\end{aligned}$$ and direct simplifications due to the standard property of the Gamma function $$\begin{aligned}
\Gamma(A+1)=A\Gamma(A).
\end{aligned}$$ Let us introduce the auxilliary kernel $\tilde{K}_{z,z',\xi}^k(x,y)$: $$\begin{aligned}
\tilde{K}_{z,z',\xi}^k(x,y)=\frac{f_{z,z'}(y)}{f_{z,z'}(x)}D_k^2 \sqrt{(z'+1)z'...(z'-2k-1)(z+1)z...(z-2k-1)}K_{z,z',\xi}^k(x,y),
\end{aligned}$$ i.e. $$\begin{gathered}
\tilde{K}_{z,z',\xi}^k(x,y)\\
= \left( (z'+1)z'...(z'-2k-1) \det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z,z',\xi) \right)  \\
\left( I_{-1/2-j+1}'(u_i;z,z',\xi) \right)\\
\left(I_{-1/2-j+1}(x;z,z',\xi)\right)
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{1/2-j+1}(u_i;z',z,\xi) \right)   \\
\left( I_{1/2-j+1}'(u_i;z',z,\xi) \right)\\
\left(I_{1/2-j+1}(y;z',z,\xi)\right)
\end{pmatrix} \right.\\
\left. - (z+1)z...(z-2k-1) \det\begin{pmatrix}
\left( I_{1/2-j+1}(u_i;z,z',\xi) \right)   \\
\left( I_{1/2-j+1}'(u_i;z,z',\xi) \right)\\
\left(I_{1/2-j+1}(x;z,z',\xi)\right)
\end{pmatrix}
\det\begin{pmatrix}
\left( I_{-1/2-j+1}(u_i;z',z,\xi) \right)   \\
\left( I_{-1/2-j+1}'(u_i;z',z,\xi) \right)\\
\left(I_{-1/2-j+1}(y;z',z,\xi)\right)
\end{pmatrix}  \right),
\end{gathered}$$ and observe that it has an expansion in $\sqrt{\xi}$ around zero with coefficients that are polynomials in $(z,z')$, since it is the case for the integrals $I_a$ and their derivatives. Observe also that, for any $\{x_1,...,x_n\} \subset \mathbb{Z}'$, we have $$\begin{gathered}
\det\left( \tilde{K}_{z,z',\xi}^k(x_i,x_j) \right)_{i,j=1}^n \\
= D_k^{2n} \sqrt{(z'+1)z'...(z'-2k-1)(z+1)z...(z-2k-1)}^n \det\left( K_{z,z',\xi}^k(x_i,x_j) \right)_{i,j=1}^n.
\end{gathered}$$

#### **Final step.** 

Our computations above remain valid for $z$ and $z'$ belonging to the degenerate series case, provided $z > 2k+2$. Assume now that we are in this case, and let $\{x_1,...,x_n\} \subset \mathbb{Z}'$ be a finite subset of $\mathbb{Z}'$. We have established the following equality between series in $\sqrt{\xi}$ with coefficients that are polynomials in $(z,z')$: $$\begin{aligned}
\left(\det \left( \tilde{K}_{z,z',\xi}^k(x_i,x_j) \right)_{i,j=1,...,n}\right)^2 & = D_k^{4n}\left((z'+1)z'...(z'-2k-1)(z+1)z...(z-2k-1)\right)^n \\
&\times   M_{z,z',\xi}^k \left( \{x_1,...,x_n \} \subset \mathfrak{S}(\lambda) \right)^2 .
\end{aligned}$$ Indeed, the equality follows from the first step and Lemma [\[lemmestep1\]](#lemmestep1){reference-type="ref" reference="lemmestep1"}. The right hand side has an analytic expansion in $\xi$ with polynomial coefficients in $(z,z')$, by step 2 and 3, while it also holds for the left hand side by step 3. Since the set: $$\begin{aligned}
\{ (z,z') \in \mathbb{C}^2, z \in \mathbb{N}, \hspace{0.1cm} z > 2k+2 \text{ and } z' \in \mathbb{R}, \hspace{0.1cm} z'>z-1 \}
\end{aligned}$$ is a set of uniqueness for polynomials in two variables, the latter equality holds for all values of $(z,z')$, in particular for all admissible values. This proves the Theorem. ◻
:::
