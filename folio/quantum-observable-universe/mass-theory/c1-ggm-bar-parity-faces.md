**Conjecture (bar-parity conjugate faces).**

Let $\mathcal{K}$ be the rank-$2$ $q$-difference module of the binding $q$-lift
recurrence
$[m+2]_q\,b_{m+2}=b_{m+1}+b_m$
([The q-difference kernel R is the jet-prolongation symbol, carried by the binding q-lift module](#conj:qdifference-kernel-prolongation-symbol)),
and let $\mathcal{G}$ be the module of
$$
y_{m+2}-(2-q^{m+1})\,y_{m+1}+y_m \;=\; 0,
$$
the Stokes carrier of the resurgent colored-Jones series of
[garoufalidis-gu-marino2021]. Their Newton polygons at $x=\infty$ are
$\{\tfrac12,\tfrac12\}$ and $\{-1,+1\}$, so $\mathcal{K}\not\cong\mathcal{G}$ as
$q$-difference modules. The conjecture is that they are nevertheless related,
and by exactly one twist.

1. **The tensor square has the right graded module.**
   $\mathcal{K}^{\otimes 2}$ is anisoclinic with slopes $\{+1,0,-1\}\supset
   \{+1,-1\}$. Doubling the slope $\tfrac12$ produces the integral slopes the
   rank-$2$ comparison could not reach, which is why the Newton-polygon
   obstruction does not apply to it.
2. **No Stokes obstruction on that piece.** On the $\{+1,-1\}$ graded part the
   unipotent part of the connecting datum is trivial and the connecting matrix
   is constant, so $\mathcal{K}^{\otimes 2}$ and $\mathcal{G}$ agree as graded
   modules *with* their Stokes data.
3. **One residual, and it is a parity.** The sole difference is the diagonal
   $\mathbb{Z}/2$ character $(-1)^{m}$: the growing solution of $\mathcal{G}$
   alternates in sign, $y_{m+1}\sim -q^{m}y_m$, while the squares
   $f_+^{2},f_-^{2}$ built from $\mathcal{K}$ are non-negative and provably
   cannot. This is the framework's bar-even / bar-odd ($\cosh$ / $\sinh$)
   distinction: $\mathcal{K}$ is the bar-even face and $\mathcal{G}$ the
   bar-odd one.

**The obstruction half is proved.** No combination
$\alpha p_n+\beta q_n$ with $\alpha,\beta\ge 0$ and $p,q\ge 0$ can equal a
sequence with a single consecutive sign flip: the left side lies in the
non-negative cone. Hence the squares cannot reproduce the alternating solution
without a sign twist, and the twist is forced rather than fitted.

**What is conjectural** is the positive half — that after the $(-1)^{m}$ twist
the agreement is *exact*, so that the parity is the whole difference and not
merely a difference. Items 1--3 are established at probe level; the
exact-coefficient identity is open.

**One reading of the positive half is excluded.** The twist inverts *every*
consecutive-pair sign, $z_mz_{m+1}=-y_my_{m+1}$ with $z_m=(-1)^my_m$, not only
the alternating ones. It can therefore clear the non-negativity obstruction only
for a target that alternates at *every* consecutive pair, and no solution of
$\mathcal{G}$ does: for $m+1<\log 2/\log q$ the coefficient $2-q^{m+1}$ is
positive, and while it is positive a sign flip is always followed by a
same-sign pair, since $y_{m+2}y_{m+1} = (2-q^{m+1})\,y_{m+1}^2 - y_m y_{m+1} > 0$
whenever $y_m y_{m+1} < 0$
(this holds over any
ordered field). The recurrence *is* oscillatory there — its solutions do change
sign inside the window — but never
at two consecutive pairs, and that is what the argument needs. So the untwisted
sequence has same-sign consecutive pairs in that window, the twisted sequence
acquires flips exactly there, and the obstruction fires on it too. At the
substrate value the window is $m \le 5$, and the strict alternation of the
growing solution becomes persistent only later, at an index that depends on the
initial data ($m \approx 11$–$14$ across six generic choices, measured numerically).

Consequently the residual claim must be read **at the level of modules**, up to
a gauge transformation over the $q$-difference field — not as the assertion that
$(-1)^{m}z$ is a non-negative combination of $f_+^{2}$ and $f_-^{2}$. That
scalar reading is excluded by the same non-negativity invariant that supplies
the obstruction. The module-level statement is untouched by this and remains
what is conjectured.

**Where median-resummation theorems would enter, and the check they need.**
McSpirit and Rolen prove that cusp forms of integral or half-integral weight,
Eichler integrals of such cusp forms, and two periodic functions attached to
weight-$\tfrac12$ Maass and Eisenstein data are holomorphic quantum modular
forms whose modular obstruction $h_\gamma$ is a Borel--Laplace sum of the
asymptotic series at the cusp $\gamma^{-1}(i\infty)$ \cite[\S1.1, Thm.~1.5]{mcspirit-rolen2025};
for the half-integral weight Eichler integrals and the two periodic functions,
the median resummation of the asymptotic series recovers the function
\cite[Cor.~1.6]{mcspirit-rolen2025}. Those results apply to $\mathcal{G}$ or
$\mathcal{K}$ only after their solutions are shown to lie in one of the six
classes of Thm.~1.5. Neither module is presented here in that form: both are
given by $q$-difference recurrences and their Newton polygons, not as Eichler
integrals of a named cusp form. Until that membership is established, the
connection to these theorems is thematic, and no step of items 1--3 uses them.
