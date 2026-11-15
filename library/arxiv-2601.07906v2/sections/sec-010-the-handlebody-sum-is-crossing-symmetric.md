---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-010-the-handlebody-sum-is-crossing-symmetric
section_title: "The handlebody sum is crossing symmetric"
section_number: null
pages: 34-41
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.985
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{sec:3.3}

Now that we have reviewed the topology of handlebodies and their description in Virasoro TQFT, we will study the sum over handlebodies and its implications for the statistics of OPE coefficients. This handlebody sum is the simplest sum over a subset of topologies that is compatible with crossing symmetry.

Crossing symmetry is most clear on the level of the canonical partition function. Namely, by the previous section, the handlebody sum is just a sum over mapping class group images of some `seed’ vacuum block:\vspace{1mm} \begin{equation}\label{eq:handlebodysum3}
        \overline{Z[\Sigma_{g};\Omega,\bar\Omega]} \quad \supset \,\sum_{\gamma \in \text{MCG}(\Sigma_g)/\mathcal{H}_g} \left |  \mathcal{F}_g^{\,\gamma\cdot\mathcal{C}_0}(\mathds{1};\Omega) \right |^2\,.
    \end{equation}
This is clearly invariant under the action of the mapping class group $\Omega \mapsto \gamma’\cdot\Omega$, $\bar\Omega \mapsto \gamma’\cdot\bar\Omega$, simply by relabelling the sum $\gamma \circ \gamma’ \to \gamma$. The choice of seed $\mathcal{C}_0$ is irrelevant, as the mapping class group coset \eqref{eq:coset} acts transitively on the full set of handlebodies. Our convention is to pick $\mathcal{C}_0$ to be the genus-$g$ generalization of the dumbbell channel (called the `necklace' in \cite{Belin:2021ryy}):
\begin{equation}\label{eq:choiceofseed}
\mathcal{C}_0 = \vcenter{\hbox{
\begin{tikzpicture}
    \draw[very thick, wilsonred] (-2,0) circle (0.5);
    \draw[very thick, wilsonred] (-1.5,0) -- (-1,0);
    \draw[very thick, wilsonred] (-0.5,0) circle (0.5);
    \draw[very thick, wilsonred] (0,0) -- (0.15,0);
    \draw[very thick, wilsonred, dotted] (0.15,0)--(0.8,0);
    \draw[very thick, wilsonred] (0.8,0)--(1,0);
    \draw[very thick, wilsonred] (1.5,0) circle (0.5);
\end{tikzpicture}
}}.
\end{equation}

Each vacuum block in the sum \eqref{eq:handlebodysum3} is the leading saddle (in the semiclassical limit) in some region of moduli space. This is because the classical on-shell action is proportional to the renormalized volume of the handlebody, which goes to $-\infty$ in the limit where we pinch a compressible disk \cite{Schlenker:2022dyo} (which can be thought of as a high-temperature limit in a corner of moduli space). Thus, the handlebody sum gives the leading large-$c$ contribution to the average $\overline{Z[\Sigma_g]}$.

Next, let us translate the handlebody sum \eqref{eq:handlebodysum3} to the level of OPE coefficients.  We do so by expanding the LHS of \eqref{eq:handlebodysum3} in conformal blocks in some channel $\mathcal{C}$, and using the identity crossing kernels to rewrite the RHS in the same channel. We can then strip off the conformal blocks, so that we are left with:
\begin{equation}\label{eq:handlebody sum statistics}
    \overline{\prod_{e_i\in \Gamma_{\mathcal{C}}}\!\!\rho(h_i,\bar h_i)\!\!\!\prod_{v_{ijk}\in \Gamma_{\mathcal{C}}}\!\!\!C_{ijk}} \,\,\,\supset \sum_{\gamma\in \text{MCG}(\Sigma_g)/\mathcal{H}_g} \big |\mathbb{K}^{\,\gamma\cdot\gamma_\mathcal{C}}_{\mathds{1}\bm{h}} \big |^2\,.
\end{equation}
Here we have defined $\gamma_\mathcal{C}$ to be the crossing transformation that maps 
 $\gamma_\mathcal{C} \cdot \mathcal{C} = \mathcal{C}_0$, where $\mathcal{C}_0$ was our choice of seed in \eqref{eq:choiceofseed}. Its corresponding crossing kernel can be written (in terms of the Liouville momenta) as:
 \begin{equation}
     \mathbb{K}^{\,\gamma\cdot\gamma_\mathcal{C}}_{\mathds{1}\boldsymbol{P}} = \int_0^\infty \d^{3g-3} P' \,\mathbb{K}^{\,\gamma}_{\mathds{1}\boldsymbol{P}'}\, \mathbb{K}^{\gamma_\mathcal{C}}_{\boldsymbol{P'P}}\,.
 \end{equation}
 The crossing transformation $\gamma_\mathcal{C}$ parametrizes the different mapping class group orbits that arise in \eqref{eq:handlebody sum statistics}: for each choice of channel $\mathcal{C}$ in which we decide to expand the partition function, there is a corresponding orbit $\{\gamma\cdot\gamma_\mathcal{C}\}_{\gamma\in \text{MCG}(\Sigma_g)/\mathcal{H}_g}$. There are only finitely many orbits,\footnote{Technically, there are finitely many diffeomorphism classes of markings of $\Sigma_g$. One way to see this is to note that any given $\mathcal{C}$ is related by finitely many MS moves to a channel where all contractible cycles are non-separating, and then invoke the fact that the mapping class group acts transitively on the set of non-separating simple closed curves \cite{HatcherThurston1980}.} which are in one-to-one correspondence with the patterns of OPE index contractions that we discussed in section \ref{sec:2}. We highlight the distinction between $\gamma$ and $\gamma_{\mathcal{C}}$ because a mapping class $\gamma$ does not change the topology of the graph $\Gamma_{\mathcal{C}}$ (instead,  what changes is the embedding of $\Gamma_{\mathcal{C}}$ in the Riemann surface). On the other hand, $\gamma_{\mathcal{C}}$ can be any crossing transformation (in the Moore-Seiberg groupoid), which may change the graph topology of $\Gamma_{\mathcal{C}}$. 

\begin{figure}
    \centering
    $Z_\text{Vir}\Bigg[$\!\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ]   (353.41,84) -- (353.41,112.5) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (353.41,84) .. controls (362.15,82.13) and (362.3,75.45) .. (349.75,72.79) .. controls (337.19,70.13) and (318.37,78.66) .. (318.37,97.79) .. controls (318.37,116.91) and (336.67,131.3) .. (350.27,122.95) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (353.41,84) .. controls (345.97,82.66) and (345.04,78.11) .. (351.84,76.97) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (361.25,73.93) .. controls (371.78,69.47) and (390.47,77.84) .. (390.84,96.15) .. controls (391.21,114.45) and (378.9,128.8) .. (362.44,124.06) .. controls (345.97,119.31) and (345.1,112.98) .. (350.79,112.88) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (350.79,112.88) .. controls (359.83,111.93) and (363.34,116.49) .. (357.59,119.15) ;

\draw (320.39,93.07) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{1}$};

\draw (352.8,92.88) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{3}$};

