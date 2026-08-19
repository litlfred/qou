---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-011-2-functional-equations
section_title: "Functional equations"
section_number: 2
pages: 6-8
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
In contrast to the paucity of special values, the dilogarithm function s atisﬁes
a plethora of functional equations. To begin with, there are the two re ﬂection
properties
Li2
( 1
z
)
= − Li2(z) − π2
6 − 1
2 log2(−z) ,
Li2(1 − z)= − Li2(z)+ π2
6 − log(z) log(1 − z) .
The Dilogarithm Function 9
Together they say that the six functions
Li2(z), Li2
( 1
1 − z
)
, Li2
( z − 1
z
)
, − Li2
( 1
z
)
, −Li2(1 − z), −Li2
( z
z − 1
)
are equal modulo elementary functions, Then there is the duplicat ion formula
Li2(z2)=2
(
Li2(z)+L i 2(−z)
)
and more generally the “distribution property”
Li2(x)= n
∑
zn=x
Li2(z)( n =1 , 2, 3,... ).
Next, there is the two-variable, ﬁve-term relation
Li2(x)+L i 2(y)+L i 2
( 1 − x
1 − xy
)
+L i2 (1 − xy)+L i 2
( 1 − y
1 − xy
)
= π2
6 − log(x) log(1 − x) − log(y) log(1 − y) + log
( 1 − x
1 − xy
)
log
( 1 − y
1 − xy
)
which (in this or one of the many equivalent forms obtained by applying
the symmetry properties given above) was discovered and rediscov ered by
Spence (1809), Abel (1827), Hill (1828), Kummer (1840), Schaeﬀer (1846),
and doubtless others. (Despite appearances, this relation is symmet ric in the
ﬁve arguments: if these are numbered cyclically as zn with n ∈ Z/5Z, then
1 − zn =
(
z−1
n−1 − 1
)(
z−1
n+1 − 1
)
= zn−2zn+2.) There is also the six-term relation
1
x + 1
y + 1
z =1 ⇒ Li2(x)+L i 2(y)+L i 2(z)
= 1
2
[
Li2
(
− xy
z
)
+L i2
(
− yz
x
)
+L i2
(
− zx
y
)]
discovered by Kummer (1840) and Newman (1892). Finally, there is the
strange many-variable equation
Li2(z)=
∑
f (x)=z
f (a)=1
Li2
( x
a
)
+ C(f ) , (1)
where f (x) is any polynomial without constant term and C(f ) a (complicated)
constant depending on f .F o r f quadratic, this reduces to the ﬁve-term rela-
tion, while for f of degree n it involves n2 + 1 values of the dilogarithm.
All of the functional equations of Li 2 are easily proved by diﬀerentiation, C
while the special values given in the previous section are obtained by combin-
ing suitable functional equations. See [4].
