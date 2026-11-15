---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-004-21-locally-stable-pair-potentials
section_title: "(Locally) Stable Pair Potentials"
section_number: 2.1
pages: 4-8
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
Let (X, X) be a measurable space, λ a σ-ﬁnite reference measure, and v a pair potential, i.e.,
v : X × X →R ∪{∞} is measurable and symmetric—in the sense that v(x, y) = v(y, x)
for any x, y ∈X. Corresponding to the potential v, Mayer’s f function is given by
f (x, y) = e−v(x,y) −1.
We call the pair potential v stable if there exists a measurable map B : X →R+ such
that for any n ∈N and x1, . . . , xn ∈X

1≤i< j≤n
(1 + f (xi, x j)) ≤e
n
k=1 B(xk)
(2.1)
holds; we call v locally stable or Penrose stable (due to O. Penrose, see [23]) if there exists
a measurable map C : X →R+ such that for any x0 ∈X, n ∈N and x1, . . . , xn ∈X
satisfying 
1≤i< j≤n(1 + f (xi, x j))̸ = 0
n

i=1
(1 + f (x0, xi)) ≤eC(x0)
(2.2)
holds. Notice that every locally stable potential is stable and that every non-negative potential
v is locally stable (with the choice C ≡0).
An activity function is a measurable map z : X →R. Physically relevant activities are
non-negative but for the purpose of studying the convergence of expansions it can be helpful
to admit negative (or complex) activities as well. We deﬁne the (signed) measure λz on X by
λz(B) :=

B
z(x)λ(dx),
B ∈X.
(2.3)
Cluster Expansions: Necessary...
Page 5 of 47
33
The weight of a graph G with vertex set [n] = {1, . . . , n} and edge set E(G) is
w(G; x1, . . . , xn) :=

{i, j}∈E(G)
f (xi, x j).
Let Gn be the set of all graphs with vertex set [n], Cn ⊂Gn the set of connected graphs and
ϕT
n(x1, . . . xn) :=

G∈Cn
w(G; x1, . . . , xn)
the n-th Ursell function. For n ∈N and k ∈N0, let Dn,n+k ⊂Gn+k be the collection of all
graphs G such that every vertex j ∈{n +1, . . . , n +k} connects to at least one of the vertices
i ∈{1, . . . , n}. We may view the vertices {1, . . . , n} as roots and call the graphs G ∈Dn,n+k
multi-rooted graphs or, following the footnote 53 in [30], root-connected graphs. Consider
the functions
ψn,n+k(x1, . . . , xn+k) :=

G∈Dn,n+k
w(G; x1, . . . , xn+k).
For n = 1, the functions coincide with the standard Ursell functions, i.e., ψ1,1+k = ϕT
1+k.
We are interested in the associated series
ρn(x1, . . . , xn; z) :=
∞

k=0
1
k!

Xk ψn,n+k(x1, . . . , xn, y1, . . . , yk)z(x1) · · · z(xn)λk
z(d y).
The summand for k = 0 is to be read as ψn,n(x1, . . . , xn)z(x1) · · · z(xn). The series ρn
corresponds to the n-point correlation function of a grand-canonical Gibbs measure [30,
Eqs. (4–7)], see also [14]—it is the expansion of the correlation function in the activity z
around 0.
We will say that the activity expansions ρ converge absolutely for a non-negative activity
function z if
∞

k=0
1
k!

Xk |ψn,n+k(x1, . . . , xn, y1, . . . , yk)|z(x1) · · · z(xn)λk
z(d y) < ∞
for all n ∈N and (x1, . . . , xn) ∈Xn.
Our main concern is to derive necessary and sufﬁcient convergence conditions, but some-
times it is useful to view the series as purely formal; relevant background on formal power
series whose variable is a measure (here λz(dx)) is given in [17, Appendix A].
Next we introduce sign-ﬂipped Kirkwood–Salsburg operators. A selection rule s(·) is a
map from P(X) := ⊔∞
n=1Xn to N such that s(x1, . . . , xn) ∈{1, . . . , n} for all (x1, . . . , xn) ∈
P(X). To lighten notation we write xs rather than xs(x1,...,xn). Further let (x′
2, . . . , x′
n) be
the vector obtained from (x1, . . . , xn) by deleting the entry xs, leaving the order otherwise
unchanged. For the simplest selection rule that picks the ﬁrst entry s = 1, we have x′
i = xi.
The sign-ﬂipped Kirkwood–Salsburg operator ˜K s
z with selection rule s(·) acts on families
ξ = (ξn)n∈N of measurable symmetric functions ξn : Xn →R+ as
( ˜K s
z ξ)n(x1, . . . , xn) := z(xs)
n

