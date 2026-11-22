---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-037-49-parity-and-the-field-strength-tensor
section_title: "Parity and the field strength tensor"
section_number: 4.9
pages: 36-40
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
The work in this section is to appear in a joint paper, together with G. Fiore from INFN.


In Section~\ref{mh}, we introduced four-vectors, $p$,  as generalized ideals under the hermitian invariant-action, $m_h$.   These can be described as 

\begin{equation}p =  p_0 + p_1i{\epsilon_x} +p_2i{\epsilon_y} + p_3i{\epsilon_z}, 
\end{equation}

\noindent which transform under the Lorentz group as $p' = m_h(L,p) = LpL^{\dagger}$, for $L\in SL(2,\C)$.




Furthermore, in Section~\ref{mq}, we introduced the  field strength tensor, $F$, as a generalized ideal under the quaternionic invariant-action, $m_q$.  Explicitly, we had

\begin{equation}F = \left( B_1 -iE_1\right){\epsilon_x} + \left( B_2-iE_2 \right){\epsilon_y}  + \left( B_3-iE_3  \right){\epsilon_z},
\end{equation}

\noindent which transforms under the Lorentz group as $F' =m_q(L, F)=LF\widetilde{L}$.  Of course, we also studied spinors and scalars in previous sections, but these will not be relevant for us at the moment.



Given these two Lorentz representations, we might wonder how parity transformations are to be carried out.  Under a parity transformation, we would expect

\begin{equation}\begin{array}{lll}p& \hspace{2mm}\mapsto& \hspace{2mm}p' =  p_0 - p_1i{\epsilon_x} -p_2i{\epsilon_y} - p_3i{\epsilon_z}, \vspace{6mm}\\
F&  \hspace{2mm}\mapsto\hspace{2mm}& F' = \left( B_1 +iE_1\right){\epsilon_x} + \left( B_2+iE_2 \right){\epsilon_y}  + \left( B_3+iE_3  \right){\epsilon_z}.
\end{array}
\end{equation}



Now, it might be tempting to consider the quaternionic conjugate as the parity conjugate, since $\widetilde{\epsilon_x} = -\epsilon_x$, $\widetilde{\epsilon_y} = -\epsilon_y$, and $\widetilde{\epsilon_z} = -\epsilon_z$.  However, the quaternionic conjugate sends $F\mapsto -F$, which does not give the desired result:  $E_i\mapsto-E_i$, and $B_j\mapsto B_j$.  So how might we define a parity transformation?







In Section~\ref{da}, we demonstrated a representation of the Dirac algebra, $\C\otimes Cl(1,3)$, using both left and right multiplication of $\CH$ on itself.  From this Clifford algebra, it is then possible to define a parity transformation:

\begin{equation}\label{parity} \gamma^0\hspace{2mm}\mapsto\hspace{2mm}\gamma^0 = 1\hspace{1mm}|\hspace{1mm}i\epsilon_x,\hspace{1cm} \gamma^j\hspace{2mm}\mapsto\hspace{2mm}-\gamma^j = -i\epsilon_j \hspace{1mm}| \hspace{1mm}\epsilon_y,
\end{equation}

\noindent for $j = 1,2,3.$  



So, the question is now:  how do we use this parity transformation on the $\gamma^{\mu}$ to induce a parity transformation on $p$ and $F$?  


The resolution to this question is not obvious, because $p$ and $F$ are objects which are derived from $\CH\simeq\CLtwo$ structure, while the $\gamma^{\mu}$ belong in $\left(\CH\right)\otimes_{\C}\left(\CH\right)\simeq\C\otimes Cl(1,3) \simeq \CLfour$.  One solution, which we will now show, is to generalize the $\CLtwo$ objects, $p$ and $F$, to two new $\CLfour$ operators, $\hat{p}$ and $\hat{F}$.  We might hope, then, that under the right conditions, $\hat{p}$ and $\hat{F}$ would reduce to $p$ and $F$.   In summary, we would like to see the parity transformations on $\hat{p}$ and $\hat{F}$, given by equation~\ref{parity}, automatically induce parity transformations on $p$ and $F$.


Let us then define $\hat{p}$ to be

\begin{equation}\hat{p} \equiv p_{\mu} \gamma^{\mu} = p_0 \hspace{1mm}1\hspace{1mm}|\hspace{1mm}i\epsilon_x + p_j\hspace{1mm} i\epsilon_j \hspace{1mm}| \hspace{1mm}\epsilon_y, 
\end{equation}

\noindent for $p_{\mu}\in\R$, for $\mu = 0,1, 2, 3$, and $j=1,2,3.$ This is none other than the usual $p_{\mu} \gamma^{\mu}$ of quantum field theory.



Making use of  the Clifford algebraic description of~\cite{loun}, let us define $\hat{F}$ to be 

