---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-38
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
---
1
 
 
 
 
The GAUSS LINKING INTEGRAL 
 
on the 3-SPHERE  
 
and in HYPERBOLIC 3-SPACE 
 
Dennis DeTurck and Herman Gluck 
 
 
      
We introduce here explicit integral formulas for linking, twisting, writhing and helicity 
on the 3-sphere and in hyperbolic 3-space.   
 
   ∙ These formulas, like their prototypes in Euclidean 3-space, are geometric rather than           
   just topological, in the sense that their integrands are invariant under orientation-preserving  
   isometries of the ambient space. 
 
   ∙ They are obtained by developing and then applying a steady-state version of classical   
   electrodynamics in these two spaces, including an explicit Biot-Savart formula for the   
   magnetic field and a corresponding Ampere’s law contained in Maxwell’s equations.   
 
   ∙ The Biot-Savart formula leads, in turn, to upper bounds for the helicity of vector fields  
   and lower bounds for the first eigenvalue of the curl operator on subdomains of the 
   3-sphere and hyperbolic 3-space. 
   
   ∙ We give only a hint of the proofs. 
 
 
 
 
                                                                                                             June 2004 
 
 2
1. Linking integrals in  S3  and  H3 .  
 
Let  K1  =  {x(s)}  and  K2  =  {y(t)}  be disjoint oriented smooth closed curves in 
either the unit 3-sphere  S3  or hyperbolic 3-space  H3 ,  and let  α (x, y)  denote the 
distance from  x  to  y .   
 
The integral formulas below contain vectors lying in different tangent spaces; in 
non-Euclidean settings we must move them to a common location to be combined. 
In  S3  regarded as the group of unit quaternions, the differential  L yx—1  of left 
translation by  yx—1 moves tangent vectors from  x  to  y .  In either  S3  or  H3 , 
parallel transport  Pyx  along the geodesic segment from  x  to  y  also does this. 
 
 
THEOREM 1.  LINKING INTEGRALS  in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format: 
 
         Lk(K1, K2)  =  1/(4π2) ∫K1×K2  Lyx—1 dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt 
 
                     —  1/(4π2) ∫K1×K2  Lyx—1 dx/ds ∙ dy/dt  ds dt  , 
 
where     ϕ(α )  =  (π — α ) cot α  . 
 
(2)  On  S3  in parallel transport format: 
 
         Lk(K1, K2)  =  1/(4π2) ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt , 
   
where     ϕ(α )  =  (π — α ) csc α  . 
 
(3)  On  H3  in parallel transport format: 
 
         Lk(K1, K2)  =  1/(4π) ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt , 
 
where     ϕ(α )  =  csch α  . 
 
For each of the kernel functions  ϕ(α)  above, we have written  ϕ(x, y)  in place of 
ϕ(α (x, y)) . 
 3
 
∙  The kernel functions appearing in these integrals have the following significance. 
 
 In formula (1), the function  ϕ(α )  =  (—1/(4π2)) (π — α) cot α  ,  where  α  is 
 distance from a fixed point, is the fundamental solution of the Laplacian on  S 3 , 
 
∆ϕ  =  δ  —  1/(2π2) . 
 
 Here  δ  is the Dirac δ-function, and, since the volume of  S3  is  2π2 ,  the right- 
 hand side has average value zero.  
 
 In formula (2), the function  ϕ(α )  =  (—1/(4π2)) (π — α) csc α  is the fundamental 
 solution of a shifted Laplacian on  S 3 , 
 
∆ϕ  —  ϕ  =  δ . 
 
 In formula (3), the function  ϕ(α )  =  (—1/(4π)) csch α  is the fundamental 
 solution of a shifted Laplacian on  H 3 , 
 
∆ϕ  +  ϕ  =  δ . 
 
∙  In formula (1), the first integral is the dominant term when the curves are small. 
At the other extreme, for orthogonal great circles, say, the first integral vanishes 
and the second integral takes the value  –1.  In 3-space, the second integral always 
vanishes. 
 
