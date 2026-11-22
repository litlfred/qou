---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-013-41-some-properties-of-the-kostant-functor-κℏ
section_title: "Some properties of the Kostant functor κℏ"
section_number: 4.1
pages: 14-15
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.963
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
The following properties of the Kostant functor will play an important role in the proof of the main results.

::: lem
[]{#propKons label="propKons"} a) The functors $\kappa,\, {\kappa_\hbar}$ are exact.

b\) The functors $\kappa|_{Coh_{fr}^{{\check{G}}\times {{\mathbb G}_m}}(\check{\mathfrak g}{}^*)}$, ${\kappa_\hbar}|_{\HC_\hbar^{fr}}$ are full embeddings.
:::

*Proof* is essentially due to B. Kostant, cf. [@K1].

a\) For the exactness of $\kappa$, note that the functor of restriction $\CF\mapsto\CF|_\Upsilon$ is exact on $Coh^{\check{G}}(\check{\mathfrak g}{}^*)$, and then $\CF|_\Upsilon$ is an $\check{N}{}_-$-equivariant coherent sheaf on $\Upsilon$. Recall that $\check{N}{}_-$ acts on $\Upsilon$ freely, and $\Upsilon/\check{N}{}_-\simeq\Sigma$. Hence the functor of invariants $\CG\mapsto\CG^{\check{N}{}_-}$ is exact on $Coh^{\check{N}{}_-}(\Upsilon)$. The exactness of $\kappa$ follows.

For the exactness of $\kappa_\hbar$, we will prove that both the functors of $-\psi$-coinvariants, and $\check{N}{}_-$-invariants are exact, and hence $\kappa_\hbar$ is exact as their composition. It is enough to check it on the positively graded $\hbar$-Harish-Chandra bimodules. Then it is enough to check the exactness on the subcategory of $\hbar$-Harish-Chandra bimodules with grading degrees between 0 and $n$ for a fixed $n\gg0$. Thus it suffices to check the exactness on the subcategory of $\hbar$-Harish-Chandra bimodules with nilpotent action of $\hbar$, and then it suffices to consider the subcategory of $\hbar$-Harish-Chandra bimodules with the *trivial* action of $\hbar$. However, an $\hbar$-Harish-Chandra bimodule $M$ with the trivial action of $\hbar$ is nothing else than a ${\check{G}}$-equivariant coherent sheaf on $\check{\mathfrak g}{}^*$, and $M\overset{\rm L}{\otimes}_{U_\hbar(\check{\mathfrak n}{}_-)_2}(-\psi)=M|_\Upsilon$. In particular, the functor of $-\psi$-coinvariants is exact according to the previous paragraph. For the same reason, $M\mapsto(M\overset{\rm L}{\otimes}_{U_\hbar(\check{\mathfrak n}{}_-)_2}(-\psi))^{\check{N}{}_-}=(M|_\Upsilon)^{\check{N}{}_-}$ is exact. This completes the proof of a).

b\) $\kappa|_{Coh_{fr}^{{\check{G}}\times {{\mathbb G}_m}}(\check{\mathfrak g}{}^*)}$ is fully faithful since the complement to $(\check{\mathfrak g}{}^*)^{reg}$ in $\check{\mathfrak g}{}^*$ has codimension 2, and the centralizer of a generic regular element is connected.

To prove that ${\kappa_\hbar}|_{\HC_\hbar^{fr}}$ is fully faithful, we consider free $\hbar$-Harish-Chandra bimodules $M_1=U_\hbar\otimes V_1,\
M_2=U_\hbar\otimes V_2$, and the following commutative diagram:

$$\begin{CD}
\Hom(M_1,M_2)@>\epsilon>>\Hom({\kappa_\hbar}M_1,{\kappa_\hbar}M_2)@>\delta>>
\Hom({\kappa_\hbar}M_1,{\kappa_\hbar}M_2)/\hbar\\
@VV\beta V @. @VV\gamma V\\
\Hom(M_1/\hbar,M_2/\hbar)@>\alpha>>\Hom(\kappa(M_1/\hbar),\kappa(M_2/\hbar))
@>\sim>>\Hom(({\kappa_\hbar}M_1)/\hbar,({\kappa_\hbar}M_2)/\hbar)
\end{CD}$$

We have just proved that $\alpha$ is an isomorphism. Moreover, $\beta$ is surjective since $\Hom(U_\hbar\otimes V_1,U_\hbar\otimes V_2)=
\Hom_{\check{G}}(V_1\otimes V_2^*,U_\hbar)$, and all the ${\check{G}}$-modules in question are semisimple. It follows that $\gamma$ is surjective. On the other hand, $\gamma$ is injective since ${\kappa_\hbar}M_1,\ {\kappa_\hbar}
M_2$ are free over $\mathsf k[\hbar]$. Now that $\gamma$ is proved to be an isomorphism, the composition $\delta\circ\epsilon$ must be surjective. Hence $\epsilon$ is surjective by Nakayama Lemma. It remains to prove that $\epsilon$ is injective. Since ${\kappa_\hbar}$ is exact, it is enough to prove that ${\kappa_\hbar}M\ne0$ for a nonzero subobject $M$ of a free $\hbar$-Harish-Chandra bimodule $M_2$. We consider a nonzero subobject $M/\hbar\subset M_2/\hbar$ of a free $\CO(\check{\mathfrak g}{}^*)$-module $M_2/\hbar$. It suffices to prove that $\kappa M\ne0$. However, the support of any nonzero section of a free $\CO(\check{\mathfrak g}{}^*)$-module is the whole of $\check{\mathfrak g}{}^*$, hence its restriction to $\Upsilon$ is nonzero.

The lemma is proved. $\Box$
