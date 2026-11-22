---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-010-beyond-ribbon-fusion-categories
section_title: "Beyond ribbon fusion categories"
section_number: null
pages: 9-11
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 1.0
doc_brief: "Categorical Quantum Volume Operator — 17 sections: Categorical Quantum Volume Operato; Introduction; The Volume Operator in Loop Quantu"
---
\label{subsec:spherical.C}
In the derivation of the standard volume operator for $\SU(2)$, the closure constraint~\eqref{eq:closure_constraint} guarantees that any oriented triplet $\vec{L}_j,\vec{L}_k,\vec{L}_\ell$ in the definition of the volume operator~\eqref{eq:def_volume_operator} gives the same result. As mentioned previously, the category-theoretic analog of the closure constraint is the tetrahedral symmetry condition~\eqref{eq:tetrahedral_symmetry}\@. However, there is a subtlety, which comes from the fact that we have to project the diagram in Eq.~\eqref{eq:volume_diagram} to the plane to make it amenable to the string diagram calculus in fusion categories. In the absence of tetrahedral symmetry, different couplings $j_k$--$j_\ell$ are, \textit{a priori}, not equivalent topologically. For example, consider the case of coupling $j_2$ and $j_3$ in Eq.~\eqref{eq:volume_diagram}\@. Then, Eq.~\eqref{eq:volume_derivation_starting_point} becomes
\begin{equation}
	\tensor{\tilde{Q}}{_\kappa^{\kappa'}} = - \frac{\rmi}{4} (\alpha_\kappa - \alpha_{\kappa'}) \bra{\iota_\kappa} L_{23}^2 \ket{\iota_{\kappa'}}\label{eq:volume_derivation_starting_point_j23}
\end{equation}
where we have denoted the operator as $\tilde{Q}$ for distinction from $\hat{Q}$. The diagram corresponding to Eq.~\eqref{eq:volume_diagram} then becomes
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
		\node[draw,rectangle] (L13) at (1,0.65) {$L_{23}^2$};
		\draw[dashed] (0.225,0.65) -- (L13);
		\draw (1.775,0.65) -- (L13);
		\node (j3) at (1.6,1.15) {$j_3$};
		\node (j2) at (0.4,1.15) {$j_2$};
	\end{tikzpicture}\;.\label{eq:volume_diagram_j23}
\end{equation}
Now, projecting the diagram in Eq.~\eqref{eq:volume_diagram_j23} to the plane does not involve braiding anymore. More concretely, we obtain the following volume operator for this scenario
\begin{align}
	\tensor{\tilde{Q}}{_\kappa^{\kappa'}}
	=& -\frac{\rmi}{4} (\alpha_\kappa - \alpha_{\kappa'}) \frac{1}{\sqrt{d_{j_1} d_{j_2} d_{j_3} d_{j_4}}}\nonumber\\
	&\sum_\ell \sqrt{\frac{d_\ell}{d_{j_2}d_{j_3}}}\; \alpha_\ell\;
	\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
		\coordinate[] (kb) at (0,0);
		\coordinate[] (j1) at (-2,2);
		\coordinate[] (j4) at (2,2);
		\coordinate[] (j3j4kb) at (1,1);
		\coordinate[] (j1j2kb) at (-1,1);
		\coordinate[] (j1o) at (-2,5);
		\coordinate[] (j1j2k) at (-1,6);
		\coordinate[] (k) at (0,7);
		\coordinate[] (j3j4k) at (1,6);
		\coordinate[] (j4o) at (2,5);
		\coordinate[] (j2j3) at (0,2);
		\coordinate[] (j2j3o) at (0,5);
		
		\node (textkb) at (0,-0.4) {$\kappa'$};
		\draw[{postaction=decorate}] (j3j4kb) -- (kb);
		\draw (j3j4kb) -- (j4);
		\draw[{postaction=decorate}] (kb) -- (j1j2kb);
		\draw (j1j2kb) -- (j1);
		\draw[{postaction=decorate}] (k) -- (j3j4k);
		\draw (j3j4k) -- (j4o);
		\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
		\draw (j1o) -- (j1j2k);
		\draw[{postaction=decorate}] (j1j2k) -- (k);
		\draw[{postaction=decorate}] (j1) to node[left] {$j_1$} (j1o);
		\draw[{postaction=decorate}] (j1j2kb) to node[above left] {$j_2$} (j2j3);
		\draw[{postaction=decorate}] (j3j4kb) to node[above right] {$j_3$} (j2j3);
		\draw[{postaction=decorate}] (j2j3o) to node[below left] {$j_2$} (j1j2k);
		\draw[{postaction=decorate}] (j2j3o) to node[below right] {$j_3$} (j3j4k);
		\draw[{postaction=decorate}] (j2j3) to node[left] {$\ell$} (j2j3o);
		\node (textkb) at (0,7.4) {$\kappa$};
	\end{tikzpicture}\;.\label{eq:Qkkb_j23}
\end{align}
Due to the vector identities $\vec{v}\times\vec{w}=-\vec{w}\times\vec{v}$ and $\vec{w}\cdot(\vec{u}\times\vec{v})=\vec{u}\otimes(\vec{v}\times\vec{w})=\vec{v}\cdot(\vec{w}\times\vec{u})$ as well as rotational symmetry of the diagram \eqref{eq:volume_diagram}, all possible different couplings of $j_k$ and $j_\ell$ are equivalent to either $j_1$--$j_3$ or $j_2$--$j_3$. That is, the coupling of two neighbouring $j_{k}$--$j_{k+1}$ corresponds to $j_2$--$j_3$, whereas a coupling of two next-to-nearest neighbours $j_{k}$--$j_{k+2}$ corresponds to $j_1$--$j_3$ [subject to periodicity $j_{k+4}=j_k$]. The couplings $j_1$--$j_2$ and $j_3$--$j_4$ are topologically trivial and therefore forbidden. We can compute the diagram \eqref{eq:Qkkb_j23} using a sequence of $F$-symbols, namely
\begin{widetext}
	\begingroup
	\allowdisplaybreaks
	\begin{align*}
		\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
			\coordinate[] (kb) at (0,0);
			\coordinate[] (j1) at (-2,2);
			\coordinate[] (j4) at (2,2);
			\coordinate[] (j3j4kb) at (1,1);
			\coordinate[] (j1j2kb) at (-1,1);
			\coordinate[] (j1o) at (-2,5);
			\coordinate[] (j1j2k) at (-1,6);
			\coordinate[] (k) at (0,7);
			\coordinate[] (j3j4k) at (1,6);
			\coordinate[] (j4o) at (2,5);
			\coordinate[] (j2j3) at (0,2);
			\coordinate[] (j2j3o) at (0,5);
			
			\node (textkb) at (0,-0.4) {$\kappa'$};
			\draw[{postaction=decorate}] (j3j4kb) -- (kb);
			\draw (j3j4kb) -- (j4);
			\draw[{postaction=decorate}] (kb) -- (j1j2kb);
			\draw (j1j2kb) -- (j1);
			\draw[{postaction=decorate}] (k) -- (j3j4k);
			\draw (j3j4k) -- (j4o);
			\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
			\draw (j1o) -- (j1j2k);
			\draw[{postaction=decorate}] (j1j2k) -- (k);
			\draw[{postaction=decorate}] (j1) to node[left] {$j_1$} (j1o);
			\draw[{postaction=decorate}] (j1j2kb) to node[above left] {$j_2$} (j2j3);
			\draw[{postaction=decorate}] (j3j4kb) to node[above right] {$j_3$} (j2j3);
			\draw[{postaction=decorate}] (j2j3o) to node[below left] {$j_2$} (j1j2k);
			\draw[{postaction=decorate}] (j2j3o) to node[below right] {$j_3$} (j3j4k);
			\draw[{postaction=decorate}] (j2j3) to node[left] {$\ell$} (j2j3o);
			\node (textkb) at (0,7.4) {$\kappa$};
		\end{tikzpicture}
		=&
		\big(F_0^{j_1j_2\kappa'^*}\big)_{\kappa'j_1^*} \big(F_0^{j_1j_2\kappa^*}\big)_{\kappa j_1^*}^\T\;
		\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
			\coordinate[] (kb) at (0,0);
			\coordinate[] (j1) at (-2,2);
			\coordinate[] (j4) at (2,2);
			\coordinate[] (j3j4kb) at (0.75,0.75);
			\coordinate[] (j1j2kb) at (-1,1);
			\coordinate[] (j1o) at (-2,5);
			\coordinate[] (j1j2k) at (-1,6);
			\coordinate[] (k) at (0,7);
			\coordinate[] (j3j4k) at (0.75,6.25);
			\coordinate[] (j4o) at (2,5);
			\coordinate[] (j2j3) at (0,1.5);
			\coordinate[] (j2j3o) at (0,5.5);
			\coordinate[] (j2j3k) at (1.25,5.75);
			\coordinate[] (lo) at (0,4.5);
			\coordinate[] (j2j3kb) at (1.25,1.25);
			\coordinate[] (l) at (0,2.5);
			
			\draw[{postaction=decorate}] (j3j4kb) -- (kb);
			\draw (j2j3kb) -- (j4);
			\draw (kb) -- (j1j2kb);
			\draw (j1j2kb) -- (j1);
			\draw[{postaction=decorate}] (k) -- (j2j3k);
			\draw (j2j3k) -- (j4o);
			\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
			\draw (j1o) -- (j1j2k);
			\draw (j1j2k) -- (k);
			\draw[{postaction=decorate}] (j1) to node[left] {$j_1$} (j1o);
			\draw[{postaction=decorate}] (j3j4kb) -- (j2j3);
			\draw[{postaction=decorate}] (j2j3o) -- (j3j4k);
			\draw[{postaction=decorate}] (j2j3) to node[left] {$\ell$} (j2j3o);
			\draw[{postaction=decorate}] (lo) to node[below right] {$j_3$} (j2j3k);
			\draw[{postaction=decorate}] (j2j3k) to node[above right] {$\kappa$} (j3j4k);
			\draw[{postaction=decorate}] (j2j3kb) to node[above right] {$j_3$} (l);
			\draw[{postaction=decorate}] (j3j4kb) to node[below right] {$\kappa'$} (j2j3kb);
			\node (textj2) at (-0.25,1.5) {$j_2$};
			\node (textj2o) at (-0.25,5.5) {$j_2$};
		\end{tikzpicture}\\
		=&
		\big(F_0^{j_1j_2\kappa'^*}\big)_{\kappa'j_1^*} \big(F_0^{j_1j_2\kappa^*}\big)_{\kappa j_1^*}^\T
		\sum_{m,n} \big(F_{j_1^*}^{j_2j_3j_4}\big)_{\kappa'm}^{-1} \left(\big(F_{j_1^*}^{j_2j_3j_4}\big)_{\kappa n}^\T\right)^{-1}\;
		\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
			\coordinate[] (kb) at (0,0);
			\coordinate[] (j1) at (-2,2);
			\coordinate[] (j4) at (2,2);
			\coordinate[] (j3j4kb) at (0.75,0.75);
			\coordinate[] (j1j2kb) at (-1,1);
			\coordinate[] (j1o) at (-2,5);
			\coordinate[] (j1j2k) at (-1,6);
			\coordinate[] (k) at (0,7);
			\coordinate[] (j3j4k) at (0.75,6.25);
			\coordinate[] (j4o) at (2,5);
			\coordinate[] (j2j3) at (0,1.5);
			\coordinate[] (j2j3o) at (0,5.5);
			\coordinate[] (n) at (0,5);
			\coordinate[] (m) at (0,2);
			\coordinate[] (l) at (0,3);
			\coordinate[] (lo) at (0,4);
			\coordinate[] (bul) at (-0.5,2.5);
			\coordinate[] (bur) at (0.5,2.5);
			\coordinate[] (bol) at (-0.5,4.5);
			\coordinate[] (bor) at (0.5,4.5);
			
			\draw[{postaction=decorate}] (j3j4kb) -- (kb);
			\draw (j3j4kb) -- (j4);
			\draw (kb) -- (j1j2kb);
			\draw (j1j2kb) -- (j1);
			\draw[{postaction=decorate}] (k) -- (j3j4k);
			\draw (j3j4k) -- (j4o);
			\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
			\draw (j1o) -- (j1j2k);
			\draw (j1j2k) -- (k);
			\draw[{postaction=decorate}] (j1) to node[left] {$j_1$} (j1o);
			\draw (j3j4kb) -- (j2j3);
			\draw (j2j3o) -- (j3j4k);
			\draw[{postaction=decorate}] (n) to node[left] {$n$} (j2j3o);
			\draw[{postaction=decorate}] (j2j3) to node[left] {$m$} (m);
			\draw[{postaction=decorate}] (l) to node[left] {$\ell$} (lo);
			\draw (m) -- (bul);
			\draw[{postaction=decorate}] (bul) -- (l);
			\draw (m) -- (bur);
			\draw[{postaction=decorate}] (bur) -- (l);
			\draw (lo) -- (bol);
			\draw[{postaction=decorate}] (bol) -- (n);
			\draw (lo) -- (bor);
			\draw[{postaction=decorate}] (bor) -- (n);
			\node (textj2) at (-0.75,2.5) {$j_2$};
			\node (textj3) at (0.75,2.5) {$j_3$};
			\node (textj2o) at (-0.75,4.5) {$j_2$};
			\node (textj3o) at (0.75,4.5) {$j_3$};
		\end{tikzpicture}\\
		=&
		\big(F_0^{j_1j_2\kappa'^*}\big)_{\kappa'j_1^*} \big(F_0^{j_1j_2\kappa^*}\big)_{\kappa j_1^*}^\T
		\sum_{m,n} \big(F_{j_1^*}^{j_2j_3j_4}\big)_{\kappa'm}^{-1} \left(\big(F_{j_1^*}^{j_2j_3j_4}\big)_{\kappa n}^\T\right)^{-1}
		\frac{d_{j_2}d_{j_3}}{d_\ell} \delta_{m,\ell}\delta_{n,\ell}\\
		&
		\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.4]
			\coordinate[] (kb) at (0,0);
			\coordinate[] (j1) at (-2,2);
			\coordinate[] (j4) at (2,2);
			\coordinate[] (j3j4kb) at (1,1);
			\coordinate[] (j1j2kb) at (-1,1);
			\coordinate[] (j1o) at (-2,5);
			\coordinate[] (j1j2k) at (-1,6);
			\coordinate[] (k) at (0,7);
			\coordinate[] (j3j4k) at (1,6);
			\coordinate[] (j4o) at (2,5);
			\coordinate[] (j2j3) at (0,2);
			\coordinate[] (j2j3o) at (0,5);
			
			\draw[{postaction=decorate}] (j3j4kb) -- (kb);
			\draw (j3j4kb) -- (j4);
			\draw (kb) -- (j1j2kb);
			\draw (j1j2kb) -- (j1);
			\draw[{postaction=decorate}] (k) -- (j3j4k);
			\draw (j3j4k) -- (j4o);
			\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
			\draw (j1o) -- (j1j2k);
			\draw (j1j2k) -- (k);
			\draw[{postaction=decorate}] (j1) to node[left] {$j_1$} (j1o);
			\draw (j3j4kb) -- (j2j3);
			\draw (j2j3o) -- (j3j4k);
			\draw[{postaction=decorate}] (j2j3) to node[left] {$\ell$} (j2j3o);
		\end{tikzpicture}\\
		=&
		\big(F_0^{j_1j_2\kappa'^*}\big)_{\kappa'j_1^*} \big(F_0^{j_1j_2\kappa^*}\big)_{\kappa j_1^*}^\T
		\big(F_{j_1^*}^{j_2j_3j_4}\big)_{\kappa'\ell}^{-1} \left(\big(F_{j_1^*}^{j_2j_3j_4}\big)_{\kappa \ell}^\T\right)^{-1}
		\frac{d_{j_2}d_{j_3}}{d_\ell} \sqrt{\frac{d_\ell d_{j_4}}{d_{j_1}}}
		\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)]
			\draw[{postaction=decorate}] (0,-0.5) to node [left,midway] {$j_1$} (0,0.5);
			\draw (0,0.5) -- (0.5,1) -- (1,0.5);
			\draw[{postaction=decorate}] (1,0.5) to node [right,midway] {$j_1$} (1,-0.5);
			\draw (1,-0.5) -- (0.5,-1) -- (0,-0.5);
		\end{tikzpicture}\\
		=&
		\sqrt{\frac{d_{j_1}d_{j_4}}{d_\ell}} d_{j_2} d_{j_3} \big(F_0^{j_1j_2\kappa'^*}\big)_{\kappa'j_1^*} \big(F_0^{j_1j_2\kappa^*}\big)_{j_1^* \kappa}
		\big(F_{j_1^*}^{j_2j_3j_4}\big)_{\kappa'\ell}^{-1} \big(F_{j_1^*}^{j_2j_3j_4}\big)_{\ell \kappa}^{-1}.
	\end{align*}
	\endgroup	
\end{widetext}
In total, the volume operator for the $j_2$--$j_3$ coupling becomes
\begin{align}
	\tensor{\tilde{Q}}{_\kappa^{\kappa'}}=&-\frac{\rmi}{4} (\alpha_\kappa -\alpha_{\kappa'})\big(F_0^{j_1j_2\kappa'^*}\big)_{\kappa'j_1^*} \big(F_0^{j_1j_2\kappa^*}\big)_{j_1^* \kappa}\nonumber\\
	&\sum_{\ell} \alpha_\ell \big(F_{j_1^*}^{j_2j_3j_4}\big)_{\kappa'\ell}^{-1} \big(F_{j_1^*}^{j_2j_3j_4}\big)_{\ell \kappa}^{-1},\label{eq:volume_j2j3}
\end{align}
where the sum over $\ell$ goes over the fusion product
\begin{equation}
	\ell\in (j_2\otimes j_3)\cap (j_1^*\otimes j_4).
\end{equation}
In the unitary case, $\tensor{\tilde{Q}}{_\kappa^{\kappa'}}$ reduces to
\begin{align}
	\tensor{\tilde{Q}}{_\kappa^{\kappa'}}=&-\frac{\rmi}{4} (\alpha_\kappa -\alpha_{\kappa'})\big(F_0^{j_1j_2\kappa'^*}\big)_{\kappa'j_1^*} \overline{\big(F_0^{j_1j_2\kappa^*}\big)}_{\kappa j_1^*}\nonumber\\
	&\sum_{\ell} \alpha_\ell \overline{\big(F_{j_1^*}^{j_2j_3j_4}\big)}_{\ell\kappa'} \big(F_{j_1^*}^{j_2j_3j_4}\big)_{\ell\kappa}.\label{eq:volume_j2j3_unitary}
\end{align}
A remarkable property of the $j_2$--$j_3$ volume operator is that its derivation involves neither the $R$-matrices nor the tetrahedral symmetry condition. Therefore, we can use this construction to go beyond the case of ribbon fusion categories. In particular, Eq.~\eqref{eq:volume_j2j3} is well-defined for any spherical fusion category $\C$ and Eq.~\eqref{eq:volume_j2j3_unitary} requires $\C$ to be a unitary fusion category. Nevertheless, for ribbon fusion categories, tetrahedral symmetry ensures that both the $j_1$--$j_3$ volume operator $\hat{Q}$  [Eq.~\eqref{eq:generalized_volume_unitary}] and the $j_2$--$j_3$ volume operator $\tilde{Q}$[Eq.~\eqref{eq:volume_j2j3_unitary}] coincide up to a phase factor related to the braiding. For $\C=\SU(2)_k$, it can be verified that this phase factor is $(-1)^{\kappa+\kappa'+2j_1+2j_2}$.
