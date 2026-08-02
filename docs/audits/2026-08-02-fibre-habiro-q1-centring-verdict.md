# Fibre-level bar-odd Habiro element realising the owner's saddle picture — VERDICT

**Date:** 2026-08-02
**Branch/PR:** `claude/fibre-habiro-q1-centring-2026-08-02` / #4587
**Bean:** `qou-q86o` (the surviving "origin-centred only at q=1" leg)
**Kind:** open-outcome research verdict — corpus-first synthesis + one new sorry-free Lean lemma.
**Siblings:** #4577 (`IotaOddSaddleOffsetAmphichiral`, chirality gate), #4578/#4583
(`SaddleOffsetBarGrade`, bar-grade distinction), #4519 (`qou-dri7`, bar-odd Borel resummation).
**Arc ledger:** [`docs/coordination/2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md).
**Discipline:** no fit, no `c_k` wired, nothing to any dashboard / the Q_β ladder. Scope-(a).
No open-item declaration made without the corpus-grep checklist; no "refuted" without (a)/(b) scope.

---

## Question under test

The owner's saddle-vector picture: a knot-particle is a *vector* (angle + magnitude) at a
saddle of Bring's surface, **origin-centred only at `q = 1`**, the offset being the
`q ↔ q⁻¹` bar-odd grade of `ω = βp − β⁻¹q`. The sibling gates settled its *archimedean/DT*
reading:

- **#4577** (`IotaOddSaddleOffsetAmphichiral`, sorry-free): the certified saddle offset
  `o = c⁺ − c⁻` vanishes **iff** the knot is (ι-fixed) *amphichiral*, modelling the
  **chirality** swap `(a,b) ↦ (b,a)` as the involution. `offset(4₁)=0`, `offset(5₂)=½` (numerator
  the certified `chiralityOdd 4 3 = 1`).
- **#4583** (`SaddleOffsetBarGrade`, sorry-free): that certified offset is **not** a
  `q ↔ q⁻¹` bar-odd Laurent object — its `q→0` constant coefficient is `1 ≠ 0`, whereas any
  genuinely `q↔q⁻¹`-odd object has zero constant coefficient. So the picture is **refuted as an
  archimedean/DT claim** (the offset is a *cross-chirality* difference, not `f(q)−f(q⁻¹)`).

The **surviving leg**, and the question this branch answers: is there a **DERIVED** (not
fitted) *fibre-level* Habiro-ring / cyclotomic-completion element `F(q)` whose `q↔q⁻¹` bar-odd
part has a forced-zero **bar-fixed coefficient degree** (`n=0` / constant term) **by
construction** — the precise fibre reading of the owner's "centred at `q=1`" (evaluation at the
involution's fixed points `q=±1` is a *distinct* statement, not what the Lean establishes) — and
whose root-of-unity / substrate evaluations reproduce the certified `{3,4}` / DT data?

---

## One-line verdict

**HONEST NEGATIVE — no derivation exists; the fibre-level bar-odd Habiro route collapses to a
vacuous-or-fit dichotomy, and the target data is not even Habiro-shaped.** A bar-odd element
realising *only* the `q=1` centring is **content-free** (the centring is automatic for the whole
class and selects nothing); one additionally reproducing the `{3,4}`/DT data is a **fit** (the data
lives in the forced-to-zero fixed degree, so it must be supplied by the *free* root-of-unity degrees
— unconstrained Habiro flexibility). Four already-proved corpus pillars converge on this; the branch
adds one new sorry-free lemma (pillar 1).

This is **scope-(a)**: a structural narrowing of the *reading* of the picture. It invokes no proved
invariant to exclude an ingredient, derives no physical number, wires nothing.

---

## The four pillars

### Pillar 1 — the `q=1` centring is automatic and NON-SELECTIVE (this branch, new, sorry-free)

[`BarOddQOneCentringNonselective.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BarOddQOneCentringNonselective.lean).

The `q↔q⁻¹` involution acts on a Laurent-coefficient sequence `g : ℤ → R` by `n ↦ -n`; its **only**
fixed degree is `n = 0` (`barInvolution_fixedDegree_iff`), the `q→0` / semiclassical datum. A bar-odd
object is forced to zero there (`barAntisym_fixedDegree_zero`, the mechanism the centring rides on).
Hence:

- `q1_centring_nonselective`: `BarAntisym g ↔ (BarAntisym g ∧ g 0 = 0)`. **Imposing "origin-centred at
  `q=1`" on a bar-odd fibre element adds *nothing* — it is satisfied by the entire class.** A property
  every candidate has cannot single out *the knot's* saddle vector.
- `centring_underdetermined`: two distinct bar-odd sequences (`n↦n`, `n↦2n`) share the fixed datum
  `g 0 = 0`; the centring does not pin the element.

**Consequence (vacuous horn).** A *derived* bar-odd element realising *only* the `q=1` centring exists
trivially (e.g. the bar-odd part of any colored-Jones combination) but is **content-free**: it says
nothing beyond bar-oddness and does not reproduce the `{3,4}` distinguisher as anything forced.

### Pillar 2 — the `{3,4}` DT datum is incompatible with bar-odd low-order structure (#4583, proved)

`certified_offset_not_barAntisym` (and here `certified_datum_not_barOdd_fixedDegree`): no bar-odd
Laurent object has bar-fixed-degree coefficient equal to the certified `chiralityOdd 4 3 = 1`. The DT
integers `{3,4}` live in the `q→0` semiclassical constant coefficient — exactly the degree a bar-odd
object forces to zero. So the DT datum **cannot** be read off the low-order (semiclassical) coefficients
of a bar-odd `F(q)`; recovering it must come from the **non-fixed** degrees (root-of-unity evaluations),
which bar-oddness leaves entirely free.

**Consequence (fit horn).** Fixing the root-of-unity values of a bar-odd Habiro element to reproduce
`{3,4}` is unconstrained CRT/Habiro interpolation — the Habiro ring is flexible enough to hit any finite
set of prescribed root-of-unity values. That is precisely the "worthless fit" the anti-fit discipline
forbids passing off as a derivation. No categorical structure forces those values.

### Pillar 3 — the `{3,4}` target is q-EXACT with NO resurgent tail (#4554, proved; arc-ledger keystone)

