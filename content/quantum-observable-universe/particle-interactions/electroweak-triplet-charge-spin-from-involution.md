**Theorem (conditional on the electroweak sector-selection postulate — the
axiomatised C1 selection of
[conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)).**
*Fix the categorical coefficient ring $R$ (a field with $\tfrac{1}{2} \in R$)
and the sector-selection postulate `EWSectorSelection`: each electroweak
carrier is assigned to the spin-singlet sector $A_+$ ($\sigma$-fixed, bar-even)
or the spin-doublet sector $A_-$ ($\sigma$-negated, bar-odd) of the spin
involution $\sigma$ of ([def:spin-involution](#def:spin-involution)), with $H$
the singlet and $W^\pm, Z$ the doublets, together with the isospin label map
$T_3(W^\pm) = \pm 1$, $T_3(Z) = T_3(H) = 0$. Then the spin and charge of the
triplet are determined:*

$$
  \mathrm{spin}(H) = 0 \ (\text{scalar, neutral}), \qquad
  \mathrm{spin}(W^\pm) = \mathrm{spin}(Z) = 1 \ (\text{vector}),
$$
$$
  T_3(W^\pm) = \pm 1 \ (\text{charged}), \qquad T_3(Z) = 0 \ (\text{neutral}).
$$

Charge and spin are **not** two independent open conjectures. Both follow from
one physics selection postulate through the corpus spin involution
([def:spin-involution](#def:spin-involution)), whose formalised projection
algebra ($A = A_+ \oplus A_-$, $T_3 = \tfrac{1}{2}\,\mathrm{sgn}_\sigma$) is
proved sorry-free. This **collapses the former C3 (charge) and C4 (spin)** —
previously two independent open primary conjectures — into proved consequences.

**The provable half — bar-parity of the even-twist carriers.**

The even-twist carrier $T(2,2k)$ occupies the two-dimensional sym/alt Hecke
block with eigenvalues $(q^{2k}, q^{-2k})$, modelled as the pair
$(\uparrow a, \uparrow a^{-1}) \in R \times R$ with $a = q^{2k} \in R^\times$.
The spin involution acts on this block as the **swap**
$\sigma(x,y) = (y,x)$ — precisely the bar involution $q \mapsto q^{-1}$
sending $q^{2k} \leftrightarrow q^{-2k}$. Its projections split the carrier:

1. **bar-even part** $a_+ = \tfrac{1}{2}(m + \sigma m) \in A_+$, $\sigma$-fixed,
   with neutral (Markov-trace) value $q^{2k} + q^{-2k}$ ($= 2\cosh$) — the
   retained, neutral channel (per
   ([prop:vdw-pskew-isolation](#prop:vdw-pskew-isolation)));
2. **bar-odd part** $a_- = \tfrac{1}{2}(m - \sigma m) \in A_-$, $\sigma$-negated,
   **traceless** ($\mathrm{trSum}(a_-) = 0$, the $P_{\mathrm{skew}}$ / charged
   channel) but with nonzero skew value $q^{2k} - q^{-2k}$ ($= 2\sinh$).

All of these are Lean-proved sorry-free. The Higgs is the bar-even /
self-dual / real-volume carrier
([prop:self-dual-higgs-real-volume](#prop:self-dual-higgs-real-volume)); the
$W^\pm, Z$ are bar-odd.

**The forced quantum numbers.**

Given the sector assignment, spin is *defined* by
$2s(c) = 0$ if $c$ is a singlet and $2s(c) = 2$ if $c$ is a doublet; then
$\mathrm{spin}(H) = 0$ (scalar) and $\mathrm{spin}(W^\pm) = \mathrm{spin}(Z) =
1$ (vector) are theorems, immediate from the postulate's sector fields.
Neutrality is forced by bar-parity: a singlet carrier realises the bar-even
(traceless-skew, neutral) part, a doublet the bar-odd (charged) part.

The only genuinely postulated data are the sector map itself and the $T_3$
label. In particular $Z$ is a **doublet** (vector) yet **neutral**
($T_3 = 0$): its neutrality is not bar-even membership but the
$(W^3, B) \mapsto (Z, \gamma)$ Weinberg mixing
([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)), carried
as the postulate field $T_3(Z) = 0$.

**The $\sigma_5^8$ bar-grading is DERIVED from spin (not merely stated).**

The Weinberg-angle block
([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)) reads the
Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ hypercharge gauge boson $B$
(pre-mixing), whereas
([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet))
reads $\sigma_5^8$ (that is $T(2,8)$, strands $5$–$6$) as the Higgs. These are
not in conflict: $\sigma_5^8$ **carries both, bar-graded** by the spin
involution above. The Higgs *boson* $H$ is the $A_+$ (bar-even, scalar) part;
the hypercharge gauge boson $B$ is the $A_-$ (bar-odd, vector) part.

This bar-grading is no longer an owner postulate: it is now **derived from the
two carriers' spins**, sorry-free (`ew_sigma5_bargrade_forced`). The
sector$\to$spin map (singlet $\mapsto 0$, doublet $\mapsto 2$) is injective, so
it **inverts** — spin *determines* the sector (`barSectorOfSpin`, proved a
genuine two-sided inverse by `barSectorOfSpin_inverts`). The Higgs is a scalar
(spin $0$) and $B$ is a vector (spin $1$) as independent physical inputs; hence
$H \in A_+$ and $B \in A_-$ of the $\sigma_5^8$ slot are **forced, not chosen**.
The single residual postulate is that both $H$ and $B$ inhabit the one
$\sigma_5^8$ slot; its *grading into $A_+ / A_-$* is a consequence of their
spins. Weinberg (reading $A_-$) and the triplet block (reading $A_+$) therefore
agree by derivation, not by fiat. Distinct again is the self-dual figure-eight
$4_1$ of ([prop:self-dual-higgs-real-volume](#prop:self-dual-higgs-real-volume)):
it is the Higgs *mass mechanism* (the muon scale
$m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$), **not** the $125\,$GeV Higgs boson
$H = T(2,8) = A_+$ of $\sigma_5^8$.

**Which slot is $W$ ($\sigma_1^4$ vs $\sigma_3^6$) is a free label — not forced.**

The sector membership $A_+ / A_-$ of each carrier is forced by its spin above,
and a *charged* carrier must be a bar-odd $A_-$ doublet
(`charged_are_doublets_singlet_neutral`). What is **not** forced is which of the
two vector slots — $\sigma_1^4$ ($T(2,4)$, $4$ crossings) or $\sigma_3^6$
($T(2,6)$, $6$ crossings) — hosts the *charged* $W^\pm$ ($T_3 = \pm 1$) versus
the *neutral* $Z$ ($T_3 = 0$). The corpus crossing$\to$charge map
([def:coulomb-charge](#def:coulomb-charge)), $Q = \tfrac12(n_+ - n_-) =
\tfrac12\,\mathrm{writhe}$, evaluated on the all-positive braid $\sigma_1^{2k}$
gives $Q(T(2,2k)) = k > 0$ for *every* carrier ($k = 2, 3, 4$), so it makes
$W, Z, H$ all charged and cannot single out the neutral slot; independently the
$\mathrm{writhe} \to Y$ hypercharge map is falsified. Of the three
crossing$\to$quantum-number maps the U(1)-assignment audit tested, only
$\mathrm{writhe} \to I_3$ survives — and even *it* fails to select the neutral
slot once evaluated on these carriers. That surviving map is the *sign+ratio*
relation $2 I_3 = \mathrm{writhe}$, keyed on the **crossing sign**: it matched
the nucleon doublet because $p$ and $n$ differ by the $\sigma \leftrightarrow
\sigma^{-1}$ ($u \leftrightarrow d$) crossing-sign flip ($w(p) = +1$,
$w(n) = -1$, whence $I_3(p) = +\tfrac12$, $I_3(n) = -\tfrac12$). But the
even-twist carriers $\sigma_1^{2k}$ are all-positive (writhe $2k$, no negative
crossings), so the surviving map assigns them $2 I_3 = 2k$: strictly positive,
strictly monotone in $k$ ($4 < 6 < 8$), and **nonzero on both vector slots**
$\sigma_1^4$ and $\sigma_3^6$. It is thus a magnitude / twist ladder — the exact
analogue of the audit's monotone $\theta_j = q^{j(j+1)}$ spin ladder, with no
sign change and no zero — not an additive sign charge, and it produces no
neutral slot. The structural reason is that $I_3$'s sign *is* the crossing sign,
and the two same-sign vector carriers offer no $\sigma \leftrightarrow
\sigma^{-1}$ flip for the map to act on.

So no proved crossing$\to$charge principle selects the $W$ slot. The paper's
choice $W = \sigma_1^4$ (the lower crossing) is supported only by the mass
ordering $4 < 6 < 8$ (necessary, not sufficient). This underdetermination is
proved sorry-free (`which_slot_is_W_free`), and the failure of the surviving map
to close it is proved sorry-free as well
(`evenTwist_doubledI3_pos`, `evenTwist_doubledI3_strictMono`,
`writheI3_does_not_select_neutral_slot`): both $W = \sigma_1^4$ and the mirror
$W = \sigma_3^6$ satisfy every proved constraint, and the surviving $\mathrm{writhe}
\to I_3$ map cannot even furnish the neutral-slot datum needed to break the tie.
It is carried as the explicit free-label field `t3Label` of the sector postulate
([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)).
What *would* force it is a genuinely *signed* crossing/linking $\to T_3$ (or
electric charge) invariant — a carrier realisation with a $\sigma \leftrightarrow
\sigma^{-1}$ asymmetry that drives one vector slot's net writhe to zero — or the
second independent baryon / color-trace charge the audit names; the framework
supplies neither for the same-sign even-twist triple.

**The signed $\sigma \leftrightarrow \sigma^{-1}$ / charge-conjugation test:
still free, and the neutral slot is forced to be mixed.**

The two ingredients just named — a *signed* crossing asymmetry and a second
charge — can be examined directly. Charge conjugation is crossing reversal
([rem:chirality-trefoil-electron-positron](#rem:chirality-trefoil-electron-positron)):
the operation $C = (\sigma \leftrightarrow \sigma^{-1})$ reverses every crossing,
so on the signed writhe $w$ it acts as negation, $C(w) = -w$, and
$Q(\mathfrak{p}^{\sigma}) = -Q(\mathfrak{p})$. A carrier is **neutral iff it is a
fixed point of $C$** — its own antiparticle — i.e. **$C$-invariant**, i.e.
**amphichiral**. Over $\mathbb{Z}$ this fixed-point condition is exactly the
vanishing of the signed writhe,

$$
  C(w) = w \iff -w = w \iff w = 0,
$$

proved sorry-free (`cInvariant_iff_writhe_zero`, by integer arithmetic — not a
type tautology). Two consequences follow, and together they give a sharper
negative than the unsigned analysis above.

First, admitting the signed asymmetry does **not** force which slot is $W$. Two
distinct signed labelings — one placing the charged (chiral, $w \neq 0$) $W$ at
$\sigma_1^4$ and the amphichiral ($w = 0$) neutral member at $\sigma_3^6$, the
other the mirror — both satisfy the full $C$-invariance neutrality constraint yet
disagree on the charged slot (`signed_which_slot_is_W_free`). The signed test
constrains the neutral slot to be *amphichiral*, but not *which* slot it is.

Second, and more sharply, the $C$-invariance criterion **excludes every pure
even-twist slot from being the neutral member**. Each carrier
$\sigma_1^{2k} = T(2,2k)$ has signed writhe $2k \neq 0$ for $k \geq 1$, so none is
$C$-invariant / amphichiral — all three of $\sigma_1^4$ ($k=2$), $\sigma_3^6$
($k=3$), $\sigma_5^8$ ($k=4$) are genuinely chiral (`evenTwist_not_cInvariant`).
Hence the neutral electroweak boson is **necessarily not a single even-twist
slot**: it must be the mixed $(W^3, B) \mapsto (Z, \gamma)$ Weinberg combination
([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)) — a $w = 0$
amphichiral state assembled from chiral pieces, not any one slot. This upgrades
`which_slot_is_W_free` with the *reason* it holds: the correct neutrality
criterion (charge-conjugation invariance) forbids every chiral slot from being
neutral, so no single-slot topological invariant can pick out the $Z$.

What *would* break the tie is precisely the second charge the audit names. If a
hypothetical second (baryon / color-trace) charge $S$ were nonzero on exactly one
vector slot, reading "neutral $\iff$ $S$ vanishes" would determine the neutral
slot uniquely (`second_charge_would_force_neutral_slot`, a proved conditional).
The corpus supplies no such $S$ for the same-sign even-twist triple (the
2026-06-02 U(1)-assignment audit records this second charge as a *missing*
object). The capstone
`signed_C_does_not_force_W_slot_but_forces_neutral_mixed` bundles the three facts
sorry-free: signed non-forcing, $C$-invariance $=$ amphichirality, and the
chirality of all three even-twist carriers. The $T_3$ label of the pure slots is
therefore fixed **only by the mixing / second-charge data**, not by any
single-slot invariant.