∙  In formula (2), it makes no difference that parallel transport from  x  to  y  on  S 3 
is ambiguous when  y  is the antipode  —x  of  x ,  because when  α  =  π  we have 
∇y(ϕ(α(x, y))  =  0 . 
 
∙  All of the integrands in formulas (1), (2) and (3) are invariant under orientation- 
preserving isometries of the ambient space.  In formula (1), this follows from the 
fact that the group of left translations by unit quaternions is a normal subgroup of 
the group  SO(4)  of all orientation-preserving isometries of  S 3 .  In formulas (2) 
and (3), this is transparent. 
 
∙  The fact that formula (1) on  S3  has no counterpart in  H3  is due to the simplicity 
of the group  SO(3, 1)  of orientation-preserving isometries of  H3 . 
 
∙  Greg Kuperberg, after receiving a copy of this research announcement, wrote to 
us, "As it happens, I thought about this question a few years ago and I obtained one 
of your formulas, I think, but I never wrote it up."  Subsequent correspondence shows 
that he did indeed obtain, by a beautiful geometric argument totally different from 
ours, an expression equivalent to formula (2). 
 4
 
2. Historical background.   
 
 
Carl Friedrich Gauss, in a half-page paper dated January 22, 1833, gave an 
integral formula for the linking number of two disjoint smooth closed curves in 
Euclidean 3-space: 
 
Lk(K1, K2)  =  1/(4π) ∫K1×K2  dx/ds × dy/dt ∙ (x — y)/|x — y|3  ds dt . 
 
According to historian Moritz Epple (l998), Gauss was interested in computing the 
linking number of the earth’s orbit with the orbits of certain asteroids, and although 
he presented his formula without proof, it is believed that he simply counted up how 
many times the vector from the earth to the asteroid covered the "heavenly sphere" 
..... a degree-of-map argument.  Gauss undoubtedly knew another proof: run a 
current through the first loop, and calculate the circulation of the resulting magnetic 
field around the second loop.  By Ampere’s Law, this circulation is equal to the total 
current enclosed by the second loop, which means the current flowing along the first 
loop, multiplied by the linking number of the two loops.  Then the Biot-Savart 
formula (1820) for the magnetic field leads directly to Gauss’s linking integral. 
 
 
Georges Calugareanu, in a series of three papers (1959-1961), let the two curves 
in Gauss’s linking integral come together, and defined a real-valued invariant, later  
called the "writhing number" by F. Brock Fuller (1971), of a smooth simple closed 
curve in Euclidean 3-space, which measures the extent to which the curve wraps 
and coils around itself: 
 
Wr(K)  =  1/(4π) ∫K×K  dx/ds × dy/dt ∙ (x — y)/|x — y|3  ds dt . 
 
In these papers, Calugareanu also discovered the formula  LINK = TWIST + WRITHE ,  
in which  LINK  is the linking number of the two edges of a closed ribbon, TWIST 
measures the extent to which the ribbon twists around one of its edges, and WRITHE 
is the writhing number of that edge. 
 
Calugareanu proved this formula under the assumption that the simple closed curve  K 
has nowhere-vanishing curvature although, as we note in section 11, the basic ideas 
for proving the formula without this assumption are already present in his papers. 
Calugareanu’s formula without this restriction was proved by James White (1969) in 
his thesis, using a totally different approach based on ideas of William Pohl (1968a, b). 
 
 5
 
 
Lodewijk Woltjer introduced in 1958 the notion of "helicity" of a vector field  V  
defined on a domain  Ω  in Euclidean 3-space, 
     
H(V)  =  1/(4π) ∫Ω×Ω   V(x) × V(y) ∙ (x — y)/|x — y|3  d(volx) d(voly) , 
 
as an invariant during ideal MHD evolution of plasma fields.  Keith Moffatt (1969), 
recognizing that this quantity measures the extent to which the field lines of  V  wrap 
and coil around one another, named it "helicity" and showed that Woltjer’s original 
formula could be written in the above form. 
 
 
The formulas of Gauss and Calugareanu serve as cornerstones of geometric knot 
theory in Euclidean space, with rich connections to molecular biology, especially in 
the study of knotted duplex DNA and of the enzymes which affect it, and, through 
the related formula of Woltjer and Moffatt, to fluid dynamics, electrodynamics and 
plasma and solar physics. 
 
 6
 
 
3.  Organization of this report. 
 
Gauss’s degree-of-map derivation of his linking integral does not work on the  
3-sphere  S3  because the set of ordered pairs of distinct points in  S3  deformation 
retracts to a 3-sphere rather than to a 2-sphere, as it does in  R3 .  But a degree-of- 
map derivation, suitably modified, does work in hyperbolic 3-space.  
 
So we begin by developing a steady-state version of classical electrodynamics on  S 3  
and  H3  in sections 4 through 8, including an explicit Biot-Savart formula for the 
magnetic field and a corresponding Ampere’s law contained in Maxwell’s equations. 
In section 9, this enables us to follow Gauss’s second proof of the linking integrals. 
 
With the linking integrals in hand, in sections 10 and 11 we follow the lead  
of Calugareanu towards the writhing and twisting integrals and the formula   
Link  =  Twist  +  Writhe. 
 
In section 12 we follow the lead of Woltjer towards the helicity integrals. 
 
In section 13 we derive upper bounds for the helicity of vector fields in  R 3 ,  S3 
and  H3 ,  and in section 14 we derive lower bounds for the first eigenvalue of 
the curl operator on subdomains of these spaces. 
 
For a development of electrodynamics on bounded subdomains of the 3-sphere, 
and for applications of the linking, writhing and helicity integrals in this setting, 
including a proposed application to solar physics, see the Ph.D. thesis of Jason  
Parsley (2004) . 
 
We take pleasure in acknowledging Jason Parsley’s help throughout the preparation 
of this report, and especially in the development of electrodynamics on  S 3 . 
 
 7
 
4. Magnetic fields on  S3  and  H3 . 
 
In Euclidean 3-space  R3 ,  the classical convolution formula of Biot and Savart gives 
the magnetic field  BS(V)  generated by a compactly supported current flow  V : 
 
BS(V)(y)  =  1/(4π) ∫R3  V(x) × (y — x) / |y — x|3  dx . 
 
For simplicity, we write  dx  to mean  d(volx) . 
 
The function  ϕ(r)  =  —1/(4πr)  is the fundamental solution of the Laplacian in  R 3 , 
 
∆ϕ  =  δ . 
 
Because the gradient of  ϕ  at  y , 
 
∇y ϕ(x, y)  =  (1/(4π)) (y — x)/|y — x|3 , 
 
is the kernel function appearing in the Biot-Savart formula above, this formula can 
be written as 
 
BS(V)(y)  =  ∫R3  V(x) × ∇y ϕ(x, y)  dx . 
 
 8
 
 
In  R3 ,  the magnetic field  BS(V)  of a smooth, compactly supported current flow  V  
has four important properties: 
 
 (1)  It has finite energy, that is  ∫R3  BS(V)(y) ∙ BS(V)(y)  dy  <  ∞ . 
 
 (2)  It is divergence-free,  ∇ ∙ BS(V)  =  0 . 
 
 (3)  If  V  is a gradient field, then  BS(V)  =  0 . 
 
 (4)  If  V  is divergence-free, then  ∇ × BS(V)  =  V . 
 
Properties (1), (2) and (4) are well known, and the simple verification of (3) can 
be found in our paper (2001). 
 
It is easy to see that in  R3  there can’t be two different linear operators  BS  with 
the above properties, so in this familiar setting we have both existence and 
uniqueness. 
 
We take these properties as constraints on the definition of the Biot-Savart operator 
in  S3  and  H3 ,  giving us uniqueness there as well. 
 
The following theorem asserts existence, and provides explicit integral formulas. 
 
 
 9
 
 
THEOREM 2.  BIOT-SAVART INTEGRALS  in  S3  and  H3 . 
 
The Biot-Savart operator exists in  S3  and  H3 ,  and is given by the following 
formulas. 
 
(1)  On  S3  in left-translation format: 
 
  BS(V)(y)  =  ∫S3  Lyx—1 V(x) × ∇y ϕ0(x, y)  dx    
 
       —  1/(4π2) ∫S3  Lyx—1 V(x)  dx 
 
          +   2  ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ1(x, y)  dx , 
 
where    ϕ 0(α )  =  (—1/(4π2)) (π—α ) cot α    and     ϕ1(α )  =  (—1/(16π2)) α  (2π—α ) . 
 
(2)  On  S3  in parallel transport format: 
 
BS(V)(y)  =  ∫S3  Pyx V(x)  ×  ∇y ϕ(x, y)  dx , 
 
where     ϕ (α )  =  (—1/(4π2)) (π — α ) csc α  . 
 
(3)  On  H3  in parallel transport format: 
 
BS(V)(y)  =  ∫H3  Pyx V(x)  ×  ∇y ϕ(x, y)  dx , 
 
where     ϕ(α )  =  (—1/(4π)) csch α  . 
 
 
∙ In formula (1), the function   ϕ1(α)  =  (—1/(16π2)) α (2π—α)  satisfies the 
equation 
 
∆ϕ1  =  ϕ0  —  [ϕ0] , 
 
where  [ϕ0]  denotes the average value of  ϕ0  over  S3 .  The other kernel functions 
already appeared in the linking integrals in Theorem 1. 
 10
 
 
∙  A vector field  V  on  S3  is said to be left-invariant if 
 
Lyx—1 V(x)  =  V(y)         for all  x, y ∊ S3 . 
 
For example, using multiplication of unit quaternions, the vector fields 
 
V1(x)  =  x i  ,     V2(x)  =  x j  ,     V3(x)  =  x k 
 
form a pointwise orthonormal basis for the 3-dimensional subspace of left-invariant 
vector fields on  S3 . 
 
Left-invariant and right-invariant vector fields on  S3  are tangent to the orbits of 
Hopf fibrations of  S3  by parallel great circles. 
 
 
 
 
 11
 
 
 
It is not surprising that left-invariant fields play an important role in the left-transla- 
tion versions of our theorems.  In particular, if  V  is a left-invariant field on  S 3 ,  then 
V  is divergence-free and is a curl eigenfield with eigenvalue  —2 , 
 
∇ × V  =  —2 V . 
 
Moreover, the Biot-Savart operator is the inverse of curl on divergence-free fields  
on  S3 ,  
 
BS(V)  =  —‰ V . 
 
 
In formula (1) of Theorem 2,  
 
 ∙ the first integral is nonzero unless  V  is a left-invariant field;  
 
 ∙ the second integral is nonzero if and only if  V  has a nonzero component, 
  with respect to the L 2 inner product  <V, W>  =  ∫S3  V ∙ W  d(vol), 
  in the direction of the 3-dimensional subspace of left-invariant fields; 
 
 ∙ the third integral is zero if and only if  V  is divergence-free;  
 
 ∙ if  V  is a gradient field, then the first and third integrals are nonzero and  
  cancel each other, while the second integral is zero. 
 12
 
5. Proof scheme for Theorem 2, formula (1). 
 
Let  VF(S3)  denote the set of all smooth (C∞) vector fields on  S3 ,  regarded as an 
infinite-dimensional vector space with the L2 inner product   
 
<V, W>  =  ∫S3  V ∙ W  d(vol) . 
 
The vector Laplacian, 
 
∆V  =  — ∇ × ∇ × V  +  ∇(∇ ∙ V) , 
 
corresponds to the Laplacian on forms, 
 
∆βV  =  — *d*d βV  +  d*d* βV  , 
 
where the one-form  βV  is defined by  βV(W)  =  V ∙ W .   
 
The vector Laplacian  ∆: VF(S3)  →   VF(S3)  is an unbounded self-adjoint linear 
operator which is bijective, and which takes divergence-free fields to divergence- 
free fields, and gradient fields to gradient fields. 
 
The Green’s operator  Gr: VF(S3)  →   VF(S3)  is defined to be the inverse of the 
vector Laplacian.  It is a bounded self-adjoint linear operator which takes 
divergence-free fields to divergence-free fields and gradient fields to gradient 
fields. 
 
Let  V  be a smooth vector field on  S3 .  Thinking of  V  as a steady current flow,  
we define the corresponding magnetic field, and the Biot-Savart operator  BS ,  by 
 
BS(V)  =  — ∇ × Gr(V) . 
 
It is easy to check that the magnetic field  BS(V)  satisfies the four properties 
required of it in the preceding section. 
 
Once we get an explicit formula for the Green’s operator  Gr(V) ,  the negative of 
its curl will lead to the desired explicit formula for  BS(V) .  This in turn will lead 
us in section 9 to the linking integral formula given in Theorem 1, part (1). 
 
The fact that an explicit formula for the Green’s operator can lead (via a different 
route) to an explicit formula for the linking integral was known to de Rham (1960, 
section 33).  The issue is to find the formula for the Green’s operator, and we turn 
now to showing how to do this on  S3 . 
 13
 
Working in left-translation format, it is natural to hope, by analogy with  R 3 ,  that 
 
A(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
will be the Green’s operator on  S3  when we choose  ϕ  to be the fundamental 
solution of the Laplacian.  But it doesn’t work out this way. 
 
However,  ϕ  is not the only possible kernel function, and  A(V, ϕ)  is not the only 
way of convolving a vector field with a kernel to get another vector field. 
 
Consider the convolutions 
 
  A(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
  B ( V ,  ϕ)(y)  =  ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx   
 
  G(V, ϕ)(y)  =  ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx . 
 
In  R3 ,  if we let  ϕ  be the fundamental solution of the scalar Laplacian, then the 
convolution  A(V, ϕ)  gives the Green’s operator,  B(V, ϕ)  gives the magnetic 
field, and  G(V, ϕ)  gives the  ∂E/∂t  term in Maxwell’s equation. 
 
On  S3 ,  it turns out that a linear combination of all three types of vector convo-
lution, each with a different kernel function  ϕ ,  will give the Green’s operator. 
 
To prove this, we develop a "calculus of vector convolutions" in left-translation 
format, in which we compute formulas for curls, divergences and Laplacians of 
convolutions of types  A ,  B  and  G .  The key formulas are the following: 
 
  ∆A(V, ϕ)  =  A(V, ∆ϕ)       —  4 A(V, ϕ)     —  2 B(V, ϕ) 
 
  ∆B(V, ϕ)  =  B(V, ∆ϕ)        +  2 A(V, ∆ϕ)  —  2 G(V, ϕ) 
 
  ∆G(V, ϕ)  =  G(V, ∆ϕ) . 
 
The large spaces after the first terms on the right hand sides of the  A  and  B  lines 
serve as a reminder that in Euclidean space  R3 ,  only those first terms appear. 
In particular, in  R3  we have  ∆A(V, ϕ)  =  A(V, ∆ϕ) .  So naturally, when we 
choose  ϕ  to be a fundamental solution of the scalar Laplacian in  R3 ,  we get 
∆A(V, ϕ)  =  A(V, δ)  =  V ,  which tells us that  A(V, ϕ)  =  Gr(V)  there. 
 14
 
 
On the 3-sphere  S3 ,  we get the Green’s operator by adding one copy of line A 
to two copies of line B and four copies of line G, each with a different choice of 
kernel function  ϕ ,  as follows.   
 
 
THEOREM 3.  On  S3  in left-translation format, the Green’s operator on vector 
fields is given by 
 
     Gr(V)(y)  =   ∫S3  Lyx—1 V(x) ϕ0(x, y)  dx 
 
                          +  2 ∫S3  Lyx—1 V(x) × ∇y ϕ1(x, y)  dx   
 
                                    +  4 ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ2(x, y)  dx , 
 
where 
 
  ϕ 0(α )  =  (—1/(4π2)) (π—α ) cot α  
 
  ϕ 1(α )  =  (—1/(16π2)) α  (2π—α ) 
 
  ϕ 2(α )  =  (—1/(192π2)) (3α (2π—α ) + 2α (π—α )(2π—α )cot α ) , 
 
and these three kernel functions are related by 
 
                             ∆                       ∆                      ∆ ϕ2  →  ϕ 1  —  [ϕ 1]  →  ϕ 0  —  [ϕ0]  →   δ  —  [δ] . 
 
 
The negative curl of the above formula for the Green’s operator, 
 
BS(V)  =  — ∇ × Gr(V) , 
 
leads to formula (1) of Theorem 2 for the Biot-Savart operator on  S 3 . 
 
 15
 
6. Proof scheme for Theorem 2, formula (2). 
 
Now we are working on  S3  in parallel transport format, and use an entirely different 
approach. 
 
 
KEY LEMMA, spherical version. 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x (cos α  ϕ)}   
 
                                                                 =  (∆ϕ  —  ϕ) (V(x)  —  < V(x), y > y) .  
 
 
The above lemma is quite flexible:  V  can be a smooth vector field defined on all 
of  S3 ,  or just on a bounded subdomain  Ω   of  S3 ,  or just along a smooth closed 
curve  K  in  S3 ,  or even just at the single point  x .  The kernel function  ϕ(α)  is 
any smooth function, which typically blows up at  α = 0  and is asymptotic there to  
—1/(4πα ) .  As usual,  α  =  α(x, y)  is the distance on  S3  between  x  and  y .  The 
dot product  ∙  on the left hand side of the above equation is in the tangent space to  
S3  at  x ,  while the inner product  < , >  on the right hand side is in  R 4 . 
 
The proof of the lemma exploits the interplay between the geometry of  S 3  and 
the linear algebra of the space  R4  in which it lies.  Here are four samples: 
 
∙  We define a triple vector product  [A, B, C]  in  R4 ,  whose value is a vector 
orthogonal to the 3-space spanned by  A ,  B  and  C ,  and whose length is the  
3-dimensional volume of the parallelepiped spanned by these three vectors.   
 
∙  If  u  and  v  are both tangent to  S3  at  x ,  then   u × v  =  [x, u, v] . 
 
∙  If  x  and  y  are points of  S3  and  V(x)  is tangent to  S3  at  x ,  then 
 
∇y × [x, V(x), y]  =  2 < x, y > V(x)  —  2 < V(x), y > x . 
 
∙  Under these same hypotheses, 
 
[y, x, [y, x, V(x)]]  =  — sin2α V(x)  +  < V(x), y > y  —  cos α  < V(x), y > x . 
 
 
 16
 
Once the Key Lemma is proved, we apply it using the kernel function 
 
ϕ(α )  =  (—1/(4π2)) (π — α) csc α , 
 
which, as we noted earlier, is a fundamental solution of the shifted Laplacian on  S 3 , 
 
∆ϕ  —  ϕ  =  δ . 
 
With this choice of kernel function, we have 
 
(cos α) ϕ(α)  =  ϕ0(α)  =  (—1/(4π2)) (π — α ) cot α , 
 
which is the fundamental solution of the Laplacian on  S3 , 
 
∆ϕ0  =  δ  —  1/(2π2) .  
 
With these choices, the Key Lemma reads 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x ϕ0}   
 
                                                                 =  δ(x, y) (V(x)  —  < V(x), y > y) .  
 
Keeping these choices of kernel functions, we now define the Biot-Savart operator 
by formula (2) of Theorem 2, 
 
BS(V)(y)  =  ∫S3  PyxV(x) × ∇y ϕ(x, y) dx . 
 
Then we integrate the Key Lemma over  S3  and get 
 
   ∫S3  ∇y × {PyxV(x) × ∇yϕ} dx   —   ∫S3  ∇y {V(x) ∙ ∇x ϕ0}  dx 
 
                                                          =   ∫S3  δ(x, y) (V(x)  —  < V(x), y > y)  dx . 
 
The integral on the right hand side above equals   
 
V(y)  —  < V(y), y > y  =  V(y) , 
 
since  V(y) is a tangent vector to  S3  at  y ,  and hence orthogonal to  y  in  R4 . 
 17
 
 
Taking the curl and the gradient outside the two integrals on the left-hand side,  
we then get 
 
∇y × ∫S3  PyxV(x) × ∇yϕ(x, y)  dx   —   ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx   =   V(y) , 
 
or 
 
∇y × BS(V)(y)  =  V(y)  +  ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
Integrating by parts over  S3 ,  we have 
 
∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx  =  — ∫S3  ∇x ∙V(x)  ϕ0(x, y)  dx , 
 
and inserting this, we get 
 
∇y × BS(V)(y)  =  V(y)  — ∫S3  ∇x ∙V(x)  ϕ0(x, y)  dx . 
 
If we think of the vector field  V(x)  as a steady current, then the negative divergence,  
— ∇x ∙V(x) ,  is the time rate of accumulation of charge at  x ,  and hence the integral 
 
— ∫S3  ∇x ∙V(x)  ϕ0(x, y)  dx 
 
is the time rate of increase of the electric field at  y  (see section 8) .  Thus the above 
equation is Maxwell’s equation 
 
∇ × B  =  J  +  ∂E/∂t . 
 
With this line of reasoning in mind, we view the Key Lemma, with our specific 
choice of kernel functions, as a pointwise version of Maxwell’s equation. 
 
It is now easy to verify that  BS(V)  satisfies the four properties required of it in 
section 4. 
 
Remark.  Jason Parsley, in his thesis (2004), proves Maxwell’s equation in the 
case that the current flow  J  runs only within some bounded subdomain  Ω   ⊂   S3 . 
In that situation, the  ∂E/∂t  term also reflects the time rate of change of the 
electric field due to the gradual deposit or removal of charge along the boundary  
of  Ω  .  His proof of this in left-invariant format inspired our own arguments.  
 18
 
7. Proof scheme for Theorem 2, formula (3). 
 
We replace  R4   by Minkowski space  R1,3  with the indefinite inner product 
 
< x, y >  =  x0 y0  —  x1 y1  —  x2 y2  —  x3 y3 , 
 
and then regard hyperbolic 3-space as the hyperboloid 
 
H3  =  { x  ∊  R1,3 :  < x, x >  =  1  and  x0  >  0 }  ⊂   R1,3 . 
 
 
 
If  u  and  v  are tangent to  H3  at  x ,  we define the induced inner product  ∙   
on  TxH3  by 
u ∙ v  =  — < u, v > . 
 
This time we exploit the interplay between the geometry of  H3  and the linear 
algebra of  R1,3  to prove the following 
 
KEY LEMMA, hyperbolic version. 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x (cosh α  ϕ)}   
 
                                                                 =  (∆ϕ  +  ϕ) (V(x)  —  < V(x), y > y) .  
 
