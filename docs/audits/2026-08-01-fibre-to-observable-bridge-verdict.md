# Fibre→observable bridge for c₃: is the c₃-via-Borel route mis-targeted? — VERDICT

**Date:** 2026-08-01
**Axis:** c₃ / Q_β bar-odd swing / 1ppQ; fibre-vs-observable wall
**Tier:** assessment + synthesis. scope-(a)/(b) classified. **No fit, no c_k
value claimed, nothing wired, no tier change.**
**Trigger:** program-roast §4 "load-bearing gate" — the c₃-via-Borel program
built a rigorous scaffold (5₂ AK integral, GGM/FW Stokes matrices, Lean bricks)
around the *resurgent* structure, which lives at **q = root of unity / |q|→1
(fibre)**, while c₃ is an **archimedean** coefficient at fixed real q₀ ≈ 1.1097
(observable). Is there an established bridge, or is the whole route mis-targeted?

> This is a **corpus-first synthesis** (per AGENTS.md §"Before declaring 'open'").
> The corpus has already worked this bridge extensively; the deliverable reads
> and classifies what is closed vs open, and does **not** re-derive. Every
> factual "open"/"closed" call below is grounded in an existing audit, content
> block, Lean file, or probe.

---

## One-line verdict

**(b) PARTIALLY on-target.** The route is **not** mis-targeted (roast option (c)
would be a scope-(b) over-claim the corpus refutes): there *is* a named,
literature-established bridge — quantum modularity / the Ohtsuki-tower expansion
at the imaginary substrate / median resummation — and the corpus has it
Lean-scaffolded sorry-free and **independently forced the c₃-odd channel onto
exactly this resurgent / complex-volume home** via a Lean-proved rigidity prune.
But the bridge is **incomplete for the value**: (i) **c₃-even is already
substrate-solved and never needed Borel**; (ii) for **c₃-odd** the smooth Borel
sum is **anchor-blind** (supplies no swing), the anchor-dependent piece is a
**CAL-2 calibration input** (its derivation is Subgoal-2, not a resummation),
and the exact-integer Stokes identification (`A_ω = 3`) is **explicitly open**.

---

## 1. What is the bridge, precisely?

The "fibre → observable" passage is **not analytic continuation** of a fibre
value to real q₀. It is one of two established, related mechanisms, and the
corpus instantiates both:

### 1a. Quantum modularity / the Ohtsuki tower at the imaginary substrate — the *primary* named bridge