\draw (371.18,93.32) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{2}$};
\end{tikzpicture} $\Bigg]$, \qquad $Z_{\text{Vir}}\Bigg[\!\!$
    \tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.3,xscale=1.3,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [draw opacity=0] (263.34,142.94) .. controls (261.02,143.77) and (258.51,144.23) .. (255.9,144.23) .. controls (243.81,144.23) and (234,134.5) .. (234,122.49) .. controls (234,110.48) and (243.81,100.75) .. (255.9,100.75) .. controls (267.99,100.75) and (277.8,110.48) .. (277.8,122.49) .. controls (277.8,128.87) and (275.02,134.62) .. (270.61,138.59) -- (255.9,122.49) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (263.34,142.94) .. controls (261.02,143.77) and (258.51,144.23) .. (255.9,144.23) .. controls (243.81,144.23) and (234,134.5) .. (234,122.49) .. controls (234,110.48) and (243.81,100.75) .. (255.9,100.75) .. controls (267.99,100.75) and (277.8,110.48) .. (277.8,122.49) .. controls (277.8,128.87) and (275.02,134.62) .. (270.61,138.59) ;  

\draw  [draw opacity=0] (270.78,102.33) .. controls (273.13,101.48) and (275.65,101.02) .. (278.29,101.02) .. controls (290.39,101.02) and (300.19,110.75) .. (300.19,122.76) .. controls (300.19,134.77) and (290.39,144.5) .. (278.29,144.5) .. controls (266.2,144.5) and (256.4,134.77) .. (256.4,122.76) .. controls (256.4,117.02) and (258.64,111.79) .. (262.3,107.91) -- (278.29,122.76) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (270.78,102.33) .. controls (273.13,101.48) and (275.65,101.02) .. (278.29,101.02) .. controls (290.39,101.02) and (300.19,110.75) .. (300.19,122.76) .. controls (300.19,134.77) and (290.39,144.5) .. (278.29,144.5) .. controls (266.2,144.5) and (256.4,134.77) .. (256.4,122.76) .. controls (256.4,117.02) and (258.64,111.79) .. (262.3,107.91) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (255.9,122.49) -- (278.29,122.76) ;

\draw (235,118.06) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{1}$};

\draw (286.4,118.06) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{2}$};

\draw (259.41,122.68) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{3}$};
\end{tikzpicture}$\,\Bigg]$
    \caption{Two VTQFT diagrams that describe the same handlebody: one is in the sunset basis (left), the other in the dumbbell basis (right).}
    \label{fig:twopartitionfunctions}
\end{figure}

An example at genus 2 will help to understand this point. In the dumbbell channel, the handlebody sum \eqref{eq:handlebody sum statistics} should include the contribution from the mapping class $\gamma = \mathbb{S}\circ \mathbb{S}\circ \mathbb{F}\circ \mathbb{B}^2 \circ \mathbb{F}$,
whose VTQFT diagram is the linked dumbbell shown in figure \ref{fig:twopartitionfunctions} (right). This is indeed a MCG transformation, and $\gamma_\mathcal{C} = 1$. In the sunset channel, on the other hand, we have $\gamma_\mathcal{C} = \mathbb{F}$, so the same handlebody is now represented by $\gamma\circ \gamma_\mathcal{C} = \mathbb{S}\circ \mathbb{S}\circ \mathbb{F}\circ \mathbb{B}^2$, where we used that $\mathbb{F}^2 =1$. The corresponding VTQFT diagram is shown in figure \ref{fig:twopartitionfunctions} (left). The two representations of the same handlebody indeed lead to the same identity block:
\begin{multline}
  \int_0^\infty \d^3 P \,\sker{\mathds{1}}{P_1}{\mathds{1}}\sker{\mathds{1}}{P_2}{\mathds{1}}\fker{\mathds{1}}{P_3}{P_2}{P_1}{P_1}{P_2}\big(\mathbb{B}^{P_3}_{P_1P_2}\big)^2\mathcal{F}_{g=2}\!\left[\!\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.7,xscale=0.7]
        \draw[very thick, wilsonred] (0,0) ellipse (1.5 and 1);
        \draw[very thick, wilsonred] (0,1) -- (0,-1);
        \node at (-1.15,0) {\footnotesize $P_1$};
        \node at (0.31,0) {\footnotesize $P_3$};
        \node at (1.15,0) {\footnotesize $P_2$};
    \end{tikzpicture}
    }}\!\right]  \\ =  \mathcal{F}_{g=2}\!\left[\!\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [draw opacity=0] (263.34,142.94) .. controls (261.02,143.77) and (258.51,144.23) .. (255.9,144.23) .. controls (243.81,144.23) and (234,134.5) .. (234,122.49) .. controls (234,110.48) and (243.81,100.75) .. (255.9,100.75) .. controls (267.99,100.75) and (277.8,110.48) .. (277.8,122.49) .. controls (277.8,128.87) and (275.02,134.62) .. (270.61,138.59) -- (255.9,122.49) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (263.34,142.94) .. controls (261.02,143.77) and (258.51,144.23) .. (255.9,144.23) .. controls (243.81,144.23) and (234,134.5) .. (234,122.49) .. controls (234,110.48) and (243.81,100.75) .. (255.9,100.75) .. controls (267.99,100.75) and (277.8,110.48) .. (277.8,122.49) .. controls (277.8,128.87) and (275.02,134.62) .. (270.61,138.59) ;  

\draw  [draw opacity=0] (270.78,102.33) .. controls (273.13,101.48) and (275.65,101.02) .. (278.29,101.02) .. controls (290.39,101.02) and (300.19,110.75) .. (300.19,122.76) .. controls (300.19,134.77) and (290.39,144.5) .. (278.29,144.5) .. controls (266.2,144.5) and (256.4,134.77) .. (256.4,122.76) .. controls (256.4,117.02) and (258.64,111.79) .. (262.3,107.91) -- (278.29,122.76) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (270.78,102.33) .. controls (273.13,101.48) and (275.65,101.02) .. (278.29,101.02) .. controls (290.39,101.02) and (300.19,110.75) .. (300.19,122.76) .. controls (300.19,134.77) and (290.39,144.5) .. (278.29,144.5) .. controls (266.2,144.5) and (256.4,134.77) .. (256.4,122.76) .. controls (256.4,117.02) and (258.64,111.79) .. (262.3,107.91) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (255.9,122.49) -- (278.29,122.76) ;

\draw (235,116.06) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\mathds{1}$};

\draw (288.4,116.06) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\mathds{1}$};

\draw (261.41,123.68) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\mathds{1}$};

