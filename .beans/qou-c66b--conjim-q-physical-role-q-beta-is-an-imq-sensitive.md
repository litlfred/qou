---
# qou-c66b
title: 'conj:im-q-physical-role: Q_beta IS an Im(q)-sensitive observable already in the framework — the conjecture''s stated obstacle is wrong'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T10:42:33Z
updated_at: 2026-09-05T10:06:07Z
---

Parent: `conj:im-q-physical-role`. Reached from `qou-pdix` route 5 (the elliptic
generator) on the author's instruction to chip away at where the imaginarity
comes from.

## The conjecture's stated obstacle

`content/quantum-observable-universe/mass-theory/conj-im-q-physical-role.md`,
§"Obstacles to a current proof":

> *The framework's mass formula explicitly **projects away** Im(q) content via
> `|·|`, so **no mass observable** can detect Im(q) directly. The candidate roles
> are all in **non-mass observables**.*

and candidate (iii)'s test is listed as needing *"a categorical formula for decay
widths Γ"* — i.e. the framework is said not to have an Im-sensitive observable yet.

## Measured: Q_beta already is one

`Q_β/m_e = |q² − 2q − 1| · (q+1) / (2q³)` (AGENTS.md cheat sheet). **The modulus
sits on ONE factor.** `(q+1)/(2q³)` is not under it, so the modulus projection
that makes the mass formula Im-blind does not apply to two of the three factors:

    Im q        Q_b(q)                          Q_b(conj q)                |diff|
    0           1.5335566273 + 0j               1.5335566273 + 0j          0
    1e-6        1.5335566273 - 3.418016e-6j     ... + 3.418016e-6j         6.836e-6
    1e-3        1.53355190423 - 3.418010e-3j    ... + 3.418010e-3j         6.836e-3
    0.01        1.53308438987 - 3.417423e-2j    ... + 3.417423e-2j         6.835e-2
    0.139956    1.44367544417 - 0.462524635j    ... + 0.462524635j         0.925

Control, the mass shape `|f(q)|` — fully modulus-projected, invariant, diff
**exactly 0** at both Im q = 1e-3 and 0.139956.

So `Q_β(q̄) = conj(Q_β(q))`, and the sensitivity is **linear**:
`∂Im(Q_β)/∂Im(q) ≈ 3.418`.

## What follows, at the OBSERVABLE level

`Q_β` is experimentally a real Q-value in MeV. Requiring `Im Q_β = 0` therefore
forces `Im q = 0` — the same conclusion `character_im_zero_iff` reaches from the
Kohno–Drinfeld character, but reached from a **decay** observable and from the
`Q_β` formula rather than from the holonomy.

Two consequences, and the second is the useful one:

1. The conjecture's obstacle statement needs correcting. It is not the case that
   the framework lacks an Im-sensitive observable; candidate (iii)'s test is
   *partially runnable now*, on `Q_β`, without a categorical Γ.
2. The answer it gives is a **constraint, not a discovery**: `Im q = 0` at the
   observable level. That corroborates the framework's default from a third
   independent direction and pushes all three candidate roles firmly to the
   **fibre** level — which is where `qou-cds1` already says a D-frame story must
   live ("must first close a FIBRE-level construction").

## 🛑 The caveat, and it is load-bearing

**The complex extension of `Q_β` used here is MINE, not the corpus's.** That
formula was derived for real `q`, where the `|·|` is a sign fix — `q² − 2q − 1`
is negative at `q₀` and `Q_β` must be positive. Extending to complex `q` by
keeping the modulus on that one factor and nothing else is *a* reading, and the
Im-sensitivity is entirely an artefact of which factors the projection covers.

So the honest statement is conditional: **any complex extension of `Q_β` that
preserves the formula's shape is Im(q)-sensitive, because only one of its three
factors is modulus-projected.** Whether that extension is the canonical one is
itself unfixed, and fixing it is prerequisite to running candidate (iii)'s test
properly. What is NOT conditional is the correction to the obstacle statement:
the mass formula's Im-blindness comes from `|tr_M|` covering the whole
expression, and `Q_β`'s does not have that property under any reading.

Scope (a). Derives no `α`, adjudicates no convention, proposes no wiring.


---

## 2026-09-04 — MEASURED, and it CORRECTS the claim above

