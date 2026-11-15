---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-009-derivation-of-the-categorical-volume-operator
section_title: "Derivation of the categorical volume operator"
section_number: null
pages: 6-9
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.996
doc_brief: "Categorical Quantum Volume Operator — 17 sections: Categorical Quantum Volume Operato; Introduction; The Volume Operator in Loop Quantu"
---
\label{subsec:Qvol.derivation}
To compute the matrix elements of the generalized volume operator, we follow the same steps as for the standard $\SU(2)$ volume operator in LQG~\cite{Rovelli2014}\@. That is, we consider a tetrahedron, but the corresponding four-valent intertwiners are not necessarily irreducible representations of $\SU(2)$. Instead, we treat them as morphisms in a premodular category $\C$,
\begin{equation*}
	\ket{\iota_\kappa}=
	(d_{j_1} d_{j_2} d_{j_3} d_{j_4})^{-1/4}\;
	\begin{tikzpicture}[decoration={markings,mark=at position 0.6 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.5]
		\node (k) at (0,-0.4) {$\kappa$};
		\draw[{postaction=decorate}] (1,0.6) -- (0,0);
		\draw[{postaction=decorate}] (1,0.6) -- (2,1.2);
		\node (j4) at (2,1.6) {$j_4$};
		\draw[{postaction=decorate}] (1,0.6) -- (0.6,1.2);
		\node (j3) at (0.6,1.6) {$j_3$};
		\draw[{postaction=decorate}] (0,0) -- (-1,0.6);
		\draw[{postaction=decorate}] (-1,0.6) -- (-2,1.2);
		\node (j1) at (-2,1.6) {$j_1$};
		\draw[{postaction=decorate}] (-1,0.6) -- (-0.6,1.2);
		\node (j2) at (-0.6,1.6) {$j_2$};
	\end{tikzpicture}\;.
\end{equation*}
With this approach, we can make sense of Eq.~\eqref{eq:volume_derivation_starting_point} in terms of string diagrams. For this purpose, we project the diagram representing $\bra{\iota_\kappa} L_{13}^2 \ket{\iota_{\kappa'}}$ [cf.\ Eq.~\eqref{eq:volume_diagram}] to the plane.
We remark that when working with objects from categories in 3D (as for the quantum volume operator) it is \emph{necessary} to define the operator acting on those degrees of freedom by projecting onto a two-dimensional plane.
For instance, this has also been done in the context of Walker--Wang models~\cite{Walker2012}, which realize topological phases of matter in 3D using objects from unitary braided fusion categories. These are fundamentally different from their 2D Levin--Wen cousins~\cite{LW04} since some twist factors with $R$-matrices appear in the former. 
The projection onto the plane is achieved by using the completeness relation~\eqref{eq:completeness_relation}\@.
Furthermore, we use that
\begin{equation}
	L_{13}^2\;
	\begin{tikzpicture}[baseline=(current bounding box.center)]
		\node (j1_b) at (-0.5,-1.2) {$j_1$};
		\draw (-0.5,-1) -- (0,-0.5);
		\node (j3_b) at (0.5,-1.2) {$j_3$};
		\draw (0.5,-1) -- (0,-0.5);
		\draw (0,-0.5) to node[right] {$\ell$} (0,0.5);
		\node (j1_a) at (-0.5,1.2) {$j_1$};
		\draw (0,0.5) -- (-0.5,1);
		\node (j3_a) at (0.5,1.2) {$j_3$};
		\draw (0,0.5) -- (0.5,1);
	\end{tikzpicture}
	= \alpha_\ell
	\begin{tikzpicture}[baseline=(current bounding box.center)]
		\node (j1_b) at (-0.5,-1.2) {$j_1$};
		\draw (-0.5,-1) -- (0,-0.5);
		\node (j3_b) at (0.5,-1.2) {$j_3$};
		\draw (0.5,-1) -- (0,-0.5);
		\draw (0,-0.5) to node[right] {$\ell$} (0,0.5);
		\node (j1_a) at (-0.5,1.2) {$j_1$};
		\draw (0,0.5) -- (-0.5,1);
		\node (j3_a) at (0.5,1.2) {$j_3$};
		\draw (0,0.5) -- (0.5,1);
	\end{tikzpicture}
	\label{eq:Casimir_second_order}
\end{equation}
and obtain
\begin{align}
	\tensor{Q}{_\kappa^{\kappa'}}
	=& -\frac{\rmi}{4} (\alpha_\kappa - \alpha_{\kappa'}) \frac{1}{\sqrt{d_{j_1} d_{j_2} d_{j_3} d_{j_4}}}\nonumber\\
	&\sum_\ell \sqrt{\frac{d_\ell}{d_{j_1}d_{j_3}}}\; \alpha_\ell\;
	\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
		\coordinate[] (kb) at (0,0);
		\coordinate[] (j1) at (-2,2);
		\coordinate[] (j2) at (1,3);
		\coordinate[] (j3) at (-1,3);
		\coordinate[] (j4) at (2,2);
		\coordinate[] (j3j4kb) at (1,1);
		\coordinate[] (j1j2kb) at (-1,1);
		\coordinate[] (l) at (-1,4);
		\coordinate[] (j1o) at (-2,5);
		\coordinate[] (j1j2k) at (-1,6);
		\coordinate[] (k) at (0,7);
		\coordinate[] (j3j4k) at (1,6);
		\coordinate[] (j4o) at (2,5);
		\coordinate[] (j2o) at (1,4);
		
		\node (textkb) at (0,-0.4) {$\kappa'$};
		\draw[{postaction=decorate}] (j3j4kb) -- (kb);
		\draw (j3j4kb) -- (j4);
		\draw[decoration={markings,mark=at position 0.25 with {\arrow[scale=1,thick,>=stealth]{>}}},{postaction=decorate},{postaction=decorate}] (j3j4kb) -- (j3);
		\draw[{postaction=decorate},overdraw=10pt] (j1j2kb) -- (j2);
		\draw[{postaction=decorate}] (kb) -- (j1j2kb);
		\draw[{postaction=decorate}] (j1j2kb) to node[left] {$j_1$} (j1);
		\draw[{postaction=decorate}] (j1) -- (j3);
		\draw[{postaction=decorate}] (j3) to node[left,midway] {$\ell$} (l);
		\draw[{postaction=decorate}] (l) -- (j1o);
		\draw[{postaction=decorate}] (k) -- (j3j4k);
		\draw (j3j4k) -- (j4o);
		\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
		\draw[decoration={markings,mark=at position 0.8 with {\arrow[scale=1,thick,>=stealth]{>}}},{postaction=decorate},{postaction=decorate}] (l) -- (j3j4k);
		\draw[{postaction=decorate}] (j2) to node[left] {$j_2$} (j2o);
		\draw[{postaction=decorate},overdraw=10pt] (j2o) -- (j1j2k);
		\draw[{postaction=decorate}] (j1o) to node[left] {$j_1$} (j1j2k);
		\draw[{postaction=decorate}] (j1j2k) -- (k);
		\node (textkb) at (0,7.4) {$\kappa$};
		\node (textj3) at (0.7,1.8) {$j_3$};
		\node (jextj3o) at (0.7,5.3) {$j_3$};
	\end{tikzpicture}\;.\label{eq:Qkkb}
\end{align}
The diagram can be computed using the graphical calculus of string diagrams introduced in the previous section. This gives
\begin{widetext}
	\begingroup
	\allowdisplaybreaks
	\begin{align*}
		\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
			\coordinate[] (kb) at (0,0);
			\coordinate[] (j1) at (-2,2);
			\coordinate[] (j2) at (1,3);
			\coordinate[] (j3) at (-1,3);
			\coordinate[] (j4) at (2,2);
			\coordinate[] (j3j4kb) at (1,1);
			\coordinate[] (j1j2kb) at (-1,1);
			\coordinate[] (l) at (-1,4);
			\coordinate[] (j1o) at (-2,5);
			\coordinate[] (j1j2k) at (-1,6);
			\coordinate[] (k) at (0,7);
			\coordinate[] (j3j4k) at (1,6);
			\coordinate[] (j4o) at (2,5);
			\coordinate[] (j2o) at (1,4);
			
			\node (textkb) at (0,-0.4) {$\kappa'$};
			\draw[{postaction=decorate}] (j3j4kb) -- (kb);
			\draw (j3j4kb) -- (j4);
			\draw[decoration={markings,mark=at position 0.25 with {\arrow[scale=1,thick,>=stealth]{>}}},{postaction=decorate},{postaction=decorate}] (j3j4kb) -- (j3);
			\draw[{postaction=decorate},overdraw=10pt] (j1j2kb) -- (j2);
			\draw[{postaction=decorate}] (kb) -- (j1j2kb);
			\draw[{postaction=decorate}] (j1j2kb) to node[left] {$j_1$} (j1);
			\draw[{postaction=decorate}] (j1) -- (j3);
			\draw[{postaction=decorate}] (j3) to node[left,midway] {$\ell$} (l);
			\draw[{postaction=decorate}] (l) -- (j1o);
			\draw[{postaction=decorate}] (k) -- (j3j4k);
			\draw (j3j4k) -- (j4o);
			\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
			\draw[decoration={markings,mark=at position 0.8 with {\arrow[scale=1,thick,>=stealth]{>}}},{postaction=decorate},{postaction=decorate}] (l) -- (j3j4k);
			\draw[{postaction=decorate}] (j2) to node[left] {$j_2$} (j2o);
			\draw[{postaction=decorate},overdraw=10pt] (j2o) -- (j1j2k);
			\draw[{postaction=decorate}] (j1o) to node[left] {$j_1$} (j1j2k);
			\draw[{postaction=decorate}] (j1j2k) -- (k);
			\node (textkb) at (0,7.4) {$\kappa$};
			\node (textj3) at (0.7,1.8) {$j_3$};
			\node (jextj3o) at (0.7,5.3) {$j_3$};
		\end{tikzpicture}
		=&
		\big(F_0^{\kappa'j_3j_4}\big)^{-1}_{\kappa'^*j_4^*} \big(F_0^{\kappa j_3j_4}\big)^{\T}_{\kappa^*j_4^*}
		\begin{tikzpicture}[decoration={markings,mark=at position 0.45 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
			\coordinate[] (kb) at (0,0);
			\coordinate[] (j1) at (-2,2);
			\coordinate[] (j2) at (1,3);
			\coordinate[] (lstart) at (-1,3);
			\coordinate[] (j4) at (2,2);
			\coordinate[] (j3) at (0.5,1.5);
			\coordinate[] (j1j2kb) at (-1,1);
			\coordinate[] (l) at (-1,4);
			\coordinate[] (j1o) at (-2,5);
			\coordinate[] (j1j2k) at (-1,6);
			\coordinate[] (k) at (0,7);
			\coordinate[] (j3o) at (0.5,5.5);
			\coordinate[] (j4o) at (2,5);
			\coordinate[] (j2o) at (1,4);
			\coordinate[] (j3j4k) at (-0.5,6.5);
			\coordinate[] (j3j4kb) at (-0.5,0.5);
			
			\draw (j4) -- (kb);
			\draw[decoration={markings,mark=at position 0.7 with {\arrow[scale=1,thick,>=stealth]{>}}},{postaction=decorate}] (j3) -- (lstart);
			\draw[{postaction=decorate}] (j3j4kb) -- (kb);
			\draw[{postaction=decorate},overdraw=10pt] (j1j2kb) -- (j2);
			\draw[{postaction=decorate}] (j3j4kb) to node[below left] {$\kappa'$} (j1j2kb);
			\draw[{postaction=decorate}] (j1j2kb) to node[left] {$j_1$} (j1);
			\draw[{postaction=decorate}] (j1) -- (lstart);
			\draw[{postaction=decorate}] (lstart) to node[left,midway] {$\ell$} (l);
			\draw[{postaction=decorate}] (l) -- (j1o);
			\draw (k) -- (j4o);
			\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
			\draw[{postaction=decorate}] (l) -- (j3o);
			\draw[{postaction=decorate}] (j2) to node[left] {$j_2$} (j2o);
			\draw[{postaction=decorate},overdraw=10pt] (j2o) -- (j1j2k);
			\draw[{postaction=decorate}] (j1o) to node[left] {$j_1$} (j1j2k);
			\draw[{postaction=decorate}] (j1j2k) to node[above left] {$\kappa$} (j3j4k);
			\draw[{postaction=decorate}] (k) -- (j3j4k);
			\draw (j3o) -- (j3j4k);
			\draw (j3) -- (j3j4kb);
			\node (textj3) at (0.7,1.8) {$j_3$};
			\node (jextj3o) at (0.7,5.3) {$j_3$};
		\end{tikzpicture}\\
		=&
		\big(F_0^{\kappa'j_3j_4}\big)^{-1}_{\kappa'^*j_4^*} \big(F_0^{\kappa j_3j_4}\big)^{\T}_{\kappa^*j_4^*}
		\sum_{m,n} \big(F_{j_4^*}^{j_1j_2j_3}\big)_{\kappa'm} \left(\big(F_{j_4^*}^{j_1j_2j_3}\big)^\T_{\kappa n}\right)^{-1}
		\begin{tikzpicture}[decoration={markings,mark=at position 0.45 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
			\coordinate[] (kb) at (0,0);
			\coordinate[] (j1) at (-2,2);
			\coordinate[] (j2) at (1,3);
			\coordinate[] (lstart) at (-1,3);
			\coordinate[] (j4) at (2,2);
			\coordinate[] (j3) at (0.5,1.5);
			\coordinate[] (l) at (-1,4);
			\coordinate[] (j1o) at (-2,5);
			\coordinate[] (k) at (0,7);
			\coordinate[] (j3o) at (0.5,5.5);
			\coordinate[] (j4o) at (2,5);
			\coordinate[] (j2o) at (1,4);
			\coordinate[] (j3j4k) at (-0.5,6.5);
			\coordinate[] (j3j4kb) at (-0.5,0.5);
			\coordinate[] (j2oo) at (-0.5,5.5);
			\coordinate[] (j2uu) at (-0.5,1.5);
			\coordinate[] (j2j3o) at (0,6);
			\coordinate[] (j2j3u) at (0,1);
			
			\draw (j4) -- (kb);
			\draw[decoration={markings,mark=at position 0.7 with {\arrow[scale=1,thick,>=stealth]{>}}},{postaction=decorate}] (j3) -- (lstart);
			\draw[{postaction=decorate}] (j3j4kb) -- (kb);
			\draw[{postaction=decorate},overdraw=10pt] (j2uu) -- (j2);
			\draw[{postaction=decorate}] (j3j4kb) to node[below left] {$j_1$} (j1);
			\draw[{postaction=decorate}] (j1) -- (lstart);
			\draw[{postaction=decorate}] (lstart) to node[left,midway] {$\ell$} (l);
			\draw[{postaction=decorate}] (l) -- (j1o);
			\draw (k) -- (j4o);
			\draw[{postaction=decorate}] (j4) to node[right] {$j_4$} (j4o);
			\draw[{postaction=decorate}] (l) -- (j3o);
			\draw[{postaction=decorate}] (j2) to node[left] {$j_2$} (j2o);
			\draw[{postaction=decorate},overdraw=10pt] (j2o) -- (j2oo);
			\draw[{postaction=decorate}] (j1o) to node[above left] {$j_1$} (j3j4k);
			\draw[{postaction=decorate}] (k) -- (j3j4k);
			\draw (j3o) -- (j2j3o);
			\draw[{postaction=decorate}] (j2j3o) to node[right] {$n$} (j3j4k);
			\draw (j3) -- (j2j3u);
			\draw[{postaction=decorate}] (j3j4kb) to node[right] {$m$} (j2j3u);
			\draw (j2oo) -- (j2j3o);
			\draw (j2uu) -- (j2j3u);
			\node (textj3) at (0.7,1.8) {$j_3$};
			\node (jextj3o) at (0.7,5.3) {$j_3$};
		\end{tikzpicture}\\
		=&
		\big(F_0^{\kappa'j_3j_4}\big)^{-1}_{\kappa'^*j_4^*} \big(F_0^{\kappa j_3j_4}\big)^{\T}_{\kappa^*j_4^*}
		\sum_{m,n} \big(F_{j_4^*}^{j_1j_2j_3}\big)_{\kappa'm} \left(\big(F_{j_4^*}^{j_1j_2j_3}\big)^\T_{\kappa n}\right)^{-1}
		R_m^{j_2j_3} \big(R_n^{j_3j_2}\big)^{-1}\\
		&\qquad\begin{tikzpicture}[decoration={markings,mark=at position 0.45 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
			\coordinate[] (bottom) at (0,0);
			\coordinate[] (top) at (0,7);
			\coordinate[] (bottomleft) at (-2,2);
			\coordinate[] (bottomright) at (2,2);
			\coordinate[] (topleft) at (-2,5);
			\coordinate[] (topright) at (2,5);
			\coordinate[] (j1j4n) at (-1,6);
			\coordinate[] (j1j4m) at (-1,1);
			\coordinate[] (n) at (0,5);
			\coordinate[] (m) at (0,2);
			\coordinate[] (lstart) at (-2,3);
			\coordinate[] (lend) at (-2,4);
			\coordinate[] (j2start) at (0,3);
			\coordinate[] (j2end) at (0,4);
			\coordinate[] (tl) at (-1.5,4.5);
			\coordinate[] (tr) at (-0.5,4.5);
			\coordinate[] (bl) at (-1.5,2.5);
			\coordinate[] (br) at (-0.5,2.5);
			
			\draw[{postaction=decorate}] (j1j4m) -- (bottom);
			\draw[{postaction=decorate}] (j1j4m) to node[below left] {$j_1$} (bottomleft);
			\draw[{postaction=decorate}] (bottom) -- (bottomright);
			\draw[{postaction=decorate}] (topleft) to node[above left] {$j_1$} (j1j4n);
			\draw[{postaction=decorate}] (top) -- (j1j4n);
			\draw[{postaction=decorate}] (topright) -- (top);
			\draw[{postaction=decorate}] (bottomright) to node[right] {$j_4$} (topright);
			\draw[{postaction=decorate}] (n) to node[right] {$n$} (j1j4n);
			\draw[{postaction=decorate}] (j1j4m) to node[right] {$m$} (m);
			\draw[{postaction=decorate}] (lstart) to node[left] {$\ell$} (lend);
			\draw[{postaction=decorate}] (j2start) to node[right] {$j_2$} (j2end);
			\draw[{postaction=decorate}] (tr) to node[below] {$j_3$} (tl);
			\draw[{postaction=decorate}] (tl) -- (topleft);
			\draw[{postaction=decorate}] (tr) -- (n);
			\draw[{postaction=decorate}] (lend) -- (tl);
			\draw[{postaction=decorate}] (j2end) -- (tr);
			\draw[{postaction=decorate}] (bl) to node[below] {$j_3$} (br);
			\draw[{postaction=decorate}] (br) -- (j2start);
			\draw[{postaction=decorate}] (bl) -- (lstart);
			\draw[{postaction=decorate}] (bottomleft) -- (bl);
			\draw[{postaction=decorate}] (m) -- (br);
		\end{tikzpicture}\\
		=&
		\big(F_0^{\kappa'j_3j_4}\big)^{-1}_{\kappa'^*j_4^*} \big(F_0^{\kappa j_3j_4}\big)^{\T}_{\kappa^*j_4^*}
		\sum_{m,n,o,p} \big(F_{j_4^*}^{j_1j_2j_3}\big)_{\kappa'm} \left(\big(F_{j_4^*}^{j_1j_2j_3}\big)^\T_{\kappa n}\right)^{-1}
		R_m^{j_2j_3} \big(R_n^{j_3j_2}\big)^{-1}\\
		&\qquad \big(F_{j_2}^{\ell^*j_1n}\big)_{j_3o} \big(F_m^{j_1^*\ell j_2}\big)_{j_3^*p^*}\\
		&\qquad\begin{tikzpicture}[decoration={markings,mark=at position 0.45 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),scale=0.8]
			\coordinate[] (bottom) at (0,0);
			\coordinate[] (top) at (0,7);
			\coordinate[] (bottomleft) at (-2,2);
			\coordinate[] (bottomright) at (2,2);
			\coordinate[] (topleft) at (-2,5);
			\coordinate[] (topright) at (2,5);
			\coordinate[] (j1j4n) at (-1,6);
			\coordinate[] (j1j4m) at (-1,1);
			\coordinate[] (n) at (0,5);
			\coordinate[] (m) at (0,2);
			\coordinate[] (lstart) at (-2,3);
			\coordinate[] (lend) at (-2,4);
			\coordinate[] (j2start) at (0,3);
			\coordinate[] (j2end) at (0,4);
			\coordinate[] (ctop) at (-1,4);
			\coordinate[] (cbottom) at (-1,3);
			\coordinate[] (tritop) at (-1,5);
			\coordinate[] (tribottom) at (-1,2);
			
			\draw[{postaction=decorate}] (j1j4m) -- (bottom);
			\draw[{postaction=decorate}] (j1j4m) to node[below left] {$j_1$} (bottomleft);
			\draw[{postaction=decorate}] (bottom) -- (bottomright);
			\draw[{postaction=decorate}] (topleft) to node[above left] {$j_1$} (j1j4n);
			\draw[{postaction=decorate}] (top) -- (j1j4n);
			\draw[{postaction=decorate}] (topright) -- (top);
			\draw[{postaction=decorate}] (bottomright) to node[right] {$j_4$} (topright);
			\draw[{postaction=decorate}] (n) to node[right] {$n$} (j1j4n);
			\draw[{postaction=decorate}] (j1j4m) to node[right] {$m$} (m);
			\draw[{postaction=decorate}] (lstart) to node[left] {$\ell$} (lend);
			\draw[{postaction=decorate}] (j2start) to node[right] {$j_2$} (j2end);
			\draw[{postaction=decorate}] (j2end) -- (ctop);
			\draw[{postaction=decorate}] (lend) -- (ctop);
			\draw[{postaction=decorate}] (cbottom) -- (j2start);
			\draw[{postaction=decorate}] (cbottom) -- (lstart);
			\draw[{postaction=decorate}] (bottomleft) -- (tribottom);
			\draw[{postaction=decorate}] (m) -- (tribottom);
			\draw[{postaction=decorate}] (tritop) -- (topleft);
			\draw[{postaction=decorate}] (tritop) -- (n);
			\draw[{postaction=decorate}] (cbottom) to node[left] {$p$} (tribottom);
			\draw[{postaction=decorate}] (ctop) to node[left] {$o$} (tritop);
		\end{tikzpicture}\\
		=&\big(F_0^{\kappa'j_3j_4}\big)^{-1}_{\kappa'^*j_4^*} \big(F_0^{\kappa j_3j_4}\big)^{\T}_{\kappa^*j_4^*}
		\sum_{m,n,o,p} \big(F_{j_4^*}^{j_1j_2j_3}\big)_{\kappa'm} \left(\big(F_{j_4^*}^{j_1j_2j_3}\big)^\T_{\kappa n}\right)^{-1}
		R_m^{j_2j_3} \big(R_n^{j_3j_2}\big)^{-1}\\
		&\qquad \big(F_{j_2}^{\ell^*j_1n}\big)_{j_3o} \big(F_m^{j_1^*\ell j_2}\big)_{j_3^*p^*}\sqrt{\frac{d_{j_1}d_m}{d_{j_4}}}\delta_{p^*,j_4^*}\sqrt{\frac{d_\ell d_{j_2}}{d_p}} \delta_{o,p^*} \sqrt{\frac{d_{j_1}d_n}{d_{j_4}}}\delta_{o,j_4^*}\;
		\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{<}}},baseline=(current bounding box.center)]
			\draw[{postaction=decorate}] (0,-0.5) to node [left,midway] {$j_4$} (0,0.5);
			\draw (0,0.5) -- (0.5,1) -- (1,0.5);
			\draw[{postaction=decorate}] (1,0.5) to node [right,midway] {$j_4$} (1,-0.5);
			\draw (1,-0.5) -- (0.5,-1) -- (0,-0.5);
		\end{tikzpicture}\\
		=&
		\big(F_0^{\kappa'j_3j_4}\big)^{-1}_{\kappa'^*j_4^*} \big(F_0^{\kappa j_3j_4}\big)_{j_4^*\kappa^*} d_{j_1} \sqrt{\frac{d_{j_2}d_\ell}{d_{j_4}}}
		\sum_{m,n} \sqrt{d_md_n} \big(F_{j_4^*}^{j_1j_2j_3}\big)_{\kappa'm} \big(F_{j_4^*}^{j_1j_2j_3}\big)^{-1}_{n\kappa}
		\\
		&\qquad R_m^{j_2j_3} \big(R_n^{j_3j_2}\big)^{-1}\big(F_{j_2}^{\ell^*j_1n}\big)_{j_3j_4^*} \big(F_m^{j_1^*\ell j_2}\big)_{j_3^*j_4^*},
	\end{align*}
	\endgroup
\end{widetext}
where the penultimate step uses the bigon relation~\eqref{eq:bigon_relation} three times. This expression can be further simplified using tetrahedral symmetry~\eqref{eq:tetrahedral_symmetry}\@. In particular, we can rewrite the following $F$-symbol by using the equality from the first to the second tetrahedral symmetry relation
\begin{equation}
	\big(F_m^{j_1^*\ell j_2}\big)_{j_3^*j_4^*} = \big(F_{j_2^*}^{\ell j_1^* m^*}\big)_{j_3^* j_4}.
\end{equation}
Then, we use the equality from the first to the fourth tetrahedral symmetry relation to rewrite
\begin{align}
	\big(F_{j_2}^{\ell^*j_1n}\big)_{j_3j_4^*} &= \sqrt{\frac{d_{j_3} d_{j_4}}{d_n d_\ell}} \big(F_{j_2^*}^{j_3^* j_1 j_4}\big)_{\ell n^*}\\
	\big(F_{j_2^*}^{\ell j_1^* m^*}\big)_{j_3^* j_4} &= \sqrt{\frac{d_{j_3} d_{j_4}}{d_m d_\ell}} \big(F_{j_2}^{j_3 j_1^* j_4^*}\big)_{\ell^* m}.
\end{align}
Inserting everything back into Eq.~\eqref{eq:Qkkb} finally gives
\begin{align}
	\tensor{Q}{_\kappa^{\kappa'}} =& -\frac{\rmi}{4} (\alpha_\kappa - \alpha_{\kappa'}) \big(F_0^{\kappa'j_3j_4}\big)^{-1}_{\kappa'^*j_4^*} \big(F_0^{\kappa j_3j_4}\big)_{j_4^*\kappa^*}\nonumber
	\\
	&\sum_{m,n} \big(F_{j_4^*}^{j_1j_2j_3}\big)_{\kappa'm} \big(F_{j_4^*}^{j_1j_2j_3}\big)^{-1}_{n\kappa} R_m^{j_2j_3} \big(R_n^{j_3j_2}\big)^{-1}\nonumber
	\\
	&\quad\sum_\ell \alpha_\ell \big(F_{j_2^*}^{j_3^* j_1 j_4}\big)_{\ell n^*} \big(F_{j_2}^{j_3 j_1^* j_4^*}\big)_{\ell^* m}.\label{eq:generalized_volume}
\end{align}
In the case where $\C$ is unitary, we have the additional relation
\begin{equation}
	\big(F_{d^*}^{a^*b^*c^*}\big)_{e^*f^*} = \overline{\big(F_d^{abc}\big)}_{ef}
\end{equation}
for the $F$-symbols. This allows us to further simplify Eq.~\eqref{eq:generalized_volume} for unitary categories. Here, we obtain
\begin{align}
	\tensor{Q}{_\kappa^{\kappa'}} =& -\frac{\rmi}{4} (\alpha_\kappa - \alpha_{\kappa'}) \overline{\big(F_0^{\kappa'j_3j_4}\big)}_{j_4^* \kappa'^*} \big(F_0^{\kappa j_3j_4}\big)_{j_4^*\kappa^*} \nonumber \\
	&\sum_{m,n} \big(F_{j_4^*}^{j_1j_2j_3}\big)_{\kappa'm} \overline{\big(F_{j_4^*}^{j_1j_2j_3}\big)}_{\kappa n} R_m^{j_2j_3} \overline{R_n^{j_2j_3}} \nonumber \\
	&\quad\sum_\ell \alpha_\ell \big(F_{j_2^*}^{j_3^* j_1 j_4}\big)_{\ell n^*} \overline{\big(F_{j_2^*}^{j_3^* j_1 j_4}\big)}_{\ell m^*}.\label{eq:generalized_volume_unitary}
\end{align}
Note that the summation indices in Eq.~\eqref{eq:generalized_volume} and Eq.~\eqref{eq:generalized_volume_unitary} range over the following fusion products:
\begin{align}
	\begin{aligned}
		m,n &\in (j_1\otimes j_4^*) \cap (j_2\otimes j_3)\\
		\ell &\in (j_1\otimes j_3) \cap (j_2\otimes j_4^*).
	\end{aligned}
\end{align}
Finally, we comment on some aspects of our construction starting with the quadratic Casimir operator $L_{13}$, whose eigenvalues appear in our formulas for the generalized volume operator. In Ref.~\cite{Links1992} it has been shown how to generalize the idea of a Casimir invariant in Lie groups to quasi-triangular Hopf algebras. Notice that ribbon Hopf algebras are quasi-triangular, so if $\C$ is the representation category of a Hopf algebra, then the theory of Ref.~\cite{Links1992} applies:
Let $A$ be a Hopf algebra and fix an invariant bilinear form $\langle\cdot,\cdot\rangle$ on $A$. Furthermore, let $M$ be a finite-dimensional subspace of $A$, which is stable under the adjoint action of elements in $A$ and on which $\langle\cdot,\cdot\rangle$ is nondegenerate. Such an $M$ is a submodule of $A$. If we choose a basis $\{a_i\}_{i=1}^m$ for $M$, then we can define the quadratic Casimir as
\begin{equation}
	C_M = \sum_{i=1}^m a_i(a^i),
	\label{eq:Casimir}
\end{equation}
where $\{a^i\}_{i=1}^m$ is the $\langle\cdot,\cdot\rangle$-dual basis. As per Eq.~\eqref{eq:Casimir_second_order}, $L_{13}^2$ is a second-order Casimir operator, i.e.\ $C_M\in A \otimes A$. Links and Gould prove that $C_M$ is in the centre of $A$~\cite[Prop.~1]{Links1992}\@. Furthermore, $C_M$ is proportional to the identity $I\otimes I\in A\otimes A$ due to Schur's Lemma. In our setting, $M$ is a simple object in $\C$ and the proportionality constant $C_M\propto I\otimes I$ is $\alpha_M$. Links and Gould construct $C_M$ for the cases where $A=\mathcal{D}(G)$~\cite[Sec.~4]{Links1992}, i.e.\ the quantum double of a finite group $G$, and for $A=U_q(\mathfrak{g})$~\cite[Sec.~5]{Links1992}, i.e.\ a quantum group associated to a simple Lie algebra $\mathfrak{g}$. For quantum groups, the $\alpha_M$ are explicitly constructed in~\cite[Sec.~5]{Links1992}\@. For quantum double models, they can be computed through the universal $R$-matrix in $A$. It is worth noting that the universal $R$-matrix differs from the categorical $R$-matrix introduced in Eq.~\eqref{eq:R-matrix}\@. While the categorical $R$-matrix concerns the braiding of two $A$-modules $M$, the universal $R$-matrix is an invertible element in $A\otimes A$ satisfying the Yang--Baxter equation. To compute $C_M$ for $A=\mathcal{D}(G)$, we must find the representation $R_M$ of the universal $R$-matrix in the submodule $M$. Then, for every $M$, the element $C_M=T(R_M) R_M$ defines the Casimir operator. Here, $T:A\otimes A\rightarrow A\otimes A, a\otimes b \mapsto b\otimes a$.
	
It is worth pointing out that in the case where $\alpha_\ell=1$ for all $\ell$, the volume operator becomes zero due to the term $(\alpha_\kappa - \alpha_{\kappa'})$. This is the case if $A$ is triangular so that $\C$ has a symmetric braiding.

Lastly, we would like to mention that our construction is compatible with defining curved tetrahedra, which have been considered in Ref.~\cite{Han2023}\@.
In this case, isotopy invariance~\eqref{eq:normalization_trivalent_vertices} ensures that the value of the tetrahedron does not change despite continuous deformation of its edges.
Therefore, our generalized quantum tetrahedron can be flatly embedded in an arbitrarily curved spacetime.