i=2
(1 + f (xs, x′
i))

1l{n≥2}ξn−1(x′
2, . . . , x′
n)
+
∞

k=1
1
k!

Xk
k
j=1
 f (xs, y j)
 ξn−1+k(x′
2, . . . , x′
n, y1, . . . , yk)λk(d y)
	
,
(2.4)
33
Page 6 of 47
S. Jansen, L. Kolesnikov
for all n ∈N and (x1, . . . , xn) ∈Xn. Here we allow the functions ( ˜K s
z ξ)n to assume the
value “∞”. For non-negative potentials and on a suitably reduced domain, ˜K s
z differs from the
standard Kirkwood–Salsburg operator [26, Chapter 4.2] by a mere sign-ﬂip: it has | f (xs, yi)|
instead of f (xs, yi).
Theorem 2.1 Let z(·) be a non-negative activity and s(·) any selection rule. Consider the
following two conditions:
(i) There is a family ξ = (ξn)n∈N of measurable symmetric functions ξn : Xn →R+ such
that
z(x1)δn,1 + ( ˜K s
z ξ)n (x1, . . . , xn) ≤ξn(x1, . . . , xn)
(2.5)
for all n ∈N and (x1, . . . , xn) ∈Xn.
(ii) The series ρn(x1, . . . , xn; z) converges absolutely, for all n ∈N and (x1, . . . , xn) ∈Xn.
Condition (i) is sufﬁcient for (ii) to hold; moreover, if (i) is satisﬁed, then
∞

k=0
1
k!

Xk
ψn,n+k(x1, . . . , xn, y1, . . . , yk)
z(x1) · · · z(xn)λk
z(d y) ≤ξn(x1, . . . , xn)
(2.6)
on Xn, for all n ∈N.
In addition, if we assume the pair potential to be non-negative, then (ii) implies (i) as well,
so that the two conditions are equivalent in this case.
Remark 2.1 We formulate this theorem—as well as the following results—for non-negative
activities, mainly for the purpose of notational convenience. Naturally, such conditions for
absolute convergence can be formulated in the usual framework of complex analysis by
exchanging complex activities z with |z| in the convergence criteria.
We prove the theorem in Subsect. 3.2. The known sufﬁcient convergence conditions of
Kotecký–Preiss and Fernández–Procacci types are easily recovered from Theorem 2.1. We
start with the Kotecký–Preiss type criterion [18], as extended to soft-core and continuum
systems by Ueltschi in [32] (and to stable interactions by Ueltschi and Poghosyan in [24]).
Corollary 2.2 Let z be a non-negative activity function and assume stable interactions in the
sense of (2.1) for some B ≥0. If there exists a measurable function a : X →R+ such that
for all x ∈X

X
 f (x, y)
ea(y)λz(dy) + 2B(x) ≤a(x),
(2.7)
then the activity expansions ρn(x1, . . . , xn; z) converge absolutely and the bounds
ρn(x1, . . . , xn; z) ≤z(x1) · · · z(xn)ea(x1)+···+a(xn)
hold for all n ∈N and (x1, . . . , xn) ∈Xn. Notice that for non-negative pair interactions, we
can choose B ≡0 in condition (2.7).
Remark 2.2 Notice that via the substitution ˆa = a −2B the above criterion is equivalent to
the existence of a measurable function ˆa : X →R+ such that for all x ∈X

X
 f (x, y)
eˆa(y)+2B(y)λz(dy) ≤ˆa(x).
Cluster Expansions: Necessary...
Page 7 of 47
33
Proof Assume that (2.7) holds and deﬁne ξ = (ξn)n∈N, ξn : Xn →[0, ∞), by
ξn(x1, ..., xn) := z(x1) · · · z(xn)ea(x1)+···+a(xn)
for some a(·) satisfying (2.7). The interactions fulﬁll the stability condition (2.1), therefore
for every n ∈N and x1, ..., xn ∈X there exists an index j ∈{1, . . . , n} such that the bound

