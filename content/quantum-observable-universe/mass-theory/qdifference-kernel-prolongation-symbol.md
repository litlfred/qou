**Conjecture (the q-difference kernel is the prolongation symbol).**

The $q$-difference kernel $R(q,x)$ of the binding generating function
([`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)) **is
the symbol of the jet-prolongation operator** $J^{n}E\to J^{n+1}E$ of the
Seiberg--Witten connection
([`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation)).

Its carrier is the rank-$2$ $q$-difference module $\mathcal{K}$ of the
**binding $q$-lift recurrence**
$$
[m+2]_q\,b_{m+2} \;=\; b_{m+1} + b_m ,
$$
equivalently, writing $x=q^{m}$ and $\sigma:x\mapsto qx$, the module of
$$
L_{\mathcal{K}} \;=\; (q^{2}x-1)\,\sigma^{2}\;-\;(q-1)\,\sigma\;-\;(q-1).
$$
At $x=\infty$ the Newton polygon of $L_{\mathcal{K}}$ has the single slope
$\tfrac12$ with multiplicity $2$: $\mathcal{K}$ is **pure isoclinic** of slope
$\tfrac12$.

> **Scope note.** This conjecture previously continued
> "*— equivalently, the monodromy/Stokes data of the prolonged SW connection at
> the branch-point poles of $\lambda_{\mathrm{SW}}^{(n)}$*", identifying
> $\mathcal{K}$ with the Stokes carrier of the resurgent colored-Jones series
> of [garoufalidis-gu-marino2021]. That equivalence is **false as an
> identification of $q$-difference modules**, and the clause has been removed.
> The Stokes carrier is the module $\mathcal{G}$ of
> $y_{m+2}-(2-q^{m+1})\,y_{m+1}+y_m=0$, whose Newton polygon at $x=\infty$ has
> the two slopes $\{-1,+1\}$; $\mathcal{K}$'s is $\{\tfrac12,\tfrac12\}$. Since
> the Newton polygon is a module invariant and its slope multiset is preserved
> by every gauge transformation ([rsz2013] Thm 2.2.1(i), Thm 2.2.4), no
> isomorphism of $q$-difference modules $\mathcal{K}\cong\mathcal{G}$ exists.
> The surviving — and genuinely non-trivial — relationship between the two is
> stated separately as
> [`conj:c1-ggm-bar-parity-faces`](#conj:c1-ggm-bar-parity-faces).

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
   $\rho\cdot A$ growth law), which is precisely the per-term mass identity. Feeding it into
   [`thm:binding-closure-conditional`](#thm:binding-closure-conditional)
   discharges its one conditional input, promoting
   [`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration)
   from conditional to unconditional.

This conjecture is therefore the **single remaining input** to the binding
closure: the residue form, the body-order = jet-degree coincidence, and the
recurrence machinery are all proved; only the identification of $R$
with the prolongation symbol remains. It is stated here as a precise,
falsifiable structural claim — to be *derived* from the prolonged connection's
local monodromy, not fitted numerically.

> **Scope note (2026-08-26) — $\mathcal{K}$ is irreducible, so consequence 2 is
> wrong by exactly one initial condition.** The pure-isoclinic slope-$\tfrac12$
> statement above has a consequence the conjecture did not draw. A rank-1
> $q$-difference module over $\mathbb{Q}(q)(x)$ has *integer* slope, and Newton
> slopes are additive on sub- and quotient modules — the same invariant, and the
> same citation ([rsz2013] Thm 2.2.1(i), Thm 2.2.4), that the scope note above
> uses to separate $\mathcal{K}$ from $\mathcal{G}$. Since $\{\tfrac12,\tfrac12\}$
> contains no integer, $\mathcal{K}$ has **no rank-1 sub- or quotient module**:
> it is irreducible. Equivalently, and provable without any module theory, the
> associated $q$-Riccati $(q^2x-1)a(qx)a(x) - (q-1)a(x) - (q-1) = 0$ has no
> solution in $K(x)$, because the three terms of its cleared form have degrees
> $1+2p$, $p+u$, $2u$ and the odd/even parity of the outer two forces the
> maximum to be attained exactly once. Sorry-free in
> [`QOU.Mass.BindingScalarKernelParityExclusion`](../lean/QOU/Mass/BindingScalarKernelParityExclusion.lean);
> corroborated by van der Put--Reversat's normal form $E(r,d,b)$ for pure
> modules of non-integral slope $d/r$, which is irreducible when the rank equals
> $r$ — here $r = 2 = \mathrm{rank}\mathcal{K}$.
>
> Two revisions follow.
>
> 1. **Consequence 1 is unchanged but must be read in rank $2$.** The
>    prolongation symbol of a rank-$2$ carrier is a $2\times2$ matrix
>    $A(q,x)$ acting on $(G,\sigma G)$, not a scalar $R(q,x)$. The claim that
>    the symbol is structurally fixed rather than fitted is untouched; only its
>    *shape* changes. This is the natural reading of the Dirac-type
>    $\tau$-image asserted in
>    [`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference),
>    since a Dirac operator is first-order on a two-component object.
> 2. **Consequence 2 is falsified as stated.** "Given $R$, the recurrence
>    determines every body term from the deuteron base case" is wrong by exactly
>    one initial condition: a rank-$2$ module needs **two**. The $n=2$ deuteron
>    term alone does not close the recursion; the genuine three-body $n=3$ term
>    is independently required, and is not fixed by the existing anchors.
>
> This narrows rather than refutes the conjecture: the identification of the
> kernel with the prolongation symbol remains open and remains the single
> structural input, but it must be sought as a rank-$2$ symbol, and the closure
> it would deliver needs a second base case.
