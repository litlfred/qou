---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-009-34-higher-order-spectral-correlations
section_title: "Higher Order Spectral Correlations"
section_number: 3.4
pages: 7-8
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 1.0
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec34}

The wealth of data allows us to go beyond a previous
analysis~\cite{halasz97} of higher moments of the eigenvalue
partition,
\begin{equation}
\mu_k(L)=\overline{\langle(L-n_{\alpha}(L))^k\rangle}\;.
\label{moments}
\end{equation}
We notice that $\mu_2(L)=\Sigma^2(L)$. The skewness and the excess
\cite{Mehta} are defined by
\begin{equation}
\gamma_1(L)=\mu_3(L)\mu_2(L)^{-3/2}
\label{skew}
\end{equation}
and
\begin{equation}
\gamma_2(L)=\mu_4(L)\mu_2(L)^{-2}-3 \ ,
\label{excess}
\end{equation}
respectively.  The comparison of RMT predictions with lattice data for
these both quantities in Fig.~\ref{agree2} again shows very good
agreement.

The measures $\gamma_1(L)$ and $\gamma_2(L)$ only contain a small
amount of information of the spectral correlations. Moreover,
$\gamma_1(L)$ and $\gamma_2(L)$ also involve lower order correlations:
$\gamma_1$ is a combination of the two-- and the three--point
correlator, $Y_2(r)$ and $Y_3(r_1,r_2)$, and $\gamma_2$ involves in
addition the four--point correlator $Y_4(r_1,r_2,r_3)$. The
representation of the moments in terms of integrals over the
correlators reads
\begin{equation}
\mu_3(L) =
L-6\int_{0}^{L}(L-r)Y_2(r)dr-6\int_{0}^{L}dr_1\int_{0}^{L-r_1}dr_2
(L-r_1-r_2)Y_3(r_1,r_2)
\label{mu3}
\end{equation}
and
\begin{eqnarray}
  \mu_4(L) & = & L-(14-12L)\int_{0}^{L}(L-r)Y_2(r)dr + 12 \left[
  \int_{0}^{L}(L-r)Y_2(r)dr \right]^{2} \nonumber \\ & + & 36
  \int_{0}^{L}dr_1\int_{0}^{L-r_1}dr_2(L-r_1-r_2)Y_3(r_1,r_2)
  \nonumber \\ & - &
  24\int_{0}^{L}dr_1\int_{0}^{L-r_1}dr_2\int_0^{L-r_1-r_2}
  dr_3(L-r_1-r_2-r_3)Y_4(r_1,r_2,r_3)\;.  \nonumber\\
\label{mu4}
\end{eqnarray}
Obviously, by analyzing $\gamma_1(L)$ and $\gamma_2(L)$, one cannot
easily estimate to what extent the three-- and the four--point
correlators themselves obtained from the lattice calculations follow
the predictions of RMT.

Here, the three-- and the four--point cluster functions,
$Y_3(r_1,r_2)$ and $Y_4(r_1,r_2,r_3)$ are written as functions of the
arguments $r_i$ ($i=1,2,3$) which are defined terms of the original
arguments $\xi_i$ ($i=1,2,3,4$) by
\begin{equation}
  r_1=\xi_2-\xi_1, \ \ r_2=\xi_3-\xi_2, \ \ r_3=\xi_4-\xi_3.
\label{arg1}
\end{equation}
We constructed from the data the two--point and the three--point
correlation functions $X_2(s)$ and $X_3(s_1,s_2)$ and the
corresponding cluster functions $Y_2(s)$ and $Y_3(s_1,s_2)$. Here, for
convenience, we redefined the arguments for the three--point
correlators as follows:
\begin{equation}
s_1=\xi_2-\xi_1=r_1, \ \ \ s_2=\xi_3-\xi_1=r_1+r_2.
\end{equation}
The results for $X_3(s_1,s_2)$ and $Y_3(s_1,s_2)$ are plotted with
error bars in Fig.~\ref{twfig2} for some given values of $s_1$.  The
results do not depend on unfolding.  In the construction of these
correlators, we first performed a spectral average by using the
translational invariance due to unfolding, and then averaged over the
ensemble. The errors for $X_3(s_1,s_2)$ and $Y_3(s_1,s_2)$ were
estimated as the variance of the ensemble fluctuations.  Once more,
very good agreement with the RMT predictions for $X_3(s_1,s_2)$ is
found, apart from a small systematic deviation which we believe can be
understood as follows. {}From the relation between $X_3(s_1,s_2)$ and
$X_2(s)$
\begin{equation}
X_3(s_1,s_2)=Y_3(s_1,s_2)-2+X_2(s_1)+X_2(s_2)+X_2(s_1-s_2),
\end{equation}
one has
\begin{equation}
X_3(s_1,s_2)|_{s_2\to \infty} = X_2(s_1).
\end{equation}
Therefore, even a small point--deviation of the two--point correlator
at $s_1$ from the theoretical predictions can result in a systematic
deviation of the whole curve $X_3(s_1,s_2)$ versus $s_2$ for this
given $s_1$.  For $Y_3(s_1,s_2)$, the quality of the agreement with
RMT is only slightly reduced, but still remarkable.  In addition to
the systematic deviation, one can see some random fluctuations around
the theoretical curves.  This is because $Y_3(s_1,s_2)$ is the
disconnected correlator, and it should represent the true three--point
correlation, while $X_3(s_1,s_2)$ also contains the two-- and
one--point functions. They play a dominate role and are in good
agreement with the corresponding GSE predictions. We notice that this
analysis was only possible due to the extremely higher number of
levels available.
