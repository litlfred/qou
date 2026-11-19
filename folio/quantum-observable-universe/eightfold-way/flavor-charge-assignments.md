The $A_2$ weight lattice of [the $A_2$
proposition](#prop:a2-from-three-strands)
assigns two quantum numbers to each state: the third component of
isospin $I_3$ and the hypercharge $Y$, related to the fundamental
weights by
$$
  I_3 = \tfrac{1}{2}(\lambda_1 - \lambda_2),
  \qquad
  Y   = \tfrac{1}{3}(\lambda_1 + \lambda_2).
$$
The electric charge is then the Gell-Mann--Nishijima relation
$Q = I_3 + Y/2$.

**Derived quantity: isospin $I_3$.**
The writhe-to-isospin map $w \mapsto I_3$ is derived in the framework
without fitted parameters.  Over the nucleon doublet, the proton braid
$\mathfrak{p}$ and neutron braid $\mathfrak{n}$ carry writhes whose
difference reproduces $\Delta I_3 = 1$ scale-free.  This identifies $I_3$
as the *writhe coordinate* on the $A_2$ weight lattice.

**Open quantity: hypercharge $Y$.**
The writhe map is falsified as a hypercharge assignment: the proton and
neutron share $Y = +1$ while their writhes differ.  The framework
therefore requires a second crossing invariant, independent of the
writhe, to instantiate $Y$.

The candidate direction, recorded without endorsement, is the
*ribbon-framing twist*.  In the categorical braid representation,
each strand carries a framing datum whose total $T(t)$ is independent
of the crossing word (hence independent of the writhe $w$).  The
candidate hypercharge is
$$
  Y_t = 2\bigl(Q_{\mathrm{twist}} - I_3\bigr),
  \qquad
  Q_{\mathrm{twist}} = \frac{T(t)}{3},
$$
where $T(t)/3$ is the colour-tube charge quantum of the quark picture
(the helon-model normalisation \cite{bilson-thompson2005}).  The
Gell-Mann--Nishijima relation holds by construction *if and only if*
$Q_{\mathrm{twist}} = Q$ against the crossing-derived Coulomb charge
$Q = w/2$ --- a falsifiable consistency condition, not a definition.

**Status and batteries.**
Neither the candidate nor any alternative has been wired.  Any hypercharge
proposal must pass two batteries before instantiating the class:

1. **Gell-Mann--Nishijima consistency:** $Q = I_3 + Y/2$ must hold
   against the independently derived $Q$ and $I_3$ on the nucleon doublet,
   without tuning a coupling.
2. **First-generation spectrum:** The $Y$ values of $u, d, e^-,
   \nu_e$ must reproduce $\{+1/3, +1/3, -1, -1\}$ (left-handed) and
   $\{+4/3, -2/3, -2, 0\}$ (right-handed), satisfying the $\mathbb{Z}_6$
   compatibility relations \cite{baez-huerta2010}.

A candidate requiring a fitted scale to pass either battery is a fit,
not a derivation, and does not instantiate this class.

**Enumeration result, and why it carries no corroboration.**
The battery has been run over all $10{,}000$ helon-style assignments (3
strands per fermion, per-strand twist in $\{-1, 0, +1\}$), of which $4$
survive. That ratio must not be read as a $2500\!:\!1$ filter: the battery
collapses to a single linear equation per flavour, and the surviving count
is multiset counting:

1. **The spectrum battery is exactly $T = 3Q$.** Both the candidate
   $Y_t = 2(Q_{\mathrm{twist}} - I_3)$ and the target $Y = 2(Q - I_3)$ carry
   the same $-2I_3$, which cancels. What remains is
   $Q_{\mathrm{twist}} = Q$ --- the defining equation of
   $Q_{\mathrm{twist}}$, not a test of it. The battery constrains nothing
   about isospin.
2. **The nucleon-doublet check is entailed**, by charge additivity
   alone: $T_{\mathfrak{p}} = 2T_u + T_d = 3(2Q_u + Q_d)$ follows from
   $T = 3Q$ on the quarks, so no surviving assignment can fail it. As
   implemented it also states one condition twice --- its second clause
   $2(T_{\mathfrak{p}}/3 - 1/2) = 1$ clears to $T_{\mathfrak{p}} = 3$, which
   is its own first clause.
3. **The $\mathbb{Z}_6$ condition is not a filter.** In
   `strand_twist_y_battery.py` it is a function of the
   Standard-Model table alone and never sees the candidate assignment; it
   runs as an input assertion and cannot exclude any multiset.

So each flavour is filtered independently by one equation, and $4 = 1
\times 2 \times 2 \times 1$ counts the multisets of three twists from
$\{-1,0,+1\}$ with the required totals $3Q = (2, -1, 0, -3)$. The $u$-quark
twist $\{0,1,1\}$ and the electron twist $\{-1,-1,-1\}$ are the two totals
admitting a single multiset --- a fact about writing $2$ and $-3$ as a sum
of three elements of $\{-1,0,+1\}$, not about the framework; the $d$-quark
and neutrino each admit two. Passing the battery is therefore equivalent to
choosing $t$ with $\sum_i t_i = 3Q$, which is always possible.

The open content is unchanged and is the whole question: whether the twist
multisets are *forced* by the framework's braid words rather than
only consistent with them. See
`strand-twist-y-battery.witness.json`.

**A derived-twist repair, tested and refuted (scope-(a)).**
The defect above is that $t$ is a free label. The natural repair is to
replace it with the *canonical* twist of the ribbon category --- on a
simple object the twist acts by a scalar whose exponent is the content sum
$c(\lambda) = \sum_{(i,j) \in \lambda} (j - i)$, a derived per-block
integer. Taking $Q = c(\lambda)/3$ is parameter-free. It does not work: at
$n = 3$ the content sums are $\{3, 0, -3\}$, giving the *integer*
charges $\{+1, 0, -1\}$ with no third-integer charge at all, and no
$n \le 8$ yields both quark charges $\{+2/3, -1/3\}$
(`ribbon_twist_charge_quantum_probe.py`). This is scope-(a) for
the plain content-sum reading, not an exclusion of the ribbon route: other
normalisations remain untested.
