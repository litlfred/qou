# Red-team: the canonical nucleon-mass formula `m_p = 2·(m_μ·F_Bor − 6·m_e)`

**Date:** 2026-08-22
**Bean:** `qou-n04i`
**Type:** read-only adversarial audit (Critical-distance license, AGENTS.md)
**Producer under review:** [`computations/canonical_mass.py`](../../computations/canonical_mass.py)
(facade) → [`computations/m_p_substrate_identity_50dps.py`](../../computations/m_p_substrate_identity_50dps.py)
(producer) → `m-p-substrate-identity-50dps.witness.json`
**Companion red-teams (same rigor):**
[`2026-08-16-ck-ladder-red-team.md`](2026-08-16-ck-ladder-red-team.md),
[`2026-08-22-mK-mpi-l2-red-team.md`](2026-08-22-mK-mpi-l2-red-team.md),
[`2026-08-22-avol-binding-redteam.md`](2026-08-22-avol-binding-redteam.md)

## Bottom line (blunt)

**The formula has no *continuous* free parameter beyond `q₀` — but it is not a
parameter-free derivation of `m_p/m_e`.** Its predictive content, once the
round-trip theatre is stripped, is one calibration and one cross-check that
misses. Concretely:

1. **In production, `m_p/m_e` is a tautology, not a prediction.** The proton pin
   `_solve_q_proton_f64` ([`constants.py:112`](../../tools/qou-substrate/python/qou_substrate/constants.py))
   *defines* `q₀` as the root of `m_p/m_e = 2·(Vol(4₁)/ℏ_q²·F_Bor(q) − 12)`.
   Feeding `q₀` back through the same formula returns `m_p/m_e` to machine
   precision (verified below). The "0.0004 ppb / 0.24 ppm match" is `f(f⁻¹(x))`.
   The producer docstring is honest about this ("ANCHOR round-trip, not a
   prediction").

2. **The one genuine, non-circular test is the μ–p consistency, and it fails the
   accuracy target.** Given `q₀` from `m_p`, the muon anchor
   `m_μ/m_e = Vol(4₁)/ℏ_q²` predicts a value **211 ppb** off CODATA — a ~963×
   miss of the 100× target. Equivalently (muon pin), `m_p/m_e` via `F_Bor` is a
   real prediction at 0.24 ppm = ~437× miss. These are the *same* ~11.5 ppb
   substrate tension, amplified ~21× by the steep `ℏ_q=(q−1)/q`.

3. **The `F_Bor` observable is a *selected/asserted* combination, not a derived
   one.** Its `/q³` normalization is asserted, has no derivation trail, **breaks
   the bar-symmetry** a ribbon/Markov trace should carry, and is a **37 % lever**
   on `m_p` (bean [`qou-24w9`](../../.beans/qou-24w9--hidden-assumption-f-bors-q3-is-asserted-breaks-bar.md)).
   The braid `β_Bor = Borromean` is a **conjecture** (`conj:proton-borromean-assembly`),
   not a derived proton assignment.

4. **The integers `2` and `6` (=`12`) are post-hoc identifications, and the
   supporting `−1/12` Ocneanu provenance is refuted for `β_Bor` yet still cited
   in the live content blocks.** The "12" was first claimed `= 1/(−1/12)`
   (Ocneanu leading pole), that identification was refuted (`|tr_M(β_Bor)| ~
   q⁻⁴`, coeff −1, **not** `q⁻¹⁰·(−1/12)`), and it was then re-identified as
   `2·6 = dim V_{(2,1)}·|S₃|`. Both stories still appear, presented as
   consistent, in `conj:proton-borromean-assembly` and `def:f-bor-borromean-observable`.

**Verdict:** a **one-continuous-parameter (`q₀`) fit dressed with
post-hoc-identified integers and an asserted normalization**. There is *some*
genuine structure (Vol(4₁), convention D, the Lean `|tr_M|` closed form), so it
is not pure numerology — but "genuine parts + selected joints" is a *partial
derivation with fitted joints*, not a parameter-free derivation of `m_p/m_e`.
This is consistent with, and does not contradict, the framework's own honest
labeling (conditional-on-conjecture; absolute mass excised 2026-08-11; L2
dashboard records m_p at ~437× miss).

## The formula and every input, traced

$$m_p \;=\; 2\cdot\bigl(m_\mu\cdot F_{\mathrm{Bor}} - 6\,m_e\bigr)
        \;=\; 2\,m_\mu\,F_{\mathrm{Bor}} - 12\,m_e,
\quad
m_\mu = m_e\frac{\mathrm{Vol}(4_1)}{\hbar_q^2},
\quad
F_{\mathrm{Bor}} = \frac{|\mathrm{tr}_M(\beta_{\mathrm{Bor}},q_0)|\cdot[3]_q!}{q_0^{3}}.$$

| Ingredient | Value at `q₀` | Tier | Notes |
|---|---|---|---|
| `Vol(4₁) = 2·Cl₂(π/3)` | `2.0298832…` | **DERIVED** ✓ | real hyperbolic volume of the figure-8 complement; 0 DOF |
| `ℏ_q = 1 − 1/q₀` | — | **CALIBRATION** | `q₀` is CAL-2 (pinned; see below) |
| `m_e` | CODATA | **CAL-1** | fixes the MeV unit by fiat |
| `m_μ = m_e·Vol(4₁)/ℏ_q²` | — | muon anchor | the CAL-2 relation itself; genuine, testable |
| `|tr_M(β_Bor,q)| = (4+h²−3h⁴−h⁶)/(h²+4)` | `0.9985622…` | **DERIVED (Lean)** ✓ | `BorromeanMarkovTrace.lean`, *given* `β_Bor` and convention D |
| trace convention **D** (`z=q³/(q²+1)`) | — | **DERIVED** ✓ | forced by fibre `N=2` (SU(2)-emergence) — a genuine bright spot; see below |
| `β_Bor = Borromean` | — | **SELECTED / CONJECTURAL** ✗ | `conj:proton-borromean-assembly`; why Borromean = proton is open |
| `[3]_q! = (q²+1+q⁻²)(q+q⁻¹)` | `6.1205793…` | closed form | but its *appearance* in `F_Bor` is part of the selected combination |
| `/q³` normalization | `q₀³=1.3675518…` | **ASSERTED** ✗ | no derivation trail; breaks bar-symmetry; **37 % lever** (`qou-24w9`) |
| `F_Bor` combination overall | `4.4691387…` | **OPEN bridge** ✗ | `conj` status admits "the formal categorical statement is pending" |
| `mult = 2 = dim V_{(2,1)}` | 2 | **post-hoc integer** ✗ | trace-dominant irrep dim; identified after the fact |
| `bind = 6 = |S₃|` | 6 | **post-hoc integer** ✗ | `−1/12` Ocneanu provenance **refuted** for `β_Bor`, still cited |

### Convention D is genuinely derived — credit where due

The one part I expected to be a hidden knob and is not: the Jones/TL (`z_D`)
vs full-Hecke Ocneanu (`z_C`) trace choice. Per
[`2026-08-08-mass-fibre-dimension-forces-convention-d.md`](2026-08-08-mass-fibre-dimension-forces-convention-d.md)
and `FibreDimensionForcesTL.lean` (sorry-free), the mass channel's fibre is the
`N=2` fundamental of SU_q(2) (`thm:su2-emergence`, `lem:feynman-eigenbasis-decomposition`,
row cap `ℓ(λ)≤2`), and `dim_q V = [2]_q` forces `z·[2]_q = q²` = convention D
uniquely — **with no experimental input**. The C↔D gap is 195 ppm, ~800× larger
than the 240 ppb "agreement," so had the convention been a free choice this would
be the dominant knob; it is instead pinned by the fibre. This is a real
derivation and should not be lumped with the selected pieces.

## DOF vs. constraints

**Continuous DOF: 1 (`q₀`). Continuous constraints consumed: 1 (one mass ratio).**

- Production pins `q₀` by *inverting the mass formula itself* against `m_p/m_e`.
  So `m_p/m_e` = the input that defines `q₀`. Net proton prediction: **zero.**
- The muon anchor `m_μ/m_e = Vol(4₁)/ℏ_q²` is a *second, independent* relation.
  With `q₀` fixed by the proton, it is a genuine 0-continuous-knob prediction —
  and it misses by 211 ppb (963× the target). This is the *only* real number the
  proton–muon sector produces.
- "m_p AND m_n both land" is **not** 2 predictions from 0 knobs. `m_n = m_p + Q_β
  + m_e` with `Q_β` the parameter-free Kashiwara b² value; given `m_p` (a
  round-trip), the neutron adds exactly one prediction, `Δ_pn = Q_β + m_e`, whose
  own accuracy (~1 ppb claimed, near-match tier, gated on the open s5bb keystone)
  is a separate question and is *not* what makes m_p land.

**Discrete DOF selected with knowledge of the target:** `β_Bor` (conjectural),
the `F_Bor` normalization `/q³` (asserted; 37 % lever), and the integers `2`, `6`.
None is a continuous fit parameter, but at least three are corpus-labeled
conjectural/asserted, and the `/q³` + integer choices were demonstrably *searched*
(the −1/12 → 2·6 re-identification history).

### Sensitivity — how the discrete choices behave (my 60-dps mpmath probe)

Re-pinning `q₀` from `m_p/m_e` for each integer choice, then reading off the
`m_μ/m_e` prediction (the only non-circular observable):

| `bind` (the `−6`) | `m_p` round-trip | `m_μ/m_e` miss |
|---|---|---|
| 4 | exact | −1.89e6 ppb |
| 5 | exact | −943,204 ppb |
| **6** | exact | **+211 ppb** |
| 7 | exact | +943,554 ppb |
| 8 | exact | +1.89e6 ppb |

| `mult` (the `2`) | `m_μ/m_e` miss |
|---|---|
| 1 | q₀ nonsensical (−6.05) |
| **2** | **+211 ppb** |
| 3 | −2.9e8 ppb |

Two readings, both true and both worth stating:

- **In the framework's favor:** `m_p` round-trips for *any* integer, but the
  *muon* cross-check is sharp — only `(mult,bind)=(2,6)` lands `m_μ/m_e` at 200 ppb
  while neighbors are ~4500× worse. A *random* integer pair would not do this, so
  there is real structure, not free numerology.
- **Against:** that sharpness exists **only because `F_Bor` was pre-normalized**
  (via `/q³` and the `β_Bor` choice) so that `2·m_μ·F_Bor` overshoots `m_p` by
  *exactly* `12·m_e` at `q₀`. My probe: `2·m_μ·F_Bor = 1848.1527 m_e`, and the
  quantity that must be subtracted to reach `m_p/m_e = 1836.1527` is **`12.0` m_e`
  to the last digit** — i.e. the "12" is the *residual the selected `F_Bor` leaves*,
  subsequently re-labeled `2·|S₃|`. Pick a different (equally "natural") `F_Bor`
  normalization and a different integer would be "forced." The integer being an
  `H₃(q)` invariant is an *identification of a needed number*, not a derivation of it.

### The `/q³` normalization (the 37 % hidden lever) — per bean `qou-24w9`

- **Asserted, not derived:** `F_Bor(q) := |tr_M|·[3]_q!/q³` — a `:=` and the word
  "natural"; the exponent 3 has no derivation trail.
- **Breaks bar-symmetry:** `[3]_q!` is *already* bar-symmetric
  (`q³+2q+2q⁻¹+q⁻³`); `[3]_q!/q³ = 1+2q⁻²+2q⁻⁴+q⁻⁶` is **not** invariant under
  `q→1/q`. So `/q³` un-balances a quantity a ribbon trace is expected to keep
  balanced — the normalization fights the structure. (The audit
  `2026-06-24-fbor-q3-exact-habiro-ratio-fit.md` calls `/q³` "exact balancing";
  its algebra is right, its meaning backwards — `qou-24w9`.)
- **Load-bearing at 37 %:** removing `/q³` moves `m_p` by +37 %. A 37 % factor
  justified by "natural" is a hidden assumption.

### The `−1/12` Ocneanu provenance is refuted but still cited

`|tr_M(β_Bor,q)|·q⁴ → 1` and `·q¹⁰ → 0` as `q→0` (my probe; matches the
2026-05-25 audit): `β_Bor`'s trace has a **q⁻⁴ pole with coefficient 1**, not the
`q⁻¹⁰·(−1/12)` of the "proton (no-inter)" braid the Ocneanu audit measured. The
2026-05-25 audit **retracted** the `12 = 1/(−1/12)` identification on exactly this
ground. Yet `conj:proton-borromean-assembly` still reads *"bind = |S₃| = 6, the
inverse of the Ocneanu leading-pole coefficient −1/12"*, and
`def:f-bor-borromean-observable` still invokes the `−1/12` pole. This is a live
laundering of a refuted numerology as a supporting identification — should be
corrected (follow-up).

### The Lean "theorem" is close to a self-assuming projection

`conj:proton-borromean-assembly` is axiomatized as a class
`QOU.AppendixQValues.ProtonBorromeanAssembly` whose *fields are* the two integers
and **the factored assembly law itself**; `prop:proton-mass-substrate-identity`
then "derives" the flat identity `m_p = 2 m_μ F − 12 m_e` from the factored one —
which is just distributing the `2`. Per AGENTS §3b-cond item 5, a class carrying
the block's own conclusion with a theorem that projects it is a vacuous
self-assuming projection. "Sorry-free modulo the class instance" here means
"sorry-free modulo assuming the entire physics content." This is honest labeling
(it *is* a `conj`), but the "prop" adds no derivation.

## Answers to the charged questions

- **Is `m_p/m_e` parameter-free from `q₀`?** No continuous free parameter — but
  (i) in production `q₀` *is* `m_p/m_e` inverted, so it is a tautology, not a
  prediction; (ii) the *form* carries selected/asserted discrete structure
  (`β_Bor` conjectural, `/q³` asserted 37 % lever, `2` and `6` post-hoc); (iii)
  the only non-circular cross-prediction (`m_μ/m_e`) misses the target by ~963×.
  So: **not a parameter-free derivation.**
- **Are the `−6`/`2` fitted?** Not as continuous parameters, but yes as
  **post-hoc-selected integers**: `bind=6` is the residual the pre-selected
  `F_Bor` leaves (my probe: exactly `12.0 m_e`), re-labeled `2·|S₃|`; its `−1/12`
  Ocneanu justification is refuted for `β_Bor`. The corpus itself calls the bridge
  "open."
- **2 constraints (m_p, m_n) from 2 knobs?** No — m_p is a round-trip (0
  constraints net), m_n adds one genuine but near-match/gated prediction (`Δ_pn`).

## What is genuinely good here (fairness)

Vol(4₁) is a real 0-DOF hyperbolic volume; convention D is a genuine
fibre-forced derivation (not CODATA-selected); the `|tr_M|` closed form is
Lean-proved; and the μ–p consistency at 211 ppb with a *sharply* preferred
integer pair is a modest non-trivial structural fact. The framework has already
excised the worst overclaim (absolute mass, 2026-08-11), dropped the fitted
Habiro tower (2026-07-04), and labels the assembly as a conjecture. The residual
red-team finding is narrower: **`F_Bor`'s `/q³` + the `2`/`6` integers are the
fitted joints of an otherwise partly-structural form, and the refuted `−1/12`
provenance should be scrubbed from the live blocks.**

## Follow-ups (not done here — read-only audit)

1. Scrub the refuted `−1/12` Ocneanu provenance from `conj:proton-borromean-assembly`
   and `def:f-bor-borromean-observable` (keep `12 = 2·6`, drop the `1/(−1/12)`
   claim). Own commit + render-QA (math-bearing).
2. Resolve or re-scope bean `qou-24w9` (`/q³` asserted, breaks bar-symmetry, 37 %):
   either derive the `/q³` (e.g. the Li₂^q brane-tower route, bean `ovud`) or label
   `F_Bor` explicitly as a selected observable in the content blocks.
3. Consider re-labeling `prop:proton-mass-substrate-identity` to make explicit that
   it only *distributes* the assembly law it assumes (§3b-cond item 5 non-degeneracy).
