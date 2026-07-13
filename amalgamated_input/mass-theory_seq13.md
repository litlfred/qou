<!-- FILE_START: qdifference-kernel-prolongation-symbol.md -->
**Conjecture (the q-difference kernel is the prolongation symbol).**

The $q$-difference kernel $R(q,x)$ of the binding generating function
([`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)) **is
the symbol of the jet-prolongation operator** $J^{n}E\to J^{n+1}E$ of the
Seiberg--Witten connection
([`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation)) — equivalently, the
monodromy/Stokes data of the prolonged SW connection at the branch-point poles
of $\lambda_{\mathrm{SW}}^{(n)}$ on $\mathcal{S}_c\cong\mathbb{P}^1$.

Two consequences follow:

1. **$R$ is structurally fixed, not fitted.** The prolongation operator is a
   single fibre-level object; its symbol is read off the connection, not
   tuned to reproduce the terms. This is forced by the precision-floor
   obstruction (the $c_k$ information bound makes term data unable to fix $R$
   beyond low order), and it is the same fibre-level / root-of-unity
   singularity structure that governs the $\mathfrak{Q}_\beta$ ladder.
2. **It closes the binding program.** Given $R$, the recurrence of
   [`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)
   determines every body term from the deuteron base case (fixing the
   $\rho\cdot A$ growth law), which is precisely the per-term mass identity
   (B). Feeding (B) into
   [`thm:binding-closure-conditional`](#thm:binding-closure-conditional)
   discharges its one conditional input, promoting
   [`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration)
   from conditional to unconditional.

This conjecture is therefore the **single keystone** of the step-9b binding
closure: the residue form (D), the body-order = jet-degree coincidence (C), and
the recurrence machinery (L3) are all proved; only the identification of $R$
with the prolongation symbol remains. It is stated here as a precise,
falsifiable structural claim — to be *derived* from the prolonged connection's
local monodromy, not searched canonical.
<!-- FILE_END: qdifference-kernel-prolongation-symbol.md -->

