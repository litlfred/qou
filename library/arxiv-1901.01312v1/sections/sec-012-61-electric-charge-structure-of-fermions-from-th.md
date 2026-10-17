---
doc_id: arxiv-1901.01312v1
doc_title: "Braided fermions from Hurwitz algebras"
section_id: sec-012-61-electric-charge-structure-of-fermions-from-th
section_title: "Electric charge structure of fermions from the $\mathbb{C}$ representation of $B_2$"
section_number: 6.1
pages: 7-8
source_pdf: 1901.01312v1.pdf
source_sha256: a480da38283622d6
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 1.0
---
One speculative idea is that the lack of faithfulness of the representations of the braid groups $B_2$ and $B_3^c$ using $\mathbb{C}$ and $\mathbb{H}$ respectively naturally places a restriction on the number of distinct braided physical states that can be represented. The Helon model has no mechanism in place to restrict the number of allowable physical states. One could add more twisting to the ribbons and increase the complexity of braiding without limit, to get an infinite number of distinct states. Indeed, the model has been extended to a infinite number of generations [@Bilson-Thompson2008]. However, because the $\mathbb{C}$ and $\mathbb{H}$ representations of $B_2$ and $B_3^c$ representations are not faithful, many distinct braids are represented by the same (hyper)complex number. Each (hyper)complex number therefore represents an equivalence class of braids, each to be identified with a physical state. The finite set of equivalence classes then places a limit on the number of admissible physical states.

The twisted ribbons (helons) of the Helon model may be represented as braids in $B_2$ as $$\begin{aligned}
H_+=\sigma_1^2,\qquad H_-=\sigma_1^{-2},\qquad H_0=I,
\end{aligned}$$ where $I$ denotes the identity unbraid. Because the braid word for each twisted ribbon is even, we therefore restrict ourselves to braids composed of an even number of braid generators[^1].

The $\mathbb{C}$ representation of $B_2$ is not faithful, dividing this braid group into eight equivalence classes, each represented by a complex number. It is readily checked that any even product of $B_2$ braid generators defined in ([\[complexgenerators\]](#complexgenerators){reference-type="ref" reference="complexgenerators"}) is equal to one of four complex numbers $\pm 1, \pm i$, each defining an equivalence class of braids.

The shortest possible braid in each class can be used as a representative for the equivalence class $$\begin{aligned}
\rightarrow 1,\qquad [\sigma_1^2]\rightarrow i,\qquad [\sigma_1^4]=[\sigma_1^{-4}]\rightarrow -1,\qquad [\sigma_1^{-2}](=[\sigma_1^{6}])\rightarrow -i.
\end{aligned}$$ The first, second, and fourth equivalence class representatives correspond to the helons $H_0$, $H_+$, and $H_-$ respectively, or equivalently, electric charges of $0$, $e/3$, and $-e/3$. Because $\sigma_1^4$ and $\sigma_1^{-4}$ both belong to the same equivalence class, it is impossible to represent both a ribbon with charge $2e/3$ and a ribbon with charge $-2e/3$ in a consistent manner[^2]. In other words, electric charges (for a single ribbon) outside the range $\left\lbrace 0, e/3,-e/3\right\rbrace$ are naturally excluded as a result of the complex representation of $B_2$ not being faithful.

## Equivalence classes of braids from $\mathbb{H}$

The braid generators in ([\[quaterniongenerators\]](#quaterniongenerators){reference-type="ref" reference="quaterniongenerators"}) and their products correspond to unit quaternions, which we write as $a+bI+cJ+dK$ with $a^2+b^2+c^2+d^2=1$. It is not difficult to show that any even product of braid generators is of the form $$\begin{aligned}
\label{Hequivalence}
b_n\mapsto a+bI+cJ+dK,\quad \textrm{where} \quad a,b,c,d\in \left\lbrace 0, \pm \frac{1}{2}, \pm 1 \right\rbrace. 
\end{aligned}$$ This gives $2\times 4+2^4=24$ possibilities, but includes braids that lead to charge mixing, such as $\sigma_1^2,\sigma_2^2$, and $\sigma_3^2$. Written in pure twist form, $\sigma_1^2=[1,1,-1]$, $\sigma_2^2=[1,-1,1]$, and $\sigma_3^2=[-1,1,1]$. Since $$\begin{aligned}
\sigma_1^2 \mapsto I,\qquad \sigma_2^2 \mapsto J,\qquad \sigma_3^2\mapsto K,
\end{aligned}$$ these quaternions must be ruled out from representing physical states. This leaves 18 equivalence classes, 16 with four terms and 2 with one term. It is not yet clear if it if possible to, and if so how, to identify 16 of these 18 equivalence classes with 16 distinct fermions, nor how to interpret the remaining two equivalence classes in this case.

[^1]: One may ask, why not identify a $\pm\pi$ twist with a charge of $\pm e/3$ instead? In that case the braid words would be odd instead. The problem is that when combining three such ribbons together, all the quarks would correspond to unorientable braids.

[^2]: It is assumed here that every particle has a corresponding antiparticle. If one constructs a particle using an electric charge of $2e/3$ on one or more ribbons, then the corresponding antiparticle cannot be constructed because $\sigma_1^{-4}$ lies in the same equivalence class as $\sigma_1^4$.