Comparing the Key Lemmas in  S3  and  H3 ,  we see that the only changes are that 
cos α  has been replaced by  cosh α  on the left-hand side, and  ∆ϕ  —  ϕ  has been 
replaced by  ∆ϕ  +  ϕ  on the right-hand side. 
 
 19
 
 
After proving the Key Lemma for  H3 ,  we apply it using the kernel function 
 
ϕ(α )  =  (—1/(4π)) csch α , 
 
which, as we noted earlier, is a fundamental solution of the shifted Laplacian on  H 3 , 
 
∆ϕ  +  ϕ  =  δ . 
 
With this choice of kernel function, we have 
 
(cosh α) ϕ(α )  =  ϕ0(α)  =  (—1/(4π)) coth α , 
 
which is the fundamental solution of the Laplacian on  H3 , 
 
∆ϕ0  =  δ .  
 
With these choices, the Key Lemma reads 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x ϕ0}   
 
                                                                 =  δ(x, y) (V(x)  —  < V(x), y > y) .  
 
When we define the Biot-Savart operator by formula (3) of Theorem 2, 
 
BS(V)(y)  =  ∫H3  PyxV(x) × ∇y ϕ(x, y) dx , 
 
and follow the line of reasoning from the previous section, we obtain Maxwell’s 
equation 
 