`StokesSymmetryConstant.symmetryConstant_const` (sorry-free): the GGM symmetry constant `S₁₂+S₂₁ = 3·S₁₁`
is **q-independent**, so it equals its own `q→0` value. Per the arc ledger
([`2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md),
PR #4554 keystone): a q-independent quantity has **no resurgent tail**, so deriving the integer target is
a **decidable `q→0` DT / 3d-index count** — *drivers 11/13* (Lobachevsky volume / crystal `q→0`), **not**
driver-12 resurgence / Habiro. The remaining gap is "a categorical formula for the `q→0` DT count
reproducing `{3,4}` across knots" — an open problem in DT/3d-index **categorification**, not a
Habiro-element question.

**Consequence.** The target `{3,4}` data is *not Habiro-shaped content at all* — it has no resurgent tail
for a fibre Habiro element to carry. Attaching it to a bar-odd `F(q)` mis-identifies a q-exact count as a
q-deformation coefficient.

### Pillar 4 — the substrate anchor is a proved WALL for infinite Habiro elements, and the bar-odd resummation is anchor-blind (#4519/#4364-era, proved + numerical)

[`HabiroMagnitudeA3.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/HabiroMagnitudeA3.lean)
(sorry-free): for real `q > 1` the cyclotomic basis magnitude `|(q;q)_n| = ∏(q^k−1)` is **unbounded**
(`pochAbs_unbounded`), so a genuine (infinite) integer-coefficient Habiro element `Σ aₙ(q;q)ₙ` is **not
summable** at the substrate `q₀ ≈ 1.10998 > 1` (`habiro_terms_not_tendsto_zero`) — it has **no canonical
archimedean value there**. Only *finite* Laurent shapes (the `[k]_q(1−h²X)` α_EM family) evaluate at `q₀`,
and those are governed by the already-established finite-type bracketing. Independently, the **bar-odd**
D-ladder Borel/Écalle resummation to a value at the substrate is **precise but anchor-blind**
([`2026-08-01-qborel-ecalle-resum-barodd.md`](2026-08-01-qborel-ecalle-resum-barodd.md), `qou-dri7`,
δ_np ≈ 5·10⁻²⁷…⁻³⁹, suppressed): the resummed bar-odd fibre object supplies **no forced value / no swing**
at the anchor.

**Consequence.** Even setting aside pillars 1–3, a genuine cyclotomic-completion `F(q)` cannot be evaluated
at the substrate, and the resummed bar-odd object that *can* be evaluated is anchor-blind — so there is no
substrate-level number for the derivation to land.

---

## Why the α_EM precedent does not rescue it

The proved α_EM Habiro element `H(q) = [2]_q(1 − h²α)` (PR #1511,
[`alpha-em-habiro-bar-involution.lean`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.lean),
`alphaEmHabiro_bar_invariant`) is a genuine "fibre object whose special-value evaluations give observable
content" — but it is **bar-EVEN** (`H(q⁻¹)=H(q)`), a *fixed point* of the bar involution, and a **finite
Laurent** object with structurally-fixed integer coefficients (`H(ζ₁)=2`, `H(ζ₄)=0`). Its content is
*forced* (charge-conjugation-symmetric, even sector). The bar-ODD analogue this branch seeks has the
opposite grade: its defining property (vanishing at the bar-fixed point) is **automatic for the whole
class** (pillar 1), so it fixes no coefficients — the exact reason the even precedent's "forced content"
does not transfer.

---

## Verdict, scope-labelled

- **CONFIRMED [scope-(a)]:** the fibre-level bar-odd Habiro picture is a *genuinely different object* from
  the archimedean DT offset (#4583), and its **bar-fixed-degree** vanishing (the `n=0` constant term,
  `g 0 = 0`) is real — but that vanishing is a **triviality of oddness at the involution's fixed
  *degree***, automatic for the entire bar-odd class (pillar 1, new sorry-free Lean). Evaluation at the
  fixed points `q = ±1` is a distinct statement the Lean does not establish.
- **HONEST NEGATIVE — the route is NOT a derivation.** It is a vacuous-or-fit dichotomy:
  - *vacuous horn* — a bar-odd element realising only `q=1` centring is content-free (pillar 1);
  - *fit horn* — one reproducing `{3,4}`/DT requires unconstrained root-of-unity interpolation (pillar 2),
    against a target that is q-exact with no resurgent tail (pillar 3) and has no substrate value to land on
    (pillar 4).
- **NOT a structural exclusion of any ingredient.** Per the STRICT "refuted/ruled out" rule this is
  **scope-(a)** throughout: no proved invariant forbids a bar-odd fibre object per se; what is shown is that
  the *specific claim* (a derived such object reproducing the certified data) is underdetermined / mis-targeted.
  The DT-count categorification (pillar 3) remains genuinely open — as a `q→0` driver-11/13 problem, not a
  fibre-Habiro one.

**Nothing is wired.** No `c_k`, no dashboard, no Q_β ladder; the one new Lean lemma is a standalone
scope-(a) structural fact.

---

## Anti-numerology / discipline guards respected

- Corpus-grep first (docs/ content/ computations/): the mature Habiro corpus was read, not reinvented; the
  four pillars cite existing proved Lean / audits.
- Formalize-first: the load-bearing claim (non-selectivity of the centring) is a sorry-free Lean lemma, not
  a prose assertion.
- No fit; nothing wired; scope-(a) throughout; "refuted" avoided in favour of the (a)-scoped
  vacuous-or-fit framing.
- Machine-validation of the new Lean was **disk-blocked** in this sandbox (the `lake-cache/qou-v4-24-0` fetch
  succeeds but the full Mathlib olean set exceeds free disk); the file was **hand-audited** — imports and the
  two core lemmas mirror the proven #4583 verbatim, and the new lemmas use only `omega`/`ring`/`rfl`/`norm_num`
  on elementary linear-integer goals plus the proven `chirality_odd_datum_eq_one`. Stated explicitly per AGENTS.md.

## Honest exit

The bean `qou-q86o` ("origin-centred only at q=1" leg) is answered: **no derived fibre-level Habiro element
realises the picture** — the route is a vacuous-or-fit dichotomy (pillars 1–2), the target is q-exact /
not Habiro-shaped (pillar 3), and the substrate has no value to land on (pillar 4). The *only* live remaining
question in this neighbourhood is the **DT-count categorification** (a `q→0` driver-11/13 problem, arc-ledger),
which is distinct from — and not advanced by — a fibre-Habiro centring element.
