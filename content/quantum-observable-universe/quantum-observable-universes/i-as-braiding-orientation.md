The imaginary unit $i$ appears in three distinct but related contexts
in the QOU framework.  Each appearance is, in reality, the same
underlying datum: the **orientation of the braiding**
$c_{V,V}$ versus $c_{V,V}^{-1}$.

**Algebraic face (Wick rotation).**
The [Wick-rotation remark](#rem:laplace-fourier-wick-rotation)
identifies $i$ in the Fourier grouplike pairing
$\exp_q(i\xi\,\cdot)$ with the complex-time rotation
$t \mapsto it$ that converts the Laplace half-plane into the Fourier
half-plane.  This rotation is **orientation-dependent**: replacing
$i$ with $-i$ swaps the two half-planes (Laplace $\leftrightarrow$
Fourier), reversing the direction of complex-time evolution.

**Geometric face (CR complex structure).**
The [linearisation convention](#sec:linearisation-convention) identifies
$i$ with the CR complex structure operator
$J \colon H \to H$ ($J^2 = -\mathrm{Id}$) on the Levi distribution.
The operator $J$ is determined by the contact form up to an overall
sign: choosing $+J$ or $-J$ is a choice of **CR orientation**.  This
sign choice is identical to the braiding-orientation choice encoded in
[braiding-induced ordering](#prop:braiding-induced-ordering):
$c_{V,V}$ (positive crossing, forward time) versus
$c_{V,V}^{-1}$ (negative crossing, reverse time).

**Combinatorial face (arrow of time).**
[Proposition~braiding-induced-ordering](#prop:braiding-induced-ordering)
establishes that $c_{V,V}$ (positive crossing) defines "forward time"
in the Hecke basis ordering $\prec_c$, while $c_{V,V}^{-1}$ reverses
this ordering.  Negating $i$ in either of the above faces
($i \mapsto -i$ in the Wick rotation, $J \mapsto -J$ in the CR
structure) is equivalent to flipping crossing orientation
($c_{V,V} \leftrightarrow c_{V,V}^{-1}$), which is time reversal
(the T component of CPT symmetry).

**Summary.**  The three faces — algebraic, geometric, combinatorial —
are three manifestations of a single binary choice: the orientation of
$c_{V,V}$.  Fixing $i$ (rather than $-i$) as the Wick-rotation factor
is the same convention as fixing $c_{V,V}$ (rather than $c_{V,V}^{-1}$)
as the positive crossing — the arrow of time for the QOU.
