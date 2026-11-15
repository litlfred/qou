---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-005-4-left-invariant-vector-fields-on-s3
section_title: "Left-invariant vector fields on S3 ."
section_number: 4
pages: 12-15
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Left-invariant vector fields on  S3  play an important role in understanding formula (1) 
for the Biot-Savart operator.  A vector field  V  on  S3  is said to be left-invariant if 
 
Lyx—1 V(x)  =  V(y)         for all  x, y ∊ S3 . 
 
For example, using multiplication of unit quaternions, the vector fields 
 
V1(x)  =  x i  ,     V2(x)  =  x j  ,     V3(x)  =  x k 
 
form a pointwise orthonormal basis for the 3-dimensional subspace of left-invariant 
vector fields on  S3 . 
 
Left-invariant and right-invariant vector fields on  S3  are tangent to the orbits of 
Hopf fibrations of  S3  by parallel great circles.  Since a steady flow along these 
parallel great circles is distance-preserving, the left- and right-invariant vector 
fields are certainly divergence-free. 
 
 
PROPOSITION 1.  Left- and right-invariant vector fields on  S3  are curl eigenfields 
with eigenvalues  —2  and  +2 ,  respectively. 
 
Proof.  We will show that  ∇ × V  =  —2 V  for left-invariant fields  V . 
 
Recall the primitive meaning of "curl".  To find the component of  ∇ × V  at the 
point  x  in a given direction on an oriented Riemannian 3-manifold, you pick a  
small disk orthogonal at  x  to that direction, compute the circulation of  V  around 
the boundary of this disk, divide by the area of the disk, and then take the limit as  
the disk shrinks to the point  x .  To keep signs straight, the orientation of the disk, 
combined with the orientation of the normal direction, should give the chosen 
orientation on the ambient space.  In this view, the primitive meaning of "curl"  
is given by the "curl theorem", i.e., Stokes' theorem.   
 
To apply this to left-invariant vector fields on  S3 ,  first note that any two of these 
are equivalent to one another by an orientation-preserving rigid motion of  S3 ,  so it 
is enough to prove the result for one such field.   
 
 
 
 
 
For example, if 
 
x  =  x0  +  x1 i  +  x2 j  +  x3 k , 
we will use 
                              V(x)  =  x i  =  (x0  +  x1 i  +  x2 j  +  x3 k) i   
 
                                                  =  —x1  +  x0 i  +  x3 j  —  x2 k . 
 
Furthermore,  V  itself is invariant under a transitive group of orientation-preserving 
rigid motions of  S3 ,  so it is enough to show that  ∇ × V  =  —2 V  at a single point. 
Choose the point  x  =  1 ,  where  V(x)  =  i .  Orient  S3  as usual, so that  i , j , k   
is an ordered basis for the tangent space at the point  x  =  1 .  Now we find the 
component of  ∇ × V  at the point  x  =  1  in the i-direction, as follows. 
 
To get a small disk through  x  orthogonal to this direction, use the spherical cap 
of geodesic radius  α  on the great 2-sphere in the 1jk-subspace.  The typical point 
along the boundary of this disk is 
 
                    y  =  cos α  +  (sin α cos ϕ) j  +  (sin α sin ϕ) k . 
 
Note that 
 
            dy/dϕ  =  (— sin α sin ϕ) j  +  (sin α cos ϕ) k , 
 
and 
              V(y)  =  y i  =  (cos α) i  +  (sin α sin ϕ) j  —  (sin α cos ϕ) k . 
 
The circulation of  V  around the boundary of this disk is given by 
 
∫0
2π  V(y) ∙ dy/dϕ  dϕ  =  ∫0
2π  — sin2α  dϕ  =  — 2π sin2α . 
 
The area of this disk is given by 
 
∫0
α  2π sin α  dα  =  2π (1  —  cos α) . 
 
Dividing circulation by area, we get 
 
— sin2α / (1 — cos α)  =  — (1 — cos2α) / (1 — cos α)  =  — (1 + cos α) . 
 
As we let  α  →  0 ,  this approaches  — 2 .  Hence at the point  x  =  1 ,  the 
component of  ∇ × V  in the  i-direction is  — 2.  So far, so good, since  V(x)  =  i . 
 
 
 
 
 
A similar computation shows that the components of  ∇ × V  in the  j- and k-
directions are zero.  Thus, at the point  x  =  1 ,  we have  ∇ × V  =  — 2 i  =  — 2 V .  
As mentioned earlier, this implies that  ∇ × V  =  — 2 V  at every point of  S3 ,  
completing our proof. 
 
Likewise, if  V  is right-invariant, then  ∇ × V  =  +2 V . 
 
We noted in section 3 that if  V  is divergence-free, then  ∇ × BS(V)  =  V . 
If  V  is left-invariant, then we also have  ∇ × (—½V)  =  V .  Therefore  BS(V)  
and  —½V  are divergence-free fields with the same curl.  Their difference is a  
field which is simultaneously divergence-free and curl-free, and hence, since  S3   
is simply connected, must be zero.  Thus  BS(V)  =  —½V .   
 
Likewise, if  V  is right-invariant, then  BS(V)  =  +½V .  
 
Let  VF(S3)  denote the set of all smooth vector fields on  S3 ,  regarded as an 
infinite-dimensional vector space with the L2 inner product   
 
<V, W>  =  ∫S3  V ∙ W  d(vol) . 
 
The following comments, which we do not prove here, help to explain the different 
roles played by the three integrals in formula (1) of Theorem 2 above. 
 
(a)  The first integral is zero if and only if  V  is a left-invariant field. 
 
(b)  The second integral is zero if and only if  V  is orthogonal, in the above 
       inner product, to the 3-dimensional subspace of left-invariant fields. 
 
(c)  The third integral is zero if and only if  V  is divergence-free. 
 
(d)  If  V  is a nonzero gradient field, then the first and third integrals are  
       nonzero and cancel each other, while the second integral is zero.
