---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-014-42-local-limit-theorem
section_title: "Local limit theorem"
section_number: 4.2
pages: 30-32
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.914
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
Combining Proposition \ref{prop:sizefourier} with Theorem 5 in \cite{DKN11} on local limit theorems for mod-$\phi$ convergence, we obtain the following local limit theorem for the magnetization in the Curie-Weiss model:

\begin{theorem}
In the Curie-Weiss model, if we note $M_n$ for the total magnetization, then we have:
$$\lim_{n\to\infty} n^{1/2}\, \proba[n^{-1/4} M_n\in B]=\frac{2}{12^{1/4} \Gamma(\frac{1}{4})}\, m(B),$$
for relatively compact sets $B$ with $m(\partial B)=0$, $m$ denoting the Lebesgue measure.
\end{theorem}

\begin{proof}
With the notation of \S\ref{subsec:speedofconv}, $Y_n=n^{-1/4} M_n$ and we need to check assumptions \textbf{H1}, \textbf{H2} and \textbf{H3} of \cite{DKN11} for $(Y_n)_{n\in \N}$ in order to apply Theorem 5 in \emph{loc. cit.} 
\begin{itemize}
	\item[$\bullet$ \textbf{H1.}] The Fourier transform of the limit law $\mu(dx)=\frac{\psi(x)\,dx}{I_\infty}$ of $\frac{Y_n}{n^{1/2}}$ is in the Schwartz space, hence is integrable.\vspace{2mm}
	\item[$\bullet$ \textbf{H2.}] The Fourier transforms $\frac{\widehat{\psi_n}(\xi)}{I_n}\,\E^{\frac{\xi^2}{2n^{1/2}}}$ of $\frac{Y_n}{n^{1/2}}$ converge locally uniformly in $\xi$ towards the Fourier transform $\frac{\widehat{\psi}(\xi)}{I_\infty}$. Indeed, by Theorem \ref{thm:ellnew}, $$\frac{\psi_n(x)}{I_n}\to_{\mathrm{L}^1(\R)}\frac{\psi(x)}{I_\infty},$$
	 so $\frac{\widehat{\psi_n}(\xi)}{I_n} \to \frac{\widehat{\psi}(\xi)}{I_\infty}$, and the term $\E^{\frac{\xi^2}{2n^{1/2}}}$ converges locally uniformly to $1$.\vspace{2mm}
	\item[$\bullet$ \textbf{H3.}] Finally, we have to prove that for all $k\geq0$, 
	$$f_{n,k}(\xi)=\esper\left[\E^{\I \xi \frac{Y_n}{n^{1/2}}}\right] \,1_{|\xi|\leq k n^{1/2}}$$ is uniformly integrable. Following Remark 2 in \cite{DKN11}, it is enough to show that 
	$$\left|\esper\left[\E^{\I \xi \frac{Y_n}{n^{1/2}}}\right]\right|\leq h(\xi)$$
	 for $\xi$ such that $|\xi|\leq k n^{1/2}$ for some non-negative and integrable function $h$ on $\R$. This is a consequence of Proposition \ref{prop:sizefourier}: since $|\widehat{\psi_n}(\xi)|\leq C(k)\,\E^{-k|\xi|}$ for any $k>0$, one can write
	 \begin{align*}
	 \left|\esper\left[\E^{\I \xi \frac{Y_n}{n^{1/2}}}\right]\right|&=\frac{|\widehat{\psi_n}(\xi)|}{I_n}\,\E^{\frac{\xi^2}{2n^{1/2}}} \\
	 &\leq \frac{C(k)}{I_\infty} \,\E^{-k|\xi|+\frac{\xi^2}{2n^{1/2}}} \\
	 &\leq \frac{C(k)}{I_\infty} \,\E^{-\frac{k}{2}\,|\xi|}
	 \end{align*}
	 for any $|\xi|<k\,n^{1/2}$. We can hence apply Theorem 5 of \cite{DKN11} with $\frac{d\mu}{dm}(0)=1/I_{\infty}$,and the value of $I_{\infty}$ was computed in the proof of Lemma \ref{lem:tao}.
\end{itemize}
\end{proof}

\begin{remark}
A similar result would more generally hold for $Y_n$ whenever one has some estimates of exponential decay on $\widehat{\psi_n}(\xi)$ similar to the one given in Lemma \ref{prop:sizefourier}:
$$\lim_{n\to\infty} t_n \,\proba[Y_n\in B]=\frac{1}{I_\infty}\,  m(B).$$
In particular, the result holds for the random walks changed in measure studied in \S\ref{subsec:randomwalkchange}.
\end{remark}

\begin{remark}
The idea behind the proof the local limit theorem above and which is found in \cite{DKN11} is the following: thanks to approximation arguments, one can show that it is enough to prove the local limit theorem for functions whose Fourier transforms have compact support (instead of indicator functions $1_B$). Then, one uses Parseval's relation for such functions $f$ to write:
$$\esper[f(Y_n)]=\frac{1}{2\pi}\int_\R \frac{\widehat{\psi_n}(\xi)}{I_n}\, \E^{\frac{\xi^2}{2t_n}} \widehat{f}\left(-\frac{\xi}{t_n}\right)\, d\xi $$
and then use the assumptions to conclude.
\end{remark}
\bigskip
\bigskip
