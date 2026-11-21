---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-004-23-geodesic-boundaries
section_title: "Geodesic boundaries"
section_number: 2.3
pages: 13-17
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.997
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:geobdy label="sec:geobdy"}

We proceed to provide some details of the phase spaces $\mathcal{P}_{\partial M}$ associated to the various types of boundary for $M$, and to give explicit examples of their construction. A more complete, mathematical analysis of boundaries and phase spaces will appear in [@DGGV-hybrid].

It is perhaps simplest to begin with geodesic boundaries. As discussed above, these arise when tetrahedra $\Delta_i$ are impartially glued; then some tetrahedron faces are left over to form one or more disjoint boundaries $\mathcal{C}\subset \partial M$, each a triangulated, punctured Riemann surface. The punctures are places where vertices of the tetrahedra $\Delta_i$ are located, and can ultimately be regularized into cusps that end on $\mathcal{C}$ --- we will say a bit more about this later. The induced 2d triangulation of $\mathcal{C}$ is "ideal" in the sense that all edges begin and end on punctures.

The phase space $\mathcal{P}_\mathcal{C}$, a factor in $\mathcal{P}_{\partial M}$, is the moduli space of flat $SL(2,{\mathbb C})$ connections on $\mathcal{C}$, with specified (fixed) holonomy eigenvalues at every puncture. These eigenvalues become central elements in the algebra of functions on $\mathcal{P}_\mathcal{C}$. Geometrically, we can also describe $\mathcal{P}_\mathcal{C}$ as the complexified Teichmüller space of $\mathcal{C}$, a complexification of the moduli space of 2-dimensional hyperbolic metrics. From this perspective, the puncture eigenvalues reflect the geometric size of holes in $\mathcal{C}$.

We can construct coordinates on $\mathcal{P}_\mathcal{C}$ by associating to every edge $E$ in the triangulation of $\mathcal{C}$ the total complexified dihedral angle around it.

[^1]

In other words,

$$\text{edge $E$}\;\;\leadsto\;\;
 \text{coordinate $X_E$} = \sum_{i=1}^N\Big[ n(E,i)Z_i+n'(E,i)Z_i'+n''(E,i)Z_i''\Big]\,, \label{defXE}$$

where $n(E,i) \in \{0,1,2\}$ is the number of times an edge of tetrahedron $\Delta_i$ with parameter $Z_i$ coincides with the glued edge $E$, and similarly for $n'(E,i)$ and $n''(E,i)$. This definition is analogous to [\[defCj\]](#defCj){reference-type="eqref" reference="defCj"}, except that now $E$ is an external edge of $M$.

It turns out that the coordinates $X_E$ are already well known mathematically as complexified "shear coordinates" on $\mathcal{P}_\mathcal{C}$ [@Thurston-shear; @Fock-Teich], defined rigorously in [@FG-Teich] in the complex case.

[^2] By following the arguments of [@NZ], one can show that the Poisson structure induced on these edge coordinates is

