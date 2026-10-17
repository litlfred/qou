---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-012-definition
section_title: "Definition"
section_number: null
pages: 9-10
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.974
---
The \textit{character} $\chi$ of a Soergel bimodule $B$ is defined as the element 
$$\chi(B) = \sum_{x \in W}v^{l(x)}h_x(B)\delta_x$$
of $\mathcal{H}.$ We have $h_{id}(B_s) = v^{+1}$ and $h_s(B_s) = v^{-1},$ and thus $\chi(B_s) = v\delta_{id} + v - v^{-1}\delta_s = v + \delta_s.$ Thus, wonderfully, $\chi(B_s) = b_s $ for every $s \in S.$ It follows that $\chi(B \oplus B') = \chi(B) + \chi(B')$ and $\chi(B(1)) = v\chi(B).$ Since $v[B] = [B(1)]$ in the Grothendieck group, $\chi$ induces a $\Z$-linear, but moreover $\Z[v, v^{-1}]$-linear map 
$$\chi: [\mathbb{S}\text{Bim}]_\oplus \rightarrow \mathcal{H}.$$
We can now introduce these very important results : 


\subsubsection{Soergel's Categorification theorem}
\begin{enumerate}
    \item \textit{There exists a $\Z[v^{\pm 1}]$-algebra homomorphism}
    $$\phi: \mathcal{H} \rightarrow [\mathbb{S}\text{Bim}]_\oplus, \text{       }b_s \mapsto [B_s]$$
    \textit{for each $s \in S$.}

    \item \textit{$W$ is in bijection with the set of indecomposable objects in $\mathbb{S}\text{Bim}$ mod shift and isomorphism. Formally, }
    $$W \longleftrightarrow \{\text{indecomposable objects} \in \mathbb{S}\text{Bim}\}/\simeq, (k), \text{     } w \mapsto B_w, $$
    \textit{where $B_w$ are direct summands in the Bott-Samelson bimodules $BS(\underline{w})$}.

    \item \textit{$\chi$ descends to a $\Z[v^{\pm 1}]$-module homomorphism }
    $$\chi: [\mathbb{S}\text{Bim}]_\oplus \rightarrow \mathcal{H}$$
    \textit{which is inverse to $\phi$. Thus $\phi$ and $\chi$ are isomorphisms, and we have $[\mathbb{S}\text{Bim}]_\oplus \simeq \mathcal{H}.$} 
\end{enumerate}


\subsubsection{Soergel's Hom formula}

\textit{For any Soergel bimodules $B, B'$, the graded $R$-bimodule hom space $\Hom^\bullet_{\mathbb{S}\text{Bim}}(B, B')$ is free as a graded left (resp., right) $R$-module. Moreover, }
$$\text{gr(rank)}\Hom^\bullet_{\mathbb{S}\text{Bim}}(B, B') = (\chi(B), \chi(B')),$$
\textit{where (  ,  ) is the standard form on $\mathcal{H}.$} 


\subsubsection{}
Soergel's Hom formula motivates what we call \textit{Soergel's conjecture,} which was proved for arbitrary Coxeter systems (Soergel proved for Weyl groups) by [Elias / Williamson]. We state it here: 


\subsubsection{Soergel's conjecture}
\textit{For every $x \in W$, $\chi(B_x) = b_x.$ Equivalently, the Kazhdan-Lusztig polynomial $h_{x,y} = h_x(B_y)$.}
