---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-010-32-action-of-a-charged-black-hole
section_title: "Action of a charged black hole"
section_number: 3.2
pages: 19-21
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.987
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Adding electrical charge to an AdS black hole changes how the Wheeler-DeWitt patch terminates. Rather than terminating when the ingoing lights heets run into the singularity at $r=0$, it now terminates when the light sheets run into each other at $t=0$ (for $t_L = t_R$). Nevertheless, we can use much the same reasoning as before to find the late-time growth of the enclosed  action.

The entire WDW patch lies outside of the inner horizon at $r_-$. This is reassuring because it means the action is not sensitive to quantum instabilities of the inner horizon, so long as the horizon remains null. (We will not consider classical instabilities, which can lead to large changes in the structure of the inner horizon.)

As with the uncharged case, the action of that part of the patch that lies outside the outer horizon is independent of time, and the action of that part of the patch that lies behind the past horizon shrinks exponentially to zero at late times. The late-time rate of change of action comes from the part of the patch behind the future horizon, which is shown in Fig.~\ref{fig-incrementalcharged}.

\begin{figure}[h] 
   \centering
   \includegraphics[width=6in]{fig-incrementalcharged.pdf}
   \caption{A charged AdS black hole. When $t_L$ increases, the Wheeler-DeWitt patch gains a slice (in blue) and loses a slice (in red). It is useful to consider separately the pieces above and below $r = r_\textrm{meet}(t_L,t_R)$. }
   \label{fig-incrementalcharged}
\end{figure}

The contribution from $B$ will cancel that from $B'$, the corners at $AB$ and $AB'$ will cancel, and the corners at $BC$ and $B'C$ will cancel. The contribution from $D$ is of order $\delta^2$ (since the size of the two-sphere is stationary at $D$, we are able to use the two-dimensional Gauss-Bonnet theorem there), and therefore does not contribute.  This leaves $A, C$, and the bulk term.

For simplicity we will work in $(3+1)$ dimensions where the  electromagnetic energy-momentum tensor is traceless. The electric field strength is
\begin{equation}
F_{r t} = - F_{t r}  = \frac{Q}{r^2} ,
\end{equation}
so  the Einstein-Hilbert-Maxwell (EHM) contribution to the on-shell action (Eq.~\ref{eq:EinsteinHilbertActionForRealz}) is


\begin{equation}
\frac{\CA_\textrm{EHM}}{dt_L}

=  \frac{r_+ - r_-}{2} \left( \frac{Q^2 }{r_+ r_-} - \frac{r_-^2 + r_+ r_- + r_+^2}{G \lads^2} \right) \label{eq:bulkchargedaction} .
\end{equation}
\noindent The York-Gibbons-Hawking surface actions at $A$ (at $r=r_+$) and at $C$ (at $r=r_-$) are
\begin{equation}
\frac{d\CA_{\partial \mathcal{M}}}{dt_L} =    \left[ -  \frac{3 M}{2} +  \frac{Q^2 }{2r}   + \frac{r }{G}  + \frac{3}{2G}  \frac{r^3}{\lads^2} \right]^{r_+}_{r-} . \label{eq:chargedAboundary}
 \end{equation}
 In total, the rate of change of action is (using that $f(r_+) = f(r_-) = 0$)
 \begin{equation}
\boxed{\frac{d\CA}{d t_L } =  \frac{r_+ - r_-}{G} \left( 1 + \frac{ r_-^2 + r_-  r_+ + r_+^2}{\lads^2 }   \right)  = \frac{Q^2 }{r_-} - \frac{Q^2 }{r_+}    . } \label{eq:chargedactionincrement}
 \end{equation}
Reassuringly, the total action reduces to the uncharged result Eq.~\ref{eq:unchargedactionincrement} when $Q \rightarrow 0$ (though how this total breaks up into bulk and boundary contributions differs).


 
\subsubsection{Near-extremal black holes}

 As extremality is approached, the complexification rate slows to a halt. The precise coefficient depends on the size of the black hole compared to the AdS length.



For very small  $(3+1)$-dimensional  charged black holes, extremality occurs at $M_\textrm{Q} = Q/\sqrt{G}$. The rate of change of action, whether near or far from extremality, is
\begin{equation}
\boxed{\frac{d \CA}{dt_L} \bigg|_{r_+ \ll \lads}  = 2 \sqrt{M^2 - Q^2/G} .}

\label{small-action}
\end{equation}

For very large  $(3+1)$-dimensional  charged black holes, extremality occurs at {$M_Q =\frac{2}{3} \left(\frac{G}{3} \right)^{-\frac{1}{4}  }\sqrt{ \frac{Q^3}{\lads}}$}. Near extremality
\begin{equation}
\boxed{\frac{d \CA}{dt_L}  \bigg|_{r_+ \gg \lads} = \sqrt{6} \sqrt{M_Q (M - M_Q)} \left( 1+ O\left( \frac{M - M_Q}{M_Q} \right) \right) .}
\label{3.15}
\end{equation}
