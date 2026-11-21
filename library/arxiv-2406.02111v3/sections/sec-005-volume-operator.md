---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-005-volume-operator
section_title: "Volume operator"
section_number: null
pages: 4-5
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "Categorical Quantum Volume Operator — 17 sections: Categorical Quantum Volume Operato; Introduction; The Volume Operator in Loop Quantu"
---
\label{subsec:volumeoperator}
The action of the volume operator is given by~\cite{Rovelli2014}
\begin{equation}
	\hat{V} \ket{\iota_\kappa} = \frac{\sqrt{2}}{3} \left( 8 \pi G \hbar \gamma \right)^{3/2} \sqrt{\vert \hat{Q} \vert} \ket{\iota_\kappa} ,
	\label{eq:def:vol_op}
\end{equation}
where $\gamma$ denotes the Barbero--Immirzi parameter, and $G$ and $\hbar$ the gravitational and reduced Planck constant, respectively.\footnote{While the volume operator is technically $\hat{V} \propto \big(\hat{Q}^\dagger \hat{Q}\big)^{\nicefrac{1}{4}}$, where the dagger symbol $^\dagger$ indicates the adjoint, we take the liberty to refer to $\hat{Q}$ itself as the volume operator as well when there is no need (in terms of their physical relevance) to account for the various prefactors that appear in Eq. (\ref{eq:def:vol_op}).} The operator $\hat{Q}$ quantifies the volume of a single tetrahedron and is defined by
\begin{equation}
		\hat{Q} \defeq \vec{L}_1 \cdot \left( \vec{L}_2 \times \vec{L}_3 \right).
		\label{eq:def_volume_operator}
\end{equation}
The matrix elements $\tensor{Q}{_\kappa^{\kappa'}} = \braket{\iota_\kappa | \vec{L}_1 \cdot ( \vec{L}_2 \times \vec{L}_3 ) | \iota_{\kappa'}}$ of this operator are computed in Ref.~\cite{Rovelli2014}\@. We revisit the relevant parts of the derivation here, following Ref.~\cite{Rovelli2014} closely. First, we recall that due to the closure relation Eq.~\eqref{eq:closure_constraint}, any triple from $\{\vec{L}_1,\vec{L}_2,\vec{L}_3,\vec{L}_4\}$ can be used to derive $\hat{Q}$, and thus we can choose $\{\vec{L}_1,\vec{L}_2,\vec{L}_3\}$ [as in Eq.~\eqref{eq:def_volume_operator}] without loss of generality. Next, we define $L_{jk} \equiv L_j + L_k$ and compute
\begin{align}
	& \frac{1}{2}\left[(\vec{L}_1+\vec{L}_2)^2, \vec{L}_1\cdot\vec{L}_3\right] = \frac{1}{2}\left[ L_1^2 +L_2^2 + 2\vec{L}_1\cdot \vec{L}_2,\vec{L}_1\cdot \vec{L}_3\right] \nonumber \\
	& \qquad = \left[ \vec{L}_1\cdot \vec{L}_2, \vec{L}_1\cdot\vec{L}_3\right] = \sum_{j,k=1}^3 \left[ L_{1j} L_{2j}, L_{1k} L_{3k}\right] \nonumber \\
	& \qquad = \sum_{j,k,\ell=1}^3 \rmi \epsilon_{jk\ell} L_{1\ell} L_{2j} L_{3k} = \rmi \vec{L}_1 \cdot (\vec{L}_2\times\vec{L}_3), 
