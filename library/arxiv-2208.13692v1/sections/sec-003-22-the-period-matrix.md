---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-003-22-the-period-matrix
section_title: "The Period Matrix"
section_number: 2.2
pages: 8-10
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.982
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: period matrix label="subsec: period matrix"} We record now a result from the literature.

::: theorem
Define the matrices $M$, $M_S$ by $$M =  \begin{pmatrix}
4 & 1 & -1 & 1 \\ 1 & 4 & 1 & -1 \\ -1 & 1 & 4 & 1 \\ 1 & -1 & 1 & 4
\end{pmatrix}, \quad
M_S =  \begin{pmatrix}
4 & -1 & -1 & -1 \\ -1 & 4 & -1 & -1 \\ -1 & -1 & 4 & -1 \\ -1 & -1 & -1 & 4
\end{pmatrix}.$$ A Riemann matrix for Bring's curve is given by $\tau_{\mathcal{B}} = \tau_0 M$, where $\tau_0 = -0.5+0.186676i \, (6.d.p)$ is given by the conditions $$j(\tau_0) = - \frac{29^3 \times 5}{2^5}, \quad j(5\tau_0) = -\frac{25}{2} .$$ Further, there exists a symplectic transformation such that $\tau_{\mathcal{B}} = \tau_0 M_S$.
:::

::: proof
*Proof.* This was first shown in [@Riera1992], but the equations for $j(\tau_0)$, $j(5\tau_0)$ were incorrectly swapped as first noted[^1] in [@Braden2012], where the above period matrix was also calculated via the HC-model.

Moreover, in [@Weber2005], a period matrix is constructed with respect to a homology basis with intersection matrix $$I_W = \begin{pmatrix}
0 & 1 & 1 & -1 & -1 & 0 & 0 & 1 \\ -1 & 0 & 1 & 1 & 0 & 1 & 0 & -1 \\ -1 & -1 & 0 & 1 & 0 & -1 & 0 & 0 \\ 1 & -1 & -1 & 0 & 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 & 0 & 1 & 1 & -1 \\ 0 & -1 & 1 & 0 & -1 & 0 & 1 & 1 \\0 & 0 & 0 & -1 & -1 & -1 & 0 & 1 \\ -1 & 1 & 0 & 0 & 1 & -1 & -1 & 0 
\end{pmatrix}  ,$$ that is given as $\Omega = (A, B)$ where the columns $A_k, B_k$ are $$A_k = \begin{pmatrix} \zeta^{k} (1-\zeta^2) \\ \zeta^{2k+3/2}(1-\zeta^4)(l\Phi-1) \\ \zeta^{4k+3}(1-\zeta^3)\Phi(1-l) \\ \zeta^{3k+2}(1-\zeta)l \end{pmatrix}, \quad B_k = \begin{pmatrix}  \zeta^{2k+3/2}(1-\zeta^4)(l\Phi-1) \\ \zeta^{4k+3}(1-\zeta^3)\Phi(1-l) \\ \zeta^{3k+2}(1-\zeta)l \\ \zeta^{k} (1-\zeta^2) \end{pmatrix}  ,$$ for $k=0, \dots, 3$, $\Phi = \frac{1}{2}(1+\sqrt{5})$, and $l = \left \lvert {\frac{I(-1,0)}{I(-\infty, -1)}} \right \rvert \approx 0.848641$ where $$I(a,b) = \int_a^b (t-1)^{-1/5} t^{-3/5} (t+1)^{-4/5}  dt  .$$ Note [@Weber2005 Lemma 5.1] uses $\zeta= \exp(2 \pi i/10)$, whereas we take $\zeta= \exp(2 \pi i/5)$. As such, the columns of $\Omega$ look different to those of Weber in terms of the exponent of $\zeta$, but they do indeed agree.

