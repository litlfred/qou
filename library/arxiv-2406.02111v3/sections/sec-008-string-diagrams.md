---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-008-string-diagrams
section_title: "String diagrams"
section_number: null
pages: 5-6
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.975
doc_brief: "Categorical Quantum Volume Operator — 17 sections: Categorical Quantum Volume Operato; Introduction; The Volume Operator in Loop Quantu"
---
\label{subsec:string_diagrams}
A fusion category is uniquely specified by its skeletal data, see e.g.\ Refs.~\cite{Bridgeman2020,Barter2022}\@. That is
\begin{enumerate}[(i)]
	\item a finite set $I=\{0,a,b,\dots\}$ of simple objects as well as their duals $0,a^*,b^*,\dots$, where $0$ labels the unit object;
	\item the fusion rules for all $a,b\in I$,
	\begin{equation*}
		a\otimes b = \sum_{c\in I} N_{ab}^{c} c,
	\end{equation*}
	together with the fusion spaces $\hom(a\otimes b,c)$ [which are vector spaces of dimension $N_{ab}^c$] represented by trivalent vertices
	\begin{equation*}
		\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),rotate=180] 
			\draw[{postaction=decorate}] (0,0) to node [right,midway] {$c$} (0,-1);
			\draw[{postaction=decorate}] (0.75,0.75) to node [above left,midway] {$a$} (0,0);
			\draw[{postaction=decorate}] (-0.75,0.75) to node [above right,midway] {$b$} (0,0);
		\end{tikzpicture}\;,
	\end{equation*}
	and
	\item the $F$-symbols, which relate different fusion paths to each other via relations of the form
	\begin{equation}
		\begin{tikzpicture}[scale=1,baseline=(current bounding box.center), decoration={markings,mark=at position .6 with {\arrow[>=stealth]{>}}}]
			\node (u1) at (0,0) {$d$};
			\coordinate (v11) at (0,0.5);
			\coordinate (v12) at (-0.5,1);
			\node (x1) at (-1,1.5) {$a$};
			\node (y1) at (0,1.5) {$b$};
			\node (z1) at (1,1.5) {$c$};
				
			\draw[{postaction=decorate}] (u1) -- (v11);
			\draw[{postaction=decorate}] (v11) -- (z1);
			\draw[{postaction=decorate}] (v11) to node[below left] {$e$} (v12);
			\draw[{postaction=decorate}] (v12) -- (y1);
			\draw[{postaction=decorate}] (v12) -- (x1);
		\end{tikzpicture}
		=\sum_{f} \big(F_d^{abc}\big)_{ef}
		\begin{tikzpicture}[scale=1,baseline=(current bounding box.center), decoration={markings,mark=at position .6 with {\arrow[>=stealth]{>}}}]
			\node (u2) at (0,0) {$d$};
			\coordinate (v21) at (0,0.5);
			\coordinate (v22) at (0.5,1);
			\node (x2) at (-1,1.5) {$a$};
			\node (y2) at (0,1.5) {$b$};
			\node (z2) at (1,1.5) {$c$};
				
			\draw[{postaction=decorate}] (u2) -- (v21);
			\draw[{postaction=decorate}] (v21) -- (x2);
			\draw[{postaction=decorate}] (v21) to node[below right] {$f$} (v22);
			\draw[{postaction=decorate}] (v22) -- (y2);
			\draw[{postaction=decorate}] (v22) -- (z2);
		\end{tikzpicture}\;.\label{eq:F-symbols}
	\end{equation}		
\end{enumerate}
For notational simplicity, we work with multiplicity-free categories, i.e.\ $N_{ab}^c=1$ for all $a,b,c\in I$. However, this is not a necessary assumption and our construction can be made general by introducing an additional fusion label to each trivalent vertex. The $F$-symbols are the category-theoretic generalization of the Wigner $6j$ symbols.
	
