---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-009-312-adding-supersymmetry
section_title: "Adding supersymmetry"
section_number: 3.1.2
pages: 23-37
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.986
---
[]{#sec:susySp label="sec:susySp"}

The $Sp(2N,{\mathbb Z})$ action can be supersymmetrized to give an $Sp(2N,{\mathbb Z})$ action on supersymmetric 3d theories equipped with a supersymmetric coupling to a background abelian gauge supermultiplet. This can be done for any amount of supersymmetry, but it is important to make a specific choice, as different choices give different group actions.

In the reference [@GW-Sduality] this was applied to theories with $\mathcal{N}=4$ supersymmetry. As a useful example of the $S$ action in the context of $\mathcal{N}=4$ theories, we can consider a single hypermultiplet of unit flavor charge canonically coupled to an $\mathcal{N}=4$ background gauge field. If we make the $\mathcal{N}=4$ background gauge field dynamical --- performing an $S$ operation --- we have a familiar 3d theory: $\mathcal{N}=4$ SQED with one flavor. This is the canonical setup for 3d mirror symmetry [@IS; @dBHOY], which provides an alternative description of the theory in terms of a free twisted hypermultiplet that arises as a monopole operator in the original description. In particular, it carries unit flavor charge under the new $\mathcal{N}=4$ background gauge field. So the transformation $S$ acts rather trivially on this simple 3d theory: it sends it back to itself [@KS-mirror]. On the other hand, $T$ acts non-trivially.

Any $\mathcal{N}=4$ statement can be reinterpreted as an $\mathcal{N}=2$ statement, but a little care is needed: the $\mathcal{N}=4$ 3d gauge multiplet consists of an $\mathcal{N}=2$ 3d gauge multiplet plus a chiral multiplet. The $\mathcal{N}=4$ $Sp(2N,{\mathbb Z})$ action is the combination of an $\mathcal{N}=2$ $Sp(2N,{\mathbb Z})$ action plus additional operations involving 3d chiral multiplets and superpotential couplings. This anticipates a central theme of this paper: the interplay between the "gauge" $Sp(2N,{\mathbb Z})$ action and a "matter" action which involves adding new chiral multiplets with appropriate superpotential couplings. Indeed, the 3d $\mathcal{N}=2$ theories $T_M$ associated to 3-manifolds $M$ with boundary will be coupled both to background gauge fields and background chiral multiplets.

As a first step towards understanding this statement, let us describe the "gauge" $Sp(2N,{\mathbb Z})$ action for $\mathcal{N}=2$ theories. Suppose we have a theory with $U(1)^N$ flavor symmetry, coupled to $N$ background vector multiplets $V_i$. Each $V_i$, containing a real scalar field $\sigma_i$ and two Majorana fermions $\lambda^\alpha_i$ in addition to the gauge field $A_i$, can also be dualized to a linear multiplet [@AHISS; @NishinoGates]

$$V_i\quad\leftrightarrow\quad \Sigma_i = \overline{D}^\alpha D_\alpha V\,,$$

where the lowest component of $\Sigma_i$ is $\sigma_i$. Now, in order to supersymmetrize the $Sp(2N,{\mathbb Z})$ action [\[SpT\]](#SpT){reference-type="eqref" reference="SpT"}--[\[SpGL\]](#SpGL){reference-type="eqref" reference="SpGL"}, one simply has to substitute $AdA'\to V\Sigma'$ for all relevant Chern-Simons or FI terms:

$$\begin{aligned}
 \text{``$T$-type''}\quad g=\begin{pmatrix} I & 0 \\ B & I \end{pmatrix} \;\;&:\qquad \mathcal{L}[\vec{V}]\to\mathcal{L}[\vec{V}_{\rm new}]+\frac{1}{4\pi}\int d^4\theta\,\vec\Sigma_{\rm new} \cdot B\,\vec V_{\rm new}\,; \label{Sp2T} \\

\text{``$S$-type''}\quad g= \begin{pmatrix}I-J & -J \\ J & I-J \end{pmatrix}\;\;&:\qquad \mathcal{L}[\vec V]\to\mathcal{L}[\vec V]+\frac{1}{2\pi}\int d^4\theta\, \vec{\Sigma}_{\rm new}\cdot J\,\vec V\, \label{Sp2S} \\

\text{``$GL$-type''}\quad g = \begin{pmatrix} U & 0 \\ 0 & U^{-1\,t}\end{pmatrix}\;\;&:\qquad \mathcal{L}[\vec V]\to \mathcal{L}[U^{-1}\vec V_{\rm new}]\,. \label{Sp2GL}
\end{aligned}$$ Note that a $GL(N,{\mathbb Z})$ linear transformation $U^{-1}$ can be applied both to a collection of vector multiplets $\vec V$ and linear multiplets $\vec \Sigma$, wherever they occur in the Lagrangian.

## A ${\mathbb Z}_2$ action on 3d $\mathcal{N}=2$ theories with a chiral operator {#sec:F}

The basic "matter" action on 3d $\mathcal{N}=2$ theories begins with a theory that has a coupling to a background 3d chiral multiplet $\phi$. In practice, what we mean is a choice of chiral operator $\mathcal{O}$ that can be inserted in a superpotential $$\mathcal{W}= \phi\,\mathcal{O}\,.$$ Here and elsewhere, we will not keep track of the normalization of superpotential terms. In particular, we will view a rescaling of $\mathcal{O}$ as a trivial operation.

We can define an operation $F$ that makes $\phi$ dynamical (thus, setting $\mathcal{O}$ effectively to zero). The new theory can be coupled to a new background chiral field $\phi'$ by coupling to the new chiral operator $\mathcal{O}'=\phi$, namely by the superpotential $$\mathcal{W}= \phi' \phi \,.$$ It is easy to see that $F^2=1$. We can simply look at the combined superpotential $$\mathcal{W}= \phi'' \phi'+\phi' \phi +\phi\,\mathcal{O}$$ and integrate out $\phi'$.

Much like the "gauge" $Sp(2N,{\mathbb Z})$ action of the previous subsection, the operation $F$ can be given an interesting four-dimensional interpretation. One can consider possible boundary conditions on a four-dimensional hypermultiplet. If we split the four real scalar fields in the hypermultiplet into two complex scalar fields, which we can denote as $X$ and $Y$, then the two basic boundary conditions are either Neumann for $X$ and Dirichlet for $Y$, or vice versa. A way to understand this is that $Y$ sits in a multiplet of the unbroken supersymmetry which contains the normal derivative of $X$.

If we introduce extra degrees of freedom at the boundary, say a 3d theory with a preferred chiral operator $\mathcal{O}$, then we can consider a deformed Dirichlet boundary condition $Y=\mathcal{O}$. This will be accompanied by a corresponding deformation of the Neumann boundary conditions for $X$, involving the corresponding piece of the supermultiplet $\mathcal{O}$. This defines a certain class of boundary conditions which we denote $\mathcal{B}_Y$, so that the boundary condition associated to a 3d theory $\mathcal{T}$ is denoted by $\mathcal{B}_Y[\mathcal{T}]$. An alternative way to describe this boundary condition is to start with the undeformed boundary condition and add the boundary superpotential coupling $$\mathcal{W}= X \mathcal{O}\,.$$

Naively, one can construct a completely different class of boundary conditions $\mathcal{B}_X$ as Dirichlet boundary conditions with $X=\mathcal{O}'$, where $\mathcal{O}'$ is a chiral operator in a 3d boundary theory $\mathcal{T}'$. It turns out that these two classes actually coincide, as every member $\mathcal{B}_Y[\mathcal{T}]$ of one class has a mirror $\mathcal{B}_X[\mathcal{T}']$ in the other class. One simply takes $\mathcal{T}'$ to be the image of $\mathcal{T}$ under $F$, with $\mathcal{O}' = \phi$; then we claim that

$$\mathcal{B}_Y[\mathcal{T}] = \mathcal{B}_X[F\circ\mathcal{T}]\,.$$

To see this, we simply follow the definition of $F\circ\mathcal{T}$ to obtain an overall superpotential coupling $$\mathcal{W}= Y \phi + \phi\,\mathcal{O}\,.$$ Integrating out $\phi$ sets $Y = - \mathcal{O}$. Furthermore, the boundary condition $X=\phi$ means that we can simply "absorb" $\phi$ into $X$, thus relaxing the Dirichlet boundary conditions. It takes a bit more work to make sure that $X$ acquires Neumann boundary conditions, but it follows from the fact that the normal derivative $\partial_n X$ plays the role of auxiliary field in the $Y$ supermultiplet. In summary, if we begin with Dirichlet boundary conditions for $X$ and perform an $F$ transformation --- adding a single boundary chiral multiplet $\phi$ and a superpotential $\mathcal{W}= Y\phi$ --- we will flow in the IR to Dirichlet boundary conditions for $Y$.

## Useful $\mathcal{N}=2$ mirror symmetries {#sec:MS}

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

# Construction of $T_M$ {#sec:glue}

In this section, we will now combine the ingredients of Sections [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"} and [\[sec:ops\]](#sec:ops){reference-type="ref" reference="sec:ops"} to provide the map from a pair $(M,\Pi)$, where $M$ is a 3-manifold and $\Pi$ a polarization of its boundary phase space $\mathcal{P}_{\partial M}$, to a 3d SCFT $T_{M,\Pi}$, with specified couplings to background gauge fields and chiral multiplets. We will do so in two steps. First, we attach a 3d theory to any triangulation $\{\Delta_i\}_{i=1}^N$ of the three-manifold $M$, and then we show that different triangulations of the same three-manifold give mirror descriptions of the 3d SCFT.

## Definition {#sec:defTM}

In order to implement the first step, we begin by defining a theory $T_{\Delta, \Pi_Z}$ that we associate to a single tetrahedron $\Delta$ in polarization $\Pi_Z$ (as in [\[tetpols\]](#tetpols){reference-type="eqref" reference="tetpols"}): $$\boxed{\phantom{\int}
T_{\Delta, \Pi_Z} = \mathcal{T}_1\,.
\phantom{\int}}
\label{TDelta}$$

Recall from Section [0.2](#sec:MS){reference-type="ref" reference="sec:MS"} that $\mathcal{T}_1$ is a theory of a single chiral multiplet coupled to a background $U(1)$ gauge field, with a level $-\frac12$ Chern-Simons term turned on. We will say from now on that the free chiral is associated to the edges of the tetrahedron $\Delta$ labelled by $Z$, and denote it as $\phi_Z$ or $\mathcal{O}_Z$. It is also useful to think of the twisted mass of $\mathcal{O}_Z$ as ${\rm Re}(Z)$, and its R-charge as ${\rm Im}(Z)/\pi$, where $Z$ is the classical edge/shape parameter of $\Delta$. We use this interpretation here as an intuitive aid to motivate our gluing construction; it will be made much more precise in Sections [\[sec:moduli\]](#sec:moduli){reference-type="ref" reference="sec:moduli"} and [\[sec:S3b\]](#sec:S3b){reference-type="ref" reference="sec:S3b"}.

We can extend the definition [\[TDelta\]](#TDelta){reference-type="eqref" reference="TDelta"} to any other polarization $\Pi$ obtained by an (affine) $SL(2,{\mathbb Z})$ transformation $g$ on $\Pi_Z$:

$$T_{\Delta, g \circ \Pi_Z} = g \circ \mathcal{T}_1 \label{TDeltaPi}$$

For example, in a polarization $\Pi_Z^-$ as in [\[PiZm\]](#PiZm){reference-type="eqref" reference="PiZm"}, we would find $T_{\Delta,\Pi_Z^-}=T\circ \mathcal{T}_1$ to be the theory of a free chiral coupled to a background $U(1)$ with Chern-Simons level $k=+\frac12$. This definition is consistent with the ${\mathbb Z}_3$ symmetry of the tetrahedron: the triality symmetry permutes three equivalent polarizations $\Pi_{Z}$, $\Pi_{Z'}$, $\Pi_{Z''}$ in [\[tetpols\]](#tetpols){reference-type="eqref" reference="tetpols"} which, on the $\mathcal{N}=2$ gauge theory side, correspond to the three duality frames [\[STonT1\]](#STonT1){reference-type="eqref" reference="STonT1"} of the theory $\mathcal{T}_1$ permuted by the $ST$ element of $SL(2,{\mathbb Z})$.

The second step is the definition of $T_{\{ \Delta_i\}, \tilde\Pi}$, the theory associated to the union of $N$ tetrahedra $\Delta_i$, in a generic polarization $\tilde\Pi$. We can always write $\tilde\Pi = g \circ \{ \Pi_i \}$ for some $g\in Sp(2N,{\mathbb Z})$, where $\{ \Pi_i \}$ is a polarization defined as a product of independent polarizations $\Pi_i$ of the individual tetrahedra. We choose each $\Pi_i$ to be either $\Pi_{Z_i}$, $\Pi_{Z'_i}$ or $\Pi_{Z''_i}$. Then we define $$\boxed{\phantom{\int}
M = \bigcup_{i=1}^N \Delta_i^{(\Pi)} \qquad \leadsto \qquad T_{ \{\Delta_i\} , \tilde\Pi} \; = \; g \circ \bigotimes_{i=1}^N T_{\Delta_i,\Pi_i}
\phantom{\int}}
\label{TMoutofTD}$$ where we regard the product of $N$ copies of $\mathcal{T}_1$ theories as a theory with a canonical coupling to a $U(1)^N$ background gauge field. We should think of each $U(1)$ as corresponding to an *independent* position coordinate in the polarization $\tilde \Pi$. This definition is independent of the choice of $\Pi_i\in \{\Pi_{Z_i},\Pi_{Z'_i},\Pi_{Z''_i}\}$ due to the the symmetry $ST \circ \mathcal{T}_1 = \mathcal{T}_1$.

In order to define the actual SCFT $T_{M,\Pi}$ associated to the 3-manifold $M$, we need to implement a field-theory version of the gluing constraints $C_I\to 2\pi i$ for each internal edge $I$ in the triangulation. The basic idea is to choose a polarization $\tilde\Pi = g\circ\{\Pi_i\}$ for the collection of tetrahedra such that

-   it is compatible with the final desired polarization $\Pi$ of the boundary $\mathcal{P}_{\partial M}$; and

-   all the internal edge coordinates $C_I$ are "positions" in $\tilde\Pi$.

If we are careful, we can then construct operators $\mathcal{O}_I$ in the theory $T_{\{\Delta_i\},\tilde\Pi}$, one for each internal edge. These operators will be charged under a subset of $U(1)$ flavor symmetries, also associated to the edges $C_I$ --- or rather to independent linear combinations of them. We can then define $T_{M,\Pi}$ by adding a superpotential to $T_{\{\Delta_i\},\tilde\Pi}$ of the form

$$\boxed{\phantom{\int}
\mathcal{W}\; = \; \sum_{{I \in \, \text{internal} \atop \text{edges of~} M}} \mathcal{O}_I\,.
\phantom{\int}}
\label{WforTM}$$

This superpotential breaks all the $U(1)$ symmetries under which the $\mathcal{O}_I$ are charged. It also sets the R-charge of each $\mathcal{O}_I$ equal to $2$. We will see later that this is precisely equivalent to setting $C_I=2\pi i$.

In addition to the internal edge operators $\mathcal{O}_I$, the theories $\mathcal{T}_{\{\Delta_i\},\tilde\Pi}$ and $\mathcal{T}_{M,\Pi}$ also have a set of operators $\mathcal{O}_E$ associated to the external edges that are "positions" in $\Pi \subset \tilde\Pi$. These operators are charged precisely under the $U(1)$ gauge symmetries that persist as symmetries of $T_{M,\Pi}$ --- one for each independent position in $\Pi$. Indeed, it is easy to see that the flavor group of $T_{M,\Pi}$ will contain exactly $\frac12\dim \mathcal{P}_{\partial M}$ $U(1)$'s. In summary, we have built a correspondence:

$$\begin{array}{c@{\quad}|@{\quad}c}
\text{geometry} & \text{gauge theory} \\\hline
\Delta,\,\Pi_Z & T_{\Delta,\Pi_Z}= \mathcal{T}_1 \\[.1cm]
\{\Delta_i\},\, \{\Pi_i\} & T_{\{\Delta_i\},\{\Pi_i\}}=\otimes_i T_{\Delta_i,\Pi_i} \\[.1cm]
\text{positions, \emph{e.g.}\ $Z_i$} & \text{operators $\mathcal{O}_{Z_i}$ with $U(1)$ symmetries} \\[.1cm]
\{\Pi_i\} \to \tilde\Pi=g\circ \{\Pi_i\} & T_{\{\Delta_i\},\{\Pi_i\}}\to \mathcal{T}_{\{\Delta_i\},\tilde\Pi}=  g\circ T_{\{\Delta_i\},\{\Pi_i\}} \\[.1cm]
\text{internal edges}\;C_I & \text{operators}\; \mathcal{O}_I \\[.1cm]
\text{external positions, \emph{e.g.}\ $X_E$} & \text{operators $\mathcal{O}_E$} \\[.1cm]
C_I \to 2\pi i \;\text{(symp$^\text{c}$ reduction)} & \mathcal{W}= \sum_I \mathcal{O}_I \\[.1cm]
M = \cup_i\Delta_i,\;\;\Pi  & T_{M,\Pi} = \mathcal{T}_{\{\Delta_i\},\tilde\Pi}\;\text{+ superpotential $\mathcal{W}$}
\end{array}$$

The construction of operators $\mathcal{O}_I$ (and also $\mathcal{O}_E$) in the product theory $\mathcal{T}_{\{\Delta_i\},\tilde\Pi}$ is a little tricky. In order to describe it, we must distinguish two classes of edges. We call an edge "easy" if its classical coordinate $C_I$ (or $X_E$) is a sum containing at most one of the edge parameters $Z_i,\,Z_i',\,Z_i''$ for any tetrahedron $\Delta_i$; otherwise the edge is "hard." Thus, $C_I = Z_1+Z_2$ or $C_I=2Z_1''+Z_3+Z_4'$ would be examples of easy edges, while the internal edges [\[C41\]](#C41){reference-type="eqref" reference="C41"} in the standard triangulation of the figure-eight knot complement are hard.

Suppose that a triangulation $M=\{\Delta_i\}_{i=1}^N$ only contains easy edges, and let us focus on the internal ones $C_I$. For every edge $I$, we can define a polarization $\{\Pi_i^I\}$ so that the tetrahedron parameters appearing in $C_I$ are all position coordinates. Due to the definition of easy edges, we can always choose $\Pi_i\in \{\Pi_Z,\Pi_{Z'},\Pi_{Z''}\}$ so that the product polarization has this property. Then, in the theory $T_{\{\Delta_i\},\{\Pi_i^I\}}$ there will automatically exist an operator $\mathcal{O}_I$ for the edge $C_I$, constructed as a product of elementary chiral fields. For example, if our easy edge is $C_I = 2Z_1''+Z_3+Z_4'$, we choose a product polarization $\{\Pi_i^I\}$ that includes $\Pi_1^I = \Pi_{Z_1''},\,\Pi_3^I=\Pi_{Z_3},$ and $\Pi_4^I=\Pi_{Z_4'}$. Then $T_{\{\Delta_i\},\{\Pi_i^I\}}$ will have operators $\mathcal{O}_{Z_1''}$, $\mathcal{O}_{Z_3}$ and $\mathcal{O}_{Z_4'}$, all elementary chiral fields, from which we define $\mathcal{O}_I = (\mathcal{O}_{Z_1''})^2\mathcal{O}_{Z_3}\mathcal{O}_{Z_4'}$.

Now, we are really interested in the theory $T_{\{\Delta_i\},\tilde\Pi}$, associated to the polarization $\tilde\Pi$ in which every internal edge is a position coordinate. For each individual $C_I$, there exists an (affine) $Sp(2N,{\mathbb Z})$ transformation $g_I$ such that

$$\tilde\Pi = g_I\circ \{\Pi_i^I\}\,,\qquad T_{\{\Delta_i\},\tilde\Pi} = g_I\circ T_{\{\Delta_i\},\{\Pi_i^I\}}\,. \label{gI}$$

This is not quite an arbitrary transformation. In particular, since $C_I$ is a position coordinate in both $\{\Pi_i^I\}$ and $\tilde \Pi$, the action of $g_I$ cannot gauge any of the $U(1)$ flavor symmetries under which the operator $\mathcal{O}_I$ transforms. Therefore, we can easily pull $\mathcal{O}_I$ through the transformation on the right of [\[gI\]](#gI){reference-type="eqref" reference="gI"} to define the corresponding internal edge operator in $T_{\{\Delta_i\},\tilde\Pi}$.

If a triangulation only contains easy edges, we can repeatedly use this construction to define all the operators appearing in the superpotential [\[WforTM\]](#WforTM){reference-type="eqref" reference="WforTM"}. Notice, however, that we define each $\mathcal{O}_I$ using a different mirror Lagrangian description of $T_{\{\Delta_i\},\tilde\Pi}$. In any given description, one of the internal edge operators is "simple," being a gauge-invariant product of elementary chiral multiplets. The other operators may appear more complicated, and will in general take the form of monopole operators.

Just as we defined operators for internal edges, we can also define operators $\mathcal{O}_E$ for any easy external edges (or cusp holonomies) that are positions in $\Pi\subset\tilde\Pi$. In various mirror duality frames, they will appear either as products of chiral fields or monopole operators, and they will be charged under the flavor symmetries of $T_{M,\Pi}$ that correspond to the positions $X_E$ (or $U$, etc.).

Currently, we only have a rigorous construction of operators $\mathcal{O}_I$ and $\mathcal{O}_E$ for triangulations with easy edges. Indeed, it appears that if we try to define a theory $T_{M,\Pi}$ using a triangulation of $M$ with hard edges, the theory will be slightly degenerate --- and potentially missing some expected operators. We will see an example of this behavior in Section [\[sec:gauge41\]](#sec:gauge41){reference-type="ref" reference="sec:gauge41"}. Fortunately, it seems that we can always refine a given triangulation of a 3-manifold $M$ so that no hard edges are present, and then use this triangulation to construct $T_{M,\Pi}$.\
One of our central claims is that the theories $T_{M,\Pi}$ constructed here are topological invariants of a three-manifold $M$ (and a polarization of its boundary), which do not depend on the actual triangulation being used to define them --- or on the choice of refinement, should a given triangulation include hard edges. In particular, we claim that different triangulations lead to different mirror-symmetric descriptions of the same underlying 3d SCFT. To understand this, we now proceed to analyze the simplest and most important example of a triangulated 3-manifold: the bipyramid.

## The bipyramid and the 2--3 move {#sec:gauge23}

Let's consider the theory of the bipyramid, as constructed from two different triangulations. To keep things simple, we will focus on the "equatorial" polarization $\Pi=\Pi_{\rm eq}$ for the bipyramid, as defined in [\[bipcoord3\]](#bipcoord3){reference-type="eqref" reference="bipcoord3"} or [\[bipcoord2\]](#bipcoord2){reference-type="eqref" reference="bipcoord2"}. In particular, the three equatorial edges of the bipyramid are position coordinates in $\Pi$. We keep the same notation as in Section [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"}, and repeat Figure [\[fig:Pach\]](#fig:Pach){reference-type="ref" reference="fig:Pach"} here as a visual reference.

![Decompositions of the bipyramid, with labelled edge coordinates (Figure [\[fig:Pach\]](#fig:Pach){reference-type="ref" reference="fig:Pach"}).](Pach){#fig:Pach2 width="5in"}

If we decompose the bipyramid into three tetrahedra, then according to our rules $T_{ \{\Delta_i\} , \Pi}$ is a theory of three free chiral multiplets, coupled to a background $U(1)^3$, with some extra CS couplings determined by our choice of momenta in $\Pi$. The operator associated to the unique internal edge is simply the product of the three chiral fields. Hence $T_{M,\Pi}$ is simply the XYZ model, with appropriate coupling to the unbroken $U(1)^2$ flavor symmetry. The operators associated to the external edges are the three chiral multiplets themselves.

Being more explicit, we can start with a product polarization $\{\Pi_i\} = \{\Pi_Z,\Pi_W,\Pi_Y\}$, such that $Z,W,Y$ are coordinates and $Z'',W'',Y''$ are momenta. In the equatorial polarization $\Pi_{\rm eq}$, we know that $X_1 = Z$ and $X_2=W$ are positions while $P_1=Z''+Y'$ and $P_2=W''+Y'$ are momenta; we therefore choose a compatible polarization $\tilde\Pi$ on $\mathcal{P}_{\{\partial\Delta_i\}}$ with positions $X_1,X_2,C$ and momenta $P_1,P_2,\Gamma$, where $C=X+Y+Z$ and $\Gamma=-Y'$. The affine symplectic transformation $g$ from $\{\Pi_i\}$ to $\tilde\Pi$ is encoded as

$$\begin{pmatrix} X_1\\X_2\\C\\P_1\\P_2\\\Gamma\end{pmatrix}= \begin{pmatrix} 1&0&0&0&0&0\\ 0&1&0&0&0&0\\1&1&1&0&0&0 \\0&0&0&1&0&-1\\0&0&0&0&1&-1\\0&0&0&0&0&1\end{pmatrix}\begin{pmatrix} 1&0&0&0&0&0\\0&1&0&0&0&0\\0&0&1&0&0&0\\0&0&0&1&0&0 \\0&0&0&0&1&0\\0&0&1&0&0&1\end{pmatrix} \begin{pmatrix} Z\\W\\Y\\Z''\\W''\\Y''\end{pmatrix}+\begin{pmatrix} 0\\0\\0\\i\pi\\i\pi\\-i\pi\end{pmatrix}\,, \label{Spbip3}$$

which involves a $T$-type transformation, a $GL$-type transformation, and a shift that will not be visible at the level of Lagrangians. Thus, starting with a Lagrangian description

$$\begin{aligned}
 \mathcal{L}_{\{\Pi_i\}}[V_Z,V_W,V_Y] &= \frac{1}{4\pi}\int d^4\theta\Big(-\frac12 \Sigma_ZV_Z-\frac12 \Sigma_WV_W-\frac12\Sigma_YV_Y\Big)+ \notag\\ &\hspace{.8in} \int d^4\theta \big( \phi_Z^\dagger e^{V_Z}\phi_Z+\phi_W^\dagger e^{V_W}\phi_W+\phi_Y^\dagger e^{V_Y}\phi_Y\big) 
\end{aligned}$$

for $T_{\{\Delta_i\},\{\Pi_i\}}$, we construct the Lagrangian for $T_{\{\Delta_i\},\tilde\Pi} = g\circ T_{\{\Delta_i\},\{\Pi_i\}}$ simply as

$$\mathcal{L}_{\tilde\Pi}[V_{X_1},V_{X_2},V_C] = \mathcal{L}_{\{\Pi_i\}}[V_{X_1},V_{X_2},V_C-V_{X_1}-V_{X_2}]+\frac{1}{4\pi}\int d^4\theta(\Sigma_C-\Sigma_{X_1}-\Sigma_{X_2})\,(V_C-V_{X_1}-V_{X_2})\,, \label{Lbip3eq}$$

in other words by adding a level 1 Chern-Simons term for $V_Y$, and redefining $V_Z=V_{X_1},\,V_W=V_{X_2}$, and $V_Y=V_C-V_{X_1}-V_{X_2}$. It is trivial to see that the elementary operator

$$\mathcal{O}_C \equiv \phi_Z\phi_W\phi_Y \label{WXYZ}$$

exists in $T_{\{\Delta_i\},\tilde\Pi}$, as do the individual operators $\phi_Z,\phi_W,\phi_Y$ associated to the equatorial external edges. The bipyramid theory $T_{M,\Pi_{\rm eq}}$ is then defined by adding the superpotential $\mathcal{W}= \mathcal{O}_C$ to [\[Lbip3eq\]](#Lbip3eq){reference-type="eqref" reference="Lbip3eq"}, which forces $V_C=\theta\bar\theta m_C=0$; direct calculation then shows

$$\begin{aligned}
 \mathcal{L}_{M,\Pi_{\rm eq}}[V_{X_1},V_{X_2}]&=\frac{1}{4\pi}\int d^4\theta\, \Sigma_{X_1}V_{X_2} + \int d^4\theta \big( \phi_Z^\dagger e^{V_{X_1}}\phi_Z+\phi_W^\dagger e^{V_{X_2}}\phi_W+\phi_Y^\dagger e^{-V_{X_1}-V_{X_2}}\phi_Y\big) \notag\\
 &\hspace{.8in} + \int \big(d^2\theta \,\phi_Z\phi_W\phi_Y +c.c.\big)\,.
\label{XYZbip}
\end{aligned}$$

This is the promised XYZ model, with slightly redefined $U(1)^2$ symmetries, and a mixed Chern-Simons term.

If we decompose the bipyramid into two tetrahedra instead of three, we need no superpotential. On the other hand, the transformation $g$ from the polarization $\{\Pi_R,\Pi_{S''}\}$ for the two tetrahedra to $\Pi_{\rm eq}$ is non-trivial: as the positions are $X_1=R + S''$, $X_2=R'' + S$, and $R'+S'$, it is easy to see that $g$ involves gauging (with no CS coupling) the $U(1)$ under which the two chiral multiplets have opposite charge. Hence with this definition $T_{M,\Pi}$ is simply $N_f=1$ SQED, with appropriate coupling to the $U(1)^2$ flavor symmetry. The operator associated to the edge coordinate $X_1=R+S''$ is simply the meson operator.

Again, one can go through explicit Lagrangian manipulations as above. Starting from a polarization $\{\Pi_i\}=\{\Pi_R,\Pi_{S''}\}\sim (R,S'';R'',S')$ we reach the equatorial polarization $\Pi_{\rm eq}\sim (X_1,X_2;P_1,P_2)$ via a symplectic transformation $g = g_S\,g_T\,g_U$, with

$$\label{gbip2}
g_S = \begin{pmatrix} 1&0&0&0\\0&0&0&-1\\0&0&1&0\\0&1&0&0\end{pmatrix},\quad
g_T = \begin{pmatrix} 1&0&0&0\\0&1&0&0\\0&0&1&0\\0&1&0&1\end{pmatrix},\quad
g_U = \begin{pmatrix} 1&1&0&0\\0&1&0&0\\0&0&1&0\\0&0&-1&1 \end{pmatrix}\,.$$

Therefore, we obtain $\mathcal{L}_{M,\Pi_{\rm eq}}[V_{X_1},V_{X_2}]$ by starting with

$$\mathcal{L}_{\{\Delta_i\},\{\Pi_i\}}[V_R,V_{S''}]=\frac{1}{4\pi}\int d^4\theta\Big(-\frac12 \Sigma_RV_R-\frac12 \Sigma_{S''}V_{S''}\Big)+ \int d^4\theta \big( \phi_R^\dagger e^{V_R}\phi_R+\phi_{S''}^\dagger e^{V_{S''}}\phi_{S''}\big)\,,$$

redefining the $U(1)^2$ symmetry, adding a Chern-Simons term, and gauging a $U(1)$. A straightforward calculation produces

[^3]

$$\begin{aligned}
 \mathcal{L}_{M,\Pi_{\rm eq}}[V_{X_1},V_{X_2}] &= \frac{1}{4\pi}\int d^4\theta\big(\Sigma_{X_1}V_{X_2}+(\Sigma_{X_1}+2\Sigma_{X_2})\,V\big) \notag \\
 &\qquad\qquad +\int d^4\theta\big( \phi_R^\dagger e^{V+\frac12{V_{X_1}}}\phi_R+\phi_{S''}^\dagger e^{-V+\frac12{V_{X_1}}}\phi_{S''}\big)\,, \label{SQEDbip}
\end{aligned}$$

with the $U(1)$ gauge multiplet $V$ dynamical. This is precisely $N_f=1$ SQED, with a mixed Chern-Simons coupling, and slightly redefined $U(1)^2$ symmetry. The meson operator $\mathcal{O}_{X_1}\equiv \phi_R\phi_{S''}$ is obviously charged under $V_{X_1}$. We know that SQED also has two monopole operators $v_+$ and $v_-$, and from the form of the FI term in [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"} we see that they must be charged under the combinations $V_{X_2}$ and $-V_{X_1}-V_{X_2}$, respectively. Thus, they correspond to the remaining two equatorial edges.

Thanks to the basic $\mathcal{N}=2$ mirror symmetry statement [\[XYZmir\]](#XYZmir){reference-type="eqref" reference="XYZmir"}, our construction gives the same theory $T_{M,\Pi}$ for the bipyramid, *no matter how we triangulate it*. By carefully comparing the Lagrangian descriptions [\[XYZbip\]](#XYZbip){reference-type="eqref" reference="XYZbip"} and [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"}, we see that the three equatorial edge operators --- elementary fields in the XYZ model and a meson/monopoles in SQED --- are mapped to each other by mirror symmetry, and their coupling to the background $U(1)$ gauge multiplets $V_{X_1}$ and $V_{X_2}$ coincide perfectly.

One can also repeat the exercise for the longitudinal polarization. The two triangulations give respectively $\mathcal{N}=4$ SQED with $N_f=1$ and the theory of a free hypermultiplet, *i.e.* the basic $\mathcal{N}=4$ mirror pair. This is a useful exercise in order to show that the operators associated to longitudinal edges by the two polarizations are also mapped into each other by mirror symmetry.

With this result, we are in position to argue that the theories $T_{M,\Pi}$ defined by different triangulations of the same three-manifold $M$ are mirror to each other. Different triangulations are related by a sequence of $2-3$ moves.

[^4]

Two triangulations that differ by a $2-3$ move give two definitions of the theory $T_{M,\Pi}$ that differ only by a basic mirror symmetry relation. The mirror symmetry acts on the degrees of freedom associated to the particular bipyramid that is decomposed in two different ways in the course of a $2-3$ move.

## The flip {#sec:flip}

Just as $2-3$ moves change the internal triangulation of a 3-manifold, the flips described in Section [\[sec:geom23\]](#sec:geom23){reference-type="ref" reference="sec:geom23"} can change the triangulation of its (geodesic) boundary. This has a very simple effect on a theory $T_{M,\Pi}$.

For example, suppose that $T_{M,\Pi}$ has an operator $\mathcal{O}_X$, charged under a global symmetry $U(1)_X$, that corresponds to an external edge with position coordinate $X$. We want to add a tetrahedron $\Delta_Z$ to flip this edge, as in Figure [\[fig:flip\]](#fig:flip){reference-type="ref" reference="fig:flip"}. Following our gauge theory dictionary, this means that we form the combined theory $T_{M,\Pi}\otimes T_{\Delta_Z,\Pi_Z}$, and add a superpotential coupling

$$\mathcal{W}= \mathcal{O}_X\phi_Z\,. \label{Wflip}$$

The new theory now has a chiral operator $\phi_Z$ that transforms under the anti-diagonal subgroup of $U(1)_X\times U(1)_Z$ that is unbroken by [\[Wflip\]](#Wflip){reference-type="eqref" reference="Wflip"}.

This transformation simply describes the $F$ operation of Section [0.1](#sec:F){reference-type="ref" reference="sec:F"}. Just as $F^2$ is a trivial operation on a 3d SCFT, flipping a diagonal twice is a trivial operation on the boundary of a 3-manifold.

## $T_M$ as a boundary condition {#sec:gauge4d}

In section [\[sec:ops\]](#sec:ops){reference-type="ref" reference="sec:ops"} we learned some useful facts about the relation between three dimensional theories and boundary conditions for four-dimensional theories. We saw that all the 3d theories in an orbit of the $Sp(N,Z)$ action can be thought of as representing the same boundary condition in different electric-magnetic duality frames of a four-dimensional abelian gauge theory. We also saw that the $F$ transformation on three-dimensional theories can be thought of as relating two mirror description of the same boundary condition for one hypermultiplet.

We can use these facts to try to liberate $T_{M,\Pi}$ from the dependence on the polarization $\Pi$, and even on the choice of triangulation of the geodesic boundary $\mathcal{C}$ of $M$. To remove the polarization dependence, we can couple $T_{M,\Pi}$ to a four-dimensional gauge theory, whose symplectic lattice of electric-magnetic charges is modeled on the lattice generated by the edge coordinates of the triangulation of $\mathcal{C}$, the geodesic boundary of $M$. In order to remove the dependence on the triangulation of $\mathcal{C}$, we need to couple $T_{M,\Pi}$ to a set of hypermultiplets as well, one for each edge of the triangulation of $\mathcal{C}$. In order for the flip to coincide with an $F$ move, each hyper must be coupled by a superpotential to $\mathcal{O}_E$, and hence have four-dimensional gauge charges equal or opposite to the charge associated to the edge itself.

Thus we find it natural to couple $T_{M,\Pi}$ to an apparently bizarre four-dimensional theory: an $\mathcal{N}=2$ abelian gauge theory coupled to hypermultiplets of several dyonic charges, one for each edge of the triangulation of $\mathcal{C}$. This theory is less bizarre than it seems. Indeed, [@GMNIII], the symplectic lattice generated by a triangulation of $\mathcal{C}$ coincides naturally with the lattice of IR electric-magnetic charges for the four-dimensional theory obtained from two M5 branes wrapping $\mathcal{C}$. Furthermore, in a large patch of the 4d Coulomb branch, the whole spectrum of IR BPS particles can be thought of as bound states of a basis of hypermutliplet particles, each associated to an edge of the triangulation, and carrying the corresponding charges.

Thus there is a sense in which the abelian gauge theory with the hypermultiplets associated to the edges of the triangulation is a complete IR description of the four-dimensional theory associated to $\mathcal{C}$. And thus $T_{M,\Pi}$ can be thought as the description of a boundary condition for the four-dimensional theory, in a given duality frame. This is a property which we surely expect to be true of $T[M,\mathfrak{su}(2)]$. In later sections we will reinforce the connection further. For example, the moduli space of vacua of $T_{M, \Pi}$ compactified on a circle naturally defines a boundary condition for the four-dimensional gauge theory compactified on a circle.

[^1]: Notice that the coupling of the background gauge field to $\mathcal{T}_2$ is unaffected by charge conjugation $C$.

[^2]: By "twisted mass" in three dimensions, we mean a mass term arising as a background value for the real scalar field in a vector multiplet. Sometimes this is also called a "real mass."

[^3]: []{#foot:half label="foot:half"} In the last step of the derivation of [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"}, we shifted the dynamical gauge multiplet $V\to V+\frac12 V_{X_1}$, thereby adding to the '$X_1$' flavor current a half-integral multiplet of the gauge current. This non-integral shift is not necessary, but can be made sense of because the multiplet $V_{X_1}=\theta\bar\theta m_{X_1}$ is nondynamical. In the form [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"} of the Lagrangian, the identification of $\frac12 V_{X_1}$ with an axial flavor multiplet becomes immediate.

[^4]: Strictly speaking, we should only consider triangulations that have easy edges, as discussed in Section [1.1](#sec:defTM){reference-type="ref" reference="sec:defTM"}. It is very plausible --- although not mathematically proven --- that to connect two "easy" triangulations, one can always find a chain of $2-3$ moves that only pass through other easy triangulations.