The colored-Jones / complex-volume asymptotic series around a root of unity is a
**quantum modular** object (Zagier 2010; Garoufalidis–Zagier). Its all-orders
expansion is the Ohtsuki tower. The QOU substrate evaluation makes this concrete
and **Lean-proved sorry-free**
([`mass-theory/rem-ohtsuki-tower-bar-parity.md`](../../content/quantum-observable-universe/mass-theory/rem-ohtsuki-tower-bar-parity.md),
[`OhtsukiTowerBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/OhtsukiTowerBarParity.lean)):

$$
\mathfrak{V}_b = \mathfrak{V}_0 + \sum_{n\ge 1}\kappa_n\,(2\pi b^2)^n,
\qquad \kappa_n \in \mathbb{Q}(\sqrt 3)\cdot \pi^{\lceil n/2\rceil},
$$

with the substrate fluctuation variable **imaginary**:
`b = √(log q₀/2π)·e^{iπ/4}`, so `2πb² = i·t`, `t = log q₀ ∈ ℝ`. This *is* the
fibre-object-evaluated-at-q₀ map (AGENTS.md §"Im(q) at fibre vs observable
level"): the fibre object (the root-of-unity Ohtsuki asymptotics, real `κ_n`)
evaluated at the real substrate direction `t = log q₀`. The parity split is the
`𝔙 = Vol + i·CS` decomposition, proved sorry-free (`even_rung_real`,
`odd_rung_imaginary`): **even rungs → Re 𝔙 = Vol (bar-even mass face); odd rungs
→ Im 𝔙 = CS (bar-odd S / decay face).**

### 1b. Median resummation — the rigorous "recover the value from the asymptotics" map

McSpirit–Rolen ([`library/arxiv-2505.00799v2/2505.00799v2.pdf`](../../library/arxiv-2505.00799v2/2505.00799v2.pdf),
*Quantum modular forms and resurgence*, 2025) prove **median-resummation-type
results** showing Zagier's holomorphic quantum modular forms **can be recovered
from their (divergent) asymptotics**. This is the literature-established sense in
which the resurgent/Stokes data of a fibre series *determines a real-analytic
value* — the honest name for "a bridge." Wheeler et al.
([`library/arxiv-2304.07001v3/2304.07001v3.pdf`](../../library/arxiv-2304.07001v3/2304.07001v3.pdf), *Resurgence,
Habiro elements and strange identities*, 2025) supply the fibre-side half: they
prove resurgence of the **Borel transform** of the formal series attached to
**Habiro-ring elements** arising from **radial limits of partial theta series via
strange identities** — i.e. the Habiro element ↔ root-of-unity asymptotics ↔
Borel/Stokes chain is a theorem, not a hope.

### 1c. Does the α_EM Habiro precedent already instantiate the bridge? — Yes, but only for the structurally-fixed even sector

[`braids-and-knots/alpha-em-habiro-bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md)
/ [`.lean`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.lean):
`H(q) = [2]_q(1 − h²α)` is a **bar-involution fixed point** (`H(q⁻¹)=H(q)`,
sorry-free `alphaEmHabiro_bar_invariant`) whose **root-of-unity evaluations**
give the observable content: `H(ζ₁)=H(1)=2` (classical `α/4π` leading term),
`H(ζ₄)=0` (the modular pole dual to Q_β). This is a genuine "fibre object whose
evaluation at special q reproduces an observable" — the pattern the roast asks
about. **But it is confined to the bar-EVEN, charge-conjugation-symmetric sector
and its content is structurally fixed** (a Laurent element with integer
coefficients); it does not carry an anchor-dependent archimedean scalar. It is
the template, not the c₃-odd solution.

**Summary of item 1.** The bridge is real, named, and multiply instantiated:
quantum modularity (Ohtsuki tower at the imaginary substrate, Lean-proved),
median resummation (McSpirit–Rolen, recovers the value from asymptotics), and
the Habiro-element↔strange-identity resurgence chain (Wheeler et al.). The α_EM
Habiro precedent instantiates it for the even sector.

---

## 2. Is c₃ reachable? — split the two channels

### 2a. c₃-EVEN — CLOSED, and it never needed the Borel bridge

Per [`2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
§1: the bar-even channel of `log R` is a **substrate-exact ℚ(√3) ũ-ladder**
(`e₁ = 3√3/4, …`), **over-determined with margin 9, every residual order exactly
zero through s¹⁷**. It carries **no archimedean leak** — the `√3` is the
substrate's own hexagonal/ζ₃ constant, categorical, not an experimental input.
The companion archimedean face is exact too: the 4₁ bar-even Habiro-tail action
= **π²/5** (a ℚ(√5) golden constant, merged `b3ix`; cross-ref
[`2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md`](2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md)).

In the Ohtsuki-tower language (§1a) the even sub-tower feeds **Re 𝔙 = Vol**, the
**anchor-blind** volume/mass channel. So "c₃-even solved via complex-volume
rigidity" covers exactly: *the even channel is a substrate-exact rational (ℚ(√3))
ladder with no calibration content, whose archimedean face is an elementary
dilog constant (π²/5); it lands in the real, anchor-blind even sub-tower of the
complex volume.* **c₃-even does not require, and is not blocked on, the Borel /
resurgence bridge.** It is categorical, full stop.

### 2b. c₃-ODD — the genuine gap, with a sharp two-part structure

The odd channel factors `c₃^odd = κ_(2,1)(q)·S` with the **derived pure-q bar-odd
carrier** `κ_(2,1) = (q−1)³(q+1)/q²` (fibre, sorry-free, #2240) times a **single
archimedean scalar** `S = Q_β/E₀`
([`2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
§2). Two corpus facts pin its status:

- **The smooth part of S is Borel-recoverable — but anchor-BLIND.**
  [`rem-ohtsuki-tower-bar-parity.md`](../../content/quantum-observable-universe/mass-theory/rem-ohtsuki-tower-bar-parity.md):
  the odd sub-tower feeds `Im 𝔙 = CS`, is factorially divergent (Gevrey-1), and
  its **Borel–Padé resummation at the imaginary substrate is single-valued** —
  the Borel singularity sits at the *real* action `A = Vol(4₁)/π ≈ 0.646`, **off
  the imaginary integration ray**, so there is **no Stokes ambiguity and no
  exponentially small trans-series**. Resurgence returns the exact **smooth**
  `Im 𝔙 ≈ 0.055` plus the action cross-check, but **supplies no
  anchor-dependent piece** (probe `qbeta_c3_borel_pade_resummation_probe.py`).
  So the Borel route *does* deliver a rigorous real-q₀ value — but it is the
  smooth, anchor-blind geometric CS, **not** the c₃ cross-anchor swing.

- **The anchor-dependent piece of S is forced onto the quantum complex volume,
  and is a CAL-2 input.** `S` swings **2.375 %** across the proton/muon anchors
  (`dc₃/dq ≈ 4.6×10⁶`;
  [`2026-07-06-c3-not-exact-cross-anchor-verdict.md`](2026-07-06-c3-not-exact-cross-anchor-verdict.md),
  the 6th settle). It is **Lean-proved sorry-free** *not* to be a pure function
  of any anchor-invariant datum
  ([`SRigidityPrune.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean),
  `no_anchor_invariant_realizes_swing`), which **excludes** every fixed CAL
  constant and every classical topological invariant and **forces** the
  anchor-dependent **quantum** complex volume `𝔙_q(K)` (Faddeev `Φ_b`),
  `conj:binding-qbeta-complex-volume`. And `S = Q_β/E₀` carries
  `Q_β = ℏ/𝔇_β = CAL-2`, a **calibration input** — so *deriving* S ⟺
  substrate-deriving CAL-2 = **Subgoal-2** (owner-declined 2026-05-08, **generally
  reversed / open-for-all 2026-07-11**; the anti-fit discipline still gates
  *how*, not *whether*).

**c₃-odd is therefore the genuine gap.** Its home is exactly the resurgent /
complex-volume route — the corpus *forced* it there by a proved invariant, not
by choice. What remains open is the **anchor-dependent** content, which the
smooth Borel sum does not carry, and whose ultimate origin is a CAL-2 input.

---

## 3. Verdict on the roast's premise — (b) partially on-target

The roast's fibre-vs-observable distinction is **correct and load-bearing**: the
resurgent structure genuinely lives at roots of unity / |q|→1, and c₃ is
genuinely an archimedean coefficient at real q₀. But its implied worry — that
this makes the c₃-via-Borel route **mis-targeted** — is **too strong** and the
corpus refutes it:

| roast option | verdict | evidence |
|---|---|---|
| (a) fully on-target, real bridge delivers the c₃ value | **NO** | c₃-odd's anchor-dependent value is not in the smooth Borel sum (anchor-blind), is forced onto `𝔙_q` but ultimately anchored on CAL-2 (Subgoal-2), and `A_ω=3` is explicitly open |
| **(b) partially on-target (even yes, odd open)** | **YES** | even: substrate-exact ℚ(√3)/π²/5, needs no Borel; odd: resurgent/complex-volume home is Lean-*forced* (`SRigidityPrune`), rigidity Lean-scaffolded, but value incomplete + CAL-anchored |
| (c) mis-targeted — no bridge | **NO (scope-(b) over-claim)** | a named bridge exists (quantum modularity / median resummation / Ohtsuki tower at imaginary substrate), is Lean-proved sorry-free for the parity split, and the odd channel is *independently forced* onto exactly this home by a proved invariant |

**Why not (c).** Declaring the route mis-targeted would assert an ingredient is
excluded from any closure — a scope-(b) structural exclusion — with **no proved
invariant forbidding it**. The opposite is true: a proved invariant
(`no_anchor_invariant_realizes_swing`) *forces* the anchor-dependent S onto the
`Φ_b` quantum complex volume, i.e. onto the resurgent object. The correct
scope-(a) statement is: *the smooth Borel resummation of the 4₁ complex-volume
tower, alone, does not reproduce the c₃ cross-anchor swing — it returns the
anchor-blind geometric CS ≈ 0.055.* That constrains a magnitude/combination, not
the ingredient.

**Why not (a).** Three concrete, corpus-recorded incompletenesses stand between
the scaffold and a delivered c₃-odd value:

1. **Anchor-blindness of the smooth sum** (§2b, first bullet) — the swing is not
   in the resurgent data of the 4₁ tower.
2. **The un-measured categorical Stokes datum `A_ω` (the G3 keystone).** The
   Q_β/Φ_b odd-face passage is a **categorical Stokes/monodromy datum** (irregular
   q-difference connection), not a resummation constant
   ([`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md)).
   The anti-fit derivation target is the **exact integer** Stokes constant
   (GGM `S⁰=[[1,0],[−3,1]]`, integer **3** = a Donaldson–Thomas/3d-index count),
   **not** a float from finitely many rungs — and its identification with the
   corpus `A_ω` normalization is **explicitly not claimed** (open, falsifiable).
3. **S is a CAL-2 input** (§2b, second bullet) — deriving it is Subgoal-2, so
   even a perfect bridge would *identify* S with a known invariant, not *derive*
   it free of the calibration.

**Net.** The scaffold (5₂ AK integral, GGM/FW Stokes matrices, Lean rigidity
bricks) is built around the **correct** object. It is over-built for the
**even** channel (already closed without it) and **correctly targeted but
incomplete** for the **odd** channel (home Lean-forced; value blocked on the
integer-Stokes identification and, beneath that, a CAL-2 input). That is (b).

---

## 4. Lean-formalizable structural sub-claim — already covered; the genuine gap is beaned, not axiomatized

The item-4 candidate — *"the archimedean evaluation of the bar-involution-
symmetric fibre object is real"* — is **already established in the corpus,
sorry-free**, and adding another brick would be redundant or near-vacuous:

- **Bar-symmetry of the fibre object:** `alphaEmHabiro_bar_invariant`
  (sorry-free, generic `CommRing`).
- **Realness of the even face / imaginariness of the odd face:** `even_rung_real`
  / `odd_rung_imaginary` in
  [`OhtsukiTowerBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/OhtsukiTowerBarParity.lean)
  (sorry-free over ℂ) — this *is* the "archimedean evaluation of the
  bar-symmetric object splits into a real (even) and imaginary (odd) part" claim,
  proved.
- **Im(q₀)=0 at the observable evaluation:** the archimedean constraint
  `lusztig_q_0_imaginary_part_zero` (asserted in
  `four_unwired_theorems_regression.py`).

A fresh "realness of a bar-symmetric Laurent element at real q" theorem would be
a real-polynomial triviality (`Real` coefficients ⇒ real value), adding no
content beyond the above. **Per the anti-laundering discipline, the genuinely
open Lean piece must NOT be axiomatized to "close" the bridge.** The honest
division (from
[`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md)
§8–10) is already recorded and largely landed:

