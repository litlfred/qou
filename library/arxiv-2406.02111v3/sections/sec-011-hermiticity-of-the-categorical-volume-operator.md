---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-011-hermiticity-of-the-categorical-volume-operator
section_title: "Hermiticity of the categorical volume operator"
section_number: null
pages: 11-12
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.986
doc_brief: "Categorical Quantum Volume Operator — 17 sections: Categorical Quantum Volume Operato; Introduction; The Volume Operator in Loop Quantu"
---
\label{subsec:Hermicity}
For the volume operator to be a physical observable, it must be Hermitian. By looking at a specific example, we will see that for non-unitary $\C$ the volume operator is \emph{not} Hermitian in general. This is not surprising, but rather the expected behavior of generic non-unitary models. The same observation has been made, for instance, in anyon chains~\cite{Ardonne2011} and Levin--Wen string-net models~\cite{Freedman2012, Hahn2020}\@. However, we can prove that the volume operator is always Hermitian if $\C$ is unitary.
Furthermore, even in the non-unitary case, the physical volume operator $\hat{V}$ as defined in Eq.~\eqref{eq:def:vol_op} is Hermitian by construction (as $\vert\hat{Q}\vert$ is positive).
	
Let us start by first considering the non-unitary case. For this, we will look at the standard example, which is the Yang--Lee category $\YL$. $\YL$ is the Galois conjugate of the Fibonacci category, which consists of the two integer (or half-integer) spin irreducible representations of $\SU(2)_3$. While the $\SU(2)_k$ categories are specified by the deformation parameter $q=\rme^{\frac{2\pi\rmi}{k+2}}$, the Galois conjugate categories have a deformation parameter $q'=\rme^{\frac{4\pi\rmi}{k+2}}$ (see Ref.~\cite{Freedman2012} for more details). $\YL$ has two simple objects, usually denoted by $1$ and $\tau$. Their respective quantum dimensions are $d_1=1$ and $d_\tau=\phi$, where $\phi=(1+\sqrt{5})/2$ is the golden ratio. $\YL$ has the fusion rules
\begin{equation}
	1\otimes a = a = a \otimes 1, \;\forall a\in I,\quad \tau\otimes\tau = 1\oplus\tau
\end{equation}
and non-trivial $F$-symbols
\begin{equation}
	F_\tau^{\tau\tau\tau}=\begin{pmatrix}
		-\phi & \rmi\sqrt{\phi}\\
		\rmi\sqrt{\phi} & \phi
	\end{pmatrix}.
\end{equation}
The $R$-matrix reads
\begin{equation}
	R=\begin{pmatrix}
		-\rme^{-\frac{3\pi\rmi}{5}} & 0 \\
		0 & -\rme^{-\frac{4\pi\rmi}{5}}
	\end{pmatrix},
\end{equation}
where the entries of $R$ correspond to the non-trivial exchange of two $\tau$ objects fusing to either $1$ (upper left) or $\tau$ (lower right), respectively. The Casimir eigenvalues are given by a $q'$-deformation of the standard $\SU(2)$ Casimir eigenvalues. That is, we define the $q'$-deformed integer
\begin{equation}
	\qddi{n}=\frac{q'^{\frac{n}{2}}-q'^{-\frac{n}{2}}}{q'^{\frac{1}{2}}-q'^{-\frac{1}{2}}},\quad n\in\mathbb{Z}_{\geq0},
\end{equation}
such that $\alpha_\ell =\qddi{\ell(\ell+1)}$. With this data, $\YL$ only admits one non-trivial volume operator, namely if $j_1=j_2=j_3=j_4=\tau$. This is
\begin{equation}
	Q=\begin{pmatrix}
		0 & c_1\\
		c_2 & 0
	\end{pmatrix},
\end{equation}
where
\begin{align*}
	c_1 =& -\frac{(-1)^{1/5} \left(-\phi +\sqrt{\phi }+(-1)^{1/5}\right) \phi ^{3/2}}{16 \left(1+(-1)^{1/5}+(-1)^{2/5}\right)^2}\\
	\approx& -0.013514 - 0.0038170\,\rmi\\
	c_2 =& \; \frac{1}{16} (-1)^{3/5} \left(1+(-1)^{4/5}\right)^2 \phi  (2 \phi -3)\\
	&\quad \left((-1)^{1/5} \phi ^2-\sqrt{\phi }\right)\\
	\approx& \; 0.010961 - 0.011673\,\rmi,
\end{align*}
which is clearly non-Hermitian.
	
To prove Hermitianity of the volume operator for unitary fusion categories $\C$, we have to show $\tensor{Q}{_\kappa^{\kappa'}}=\overline{\tensor{Q}{_{\kappa'}^{\kappa}}}$. To this end, we compute
\begin{align}
	\overline{\tensor{Q}{_{\kappa'}^{\kappa}}}
	=& \frac{\rmi}{4} (\overline{\alpha}_{\kappa'} - \overline{\alpha}_{\kappa}) \frac{1}{\sqrt{d_{j_1} d_{j_2} d_{j_3} d_{j_4}}}\nonumber\\
	&\sum_\ell \sqrt{\frac{d_\ell}{d_{j_1}d_{j_3}}}\; \overline{\alpha}_\ell\;
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
	\end{tikzpicture}\;.
\end{align}
We note that the string diagram in $\overline{\tensor{Q}{_{\kappa'}^{\kappa}}}$ is the same as the one for $\tensor{Q}{_\kappa^{\kappa'}}$ in Eq.~\eqref{eq:Qkkb} due to the mirror symmetry for unitary $\C$, i.e.\ taking the complex conjugate of a string diagram corresponds to flipping the diagram along the horizontal axis (while not flipping the arrows). Therefore, complex conjugation of the string diagram reverses the swap of the labels $\kappa,\kappa'$ in $\overline{\tensor{Q}{_{\kappa'}^{\kappa}}}$. Furthermore, we notice that by construction, all $\alpha_\ell\in\mathbb{R}$, see Eq.~\eqref{eq:Casimir}\@. Thus, we conclude that $\tensor{Q}{_\kappa^{\kappa'}}=\overline{\tensor{Q}{_{\kappa'}^{\kappa}}}$, which implies that $\hat{Q}$ is a Hermitian matrix. The same argumentation can be followed for the volume operator $\tilde{Q}$ that involves the $j_2$--$j_3$ coupling.
