**Conjecture (adelic critical-line persistence).** *Suppose the local spectral
exponents are critical-line aligned at every place --- that is, for every place
$v$ and every fundamental mode $i$, the exponent $\rho_i^{(v)}$ satisfies
$\mathrm{Re}(\rho_i^{(v)}) = \tfrac{1}{2}$. Then the global zeta function
inherits the alignment: every non-trivial zero $s$ of $\zeta(s)$ satisfies
$\mathrm{Re}(s) = \tfrac{1}{2}$.*

The antecedent is what the local half of the chain supplies. The
[Hasse--Weil bound](#thm:hasse-weil-bound) constrains the Frobenius eigenvalues
of Bring's curve to $|\alpha_i| = q^{1/2}$, and the
[spectral half-line](#cor:spectral-half-line) converts that into
$\mathrm{Re}(\rho_i) = \tfrac{1}{2}$ under the spectral coordinate
$\alpha_i = q^{\rho_i}$. That real part is well defined: the coordinate itself
is pinned only modulo $2\pi i / \log q$, but every exponent with the same
$q$-power has the same real part.

What the conjecture adds is the passage from *each place separately* to the
global object. The local alignment is a statement about one geometry at a time;
the global zeta function is assembled from all places at once, and nothing in
the local statements constrains how the assembly behaves.

**The implication carries the whole distance.** The Hasse--Weil bound holds at
every place unconditionally, and has done so since Weil proved it in 1948, while
the Riemann hypothesis has remained open throughout. Local alignment therefore
cannot by itself be close to the global statement, and this conjecture should
not be read as a small remaining step. It is stated here so that the arc's
actual claim is explicit and can be attacked, rather than resting in a
subordinate clause of the surrounding exposition.

A consequence worth recording: any construction that establishes this
implication, together with the local alignment already available, yields the
Riemann hypothesis. That is the precise sense in which the framework offers a
reduction --- and the reduction is only as strong as the conjecture above.
