---
doc_id: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin
doc_title: "© 2008, Sociedade Brasileira de Matem´ atica TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INV ARIANTS"
section_id: sec-008-completing-the-proof-of-theorem-b
section_title: "Completing the proof of Theorem B"
section_number: null
pages: 26-33
source_pdf: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-linking-numbers.pdf
source_sha256: db149864ce367da2
doc_brief: "Matemática Contemporânea, Vol. 34, 251–283 © 2008, Sociedade Brasileira de Matemática TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INVARIANTS — Three-component links in the 3-dimensional sphere were"
---
Now we have an explicit formula for the fundamental solution φ of the
scalar Laplacian on the 3-torus T 3, and just as in R3, both the scalar and
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 277
vector Green’s operators act by convolution with φ. In particular, if V is
a smooth vector field on T 3, then Gr(V ) =V∗φ, that is,
Gr(V )(τ) =
Z
T 3
V (σ)φ(τ−σ) dσ.
To obtain the formula for the magnetic field BS(V ), we take the negative
curl of the above formula and get
BS(V )(τ) = −∇τ× Gr(V )(τ) = −
Z
T 3
∇τ× (V (σ)φ(τ−σ))dσ
=
Z
T 3
V (σ)×∇τφ(τ−σ) dσ.
Then the helicity of V is given by
Hel(V ) =
Z
T 3
V (τ)  BS(V )(τ) dτ
=
Z
T 3×T 3
V (σ)×V (τ)  ∇σφ(σ−τ) dσdτ.
Applying this to the vector field VL associated with our 3-component
link L, we get the desired formula for the Pontryagin invariant ν of gL:
ν(gL) = Hopf( gL) = Hel(VL) =
Z
T 3
BS(VL)  VL d(vol)
=
Z
T 3×T 3
VL(σ)×VL(τ)  ∇σφ(σ−τ) dσdτ.
Hence by Theorem A, Milnor’s µ-invariant of the 3-component link L
is given by
µ(L) = 1
2ν(gL) = 1
2
Z
T 3×T 3
VL(σ)×VL(τ)  ∇σφ(σ−τ) dσdτ,
completing the proof of Theorem B.
Acknowledgements. We are grateful to Fred Cohen and Jim Stasheff for
their substantial input and help during the preparation of this paper, and
to Toshitake Kohno, whose 2002 paper provided the original inspiration
278 DETURC, GLUCK, KOMENDARCZYK, MEL VIN et al
for this work. Komendarczyk and Shonkwiler also acknowledge support
from DARPA grant #FA9550-08-1-0386.
The Borromean rings shown on the first page of this paper are from
a panel in the carved walnut doors of the Church of San Sigismondo in
Cremona, Italy. The photograph is courtesy of Peter Cromwell.
References
[1820] Biot, J.-B.; Savart, F., Note sur le magnetisme de la pile deVolta ,
Annales de Chimie et de Physique, 2nd ser. 15, (1820), 222–223.
[1824] Biot, J.-B., Precise Elementaire de Physique Experimentale, 3rd ed.,
vol. II, Chez Deterville, Paris.
[1833] Gauss, C. F., Integral formula for linking number , Zur Mathematis-
chen Theorie der Electrodynamische Wirkungen (Collected Works, Vol.
5), Koniglichen Gesellschaft des Wissenschaften, G¨ ottingen, 2nd ed.,
p. 605.
[1938] Pontryagin, L. S., A classification of continuous transformations of a
complex into a sphere , Dokl. Akad. Nauk SSSR 19, 361–363.
[1941] Pontryagin, L. S., A classification of mappings of the three-dimensional
complex into the two-dimensional sphere, Rec. Math. [Mat. Sbornik] N.
S. 9, no. 51, 331–363.
[1947] Steenrod, N. E., Products of cocycles and extensions of mappings, Ann.
of Math. (2) 48, 290–320.
[1947] Whitehead, J. H. C., An expression of Hopf’s invariant as an integral ,
Proc. Natl. Acad. Sci. USA 33, no. 5, 117–123.
[1948] Fox, R. H., Homotopy groups and torus homotopy groups , Ann. of
Math. (2) 49, no. 2, 471–510.
[1954] Milnor, J., Link groups, Ann. of Math. (2) 59, no. 2, 177–195.
[1957] Milnor, J., Isotopy of links , Algebraic Geometry and Topology:
A Symposium in Honor of S. Lefschetz, Princeton University Press,
Princeton, N.J., pp. 280–306.
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 279
[1958] Massey, W. S., Some higher order cohomology operations , Sympo-
sium Internacional de Topolog´ ıa Algebraica, Universidad Nacional
Aut´ onoma de M´ exico and UNESCO, Mexico City, pp. 145–154.
[1958] Woltjer, L., A theorem on force-free magnetic fields, Proc. Natl. Acad.
Sci. USA 44, no. 6, 489–491.
[1969] Massey, W. S., Higher order linking numbers, Conf. on Algebraic Topol-
ogy (Univ. of Illinois at Chicago Circle, Chicago, Ill., 1968), Univ. of
Illinois at Chicago Circle, Chicago, Ill., 1969, pp. 174–205.
[1969] Moffatt, H. K., The degree of knottedness of tangled vortex lines ,
J. Fluid Mech. 35, no. 1, 117–129.
[1973] Arnol ′d, V. I., The asymptotic Hopf invariant and its applications ,
Proc. Summer School in Differential Equations at Dilizhan (Erevan).
English translation in Selecta Math. Soviet. 5 (1986), no. 4, 327–345.
[1974] Hansen, V. L., On the space of maps of a closed surface into the 2-
sphere, Math. Scand. 35, 149–158.
[1975] Casson, A., Link cobordism and Milnor’s invariant , Bull. Lond. Math.
Soc. 7, no. 1, 39–40.
[1976] Turaev, V., The Milnor invariants and Massey products , in Studies in
Topology-II, Zap. Nanc. Sem. Lenin. Ot. Math. Kogo oi Stet. Acad.
Nauk USSR 66, transl. Journ. Soviet Math.
[1980] Larmore, L. L.; Thomas, P. E., On the fundamental group of a space
of sections, Math. Scand. 47, 232–246.
[1980] Porter, R., Milnor’s ¯µ-invariants and Massey products , Trans. Amer.
Math. Soc. 257, no. 1, 39–71.
[1983] Fenn, R. A., Techniques of Geometric Topology, London Math. Soc.
Lecture Note Ser., vol. 57, Cambridge University Press, Cambridge.
[1983] Gluck, H.; Warner, F. W., Great circle fibrations of the three-sphere ,
Duke Math. J. 50, 107–132.
[1983] Warner, F. W., Foundations of Differentiable Manifolds and Lie
Groups, Grad. Texts in Math., vol. 94, Springer-Verlag, New York.
Corrected reprint of the 1971 edition.
280 DETURC, GLUCK, KOMENDARCZYK, MEL VIN et al
[1984] Berger, M. A.; Field, G. B., The topological properties of magnetic
helicity, J. Fluid Mech. 147, 133–148.
[1987] Matveev, S. V., Generalized surgeries of three-dimensional manifolds
and representations of homology spheres (Russian), Mat. Zametki, 42,
no. 2, 268–278.
[1989] Griffiths, D., Introduction to Electrodynamics, 2nd ed., Prentice-Hall,
Upper Saddle River, New Jersey.
[1989] Murakami, H.; Nakanishi, Y., On a certain move generating link-
homology, Math. Ann. 284, no. 1, 75–89.
[1989] Orr, K. E., Homotopy invariants of links , Invent. Math. 95, 379–394.
[1990] Berger, M. A., Third-order link integrals, J. Phys. A: Math. Gen. 23,
2787–2793.
[1990] Cochran, T. D., Derivatives of Links: Milnor’s Concordance Invariants
and Massey’s Products, Mem. Amer. Math. Soc. 84, no. 427, Amer.
Math. Soc., Providence, RI.
[1990] Habegger, N.; Lin, X.-S., The classification of links up to link-
homotopy, J. Amer. Math. Soc. 3, no. 2, 389–419.
[1991] Berger, M. A., Third-order braid invariants , J. Phys. A: Math. Gen.
24, 4027–4036.
[1992] Evans, N. W.; Berger, M. A., A hierarchy of linking integrals, Topolog-
ical Aspects of the Dynamics of Fluids and Plasmas (Santa Barbara,
CA, 1991), NATO Adv. Sci. Inst. Ser. E Appl. Sci., vol. 218, Kluwer
Acad. Publ., Dordrecht, 237–248.
[1994] Ruzmaikin, A.; Akhmetiev, P. M., Topological invariants of magnetic
fields, and the effect of reconnections, Phys. Plasmas 1, no. 2, 331–336.
[1995] Akhmetiev, P. M.; Ruzmaikin, A., A fourth-order topological invariant
of magnetic or vortex lines , J. Geom. Phys. 15, no. 2, 95–101.
[1995] Thurston, D. P., Integral expressions for the Vassiliev knot invariants ,
A.B. thesis, Harvard University. arXiv:math/9901110 [math.QA].
[1997] Bott, R., Configuration spaces and imbedding problems , Geometry
and Physics (Aarhus, 1995), Lect. Notes Pure Appl. Math., vol. 184,
Dekker, New York, 135–140.
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 281
[1997] Koschorke, U., A generalization of Milnor’s µ-invariants to higher-
dimensional link maps , Topology 36, no. 2, 301–324.
[1998] Akhmetiev, P. M., On a higher analog of the linking number of two
curves, Topics in Quantum Groups and Finite-Type Invariants, Amer.
Math. Soc. Transl. Ser. 2, vol. 185, Amer. Math. Soc., Providence, RI,
113–127.
[1998] Arnol ′d, V. I.; Khesin, B. A., Topological Methods in Hydrodynamics,
Appl. Math. Sci., vol. 125, Springer-Verlag, New York.
[1998] Cromwell, P.; Beltrami, E.; Rampichini, M., The Borromean rings ,
Math. Intelligencer 20, no. 1, 53–62.
[1998] Gompf, R. E., Handlebody construction of Stein surfaces, Ann. of Math.
(2) 148, no. 2, 619–693.
[2000] Laurence, P.; Stredulinsky, E., Asymptotic Massey products, induced
currents and Borromean torus links , J. Math. Phys. 41, no. 5, 3170–
3191.
[2001] Cantarella, J.; DeTurck, D.; Gluck, H., The Biot-Savart operator
for application to knot theory, fluid dynamics, and plasma physics ,
J. Math. Phys. 42, no. 2, 876–905.
[2001] Kallel, S., Configuration spaces and the topology of curves in projective
space, Contemp. Math. 279, 151–175.
[2002] Hornig, G.; Mayer, C., Towards a third-order topological invariant for
magnetic fields, J. Phys. A: Math. Gen. 35, 3945–3959.
[2002] Kohno, T., Loop spaces of configuration spaces and finite type invari-
ants, Invariants of Knots and 3-Manifolds (Kyoto, 2001), Geom. Topol.
Monogr., vol. 4, Geom. Topol. Publ., Coventry, 143–160.
[2002] Rivi` ere, T., High-dimensional helicities and rigidity of linked foliations ,
Asian J. Math. 6, no. 3, 505–533.
[2003] Khesin, B. A., Geometry of higher helicities , Mosc. Math. J. 3, no. 3,
989–1011.
[2003] Mayer, C., Topological link invariants of magnetic fields , Ph.D. thesis,
Ruhr-Universit¨ at Bochum.
282 DETURC, GLUCK, KOMENDARCZYK, MEL VIN et al
[2003] Mellor, B.; Melvin, P., A geometric interpretation of Milnor’s triple
linking numbers, Algebr. Geom. Topol. 3, 557–568.
[2004] Bodecker, H. V.; Hornig, G., Link invariants of electromagnetic fields ,
Phys. Rev. Lett. 92, 030406.
[2004] Koschorke, U., Link homotopy in Sn× Rm−n and higher order
µ-invariants, J. Knot Theory Ramifications 13, no. 7, 917–938.
[2005] Akhmetiev, P. M., On a new integral formula for an invariant of 3-
component oriented links, J. Geom. Phys. 53, no. 2, 180–196.
[2005] Auckly, D.; Kapitanski, L., Analysis of S2-valued maps and Faddeev’s
model, Comm. Math. Phys. 256, 611–620.
[2007] Cencelj, M.; Repovˇ s, D.; Skopenkov, M. B., Classification of framed
links in 3-manifolds , Proc. Indian Acad. Sci. Math. Sci. 117, no. 3,
301-306. arXiv:0705.4166v2 [math.GT].
[2007] Voli´ c, I., A survey of Bott-Taubes integration , J. Knot Theory Ramifi-
cations 16, no. 1, 1–43. arXiv:math/0502295v2 [math.GT].
[2008] DeTurck, D.; Gluck, H., Electrodynamics and the Gauss linking integral
on the 3-sphere and in hyperbolic 3-space , J. Math. Phys. 49.
[2008] Kuperberg, G., From the Mahler conjecture to Gauss linking forms ,
Geom. Funct. Anal. 18, no. 3, 870–892. arXiv:math/0610904v3
[math.MG].
[2009] Cantarella, J.; Parsley, J., A new cohomological formula for helicity
in R2k+1 reveals the effect of a diffeomorphism on helicity , preprint.
arXiv:0903.1465v2 [math.GT]
[2009] Komendarczyk, R., The third order helicity of magnetic fields via link
maps, to appear in Comm. Math. Phys. arXiv:0808.1533v1 [math.DG].
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 283
deturck@math.upenn.edu
gluck@math.upenn.edu
rako@tulane.edu
pmelvin@brynmawr.edu
cshonkwil@haverford.edu
shea@math.columbia.edu