∇ × B  =  J  +  ∂E/∂t , 
 
and learn that  BS(V)  satisfies the four properties required of it in section 4. 
 
 
 20
 
 
8. Maxwell’s equations on  S3  and  H3 . 
 
Maxwell’s equations, so familiar to us in Euclidean 3-space  R3 ,  can also be shown 
to hold on  S3  and  H3 ,  with the appropriate definitions, as follows. 
 
Let  ρ  be a smooth real-valued function, which we think of as a charge density.  
On  R3  and  H3 ,  we ask that  ρ  have compact support, while on  S3  we ask that  
it have average value zero. 
 
In each case, we define the corresponding electric field  E  =  E( ρ)  by the formula 
 
E(ρ)(y)  =  ∇y ∫ ρ(x) ϕ(x, y) dx , 
 
where  ϕ  is the fundamental solution of the Laplacian. 
 
Let  J  be a smooth vector field, which we think of as a steady-state (i.e., time- 
independent) current distribution.  On  R3  and  H3 ,  we ask that  J  have compact 
support, while on  S3  we impose no restriction on  J . 
 
In each case, we define the corresponding magnetic field  B  =  BS(J)  by one of 
the formulas in Theorem 2.  Since  J  is steady-state, so is  B ,  and therefore 
∂B/∂t  =  0 . 
 
 
THEOREM 4.  MAXWELL’S EQUATIONS  in  S3  and  H3 . 
 
