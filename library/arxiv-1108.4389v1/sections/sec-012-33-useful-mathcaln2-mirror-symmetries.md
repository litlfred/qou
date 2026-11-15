---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-012-33-useful-mathcaln2-mirror-symmetries
section_title: "Useful $\mathcal{N}=2$ mirror symmetries"
section_number: 3.3
pages: 25-30
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.984
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:MS label="sec:MS"}

From the above, it should be clear that the $\mathcal{N}=4$ $S$ operation consists of a combination of $\mathcal{N}=2$ $S$ and $F$ operations. Indeed, the $\mathcal{N}=4$ conserved current supermultiplet contains a complex moment map operator $\mu$, which is a chiral operator for an $\mathcal{N}=2$ subalgebra. The $\mathcal{N}=4$ gauge multiplet contains an $\mathcal{N}=2$ chiral multiplet $\phi$, which is coupled to the complex moment map operator $\mu$ by the superpotential coupling $$\mathcal{W}= \phi \mu \,.$$ Thus, for example, the basic $\mathcal{N}=4$ mirror symmetry statement of Section [\[sec:susySp\]](#sec:susySp){reference-type="ref" reference="sec:susySp"} can be recast as a statement about a 3d $\mathcal{N}=2$ theory $\mathcal{T}_2$ of two chiral multiplets $u$ and $\tilde u$ with opposite flavor charges, and an operator $\mathcal{O}= \mu = u \tilde u$. This theory is invariant under the combined $\mathcal{N}=2$ $S$ and $F$ operations, *i.e.* it satisfies $S F \circ \mathcal{T}_2 = \mathcal{T}_2$.

A basic consequence, pointed out in [@AHISS; @dBHO], is that the two theories that are obtained from a $S$ operation or from a $F$ operation on the theory of two chiral multiplets are actually the same in the IR, *i.e.* they are $\mathcal{N}=2$ mirror duals.[^1] The theory $S \circ \mathcal{T}_2$ is just $\mathcal{N}=2$ SQED with $N_f=1$. The theory $F \circ \mathcal{T}_2$, or rather $CF \circ \mathcal{T}_2$, is the so-called XYZ model, a theory of three chiral fields $\phi$, $u$, $\tilde u$ with a superpotential $$\mathcal{W}= \phi u \tilde u \,.
\label{Wuuu}$$ These two theories are mirror to each other: $$\begin{array}{ll}
\text{\bf SQED}~(S\circ \mathcal{T}_2): & \quad \text{gauged $U(1)$ with two chirals of charge} \; +1 \; \text{and} \; -1 \;  \\[.1cm]
\text{\bf XYZ}~(CF\circ \mathcal{T}_2): & \quad \text{three chirals with superpotential} \; \mathcal{W}= \phi u \tilde u
\end{array} \label{XYZmir}$$

There is actually a bit more structure to this problem. In $\mathcal{N}=2$ language, each of the two chiral multiplets in $\mathcal{T}_2$ can be rotated independently, and the theory really has $U(1)^2$ flavor symmetry. Similarly, the XYZ model has a $U(1)^2$ flavor symmetry that rotates the phase of $\phi$, $u$, $\tilde u$ and leaves the superpotential $\mathcal{W}$ invariant. The two $U(1)$'s map via the mirror symmetry [\[XYZmir\]](#XYZmir){reference-type="eqref" reference="XYZmir"} to an axial $U(1)$ and a topological $U(1)$ in $N_f=1$ SQED. In terms of SQED, the topological $U(1)$ symmetry is carried by two chiral monopole operators $v_\pm$ with charges $\pm 1$. It is slightly nontrivial (*cf.* [@AHISS]) to see that the monopole operators also transform with charge $-1$ under the axial $U(1)$. We summarize these various flavor symmetries in Table [\[tab:charges\]](#tab:charges){reference-type="ref" reference="tab:charges"}.

$$\begin{array}{l@{\;}|@{\;}cc@{\;}|@{\;}ccc}
\multicolumn{6}{c}{\text{$N_f=1$ SQED}} \\[.1cm]
& u & \tilde u & \mu & v_+ & v_- \\\hline
U(1)_{\rm gauge} & 1 & -1 & 0 & 0 & 0 \\
U(1)_{\rm axial} & 1 & 1 & 2 & -1 & -1 \\
U(1)_{\rm top} & 0 & 0 & 0 & 1 & -1
\end{array} \qquad\qquad

\begin{array}{l@{\;}|@{\;}ccc}
\multicolumn{4}{c}{\text{XYZ}} \\[.4cm]
& \phi & u & \tilde{u} \\\hline
U(1)_{\rm axial} & 2 & -1 & -1\\
U(1)_{\rm top} & 0 & 1 & -1
\end{array}
\notag$$

Eventually, we will investigate the properties of these theories under $Sp(4,{\mathbb Z})$ transformations. For now, we would like to derive yet another useful $\mathcal{N}=2$ mirror pair by a mass deformation of this theory.

We aim to understand the properties of a simple theory, consisting of a single chiral multiplet $\phi$ of charge $1$. In order to define a coupling to a background gauge field, we need to face a subtlety: a single chiral multiplet canonically coupled to a background gauge field has an anomaly, which can be cancelled by adding a half-integral Chern-Simons coupling for the background gauge field. This fact is closely related to another important fact. If we integrate out a massive chiral multiplet coupled with charge $q$ to a background gauge field, we generate an effective (supersymmetric) Chern-Simons interaction at level $k = \tfrac{1}{2}\,q^2\,{\rm sign} (m)$.

Thus we define an $\mathcal{N}=2$ theory $\mathcal{T}_1$ as a chiral field of charge $1$, coupled to a background field with an extra Chern-Simons interaction at level $-\tfrac{1}{2}$. We want to show that $ST \circ \mathcal{T}_1$ coincides with $\mathcal{T}_1$. This is certainly compatible with $(ST)^3 = 1$. In particular, we want to show that a $U(1)$ CS theory at level $k=\tfrac{1}{2}$ coupled to a single chiral multiplet of charge $+1$ is mirror to a free chiral multiplet of charge $+1$. To demonstrate this statement, we will go back to the XYZ model.

![The quantum moduli space of $\mathcal{N}=2$ SQED is identical to the moduli space of vacua in the $XYZ$ model. It has three branches, permuted by the quantum ${\mathbb Z}_3$ symmetry.](moduli3){#fig:moduli3 width="3.4in"}

The XYZ model, or $N_f=1$ SQED, has a triality property. In the XYZ model this is just permutation of the three chiral fields. The theory has three 1-complex-dimensional branches of SUSY vacua. Indeed, the superpotential [\[Wuuu\]](#Wuuu){reference-type="eqref" reference="Wuuu"} leads to the scalar potential $$V \; = \; \Big| \frac{\partial \mathcal{W}}{\partial \phi} \Big|^2 + \Big| \frac{\partial \mathcal{W}}{\partial u} \Big|^2
+ \Big| \frac{\partial \mathcal{W}}{\partial \tilde u} \Big|^2
\; = \; |\phi u|^2 + |\phi \tilde u|^2 + |u \tilde u|^2$$ which is minimized on field configurations where one of the chiral fields has a vev, while the other two vanish. The resulting three branches parametrized by the vevs of $\phi$, $u$, or $\tilde u$ meet at the origin. In the $N_f=1$ SQED, on the other hand, the classical moduli space is controlled by the term $\sigma^2 (|u|^2 + |\tilde u|^2)$ in the scalar potential $$V \; = \; \frac{e^2}{2} \Big( |u|^2 - |\tilde u|^2 - \zeta \Big)^2 + \sigma^2 |u|^2 + \sigma^2 |\tilde u|^2$$ that forces either $\sigma = 0$ or $u = \tilde u = 0$. The quantum corrected moduli space of the $N_f=1$ SQED is the same as that of the XYZ model, as shown in Figure [1](#fig:moduli3){reference-type="ref" reference="fig:moduli3"}. One of the branches in the moduli space of SUSY vacua is the Higgs branch, parameterized by the vev of the meson $\mu =u \tilde u$. The other two are halves of the Coulomb branch, where $\sigma$ is real and positive, or real and negative. The two halves of the Coulomb branch are parameterized by the vevs of the corresponding vortex-creation (monopole) operators.

Now, if one turns on opposite twisted mass

[^2]

for two of the chiral fields in the XYZ model, it kills two branches and makes the third smooth: $$\mathcal{M}_{{\rm SUSY}} ~=~~
{\raisebox{-0.7cm}{\includegraphics[width=3.0cm]{moduli1}}\,}$$ In the $N_f=1$ SQED description, this statement can take three equivalent forms. The first form is simple: an FI parameter is the same as a twisted mass for the monopole operators. It kills the Coulomb branch and smoothens the Higgs branch. The other two forms of the statement --- which are really what we need --- are more subtle. We must to turn on twisted masses for the other two choices of flavor symmetry in the XYZ description. They rotate only one of the monopole operators, and the meson.

Let us start with the XYZ model. By consulting Table [\[tab:charges\]](#tab:charges){reference-type="ref" reference="tab:charges"}, we see that if we turn on a large and (say) positive twisted mass $m_{\rm axial}$ for the axial $U(1)$, and an equal mass $m_{\rm top}$ for the "topological" $U(1)$,

$$m_{\rm axial} \approx m_{\rm top} \gg 0\,,$$

we can integrate out the chirals $\phi$ and $\tilde u$. We are left with a single free chiral $u$, which still transforms under the difference of $U(1)_{\rm top}$ and $U(1)_{\rm axial}$. Explicitly, defining a new background gauge multiplet $V_{\rm top}'\equiv V_{\rm top}-V_{\rm axial}$, which can still have a small twisted mass parameter $m_{\rm top}'=m_{\rm top}-m_{\rm axial}$, we find that $u$ is coupled to $V_{\rm top}'$ with charge $1$. Integrating out the multiplet $\tilde{u}$ generates a background Chern-Simons term $\frac{k}{4\pi}\int d^4\theta\,\Sigma_{\rm top}'\,V_{\rm top}'$ at level $k=-1/2$. Thus we obtain our theory $\mathcal{T}_1$. (Alternatively, we could have chosen $m_{\rm axial}=-m_{\rm top}\gg 0$, which would allow us to integrate out $u$ and keep $\tilde u$. This leads to an equivalent description of $\mathcal{T}_1$.)

In terms of $N_f=1$ SQED, the topological mass $m_{\rm top}\approx-m_{\rm axial}$ becomes an FI parameter

$$\frac{2}{4\pi}\int d^4\theta\, \Sigma_{\rm top}\,V_{\rm gauge}\,=\, \frac{1}{2\pi}\int d^4\theta\,m_{\rm top}\,V_{\rm gauge}\,. \label{SQEDFI}$$

It is this large FI term which ultimately allows us to keep the monopole $v_+$ light. This may look a bit mysterious, but it is easily motivated by looking at what happens to the fundamental matter fields of $N_f=1$ SQED in the presence of a large axial mass. Both $u$ and $\tilde u$ become very heavy, unless we tune $\sigma$ to $\pm m_{\rm axial}$, so that either $\tilde u$ is light and $u$ is heavy, or vice versa. Let us choose $\sigma=-m_{\rm axial}$; or, more appropriately, let us redefine the dynamical gauge multiplet as $V_{\rm gauge}\to V_{\rm gauge}-V_{\rm axial}=V_{\rm gauge}-\theta\bar\theta\, m_{\rm axial}$. Then we can integrate out $\tilde u$, and in the process generate a Chern-Simons term of level $1/2$ for the combination $-V_{\rm gauge}+2V_{\rm axial}$, under which $\tilde u$ is charged. Hidden in the cross-term of the supersymmetric Chern-Simons interaction is an FI term $-\frac{1}{2\pi}\int d^4\theta\,m_{\rm axial}\,V_{\rm gauge}$, which cancels [\[SQEDFI\]](#SQEDFI){reference-type="eqref" reference="SQEDFI"}, leaving behind a small difference $\frac{1}{2\pi}\int d^4\theta\,m_{\rm top}'\,V_{\rm gauge}$ ! Thus we end up with a fundamental chiral $u$, coupled with charge $1$ to a $U(1)$ gauge multiplet $V_{\rm gauge}$, which has a level $\frac12$ Chern-Simons interaction $\frac{1}{8\pi}\int d^4\theta\,\Sigma_{\rm gauge}\,V_{\rm gauge}$. The theory has a single light monopole operator $v_+$, transforming with charge $1$ under the new topological $U(1)_{\rm top}'$. This is precisely the description of $ST\circ \mathcal{T}_1$. We have therefore derived

$$\boxed{ST\circ \mathcal{T}_1 \,\simeq\, \mathcal{T}_1} \label{STmir}$$

as a consequence of the basic $\mathcal{N}=2$ mirror symmetry [\[XYZmir\]](#XYZmir){reference-type="eqref" reference="XYZmir"}.

In section [\[sec:dualities\]](#sec:dualities){reference-type="ref" reference="sec:dualities"}, we discussed the interpretation of the $Sp(2N,{\mathbb Z})$ action on a 3d theory $\mathcal{T}$ as the action of electric-magnetic duality in 4d abelian gauge theory on a corresponding boundary condition $\mathcal{B}[\mathcal{T}]$. In this interpretation, our simple 3d theory $\mathcal{T}_1$ can define a boundary condition for a 4d theory with gauge group $U(1)$ --- by identifying the 4d gauge symmetry with the 3d flavor symmetry. If we start with a 4d duality frame in which the chiral multiplet of $\mathcal{T}_1$ carries 4d electric charge, then by acting with $SL(2,{\mathbb Z})$ duality we obtain all other variants of the theory $\mathcal{T}_1^{(p,q)}$, where a distinguished chiral operator transforms as a dyon of electric charge $p$ and magnetic charge $q$. In particular, the $ST$ element of $SL(2,{\mathbb Z})$ acts as $$\mathcal{T}_1^{(1,0)} \; \xrightarrow{ST} \;
\mathcal{T}_1^{(0,1)} \; \xrightarrow{ST} \;
\mathcal{T}_1^{(-1,1)} \; \xrightarrow{ST} \;
\mathcal{T}_1^{(1,0)}\,.
\label{STonT1}$$ The mirror symmetry [\[STmir\]](#STmir){reference-type="eqref" reference="STmir"} actually guarantees that, just like $\mathcal{T}_1^{(1,0)}$, the theories $\mathcal{T}_1^{(0,1)}$ and $\mathcal{T}_1^{(-1,1)}$ are equivalent to theories of free chirals coupled to the appropriate (magnetic or dyonic) 4d $U(1)$ gauge field with Chern-Simons level $-\frac12$. The chain of equivalences [\[STonT1\]](#STonT1){reference-type="eqref" reference="STonT1"} should remind us of [\[tetpols\]](#tetpols){reference-type="eqref" reference="tetpols"}.\
This concludes our quick tour of the basic operations and mirror symmetries in 3d $\mathcal{N}=2$ gauge theories. Of particular importance in the rest of the paper is the basic relation $ST \circ \mathcal{T}_1 = \mathcal{T}_1$ and the mirror symmetry between the XYZ model and $N_f=1$ SQED. These basic duality relations admit many generalizations in various directions (to theories that include larger gauge groups and / or larger spectrum of matter fields), which have an elegant interpretation in terms of triangulations of 3-manifolds.

One simple generalization, which we mention only briefly, is that the XYZ model and $N_f=1$ SQED appear as the first mirror pair in the infinite family of mirror abelian gauge theories: $$\begin{aligned}

\text{\bf Theory A}~: & \quad U(1)^r \; \text{with} \; k \; \text{neutral chirals and} \; N \; \text{charged hypermultiplets} \label{mirrorR} \\
\text{\bf Theory B}~: & \quad \widehat{U(1)}{}^{N-r} \; \text{with} \; N-k \; \text{neutral chirals and} \; N \; \text{charged hypermultiplets} \notag 
\end{aligned}$$ where the charges of the hypermultiplets in the two theories, $R_i^a$ and $\widehat R_i^a$, obey the "orthogonality" constraints $$\sum_{i=1}^N R_i^a \widehat R_i^b = 0 \qquad \forall \; a, b \,.
\label{rrmirror}$$ In addition, both mirror theories A and B have gauge invariant cubic superpotential of the form $$\mathcal{W}\; = \; \sum_{\alpha=1}^k \sum_{i=1}^N \; y_{\alpha i} \, \phi_{\alpha} \tilde Q_i Q_i$$ with Yukawa couplings $y_{\alpha i}$ (resp. $\widehat{y}_{\beta i}$) which obey a relation similar to [\[rrmirror\]](#rrmirror){reference-type="eqref" reference="rrmirror"}: $$\sum_{i=1}^N y_{\alpha i} \widehat{y}_{\beta i} = 0 \qquad \forall \; \alpha, \beta \,.$$ All four matrices $R$, $\widehat{R}$, $y$, and $\widehat{y}$ are assumed to be of maximal rank. It is easy to see that if we take $N=r=1$ and $k=0$, then Theory A is $\mathcal{N}=2$ SQED with $N_f=1$, whereas Theory B is the XYZ model. The next simplest case, $N=r=k=1$, gives another prominent pair of mirror 3d theories that we also mentioned earlier: a free hypermultiplet and $\mathcal{N}=4$ SQED. More generally, in this class of examples Theory A contains a total of $2N+k$ chiral multiplets (with charges $-1$, $0$, and $+1$), whereas Theory B contains a total of $3N-k$ chiral multiplets. For this reason, the mirror symmetry of such a mirror pair could be referred to as a "$(2N+k)-(3N-k)$ move."

[^1]: Notice that the coupling of the background gauge field to $\mathcal{T}_2$ is unaffected by charge conjugation $C$.

[^2]: By "twisted mass" in three dimensions, we mean a mass term arising as a background value for the real scalar field in a vector multiplet. Sometimes this is also called a "real mass."
