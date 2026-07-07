<!-- FILE_START: electroweak-triplet-bring-embedding.md -->
**Proposition (electroweak triplet Bring embedding).**
*The even-twist 2-component torus links $T(2,4), T(2,6), T(2,8)$ — the braids $\sigma_1^{2k} \in B_2$ for $k = 2, 3, 4$ — have Seifert genera $1, 2, 3$ respectively. These genera strictly increase and satisfy $g \leq 4 = g(\Sigma_4)$. The three links therefore co-embed in the genus-$4$ Seifert fiber of ([Bring's surface](#def:brings-surface)) alongside the saturating force-carriers $\{T(2,9), T(3,5)\}$ (genus $4$), by the embeddability bound $g(K) \leq g(\Sigma_4)$ of ([prop:torus-embeddable-complete](#prop:torus-embeddable-complete)). Moreover, the three cells carry the pairwise-orthogonal Hoefsmit idempotent decomposition in $\mathrm{End}_R(V^{\otimes 6})$ of ([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)).*

**Proof.**

The canonical Seifert surface of the 2-component torus link $T(2, 2k)$ has genus $g(T(2, 2k)) = k - 1$. At $k = 2, 3, 4$ the genera are $1, 2, 3$. These strictly increase and remain $\leq 4$. The even-twist links with genus in $\{1, 2, 3\}$ are exactly those with $k \in \{2, 3, 4\}$. The family is finite and closed at these three. The embeddability bound $g(K) \leq g(\Sigma_4) = 4$ places all three in the same genus-$4$ Seifert fiber alongside the saturating carriers.

The genus, enumeration, and embedding steps involve elementary $\mathbb{N}$-arithmetic. They are verified sorry-free in Lean via `omega`: `ew_genus_values`, `ew_enumeration`, and `ew_triplet_embeds`, combined in `electroweak_triplet_bring_embedding`. The Hoefsmit idempotent orthogonality is cited from ([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)). $\square$

**Scope.**
This proposition supplies the provable structural half of the electroweak torus-link story. It establishes that the triplet fits the genus-$4$ host. It does not fix *which* link carries $W^\pm$ versus $Z$ versus $H$. That physical identification constitutes the conjecture ([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)). This conjecture relies on the open selection, charge, and spin sub-conjectures.
<!-- FILE_END: electroweak-triplet-bring-embedding.md -->

<!-- FILE_START: electroweak-triplet-far-commuting-minimal.md -->
**Theorem (far-commuting minimality of the even-twist triplet).**
*Let $\sigma_a, \sigma_b, \sigma_c$ be pairwise far-commuting braid generators: $|a-b|, |b-c|, |a-c| \geq 2$. Then:*

1. *(Minimality.) These generators require at least $6$ strands. With $1 \leq a < b < c$, the pairwise gap $\geq 2$ forces $c \geq 5$, yielding $n \geq c+1 \geq 6$. The bound is attained **uniquely** by the consecutive odd triple $(a,b,c) = (1,3,5)$ in $B_6$.*
2. *(Enumeration.) The even-twist $2$-component torus links $T(2,2k)$ (braid $\sigma_1^{2k}$, Seifert genus $g = k-1$) with genus strictly between the trivial Hopf endpoint $g=0$ and the genus-$4$ Bring saturation ($1 \leq g \leq 3$) are exactly those with $k \in \{2,3,4\}$: the triplet $T(2,4), T(2,6), T(2,8)$.*

This forms the **physics-free mathematical core** of the electroweak selection principle C1 of ([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)). Both halves rely on elementary $\mathbb{N}$-arithmetic and are Lean-proved sorry-free (`omega`).

**Far-commuting minimality.**

Each even-twist carrier $T(2,2k)$ acts on a single strand-pair. Three mutually non-interfering carriers require three generators $\sigma_a, \sigma_b, \sigma_c$ that pairwise commute without sharing a strand. This is the far-commutativity condition $|i-j| \geq 2$. In $B_n$, a generator $\sigma_i$ requires $1 \leq i \leq n-1$. Three indices with $a \geq 1$, $b \geq a+2$, $c \geq b+2$ dictate $c \geq 5$, so $n = c+1 \geq 6$. Setting $c = 5$ forces $(a,b,c) = (1,3,5)$. This mathematical statement is physically realised in ([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)). The $n=6$ minimum supplies three disjoint strand-pairs $\{1,2\}, \{3,4\}, \{5,6\}$ carrying $\sigma_1^4, \sigma_3^6, \sigma_5^8$.

**Enumeration.**

The genus filtration places the trivial Hopf link $T(2,2)$ at $g=0$ and the force-carrier saturation $\{T(2,9), T(3,5)\}$ at $g=4 = g(\Sigma_4)$. The open window $0 < g < 4$ contains exactly the genera $1,2,3$ ($k \in \{2,3,4\}$). This forward inclusion matches the arithmetic proved sorry-free as `ew_enumeration` in ([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)). It is reproduced inline in the Lean sibling because content-block sibling `.lean` files compile standalone and cannot import one another. The proposition serves as the canonical statement.

**Scope.**

This theorem elevates the mathematical content of C1 to a proved statement. It does **not** assert that the electroweak sector *is* this set of links. That identification remains the conjectural input of ([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)). The far-commuting bound and enumeration provide the facts upon which that postulate operates.
<!-- FILE_END: electroweak-triplet-far-commuting-minimal.md -->

<!-- FILE_START: electroweak-higgs-torus-link-triplet.md -->
**Conjecture (electroweak/Higgs torus-link identification).**
*In any QOU built on ([Bring's surface](#def:brings-surface)) with EM/strong sector $\{T_{2,9}, T_{3,5}\}$ ([force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness)), the standard-model electroweak gauge bosons $W^\pm, Z$ and the Higgs scalar $H$ correspond to the three even-twist $2$-component torus links of the sub-saturating complement:*

$$
  W^{\pm} \;\longleftrightarrow\; T(2,4),
  \qquad
  Z \;\longleftrightarrow\; T(2,6),
  \qquad
  H \;\longleftrightarrow\; T(2,8).
$$

This is the **top node** of the electroweak conjecture lattice. Its provable base — that these three links exist, have Seifert genera $1, 2, 3$, co-embed in Bring's genus-$4$ fiber alongside the saturating carriers, and fit minimally in $B_6$ at the far-commuting triple $(1,3,5)$ — is discharged to the sorry-free ([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)) and ([thm:ew-triplet-far-commuting-minimal](#thm:ew-triplet-far-commuting-minimal)). What remains conjectural is the *identification itself*. As of 2026-07-05, charge and spin are proved consequences of a single sector postulate.

**The conjecture lattice (narrowed).**

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| **C1** selection | primary | — | EW carriers *are* the nontrivial, strictly sub-saturating even-twist links ($0 < g < 4$). |
| **C2** enumeration | dependent (C1) | C1 | These carriers are exactly $\{T(2,4), T(2,6), T(2,8)\}$. |
| **C$_{\text{sector}}$** sector assignment | primary | — | Which link sits in the singlet $A_+$ versus doublet $A_-$ of the spin involution. |
| **C$_{\text{top}}$** identification | dependent (C1, C$_{\text{sector}}$) | C1, C$_{\text{sector}}$ | The full map above. |

The former **C3 (charge)** and **C4 (spin)** are proved consequences of C$_{\text{sector}}$ via ([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)).

**C1 — the selection principle (strong corpus grounding).**

The electroweak carriers are the *nontrivial, strictly sub-saturating* even-twist $2$-component torus links. Their Seifert genus $g$ lies in the window $0 < g < 4 = g(\Sigma_4)$. This forms the sub-saturating complement of the genus-$4$ **saturating** force-carrier knots $\{T_{2,9}, T_{3,5}\}$. These two are the only coprime solutions of $(p-1)(q-1) = 8$, exhausting Bring's genus-$4$ capacity. The Hopf link $T(2,2)$ (genus $0$) is the trivial endpoint and is excluded. C1 ties to the $S_5$ action on the Hecke slice ([conj:n-v-bring-action](#conj:n-v-bring-action)). The saturation mechanism that forces $\{T_{2,9}, T_{3,5}\}$ for the strong carriers selects the sub-saturating window for the weak carriers.

**C2 — enumeration (dependent on C1).**

Given C1, the carrier window $0 < g < 4$ contains exactly the genera $1, 2, 3$ ($k \in \{2, 3, 4\}$): the triplet $T(2,4), T(2,6), T(2,8)$. The forward inclusion is the *provable* enumeration `ew_enumeration` of ([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)). The conjectural content of C2 is the reverse inclusion: all three genera are realised as carriers.

**C$_{\text{sector}}$ — the single sector-assignment postulate.**

Charge and spin are unified by one $\mathbb{Z}/2$ datum: the assignment of each carrier to a sector of the spin involution $\sigma$ of ([def:spin-involution](#def:spin-involution)), $A = A_+ \oplus A_-$. Restricted to the sym/alt Hecke block, $\sigma$ is the swap of the eigenvalues $q^{2k} \leftrightarrow q^{-2k}$ (the bar involution $q \mapsto q^{-1}$). Its projections give a bar-even part in $A_+$ (neutral, retained by the Markov trace) and a bar-odd part in $A_-$ (charged, traceless), per ([prop:vdw-pskew-isolation](#prop:vdw-pskew-isolation)). The Higgs is the bar-even self-dual carrier ([prop:self-dual-higgs-real-volume](#prop:self-dual-higgs-real-volume)).

**Charge and spin are proved consequences.** Given the sector assignment ($H$ singlet, $W^\pm, Z$ doublets), ([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)) derives: $H \in A_+$ implies scalar (spin $0$) and neutral; $W^\pm \in A_-$ implies vector (spin $1$) with $T_3 = \pm 1$; $Z \in A_-$ implies vector, neutral with $T_3 = 0$ via the $(W^3, B) \mapsto (Z, \gamma)$ Weinberg mixing ([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)). The remaining conjectural input is the sector assignment itself.

**The $\sigma_5^8$ bar-grading is derived from spin.**

The Weinberg-angle block ([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)) reads the Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ hypercharge gauge boson $B$ (pre-mixing). This block reads $\sigma_5^8$ ($= T(2,8)$, strands $5$–$6$) as the Higgs. There is no conflict: $\sigma_5^8$ **carries both, bar-graded** by the spin involution ([def:spin-involution](#def:spin-involution)). The Higgs boson $H$ is the $A_+$ (bar-even, scalar) part. The hypercharge gauge boson $B$ is the $A_-$ (bar-odd, vector) part.

This bar-grading is derived from the two carriers' spins (`ew_sigma5_bargrade_forced` in ([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution))). The sector$\to$spin map is injective and inverts. Spin determines the sector. The Higgs is a scalar and $B$ a vector as independent physical inputs, so $H \in A_+$ and $B \in A_-$ are forced. The residual postulate is that both $H$ and $B$ inhabit the one $\sigma_5^8$ slot. The self-dual figure-eight $4_1$ of ([prop:self-dual-higgs-real-volume](#prop:self-dual-higgs-real-volume)) is the Higgs *mass mechanism* ($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$), not the $125\,$GeV Higgs boson. The boson is the electroweak-slot link $T(2,8) = A_+$ of $\sigma_5^8$.

**The $W$ vs $Z$ slot assignment is a free label.**

Spin fixes each carrier's sector (scalar $H \to A_+$; vectors $W, Z \to A_-$). It does not fix which of the two $A_-$ vector slots is the charged $W^\pm$ and which is the neutral $Z$. The corpus map ([def:coulomb-charge](#def:coulomb-charge)), $Q = \tfrac12(n_+ - n_-) = \tfrac12\,\mathrm{writhe}$, on the all-positive braid $\sigma_1^{2k}$ gives $Q(T(2,2k)) = k > 0$ for all three carriers. It cannot single out the neutral slot. The $\mathrm{writhe} \to Y$ map is falsified. Only $\mathrm{writhe} \to I_3$ survives. The assignment $W = \sigma_1^4$ relies on the mass ordering $4 < 6 < 8$. It is carried as the explicit free-label field `t3Label` of $C_{\text{sector}}$. Its underdetermination is proved sorry-free (`which_slot_is_W_free`). Both $W = \sigma_1^4$ and the mirror $W = \sigma_3^6$ satisfy every proved constraint.

**Supporting evidence.**

The identification aligns with the following observations:

1. **Mass ordering.** The standard-model ordering $m_{W^\pm} < m_Z < m_H$ ($80.4 < 91.2 < 125.3$ GeV) maps monotonically onto the crossing-number ordering $4 < 6 < 8$.
2. **PSD-feasibility probe.** An exploratory SDP-feasibility probe ([`ew-higgs-sdp-probe.witness.json`](https://github.com/litlfred/qou/blob/main/computations/probes/ew-higgs-sdp-probe.witness.json)) shows PSD discrimination. Only the even-twist torus-link triplet $\{T(2,4), T(2,6), T(2,8)\}$ produced positive-semidefinite Hecke certificates on every Wedderburn block. 

PSD-feasibility is necessary but not sufficient. It holds for every even-twist $T(2, 2k)$ at any $k \geq 1$. The probe cannot select the specific triplet from the infinite family.

See [Table 1](#tbl:electroweak-higgs-torus-link-triplet-table1-data) for the $1/\alpha_{EM}$-parallel pipeline ([`rem:alpha-em-categorical-trace`](#rem:alpha-em-categorical-trace)), [Table 2](#tbl:electroweak-higgs-torus-link-triplet-table2-data) for the sub-argument factorisation, and [Table 3](#tbl:electroweak-higgs-torus-link-triplet-table3-data) for the probe over $T(2, 2k)$, $k = 1 \ldots 7$.

**What the conjecture closes.**

If true, the identification supplies the categorical structure for the weak-scale crossing count $N_v$ in the Fermi-constant decomposition $G_F = 1/(\sqrt{2}\,v^2)$, $v = N_v\,E_\times\,\mu_0$ (the **NV-1** audit flag ([NV-1 / FROB-FILTER conjectures, 2026-05-02](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-02-nv-frob-filter-conjectures.md))). The residual to close is C1 (selection) and C$_{\text{sector}}$ (sector assignment). Enumeration and far-commuting minimality are discharged to ([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)) and ([thm:ew-triplet-far-commuting-minimal](#thm:ew-triplet-far-commuting-minimal)). Charge and spin are discharged to ([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)).
<!-- FILE_END: electroweak-higgs-torus-link-triplet.md -->

<!-- FILE_START: electroweak-triplet-charge-spin-from-involution.md -->
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

**The two natural realizations of the second charge also fail.**

The audit names the missing object as a baryon / color-trace charge. Its two
natural knot-theoretic realizations — the pairwise linking number $\mathrm{Lk}$
and the Milnor triple linking $\bar\mu(123)$ — can be tested directly against the
forcing hypothesis of `second_charge_would_force_neutral_slot` (a charge nonzero
on exactly one vector slot). Neither qualifies
(`named_second_charge_candidates_do_not_force_label`): the even-twist carrier
$T(2,2k)$ is a two-component link, so $\bar\mu(123) \equiv 0$ on every carrier (a
triple linking needs $\geq 3$ components) — it vanishes on *both* slots, giving no
charged slot; while $\mathrm{Lk}(T(2,2k)) = k \neq 0$ on every carrier
($k = 2, 3, 4$) — it vanishes on *neither* slot, giving no neutral slot. These are
the two distinct ways of missing the "nonzero on exactly one slot" datum, and both
are proved (not a vacuous non-existence).

**The group-structure data does force the label (conditional positive).**

Topology cannot force the label, but the $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$
group assignment can. The genuine missing input is the alignment of the two
vector slots with the $\mathfrak{su}(2)_L$ Cartan–Weyl basis — *which* slot hosts
the neutral Cartan generator $W^3$ (the zero-weight member of the adjoint, which
mixes into $Z$) versus the charged root member $W^\pm$. Axiomatised as the open
hypothesis class `EWGroupAssignment` (carrying the Cartan/charged slot alignment
and its non-degeneracy — a group-theoretic datum, *not* the $T_3$ values), the
label is then **derived**: the neutral slot is the Cartan slot ($2 T_3 = 0$), the
charged slot is the complementary root slot ($2 T_3 = 2$), and a slot is neutral
*iff* it is the Cartan slot — read off from the adjoint weights $\{+1, 0, -1\}$,
not projected (`label_forced_given_group_assignment`, §3b-cond conditional
positive). No instance of `EWGroupAssignment` is supplied — it stays an open
input, precisely the $(W^3, B) \mapsto (Z, \gamma)$ Weinberg mixing data
([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)).

The net picture: the $W/Z$ label is **unforced by any single-slot topological
invariant** (the signed / $C$-invariance results and the two named second-charge
candidates), and **forced only by the conjectural $\mathrm{SU}(2)_L \times
\mathrm{U}(1)_Y$ group assignment**. This *relocates* the postulate — from a bare
$T_3$ label to the group-structure (mixing) input — rather than closing it: given
the group datum the label is a theorem, but the group datum itself remains the
open conjectural input.
<!-- FILE_END: electroweak-triplet-charge-spin-from-involution.md -->

<!-- FILE_START: ew-slot-far-commutation-obstruction.md -->
**Proposition (far-commutation obstruction — the non-abelian $\mathrm{SU}(2)_L$ structure is not carried by the slots).**
*Let $A$ be a ring. Let $\sigma_1, \sigma_3, \sigma_5 \in A$ be the braid generators hosting the electroweak carriers on the disjoint strand-pairs $1\text{--}2 \mid 3\text{--}4 \mid 5\text{--}6$ of [`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content). These are subject to the braid far-commutation relation $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i - j| \ge 2$. Let $\mathcal{A}_{\mathrm{slot}} \subseteq A$ be the subalgebra they generate. Suppose $J_1, J_2, J_3 \in A$ realise an $\mathfrak{su}(2)_L$ adjoint structure relation $\lbrack J_1, J_2 \rbrack = J_3$ with $J_3 \ne 0$. Then $J_1$ and $J_2$ cannot both lie in $\mathcal{A}_{\mathrm{slot}}$. The non-abelian $\mathrm{SU}(2)_L$ structure therefore cannot be realised purely among the far-commuting slots.*

### Statement (formal)

The slot indices $1, 3, 5$ are pairwise far apart:
$$
  |1 - 3| = 2, \qquad |1 - 5| = 4, \qquad |3 - 5| = 2.
$$
The far-commutation relation applies to every pair. Thus $\sigma_1, \sigma_3, \sigma_5$ pairwise commute. Consequently, the subalgebra $\mathcal{A}_{\mathrm{slot}} = \langle \sigma_1, \sigma_3, \sigma_5 \rangle$ is **commutative**. Every commutator $\lbrack x, y \rbrack = xy - yx$ vanishes for $x, y \in \mathcal{A}_{\mathrm{slot}}$. In particular, the three carriers $W \leftrightarrow \sigma_1^{4}$, $Z \leftrightarrow \sigma_3^{6}$, $H \leftrightarrow \sigma_5^{8}$ pairwise commute.

The obstruction is the incompatibility of two facts:

1. **Commuting operators have vanishing bracket.** For $x, y \in \mathcal{A}_{\mathrm{slot}}$, $\lbrack x, y \rbrack = 0$.
2. **The $\mathfrak{su}(2)_L$ adjoint is non-abelian.** Its generators satisfy $\lbrack J_a, J_b \rbrack = \varepsilon_{abc} J_c \ne 0$. A nonzero bracket forbids commutation.

If both $J_1, J_2 \in \mathcal{A}_{\mathrm{slot}}$, then $\lbrack J_1, J_2 \rbrack = 0$ by (1), contradicting $J_3 \ne 0$ by (2). At least one $\mathfrak{su}(2)_L$ generator must escape the slot subalgebra.

### What this forces (localization, not closure)

This result is a **structural exclusion**. It proves an impossibility, not a numerical near-miss. The invariant forbidding the realisation is the identical vanishing of the commutator on a commutative subalgebra. It does **not** fit the gauge group into the framework by fiat, nor does it supply the Weinberg angle. It establishes *where the missing structure must reside*.

The far-commutation relation covers only pairs with $|i - j| \ge 2$. The adjacent generators $\sigma_2, \sigma_4$ bridge strand-pairs $2\text{--}3$ and $4\text{--}5$. For these:
$$
  |2 - 1| = |2 - 3| = |4 - 3| = |4 - 5| = 1 < 2.
$$
These are exactly the generators the relation does not cover. They do **not** commute with the slots. The categorical linking operation $\mathrm{Lk}_R^{(k)}$ of [`conj:categorical-linking-operation`](#conj:categorical-linking-operation) braids *between* strand-pairs through precisely these generators. The non-abelian $\mathrm{SU}(2)_L$ structure must therefore be carried by the **inter-slot linking**, not by the individual slots.

This **narrows** the group-assignment postulate $\texttt{EWGroupAssignment}$ of [`thm:ew-triplet-charge-spin-from-involution`](#thm:ew-triplet-charge-spin-from-involution). The residual $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ input—which slot is the neutral Cartan member $W^3 \to Z$ versus the charged root member $W^\pm$—is a property of the bracket-carrying linking data, not of the mutually commuting slots. This is consistent with the prior finding that no single-slot topological invariant forces the label (`which_slot_is_W_free` in [`thm:ew-triplet-charge-spin-from-involution`](#thm:ew-triplet-charge-spin-from-involution)). The label lives where the non-abelianness lives: in the linking, not the slots.

### Lean structure

The formalisation is purely algebraic over a generic ring (no archimedean structure):

- `bracket_eq_zero_of_commute`: commuting elements have zero commutator.
- `nonabelian_bracket_forbids_commute`: the crux ($\lbrack x, y \rbrack = z \ne 0 \implies x, y$ do not commute).
- `commute_of_mem_closure`: the submonoid generated by a pairwise-commuting set is commutative (via the centralizer submonoid).
- `slotSubmonoid_commutative`, `carriers_commute`: the slot subalgebra is mutually abelian; the carriers $\sigma_1^4, \sigma_3^6, \sigma_5^8$ pairwise commute.
- `su2L_nonabelianness_not_in_slots`, `su2L_generator_escapes_slots`: the capstone obstruction and its positive form.

All are sorry-free.e form.

All sorry-free.
<!-- FILE_END: ew-slot-far-commutation-obstruction.md -->

