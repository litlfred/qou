---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-085-184-the-non-archimedean-triangle-groups-delta-32
section_title: "The non-archimedean triangle groups $\Delta_3(2,4,6), \Delta_2(2,4,6)$ and Herrlich's tree."
section_number: 18.4
pages: 202-208
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.977
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::6.4}

\begin{para}\label{para::6.4.1} Our aim here is to explore the combinatorics
 of the finitely  
 generated groups $\Delta_3(2,4,6)$ and $ \Delta_2(2,4,6)$. 

\noindent It follows from the above considerations that
 $\Delta_3(2,4,6)$ sits in an exact sequence 
\begin{equation*}
1\to \an{\gamma_1,\gamma_2,\gamma_3}=\Gamma_3^+(2)\to \Delta_3(2,4,6)\to
 \mathfrak{S}_4\times \Z/2\Z =\Aut(\mathcal{X}^+(2))\to 1.
\end{equation*} 
 \noindent This extension is described by the outer action of
 $\mathfrak{S}_4\times \Z/2\Z$ on  $\an{\gamma_1,\gamma_2,\gamma_3}$. 
 Similarly, $\Delta_2(2,4,6)$ is an extension of a group of order $72$,
 $\Aut(\mathcal{X}^+(3))$, by a free group of rank four. In order to
 describe these extensions, we shall use F. Herrlich's work on 
 automorphisms of Mumford curves. 
\end{para}

\begin{para}\label{para::6.4.2} Let $S$ be a Mumford curve over some finite
 extension $K$ of $\Q_p$, and let $\Gamma 
 \subset PGL_2(K)$ be the corresponding Schottky group. It is known that
 any automorphism of $S$ lifts to $PGL_2(K)$: in fact, 
 the normalizer $N(\Gamma)$ of $\Gamma$ in sits $PGL_2(K)$ in an exact
 sequence \cite[IV]{sgamc}: 
\begin{equation*}
 1\to \Gamma\to N(\Gamma)\to  \Aut S\to 1.
\end{equation*} 
 \noindent Herrlich constructs a tree $\mathcal{T}$ endowed with an
 action of $N(\Gamma)$ as follows. One introduces a partition of the set
 of affinoid disks in $\P^1(K)$ into classes of the following form: a
 class contains a unique disk in $\A^1(K)$, of radius denoted by $r$ and
 all affinoid disks of the form $| z-a|\geq r$. The vertices of
 $\mathcal{T}$ are the classes of those disks which contain two fixpoints
 of some non-trivial element of $N(\Gamma)$, whose distance is the radius
 of the disk.  Two vertices are related by an edge if they can be
 represented by disks which are either both maximal, or nested in such a
 way that one is a maximal proper subdisk of the other. Herrlich shows
 that the natural action of $N(\Gamma)$ on affinoid disks induce an
 action without inversion on $\mathcal{T}$. This allows to apply the
 Bass-Serre theory of graphs of groups \cite{aas}, exploiting the fact
 that the stabilizer of vertices or edges belong to the short list of
 finite subgroups of $PGL_2(K)$
 \cite{herrlich80:_ordnun_autom_schot} \cite{herrlich80:_endlic_grupp}.
 When $S/\Aut(S)$ has genus $0$, the quotient $\mathcal{T}/N(\Gamma)$ is
 a finite tree of groups. The group $N(\Gamma)$ can then 
 be identified with its fundamental group, which is an amalgamated sum of
 the stabilizers of the vertices along the stabilizers of the edges.
\end{para}

