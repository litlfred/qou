---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-010-time-symmetry-of-the-expansion
section_title: "Time-symmetry of the expansion"
section_number: null
pages: 15-16
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The map g! : Y(t) —> Y(t) corresponding to the linear differential equation (30) with Y (to) = Yo is time symmetric,
gy ‘og! =Id, since integrating (30) from t = to tot = ty for every ty > fo and back to to leads us to the original initial value
Y(to) = Yo. Observe that, according to (3), the map gy! can be expressed in terms of the fundamental matrix (or evolution
operator) U(t, to) as yf (Yo) = U(ty, to) Yo. Then time-symmetry establishes that

U(to, ty) = U- (ty, to)
or, in terms of the Magnus expansion,
Qty, to) = —2(to, ty).

To take advantage of this feature, let us write the solution of (30) at the final time t; = tp +s as

Y (ti + >) = exp (2 (ti + >. tiyja- >)) Y (ti - >) ; (63)
where t1/2 = (to + t)/2. Then
Y (ti - >) = exp (-2 (ti + , tia >)) Y (ae + >) : (64)

On the other hand, the solution at to can be written as

Y (t2 - >) = exp (2 (ti - >. tat >)) Y (t2 + >) ; (65)
166 S. Blanes et al. / Physics Reports 470 (2009) 151-238
so that, by comparing (64) and (65),

a(e St +3)= ae 4int >) (66)
1/2 2 1/2 3) = 1/2 z 1/2 3
and thus 92 does not contain even powers of s. If A(t) is an analytic function and a Taylor series centered around t1/2 is
considered, then each term in {2; is an odd function of s and, in particular, 82;,1(s) = @(s?'*3). This fact has been noticed in
[61,62] and will be fully exploited in Section 5.4 when analyzing the Magnus expansion as a numerical device for integrating
differential equations.
