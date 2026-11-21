---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-019-35-the-question-of-compatibility
section_title: "The Question of Compatibility"
section_number: 3.5
pages: 62-65
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.917
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:compatibility label="sec:compatibility"}

We now have two routes to the ${\rm Spin}(10)$ theory. In Section [\[sec:so(10)\]](#sec:so(10)){reference-type="ref" reference="sec:so(10)"} we saw how to reach it via the ${\rm SU}(5)$ theory:

$$\xymatrix{
{G_{\mbox{\rm SM}}}\ar[r]^-\phi \ar[d] & {\rm SU}(5) \ar[r]^-\psi \ar[d] & {\rm Spin}(10) \ar[d] \\  
{\rm U}(F \oplus F^*) \ar[r]^-{{\rm U}(f)} & {\rm U}(\Lambda{\mathbb C}^5) \ar[r]^-1 & {\rm U}(\Lambda{\mathbb C}^5) \\
}$$ $$\xymatrix{ & \ar@{~>}[r]_{\txt{More Unification}} & }$$

Our work in that section and in Section [\[sec:su(5)\]](#sec:su(5)){reference-type="ref" reference="sec:su(5)"} showed that this diagram commutes, which is a way of saying that the ${\rm Spin}(10)$ theory extends the Standard Model.

In Section [\[sec:route\]](#sec:route){reference-type="ref" reference="sec:route"} we saw another route to the ${\rm Spin}(10)$ theory, which goes through ${\rm Spin}(4) \times {\rm Spin}(6)$: $$\xymatrix{
{G_{\mbox{\rm SM}}}\ar[r]^-\theta \ar[d]       & {\rm Spin}(4) \times {\rm Spin}(6) \ar[r]^-\eta \ar[d]  & {\rm Spin}(10) \ar[d] \\  
{\rm U}(F \oplus F^*) \ar[r]^-{{\rm U}(h)} & {\rm U}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[r]^-{{\rm U}(g)} & {\rm U}(\Lambda{\mathbb C}^5) \\
}$$ $$\xymatrix{ & \ar@{~>}[r]_{\txt{More Unification}} & }$$ Our work in that section and Section [\[sec:g(2,2,4)\]](#sec:g(2,2,4)){reference-type="ref" reference="sec:g(2,2,4)"} showed that this diagram commutes as well. So, we have *another* way to extend the Standard Model and get the ${\rm Spin}(10)$ theory.

Drawing these two routes to ${\rm Spin}(10)$ together gives us a cube: $$\xymatrix{
& {G_{\mbox{\rm SM}}}\ar[rr]^\phi \ar[dl]_\theta \ar'[d] [ddd] & & {\rm SU}(5) \ar[dl]_\psi \ar[ddd] \\
{\rm Spin}(4) \times {\rm Spin}(6) \ar[rr]^\eta \ar[ddd] & & {\rm Spin}(10) \ar[ddd] & \\
& & & \\
& {\rm U}(F \oplus F^*) \ar'[r]^(0.8){{\rm U}(f)}[rr] \ar[dl]_-{{\rm U}(h)} & & {\rm U}(\Lambda{\mathbb C}^5) \ar[dl]_-1 \\
{\rm U}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[rr]^-{{\rm U}(g)}  & & {\rm U}(\Lambda{\mathbb C}^5) & \\
}$$ Are these two routes to ${\rm Spin}(10)$ theory the same? That is, does the cube commute?

::: thm
[]{#thm:cube label="thm:cube"} The cube commutes.
:::

*Proof*. We have already seen in Sections [\[sec:su(5)\]](#sec:su(5)){reference-type="ref" reference="sec:su(5)"}-[\[sec:route\]](#sec:route){reference-type="ref" reference="sec:route"} that the vertical faces commute. So, we are left with two questions involving the horizontal faces. First: does the top face of the cube $$\xymatrix{
& {G_{\mbox{\rm SM}}}\ar[rr]^\phi \ar[dl]_\theta  & & {\rm SU}(5) \ar[dl]_\psi \\
{\rm Spin}(4) \times {\rm Spin}(6) \ar[rr]^\eta & & {\rm Spin}(10) & \\
}$$ commute? In other words: does a symmetry in ${G_{\mbox{\rm SM}}}$ go to the same place in ${\rm Spin}(10)$ no matter how we take it there? And second: does the bottom face of the cube commute? In other words: does this triangle: $$\xymatrix{
F \oplus F^* \ar[r]^f \ar[d]_h & \Lambda{\mathbb C}^5 \\
\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3 \ar[ru]_g \\
}$$ commute?

In fact they both do, and we can use our affirmative answer to the second question to settle the first. As we remarked in Section [\[sec:route\]](#sec:route){reference-type="ref" reference="sec:route"}, applying the map $g$ to the Pati--Salam binary code given in Table [\[tab:pscode2\]](#tab:pscode2){reference-type="ref" reference="tab:pscode2"}, we get the ${\rm SU}(5)$ binary code given in Table [\[tab:su5code\]](#tab:su5code){reference-type="ref" reference="tab:su5code"}. Thus, the linear maps $f$ and $gh$ agree on a basis, so this triangle commutes: $$\xymatrix{
F \oplus F^* \ar[r]^f \ar[d]_h & \Lambda{\mathbb C}^5 \\
\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3 \ar[ru]_g \\
}$$ This in turn implies that the bottom face of the cube commutes, from which we see that the two maps from ${G_{\mbox{\rm SM}}}$ to ${\rm U}(\Lambda{\mathbb C}^5)$ going around the bottom face are equal: $$\xymatrix{
{G_{\mbox{\rm SM}}}\ar[dr] &                                                    & \\
             & {\rm U}(F \oplus F^*) \ar[r]^-{{\rm U}(f)} \ar[d]_{{\rm U}(h)} & {\rm U}(\Lambda{\mathbb C}^5) \ar[d]^1 \\
             & {\rm U}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[r]^-{{\rm U}(g)}    & {\rm U}(\Lambda{\mathbb C}^5) \\
}$$

The work of Section [\[sec:su(5)\]](#sec:su(5)){reference-type="ref" reference="sec:su(5)"} through Section [\[sec:route\]](#sec:route){reference-type="ref" reference="sec:route"} showed that the vertical faces of the cube commute. We can thus conclude from diagrammatic reasoning that the two maps from ${G_{\mbox{\rm SM}}}$ to ${\rm U}(\Lambda{\mathbb C}^5)$ going around the top face are equal: $$\xymatrix{
{G_{\mbox{\rm SM}}}\ar[r]^\phi \ar[d]_\theta         & {\rm SU}(5) \ar[d]^\psi & \\
{\rm Spin}(4) \times {\rm Spin}(6) \ar[r]^-\eta  & {\rm Spin}(10) \ar[dr]  & \\
                                       &                    & {\rm U}(\Lambda{\mathbb C}^5) \\
}$$ Since the Dirac spinor representation is faithful, the map ${\rm Spin}(10) \to
{\rm U}(\Lambda{\mathbb C}^5)$ is injective. This means we can drop it from the above diagram, and the remaining square commutes. But this is exactly the top face of the cube. So, the proof is done. 3em $\sqcap$ -1em $\sqcup$ 2ex