\begin{para}\label{para::6.4.3} Let us apply this to
 $S=\mathcal{X}^+(2)_{\Q_9}$ with $N(\Gamma)=\Delta_3(2,4,6)$.  One has
 $(g-1)/\sharp(\Aut(S))=\frac{1}{24}$, and an inspection of the list of
 \cite{herrlich80:_ordnun_autom_schot} leaves only one possibility for
 the tree of groups $\mathcal{T}_3/\Delta_3(2,4,6)$, namely:

 \begin{center}
  \begin{picture}(100,35)(-50,-15)
   \put(-30,0){\makebox(0,0)[c]{$\mathfrak{D}_6$}}
   \put(-14.5,0){\makebox(0,0)[r]{$\bullet$}}
   \put(-15,0){\line(1,0){30}}
   \put(14.5,0){\makebox(0,0)[l]{$\circ$}}
   \put(30,0){\makebox(0,0)[c]{$\mathfrak{S}_4$}}
   \put(0,-10){\makebox(0,0)[c]{$\mathfrak{D}_3$}}
  \end{picture}
 \end{center}

 \medskip\noindent where $\mathfrak{D}_n$ are the dihedral groups.  
 In this case, the Herrlich tree $\mathcal{T}_3$ may be considered as a
 triadic analogue of the Schwarz-Escher tesselation:
 

\begin{figure}[h]
 \begin{picture}(180,180)(0,0)
  \put(0,0){\includegraphics[scale=0.5,clip]{fig3-6g.eps}}
 \end{picture}
 \caption{}
\end{figure}


\end{para}
 
\begin{para}\label{para::6.4.4} In the case of $S=\mathcal{X}^+(3)_{\Q_4}$
 with $N(\Gamma)=\Delta_2(2,4,6)$, one still has
 $(g-1)/\sharp(\Aut(S))=\frac{1}{24}$, and an inspection of the list of
 \cite{herrlich80:_ordnun_autom_schot} leaves only two possibilities for
 the tree of groups $\mathcal{T}_2/\Delta_2(2,4,6)$, namely: 

 \begin{center}
  \begin{picture}(100,35)(-50,-15)
   \put(-30,0){\makebox(0,0)[c]{$\mathfrak{D}_6$}}
   \put(-14.5,0){\makebox(0,0)[r]{$\bullet$}}
   \put(-15,0){\line(1,0){30}}
   \put(14.5,0){\makebox(0,0)[l]{$\circ$}}
   \put(30,0){\makebox(0,0)[c]{$\mathfrak{D}_4$}}
   \put(0,-10){\makebox(0,0)[c]{$\mathfrak{D}_2$}}
  \end{picture}
 \end{center}

\noindent and 

 \begin{center}
  \begin{picture}(100,35)(-50,-15)
   \put(-30,0){\makebox(0,0)[c]{$\mathfrak{S}_4$}}
   \put(-14.5,0){\makebox(0,0)[r]{$\bullet$}}
   \put(-15,0){\line(1,0){30}}
   \put(14.5,0){\makebox(0,0)[l]{$\circ$}}
   \put(30,0){\makebox(0,0)[c]{$\mathfrak{S}_4$}}
   \put(0,-10){\makebox(0,0)[c]{$\mathfrak{D}_4$}}
  \end{picture}
 \end{center}

\medskip\noindent In order to select the right one, we remark that
 $\Delta_2(2,4,6)$ contains the finite group generated by $ij$ and the
 quotient of $(\mathcal{B}_{3.\infty})^\times=
 \bigl\{\pm1,\;\pm i,\; \frac{\pm i\pm j}{2},\; \frac{\pm 1\pm ij}{2}\bigr\}$
 by $\pm 1$. This group is
 isomorphic to $\mathfrak{D}_6\cong \Z/2\Z\;\times \mathfrak{D}_3$,
 which is not contained in $\mathfrak{S}_4$.  Since any finite subgroup
 of the amalgamated sum of two groups is conjugated to a subgroup of one
 of these groups \cite[4.3]{aas}, we conclude that
 $\Delta_2(2,4,6)\cong \mathfrak{D}_6
 \ast_{\mathfrak{D}_2}\mathfrak{D}_4$,
 not $\mathfrak{S}_4 \ast_{\mathfrak{D}_4}\mathfrak{S}_4$

\medskip\noindent
The Herrlich tree $\mathcal{T}_2$ may be considered as a diadic analogue of
the Schwarz-Escher tesselation:


