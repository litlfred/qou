---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-559-3-relation-with-formal-geometry-213
section_title: "RELATION WITH FORMAL GEOMETRY. 213"
section_number: 3
pages: 217-219
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
(ii) A◦ is (π)-adically completed,
(iii) A◦ is topologically of ﬁnite type over R; i.e. R{t1,... ,t n}/a∼
= A for
some ideal a in R{t1,... ,t n},
(iv) A◦ is ﬂat over R,
(v)
A is a k-algebra of ﬁnite type.
Proof. (i) and (ii) are easy to see. The ﬂatness of R is now equivalent to
the lack of R-torsion. So (iv) can be seen immediately.
Before proving (iii) and (v), we need some terminology: let ‖·‖α be a
Banach norm of A (α : T n
K→ A: surjective). We say an element f of A is
power-bounded if{‖f n‖α| n∈ N} is bounded. This does not depend on
the choice of the presentation α since the equivalence class of the resulting
norms do not change. An element f of A is said to be topologically nilpotent
if limf n = 0; here the limit is taken with respect to the Banach norm ‖·‖α,
and is not dependent of the choice.
Let us prove (iii). By [ BGR84, 6.2.3], A◦ is the set of all power-bounded
elements of A, and A◦◦ is the set of all topologically nilpotent elements.
Hence a choice of a presentation α : T n
K→ A induces surjections
T n
K
◦ −→ A◦
T n
K
◦◦ −→ A◦◦.
(iii) is due to the surjectivity of the ﬁrst arrow. By the surj ectivity of these
arrows and 3.2, we have (v).
Deﬁnition 3.4. AnR-algebraA is said to be admissible ifA is (π)-adically
completed, ﬂat over R, and topologically of ﬁnite type over R.
Remark 3.5. By [ BL93, 1.1 (c)], any admissible R-algebra A is topologi-
cally of ﬁnite presentation, i.e., there exists a ﬁnitely ge nerated ideal a in
R{t1,... ,t n} such that R{t1,... ,t n}/a∼
= A.
Deﬁnition 3.6 (Formal model and Analytic reduction) . Let X = Spm A
be an aﬃnoid over K. Then the formal scheme X = Spf A◦ over R is
called the formal model of X, and the algebraic scheme
X = Spec A overk
is called the analytic reduction of X.
We deﬁne the so-called reduction map
RedX : X = SpmA−→X = Spec A
by a↦→a∩ A◦/a∩ A◦◦.
Proposition 3.7. The map Red X is continuous with respect to the Zariski
topology of X and the G-topology of X; it maps X surjectively onto the set
of all closed points of X.
Proof. Let us consider the aﬃne open set Uf = Spec Af of Spec A relevant
tof∈ A. Take f∈ A◦ from the residue class f . The function f takes values
less than equal to 1 on Spm A. So Uf ={x∈ SpmA||f (x)| = 1} is a rational
subdomain whose associated aﬃnoid is Spm A{f,f−1}. Since the condition
214 A. RAPID COURSE IN p-ADIC ANALYSIS.
|f (x)| = 1 is equivalent to f (RedX (x))⁄= 0, we have Red−1
X (Uf ) = Uf . Then
the ﬁrst assertion follows. The last one is almost trivial.
Example 3.8 (Analytic reduction of the unit disk) . Let us consider the an-
alytic reduction of the unit disk D1 = D(0, 1+) = Spm K{T} (here we as-
sume that K is algebraically closed for simplicity). The analytic redu ction
is given by the aﬃne line A1
k = Speck[T ]. The reduction map Red D 1 maps
all “interior” points, i.e. those points lying in D(0, 1−) to the origin in A1
k,
and the other points to the non-zero points. If we identify D1 andR, A1
kand
k, then this is nothing but the mapping obtained by the reducti on modulo
m.
It is very important to see how the formal models behave under localiza-
tion of aﬃnoids. Let X = SpmA be an aﬃnoid over K andf0,... ,f n∈ A a
sequence of elements which does not have common zeros on Spm A. We con-
sider the admissible covering X =⋃
iUi consisting of rational subdomains
Ui ={x∈X||fj(x)|≤| fi(x)| for j⁄=i};
by multiplying a suitable power of π, we may assume that each fi belongs
to A◦. For each i,
Ui = SpmA
{ f0
fi
,... , fn
fi
}
,
and then the corresponding formal model is given by
Ui = Spf A◦
{ f0
fi
,... , fn
fi
}
/ ((π)−torsions).
These formal schemes glue and the resulting morphism
⋃
0≤i≤n
Ui−→ X = Spf A◦
is the formal blow-up along the ideal a = (f0,... ,f n)⊂ A◦. We note here
that the ideal a contains a power of π, or what amounts to the same, a is
an open ideal, for aA = A.
This simple observation indicates:
Slogan (vague): Reﬁnements of admissible coverings corresponds to formal
blow-up’s along open coherent ideals.
Example 3.9. Let us assume in this example that K is algebraically closed.
We consider the admissible covering D1 = U1∪U2 of the unit disk D1 =
SpmK{T} given by
U1 = {z∈K||z|≤| π|} = Spm K
{ T
π
}
,
U2 = {z∈K||π|≤| z|≤ 1} = Spm K
{
T, π
T
}
.
The corresponding formal models are
U1 = Spf R
{ T
π
}
= Spf R{T,U}/(πU−T ),
U2 = Spf R
{
T, π
T
}
= Spf R{T,V}/(TV −π)
