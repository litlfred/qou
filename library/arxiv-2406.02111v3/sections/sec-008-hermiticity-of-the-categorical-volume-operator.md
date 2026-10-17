---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-008-hermiticity-of-the-categorical-volume-operator
section_title: "Hermiticity of the categorical volume operator"
section_number: null
pages: 11-14
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.993
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
	
	
	

\section{Recovering the Standard $\SU(2)$ Volume Operator} \label{sec:recovery}
In this section, we show that our construction recovers the standard volume operator for $\SU(2)$, see Eq.~\eqref{eq:QRS} and Eq.~\eqref{eq:QCh}\@. For this, we consider the input category $\SU(2)_k$, which is the $q$-deformed version of $\SU(2)$ with deformation parameter $q=\rme^{\frac{2\pi\rmi}{k+2}}$. In the limit $k\rightarrow\infty$, we have $q \rightarrow 1$ and recover $\SU(2)$. The categorical data of $\SU(2)_k$ can be found in Ref.~\cite{Bonderson2007} or Ref.~\cite{Ardonne2010}\@. $\SU(2)_k$ has simple objects $I=\big\{\frac{1}{2},1,\frac{3}{2},\dots k\big\}$. With
\begin{equation}
	\qdi{n}=\frac{q^{\frac{n}{2}}-q^{-\frac{n}{2}}}{q^{\frac{1}{2}}-q^{-\frac{1}{2}}},\quad n\in\mathbb{Z}_{\geq0},
\end{equation}
being a $q$-deformed integer, we have $\alpha_\ell = \qdi{\ell(\ell+1)}$. In the limit $k\rightarrow\infty$, $\alpha_\ell\rightarrow\ell(\ell+1)$. The $R$-matrices read
\begin{align}
	R_j^{j_1 j_2} &= (-1)^{j-j_1-j_2} q^{\frac{1}{2}\big(j(j+1)-j_1(j_1+1)-j_2(j_2+1)\big)} \nonumber \\
	&\rightarrow (-1)^{j-j_1-j_2}
\end{align}
and the quantum dimensions become
\begin{equation}
	d_j = \frac{\sin\left(\frac{(2j+1)\pi}{k+2}\right)}{\sin\left(\frac{\pi}{k+2}\right)}
	\rightarrow 2j+1.
\end{equation}
In the same way, we evaluate the limit $k\rightarrow\infty$ for the $F$-symbols, which yields
\begin{align}
	\big(F_j^{j_1 j_2 j_3}\big)_{j_{12} j_{23}} \rightarrow & (-1)^{j_1+j_2+j_3+j} \sqrt{(2j_{12}+1)(2j_{23}+1)}\nonumber \\&\sixj{j_1}{j_2}{j_{12}}{j_3}{j}{j_{23}}.
