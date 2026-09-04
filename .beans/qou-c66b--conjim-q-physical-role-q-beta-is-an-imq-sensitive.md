---
# qou-c66b
title: 'conj:im-q-physical-role: Q_beta IS an Im(q)-sensitive observable already in the framework — the conjecture''s stated obstacle is wrong'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T10:42:33Z
updated_at: 2026-09-04T20:56:04Z
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
