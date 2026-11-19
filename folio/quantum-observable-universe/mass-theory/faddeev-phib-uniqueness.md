**Proposition (conditional on the Faddeev shift-class and its strip-growth characterization).**
*Fix the aether parameter $b = b(t)$ on the product-supported branch $\mathrm{Im} b^2 > 0$
(in particular the physical map $b(t) = \sqrt{t/2\pi}\,e^{i\pi/4}$ with $t = \ln q_0 > 0$).
Let $\Phi_1$ be any solution of the two modular-double $q$-difference equations of the
non-compact quantum dilogarithm at $b$ that is (i) comparable in modulus to the canonical
product $\Phi_b$ (some $C > 0$ bounds each of $\lVert\Phi_1\rVert,\ \lVert\Phi_b\rVert$ by $C$
times the other) and (ii) meromorphic on $\mathbb{C}$ and continuous wherever $\Phi_b \neq 0$.
Then $\Phi_1 = c\,\Phi_b$ for a single constant $c$, on the nonvanishing locus of $\Phi_b$.*

Here $\Phi_b$ is the modular-double product

$$
\Phi_b(z) \;=\;
\frac{\prod_{k\ge 0}\bigl(1 + e^{i\pi b^2(2k+1)}\,e^{2\pi b z}\bigr)}
     {\prod_{k\ge 0}\bigl(1 + e^{-i\pi b^{-2}(2k+1)}\,e^{2\pi z/b}\bigr)},
$$

which on the branch $\mathrm{Im} b^2 > 0$ converges and equals the Faddeev contour
integral. It is the canonical solution: it satisfies both hypotheses with $c = 1$, so the
admissible class is nonempty and the constant is genuinely pinned.

## Non-uniqueness under a single shift equation

The two first-order $q$-difference equations are invariant under multiplication by any function
elliptic for the aether lattice $\langle ib, i/b\rangle$: the shift multipliers cancel in the
ratio $\Phi_1/\Phi_b$, which is therefore doubly periodic. A nonconstant elliptic factor (a
full-lattice Weierstrass $\wp$) is thus compatible with the difference equations and would give
a second, non-proportional solution. Rigidity requires two further inputs the shift class does
not record, and one growth condition:

1. The **inversion relation** $\Phi_b(x)\Phi_b(-x) = c_0$ excludes the even part of the elliptic
   freedom algebraically.
2. **$\sigma$-unitarity** (self-duality, $\lvert\Phi_b\rvert = 1$) excludes the bar-even
   reciprocal-odd part algebraically.
3. The residual non-$\sigma$-fixed reciprocal-odd freedom is excluded **analytically**: a
   nonconstant elliptic function has poles, so it violates the boundedness the strip-growth
   comparability enforces on the ratio.

## Standing

Every analytic ingredient is established without contour integration. The product $\Phi_b$ is
meromorphic on the branch (its two infinite products are entire, as locally-uniform limits of
entire partial products), its zeros are isolated (each factor's zeros form a discrete lattice, and
the products vanish only where a factor does), and the strip growth follows from elementary
product-norm bounds. The ratio's global boundedness is derived from comparability by a
removable-singularity extension, and the two periodicity loci are dense because their complements
are countable unions of the factor lattices. The remaining hypotheses (that the *second* solution
is comparable, meromorphic, and continuous where finite) are the honest content of "the physical
$\Phi_b$ is a bona-fide meromorphic function" rather than a mathematical gap.
