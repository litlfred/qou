---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-002-21-basic-properties
section_title: "Basic Properties"
section_number: 2.1
pages: 3-8
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.982
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
Towards proving the birational equivalence of the two models given for Bring's curve we begin with some basic properties of the curve. We introduce affine coordinates $(x,y)=(X/Z,Y/Z)$ such that the HC-model is $0=f(x,y)=F(x,y,1)$. Then $\mathop{\mathrm{Res}}_y(f(x,y),\partial_y f(x,y))=x^4(x^5-1)^2(256x^{10}-837 x^5+3456)$. Investigation of the vanishing of this resultant leads to the following.

::: lemma
[]{#HCdoublepoints label="HCdoublepoints"} The only singular (double) points in the HC-model of the curve are $V_k = [\zeta^k : \zeta^{2k} : 1]$ for $k=0, \dots, 4$, where $\zeta=\exp(2\pi i/5)$, and $V_5 = [1:0:0]$.
:::

We shall return these points in due course; each of these singular points desingularizes to two points. We also find

::: lemma
[]{#lemma: local expansion in Bring's curve label="lemma: local expansion in Bring's curve"} In the HC-model we have local expansions about the following points on the curve $$\begin{aligned}
a&:=[0:0:1]\simeq[2t^3:t:1],& b&:=[0:1:0]\simeq[2t^2:1/t:1],\\
c&:=[1:0:0]_2\simeq[1:t:t^4],& d&:=[1:0:0]_1\simeq[1:t^4:t].
\end{aligned}$$
:::

We see from this that

::: corollary
$$\mathop{\mathrm{div}}(x)=3a+2b-4c-d,\qquad \mathop{\mathrm{div}}(y)=a-b-3c+3d,\qquad R_F = 2a + b+ 3c + \sum_i r_i,$$ where $R_F$ is the ramification divisor corresponding to the map $x:\mathcal{B} \to \mathbb{P}^1$ and the $r_i$ are the roots of the polynomial $256 x^{10} - 837 x^5 + 3456$ appearing in the resultant.
:::

::: lemma
[]{#lemma: basis of differentials label="lemma: basis of differentials"} The genus of Bring's curve is $g=4$ and we have the ordered basis of (unnormalised) differentials $$\begin{aligned}
  v_1 &= \frac{(y^3-x)\mathrm{d}x}
    {\partial_y f(x,y)}, &
  v_2 &= \frac{(y^2x-1)\mathrm{d}x}
    {\partial_y f(x,y)}, &
  v_3 &= \frac{(y-x^2)\mathrm{d}x}
    {\partial_y f(x,y)}, &
  v_4 &= \frac{y(x^2-y)\mathrm{d}x}
    {\partial_y f(x,y)}.
\end{aligned}$$
:::

These differentials, while independent as holomorphic differentials, do satisfy an algebraic relation.

::: lemma
The canonical embedding of Bring's curve in $\mathbb{P}\sp3=\left\{ [v_1:v_2:v_3:v_4] \right\}$ lies on the quadric $$\label{quaddif}
\mathcal{Q}:  v_1v_2+v_3v_4=0  .$$
:::

While all full-rank quadrics in $\mathbb{P}^3$ are isomorphic to $\mathbb{P}^1 \times \mathbb{P}^1$ [@Vakil2010], the standard proof of which goes via showing every such quadric can be written in some coordinate system as $\mathcal{Q}$, we will subsequently want an explicit form of the isomorphism.

::: prop
[]{#prop: quadric of canonical embedding isomorphic to PxP label="prop: quadric of canonical embedding isomorphic to PxP"} $\mathcal{Q}\simeq \mathbb{P}\sp1\times\mathbb{P}\sp1$.
:::

::: proof
*Proof.* Consider the map $\mathcal{Q} \to \mathbb{P}^1 \times \mathbb{P}^1$, a modification of the Segre embedding, given by $$\varphi: \mathbb{P}\sp1\times\mathbb{P}\sp1\rightarrow \mathbb{P}\sp3,\qquad
\varphi([u:v],[z:w])=[uz:vw:vz:-uw]:=[v_1:v_2:v_3:v_4]  .$$ Then $\varphi([u:v],[z:w])\in \mathcal{Q}$.

The map $\varphi$ is injective for suppose $\varphi([u:v],[z:w])=\varphi([u':v'],[z':w'])$. Consider first that $v_4\ne0$. Then $$-\frac{v_1}{v_4}=\frac{z}{w}=\frac{z'}{w'},\qquad -\frac{v_2}{v_4}=\frac{v}{u}=\frac{v'}{u'} ,$$ and so correspond to the same point in $\mathbb{P}\sp1\times\mathbb{P}\sp1$. Next suppose that $0=-v_4=uw=u'w'$ and without loss of generality that $u=0$. If $u'=0$ we have injectivity, so suppose that $u'\ne0$. Then $w'=0$ and $[0:vw:vz:0]=[u'z':0:v'z':0]$ requiring $z'=0$ and a contradiction. Thus we have that $\varphi$ is injective.

To show the surjectivity of $\varphi$ we may assume without loss of generality that $v_4\ne0$. Then set $$-\frac{v_1}{v_4}=\frac{z}{w},\qquad -\frac{v_2}{v_4}=\frac{v}{u}  .$$ Indeed we can spot the inverse map $\varphi^{-1} : \mathcal{Q} \to \mathbb{P}^1 \times \mathbb{P}^1$ to be given by $$\varphi^{-1}([v_1:v_2:v_3:v_4]) = \left \lbrace \begin{array}{cc}
    ([v_1:v_3], [v_3:v_2]) & \left\{ v_1, v_3 \right\}  \neq \left\{ 0 \right\}  \neq \left\{ v_2, v_3 \right\} , \\
    ([-v_4:v_2], [v_3:v_2]) & \left\{ v_1, v_3 \right\}  = \left\{ 0 \right\}  \neq \left\{ v_2, v_3 \right\}  ,\\
    ([v_1:v_3], [v_1:-v_4]) & \left\{ v_1, v_3 \right\}  \neq \left\{ 0 \right\}  = \left\{ v_2, v_3 \right\}  ,\\
    ([-v_4:v_2], [v_1:-v_4]) & \left\{ v_1, v_3 \right\}  = \left\{ 0 \right\}  = \left\{ v_2, v_3 \right\} .
\end{array} \right .$$ ◻
:::

::: prop
[]{#prop: Canonical divisor of Bring's curve label="prop: Canonical divisor of Bring's curve"} The canonical divisor class on Bring's curve is $[\mathcal{K}_{\mathcal{B}}] = [a+2b+3c]$.
:::

::: proof
*Proof.* This may be shown analytically or (as given in the accompanying notebook) entirely using computer algebra. To show this analytically we use $\mathop{\mathrm{div}}(dx) = -2(4c+d) + R_F$. ◻
:::

We now establish the main result of this subsection.

::: prop
[]{#prop: HC valid model for Bring label="prop: HC valid model for Bring"} The HC-model ([\[eq: P2 model of Bring\]](#eq: P2 model of Bring){reference-type="ref" reference="eq: P2 model of Bring"}) is a model of Bring's curve ([\[eq: P4 model of Bring\]](#eq: P4 model of Bring){reference-type="ref" reference="eq: P4 model of Bring"}).
:::

::: proof
*Proof.* We will prove this by explicitly constructing the birational transform. To do so we make use of the proof of Theorem 3 in [@Dye1995], where the author considers a particular Clebsch hexagon[^1], constructs a pencil of plane sextics from this, and finds Bring's curve as the canonical model of a distinguished point in this pencil. By assuming that the HC-model is already the distinguished curve in a pencil, we can construct the birational map. Note this is a fundamentally different approach to the that originally taken with the HC-model, which was derived from considerations of the modular theory of the curve.

Explicitly, Dye introduces $j$ as a solution to $j^2-j-1=0$ and then defines the pencil of curves[^2] $S_\lambda = S+ \lambda \left \lvert \mathcal{C} \right \rvert^3$ where $$\label{dyespencil}
\begin{split}
    S(x,y,z) &= (x+jy)^6+(x-jy)^6+(y+jz)^6+(y-jz)^6+(z+jx)^6+(z-jx)^6  , \\
    \mathcal{C}(x,y,z) &= x^2 + y^2 + z^2  .
\end{split}$$ Next Dye considers the Clebsch hexagon $H$ with vertices $$(1, \pm j, 0)  , \quad (0, 1, \pm j)  , \quad (\pm j, 0, 1) ,$$ for which the corresponding 10 Brianchon points are at $$(\pm j^2, 1, 0)  , \quad (0, \pm j^2, 1)  , \quad (1, 0, \pm j^2)  , \quad (1, \pm 1, \pm 1).$$ Dye shows that there is a unique member of the pencil, which he calls $\Gamma$, that contains the vertices. Moreover, $\Gamma$ has the vertices and only the vertices as double points.

To get a canonical model for $\Gamma$, which Dye show's has genus 4, we now need a little theory from [@Semple1949 pp. 122-124], namely that a generic cubic surface in $\mathbb{P}^3$ is birational to a system of plane cubics through 6 base points. We apply this taking these six points to be the vertices of the hexagon $H$. Such a generic cubic surface $F \subset \mathbb{P}^3$ can be written as the vanishing of a determinant $$\begin{vmatrix} u_1 & v_1 & w_1 \\ u_2 & v_2 & w_2 \\ u_3 & v_3 & w_3 \end{vmatrix} = 0  ,$$ where $u_1, \dots, w_3$ are linear homogeneous functions of the $\mathbb{P}^3$ coordinates, that is to say $P=[L_1 : L_2 : L_3 : L_4]\in F\subset \mathbb{P}^3$ if and only if there exists $P^\prime=[X : Y : Z] \in \mathbb{P}^2$ such that $$\begin{aligned}
    X u_i(P) +Y v_i(P) + Z w_i(P) = 0  .
\end{aligned}$$ Thinking of $P^\prime$ as a point in a plane $\Pi$ we get a birational transformation $\Pi \leftrightarrow F$, $P^\prime \leftrightarrow P$. The map $\Psi : \Pi \to F$ will have the $L_a$ as homogeneous cubics in $X, Y, Z$. To see this rewrite the determinant equation as (for $i=1,2,3$) $$\sum_{a=1}\sp{4} a_{ia}(P^\prime) L_a = 0$$ for some $a_{ia}$ linear homogeneous in the $X,Y,Z$. On each affine patch $L_a \neq 0$ solving this involves inverting a $3 \times 3$ matrix whose entries are linear homogeneous polynomials in $X,Y,Z$. Likewise, given the $L_a$, we have a 3-parameter family of cubics given by $$a L_1 + b L_2 + c L_3 + d L_4 = 0 \quad \text{for} \quad [a:b:c:d] \in \mathbb{P}^3  .$$ A cubic in $\mathbb{P}^2$ has 10 projective coefficients, and so a 3-parameter family is defined by 6 constraints. Generically we can take those constraints to come in the form of intersection with 6 generic points $O_i \in \Pi$.

For our purposes, the six points we want to intersect with are the vertices of the Clebsch hexagon, which are the double points of the exceptional curve $\Gamma$. Assuming the the HC-model gives such an exceptional curve, we take the points $V_k$ identified in Lemma [\[HCdoublepoints\]](#HCdoublepoints){reference-type="ref" reference="HCdoublepoints"}. Hence, if we write a generic cubic in $X, Y, Z$ as $$a_0 X^3 + a_1 X^2 Y + a_2 X^2 Z + a_3X Y^2 + a_4 X Y Z + a_5 X Z^2 + a_6 Y^3 + a_7 Y^2 Z + a_8 Y Z^2 + a_9 Z^3$$ the equations on the coefficients we get (coming from intersecting with $V_k$ ($k=0,\dots,4$) and $V_5$ respectively) are $$\begin{aligned}
    a_0 \zeta^{3k} + a_1 \zeta^{4k} + a_2 \zeta^{2k} + a_3 + a_4 \zeta^{3k} + a_5 \zeta^k + a_6 \zeta^{k} + a_7 \zeta^{4k} + a_8 \zeta^{2k} + a_9 &= 0, \\
    a_0   &= 0.  
\end{aligned}$$ Setting the coefficients of $\zeta^{nk}$ to be zero gives us the 3-parameter family of cubics $$\begin{aligned}
 0 &= a X^2 Y + b X^2 Z + cX Y^2  + d X Z^2 -d Y^3 -a Y^2 Z -b Y Z^2 -c Z^3  , \\
 &:= aL_1 + b L_2 + cL_3 + dL_4  .
\end{aligned}$$

Comparing the coefficients we see that our map into $\mathbb{P}^3$ is (essentially) the canonical embedding. as $$[v_1 : v_2 : v_3 : v_4 ] = [-L_4 : L_3 : -L_2 : L_1]  .$$ One can check, using for example Gröbner bases, that the $L_a$ satisfy the equation $$L_2 L_4^2 - L_1^2 L_4 - L_1 L_3^2 + L_2^2 L_3= 0.$$ This is the cubic we call $F$. One can use the package `Cremona` [@Stagliano2018] in Macaulay2 to check that the map $\Psi$ is birational. Note one needs to make sure that the range is chosen such that the map is explicitly surjective, not just use the implicit knowledge that the map is surjective onto its image. Doing so and asking for the inverse map gives $$\begin{aligned}
= [L_2^2 - L_1 L_3 : L_1 L_4 : L_2 L_4] . 
\end{aligned}$$ For example, we can see $$\begin{aligned}
\frac{L_2^2 - L_1 L_3}{L_1 L_4} &= \frac{\left( X^2 Z - Y Z^2 \right)^2 - \left( X^2 Y - Y^2 Z \right)\left( X Y^2 - Z^3 \right)}{\left( X^2 Y - Y^2 Z \right) \left( X Z^2 - Y^3 \right)}  ,  \\
&= \frac{X^4 Z^2 -X^2 Y Z^3 -X^3 Y^3 + X Y^4 Z}{X^3 Y Z^2 - X Y^2 Z^3 - X^2 Y^4 + Y^5 Z} = \frac{X}{Y}  ,
\end{aligned}$$ and $$\frac{L_1L_4}{L_2 L_4} = \frac{L_1}{L_2} = \frac{X^2 Y - Y^2 Z}{X^2 Z - Y Z^2 } = \frac{(X^2 Z - Y Z^2)(Y/Z)}{X^2 Z - Y Z^2 } = \frac{Y}{ Z}  .$$ We now have a cubic surface in $\mathbb{P}^3$ corresponding to the system of curves intersecting the $V_i$. From [@Hirschfeld1986 pp. 198-201] we know there exists a coordinate system in which this cubic can be written as the subset of $\mathbb{P}^4$ $$H_3 = 0 = H_1$$ (this is called 'the' Clebsch surface). To look for such a coordinate system, we write this surface in $\mathbb{P}^3$ as $$\begin{aligned}
0 &= x_1^{2} x_2 + x_1 x_2^{2} + x_1^{2} x_3 +  x_2^{2} x_3 + x_1 x_3^{2} + x_2 x_3^{2} + x_1^{2} x_4 +  x_2^{2} x_4  +  x_3^{2} x_4 + x_1 x_4^{2} + x_2 x_4^{2} + x_3 x_4^{2} \\
&\phantom{=} + 2 x_1 x_2 x_3 + 2 x_1 x_2 x_4 + 2 x_1 x_3 x_4 + 2 x_2 x_3 x_4   .
\end{aligned}$$ From here, one can use the fact that the 10 Eckardt points[^3] of the cubic in $L_a$ form the 10 vertices of a pentahedron [@Hirschfeld1986], and that in the coordinate system of the Clebsch surface in $\mathbb{P}^4$ these lie at the permutations of $[1:-1:0:0:0]$ [@Edge1978]. This gives us a possible way a spotting the transform if we can calculate the Eckardt points of $F$. To do this, we use the identification from [@Dye1995], that the 3 lines in $F$ intersecting to give an Eckardt point come from the 3 edges of $H$ intersecting at a Brianchon point. To this end we find the images of the $V_i V_j$ for which we give a generating set of the ideal corresponding to the line, for example

1.  $\Psi(V_0 V_5) : \left\langle L_4 - L_3, L_2 - L_1 \right\rangle$,

2.  $\Psi(V_1 V_2) : \left\langle L_4 + (\zeta^2 + \zeta+1 )L_2 + (\zeta^4 - \zeta^2 - \zeta)L_1,  L_3 + (\zeta^3+ 2 \zeta^2 + \zeta)L_2 + (\zeta^3 + \zeta^2 + \zeta) L_1 \right\rangle$,

3.  $\Psi(V_3 V_4) : \left\langle L_4 + (-\zeta^2 - \zeta)L_2 + (\zeta^3 + 2\zeta^2 + \zeta)L_1,  L_3 + (\zeta^3 - \zeta - 1)L_2 + (\zeta^2 + \zeta + 1)L_1 \right\rangle$.

Then $$\Psi(V_0 V_5) \cap \Psi(V_1 V_2) \cap \Psi(V_3 V_4) = [-\zeta^3 - \zeta^2 - 1 : -\zeta^3 - \zeta^2 - 1 : 1 : 1] = \Psi(V_0 V_5 \cap V_1 V_2 \cap V_3 V_4)  .$$ One can do likewise to find the other Eckardt points.

Armed now with the knowledge of the Eckardt points, we can find appropriate projective transforms $A$ that biject the sets of Eckardt points by acting $(x_1, x_2, x_3, x_4)^T = A(L_1, L_2, L_3, L_4)^T$, for example $$A = \begin{pmatrix}
\zeta^3 & -1 & -\zeta^{2} & \zeta \\ 1 & -\zeta^3 & -\zeta & \zeta^{2} \\ \zeta^{2} & -\zeta & -1 & \zeta^3 \\ \zeta & -\zeta^2 & -\zeta^3 & 1 \end{pmatrix} .$$ We can then use again Macaulay2 to check that this transform then gives us the correct cubic in $\mathbb{P}^3$. Moreover, if we now restrict to the HC-model in the system of curves that intersect the $V_i$, that is we impose the condition that $F(X, Y, Z)=0$, we get the final degree-2 polynomial on the $x_i$ ($H_2=0$). This quadric is in fact the Schur quadric corresponding to a distinguished double-six[^4] of lines that necessarily exist on a cubic surface constructed as above [@Dye1995]. An equivalent rational map is given in [@Dolgachev2012 p. 557], but the inverse is not provided.

To see this working, let's consider $c$ and $d$, and see that these are desingualrised on the smooth canonical embedding. Taking $[X:Y:Z] = [1:t:t^4]$ we get $$[L_1: L_2: L_3: L_4] = [1: t^3 :t+ t^6 : -t^2]  ,$$ and so taking the limit we get $[1:0:0]_2 \mapsto [1:0:0:0]$ in $L$ coordinates. Acting with $A$, we get the point in $\mathbb{P}^4$ given by $$[x_1 : x_2 : x_3 : x_4 : x_5] = [\zeta^3 : 1 : \zeta^2 : \zeta : \zeta^4]  .$$ Repeating the process taking $[X:Y:Z] = [1:t^4:t]$ gives $[1:0:0]_1 \mapsto [0:1:0:0]$ in $L$ coordinates, which is equivalently $$[x_1 : x_2 : x_3 : x_4 : x_5] = [1 : \zeta^3 : \zeta : \zeta^2 : \zeta^4]  .$$ This makes sense, as the change $Y \leftrightarrow Z$ corresponds to $L_1 \leftrightarrow L_2$, $L_3 \leftrightarrow L_4$.

Moreover, to clarify our last point on the imposition of $H_2=0$, we consider the point $[X:Y:Z] = [0:1:1]$ which does not lie on the HC-model of the curve. Under our birational map this corresponds to the point $$\begin{aligned}
&= [1:  1 :1 :1]  
    \Rightarrow [x_1 : x_2 : x_3 : x_4 : x_5] &=  [2-\sqrt{5} : -2+\sqrt{5} : -1 : 1 : 0]  .
\end{aligned}$$ This point does lie on the Clebsch diagonal surface given by $H_1 = 0 = H_3$, but does not satisfy $H_2=0$. ◻
:::

Note that in the above proof of the equivalence of the Riemann surfaces, the birational map we constructed was defined over $\mathbb{Q}[\zeta]$. As such, to equate the two algebraic curves we need to be working over a field containing $\mathbb{Q}[\zeta]$. We will later see when looking at quotients of Bring's curve that it is insufficient to work over $\mathbb{Q}$. Indeed, note that over $\mathbb{Q}$ there are no solutions to the equations defining Bring's curve in the $\mathbb{P}^4$-model.

[^1]: For the purposes of this definition a hexagon is a set of 6 points in $\mathbb{P}^2$, no three of which are collinear, called the vertices. A **Brianchon point** of a hexagon is a non-vertex point through which 3 edges (the lines joining two distinct vertices) pass. A **Clebsch hexagon** is a hexagon with 10 Brianchon points [@Dye1991].

[^2]: We are using the coordinates $[x,y,z]$ here, distinct from $[X,Y,Z]$, to highlight that these are not those of the HC-model.

[^3]: An **Eckardt point** of a surface is a point where three lines contained within the surface intersect [@Hirschfeld1986].

[^4]: A **double six** is a collection of 12 lines $a_1, \dots, a_6, b_1, \dots, b_6$ in $\mathbb{P}^3$, arranged as $$\begin{array}{cccccc}
        a_1 & a_2 & a_3 & a_4 & a_5 & a_6  \\
        b_1 & b_2 & b_3 & b_4 & b_5 & b_6 
    \end{array}$$ so that each line is disjoint from those in the same row and column, but intersects the other 5 lines.