Branch `claude/im-q-physical-role-2026-09-04`. Probe
`computations/qbeta/qbeta_imq_reality_locus_probe.py` (8/8), Lean
`QOU/QBeta/ImQRealityLocus.lean` (lean-direct exit 0, 8 decls, no sorryAx),
audit `docs/audits/2026-09-04-imq-reality-locus-and-what-it-closes.md`.

### 🛑 The claim above is TOO STRONG

This bean asserted, without proof:

> "Requiring `Im Q_β = 0` therefore forces `Im q = 0`."

**One real equation on two real unknowns has a CURVE of solutions, not a
point.** The non-real branch is non-empty under both readings, and the Lean
carries two explicit counterexamples to the unqualified form
(`im_e2_locus_is_nonempty` at `(1/2, 1)`, `im_e1_locus_is_nonempty` at
`(−1/2, 1/2)`). The correct statement carries a hypothesis:

> On the substrate branch `Re q > 1/2`, `Im Q_β = 0` forces `Im q = 0`.

The qualifier is not cosmetic — without it the statement is false at `x = 1/2`.

### The caveat above is RESOLVED as an obstacle, not as a question

This bean flagged, correctly, that the complex extension of `Q_β` is the
agent's and not the corpus's. It still is. But the corpus's own block gives
**two** readings one line apart, and the answer is the same under both:

| | modulus covers | `Im Q_β = 0` zero set | non-real branch real for |
|---|---|---|---|
| E1 printed closed form (= live code, `qbeta_utils.py:293`) | one quadratic | `y·(2x³+3x²+2xy²−y²) = 0` | `x ∈ (−3/2,0) ∪ (0,1/2)` |
| E2 the derivation `\|Δ(net)\|·E₀` | `Δ(net)` only | `y·(2x−1) = 0` | `x = 1/2` exactly |

`Re q = q₀ ≈ 1.10998 > 1/2` is in **neither**. The third escape, the modulus
factor vanishing, gives `q = 1 ± √2` — both real.

E1 is E2 simplified *using* `q` real and `q > 1`, so extending E1 past that
hypothesis is exactly the shape AGENTS.md warns about under "defined residual ≠
derived decomposition". Running both is therefore the point rather than a
hedge — and the two loci are **disjoint**, so the extensions disagree about
where imaginarity is admissible everywhere *except* the substrate.

### Slope reproduced across the compaction boundary

The probe's `Im(Q_β/m_e)` at `Im q = 1e-6` is `−3.4180161e-6`, i.e. slope
`3.418` — byte-consistent with the `∂Im(Q_β)/∂Im(q) ≈ 3.418` measured in the
table above by a different route. E2's slope is `15.326`, different as
expected: the extensions are not the same function.

### What it closes

`conj:im-q-physical-role` candidate (ii) states its own test: *"if only real
solutions exist, candidate (ii) is closed."* Only real solutions exist on the
substrate branch, forbidden by a proved algebraic identity — **scope-(b)**,
citing `e1_branch_pos` / `e2_branch_pos`, not a numerical near-miss. And it
closes using an observable the framework already carries, so the conjecture's
"needs a second independent constraint" was already satisfied.

Candidate (iii)'s obstacle is **narrower than written**, not absent: the β
channel has its categorical decay observable; what is missing is `Γ` for the
other unstable states.

Candidate (i), chirality, is **untouched** and is now the only one of the three
with no closure argument from either direction.

Scoped to the ARCHIMEDEAN evaluation only. AGENTS.md's fibre-vs-observable
banner leaves `Im(q)` unconstrained on the fibre and nothing here touches that.
What is new is that `lusztig_q_0_imaginary_part_zero`'s archimedean `Im q₀ = 0`
now **follows** from a decay observable instead of being asserted.

### Still open (author's call, framed in the PR)

Whether to edit `conj-im-q-physical-role.md` itself — marking candidate (ii)
closed and narrowing candidate (iii)'s obstacle — is a verdict on the author's
conjecture, not a currency fix, so it is proposed rather than applied.


---

## 2026-09-04 (later) — CANDIDATE (i) TOO, and the corpus decides it

Branch `claude/imq-chirality-parity-2026-09-04`. Probe
`computations/qbeta/imq_chirality_is_the_bar_involution_probe.py` (5/5), Lean
`QOU/QBeta/ImQChiralityIsBarInvolution.lean` (lean-direct exit 0, 4 theorems, no
sorryAx).

### The identification candidate (i) makes is not the corpus's

Candidate (i): *"`arg q` is naturally a **chirality coordinate** … the mass
formula is invariant under `q ↦ q̄` … consistent with mass being
chirality-invariant."* So it identifies **chirality flip = complex conjugation**.

