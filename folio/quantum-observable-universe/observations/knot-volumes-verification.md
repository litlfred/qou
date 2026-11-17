**Scope.** This block is a numerical check, not a proof. It recomputes the
hyperbolic volumes the paper uses with SnapPy 3.3 and compares them with the
values quoted elsewhere. It derives no step of the mass chain, and a SnapPy
agreement is evidence about a floating-point computation, not a theorem.

Where a closed form is known, it is the value of record, and SnapPy only
checks it:

- $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) = 6\,\Lambda(\pi/3) \approx 2.0298832128$, two regular ideal tetrahedra.
- $\mathrm{Vol}(\text{Borromean rings}) = 16\,\Lambda(\pi/4) = 8G \approx 7.3277247534$, with $G$ Catalan's constant (two regular ideal octahedra).
- Torus knots and links, including $3_1$, $5_1$, $7_1$ and the Hopf link, are not hyperbolic, and their volume is $0$ by definition.
- $\mathrm{Vol}(5_2) \approx 2.8281220883$ has no closed form of this kind. It is a sum of Bloch–Wigner values at the shape parameters of an ideal triangulation (a root of a cubic), so here the SnapPy value is the one used.

**Checked values**: see [Table 1](#tbl:knot-volumes-verification-table1-data).

**Derived quantities**: see [Table 2](#tbl:knot-volumes-verification-table2-data).