With these definitions, Maxwell’s equations,  
 
  ∇ ∙ E  =  ρ     ∇ × E  =  0 
 
  ∇ ∙ B   =   0      ∇ ×  B  =  J  +  ∂E/∂t , 
 
hold on  S3  and in  H3 ,  just as they do in  R3 . 
 
 21
 
 
The proofs of Maxwell’s equations are either self-evident or immediate 
consequences of information from previous sections, as follows. 
 
We have 
 
   ∇y ∙ E(ρ)(y)  =  ∇y ∙ ∇y ∫ ρ(x) ϕ(x, y) dx   
 
        =   ∆y ∫ ρ(x) ϕ(x, y) dx   
 
                                                       =  ρ(y) , 
 
because  ϕ  is the fundamental solution of the Laplacian. 
 
We have  ∇ × E  =  0  because  E  is a gradient field. 
 
We have  ∇ ∙ B  =  0  because that is one of the four properties required of  B . 
 
We have already noted in sections 6 and 7 how we get the last Maxwell equation,   
∇ × B  =  J  +  ∂E/∂t ,  from the Key Lemma. 
 
 
∙ The equation  dρ/dt  =  — ∇ ∙ J  expresses the fact that the divergence of the current 
flow  J  corresponds to the time rate of accumulation or dissipation of charge, which 
then leads to the  ∂E/∂t  term in Maxwell’s equation above, as we noted in section 6. 
 
∙ If the current flow  J  is divergence-free, then  ∂E/∂t  =  0 ,  and hence  ∇ × B  =  J .  
In that case, we get Ampere’s Law (just the curl theorem), which says that the 
circulation of  B  around a loop equals the flux of  J  through any surface bounded   
by that loop. 
 
 22
 
 
9. Proof scheme for Theorem 1. 
 
With steady-state electrodynamics in hand, we can follow what we imagine to be 
Gauss’s second line of reasoning and obtain the linking integral formulas on  S3   
and  H3  given in Theorem 1. 
 
To do this, run a unit current  V  =  dx/ds  along the first loop  K 1 ,  and use one of 
the three Biot-Savart formulas from Theorem 2 to calculate the resulting magnetic 
field  B .  For example, on  S3  in parallel transport format, we have 
 
B(y)  =  BS(dx/ds)(y)  =  ∫K1  Pyx dx/ds  ×  ∇y ϕ(x, y)  ds , 
 
where  ϕ(α)  =  (—1/(4π2)) (π — α) csc α ,  and where the integration takes place with 
respect to arc length along  K1  rather than with respect to volume in  S3 . 
 
We intend to calculate the circulation of this magnetic field  B  along the second 
loop  K2 ,  and then apply Ampere’s Law to get the formula for the linking integral. 
 
 
 23
 
We can view  V  as the limit of divergence-free current flows  V ε  supported in 
smaller and smaller tubular neighborhoods  Nε  of  K1 ,  each disjoint from  K2 ,  and 
each with unit flux through a cross-sectional disk.  Let  Bε  be the corresponding 
magnetic field, defined throughout  S3  or  H3 .  Since  Vε  is divergence-free, we 
have  ∇ × Bε  =  Vε ,  and so by Ampere’s Law, the circulation of  Bε  around the 
second loop  K2  equals the unit flux of  Vε  through the cross-sectional disks of  Nε ,  
multiplied by the linking number of  K1  and  K2 . 
 
Now the magnetic fields  Bε  converge uniformly to  B  on the complement of any 
fixed tubular neighborhood of  K1 ,  and in particular along the loop  K2 .  Hence 
the circulation of  B  along  K2  also equals the linking number of  K1  and  K2 . 
   
The three formulas for the magnetic field given in Theorem 2 then lead quickly to 
the three linking integrals in Theorem 1. 
 
For example, working on  S3  in parallel transport format, 
 
 Lk(K 1, K2)  =  circulation of  B  along  K2 
 
                              =  ∫K2  BS(dx/ds)(y)  ∙  dy/dt  dt 
 
                     =  ∫K2  (∫K1  Pyx dx/ds  ×  ∇y ϕ(x, y)  ds)  ∙  dy/dt  dt 
 
                              =  ∫K1×K2  Pyx dx/ds  ×  ∇y ϕ(x, y)  ∙  dy/dt  ds dt 
 
                              =  —∫K1×K2  Pyx dx/ds  ×  dy/dt  ∙  ∇y ϕ(x, y)  ds dt , 
 
where  ϕ(α)  =  (—1/(4π2)) (π — α) csc α , 
 
                              =  1/(4π2)∫K1×K2  Pyx dx/ds  ×  dy/dt  ∙  ∇y ϕ(x, y)  ds dt , 
 
where now  ϕ(α)  =  (π — α ) csc α ,  giving us formula (2) of Theorem 1. 
 
 
∙  Note that the third integral in the formula for  BS(V)  in left-translation format  
on  S3 ,  given in Theorem 2 part (1), is missing from the corresponding linking 
integral, given in Theorem 1 part (1), because the approximating current flows  V ε 
are all divergence-free. 
 
 24
10. Link, twist and writhe on  S3  and  H3 . 
 
We follow Calugareanu’s lead and replace the two closed curves  K1  and  K2  in our 
linking integrals by a single closed curve  K ,  which we must assume to be simple.   
Now the points  x(s)  and  y(t)  run along the same curve, and therefore can coincide, 
making three out of the four linking integrals appearing in Theorem 1 seem improper  
(the second integral on  S3  in left-translation format is clearly proper).  But as 
Calugareanu noted for the corresponding  R3 integral, the three threatening integrands 
actually vanish along the diagonal of  K × K ,  so the integrals converge.  The resul- 
ting value  Wr(K)  is a real number called the writhing number of  K .  It is, as we 
mentioned earlier, a measure of the extent to which  K  wraps and coils around itself. 
 
DEFINITION of the WRITHING INTEGRALS in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format: 
 
           WrL(K)  =defn  1/(4π2)∫K×K  Lyx—1 dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt 
 
                     —  1/(4π2)∫K×K  Lyx—1 dx/ds ∙ dy/dt  ds dt  , 
 
where     ϕ(α )  =  (π — α ) cot α  . 
 
(2)  On  S3  in parallel transport format: 
 
 Wr P(K)  =defn  1/(4π2)∫K×K  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x,y)  ds dt , 
 
where     ϕ(α )  =  (π — α ) csc α  . 
 
(3)  On  H3  in parallel transport format: 
 
 WrP(K)  =defn  1/(4π) ∫K×K  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x,y)  ds dt , 
 
where     ϕ(α )  =  csch α  . 
 
The two versions of the writhing number on  S3  are not the same, and one can show 
that 
WrL(K)  =  WrP(K)  +  L/(2π) , 
 
where  L  is the length of the closed curve  K .  The parallel transport version of 
writhe is the more intuitively satisfying, since in this version the writhing number 
of a great circle is zero. 
 25
 
 
We turn next to the definition of "twist". 
 
Let  K  be a smooth simple closed curve in  S3  or  H3 ,  parametrized by arc length  s ,  
with  0  ≤  s  ≤  L .   Let  x(s)  be a moving point along  K ,  and  T(s)  =  x’(s)  the unit 
tangent vector field. 
 
