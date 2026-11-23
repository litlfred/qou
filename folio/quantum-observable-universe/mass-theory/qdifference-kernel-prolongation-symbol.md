**Conjecture (the q-difference kernel is the prolongation symbol).**

The $q$-difference kernel $R(q,x)$ of the binding generating function
([The binding generating function's q-difference equation gives a depth-d recurrence](#prop:binding-genfun-qdifference)) **is
the symbol of the jet-prolongation operator** $J^{n}E\to J^{n+1}E$ of the
Seiberg--Witten connection
([Abelianisation of the MI integral on exceptional divisors](#prop:mi-sw-abelianisation)).

For jet spaces, their prolongations and the Cartan distribution, see \cite[\S1.1--1.2]{pugliese2023}. For linear $q$-difference modules, fundamental solution matrices at $0$ and $\infty$, the $q$-Borel and $q$-Laplace transforms and the resulting connection matrices, see \cite[\S2.2--2.3]{garoufalidis-wheeler-modular}.

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

Two consequences follow:

1. **$R$ is structurally fixed, not fitted.** The prolongation operator is a
   single fibre-level object; its symbol is read off the connection, not
   tuned to reproduce the terms. This is forced by the precision-floor
   obstruction (the $c_k$ information bound makes term data unable to fix $R$
   beyond low order), and it is the same fibre-level / root-of-unity
   singularity structure that governs the $\mathfrak{Q}_\beta$ ladder.
2. **It closes the binding program.** Given $R$, the recurrence of
   [The binding generating function's q-difference equation gives a depth-d recurrence](#prop:binding-genfun-qdifference)
   determines every body term from the deuteron base case (fixing the
   $\rho\cdot A$ growth law), which is precisely the per-term mass identity. Feeding it into
   [Binding closure, conditional on the per-term mass identity](#thm:binding-closure-conditional)
   discharges its one conditional input, promoting
   [Binding many-body series equals the jet-order filtration: $B(K)=\sum_n m_e\,a_D^{(n)}$](#conj:binding-manybody-eq-jet-filtration)
   from conditional to unconditional.

This conjecture is therefore the **single remaining input** to the binding
closure: the residue form, the body-order = jet-degree coincidence, and the
recurrence machinery are all proved; only the identification of $R$
with the prolongation symbol remains. It is stated here as a precise,
falsifiable structural claim — to be *derived* from the prolonged connection's
local monodromy, not fitted numerically.

> **Scope of Consequence 2 — $\mathcal{K}$ is irreducible, so the rank-1 claim is
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
> maximum to be attained exactly once. This is
> corroborated by the van der Put--Reversat classification
> \cite{vanderput-reversat2007,vanderput2006} of pure modules of non-integral
> slope $d/r$ — the normal form $E(r,d,b)$ in Bugeaud's notation
> \cite{bugeaud2011} — which is irreducible when the rank equals $r$; here
> $r = 2 = \mathrm{rank}\mathcal{K}$.
>
> Two revisions follow.
>
> 1. **Consequence 1 is unchanged but must be read in rank $2$.** The
>    prolongation symbol of a rank-$2$ carrier is a $2\times2$ matrix
>    $A(q,x)$ acting on $(G,\sigma G)$, not a scalar $R(q,x)$. The claim that
>    the symbol is structurally fixed rather than fitted is untouched; only its
>    *shape* changes. This is the natural reading of the Dirac-type
>    $\tau$-image asserted in
>    [The binding generating function's q-difference equation gives a depth-d recurrence](#prop:binding-genfun-qdifference),
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

> **Structure of the prolongation operator on
> the ramified chart, before it is constructed.** The classical lift
> $d/dz$ is excluded
> ([The classical-jet prolongation of $\lambda_{\mathrm{SW}}$ is exact for $n \ge 1$](#prop:sw-classical-jet-exactness)), and
> the residue that a period needs vanishes for it *locally*, at every branch
> point, because at $z = z_c + t^2$ the operator $d/dz = (1/2t)\,d/dt$ reads the
> $t^{-2}$ residue slot from the constant term with multiplier $(-2)+2 = 0$.
> That observation generalises exactly. On the coefficient model
> $f:\mathbb{Z}\to R$ of a local Laurent expansion, every derivative-like
> operator is a **shift operator** $(S_{k,c}f)(e) = c(e)\,f(e+k)$ — a pair
> (shift $k$, multiplier $c$), which *is* its symbol on the punctured $t$-disk,
> and symbols compose by adding shifts and multiplying multipliers along the
> shift. Two exact facts then constrain any single-shift candidate $D_q$
> (over a generic commutative
> ring):
>
> 1. **Residue.** If $D_q$ annihilates constants, $c(-k) = 0$ — as every
>    derivative does: $d/dz$, its $q$-deformation $[e+2]_q$ in either
>    $q$-integer convention, the Jackson operator $[e+1]_q$ in the local
>    coordinate, all because $[0]_q = 0$ — then for shift $k \in \{1, 2\}$ the
>    residue slot is dead at every jet level on a power-series seed such as the
>    colour-cubic branch. **No derivative-like prolongation of shift $1$ or $2$
>    can produce the binding period.** A residue needs a component with
>    $c(-k) \neq 0$: a genuine zeroth-order term, which in rank $2$ is the
>    connection-matrix datum the previous note already places the symbol in.
> 2. **Parity.** An even shift commutes with the covering monodromy
>    $t \mapsto -t$; an odd shift anti-commutes, so its jet tower's monodromy
>    eigenvalue alternates as $(-1)^n$. Carrying
>    that alternation needs an **odd** shift.
>
> So $D_q$ must have an odd shift and a non-derivative component. Both
> conditions are derived from the local geometry of $\Sigma$ and the two
> measured target properties, never from the kernel's coefficients — the
> anti-fit obligation is respected. $D_q$ is *not* constructed here; the class
> is narrowed, which is what the scoping audit's walls W1–W2 asked for first.
>
> **The sum case does not behave as the single-shift case suggests.** For a
> finite sum $\sum_k c_k\sigma^k$ the residue slot of the $n$-th jet is a sum
> over *words*, and the word (shift $1$, then shift $2$) reads $t^{-2}$ from
> $t^{-1}$ and $t^{-1}$ from $t^{+1}$, never landing on the constant slot where
> a derivative's multiplier vanishes. So two derivative-like terms of shifts
> $1$ and $2$ — classical $d/dt + (1/t)\,d/dt$, or Jackson $[e+1]_q$ with
> $[e+2]_q$ — **do** reach the residue slot: at level $n+2$ it is
> $c_1(-2)\,c_2(-1)$ times the $t^{1}$ coefficient of the level-$n$ jet, weight
> $-1$ in both cases. The
> non-derivative clause is therefore a single-shift statement. What restores it
> for sums is the residual: an operator with even part $E$ and odd part $O$
> satisfies $\mathrm{mono}(Df) = E(\mathrm{mono}\,f) - O(\mathrm{mono}\,f)$, and
> a tower carrying the full $(-1)^n$ alternation is generated by $O$ alone with
> $E$ annihilating every level — after which the single-shift prune kills the
> residue again. For derivative-like sums of shifts $\le 2$ the residue and the
> residual are mutually exclusive **level by level**: alternation demanded from
> a level $n_0$ on kills the residue from level $n_0+2$ on and leaves levels
> $2,\dots,n_0+1$ alive. The
> distinction matters, because the Door-v alternation of the carrier
> $\mathcal{G}$ cannot hold at every level — while $2-q^{m+1}>0$ no solution flips at two
> consecutive pairs, so at the substrate value
> the alternation is absent for $m \le 5$ and persistent only from
> $m \approx 11$ on. The conclusion above therefore stands for sums only
> *above* that window; at the low body orders a mixed-shift $D_q$ built from
> derivatives alone remains admissible by the two target properties, and the
> non-derivative clause is not forced by them there.
>
> **The kernel is a recurrence across jet levels, and on that axis it forces
> the non-derivative clause too.** In $L_{\mathcal{K}}$ the variable is
> $x = q^{m}$ with $m$ the body order, which
> [The Seiberg–Witten period is an algebraic residue sum](#prop:sw-period-residue-sum) identifies with
> the jet degree; so $\sigma$ is the step from one jet level to the next, and
> $L_{\mathcal{K}}$ is the second-order recurrence that the level-indexed
> residues $r_{n} = (D_{q}^{n}X)_{t^{-2}}$ of the prolongation tower must
> satisfy — never $D_{q}$ itself, which is first-order in the level. On a
> power-series seed $r_{0} = 0$ for every operator, so the residue tower cannot
> coincide with a carrier whose first term is nonzero (the involution-number
> carrier has $b_{0} = b_{1} = 1$): the recurrence is demanded from a level on,
> and a level-$n_{0}$ C1 sequence is fixed by its two values at $n_{0}$ and
> $n_{0}+1$ — the two base cases of the scope note above. For the admissible
> two-term operator $r_{1} = c_{2}(-2)\,a_{0}$, the branch value read through
> the shift-$2$ weight at the residue slot; a derivative-like shift-$2$ term has
> $c_{2}(-2) = 0$, so $r_{0} = r_{1} = 0$ and a C1 residue tower from level $0$
> is identically zero. For a derivative-only tower the recurrence from level
> $2$ is *equivalent* to the index-shifted recurrence
> $[m+4]_{q}\,s_{m+2} = s_{m+1} + s_{m}$ on the tower's $t^{1}$-coefficients
> $s_{m} = (D_{q}^{m}X)_{t^{1}}$, since $r_{m+2} = c_{1}(-2)c_{2}(-1)\,s_{m}$;
> each level's constraint reaches one new seed coefficient and none of them
> reads the branch value $a_{0}$ (for
> $q$ not a root of unity). On the actual seed — the branch-point
> expansion of the colour cubic at its simple ramification point — neither
> the Jackson nor the $q$-derivative tower, in either $q$-integer convention
> and on either sheet, satisfies that recurrence at any tested $q$: the
> defect is of order one relative to the residues themselves, not a
> precision artefact. And with the weights left free, each level introduces
> at least four new weight values against one constraint, so the recurrence
> constrains nothing until the weights are supplied by the geometry. Both
> statements are scope-(a): they concern these two candidates on this seed,
> and the two-term derivative-only class, respectively. The weights cannot be
> supplied by a $q$-connection on the base either: the colour cubic is
> irreducible over $K(z)$ for every field $K$ of characteristic zero
>, so no sheet is a rational
> function of $z$; each sheet is algebraic, hence D-finite; and a rational
> rank-$3$ $q$-difference system in $z \mapsto \lambda z$ with the sheets as
> solutions would make a sheet $q$-holonomic, which together with D-finiteness
> forces rationality (Bézivin, Ramis; Schäfke–Singer). So a rational
> $q$-connection on the $z$-line with the sheets as flat sections does not
> exist — scope (b), the cited theorem being the invariant. Localising at the
> ramification point does not evade this. In the local coordinate $t$, with
> $z = z_{c} + t^{2}$, the sheets are power series algebraic over $K(t)$ and so
> still D-finite; and they are still not rational, because $t^{2} = z - z_{c}$
> makes $K(t)/K(z)$ quadratic while an irreducible cubic has no root of degree
> at most two. The
> same theorem therefore excludes the local $q$-dilation as well, and what
> survives is an operator whose coefficients are not rational in a coordinate,
> or one defined on the curve rather than on a coordinate line.
>
> Two earlier readings of the same kernel took $\sigma$ to be a shift in the
> $t$-exponent of a single jet — the unit $t$-shift with $x = q^{e}$, or the
> $t$-shift by two on the double cover. That is the special case in which the
> level and the exponent lock, $r_{n} = c^{n}a_{n-2}$ for a constant-weight
> pure shift-$1$ tower, not the conjecture's reading. What was proved there
> stands as mathematics about those $t$-operators: neither can be written as a
> sum of derivative-like terms, because each carries a zeroth-order term
> $-(q-1)$ that does not annihilate the constant seed
>, and neither can carry the $(-1)^{m}$
> alternation of the preceding note on a nonzero tower — on the double cover
> because a monodromy-commuting operator transports the character unchanged,
> under the unit shift because the even part would have to annihilate both a
> jet and its odd image, and those two recurrences differ by
> $q^{e+1}(q-1)Y_{e+2}$. Read on the
> correct axis those facts say nothing about $D_{q}$, and the
> "$\sigma \leftrightarrow t$-shift dictionary" they posed as wall W2 is not a
> question the conjecture asks.

> **Branch-locus obstruction on the curve — an operator on $\Sigma$ does not evade the
> exclusion either, when its base map is a dilation.** The two preceding
> exclusions constrain the *coefficient field*, so an operator living on
> $\Sigma$ rather than on a coordinate line is not reached by them. It is
> reached by the branch locus. An automorphism of $\Sigma$ covering the base
> dilation $z \mapsto \lambda z$ is an isomorphism of coverings up to that base
> automorphism, so it carries ramification points to ramification points and
> therefore permutes the six finite branch points — the zeros of the branch
> sextic $D(z) = 16z^{6} + 24z^{5} + 35z^{4} + 50z^{3} + 35z^{2} + 24z + 16$,
> which is squarefree with $D(0) = 16 \neq 0$. Equal root multisets means
> $D(\lambda z) = c\,D(z)$, and then two coefficients settle it: the constant
> term gives $16 = 16c$, so $c = 1$, and the linear term gives $24\lambda = 24$,
> so $\lambda = 1$ (over a generic
> characteristic-zero field). **Only the identity dilation lifts to $\Sigma$**,
> for every $\lambda$ and at every $q$ — scope (b), the invariant being the
> sextic's own coefficients rather than a cited analytic theorem, so this
> covers the root-of-unity case that the rationality theorem does not. The
> substrate asks for $\lambda = q_{0}^{2} \approx 1.2321$, which is excluded
> both by that identity and by the weaker bound $\lambda^{6} = 1$ that the
> product of the roots alone would give. This does **not** touch a
> $q$-difference operator whose base map is not a dilation, nor the fibre
> monodromy route, which acts on the fibre and is untouched by any statement
> about maps of the $z$-line.
