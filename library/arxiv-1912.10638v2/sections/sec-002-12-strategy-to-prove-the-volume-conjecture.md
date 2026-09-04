---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-002-12-strategy-to-prove-the-volume-conjecture
section_title: "Strategy to prove the volume conjecture"
section_number: 1.2
pages: 3-3
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by"
---
In this subsection, we brieﬂy discuss our approach to study the volume conjecture. A standard way to
prove volume conjecture involves three steps. Roughly speaking, ﬁrst of all, given the explicit formula of
the colored Jones polynomials of a link L evaluated at the (N + 1/2)-th root of unity, we convert it into
an integral of the form
∫
D
f(z1,z 2,...,z n) exp
((
N + 1
2
)
ΦL(z1,z 2,...,z n)
)
dz1dz2...dz n,
where (z1,z 2,...,z n)∈ Cn for some n, f(z1,z 2,...,z n) is a holomorphic function and Φ L(z1,z 2,...,z n)
is called the potential function of the link L. After that, we apply the saddle point approximation, which
says that the large N behavior of the integral is determined by the critical value of the potential function
at certain non-degenerate critical point.
The last step is to show that the real part of the critical value gives us the hyperbolic volume of the
link complement. Recall that in order to ﬁnd the critical point of the potential function, we need to solve
the critical point equations
∂
∂zi
ΦL(z1,z 2,...,z n) = 0 for i = 1, 2,...,n
It turns out that in many situations, the critical point equations of the potential function coincide with
the hyperbolic gluing equations (e.g. edges equations, surgery equations) of certain triangulation of the
link complement with shapes parameters parametrized by z1,z 2,...,z n. Finally, we need to argue that
the critical value of the potential function gives the hyperbolic volume of the link complement.
This approach has been used to study the volume conjecture of the colored Jones polynomials for
the ﬁgure eight knot [14], the 5 2 knot [18], and knots with 6 or 7 crossings [19, 20]. Moreover, the
correspondence between the critical point equations of the potential function to the edges equations of
certain triangulation has been studied for the twist knots [4] and two bridge knots [17].
Once the original volume conjecture is proved in this way, the generalized volume conjecture can be
proved by the ‘continuity argument’. The continuity argument has been used in [23]. The key point is
that all the technical assumptions in the above analysis depend continuously on the potential function
ΦL(z1,z 2,...,z n). In particular, if we change the colors Mi, we obtain a family of potential functions
which depends smoothly on the parameters si. Therefore, as long as si’s are suﬃciently close to 1, the
above analysis works and the result follows.
Remark 1. It turns out that for the colored Jones polynomials of the Whitehead link and the White-
head chains, we obtain two potential functions, and both of them give the hyperbolic volume of the link
complement at certain critical points. See Section 2 for more details.
