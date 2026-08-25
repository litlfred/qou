---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-010-c-examples
section_title: "Examples"
section_number: C
pages: 12-13
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
We give three examples to illustrate Proposition 1, each in ‘‘bare bones’’ format, and invite
the interested reader to carry out the supporting calculations.
Example 1: In this example, we start with the vector ﬁeld
V5]/]z5zˆ ~3.29!
on the ball V of radius a centered at the origin. Note that Ve CG(V).
Switching to spherical coordinates ( r,u,w), a straightforward computation yields
BS~V!5~a3/3!~sin u!/r2wˆ for r>a
5~1/3!r sin uwˆ for r<a. ~3.30!
Note that inside the ball, BS( V) coincides with the velocity ﬁeld of a body rotating with
constant angular velocity about the z-axis.
Next we compute „ 3BS(V),
„ 3BS~V!5~a3/3!$~2 cos u/r3!rˆ1~sin u/r3!uˆ% for r>a, ~3.31!
which is a standard dipole ﬁeld, while
„ 3BS~V!5~2/3!$~cos u!rˆ2~sin u!uˆ%5~2/3!V for r<a. ~3.32!
We invite the reader to check Proposition 1, equivalently the Maxwell equation ~3.10!, inside
the domain V by directly computing that Es85(21/3)V there.
Example 2 (see Example 4 of Sec. II C): In this example, we start with the function f 51/r on
the domain V between the spheres of radii 1 and 2 centered at the origin, and then consider the
vector ﬁeld
V5„ f 52 rˆ/r2 ~3.33!
on this domain. Note that the function f is harmonic, and is constant on each component of ]V.
Therefore V lies in the subspace HG ~V! of harmonic gradients inside VF ~V!. Borrowing once
again from the future proof of Theorem B, we note that V lies in the kernel of the Biot–Savart
operator.
We invite the reader to conﬁrm Maxwell’s equation ~3.10! by checking that
Es5rˆ/r2 inside V,
50 outside V. ~3.34!
Example 3 (see Example 5 of Sec. II C): In this example, we start with the function
f (x,y,z)5x21y21z2215r221 on the unit ball V centered at the origin, and then consider the
vector ﬁeld
V5„ f 52rrˆ ~3.35!
on this ball. Note that V lies in the subspace GG ~V! of grounded gradients inside VF ~V!, and is
therefore ~borrowing from the future proof of Theorem B ! in the kernel of the Biot–Savart
operator BS.
886 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
With this in mind, we invite the reader to conﬁrm Maxwell’s equation ~3.10! in this case by
computing that
Er52 2rrˆ inside V
52 2rˆ/r2 outside V, ~3.36!
and that
Es50 inside V
52rˆ/r2 outside V. ~3.37!
