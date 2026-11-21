---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-013-5-numerical-determination-of-the-eigenspace-asso
section_title: "Numerical determination of the eigenspace associated to 1"
section_number: 5
pages: 32-37
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.992
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
Having established that the first eigenvalue of the Fricke-Macbeath surface has a multiplicity of 7, our objective in this section is to numerically determine which 7-dimensional representation of $\Aut(\X)=\Delp/\Gamma$ corresponds to the eigenspace associated to $\la_1$. There are four 7-dimensional irreducible representations of $\Aut(\X)\cong \PSL_2(8)$. Refer to Table [1](#table:character_table){reference-type="ref" reference="table:character_table"} for the character table of $\Aut(\X)$. You can find the GAP code in Appendix [\[sec:appB\]](#sec:appB){reference-type="ref" reference="sec:appB"} to obtain the character table. See [@MR0827219 p. 6] for more information about the character table. In the character table, $A, B, C, D, E,$ and $F$ are defined as follows: $$\label{eq:abcdef}
\begin{aligned}
A &= \zeta_7^3 + \zeta_7^4, & B &= \zeta_7^2 + \zeta_7^5, & C &= \zeta_7 + \zeta_7^6, \\
D &= -\zeta_9^4 - \zeta_9^5, & E &= -\zeta_9^2 - \zeta_9^7, \\
F &= \zeta_9^2 + \zeta_9^4 + \zeta_9^5 + \zeta_9^7.
\end{aligned}$$ Here, $\zeta_n = e^{2\pi \i /n}$.

::: {#table:character_table}
              **1A**   **2A**   **3A**   **7A**   **7B**   **7C**   **9A**   **9B**   **9C**
  ---------- -------- -------- -------- -------- -------- -------- -------- -------- --------
  $\chi_1$      1        1        1        1        1        1        1        1        1
  $\chi_2$      7        -1       -2       0        0        0        1        1        1
  $\chi_3$      7        -1       1        0        0        0       $D$      $F$      $E$
  $\chi_4$      7        -1       1        0        0        0       $E$      $D$      $F$
  $\chi_5$      7        -1       1        0        0        0       $F$      $E$      $D$
  $\chi_6$      8        0        -1       1        1        1        -1       -1       -1
  $\chi_7$      9        1        0       $A$      $C$      $B$       0        0        0
  $\chi_8$      9        1        0       $B$      $A$      $C$       0        0        0
  $\chi_9$      9        1        0       $C$      $B$      $A$       0        0        0

  : Character table of $\Aut(\X) \cong \PSL_2(8)$; the values of $A, B, C, D, E,$ and $F$ are given in [\[eq:abcdef\]](#eq:abcdef){reference-type="eqref" reference="eq:abcdef"}
:::

GAP enumerates representative elements from each conjugacy class as follows:

1.  $\id$

2.  $a^2 b (b a^2)^2 b^3 a^2 b$

3.  $a$

4.  $a^2 b (b a^2)^2 b^3 a^2$

5.  $b^4 a^2 (b a^2 b)^2$

6.  $a^2 b^3 (b a^2)^2 b^2$

7.  $(a b^2 a)^2 a b^3 a$

8.  $a (b a^2 b)^2 b^2 a^2$

9.  $a b^2 (b^2 a^2)^2 b$

For the actions of the generators $a$ and $b$ on $\disk$, recall [\[eq:matrixA\]](#eq:matrixA){reference-type="eqref" reference="eq:matrixA"} and [\[eq:matrixB\]](#eq:matrixB){reference-type="eqref" reference="eq:matrixB"}.

It is noteworthy that the outer automorphism group of $\PSL_2(8)$ has order 3. An outer automorphism interchanges the conjugacy classes of elements of order 9 with each other and similarly for those of order 7. Consequently, there is an inherent ambiguity in assigning specific labels like **9A**, **9B**, **9C** to elements of order 9, and similarly, **7A**, **7B**, **7C** to those of order 7. Throughout this section, we will adhere to the aforementioned convention for naming conjugacy classes.

Here we present a numerical method to compute the character of a representation obtained from a set of eigenfunctions. Assume that we have a set of eigenfunctions, denoted as $L = \{f_1,\dots, f_n\}$, which have close eigenvalues. These eigenfunctions are expected to form a basis for a representation of $\Aut(\X)$, which may not necessarily be irreducible.

One of the core assumptions in our approach is that we can approximate the value $f_i(z)$ for a given point $z \in \F$. For instance, by employing the finite element method on $\F$, along with periodic boundary conditions determined by side-pairing transformations, we can achieve such approximations for eigenfunctions of hyperbolic surfaces. The application of these methods to the Bolza surface, a genus 2 Riemann surface with the highest number of symmetries, has been introduced in [@MR1028714]. Cook's dissertation [@cook2018] provides FreeFEM++ [@MR3043640] code to compute low-lying eigenvalues and eigenfunctions for certain compact Riemann surfaces of low genera, albeit not including the Fricke-Macbeath surface. For further details, see appendices C, D, and E in [@cook2018]. Meanwhile, an alternative approach detailed in [@MR3009726] delivers exceptionally accurate numerical eigenvalues and eigenfunctions. Although this method promises accuracy, its implementation seems to be quite challenging.

For our numerical evaluations, we have utilized Mathematica [@Mathematica]. Within this environment, the `NDEigensystem` function serves as an instrumental tool for determining the eigenvalues and eigenfunctions of differential operators over a given region. A distinctive capability of this function is its adeptness in handling periodic boundary conditions. With the `PeriodicBoundaryCondition` option, the function allows specific boundary pairs to be treated as if they were identical.

To begin, we initiate the following preliminary procedures:

-   Select an interior point $z_0$ within $\F$ that is not fixed by any element of $\Del$. Additionally, ensure that the orbits of $z_0$ under $\Del$ do not intersect the boundary of $\F$. An appropriate point can readily be located within the fundamental triangle of $\Del$, as shown in Figure [\[fig:237_tri\]](#fig:237_tri){reference-type="ref" reference="fig:237_tri"}.

-   Determine representatives $S=\{M_1,\dots, M_d\}\subseteq \Delp$ for $\Aut(\X) = \Delp/\Gamma$ such that each $z_k : = M_k z_0$ lies within $\F$ for all $k\in \{1,\dots, d\}$. Here, $d=|\Aut(\X)|$. We can find such a list, for example, as follows :

    -   Enumerate elements of the Coxeter group $\Del$ based on length.

    -   Collect all elements $M\in \Del$ of even length such $M z_0$ is contained in the interior of $\F$.

    -   Given our choice of $z_0$, these collected elements serve as representatives for $\Aut(\X) = \Delp/\Gamma$.

-   For each eigenfunction $f$ in $L$, compute the approximate values of $f(z_k)$ for all $k\in \{1,\dots, d\}$.

Given $M_l\in S$ and $f_i \in L$, we want to express the transformed function $M_l\cdot f_i$ as a linear combination of $\{f_1,\dots, f_n\}$, meaning that $$(M_l\cdot f_i)(z) = f_i(M_l^{-1}z) = \sum_{j=1}^n \rho(M_l,i,j)f_j(z),\, z\in \F.$$ Here, the matrix $\left(\rho(M_l,i,j)\right)_{i,j}$ serves as the representation matrix for $M_l$. Our goal is to approximate these matrix entries, treating $\{\rho(M_l,i,j)\}$ as the unknowns we want to determine.

For a given pair $(l,i)$, the equation $$\sum_{j=1}^n \rho(M_l,i,j)f_j(z_k) = f_i(M_l^{-1}z_k), \, k=1,\dots, d
\label{eq:rho_equation}$$ yields $d$ relations with $n$ unknowns $\{\rho(M_l,i,j) : j=1, \dots, n\}$. Therefore, when $d$ significantly exceeds $n$, we obtain an overdetermined system of linear equations for those unknowns. For our particular case, the values are $d=504$ and $n=7$. To handle such overdetermined systems, a common approach is to use the least squares method. This method seeks to minimize the sum of the squares of the residuals, which are the differences between the left and the right sides of [\[eq:rho_equation\]](#eq:rho_equation){reference-type="eqref" reference="eq:rho_equation"}. By applying this method, we can approximate the values of $\{\rho(M_l,i,j)\}$.

To enhance the system's robustness further, one could perturb the initial point $z_0$ to obtain $z_0'$ and then consider its orbits $z_k'$ under the action of $\Aut(\X)$. This leads to an extended set of relations, in addition to those in [\[eq:rho_equation\]](#eq:rho_equation){reference-type="eqref" reference="eq:rho_equation"}: $$\sum_{j=1}^n \rho(M_l,i,j)f_j(z_k') = f_i(M_l^{-1}z_k'), \, k=1,\dots, d.$$ By doing so, we can also increase the number of equations, even when $d$ is small compared to $n$.

Note that on the right-hand side of [\[eq:rho_equation\]](#eq:rho_equation){reference-type="eqref" reference="eq:rho_equation"}, $M_l^{-1}z_k=M_l^{-1}M_k z_0$ may not be a point in $\F$. Since our approach relies on knowing approximate values of $f_i(z_j)$ for orbits $z_j\in \F$ of $z_0$, calculating $f_i(M_l^{-1}z_k)$ presents a challenge. Given $(l, k)$, we need to find $p\in \{1,\dots, d\}$ and $\gamma\in \Gamma$ such that $$\gamma M_l^{-1}M_k = M_p.
\label{eq:findp}$$ Once we find $(p,\gamma)$, we can simply set $f_i(M_l^{-1}z_k)=f_i(M_p z_0) = f_i(z_p)$ due to the $\Gamma$-invariance of $f_i$.

Equation [\[eq:findp\]](#eq:findp){reference-type="eqref" reference="eq:findp"} can be equivalently stated as: $$\gamma M_l^{-1}M_kz_0 = M_p z_0.$$ This formulation is essentially about moving the point $M_l^{-1}M_kz_0 = M_l^{-1}z_k$ into the fundamental domain $\F$ through the action of $\Gamma$. Notably, $\F$ is also the Dirichlet domain $D(0)$ from Theorem [\[thm:dirichlet\]](#thm:dirichlet){reference-type="ref" reference="thm:dirichlet"}. In [@MR2541438], Voight explored various algorithms related to such fundamental domains for Fuchsian groups. Of particular interest is an algorithm that, when given a point $z \in \disk$, returns a point $z' \in \F$ and an element $\gamma \in \Gamma$ such that $z' = \gamma(z)$. This algorithm is detailed further in [@MR2541438 Algorithm 4.3]. In the context of our study, we begin by setting $z = M_l^{-1}z_k$. Subsequently, we identify a side-pairing transformation $\gamma_i$ such that $\gamma_i z$ is closer to the fundamental polygon $\F$ than the original location of $z$, meeting the condition: $$\distD(0, \gamma_i z) \leq \distD(0, z).$$ As long as the point $z$ is not located inside the fundamental domain $\F$, such a transformation $\gamma_i$ exists. This procedure can be iterated until we identify a $\Gamma$-orbit of $z$ inside $\F$. By employing this method, we can effectively relocate $z$ to $\F$ using the generators $\{\gamma_i\}$ of $\Gamma$. While determining $\gamma$ and $M_p$ for [\[eq:findp\]](#eq:findp){reference-type="eqref" reference="eq:findp"} may involve numerical calculations, we can verify its correctness in a symbolic manner using [\[eq:coxrelation\]](#eq:coxrelation){reference-type="eqref" reference="eq:coxrelation"}.

Once we apply the method described above to determine the 7-dimensional representation $V_{\la_1}$ formed by eigenfunctions with eigenvalue $\la_1$, we obtain the following numerical values for its character $\chi_{\la_1}$: $$\begin{array}{c|c|c|c|c|c|c|c|c}
\textbf{1A} & \textbf{2A} & \textbf{3A} & \textbf{7A} & \textbf{7B} & \textbf{7C} & \textbf{9A} & \textbf{9B} & \textbf{9C} \\
\hline
7.0000 & -1.0163 & 0.9614 & 0.0778 & 0.0231 & 0.0059 & -1.4985 & -0.3453 & 1.8829 \\
\end{array}$$ Recall that the inner product of two characters $\chi, \chi'$ of $G$ are defined by $$\langle \chi, \chi' \rangle = \frac{1}{|G|} \sum_{g \in G} \chi(g) \ol{\chi'(g)}.$$ When we compute the inner product of characters $\chi_{\la_1}$ and $\chi_i$, we obtain the following approximate values of $m_i = \langle \chi_{\la_1}, \chi_i \rangle$ for each $i$: $$\begin{array}{c|c|c|c|c|c|c|c|c|c}
\hline
i & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
\hline
m_i & 0.0133 & 0.0150 & 0.0043 & -0.0037 & 0.9927 & 0.0152 & -0.0183 & -0.0119 & 0.0088 \\
\hline
\end{array}$$ Note that $m_i$ is the multiplicity of $\chi_i$ in the decomposition of $\chi_{\la_1}$ into irreducible representations. Given that these values are close approximations of integers, it becomes straightforward to guess their exact integer values. Hence we propose the following conjecture:

::: conjecture
[]{#conj:rep7 label="conj:rep7"} Let $V_{\la_1}$ be the 7-dimensional representation of $\Aut(\X)$ formed by eigenfunctions with eigenvalue $\la_1$. The character of $V_{\la_1}$ is equal to $\chi_5$.
:::

From our numerical computations, we have obtained the following 7 approximate values for $\la_1, \dots, \la_7$: $$1.25065,1.25336,1.25336,1.26103,1.26103,1.28662,1.38342.$$ Despite the lack of precision in these values, it is evident that we can still obtain convincing evidence for the true values of $\chi_{\la_1}$. Similarly, we have obtained the following 9 approximate values for $\la_8, \dots, \la_{16}$: $$2.05821,2.0602,2.06123,2.06488,2.0661,2.08243,2.09857,2.09857,2.2991.$$ While the accuracy of these values remains uncertain, the eigenfunctions for these eigenvalues appear to span a 9-dimensional representation of $\Aut(\X)$. Its character seems to be a good approximation to $\chi_9$ in Table [1](#table:character_table){reference-type="ref" reference="table:character_table"}.