The corpus identifies it with the **bar involution `q ↦ q⁻¹`**, in three places:

- `archimedean-image-table-table1-data.md` row 4: *"J_K̄(q) = J_K(q⁻¹) (mirror;
  matter/antimatter CPT)"*
- `hq-bi-filtration.md`: *"Bar involution `∗ : q ↦ q⁻¹` … where `K*` is the
  **mirror knot**"*
- `knot-indexed-convolution-grid-table2-data.md`, same row

plus `knot-notation-convention.md`, which fixes the physics: the mirror flips
the writhe sign, and the weak isospin **is** that sign.

### They coincide EXACTLY on the unit circle — and the substrate is not on it

`q̄ = q⁻¹ ⟺ q·q̄ = 1 ⟺ |q|² = 1`, exactly (`conj_eq_inv_iff_modulus_one`).
Candidate (i) places itself *"near the unit circle"* (Kashaev `q = e^{2πi/N}`)
and **there it is right**.

Measured at the substrate: `|q₀| = 1.1099785827513808076 ≠ 1`; the corpus's
mirror is `q₀⁻¹ = 0.9009182839557414922`, a **real** number needing no `Im q`;
and the two flips sit `0.20906` apart, **18.83 % of `q₀`** — not a near
coincidence that could be waved away.

**So at the substrate the role candidate (i) proposes for `arg q` is already
carried, in full, by a real-`q` mechanism the corpus has developed in detail:
the bar involution's `P_avg`/`P_skew` split — which is `rem:im-q-vs-p-skew`,
the conjecture's OWN exclusions block.**

### Second leg: granting the identification anyway, it still collapses

Both `Q_β` extensions are (real ≥ 0 modulus) × (real-coefficient rational), so
Schwarz reflection gives `Q_β(q̄) = conj(Q_β(q))` — verified at residual **0.0**,
50 dps, 3 points × 2 extensions. Chirality-invariance says `Q_β(q̄) = Q_β(q)`.
The two pull in opposite directions, so `Q_β` is real, and
`im_qbeta_zero_iff_e2` forces `Im q = 0`.

🛑 **The premise is carried, not smuggled.** *"`Q_β` is chirality-invariant"* is
physics — a Q-value is a parity-even energy — so it is an explicit Lean
hypothesis (`hchiral`) beside the arithmetic one (`hschwarz`), never assumed
inside a proof. Leg one needs no premise at all: arithmetic plus three
citations.

### Status of the conjecture after both PRs