\begin{figure}[h]
 \begin{picture}(180,180)(0,0)
  \put(0,0){\includegraphics[scale=0.5,clip]{fig3-6h.eps}}
 \end{picture}
 \caption{}
\end{figure}

\bigskip\noindent
{\small (this is the set of points $u$ such that 
$j(\frac{e^{\pi i/3}-u}{1-e^{\pi i/3}u})\in [0,1728]$, 
where $j$ denotes the modular invariant).}

\medskip
It is important to pay attention to the fact that the symbol 
$\mathfrak{D}_6 \ast_{\mathfrak{D}_2}\mathfrak{D}_4$ is not free from
ambiguity: namely, there are essentially two non-equivalent ways of
embedding $\mathfrak{D}_2$ into $\mathfrak{D}_6\times \mathfrak{D}_4$:

{\it $1$st way$)$} the centers of $\mathfrak{D}_6$ and $\mathfrak{D}_4$ 
restrict to the same subgroup $\Z/2\Z$
of $\mathfrak{D}_2$. On identifying $\mathfrak{D}_6$ and $\mathfrak{D}_4$ with 
the matrix groups
\begin{equation*}
 \Bigl\langle\begin{pmatrix} 0& 1 \\ 1& 0
\end{pmatrix}, \begin{pmatrix} 0& -1 \\ 1& 1
\end{pmatrix}\Bigr\rangle\text{ and }
 \Bigl\langle\begin{pmatrix} 0& 1 \\ \pm1& 0
\end{pmatrix}\Bigr\rangle
\end{equation*}
respectively, the corresponding amalgam 
$\mathfrak{D}_6 \ast_{\mathfrak{D}_2}\mathfrak{D}_4$ is isomorphic 
to $GL_2(\Z)$;

{\it $2$nd way $)$} the trace of the center of $\mathfrak{D}_6\times 
\mathfrak{D}_4$ on $\mathfrak{D}_2$  is $\mathfrak{D}_2$ itself. The
corresponding amalgam $\mathfrak{D}_6
\ast_{\mathfrak{D}_2}\mathfrak{D}_4$ maps onto  
a semidirect product of $(\Z/3\Z)^2$ and ${\mathfrak{D}_4}$ (the 
latter acting on $(\Z/3\Z)^2$ as a matrix group
$\Bigl\langle
\begin{pmatrix}
 0& 1 \\ \pm1& 0
\end{pmatrix}
\Bigr\rangle$).
\end{para}

The following theorem summaries our results and settles the remaining 
ambiguity:

\begin{thm}\label{thm::6.4.5}
 \begin{enumerate}
  \item $\Delta_3(2,4,6)\cong \mathfrak{D}_6 
        \ast_{\mathfrak{D}_3} \mathfrak{S}_4$.
  \item $\Delta_2(2,4,6)\cong\mathfrak{D}_6\ast_{\mathfrak{D}_2}
	\mathfrak{D}_4$, where the embedding of $\mathfrak{D}_2$ into
	$\mathfrak{D}_6\times \mathfrak{D}_4$ is such that the trace of
	the center of $\mathfrak{D}_6\times \mathfrak{D}_4$ on
	$\mathfrak{D}_2$ is $\mathfrak{D}_2$ itself.
 \end{enumerate} 
\end{thm}