\end{align}
where $\epsilon_{jk\ell}$ denotes the Levi--Civita symbol. Therefore,
\begin{align}
	\begin{aligned}
		\tensor{Q}{_\kappa^{\kappa'}}
		=& -\frac{\rmi}{2}\bra{\iota_\kappa} [(\vec{L}_1+\vec{L}_2)^2, 	\vec{L}_1\cdot\vec{L}_3]\ket{\iota_{\kappa'}}\\
		=& -\frac{\rmi}{2} \big(\bra{\iota_\kappa} L_{12}^2(\vec{L}_1\cdot \vec{L}_3)\ket{\iota_{\kappa'}} \\
		&\qquad- \bra{\iota_\kappa} (\vec{L}_1\cdot\vec{L}_3)L_{12}^2\ket{\iota_{\kappa'}}\big)\\
		=&-\frac{\rmi}{2} (\alpha_\kappa - \alpha_{\kappa'}) \bra{\iota_\kappa} \vec{L}_1 \cdot \vec{L}_3 	\ket{\iota_{\kappa'}},
	\end{aligned}
\end{align}
where the last step follows from the Casimir property of $L_{12}^2$, that is
\begin{equation*}
	L_{12}^2\;
	\begin{tikzpicture}[baseline=(current bounding box.center)]
		\draw (0,-1) to node [left,midway] {$\kappa$} (0,0);
		\draw (0,0) to node [right,midway] {$j_2$} (0.75,0.75);
		\draw (0,0) to node [left,midway] {$j_1$} (-0.75,0.75);
	\end{tikzpicture}
	\;= \alpha_\kappa\;
	\begin{tikzpicture}[baseline=(current bounding box.center)]
		\draw (0,-1) to node [left,midway] {$\kappa$} (0,0);
		\draw (0,0) to node [right,midway] {$j_2$} (0.75,0.75);
		\draw (0,0) to node [left,midway] {$j_1$} (-0.75,0.75);
	\end{tikzpicture}\;.
\end{equation*}
For $\SU(2)$, we have $\alpha_\kappa = \kappa(\kappa+1)$. However, since one of our aims is to generalize this derivation, we do not make use of this specific relation here and proceed by referring to $\alpha_\kappa$ as the general eigenvalue of the quadratic Casimir operator instead. Using $(\vec{L}_1+\vec{L}_3)^2 = L_{13}^2 = L_1^2 + L_3^2 + 2 \vec{L}_1 \cdot \vec{L}_3$, we can compute
\begin{align}
	\tensor{Q}{_\kappa^{\kappa'}}
	&= - \frac{\rmi}{4} (\alpha_\kappa - \alpha_{\kappa'}) \bra{\iota_\kappa} L_{13}^2 - L_1^2 - L_3^2 \ket{\iota_{\kappa'}}\\
	&= - \frac{\rmi}{4} (\alpha_\kappa - \alpha_{\kappa'}) \big(\bra{\iota_\kappa} L_{13}^2 \ket{\iota_{\kappa'}} - (\alpha_{j_1} + \alpha_{j_3})\delta_{\kappa,\kappa'}\big), \nonumber
\end{align}
where we have made use of the fact that $L_1^2$ and $L_3^2$ are quadratic Casimir operators with eigenvalues $\alpha_{j_1},\alpha_{j_3}$, respectively. Note that the second term in the parentheses is zero as $(\alpha_\kappa - \alpha_{\kappa'})\delta_{\kappa,\kappa'}=0$. Therefore, we obtain
\begin{equation}
	\tensor{Q}{_\kappa^{\kappa'}} = - \frac{\rmi}{4} (\alpha_\kappa - \alpha_{\kappa'}) \bra{\iota_\kappa} L_{13}^2 \ket{\iota_{\kappa'}}
	\label{eq:volume_derivation_starting_point}
\end{equation}
as a final result. In Ref.~\cite{Rovelli2014}, the term $\bra{\iota_\kappa} L_{13}^2 \ket{\iota_{\kappa'}}$ is computed diagrammatically by inserting a resolution of the identity in terms of trivalent intertwiners, represented by a diagram of the form
\begin{equation}
	\begin{tikzpicture}[baseline=(current bounding box.center)]
		\draw[dashed] (0,0) arc (-40:40:1);
		\draw[rotate=180] (0,0) arc (40:-40:1);
		\draw (2,0) arc (-40:40:1);
		\draw[rotate=180] (-2,0) arc (40:-40:1);
		\draw (2,0) -- (1,-0.5);
		\draw (1,-0.5) -- (0,0);
		\draw (2,1.287) -- (1,1.8);
		\draw (1,1.8) -- (0,1.287);
		\node (kb) at (1,-0.8) {$\kappa'$};
		\node (k) at (1,2.1) {$\kappa$};
		\node (j1) at (-0.5,0.65) {$j_1$};
		\node (j4) at (2.5,0.65) {$j_4$};
		\node[draw,rectangle] (L13) at (1,0.65) {$L_{13}^2$};
		\draw (-0.225,0.65) -- (L13);
		\draw (1.775,0.65) -- (L13);
		\node (j3) at (1.6,1.15) {$j_3$};
		\node (j2) at (0.4,1.15) {$j_2$};
	\end{tikzpicture}\;.\label{eq:volume_diagram}
\end{equation}
The authors conclude that the matrix elements $\tensor{Q}{_\kappa^{\kappa'}}$ are nonzero only if $\kappa$ and $\kappa'$ differ by exactly one, and are given by~\cite{Rovelli2014}
\begin{equation}
	\begin{array}{lll}		
		c_\kappa &=& \tensor{Q}{_\kappa^{\kappa-1}}\\
		&=& - \frac{\rmi}{2} \left( \kappa(\kappa+1) - (\kappa-1)\kappa \right) \sqrt{2\kappa+1}\\
		&&\sqrt{2k-1} \sqrt{j_1(j_1+1)(2j_1+1)} \sqrt{j_3(j_3+1)(2j_3+1)} \\
		&&
		\begin{Bmatrix}
			j_1 & 1 & j_1 \\
			\kappa & j_2 & \kappa-1
		\end{Bmatrix}
		\begin{Bmatrix}
			j_3 & 1 & j_3 \\
			\kappa & j_4 & \kappa-1
		\end{Bmatrix} ,
	\end{array}
	\label{eq:QRS}
\end{equation}
where the curly brackets denote Wigner $6j$ symbols.\footnote{For a comprehensive derivation of the Wigner $6j$ symbol and possible decompositions, for instance into Wigner $3jm$ symbols, see Ref.~\cite{MartinDussaud2019}.} The resulting matrices are Hermitian and of the form
\begin{align}
	\tensor{Q}{_\kappa^{\kappa'}} 
	&=
	\begin{bmatrix}
		0 & c_1 & 0 & \cdots \\
		\overline{c_1} & 0 & c_2 & \\
		0 & \overline{c_2} & 0 & \\
		\vdots & & & \ddots
	\end{bmatrix} ,
\end{align}
which guarantees that the spectrum of the volume operator is non-degenerate. 
(The eigenvalues come in pairs $\pm\lambda_i$ with an additional zero for odd dimensions.)