\draw (299.43,102.83) node [anchor=north west][inner sep=0.75pt]    {$'$};

\draw (230.57,102.54) node [anchor=north west][inner sep=0.75pt]    {$'$};
\end{tikzpicture}\!\right] .
\end{multline}
This reproduces the answer from our previous calculation \eqref{eq:identitylinkeddumbbell} in the dumbbell channel. The two representations of the same handlebody are related by an overall fusion move, which we can think of as a change of basis.

\paragraph{Spin quantization.} One immediate corollary of 
equation \eqref{eq:handlebody sum statistics}, which expresses a statistical moment of CFT data in terms of a mapping class group orbit, is that the spins $J_i = h_i-\bar h_i$ are manifestly quantized. To see this, note that the sum over the mapping class group contains a sub-sum where we precompose with powers of Dehn twists $T_i^{n_i}$ acting on the cycles in the channel $\mathcal{C}$. Writing $\gamma = \tilde\gamma \circ T^{n_1}\circ \dots \circ T^{n_{3g-3}}$, the corresponding partial sum over crossing kernels takes the form:
\begin{equation}
    \sum_{\bm{n}\in \mathbb{Z}^{3g-3}} \Big |\mathbb{K}^{\,\tilde \gamma}_{\mathds{1}\bm{h}}\, \mathbb{T}_{h_1}^{\,n_1}\cdots \mathbb{T}_{h_{3g-3}}^{\,n_{3g-3}}\Big |^2 = \left |\mathbb{K}^{\,\tilde \gamma}_{\mathds{1}\bm{h}}\right |^2 \prod_{i=1}^{3g-3}\delta_{\mathbb{Z}}(J_i),
\end{equation}
where we used the Poisson resummation formula to rewrite the sum over Dehn twists as the Dirac comb, $\sum_{n\in \mathbb{Z}} \e^{2\pi i n (h_i-\bar h_i)} = \delta_{\mathbb{Z}}(h_i-\bar h_i)$.
Note that this holds when all weights $h_i>0$ are in a heavy channel: for the vacuum contributions ($h_i,\bar h_i = 0$), spin is trivially quantized ($J_i=0$), and we do not sum over Dehn twists because $[T_{\mathds{1}}^n] = [1]$ in the handlebody group $\mathcal{H}_g$. So, spin quantization naturally follows from the sum over topologies, as was also stressed in \cite{deBoer:2025rct}.


\paragraph{Reduction to punctured surfaces of lower genus.} Another immediate consequence of  \eqref{eq:handlebody sum statistics} is that the sum over the genus-$g$ MCG contains, as a special case, the contributions from crossing in identity channels of punctured surfaces with lower genus. This can be seen by cutting the surface along non-separating geodesics, or, in terms of VTQFT diagrams, along edges that leave the VTQFT graph connected. The subset of mapping classes acting only on the cut surface gives rise to a sub-sum of  \eqref{eq:handlebody sum statistics}, which implements crossing symmetry of the lower-genus correlation functions of CFT operators below the black hole threshold. 

As an example at genus 2, consider the subset of mapping classes of the form $\gamma= \gamma_1 \circ \gamma_2\circ \gamma_{0,4}$, where $\gamma_1$ and $\gamma_2$ are modular transformations on the two dumbbell handles and $\gamma_{0,4}$ only acts on the 4-punctured sphere obtained by cutting the two bells. The corresponding crossing kernel simplifies to:
\be 
\mathbb{K}^{\gamma}_{\id P_1P_2P_3}= \mathbb{K}_{\id P_1}^{\gamma_1}\, \mathbb{K}_{\id P_2}^{\gamma_2}\, \mathbb{K}^{\gamma_{0,4}}_{\id P_3}\!\begin{bmatrix} P_1 & P_2 \\ P_1 & P_2 \end{bmatrix}\,  , \label{eq:genus 2 to genus0,4 reduction}
\ee
where $\mathbb{K}^{\gamma_{0,4}}_{\id P_3}$ only acts on the embedded 4-punctured sphere conformal block with internal momentum $P_3$ and pairwise identical external momenta $P_1,P_2$. The sum over $\gamma_{0,4}\in \text{MCG}(\Sigma_{0,4})$ implements crossing symmetry of the averaged 4-point function $\langle \mathcal{O}_1 \mathcal{O}_1 \mathcal{O}_2 \mathcal{O}_2\rangle_{\mathrm{S}^2}$. The only difference is that in \eqref{eq:genus 2 to genus0,4 reduction}, the conformal weights $h_1,h_2$ are continued above the black hole threshold. Moreover, summing over $\gamma_1$ and $\gamma_2$ in the modular group leads to two copies of the modular invariant spectral density at genus 1:
\be \label{eq:MWKdensity}
\rho_\text{MWK}(P,\bar P)=\sum_{\gamma \in \text{PSL}(2,\mathbb{Z})/\ZZ} \left|\mathbb{K}_{\id P}^{\gamma}\, \right|^2,
\ee
where MWK stands for Maloney-Witten-Keller \cite{Maloney:2007ud,Keller:2014xba}.

Since the full genus-$g$ mapping class group is bigger than the product of mapping class groups of its subsurfaces, crossing symmetry of the genus-$g$ partition function imposes a stronger constraint on the CFT ensemble than just crossing symmetry of the bordered surfaces embedded in $\Sigma_g$.
The moments of OPE coefficients with light external states arise as special cases of the handlebody sum \eqref{eq:handlebody sum statistics} (appropriately analytically continued) for restricted crossing transformations such as \eqref{eq:genus 2 to genus0,4 reduction}. 


\paragraph{Identity contributions and support of $\mathbb{K}^\gamma$.} The sum over crossing kernels \eqref{eq:handlebody sum statistics} has a subtlety that has to do with the contributions from the vacuum state $h_i = \bar h_i =0$. Namely, we should understand both sides of equation \eqref{eq:handlebody sum statistics} as distributions, to be integrated against conformal blocks. For moments with $h_i,\bar h_i$ all heavy, the crossing kernels contributing to the handlebody sum are smooth meromorphic functions. However,  they may have delta function support on identity contributions. 

The simplest example where this occurs is at genus one, where the  handlebody sum is the MWK density \eqref{eq:MWKdensity}. Transforming this density from Liouville variables to conformal weights, $\rho_{\text{MWK}}(P,\bar P)\d P \d \bar P = \rho_{\text{MWK}}(h,\bar h)\d h \d \bar h$, we can write the modular sum as:
\begin{equation}\label{eq:MWK2}
     \rho_{\text{MWK}}(h,\bar h) = \delta(h)\delta(\bar h) + \sum_{\gamma \neq I} \left|\mathbb{K}_{\id h}^{\gamma} \right|^2\,,
\end{equation}
where we separated out the contribution from the unit matrix $\gamma = I$. The modular kernel of the unit matrix is just the Dirac delta $\mathbb{K}_{\id h}^{\gamma= I} = \delta(h)$, with support only on $h=0$, whereas the modular kernels of the other elements of $\text{PSL}(2,\mathbb{Z})/\mathbb{Z}$ are smooth functions of $h$ (written, for example, in \cite{Benjamin:2020mfz}). The identity contribution $\delta(h)\delta(\bar h)$, besides being physically relevant for the spectrum of the CFT, is also important for crossing symmetry: under the modular S-transform in \eqref{eq:Sinvariance}, the term with $\gamma = S$ in \eqref{eq:MWK2} gets mapped to the identity $\gamma = I$, because $S$ squares to one. The fact that this holds as distributions is best understood by integrating against a Virasoro character and carefully analyzing the integration contour. 

At genus 2 and higher, there are more identity contributions, again encoded in the analytic properties of the crossing kernels. For example, in the dumbbell channel $\overline{\rho_1\rho_2\rho_3C_{113}C_{223}}$, the identity contributions come from simple mapping classes:
\begin{equation}
    \mathbb{K}^{\gamma = I}_{\id \bm{h}} = \prod_{i=1}^3 \delta(h_i), \quad \mathbb{K}^{\gamma = S}_{\id \bm{h}} = \sker{\id}{h_1}{\id}\delta(h_2)\delta(h_3), \quad \mathbb{K}^{\gamma = S\circ S}_{\id \bm{h}} = \sker{\id}{h_1}{\id}\sker{\id}{h_2}{\id}\delta(h_3), \dots
\end{equation}
and more generally any kernel that acts trivially on the middle edge of the dumbbell. As remarked above, this generates a subgroup isomorphic to $\text{PSL}(2,\mathbb{Z})\times \text{PSL}(2,\mathbb{Z})$ acting on the two subtori. In the sunset channel $\overline{\rho_1\rho_2\rho_3C_{123}C^*_{123}}$, the identity contributions come from $\gamma = \mathbb{F}$ and $\gamma = \mathbb{S}\circ \mathbb{F}$:
\begin{align}
   \mathbb{K}^{\gamma = F}_{\id \bm{h}} &= \delta(h_1)\delta(h_2) \fker{\id}{h_3}{\id}{\id}{\id}{\id} = \prod_{i=1}^3 \delta(h_i) ,\\
    \mathbb{K}^{\gamma = S\circ F}_{\id \bm{h}} &= \delta(h_1)\sker{\id}{h_2}{\id}\fker{\id}{h_3}{h_2}{\id}{\id}{h_2} = \delta(h_1)\rho_0(h_2)\delta(h_3-h_2),
\end{align}
and more generally any element of the form $\gamma_{p,q}\circ \mathbb{F}$, where $\gamma_{p,q} \in \text{PSL}(2,\mathbb{Z})$.
Here we used that the fusion kernel reduces to a delta function when one or more of the external operators is the identity \cite{Eberhardt:2023mrq}. This reflects the fact that $F$ and $I$ are identified under the handlebody group, i.e.~they lead to same handlebody:
\begin{equation}
  \tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (250.73,197.17) .. controls (250.8,197.17) and (250.88,197.16) .. (250.96,197.16) .. controls (254.74,197.16) and (257.81,205.95) .. (257.81,216.8) .. controls (257.81,227.64) and (254.74,236.43) .. (250.96,236.43) .. controls (250.76,236.43) and (250.56,236.41) .. (250.37,236.36) -- (250.96,216.8) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (250.73,197.17) .. controls (250.8,197.17) and (250.88,197.16) .. (250.96,197.16) .. controls (254.74,197.16) and (257.81,205.95) .. (257.81,216.8) .. controls (257.81,227.64) and (254.74,236.43) .. (250.96,236.43) .. controls (250.76,236.43) and (250.56,236.41) .. (250.37,236.36) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (252.06,236.18) .. controls (251.7,236.34) and (251.34,236.43) .. (250.96,236.43) .. controls (247.18,236.43) and (244.11,227.64) .. (244.11,216.8) .. controls (244.11,205.95) and (247.18,197.16) .. (250.96,197.16) .. controls (251.34,197.16) and (251.71,197.25) .. (252.07,197.42) -- (250.96,216.8) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (252.06,236.18) .. controls (251.7,236.34) and (251.34,236.43) .. (250.96,236.43) .. controls (247.18,236.43) and (244.11,227.64) .. (244.11,216.8) .. controls (244.11,205.95) and (247.18,197.16) .. (250.96,197.16) .. controls (251.34,197.16) and (251.71,197.25) .. (252.07,197.42) ;  

\draw    (172.53,217.09) .. controls (172.68,190.8) and (193.96,183.5) .. (208.02,183.84) .. controls (226.09,184.19) and (236.48,197.3) .. (250.54,197.2) .. controls (264.84,197.32) and (275.72,184.02) .. (293.09,183.93) .. controls (307.39,184.05) and (328.65,190.73) .. (328.5,217.25) .. controls (328.59,244.21) and (307.31,250.85) .. (293.02,250.5) .. controls (275.88,250.59) and (264.79,237.05) .. (250.49,237.14) .. controls (236.43,237.24) and (225.78,250.54) .. (207.94,250.42) .. controls (194.12,250.74) and (172.86,244.06) .. (172.53,217.09) -- cycle ;

\draw    (193.94,217.47) .. controls (199.38,205.85) and (221.27,204.47) .. (230.49,216.82) ;

\draw    (193.94,217.47) .. controls (200.49,229.14) and (224.83,228.94) .. (230.49,216.82) ;

\draw    (270.24,217.44) .. controls (276.37,205.85) and (299.04,205.16) .. (306.79,216.79) ;

\draw    (270.24,217.44) .. controls (280.51,228.71) and (301.07,227.05) .. (306.79,216.79) ;

\draw    (270.24,217.44) .. controls (269.67,216.7) and (269.48,216.61) .. (269.08,215.61) ;

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (172.84,217.21) .. controls (172.83,217.08) and (172.82,216.95) .. (172.82,216.82) .. controls (172.82,213.35) and (177.56,210.54) .. (183.41,210.54) .. controls (189.26,210.54) and (194,213.35) .. (194,216.82) .. controls (194,217.35) and (193.89,217.87) .. (193.68,218.36) -- (183.41,216.82) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (172.84,217.21) .. controls (172.83,217.08) and (172.82,216.95) .. (172.82,216.82) .. controls (172.82,213.35) and (177.56,210.54) .. (183.41,210.54) .. controls (189.26,210.54) and (194,213.35) .. (194,216.82) .. controls (194,217.35) and (193.89,217.87) .. (193.68,218.36) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (193.78,215.54) .. controls (193.93,215.95) and (194,216.38) .. (194,216.82) .. controls (194,220.3) and (189.26,223.11) .. (183.41,223.11) .. controls (177.56,223.11) and (172.82,220.3) .. (172.82,216.82) .. controls (172.82,216.44) and (172.88,216.07) .. (172.99,215.71) -- (183.41,216.82) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (193.78,215.54) .. controls (193.93,215.95) and (194,216.38) .. (194,216.82) .. controls (194,220.3) and (189.26,223.11) .. (183.41,223.11) .. controls (177.56,223.11) and (172.82,220.3) .. (172.82,216.82) .. controls (172.82,216.44) and (172.88,216.07) .. (172.99,215.71) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (306.47,216.11) .. controls (306.97,212.91) and (311.63,210.4) .. (317.3,210.4) .. controls (323.1,210.4) and (327.83,213.01) .. (328.17,216.31) -- (317.3,216.69) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (306.47,216.11) .. controls (306.97,212.91) and (311.63,210.4) .. (317.3,210.4) .. controls (323.1,210.4) and (327.83,213.01) .. (328.17,216.31) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (328.04,215.67) .. controls (328.14,216) and (328.19,216.34) .. (328.19,216.69) .. controls (328.19,220.16) and (323.31,222.97) .. (317.3,222.97) .. controls (311.29,222.97) and (306.42,220.16) .. (306.42,216.69) .. controls (306.42,216.34) and (306.47,216.01) .. (306.56,215.68) -- (317.3,216.69) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (328.04,215.67) .. controls (328.14,216) and (328.19,216.34) .. (328.19,216.69) .. controls (328.19,220.16) and (323.31,222.97) .. (317.3,222.97) .. controls (311.29,222.97) and (306.42,220.16) .. (306.42,216.69) .. controls (306.42,216.34) and (306.47,216.01) .. (306.56,215.68) ;  

\draw    (230.49,216.82) .. controls (231.01,215.91) and (231.19,215.02) .. (231.36,214.47) ;

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (441.14,216.7) .. controls (441.13,216.62) and (441.13,216.54) .. (441.13,216.46) .. controls (441.13,212.68) and (449.92,209.61) .. (460.76,209.61) .. controls (471.6,209.61) and (480.39,212.68) .. (480.39,216.46) .. controls (480.39,216.66) and (480.37,216.86) .. (480.32,217.05) -- (460.76,216.46) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (441.14,216.7) .. controls (441.13,216.62) and (441.13,216.54) .. (441.13,216.46) .. controls (441.13,212.68) and (449.92,209.61) .. (460.76,209.61) .. controls (471.6,209.61) and (480.39,212.68) .. (480.39,216.46) .. controls (480.39,216.66) and (480.37,216.86) .. (480.32,217.05) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (480.14,215.36) .. controls (480.31,215.72) and (480.39,216.09) .. (480.39,216.46) .. controls (480.39,220.25) and (471.6,223.31) .. (460.76,223.31) .. controls (449.92,223.31) and (441.13,220.25) .. (441.13,216.46) .. controls (441.13,216.09) and (441.21,215.72) .. (441.38,215.36) -- (460.76,216.46) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (480.14,215.36) .. controls (480.31,215.72) and (480.39,216.09) .. (480.39,216.46) .. controls (480.39,220.25) and (471.6,223.31) .. (460.76,223.31) .. controls (449.92,223.31) and (441.13,220.25) .. (441.13,216.46) .. controls (441.13,216.09) and (441.21,215.72) .. (441.38,215.36) ;  


\draw    (382.33,216.76) .. controls (382.48,190.46) and (403.76,183.16) .. (417.82,183.51) .. controls (435.89,183.86) and (446.28,196.96) .. (460.34,196.87) .. controls (474.64,196.99) and (485.52,183.69) .. (502.89,183.59) .. controls (517.19,183.72) and (538.45,190.4) .. (538.3,216.91) .. controls (538.39,243.88) and (517.11,250.51) .. (502.82,250.17) .. controls (485.68,250.26) and (474.59,236.71) .. (460.29,236.81) .. controls (446.23,236.91) and (435.58,250.21) .. (417.74,250.08) .. controls (403.92,250.4) and (382.66,243.72) .. (382.33,216.76) -- cycle ;

\draw    (403.74,217.14) .. controls (409.18,205.52) and (431.07,204.14) .. (440.29,216.49) ;

\draw    (403.74,217.14) .. controls (410.29,228.8) and (434.64,228.61) .. (440.29,216.49) ;

\draw    (480.04,217.11) .. controls (486.17,205.52) and (508.84,204.83) .. (516.59,216.46) ;

\draw    (480.04,217.11) .. controls (490.31,228.37) and (510.87,226.71) .. (516.59,216.46) ;

\draw    (480.04,217.11) .. controls (479.47,216.37) and (479.28,216.28) .. (478.88,215.28) ;

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (382.64,216.87) .. controls (382.63,216.75) and (382.62,216.62) .. (382.62,216.49) .. controls (382.62,213.02) and (387.36,210.2) .. (393.21,210.2) .. controls (399.06,210.2) and (403.8,213.02) .. (403.8,216.49) .. controls (403.8,217.02) and (403.69,217.54) .. (403.48,218.03) -- (393.21,216.49) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (382.64,216.87) .. controls (382.63,216.75) and (382.62,216.62) .. (382.62,216.49) .. controls (382.62,213.02) and (387.36,210.2) .. (393.21,210.2) .. controls (399.06,210.2) and (403.8,213.02) .. (403.8,216.49) .. controls (403.8,217.02) and (403.69,217.54) .. (403.48,218.03) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (403.58,215.2) .. controls (403.73,215.62) and (403.8,216.05) .. (403.8,216.49) .. controls (403.8,219.96) and (399.06,222.78) .. (393.21,222.78) .. controls (387.36,222.78) and (382.62,219.96) .. (382.62,216.49) .. controls (382.62,216.11) and (382.68,215.74) .. (382.79,215.38) -- (393.21,216.49) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (403.58,215.2) .. controls (403.73,215.62) and (403.8,216.05) .. (403.8,216.49) .. controls (403.8,219.96) and (399.06,222.78) .. (393.21,222.78) .. controls (387.36,222.78) and (382.62,219.96) .. (382.62,216.49) .. controls (382.62,216.11) and (382.68,215.74) .. (382.79,215.38) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (516.27,215.78) .. controls (516.77,212.58) and (521.43,210.07) .. (527.1,210.07) .. controls (532.9,210.07) and (537.63,212.68) .. (537.97,215.98) -- (527.1,216.35) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (516.27,215.78) .. controls (516.77,212.58) and (521.43,210.07) .. (527.1,210.07) .. controls (532.9,210.07) and (537.63,212.68) .. (537.97,215.98) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (537.85,215.34) .. controls (537.94,215.67) and (537.99,216.01) .. (537.99,216.35) .. controls (537.99,219.82) and (533.11,222.64) .. (527.1,222.64) .. controls (521.09,222.64) and (516.22,219.82) .. (516.22,216.35) .. controls (516.22,216.01) and (516.27,215.67) .. (516.36,215.35) -- (527.1,216.35) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (537.85,215.34) .. controls (537.94,215.67) and (537.99,216.01) .. (537.99,216.35) .. controls (537.99,219.82) and (533.11,222.64) .. (527.1,222.64) .. controls (521.09,222.64) and (516.22,219.82) .. (516.22,216.35) .. controls (516.22,216.01) and (516.27,215.67) .. (516.36,215.35) ;  

\draw    (440.29,216.49) .. controls (440.81,215.58) and (440.99,214.69) .. (441.16,214.13) ;

\draw (345,208.4) node [anchor=north west][inner sep=0.75pt]    {$\cong $};

\draw (180.75,196.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\id$};

\draw (258.75,210.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\id$};

\draw (311.75,195.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\id$};

\draw (390.75,196.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\id$};

\draw (455.25,196.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\id$};

\draw (522.75,196.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\id$};
\end{tikzpicture}\,.
\end{equation}
Note that the above identity contributions in the handlebody sum correctly implement the selection rule $C_{\id 23} = \delta_{23}$ for the statistical moment \eqref{eq:handlebody sum statistics}, as a distribution.


\paragraph{Crossing from handlebody surgery.}

So far, we discussed crossing symmetry of the handlebody sum on the level of the crossing kernels $\mathbb{K}^\gamma$. However, it is also useful to understand how crossing symmetry is manifest on the level of the fixed-$P$ partition functions $Z_{\text{Vir}}[M;P]$. This provides a diagrammatic interpretation of the terms in the sum. Namely, translating the handlebody sum in \eqref{eq:handlebody sum statistics} to VTQFT diagrams, we see that we only need to sum over fixed-$P$ partition functions on Wilson line networks with the same graph topology as $\Gamma_{\mathcal{C}}$. This is also clear from the interpretation of OPE coefficients as 3-punctured sphere boundaries discussed above equation \eqref{eq:ZVirOPE}.
This reformulation allows us to check that the handlebody sum \eqref{eq:handlebody sum statistics} satisfies the fixed-$P$ versions of the crossing symmetry constraints \eqref{eq:Binvariance}-\eqref{eq:Finvariance}. 

Namely, take any element in the handlebody sum and consider its corresponding VTQFT diagram, contributing as \eqref{eq:ZVirOPE}. Then, around any vertex of the diagram (embedded in $\mathrm{S}^3$), we can cut along a 3-punctured sphere and apply a braiding move:
\begin{equation}\label{eq:Z_vir braiding}
    \mathbb{B}^{P_1}_{P_2P_3} \,Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (250,90) -- (250,61.67) ;
\draw [shift={(250,61.67)}, rotate = 315] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (270,110) -- (250,90) ;
\draw [shift={(270,110)}, rotate = 270] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (250,90) -- (230,110) ;
\draw [shift={(230,110)}, rotate = 180] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (285,90) .. controls (285,109.33) and (269.33,125) .. (250,125) .. controls (230.67,125) and (215,109.33) .. (215,90) .. controls (215,70.67) and (230.67,55) .. (250,55) .. controls (269.33,55) and (285,70.67) .. (285,90) -- cycle ;

\draw (239.33,59.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (224.33,94.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (269,94.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};
\end{tikzpicture}\right] = Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (269.95,110.9) -- (270,82.07) ;
\draw [shift={(270,82.07)}, rotate = 315.09] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (305,110) .. controls (305,129.33) and (289.33,145) .. (270,145) .. controls (250.67,145) and (235,129.33) .. (235,110) .. controls (235,90.67) and (250.67,75) .. (270,75) .. controls (289.33,75) and (305,90.67) .. (305,110) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (270,110) .. controls (259.22,108.44) and (266.33,133.11) .. (290,130) ;
\draw [shift={(290,130)}, rotate = 37.51] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (270,110) .. controls (277.67,108.89) and (277.44,117.11) .. (271.44,121.78) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (250,130) .. controls (257.44,128.89) and (263.44,126.67) .. (267.67,124.44) ;
\draw [shift={(250,130)}, rotate = 36.51] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw (259.33,79.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (284.33,115.51) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (246.33,115.07) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};
\end{tikzpicture}
\right]\,.
\end{equation}
We labeled the Liouville momenta by $i\equiv P_i$. The dashed lines indicate that this vertex is part of the larger VTQFT diagram. We can view this as a local surgery operation, which sends handlebodies to handlebodies. If we then multiply by the anti-holomorphic counterpart, the LHS contributes to $\overline{C_{123}X}$, and the RHS to $\overline{C_{132}X}$; hence, the sum over handlebodies satisfies the first constraint equation \eqref{eq:Binvariance}. 

Similarly, given some VTQFT diagram, we can take any \emph{pair} of vertices that are connected by an edge, and cut along a 4-punctured sphere surrounding only these vertices and one edge. We then apply an F-move inside this 4-punctured sphere:
\begin{align}
\rho_0(P_3)\mathsf{C}_{123}&\mathsf{C}_{345} \, Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (265.83,105.83) -- (294.17,105.83) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (245.83,125.83) -- (265.83,105.83) ;
\draw [shift={(245.83,125.83)}, rotate = 360] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (265.83,105.83) -- (245.83,85.83) ;
\draw [shift={(245.83,85.83)}, rotate = 270] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (313.58,85.83) -- (293.58,105.83) ;
\draw [shift={(313.58,85.83)}, rotate = 180] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (293.58,105.83) -- (313.58,125.83) ;
\draw [shift={(313.58,125.83)}, rotate = 90] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (240,81.75) .. controls (251.75,68.63) and (266,99.13) .. (280.25,98.38) .. controls (294.5,97.63) and (308.5,71.88) .. (318,80.13) .. controls (327.5,88.38) and (306.75,96.13) .. (305.75,105.63) .. controls (304.75,115.13) and (328.5,121.38) .. (317.5,130.38) .. controls (306.5,139.38) and (294.5,111.88) .. (280,113.38) .. controls (265.5,114.88) and (251,138.88) .. (242.25,131.13) .. controls (233.5,123.38) and (253.25,111.38) .. (254.25,106.63) .. controls (255.25,101.88) and (234.25,88.88) .. (240,81.75) -- cycle ;

\draw (228.58,77.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (228.58,119.15) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (276.75,115.65) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (323.08,78.23) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$4$};

\draw (323.25,119.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$5$};
\end{tikzpicture}
\right]\,\nonumber \\
&=\rho_0(P_3)\mathsf{C}_{123}\mathsf{C}_{345} \int \d P_3'\,\fker{P_3}{P_3'}{P_4}{P_2}{P_1}{P_5}Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (300.33,121.08) -- (300.33,128.83) ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (260,101.75) .. controls (271.75,88.63) and (286,119.13) .. (300.25,118.38) .. controls (314.5,117.63) and (328.5,91.88) .. (338,100.13) .. controls (347.5,108.38) and (326.75,116.13) .. (325.75,125.63) .. controls (324.75,135.13) and (348.5,141.38) .. (337.5,150.38) .. controls (326.5,159.38) and (314.5,131.88) .. (300,133.38) .. controls (285.5,134.88) and (271,158.88) .. (262.25,151.13) .. controls (253.5,143.38) and (273.25,131.38) .. (274.25,126.63) .. controls (275.25,121.88) and (254.25,108.88) .. (260,101.75) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (265.83,105.83) .. controls (285.83,126.75) and (313.17,125.75) .. (333.58,105.83) ;
\draw [shift={(333.58,105.83)}, rotate = 0.71] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;
\draw [shift={(265.83,105.83)}, rotate = 91.28] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (265.83,145.83) .. controls (285.83,123.41) and (313.17,124.48) .. (333.58,145.83) ;
\draw [shift={(333.58,145.83)}, rotate = 91.28] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;
\draw [shift={(265.83,145.83)}, rotate = 356.73] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw (249.58,97.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (249.58,139.15) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (295.58,136.15) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3'$};

\draw (343.08,98.23) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$4$};