\begin{proof}
 Only the last assertion remains to be established. Let $\mathcal{S}$ be 
 the diadic Schwarz orbifold
 $(\P^1;(0,2),(1,4),(\infty,6))$.  There are surjective homomorphisms 
 (3.5.5, \ref{pro::4.3.3})
 \begin{equation*}
  \pi_1^{\mathrm{temp}}(\P^1\setminus
   \{0,1,\infty\})\to
   \pi_1^{\mathrm{orb}}(\mathcal{S})\to \Delta_2(2,4,6).
 \end{equation*} 
 The images 
 $\bar\gamma_0,\bar\gamma_1,\bar\gamma_\infty\in  \Delta_2(2,4,6)$
 of local monodromy elements $\gamma_0,\gamma_1,\gamma_\infty \in 
 \pi_1^{\mathrm{temp}}(\P^1\setminus
 \{0,1,\infty\})$ are elements of order $2,4,6$ respectively. By 
 \ref{pro::2.3.9}, the smallest closed normal
 subgroup of $\pi_1^{\mathrm{temp}}(\P^1\setminus
 \{0,1,\infty\})$ containing $\gamma_1,\gamma_\infty$ is 
 $\pi_1^{\mathrm{temp}}(\P^1\setminus
 \{0,1,\infty\})$ itself. It follows that the smallest normal
 subgroup of the discrete group $\Delta_2(2,4,6)$ containing 
 $\bar\gamma_1,\bar\gamma_\infty$ is $\Delta_2(2,4,6)$ itself.
 It thus suffices to show that if we where in the case $\mathfrak{D}_6 
 \ast_{\mathfrak{D}_2}\mathfrak{D}_4\cong
 GL_2(\Z)$, then $\bar\gamma_1,\bar\gamma_\infty\in SL_2(\Z)$. This is 
 clear, since any element of order $6$ (\resp $4$) in $ GL_2(\Z)$ is
 conjugate to $\pm
 \begin{pmatrix}
  0 & -1 \\ 1& 1
 \end{pmatrix}$
 (\resp to
 $\pm\begin{pmatrix}
      0& -1 \\ 1& 0
     \end{pmatrix}$).
\end{proof}

\medskip Part (ii) of this theorem allows us to answer at last 
question \ref{que::2.3.11} concerning
local monodromies $\gamma_0,\gamma_1,\gamma_\infty$ at $0,1,\infty$ 
in the temperate fundamental group
$\pi_1^{\mathrm{temp}}(\P^1_{\C_p}\setminus \{0,1,\infty\})$:

\begin{cor}\label{cor::6.4.6} Question \ref{que::2.3.11} has a negative
 answer for $p=2$: one cannot find local monodromies
 $\gamma_0,\gamma_1,\gamma_\infty$ such that 
 $\gamma_0.\gamma_1.\gamma_\infty = 1$.
\end{cor}

\begin{proof}
 Assume that such local monodromies exist.  By means of their images
 $\bar\gamma_0,\bar\gamma_1,\bar\gamma_\infty \in \Delta_2(2,4,6)\cong 
 \mathfrak{D}_6 \ast_{\mathfrak{D}_2}\mathfrak{D}_4 $ (notation of 
 the previous proof), it would be possible to construct
 a homomorphism
 \begin{equation*}
  \phi: \Delta (2,4,6)\to\Delta_2(2,4,6),
 \end{equation*}
 where $\Delta (2,4,6)$ 
 denotes the standard (archimedean) triangle group.
 Notice that the image of $\phi$ cannot be contained in any conjugate 
 of $\mathfrak{D}_6$ or $\mathfrak{D}_4$, since none of
 these finite groups contains elements of order $6$ and of order $4$ 
 simultaneously.

  According to \cite[6.3.5]{aas}, any (cocompact) triangle group 
 $\Delta$ has the
 fixpoint property $(FA)$: any action (without inversion) of $\Delta$ 
 on any tree has a fixpoint. It follows that the
 quotient
 $\Im\phi$ of $\Delta (2,4,6)$ would have property
 $(FA)$ as well. Since $Im\,\phi$ is a subgroup of the amalgam
 $\mathfrak{D}_6 \ast_{\mathfrak{D}_2}\mathfrak{D}_4$, this would 
 imply, according to \cite[6.2, prop. 21]{aas}, that
 $Im\,\phi$ is contained in a conjugate of $\mathfrak{D}_6$ or 
 $\mathfrak{D}_4$, a contradiction. 
\end{proof}