- **Landed sorry-free:** `monodromy_datum_rigidity` (every scale-invariant readout
  of any `FaddeevPhi` solution is identical ⇒ `A_ω` carries **zero fitting
  freedom**); the elliptic-Liouville step (upstream `DoublyPeriodicLiouville.lean`);
  `hspan` (`exists_period_basis`); the reduction `uniqueUpToScalar_of_entire`.
- **Genuinely open (do NOT axiomatize):** (i) `hratio`/entireness — `Φ_b`
  holomorphicity + divisor cancellation of two solutions (bean `qou-2cvs`);
  (ii) `hibinv` — the `i/b`-period identity-theorem extension (bean `qou-q95i`);
  and (iii) the physics content — the **integer-3 Stokes identification**
  `A_ω = 3` (DT/3d-index count), which stays falsifiable and unclaimed.

**Decision:** no new Lean brick this pass (it would be redundant or a
laundering risk, and the olean-restore budget is better left unspent per the
session budget note). The open pieces are **precisely beaned** (below).

---

## Beans

- **`qou-2cvs`** (existing) — G3 endowment `hratio`: `Φ_b` holomorphicity +
  divisor cancellation ⇒ ratio entire. Hard real math; do not axiomatize.
- **`qou-q95i`** (existing) — G3 `hibinv`: `i/b`-period identity-theorem
  extension off the dual pole lattice.