\end{align}
Note that the $F$-symbols for $\SU(2)_k$ are always real for all $k$ and, in addition, all simple objects are self-dual, i.e.\ $j=j^*$ for all $j\in I$. The same properties also hold for $\SU(2)$. Since $\SU(2)_k$ is unitary, we can take the limit $k\rightarrow\infty$ of Eq.~\eqref{eq:generalized_volume_unitary}\@. This gives
\begin{align}
	\tensor{Q}{_\kappa^{\kappa'}}\rightarrow & -\frac{\rmi}{4} [\kappa(\kappa+1)-\kappa'(\kappa'+1)] (-1)^{\kappa+\kappa'} (-1)^{2(j_4-j_2)}\nonumber\\
	&(2j_4+1)(2\kappa+1)(2\kappa'+1) \sixj{\kappa'}{j_3}{j_4}{j_4}{0}{\kappa'}\nonumber\\
	&\sixj{\kappa}{j_3}{j_4}{j_4}{0}{\kappa} \sum_{m,n\in\mathcal{L}_{23}} (-1)^{m+n} (2m+1) (2n+1)\nonumber\\
	&\quad \sixj{j_1}{j_2}{\kappa'}{j_3}{j_4}{m} \sixj{j_1}{j_2}{\kappa}{j_3}{j_4}{n}\sum_{\ell\in\mathcal{L}_{13}} \ell(\ell+1)(2\ell+1)\nonumber\\
	&\qquad \sixj{j_3}{j_1}{\ell}{j_4}{j_2}{m} \sixj{j_3}{j_1}{\ell}{j_4}{j_2}{n},
\end{align}
where $\mathcal{L}_{13}=\{\vert j_1-j_3\vert,\dots,j_1+j_3\}\cap\{\vert j_2-j_4\vert,\dots,j_2+j_4\}$. Now, we use the following identity for $6j$-symbols involving a zero charge~\cite[Ch.~9]{Varshalovich1988}:
\begin{equation}
	\sixj{b}{a}{c}{c}{0}{b} = \sixj{a}{b}{c}{0}{c}{b} = \frac{(-1)^{a+b+c}}{\sqrt{(2b+1)(2c+1)}},
\end{equation}
where the first step follows from the fact that the $6j$-symbols are invariant under permutation of their columns. This leads to
\begin{align*}
	\tensor{Q}{_\kappa^{\kappa'}}\rightarrow & -\frac{\rmi}{4} [\kappa(\kappa+1)-\kappa'(\kappa'+1)] (-1)^{\kappa+\kappa'} (-1)^{2(j_3-j_2)}\\
	&\sqrt{(2\kappa+1)(2\kappa'+1)} \sum_{\ell\in\mathcal{L}_{13}} \ell(\ell+1)(2\ell+1) (-1)^{-2\ell}\\
	&\sum_{m\in\mathcal{L}_{23}} (-1)^{m+\ell+\kappa'} (2m+1) \sixj{j_3}{j_2}{m}{j_1}{j_4}{\kappa'} \sixj{j_1}{j_4}{m}{j_2}{j_3}{\ell}\\
	&\sum_{n\in\mathcal{L}_{23}} (-1)^{n+\ell+\kappa} (2n+1) \sixj{j_3}{j_2}{n}{j_1}{j_4}{\kappa} \sixj{j_1}{j_4}{n}{j_2}{j_3}{\ell},
\end{align*}
where we again used invariance under permutation of columns and also that the $6j$-symbols are invariant under simultaneous exchange of upper and lower labels in two columns. By inspection of the set $\mathcal{L}$, we notice that the factor $(-1)^{2\ell}$ can be rewritten as $(-1)^{2\ell}=(-1)^{2(j_2+j_4)}$. The next step is to use another identity of the $6j$-symbols, namely~\cite[Ch.~9]{Varshalovich1988}
\begin{equation*}
	\sum_x (-1)^{f+g+x} (2x+1) \sixj{a}{b}{x}{c}{d}{f} \sixj{c}{d}{x}{b}{a}{g} = \sixj{a}{d}{f}{b}{c}{g}.
\end{equation*}
Thus, we finally arrive at
\begin{align}
	\tensor{Q}{_\kappa^{\kappa'}}\rightarrow & -\frac{\rmi}{4} (-1)^{\kappa+\kappa'} (-1)^{2(j_3+j_4)} [\kappa(\kappa+1)-\kappa'(\kappa'+1)]\nonumber\\
	&\sqrt{(2\kappa+1)(2\kappa'+1)} \sum_{\ell\in\mathcal{L}_{13}} \ell(\ell+1)(2\ell+1)\nonumber\\
	&\sixj{j_3}{j_4}{\kappa'}{j_2}{j_1}{\ell} \sixj{j_3}{j_4}{\kappa}{j_2}{j_1}{\ell}.\label{eq:limit_j1-j3}
\end{align}
A similar calculation shows that the $j_2$--$j_3$ volume operator $\tilde{Q}$ has a limit
\begin{align}
	\tensor{\tilde{Q}}{_\kappa^{\kappa'}}\rightarrow & -\frac{\rmi}{4} (-1)^{2(\kappa+\kappa')} (-1)^{2(j_1+j_2+j_3+j_4)}\nonumber\\
	&[\kappa(\kappa+1)-\kappa'(\kappa'+1)]\sqrt{(2\kappa+1)(2\kappa'+1)}\nonumber\\
	&\sum_{\ell\in\mathcal{L}_{23}} \ell(\ell+1)(2\ell+1)\sixj{j_1}{j_2}{\kappa'}{j_3}{j_4}{\ell}
	\sixj{j_1}{j_2}{\kappa}{j_3}{j_4}{\ell}.\label{eq:limit_j2-j3}
\end{align}
Comparison with Eq.~\eqref{eq:QCh} shows that the $j_2$--$j_3$ volume operator $\tilde{Q}$~\eqref{eq:limit_j2-j3} coincides with the standard $\SU(2)$ volume operator~\eqref{eq:QCh} up to a phase factor of $(-1)^{2(\kappa+\kappa'+j_1+j_2+j_3+j_4)}$ in the limit $k\rightarrow\infty$. Likewise, the $j_1$--$j_3$ volume operator  $\hat{Q}$~\eqref{eq:limit_j1-j3} coincides with the standard $\SU(2)$ volume operator~\eqref{eq:QCh} up to a phase factor of $(-1)^{\kappa+\kappa'+2(j_3+j_4)}$ in the limit $k\rightarrow\infty$.
	
	

\section{Spectrum of the $\SU(2)_k$ Volume Operator} \label{sec:spectrum}
The volume operator is a physical observable quantifying the volume of the three-dimensional spatial component of discrete spacetime. Therefore, the main interest is its spectral properties. The spectral analysis of the $\SU(2)$ volume operator has been carried out in Refs.~\cite{Loll1996,BrunnemannThiemann2006,Meissner2006,BrunnemannRideout2008a,BrunnemannRideout2008a}\@. By restricting the possible $\SU(2)$ irreducible representation labels of each tetrahedron to a value up to $k$, we obtain a categorical volume operator with input category $\SU(2)_k$. As shown in Sec.~\ref{sec:recovery}, this volume operator coincides with the $\SU(2)$ volume operator in the limit $k\rightarrow\infty$. In this section, we study the changes in the (tetrahedron) volume's spectrum due to the deformation $k$, while keeping the $j$ labels attached to the tetrahedron faces fixed. We also study how the spectrum varies with $k$ for different values of the fixed $j$'s. To this end, we fix two irreducible representation labels $j_1=j_2$ and vary $j_3=j_4=j_\mathrm{max}$. This is analogous to the analysis carried out in Ref.~\cite{BrunnemannRideout2008a}\@. We remark that in the context of loop quantum gravity, fixing the values of the $j$ labels corresponds to fixing the areas of the tetrahedron's faces (as measured by the $q$-deformed area operator \cite{Smolinqdeformed}\@).
	
For $j_1=j_2=\frac{1}{2}$, the volume operator becomes a $2\times2$ matrix, which we diagonalize. We find that the spectrum of the standard $\SU(2)$ volume operator and the generalized $\SU(2)_k$ volume operator are close to each other already for a moderately low value of $k$, see Fig.~\ref{fig:j1/2}\@. However, if $j_\mathrm{max}$ increases, the two spectra are significantly different for small $k$. In particular, the $\SU(2)_k$ volume operator admits smaller eigenvalues than the standard $\SU(2)$ volume operator. We find the same behaviour for the case where $j_1=j_2=1$, see Fig.~\ref{fig:j1}\@. This indicates that in spacetime regions with considerably different irreducible representation labels $j_1,j_2,j_3,j_4$ but relatively small maximum $j_\mathrm{max}$, the standard $\SU(2)$ volume operator tends to overestimate the volume. This might be due to weights in the volume from non-contributing higher irreducible representations.
	
\begin{figure}
	\centering
	\includegraphics{Fig_2_Eigenvalues_half.pdf}
	\caption{Eigenvalues of the quantum volume operator $\hat{Q}$ for $\SU(2)_k$ for different $k$. We fix the input labels to $j_1=j_2=\frac{1}{2}$ and show the eigenvalues of $\hat{Q}$ for different values of $j_3=j_4=j_\text{max}$ represented by the coloured dots. In addition, we plot the corresponding eigenvalues of the $\SU(2)$ volume operator (indicated by the constant horizontal lines), which coincide with the $\SU(2)_k$ eigenvalues in the limit $k\rightarrow\infty$.}
	\label{fig:j1/2}
\end{figure}
	
\begin{figure}
	\centering
	\includegraphics{Fig_3_Eigenvalues_one.pdf}
	\caption{Eigenvalues of the quantum volume operator $\hat{Q}$ for $\SU(2)_k$ for different $k$. We fix the input labels to $j_1=j_2=1$ and show the nonzero eigenvalues of $\hat{Q}$ for different values of $j_3=j_4=j_\text{max}$ represented by the coloured dots. Except for the case where $j_\text{max}=\frac{1}{2}$, $\hat{Q}$ is a $3\times 3$ matrix and always admits an eigenvalue of zero. This behaviour is the same as for the $\SU(2)$ volume operator. The case $j_\text{max}=\frac{1}{2}$ is the same as as $j_\text{max}=1$ in Fig.~\ref{fig:j1/2}, cf.\ the orange dots and lines therein. In addition, we plot the corresponding eigenvalues of the $\SU(2)$ volume operator (indicated by the constant horizontal lines), which coincide with the $\SU(2)_k$ eigenvalues in the limit $k\rightarrow\infty$.}
	\label{fig:j1}
\end{figure}