\begin{rem}
 The arithmetic $p$-adic triangle groups 
 $\Delta (e_0,e_1,e_\infty)$ do {\it not} have property
 $(FA)$. Indeed, their description as $p$-unit groups in quaternion 
 algebras shows that they admit a two-dimensional
 representation for which the eigenvalues are non-integral in general. 
 This property contradicts $(FA)$, \cf \cite[6.2, prop. 22]{aas}.
   Actually, Kato's description of $p$-adic triangle groups of Mumford 
 type as amalgams, together with \ref{thm::5.3.7}, implies that
 {\it no hyperbolic $p$-adic triangle group has property $(FA)$} (in 
 contrast to archimedean triangle groups).  Hence no hyperbolic $p$-adic
 triangle group can be generated by three elements $g_0,g_1,g_\infty$ of
 finite order satisfying $g_0g_1g_\infty=1$.
\end{rem}


\subsection{$F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)$ and the period 
mapping. Global analytic triadic continuation.}\label{sub::6.5}

\begin{para}\label{para::6.5.1} Rather than $\Delta(2,4,8)$, we now
 prefer to work with $\Delta(6,2,4)$ (this amounts to permute
 $0,1,\infty$ by $t\mapsto z=\frac{1}{1-t}$, and is more faithful to the
 first picture of this section which places the vertex 
 $O$ at the center of the disk). 

 The triangle group
$\Delta(6,2,4)$ is the projective monodromy group of the hypergeometric
 differential operator 
$L_{\frac{1}{24}, \frac{7}{24},\frac{5}{6}}$. More precisely,
 $L_{\frac{1}{24}, \frac{7}{24},\frac{5}{6}}(y)=0$ 
 is a {\it uniformizing differential equation} for the orbifold
 $\mathcal{X}^\ast$ viewed as the Schwarz orbifold 
\begin{equation*}
\left(\P^1,\;
 \begin{matrix}
  0& 1& \infty \\e_0=6& e_1=2& e_\infty = 4
 \end{matrix}
\right)
\end{equation*}
More explicitly, $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)$ and
 $z^{1/6}F(\frac{5}{24}, \frac{11}{24},\frac{7}{6}; z)$ are 
independent solutions of $L_{\frac{1}{24}, \frac{7}{24},\frac{5}{6}}$
 and for a suitable constant $\kappa$, the mapping 

\begin{equation*}
\tau(z)= \kappa^{-1}. \frac{z^{1/6}F(\frac{5}{24},
 \frac{11}{24},\frac{7}{6}; z) }{F(\frac{1}{24},
 \frac{7}{24},\frac{5}{6}; z)}
\end{equation*} 

\noindent sends the upper half plane bijectively to the basic triangle
 $OQP$ of the Schwarz tesselation, and 
 $\tau(0)=O,\;\tau(1)=Q,\;\tau(\infty)=P$. 

\begin{figure}[h]
 \begin{picture}(320,100)(0,-15)
  \put(0,0){\includegraphics[scale=0.8,clip]{fig3-6i-1.eps}}
  \put(57,-1){\makebox(0,0)[b]{\small $\bullet$}}
  \put(57,-8){\makebox(0,0)[c]{\small $0$}}
  \put(93,-1){\makebox(0,0)[b]{\small $\bullet$}}
  \put(93,-8){\makebox(0,0)[c]{\small $1$}}
  \put(180,25){\vector(1,0){50}}
  \put(205,35){\makebox(0,0)[c]{$\tau$}}
  \put(250,0){\includegraphics[scale=0.8,clip]{fig3-6i-2.eps}}
  \put(250,-8){\makebox(0,0)[c]{\small $O$}}
  \put(302,-8){\makebox(0,0)[c]{\small $Q$}}
  \put(312,38){\makebox(0,0)[c]{\small $P$}}
 \end{picture}
 \caption{}
\end{figure}

\noindent It extends to a multivalued analytic function on $\P^1
 \setminus \{0,1,\infty\}$ with value in $\matheur{D}(0,1^-)$. The 
