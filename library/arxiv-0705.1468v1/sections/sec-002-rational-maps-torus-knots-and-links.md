---
doc_id: arxiv-0705.1468v1
doc_title: "Knots in the Skyrme-Faddeev model"
section_id: sec-002-rational-maps-torus-knots-and-links
section_title: "Rational maps, torus knots and links"
section_number: null
pages: 7-11
source_pdf: 0705.1468v1.pdf
source_sha256: 4ff578cb3657e4a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "Knots in the Skyrme-Faddeev model — The Skyrme-Faddeev model is a modiﬁed sigma model in three-dimensional space, which has string-like topological solitons classiﬁed by the integer-valued Hopf"
---
Torus knots are classified by a pair $(a,b)$ of coprime positive integers with $a>b.$ A knot is a torus knot if it lies on the surface of a torus, in which case the integers $a$ and $b$ count the number of times that the knot winds around the two cycles of the torus. The simplest example is the trefoil knot, which is the $(3,2)$-torus knot and has three crossings. In the standard knot catalogue notation it is $3_1,$ where the number refers to the crossing number of the knot and the subscript labels its position in the knot catalogue. Other torus knots which will be of interest in this paper include the $(5,2)$-torus knot, also known as Solomon's seal knot, which has five crossings (knot $5_1$ in the catalogue), and the $(4,3)$-torus knot which has crossing number eight (knot $8_{19}$ in the catalogue). In general the $(a,b)$-torus knot has crossing number $C=a(b-1).$

Denote by ${\cal K}_{a,b}$ any field configuration in which the position curve is an $(a,b)$-torus knot. Such a field configuration will have Hopf charge $Q=C+T,$ where $C=a(b-1)$ is the knot crossing number and the integer $T$ counts the number of times that the linking curve twists around the position curve (only situations where the orientation is such that $T$ is non-negative will be of relevance here). The main aim of this section is to construct fields of type ${\cal K}_{a,b}$ for a large range of charges $Q.$

The first step is to recall the standard description [@BK] of a torus knot as the intersection of a complex algebraic curve with the three-sphere. Consider $(Z_1,Z_0)\in \hbox{\mybb C}^2$ and the unit three-sphere $S^3\subset \hbox{\mybb C}^2$ given by $|Z_1|^2+|Z_0|^2=1.$ Then the intersection of this three-sphere with the complex algebraic curve $Z_1^a+Z_0^b=0$ is indeed the $(a,b)$-torus knot.

To use the above description to produce a field configuration, the spatial coordinates $(x_1,x_2,x_3)\in \hbox{\mybb R}^3$ are mapped to the unit three-sphere via a degree one spherically equivariant map. Explicitly, $$(Z_1,Z_0)=((x_1+ix_2)\frac{\sin f}{r},\cos
f+i\frac{\sin f}{r}x_3),$$where $r^2=x_1^2+x_2^2+x_3^2$ and the profile function $f(r)$ is a monotonically decreasing function of the radius $r$, with boundary conditions $f(0)=\pi$ and $f(\infty)=0.$ The precise form of this function will be specified shortly.

A Riemann sphere coordinate $W,$ is used on the target two-sphere of the field $\mbox{\boldmath $\phi$},$ determined via stereographic projection as $$W=\frac{\phi_1+i\phi_2}{1+\phi_3}.$$With these definitions, then constructing a map $\mbox{\boldmath $\phi$}:\hbox{\mybb R}^3\mapsto S^2$ is equivalent to specifying $W(Z_1,Z_0),$ that is, $W:S^3\mapsto \hbox{\mybb C}\hbox{\mybb P}^1,$ a map from the three-sphere to the complex projective line. This map will be taken to be a rational map, which means that $W=p/q,$ where both $p$ and $q$ are polynomials in the variables $Z_1$ and $Z_0.$