Let  V(s)  be a unit normal vector field along  K .  Our intention is to define the (total) 
twist of  V  along  K  by a formula such as 
 
Tw(V)  =  1/(2π) ∫K  T(s) × V(s) ∙ V’(s)  ds , 
 
as in Euclidean 3-space. 
 
 
But on  S3  there are two flavors of twist, according as  V’(s)  is calculated as a  
"left-invariant" derivative or a covariant derivative.  If we fall back into Euclidean  
mode and write 
 
V’(s)  =  limh→ 0 (V(s + h)  —  V(s)) / h , 
 
then the vectors  V(s + h)  and  V(s)  lie in different tangent spaces, and we must 
move them together in order to subtract.  If we use left-translation in the group  S 3   
to move  V(s + h)  back to the tangent space at  x(s)  which contains  V(s) ,  then the 
resulting limit is the left-invariant derivative  V’L(s) .  If we use parallel transport to 
move  V(s + h)  back, then the resulting limit is the covariant derivative V’P(s) . 
 
 26
 
 
The two flavors of twist on  S3  are then given by 
 
(1)                             TwL(V)  =  1/(2π) ∫K  T(s) × V(s) ∙ V’L(s)  ds  
 
and 
 
(2)                             TwP(V)  =  1/(2π) ∫K  T(s) × V(s) ∙ V’P(s)  ds . 
 
It is an easy exercise to prove that 
 
TwL(V)  =  TwP(V)  —  L/(2π) , 
 
where  L  is the length of the curve  K . 
 
 
 
Example.  Consider the great circle  K  =  {(cos s ,  sin s ,  0 ,  0):  0  ≤  s  ≤  2π} 
on  S3 ,  and along it the unit normal vector field  V(s)  =  (0 ,  0 ,  cos s ,  sin s) . 
Then we have  TwL(V)  =  0  and  TwP(V)  =  1 . 
 
 
 
In hyperbolic 3-space  H3 ,  we have only the parallel transport version of twist, 
 
(3)                             TwP(V)  =  1/(2π) ∫K  T(s) × V(s) ∙ V’P(s)  ds . 
 
 
 27
 
Now consider in  S3  or  H3  a narrow ribbon of width  ε  obtained by starting with 
a simple closed curve  K  =  {x(s)}  and then exponentiating a unit normal vector 
field  V(s)  along  K .  One edge of this ribbon is the original curve  K ,  and the 
other edge is the curve  Kε  =  {yε(s)} ,  given explicitly by 
 
  y ε(s)  =  cos ε  x(s)  +  sin ε  V(s)  in  S 3 ; 
 
  y ε(s)  =  cosh ε  x(s)  +  sinh ε  V(s)  in  H 3 . 
 
The vector field  V(s)  then points "across" the ribbon.                                    
 
 
THEOREM 5.  LINK  =  TWIST  +  WRITHE  in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format:        
 
                 Lk(K, K ε)  =  TwL(V)  +  WrL(K) . 
 
(2)  On  S3  in parallel transport format:    
 
                                  Lk(K, Kε)  =  TwP(V)  +  WrP(K) . 
 
(3)  On  H3  in parallel transport format:   
 
                                   Lk(K, Kε)  =  TwP(V)  +  WrP(K) . 
 
 28
 
11. Proof scheme for Theorem 5. 
 
In spirit, our proof of Theorem 5 for ribbons in  S3  and  H3  follows Calugareanu’s 
original proof in  R3 :  we begin with the linking integrals given in Theorem 1 for 
the edges  K  and  Kε  of our ribbon, let  ε  shrink to zero, and observe the behavior 
of the linking integrand. 
 
Of course, the value of the linking integral is independent of  ε  for  ε  >  0 ,  since 
the linking number is invariant under this kind of homotopy.  But the linking  
integrand develops a δ-function type singularity along the diagonal of  K × K ,   
which is handled as follows.   
 
Outside an appropriately chosen neighborhood of the diagonal, the linking integrand 
converges to the writhing integrand as  ε  →   0 ,  and its integral converges to the 
writhing number of the curve  K .  Inside this neighborhood of the diagonal, the 
linking integrand blows up, but its integral converges to the total twist of the normal 
vector field  V  along  K . 
 
The crucial thing, recognized by Calugareanu, is that the width of the neighborhood 
of the diagonal in  K × K  must go to zero much more slowly than the width  ε  of the 
ribbon.  In fact, we will choose the neighborhood of the diagonal to have width  εp , 
where  0  <  p  <  1/3 . 
 
To give a sense of this in action, we will outline here the proof of Theorem 5, 
part (2), dealing with  Link = Twist + Writhe  in parallel transport format on  S 3 .   
The proofs for  H3  and for left-translation format on  S3  are essentially the same.   
In particular, in left-translation format, the integrand of the second integral in the 
expression for the linking number converges uniformly to the corresponding  
integrand for the writhing number. 
 
Consider, in parallel transport format on  S3 ,  the linking integrand of  K  with  Kε , 
 
 F ε(s, t)  =  (1/(4π2)) dx/ds  ∙  Px(s)yε(t)(dyε/dt  ×  ∇yε(t) ϕ(α(x(s), yε(t)))) 
 
and the writhing integrand of  K , 
 
 F 0(s, t)  =  (1/(4π2)) dx/ds  ∙  Px(s)x(t)(dx/dt  ×  ∇x(t) ϕ(α(x(s), x(t)))) , 
 
where   ϕ(α)  =  (π  —  α) csc α . 
 29
Then the linking number of  K  and  Kε  is given by 
 
                                         Lk(K, Kε)  =  ∫∫0 ≤ s,t ≤ L  Fε(s, t)  ds dt , 
 
and the writhing number of  K  is given by 
 
                                              WrP(K)  =  ∫∫0 ≤ s,t ≤ L  F0(s, t)  ds dt . 
 
Since  α(x, y)  is the distance between  x  and  y ,  and since  ϕ  has a singularity 
just at  α  =  0 ,  the only difficulty in considering the convergence of the linking  
integral as  ε →  0  happens near the diagonal, where  s  =  t . 
 
To handle this, we first show that because the singularity of  ϕ’’(α)  at  α = 0  is like  
1/α3 ,  we have that for sufficiently small  ε > 0 , 
 
|Fε(s, t)  —  F0(s, t)|  ≤  C ε1—3p  , 
 
provided that  |s — t|  ≥  εp .   
 
If  0  <  p  <  1/3 ,  then  1 — 3p  >  0 ,  and hence  C ε1—3p  →   0  as  ε  →   0 . 
Therefore  Fε(s, t)  converges uniformly to  F0(s, t)  in the region  |s — t|  ≥  εp .   
Since the writhing integrand  F0(s, t)  remains bounded even along the diagonal,  
this shows that 
 
∫∫|s—t| ≥ εp  Fε(s, t)  ds dt   →    ∫∫0 ≤ s,t ≤ L  F0(s, t)  ds dt  =  WrP(K) , 
 
as  ε →   0 ,  that is, a portion of the linking integral converges to the entire writhing 
integral. 
 