For the fusion spaces in $\C$, we fix the standard basis
\begin{equation}
	\begin{tikzpicture}[scale=1.5,baseline=(current bounding box.center), decoration={markings,mark=at position .6 with {\arrow[>=stealth]{>}}}]
		\coordinate (ydown) at (0,0);
		\coordinate (yup) at (0,0.5);
		\coordinate (t12) at (-0.5,1);
		\node (x1) at (-1,1.5) {$a_1$};
		\node (x2) at (0,1.5) {$a_2$};
		\node (xm) at (1,1.5) {$a_m$};
		
		\draw[{postaction=decorate}] (ydown) to node[right] {$b$} (yup);
		\draw[{postaction=decorate}] (yup) -- (xm);
		\draw[{postaction=decorate}] (yup) to node[below left] {$b_2$} (t12);
		\draw[{postaction=decorate}] (t12) -- (x2);
		\draw[{postaction=decorate}] (t12) -- (x1);
		
		\node (xsn) at (1,-1) {$a'_n$};
		\draw[{postaction=decorate}] (xsn) -- (ydown);
		\node (xs1) at (-1,-1) {$a'_1$};
		\node (xs2) at (0,-1) {$a'_2$};
		\coordinate (t12s) at (-0.5,-0.5);
		\draw[{postaction=decorate}] (xs1) -- (t12s);
		\draw[{postaction=decorate}] (xs2) -- (t12s);
		\draw[{postaction=decorate}] (t12s) to node[above left] {$b'_2$} (ydown);
		
		\node (downdots) at (0.5,-1) {$\cdots$};
		\node (updots) at (0.5,1.5) {$\cdots$};
		\node[rotate=45] (ysdots) at (-0.15,-0.35) {$\cdots$};
		\node[rotate=-45] (ydots) at (-0.15,0.85) {$\cdots$};
	\end{tikzpicture}\label{eq:standard_basis}
\end{equation}
and choose the following normalization for the trivalent vertices:
\begin{equation}
	\left(\frac{d_c}{d_ad_b}\right)^{1/4}\;
	\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)] 
		\draw[{postaction=decorate}] (0,-1) to node [left,midway] {$c$} (0,0);
		\draw[{postaction=decorate}] (0,0) to node [below right,midway] {$b$} (0.75,0.75);
		\draw[{postaction=decorate}] (0,0) to node [below left,midway] {$a$} (-0.75,0.75);
	\end{tikzpicture}\;,
	\quad
	\left(\frac{d_c}{d_ad_b}\right)^{1/4}\;
	\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),rotate=180] 
		\draw[{postaction=decorate}] (0,0) to node [right,midway] {$c$} (0,-1);
		\draw[{postaction=decorate}] (0.75,0.75) to node [above left,midway] {$a$} (0,0);
		\draw[{postaction=decorate}] (-0.75,0.75) to node [above right,midway] {$b$} (0,0);
	\end{tikzpicture}\;,\label{eq:normalization_trivalent_vertices}
\end{equation}
where $d_a$ denotes the quantum dimension of the object $a\in\C$,
\begin{equation}
	d_a=
	\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)]
		\draw[{postaction=decorate}] (0,-0.5) to node [left,midway] {$a$} (0,0.5);
		\draw (0,0.5) -- (0.5,1) -- (1,0.5);
		\draw[{postaction=decorate}] (1,0.5) to node [right,midway] {$a$} (1,-0.5);
		\draw (1,-0.5) -- (0.5,-1) -- (0,-0.5);
	\end{tikzpicture}
	\; , \label{eq:quantum_dimension}