inverse mapping
$z(\tau): \matheur{D}(0,1^-)\to \P^1$ is the (single-valued)
$\Delta(2,4,6)$-automorphic uniformizing mapping of the Shimura orbifold
 $\mathcal{X}^\ast $.
\end{para}

\begin{para}\label{para::6.5.2}  Actually, $\tau$ expresses the period mapping
 $\mathcal{P}$ for ``fake elliptic curves'' with multiplication by 
 $\mathcal{B}_{2.3}$, \cf  II.\ref{sub:1.2} and
 II.\ref{sub:7.4}: more precisely, 
 the multivalued function $\tau(z)$ is related to 
 the commutative diagram  
 \begin{equation*}
  \begin{CD}
   \widetilde{{\mathcal{X}^\ast_\C}^{\mathrm{an}}}
    @>{}^{\begin{subarray}\mathcal{P}\\\sim\end{subarray}}>>
   \mathcal{D}=\matheur{D}(0,1^-) @. \quad \subset \;\mathcal{D}^\vee=\P^1 \\
   @V\mathcal{Q}VV @VVV\\
   \left(\P^1,\;
   \begin{matrix}
    0& 1& \infty \\
    6& 2& 4
   \end{matrix}
   \right)
   ={\mathcal{X}^\ast_\C}^{\mathrm{an}}
   @>>> \mathcal{D}/\Delta(2,4,6)
  \end{CD}
 \end{equation*}
by
 \begin{equation*}
  \tau(z)= \mathcal{P}\circ {\mathcal{Q}}^{-1},\; z(\tau )= {\mathcal{Q}}\circ
   \mathcal{P}^{-1}.
 \end{equation*} 
\end{para}

\begin{para}\label{para::6.5.3} Using Gauss' formula for the value of
 hypergeometric functions at $1$, one can compute the constant $\kappa$, 
 \cf \cite[392]{f2}:
 \begin{equation*}
 \kappa=\frac{\Gamma (\frac{7}{6})}{\Gamma
  (\frac{5}{6})}\sqrt\frac{\Gamma (\frac{1}{24})\Gamma
  (\frac{7}{24})\Gamma (\frac{13}{24})\Gamma (\frac{19}{24}) 
 }{\Gamma (\frac{5}{24}) \Gamma (\frac{11}{24})\Gamma
 (\frac{17}{24})\Gamma (\frac{23}{24})}. 
 \end{equation*}

 Using the functional equations of $\Gamma$, one checks that $\kappa
 \sim \Bigl(\frac{\Gamma(\frac{1}{3})}{\Gamma(\frac{2}{3})}\Bigr)^3$
 $\pmod{\ovl{\Q}^\times}$, in conformity with II.\ref{thm:7.6.4} (taking into
 account the fact that $z=0$ corresponds to a fake elliptic curve with
 complex multiplication by an order in $M_2(\Q(\sqrt{-3}))$). 
\end{para}

\begin{para}\label{para::6.5.4} For $p\neq 2,3$, the $p$-adic radius of
 convergence of $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)$ and 
 $F(\frac{5}{24}, \frac{11}{24},\frac{7}{6}; z)$ is $1$. The unit disk
 $|z|_p<1$ is ordinary or supersingular according 
 to whether $p\equiv 1$ $\pmod{3}$ or not. The ratio 
 $\frac{z^{1/6}F(\frac{5}{24}, \frac{11}{24},\frac{7}{6}; z)
 }{F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)}$ expresses a local 
 $p$-adic period mapping. 

 The $p$-divisible group of the fake elliptic curve parametrized by $z$
 is isogenous to the square of the $p$-divisible group of an elliptic
 curve; the period 
 mapping is thus completely analogous to one of those studied 
 in II.\ref{para:6.3.1}, \ref{para:6.3.3} (Dwork, 
 Gross-Hopkins). From the viewpoint of analytic continuation, this is
 essentially the situation studied in  I.\ref{sec-tale} 
 (for $F(\frac{1}{2},\frac{1}{2},{1}; z)$).
\end{para}