| candidate | archimedean status |
|---|---|
| (i) chirality | **closed** — the identification holds only on `|q| = 1`; the substrate is 18.8 % off it, and the corpus's own flip is real |
| (ii) phase coordinate dual to CAL-2 | **closed** on its entire Apollonius circle (PR #6639, merged) |
| (iii) non-Hermitian / open-system | obstacle **narrowed**: the β channel has its categorical decay observable; `Γ` for W/Z/top/resonances is what is missing |

All three scoped to the **archimedean evaluation**. The **fibre** is untouched
and is where the Kashaev regime actually lives — candidate (i) may well be right
there. And this is not a demotion of chirality: it says the chirality content
the conjecture went looking for in `Im q` is already in the corpus at real `q`,
as `P_skew`, which `rem:im-q-vs-p-skew` says is *"kept then discarded"* by the
canonical `P_avg` projection.


---

## 2026-09-04 (third) — CANDIDATE (iii): the stated obstacle is not the live one

Branch `claude/imq-decay-width-mechanism-2026-09-04`. Probe
`computations/qbeta/imq_decay_width_mechanism_probe.py` (5/5), Lean
`QOU/QBeta/ImQDecayWidthMechanism.lean` (lean-direct exit 0, 6 theorems, no
sorryAx).

### Its premise is correct, and I verified it rather than assuming it

The Hecke generator satisfies `(σ − q)(σ + q⁻¹) = 0`, spectrum `{q, −q⁻¹}`, and
`Im(−q⁻¹) = y/(x²+y²)` vanishes **exactly** where `y` does — no extra locus. So
`Im q ≠ 0` really is precisely the non-Hermitian deformation (iii) describes.

### The stated obstacle — *"needs a categorical formula for Γ"* — is wrong

`docs/canonical-derivation-cheat-sheet.md` lines 134 and 490: **`𝔇_β`, the
neutron β-decay width, IS CAL-2** — one of the three calibration inputs — with
`Q_β = ℏ/𝔇_β` and the closed form `m_e|q₀²−2q₀−1|(q₀+1)/(2q₀³)` in real `q₀`.
The decay sector is not a gap; it is a calibration, and it is real.

### Two mechanisms, and the framework uses the other one

| | width from | needs |
|---|---|---|
| **A** framework's | `𝔇 = ℏ/Q`, the **reciprocal** of a real energy | nothing complex |
| **B** candidate (iii)'s | `E = E₀ − iΓ/2`, the **imaginary part** | complex `q` |

On a real spectrum **B gives `Γ = 0` identically while A gives a nonzero
width**, and the framework sits in exactly that configuration: `Q_β =
0.783645827374621213` MeV at `Im q₀ = 0`, so `𝔇_β = 8.39935509011e-22 ≠ 0`.
They are not two descriptions of one thing.

### 🛑 Scope (a), and the Lean says so

`imaginary_mechanism_does_produce_a_width` is in the file deliberately:
mechanism B works fine when `Im E ≠ 0`. **Nothing here excludes `Im q` from
encoding a resonance width.** The burden is *relocated*: to keep (iii) alive one
must exhibit a `Γ` — W, Z, top, or a hadronic resonance — that mechanism A
demonstrably **fails** to produce. Sharper than the conjecture's own question,
and **left open**.

Second place the burden is owed: `AGENTS.md` §7b item 3 gives the corpus another
real-`q` account of exactly those states — unstable intermediaries as **Demazure
sub-crystals**, *"without ad-hoc decay machinery"*. Not verified numerically.

### 🛑 A units question in the corpus's own naming — reported, not resolved

`𝔇_β` is called a **width** (energy) while `Q_β = ℏ/𝔇_β ≈ 0.784 MeV` is also an
energy; `ℏ/(energy)` is a **time**. Both cannot hold. Either `𝔇_β` is a lifetime
and "width" is loose, or an `ℏ`-convention is implicit. It does not affect the
argument, which needs only that the two are reciprocal and `Q_β` real — but it
is the author's naming, so it is flagged and left alone. **Author's call.**

### All three candidates, after three PRs

| candidate | archimedean status | scope |
|---|---|---|
| (i) chirality | **closed** | (b) |
| (ii) phase dual to CAL-2 | **closed** on its whole Apollonius circle | (b) |
| (iii) non-Hermitian | **narrowed** — premise right, obstacle misidentified, burden relocated | (a) |

All three scoped to the **archimedean evaluation**. The **fibre** is untouched
throughout and is where the Kashaev regime lives.


---

## 2026-09-04 (fourth) — the conjecture block itself, retargeted to the fibre (owner picked A + B)

Branch `claude/imq-conjecture-retarget-fibre-2026-09-04`. The three earlier PRs
deliberately left the block untouched because editing it is a verdict on the
author's conjecture; the owner has now chosen both the scope note (A) and the
fibre retarget (B), so they land as one edit.

**What changed in `conj-im-q-physical-role.md`:**

1. **Opening** — the catalogue no longer says "open work". All three candidates
   are settled at `q_0` and all three stay open on the fibre, so the conjecture
   is restated as a fibre-level question.
2. **New section** `Reality of $\mathfrak{Q}_\beta$ at the substrate` — the
   three conclusions with scope and Lean carrier, plus why `Q_β` is the
   Im-sensitive observable the opening paragraph did not anticipate.
3. **Each candidate's `Testable`** retargeted to the fibre, keeping the
   superseded archimedean form visible rather than deleting it.
4. **Obstacles** — two of the three stated requirements were satisfied by
   observables *already in the corpus*; what survives is one obstacle and it is
   at the fibre.
5. 🛑 **`Default value: Im(q) = 0`** — this said *"**NOT structurally forced** …
   a convention pending an Im-sensitive measurement"*. That is now **false at
   the archimedean layer**: `im_qbeta_zero_iff_e2` derives it, and the
   measurement it was waiting for is `Q_β` itself. Split by layer — forced at
   `q_0`, not forced on the fibre. **This is the correction the block most
   needed**; left alone it would have kept asserting the opposite of a merged
   theorem.

**Candidate (ii) states its own closure condition** — *"if only real solutions
exist, candidate (ii) is closed"* — and that is exactly what #6639 proved. Quoted
in the block.

**QA.** `qa-sweep` clean of anything I introduced. One catch worth recording: my
first heading was `## Archimedean status`, which tripped `voice-status-section`
— a status label in prose, the §4d violation. Renamed to a noun phrase naming
the mathematics. `trap-nonspeakable` and `trap-superlative` fail both before and
after and are **pre-existing on main**, not mine; verified by diffing the
sidecar against `origin/main` rather than by reading the post-edit state alone.

**A measurement slip of my own, caught mid-check:** my first before/after
comparison read `status`/`verdict` but not `result`, and reported *zero*
failures on both sides against a true 2-and-3. Two scripts of mine disagreed and
the wrong one looked cleaner — the same field-name-assumption class as the
detector-blindness taxonomy's rows 22/25/26.


---

## 2026-09-04 (fifth) — 🛑 RETRACTION: `𝔇_β` is not a decay width, and (iii) returns to OPEN

Branch `claude/frakd-beta-is-not-a-decay-width-2026-09-04`. Probe
`computations/qbeta/frakd_beta_is_not_a_decay_width_probe.py` (5/5). This is the
owner-selected follow-up **D** — *exhibit a `Γ` the reciprocal mechanism fails to
produce* — and the exhibit turned out to be the neutron's own, which retracts an
interpretive claim I landed in **#6687** and repeated in **#6700**.

### What I claimed

That (iii) was narrowed because *"the framework's one canonical decay width
`𝔇_β` IS CAL-2, obtained at real `q₀`, so decay needs no `Im(q)`"*.

### Why it is wrong

The corpus asserts both that `𝔇_β` is the neutron β-decay **width** and that
`𝔔_β = ℏ/𝔇_β ≈ 0.784 MeV` is a **Q-value**
(`epistemic-status-of-calibrations.md:3`,
`three-calibration-discipline-discussion.md:7`, cheat sheet `:134`, `:490`).
A width and a lifetime are reciprocal **by definition**, so:

| reading | consequence |
|---|---|
| `𝔇_β := Γ_n` | `ℏ/𝔇_β = τ_n = 878.4 s` — a **time**, not 0.784 MeV |
| `𝔇_β := ℏ/𝔔_β` | `= 8.3993551e-22 s`, **24.0194 orders** from `τ_n` |

Equivalently `Γ_n = ℏ/τ_n = 7.4933055e-19 eV` sits **24.02 orders** below
`𝔔_β = 783645.83 eV`.

**`𝔔_β` and `Γ_n` are independent properties of one decay, not reciprocals**: a
Q-value is fixed by mass differences alone; a width also needs the coupling and
the phase-space integral. The framework computes the **energy release**, not the
**rate**.

### What stands and what does not

- **Stands** — `𝔔_β` as a CAL-2 proxy, reproduced to **0.16819 %** (matching the
  documented 0.17 %). Untouched.
- **Stands** — all the Lean of #6687. It is about two width *mechanisms* and is
  pure mathematics; nothing in it is affected.
- **Retracted** — the step from *"`𝔇_β` is CAL-2"* to *"the framework has a
  categorical decay width"*. **Candidate (iii) returns to OPEN**, with its
  obstacle sharpened: the missing object is not a decay observable but
  specifically the **rate**.

### 🛑 And a silent no-op in #6700 that I only found now

Of the seven edits #6700's body claims, **six landed and one did not**: the
Obstacles rewrite. My `str.replace` searched for `$\lvert\cdot\rvert$` where the
file has `$|\cdot|$`, so it matched nothing and I never verified. The PR body
describes a change that is not in the diff. Fixed here, and every replacement in
this pass is now verified as it is applied rather than afterwards.

By luck the un-replaced original text says *"(iii) needs a categorical formula
for decay widths Γ"* — which the retraction above makes **correct again**.

### Candidate status

| candidate | status | scope |
|---|---|---|
| (i) chirality | closed at `q₀` | (b) |
| (ii) phase dual to CAL-2 | closed at `q₀` | (b) |
| (iii) non-Hermitian | **OPEN** — obstacle stands, now sharpened to *the rate* | (a) |


---

## 2026-09-05 — decay as computational time (owner proposal), and the Demazure range test

Branch `claude/cal-cone-audit-and-frakd-tail-2026-09-05`, PR #6759.

### The owner's proposal survives, with one forced correction

Owner: *"decay rate in terms of computational time. no?"* The corpus already
holds the clock —
[`2026-07-11-planck-tick-disqualifier.md`](../docs/audits/2026-07-11-planck-tick-disqualifier.md)
fixes the per-operation tick at the **electron Compton time** 1.288e-21 s and
disqualified only the *Planck* value, not the notion.

On a **fixed** electron tick, `N_ops = τ/t_C` gives the **Z boson 2.05e-4** —
below one operation, which a decay-as-computation cannot be. Making the tick
particle-relative forces

`N_ops(K) = τ_K/t_C(K) = (ℏ/Γ_K)/(ℏ/m_K c²) = m_K/Γ_K`

the resonance narrowness: `≥ 1` by construction, and **dimensionless** — the
regime the 2026-08-11 ruling leaves open. Target: **25.535 orders**, Z 36.55 →
neutron 1.25e27.

### The Demazure/length route FAILS at order zero — scope (a)

Set `N_ops = q₀^L` with `q₀` pinned, so `L` is **determined, not fitted**:

| | L required | tower depth needed |
|---|---|---|
| Z boson | 34.49 | n ≥ 9 |
| tau | 262.48 | n ≥ 24 |
| muon | 387.23 | n ≥ 29 |
| neutron | 598.00 | n ≥ 36 |

The corpus assigns a nucleon **`B_3`** (`atomic-braid-recipe-n-canonical`), so
`ℓ(w₀) = 3`. The neutron needs ~598. **Short by 199.33×**, and no `w` inside
`S_3` helps — 3 is the ceiling. **A decay rate is not a reduction length of the
particle's own braid.**

The required depths are *tower* depths, consistent in **form** with the
2026-09-03 full-tower ruling. Consistency in form is **not evidence** and
nothing here derives them.

### 🛑 A near-integer that is NOT a result

The neutron gives `L = 598.002698` — 0.0027 from 598. **Not a hit.** The PDG
bottle σ alone gives `ΔL = ±0.0055`, and the unresolved beam–bottle spread
`±0.087`. The offset is inside the band; the input precision cannot support an
integer there. The other four are nowhere near integers (387.23, 347.39,
262.48, 34.49) — one coincidence in five samples. Recorded so nobody picks it
up later.

### Still open

Whether any Demazure incompleteness measure at tower depth `n ~ 9–36`
reproduces the ordering Z < τ < π < μ < n.


---

**2026-09-05 — CORRECTION to my own #6704 claim (PR #6823).**

#6704 closed with *"the missing object is not 'a decay observable' (the corpus
has one) but specifically **the rate**."* **Wrong.** `prop:hadron-half-life`
states a categorical decay rate

    Gamma_beta = |W(q)|^2 mu_0/(2 pi^3) * [2]_q * |M_q|^2 * f(Q),  f(Q) ~ Q^5