$$\{X_E,X_{E'}\} = f(E,E')\,, \label{XEbracket}$$

where $f(E,E')\in\{0,\pm 1,\pm 2\}$ is the number of faces shared by edges $E$ and $E'$, counted with orientation (*cf.* Figure [\[fig:Ebracket\]](#fig:Ebracket){reference-type="ref" reference="fig:Ebracket"}). Expression [\[XEbracket\]](#XEbracket){reference-type="eqref" reference="XEbracket"} is precisely the Weil-Petersson Poisson structure on $\mathcal{P}_\mathcal{C}$, *cf.* [@Fock-Teich]. Moreover, for each puncture $p\in \mathcal{C}$, one finds that the sum of edge coordinates encircling the puncture is

$$\sum_{\text{$E$ ending on $p$}} \big(i\pi-X_E\big) = 2(\Lambda_p-i\pi)\,, \label{phol}$$

where $\exp(\pm\Lambda_p)$ are the holonomy eigenvalues at $p$. The elements $\Lambda_p$ form a basis for the center of the Poisson algebra [\[XEbracket\]](#XEbracket){reference-type="eqref" reference="XEbracket"}.

Shear coordinates on $\mathcal{P}_\mathcal{C}$ recently featured prominently in the analysis of BPS states and wall crossing for 4-dimensional $\mathcal{N}=2$ theories associated to punctures Riemann surfaces $\mathcal{C}$ [@GMNII]. In particular, we note that [@GMNII] considered edge coordinates $\mathcal{X}_E = \exp(i\pi-X_E)$, which could be identified as the exponentiated central charges for a generating set of BPS states in 4d gauge theory. The electric-magnetic pairing of BPS charges was given by [\[XEbracket\]](#XEbracket){reference-type="eqref" reference="XEbracket"}.

The simplest example of shear/edge coordinates already appeared above, when we described the phase space $\mathcal{P}_{\partial\Delta}$ [\[PDelta\]](#PDelta){reference-type="eqref" reference="PDelta"} of an ideal tetrahedron. If we view the boundary $\partial\Delta$ as a triangulated four-punctured sphere, we should start with six (logarithmic) edge coordinates $(Z,Z',Z'',W,W',W'')$ that obey a Poisson algebra

$$\begin{aligned}
 &\{Z,Z'\}=\{Z',Z''\}=\{Z'',Z\}=\{Z,W'\} \notag \\ &\quad =\{Z',W''\}=\{Z'',W\}=\{W,Z'\}=\{W',Z''\} \\ &\quad =\{W'',Z\}= \{W,W'\}=\{W',W''\}=\{W'',W\} = \hbar\,, \notag
\end{aligned}$$

according to the faces shared by these edges, with all other brackets vanishing. Then we impose conditions [\[phol\]](#phol){reference-type="eqref" reference="phol"} that the holonomy eigenvalue around each vertex $p$ is $\Lambda_p=2\pi i$ --- in other words, we require that the holonomy be unipotent:

$$W+W'+W''=Z+Z'+W''=Z+W'+Z''=W+Z'+Z''=i\pi$$

This forces opposite edges to have equal parameters, $W=Z,\,W'=Z',\,W''=Z''$, and cuts down the phase space to $\mathcal{P}_{\partial\Delta} = \{(Z,Z',Z'')\,|\,Z+Z'+Z''=i\pi\}$, with Poisson structure [\[DPoisson\]](#DPoisson){reference-type="eqref" reference="DPoisson"}

![Forming a bipyramid from three tetrahedra.](bip3){#fig:bip3 width="4.8in"}

As an example involving a nontrivial gluing, we can consider the "bipyramid" $M$ of Figure [1](#fig:bip3){reference-type="ref" reference="fig:bip3"}. Its boundary is a 5-punctures sphere $\mathcal{C}$. Here, we form the bipyramid from three ideal tetrahedra, with respective shape parameters $Z{}^{(}{}'{}^{)(}{}''{}^{)},\,W{}^{(}{}'{}^{)(}{}''{}^{)},\,Y{}^{(}{}'{}^{)(}{}''{}^{)}$. 

[^3]

This leads to a 6-dimensional product phase space $\mathcal{P}_{\{\partial\Delta_i\}} \approx \{(Z,Z',Z'',W,W',W'',Y,Y',Y'')\}$ with relations $Z+Z'+Z''=W+W'+W''=Y+Y'+Y''=i\pi$. Inside $\mathcal{P}_{\{\partial\Delta_i\}}$ there is a single gluing constraint

$$C \equiv Z+W+Y \,\to\, 2\pi i\, \label{bipC}$$

corresponding to the internal, vertical edge of the bipyramid; it should be used as a symplectic moment map to reduce $\mathcal{P}_{\{\partial\Delta_i\}}$ to the 4-dimensional phase space $\mathcal{P}_{\partial M}=\mathcal{P}_\mathcal{C}$.

Explicitly, coordinates on $\mathcal{P}_\mathcal{C}$ are given by the dihedral angles of the nine external edges of the bipyramid:

$$\label{bipedges}
\begin{equation}Z\,,\quad W,\,\quad Y  \end{equation}

for the three equatorial edges, and

\begin{equation}Z'+W'',\,\quad Z''+W',\,\quad W'+Y''\,,\quad W''+Y'\,,\quad Y'+Z''\,,\quad Y''+Z' \end{equation}$$

for the six longitudinal edges. It is easy to check that, as functions on the product phase space $\mathcal{P}_{\{\partial\Delta_i\}}$, the nine external shear/edge coordinates [\[bipedges\]](#bipedges){reference-type="eqref" reference="bipedges"} all commute with $C$. Moreover, modulo the gluing constraint [\[bipC\]](#bipC){reference-type="eqref" reference="bipC"}, one can check using formula [\[phol\]](#phol){reference-type="eqref" reference="phol"} that the total logarithmic holonomy eigenvalue around each of the five punctures $p$ of $\mathcal{C}$ is $\Lambda_p=2\pi i$. The resulting five relations among the nine external edge coordinates cut the dimension of $\mathcal{P}_\mathcal{C}$ down to four.

As in the case of a single tetrahedron, the punctures on the boundary of the bipyramid carry unipotent holonomy (with logarithmic eigenvalue $2\pi i$). This is related to the fact that, upon truncating tetrahedron vertices as in Figures [\[fig:trunc\]](#fig:trunc){reference-type="ref" reference="fig:trunc"}, [1](#fig:bip3){reference-type="ref" reference="fig:bip3"}, the small vertex triangles come together to form Euclidean 2d discs. These discs effectively cap off the punctures and force unipotent holonomy. In general one can build 3-manifolds that have annular cusps, rather than discs, ending at the punctures of a geodesic boundary. The annular cusps will then allow any holonomy eigenvalues to be realized. Constructions of this type are extremely interesting in the context of 3d and 4d gauge theory, but will mainly be deferred to future work [@DGGV-hybrid].

For simple manifolds such as the tetrahedron and the bipyramid, whose boundaries carry unipotent punctures and whose interiors have the topology of 3-balls, the Lagrangian submanifolds $\mathcal{L}_M\,\subset\,\mathcal{P}_{\partial M}$ are also very simple. They are always cut out by the condition that the puncture holonomies are actually trivial (not just unipotent) --- so that a flat connection on the boundary can be extended to the bulk of $M$.

To conclude the discussion of geodesic boundaries, we observe that several natural polarizations $\Pi$ for a phase spaces $\mathcal{P}_\mathcal{C}$ can be specified by choosing maximal subsets of commuting edges on $\mathcal{C}$. In other words, we choose a maximal set of independent edges that share no common faces. The corresponding coordinates $X_E$ then correspond to "positions" in $\mathcal{P}_\mathcal{C}$. Their conjugate momenta can be constructed (not quite uniquely) as combinations of the remaining edges.

For example, in the case of the bipyramid, two such polarizations are shown in Figure [\[fig:bippol\]](#fig:bippol){reference-type="ref" reference="fig:bippol"}, one using "positions" on equatorial edges and the other on longitudinal edges. (Note that the three equatorial edges all commute, but obey a constraint $Z+W+Y=C=2\pi i$, so only two of them, say $Z$ and $W$, are independent.) The respective positions $X_{1,2}$ and momenta $P_{1,2}$ in these polarizations are summarized as

$$\label{bipcoord3}
 \begin{array}{lc@{\;\;}c@{\qquad}c}
  && \text{positions} & \text{momenta} \\[.1cm]
  \Pi_{\rm eq} &:\;& X_1 = Z\,,\quad X_2=W & P_1 = Z''+Y'\,,\quad P_2 = W''+Y'\,\\[.1cm]
  \Pi_{\rm long} &:\;& X_1'=W'+Y''\,,\quad X_2' =Z'+Y'' & P_1' =Z''+Y'\,,\quad P_2' = W''+Y'\,
\end{array}$$

In equatorial coordinates $(X_i,P_i)$, the Lagrangian $\mathcal{L}_M$ (*i.e.* the set of connections with trivial holonomy) can be shown to have the simple description

$$\mathcal{L}_M\;:\qquad p_1+\frac{p_2}{x_1}-1=0\,,\qquad p_2+\frac{p_1}{x_2}-1=0\,, \label{Lbipeq}$$

while in longitudinal coordinates we have

$$\mathcal{L}_M\;:\qquad p_1'+x_1'^{-1}-1=0\,,\qquad p_2'+x_2'^{-1}-1=0\,,$$

with $x_i=\exp(X_i)$, $p_i=\exp(P_i)$, etc.

Different polarizations for a geodesic boundary phase space $\mathcal{P}_\mathcal{C}$ are related to one another by affine $Sp(\dim_{\mathbb C}\mathcal{P}_\mathcal{C},{\mathbb Z})$ transformations. From the above discussion, it should be easy to see that the complex dimension of $\mathcal{P}_\mathcal{C}$ must be

$$\dim_{\mathbb C}\,\mathcal{P}_\mathcal{C}= (\text{\# external edges on $\mathcal{C}$})-(\text{\# punctures on $\mathcal{C}$})\,,$$

which by an Euler character argument agrees with the standard formula $\dim_{\mathbb C}\,\mathcal{P}_\mathcal{C}= 6g-6+2n$, where $g$ is the genus and $n$ is the number of punctures of $\mathcal{C}$. The affinely extended group $Sp(6g-6+n,{\mathbb Z})$ is a subgroup of the full affine group $Sp(2N,{\mathbb Z})$ of transformations on the product phase space $\mathcal{P}_{\{\partial\Delta_i\}}=\prod_{i=1}^N\mathcal{P}_{\partial\Delta_i}$. Therefore, we can always choose a polarization of $\mathcal{P}_{\{\partial\Delta_i\}}$ that is compatible with the final desired polarization of the quotient space $\mathcal{P}_\mathcal{C}$.

[^1]: In fact, these are coordinates on algebraically open patches of $\mathcal{P}_\mathcal{C}$ that have the topology of complex tori, *cf.* [@FG-Teich; @GMNII].

[^2]: We thank R. Kashaev for first making us aware of this connection.

[^3]: Any solid 3-ball whose boundary is an $n$--punctured sphere ($n\geq 4$), with unipotent holonomy at each puncture, can be obtained via a similar gluing.