\draw (343.25,139.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$5$};
\end{tikzpicture}
\right]  \\
&= \int \d P_3'\,\fker{P_3'}{P_3}{P_1}{P_2}{P_4}{P_5}\,\rho_0(P_3')\mathsf{C}_{13'5}\mathsf{C}_{43'2}\,Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (300.33,121.08) -- (300.33,128.83) ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (260,101.75) .. controls (271.75,88.63) and (286,119.13) .. (300.25,118.38) .. controls (314.5,117.63) and (328.5,91.88) .. (338,100.13) .. controls (347.5,108.38) and (326.75,116.13) .. (325.75,125.63) .. controls (324.75,135.13) and (348.5,141.38) .. (337.5,150.38) .. controls (326.5,159.38) and (314.5,131.88) .. (300,133.38) .. controls (285.5,134.88) and (271,158.88) .. (262.25,151.13) .. controls (253.5,143.38) and (273.25,131.38) .. (274.25,126.63) .. controls (275.25,121.88) and (254.25,108.88) .. (260,101.75) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (265.83,105.83) .. controls (285.83,126.75) and (313.17,125.75) .. (333.58,105.83) ;
\draw [shift={(333.58,105.83)}, rotate = 0.71] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;
\draw [shift={(265.83,105.83)}, rotate = 91.28] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (265.83,145.83) .. controls (285.83,123.41) and (313.17,124.48) .. (333.58,145.83) ;
\draw [shift={(333.58,145.83)}, rotate = 91.28] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;
\draw [shift={(265.83,145.83)}, rotate = 356.73] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw (249.58,97.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (249.58,139.15) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (295.58,136.15) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3'$};

\draw (343.08,98.23) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$4$};

\draw (343.25,139.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$5$};
\end{tikzpicture}
\right]\,.\label{eq:RHScrossing}
\end{align}
Here we used that the fixed-$P$ partition function is multiplied by the normalization factor \eqref{eq:ZVirOPE}, and we have written only the part of this factor that involves the vertices that have been singled out. In the last line, these normalization factors have nicely combined with the fusion kernel to swap the internal indices of $\mathbb{F}_{P_3P_3'}$, using the formula \eqref{eq:fusioninverse}. If we now multiply the LHS and RHS by the remaining normalization factors of \eqref{eq:ZVirOPE}, and then take the absolute value square on both sides, we see that the LHS contributes to $\overline{\rho(h_3,\bar h_3)C_{123}C_{345}X}$ (where $X$ represents the rest of the diagram) and the integrand of \eqref{eq:RHScrossing} contributes to $\overline{\rho(h_3',\bar h_3')C_{13'5}C_{43'2}X}$. Since the above 
surgery move sends handlebodies to handlebodies, and has a well-defined inverse $\mathbb{F}^{-1}$, we conclude that the handlebody sum satisfies the second constraint equation \eqref{eq:Binvariance}.

Finally, let us discuss invariance under the S-transform $\mathbb{S}_{P_1P_2}[P_3]$. Unlike the fusion move, $\mathbb{S}$ is a genuine mapping class group transformation and does not change the graph $\Gamma_{\mathcal{C}}$. Since the handlebody sum is a mapping class group orbit, it is clearly invariant under $\mathbb{S}$. Still, the S-transform has the interesting property that it changes the embedding manifold of the VTQFT graph $\Gamma_{\mathcal{C}}$, as we will now explain. Namely, take any VTQFT diagram with a loop, contributing to $\overline{C_{113}X}$. Regardless of how this loop is linked to the rest of the diagram, we can always surround it by a once-punctured torus, and apply an S-transform on the torus, giving:
\begin{multline}
   Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.1,xscale=1.1,baseline={([yshift=-0.5ex]current bounding box.center)}]  

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (70,110) .. controls (70,98.95) and (78.95,90) .. (90,90) .. controls (101.05,90) and (110,98.95) .. (110,110) .. controls (110,121.05) and (101.05,130) .. (90,130) .. controls (78.95,130) and (70,121.05) .. (70,110) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (110,110) -- (130,110) ;
\draw [shift={(130,110)}, rotate = 45] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (62.43,110.29) .. controls (62.43,95.3) and (79.83,83.14) .. (101.29,83.14) .. controls (122.75,83.14) and (140.14,95.3) .. (140.14,110.29) .. controls (140.14,125.28) and (122.75,137.43) .. (101.29,137.43) .. controls (79.83,137.43) and (62.43,125.28) .. (62.43,110.29) -- cycle ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (75.14,106.03) .. controls (81,131.43) and (101.57,122.29) .. (104.43,105.43) ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (76.86,109.01) .. controls (79.86,98.37) and (95.86,93.26) .. (103.57,109.78) ;

