**Conjecture (electroweak/Higgs torus-link identification).**
*In any QOU built on ([Bring's surface](#def:brings-surface)) with
EM/strong sector $\{T_{2,9}, T_{3,5}\}$
([force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness)),
the standard-model electroweak gauge bosons $W^\pm, Z$ and the Higgs
scalar $H$ are identified with the three even-twist $2$-component
torus links of the sub-saturating complement as*

$$
  W^{\pm} \;\longleftrightarrow\; T(2,4),
  \qquad
  Z \;\longleftrightarrow\; T(2,6),
  \qquad
  H \;\longleftrightarrow\; T(2,8).
$$

This is the **top node** of the electroweak conjecture lattice. Its
provable base — that these three links exist, have Seifert genera
$1, 2, 3$, co-embed in Bring's genus-$4$ fiber alongside the saturating
carriers, and fit minimally in $B_6$ at the far-commuting triple $(1,3,5)$ —
is discharged to the sorry-free
([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding))
and
([thm:ew-triplet-far-commuting-minimal](#thm:ew-triplet-far-commuting-minimal)).
What remains conjectural is the *identification itself*: which link is
which particle. As of 2026-07-05 that residual is **narrowed**: charge and
spin are no longer independent open gaps but proved consequences of a single
sector postulate (see below).

**The conjecture lattice (narrowed).**

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| **C1** selection | primary | — | EW carriers *are* the nontrivial, strictly sub-saturating even-twist links ($0 < g < 4$) — physics postulate only |
| **C2** enumeration | dependent (C1) | C1 | those carriers are exactly $\{T(2,4), T(2,6), T(2,8)\}$ |
| **C$_{\text{sector}}$** sector assignment | primary | — | which link sits in the singlet $A_+$ versus doublet $A_-$ of the spin involution |
| **C$_{\text{top}}$** identification | dependent (C1, C$_{\text{sector}}$) | C1, C$_{\text{sector}}$ | the full map above |

The former **C3 (charge)** and **C4 (spin)** — previously two independent
open primary conjectures — are **removed as independent nodes**: they are now
proved consequences of C$_{\text{sector}}$ via
([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)).

**C1 — the selection principle (strong corpus grounding).**

The electroweak carriers are the *nontrivial, strictly sub-saturating*
even-twist $2$-component torus links: those with Seifert genus $g$ in the
window $0 < g < 4 = g(\Sigma_4)$. This is the sub-saturating complement of
the genus-$4$ **saturating** force-carrier knots $\{T_{2,9}, T_{3,5}\}$ —
the only two coprime solutions of $(p-1)(q-1) = 8$, which exhaust Bring's
genus-$4$ capacity. The Hopf link $T(2,2)$ (genus $0$) is the trivial/vacuum
endpoint and is excluded by the strict lower bound. C1 ties to the $S_5$
action on the Hecke slice
([conj:n-v-bring-action](#conj:n-v-bring-action)): the same saturation
mechanism that forces $\{T_{2,9}, T_{3,5}\}$ for the force carriers selects
the sub-saturating window for the weak carriers.

**C2 — enumeration (dependent on C1).**

Given C1, the carrier window $0 < g < 4$ contains exactly the genera
$1, 2, 3$, i.e. $k \in \{2, 3, 4\}$: the triplet $T(2,4), T(2,6), T(2,8)$.
The forward inclusion (carriers $\subseteq \{2,3,4\}$) is the *provable*
enumeration `ew_enumeration` of
([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding));
the conjectural content of C2 is only the reverse inclusion — that all
three genera are realised as carriers.

**C$_{\text{sector}}$ — the single sector-assignment postulate (replaces C3 + C4).**

Charge and spin were previously two separate open conjectures because a
link's Seifert genus is blind to both. They are now unified: both are read
off one $\mathbb{Z}/2$ datum — the assignment of each carrier to a sector of
the spin involution $\sigma$ of ([def:spin-involution](#def:spin-involution)),
$A = A_+ \oplus A_-$. Restricted to the sym/alt Hecke block, $\sigma$ is the
swap of the eigenvalues $q^{2k} \leftrightarrow q^{-2k}$ (the bar involution
$q \mapsto q^{-1}$); its projections give a bar-even part in $A_+$ (neutral,
retained by the Markov trace) and a bar-odd part in $A_-$ (charged,
$P_{\mathrm{skew}}$, traceless), per
([prop:vdw-pskew-isolation](#prop:vdw-pskew-isolation)). The Higgs is the
bar-even self-dual carrier
([prop:self-dual-higgs-real-volume](#prop:self-dual-higgs-real-volume)).

**Charge and spin are now proved consequences, not conjectures.** Given the
sector assignment ($H$ singlet, $W^\pm, Z$ doublets), the theorem
([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution))
derives (sorry-free): $H \in A_+ \Rightarrow$ scalar (spin $0$) and neutral;
$W^\pm \in A_- \Rightarrow$ vector (spin $1$) with $T_3 = \pm 1$;
$Z \in A_- \Rightarrow$ vector, neutral with $T_3 = 0$ via the
$(W^3, B) \mapsto (Z, \gamma)$ Weinberg mixing
([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)). The
single residual conjectural input is the sector assignment itself (which link
lands in which sector) plus the bare particle-label map — the physics
selection, not the derivation of the quantum numbers.

**Notation tension flagged for the owner ($\sigma_5^8 = B$ versus $H$).**

The Weinberg-angle block
([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)) reads
the Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ singlet $B$
(pre-mixing), whereas this block reads $\sigma_5^8$ ($= T(2,8)$, strands
$5$–$6$) as the Higgs $H$. Both are singlet-like (bar-even, $A_+$), but the
gauge singlet $B$ — which mixes into $Z$ and $\gamma$ — and the scalar $H$
are distinct particles. This assignment needs an owner ruling; it is
recorded here and in
([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)),
not silently resolved.

**Supporting evidence (necessary, not sufficient).**

The identification is consistent with, but not selected by, the following.

1. **Mass ordering.** The standard-model ordering
   $m_{W^\pm} < m_Z < m_H$ ($80.4 < 91.2 < 125.3$ GeV, CODATA/PDG) maps
   monotonically onto the crossing-number ordering $4 < 6 < 8$.
2. **PSD-feasibility probe.** An exploratory SDP-feasibility probe
   ([`ew-higgs-sdp-probe.witness.json`](https://github.com/litlfred/qou/blob/main/computations/probes/ew-higgs-sdp-probe.witness.json))
   on three candidate identification paths returned a clean PSD
   discrimination: only the even-twist torus-link triplet
   $\{T(2,4), T(2,6), T(2,8)\}$ produced positive-semidefinite Hecke
   certificates on every Wedderburn block. The two competing paths —
   $T_{3,5}$ as a unified weak triplet, and non-torus knots ($4_1$ for
   Higgs, $5_2$ for $Z$, $3_1$ for $W$) — failed PSD on the standard
   $(2,1)$ representation.

   PSD-feasibility is *necessary but not sufficient*: it holds for **every**
   even-twist $T(2, 2k)$ at any $k \geq 1$ (the even power squares the sign
   of the alternating Hecke eigenvalue, $(-q^{-1})^{2k} = q^{-2k} > 0$
   under any real specialisation $q \mapsto q^* > 1$; the
   [Hecke algebra from braiding](#rem:hecke-algebra-from-braiding),
   Hecke–Skein convention, §7a of AGENTS.md). So the probe cannot select
   the specific triplet from the infinite even-twist family — the
   selection is C1, and the charge/spin assignment is C3/C4.

See [Table 1](#tbl:electroweak-higgs-torus-link-triplet-table1-data) for
the $1/\alpha_{EM}$-parallel pipeline (the categorical route to $G_F$ that
this identification would unlock, via
([`rem:alpha-em-categorical-trace`](#rem:alpha-em-categorical-trace))),
[Table 2](#tbl:electroweak-higgs-torus-link-triplet-table2-data) for the
sub-argument factorisation, and
[Table 3](#tbl:electroweak-higgs-torus-link-triplet-table3-data) for the
probe over $T(2, 2k)$, $k = 1 \ldots 7$ (every row PSD-passes; selection
of rows $2$–$4$ is C1–C4, not PSD).

**What the conjecture would close.**

If true, the identification supplies the missing categorical structure for
the weak-scale crossing count $N_v$ in the Fermi-constant decomposition
$G_F = 1/(\sqrt{2}\,v^2)$, $v = N_v\,E_\times\,\mu_0$ — the **NV-1** audit
flag ([NV-1 / FROB-FILTER conjectures, 2026-05-02](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-02-nv-frob-filter-conjectures.md)).
The residual to close is now just C1 (selection) and C$_{\text{sector}}$ (the
sector assignment); the enumeration and far-commuting minimality are
discharged to
([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding))
and
([thm:ew-triplet-far-commuting-minimal](#thm:ew-triplet-far-commuting-minimal)),
and charge and spin (the former C3, C4) to
([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)).