1≤i≤n,i̸= j
(1 + f (x j, xi)) ≤e2B(x j)
(2.8)
holds. Choose the selection rule s that always picks an element x j satisfying (2.8) from
(x1, . . . , xn). Plugging our choice of ξ into the left-hand side of Eq. (2.5) and bounding the
interaction term as n
i=2(1 + f (xs, x′
i)) ≤e2B(xs), we recognize an exponential series, and
ﬁnd altogether that the left-hand side of (2.5) is bounded by
z(xs)z(x′
2) · · · z(x′
n) ea(x′
2)+···+a(x′
n) exp

X
| f (xs, y)|ea(y)λz(dy) + 2B(xs)
	
.
By condition (2.7), this is in turn bounded by ξn(x1, . . . , xn). It follows that condition (i) of
Theorem 2.1 is satisﬁed.
⊓⊔
Analogously, one shows that the criterion by Fernández and Procacci [8], extended to soft-
core and continuum systems by Faris in [5] and by Jansen in [14], is sufﬁcient for absolute
convergence of the activity expansions ρ. We prove the result in the slightly more general
setup of locally stable interactions.
Corollary 2.3 Let z be a non-negative activity function and assume locally stable interactions
in the sense of (2.2) for some C ≥0. If there exists a measurable function μ : X →[0, ∞)
such that for all x ∈X
z(x)
⎛
⎝1 +
∞

k=1
1
k!

Xk e
k
j=1 C(y j)
k
j=1
 f (x, y j)


1≤i< j≤k
(1 + f (yi, y j))λk
μ(d y)
⎞
⎠≤μ(x),
(2.9)
then the activity expansions ρn(xn, . . . , xn; z) converge absolutely and the bounds
ρn(xn, . . . , xn; z) ≤

1≤i< j≤n

1 + f (xi, x j)
 n

i=1
μ(xi)
hold for all n ∈N and (x1, . . . , xn) ∈Xn. Notice that for non-negative pair interactions, we
can choose C ≡0 in condition (2.9).
Remark 2.3 The Fernández–Procacci condition improves on the the Kotecký–Preiss
condition—in the sense that the assumptions of Corollary 2.2 yield the assumptions of Corol-
lary 2.3. In other words, Corollary 2.3 in general guarantees convergence of ρ on a larger
domain of activities .
Proof Assume that (2.9) holds and deﬁne ξ = (ξn)n∈N, ξn : Xn →[0, ∞), by
ξn(x1, . . . , xn) :=

1≤i< j≤n

1 + f (xi, x j)
 n

i=1
μ(xi)
33
Page 8 of 47
S. Jansen, L. Kolesnikov
for some μ satisfying (2.9). Let s be the selection rule that always selects the ﬁrst entry—so
that xs = x1 and x′
i = xi for i ≥2. For locally stable pair potentials, we have
n

i=2
(1 + f (x1, xi))ξn+k−1(x2, . . . , xn, y1, . . . , yk)
=

1≤i< j≤n
(1 + f (xi, x j))

1≤i< j≤k
(1 + f (yi, y j))
n

i=2
k
j=1
(1 + f (xi, y j))
n

i=2
μ(xi)
k
j=1
μ(y j)
≤


1≤i< j≤n
(1 + f (xi, x j))
n

i=2
μ(xi)
	

1≤i< j≤k
(1 + f (yi, y j))
k
j=1
μ(y j)
	
e
k
j=1 C(y j ), (2.10)
where we used the local stability to estimate
n

i=2
k
j=1
(1 + f (xi, y j)) =
k
j=1
n

i=2
(1 + f (xi, y j)) ≤
k
j=1
eC(y j) = e
k
j=1 C(y j).
We plug our choice of ξ into the left-hand side of (2.5) and use the estimate (2.10) together
with the assumption (2.9) to ﬁnd that condition (i) of Theorem 2.1 is satisﬁed.
⊓⊔
Remark 2.4 We see that Theorem 2.1 provides a mechanism to prove sufﬁcient conditions for
absolute convergence—by constructing a sequence of ansatz functions ξ tailored to satisfy the
Kirkwood–Salsburg inequalities under the given condition. Conversely, given an appropriate
sequence of ansatz functions ξ, obtained, for example, as an approximation of ρ, one can try
to determine the corresponding sufﬁcient condition for convergence.
We now proceed to demonstrate the usefulness of that approach by deriving a sufﬁcient
condition that improves on the classical examples above.
