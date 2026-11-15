---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-025-62-symplectic-action
section_title: "Symplectic action"
section_number: 6.2
pages: 62-65
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.968
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:CSsymp label="sec:CSsymp"}

We would like to define an affine symplectic action on the Hilbert space $\mathcal{H}\equiv \mathcal{H}_{0,s}$ (or products thereof) that intertwines an obvious symplectic action in the algebra of operators [\[CSops\]](#CSops){reference-type="eqref" reference="CSops"}. This was already done in Section [\[sec:actions\]](#sec:actions){reference-type="ref" reference="sec:actions"} for the index, but we want to rediscover it here from the point of view of Chern-Simons theory and geometric quantization.

Fortunately, a holomorphic version of the desired symplectic action was defined in [@Dimofte-QRS]. There, the relevant tetrahedron (say) phase space was viewed as a complexification of $\big(\mathcal{P}_{\mathbb R},\tfrac{i}{2\hbar}\Omega_{\mathbb R}\big)$, where $\mathcal{P}_{\mathbb R}$ is the slice of $\mathcal{P}$ with $X,\,P\in {\mathbb R}$, and $\Omega_{\mathbb R}$ is the corresponding real restriction of the holomorphic symplectic form [\[Omega\]](#Omega){reference-type="eqref" reference="Omega"}. Quantization then produced a Hilbert space $\mathcal{H}^{SL(2)}\simeq L^2({\mathbb R})$ containing functions $f(X;\hbar)$. Actual Chern-Simons wavefunctions had the additional property that they were locally *analytic* in $X$ and $\hbar$. Such analytic "$SL(2)$" wavefunctions were identified with ellipsoid partition functions of theories $T_M$ in [@Yamazaki-3d; @DG-Sdual; @DGG].

We recall from [@Dimofte-QRS] that the symplectic group $Sp(2,{\mathbb Z})$ acted on wavefunctions $f(Z;\hbar)$ in the Weil representation [@Shale-rep; @Weil-rep]. In particular, the generators $T$ and $S$ were implemented as

$$\label{SpSL}
\begin{align} T\;&:\quad f(X;\hbar)\;\mapsto\; (T\circ f)(X';\hbar)= e^{\frac{1}{2\hbar}X'^2}f(X;\hbar)\,, \\
S\;&:\quad f(X;\hbar)\;\mapsto\; (S\circ f)(X';\hbar)= \frac{1}{\sqrt{2\pi i\hbar}}\int_{\mathbb R}dX\, e^{\frac{1}{\hbar}XX'} f(X;\hbar)\,.
\end{align}$$

These generate a projective representation of $Sp(2,{\mathbb Z})$ on $L^2({\mathbb R})$ --- projective because the group relations $(ST)^3=id$ and $S^2=C$ only hold up to a phase.

In the present case of $SL(2,{\mathbb C})$ Chern-Simons at $k=0$, the complex phase space $(\mathcal{P},\omega_{0,s})$ can roughly

[^1]

be considered a product of holomorphic and antiholomorphic copies of $\big(\mathcal{P}_{\mathbb R},\pm\tfrac{i}{2\hbar}\Omega_{\mathbb R}\big)$. This is easy to see from the expression [\[ws1\]](#ws1){reference-type="eqref" reference="ws1"} for $\omega_{0,s}$. We can then guess what the appropriate symplectic action on $(\mathcal{P},\omega_{0,s})$ should be by combining holomorphic and antiholomorphic copies of [\[SpSL\]](#SpSL){reference-type="eqref" reference="SpSL"}.

For example, let us work in representation $(b)$ of the Hilbert space $\mathcal{H}$, so that wavefunctions $f^{(b)}(x,\overline x;q)$ depend non-holomorphically on $x=\exp(X)$. The natural guess for the $T$ action is

$$T\;:\quad f(x,\overline x;q)\;\mapsto\; (T\circ f)(x',\overline x';q) = e^{\frac{1}{2\hbar}X'^2-\frac{1}{2\hbar}\overline X'^2}f(x',\overline x';q)\,, \label{Ts}$$

with $X'=\log x'$. It is important to check that the right-hand side of [\[Ts\]](#Ts){reference-type="eqref" reference="Ts"} is still an element of $\mathcal{H}$, namely that it is periodic as $X'\to X'+2\pi i$, and that ${\rm Re}\,X' \in \tfrac\hbar2{\mathbb Z}$ is quantized. The latter condition is automatic, since $f(x,\overline x;q)$ was only initially defined for ${\rm Re}\,X = \log |x| \in \tfrac\hbar2{\mathbb Z}$; so let us set ${\rm Re}\,X' = m'\tfrac\hbar 2$. Then the exponential in [\[Ts\]](#Ts){reference-type="eqref" reference="Ts"} becomes

$$e^{\frac{1}{2\hbar}X'^2-\frac{1}{2\hbar}\overline X'^2} = e^{im'\,{\rm Im}\,X'}\,,$$

enforcing the required periodicity in ${\rm Im}\, X'$.

Similarly, a first guess for the $S$ transformation would be

$$S\;:\quad f(x,\overline x;q)\;\overset{?}{\mapsto}\; (S\circ f)(x',\overline x';q)=\int dX\,d\overline X\,e^{\frac1\hbar XX'-\frac1\hbar \overline X\overline X'}f(x,\overline x;q)\,, \label{Ss1}$$

with some appropriate normalization. Now, setting ${\rm Re}\,X = m\tfrac\hbar2$ and ${\rm Re}\,X'=m'\tfrac\hbar2$, the exponent becomes $\tfrac1\hbar XX'-\tfrac1\hbar \overline X\overline X'=im'\,{\rm Im}\,Z+im\,{\rm Im}\,X'$ . Therefore, quantization of ${\rm Re}\,X$ ensures periodicity in ${\rm Im}\,X'$, while requiring quantization of ${\rm Re}\,X'$ makes the entire integrand in [\[Ss1\]](#Ss1){reference-type="eqref" reference="Ss1"} periodic in ${\rm Im}\,X$. This is almost as desired, except that the integration measure $\int dX\,d\overline X$ does not quite make sense. The correct interpretation of $\int dX\,d\overline X$ is as an integration over a fundamental domain where $f(x,\overline x;q)$ is defined, *i.e.* $\int dX\,d\overline X \,\to\, \sum_{m\in {\mathbb Z}}\int_0^{2\pi} d\,{\rm Im}X$ . If we use the notation $x = q^{\frac m2}\zeta,\,\overline x'=q^{\frac {m'}2}\zeta'$, then the proper transformation becomes

$$S\;:\quad f(m,\zeta;q)\;\mapsto\; (S\circ f)(m',\zeta';q) = \sum_{m\in {\mathbb Z}} \int \frac{d\zeta}{2\pi i\zeta}\,\zeta^{m'}{\zeta'}^mf(m,\zeta;q)\,, \label{Ss2}$$

with integration done over the unit circle. The normalizations in [\[Ts\]](#Ts){reference-type="eqref" reference="Ts"} and [\[Ss2\]](#Ss2){reference-type="eqref" reference="Ss2"} are just right to ensure that $T$ and $S$ generate a true representation of $Sp(2,{\mathbb Z})$ acting on our Hilbert space $\mathcal{H}$.

It should now be clear that the transformations [\[Ts\]](#Ts){reference-type="eqref" reference="Ts"}--[\[Ss2\]](#Ss2){reference-type="eqref" reference="Ss2"} coincide with the $Sp(2,{\mathbb Z})$ action on the index, described in [@KW-index] and in Section [\[sec:Sp\]](#sec:Sp){reference-type="ref" reference="sec:Sp"} above. To make the correspondence even clearer, we could use a "charge basis" for wavefunctions in $\mathcal{H}$, option $(d)$ of Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"}. Using Fourier transform to relate polarizations $(b)$ and $(d)$, we then recover the more familiar symplectic action

$$T\;:\; f(m,e;q)\;\mapsto\; f(m'-e',e';q)\,, \qquad S\;:\; f(m,e;q)\;\mapsto\; f(e',-m';q)\,,$$

or more generally,

$$g\;:\; f(m,e;q)\;\mapsto\; f\big( g^{-1}\!\cdot\! \big(\begin{smallmatrix} m\\e\end{smallmatrix}\big);q)\,,$$

*cf.* [\[Spem\]](#Spem){reference-type="eqref" reference="Spem"}. This last expression generalizes nicely to an $Sp(2N,{\mathbb Z})$ action on products of Hilbert spaces $\mathcal{H}$.

Note that both the options $(a\!-\!d)$ in Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"} and the present $Sp(2,{\mathbb Z})$ action can be understood as choices of basis in $\mathcal{H}$, or of polarization for $\mathcal{P}$. More precisely, it is a choice of element $g\in Sp(2,{\mathbb Z})$ together with a choice $(a\!-\!d)$ from Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"} that fully determines a polarization. The two choices are largely independent. The element $g\in Sp(2,{\mathbb Z})$ acts *holomorphically* on the phase space $\mathcal{P}$, viewed as ${\mathbb C}^*\times {\mathbb C}^*$, and makes a rough selection of "position" ($X'$) and "momentum" ($P'$) coordinates, with $\left(\begin{smallmatrix} X'\\ P'\end{smallmatrix}\right) = g\left(\begin{smallmatrix} X\\ P\end{smallmatrix}\right)$. The choice $(a\!-\!d)$ then splits the real and imaginary parts of $X'$ and $P'$ to provide a specific real polarization for $(\mathcal{P},\omega_{0,s})$. In terms of an index, the former comes from an $Sp(2,{\mathbb Z})$ action on 3d SCFT's, while the latter is a choice of fugacity-vs-charge basis for writing the index. The one relation between the two choices is that switching $(b)\leftrightarrow(c)$ is equivalent to applying $S\in Sp(2,{\mathbb Z})$.

In addition to a symplectic action, both Chern-Simons theory and the index require an action of affine shifts. In the holomorphic version of Chern-Simons theory discussed in [@Dimofte-QRS], such shifts in position or momentum always came in multiples of $i\pi+\tfrac\hbar2$, with $i\pi$ the classical shift and $\hbar/2$ a quantum correction. Now, for full $SL(2,{\mathbb C})$ Chern-Simons theory, we would expect a shift $\sigma_X$ in position $X$ to act as

$$\sigma_X\,:\,f(x,\overline x;q)\;\mapsto\; f(-q^{-\frac12}x,-q^{\frac12}\overline x;q)\,,\quad\text{or}\quad  \sigma_X\,:\,f(m,\zeta;q)\;\mapsto\; f(m,-q^{-\frac12}\zeta;q)\,,$$

intertwining the operator algebra transformation $\big(\hat X,\hat{\overline X}\big)\mapsto \big(\hat X+i\pi+\tfrac\hbar2,\hat {\overline X}-i\pi-\tfrac\hbar2\big)$. Note that the quantum correction has a different sign for the holomorphic and antiholomorphic coordinates, due to the opposite signs appearing in the symplectic structure $\omega_{0,s}$ [\[ws1\]](#ws1){reference-type="eqref" reference="ws1"}. Similarly, a shift by $i\pi +\tfrac\hbar2$ in momentum $P$ acts as

$$\sigma_P\,:\,f(x,\overline x;q)\;\mapsto\; e^{\frac1\hbar X(i\pi+\frac\hbar 2)-\frac1\hbar X(-i\pi-\frac\hbar 2)}f(x,\overline x;q) = \big(-q^{\frac12}\big)^mf(x,\overline x;q)\,.$$

Again, these transformations are consistent with the combined fermion number and R-charge shifts of the index defined in Section [\[sec:aff\]](#sec:aff){reference-type="ref" reference="sec:aff"}.

In contrast to analytically continued Chern-Simons theory, where the representation of the affine symplectic group on wavefunctions is only projective, and leads to normalization ambiguities for wavefunctions of 3-manifolds, the present actions in $SL(2,{\mathbb C})$ Chern-Simons theory at $k=0$ define a true, faithful representation of $Sp(2,{\mathbb Z})\ltimes \big[\big(i\pi+\tfrac\hbar2\big){\mathbb Z}\big]^2$ on $\mathcal{H}$. It is straightforward to check that group relations such as [\[affrels\]](#affrels){reference-type="eqref" reference="affrels"} hold on the nose. More generally, we have a true representation of $Sp(2N,{\mathbb Z})\ltimes \big[\big(i\pi+\tfrac\hbar2\big){\mathbb Z}\big]^{2N}$ on $\mathcal{H}^{\otimes N}$. Therefore, wavefunctions obtained via a symplectic gluing procedure --- the procedure outlined in Section [\[sec:rules\]](#sec:rules){reference-type="ref" reference="sec:rules"} --- should be unambiguously defined. As already mentioned above, invariance of gluing under 2-3 moves completely fixes the normalization of the basic building block for any triangulated 3-manifold, the wavefunction of tetrahedron.

The final step in constructing wavefunctions for a triangulated 3-manifold is a "symplectic reduction," the quantum equivalent to setting internal edge coordinates $C_I\to 2\pi i$. We finish this discussion by commenting briefly on it. In the analytically continued Chern-Simons theory, the reduction is implemented by transforming a wavefunction to a (holomorphic) polarization such that $C_I$ is a position coordinate, and simply setting $C_I \to 2\pi i +\hbar$, where the '$+\hbar$' is the usual quantum correction. For the non-holomorphic $SL(2,{\mathbb C})$ wavefunction, this translates to setting $C_I\to 2\pi i+\hbar \simeq \hbar$ and $\overline C_I \to -2\pi i-\hbar\simeq -\hbar$; or, with $x_I = e^{C_I} = q^{\frac{m_I}{2}}\zeta_I$, setting $m_I\to 0$ and $\zeta_I \to q$. In a charge basis, this means

$$\text{reduction\,:}\qquad \mathcal{Z}(m_I,m,e_I,e;q)\;\mapsto\; \sum_{e_I\in {\mathbb Z}} q^{e_I}\mathcal{Z}(0,m,e_I,e;q)\,,\qquad$$

just as in [\[indsum\]](#indsum){reference-type="eqref" reference="indsum"}, the last step of the index gluing rules. This completes the argument that the Chern-Simons wavefunction at $k=0$ is fully equivalent to the index.

[^1]: A precise statement is that the analytic continuation of $(\mathcal{P},\omega_{0,s})$, with independent complex coordinates $X,P$ and $\overline X,\overline P$, is isomorphic to $(\mathcal{P},\tfrac{i}{2\hbar}\Omega)\times(\mathcal{P},-\tfrac{i}{2\hbar}\Omega)$. We do *not* want to analytically continue anything here, though.