\begin{para}\label{para::6.5.5} For $p=3$ (\resp $p=2$), the
 situation is radically different; the $p$-adic radius of convergence of 
 $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)$ and
 $F(\frac{5}{24}, \frac{11}{24},\frac{7}{6}; z)$ is $3^{-3/2}$
 (\resp $2^{-6}$).

 The ratio
 $ \frac{z^{1/6}F(\frac{5}{24},\frac{11}{24},\frac{7}{6}; z)}
 {F({\frac{1}{24},{\frac{7}{24}},\frac{5}{6}}; z)}$
 expresses the Drinfeld $3$-adic period mapping: 

 \begin{center}
  \begin{picture}(120,125)(0,-10)
   \put(45,105){\makebox(0,0)[c]{${}^\mathcal{P}$}}
   \put(45,95){\makebox(0,0)[c]{$\sim$}}
   \put(0,90){\makebox(0,0)[c]{$\til{\mathcal{X}^+(2)_{\C_3}^{\mathrm{an}}}$}}
   \put(0,75){\vector(0,-1){15}}
   \put(0,45){\makebox(0,0)[c]{${\mathcal{X}^+(2)}_{\C_3}^{\mathrm{an}}$}}
   \put(0,30){\vector(0,-1){15}}
   \put(0,0){\makebox(0,0)[c]{${\mathcal{X}^{\ast\,\mathrm{an}}_{\C_3}}2$}}
   \put(30,90){\vector(1,0){30}}
   \put(80,90){\makebox(0,0)[dc]{$\mathcal{D}$}}
   \put(97,90){\makebox(0,0)[c]{$\subset$}}
   \put(110,90){\makebox(0,0)[dl]{$\mathcal{D}^{\vee}=\P^1$}}
   \put(80,75){\vector(0,-1){60}}
   \put(80,0){\makebox(0,0)[c]{$\mathcal{D}/\Delta_3(2,4,6)$}}
   \put(25,0){\vector(1,0){15}}
  \end{picture}
 \end{center}

 \noindent 
 Here $\mathcal{D}$ is the image of the Drinfeld space $\Omega_{\C_3}$
 by a suitable homography (it would be interesting to 
 determine this homography explicitly). That this homography is actually
 defined over $\ovl{\Q}$ 
 comes from II.\ref{thm:7.6.4} (ramified variant), I.\ref{para-ramif},
 \ref{thm-cm-period} (the point is
 that the triadic periods, in the sense of
 I.\ref{sub-p-adic-betti-lattice-supersing}, of the abelian surface 
 with complex multiplication by $M_2(\Q[\sqrt{-3}])$ parametrized by
 $z=0$, belong to $\ovl{\Q}$).

 \bigskip Although $F(\frac{5}{24}, \frac{11}{24},\frac{7}{6};
 z)/F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)$ has very small triadic
 radius of convergence, its pull-back on the Shimura curve
 $\mathcal{X}^+(2)$ extend to a global multivalued meromorphic
 function, with poles only above $0,1,\infty$ (in other words, its
 pull-back on $\widetilde{\mathcal{X}^+(2)}_{\C_3} \cong \Omega_{\C_3}$
 is single-valued).

 Note however that the same is not true for $F(\frac{1}{24},
 \frac{7}{24},\frac{5}{6}; z)$ and $F(\frac{5}{24},
 \frac{11}{24},\frac{7}{6}; z)$ individually, for reasons of exponents
 at $\infty$.  Nevertheless, they enjoy a similar property, on replacing
 $\mathcal{X}^+(2)$ by a suitable ramified finite covering.

 \medskip Similarly, in the diadic case: the pull-back of
 $F(\frac{5}{24}, \frac{11}{24},\frac{7}{6}; z)/F(\frac{1}{24},
 \frac{7}{24},\frac{5}{6}; z)$ on the Shimura curve $\mathcal{X}^+(3)$
 extends to a global multivalued meromorphic functions (with poles only
 above $0,1,\infty$).
\end{para}
