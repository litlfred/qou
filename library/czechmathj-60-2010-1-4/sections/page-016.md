---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: page-016
section_title: "Page 16"
section_number: null
pages: 16-16
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
toc_source: undetermined
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
---
Theorem 7.3. Let I be as above. Then, with the ordering ≺on XX∗as above,
I is a Gröbner-Shirshov basis in mod⟨X⟩k⟨X⟩.
P r o o f.
There are two kinds of compositions: w1 = xabc (a > b > c) and
w2 = ucdvab (c > d, a > b). Denote
f1 = xabc −xacb +
X
(xa)(1)⟨(xa)(2); b, c⟩,
f2 = xab −xba +
X
x(1)⟨x(2); a, b⟩,
f3 = ucdvab −ucdvba +
X
(ucdv)(1)⟨(ucdv)(2); a, b⟩,
f4 = ucd −udc +
X
u(1)⟨u(2); c, d⟩.
Then, since σa,b,c(⟨xc; a, b⟩+ P⟨x(1); ⟨x(2); a, b⟩, c⟩) = 0, we have
(f1, f2)w1 = xabc −xacb +
X
x(1)a⟨x(2); b, c⟩+
X
x(1)⟨x(2)a; b, c⟩
−xabc + xbac −
X
x(1)⟨x(2); a, b⟩c
≡−xcab +
X
x(1)⟨x(2); a, c⟩b +
X
x(1)a⟨x(2); b, c⟩+
X
x(1)⟨x(2)a; b, c⟩
+ xbca −
X
x(1)b⟨x(2); a, c⟩−
X
x(1)⟨x(2)b; a, c⟩−
X
x(1)⟨x(2); a, b⟩c
≡
X
x(1)c⟨x(2); a, b⟩+
X
x(1)⟨x(2)c; a, b⟩+
X
x(1)⟨x(2); a, c⟩b
+
X
x(1)a⟨x(2); b, c⟩+
X
x(1)⟨x(2)a; b, c⟩−
X
x(1)⟨x(2); b, c⟩a
−
X
x(1)b⟨x(2); a, c⟩−
X
x(1)⟨x(2)b; a, c⟩−
X
x(1)⟨x(2); a, b⟩c
≡
X
x(1)⟨x(2)a; b, c⟩+
X
x(1)⟨x(2); ⟨x(3); b, c⟩, a⟩+
X
x(1)⟨x(2)b; c, a⟩
+
X
x(1)⟨x(2)c; a, b⟩+
X
x(1)⟨x(2); ⟨x(3); c, a⟩, b⟩
+
X
x(1)⟨x(2); ⟨x(3); a, b⟩, c⟩
≡0
and since ⟨x[a, b]y; c, e⟩+ P⟨x(1)⟨x(2); a, b⟩y; c, e⟩= 0,
(f3, f4)w2
= ucdvab −ucdvba +
X
u(1)v(1)⟨u(2)cdv(2); a, b⟩+
X
u(1)cv(1)⟨u(2)dv(2); a, b⟩
+
X
u(1)dv(1)⟨u(2)cv(2); a, b⟩+
X
u(1)cdv(1)⟨u(2)v(2); a, b⟩
−ucdvab + udcvab −
X
u(1)⟨u(2); c, d⟩vab
73