- **NEW (file):** *integer-Stokes identification `A_ω = 3`* — derive the exact
  GGM Stokes constant as a Donaldson–Thomas / 3d-index integer count and identify
  it with the corpus `A_ω` normalization (`Im 𝔙 → N_odd`). Anti-fit target: an
  emergent integer, never a float from finitely many rungs. Explicitly the
  physics-content leg of the c₃-odd bridge; falsifiable; currently open.

## Discipline / scope notes

- **No open-item over-declaration.** Every "open" here (c₃-odd value, `A_ω=3`,
  `hratio`, `hibinv`) is grounded in an existing audit/ledger; the corpus-grep
  checklist was run (audits, content, computations, coordination) and returns
  the same open frontier.
- **No refutation over-claim.** "The route is mis-targeted" is rejected as a
  scope-(b) over-claim; the scope-(a) statement (the smooth Borel sum alone does
  not reproduce the swing) is what the evidence supports.
- **No fit, nothing wired, no tier change.** Q_β stays c₂-only in production
  (the honest ≈1279 ppb prediction); c₃-odd remains cal-anchored/circular and
  must not be wired (canonical-mass guardrail).

## Cross-references

- Roast §4 gate (this doc answers it); roast bean `qou-q8j6` (same 2026-08-01
  roast session).
