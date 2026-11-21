---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-017-33-shift-and-evolution-operators
section_title: "Shift and evolution operators"
section_number: 3.3
pages: 9-10
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.973
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
[]{#subsec:shevol label="subsec:shevol"} If we guessed the equation right, there must exist the "evolution operator", that is an element $K$ such that $$\chi_{j,k+1}=K^{-1}\chi_{j,k-1}K.$$ Needless to say, these relations will hold everywhere if and only if they do so for $k$ equal $0$ and $-1$ where they become $$\begin{aligned}
 \chi_{2n-1}K\chi_{2n-1}
  K^{-1}&=\frac{q^2\chi_{2n-2}\chi_{2n}}
  {(1+q\chi_{2n-2})(1+q\chi_{2n})}              \\
  K^{-1}\chi_{2n}K\chi_{2n} &=\frac{q^2\chi_{2n-1}\chi_{2n+1}}
  {(1+q\chi_{2n-1})(1+q\chi_{2n+1})}. 
\end{aligned}$$ Following [@fadVol93; @fadVol97] we shall produce that element, with explicitly singled out d'Alembert part $K_\infty^{}$ good for $$\chi_{2n-1}K_\infty^{}\chi_{2n-1}
K_\infty^{-1}=q^2\chi_{2n-2}\chi_{2n}\qquad
K_\infty^{-1}\chi_{2n}K_\infty^{}\chi_{2n} =q^2\chi_{2n-1}\chi_{2n+1}
,$$ and complete with the "shift operator" $J$ moving the $\chi$'s in the spatial direction $$\chi_{j+1,k}=J^{-1}\chi_{j-1,k}J  .$$ Here follow explicit formulas for these shift and evolution operators $$K_\infty^{}=VU\qquad\qquad K=E_2K_\infty^{}E_1
\qquad\qquad J=VU^{-1}$$ where $$\begin{aligned}
 E_1&=\prod_{n=1}^N
  \epsilon(\chi_{2n-1})\qquad\qquad
  E_2=\prod_{n=1}^N\epsilon(\chi_{2n})                \\
  U&=\theta(q\chi_1^{-1}\chi_2^{}) \theta(q\chi_3^{-1}\chi_4^{})\ldots
  \theta(q\chi_{2N-3}^{-1}\chi_{2N-2}^{})       \\
  V&=\theta(q\chi_{2N-1}^{}\chi_{2N-2}^{-1})
  \theta(q\chi_{2N-3}^{}\chi_{2N-4}^{-1})\ldots
  \theta(q\chi_3^{}\chi_2^{-1}) .  
\end{aligned}$$ Of course, $U$ and $V$ have everything to do with braids but we will not go into that. The two special functions involved $$\begin{aligned}
    \epsilon(z)&=\prod_{p=0}^\infty(1+q^{2p+1}z)
    =(-qz;q^2)_\infty                             \\
    \theta(z)&=\epsilon(z)\,\epsilon(z^{-1})=\text{const}
    \cdot\sum_{p=-\infty}^\infty q^{p^2}z^p
                       \end{aligned}$$ are quite special indeed but all we want to know about them, for now at least, are the beautiful functional equations $$\frac{\epsilon(qz)}{\epsilon(q^{-1}z)}=\frac1{1+z} \qquad\qquad  
\frac{\theta(qz)} {\theta(q^{-1}z)}=\frac1{z}\;$$ fulfiled by the former, and the ensuing equation on the latter which has already been used, albeit implicitly, in subsection 2.4. This time those functional equations and condition ([\[cc\]](#cc){reference-type="ref" reference="cc"}) gradually translate into relations

::: xxalignat
2 E_1\^-1\_2n-1\^E_1 =\_2n-1\^&&&E_1\^-1\_2n\^E_1 =\_2n\^ (1+q\_2n-1\^)(1+q\_2n+1\^)\
E_2\^-1\_2n\^E_2 =\_2n\^&&&E_2\^-1\_2n-1\^E_2 =((1+q\_2n-2\^) (1+q\_2n\^))\^-1\_2n-1\^\
U\^-1\_2n\^U=\_2n-1\^&&& U\^-1\_2n+1\^U=q\^2\_2n-1\^ \_2n+1\^\_2n\^-1\
V\^-1\_2n\^V=\_2n+1\^&&& V\^-1\_2n-1\^V=q\^2\_2n-1\^ \_2n+1\^\_2n\^-1
:::

which combined make $J$ and $K$ satisfy what they have to. We omit the calculation but a remark is in order.

## Odd $N$ or no condition ([\[cc\]](#cc){reference-type="ref" reference="cc"})

In these cases it all fails, and subsection [\[subsecProof\]](#subsecProof){reference-type="ref" reference="subsecProof"} gives an idea why. In fact, they are better served by those cross-ratio-splitting variables $h$ and Hirota's lattice Liouville equation which we were so quick to discard. We are planning to return to this issue elsewhere.
