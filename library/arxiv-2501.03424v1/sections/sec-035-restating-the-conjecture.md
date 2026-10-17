---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-035-restating-the-conjecture
section_title: "Restating the conjecture"
section_number: null
pages: 18-20
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.928
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
The Kazhdan-Lusztig conjecture states that for a complex semisimple Lie algebra $\g$, and any $x,y$ in the Weyl group $W,$
$$[M_y : L_x] = h_{y,x}(1)$$
where $h_{y,x}(1)$ is the value of the Kazhdan-Lusztig polynomial $h_{y,x}(v)$ at $v = 1$. By Bernstein-Gelfand-Gelfand reciprocity\ref{app5}, the Kazhdan-Lusztig conjecture is equivalent to stating 
$$(\text{Pr}_x : M_y) = h_{y,x}(1).$$
Using the correspondence $[\mathcal{O}_0] \simeq \Z[W]$ in the Grothendieck group, this means that we equivalently have 
$$[\text{Pr}_x] = b_x|_{v=1},$$
where $b_x|_{v=1}$ is the specialization at $v = 1$ of the Kazhdan-Lusztig basis element $b_x \in \mathcal{H}.$ Recall finally that Soergel's conjecture is true if for every $x \in W,$
$$\chi(B_x) = b_x.$$
We now move to our final proposition.

 
\subsubsection{Proposition}\ref{ref2}
 \textit{Let $\g$ be a complex semisimple Lie algebra. Then Soergel's conjecture for the geometric representation of its Weyl group $W$ implies the Kazhdan-Lusztig conjecture for $\g.$}\\\\
 \textit{Proof:} We will begin by induction on Bruhat order. We have 
 $$\text{Pr}_{\text{id}} = M_{\text{id}},$$
 which implies that $[\text{Pr}_{\text{id}}] = \text{id} = b_{\text{id}}|_{v=1}.$ Let $x > \text{id}$ in Bruhat order. Choose $s \in S$ such that $xs < s,$ and take $x = ws,$ where $w < x.$ Then 
 $$\Theta_s\text{Pr}_w \simeq \text{Pr}_x \oplus \bigoplus_{z<x}\text{Pr}^{\oplus m_z}_z$$
 for multiplicities $m_z \ge 0.$ In the Grothendieck group, we obtain by induction 
 $$[\text{Pr}_x] = [\Theta_s\text{Pr}_w] - \sum_{z<x}m_z [\text{Pr}_z] = [\text{Pr}_w](1+s) - \sum_{z<x}m_z [\text{Pr}_z] $$
 $$= b_wb_s - \sum m_zb_z|_{v=1}.$$
 Applying $\mathbb{V}$ to $\Theta_s\text{Pr}_w,$ we get 
 $$\overline{B_w}B_s \simeq \overline{B_x} \oplus \bigoplus_{z<x}\overline{B_z}^{\oplus m_z}, $$
 and since Soergel modules decompose the same as Soergel bimodules, 
 $$B_wB_s \simeq B_x \oplus \bigoplus_{z<x}B^{\oplus m_z}_z.$$
 Taking characters and invoking Soergel's conjecture, we get 
 $$b_x = b_wb_s - \sum_{z<x}m_zb_z. $$ 
 Then by the equality 
 $$[\text{Pr}_w](1+s) - \sum_{z<x}m_z [\text{Pr}_z] =  b_wb_s - \sum m_zb_z|_{v=1}, $$ 
 we get $[\text{Pr}_x] = b_x|_{v=1},$ which is the equivalent form of the Kazhdan-Lusztig conjecture.  \Laughey

 
 




 











\newpage
\begin{center}
