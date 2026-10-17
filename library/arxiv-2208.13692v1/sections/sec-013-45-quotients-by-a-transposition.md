---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-013-45-quotients-by-a-transposition
section_title: "Quotients by a transposition"
section_number: 4.5
pages: 25-27
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.977
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: quotients by transposition label="subsec: quotients by transposition"} The strategy of quotienting from the $\mathbb{P}^4$-model using semi-invariants from the previous sections can also be used to calculate the quotient of Bring's curve by a transposition. We take semi-invariants $$(s_1, s_2, s_3, s_4)^T = \begin{pmatrix}
    1 & 1 & 0 & 0 \\ 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & -1
    \end{pmatrix} (x_1, x_2, x_3, x_4)^T  ,$$ and in terms of these variables the defining equations of Bring's curve become $$\begin{aligned}
H_2&=  \frac12( s_1^2+s_2^2)+ s_3^2+s_4^2+ (s_1+s_3+s_4)^2  , \\
H_3&=  \frac14( s_1^3+3 s_1 s_2^2)+ s_3^3+s_4^3 -(s_1+s_3+s_4)^3  .    
\end{aligned}$$ Taking invariants $[s:t:u:v] = [s_1 : s_2^2 : s_3 : s_4]$ and eliminating $t$ yields the elliptic curve $$\label{qe2p} 
\mathcal{E}_2: \ 4s^3 + 8s^2u + 7s u^2 + u^3 + s v^2 - u v^2=0, \quad j_{\mathcal{E}_2}=-\frac{25}{2} = j(5 \tau_0).$$ We observe that (also curiously) the quotient of $\mathcal{B}$ by a transposition is isomorphic to the quotient by a 4-cycle. It is not clear that there is any apriori reason for this to be the case. We are however able to relate the elliptic curves $\mathcal{E}_2$ and $\mathcal{E}_4$ as follows.

