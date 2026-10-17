---
doc_id: arxiv-1604.01247v2
doc_title: "EXCEPTIONAL QUANTUM GEOMETRY"
section_id: sec-010-41-modules-over-jordan-algebras
section_title: "Modules over Jordan algebras"
section_number: 4.1
pages: 18-21
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.987
doc_brief: "EXCEPTIONAL QUANTUM GEOMETRY — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3 generations, we develop an"
---
There are general definitions of bimodules for classes of algebras [@sch:1995], [@jac:1968] or for categories of algebras [@mdv:2001]. For Jordan algebras this reduces to the following (see also in [@kas-ovs-she:2011]). Let $J$ be a Jordan algebra and let $M$ be a vector space equipped with left and right actions of $J$ $$J\otimes M\rightarrow M,\>\>\> x\otimes\Phi\mapsto x\Phi\in M$$ $$M\otimes J\rightarrow M, \>\>\> \Phi\otimes x\mapsto \Phi x\in M$$ for $x\in J$, $\Phi\in M$. Define a bilinear product on $J\oplus M$ by setting $$(x+\Phi)(x'+\Phi')=xx'+(x\Phi'+\Phi x').$$ Then $M$ is said to be *a Jordan bimodule over* $J$ if $J\oplus M$ endowed with the above product is a Jordan algebra. This is equivalent to the following conditions (i), (ii) and (iii) : $$\left\{
\begin{array}{l}
\mathrm {(i)}\>\>\> x\Phi=\Phi x\\
\mathrm {(ii)}\>\>\> x(x^2\Phi)=x^2(x\Phi)\\
\mathrm {(iii)}\>\>\> (x^2y)\Phi -x^2(y\Phi)=2((xy)(x\Phi)-x(y(x\Phi)))
\end{array}
\right.$$ for $x,y\in J$ and $\Phi\in M$. When $J$ is unital with unit denoted by $\mbox{\rm 1\hspace {-.6em} l}$, the Jordan bimodule $M$ will be said to be *unital* whenever it satisfies the further condition (iiii)\
$\mathrm{(iiii)}\>\>\>\> \mbox{\rm 1\hspace {-.6em} l}\Phi=\Phi$\
for any $\Phi\in M$, which implies that $J\oplus M$ is again a unital Jordan algebra with unit $\mbox{\rm 1\hspace {-.6em} l}$.\
It follows from Condition (i) that one can restrict attention to the left action (for instance), this is why Jordan bimodules are usually refered to as *Jordan modules*.\
Let us define the linear mapping $x\mapsto L_x$ of $J$ into the algebra ${\cal L}(M)$ of linear endomorphisms of the $J$-module $M$ by setting $$L_x\Phi=x\Phi
\label{LM}$$ for $x\in J$ and $\Phi\in M$. Then (ii) reads $$=0
\label{Lxx2}$$ for $x\in J$, while (iii) reads $$L_{x^2y}-L_{x^2}L_y-2L_{xy}L_x+2L_xL_yL_x=0$$ for $x,y\in J$ which is equivalent to $$L_{x^3}-3L_{x^2}L_x+2L^3_x=0
\label{Lx3}$$ and $$,L_z]+L_{[x,z,y]}=0
\label{intder}$$ for $x,y,z\in J$ where $[x,z,y]=(xz)y-x(zy)$ is the associator.\
Thus Conditions (ii) and (iii) can be replaced by Conditions ([\[Lxx2\]](#Lxx2){reference-type="ref" reference="Lxx2"}), ([\[Lx3\]](#Lx3){reference-type="ref" reference="Lx3"}) and ([\[intder\]](#intder){reference-type="ref" reference="intder"}) above while the unital condtion (iiii) reads $$L_{\mbox{\rm 1\hspace {-.6em} l}} =\mbox{\rm 1\hspace {-.6em} l}
\label{L1}$$ where on the right-hand side $\mbox{\rm 1\hspace {-.6em} l}$ denotes the unit of the algebra ${\cal L}(M)$.\
Notice that if $p\in J$ is an idempotent, i.e. satisfies $p^2=p$, then ([\[Lx3\]](#Lx3){reference-type="ref" reference="Lx3"}) reads $$L_p-3 L^2_p+ 2L^3_p=0$$ that is $$L_p(L_p-\frac{1}{2})(L_p-1)=0
\label{p}$$ from which follows the associated Pierce decomposition of the module $M$.

## $J^8_3$-modules and $SU(3)\times SU(3)$-action

Any Jordan algebra $J$ is canonically a Jordan module over itself which is unital whenever $J$ has a unit. The list of the unital irreducible Jordan modules over the finite-dimensional simple Euclidean Jordan algebras can be found in [@jac:1968]. In the case of the exceptional Jordan algebra $J^8_3$, it turns out that any unital Jordan module is a product or a direct sum of modules isomorphic to $J^8_3$, [@jac:1968]. In particular any finite module $M$ over $J^8_3$ is a finite product (or direct sum) of modules isomorphic to $J^8_3$ so that one has $M=J^8_3\otimes E$ for some finite-dimensional real vector space $E$.\
In view of our interpretation of the quark-lepton symmetry it is important to describe the subgroup of $F_4$ which preserves the representations of the octonions occuring in the elements of $J^8_3$ as elements of $\mathbb C\oplus\mathbb C^3$. For this, following [@yok:2009], one associates to the element $$\left(
\begin{matrix}
\zeta_1 & x_3 & \bar x_2\\
\bar x_3 & \zeta_2 & x_1\\
x_2 & \bar x_1 & \zeta_3
\end{matrix}
\right)
\label{jel}$$ of $J^8_3$ the following element $$\left(
\begin{matrix}
\zeta_1 & z_3 & \bar z_2\\
\bar z_3 & \zeta_2 & z_1\\
z_2 & \bar z_1 & \zeta_3
\end{matrix}
\right) +(Z_1,Z_2,Z_3)
\label{cjl}$$ of $J^2_3\oplus M_3(\mathbb C)$ where $$x_i=z_i+Z_i\in \mathbb C \oplus \mathbb C^3
\label{coc}$$ are the representation in $\mathbb C\oplus \mathbb C^3$ of the 3 elements $x_i$ of $\mathbb O$. The desired subgroup of $F_4$ is the group $SU(3)\times SU(3)/\mathbb Z_3$ with action induced by the action of $SU(3)\times SU(3)$ on $J^2_3\oplus M_3(\mathbb C)$ given by [@yok:2009] $$H\mapsto VHV^\ast, \>\>\> M\mapsto UMV^\ast
\label{acg}$$ for $(U,V)\in SU(3)\times SU(3)$ and $H\in J^2_3={\cal H}_3(\mathbb C), M\in M_3(\mathbb C)$. Notice that the action of the first factor $U$ is the one which corresponds to the previous action of $SU(3)$ on $\mathbb C\oplus \mathbb C^3$ $(\simeq \mathbb O)$ described in Section 2. Thus with the previous interpretation, the first factor $SU(3)$ is the "colour group\". The second factor $SU(3)$ mixes the generations and furthermore mixes the complexes $z_i$ corresponding to generations of leptons with the reals $\zeta_i$ of the diagonal which correspond in this picture to new particles of spin 1/2. Since the mass scales of the 3 generations are very different this latter factor $SU(3)$ must be strongly broken, however there could remain some unbroken finite subgroup of this $SU(3)$ which should then play a role in this approach for the see-saw mechanism and the structure of the fermion mass matrices.
