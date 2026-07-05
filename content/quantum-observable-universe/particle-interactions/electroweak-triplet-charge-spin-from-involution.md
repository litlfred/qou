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

**Notation tension flagged for the owner ($\sigma_5^8 = B$ versus $H$).**

The Weinberg-angle block
([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)) reads the
Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ singlet $B$ (pre-mixing),
whereas
([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet))
reads $\sigma_5^8$ (that is $T(2,8)$, strands $5$–$6$) as the Higgs $H$. Both
are singlet-like (bar-even, $A_+$), but the gauge singlet $B$ — which mixes
into $Z$ and $\gamma$ — and the scalar $H$ are distinct particles. This
assignment needs an owner ruling; it is recorded, not silently resolved.
