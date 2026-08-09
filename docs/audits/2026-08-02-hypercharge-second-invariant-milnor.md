# The second crossing invariant for hypercharge Y: Milnor triple linking μ̄₁₂₃

**Date:** 2026-08-02
**Branch:** `claude/hypercharge-second-invariant-2026-08-02`
**Scope:** Identify a **second crossing invariant, independent of the writhe
`w`**, that could supply the weak hypercharge `Y` (equivalently, unblock
`sin²θ_W`). Follow-up to the G2 twist-derivation
(`claude/hypercharge-twist-derivation-2026-08-02`, PR #4561), which reduced
`Y` to the total twist but falsified the writhe→I₃ map as the SOLE invariant
and named the residual: a second invariant independent of `w`.
**Lean:**
[`SecondCrossingInvariant.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/SecondCrossingInvariant.lean)
(standalone library file, lean-direct-verified, v4.24.0, **exit 0,
sorry-free**).
**No coefficient fitted; no instance provided; no SM Y-assignment reverse-engineered.**

---

## VERDICT (one line)

**Of the six candidate second invariants, four are EXCLUDED and one is
selected: the second invariant is the *degree-2* datum — the Milnor triple
linking number `μ̄₁₂₃` of the three color-tube components (= baryon number `B`
on the confined triple). The reason is sharp and structural: the canonical
baryon is the Borromean link `𝓑₃`, on which *every degree-1 crossing
invariant vanishes* (writhe `= 0`, all pairwise linkings `= 0`), so `Y`
cannot be any degree-1 object; `μ̄₁₂₃ = ±1` is the first non-vanishing
finite-type invariant and equals `B`. It is (a) independent of the writhe
(structurally — degree-1 vanishes on the baryon), (b) GMN-compatible on the
non-strange sector (`Y = B`, closing `Q = I₃ + Y/2` with `I₃ = w/2`), and (c)
the right categorical *shape* (an intrinsic invariant of the framework's own
Borromean-baryon object, not a fit). What is NOT closed and stays honest:
the full `Y = B + S` (strangeness) and the relative U(1) coupling
normalization that `sin²θ_W` requires both inherit the open SU(3)-flavor
problem.**

---

## Corpus-grep checklist (STRICT, run before declaring anything)

1. `docs/audits/` — the writhe→I₃/Y story is closed in
   [`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md)
   (PR #1683): `c = ½` fixed by `def:coulomb-charge`, writhe→I₃ derived,
   writhe→Y **falsified** (p/n share `Y = +1`), missing object named as
   "a second, independent crossing/trace invariant (a baryon-number /
   color-trace charge B)". The dimensionful-magnitude sibling
   [`2026-06-03-em-linking-invariant.md`](2026-06-03-em-linking-invariant.md)
   repeats the same "missing object" class. The s5-so3 fiber audit
   [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)
   (PR #1672) records the load-bearing fact: **β_Bor = (σ₁⁻¹σ₂)³ has
   writhe 0**, so the U(1)_framing is *trivial* on the baryon.
2. `content/` — `borromean-quark.md` states the baryon is `𝓑₃`, "no two
   components link, yet all three inseparable" (pairwise lk = 0, triple ≠ 0),
   and *explicitly rejects the Hopf link* (pairwise linking) because it
   permits diquarks. `sm-hypercharge-invariant.md` carries the conjecture;
   `sm-params-gauge-couplings.md` marks `sin²θ_W` conjectural.
3. `computations/` — `u1_hypercharge_assignment.py` (the falsification
   probe). No compute names μ̄₁₂₃ as the hypercharge invariant.
4. Coordination ledgers — no prior agent has *named* μ̄₁₂₃ as the second
   hypercharge invariant. The Milnor/Vassiliev Lean infra
   (`MilnorVassilievBridge.lean`, `BrunnianVassilievBridge`,
   `MilnorParitySignLaw`) exists but is wired to the **binding-magnitude /
   Δ_λ** work (`VassilievMagnitudeA3`), a *different* application.

**Conclusion:** the identification `Y ← μ̄₁₂₃` is a new proposal, not a
re-declaration of a closed item. Corpus-grep clean.

---

## The candidates, evaluated against (a) writhe-independence, (b) GMN-compatibility, (c) derivability

The decisive fact organizing the table: **the canonical baryon `𝓑₃` has
writhe 0 and all pairwise linkings 0** (s5-so3 audit; `borromean-quark.md`).
So every *degree-1* crossing/linking invariant vanishes on it. `I₃` already
consumes the (inter-nucleon) degree-1 writhe. The second invariant must
therefore be *degree ≥ 2* to be nonzero on the intra-baryon structure.

| # | Candidate | (a) indep. of `w`? | (b) GMN-compatible? | (c) derivable? | Verdict |
|---|-----------|---------------------|----------------------|-----------------|---------|
| 1a | Framing phase `q^{w·c}` | **No** — a function of `w` by construction; trivial (writhe 0) on `β_Bor` | — | — | **EXCLUDED**: factors through `w`; the ribbon twist `θ_j = q^{j(j+1)}` is a *spin/Casimir* ladder (2026-06-02 audit §3), not a charge |
| 1b | Per-strand framing datum `T(t)` (`def:strand-twist-datum`) | **Yes** — provably *not* a function of `w`: `exists_same_writhe_ne_totalTwist` gives framings with distinct total twist at fixed writhe | Yes (free ℤ label) | — | **NOT EXCLUDED — correction, see below**. Independent, but *freely assignable*, so the published enumeration supplies no corroboration (`TwistBatteryVacuity.lean`) |
| 2 | Self-linking / framing-independent part | **No** — `sl = w + tw`; its isotopy content *is* the writhe; vanishes on `β_Bor` (w=0, pairwise=0) | — | — | **EXCLUDED**: not a new invariant; degree-1, vanishes on baryon |
| 3 | Determinant `det = \|Δ_K(−1)\|` | Yes (isotopy) | **No** — positive-definite | — | **EXCLUDED (scope-(b), positivity)**: a provably non-negative invariant cannot carry a *signed* `Y` (matter/antimatter `Y = ±1`) |
| 4 | Signature `σ(K)` | Yes (concordance inv.) | **No derivation** — even-integer, connected-sum-additive but no map `σ → Y`; wrong value spectrum | Not derived | **NOT SELECTED**: independent but no derivation `Y = σ`; would need a fit |
| 5 | Pairwise linking number in color-tube fibration | **No** — *vanishes on `𝓑₃`* by the Borromean/anti-Hopf choice; this is exactly the degree-1 data that is 0 | — | — | **EXCLUDED**: the framework's own Borromean choice kills pairwise linking (that is what forbids diquarks) |
| 6 | **Milnor triple linking `μ̄₁₂₃` = leading Vassiliev deg-2 datum** | **Yes, sharply** — first non-vanishing finite-type invariant *above* the vanishing degree-1 data; `±1` on `𝓑₃` | **Yes** on non-strange sector: `μ̄₁₂₃ = B`, `Y = B`, `Q = I₃ + Y/2` closes | **Right shape** — intrinsic invariant of the framework's own baryon `𝓑₃`; normalization inherits open SU(3)-flavor | **SELECTED** (with honest caveat below) |

### Why candidate 6 works, precisely

- **(a) Independence is structural, not assumed.** Milnor 1954: `μ̄₁₂₃` is
  well-defined *modulo the gcd of the pairwise linking numbers*. On `𝓑₃`
  every pairwise linking is `0`, so the indeterminacy is `gcd(0,0,0) = 0`
  and `μ̄₁₂₃` is an *unambiguous integer* `±1`. The very same vanishing that
  makes writhe/self-linking/pairwise-linking useless on the baryon (they are
  all `0`) makes `μ̄₁₂₃` well-defined and nonzero. Independence from `w` is
  not a hope — it is forced by the Borromean geometry the framework already
  adopted. Formally: `μ̄₁₂₃` is order `2(A−1)` and every strictly-lower-order
  invariant vanishes on the `A`-component Brunnian link
  (`BrunnianVassilievBridge`, Habegger–Masbaum 2000).
- **(b) GMN closes on the reachable sector.** Take `Q = w/2` (Coulomb),
  `I₃ = w/2` with `w` the *inter-nucleon* writhe (p:+1, n:−1 ⇒ I₃ = ±½), and
  `B = μ̄₁₂₃ = +1` the baryon-number invariant (same on p and n — it does
  *not* split the doublet, exactly as `Y` must not). Then
  `Y = B = +1` and `Q = I₃ + Y/2` gives proton `½ + ½ = 1` ✓, neutron
  `−½ + ½ = 0` ✓. On a 2-tube meson there is no triple, `μ̄₁₂₃ = 0 = B`,
  `Y = 0` ✓. This is the non-strange (`S = 0`) sector where `Y = B`.
- **(c) Derivable shape, open normalization.** `μ̄₁₂₃` is an *intrinsic*
  invariant of `𝓑₃` — no fit, no free coupling; the framework already commits
  to `𝓑₃` (over Hopf) to enforce confinement. The identification `B = μ̄₁₂₃`
  is therefore the framework's own confinement statement ("removing any one
  component frees the other two" = no stable fractional/diquark states). What
  is NOT derived: the normalization "`μ̄₁₂₃ = 1 ↦ Y = +1`" beyond the
  non-strange sector — full `Y = B + S` needs strangeness, i.e. the SU(3)
  flavor sector, which is open (`sm-params-gauge-couplings.md`: strong/flavor
  sector conjectural).

---

## What this buys `sin²θ_W` (and what it does not)

The Weinberg angle `sin²θ_W = g'²/(g² + g'²)` mixes the two U(1)'s: the `I₃`
(SU(2), here degree-1 writhe) and the `Y` (the second U(1)). Before this
identification the two U(1)'s were *not even separated* — `Y` had no carrier
distinct from `I₃`, both being the single writhe datum. Naming `Y = μ̄₁₂₃`
(degree-2) as a carrier **orthogonal** to `I₃ = w/2` (degree-1) *separates
the two U(1)'s* — the prerequisite `sin²θ_W` was missing. What remains open
for `sin²θ_W` is the **relative coupling normalization** between the degree-1
(`I₃`) and degree-2 (`Y`) U(1)'s — the same dimensionful/normalization class
of obstruction named in the em-linking audit. So this advances `sin²θ_W`
from "the two U(1)'s are indistinguishable" to "they are separated
(deg-1 vs deg-2); their relative coupling is the residual."

---

## Lean scaffold status (formalize-first)

[`SecondCrossingInvariant.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/SecondCrossingInvariant.lean)
— standalone library file, imports Mathlib only, **lean-direct verified
(v4.24.0, exit 0, sorry-free, no axiom/native_decide)**.

- `secondInvariant_gives_separating_pair` (proved) — the constructive
  converse of the G2 `exists_writhe_degenerate_pair`: any invariant `B` not
  factoring through `w` supplies the writhe-degenerate separating pair the
  `HyperchargeInvariant` conjecture requires.
- `baryon_vacuum_separating` (proved) — the concrete pair: baryon (`w = 0`,
  `B = 1` = μ̄₁₂₃) vs vacuum/meson (`w = 0`, `B = 0`) — same writhe, split by
  the second invariant. The mechanism, realized by the framework's own objects.
- `writheZero_Y_eq_twoQ` (proved) — on the writhe-0 baryon, GMN forces
  `Y = 2Q`: the writhe contributes nothing, so `Y` is carried *entirely* by
  the second invariant. This is the Lean statement of "degree-1 vanishes on
  the baryon."
- `SecondCrossingInvariant` (conjecture class, **primary**, §3b-tax) —
  content-bearing single existential Prop field asserting a gauge-invariant
  integer `B`, integers `a, b` with `b ≠ 0`, `Y = a·w + b·B` realizing GMN
  and not factoring through `w`. **No instance — OPEN.**
- `SecondCrossingInvariant.exists_writhe_degenerate_pair` (proved,
  conditional §3b-cond) — coherence check: the conjecture's hypotheses do
  deliver the object `HyperchargeInvariant` demands.

The class is **not** an instance-carrying assumption of the physics: it
axiomatizes the *hypothesis shape*, no instance is provided, and no `μ̄₁₂₃ = B
= Y` identification is proved. Per AGENTS.md anti-laundering, the scaffold
proves only the abstract reductions; the identification stays a conjecture.

---

## Honest verdict (what is and is not established)

- **Established (proved / structural):** four candidates EXCLUDED with
  reasons (framing phase not independent; self-linking not independent;
  determinant excluded by positivity, scope-(b); pairwise linking vanishes
  on the Borromean baryon). The surviving candidate is forced to be
  *degree-2* because degree-1 vanishes on `𝓑₃`, and the first non-vanishing
  degree-2 datum is `μ̄₁₂₃`, unambiguous (Milnor gcd = 0) and equal to `B`.
- **Conjectural (open):** the identification `Y = μ̄₁₂₃ = B` beyond the
  non-strange sector; the `Y = B + S` strangeness extension; the relative
  U(1) coupling normalization for `sin²θ_W`. All inherit the open
  SU(3)-flavor problem. No instance of the class is provided.
- **Not done (out of scope / forbidden):** no coefficient fitted to SM `Y`
  assignments; no wiring to production; no L2 numerical advance; no `sorry`
  discharged in any *other* file. This is a scaffold + identification, not a
  closure.

If a reviewer wants the honest one-liner: **the second invariant is not any
crossing-*sign* quantity (those are degree-1 and vanish on the baryon) — it
is the degree-2 Milnor triple-linking `μ̄₁₂₃`, which the framework's own
Borromean-baryon choice makes both well-defined and nonzero, and which equals
baryon number; `Y = B` closes the non-strange doublet, and the strange
sector + coupling normalization remain open.**

## Cross-references

- G2 predecessor: `sm-hypercharge-invariant.{md,lean}` (PR #4561),
  [`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md).
- Writhe-0 baryon braid:
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md).
- Borromean baryon (pairwise lk = 0, anti-Hopf):
  [`borromean-quark.md`](../../content/quantum-observable-universe/observations/borromean-quark.md).
- Milnor/Vassiliev infra (μ̄₁₂₃ = leading Vassiliev, indeterminacy gate):
  [`MilnorVassilievBridge.lean`](../../content/quantum-observable-universe/lean/QOU/KnotTheory/Vassiliev/MilnorVassilievBridge.lean),
  `milnor1954` + `habegger-masbaum2000` in `references.ts`.
- Dimensionful-normalization sibling obstruction:
  [`2026-06-03-em-linking-invariant.md`](2026-06-03-em-linking-invariant.md).

---

## Correction (2026-08-09): candidate 1 was two objects, and one was wrongly excluded

The original candidate table listed *"framing phase `q^{w·c}` / ribbon
twist"* as a single row and excluded it on the ground that it "factors
through `w`". That conflated two different objects, and the exclusion is
correct for only one of them.

* **The framing phase `q^{w·c}`** is built from the writhe by construction,
  so it does factor through `w`. Row 1a stands.
* **The per-strand framing datum `T(t)`** (`def:strand-twist-datum`, landed
  on `main` in the eightfold-way chapter) is a function
  `t : {1,…,n} → ℤ` with `T(t) = Σᵢ tᵢ`. Its Lean sibling proves
  `exists_same_writhe_ne_totalTwist`: at *fixed* writhe there exist framings
  with distinct total twist. So `T(t)` provably does **not** factor through
  `w`, and the original exclusion never reached it.

The two documents therefore did not contradict each other; this audit's
table was simply mislabelled. Recorded because the apparent contradiction
was flagged as blocking (bean `qou-6006`) and is now resolved.

### What the correction does *not* restore

`T(t)` is independent of the writhe precisely because it is a **free
integer label**, and that is also why the published enumeration cannot
corroborate it. `QOU/StandardModel/TwistBatteryVacuity.lean` proves
(sorry-free) that the whole battery collapses: the spectrum test is exactly
`T = 3Q` (the `−2I₃` common to candidate and target cancels), the nucleon
test is entailed by charge additivity and states one condition twice, and
the `Z₆` condition never sees the assignment. The reported "4 of 10,000
survivors" is `1 × 2 × 2 × 1` multiset counting.

A parameter-free repair — replacing the free label by the **canonical
ribbon twist**, `Q = c(λ)/3` with `c` the content sum — was tested and
fails: at `n = 3` the content sums `{3, 0, −3}` give the *integer* charges
`{+1, 0, −1}`, and no `n ≤ 8` yields both quark charges `{+2/3, −1/3}`
(`computations/ribbon_twist_charge_quantum_probe.py`). Scope-(a) for that
reading; other ribbon normalisations are untested.

So `T(t)` is a *live* candidate — the framing route is not excluded — but it
is not corroborated, and the open content is exactly what the chapter
already says: whether the twist multisets are **forced** by the categorical
braid words.

### Bearing on `μ̄₁₂₃`

Unchanged. The load-bearing argument for a degree-2 invariant — every
degree-1 crossing invariant vanishes on the Borromean baryon `𝓑₃` — is
untouched, and `T(t)` is not a crossing invariant at all (it is framing
data), so the two candidates are not competitors on the same axis. Per
`2026-08-09-hypercharge-battery-reduction.md`, `μ̄₁₂₃ = B` supplies the `B`
half of the left-handed requirement `Y = B − L` and leaves the `L` half
open.