<!-- FILE_START: prolonged-periods-fixed-depth.md -->
The prolonged Seiberg--Witten periods $a_D^{(n)} = \varphi(M^n v_0)$ are orbits of
the jet-prolongation operator $M$
([`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation)) acting on the
Gauss--Manin period space $V$ of the SW family over Bring's surface. Since $V$
is **finite-rank** — it is the de Rham cohomology of the family, $\dim V \leq 2g
= 8$ for the genus-$4$ Bring curve — the operator $M$ satisfies its
characteristic polynomial (Cayley--Hamilton):
$M^d = \sum_{j<d} c_j\,M^j$ with $d \leq \operatorname{rank} V$ and $c_j$ the
characteristic-polynomial coefficients. Therefore the operator powers — and
hence the periods — satisfy the depth-$d$ linear recurrence

$$
M^{\,n+d} = \sum_{j<d} c_j\,M^{\,n+j},
\qquad
a_D^{(n+d)} = \sum_{j<d} c_j\,a_D^{(n+j)},
$$

with **$n$-independent** kernel $c$, for every $n$.

This **proves the existence half** of
[`conj:qdifference-kernel-prolongation-symbol`](#conj:qdifference-kernel-prolongation-symbol):
a fixed-depth recurrence on the prolonged periods *necessarily* exists, with
depth bounded by the rank of the Gauss--Manin local system. What remains is the
**identification half** — that $d$ and the kernel $c$ are *exactly* the Bring
Picard--Fuchs operator (so the kernel is the prolongation symbol, not a generic recurrence). That is fixed by computing the SW connection's local monodromy
at the branch points and matching it against the residue weights $a_D^{(n)}$
(the consistency test of the keystone workplan, gated on the per-knot weights at
$n = 2, 3$).

The operator recurrence is verified sorry-free
([`QOU.Mass.prolongation_fixed_depth_recurrence`](#prop:prolonged-periods-fixed-depth));
the finite-rank premise (Gauss--Manin / Cayley--Hamilton) is the cited
structural input, and the scalar period recurrence follows by applying the
linear functional $\varphi(\,\cdot\,v_0)$ to both sides.
<!-- FILE_END: prolonged-periods-fixed-depth.md -->

<!-- FILE_START: sl2-prolongation-recurrence.md -->
The recurrence on the prolonged Seiberg--Witten periods has depth $2$
([`prop:prolonged-periods-fixed-depth`](#prop:prolonged-periods-fixed-depth)
together with the $S_5$-Hodge count $H^1 = 2W$): the $2\times 2$ prolongation
operator $B$ on the Hodge multiplicity plane carries the whole kernel,
$R = x^2 - \operatorname{tr}(B)\,x + \det(B)$.

The Gauss--Manin monodromy **preserves the principal polarisation** of the
curve — the cup-product symplectic form on $H^1$, which restricts
non-degenerately to the rank-$2$ $W$-isotypic Hodge plane (the polarisation is
$S_5$-invariant). Hence $B \in \mathrm{Sp}(2) = \mathrm{SL}_2$ and

$$
\boxed{\;\det B = 1\;}
\qquad\Longrightarrow\qquad
R = x^2 - \tau\,x + 1,\quad \tau := \operatorname{tr} B,
$$

consequently the prolonged periods satisfy the one-parameter "Lucas/Chebyshev" recurrence

$$
a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)} .
$$

The kernel $R$ is therefore reduced to the **single** number $\tau = \operatorname{tr} B$,
the trace of the prolongation monodromy. The non-hyperbolic torus sector
confirms the form: its recurrence is $x^2 - 2\cosh(2\eta_0)\,x + 1$, i.e.
$\det = 1$ with $\tau = 2\cosh(2\eta_0)$. For the hyperbolic binding sector
$\tau = 2\cosh\theta$ for a prolongation rapidity $\theta$; pinning $\theta$ is
the last open number of the keystone, and is solvable from three residue
weights via $\tau = (a_D^{(2)} + a_D^{(4)})/a_D^{(3)}$.

The Lean witness
[`QOU.Mass.sl2_prolongation_recurrence`](#prop:sl2-prolongation-recurrence)
proves the recurrence form from the $\det B = 1$ Cayley--Hamilton relation,
sorry-free.
<!-- FILE_END: sl2-prolongation-recurrence.md -->

<!-- FILE_START: sl2-period-conserved-quantity.md -->
The one-parameter recurrence
([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence))

$$
a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)},
\qquad \tau = \operatorname{tr} B,\ \det B = 1,
$$

on the prolonged Seiberg--Witten periods admits a **conserved first integral** —
the discrete energy of the Lucas/Chebyshev orbit, equivalently the cup-product
symplectic form evaluated on consecutive periods:

$$
\boxed{\;
H_n := \bigl(a_D^{(n+1)}\bigr)^2 - \tau\,a_D^{(n+1)}a_D^{(n)} + \bigl(a_D^{(n)}\bigr)^2
\quad\text{satisfies}\quad H_{n+1} = H_n
\;}
$$

so $H_n = H_0$ for every $n$. The invariant exists because $\det B = 1$: it is the
quadratic form fixed by $B \in \mathrm{SL}_2$ acting on $(a_D^{(n)}, a_D^{(n+1)})$.

**Fork consequence (the depth-$2$ hypothesis is the $n\le 4$ germ).** A genuine
depth-$2$, $\det = 1$ orbit keeps $H_n$ constant; in the hyperbolic case
$\tau = 2\cosh\theta > 2$ the conic $H_n = H_0$ forces the ratio
$a_D^{(n+1)}/a_D^{(n)}$ to a **fixed** limit $\lambda_+ = e^{\theta}$ (geometric
growth). But the true prolonged period is the residue sum
([`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum))
$a_D^{(n)} = \sum_{\lambda} \dim_q$, a per-block Wedderburn quantum-dimension sum
that grows **factorially** (super-exponentially), so its ratio
$a_D^{(n+1)}/a_D^{(n)}$ is unbounded and $H_n \to \infty$. A factorial sequence
conserves no first integral, hence satisfies **no** depth-$2$ recurrence: the
$\tau$ fitted from three residue weights
$\tau = (a_D^{(2)} + a_D^{(4)})/a_D^{(3)}$ is an effective germ matching $n\le 4$,
not the period recurrence. The exact prolongation kernel is the q-Bessel-class
$q$-difference operator of the super-exponential residue sum
([`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)), not a
$2\times 2$ Cayley--Hamilton relation.

The Lean witnesses
[`QOU.Mass.sl2Invariant_succ`](#prop:sl2-period-conserved-quantity) and
[`QOU.Mass.sl2Invariant_eq_zeroth`](#prop:sl2-period-conserved-quantity) prove
$H_{n+1} = H_n$ and $H_n = H_0$ over a generic commutative ring, sorry-free; the
single-step identity is closed by `ring` after substituting the recurrence.
<!-- FILE_END: sl2-period-conserved-quantity.md -->

