**Conjecture (MI abelianisation at algebraic poles).**
*At each $\tau_{\mathrm{arch}}$-image of a $q$-Pochhammer denominator
zero, the nonabelian multiplicative integral
([mass identity](#def\:mass-identity))
trivialises and abelianises: the gauge connection reduces strictly
to its Cartan component and becomes the prolonged Seiberg–Witten
differential $\lambda_{\mathrm{SW}}^{(n)} = X\, dz$.*

Equivalently, for each algebraic denominator zero $x = q_0^{-k}$ of
$\Phi_n(x; q_0)$
([q-Pochhammer partial product](#def\:q-pochhammer-partial-product)),
the matched complex critical point $z_c = \tau_{\mathrm{arch}}(q_0^{-k})$
sits on an exceptional divisor $\mathcal{S}_c \cong
\mathbb{P}^1(\mathbb{C})$
([Bring's surface smoothness](#rem\:brings-smoothness)),
and the restriction of the MI to $\mathcal{S}_c$ collapses to the
$n$-th prolonged SW period:

$$
  \mathrm{MI}\!\!\int_{\mathcal{S}_c}\bigl(\nabla_A q,\, L \wedge F^+\bigr)
  \,\Big|_{J^n}
  \;=\;
  \oint_{\mathcal{S}_c} \lambda_{\mathrm{SW}}^{(n)}
  \;=\;
  \bigl|a_D^{(n)}\bigr|.
$$

## Why this matters

The conjecture pins down **where** the abelianisation occurs. The
existing
[MI–SW abelianisation](#prop\:mi-sw-abelianisation)
proposition shows that the MI collapses to the SW prolongation on
each exceptional divisor; the existing
[MI–SW abelianisation Cartan](#lem\:mi-sw-abelianisation-cartan)
lemma identifies the trivialised connection with its Cartan
component. Neither block specifies which exceptional divisors are
visited by a given categorical state $T_w$.

The present conjecture supplies the missing address: the visited
divisors are **exactly** the $\tau_{\mathrm{arch}}$-images of the
algebraic denominator zeros of the $q$-Pochhammer partial product
attached to $T_w$. Combined with
[denominator zeros = SW critical points](#conj\:denominator-zeros-as-sw-critical-points),
this gives the algebraic-side prescription for the abelianisation
loci.

## Mechanism

Two facts conspire:

1. **Topological**: $\pi_1(\mathrm{SU}(2)) = 0$. Over each exceptional
   divisor $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$ (a 2-sphere
   topologically), every $\mathrm{SU}(2)$-bundle is trivialisable.
   The nonabelian connection therefore admits a global gauge in which
   it is constant on $\mathcal{S}_c$.

2. **Algebraic**: :refterm[quantum flatness]{#quantum-flatness} at the pole. The denominator
   factor $(1 - x q^k) \to 0$ at $x = q^{-k}$ forces the
   corresponding categorical curvature contribution to lie in the
   weight-$0$ sector of the Hecke representation. Under the gauge
   from item 1, the connection's Cartan component is the only
   surviving piece, and it is the prolonged SW differential
   $\lambda_{\mathrm{SW}}^{(n)} = X\, dz$.

The conjecture asserts that the two facts compose: at every algebraic
pole, item 1 gives the trivialisation gauge and item 2 selects the
Cartan component within it.

## Proof sketch (modulo upstream)

Assume
([MI–SW abelianisation](#prop\:mi-sw-abelianisation)),
([MI–SW abelianisation Cartan](#lem\:mi-sw-abelianisation-cartan)),
and
([denominator zeros = SW critical points](#conj\:denominator-zeros-as-sw-critical-points)).

1. **Locus.** By
   ([denominator zeros = SW critical points](#conj\:denominator-zeros-as-sw-critical-points)),
   each algebraic zero $x = q_0^{-k}$ lifts under
   $\tau_{\mathrm{arch}}$ to a critical point $z_c$ of $\Delta(z)$,
   and each $z_c$ sits on an exceptional divisor $\mathcal{S}_c$
   ([Bring's surface smoothness](#rem\:brings-smoothness)).

2. **Trivialisation.** By
   ([MI–SW abelianisation](#prop\:mi-sw-abelianisation)),
   the MI restricted to any exceptional divisor abelianises to the
   prolonged SW period; the gauge witness is
   $\pi_1(\mathrm{SU}(2)) = 0$.

3. **Cartan reduction.** By
   ([MI–SW abelianisation Cartan](#lem\:mi-sw-abelianisation-cartan)),
   the surviving connection is its Cartan component
   $X\, dz = \lambda_{\mathrm{SW}}^{(n)}$.

4. **Algebraic-side identification.** Step 1 picks out the divisors;
   Steps 2–3 give the abelianisation on each picked divisor; hence
   the MI evaluated on the $\tau_{\mathrm{arch}}$-image of the
   algebraic poles is the prolonged SW period. $\square$

## Status

Stated conditional on the three upstream blocks. The Lean
formulation `QOU.PicardLefschetz.abelianisation_at_algebraic_poles`
is a class instance.