The normaliser of $\left\langle (12) \right\rangle$ in $S_5$ is $N_{S_5}(\left\langle (12) \right\rangle)=\left\langle (12),(34),(345) \right\rangle\cong D_{12}$ where now $N_{S_5}(\left\langle (12) \right\rangle)/\left\langle (12) \right\rangle\cong S_3$.[^1] We may immediately identify the action of $\overline{(34)}$ as the hyperelliptic involution on $\mathcal{E}_2$ as it acts as $v \to -v$, but we also retain another group action, that of $\overline{(345)}$. To understand this action recall that there are six fixed points of the action of $(12)$ on $\mathcal{B}$, which are all Weierstrass points. This gives six more distinguished points on the curve $\mathcal{E}_2$ in addition to the two images of the vertices we have seen previously. The six Weierstrass points fixed by $(12)$ break into two orbits of three under $(345)$ which we denote by $\{H_i\}$, $\{H_i'\}$ ($i=1,2,3$). Just as $(345)$ gives Bring's curve as an unramified cover of the genus $2$ curve $\mathcal{C}_2$, quotienting each by a transposition has $\overline{(345)}$ yielding an unramified automorphism of the quotient curves. Hence there exists a quotient from $\mathcal{E}_2=\mathcal{B}/\langle(12)\rangle$ to another elliptic curve $\mathcal{E}_4 = \mathcal{B}/\left\langle (12),(345) \right\rangle$ such that the following diagram commutes,

::: center
:::

To view this action on the elliptic curve $\mathcal{E}_2$, we calculate that $(345): [s:t:u:v] \to [s:t: -s-u/2-v/2 : s+3u/2-v/2]$. In the $s=1$ affine chart $4 + 8u + 7 u^2 + u^3 + (1 - u) v^2=0$ we can take as a cohomology basis $${\eta:=\frac{du}{2v(1-u)}} ,$$ and it is a simple algebraic calculation to see that this differential is invariant under the action of $\overline{(345)}$. If $\{\overline{H}_i\}$, $\{\overline{H'}_i\}$ are the images of the Weierstrass points on $\mathcal{E}_2$ such that ${(345)}({H}_i)={H}_{i+1}$, $\overline{(345)}(\overline{H}_i)=\overline{H}_{i+1}$ and so forth, the invariance of $\eta$ tells us that $$\int_{\overline{H}_1}\sp{\overline{H}_{2}}\eta=
\int_{\overline{H}_2}\sp{\overline{H}_{3}}\eta=\ldots,\quad
\int_{\overline{H'}_1}\sp{\overline{H'}_{2}}\eta=
\int_{\overline{H'}_2}\sp{\overline{H'}_{3}}\eta=\ldots,\quad
\int_{\overline{H}_1}\sp{\overline{H'}_{1}}\eta=
\int_{\overline{H}_2}\sp{\overline{H'}_{2}}\eta=\ldots$$ This means that if $\Lambda=\left\langle 1, 5 \tau_0 \right\rangle$ is the period lattice of the elliptic curve $\mathcal{E}_2$ then $\int_{\overline{H}_i}\sp{\overline{H}_{i+1}}\eta$ and $\int_{\overline{H'}_i}\sp{\overline{H'}_{i+1}}\eta$ are the same fixed element of $\Lambda/3$. By choosing an appropriate basis we may take $\overline{(345)} : z \to z+1/3$ for $z\in\mathbb{C}/\left\langle 1, 5 \tau_0 \right\rangle$. Then the quotient map will be a 3:1 isogeny of elliptic curves and we have the period of $\mathcal{E}_4$ to be $15 \tau_0$ and $j_{\mathcal{E}_4} = j(15 \tau_0)$. Under this isogeny the six images on $\mathcal{E}_2$ of the Weierstrass points $[1:1:\alpha:\beta:\gamma]$ are mapped to two on $\mathcal{E}_4$. Indeed, one may construct the isogeny explicitly using the Weierstrass-$\wp$ function and the Abel-Jacobi map via the diagram

::: center
:::

where $J(\mathcal{E})$ represents the Jacobian of the elliptic curve viewed at $\mathbb{C}/\left\langle 1,\tau \right\rangle$.

::: remark
This calculation may be verified numerically, as shown in the notebooks.
:::

::: remark
Note that when we call $\overline{(345)}$ an automorphism of the elliptic curve, we have to think about it only in the category of projective varieties with morphisms given by rational maps. To consider the group structure on an elliptic curve $E$ we need to also give a base point $O \in E$ which acts as the additive identity. A morphisms from pair $(E, O) \to (E^\prime, O^\prime)$ must map $O \to O^\prime$. If we denote the group of automorphisms of $E$ as a projective variety as $\mathop{\mathrm{Aut}}(E)$, and the group of $O$-fixing automorphisms as $\mathop{\mathrm{Aut}}_O(E)$, then we have short exact sequence $$0 \to T_E \to \mathop{\mathrm{Aut}}(E) \to \mathop{\mathrm{Aut}}_O(E) \to 0  ,$$ where $T_E$ is the group of translations of $E$. It is a classical theorem that $\mathop{\mathrm{Aut}}_O(E)\in\{C_2, C_4, C_6\}$ (here we are over $\mathbb{C}$).

Here $\overline{(345)}$ is indeed a translation. To see this take variables $x,y$ defined by $$\begin{aligned}
    u &= \frac{-70s^3 + 6sx}{2(25s^2+3x)},\quad
    v = \frac{-3y}{25s^2 + 3x} ,
\end{aligned}$$ which in the affine patch where $s=1$ give $\mathcal{E}_2$ as the curve $x^3-25/3 x+2950/27+y^2 = 0$. In these coordinates $(345)$ acts as $$\begin{aligned}
    x &\mapsto  \frac{5(275 - 3x + 15y)}{3(65 + 15x - 3y)},\quad
    y \mapsto \frac{20(55 - 15x - 3y)}{(65 + 15x - 3y)} .
\end{aligned}$$ Indeed for the projective coordinates $[X:Y:Z]$ of our curve $X^3-25/3 X Z^2 +2950/27 Z^3+Y^2 Z = 0$ we have under $\overline{(345)}$ that $$\begin{aligned}
&\mapsto [{5(275Z/3 - X + 5Y)}:20(55Z - 15X - 3Y):65Z + 15X - 3Y ]\\
&\mapsto [275Z/3 - X - 5Y: -220Z + 60X - 12Y: 13Z + 3X + (3Y)/5  ] \mapsto [X:Y:Z].
\end{aligned}$$ When working with a Weierstrass model of an elliptic curve it is standard to take the distinguished point to be $\infty=[0:1:0]$ and we see in terms of $(x,y)$ that $\infty\mapsto (-25/3, 20)\mapsto (-25/3, -20)\mapsto \infty$.
:::

[^1]: The cosets of $\left\langle (12) \right\rangle$ in the normaliser are $\left\{ e, (12) \right\}$, $\left\{ (345), (12)(345) \right\}$, $\left\{ (354), (12)(354) \right\}$, $\left\{ (34), (12)(34) \right\}$, $\left\{ (35), (12)(35) \right\}$, and $\left\{ (45), (12)(45) \right\}$.
