---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-059-54-proof-scheme-for-theorem-1
section_title: "Proof scheme for Theorem 1."
section_number: 54
pages: 101-104
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Recall from section 2 what we imagine to be Gauss's second line of reasoning for 
obtaining his linking integral.  Run a current through the first loop, and calculate  
the circulation of the resulting magnetic field around the second loop.  By Ampere's 
Law, this circulation is equal to the total current enclosed by the second loop, 
which means the current flowing along the first loop multiplied by the linking 
number of the two loops.  Then the Biot-Savart formula for the magnetic field 
leads directly to Gauss's linking integral. 
 
                                  Linking numbers via Ampere's Law 
 
The same line of reasoning in  S3  and  H3  will lead us in the next two sections 
from the three formulas for the magnetic field given in Theorem 2 to the three 
linking integrals given in Theorem 1. 
 
But there is an issue which must be dealt with first.  We have proved Theorem 2 
only when  V  is a smooth, compactly supported current distribution on  R3 ,  S3   
or  H3 .  As things stand, when currents run through wires, we have not proved  
the corresponding formula for the resulting magnetic field, nor the accompanying 
Ampere's Law. 
 
We will get around this by observing that a field defined for a current running in a 
wire loop is the limit, in an appropriate sense, of magnetic fields caused by currents 
running in thin tubular neighborhoods of the loop.  Then the Ampere's Law that  
we want will simply be the limit of Ampere's Laws that we already know, as the 
thickness of the neighborhoods goes to zero. 
 
 
 
 
 
 
The argument is elementary, so we just outline it and leave the details to the reader. 
 
Let  K  be a simple closed curve in an oriented Riemannian 3-manifold  M ,  which 
in the present case is either  R3 ,  S3  or  H3 .  Let  r0  >  0  be a small real number,  
and let  Nr0  be the  r0-neighborhood of  K  in  M ,  that is, the set of all points in  M  
whose distance from  K  is less than  r0 .  We choose  r0  small enough so that  Nr0   
is a traditional embedded tubular neighborhood of  K . 
 
Let  K  =  {X(s) ,  0  ≤  s  ≤  L}  be a parametrization of  K  by arc length, and let   
T(s)  =  dX/ds  =  X'(s)  be the resulting unit tangent vector field along  K  .  Extend 
this vector field to an orthonormal frame field  T(s) ,  N(s) ,  B(s)  along  K .  This is 
possible because the normal bundle of a smooth curve in an oriented manifold is 
always trivial.  The notation is chosen to remind us of the Frenet frame, consisting 
of the tangent, principal normal and binormal vectors along a smooth curve of 
nowhere vanishing curvature in Euclidean 3-space  R3 . 
 
Given this orthonormal frame field along  K ,  we can use the exponential map of  
the Riemannian manifold  M  to parametrize the tubular neighborhood  Nr0  by the 
product of  K  and a Euclidean disk of radius  r0  as follows: 
 
(s, u, v)  →  X(s, u, v)  =  expX(s) (u N(s)  +  v B(s)) , 
 
where  0  ≤  s  ≤  L  and  0  ≤  u2  +  v2  <  r0
2 .  In  R3 ,  this would simplify to 
 
X(s, u, v)  =  X(s)  +  u N(s)  +  v B(s) . 
 
Now let  V(s, u, v)  =  ∂X(s, u, v)/∂s  be the tangent vector field to the s-coordinate 
curves, each of which is a simple closed curve having constant  u  and  v  coordinates. 
Since the exponential map takes rays in the normal plane to  K  at  X(s)  to geodesics 
orthogonal to  K , each of the s-coordinate curves remains at the constant geodesic 
distance  (u2  +  v2)1/2  from  K .  
 
LEMMA.  The vector field  V(s, u, v)  =  ∂X(s, u, v)/∂s  can be rescaled to make 
it divergence-free. 
 
The proof is elementary and we leave it to the reader. 
 
 
 
 
 
 
 
It is easy to further rescale and concentrate the flow  V  in  Nr0  to a flow  fε V  that  
is supported in thinner and thinner tubular neighborhoods  Nε  of  K ,  yet always  
has unit flux through the cross-sectional disks. 
 
As  ε → 0 ,  we regard the fields  fε V  supported inside the neighborhoods  Nε 
of  K  as closer and closer approximations to the unit tangent field  X'(s)  =  T(s) 
along  K . 
 
We now change notation slightly for convenience. 
 
Let  K  =  {x(s)}  be a smooth simple closed curve in  R3 ,  S3  or  H3 ,  and let   
V  =  dx/ds  be the unit tangent vector field along  K .  Let  BS(V)  denote the 
field defined in the complement of  K  by using any of the Biot-Savart formulas 
in  R3 ,  S3  or  H3  and by carrying out the required integrations with respect to  
arc length along  K ,  rather than with respect to volume in the ambient space. 
 
Let  Vε  denote a divergence-free field supported inside the tubular neighborhood 
Nε  of  K  and having unit flux through the cross-sectional disks, as constructed 
above.  In particular, all the vector fields  Vε
  are rescalings of a single vector field.  
Let  BS(Vε)  denote the corresponding magnetic field defined throughout the ambient 
space by using the same Biot-Savart formula as for  V . 
 
LEMMA.  As  ε  →  0 ,  the magnetic fields  BS(Vε)  converge uniformly to the  
field  BS(V)  on any compact subset of the complement of  K . 
 
Again, the proof of this is straightforward, and we leave the details to the reader. 
 
 
As a consequence, Ampere's law for the field  BS(V)  is the limit of Ampere's Laws 
for the fields  BS(Vε)  as  ε → 0 .  In particular, it can and will be applied to a loop 
in the complement of  K  which bounds a surface cutting through  K .
