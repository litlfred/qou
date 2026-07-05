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
$1, 2, 3$, and co-embed in Bring's genus-$4$ fiber alongside the
saturating carriers — is discharged to the sorry-free proposition
([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)).
What remains conjectural is the *identification itself*: which link is
which particle. That rests on three sub-conjectures, formalised as §3b
classes in the sibling Lean file and summarised below.

**The conjecture lattice.**

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| **C1** selection | primary | — | EW carriers are the nontrivial, strictly sub-saturating even-twist links ($0 < g < 4$) |
| **C2** enumeration | dependent (C1) | C1 | those carriers are exactly $\{T(2,4), T(2,6), T(2,8)\}$ |
| **C3** charge | primary | — | which link is the charged $W^\pm$ versus the neutral $Z, H$ |
| **C4** spin | primary | — | scalar $H$ versus vector $W, Z$ |
| **C$_{\text{top}}$** identification | dependent (C1, C3, C4) | C1, C3, C4 | the full map above |

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

**C3 — charge discriminator (OPEN).**

A link's Seifert genus does not see electric charge, so no
genus/embedding argument distinguishes the charged $W^\pm$ from the
neutral $Z, H$. C3 states the hypothesis that the minimal-genus carrier
($k = 2$) is charged and the two higher carriers ($k = 3, 4$) neutral, to
be derived — if at all — from bar-self-duality / amphichirality data
([bar T-duality of the substrate](#prop:bar-t-duality-substrate)), not
from the link genus. This remains open.

**C4 — spin discriminator (OPEN — the deepest gap).**

Link and genus data are spin-blind: nothing in the torus-link topology of
$T(2, 2k)$ determines whether the carrier is a scalar or a vector. C4
states the hypothesis that $W$ and $Z$ are spin-$1$ vectors while $H$ is a
spin-$0$ scalar. This is not addressed by any argument in the embedding
proposition and is the deepest residual of the whole identification.

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
The residual to close is exactly C1 (selection), C3 (charge), and C4
(spin); the enumeration and embedding are already discharged to
([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)).
