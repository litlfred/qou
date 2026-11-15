---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-011-43-understanding-the-isomorphism-f
section_title: "Understanding the isomorphism f"
section_number: 4.3
pages: 9-12
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.949
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section4.3 label="section4.3"}

We now turn our attention to the isomorphism, $f$, mentioned in [\[hypiso\]](#hypiso){reference-type="eqref" reference="hypiso"}. Clearly there won't be a single isomorphism since if $a$ is an automorphism of $H$ and $\sigma$ of an automorphism of the HC curve then $\sigma\circ f \circ a$ will also be an isomorphism from the hyperbolic model $H$ to the HC representation. We will exploit this fact.

There are two key ingredients to our identification. First is the rotation of the entire hyperbolic polygon about its centre by $2\pi/5$ (the automorphism $cd$ above). This automorphism allows us to express all twenty of the polygon's edges in terms of just four, a great simplification of our problem. If we knew the values of $f$ on four edges, and the matrix representing $f_*(cd)$, the induced action of $cd$ on the HC curve, then $$\begin{aligned}
  f(\text{edge } k+ 4) &= f\left((cd)(\text{edge } k)\right)
    =  f_*(cd) f(\text{edge } k),
\end{aligned}$$ which allows us to compute the values of $f$ on the remaining 16 edges.

Second is a geodesic reflection of the hyperbolic disc which will correspond to our real structure; the geodesic is denoted by the dashed lines in Fig. [\[fig:bringHyperbolic\]](#fig:bringHyperbolic){reference-type="ref" reference="fig:bringHyperbolic"}. The line starts at $P_3$, goes through $C$ to $P_1$, along edge 1 to $P_2$ and along edge 3 back to $P_3$. If we knew how this acted on the HC model, we would know its fixed points correspond in some manner to edges 1/14 and 3/12, and the marked diameter. Identifying points $P_1$, $P_2$ and $P_3$ on the HC representation would then complete the picture by dividing this fixed line up into just the intervals needed to draw homology paths around known branch points.

Starting with the central rotation $cd$ on the hyperbolic model and some isomorphism $f$ to the HC representation, since all order 5 elements of $S_5$ are conjugate there is an HC-automorphism ${\sigma}\in S_5$ such that $${\sigma} f_*(cd) {\sigma}^{-1} = Z^k,$$ where $k\in\{0,\dots,4\}$ and $$Z : \ [x,y,z] \mapsto \big[\zeta x, \zeta^2 y, z\big].$$ We are being flexible about which power of $Z$ occurs here because later choices (specifically rotations about $R$ in Fig. [\[fig:bringHyperbolic\]](#fig:bringHyperbolic){reference-type="ref" reference="fig:bringHyperbolic"}) will modify any decision made at this stage. But then $$\begin{gathered}
  (\sigma\circ f)_*(cd)  = \sigma_*(f_*(cd))
    = \sigma f_*(cd) \sigma^{-1}
    = Z^k.
\end{gathered}$$ So the isomorphism $\sigma\circ f$ from the hyperbolic model to the HC model sends $cd$ to $Z^k$.

Now consider a rotation about $R$ in Fig. [\[fig:bringHyperbolic\]](#fig:bringHyperbolic){reference-type="ref" reference="fig:bringHyperbolic"} which cyclically permutes the fixed points of $cd$. The fixed points on the hyperbolic side are $C$, $P_1$, $P_2$, $P_3$ and on the HC side $[0,1,0]$, $[0,0,1]$, $[1,0,0]_1$, $[1,0,0]_2$. Let integers $i$ and $n$ be defined by the equations $$\begin{gathered}
  P_i  = (\sigma\circ f)^{-1}([0,0,1]),  \qquad
  R^n(P_i)  = C.
\end{gathered}$$ Then $$\begin{gathered}
  (\sigma\circ f\circ R^{-n})(C)
     = (\sigma\circ f\circ  R^{-n})(R^n(P_i))
    = (\sigma\circ f)(P_i)
    = [0,0,1],
\end{gathered}$$ and further $$\begin{gathered}
  \left(\sigma\circ f\circ R^{-n}\right)_*(cd)
     = (\sigma\circ f)_*\left(R^{-n}_*(cd)\right)
    = (\sigma\circ f)_*\left((cd)^j\right)
    = Z^{jk}
    = Z^m,
\end{gathered}$$ for some integers $j$ and more importantly $m$. Since we haven't fixed the power of $Z$ up to now this means that $\sigma\circ f\circ R^{-n}$ serves our purposes just as well as $\sigma\circ f$ did.

Although we have used most of the available freedoms to constrain the relation between $f$, $Z$ and $C$, we actually still have the ability to apply a central rotation, if it would help since that would alter neither of the properties above.

Next consider complex conjugation on the HC model. This is a symmetry that reverses orientation (and so not part of the $S_5$ symmetry group). It fixes an entire line (the real axis) including the fixed points of $Z$. In the hyperbolic picture this means it must be a reflection about some diameter. We use our final remaining freedom to demand that it is reflection about the dashed diameter in Fig. [\[fig:bringHyperbolic\]](#fig:bringHyperbolic){reference-type="ref" reference="fig:bringHyperbolic"}, i.e. that the real axis in the HC model corresponds to these dashed edges (and diameter).

We now have two tasks remaining:

-   Find out what $P_1$, $P_2$ and $P_3$ become on the HC model so we can describe edge 1/14 as the real path from $P_2$ to $P_1$ and edge 3/12 as the real path from $P_2$ to $P_3$.

-   Find out what power of $Z$ the central rotation of $2\pi/5$ becomes so we can describe (for example) edge 4/15 as $Z^k$ applied to the real path from $P_2$ to $P_3$.

The second task is actually easier to accomplish at this stage. Consider the structure near $[0,0,1]$ (which we demanded was the centre of the polygon, $C$, hyperbolically); there are three sheets coming together at this branch so unwrapping it will effectively divide angles by 3. Mathematically this means that any set of manifold coordinates $\phi : \mathcal{C} \rightarrow \mathbb{C}$ centred on $[0,0,1]$ will satisfy $$\phi([x,y,1])^3 = \alpha x + O\big(x^2\big).$$ In these coordinates, since $[0,0,1]$ is a fixed point $Z : [x,y,z]
\mapsto [\zeta x, \zeta^2 y, z]$ acts locally as a rotation $$Z_{\phi}(t) = \beta t + O\big(t^2\big),$$ where $\beta$ is characteristic of $Z$ and independent of $\phi$. Now, on the one hand $$\begin{gathered}
  Z_{\phi}\left(\phi([x,y,1])\right)^3
     = \phi\left(Z([x,y,1])\right)^3
    = \phi\big([\zeta x,\zeta^2 y,1]\big)^3
    = \alpha \zeta x + O\big(x^2\big),
\intertext{but also}
  Z_{\phi}\left(\phi([x,y,1])\right)^3
     = \left(\beta \phi([x,y,1]) + O\big(\phi^2\big)\right)^3
    = \beta^3 \phi([x,y,1])^3 + O\big(\phi^4\big)
    = \beta^3 \alpha x + O\big(x^2\big).
\end{gathered}$$ So $\beta^3 = \zeta$, or $$\beta = \exp\left(\frac{2\pi\mathrm{i}}{15} + \frac{2\pi\mathrm{i}k}{3}\right)$$ for some $k\in\{0,1,2\}$. But since $Z$ has order 5 we also know that $\beta^5 = 1$, which in terms of $k$ means that $$\frac{2\pi\mathrm{i}}{3}+\frac{10\pi\mathrm{i}k}{3}
  = \frac{2\pi\mathrm{i}}{3}\left(1+5k\right) \in 2\pi\mathrm{i}\mathbb{Z},$$ or $\beta = \exp(\frac{4\pi\mathrm{i}}{5})$ and at last we can conclude that $Z$ corresponds to a rotation of $2\frac{2\pi\mathrm{i}}{5}$ about $C$ in the hyperbolic model.

Intuitively we have unwrapped the three sheets coming together at $[0,0,1]$ to obtain Fig. [1](#fig:001Z){reference-type="ref" reference="fig:001Z"} in $x$. We know that $Z$ sends (say) $[\epsilon,y,1]$ to $[\zeta\epsilon,y',1]$ on some sheet $y'$, which makes it one of the labelled destinations. But only one of these gives an order 5 transformation so we know $Z$ completely.

![Intuitive action of $Z$ near $[0,0,1]$.](001Z){#fig:001Z}

Using this information, together with our knowledge that complex conjugation on the HC model is the dashed reflection in Fig. [\[fig:bringHyperbolic\]](#fig:bringHyperbolic){reference-type="ref" reference="fig:bringHyperbolic"}, allows us to deduce the outline structure in Fig. [2](#fig:firstedges){reference-type="ref" reference="fig:firstedges"}. The dots are the branch-points of the HC model and the grey lines are the images of the hyperbolic polygon's edges under the isomorphism to the HC model. It remains to establish which parts (and sheets) of each spoke in Fig. [2](#fig:firstedges){reference-type="ref" reference="fig:firstedges"} correspond to which hyperbolic edges (for example, does edge $1/14$ correspond to $x>0$ or $x < 0$, and what about $y$?).

![Hyperbolic polygonal edges in the Hulek--Craig model.](craig_edges){#fig:firstedges}

Similar analysis of the other fixed points of $Z$ will allow us actually to identify the remaining $P_i$. We first discover

-   Near $[0,1,0]$, $Z$ is a rotation of $3\left(\frac{2\pi}{5}\right)$.

-   Near $[1,0,0]_1 \sim [1,t^4,t]$, $Z$ is a rotation of $4\left(\frac{2\pi}{5}\right)$.

-   Near $[1,0,0]_2 \sim [1,t,t^4]$, $Z$ is a rotation of $\frac{2\pi}{5}$.

But hyperbolically, it is easy to see that a rotation of $2\left(\frac{2\pi}{5}\right)$ about $C$ (which $Z$ is) is the same as one of $4\left(\frac{2\pi}{5}\right)$ about $P_1$, $3\left(\frac{2\pi}{5}\right)$ about $P_2$ or $\frac{2\pi}{5}$ about $P_3$ so we can deduce that $[0,1,0] \leftrightarrow P_2$, $[1,0,0]_1
\sim [1,t^4,t] \leftrightarrow P_1$ and $[1,0,0]_2 \sim [1,t,t^4]
\leftrightarrow P_3$.

Therefore, edge $1/14$ corresponds to the real path from $[0,1,0]$ to $[1,0,0]_1 \sim [1,t^4,t]$; referring to Fig. [\[fig:craigreal\]](#fig:craigreal){reference-type="ref" reference="fig:craigreal"} we see that this is the path where $y$ starts out large and positive near $x=0$ (and remains positive). Edge 3 corresponds to the real path from $[0,1,0]$ to $[1,0,0]_2\sim [1,t,t^4]$ which turns out to be the one starting out large and negative near $x=0$ (and remaining negative).

The remaining paths ($y$ small near $x=0$) correspond to the diameter of the hyperbolic model and have no large role to play in describing the homology basis.

Other edges can now be obtained by applying a rotation of $2\pi/5$ on the hyperbolic side and $Z^3$ on the HC side. The results are in Table [1](#tab:hypcraigedges){reference-type="ref" reference="tab:hypcraigedges"}.

::: {#tab:hypcraigedges}
  ------- ----------------------------------------------- ------- -----------------------------------------------
     1/14 $[\mathbb{R}_+,\mathbb{R}_+,1]$                     2/9 $[\zeta\mathbb{R}_+,\zeta^2\mathbb{R}_+,1]$
     3/12 $[\mathbb{R}_+,\mathbb{R}_-,1]$                    4/15 $[\zeta^4\mathbb{R}_+,\zeta^3\mathbb{R}_-,1]$
     5/18 $[\zeta^3\mathbb{R}_+,\zeta\mathbb{R}_+,1]$        6/13 $[\zeta^4\mathbb{R}_+,\zeta^3\mathbb{R}_+,1]$
     7/16 $[\zeta^3\mathbb{R}_+,\zeta\mathbb{R}_-,1]$        8/19 $[\zeta^2\mathbb{R}_+,\zeta^4\mathbb{R}_-,1]$
    10/17 $[\zeta^2\mathbb{R}_+,\zeta^4\mathbb{R}_+,1]$     11/20 $[\zeta\mathbb{R}_+,\zeta^2\mathbb{R}_-,1]$
  ------- ----------------------------------------------- ------- -----------------------------------------------

  : Values for $[x,y,1]$ on hyperbolic edges.
:::