The more delicate part of the argument is the integral near the diagonal.  A careful 
analysis using the Frenet equations reveals that for  0  <  p  <  1 , 
                                                      t+εp 
                         limε→ 0 ∫t—εp  Fε(s, t)  ds  =  (1/(2π)) x’(t) × V(t) ∙ V’P(t) . 
 
Hence 
 
∫∫|s—t| ≤ εp  Fε(s, t)  ds dt   →    ∫0 ≤ t ≤ L (1/(2π)) x’(t) × V(t) ∙ V’P(t)  dt  =  TwP(V) . 
 
That is, the remaining portion of the linking integral converges to the entire 
twisting integral.  In this way, we see that 
 
Lk(K, Kε)  =  TwP(V)  +  WrP(K) . 
 30
12. Helicity of vector fields on  S3  and  H3 . 
 
If  V  is a smooth vector field on  R3  with compact support,  then the Woltjer-
Moffatt formula for its helicity, 
 
H(V)  =  1/(4π) ∫ R3 × R3   V(x) × V(y) ∙ (x — y)/|x — y|3  dx dy , 
 
can be written succinctly as 
 
H(V)  =  ∫ R3  BS(V)(y) ∙ V(y)  dy . 
 
This is how Woltjer originally presented his invariant,  ∫A ∙ B d(vol) ,  with the 
role of  V  played by the magnetic field  B  and the role of  BS(V)  played by its 
vector potential  A .  The helicity of a vector field, as we mentioned earlier, is a 
measure of the extent to which its orbits wrap and coil around one another. 
 
We use the above formula to define the helicity of a vector field  V  on  S 3  or  H3 ,  
and then immediately obtain explicit integral formulas from Theorem 2.  
 
THEOREM 6.  HELICITY INTEGRALS  in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format: 
___ 
      H(V)  =  ∫S3×S3  Lyx—1 V(x) × V(y) ∙ ∇y ϕ0(x, y)  dx dy     
               
              — 1/(4π2) ∫S3×S3  Lyx—1V(x) ∙ V(y)  dx dy    
                                
                                          +  2 ∫S3×S3 ∇y (Lyx—1 V(x) ∙ ∇y ϕ1(x, y)) ∙ V(y)  dx dy , 
 
where     ϕ0(α )  =  (1/(4π2)) (π—α ) cot α      and     ϕ1(α )  =  (—1/(16π2)) α  (2π—α ) . 
 
(2)  On  S3  in parallel transport format: 
 
H(V)  =  ∫S3×S3  Pyx V(x)  ×  V(y)  ∙  ∇y ϕ(x, y)  dx dy , 
 
where     ϕ(α )  =  (1/(4π2)) (π — α ) csc α  . 
 
(3)  On  H3  in parallel transport format: 
 
H(V)  =  ∫H3×H3  Pyx V(x)  ×  V(y)  ∙  ∇y ϕ(x, y)  dx dy , 
 
where     ϕ(α )  =  (1/(4π)) csch α  . 
 31
 
∙ In formula (1), if  V  is divergence-free, then the third integral in the definition 
of  H(V)  vanishes. 
 
 
∙ In formulas (1) and (2), if the smooth vector field  V  on  S3  is divergence-free, 
then its helicity is the same as its asymptotic (or mean) Hopf invariant, as defined 
by Arnold (1974), and is invariant under the group of volume-preserving diffeo- 
morphisms of  S3 . 
 
 
∙ In formula (3), we assume that  V  has compact support, in order to guarantee 
convergence of the integral. 
 
 
∙ If  V  is a left-invariant unit vector field on  S3 , recall that  BS(V)  =  — ‰ V .   
Then its helicity is given by 
 
                     H(V)  =  ∫S3  BS(V)(y) ∙ V(y)  dy 
 
   =   ∫S3  — ‰ V(y) ∙ V(y)  dy   
 
                               =  — ‰ vol(S 3)  =  — ‰ (2 π2)  
 
                               =  — π2 .   
 
If  V  is a right-invariant unit vector field on  S3 ,  then  BS(V)  =  ‰ V ,  and hence 
 
                     H(V)  =  + π2 . 
 
 32
 
 
13. Upper bounds for helicity in  R3 ,  S3  and  H3 . 
 
Let  Ω   be a compact, smoothly bounded subdomain of  R3 ,  S3  or  H3 ,  and  V  a 
smooth vector field defined on  Ω  .  Thinking of  V as a current flow, its magnetic 
field  BS(V)  is defined by the same formulas as before, except that the integration is 
carried out only over  Ω  .   
 
If  Ω   ⊂   R3 ,  then 
 
BS(V)(y)  =  ∫Ω   V(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α)  =  —1/(4πα ) . 
 
If  Ω   ⊂   S3 ,  then, for example in parallel transport format, we have 
 
BS(V)(y)  =  ∫Ω   PyxV(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α)  =  (—1/(4π2)) (π — α) csc α .   
 
If  Ω   ⊂   H3 ,  then we have 
 
BS(V)(y)  =  ∫Ω   PyxV(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α)  =  (—1/(4π)) csch α . 
 
The magnetic field  BS(V)  is defined throughout the ambient space.  It is continuous 
everywhere, but its first derivatives suffer a discontinuity as one crosses the boundary 
of  Ω  .  This is a familiar situation from electrodynamics in Euclidean 3-space. 
 
In what follows, we will restrict  BS(V)  to  Ω  ,  and ignore its behavior outside this 
domain. 
 
Let  VF(Ω )  denote the space of all smooth vector fields on  Ω  ,  with the L2 inner 
product 
 
< V , W >  =  ∫Ω   V ∙ W  d(vol) , 
 
and associated energy  < V , V >  and norm  |V|  =  < V , V > 1/2  . 
 33
We seek a bound for the energy or norm of the output magnetic field  BS(V)  on  Ω   in 
terms of that of the input current flow  V .  Or to put it another way, we seek an 
upper bound for the L2 operator norm of the Biot-Savart operator,  
 
BS :  VF(Ω )  →   VF(Ω ) , 
 
in terms of the geometry of the underlying domain  Ω  . 
 
As a consequence, we will determine an upper bound for the helicity   
H(V)  =  < BS(V) , V >  of the vector field  V  in terms of its energy  < V , V >  
and the geometry of  Ω  . 
 
THEOREM 7.  Let  Ω   be a compact, smoothly bounded subdomain of  R3 ,  S3   
or  H3 ,  and let  R  =  R(Ω )   be the radius of a ball in that space having the same 
volume as  Ω  .  Let  V  be a smooth vector field defined on  Ω   .  Then 
 
|BS(V)|  ≤  N(R) |V| , 
 
where in  R3  we have  N(R)  =  R ; 
 
           in  S3  we have  N(R)  =  (1/π) (2(1 — cos R)  +  (π — R) sin R) ; 
 
           in  H3  we have  N(R)  =  sinh R . 
 
It follows immediately that the helicity  H(V)  =  < BS(V), V >  is bounded by 
 
|H(V)|  ≤  N(R) |V|2 . 
 
The proof in  R3  appears in our "upper bounds" paper (2000).  Using the formulas  
for  BS(V)  provided in Theorem 2 above,  the arguments in  S 3  and  H3  are then 
substantially the same as in that paper. 
 
Here are three observations. 
 
∙  In  R3 ,  the overestimate  N(R)  =  R  for the norm of  BS  grows like the  
cube root of the volume  (4/3)πR3  of  Ω  .    
 