\end{equation}
and $d_a=d_{a^*}$ for all objects $a\in\C$. This normalization convention is standard in the physics literature as it ensures isotopy invariance~\cite{Bonderson2007}\@. That is, the value of a string diagram remains invariant when the strings are continuously deformed keeping their open ends fixed in place. Using this normalization convention, we obtain the bigon relation
\begin{equation}
	\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)]
		\draw[{postaction=decorate}] (0,-0.5) to node [left,midway] {$a$} (0,0.5);
		\draw (0,0.5) -- (0.5,1) -- (1,0.5);
		\draw[{postaction=decorate}] (0.5,1) to node [left,midway] {$c'$} (0.5,1.5);
		\draw[{postaction=decorate}] (1,-0.5) to node [right,midway] {$b$} (1,0.5);
		\draw (1,-0.5) -- (0.5,-1) -- (0,-0.5);
		\draw[{postaction=decorate}] (0.5,-1.5) to node [left,midway] {$c$} (0.5,-1);
	\end{tikzpicture}
	=\delta_{c,c'}\sqrt{\frac{d_a d_b}{d_c}}\quad
	\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)]
		\draw[{postaction=decorate}] (0,-1.5) to node [right,midway] {$c$} (0,1.5);
	\end{tikzpicture}
	\; \label{eq:bigon_relation}
\end{equation}
and the completeness relation (resolution of the identity)
\begin{equation}
	\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)]
		\draw[{postaction=decorate}] (0,0) to node[left,midway] {$a$} (0,2);
		\draw[{postaction=decorate}] (1,0) to node[right,midway] {$b$} (1,2);
	\end{tikzpicture}\;
	= \sum_{c} \sqrt{\frac{d_c}{d_a d_b}}\;
	\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)]
		\draw[{postaction=decorate}] (-0.5,-1) to node[above left] {$a$} (0,-0.5);
		\draw[{postaction=decorate}] (0.5,-1) to node[above right] {$b$} (0,-0.5);
		\draw[{postaction=decorate}] (0,-0.5) to node[right] {$c$} (0,0.5);
		\draw[{postaction=decorate}] (0,0.5) to node[below left] {$a$} (-0.5,1);
		\draw[{postaction=decorate}] (0,0.5) to node[below right] {$b$} (0.5,1);
	\end{tikzpicture}\;.\label{eq:completeness_relation}
\end{equation}
By fixing the standard basis~\eqref{eq:standard_basis}, the $F$-symbols~\eqref{eq:F-symbols} can be represented as matrices with indices $e,f$. If these matrices are unitary, we call $\C$ a \emph{unitary} ribbon fusion category. In this case, all string diagrams satisfy mirror symmetry. That is, flipping a diagram along the horizontal axis corresponds to taking its complex conjugate with respect to the standard basis~\eqref{eq:standard_basis}\@. Therefore, for unitary $\C$, we have
\begin{equation*}
	\begin{tikzpicture}[scale=1,baseline=(current bounding box.center), decoration={markings,mark=at position .6 with {\arrow[>=stealth]{<}}},rotate=180]
		\node (u1) at (0,0) {$d$};
		\coordinate (v11) at (0,0.5);
		\coordinate (v12) at (-0.5,1);
		\node (x1) at (-1,1.5) {$c$};
		\node (y1) at (0,1.5) {$b$};
		\node (z1) at (1,1.5) {$a$};
			
		\draw[{postaction=decorate}] (u1) -- (v11);
		\draw[{postaction=decorate}] (v11) -- (z1);
		\draw[{postaction=decorate}] (v11) to node[above right] {$e$} (v12);
		\draw[{postaction=decorate}] (v12) -- (y1);
		\draw[{postaction=decorate}] (v12) -- (x1);
	\end{tikzpicture}
	=\sum_{f} \overline{\big(F_d^{abc}\big)}_{ef}
	\begin{tikzpicture}[scale=1,baseline=(current bounding box.center), decoration={markings,mark=at position .6 with {\arrow[>=stealth]{<}}},rotate=180]
		\node (u2) at (0,0) {$d$};
		\coordinate (v21) at (0,0.5);
		\coordinate (v22) at (0.5,1);
		\node (x2) at (-1,1.5) {$c$};
		\node (y2) at (0,1.5) {$b$};
		\node (z2) at (1,1.5) {$a$};
			
		\draw[{postaction=decorate}] (u2) -- (v21);
		\draw[{postaction=decorate}] (v21) -- (x2);
		\draw[{postaction=decorate}] (v21) to node[above left] {$f$} (v22);
		\draw[{postaction=decorate}] (v22) -- (y2);
		\draw[{postaction=decorate}] (v22) -- (z2);
	\end{tikzpicture}\;,