\draw (107.71,120.69) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (118.86,94.97) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (106,87.4) node [anchor=north west][inner sep=0.75pt]    {$'$};
\end{tikzpicture}
\right]
\equiv \int_0^\infty\!\!\d P_2\, \sker{P_1}{P_2}{P_3} \,Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.1,xscale=1.1,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (70,110) .. controls (70,98.95) and (78.95,90) .. (90,90) .. controls (101.05,90) and (110,98.95) .. (110,110) .. controls (110,121.05) and (101.05,130) .. (90,130) .. controls (78.95,130) and (70,121.05) .. (70,110) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (110,110) -- (130,110) ;
\draw [shift={(130,110)}, rotate = 45] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (62.43,110.29) .. controls (62.43,95.3) and (79.83,83.14) .. (101.29,83.14) .. controls (122.75,83.14) and (140.14,95.3) .. (140.14,110.29) .. controls (140.14,125.28) and (122.75,137.43) .. (101.29,137.43) .. controls (79.83,137.43) and (62.43,125.28) .. (62.43,110.29) -- cycle ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (75.14,106.03) .. controls (81,131.43) and (101.57,122.29) .. (104.43,105.43) ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (76.86,109.01) .. controls (79.86,98.37) and (95.86,93.26) .. (103.57,109.78) ;

