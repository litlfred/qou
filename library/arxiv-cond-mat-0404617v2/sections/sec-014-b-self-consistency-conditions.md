---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-014-b-self-consistency-conditions
section_title: "Self-consistency conditions"
section_number: B
pages: 16-18
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
CONDITIONS
In this section, we derive the self-consistency condi-
tions (8). We begin with the last relation, the so-called
“pentagon identity”, since it is the most fundamental.
To derive this condition, we use the fusion rule (7)
to relate the amplitude Φ
(
i
kj l
m
p q
)
to the amplitude
Φ
(
mi
j l k
sr
)
in two distinct ways (see Fig. 14). On the
one hand, we can apply the fusion rule (7) twice to obtain
i
kj l
m
qp
i m m i
j l k j l k
i m
j l k j l k
mi
q
sr
p
n n
(a) (b) (c)
(d) (e)
s
r
FIG. 14: The fusion rule (7) can be used to relate the am-
plitude of (a) to the amplitude of (c) in two diﬀerent ways.
On the one hand, we can apply the fusion rule (7) twice -
along the links denoted by solid arrows - to relate (a) → (b)
→ (c). But we can also apply (7) three times - along the links
denoted by dashed arrows - to relate (a) → (d) → (e) → (c).
Self-consistency requires that the two sequences of the ope ra-
tion lead to the same linear relations between the amplitude s
of (a) and (c).
the relation
Φ
(
i
kj l
m
p q
)
=
∑
r
F jip
q∗kr∗ Φ
(
i m
j l k
r
q
)
=
∑
r,s
F jip
q∗kr∗ F riq∗
mls∗ Φ
(
mi
j l k
sr
)
(Here, we neglected to draw a shaded region surround-
ing the whole diagram. Just as in the local rules (4-7)
the ends of the strings i, j, k, l, m are connected to some
arbitrary string-net conﬁguration). But we can also ap-
ply the fusion rule (7) three times to obtain a diﬀerent
relation:
Φ
(
i
kj l
m
p q
)
=
∑
n
F mlq
kp∗nΦ
(
i m
j l k
n
p
)
=
∑
n,s
F mlq
kp∗nF jip
mns∗ Φ
(
j l k
mi
n s
)
=
∑
n,r,s
F mlq
kp∗nF jip
mns∗ F js∗n
lkr∗ Φ
(
mi
j l k
sr
)
If the rules are self-consistent, then these two relations
must agree with each other. Thus, the two coeﬃcients
of Φ
(
mi
j l k
sr
)
must be the same. This equality implies
the pentagon identity (8).
The ﬁrst two relations in (8) are less fundamental. In
fact, the ﬁrst relation is not required by self-consistency
at all; it is simply a useful convention. To see this, con-
sider the following rescaling transformation on wave func-
tions Φ → ˜Φ. Given a string-net wave function Φ, we can
obtain a new wave function ˜Φ by multiplying the ampli-
tude Φ( X) for a string-net conﬁguration X by an arbi-
trary factor f (i, j, k) for each vertex {i, j, k} in X. As
long as f (i, j, k) is symmetric in i, j, k and f (0, i, i∗) = 1,
(a) (b) (c) (d)
n n i k l nn l
m m m j
k
i
j
l
l
i
j
j
k
i
k m
FIG. 15: Four string-net conﬁgurations related by tetrahe-
dral symmetry. In diagram (a), we show the tetrahedron cor-
responding to Gijm
kln . In diagrams (b), (c),(d), we show the
tetrahedrons Glkm∗
jin , Gjim
lkn∗ , Gimj
k∗nl, obtained by reﬂecting (a)
in 3 diﬀerent planes: the plane joining n to the center of m,
the plane joining m to the center of n, and the plane joining
i to the center of k. The four tetrahedrons correspond to the
four terms in the second relation of (8).
this operation preserves the topological invariance of Φ.
The rescaled wave function ˜Φ satisﬁes the same set of
local rules with rescaled F ijm
kln :
F ijm
kln → ˜F ijm
kln = F ijm
kln
f (i, j, m)f (k, l, m∗)
f (n, l, i)f (j, k, n∗) (B1)
Since Φ and ˜Φ describe the same quantum phase, we
regard F and ˜F as equivalent local rules. Thus the ﬁrst
relation in (8) is simply a normalization convention for F
or Φ (except when i, j or k vanishes; these cases require
an argument similar to the derivation of the pentagon
identity).
The second relation in (8) has more content. This re-
lation can be derived by computing the amplitude for a
tetrahedral string-net conﬁguration. We have:
Φ

 n
k
l
j m
i

 = F ijm
kln Φ


n
n
lk j i


=F ijm
kln F nk∗j∗
kn∗0 dkΦ
(
n
l
i
)
=F ijm
kln F nk∗j∗
kn∗0 F n∗i∗l∗
in0 dkdidnΦ( ∅) (B2)
=F ijm
kln vivj vkvlΦ( ∅) (B3)
We deﬁne the above combination in the front of Φ( ∅)
as:
Gijm
kln ≡ F ijm
kln vivjvkvl (B4)
Imagine that the above string-net conﬁguration lies on
a sphere. In that case, topological invariance (together
with parity invariance) requires that Gijm
kln be invariant
under all 24 symmetries of a regular tetrahedron. The
second relation in (8) is simply a statement of this tetra-
hedral symmetry requirement - written in terms of F ijm
kln .
(See Fig. 15).
In this section, we have shown that the relations (8)
are necessary for self-consistency. It turns out that these
relations are also suﬃcient. One way of proving this is to
use the lattice model (10). A straightforward algebraic
calculation shows that the ground state of 10 obeys the
local rules (4-7), as long as (8) is satisﬁed. This estab-
lishes that the local rules are self-consistent.
(a) (b)
FIG. 16: The fattened honeycomb lattice. The strings are
forbidden in the shaded region. A string state in the fattene d
honeycomb lattice (a) can be viewed as a superposition of
string states on the links (b).
