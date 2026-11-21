---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-007-33-real-paths-on-the-hulek-craig-curve
section_title: "Real paths on the Hulek-Craig curve"
section_number: 3.3
pages: 5-6
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.871
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section3.3 label="section3.3"}

The real structure of the HK curve leads to real ovals. Here we shall show there is in fact one. We begin by looking at portions of this oval, which we shall refer to as a 'real path' and then indicate how they join together[^1]. The real paths in this cover will be of particular interest later on so we will take some time to explore their nature now. We begin with the affine curve, further noting what happens at the real infinite points $[0,1,0]$, $[1,0,0]_{1,2}$ which compactify the real curve.

First, if the number of real roots of [\[craigp1\]](#craigp1){reference-type="eqref" reference="craigp1"} considered as a polynomial in $y$ changes then its discriminant $$\begin{gathered}
 \Delta(x) = -x^3\big(256 x^{20}-1349x^{15}+5386x^{10}-7749x^5+3456\big)\nonumber\\
 \hphantom{\Delta(x)}{}  =
 -x^3\big(256 u^2-837 u+3456\big)(u-1)^2, \qquad u=x^5,  \label{eq:disc}
\end{gathered}$$ must vanish there. The only real roots of the equation $\Delta(x)=$ are $x=0,1$, so we are reduced to considering the intervals $(-\infty,0), (0,1),
(1,\infty)$.

-   If $x < 0$ then there is just one real root.

-   If $0 < x < 1$ then there are three real roots.

-   If $x > 1$ then there are also three real roots.

Referring to the expansions [\[eq:x0exp1\]](#eq:x0exp1){reference-type="eqref" reference="eq:x0exp1"} and [\[eq:x0exp2\]](#eq:x0exp2){reference-type="eqref" reference="eq:x0exp2"} we see that a real path starting with $x < 0$ moving towards $x=0$ must be approaching $[0,0,1]$ along the expansion $y = 2^{-1/3} x^{1/3}
+\cdots$ (i.e. $y\rightarrow 0$ too). Continuity demands that when extended past $x=0$ it too should have $y$ small and positive for small $x>0$. We will call this path $\gamma_0$.

We now turn our attention to another real path approaching $x=0$, this time for $x>0$. It must lie on the expansion $y=\sqrt{2} x^{-1/2} +
\cdots$ and hence $y$ is either large and positive or large and negative; we will call these paths $\gamma_{+}$ and $\gamma_{-}$. In fact the expansion is telling us that $\gamma_{+}$ and $\gamma_{-}$ meet at $[0,1,0]$ and we could form a single continuous path, but we will maintain the distinction for now.

In summary we have three real paths coming out of $x=0$ along the positive axis, satisfying (for small $x > 0$), $$y(\gamma_{-}) \ll 0 < y(\gamma_0) \ll y(\gamma_+).$$

Now we are ready to consider what happens at $x=1$. On the desingularised curve there are three real points here (the two from desingularising $y=1$ and the remaining real root $\alpha$). Each of the curves coming out of $x=0$ must pass through one of them. Further, the order of the $y$ values among the paths must be the same approaching $x=1$ as it was leaving $x=0$ since, otherwise, they would have crossed in between and this would have shown itself in [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"}.

The three expansions near $x=1$ in order of increasing $y$ for $x <
1$ are $$\begin{gathered}
  y  \approx \alpha,\qquad
  y  \approx 1 + (x-1)\frac{-1+\sqrt{5}}{2}, \qquad
  y  \approx 1 + (x-1)\frac{-1-\sqrt{5}}{2}.
\end{gathered}$$ Thus the path that started $y\ll 0$ must pass through the first point, $y\approx 0$ must pass through the second and $y\gg 0$ the third. Significantly this means the latter two paths actually cross at $x=1$ and for $x=1+\epsilon$ we have $$y(\gamma_{-}) < y(\gamma_{+}) < 1 < y(\gamma_0).$$

Finally we consider the remaining points $[1,0,0]_{1,2}$ at $\infty$. Recall the expansions [\[eq:inftyExp\]](#eq:inftyExp){reference-type="eqref" reference="eq:inftyExp"}. If $x \ll 0$ then naturally there is only one real path, which arrives at $[1,0,0]_1$ with small $y$. If $x \gg 0$ the situation is very similar to $x=0$: two expansions with $|y| \gg
0$ arriving at $[1,0,0]_2$ and one lying between these with $y \approx 0$. As before, the paths cannot have crossed between $x=1$ and $x=\infty$ and so we are forced to conclude that $\gamma_-$ has the expansion $y\approx
-x^{3/4}$, $\gamma_+$ has the expansion $y\approx x^{-3}$ and $\gamma_0$ has the expansion $y\approx x^{3/4}$ near $\infty$.

Putting these facts together we can plot Fig. [1](#fig:craigreal){reference-type="ref" reference="fig:craigreal"} (the joined semicircular dots represent the same point on the curve, separated to show the distinct $y$ values of paths entering them). We discover that all the paths ($\gamma_-$, $\gamma_0$, $\gamma_+$ and the $x<0$ path) actually form part of one large closed loop showing that the real structure of the HK curve has one oval. (Another proof of this will be given in the next section.)

![Real paths on the Hulek--Craig curve as a branched cover of $\mathbb{P}^1$.](craig_real){#fig:craigreal}

[^1]: The Maple command `plot_real_curve`$(x y^5 + x + x^2 y^2 - x^4 y - 2 y^3,x,y)$ will in fact plot this directly.
