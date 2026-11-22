---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-009-82-wild-input
section_title: "Wild Input"
section_number: 8.2
pages: 18-20
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.969
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linear and integer programming problems."
---
One way to produce symmetric input for (integer) linear optimization algorithms is by brute force: One can take any system $Ax\le b$ of linear inequalities and let the full group $\mathop{\mathrm{Sym}}(n)$ act. This way each original inequality may give up to $n!$ inequalities in the resulting *symmetrized* system. The symmetrized system of inequalities is $\mathop{\mathrm{Sym}}(n)$-invariant by construction. In order to produce input to our algorithms which is less well behaved than the hypertruncated cubes studied above we will apply this procedure to a special class of polytopes, which can be considered "wild". We aim at symmetric polytopes with many facets whose coordinates are not so nice, but still somewhat under control.

The first building block of our construction is the regular hexagon $H$ whose vertices are at distance $56/6$ from the origin, that is, $$H \ = \ \mathop{\mathrm{conv}}\left\{\frac{56}{6} e^{k\pi i/6}\vphantom{k=0,1,\dots,5}\,\right.\left|\,\vphantom{\frac{56}{6} e^{k\pi i/6}}k=0,1,\dots,5\right\} \, .$$ Notice that only in the formula above the letter '$i$' denotes the imaginary unit, and we identify the complex numbers with ${\mathbb{R}}^2$. The coordinates of $H$ are irrational; however, the subsequent steps in the construction are chosen such that we will arrive at a rational polytope in the end. The second item is the regular cross polytope scaled by $73/10$, that is, $$C(d) \ = \ \mathop{\mathrm{conv}}\left\{\pm \frac{73}{10} e_i\vphantom{i\in[d]}\,\right.\left|\,\vphantom{\pm \frac{73}{10} e_i}i\in[d]\right\} \, .$$ Finally, we consider the *join* $P*Q$ of two polytopes $P\subset{\mathbb{R}}^\delta$ and $Q\subset{\mathbb{R}}^\epsilon$, which is defined as $$\begin{split}
  P*Q \ = \ \mathop{\mathrm{conv}}\bigl(&\left\{(x,0,1)\in{\mathbb{R}}^\delta\times{\mathbb{R}}^\epsilon\times{\mathbb{R}}\vphantom{x\in P}\,\right.\left|\,\vphantom{(x,0,1)\in{\mathbb{R}}^\delta\times{\mathbb{R}}^\epsilon\times{\mathbb{R}}}x\in P\right\}\\
  &\cup \left\{(0,y,-1)\in{\mathbb{R}}^\delta\times{\mathbb{R}}^\epsilon\times{\mathbb{R}}\vphantom{y\in Q}\,\right.\left|\,\vphantom{(0,y,-1)\in{\mathbb{R}}^\delta\times{\mathbb{R}}^\epsilon\times{\mathbb{R}}}y\in Q\right\}\bigr) \, .
\end{split}$$ If $P$ and $Q$ are full-dimensional polytopes with $\mu$ and $\nu$ vertices, respectively, the join $P*Q$ has dimension $\delta+\epsilon+1$ and $\mu+\nu$ vertices. For the combinatorics of $P*Q$ the exact values for the $(\delta+\epsilon+1)$st coordinate are inessential, as long as they are distinct. We now replace the "$-1$" for the second factor by $-11/12$ to obtain the *distorted join* $$\begin{split}
J(d) \ = \ \mathop{\mathrm{conv}}\bigl(&\left\{(x,0,1)\in{\mathbb{R}}^2\times{\mathbb{R}}^d\times{\mathbb{R}}\vphantom{x\in H}\,\right.\left|\,\vphantom{(x,0,1)\in{\mathbb{R}}^2\times{\mathbb{R}}^d\times{\mathbb{R}}}x\in H\right\}\\
  &\cup \left\{(0,y,-\frac{11}{12})\in{\mathbb{R}}^2\times{\mathbb{R}}^d\times{\mathbb{R}}\vphantom{y\in C(d)}\,\right.\left|\,\vphantom{(0,y,-\frac{11}{12})\in{\mathbb{R}}^2\times{\mathbb{R}}^d\times{\mathbb{R}}}y\in C(d)\right\}\bigr) \,
\end{split}$$ of the hexagon $H$ with the cross polytope $C(d)$. This polytope is further modified in two steps: First we perturb by rounding the (rational and irrational) coordinates to three decimal places and treating these as exact rational numbers. Since the polytopes $H$, $C(d)$, and $J(d)$ are simplicial this perturbation does not change the combinatorial types. Secondly, we symmetrize the polytope by letting the group $\mathop{\mathrm{Sym}}(d+3)$ act on the facets of the perturbed polytope. The resulting inequalities form the input of our second class of experiments.

The parameters $56/6$, $73/10$, and $11/12$ which occur in the construction are chosen, more or less, at random. They do not have a specific meaning. We refrain from further investigating these symmetrized distorted joins and the geometry of lattice points inside. This would be tedious and at the same time irrelevant for our purposes.

::: tabular*
\@rrrrr@ & &\
& & & &\
& 0.00 & 0.01 & 0.00 & 0.00\
4 & 0.00 & 0.06 & 0.01 & 0.00\
5 & 0.00 & 0.17 & 0.01 & 0.02\
6 & 0.05 & 0.74 & 0.04 & 0.04\
7 & 0.13 & 2.71 & 0.09 & 0.13\
8 & 0.62 & 10.15 & 0.24 & 0.38\
9 & 2.08 & 42.06 & 0.69 & 1.03\
10 & 8.02 & 135.51 & 1.86 & 2.89\
:::

The interesting fact is that we get symmetric polytopes which are somewhat complicated, because they have lots of inequalities: for instance, yielding $885,\!768$ inequalities for $d=10$. As a consequence `CPLEX` cannot deal with these examples in a fully automated way. The best parameter settings that we found were

::: center
  ------------------------- ----
  parallel thread count:       1
  presolve indicator:         no
  feas. pump heuristic:       -1
  RINS heuristic:             -1
  MIP optimization emph.:      2
  ------------------------- ----
:::

But even with these adjustments our implementation outperforms `CPLEX` by a large margin; see Table [\[tab:joinNgonCross\]](#tab:joinNgonCross){reference-type="ref" reference="tab:joinNgonCross"}. This holds in spite of the fact that `polymake` computes with exact rational numbers throughout.
