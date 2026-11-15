---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-013-spectrum-of-the-su2k-volume-operator
section_title: "Spectrum of the SU(2)k Volume Operator"
section_number: null
pages: 13-14
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.984
doc_brief: "Categorical Quantum Volume Operator — 17 sections: Categorical Quantum Volume Operato; Introduction; The Volume Operator in Loop Quantu"
---
\label{sec:spectrum}
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
