---
doc_id: 1-s20-0040938385900047-main
doc_title: "ToporoPy Vol. 24, No. 3, pp. 307-332. 1985. 0040-9383185 s3.00+ .OO Printed III Great Britain. C 1985. Pcrgamon Press Ltd. VOLUMES OF HYPERBOLIC THREE-MANIFOLDS"
section_id: sec-003-4-good-parameters-for-deformation
section_title: "Good parameters for deformation"
section_number: 4
pages: 14-18
source_pdf: 1-s2.0-0040938385900047-main.pdf
source_sha256: f0db9d97f2ae83c6
doc_brief: "ToporoPy Vol. 24, No. 3, pp. 307-332. 1985. 0040-9383185 s3.00+ .OO Printed III Great Britain. C 1985. Pcrgamon Press Ltd. VOLUMES OF HYPERBOLIC THREE-MANIFOLDS — 7 sections: Introduction; Combinatori"
---
We have described how the hyperbolic structure on M can be varied in dependence on the 
parameter 2 = (z,, . . , z, ). This parameter is somewhat arbitrary in that it depended on a 
choice of ideal triangulation; moreover, it contains redundant information: z is constrained 
by the “consistency relations” (equations (17) of $2) of which precisely n - h are independent 
(Proposition 2.3). In this section we shall describe a more natural and intrinsic parametriz- 
ation of the deformations, due to Thurston [7, $5.81, and discuss the relation between the 
parameters used and the geometry of the cusps. 
The parametrization to be described is an easy consequence of the fact, which we proved 
in section 2, that the deformation space has dimension precisely h. Thurston’s hyperbolic 
Dehn surgery theorem also follows easily. Thus our analysis gives a proof of these facts using 
only Mostow rigidity plus as much of the combinatorics of ideal triangulations as is 
expressed by Proposition 2.2. This seems worth noting. 
In $2 we introduced the number 
“0, Z$” (1 - c,,)m;; (27) 
associated to the chosen “meridian” mi in the torus q corresponding to the i-th unsurgered 
end of N. Up to a constant + 1 this number is the derivative of the holonomy of “i in the 
affine structure on T,. This constant & 1 is !he va!ue of formula (27) at z = z” = ($, . . . , zt). 
VOLUMES OF HYPERBOLIC THREE-MANIFOLDS 321 
Thus 
is the exact derivative of the holonomy. We denote its logarithm by ui so 
II 
I( 1-Z ui = 
v=1 
mki log -$ + mLi log * 
Y 1-z; > 
is an analytic function of z which vanishes at z”. Similarly 
vi = i 
V=l ( l-z lki log $+ l':i log& 
Y Y > 
(28) 
(29) 
is the logarithm of the holonomy for the “longitude” ei c Ti. 
The promised parameters are ul, . . . , u,,. Denote by go the variety of z E C’ which satisfy 
the consistency relations. Then u = (u,, . . . , u,,) maps a neighborhood of z” •9~ biholo- 
morphically onto a neighborhood 9 of 0 c C”. The bijectivity is not obvious at first sight; it 
would be plausible for u to be a branched covering, with the several inverse images of a given 
point corresponding to several ideal triangulations of the same Dehn surgered version of M. 
We shall prove the bijectivity of u later. 
The parameter u is still not completely natural, in that it depends on the choice of a 
primitive element ++zi in the homology of each cusp. We could, for instance, equally well have 
chosen v = (v,, . . . , u,,) as the parameter. We will, however, stick to our choice and thus 
consider the ui as dependent variables. We next discuss this dependence and draw some 
elementary consequences. 
LEMMA 4.1. In a neighborhood of the origin 
vi = u~.T~(u~, . . . , u,), i = 1,. . . , h for analytic functions 7i (u) which satisfy: 
(a) Ti(“,..-, 0) is in the upper halfplane and is the modulus of the euclidean structure on 
the torus Ti associated to the i-th CUSP of M (with respect to mi, ei). 
(b) Ti(ulr. . . 3 u,,) is an even function of each of its arguments. 
Part (a) is implicit in Thurston [7, $5.83, but we sketch the argument since we need the 
geometry. Consider ai and Li as elements of n, (M) after suitable choice of basepoint and let 
H ( mi) and H (ti) be their respective holonomies. 
We use the upper half space model 
W3={(z,r)ECxR(r>O} 
az + b 
so an element of Isom+ (w3) corresponds to a Mobius transformation z ~3 of 
(C x (0)) u {a~) with a b 
( 1 c d 
E SL (2, C). The elements H( mi) and H (Fi) are commuting 
parabolic elements, so by a conjugation we may assume they are the following translations in 
the C-plane: 
H(mi):Z~Z+l, H(Li):z~z+T. (30) 
Then 5 is the modulus of the euclidean structure on ri and with our orientation conventions 
T E w (upper half-plane). 
We now deform the hyperbolic structure slightly to a parameter value u = (u,, . . . , u,,) 
and denote the deformed holonomy by Hu. Since H,( mi) and H, (Ci) commute, they have the 
same fixed points on the sphere 6: u {ccl at infinity. If they are parabolic then the cusp of M 
has remained a cusp and ui = vi = 0. Otherwise, H,(mi) and H,((i) have two fixed points, 
which we can put at (0,O) and (0, 0~) so 
H,(rmi):z-uz, HU(li):z-bz (31) 
322 Walter D. Neumann and Don Zagier 
for some a, b E C*. By definition, ui = log a and ui = log b. Moreover, since u is small, a 
fundamental domain for (30) must be almost similar to a fundamental domain for (31) (see 
Fig. 13). Thus, noting that a and b are close to 1, we have 
ui=logbxb-lxr(a-l)zrloga=rui, 
where x means first order equality. In particular, for u near 0 it follows that vi vanishes if and 
only if ui does, so vi/ Ui is analytic and, moreover, the value of ui/ ui at u = 0 is r. Thus part (a) 
of the Lemma is proven. Before proving part (b) we need to recall some geometry. 
By Lemma 4.1 (a), if u is small and ui # 0 then ui is not a real multiple of ui. Hence there is a 
unique solution (pi, qi) E R2 U {Co} t0 
piui + qivi = 2Ki (32) 
(we take (pi, qi) = 00 if ui = 0). This (pi, qi) is called the generalized Dehn surgery coejicient 
by Thurston. It’s geometric significance is as follows. Let M, be the completion of A4 with the 
hyperbolic metric given by parameter value u. Thus M, differs topologically from M by the 
addition of a set yi of limit points at the i-th CUSP for each i. If (pi, qi) = CO then yi = 0 and M, 
still has a cusp here. If (pi, qi) is a coprime pair of integers then yi is a circle and at the i-th cusp 
M, is the result of hyperbolic (pi, qi)-Dehn surgery on M. In all other cases M, is either 
metrically singular or not even a manifold (vi a circle or a point respectively) depending on 
whether or not pi and qi are rationally dependent. 
Denote by K the map which assigns to a parameter value u near 0 the corresponding 
generalized Dehn surgery invariant ( (pl, ql), . . . , (p,,, q,,))E (R2 u {a})‘. Then K maps a 
neighborhood of 0 E CL homeomorphically to a neighborhood of CC E ( R2 u (30 > )h (to see 
this observe that if 
v((Pt9q1)9.. . , (Ph9qh))=2ni p,+iT,t,,)9.. . , 
1 
I i t Ph + qh5h to) > 
then cp 0 K has Jacobian equal to the identity at 0). This is Thurston’s hyperbolic Dehn surgery 
theorem and is how he proved it. 
Now suppose (pi, qi) is a coprime integer pair, so at the i-th cusp M, has resulted by true 
hyperbolic Dehn surgery from M. We want to compute the length and torsion of the new 
geodesic yi added at this cusp. 
LEMMA 4.2. Choose integers ri, si such that det r: ,“i = 1. Then 
( ) I 1 
length (ri) + i. torsion (vi) = - (riui + siui) (mod 2xi). 
Proof. On Ti the classes pi*ni + qili and rimi + Sigh form a basis for homology. Since 
pi~i + qiei is the class killed by Dehn surgery, rimi + siti represents the new geodesic yi in 
M,. Thus the .holonomy of yi (which is well defined up to conjugation) is given by 
H(y,) = H(rimifsili) = (zwaribsiz) 
in the notation of equation (31), and therefore 
length (yi) + i. torsion (yi) = 
= 
f log (ar,bsi) 
* (ri ui + SiVi), 
Oi x ax 
Fundamental domam for (30) Fundamental domain for (31) 
Fig. 13. 
VOLUMES OF HYPERBOLIC THREE-MANIFOLDS 323 
where the sign must be chosen to give a positive real part. To verify this sign we rewrite the 
equations 
with E = + 1 as 
piui + qiui = flri 
riui + siUi= E (length (yi) + i. torsion (yi)) (33) 
Pi 4i 
( >( 
Re(ui) Im(ui) 0 2rr 
ri si Re (vi) Im (ui) > ( = selength (yi) s.torsion (yi) > 
Then taking determinants gives 
Im (uiUi) = 27rs*length (yi) (34) 
But ui = ri (u)ui with ri (u) in the upper half plane (Lemma 4.la), so Im (uiUi) is negative. Hence 
&= -1. 
We can now finally prove part (b) of Lemma 4.1. Choose u near the origin in Ch such that 
M, is obtained by true hyperbolic Dehn surgery at every cusp, i.e. each pair (pi, qi) is either a 
coprimeintegerpairor co.Assume (pl,ql) # co andreplace (pl,ql) by (-pi, -q,)leaving 
the other (pi, qiyS unchanged. Let u’ be the corresponding parameter value. Then M,and M,. 
are the same topologically, so by Mostow rigidity they are isometric. In particular the right 
hand sides of equations (33)are unchanged. We can thus solve (33) for the new ui and ui to see 
that u1 and u1 have been replaced by - t(i and - ur while the remaining ui and Ui are 
unchanged. Thus for each i the ratio ui/ui = ?i(u) is an even function of ui and similarly of 
uz, . * . 9 u,, at least at parameter values u corresponding to true hyperbolic Dehn surgery. 
But any analytic set containing these parameter values has a dense set of tangent directions at 
the origin and thus includes a neighborhood of 0 E Ch. Thus 7i(u) is an even function of its 
arguments on all of 9. 
Replacing one coordinate of u by its negative gives isometric M, and M,, (this is so also 
for parameter values which do not correspond to hyperbolic Dehn surgeries by the 
continuation argument just used; think in terms of the holonomy homomorphism R, (M) 
+PSL(2, C)). This involution will not, in general, have a simple expression in terms of 
2 = (21, . . . , z,). In fact, from Thurston’s description of hyperbolic Dehn surgery it is clear 
that what is happening geometrically is that we have two ideal triangulations of M, 
distinguished by the direction in which edges of the triangulation spiral in towards the 
geodesic yi, and these may well have very different z values. Note that outside a tubular 
neighborhood of the yi the combinatorics of the triangulation of M, are the same as for M, 
while inside a tubular neighborhood of yi the only choice is the direction of spiral, which 
corresponds to a choice of sign for ui. Thus the parameter u determines both M,and its ideal 
triangulation, so the change of parameters from z to u is bijective, as mentioned earlier. Again, 
we use the above continuation argument to deduce this for general z and u from the 
hyperbolic Dehn surgery case. 
To end this section we give two more formulae for the length Li of the geodesic yi created 
by Dehn surgery. Though elementary, they are important ingredients of the volume 
computation. The second one is equation (2) of the introduction which proves the 
equivalence of Theorems 1A and 1B. 
PROPOSITION 4.3. 
Li = - & Im (uiVi) 
Li = 
Qi(Eqi)+ $1 O($&) (36) 
where Qi is as described in the introduction. In particular length (yi) is the restriction of the 
analytic function L,(u) = - L Im(Ui&) dt$ined in a whole neighborhood of0~ Ch (rather than 
2n 
just at the Dehn surgery points). 
324 Walter D. Neumann and Don Zagier 
Proof. (35) is just a restatement of (34). To see (36) note first that 
ui = ri (0). Ui + (higher order). 
By equation (32) (with apologies for the double use of i) 
2ni ui = 
Pi + ri(“)4i 
+ (higher order). 
Hence 
-& Im (UiVi) = 21L Im ri(O) 
IPi + Ti(O)qil’ 
+ (higher order) 
= 2rr Vol( TJ 
length (pimi + q/i ) 
+ (higher order). 
The higher order terms must start at fourth order, since they are even in each (pi, qi).
