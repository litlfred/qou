---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-002-2-1-finite-dimensional-analogs
section_title: "Finite-Dimensional Analogs"
section_number: "2.1"
pages: 8-10
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
2.1 Finite-Dimensional Analogs
A much simpler prototype of this problem is a finite-dimensional oscillatory integral such as
the one that defines the Airy function:
Zλ =
Z ∞
−∞
dx exp iλ(x
3
/3 − x)

. (2.6)
For real λ, this integral converges, though not absolutely so, because of rapid oscillations at
infinity; when λ becomes complex, it must be defined by a process of analytic continuation.
The Airy integral will serve as a useful practice case in section 3. The following slightly
more elaborate example is also useful. Introduce a complex variable z and a complex-valued
polynomial
g(z) = Xn
j=0
ajz
j
. (2.7)
Now consider the integral
Zg =
Z
|d
2
z| exp g(z) − g(z)

. (2.8)
This again is a convergent oscillatory integral and a closer analog of complex Chern-Simons
theory, with −ig(z) and ig(z) corresponding to the terms tW and et W in the action (2.3).
We stress that no contour integral is intended in (2.8) – a contour integral could scarcely
be intended here as the integrand is not holomorphic! Rather, if z = u + iv, with real u, v,
we integrate separately over u and v, the integration measure being |d
2
z| = 2 du dv.
A finite-dimensional analog of analytically continuing Chern-Simons theory with complex
gauge group as a function of s is to analytically continue the Airy function Zλ to complex
8

λ. An even closer analog is to analytically continue the integral Zg to let g be independent
of g. By this, we mean the following. Define a new polynomial
eg(z) = Xn
j=0
eajz
j
, (2.9)
and generalize the integral Zg to
Zg,eg =
Z
|d
2
z| exp (g(z) − ge(z)). (2.10)
Then Zg,eg coincides with the original Zg if ge = g (by which we mean that eaj = aj
for all j).
The natural way to analytically continue the Airy function in λ is to let x become a
complex variable and to deform the integration contour away from the real axis so that the
integral remains convergent as λ varies. Similarly, to extend the definition of Zg,eg to eg 6= g,
we analytically continue, treating z and z – or equivalently u and v, defined by z = u + iv,
z = u −iv – as independent complex variables. Denoting the independent complex variables
as z and ze (rather than z and z), the analytically continued integral is
Zg,eg =
Z
C
dz dze exp (g(z) − eg(ze)). (2.11)
The integral is over a two-dimensional real integration cycle C, which is the real slice ze = z
if eg = g, and in general must be deformed as g and eg vary so that the integral remains
convergent.
This then is the framework that we will have to imitate to understand the analytic
continuation of Chern-Simons theory with a complex gauge group. Just as we promoted
z to a complex variable ze that is independent of z, we will have to promote A to a new
G-valued connection Ae that is independent of A. Thus we consider the classical theory with
independent G-valued connections A and Ae (we recall that G is a complex Lie group such
as SL(2, C)) and action
I(A, Ae) = t
8π
Z
M
Tr A ∧ dA +
2
3
A ∧ A ∧ A+
et
8π
Z
M
Tr A ∧e dAe +
2
3
A ∧e A ∧e Ae

.
(2.12)
Then we have to find an appropriate integration cycle C in the path integral
Z
C
DA DAe exp iI(A, Ae)

. (2.13)
The cycle C must be equivalent to Ae = A if s is real, and in general must be obtained by
deforming that one as s varies so that the integral remains convergent. (We also have to
learn how to deal with gauge invariance when A and Ae are treated as independent.)
9