\draw (107.71,120.69) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (118.86,94.97) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};
\end{tikzpicture}
\right] \\[1em] = \int_0^\infty \!\!\d P_2 \,\sker{\mathds{1}}{P_2}{\mathds{1}} \,Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.1,xscale=1.1,baseline={([yshift=-0.5ex]current bounding box.center)}] 
\draw  [draw opacity=0][line width=1.2]  (128.6,137.37) .. controls (125.67,144.77) and (118.44,150) .. (110,150) .. controls (98.95,150) and (90,141.05) .. (90,130) .. controls (90,118.95) and (98.95,110) .. (110,110) .. controls (121.05,110) and (130,118.95) .. (130,130) .. controls (130,130.74) and (129.96,131.47) .. (129.88,132.19) -- (110,130) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (128.6,137.37) .. controls (125.67,144.77) and (118.44,150) .. (110,150) .. controls (98.95,150) and (90,141.05) .. (90,130) .. controls (90,118.95) and (98.95,110) .. (110,110) .. controls (121.05,110) and (130,118.95) .. (130,130) .. controls (130,130.74) and (129.96,131.47) .. (129.88,132.19) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (140,130) -- (160,130) ;
\draw [shift={(160,130)}, rotate = 45] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (78.11,130.29) .. controls (78.11,115.3) and (98.11,103.14) .. (122.78,103.14) .. controls (147.45,103.14) and (167.44,115.3) .. (167.44,130.29) .. controls (167.44,145.28) and (147.45,157.43) .. (122.78,157.43) .. controls (98.11,157.43) and (78.11,145.28) .. (78.11,130.29) -- cycle ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (95.14,126.03) .. controls (101,151.43) and (121.57,142.29) .. (124.43,125.43) ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (96.86,129.01) .. controls (99.86,118.37) and (115.86,113.26) .. (123.57,129.78) ;