\end{equation*}
while in the general non-unitary case
\begin{equation*}
	\begin{tikzpicture}[scale=1,baseline=(current bounding box.center), decoration={markings,mark=at position .6 with {\arrow[>=stealth]{<}}},rotate=180]
		\node (u1) at (0,0) {$d$};
		\coordinate (v11) at (0,0.5);
		\coordinate (v12) at (-0.5,1);
		\node (x1) at (-1,1.5) {$c$};
		\node (y1) at (0,1.5) {$b$};
		\node (z1) at (1,1.5) {$a$};
			
		\draw[{postaction=decorate}] (u1) -- (v11);
		\draw[{postaction=decorate}] (v11) -- (z1);
		\draw[{postaction=decorate}] (v11) to node[above right] {$e$} (v12);
		\draw[{postaction=decorate}] (v12) -- (y1);
		\draw[{postaction=decorate}] (v12) -- (x1);
	\end{tikzpicture}
	=\sum_{f} \big(F_d^{abc}\big)_{ef}^\T
	\begin{tikzpicture}[scale=1,baseline=(current bounding box.center), decoration={markings,mark=at position .6 with {\arrow[>=stealth]{<}}},rotate=180]
		\node (u2) at (0,0) {$d$};
		\coordinate (v21) at (0,0.5);
		\coordinate (v22) at (0.5,1);
		\node (x2) at (-1,1.5) {$c$};
		\node (y2) at (0,1.5) {$b$};
		\node (z2) at (1,1.5) {$a$};
			
		\draw[{postaction=decorate}] (u2) -- (v21);
		\draw[{postaction=decorate}] (v21) -- (x2);
		\draw[{postaction=decorate}] (v21) to node[above left] {$f$} (v22);
		\draw[{postaction=decorate}] (v22) -- (y2);
		\draw[{postaction=decorate}] (v22) -- (z2);
	\end{tikzpicture}\;,
\end{equation*}
where the superscript $\T$ denotes the transpose with respect to the standard basis. In ribbon fusion categories, the $F$-symbols satisfy the tetrahedral symmetry relation~\cite{Turaev2017}
\begin{equation}
	\begin{aligned}
		\big(F_d^{abc}\big)_{ef} &= \big(F_{c^*}^{bad^*}\big)_{ef^*} = \big(F_{a^*}^{d^*cb}\big)_{e^*f} \\
		& = \sqrt{\frac{d_e d_f}{d_a d_c}} \big(F_{d^*}^{e^*bf^*}\big)_{a^*c^*}.
	\end{aligned}
	\label{eq:tetrahedral_symmetry}
\end{equation}
Tetrahedral symmetry is studied in detail in Ref.~\cite{Fuchs2023} and implies that~\cite[Sec.~8.1]{Wolf2020}
\begin{equation*}
	\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)]
		\draw[{postaction=decorate}] (0.5,0) to node [above] {$e$} (-0.5,0);
		\draw[{postaction=decorate}] (-1,0.5) to node [right,midway] {$a$} (-0.5,0);
		\draw[{postaction=decorate}] (-1,-0.5) to node [right,midway] {$b$} (-0.5,0);
		\draw[{postaction=decorate}] (1,0.5) to node [left,midway] {$c$} (0.5,0);
		\draw[{postaction=decorate}] (1,-0.5) to node [left,midway] {$d$} (0.5,0);
	\end{tikzpicture}
	= \sum_f \big(F_d^{b^*a^*c^*}\big)_{ef}\;
	\begin{tikzpicture}[decoration={markings,mark=at position .5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)]
		\draw[{postaction=decorate}] (0,-0.5) to node[right, midway] {$f$} (0,0.5);
		\draw[{postaction=decorate}] (-1,0.5) to node[above] {$a$} (0,0.5);
		\draw[{postaction=decorate}] (1,0.5) to node[above] {$c$} (0,0.5);
		\draw[{postaction=decorate}] (-1,-0.5) to node[below] {$b$} (0,-0.5);
		\draw[{postaction=decorate}] (1,-0.5) to node[below] {$d$} (0,-0.5);
	\end{tikzpicture}\;.
