---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-021-61-one-shock
section_title: "One shock"
section_number: 6.1
pages: 32-36
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.982
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:one-shock}
First, we will consider the time evolved thermofield double state perturbed by a single precursor smeared over the entire boundary sphere
\be
e^{-i H_L t_L}\, e^{-i H_R t_R}\, W(t_w) \TFD. \label{eq:sinlge-precursors}
\ee
This state is dual to an eternal black hole geometry with a spherically symmetric shock wave emerging from the boundary at time $t_w$.
We will restrict to $t_w < 0$ and $t_L, t_R > 0$ so that we study the complexity of the state to the future of the shock wave.

The construction of these geometries has now been covered many places (see, e.g. \cite{localshocks}), so we will give only a minimal review. We will consider perturbations of global-AdS black hole geometries in $D$  dimensions. It is convenient to consider Kruskal coordinates, where the metric is given by
\begin{align}
ds^2 =\,\,-A&(uv) \, 2du dv + B(uv)\, d\Omega_{D-2}^2 + 2A(uv)h\,\delta(u) \, du^2, \\
&A(uv) = -\frac{2}{uv}\frac{f(r)}{f'(r_h)^2}, \qquad B(uv) = r^2, \\
&f(r) = 1 - \frac{8 \pi}{(D-2)\Omega_{D-2}} \frac{2 G M}{r^{D-3}} + \frac{r^2}{\lads^2}, \label{eq:metric-one-shock}
\end{align}
where $r_h$ is the horizon radius, and the last term is an ansatz for the backreaction of the perturbation.
The relationship between Kruskal coordinates and Schwarzschild coordinates is given by
\be
uv = - e^{\frac{4\pi}{\beta}r_*(r)}, \qquad u/v = - e^{-\frac{4\pi}{\beta} t}, \qquad \beta = \frac{4\pi \lads^2}{r_h (D-1) + (D-3)\frac{\lads^2}{r_h} },
\ee
with $dr_* = dr / f(r)$.

The shock wave is created by acting with the scalar operator $W$ at time $t_w<0$ smeared over the entire boundary. For large $|t_w|$, this creates a particle of null matter traveling along $u=0$ in the bulk. The expectation value of the stress tensor in this state is
\be
T_{uu} = \frac{E}{\lads^{D}} e^{ 2\pi |t_w| / \beta } \delta(u), \label{eq:stress-tensor-shock}
\ee
with the dimensionless constant $E$ related to the $O(1)$ asymptotic energy of the particle (see e.g. the Appendix of \cite{Roberts:2014ifa} for details). Plugging \eqref{eq:metric-one-shock} and \eqref{eq:stress-tensor-shock} into Einstein's equations,
we find a solution
\be
h \sim  e^{\frac{2\pi}{\beta}(|t_w| - t_* ) } \label{eq:shift}
\ee



where we have defined the fast scrambling time $t_* = \frac{\beta}{2\pi} \log \frac{\lads^{D-2} } {G}$. The main point is that since boundary time evolution acts as a boost near the horizon, the $G$ suppression can be overcome by pushing $t_w$ further into the past. In this way, a small asymptotic perturbation can have a large backreaction on the geometry and a large effect on the complexity of the state.
Finally, we note that the metric \eqref{eq:metric-one-shock} implies that the constant $h$ has the interpretation of a shift in the $v$ coordinate by $\delta v = h$ from crossing the shock. This means, among other things, that the left and right $v=0$ horizons no longer meet at $u=0$.

The Kruskal diagram of this geometry is shown in Fig.~\ref{kruskal}.\footnote{Fig.~\ref{kruskal} is only really appropriate for $D=2+1$. For $D>3$, the left and right boundaries of the Kruskal diagram are no longer at $uv=-1$ \cite{Fidkowski:2003nf}.  Since this complication does not change the asymptotic value of the complexity of the state, it will be neglected.} The left figure shows a geometry with a small shift $h$, and the right figure shows a larger shift. The shock wave is shown as double black lines along $u=0$.  The Wheeler-DeWitt patch $\CW$ is drawn in blue, and the intersection of $\CW$ and the black hole interior shown is light gray.\footnote{In this section, we will be interested only in the intersection of $\CW$ and the Einstein-Rosen bridge. The portion of $\CW$ outside of the black hole interior is time independent and divergent. Therefore, dropping this region is a consistent regularization of the complexity for all of the states that we consider.}  The shape of this region (and whether it touches the bottom singularity) is determined by the boundary times $t_L, t_R$ and the shift $h$. Geometrically, we see that for $u_0^{-1} + h  < v_0$ the past going light rays meet in the interior, and for $u_0^{-1} + h  > v_0$ they intersect the singularity. Here, we have used the definition of the Kruskal coordinates to define
\be
u_0 = e^{\frac{2\pi}{\beta} t_L}, \qquad v_0 = e^{\frac{2\pi}{\beta} t_R}. \label{eq:boundary-times-as-kruskal}
\ee
Since we are assuming $t_L > 0$, $u_0^{-1}$ is exponentially small and from now on will be neglected. This lets us express the condition for $\CW$ to intersect the past singularity as $|t_w| - t_* \ge t_R$.

\begin{figure}
\begin{center}
\includegraphics[scale=.61]{one-shocks.pdf}
\caption{Kruskal diagram of one-shock geometries with different size shifts. The double black line along $u=0$ is the shock wave. The blue lines show the boundary of $\CW$. The light gray shaded region is the intersection of $\CW$ and the black hole interior. The action in this gray region determines the complexity.
{\bf Left:} small shift $h$ with $|t_w| - t_* \le t_R$. {\bf Right:} large shift $h$ with $|t_w| - t_* \ge t_R$ .}\label{kruskal}
\end{center}
\end{figure}

The complexity will be a function of $u_0, v_0,$ and $h$, since these are the parameters of the state \eqref{eq:sinlge-precursors} in reference to the thermofield double. The geometry of the causal wedge is different depending on the value of these parameters, with a transition at $|t_w| - t_* = t_R$ or $h  = v_0$.  We expect that the complexity $\CC$ will be a piecewise continuous function due to the transition of the geometry of the $\CW$ at the point $h  = v_0$. Using the results from \S\ref{sec:bh}, we could easily compute the rate of change of complexity for each of $t_L, t_R, t_w$ and then integrate to get the overall complexity. Instead, we will take a slightly different approach. From Fig.~\ref{kruskal}, we see that either the intersection of $\CW$ with the black hole interior creates a diamond-shaped region bounded on two sides by the horizons and on two sides by the Wheeler-DeWitt patch or it creates a five-sided region bounded by the two horizons, the two edges of the patch, and the singularity. These two shapes, denoted $I$ and $II$ in Fig.~\ref{kruskal}, are shown in Fig.~\ref{regions}. Since $v_0^{-1} =  e^{-2 \pi t_R /\beta} \ll 1$, the diamond region $I$ is exponentially small \eqref{eq:boundary-times-as-kruskal} and will have a vanishing contribution to the action. The only important contribution to the action will come from the five-sided region $II$ bounded by the singularity.

\begin{figure}
\begin{center}
\includegraphics[scale=.7]{total-needed-regions.pdf}
\caption{{\bf Left:} diamond-shape region bounded on the top by the horizons and on the bottom by edges of $\CW$. This region will always have vanishing action. {\bf Right:} five-sided region bounded on the bottom by the horizons, on the sides by edges of $\CW$, and on the top by the singularity. The only significant contribution to action is from regions with this shape.}\label{regions}
\end{center}
\end{figure}

 To proceed, we will compute the action of region $II$ for arbitrary $\CW$ edges $u_1, v_1$. Since $t_L, t_R, |t_w| > 0$, we can safely assume $u_1, v_1 \gg 1$. The bulk contribution is straightforward, and we find
 \be
\CA_\textrm{bulk} = -\frac{\Omega_{D-2} \, r_h^{D-1}}{ \pi G \lads^2} \frac{\beta}{2\pi} \log u_1 v_1.
 \ee
 The boundary contributions are from the horizon and the singularity. The edges of $\CW$ do not contribute. A calculation similar to that in \S\ref{sec:bh} gives
  \be
\CA_\textrm{boundary} =  \left[  - \bigg( \frac{D-1 }{D-2}\bigg) M  + \frac{\Omega_{D-2} r^{D-3} }{8 \pi G}  \left( (D - 2 ) + (D-1) \frac{r^2}{\lads^2} \right) \right]^{r_h}_0  \frac{\beta}{2\pi} \log u_1 v_1,
 \ee
 and the total action in region $II$ is
 \be
\CA_{II} = 2M\, \frac{\beta}{2\pi} \log u_1 v_1. \label{eq:action-region-II}
 \ee

With this result in hand, let us consider the one shock geometry with small shift $|t_w| - t_* \le t_R$ (left side of Fig.~\ref{kruskal}). The only contribution is from the top five-sided region $II$. We can simply plug $u_1 = u_0$ and $v_1 = v_0 + h$ into \eqref{eq:action-region-II}. Using the fact that $v_0 > h$, we find
\be
\CA_{|t_w| - t_* \le t_R} = 2M\, (t_L + t_R),\label{eq:one-shock-complexity-weak-shock}
\ee
that is, as if the shock wave wasn't even there. This is easy to understand; for large $t_R$ we have evolved the state to a region where the backreaction of the perturbation is negligible. The complexity is simply given by the time evolution of the thermofield double state.


Now, let's consider the geometry with large shift $|t_w| - t_* \ge t_R$ (right side of Fig.~\ref{kruskal}). Now we have two five-sided region $II$s. We get the contribution from the top region as before by  plugging $u_1 = u_0$ and $v_1 = v_0 + h$ into \eqref{eq:action-region-II}. Similarly, we get the contribution from the bottom region by again using \eqref{eq:action-region-II}, but with  $u_1 = -v_0^{-1}$  and $v_1 = -u_0^{-1} - h$. (It's OK to flip it upside down.) This time using the fact that $v_0 > h$ and $u_0^{-1} \approx 0$, we find
\be
\CA_{|t_w| - t_* \ge t_R} = 2M\, \big[t_L - t_R + 2(|t_w| - t_*)\big].\label{eq:one-shock-complexity-strong-shock}
\ee
In this case, the shift $h$ is large, the backreaction of $W(t_w)$ is not negligible, and the perturbation makes a huge contribution to the complexity. Furthermore, the growth of complexity in $t_w$ is twice the rate of growth in $t_L$. We can think of this as coming from the fact that $W(t_w) = e^{i H_L t_w} W e^{-i H_L t_w}$ is made up of two time evolution operators each of which accrues complexity linearly with time.

Additionally, we see that the growth of complexity in $t_w$ is delayed by a scrambling time $t_*$. From the bulk perspective, this is the fact that we need to push the time of the shock very far into the past in order to overcome the $G$ gravitational suppression. From the boundary/complexity perspective, this has been called the  ``switchback'' effect \cite{complexityshocks}. If $W$ were the identity operator, the two time evolution operators on either side of $W(t_w)$ would cancel. $W$ is not the identity; it is a very simple operator (e.g. a perturbation of only one of the $N^2$ degrees of freedom in a lattice site). While the perturbation is still growing, there will be cancellation between the two time evolution operators. Fast scrambling dynamics dictate that the influence of this perturbation will grow exponentially, covering all $N^2$ degrees of freedom in a time $t_* = \frac{\beta}{2\pi}\log N^2$. Since the growth is exponential, almost none of the degrees of freedom are influenced until the very end. Thus, there is a delay of $t_*$ until the complexity can grow. This was predicted and matched \cite{complexityshocks} for  CV-duality, and here we are showing how simply it arises for the complexity equals action prescription.

In the next subsections, we will give extensions and related results for complexity growth in shock wave geometries. However, many of the details of these calculations will be left to the references and/or the reader.
