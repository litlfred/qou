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
as the *writhe coordinate* on the $A_2$ weight lattice.  These writhes are those of
the inter-nucleon arc, $w(\mathfrak{p}) = +1$ and $w(\mathfrak{n}) = -1$.
The ruled nucleon word $(\sigma_i\sigma_{i+1}^{-1})^3$ is the same for
both nucleons and has writhe $0$, so on the word itself the writhe does not
separate them; there $I_3$ is the weight of the up and down strand labels.

**Open quantity: hypercharge $Y$.**
The proton and neutron share $Y = +1$ while their writhes differ. This
falsifies every *injective* map from the writhe to $Y$, in particular the
linear map $Y = c\,w$ that a framing phase $q^{w c}$ would give. It does not
falsify every function of the writhe: a non-injective one such as
$Y = w^2/4$ passes the proton–neutron test. What does force a second
invariant is the charge side. The quark charges are not a function of the
writhe (the anti-up and down crossings share the writhe $-1$ but carry
$-\tfrac{2}{3}$ and $-\tfrac{1}{3}$; see [the Coulomb-charge
definition](#def:coulomb-charge)), and if both $Q$ and $I_3$ were
functions of the writhe then so would be $Y = 2(Q - I_3)$. Since $I_3$ is
read here as the writhe coordinate, a hypercharge independent of the
writhe requires a charge $Q$ that is not the halved writhe. The framework
therefore requires a second invariant, independent of the writhe, to
instantiate $Y$.

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
(the helon-model normalisation of Sundance O. Bilson-Thompson \cite{bilson-thompson2005}; in the braided-ribbon-graph formulation of Sundance O. Bilson-Thompson, Fotini Markopoulou, and Lee Smolin \cite[§I, §V]{bilsonthompson2007}, strand twists define noiseless $U(1)$-charged subsystems conserved under local evolution moves, without claiming to derive the Standard Model interactions).  The
Gell-Mann--Nishijima relation holds by construction *if and only if*
$Q_{\mathrm{twist}} = Q$ against an independently derived electric charge
$Q$ --- a falsifiable consistency condition. The halved
writhe of [the Coulomb-charge definition](#def:coulomb-charge) cannot play
that role, since it is not the electric charge, so the condition has no
derived right-hand side yet.

**Status and batteries.**
Neither the candidate nor any alternative has been wired.  Any hypercharge
proposal must pass two batteries before instantiating the class:

1. **Gell-Mann--Nishijima consistency:** $Q = I_3 + Y/2$ must hold
   against an independently derived $Q$ and $I_3$ on the nucleon doublet,
   without tuning a coupling. No derived $Q$ exists yet, so this battery
   cannot currently be run against anything but the Standard-Model table.
2. **First-generation spectrum:** The $Y$ values of $u, d, e^-,
   \nu_e$ must reproduce $\{+1/3, +1/3, -1, -1\}$ (left-handed) and
   $\{+4/3, -2/3, -2, 0\}$ (right-handed), satisfying the $\mathbb{Z}_6$
   compatibility relations of John C. Baez and John Huerta \cite{baez-huerta2010}.

A candidate requiring a fitted scale to pass either battery is a fit,
not a derivation, and does not instantiate this class.

**Enumeration result, and why it carries no corroboration.**
The battery has been run over all $10{,}000$ helon-style assignments (3
strands per fermion, per-strand twist in $\{-1, 0, +1\}$), of which $4$
survive. That ratio must not be read as a $2500\!:\!1$ filter: the battery
collapses to a single linear equation per flavour, and the surviving count
is multiset counting. The following are proved:

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
3. **The $\mathbb{Z}_6$ condition is not a filter.** As
   implemented it is a function of the
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
only consistent with them.

**A derived-twist repair, tested and refuted (scope-(a)).**
The defect above is that $t$ is a free label. The natural repair is to
replace it with the *canonical* twist of the ribbon category --- on a
simple object the twist acts by a scalar whose exponent is the content sum
$c(\lambda) = \sum_{(i,j) \in \lambda} (j - i)$, a derived per-block
integer. Taking $Q = c(\lambda)/3$ is parameter-free. It does not work: at
$n = 3$ the content sums are $\{3, 0, -3\}$, giving the *integer*
charges $\{+1, 0, -1\}$ with no third-integer charge at all, and no
$n \le 8$ yields both quark charges $\{+2/3, -1/3\}$
. This is scope-(a) for
the plain content-sum reading, not an exclusion of the ribbon route: other
normalisations remain untested.

**What the hypercharge must supply for a Coulomb term.**
On the nucleon doublet lepton number vanishes, so the Gell-Mann--Nishijima
hypercharge equals the baryon number, $Y = B = 1$ for both proton and
neutron. Per strand this is $B = \tfrac{1}{3}$, and the strand charge
$Q = T_3 + B/2$ gives $u \mapsto \tfrac{2}{3}$, $d \mapsto -\tfrac{1}{3}$
and a three-strand block with $a$ up strands the charge $a - 1$. So on the
baryon sector the content of $Y$ is a derived reading of $B$; the
non-strange identification $Y = B$ with the Milnor triple linking number of
the three colour tubes is a conjecture with no instance, and the lepton
sector further needs a lepton number for $Y = B - L$.

Hypercharge alone does not give a Coulomb pair term. The exchange of the
unbroken neutral bosons between two particles has charge factor
$g^2\,T_3T_3' + g'^2\,(Y/2)(Y'/2)$, with no $T_3 \otimes Y$ cross term. On two
three-quark blocks ($Y = 1$, $T_3 = \pm\tfrac{1}{2}$) it takes the same value
on the proton pair and the neutron pair: it is an isospin coupling with no
Coulomb part. It splits identically as

$$
  g^2\,T_3T_3' + g'^2\,\tfrac{Y}{2}\tfrac{Y'}{2}
  = e^2\,QQ' + g_Z^2\,(T_3 - s^2 Q)(T_3' - s^2 Q'),
$$

with $e^2 = g^2g'^2/(g^2+g'^2)$, $s^2 = g'^2/(g^2+g'^2)$ and
$g_Z^2 = g^2+g'^2$. The first term is the Coulomb factor, zero whenever a
neutron is involved. On nucleon blocks the exchange with a fraction
$\lambda$ of the second term kept has the Coulomb form if and only if
$\lambda = 0$, and the remaining coefficient $e^2$ vanishes exactly when
$g'^2 = 0$. Coulomb is therefore the unbroken $W^3 + B$ exchange minus the
$Z$ exchange, and it needs, besides $Y$: the mixing $s^2 = \sin^2\theta_W$,
and a $Z$ mass scale that removes the second term at nuclear distance.
Neither is derived in this framework: the electroweak torus-link triplet
of [the electroweak conjecture](#conj:electroweak-higgs-torus-link-triplet)
orders $m_W < m_Z < m_H$ by crossing number but fixes no absolute scale.

**Split-bundle framing $F = V_2 \oplus W_3^*$ and conditional hypercharge coupling.**
In the Standard Model appendix, the missing hypercharge and the missing
three-dimensional partner are shown to be one conditional gap rather than two
independent knobs.  If the two-dimensional fibre $V_2$ ($z_2 = q^3/(q^2+1)$)
is paired with a three-dimensional partner $W_3^*$ ($z_3 = q^3/[3]_q =
q^5/(q^4+q^2+1)$, separated from $z_2$ by the identity $z_2 - z_3 =
q^3 / ((q^2+1)(q^4+q^2+1)) \neq 0$) inside $F = V_2 \oplus W_3^*$, then over
any field of characteristic outside $\{2, 3\}$ the traceless centralizer
$\mathrm{diag}(y_2, y_2, y_3, y_3, y_3)$ satisfies $2 y_2 + 3 y_3 = 0$ if and
only if $y_3 = -\tfrac{2}{3} y_2$.  Fixing the doublet normalisation $y_2 = 1$
pins $y_3 = -\tfrac{2}{3}$, gives the exterior-pair quark doublet in $V_2 \otimes
W_3^*$ hypercharge $y_2 + y_3 = +\tfrac{1}{3}$, and yields the Killing traces
$\mathrm{tr}(T_3^2) = \tfrac{1}{2}$ and $\mathrm{tr}((Y_F/2)^2) = \tfrac{5}{6}$,
hence the unrenormalized Weinberg ratio
$\mathrm{tr}(T_3^2)/(\mathrm{tr}(T_3^2) + \mathrm{tr}((Y_F/2)^2)) = \tfrac{3}{8}$.
On single strands, combining the weak-crossing sign $s_2 \in \{\pm 1\}$ with the
$W_3$ versus $W_3^*$ triality orientation $\tau_3 \in \{\pm 1\}$ via
$Q = \tfrac{1}{2} s_2 + \tfrac{1}{6} \tau_3$ reproduces
$(+\tfrac{2}{3}, -\tfrac{1}{3}, +\tfrac{1}{3}, -\tfrac{2}{3})$ on
$(u, d, \bar d, \bar u)$ and separates $\bar u$ ($-\tfrac{2}{3}$) from $d$
($-\tfrac{1}{3}$) by $+\tfrac{1}{3} \neq 0$ despite their identical crossing
sign $-1$.  This implication is proved conditionally on $W_3^*$: constructing
$W_3$ categorically in the multi-fibre groupoid remains the open antecedent.