One can find (using Sage) the matrix $$C = \begin{pmatrix}
0 & 1 & -2 & 1 & 1 & 1 & 0 & -1 \\ 0 & 1 & -1 & 1 & 0 & 0 & -1 & 0 \\ 0 & 0 & -1 & 0 & 0 & 1 & 1 & 0 \\ 1 & 1 & -2 & 2 & 0 & 1 & -1 & -1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0
\end{pmatrix}$$ such that $C^T I_W C = J_g = \begin{pmatrix} 0 & \mathop{\mathrm{Id}}_g \\ -\mathop{\mathrm{Id}}_g & 0 \end{pmatrix}$, i.e. $C$ 'canonicalises' the homology basis. This means we get a Riemann matrix $\tau_W = (AC)^{-1} (BC) = C^{-1}A^{-1} B C$, and one can numerically find that the matrix $$R = \begin{pmatrix} \delta & \beta \\ \gamma & \alpha \end{pmatrix} = \begin{pmatrix}
0 & 0 & 0 & 1 & 0 & 0 & 1 & 2 \\ 0 & -1 & 1 & 0 & -1 & -2 & 1 & 1 \\ 1 & 0 & 1 & 0 & 2 & 1 & 1 & 1 \\ 0 & 1 & 0 & 0 & 1 & 2 & 0 & 0 \\ 1 & 0 & 0 & 0 & 2 & 1 & 0 & 1 \\ 1 & 0 & 1 & -1 & 1 & 1 & 1 & -1 \\ -1 & 0 & 0 & 1 & -1 & -1 & 1 & 2 \\ 1 & 0 & 1 & -1 & 1 & 2 & 1 & -1
\end{pmatrix}$$ relates $\tau_W$ to $\tau_{\mathcal{B}}$ by $$\label{transRRW}
   \tau_{\mathcal{B}} = (\delta + \tau_W \gamma)^{-1}(\beta+ \tau_W \alpha) .$$ Here $R$ is a symplectic transform with respect the standard symplectic form $J_g$.

For a fourth proof, we may consider the Riemann matrix numerically calculated by SageMath, and find a transform to $\tau_{\mathcal{B}}$, as is done in the corresponding notebook. ◻
:::

Riera and Rodriguez (hereafter abbreviated to R&R) constructed the constraints on $\tau_0$ via $j$-invariants by considering the quotients by group actions of the curve to elliptic curves [@Riera1992]. They show that these constraints give a unique value of $\tau_0$ modulo $\Gamma_0(5)$, or equivalently in the language of [@Gonzalez2000] that $\tau_0$ gives a distinguished point in the modular curve $X_0(5)$. As we will see later in §[\[subsec: quotient by 3-cycle\]](#subsec: quotient by 3-cycle){reference-type="ref" reference="subsec: quotient by 3-cycle"}, there are additional quotients to elliptic curves not considered by R&R, which have $j$-invariants $$\begin{aligned}
    j(15 \tau_0) &= -\frac{5^2 \times 241^3}{2^3}  , \\
    j(3 \tau_0) &= \frac{5 \times 211^3}{2^{15}}   .
\end{aligned}$$ The latter is identified in relation to Bring's curve in [@Serre2008 Exercise 8.3.2c]. Serre says that this curve (50H) and 50E (using the naming convention of [@Birch1975]) with $j(5\tau_0)$ are 15-isogenous over $\mathbb{Q}$. This isogeny is not too mysterious when we think on the level of the corresponding elliptic curves over $\mathbb{C}$ as $\mathbb{C}/\left\langle 1,3 \tau_0 \right\rangle$ and $\mathbb{C}/\left\langle 1,5 \tau_0 \right\rangle$, wherein the isogeny $\mathbb{C}/\left\langle 1,3 \tau_0 \right\rangle \to \mathbb{C}/\left\langle 1,5 \tau_0 \right\rangle$ is the composition of the quotients by the maps $z \mapsto z+\tau_0$ and $z \mapsto z+ 1/5$ respectively. There is a complete $\mathbb{Q}$-isogeny class of elliptic curves of order four with periods $\tau_0, 3 \tau_0, 5 \tau_0$ and $15 \tau_0$ [@Birch1975].

It follows from the above that $\tau_0$ is transcendental. By a theorem of Schneider [@Baker2008], if $j(z)$ is rational, $z$ is either transcendental or an element of a quadratic imaginary field with class number 1. However, the $j$-invariants of elements of these fields are known to be integers, which doesn't occur in the case of $\tau_0$. In Weber's form of the period matrix, the transcendentality comes about because of the constant $l$, which is a ratio of Schwarz-Christoffel integrals which arise from the map of a Euclidean quadrilateral to a hyperbolic quadrilateral.

[^1]: Note the approximation of $\tau_0$ in [@Braden2012] contains a typographic error.
