# Gap G5: what forces more than one bond per nucleon, and what it gives

**Date** 2026-11-27 · **Gap** G5 of the term-completeness ledger (#9658) · **Epic** `qou-myts`
**Lean** [`QOU/MassTheory/NucleusBondValence.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/NucleusBondValence.lean): sorry-free, lean-direct exit 0 (`-DautoImplicit=false -s 65536`), `#print axioms` = `[propext, Classical.choice, Quot.sound]` on the five main theorems, generic field, no measured value.
**Probe** [`computations/probes/nucleus_bond_valence/`](../../computations/probes/nucleus_bond_valence/): pre-registration (5/5, AME not read) committed before the comparison script was written.
**Scope** (a) for every number; (b) only where a Lean theorem is cited.

## 0. Result in one paragraph

Nothing in the corpus forces a 3D braid word **through the layout**: the Artin encoding forces the
chain, and the band reading admits every layout while the confinement SDP selects the same words
(both already proved or measured on `main`, §1). The count has to come from the selection rule.
The ruled bond is attractive at `q₀` (`0 < z − h/2 = 0.508 < 1`), so energy minimisation (owner
ruling 2026-11-22) takes the most bonds the structure allows, and a bounded count above one bond per
nucleon then needs a **valence cap**. The corpus has exactly one cap above the chain as a Lean object:
the colour valence `N_c = 3` of the `⁴He` Tait construction. Pre-registered as **T3**, it gives
`3⌊A/2⌋` bonds, **1.5 per nucleon**. Compared afterwards with AME, T3 reaches **47 % (α) / 53 % (E₀)**
of the measured binding for `A ≥ 16`, against 31 % / 35 % for the chain. It is a derived, honest
miss: about half the bonds AME needs at this bond value. The cap that would match (one bond per strand
**end**, 3 per nucleon) has no corpus object and is recorded as selection against the target.

## 1. What the corpus already settles (corpus-grep)

| fact | carrier | scope |
|---|---|---|
| Artin linear layout ⇒ bond graph is the path, `A − 1` bonds | `LinearLayoutNoBulk.card_edgeFinset_eq` | (b) |
| the Artin γγ vertex forces the contiguous layout uniquely | `GammaGammaForcesTheLayout` (27 decls) | (b) |
| band (BKL) reading admits every layout; SDP selects `β_Bor`, `G³` at `H₃`, `H₆` either way | 2026-09-14 audit, R4–R6 | (a) |
| the Frobenius pairing normalises to `tr_M(1) = 1`, adds no count | audit 2026-07-11 Part 4 | (a) |
| complete graph excluded at `A ≥ 5` | Pauli closure `Λ⁵(Fin 4) = 0`; `MaxContactSimplex` | (b) |
| `K₅` cannot carry one bond per quark (`deg 4 > 3 = N_c`) | `TetrahedralFluxRingAndMajoranaCluster.k4_tait_bijection_and_k5_obstruction` | (b) |
| deltahedron `3A − 6` | `gap1_max_contact_a5plus.py`, imported geometry | (a) |

So the layout question is closed in both readings, and the 2026-09-14 audit's conclusion stands:
a non-contiguous layout is not derived under either reading. What is new here is to move the question
from the layout to the selection rule, where a cap can act.

## 2. The selection argument

With bond value `b > 0` and an additive count, `B = b·M`, so energy minimisation maximises `M`
under whatever cap holds (`binding_le_of_card_le`). Two consequences are immediate:

* **No cap**: the complete graph, `C(A, 2)`, quadratic. Excluded at `A ≥ 5` (§1).
* **A repulsive bond** would select a spanning tree, `A − 1` bonds, the chain's count.

So a count with a finite number of bonds per nucleon above one comes from a cap of degree `k ≥ 3`,
and then `M ≤ kA/2` (`two_mul_card_le_of_valence`, `perNucleon_le_of_valence`). The chain is the
`k = 2` member.

## 3. The caps, and what each forces (pre-registered)

| premise | cap | source | `M(A)` | per nucleon |
|---|---|---|---|---|
| chain | Artin layout, `k = 2` | proved | `A − 1` | → 1 |
| **T3** | one bond per quark, bonds colour-labelled | Tait object on `K₄` (Lean) | `3⌊A/2⌋` | → 3/2 |
| V3 | one bond per quark | same file, degree only | `⌊3A/2⌋` | → 3/2 |
| V6 | one bond per strand end | **none** | `3A` | → 3 |
| planar | triangulated 2-sphere | imported geometry | `3A − 6` | → 3 |

T3 is the bound `card_le_of_proper_colouring` (each colour class is a matching); V3 is the handshake
bound. They differ by one bond at odd `A ≥ 5` (`tait_vs_valence`): the colour label forbids the
overfull graphs. Both bounds are attained by connected graphs for every `A = 2…60` (probe check 1),
and they equal the exhaustive maximum over all simple graphs for `A ≤ 6` (check 2). At `A ≤ 4` T3
reproduces the corpus's own `K_A` bond graphs (1, 3, 6 bonds).

T3 was pre-registered **before** the comparison, on the stated ground that it is the only cap above the
chain that is already a corpus object.

## 4. Comparison with AME (after pre-registration; comparison only)

Ruled `T_z`-even bond, proton pin: `−ln(z − h/2) = 0.676963077`, `b = 2.5348609` MeV at `α = 8 m_e G`,
`2.8618501` MeV at `E₀` (tower). AME2020 experimental entries, total binding (it includes Coulomb and
asymmetry, which the strong count does not model).

| nuclide | AME B (MeV) | bonds/nucleon AME needs (E₀) | chain | **T3** (α) | **T3** (E₀) | V6 (E₀) |
|---|---|---|---|---|---|---|
| ²H | 2.2246 | 0.389 | 1.287 | 1.140 | 1.287 | 1.287 |
| ³H | 8.4818 | 0.988 | 0.675 | 0.897 | 1.012 | 1.012 |
| ³He | 7.7180 | 0.899 | 0.742 | 0.985 | 1.112 | 1.112 |
| ⁴He | 28.2957 | 2.472 | 0.303 | 0.538 | 0.607 | 0.607 |
| ¹²C | 92.162 | 2.684 | 0.342 | 0.495 | 0.559 | 1.118 |
| ¹⁶O | 127.62 | 2.787 | 0.336 | 0.477 | 0.538 | 1.076 |
| ⁴⁰Ca | 342.05 | 2.988 | 0.326 | 0.445 | 0.502 | 1.004 |
| ⁵⁶Fe | 492.26 | 3.072 | 0.320 | 0.433 | 0.488 | 0.977 |
| ²⁰⁸Pb | 1636.4 | 2.749 | 0.362 | 0.483 | 0.546 | 1.091 |

Ratios are `B_pred / B_AME`. Over the 2484 experimental nuclides with `A ≥ 16`:

| premise | mean ratio, α | mean ratio, E₀ | sd (E₀) |
|---|---|---|---|
| chain | 0.310 | 0.350 | 0.022 |
| **T3** | **0.467** | **0.527** | 0.035 |
| V3 | 0.469 | 0.529 | 0.035 |
| V6 | 0.939 | 1.060 | 0.070 |
| planar | 0.919 | 1.037 | 0.065 |

Readings, all scope (a):

1. **T3 is half of AME, flat in A.** The ratio's spread over `A ≥ 16` is 3.5 % of its mean, so the
   shortfall is a bulk factor of about 2, not a missing surface term. At this bond value AME needs about
   3 bonds per nucleon; the colour valence supplies 1.5.
2. **V6 and planar land near 1.** That is the warning in the pre-registration coming true, not a
   result: neither cap has a corpus derivation, so choosing either now would be selection against the
   target. What would make V6 a derivation is a corpus reason for a bond to consume a strand *end*
   rather than a strand (for example, a bond as a band joining one nucleon's outgoing end to another's
   incoming end in the closed braid). No such object exists yet.
3. **The light nuclei.** `A = 3` lies between −10 % and +11 % under T3; ⁴He is 54–61 %, and ²H over-binds by
   14–29 % with one bond. These are the same light-nucleus features the chain law already shows, so the
   cap does not change them.

## 5. What this changes for the other gap threads

* **Extensive binding (#9618, #9587).** The merge-count thread measures how many merges a word can
  carry at `A = 3`; T3's `A = 3` count is 3 bonds (the triangle), which is the complete graph there.
  The cap first differs from the complete graph at `A = 5`.
* **Coulomb (G3, #9691).** The EM column subtracts on top of whatever strong count is used. T3's strong
  count is about half of AME, so adding Coulomb (which reduces binding) moves the T3 ratios further
  below 1, not toward it.
* **Isospin `T(T+1)` (G2).** T3 fixes the count, not which pairs are `pp`, `nn`, `pn`. That assignment,
  and hence the twist orientation the isospin thread needs, is not fixed by the cap and is left open.

## 6. Open

1. A corpus reason for a bond to consume a strand end (V6), or a second bond per quark. Until then G5
   is half closed: the count is derived, the value is half of AME.
2. The pp/nn/pn assignment on a T3 graph (needed by the isospin and Coulomb threads).
3. Whether the band-reading confinement SDP at `H₉` admits T3 words (`A = 3` is the triangle, 27
   inter-nucleon bands in `B₉`; the 2026-09-14 audit's open item 1).
