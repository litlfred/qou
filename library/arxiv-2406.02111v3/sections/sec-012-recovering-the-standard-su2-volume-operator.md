---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-012-recovering-the-standard-su2-volume-operator
section_title: "Recovering the Standard SU(2) Volume Operator"
section_number: null
pages: 12-13
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.889
doc_brief: "Categorical Quantum Volume Operator — 17 sections: Categorical Quantum Volume Operato; Introduction; The Volume Operator in Loop Quantu"
---
\label{sec:recovery}
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
