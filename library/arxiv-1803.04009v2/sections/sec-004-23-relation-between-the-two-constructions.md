---
doc_id: arxiv-1803.04009v2
doc_title: "Symmetry enhancement and closing of knots in 3d/3d correspondence"
section_id: sec-004-23-relation-between-the-two-constructions
section_title: "Relation between the two constructions"
section_number: 2.3
pages: 21-27
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.993
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
[]{#sec:rel label="sec:rel"}

One basic characteristic of the $T^{DGG}[N,X_A]$ theory is that [@Dimofte:2011ju]

$$\begin{aligned}
\begin{split}
&\mathcal{M}_{\rm parameter}(\textrm{$T^{DGG}[N,X_A]$ on $\mathbb{R}^2\times S^1$}) =\mathcal{D}[N,\mathcal{T}] \supseteq  \chi_0(N) \;.
\end{split} \label{eq:moduliID}
\end{aligned}$$

Recall the definition of each term of this equation. For simplicity, we only discuss the case where our 3-manifold $N$ only has a torus boundary and hence of the form $N=M \backslash K$. The deformation variety $\mathcal{D}[N,\mathcal{T}]$ defined in [\[deformation variety\]](#deformation variety){reference-type="eqref" reference="deformation variety"} is a set of flat $PSL(2,\mathbb{C})$ connections on $N$ which can be obtained from an ideal triangulation $\mathcal{T}$. The $\chi_0(N)$ is a subset of the algebraic variety defined in [\[Dehn-surgery com\]](#Dehn-surgery com){reference-type="eqref" reference="Dehn-surgery com"} (or [\[Dehn-surgery com-2\]](#Dehn-surgery com-2){reference-type="eqref" reference="Dehn-surgery com-2"}) which can be seen for any non-exotic ideal triangulation. The difference between the two sets are mild, higher codimension, and may be ignorable in our discussion as we discuss later.

Finally the left-hand side $\mathcal{M}_{\rm parameter}(\textrm{$T^{DGG}[N,X_A]$ on $\mathbb{R}^2\times S^1$})$ is given as follows. A DGG theory in general consists of chiral fields, dynamical vector fields, and background vector fields. Let $\Sigma_i~(i=1,\ldots, N_V)$ be twisted chiral fields constructed from dynamical vector multiplets whose lowest real component is the real scalar of the vector multiplet and the imaginary part is the gauge field in the $S^1$ direction. The $N_V$ is the number of dynamical vector multiplets, i.e., the gauge group is $u(1)^{N_V}$, and it depends on the details of $g_N$ in [\[DGG : step 2\]](#DGG : step 2){reference-type="eqref" reference="DGG : step 2"} and its decomposition into basic types. Also, let $X_A$ be the twisted chiral field of the background $u(1)$ field whose real part corresponds to the real mass parameter $m$ and the imaginary part corresponds to the background flavor gauge field around $S^1$. Then, by integrating out the matter chiral fields of the theory on ${\mathbb R}^2 \times S^1$, we get a twisted superpotential of $\Sigma_i$ and $X_A$ (in some appropriate normalization), ( {\_i}\_i=1\^N_V ; X_A). Then we define

$$\begin{aligned}
\begin{split}
&\mathcal{M}_{\rm parameter}(\textrm{$T^{DGG}[N,X_A]$ on $\mathbb{R}^2\times S^1$})
\\
&=  \big{\{} 
(e^{X_A},e^{P_B}) : \exp \big{(}  \partial_{\Sigma_k}\widetilde{\mathcal{W}}( \{\Sigma_i\}_{i=1}^{N_V} ; X_A) \big{)}=1, 
\partial_{X_A}\widetilde{\mathcal{W}}( \{\Sigma_i\}_{i=1}^{N_V} ; X_A) \big{)}=P_B
\big{\}} 
\backslash \{ \textrm{singular loci}\}.
\end{split}
\end{aligned}$$ The conditions $\exp \big{(}  \partial_{\Sigma_k}\widetilde{\mathcal{W}}( \{\Sigma_i\}_{i=1}^{N_V} ; X_A) \big{)}=1$ are just the condition for the vacua on $S^1 \times {\mathbb R}^2$. The $P_B$ has a definite value (modulo $2\pi i$) at each of the vacua for a given parameter $X_A$. In other words, the equation $\partial_{X_A}\widetilde{\mathcal{W}}( \{\Sigma_i\}_{i=1}^{N_V} ; X_A) \big{)}=P_B$ gives a polynomial equation of $(x_A, p_B):=(e^{X_A},e^{P_B})$, and solutions of that equation in terms of $p_B$ for a given $x_A$ correspond to the vacua of the theory with mass parameter $x_A$.

The relation to localization computation is as follows. The partition function of the $T^{DGG}$ theory on a curved background called squashed 3-sphere $(S^3_b)$ can be written in following form [@Hama:2011ea; @Dimofte:2011ju]

$$\begin{aligned}
\int d\sigma_1 \ldots d\sigma_{N_V} \;\mathcal{I}_b( \{\sigma_i\}_{i=1}^{N_V}  ;X_A) 
\end{aligned}$$

where $\sigma_k = \mathop{\mathrm{Re}}[\Sigma_k]$. In a degenerate limit when $b\rightarrow 0$, which corresponds to the limit where $S^3_b$ become $\mathbb{R}^2 \times S^1$, the leading asymptotic behavior of the integrand is determined by the twisted superpotential

$$\begin{aligned}
\mathcal{I}_b (  \{\sigma_i\}_{i=1}^{N_V} ;X_A)  \xrightarrow[]{\quad b\rightarrow 0 \quad }  
e^{\frac{1}{2\pi i b^2} \widetilde{\mathcal{W}}(  \{\sigma_i\}_{i=1}^{N_V} ;X_A) }\;.
\end{aligned}$$

The equations $\{ \exp (\partial_{\Sigma_i}\widetilde{\mathcal{W}})=1\}_{i=1}^{N_V}$ are equivalent to the gluing equations in [\[deformation variety\]](#deformation variety){reference-type="eqref" reference="deformation variety"}

with an additional relation $e^{a}=(-1)^{\epsilon}\prod z_i^{\alpha_i} (1-z_i^{-1})^{\alpha''_i}$ where $a=X_A~\text{or}~2X_A$ depending on $SO(3)/SU(2)$ types of boundary cycle $A$, and the integers $(\alpha_i, \alpha''_i,\epsilon)$ are given in [\[Hol(A) in terms of edges\]](#Hol(A) in terms of edges){reference-type="eqref" reference="Hol(A) in terms of edges"} [@Dimofte:2012qj].

Now, we have &\_vacua([$T^{DGG}[N,X_A]$ on $\mathbb{R}^2\times S^1$]{.roman})\
=& \_parameter([$T^{DGG}[N,X_A]$ on $\mathbb{R}^2\times S^1$]{.roman}) \|\_a=2m. []{#eq:DGGvacua label="eq:DGGvacua"} This means that by taking the parameter $a$ to be a constant fixed value $2m$, we get the vacua of the theory with the mass parameter $m$.

The above equations may have solutions like $X_A=0$. Field theoretically, when the mass parameter is zero, there could appear some continuous moduli space of vacua spanned by matter chiral fields. Those massless flat directions are subtle, especially when they are generated by monopole operators because in that case those directions appear by very strong coupling effects which may not be captured by the one-loop computation of the twisted superpotential $\widetilde{\mathcal{W}}$. See Sec. 5.2 of [@Dimofte:2011ju] for an example. We may expect that those subtle flat directions might be the reason of the mismatch between $\mathcal{D}[N,\mathcal{T}]$ and $\chi_0(N)$ This problem may be avoided if we only consider generic mass parameters. We assume that this is the case.

#### Comparison of the two constructions

Now let us compare the constructions in Sec. [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"} and Sec. [\[sec:DGG\]](#sec:DGG){reference-type="ref" reference="sec:DGG"}. Comparing the moduli space of $T^{6d}$ in [\[flat connections\]](#flat connections){reference-type="eqref" reference="flat connections"}, and $T^{DGG}$ in [\[eq:DGGvacua\]](#eq:DGGvacua){reference-type="eqref" reference="eq:DGGvacua"} we see that

$$\begin{aligned}
\mathcal{M}_{\rm vacua}(\textrm{$T^{DGG}[N,X_A]$ on $\mathbb{R}^2\times S^1$}) \subset \mathcal{M}_{\rm vacua}(\textrm{$T^{6d}[N,A]$ on $\mathbb{R}^2\times S^1$})\;.
\end{aligned}$$

This is because that an ideal triangulation captures only a subset of irreducible flat connections on $N$ as emphasized in [@Chung:2014qpa]. So we see that $T^{DGG}$ can not be identical to $T^{6d}$ but can only capture a subsector of $T^{6d}$. This point has already been seen from the effective field theory point of view in Sec. [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}. In general, there is no reason to expect that there exists a genuine 3d theory which describes all components of moduli space of vacua of $T^{6d}$. So $T^{DGG}$ can, at best, describe the low energy limit of some point of the moduli space of vacua of $T^{6d}$.

Then a possibility is that $T^{DGG}$ might be identified with $T^{6d}_{\rm irred}$ in [\[eq:defof6dtheory\]](#eq:defof6dtheory){reference-type="eqref" reference="eq:defof6dtheory"}. Both of them are genuine 3d theories and they are associated to the hyperbolic connection ${\cal A}^{\rm \overline{hyp}}$ which can be realized in ideal triangulation. However, it turns out that these two theories are still different as we now explain.

One crucial difference between the two theories is that $T^{DGG}$ generically has $U(1)_{X_A}$ flavor symmetry associated to the knot while $T^{6d}$ and hence $T^{6d}_{\rm irred}$ have $su(2)_A$. Furthermore, the $SL(2,\mathbb{Z})$ action on the canonical variables $(X_A, P_B)$ is realized in field theory as the $SL(2,\mathbb{Z})$ action of Witten [@Witten:2003ya] using $u(1)$ group on $T^{DGG}$, while the $SL(2,\mathbb{Z})$ action on the boundary cycle $(A,B)$ is realized in field theory as the $SL(2,\mathbb{Z})$ of Gaiotto-Witten [@Gaiotto:2008ak] using the $su(2)$ symmetry and $T[SU(2)]$ theory on $T^{6d}$.

The $su(2)$ $SL(2,\mathbb{Z})$ on $T^{6d}$ is defined as follows. The transformed theory $\varphi \cdot T^{6d}[N,A,B]$ with

$$\begin{aligned}
\varphi =  \left(\begin{array}{cc}r & s \\ p & q\end{array}\right)\; \in SL(2,\mathbb{Z})
\end{aligned}$$

can be obtained by

$$\begin{aligned}
\begin{split}
&T^{6d}[N,rA+sB;pA+qB] =  \varphi \cdot T^{6d}[N,A;B]
\\
&:=  \textrm{coupling the duality wall theory $T[SU(2),\varphi]$ to $T^{6d}[N,A;B]$ }\;.
\end{split}
\end{aligned}$$

$T[SU(2),\varphi]$ is a 3d $\mathcal{N}=4$ SCFT which describe the 3d theory living on a duality domain wall in 4d $su(2)$ $\mathcal{N}=4$ SYM associated to $\varphi \in SL(2,\mathbb{Z})$. The theory has $su(2)_1 \times su(2)_2$ as flavor symmetry. For example, $T[SU(2), \varphi=S] = T[SU(2)]$. In the coupling between $T[SU(2),\varphi]$ and $T^{6d}[N,A;B]$, we introduce a $\mathcal{N}=2$ vector multiplet to gauge the diagonal $su(2)_{\rm diag}\subset su(2)_{1} \times su(2)_A$ of the two theories with the following superpotential coupling

$$\begin{aligned}
\textrm{Tr}(\mu \mu')\;. \label{Superpotential coupling between T[SU(2)] and T[N]}
\end{aligned}$$

where $\mu$ is the holomorphic moment map operator associated to the $su(2)_A$ of $T^{6d}[N,A;B]$ which is a chiral operator in the adjoint representation of $su(2)_A$,[^1] and $\mu'$ is the holomorphic moment map operator of $su(2)_{1}$ of $T[SU(2),\varphi]$.

Motivated by the similarities and differences between $T_{\rm irred}^{6d}$ and $T^{DGG}$, we propose the following relation between them:

$$\begin{aligned}
T^{6d} \xrightarrow[\text{}]{\textrm{\quad on a vacuum $P_{\rm SCFT}$} \quad} T^{6d}_{\rm irred} \xrightarrow[\text{}]{\textrm{\quad deformed by $\delta W = \mu^3$} \quad} T^{DGG} \label{Relation-T6d-TDGG}
\end{aligned}$$

Here, $\mu^3$ is the Cartan component of the moment map operator ${\mu}=\{\mu^1,\mu^2,\mu^3\}$ in the adjoint representation of $su(2)_A$. The $\delta W = \mu^3$ means the superpotential deformation by the chiral operator $\mu^3$. This deformation breaks $su(2)$ to $U(1)$.

Thus we need two steps from $T^{6d}$ to $T^{DGG}$. First we put the theory on a specific vacuum, $P_{\rm SCFT}$, of the $T^{6d}$ theory on $\mathbb{R}^3$ as explained in Sec. [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}.

As a second step, we deform the intermediate theory, $T^{6d}_{\rm irred}$, by adding the Cartan component ($\mu^3$) of the $su(2)$ moment map operator $\mu$ associated to the knot to the superpotential. We give more evidence for this proposal below.

In the case of 3d ${\cal N}=4$ supersymmetry, the presence of the holomorphic moment map operator associated to a symmetry is guaranteed. However, when there are only ${\cal N}=2$, it is not guaranteed. What we call the holomorphic moment map operator is a kind of remnant of higher supersymmetry of the codimension-2 defect of the 6d ${\cal N}=(2,0)$ theory. The $\mu$ may be empty depending on the theory. However, generically (but not always), the $T^{6d}_{\rm irred}$ theory contains the moment map as chiral operators. This can be seen as follows. Suppose we are given a theory ${\cal T}$ with $su(2)$ symmetry, and then let us perform a transformation T\^k SL(2,Z) []{#eq:STk label="eq:STk"} acting on this $su(2)$. This is done by coupling ${\cal T}$ and $T[SU(2)]$ to the $su(2)$ gauge field with Chern-Simons level $k (+\text{ the original value before }T^k)$. By taking $k$ large enough, the $su(2)$ gauge field is weakly coupled and hence the two theories ${\cal T}$ and $T[SU(2)]$ almost decouple from each other. The $T[SU(2)]$ theory contains the holomorphic moment map operator $\mu$ associated to the new (ungauged) $su(2)$ global symmetry. Therefore, we conclude that the total theory has $\mu$ for generic $k$. Moreover, this argument shows that the scaling dimension of $\mu$ is close to 1, at least if $k$ is large enough, because the scaling dimension of $\mu$ in $T[SU(2)]$ alone is 1 by ${\cal N}=4$ supersymmetry. Therefore, the deformation by $\mu^3$ is a relevant deformation and it triggers RG flows. The case that $\mu$ is absent happens only in rather exceptional situations, and this will be very important in Sec. [\[sec:symm\]](#sec:symm){reference-type="ref" reference="sec:symm"}

In particular, the deformation breaks the $su(2)_A$ in $T_{\rm irred}^{6d}[N,A]$ to $U(1)$ which can be identified with $U(1)_{X_A}$ in $T^{DGG}[N,X_A]$.

$$\begin{aligned}
\big{(} su(2)_A   \textrm{ of $T^{6d}_{\rm irred}$}\big{)}\;\xrightarrow[\text{}]{\quad \delta W = \mu^3 \quad }\; \big{(} U(1)_{X_A} \textrm{ of $T^{DGG}$}\big{)}\;.
\end{aligned}$$

#### More details on $SL(2,{\mathbb Z})$ transformations of $U(1)$ and $SU(2)/SO(3)$ types.

The deformation explains not only why $T^{DGG}$ theory generically has only $U(1)_{X_A}$ associated to the knot, but also why the $SL(2,\mathbb{Z})$ action on the boundary $\mathbb{T}^2$ of the knot complement corresponds to the $U(1)$ $SL(2,\mathbb{Z})$ action on $U(1)_{X_A}$. Roughly, the relation is given by the following diagram;

$$\begin{aligned}
\xymatrix{
T^{6d}_{\rm irred}[N,A;B] \ar[d]^{su(2) \; SL(2,\mathbb{Z})} \ar[r]^{ \delta W = \mu^3 \;\; } & T^{DGG}[N,X_A;P_B]\ar[d]^{U(1)\; SL(2,\mathbb{Z})}\\
T^{6d}_{\rm irred}[N,A';B'] \ar[r]^{ \delta W = \mu^3 \;\;} &T^{DGG}[N,X_{A'}; P_{B'}]}
\end{aligned}$$

However, there are more subtle details.

We denote the $U(1)$-type and $su(2)$-type $SL(2,{\mathbb Z})$ transformations as $SL(2,{\mathbb Z})_1$ and $SL(2,{\mathbb Z})_2$, respectively. The $SL(2,{\mathbb Z})_1$ acts on the canonical variables $(X_A, P_B)$, while $SL(2,{\mathbb Z})_2$ acts on $(A,B)$ and hence on the variables $(a,b)$. Recall that they are related as X_A, P_B) =

::: cases
( 2,b),[when $(A,B)$ is of $\big{(}SU(2),SO(3)\big{)}$ type]{.roman}\
(a,2 ),[when $(A,B)$ is of $\big{(}SO(3),SU(2)\big{)}$ type]{.roman}
:::

Therefore, generic elements of $SL(2,{\mathbb Z})_1$ and $SL(2,{\mathbb Z})_2$ do not exactly correspond to each other.

The $S$-transformation $S_1 \in SL(2,{\mathbb Z})_1$ and $S_2 \in SL(2,{\mathbb Z})_2$ correspond with each other; \_1 &: (X_A,P_B) (-P_B, X_A)\
S_2 &: (a,b) (-b,a) and hence \_1 S_2. []{#eq:Srelation label="eq:Srelation"} Notice that the $S_2$ exchanges the $SU(2)/SO(3)$ types of the cycles. This is natural, because in 4d ${\cal N}=4$ theory, the gauge groups $SU(2)$ and $SO(3)$ are exchanged under the S-duality. This exchange can also be shown in purely 3d language and is explained in Appendix [\[app:susotypes\]](#app:susotypes){reference-type="ref" reference="app:susotypes"}.

On the other hand, the $T$-transformation $T_1 \in SL(2,{\mathbb Z})_1$ and $T_2 \in SL(2,{\mathbb Z})_2$ act as \_1 &: (X_A,P_B) (X_A, P_B+X_A)\
T_2 &: (a,b) (a, b+a) and hence they are related as T_1)\^2 T_2 [when $(A,B)$ is of $\big{(}SU(2),SO(3)\big{)}$ type]{.roman} []{#eq:Trelation1 label="eq:Trelation1"}\
T_1 (T_2)\^2 [when $(A,B)$ is of $\big{(}SO(3),SU(2)\big{)}$ type]{.roman} []{#eq:Trelation2 label="eq:Trelation2"} This also has a natural field theory interpretation. Let $A$ be an $su(2)$ gauge field. The global structure may be either $SU(2)$ or $SO(3)$. Its Chern-Simons 3-form is defined as (A) = (AdA +A\^3), where the trace is taken in the doublet representation of $su(2)$. When the symmetry is $SU(2)$ and is broken down to $U(1)$, we embed a $U(1)$ gauge field $a$ inside $A$ as $A = \mathop{\rm diag}\nolimits(a, -a)$. Then, under this embedding, we get (A) ada = 2 CS(a) []{#eq:U1SU2 label="eq:U1SU2"} where (a)= ada. Recalling that the $T$-transformation in field theory corresponds to the shift of Chern-Simions level of background field, we can see that the factor of 2 in [\[eq:U1SU2\]](#eq:U1SU2){reference-type="eqref" reference="eq:U1SU2"} corresponds to the exponent 2 in [\[eq:Trelation1\]](#eq:Trelation1){reference-type="eqref" reference="eq:Trelation1"}. In the same way, if the gauge group is $SO(3)$ which is broken to $U(1)$, it is natural to embed the $U(1)$ gauge field as $A=\frac{1}{2}(a, -a)$. Then we get (A) ada = CS(a). This equation corresponds to [\[eq:Trelation2\]](#eq:Trelation2){reference-type="eqref" reference="eq:Trelation2"}.

In fact, if the group is $SO(3)$ type, then the ${\rm CS}(A)$ is not a properly quantized Chern-Simons invariant. This is because, in 4d, there can be instantons of instanton number $1/2$,[^2] and hence the integral of ${\rm CS}(A)$ is not well defined in 3d, and only the $2{\rm CS}(A)$ is well defined. This means that when the $A$-cycle is $SO(3)$ type, only the $(T_2)^2$ is well defined. Therefore, the actual transformation group at the quantum level is a subgroup $\Gamma(2) \subset SL(2,{\mathbb Z})_2$ generated by $S_1$ and $(T_2)^2$. These generators $S_1$ and $(T_2)^2$ also preserves the condition that one of the cycles $A$ or $B$ is $SU(2)$ type. Under $T_2$, this condition may not be preserved.

From the above discussion of Chern-Simons levels, the field theoretical realization of [\[eq:Trelation1\]](#eq:Trelation1){reference-type="eqref" reference="eq:Trelation1"} and [\[eq:Trelation2\]](#eq:Trelation2){reference-type="eqref" reference="eq:Trelation2"} under the explicit breaking $su(2)_A \to U(1)_{X_A}$ by $W =\mu^3$ is clear. Now let us also check the correspondence of the S-transformation [\[eq:Srelation\]](#eq:Srelation){reference-type="eqref" reference="eq:Srelation"} at the field theory level. Let ${\cal T}$ be a theory with $su(2)$ symmetry. Then $S$-transformed theory is given by \_2 = T- su(2) - T\[SU(2)\],[]{#eq:StrasfT label="eq:StrasfT"} where the center $su(2)$ is a gauge group which is coupled to the $su(2)$ symmetry of ${\cal T}$ and the $su(2)_H$ symmetry of $T[SU(2)]$. In the language of 3d ${\cal N}=2$ supersymmetry, the $T[SU(2)]$ is given by a $U(1)$ vector multiplet $V$, a neutral chiral field $\phi$, and two pairs of chiral fields $(E^i,\tilde{E}_i)_{i=1,2}$ with $u(1)_{\rm gauge}$ charge $\pm$ with the superpontial = \_i E\^i. The $su(2)_H$ acts on the index $i$ of $(E^i,\tilde{E}_i)_{i=1,2}$. Now, this $T[SU(2)]$ has a $su(2)_C$ symmetry at the quantum level, and this symmetry is the new global $su(2)$ symmetry after the $S$-transformation. See Appendix [\[app:susotypes\]](#app:susotypes){reference-type="ref" reference="app:susotypes"} for more details. The Cartan component $\mu^3$ of the moment map operator of this symmetry $su(2)_C$ is given by $\mu^3=\phi$. Therefore, after the deformation by $\mu^3$, the superpotential becomes = \_i E\^i -. Thus, an F-term condition is $\tilde{E}_i E^i =1$. Then $\tilde{E}_i$ and $E^i$ get nonzero expectation values as E\^1 =\_1 ,   E\^2 =\_2 . These expectation values break the gauge symmetry $[su(2) \times u(1)]_{\rm gauge}$ down to $u(1)$. Namely, $(E^i,\tilde{E}_i)$ are charged under $u(2) = [su(2) \times u(1)]_{\rm gauge}$, and only the subgroup $u(1) \subset u(2)$ which acts on $(E^2, \tilde{E}_2)$ is preserved by the expectation values. Therefore, by the Higgs mechanism, the theory [\[eq:StrasfT\]](#eq:StrasfT){reference-type="eqref" reference="eq:StrasfT"} becomes \_2 S_1 = T- u(1), where $u(1)$ is the gauge group which survives the symmetry breaking $[su(2) \times u(1)]_{\rm gauge} \to u(1)$. The right hand side is just the $S$-transformation of $u(1)$ type. This confirms [\[eq:Srelation\]](#eq:Srelation){reference-type="eqref" reference="eq:Srelation"}.

[^1]: In general, the existence of this operator is guaranteed only for theories with 8 supercharges. However, this operator often exists due to the remnant of 8 supercharges preserved by codimension-2 defects of the 6d ${\cal N}=(2,0)$ theory. Indeed, the operator $\mu$ is absent only for some special cases. These points will be important and discussed in more detail below.

[^2]: To see this, consider a 4d manifold $S^2_1 \times S^2_2$. Then, take the subgroup $U(1) \subset SO(3)$ by $A=\frac{1}{2}(a, -a)$, and include the magnetic fluxes of $f = da$ on each $S^2_1$ and $S^2_2$ as $n_1 = \frac{1}{2\pi}\int_{S^2_1} f$ and $n_2 = \frac{1}{2\pi}\int_{S^2_2} f$. One can check that this configuration gives the instanton number $\frac{1}{2}n_1 n_2$.