\begin{equation} \hat{F} \equiv F_{\mu\nu}\gamma^{\mu\nu}  = F_{0i}\gamma^{0i} + F_{jk}\gamma^{jk} = E_i\hspace{1mm}\epsilon_{i} \hspace{1mm}|\hspace{1mm} \epsilon_z - B_j\hspace{1mm} \epsilon_j\hspace{1mm}|\hspace{1mm}1,
\end{equation}

\noindent for $\mu, \nu = 0,1, 2, 3$, $F_{\mu\nu}\in \R$,  $\gamma^{\mu\nu}\equiv \frac{1}{2}\left[\gamma^{\mu}, \gamma^{\nu}\right]$, and $i, j = 1,2,3$.



It is then trivial to see that under a parity transformation given by 

\begin{equation} \gamma^0\hspace{2mm}\mapsto\hspace{2mm}\gamma^0 = 1\hspace{1mm}|\hspace{1mm}i\epsilon_x,\hspace{1cm} \gamma^j\hspace{2mm}\mapsto\hspace{2mm}-\gamma^j = -i\epsilon_j \hspace{1mm}| \hspace{1mm}\epsilon_y,
\end{equation}

\noindent for $j = 1,2,3,$ the operator, $\hat{p}$ transforms as 

\begin{equation}\hat{p}\hspace{2mm}\mapsto\hspace{2mm} \hat{p}' = p_0 \hspace{1mm}1\hspace{1mm}|\hspace{1mm}i\epsilon_x - p_j\hspace{1mm} i\epsilon_j \hspace{1mm}| \hspace{1mm}\epsilon_y,
\end{equation}

\noindent and the operator, $\hat{F}$ transforms as

\begin{equation} \hat{F}\hspace{2mm}\mapsto\hspace{2mm} \hat{F}' = -E_i\hspace{1mm}\epsilon_{i} \hspace{1mm}|\hspace{1mm} \epsilon_z - B_j\hspace{1mm} \epsilon_j\hspace{1mm}|\hspace{1mm}1,
\end{equation}

\noindent as we would expect.

So, we  have a new description for four-momenta, $\hat{p}$, and the field strength tensor, $\hat{F}$, which transform as they should under parity.  We would now like to know how these relate to the generalized ideals, $p$ and $F$ that we found earlier in Sections~\ref{mh} and \ref{mq}.  



We find that the operators $\hat{p}$ and $\hat{F}$ reduce to the generalized ideals $p$ and $F$, when $\hat{p}$ and $\hat{F}$ are taken to be operators, \it acting on spinors \rm in $\CH$.  Incorporating the object $\gamma^0$, we find that $\hat{p}$ reduces to $p$, or $p^*$, on Weyl spinors,

\begin{equation} \gamma^0 \hat{p} \hspace{1mm}\Psi_{\textup{L}} = p^*\hspace{1mm}\Psi_{\textup{L}}, \hspace{1cm}  \gamma^0 \hat{p} \hspace{1mm}\Psi_{\textup{R}} = p\hspace{1mm}\Psi_{\textup{R}}.
\end{equation}






\noindent Similarly, we find that $\hat{F}$ reduces to $F$, or $F^*$, on Weyl spinors as

\begin{equation}\hat{F}\hspace{1mm}\Psi_{\textup{L}} =-F^*\hspace{1mm}\Psi_{\textup{L}}, \hspace{1cm} \hat{F}\hspace{1mm}\Psi_{\textup{R}} =-F\hspace{1mm}\Psi_{\textup{R}}.
\end{equation}

\noindent Readers may note that a parity transformation on $\hat{p}$ and $\hat{F}$ now automatically induces the correct parity transformation on $p$ and $F$, when these objects are taken to be operators on spinors.


Finally, we point out that this definition of parity, 

\begin{equation} \gamma^0\hspace{2mm}\mapsto\hspace{2mm}\gamma^0 = 1\hspace{1mm}|\hspace{1mm}i\epsilon_x,\hspace{1cm} \gamma^j\hspace{2mm}\mapsto\hspace{2mm}-\gamma^j = -i\epsilon_j \hspace{1mm}| \hspace{1mm}\epsilon_y,
\end{equation}

\noindent sends $\gamma^5 \mapsto -\gamma^5$, so that left- and right-handed Weyl spinors are swapped under this transformation, as we would expect.

\medskip

In summary, we have shown that the parity conjugate of the  $\C\otimes Cl(1,3) \simeq \left(\CH\right)\otimes_{\C}\left(\CH\right)$ algebra may be used to induce a parity conjugate on our  generalized ideals in $\CH$.   

Note that we have also demonstrated a way to write down four-vectors, and the field strength tensor, in the Dirac algebra formalism, which makes use of the generalized ideals found in Sections~\ref{mh} and \ref{mq}.  Namely, 

\begin{equation}\hat{p}\hspace{1mm} \Psi_{\textup{D}} =  \gamma^0\hspace{1mm} m_c(p^*, \Psi_{\textup{D}}), \hspace{1cm} \hat{F}\hspace{1mm}\Psi_{\textup{D}} = m_c(-F^*, \Psi_{\textup{D}}).
\end{equation}






\chapter{Standard model of particle physics\label{SM}  }
