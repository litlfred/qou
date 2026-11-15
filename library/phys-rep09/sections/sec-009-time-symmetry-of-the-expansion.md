---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-009-time-symmetry-of-the-expansion
section_title: "Time-symmetry of the expansion"
section_number: null
pages: 15-16
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
The map ϕt : Y(t0) −→Y(t) corresponding to the linear differential equation (30) with Y(t0) = Y0 is time symmetric,
ϕ−t ◦ϕt = Id, since integrating (30) from t = t0 to t = tf for every tf ≥t0 and back to t0 leads us to the original initial value
Y(t0) = Y0. Observe that, according to (3), the map ϕt can be expressed in terms of the fundamental matrix (or evolution
operator) U(t, t0) as ϕtf (Y0) = U(tf , t0)Y0. Then time-symmetry establishes that
U(t0, tf ) = U−1(tf , t0)
or, in terms of the Magnus expansion,
Ω(tf , t0) = −Ω(t0, tf ).
To take advantage of this feature, let us write the solution of (30) at the final time tf = t0 + s as
Y

t1/2 +
s
2

= exp

Ω

t1/2 +
s
2, t1/2 −
s
2

Y

t1/2 −
s
2

,
(63)
where t1/2 = (t0 + tf )/2. Then
Y

t1/2 −
s
2

= exp

−Ω

t1/2 +
s
2, t1/2 −
s
2

Y

t1/2 +
s
2

.
(64)
On the other hand, the solution at t0 can be written as
Y

t1/2 −
s
2

= exp

Ω

t1/2 −
s
2, t1/2 +
s
2

Y

t1/2 +
s
2

,
(65)
166
S. Blanes et al. / Physics Reports 470 (2009) 151–238
so that, by comparing (64) and (65),
Ω

t1/2 −
s
2, t1/2 +
s
2

= −Ω

t1/2 +
s
2, t1/2 −
s
2

(66)
and thus Ωdoes not contain even powers of s. If A(t) is an analytic function and a Taylor series centered around t1/2 is
considered, then each term in Ωk is an odd function of s and, in particular, Ω2i+1(s) = O(s2i+3). This fact has been noticed in
[61,62] and will be fully exploited in Section 5.4 when analyzing the Magnus expansion as a numerical device for integrating
differential equations.
