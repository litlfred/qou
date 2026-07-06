# EM-linking invariant for the pp-Coulomb T−³He split — derivation attempt

**Status:** FINDING (gap analysis, reproducible, no fit). The crux of the
merged-PR-#1775 OPEN gate
([`2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md))
is resolved with a **precise obstruction, not a fit**: the per-pair
EM-linking *structure* is already derived, but the per-pair Coulomb
*magnitude* (the remaining 3.2×) is **dimensionful** — it requires a
categorical brane-separation / nuclear-charge-radius scale the framework
does not yet supply. Any concrete value would be a CAL-4 fit to AME.

Probe: [`em_linking_invariant_probe.py`](../../computations/em_linking_invariant_probe.py)
(witness `em-linking-invariant-probe.witness.json`, EXPLORATORY, RAW @ 40
dps, 2 assertions pass). **No tuning to 0.7638 MeV, no coupling fit, no h^k.**

## The question

Is `Q_pp · [EM-linking invariant] · [α_EM normalization]` evaluated at q₀
equal to ~3.21× the derived pp-Coulomb magnitude (so total ≈ 0.76 MeV)
from first principles? **0.764 MeV is a post-hoc check, never the fitting
input.**

## What is DERIVED already (zero fit)

The EM-linking *structure* exists in the corpus today:

| Object | Value at q₀ | Source (derived) |
|---|---|---|
| Coulomb charge `Q_pp = (n₊−n₋)/2` | `+1` | [`def:coulomb-charge`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md) |
| per-pair **linking number** lk(Hopf⁺) | `+1` | [`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md): pp = `σ₁²`, writhe `+2` |
| LIVE **U(1)_framing** factor `q^{w·c}` (c=1) | `q²≈1.232` | same; live because writhe ±2 ≠ 0 (unlike writhe-0 Borromean) |
| Markov **trace asymmetry** `tr_M(pp)−tr_M(nn)` | `0.16507` | same; Wenzl trace on `H₂(q)`, both Wedderburn blocks carry weight |
| Coulomb/strong **ratio** `tanh(ln q₀)` | `0.10396` | `def:coulomb-charge` (q₀-only) |
| α_EM Habiro lead `[2]_q` | `2.0109` | [`alpha-em-habiro-bar-involution`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md) |
| ³He binding-link volume `Vol(L6a4)=8G` | `7.3277` | [`binding_link_volumes.py`](../../computations/binding_link_volumes.py) (= Borromean) |
| ³H binding-link volume `Vol(8₁₁)` | `8.2863` | same |

So the **per-pair EM-linking invariant DOES exist** as a *dimensionless*
categorical object: the Hopf linking number `lk = +1` of the two
proton color-tube sub-components, which is exactly `Q_pp = +1` (the
single integer the framework supplies per nucleon pair). The derived
categorical Coulomb already *uses* it. The U(1)_framing and the
Markov-trace asymmetry are the further derived linking data.

## The test — does any derived dimensionless form give the 3.2×?

The probe catalogues every derived dimensionless candidate and measures
its relative miss against the factor `3.2133 = 0.7638 / 0.2377`:

| derived candidate | value | rel-miss |
|---|---:|---:|
| `Q_pp` (linking number) | 1.000 | 68.9% |
| framing `q²` (U(1), c=1) | 1.232 | 61.7% |
| trace asymmetry `tr(pp)−tr(nn)` | 0.165 | 94.9% |
| `[2]_q` (α_EM Habiro lead) | 2.011 | 37.4% |
| `1/h` | 4.783 | 48.9% |
| `1/(h·[2]_q)` | 2.379 | **26.0%** (best) |
| binding-link vol ratio `Vol(8₁₁)/8G` | 1.131 | 64.8% |
| `1/tanh(ln q₀)` | 9.619 | 199.3% |

**No derived dimensionless q-form matches the 3.2× factor** (gate: <1%;
best candidate misses by 26%). Crucially, this is *not* a failure to
search hard enough — forcing a `[N]_q/h^k` combination to land at 3.21
would be exactly the PSLQ-coincidence antipattern (production-vs-
exploratory-discipline §Antipattern 2), and it would fail the q-locality
gate. The witness **asserts the refutation** (`none_match = 1`), so the
honest-negative outcome keeps the witness green.

## Why — the factor is DIMENSIONFUL (the precise obstruction)

The derived categorical Coulomb measures the pp-repulsion as a **fraction
of the strong bond**: `dHe = tanh(ln q₀)·B_pp`. But the physical pp-Coulomb
is a **dimensionful** energy `e²/(4πε₀·r_pp)` set by the inter-proton
**separation** `r_pp`. Decoding each energy into its implied single-pair
separation (`r = α·ħc / E`, `α·ħc = 1.4399645 MeV·fm`, standard physics —
not fitted):

| energy | implied separation `r` | interpretation |
|---|---:|---|
| derived `dHe = 0.2377 MeV` | **6.06 fm** | the strong-bond proxy scale |
| AME split `0.7638 MeV` | **1.885 fm** | ≈ the ³He charge radius (1.97 fm) |
| **ratio** `r_derived / r_ame` | **3.213×** | **= the open factor** |

The 3.2× is *exactly* the ratio of the nuclear-charge-radius Coulomb scale
to the strong-bond scale. As an independent cross-check, the uniform-
charged-sphere Coulomb energy of ³He at its measured radius,
`E_C = (3/5)·Z(Z−1)·α·ħc / R ≈ 0.879 MeV` (R = 1.966 fm), is within ~15%
of the AME split — confirming the split is genuinely the radius-set
Coulomb energy, and that the derived categorical Coulomb is short precisely
by the length-scale conversion.

## Verdict

- **The EM-linking invariant exists and is derived** as a dimensionless
  categorical object: the Hopf **linking number `lk = +1 = Q_pp`**, with
  the LIVE U(1)_framing and the Markov-trace asymmetry as further derived
  data. The framework supplies the *sign, the channel, and the linking
  number* with zero fit.
- **The per-pair Coulomb MAGNITUDE is NOT derivable** from the current
  framework. The remaining 3.2× is intrinsically **dimensionful** — a
  length scale (nuclear charge radius / brane separation), not a
  dimensionless q-form. No derived dimensionless object reproduces it
  (best 26% miss), and the factor decodes cleanly as `r_strong / r_charge`.
- **The MISSING OBJECT is a categorical brane-separation / nuclear-charge-
  radius scale.** This is the *same class* of obstruction already named
  twice in the corpus:
  - the `writhe → hypercharge Y` map is undefined (misses PDG by ~305× at
    the natural coupling c=1;
    [`u1_hypercharge_assignment.py`](../../computations/u1_hypercharge_assignment.py)),
    and
  - the Δ_λ per-partition closure (six ansätze failed; AGENTS.md Δ_λ gate).

  In each case the framework supplies the dimensionless/structural datum
  but not the dimensionful normalization. Here the normalization is a
  length scale.
- **Discipline:** any concrete close beyond the derived 31% would require
  tuning `r_pp` (or an equivalent coupling) to hit 0.764 MeV — a **CAL-4
  fit**, out of bounds. So the pp-Coulomb crossing **stays exploratory**;
  the gate is closed only when a categorical nuclear-radius / brane-
  separation object is derived. This is **not** an α_EM-normalization
  problem: the α_EM Habiro element is dimensionless (`[2]_q·(1−h²α)`), so
  it cannot supply the missing length scale either.

## Why α_EM normalization cannot rescue it (anticipating the obvious next try)

The crux asked specifically about `[α_EM normalization]`. The α_EM Habiro
element `[2]_q·(1−h²α)` and `1/α_EM = q·[9]_q·[10]_q + 2/(3π) ≈ 137.04`
are **dimensionless**. Multiplying the dimensionless EM-linking datum by a
dimensionless α_EM factor yields another dimensionless number; it can
never produce the MeV·fm⁻¹ × fm dimensionful Coulomb magnitude that the
3.2× encodes. The obstruction is dimensional, so an α_EM normalization —
however it is combined — does not close it. (Numerically, none of the
α_EM-flavoured candidates `[2]_q`, `1/(h·[2]_q)` come within 26% either.)

## Productive direction (for whoever picks this up)

The closure path is a **categorical nuclear-charge-radius / brane-
separation scale** — e.g. deriving `r_pp` from the JSJ decomposition of
the ³He binding link (`L6a4 = Borromean`, Vol = 8G) as a cusp/horoball
separation, or from a per-pair geometric Geom_full evaluation that carries
length units. Until that object lands, the magnitude is a fit. This is the
same "needs a categorical object the structure does not yet supply"
pattern as the other Wall-A items.

## What this audit does and does not claim

- **Does** confirm the per-pair EM-linking invariant exists and is derived
  (Hopf `lk = +1 = Q_pp`, U(1)_framing, trace asymmetry — all on main).
- **Does** show NO derived dimensionless q-form reproduces the 3.2× factor
  (best 26% miss; assert-the-refutation witness).
- **Does** diagnose the factor as dimensionful: `r_strong/r_charge =
  3.213×`, with the AME-implied separation ≈ the ³He charge radius.
- **Does** name the precise missing object: a categorical brane-separation
  / nuclear-charge-radius length scale.
- **Does NOT** fit, tune, or propose any coupling, radius, or h^k to hit
  0.764 MeV; does NOT wire to production; does NOT advance L2 numerically;
  does NOT discharge any Lean `sorry`. No LP/SDP solve (no dual required).

## Cross-references

- The OPEN gate this resolves:
  [`2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md)
  (merged PR #1775).
- The derived per-pair linked channel (linking number, U(1)_framing,
  trace asymmetry):
  [`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md).
- The same-class `writhe → Y` obstruction:
  [`u1_hypercharge_assignment.py`](../../computations/u1_hypercharge_assignment.py),
  [`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md).
- The binding-link volumes (³He = L6a4 = Borromean = 8G; ³H = 8₁₁):
  [`binding_link_volumes.py`](../../computations/binding_link_volumes.py).
- Coulomb charge definition:
  [`def:coulomb-charge`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md).
- α_EM Habiro element (dimensionless — cannot supply the length scale):
  [`alpha-em-habiro-bar-involution`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md).
- Discipline:
  [`production-vs-exploratory-discipline.md`](../../.claude/skills/local/production-vs-exploratory-discipline.md)
  (§Antipattern 2 PSLQ coincidence; the CAL-4 / fit bright line).
