---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-009-31-action-of-an-uncharged-black-hole
section_title: "Action of an uncharged black hole"
section_number: 3.1
pages: 16-19
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.996
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:actionuncharged}

 Fig.~\ref{fig-incrementaluncharged} shows the Wheeler-DeWitt patch bounded by $t_L$ on the left and $t_R$ on the right for an uncharged ($Q=0$) black hole. As time passes on the left boundary, the patch grows in some places (shown in blue) and shrinks in others (shown in red).

The total volume (and total action) of the patch outside the horizon is infinite but independent of time, due to the time-translation symmetry outside the hole.
\begin{figure}[h] 
   \centering
   \includegraphics[width=5in]{fig-incrementaluncharged.pdf}
   \caption{An uncharged AdS black hole. When $t_L$ increases, the Wheeler-DeWitt patch gains a slice (in blue) and loses a slice (in red).}
   \label{fig-incrementaluncharged}
\end{figure}

The region behind the past horizon contributes at early times, but at late times ($t_L + t_R \gg \beta$) shrinks exponentially to zero. At late times, the size of the $D-2$-sphere is constant up to terms that are exponentially small in time. Consequently, we can use the two-dimensional Gauss-Bonnet theorem \cite{GaussBonnet} on the remaining two dimensions to say that the contribution of the wedge behind the past horizon is topological and must be independent of time at late times.\footnote{It should be pointed out that while the rate of change of action from the region behind the past horizon is exponentially small in time, that exponential could in principle be multiplied by a UV-divergent quantity. We address this unresolved subtlety in \S\ref{sec:corner} and in \cite{ToAppear}. Note that  it is not always the  case that an arbitrarily small region has arbitrarily small action. A simple illustration of this is provided by a two-sphere, whose action is topological and finite even as the sphere becomes arbitrarily small. We thank Henry Maxfield for discussion.}  At late times, the whole contribution comes from the part of the blue slice that lives inside the future horizon.


This region is shown on the right hand side of Fig.~\ref{fig-incrementaluncharged}. The boundary contribution at the light sheet $B'$ replaces the old contribution at $B$; since $B'$ and $B$ are related by the time-translation symmetry, this change does not affect the total action. Similarly the added corner contribution from $AB'$ cancels the removed corner contribution from $AB$,  and $B'C$ cancels $BC$. This leaves the surface contributions from $A$ (at $r=r_h$) and from $C$ (at $r=0$), as well as the bulk contribution.

Using the expression for the action in Eq.~\ref{eq:EinsteinHilbertActionForRealz}, and using Einstein's equation $\mathcal{R}_{\mu \nu} - \frac{1}{2} \mathcal{R} g_{\mu \nu} + \Lambda g_{\mu \nu} = 8 \pi G T_{\mu \nu}$ implies that
\begin{equation}
\Lambda = -\frac{(D-1)(D-2)}{2 \lads^2} \ \  \textrm{ and } \ \  \mathcal{R} = \frac{2D}{D-2} \Lambda, \label{eq:LambdaAndR}
 \end{equation}
so the EH contribution to the action is proportional to the spacetime volume
\begin{equation}
\frac{d\CA_\textrm{EH}}{dt_L}  
= -\frac{\Omega_{D-2} r_h^{D-1}}{8 \pi G \lads^2} . \label{eq:bulkunchargedcausalpatch}
 \end{equation}
The integral extends right down to the singularity, but receives only a small contribution from the immediate vicinity of $r=0$.

To calculate the YGH surface term we will use that the trace of the extrinsic curvature of a constant-$r$  surface is
\begin{equation}
K =  \frac{1}{2} n^r  \frac{\partial_r \left(   r^{2(D-2)  } f \right)  }{ r^{2(D-2) }f},
\label{eq:K}
\end{equation}
so the YGH contributions to the action at $A$ (at $r = r_h$)
and  $C$ (at $r=0$) are
\begin{equation}
\frac{d\CA_{\partial \mathcal{M}}}{dt_L} =  \left[  - \bigg( \frac{D-1 }{D-2}\bigg) M   + \frac{\Omega_{D-2} r^{D-3} }{8 \pi G}  \left( (D - 2 ) + (D-1) \frac{r^2}{\lads^2} \right) \right]^{r_h}_0 . \label{eq:rsunchargedboundary}
 \end{equation}

 The individual rates of change Eq.~\ref{eq:bulkunchargedcausalpatch} and Eq.~\ref{eq:rsunchargedboundary} are simple expressions in terms of the black hole mass, but combining them (using that $f(r_h) = 0$) we find the remarkably simple result,
  \begin{equation}
\boxed{\frac{d \CA}{dt_L} = 2M.} \label{eq:unchargedactionincrement}
 \end{equation}

Note that this result applies to all uncharged nonrotating  AdS black holes in any number of dimensions, whether small, intermediate, or large compared to the AdS length.\footnote{We have performed a completely classical calculation, with $\hbar = 0$. Quantum mechanics can destabilize sufficiently small black holes. In the canonical ensemble, large and intermediate black holes ($r_h \, \gsim \, \lads$) are stable. In the microcanonical ensemble, even much smaller black holes may be stable.}


\subsubsection{Ambiguities avoided}
The action of a WDW patch is infinite because of the usual divergences near the AdS boundary. One also expects a matching divergence in the complexity  because of the large number of  UV degrees of freedom in the CFT dual. These divergences can cause ambiguities and nonuniversal behavior. Fortunately they do not contribute to the rates we have calculated. For example, in Fig.~\ref{divergences}  we have divided the WDW patch into four quadrants.
\begin{figure}
\centering
\includegraphics[width=.45\textwidth]{fig-divergences.pdf}

\caption{The WDW patch divided into quadrants. In quadrants III and IV the WDW patch intersects the AdS boundary and causes a divergence in the action.}
\label{divergences}
\end{figure}
Two of the quadrants, III and IV,  reach the AdS boundary, and one can expect the action of these subregions to diverge.  The boost symmetry of the TFD state means that the contributions from III and IV are time independent and therefore do not contribute to the rate of change of complexity.

We mention this because a more ambitious calculation may attempt to estimate the complexity of formation of the  TFD state. We hope to come back to this \cite{ToAppear}, but in this paper we focus only on rates of change.