\draw  [draw opacity=0][line width=1.2]  (131.29,124.45) .. controls (131.87,124.3) and (132.48,124.22) .. (133.11,124.22) .. controls (136.79,124.22) and (139.78,126.88) .. (139.78,130.17) .. controls (139.78,133.45) and (136.79,136.11) .. (133.11,136.11) .. controls (129.43,136.11) and (126.44,133.45) .. (126.44,130.17) .. controls (126.44,129.05) and (126.79,128) .. (127.39,127.11) -- (133.11,130.17) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (131.29,124.45) .. controls (131.87,124.3) and (132.48,124.22) .. (133.11,124.22) .. controls (136.79,124.22) and (139.78,126.88) .. (139.78,130.17) .. controls (139.78,133.45) and (136.79,136.11) .. (133.11,136.11) .. controls (129.43,136.11) and (126.44,133.45) .. (126.44,130.17) .. controls (126.44,129.05) and (126.79,128) .. (127.39,127.11) ;  

\draw (133.05,137.13) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (145.75,116.3) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (80.38,123.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};
\end{tikzpicture}
\right] 
\equiv Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.1,xscale=1.1,baseline={([yshift=-0.5ex]current bounding box.center)}] 
\draw  [draw opacity=0][line width=1.2]  (128.6,137.37) .. controls (125.67,144.77) and (118.44,150) .. (110,150) .. controls (98.95,150) and (90,141.05) .. (90,130) .. controls (90,118.95) and (98.95,110) .. (110,110) .. controls (121.05,110) and (130,118.95) .. (130,130) .. controls (130,130.74) and (129.96,131.47) .. (129.88,132.19) -- (110,130) -- cycle ; \draw  [color=black  ,draw opacity=1 ][line width=1.2]  (128.6,137.37) .. controls (125.67,144.77) and (118.44,150) .. (110,150) .. controls (98.95,150) and (90,141.05) .. (90,130) .. controls (90,118.95) and (98.95,110) .. (110,110) .. controls (121.05,110) and (130,118.95) .. (130,130) .. controls (130,130.74) and (129.96,131.47) .. (129.88,132.19) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (140,130) -- (160,130) ;
\draw [shift={(160,130)}, rotate = 45] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (78.11,130.29) .. controls (78.11,115.3) and (98.11,103.14) .. (122.78,103.14) .. controls (147.45,103.14) and (167.44,115.3) .. (167.44,130.29) .. controls (167.44,145.28) and (147.45,157.43) .. (122.78,157.43) .. controls (98.11,157.43) and (78.11,145.28) .. (78.11,130.29) -- cycle ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (95.14,126.03) .. controls (101,151.43) and (121.57,142.29) .. (124.43,125.43) ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (96.86,129.01) .. controls (99.86,118.37) and (115.86,113.26) .. (123.57,129.78) ;

