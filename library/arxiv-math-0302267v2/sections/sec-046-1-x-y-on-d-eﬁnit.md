---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-046-1-x-y-on-d-eﬁnit
section_title: "(X, y), on d´ eﬁnit"
section_number: 1
pages: 45-47
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
P H+ℓ
¯y,x := Q(1)H+ℓ \ P H+ℓ
y,x
et (4.4.2) se factorise par P H+ℓ
¯y,x × Q(1)H+ℓ, d´ eﬁnissant
(4.4.3) P H+ℓ
¯y,x → Z H+ℓ
Lemme 4.5. Le morphisme (4.4.3) est un plongement ferm´ e de RH+ℓ-sch´ emas.
Preuve. Il suﬃt de le v´ eriﬁer en r´ ealisation de de Rham, o` u l’asser tion se r´ eduit ` a la
suivante.
Lemme 4.6. Soit L l’alg` ebre de Lie sur k engendr´ ee par des ´ el´ ements(es)s∈S soumis ` a
la seule relation que ∑ es = 0. On suppose |S| ≥ 2, on ﬁxe ¯y ∈ S et on pose e := e¯y. Soit G
le sch´ ema en groupe prounipotent limite projective des GN := exp( L/ZN ). Le morphisme
de G/ exp(ke) dans Lie(G): g ↦→ad g(e), identiﬁe G/ exp(ke) ` a un sous-sch´ ema ferm´ e de
Lie(G), l’orbite adjointe de e.
Dans 4.6, Lie( G) est le sch´ ema pro-vectoriel limite projective des sch´ emas vectoriels
Lie(GN ).
Preuve. Les orbites de l’action d’un groupe unipotent sur un sch´ ema aﬃne sont ferm´ ees
Demazure, Gabriel (1970) IV 2.2.7). Si eN est l’image de e dans L/ZN et ZN ⊂ GN son
43
ﬁxateur, l’application g ↦→ad g(eN ) de GN /ZN dans Lie( GN ) est donc un plongement
ferm´ e. Par passage ` a la limite projective, l’application g ↦→ad g(e) de lim GN /ZN dans
Lie(G) = lim Lie( GN ) est ´ egalement un plongement ferm´ e.
L’alg` ebre de Lie du sous-groupe ZN de GN est le centralisateur de eN dans L/ZN .
Fixons b dans S distinct de ¯y. L’alg` ebre de LieL est librement engendr´ ee par leses (s ⁄= b).
D’apr` es 4.7 ci-dessous, le centralisateur de e est r´ eduit ` ake. Munissons L de la graduation
pour laquelle les es sont de degr´ e 1. La sous-alg` ebre ZN est la sous-alg` ebre “degr´ e ≥ N ”.
L’application lin´ eaire ade: L → L ´ etant de degr´ e 1 et de noyau r´ eduit ` ake, on a
Lie ZN = Ker(ad eN : L/ZN → L/ZN ) = keN + ZN−1/ZN .
La projection de GN+1/ZN+1 sur GN /ZN se factorise donc par GN / exp(keN ) et
G/ exp(ke) = lim GN / exp(keN ) ∼− →lim GN /ZN (e).
Lemme 4.7. Dans une alg` ebre de Lie libre L sur k, le centralisateur d’un g´ en´ erateure
est r´ eduit aux multiples de ce g´ en´ erateur.
D’apr` es Reutenauer (1993) 2.10, dans une alg` ebre de Lie libre, deux ´ el´ ements non nuls
quelconques qui commutent sont multiples l’un de l’autre. L e cas particulier 4.7 est, plus
simplement, cons´ equence de ce que l’alg` ebre de Lie libre L ib({e} ∪ A) est le produit semi-
direct de ke et de Lib((ad en(a))a∈A,n ≥ 0 et de ce que la d´ erivation ad en(a) ↦→ad en+1(a)
de l’alg` ebre associative libre engendr´ ee par les aden(a) est injective.
Il r´ esulte de 4.5 que P H+ℓ
¯y,x est motivique. Soient en eﬀet A l’alg` ebre deZ et AH+ℓ :=
realH+ℓ(A) celle de Z H+ℓ. D’apr` es 4.5, P H+ℓ
¯y,x est isomorphe ` a un sous-sch´ ema ferm´ e de
Z H+ℓ, d´ eﬁni par un id´ ealaH+ℓ de AH+ℓ. D’apr` es 2.14, 2.15, cet id´ eal est la r´ ealisation
d’un id´ eala de A, et P H+ℓ
¯y,x est isomorphe ` a la r´ ealisation de Spec(A/a).
4.8 Fin du cas 1 de la preuve de 4.4. Soit b ∈ S distinct de ¯y, et X ′ := P − { ¯y, b}.
Identiﬁons P et P1, par un isomorphisme envoyant ¯ y sur 0 et b sur ∞, donc X ′ sur A∗ =
Spec k[u, u−1]. Soit t := du ( y) la coordonn´ ee du vecteur tangent y en u = 0, et notons
encore t le point de Gm de coordonn´ eet. Les espaces de chemins P H+ℓ
y,x (X ′) et P H+ℓ
t,x (Gm)
44
sont canoniquement isomorphes (Deligne (1989) §14). Puisque t et x sont des points-base
` a distance ﬁnie de Gm, P H+ℓ
y,x est motivique. C’est d’ailleurs simplement un torseur de
Kummer: on a πmot