whose coupling is derived in closed form as the canonical Markov trace of the
T_{3,5} braid word in H_3(q): `W(q) = q^2(q^12+q^8-1)/(q^2+1)^2`. Verified at
60 dps — two spellings agree to 1.6e-61, `W(q_0) = 1.1874806131` (corpus quotes
1.1875), `W(1) = 1/4` exactly. See also bean `qou-egvf`, which had already
derived this closed form; I re-derived it without finding that bean first.

**What is actually open is the rate's SCALE, not its shape.** The weak-scale
crossing count `N_v` in `v = N_v E_x mu_0` is undetermined, so `G_F` enters
numerically from experiment — stated already in the `all_six_agree` docstring,
in `hadron-half-life-verification` Table 1, and in
`_deprecated/t35-transfer-matrix.py:281`.

**Measured** (`weak_scale_crossing_count_nv_probe.py`, 6/6): since
`m_e = 3 E_x mu_0`, both `E_x` and `mu_0` cancel and

    N_v = 3 v / m_e = 1445519.509159 +/- 0.372     (q-independent)

Read as a crossing count it must be a positive integer; it sits 0.4908 away,
1.320 sigma. **The test cannot reach 2 sigma at CODATA-2022 precision** — an
integrality test is bounded by (1/2)/sigma = 1.345 sigma, and the measurement
is 98.2 % of that ceiling. `G_F` at 0.514 ppm is the sole limiting input; a
3-sigma test needs 0.231 ppm, a 2.23x tightening.

**Candidate (iii) stays OPEN, re-scoped AGAINST the candidate.** Every factor
of the rate is real for real q, so the framework produces a width with no
Im(q) anywhere. (iii) now needs a reason a width should require Im(q) when the
framework's own does not. Scope (a). The 24.019-order arithmetic refuting
`Gamma = hbar/Q_beta` is untouched.