\draw  [draw opacity=0][line width=1.2]  (131.29,124.45) .. controls (131.87,124.3) and (132.48,124.22) .. (133.11,124.22) .. controls (136.79,124.22) and (139.78,126.88) .. (139.78,130.17) .. controls (139.78,133.45) and (136.79,136.11) .. (133.11,136.11) .. controls (129.43,136.11) and (126.44,133.45) .. (126.44,130.17) .. controls (126.44,129.05) and (126.79,128) .. (127.39,127.11) -- (133.11,130.17) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (131.29,124.45) .. controls (131.87,124.3) and (132.48,124.22) .. (133.11,124.22) .. controls (136.79,124.22) and (139.78,126.88) .. (139.78,130.17) .. controls (139.78,133.45) and (136.79,136.11) .. (133.11,136.11) .. controls (129.43,136.11) and (126.44,133.45) .. (126.44,130.17) .. controls (126.44,129.05) and (126.79,128) .. (127.39,127.11) ;  

\draw (133.05,137.13) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (145.75,116.3) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (78.38,123.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\Omega$};
\end{tikzpicture}
\right].\label{eq:omegaloop}
\end{multline}
In the second line we used the integral identity \eqref{eq:Verlinde lasso} (the ``Verlinde lasso''). In the final equality we recognized the VTQFT version of the $\Omega$-loop \cite{Hartman:2025cyj}, which implements a Dehn surgery with a relative S-transform. This surgery changes the manifold in which the VTQFT graph is embedded. For example, if the loop is embedded trivially in the ambient $\mathrm{S}^3$, the addition of the $\Omega$-loop in \eqref{eq:omegaloop} turns the embedding manifold into $\mathrm{S}^2\times \mathrm{S}^1$, which is a closed manifold obtained by gluing the boundaries of two solid tori with the identity map. Note, however, that in a generic tangled VTQFT diagram, there will be Wilson lines passing through the $P_1$ loop on the LHS of \eqref{eq:omegaloop}, 
so that the $\Omega$-loop acts non-trivially on the topology of the background manifold. We will see a number examples of this in section \ref{sec:5}.

\paragraph{Convergence.} One final obvious point that we have not addressed so far is the question of convergence of the handlebody sum \eqref{eq:handlebodysum3}. In the genus-1 case, this sum is known to be divergent, but it can be regulated as an analytic continuation of a convergent Eisenstein series \cite{Maloney:2007ud,Keller:2014xba}. For $g>1$, regulating the handlebody sum is still an open problem. First, as we saw in \eqref{eq:MWKdensity}, the genus-$g$ MCG contains $\text{PSL}(2,\mathbb{Z})$ as a subgroup, which leads to a divergence that can be regularized similarly to \cite{Maloney:2007ud,Keller:2014xba}. Second, there is a canonical map from $\text{MCG}(\Sigma_g)$ to $\mathrm{Sp}(2g,\mathbb{Z})$ by reducing to homology. However, this map has a non-trivial kernel (the Torelli group), and moreover the coset $\text{MCG}(\Sigma_g)/\mathcal{H}_g$ is strictly bigger than $\mathrm{Sp}(2g,\mathbb{Z})/\Gamma_\infty$, with $\Gamma_\infty$ the parabolic subgroup \cite{Collier:2023fwi}. 
In \cite{Maloney:2020nni,Collier:2021rsn}, a divergent sum over $\mathrm{Sp}(2g,\mathbb{Z})/\Gamma_\infty$ was regulated by a higher degree Eisenstein series, so potentially a similar method can be used for our MCG coset. However, this is technically challenging, first and foremost because we do not know the behavior of conformal blocks under mapping classes of high complexity. We leave this as a question for future work.
