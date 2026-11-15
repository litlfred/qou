---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-009-41-genera-of-quotients
section_title: "Genera of Quotients"
section_number: 4.1
pages: 18-20
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.965
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: genera of quotients label="subsec: genera of quotients"} Our first step is to know the topology of the quotients we are going to find. To this end, we give the following result.

::: prop
The data of the quotients of $\mathcal{B}$ by subgroups $\left\langle \sigma \right\rangle \leq S_5$ is summarised by the following table:

::: center
    $\sigma$     Example   $\left\lvert{cl(\sigma)}\right\rvert$   $\left\lvert{\operatorname{Fix(\sigma)}}\right\rvert$   Fixed Points   $N_{S_5}(\left\langle \sigma \right\rangle)/\left\langle \sigma \right\rangle$   $g\left( \mathcal{B}/\left\langle \sigma \right\rangle \right)$
  ------------- --------- --------------------------------------- ------------------------------------------------------- -------------- -------------------------------------------------------------------------------- -----------------------------------------------------------------
     $(12)$        \-                       10                                               6                                Edges                                           $S_3$                                                                       1
                                                                                                                                                                                                                          
     $(123)$      $R S$                     20                                               0                                  \-                                            $V_4$                                                                       2
                                                                                                                                                                                                                          
   $(12)(34)$      $R$                      15                                               2                               Vertices                                         $V_4$                                                                       2
                                                                                                                                                                                                                          
    $(1234)$       $U$                      30                                               2                               Vertices                                         $C_2$                                                                       1
                                                                                                                                                                                                                          
   $(123)(45)$     \-                       20                                               0                                  \-                                            $C_2$                                                                       0
                                                                                                                                                                                                                          
    $(12345)$      $S$                      24                                               4                             Face-centres                                       $C_4$                                                                       0
:::

Here $cl(\sigma)$ is the conjugacy class of $\sigma$, $\operatorname{Fix}(\sigma) = \{ P \in \mathcal{B} \, | \, \sigma(P) = P \}$.
:::

::: proof
*Proof.* As conjugate elements yield isomorphic quotients we need only to give one $\sigma$ per conjugacy class. The first three columns follow from the group theory we have previously shown in §[\[subsec: automorphism group\]](#subsec: automorphism group){reference-type="ref" reference="subsec: automorphism group"}, the fourth and fifth follow from §[\[sec: geometric points\]](#sec: geometric points){reference-type="ref" reference="sec: geometric points"} and the sixth is elementary group theory. The final column remaining is then a Riemann-Hurwitz argument for genus, which will we demonstrate for the quotient by $(2345)$ as in [@Riera1992].

For general $\sigma$, denoting by $\pi$ the projection $\mathcal{B} \to {\mathcal{B}}/{\left\langle \sigma \right\rangle} := H$, Riemann-Hurwitz says $$\begin{aligned}
g_\mathcal{B}-1 &= (\deg \pi )(g_H-1) + \frac{1}{2} B  , 
\end{aligned}$$ where $B$ is the degree of ramification of $\pi$, which in the case of a quotient by a group action corresponds to the fixed point structure of $\sigma$.

Consider $(24)(35)$. A fixed point of $\mathcal{B}$ under this, given by projective coordinates $x_i,  i=1, \dots, 5$, must have $$(x_1 , x_4 , x_5 , x_2 , x_3) = (\lambda x_1 , \lambda x_2 , \lambda x_3 , \lambda x_4 , \lambda x_5)  .$$ From this we can see $\lambda = \pm 1$. Taking $\lambda=1$ gives no solutions, but taking $\lambda=-1$ one finds the equations $$x_1 = 0, \quad x_1^2 + 2x_2^2 + 2x_3^2 = 0, \quad x_1^3=0,$$ which gives the 2 fixed points $[0:1:\pm i:-1:\mp i]$. Hence we have $$\begin{aligned}
 4-1 = 2(g_H-1) + \frac{1}{2}(1+1)   
\Rightarrow  g_H = 2  . 
\end{aligned}$$ Moving now to $(2 3 4 5)$, thinking about the possible branching structure we get from Riemann-Hurwitz $$3 = 4(g_H-1) + \frac{1}{2} \left[ \sum_{P \in \operatorname{Fix}(\sigma)} 3 + \sum_{P \in \operatorname{Fix}(\sigma^2)\setminus \operatorname{Fix}(\sigma)} 1 \right]  .$$ Fixed points of $(2345)$ will correspond to points such that $$(x_1 , x_3 , x_4 , x_5 , x_2) = (\lambda x_1 , \lambda x_2 , \lambda x_3 , \lambda x_4 , \lambda x_5)  ,$$ and we get the constraint $\lambda^4=1$. The equations of the curve become $$\begin{aligned}
    x_1 + x_2 (1+ \lambda + \lambda^2 + \lambda^3) &= 0  , \\
    x_1^2 + x_2^2 (1 + \lambda^2 + 1+ \lambda^2) &= 0  , \\
    x_1^3 + x_2^3(1 + \lambda^3 + \lambda^2 + \lambda) &= 0  , 
\end{aligned}$$ and checking the possible cases one finds that the only fixed points of $(2345)$ are $[0:1:\pm i : -1: \mp i]$. These are also the only fixed points of $(24)(35) = (2345)^2$ and so the second sum vanishes, hence we find $g_H=1$. ◻
:::

R&R [@Riera1992] provides a nice visual interpretation of the quotient by a 4-cycle, namely think of a sphere with 4 handles attached around an equator, then $(2345)$ is the cycle rotating these handles to each other by a quarter turn about the axis through the center of the equator. The fixed points are then where this axis intersects the sphere. Edge [@Edge1978], citing Wiman, says that Bring's curve "is, in ten different ways, in $(2,1)$ correspondence with a plane curve of genus 1\". The 10 $(2,1)$ correspondences noted by Edge are exactly the 10 quotients by a transposition giving a $2:1$ map $\mathcal{B} \to \mathcal{E}$, where $\mathcal{E}$ is an elliptic curve. Such a map is called a bielliptic structure, and Bring's curve is the unique genus-4 curve to have 10 such structures [@Casnati2005]. This table also lets us reconstruct the results about the gonality of Bring's curve from [@Gromadzki2010].
