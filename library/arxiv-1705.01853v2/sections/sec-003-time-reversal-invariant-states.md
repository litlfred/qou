---
doc_id: arxiv-1705.01853v2
doc_title: "Line Operators in the Standard Model"
section_id: sec-003-time-reversal-invariant-states
section_title: "Time Reversal Invariant States"
section_number: null
pages: 12-13
source_pdf: 1705.01853v2.pdf
source_sha256: 895e0b22c93bca1b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
---
It is interesting to ask: for which values of the $\theta$ angles does the theory respect time reversal invariance or, equivalently, CP? There are eight possibilities, two for each factor of the gauge group. 

\para
\underline{$\Gamma= {\bf 1}$:}\ \ All theta angles have periodicity $2\pi$. It is well known that $\theta_2,\theta_3$ and $\tilde{\theta}$ can each take values 0 or $\pi$. 

\para
\underline{$\Gamma= {\bf Z}_2$:}\ \ Here $\tilde{\theta}\in [0,8\pi)$. The values $\theta_3=0$ and $\pi$ are both time reversal invariant. We can read off the $U(2)$ $\theta$ angles from \eqn{untheta}. When $\theta_2=0$, $\tilde{\theta}=0$ or $4\pi$; when $\theta_2=\pi$ then $\tilde{\theta} = 2\pi$ or $6\pi$.

\para
\underline{$\Gamma= {\bf Z}_3$:}\ \ Here $\tilde{\theta} \in [0,18\pi)$. The values $\theta_2=0$ and $\pi$ are both time reversal invariant. The $U(3)$ theta angles can be  $\theta_3=0$ and $\tilde{\theta}  = 0$ or $9\pi$. Alternatively, we can have  $\theta_3=\pi$ and $\tilde{\theta} = 3\pi$ or $12\pi$. 

\para
\underline{$\Gamma= {\bf Z}_6$:}\ \ We have $\tilde{\theta}\in [0,72\pi)$. The time reversal invariant theories have

\begin{itemize}
\item $\theta_2=0$ and $\theta_3=0$ and $\tilde{\theta} = 0$ or $36\pi$.
\item $\theta_2=0$ and $\theta_3=\pi$ and $\tilde{\theta} = 12\pi$ or $48\pi$.
\item $\theta_2=\pi$ and $\theta_3=0$ and $\tilde{\theta} = 18\pi$ or $54\pi$.
\item $\theta_2=\pi$ and $\theta_3=\pi$ and $\tilde{\theta} =30\pi$ or $66\pi$.
\end{itemize}


\subsection{The Effect of Global Anomalies}

The chiral nature of the Standard Model means that the theta angle $\theta_2$ can be rotated away. Here we review this argument. In fact, as we will see,  a more careful statement is that a linear combination of $\theta_2$ and $\tilde{\theta}$ can be removed.

\para
In general, theta angles can be rotated away if the theory admits a  continuous global symmetry which suffers a mixed anomaly with the gauge symmetry. This arises most naturally in the presence of a massless chiral fermion. (For example, a massless up quark provides an elegant solution to the strong CP problem, albeit one that appears not to be favoured by Nature). However, even with non-vanishing Yukawa couplings, so that all fermions have a mass, the Standard Model still admits two global symmetries: these are lepton and baryon number:




\begin{center}
\begin{tabular}{c|cccccc}
 & $l_L$ &  $q_L$ & $e_R$ & $u_R$ & $d_R$ & $\nu_R$  \\ \hline
L & +1 & 0  & +1 & 0 & 0 & +1 \\
B & 0 & +$\frac{1}{3}$  & 0  &+$\frac{1}{3}$ & +$\frac{1}{3}$ & 0 \\
 \end{tabular}
 \end{center}


where, for once, we have bowed to tradition and employed the non-integer normalisation of the baryon current. 
Both $L$ and $B$ suffer mixed anomalies with both $SU(2)$ and $U(1)_{\tilde{Y}}$. They are




\be \sum L\,SU(2)^2 = \sum B\,SU(2)^2  = -1 \ \ {\rm and} \ \ \sum L\,\tilde{Y}^2 = \sum B\,\tilde{Y}^2 = +18 \nn\ee

We recover the well known fact that the combination $B-L$ is non-anomalous. Meanwhile, under a transformation of $L$, parameterised by $\alpha_L$, we have

\be L: \ \theta_2\rightarrow \theta_2-\alpha_L\ \ ,\ \ \tilde{\theta}\rightarrow \tilde{\theta} + 18\alpha_L\nn\ee

The linear combination $\tilde{\theta} + 18\theta_2$ is physical and cannot be rotated away. We will see the  interpretation of this shortly.