∙  By contrast, in  H3 ,  the overestimate  N(R)  =  sinh R  for the norm of  BS  
grows like the square root of the volume  2π(sinh R  cosh R  —  R)  of  Ω . 
 
∙  In  S3 ,  the overestimate  N(π)  =  4/π  for the norm of  BS  on the entire 3-sphere 
can be compared with the known exact value,  |BS|  =  1/2 .  
 34
 
14.  Spectral geometry of the curl operator in  R3 ,  S3  and  H3 . 
 
Again let  Ω   be a compact, smoothly bounded subdomain of  R3 ,  S3  or  H3 . 
We are interested here in curl eigenfields on  Ω  ,  that is, vector fields  V  on  Ω   
which satisfy  ∇ × V  =  λ V ,  for  λ  ≠  0 .  In  R3  these eigenfields are used to  
model stable plasma flows; see our paper (1999). 
 
Curl eigenfields exist for every value of  λ .  For example, in  R3 ,  if 
 
V  =  sin λz  i   +   cos λz  j , 
 
then 
∇ × V  =  λ V . 
 
We want to constrain the choice of vector fields  V  by interior and boundary 
conditions which guarantee a discrete spectrum, while at the same time being 
reasonable for physical applications.  We then seek a lower bound for the  
absolute values of the nonzero eigenvalues. 
 
To begin, consider again the infinite-dimensional vector space  VF( Ω )  of 
smooth vector fields on  Ω  ,  with the L2 inner product. 
 
Let  K(Ω )  ⊂   VF(Ω )  denote the subspace consisting of vector fields which are 
divergence-free and tangent to the boundary of  Ω  , 
 
K(Ω )  =  {V ∊ VF(Ω ) :  ∇ ∙ V  =  0 ,  V ∙ n  =  0} , 
 
where  n  denotes the unit outward normal vector field along the boundary  ∂Ω  
of  Ω  .  We think of the vector fields in  K(Ω )  as  fluid knots  (hence the letter  "K") 
because, in the traditional passage from geometric knot theory to fluid dynamics, a 
knot is modeled by an incompressible fluid flow, defined in a tubular neighborhood  
of the knot and tangent to its boundary. 
 
To keep our problem manageable, we are only going to look for curl eigenfields 
within the subspace  K(Ω )  of  VF(Ω ) . 
 35
 
Let  CK(Ω )  ⊂   K(Ω )  denote the subspace of vector fields whose curl lies in  K(Ω ) . 
Thus 
 
curl :  CK(Ω )  →   K(Ω ) . 
 
For example, any divergence-free vector field on  Ω   which vanishes on  ∂Ω   lies 
in  K(Ω ) .  And clearly, any eigenfield of the curl operator in  K( Ω )  must actually 
lie in  CK(Ω ) . 
 
It is easy to see that a vector field  V ∊ K(Ω )  lies in the subspace  CK(Ω )  if and  
only if the circulation of  V  around small loops on  ∂Ω   vanishes. 
 
We want to know whether  curl :  CK(Ω )  →   K(Ω )  is self-adjoint with respect to 
the L2 inner product.  In other words, is it true that 
 
< ∇ × V , W >  =  < V , ∇ × W > ? 
 
 
Fact.  If  Ω   is simply connected, or equivalently, if all the components of  ∂Ω   are  
2-spheres, then  curl :  CK(Ω )  →   K(Ω )  is self-adjoint, but not otherwise. 
 
 
So we seek further sensible boundary conditions which will make  curl  self-adjoint, 
even when the domain  Ω   is not simply connected. 
 
To this end, let  Ω *  denote the closure of the complement of  Ω   in  R3 ,  S3  or  H3 . 
Let  g  denote the total genus of  ∂Ω  , that is, the sum of the genera of its components. 
Then, using real coefficients,  H1(∂Ω )  is a 2g-dimensional vector space, while 
H1(Ω )  and  H1(Ω *)  are each g-dimensional, and we have the direct sum 
 
H1(∂Ω )  =  ker(H1(∂Ω )  →   H1(Ω ))  ⊕   ker(H1(∂Ω )  →   H1(Ω *)) , 
 
where the above homomorphisms are induced by the inclusions  ∂Ω   ⊂   Ω   and 
∂Ω   ⊂   Ω * . 
 
Let  AK(Ω )  ⊂   CK(Ω )  ⊂   K(Ω )  consist of all vector fields  V  in  K(Ω )  whose 
circulation vanishes around any loop on  ∂Ω   which bounds in  Ω * .  We call 
AK(Ω )  the space of  Amperian knots  because, by Ampere’s Law, the magnetic 
field due to a current running entirely within  Ω   will have zero circulation around 
all loops on  ∂Ω   which bound in  Ω * . 
 36
 
Magnetic fields generated by current distributions in  Ω   are divergence-free, but  
not in general tangent to the boundary of  Ω  .  So we define the modified Biot-Savart 
operator 
 
BS’ :  K(Ω )  →   K(Ω ) 
by  
 
BS’(V)  =  L2 orthogonal projection of  BS(V)  into  K(Ω ) . 
 
Remark.  It is a simple consequence of the Hodge Decomposition Theorem that 
we have an L2 orthogonal direct sum 
 
VF(Ω )  =  K(Ω )  ⊕   G(Ω ) , 
 
where  G(Ω )  is the subspace of smooth gradient fields on  Ω  .  See, for example, 
our paper (2002).  So, for  V  in  K(Ω ) , 
 
BS(V)  =  BS’(V)  +  the gradient component of  BS(V) . 
 
Some basic facts. 
 
∙  When  Ω   is simply connected, we have  AK(Ω )  =  CK(Ω ) ,  but when  Ω   is 
not simply connected, then  AK(Ω )  is smaller than  CK(Ω ) . 
 
∙  AK(Ω )  is a dense subspace of  K(Ω )  in the L2 topology. 
 
∙  AK(Ω )  is the image of  BS’ ,  and the map  BS’ :  K(Ω )  →   AK(Ω )  is a 
bijection. 
 
∙  The maps   
 
BS’ :  K(Ω )  →   AK(Ω )         and         curl :  AK(Ω )  →   K(Ω ) 
 
are inverses of one another. 
 
 
 37
 
 
THEOREM 8.  Let  Ω   be a compact, smoothly bounded subdomain of  R3 ,  S3 
or  H3 ,  and let  R  =  R(Ω )  be the radius of a ball in that space having the same 
volume as  Ω  .   
 
Then  curl: AK(Ω )  →   K(Ω )  is a self-adjoint operator, and for each  V  ∊  AK(Ω )  
we have 
 
|∇ × V|  ≥  1/N(R)  |V| , 
 
where  N(R)  is defined as in Theorem 7. 
 
In particular, if  λ  is the curl eigenvalue on  AK(Ω )  with smallest absolute value, 
then 
 
|λ|  ≥  1/N(R) . 
 
 
The bounds given in Theorem 7 for the norm of  BS(V)  certainly hold also for its 
orthogonal projection  BS’(V)  into the subspace  K(Ω ) .   
 
Since  curl :  AK(Ω )  →   K(Ω )  is the inverse of  BS’ :  K(Ω )  →   AK(Ω ) ,  we 
simply invert these bounds to get Theorem 8. 
 
 
 
 
 
 
 
 
 
 
 
 
 38
