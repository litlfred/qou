---
doc_id: lee-vanderveen-colored-jones-polynomials-without-tails
doc_title: "COLORED JONES POLYNOMIALS WITHOUT TAILS"
section_id: sec-003-2-ok-1kk-1-1kv2k-lot
section_title: "Ok = (−1)k[k + 1] = (−1)kv2k +lot"
section_number: 2
pages: 2-4
source_pdf: lee-vanderveen-colored-jones-polynomials-without-tails.pdf
source_sha256: fcc45aebd34e25dc
doc_brief: "COLORED JONES POLYNOMIALS WITHOUT TAILS — We exhibit an in nite family of knots with the property that the rst coecient of the n-colored Jones polynomial grows linearly with n."
---
(a;b;c ) =O
a+b+c
2
 a+b+c
2−a+b+c
2 ; a−b+c
2 ; a+b−c
2

= (−1)
a+b+c
2 va+b+c+ab+bc+ca−a2+b2+c2
2 +lot
∆(a;b;c;
;
;
 ) =
X
z
Oz
O
a+b+c
2
 z
a+b+c
2
 −a+b+c
2
z−a+
+
2
 a−b+c
2
z−
+b+
2
 a+b−c
2
z−
+
+c
2

=
(−1)m−a+b+c
2 vg(m+1;a+b+c
2 +1)+g( −a+b+c
2 ;m−a+
+
2 )+g(a−b+c
2 ;m−
+b+
2 )+g(a+b−c
2 ;m−
+
+c
2 ) +lot
where g(n;k ) = 2k(n−k) and 2m =a +b +c +
 +
 +
−max(a +
;b +
;c +
)
Our formulas agree with the integer normalization of [5]. The formula ∆ is the quotient of the
6j-symbol and a theta; it is in fact a Laurent polynomial. The summation range for ∆ is ﬁnite as
dictated by the binomials.
COLORED JONES POLYNOMIALS WITHOUT TAILS 3
The colored Jones polynomial of any KTG can now be deﬁned by the following three equations.
(1) ⟨Fe
±(Γ);⟩=f((e))±1⟨Γ;⟩
Here Fe
±(Γ) means the result after applying framing change to edge e of the KTG Γ.
(2) ⟨Ue(Γ);′⟩=⟨Γ;⟩
X
(e)
O(e)
((e); (b); (d))
The two colorings and′agree on all edges except that Ue(Γ) does not have edge e. The four edges
in Γ adjacent to e must have the same colors as b and d in Ue(Γ). Also, the summation is over all
possible values of color of the missing edge (e). Most values yield zero because the factorials vanish.
The only values that may be non-zero are when (e) is between|′(b)−′(d)|and ′(b) +′(d) and
has the same parity. Finally,
(3) ⟨Aw(Γ);′⟩=⟨Γ;⟩∆(′(a);′(b);′(c);′(
);′(
);′(
))
In this equation the colorings  and ′again agree on all edges where it makes sense. The colors of
the six new edges are denoted a;
;b;
;c;
 as shown in Figure 2 and ∆ is deﬁned above.
De
nition 2.2. As noted above a 0-framed knot K is a special case of a KTG with a single edge e.
In this case we denote its colored Jones polynomial by JK;n =⟨K;⟩, where (e) =n−1.
We study the family of Montesinos knots C(r;s;t;u ) shown in Figure 1. For technical reasons we
restrict ourselves to s≤−3≤3r;t;u all odd. And u< 0. A similar family was studied in [14].
A; A
 A; F
2(−r + s + t + u)
u −u−u
−u − s −u − s
s
−r − s −s − t
−r − t
=
−1 −1
1
r t
Figure 3. Starting from a theta graph (left), we ﬁrst apply the A-move to both
vertices, and again on one of the newly created vertices. Next change the framing on
many edges. The numbers on each edge indicate the number of half twists present.
Finally unzip the four edges (shown thickened) marked with r;s;t;u , respectively, to
obtain the 0-framed diagram for the knot C(r;s;t;u ).
To compute the colored Jones polynomial of K =C(r;s;t;u ) we take the following steps (see also
[13]). The ﬁrst step is to generate our knot K from the theta graph by KTG moves. One way to
achieve this is shown in Figure 3. All edges should be thought of as bands with blackboard framing.
The numbers indicate half twists (not colors). Note that the unzip applied to a twisted edge produces
two twisted bands that form a crossing as shown in the ﬁgure on the right. This is natural considering
that the black lines stand for actual strips. Reading backwards and applying the above equations we
may compute JK;n+1 as follows. The unzips yield four summations, the framing change multiplies
everything by the factors f, the A moves produce the ∆ terms and ﬁnally we are left with a single
(2a; 2b; 2c). Note we have scaled the summation variables a;b;c;d to make them integers instead of
even integers.
JC(r;s;t;u);n+1 =f(n)−2Wr(r;s;t)−2r−2s−2t+2u X
a;b;c;d∈nP∩Z
∆(2a; 2b; 2c;n;n;n )2×
∆(2b;n;n; 2d;n;n )O2aO2bO2cO2df(2a)rf(2b)sf(2c)tf(2d)−u(2a; 2b; 2c)
(2a;n;n )(2b;n;n )(2c;n;n )(2d;n;n )
