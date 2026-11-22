---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-023-332-uniqueness
section_title: "Uniqueness"
section_number: 3.3.2
pages: 18-19
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.821
latex_coverage_ratio: 0.914
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
Suppose that we have two self-dual elements $c=h_x+h$ and $c'=h_x+h'$, with $h,h' \in \cH. $ Then one has that $h-h'$ is self-dual as $h-h'=c-c'.$

We just need to prove 
\begin{claim}
If $h\in \sum_yv\ZZ[v] h_y$ and $h$ is self-dual, then $h=0$. 
\end{claim}
Let us call $b_x$ the element that we constructed  in Section \ref{1}. It is easy to see, by equation (\ref{KL}) that $$h_x\in b_x+\sum_{y<x}\ZZ[v,v^{-1}]b_y,$$
thus \begin{equation}\label{d}d(h_x)\in b_x+\sum_{y<x}\ZZ[v,v^{-1}]b_y \subseteq  h_x+\sum_{y<x}\ZZ[v,v^{-1}]h_y.\end{equation}


Let us write $h=\sum_y p_yh_y$, with $p_y\in v\ZZ[v]$ and let $z$ be a maximal element (in the Bruhat order) such that $p_z\neq 0.$ In other words, $h=p_zh_z +\sum_{y\ngeq z} p_yh_y.$ By equation (\ref{d}) we obtain 
$$d(h)\in d(p_z)h_z +\sum_{y\ngeq z}\ZZ[v,v^{-1}] h_y.$$ As $h$ is self-dual, this implies that $d(p_z)=p_z,$ contradicting the fact that \newline $p_z\in v\ZZ[v]$ and thus proving the claim.  









\subsubsection{ $\{b_x\}_{x\in W}$ is a basis}

The set $\{b_x\}_{x\in W}$ is a $\Z[v,v^{-1}]-$basis given that the set $\{h_x\}_{x\in W}$ is a basis and by using the triangularity property in Remark \ref{rem1}.
\end{proof}
