---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-048-92-equivariant-structure-for-the-generators
section_title: "Equivariant structure for the generators"
section_number: 9.2
pages: 50-51
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.983
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In this subsection we discuss the equivariant structure of the generators of the braid group. We also introduce the matrix factorization $\calC_\bullet$ that corresponds to the blob or fat point in the MOY calculus [@MOY]. We use this connection later to relate our homology theory of links to the HOMFLY-PT polynomial.

We use the following parameterization of the variety $\calX^\circ_2(G)=\frg\times G\times \frn^2$: $$\begin{aligned}
\xX &= \xmtr{ \SymbolPrint{\xz} & \SymbolPrint{\xo} \\ \SymbolPrint{\xmo} & -\xz },&
\xYi & = \xmtr{0 & \SymbolPrint{\yi} \\ 0 & 0 }\quad i=1,2,&
\xg &=\xmtr{ \SymbolPrint{\exaoo} & \SymbolPrint{\exaot} \\ \SymbolPrint{\exato} & \SymbolPrint{\exatt} }.
\end{aligned}$$ The tori $T^{(1)}$, $T^{(2)}$ of the Borel groups in the product $B^2$ are $\CC^*$ and the weights of their action are in the table: $$\begin{tabu}{| c ||r |r |r |r |r | r | r | r | r | r|}
\hline
\text{variable} &
\exaoo &\exaot & \exato &\exatt & \xmo & \xz & \xo &\txz & \yo & \yt
\\
\hline
T^{(1)} &
1 & 1 & -1 & -1 & -2 & 0 & 2 & 1 & 2 & 0
\\
\hline
T^{(2)} &
-1 & 1 & -1 & 1 & 0 & 0 & 0 & -1 & 0 & 2
\\
\hline
\end{tabu}.$$

The generator of the nilpotent part of $\Lie(B)$, $\frn=\langle \delta\rangle$ acts on the coordinates by $$\begin{aligned}
\dlto\exaoo &= \exato,&\dlto\exaot & = \exatt,&\dlto\xz & = \xmo,&\dlto\xo & = -2\xz,



\\
\dltt\exaot & = -\exaoo,&\dltt\exatt&=-\exato, 
\end{aligned}$$

In the table above and in the proofs in this section we use following functions of the coordinates: $$\begin{aligned}
\SymbolPrint{\txz} & = 2\xz \exaoo + \xo\exato, & \SymbolPrint{\ttxz} & = 2 \xz \exaot + \xo \exatt,
\end{aligned}$$ so that $$\begin{aligned}
\dlto\txz & = 2\xmo\exaoo, & \dlto \ttxz &= 2\xmo \exaot, & \dltt\ttxz & = -\txz.
\end{aligned}$$

The matrix factorization was discussed previously but in this section we need an explicit description of this matrix factorization as a strongly $B^2$-equivariant matrix factorization. We use Koszul matrix factorization conventions of the subsection [\[ssec: str eq Kosz\]](#ssec: str eq Kosz){reference-type="ref" reference="ssec: str eq Kosz"}, so the matrix factorization of the identity braid has the form $$\crXpr =
\begin{bmatrix}
\xmo & \yo - \yt\exaoo^2 & \theta_1
\\
\yt\txz

& \exato & \theta_2
\end{bmatrix},\quad
\dlto\theta_1 = -2\yt\exaoo\theta_2,$$ with $\deg_{\Tsc}\theta_1=(2,1)$ and $\deg_{\Tsc}\theta_2=(0,-1)$. The blob matrix factorization has the form $$\crXbl=
\begin{bmatrix}
\xmo & \yo - \yt\exaoo^2 & \theta_1
\\
\exato \txz

& \yt & \theta_2'
\end{bmatrix},\quad
\dlto\theta_1 = -2\exato\exaoo\theta_2'$$ or equivalently $$\crXbl=\begin{bmatrix}
\xmo & \yo & \theta'_1
\\
-\exaoo^2\xmo+
\exato \txz

& \yt & \theta_2'
\end{bmatrix},\quad \theta'_1=\theta_1 +\exatt^2\theta_2',\quad
\dlto\theta'_1 = 0$$

The matrix factorization of the positive intersection is $$\crXp= (  \mathsf{q}  \mathsf{t})^{-1}
\begin{bmatrix}
\xmo & \yo - \yt\exaoo^2 & \theta_1
\\

\txz & \exato\yt & \theta_2
\end{bmatrix}

,\quad
\dlto\theta_1 = -2\exaoo\theta_2,$$ while $$\crXn = \,\crXp\brwsh{-1}{-1}.$$
