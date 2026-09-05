---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-059-123-geometry-of-the-critical-locus
section_title: "Geometry of the critical locus"
section_number: 12.3
pages: 68-69
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
invariant let us discuss the structure of the scheme X crit
ℓ := Spec(Rℓ). First, we describe a particular set of
generators of the ideal I crit
ℓ . Let us notice that we can rewrite the intermediate potential Wi,i+1 as follows
(12.44) Wi,i+1 = Tr(Ad−1
gi (X)Yi− Ad−1
gi+1 (X)Yi+1)
As we explain in the section 5 the potential Wi,i+1 could be rewritten as follows:
Tr( ˜Xi,+Adgi,i+1 (Yi+1))− Tr( ˜Xi,−−(Yi− Adgi,i+1 (Yi+1)++)).
Here and everywhere below the notations are consistent with the n otations of section 5, that is M+ (M−) is
the upper-triangular (lower-triangular) part of a matrix M andM++ (M−−) is the strictly upper-triangular
(lower-triangular) part of M and
gi,i+1 =g−1
i gi+1, ˜Xi = Ad −1
gi (X).
Taking partial derivatives of the last function with respect to the c oordinatesYi+1, ˜Xi,+,g,Yi−Adgi,i+1 (Yi+1)++, ˜Xi,−−
we obtain equations:
Ad−1
gi,i+1 ( ˜Xi)−− = 0,(12.45)
Adgi,i+1 (Yi+1)− = 0,(12.46)
[Adgi,i+1 (Yi+1), ˜Xi,+] = 0,(12.47)
˜Xi,−− = 0,(12.48)
Yi = Ad gi,i+1 (Yi+1)++.(12.49)
Let us notice that the last equations the ﬁrst and the second lines a ctually imply:
(12.50) [Yi, ˜Xi,+] = 0,
since [Ad gi,i+1 (Yi+1), ˜Xi,+] = [Ad gi,i+1 (Yi+1)++, ˜Xi,+] + [Adgi,i+1(Yi+1)−, ˜Xi,+].
On the other hand if we compute the partial derivatives by X of the LHS of (12.44) we get
(12.51) Ad gi(Yi) = Ad gi+1 (Yi+1)
Finally let us notice that the (12.45) and (12.50) imply that [ Yi+1, ˜Xi+1] = 0 and hence
(12.52) [AdgiYi,X ] = 0.
Let us notice that because of the previous observation (12.51), t he last equations (12.52) are equivalent for
diﬀerent values of i.
Thus we see that the G×Bℓ equivariant scheme X crit
ℓ comes equipped with the following maps:
pri : X crit
ℓ →CV b×n, pr i(g•,X,Y •) = (Yi, ˜Xi,+),
this map is B-equivariant;
pr : X crit
ℓ →CV g×g, pr (g•,X,Y •) = (Ad gi (Yi),X ),
this map is G-equivariant. The varieties CV B andCV G are the commuting sub varieties of n× b and g× g
respectively.
68
Proposition 12.1. The critical locus X crit
ℓ consists of elements (X,g 1,Y 1,...,g ℓ,Y ℓ) satisfying
Adgi(Yi) = Ad gi+1 (Yi+1)
Ad−1
gi (X)−− = 0
[X, Adg1 (Y1)] = 0.
