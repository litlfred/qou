---
doc_id: arxiv-1705.01853v2
doc_title: "Line operators in the Standard Model"
section_id: sec-010-31-theta-angles
section_title: "Theta Angles"
section_number: 3.1
pages: 11-13
source_pdf: 1705.01853v2.pdf
source_sha256: 895e0b22c93bca1b
doc_brief: "Line operators in the Standard Model — There is an ambiguity in the gauge group of the Standard Model."
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 1.0
---
We can now ask how the spectrum of line operators changes as we vary the $\theta$-angles. A priori, there are three such angles, one for each factor of the gauge group. We call these $\theta_{\tilde{Y}}$, $\theta_2$ and $\theta_3$. Within the framework discussed in this paper it makes sense to ask how the line operators vary under each of these. 

\para
Before we proceed, it is worth reviewing the role of theta angles in the Standard Model.  The most discussed is the QCD theta angle, $\theta_3$. Bounds on strong CP violation restrict $\theta_3\lesssim 10^{-10}$. (The value $\theta_3=\pi$ also preserves CP but the meson spectrum derived from the chiral Lagrangian differs from the observed values \cite{baluni,crewther}.)


\para
It is usually stated that the  weak theta angle, $\theta_2$, can be rotated away in the  Standard Model . This follows from the existence of an anomalous global symmetry $B+L \rightarrow {\bf Z}_{N_f}$ where $N_f=3$ is the number of generations. 

We will revisit this below. 

\para
Finally, there is very little, if any, discussion of the theta angle for hypercharge $\theta_{\tilde{Y}}$. This changes neither the spectrum nor correlation functions of local operators. Nonetheless, it can play a role in the presence of magnetic monopoles or boundaries of space.  Correspondingly, it also changes the spectrum of line operators.


\para
Here we start by ignoring the effects of global anomalies and focus on the spectrum of line operators and the Witten effect. 
As reviewed in Section \ref{reviewsec}, for simple gauge groups, a quotient by the centre has the effect of extending the range of $\theta$. In the present context, the quotient $\Gamma = {\bf Z}_p$ extends the range of the Abelian theta angle only\footnote{For the hypercharge with normalisation $Y=\tilde{Y}/6$, the range is $36 \theta_Y\in [0,2\pi  p^2)$, so $\theta_Y\in [0,2\pi)$ when $\Gamma={\bf Z}_6$.}. We have

\be \theta_2,\theta_3\in [0,2\pi)\ \ \ {\rm and}\ \ \ \theta_{\tilde{Y}} \in [0,2\pi p^2)\label{thetarange}\ee

This is simplest to see for the case of ${\bf Z}_2$ and ${\bf Z}_3$ where the gauge group is   $G=U(2)\times SU(3)$ and $G=SU(2)\times U(3)$ respectively. Here

\be U(N) = \frac{U(1)\times SU(N)}{{\bf Z}_N}\nn\ee

We denote the $U(1)$ gauge field as $\tilde{a}$, the $SU(N)$ gauge field as $a$ and their corresponding field strengths as $\tilde{f}$ and $f$. The theta terms for the $U(1)\times SU(N)$ theory are

\be S_\theta =  \frac{\theta_N}{16\pi^2}\int\ {\rm tr}\, (f\, {}^\star\!f)  + \frac{\tilde{\theta}}{16\pi^2}\int \  \tilde{f}\, {}^\star\!{\tilde f} \nn\ee

To describe the $U(N)$ theory, we introduce the canonically normalised gauge field

\be b = a + \tilde{a}{\bf 1}_N\nn\ee

with corresponding field strength $g$. The theta terms can then be written as

\be S_\theta = \frac{\theta_N}{16\pi^2}\int \ {\rm tr}\, (g\,{}^\star\!g)  + \frac{\tilde{\theta} - N\theta_N}{16\pi^2 N^2}\int \ ({\rm tr}\, g)\, {}^\star({\rm tr}\, g)\label{untheta}\ee

We see that $\theta_N\in [0,2\pi)$ while $\tilde{\theta}\in [0,2\pi N^2)$. 

\para
Similarly, for the ${\bf Z}_6$ quotient, one can check that the spectrum of line operators is invariant under the identification \eqn{thetarange}, with $\tilde{\theta} \in [0,72\pi)$.

\para
(Some examples with the ${\bf Z}_6$ quotient: the theory with $\theta_2=0$, $\theta_3=2\pi$ and Abelian theta angle $\tilde{\theta}$ has the same spectrum of line operators as the theory with $\theta_2=\theta_3=0$ and Abelian theta angle $\tilde{\theta}'=\tilde{\theta} + 48\pi$; the theory with $\theta_2=2\pi$, $\theta_3=0$ and Abelian theta angle $\tilde{\theta}$ has the same spectrum of line operators as the theory with $\theta_2=\theta_3=0$ and Abelian theta angle $\tilde{\theta}'=\tilde{\theta} + 36\pi$.)


\subsection{Time Reversal Invariant States}


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
