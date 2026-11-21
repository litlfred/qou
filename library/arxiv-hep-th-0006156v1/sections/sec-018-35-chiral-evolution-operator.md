---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-018-35-chiral-evolution-operator
section_title: "Chiral evolution operator"
section_number: 3.5
pages: 10-11
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.937
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
We define it as $$Q=UE_1   \;   ,$$ and it indeed moves the $\chi$'s in the right direction $$\chi_{j,k+1}=Q^{-1}\chi_{j+1,k}Q$$ and equals $\sqrt{J^{-1}K}$, in the sense that $Q^2=J^{-1}K$. So, the total momentum $P$, Hamiltonian $H$ and the chiral Hamiltonian $\frac12(H-P)$ of the original equation have finally become shift-evolution-operators $J$, $K$ and $Q$ of the quantum lattice equation, but we have yet to find out in what sense, if at all, this $Q$ coincides with that hypothetical quantum lattice group-like counterpart of $L_0$ which we called $Q$ in section [\[sec:lva\]](#sec:lva){reference-type="ref" reference="sec:lva"}. The answer does not come easy but in the end few carefully placed $q$'s do it again, and so does the magic function $\epsilon$ introduced in subsection [\[subsec:shevol\]](#subsec:shevol){reference-type="ref" reference="subsec:shevol"}. It turns out that $$\label{eq:qdd}
Q=d_1d_2\ldots d_{N-1}      ,$$ where $Q$ is $UE_1$ and the $d$'s are $$d_n=\epsilon\big(q^{-1}(1+q\chi_{2n}^{}+\chi_{2n}^{}
\chi_{2n-1}^{-1})(1+q\chi_{2n+1}^{}
+\chi_{2n+2}^{-1}\chi_{2n+1}^{})-q^{-1}\big).$$ As the notation suggests, these also satisfy relations ([\[cr\]](#cr){reference-type="ref" reference="cr"}$''$) and ([\[mb\]](#mb){reference-type="ref" reference="mb"}$''$). It is instructive now to see, that argument of function $\epsilon$ in this formula is a natural quantisation of expression ([\[lse\]](#lse){reference-type="ref" reference="lse"}).

## Proof of eqn ([\[eq:qdd\]](#eq:qdd){reference-type="ref" reference="eq:qdd"})

First, we recall the two identities satisfied by $\epsilon$-function: $$\label{eq:idep}
\epsilon(u)\epsilon(v)=\epsilon(u+v),\quad \epsilon(v)\epsilon(u)=\epsilon(v+u+qvu),\quad uv=q^2vu .$$ Next, we have the identity $$\epsilon(\chi_{1}(1+q\chi_{2}^{-1}))Q=Q
\epsilon(\chi_{2N}^{-1}(1+q\chi_{2N-1}^{-1})^{-1})$$ which is a consequence of the relations in subsection [\[subsec:shevol\]](#subsec:shevol){reference-type="ref" reference="subsec:shevol"} satisfied by $U$ and $E_1$ operators. It is also easily checked that for any $j$ $$\theta(q\chi_{2j-1}^{-1}\chi_{2j})\epsilon(\chi_{2j-1})=
\epsilon(\chi_{2j-1}(1+q\chi_{2j}^{-1})) \epsilon((1+q\chi_{2j-1}^{-1})\chi_{2j}).$$ Now, using these relations, we have $$\begin{gathered}
  Q=(\epsilon(\chi_{1}(1+q\chi_{2}^{-1})))^{-1}UE_1\epsilon(\chi_{2N}^{-1}(1+q\chi_{2N-1}^{-1})^{-1})\\
  =(\epsilon(\chi_{1}(1+q\chi_{2}^{-1})))^{-1}\left(\prod_{1\le j<N}
    \theta(q\chi_{2j-1}^{-1}\chi_{2j})\epsilon(\chi_{2j-1})\right)\\
  \times\epsilon(\chi_{2N-1}) \epsilon(\chi_{2N}^{-1}(1+q\chi_{2N-1}^{-1})^{-1})\\
  =(\epsilon(\chi_{1}(1+q\chi_{2}^{-1})))^{-1}\left(\prod_{1\le j<N}
    \epsilon(\chi_{2j-1}(1+q\chi_{2j}^{-1}))
    \epsilon((1+q\chi_{2j-1}^{-1})\chi_{2j})\right)\\
  \times\epsilon(q\chi_{2N-1}\chi_{2N}^{-1})\epsilon(\chi_{2N-1}) \\
  =\prod_{1\le j<N} \epsilon((1+q\chi_{2j-1}^{-1})\chi_{2j})
  \epsilon(\chi_{2j+1}(1+q\chi_{2j+2}^{-1}))=\prod_{1\le j<N}d_j,
\end{gathered}$$ thus obtaining eqn ([\[eq:qdd\]](#eq:qdd){reference-type="ref" reference="eq:qdd"}).

The proof of relations ([\[mb\]](#mb){reference-type="ref" reference="mb"}$''$) is done in [@volkov97c] and is also based on identities ([\[eq:idep\]](#eq:idep){reference-type="ref" reference="eq:idep"}).