\end{equation*}
In particular, it gives sense to drawing horizontal lines in string diagrams. The name tetrahedral symmetry stems from the evaluation of a string diagram in the form of a tetrahedron by applying a sequence of $F$-symbols. This can be done in four different ways, which yield the same result if and only if Eq.~\eqref{eq:tetrahedral_symmetry} is satisfied, see Ref.~\cite[Sec.~8.1]{Wolf2020}\@. Therefore, the tetrahedral symmetry relation is the categorical analogue of the closure constraint~\eqref{eq:closure_constraint} for spin networks.
	
Due to the braiding structure in $\C$, we can define the $R$-matrices
\begin{equation}
	\begin{tikzpicture}[decoration={markings,mark=at position 0.8 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)] 
		\node (Y) at (1,0.8)[right] {$b$};
		\node (X) at (0,0.8)[left] {$a$};
		\draw[postaction={decorate}] (1,0) -- (0,1);
		\draw[overdraw=10pt,postaction={decorate}] (0,0) -- (1,1);
		\draw (0.5,-0.5) -- (1,0);
		\draw (0.5,-0.5) -- (0,0);
		\draw[postaction={decorate}] (0.5,-1) to node [left] {$c$} (0.5,-0.5);
	\end{tikzpicture}
	= R^{ab}_c
	\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center)] 
		\draw[{postaction=decorate}] (0,-1) to node [left,midway] {$c$} (0,0);
		\draw[{postaction=decorate}] (0,0) to node [below right,midway] {$b$} (0.75,0.75);
		\draw[{postaction=decorate}] (0,0) to node [below left,midway] {$a$} (-0.75,0.75);
	\end{tikzpicture}\;\label{eq:R-matrix}
\end{equation}
and their mirrored version
\begin{equation*}
	\begin{tikzpicture}[decoration={markings,mark=at position 0.8 with {\arrow[scale=1,thick,>=stealth]{<}}},baseline=(current bounding box.center),rotate=180] 
		\node (Y) at (1,0.8)[left] {$a$};
		\node (X) at (0,0.8)[right] {$b$};
		\draw[postaction={decorate}] (0,0) -- (1,1);
		\draw[overdraw=10pt,postaction={decorate}] (1,0) -- (0,1);
		\draw (0.5,-0.5) -- (1,0);
		\draw (0.5,-0.5) -- (0,0);
		\draw[postaction={decorate}] (0.5,-1) to node [left] {$c$} (0.5,-0.5);
	\end{tikzpicture}
	= \big(R^{ab}_c\big)^{-1}
	\begin{tikzpicture}[decoration={markings,mark=at position 0.5 with {\arrow[scale=1,thick,>=stealth]{>}}},baseline=(current bounding box.center),rotate=180] 
		\draw[{postaction=decorate}] (0,0) to node [right,midway] {$c$} (0,-1);
		\draw[{postaction=decorate}] (0.75,0.75) to node [above left,midway] {$a$} (0,0);
		\draw[{postaction=decorate}] (-0.75,0.75) to node [above right,midway] {$b$} (0,0);
	\end{tikzpicture}\;.
\end{equation*}
If $\C$ is unitary, $R$ will be a unitary matrix.
