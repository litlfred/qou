---
doc_id: cuspshapes
doc_title: "CUSP SHAPE AND TUNNEL NUMBER"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: CuspShapes.pdf
source_sha256: 01db19e63193e6ae
toc_source: outline
doc_brief: "CUSP SHAPE AND TUNNEL NUMBER — We show that the set of cusp shapes of hyperbolic tunnel number one manifolds is dense in the Teichm¨uller space of the torus."
---
This paper is concerned with two invariants for a 3-manifold with torus boundary.
The ﬁrst is geometric.
If the interior of the 3-manifold admits a hyperbolic
structure, then a tubular neighborhood of the torus boundary inherits a Euclidean
structure, and this Euclidean structure is unique up to similarity of the torus. The
similarity class of such a Euclidean structure is called the cusp shape of the 3-manifold.
Manifolds with restricted cusp shapes have restrictions on their Dehn ﬁllings, for
example by the 2π-theorem [6] or the 6-Theorem [2, 23]. There are uncountably
many similarity classes of Euclidean metrics on the torus, but only countably many
ﬁnite volume hyperbolic 3-manifolds. Thus not all similarity classes of metrics can
appear as cusp shapes of hyperbolic 3-manifolds. Nevertheless, in [31], Nimershiem
proved that the set of similarity classes occurring as cusp shapes of any hyperbolic
3-manifold is dense. Does the set of similarity classes occurring as cusp shapes remain
dense when other restrictions are put on the manifold?
The second notion is topological. Every 3-manifold M admits a Heegaard splitting:
a decomposition along an embedded Heegaard surface into two handlebodies, or
compression bodies if M has boundary. Frequently, we would like to know the
minimal genus over all possible Heegaard splittings of M. If M has a single torus
boundary component, a genus g Heegaard splitting gives a decomposition of M
into a genus g handlebody and a compression body homeomorphic to the union of
T 2 × I and g −1 one-handles; see Deﬁnition 2.1 below. In this case, the core of each
one-handle of the compression body is called a tunnel; the union of the g −1 tunnels
in M is a tunnel system for M. A 3-manifold with one torus boundary component
and a minimal genus g Heegaard splitting is called a tunnel-number g −1 manifold.
For hyperbolic manifolds, the tunnel number is known to give a lower bound on
hyperbolic volume [35].
A natural question to ask is whether there is a relationship between cusp shape
and tunnel number, or whether restrictions on tunnel number give restrictions on
cusp shape. In the case of tunnel number one, work of Baker on Berge knots [3]
implies that there is an inﬁnite sequence of cusped hyperbolic tunnel number one
2010 Mathematics Subject Classiﬁcation. 57M50, 57M27, 30F40.
1
2
VINH DANG AND JESSICA S. PURCELL
manifolds with cusp shape approaching that of a 1 × 2 rectangle, up to scale. Do
all hyperbolic tunnel number one manifolds have a restricted set of cusp shapes in
their limit set? In this paper, we show they do not. In fact, the set of cusp shapes is
dense in the Teichm¨uller space of the torus.
Theorem 1.1. For any ϵ > 0 and any point [T] in the Teichm¨uller space of the
torus, there exists a complete, ﬁnite volume, tunnel number one hyperbolic manifold
M with a single cusp whose cusp shape is ϵ-close to [T].
A similar result holds for tunnel number n manifolds.
Theorem 1.2. For any ϵ > 0, any point [T] in the Teichm¨uller space of the torus,
and any integer n ≥1, there exists a complete, ﬁnite volume hyperbolic manifold
M that admits a tunnel system of n tunnels and has a single cusp, with cusp shape
ϵ-close to [T]. Further, assuming recent work of Maher and Schleimer [26], we can
ensure M is tunnel number n.
Theorem 1.1 also has interesting Dehn ﬁlling consequences.
Corollary 5.1. For any integer n ≥1, there exist inﬁnitely many hyperbolic tunnel
number n manifolds with at most one exceptional Dehn ﬁlling.
The Berge knots form a class of tunnel number one knots in S3 that admit a lens
space Dehn ﬁlling. Thus these knots have at least two exceptional Dehn ﬁllings:
the lens space and S3. Baker showed that inﬁnitely many come from Dehn ﬁlling a
minimally twisted chain link. It follows from his work that the cusp shapes of these
knots limit to a single Euclidean similarity structure; see Proposition 6.1. In sharp
contrast, Theorem 1.1 and Corollary 5.1 imply that cusp shapes of more general
tunnel number one manifolds have broader limits, and fewer exceptional Dehn ﬁllings.
Indeed, Corollary 5.1 was already known in the case n = 1: The 2-bridge knots form
a class of tunnel number one manifolds. It is known that inﬁnitely many hyperbolic
2-bridge knots admit at most one exceptional Dehn ﬁllings, due to work of Futer,
Kalfagianni and Purcell bounding the cusp areas of these knots [16]. However, that
paper does not discuss density of cusp shapes, and does not give any information on
knots with higher tunnel numbers.
There is less literature on cusp shapes or geometric limits of tunnel number n
manifolds for higher n. Examples of such manifolds with at least two exceptional
ﬁllings are known. Inﬁnite families of one-cusped hyperbolic manifolds with tunnel
number 2 and at least two exceptional Dehn ﬁllings have been constructed by
Dunﬁeld, Hoﬀman, and Licata [14], and by Baker [4]. Earlier, Teragaito found a
family of knots in S3 with a small Seifert ﬁbred surgery [34]; these were generalised
by Baker, Gordon, and Luecke to produce knots with tunnel number at least two and
at least two exceptional Dehn ﬁllings [5]. More generally, for any n, Eudave-Mu˜noz
and Luecke have constructed hyperbolic knots in S3 with two exceptional Dehn
ﬁllings and tunnel number bounded below by n [15]. By the 6-Theorem [2, 23], the
cusp shapes of these manifolds must lie in a bounded region of the moduli space of
the torus. However, the limiting shapes of cusps of these families of manifolds have
not been analyzed.
To investigate results on Dehn ﬁlling further, for example to determine whether
there are tunnel number n manifolds with no exceptional Dehn ﬁllings, we need to
know the cusp area of our manifolds, i.e. the area of the boundary of a maximal
CUSP SHAPE AND TUNNEL NUMBER
3
∼=
γ1
Figure 1. The (1; 2)-compression body
horoball neighborhood of the cusp. In this paper we use an algebraic limit argument
to give cusp shapes, bounding the similarity structure of the cusp torus, but not its
scale. Unfortunately, our method of proof does not give any information on cusp
area; a geometric limit argument would be required. Thus while the shortest slope
of the torus must have length at least one, and therefore long narrow tori have at
most one exceptional Dehn ﬁlling, we cannot determine whether fatter tori are large
or small, with long or short slope lengths. The following are still unknown.
Question 1.3. Are there families of tunnel number n manifolds with no short slopes
and no exceptional Dehn ﬁllings? What are the cluster points of the areas of the
maximal cusps of tunnel number n manifolds?
To prove Theorem 1.1, we consider geometric structures on compression bodies,
similar to work in [11], [8], and [24]. Given any framed Euclidean similarity structure