For an $(a,b)$-torus knot the mapping is chosen to have the form $$W=\frac{p}{q}=\frac{Z_1^\alpha Z_0^\beta}{Z_1^a+Z_0^b},
\label{ratmap}$$where $\alpha$ is a positive integer and $\beta$ is a non-negative integer. A map of this form has the correct boundary conditions at spatial infinity, since as $r\rightarrow\infty$ then $(Z_1,Z_0)\rightarrow(0,1)$ and, because $\alpha>0,$ this gives $W\rightarrow 0,$ which is the stereographic projection of the point $\mbox{\boldmath $\phi$}=(0,0,1)={\bf e}_3.$ Furthermore, the position curve is the preimage of the point $-{\bf e}_3,$ which corresponds to $W=\infty,$ and hence is given by $q=0=Z_1^a+Z_0^b.$ As the coordinates $(Z_1,Z_0)$ automatically lie on the unit three-sphere then the position curve is the $(a,b)$-torus knot, for all values of $\alpha$ and $\beta.$

The Hopf charge of the map determined by ([\[ratmap\]](#ratmap){reference-type="ref" reference="ratmap"}) is given by the cross ratio $$Q=\alpha b+\beta a.\label{charge}$$To see this note that a rational map $$W:S^3\mapsto \hbox{\mybb C}\hbox{\mybb P}^1, \quad
\mbox{given\ by} \quad W(Z_1,Z_0)=\frac{p(Z_1,Z_0)}{q(Z_1,Z_0)},$$ has a natural extension to a map $$(p,q):\hbox{\mybb B}^4\subset
\hbox{\mybb C}^2\mapsto \hbox{\mybb C}^2, \quad \mbox{given\ by} \quad
(p(Z_1,Z_0),q(Z_1,Z_0)).$$Here $\hbox{\mybb B}^4$ denotes the 4-ball with boundary $S^3,$ and is obtained by replacing the constraint $|Z_1|^2+|Z_0|^2=1$ by the inequality $|Z_1|^2+|Z_0|^2\le 1.$ The map $(p,q)$ is between manifolds of the same dimension and has a degree, defined by counting preimages of a generic point of the target space, weighted by the signs of the Jacobian. As all the other mappings involved in the ansatz have degree one, and the standard Hopf map $(p,q)\mapsto p/q$ is employed, then the Hopf charge $Q$ of the combined mapping is equal to the degree of the mapping $(p,q).$ Furthermore, as the mapping $(p,q)$ is holomorphic then the sign of the Jacobian of all generic preimage points is positive, so the degree is simply the number of preimages.

For the mapping $(p,q)$ given by ([\[ratmap\]](#ratmap){reference-type="ref" reference="ratmap"}) take the generic point in target space to be $(\epsilon,0),$ so the Hopf charge is the number of solutions of the equation $(Z_1^\alpha
Z_0^\beta,Z_1^a+Z_0^b)=(\epsilon, 0).$ Writing $Z_0$ in terms of $Z_1$ from the first component of this equation and substituting into the second component yields the polynomial equation $Z_1^{\alpha b+\beta a}=(-1)^\beta\epsilon^b,$ which clearly has $Q=\alpha b+\beta a$ solutions, as stated.

For any $(a,b)$-torus knot the above ansatz can be used to construct a field configuration of the type ${\cal K}_{a,b}$ with Hopf charge $Q,$ providing there are integers $(\alpha,\beta),$ with $\alpha$ positive and $\beta$ non-negative, for which $Q=\alpha b+\beta a.$ For example, in the case of the trefoil knot then $(a,b)=(3,2)$ hence any $Q>3$ can be obtained. In fact a trefoil knot with $Q=3$ can also be obtained by interchanging the roles of $Z_1$ and $Z_0,$ but a field of this type is not relevant, as will be made clear later. Note that for some values of $Q,$ and fixed $(a,b),$ there are multiple solutions for $(\alpha,\beta).$ These multiple solutions produce qualitatively similar fields, in that both describe the same $(a,b)$-torus knot position curve, and the linking curve twists the same number of times around the position curve; though the distribution of twist may vary. In examples where such multiple solutions were used as initial conditions, the energy relaxation algorithm produced identical final results for all choices.

Recall that a profile function $f(r)$ needs to be specified, satisfying the boundary conditions $f(0)=\pi$ and $f(\infty)=0.$ In fact, these are the correct boundary conditions in an infinite domain but in the finite domain used for numerical simulations the last boundary condition needs to be replaced by $f=0$ at the boundary of the numerical grid. As the ansatz is only used to provide initial conditions then most reasonable monotonic functions will suffice. The simulations discussed in this paper were performed on a cubic grid of side-length $2L,$ that is, $-L\le x_i\le L,$ where $2L=15.$ A simple linear profile function was used, given by $f(r)=\pi(L-r)/L,$ for $r\le L$ and zero otherwise. For a given rational map one could aim to minimize the energy of the ansatz over all profile functions, but this has not been attempted for reasons discussed shortly.

As an illustration of the use of the ansatz, consider an approximation to the minimal energy $Q=7$ trefoil knot. To construct a field ${\cal K}_{3,2}$ with $Q=2\alpha+3\beta=7,$ requires $(\alpha,\beta)=(2,1),$ resulting in the map $W=Z_1^2Z_0/(Z_1^3+Z_0^2).$ The field generated from this rational map is displayed in Figure [1](#fig-approx){reference-type="ref" reference="fig-approx"}a, where both the position and linking curves are shown. It is clear from this figure that the field has similar qualitative features to the minimal energy soliton, in that it is a trefoil knot with four twists. The main qualitative difference is that the ansatz produces a more symmetric field, having a cyclic $C_3$ symmetry. This symmetry is obvious from the form of the rational map, as a rotation by $120^\circ$ around the $x_3$-axis corresponds to the transformation $Z_1\mapsto e^{2\pi i/3}Z_1,$ upon which the rational map changes by only a phase; which is simply an action of the global $O(2)$ symmetry on target space.

<figure id="fig-approx">
<div class="center">
<embed src="approx76.ps" style="width:10cm" />
</div>
<figcaption>The position (light tube) and linking (dark tube) curves for initial conditions created using the rational map ansatz: (a) <span class="math inline"><em>Q</em> = 7</span> trefoil knot; (b) <span class="math inline"><em>Q</em> = 6</span> link <span class="math inline">${\cal L}_{2,2}^{1,1}.$</span> </figcaption>
</figure>

Using the above field as the initial condition for an energy relaxation simulation yields the minimal energy soliton very quickly, and certainly requires far less computational resources than computing the solution from a perturbed axial configuration. Note that, in practice, the cyclic $C_3$ symmetry is slightly broken by the cubic numerical grid, and in particular its boundary, so an explicit symmetry breaking perturbation is not required. In examples discussed later, where initial conditions have a cyclic $C_4$ symmetry, then the configuration is created with a slight displacement from the centre of the grid to again slightly break any exact symmetry.

As mentioned above, the profile function could be optimized to find the minimal energy configuration, for a given rational map, but this has not been attempted. As with the above example, generally the ansatz is more symmetric than the relaxed solution, so it is not expected that a good estimate of the energy can be obtained in this way. It might be possible to improve the approximation to a quantitative level by minimizing over families of rational maps, which include symmetry breaking terms, rather than using the rational maps in this paper; chosen to be the simplest with the correct qualitative features. In this case it would be worthwhile to also minimize the profile function, but as the minimization problem couples the rational map and the profile function together then this is not a simple numerical task. In fact, this numerical problem appears to have about the same level of difficulty as performing energy relaxation via full field simulations. As the energy relaxation code produces a solution very quickly and efficiently from the simple ansatz, then there appears little need to try and improve upon it. The profile function could be adjusted to a minimal extent, for example, by including parameters to set the scale and thickness of the knot, but again this has not been necessary.

So far only knot initial conditions have been considered, but the ansatz can also be used to construct a variety of unknots and links by choosing suitable rational maps. For example, axial fields of the form ${\cal A}_{n,m}$ are generated by a rational map $W=Z_1^n/Z_0^m.$

Links correspond to rational maps in which the curve determined by the denominator is reducible. The torus knot maps with $(a,b)$ coprime degenerate to links if $(a,b)$ are not coprime. As an example, links of the type ${\cal L}_{n,n}^{1,1}$ (which have Hopf charge $Q=2n+2$) are derived from the rational map $$W=\frac{Z_1^{n+1}}{Z_1^2-Z_0^2} =
\frac{Z_1^n}{2(Z_1-Z_0)}+\frac{Z_1^n}{2(Z_1+Z_0)},\label{links}$$ where the partial fraction decomposition reveals the charges of the constituent links by comparison with the axial maps. The $Q=6$ field constructed using the rational map $(\ref{links})$ with $n=2$ is displayed in Figure [1](#fig-approx){reference-type="ref" reference="fig-approx"}b. As can be seen from this figure, the field is qualitatively similar to the minimal energy $Q=6$ soliton, which is of the type ${\cal L}_{2,2}^{1,1}.$ More examples of rational maps associated to linked configurations will appear in the following section.

::: {#tab-relax}
  ---- ---------------------------- -------------------------------- ------------------------ ------------------------ ------------------------ ------------------------
                 initial                                                                                                                        
   Q           $\downarrow$                                                                                                                     
                  final                                                                                                                         
             ${\cal K}_{3,2}$                                                                                                                   
   5           $\downarrow$                                                                                                                     
          ${\cal L}_{1,2}^{1,1}$                                                                                                                
             ${\cal K}_{3,2}$                                                                                                                   
   6           $\downarrow$                                                                                                                     
          ${\cal L}_{2,2}^{1,1}$                                                                                                                
             ${\cal K}_{3,2}$            ${\cal L}_{2,3}^{1,1}$                                                                                 
   7           $\downarrow$                   $\downarrow$                                                                                      
             ${\cal K}_{3,2}$               ${\cal K}_{3,2}$                                                                                    
          ${\cal L}_{3,3}^{1,1}$         ${\cal L}_{2,2}^{2,2}$       ${\cal L}_{4,2}^{1,1}$      ${\cal K}_{5,2}$         ${\cal K}_{3,2}$     
   8           $\downarrow$                   $\downarrow$                 $\downarrow$             $\downarrow$             $\downarrow$       
          ${\cal L}_{3,3}^{1,1}$         ${\cal L}_{3,3}^{1,1}$       ${\cal L}_{3,3}^{1,1}$   ${\cal L}_{3,3}^{1,1}$      ${\cal K}_{3,2}$     
        ${\cal L}_{1,1,1}^{2,2,2}$          ${\cal K}_{4,3}$                  ${\cal              ${\cal K}_{5,2}$      ${\cal L}_{2,3}^{2,2}$   ${\cal L}_{3,4}^{1,1}$
                                                                            K}_{3,2}$                                                           
   9           $\downarrow$                   $\downarrow$                 $\downarrow$             $\downarrow$             $\downarrow$             $\downarrow$
        ${\cal L}_{1,1,1}^{2,2,2}$     ${\cal L}_{1,1,1}^{2,2,2}$        ${\cal K}_{3,2}$         ${\cal K}_{3,2}$         ${\cal K}_{3,2}$         ${\cal K}_{3,2}$
        ${\cal L}_{1,1,2}^{2,2,2}$          ${\cal K}_{4,3}$                  ${\cal           ${\cal L}_{5,3}^{1,1}$      ${\cal K}_{5,2}$         ${\cal K}_{3,2}$
                                                                         L}_{3,3}^{2,2}$                                                        
   10          $\downarrow$                   $\downarrow$                 $\downarrow$             $\downarrow$             $\downarrow$             $\downarrow$
        ${\cal L}_{1,1,2}^{2,2,2}$     ${\cal L}_{1,1,2}^{2,2,2}$     ${\cal L}_{3,3}^{2,2}$   ${\cal L}_{3,3}^{2,2}$   ${\cal L}_{3,3}^{2,2}$      ${\cal K}_{3,2}$
             ${\cal K}_{4,3}$               ${\cal K}_{5,2}$             ${\cal K}_{7,2}$              ${\cal                                   
                                                                                                     K}_{3,2}$                                  
   11          $\downarrow$                   $\downarrow$                 $\downarrow$             $\downarrow$                                
        ${\cal L}_{1,2,2}^{2,2,2}$          ${\cal K}_{5,2}$          ${\cal L}_{3,4}^{2,2}$      ${\cal K}_{3,2}$                              
             ${\cal K}_{5,3}$               ${\cal K}_{3,2}$             ${\cal K}_{5,2}$              ${\cal                                   
                                                                                                     K}_{7,2}$                                  
   12          $\downarrow$                   $\downarrow$                 $\downarrow$             $\downarrow$                                
        ${\cal L}_{2,2,2}^{2,2,2}$          ${\cal K}_{4,3}$             ${\cal K}_{5,2}$      ${\cal L}_{4,4}^{2,2}$                           
             ${\cal K}_{3,2}$               ${\cal K}_{5,3}$             ${\cal K}_{5,2}$              ${\cal                                   
                                                                                                     K}_{7,2}$                                  
   13          $\downarrow$                   $\downarrow$                 $\downarrow$             $\downarrow$                                
             ${\cal K}_{4,3}$               ${\cal X}_{13}$              ${\cal K}_{5,2}$      ${\cal L}_{3,4}^{3,3}$                           
             ${\cal K}_{4,3}$               ${\cal K}_{5,3}$             ${\cal K}_{3,2}$                                                       
   14          $\downarrow$                   $\downarrow$                 $\downarrow$                                                         
             ${\cal K}_{4,3}$               ${\cal K}_{5,3}$             ${\cal K}_{5,2}$                                                       
             ${\cal K}_{5,3}$               ${\cal K}_{4,3}$             ${\cal K}_{3,2}$                                                       
   15          $\downarrow$                   $\downarrow$                 $\downarrow$                                                         
             ${\cal X}_{15}$           ${\cal L}_{1,1,1}^{4,4,4}$        ${\cal K}_{5,3}$                                                       
             ${\cal K}_{4,3}$        ${\cal L}_{1,1,1,1}^{3,3,3,3}$      ${\cal K}_{3,2}$                                                       
   16          $\downarrow$                   $\downarrow$                 $\downarrow$                                                         
             ${\cal X}_{16}$                ${\cal X}_{16}$              ${\cal X}_{16}$                                                        
  ---- ---------------------------- -------------------------------- ------------------------ ------------------------ ------------------------ ------------------------
:::

  Table 1: Initial conditions and final solutions. []{#tab-relax label="tab-relax"}

 

::: {#tab-energies}
   $Q$              type               $E$    $E/Q^{3/4}$
  ----- ---------------------------- ------- -------------
    1              ${\cal             1.204      1.204
                 A}_{1,1}$                   
    2         ${\cal A}_{2,1}$        1.967      1.170
    3    $\widetilde{\cal A}_{3,1}$   2.754      1.208
    4         ${\cal A}_{2,2}$        3.445      1.218
    5              ${\cal             4.095      1.225
              L}_{1,2}^{1,1}$                
    6              ${\cal             4.650      1.213
              L}_{2,2}^{1,1}$                
    7         ${\cal K}_{3,2}$        5.242      1.218
    8      ${\cal L}_{3,3}^{1,1}$     5.821      1.224
    8         ${\cal K}_{3,2}$        5.824      1.224
    9    ${\cal L}_{1,1,1}^{2,2,2}$   6.360      1.224
    9         ${\cal K}_{3,2}$        6.385      1.229
   10    ${\cal L}_{1,1,2}^{2,2,2}$   6.905      1.228
   10      ${\cal L}_{3,3}^{2,2}$     6.923      1.231
   10         ${\cal K}_{3,2}$        6.973      1.240
   11    ${\cal L}_{1,2,2}^{2,2,2}$   7.391      1.224
   11         ${\cal K}_{5,2}$        7.502      1.242
   11      ${\cal L}_{3,4}^{2,2}$     7.533      1.247
   11         ${\cal K}_{3,2}$        7.614      1.261
   12    ${\cal L}_{2,2,2}^{2,2,2}$   7.833      1.215
   12         ${\cal K}_{4,3}$        7.857      1.219
   12         ${\cal K}_{5,2}$        8.070      1.252
   12      ${\cal L}_{4,4}^{2,2}$     8.093      1.255
   13         ${\cal K}_{4,3}$        8.272      1.208
   13         ${\cal X}_{13}$         8.462      1.236
   13         ${\cal K}_{5,2}$        8.574      1.252
   13      ${\cal L}_{3,4}^{3,3}$     8.633      1.261
   14         ${\cal K}_{4,3}$        8.761      1.210
   14         ${\cal K}_{5,3}$        8.807      1.217
   14         ${\cal K}_{5,2}$        9.124      1.261
   15         ${\cal X}_{15}$         9.290      1.219
   15    ${\cal L}_{1,1,1}^{4,4,4}$   9.404      1.234
   15         ${\cal K}_{5,3}$        9.408      1.234
   16              ${\cal             9.769      1.221
                  X}_{16}$                   
:::

Table 2: Solution types and energies.[]{#tab-energies label="tab-energies"}