- [`2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
  — c₃-even substrate-exact; S rigidity prune.
- [`rem-ohtsuki-tower-bar-parity.md`](../../content/quantum-observable-universe/mass-theory/rem-ohtsuki-tower-bar-parity.md)
  — the Ohtsuki-tower bridge at the imaginary substrate; anchor-blind Borel sum.
- [`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md)
  — the odd-face categorical Stokes datum; integer-3 target; rigidity ledger.
- [`2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md`](2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md)
  — Habiro element evaluated at the boundary of its analyticity.
- [`2026-06-13-qbeta-root-of-unity-residue-program.md`](2026-06-13-qbeta-root-of-unity-residue-program.md)
  — root-of-unity residue over-determination; ζ₄ relaxed; parity-alternation.
- [`2026-08-01-arrow-a-stateintegral-saddle-not-index-series.md`](2026-08-01-arrow-a-stateintegral-saddle-not-index-series.md)
  — the volume-route resummation is the state-integral saddle (shared geometric
  datum), sibling of the odd-face question.
- Papers: [`library/arxiv-2505.00799v2/2505.00799v2.pdf`](../../library/arxiv-2505.00799v2/2505.00799v2.pdf)
  (McSpirit–Rolen, median resummation);
  [`library/arxiv-2304.07001v3/2304.07001v3.pdf`](../../library/arxiv-2304.07001v3/2304.07001v3.pdf) (Wheeler et al.,
  Habiro elements ↔ resurgence ↔ strange identities).

-- Ref: [manuscript] docs/audits/2026-07-07-c3-even-solved-s-complex-volume-rigidity.md
