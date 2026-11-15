---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-002-12-strategy-to-prove-the-volume-conjecture
section_title: "Strategy to prove the volume conjecture"
section_number: 1.2
pages: 3-3
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by"
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 1.0
---
[]{#strate label="strate"} In this subsection, we briefly discuss our approach to study the volume conjecture. A standard way to prove volume conjecture involves three steps. Roughly speaking, first of all, given the explicit formula of the colored Jones polynomials of a link $L$ evaluated at the $(N+1/2)$-th root of unity, we convert it into an integral of the form $$\int_D f(z_1,z_2,\dots,z_n)\exp\left( \left(N+\frac{1}{2}\right) \Phi_L(z_1,z_2,\dots,z_n) \right) dz_1dz_2 \dots dz_n,$$ where $(z_1,z_2,\dots,z_n)\in {\mathbb C}^n$ for some $n$, $f(z_1,z_2,\dots,z_n)$ is a holomorphic function and $\Phi_L(z_1,z_2,\dots,z_n)$ is called the potential function of the link $L$. After that, we apply the saddle point approximation, which says that the large $N$ behavior of the integral is determined by the critical value of the potential function at certain non-degenerate critical point.

The last step is to show that the real part of the critical value gives us the hyperbolic volume of the link complement. Recall that in order to find the critical point of the potential function, we need to solve the critical point equations $$\frac{\partial}{\partial z_i}\Phi_L(z_1,z_2,\dots,z_n)=0 \quad\text{ for $i=1,2,\dots, n$}$$ It turns out that in many situations, the critical point equations of the potential function coincide with the hyperbolic gluing equations (e.g. edges equations, surgery equations) of certain triangulation of the link complement with shapes parameters parametrized by $z_1,z_2,\dots,z_n$. Finally, we need to argue that the critical value of the potential function gives the hyperbolic volume of the link complement.

This approach has been used to study the volume conjecture of the colored Jones polynomials for the figure eight knot [@HM13], the $5_2$ knot [@O52], and knots with 6 or 7 crossings [@O6; @O7]. Moreover, the correspondence between the critical point equations of the potential function to the edges equations of certain triangulation has been studied for the twist knots [@CMY09] and two bridge knots [@KO05].

Once the original volume conjecture is proved in this way, the generalized volume conjecture can be proved by the 'continuity argument'. The continuity argument has been used in [@WA17]. The key point is that all the technical assumptions in the above analysis depend continuously on the potential function $\Phi_L(z_1,z_2,\dots,z_n)$. In particular, if we change the colors $M_i$, we obtain a family of potential functions which depends smoothly on the parameters $s_i$. Therefore, as long as $s_i$'s are sufficiently close to $1$, the above analysis works and the result follows.

::: remark
It turns out that for the colored Jones polynomials of the Whitehead link and the Whitehead chains, we obtain two potential functions, and both of them give the hyperbolic volume of the link complement at certain critical points. See Section [\[formula\]](#formula){reference-type="ref" reference="formula"} for more details.
:::
