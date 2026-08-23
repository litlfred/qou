# Red-team: the `B_vol = a_V·A` "volume-term" binding claim (`a_V = E₀·ln(1/W_free) ≈ 7.584 MeV/nucleon`, tagged "DERIVED parameter-free")

**Date:** 2026-08-22
**Scope:** adversarial audit (read-only). Same rigor as
[`2026-08-16-ck-ladder-red-team.md`](2026-08-16-ck-ladder-red-team.md) and
[`2026-08-22-mK-mpi-l2-red-team.md`](2026-08-22-mK-mpi-l2-red-team.md).
**Target:** the `B_vol` column of
[`computations/mass_binding_dashboard.py`](../../computations/mass_binding_dashboard.py)
(coefficient `a_V`, lines 545–555, 618–619, legend line 779) and its probe
[`computations/probes/su4_occupancy_binding_probe.py`](../../computations/probes/su4_occupancy_binding_probe.py).
**Bean:** `qou-lsvj` (created this session). Relatives: `qou-78pt`, `qou-qlma`.

---

## TL;DR verdict

**`a_V` is a DERIVED-CANDIDATE NEAR-MATCH shading into POSTDICTION-ANALOGY — NOT
a genuine parameter-free derivation of the binding energy, and the dashboard's
"DERIVED parameter-free" tag is NOT honest as it stands.** There is no
*continuous* fit parameter — both `E₀` and `W_free` are forced once you fix the
partition and the functional form. But (i) the "surprisal" functional form was
*selected* over the linear alternative precisely because it lands near 8; (ii)
the same file, 460 lines above the tag, carries a dated (2026-08-08) deprecation
banner declaring `B_vol` "has no basis in the derivation chain" and "removed";
(iii) `ln(1/W_free)` is called a surprisal but `W` is an *unnormalised* weight,
so it is not an information-theoretic quantity at all; (iv) the construct is
physically incoherent (a free nucleon, `A=1`, `B_AME=0`, gets 7.58 MeV of
"binding"); and (v) it never touches the Markov trace `tr_M`, so it fails the
dashboard's *own* definition of "DERIVED". The probe's own verdict already says
this honestly ("NOT a derivation ... a parameter-free COINCIDENCE with the
saturation value"). The defect on `main` is the stale, self-contradicting
dashboard tag, not a new open question.

---

## (a) The exact formula and every input traced

```python
# mass_binding_dashboard.py:554-555
a_V  = alpha * math.log(1.0 / W_lambda_float(q0, (1, 1, 1)))   # "parameter-free volume coeff"
B_vol = A * a_V
```

with `alpha = E₀`, `E₀ = m_e / (q₀(q₀−1))` (`_constants`, lines 243–254), and
`W_lambda_float(q, λ) = [n]_q! / (∏ hooks [h]_q)²` (line 129), the symmetric
q-integer `[k]_q = (qᵏ − q⁻ᵏ)/(q − q⁻¹)`.

For the fixed free-nucleon partition `λ = (1,1,1)` of `n=3` (a single column,
hooks 3,2,1): `∏ hooks = [3]_q[2]_q[1]_q = [3]_q!`, so
**`W_free = [3]_q! / ([3]_q!)² = 1/[3]_q!`** and therefore

$$
a_V = E_0 \cdot \ln[3]_q! .
$$

Recomputed end-to-end in `mpmath` (dps=60, proton-pin q₀, CODATA m_e):

| quantity | value | provenance |
|---|---|---|
| `q₀` | 1.1099785827… | **CAL-2** proxy (proton pin, per owner directive 2026-08-07) |
| `m_e` | 0.510998950690 MeV | **CAL-1** (CODATA input, fixes MeV unit) |
| `E₀ = m_e/(q₀(q₀−1))` | **4.18598136 MeV** | derived from CAL-1+CAL-2; = the dashboard `α` |
| `[3]_q!` | 6.12057928 | fixed from q₀ |
| `W_free = 1/[3]_q!` | 0.163383228 | fixed once λ=(1,1,1) is chosen |
| `ln(1/W_free) = ln[3]_q!` | 1.81165675 | — |
| **`a_V = E₀·ln[3]_q!`** | **7.58356137 MeV/nucleon** | — |

So the number is exactly what the dashboard claims (7.584). Input status:

- **`E₀` — forced.** `m_e` (CAL-1) and `q₀` (CAL-2 proxy, proton pin) are both
  calibration data; `E₀` is the unique dimensionful scale the framework can
  build (`m_e × f(q₀)`; see bean `qou-qlma` "why alpha exists: dimensionally
  forced"). **No continuous fit here.** *But* bean `qou-qlma` also establishes
  that nothing calibrated pins `E₀` as the *nuclear-binding* scale — it is an
  unexamined default reused from the lepton/meson path, and a Lean-proved floor
  (`bond_energy_floor`) shows `E₀ = 4.186` is already 30% above the value that
  could bind the deuteron under the production trace convention.
- **`W_free` — a fixed weight of a fixed partition, no scan.** `(1,1,1)` is the
  free nucleon's SU(4) spin-isospin ground partition, so the *partition* is not
  tuned. **But the weight is unnormalised** (see (c) below), which is a hidden
  convention choice, and the *functional form* `ln(1/W)` is a selected knob.

## (b) DOF-vs-precision accounting

**Continuous fit parameters: 0.** **Discrete construction choices (each made
toward the ~8 target): ≥ 3.**

1. **Functional form: surprisal `ln(1/W)` vs linear complement `1−W`.** The
   probe tests both. Linear gives `E₀·(1−W_free) = 4.186·0.8366 = 3.50 MeV`
   (too small); surprisal gives 7.58 (near 8). The probe's verdict explicitly
   picks surprisal *because* linear "is too small" (line 231–232). This is a
   discrete form-selection knob resolved by proximity to the empirical value.

2. **Normalisation of the Plancherel weight.** `ln(1/W)` is presented as an
   occupancy *surprisal*, which requires `W` to be a probability. It is not:
   `Σ_λ W_λ ≠ 1` (the in-file banner measures 1.517 at n=12, 26.28 at n=21; I
   confirmed `Σ_λ W_λ = 0.9874` at n=3). Using the *unnormalised* weight is a
   convention choice; normalising would move the number (small for `a_V` itself
   — 1.812 → 1.799, ~0.7%, because n=3 happens to sum near 1 — but large for the
   `B_gate`/`E_gate` cluster values it was co-derived with).

3. **"All-knots" ×A packaging.** The single-partition `E_gate = E₀·ln(1/W_λ)`
   was found to be ⁴He-local and to break (`W_λ ≥ 1`, negative "surprisal") by
   ²⁴Mg. `B_vol = A·a_V` was introduced *afterwards* to rescue a valid-∀A
   linear term — i.e. the packaging was reverse-engineered from the observed
   breakdown to reproduce the liquid-drop volume shape.

**Is 5% agreement meaningful given this?** No. The "target" is the empirical net
`B/A` saturation value, which is not a single number: it ranges from ~1.1 MeV/A
(²H) through ~8.0 (typical) to 8.79 (Fe peak) and back down. "≈8 MeV/A" is a
soft, ~1-significant-figure quantity. Landing within 5% of a 1-sig-fig soft
target, using a construct with ≥3 discrete choices each resolved toward that
target, is a coincidence, not a prediction. Measured misses: −5.2% vs 8.0,
−13.7% vs the 8.79 Fe peak. And `B_vol = a_V·A` has **zero A-structure** — the
probe itself shows the residual `R = B_vol − B_AME` changes sign (+8.2 at ²H →
0 at ¹²C → −4.6 at ⁵⁶Fe), so it is not even a liquid-drop surface term; all real
binding-curve shape is missing.

## (c) The "surprisal" story is false, and the construct is incoherent

- **Not a surprisal.** `-ln W` is an information content only if `W` is a
  probability. `Σ_λ W_λ ≠ 1` at q₀ (verified), so the construct "treated an
  unnormalised weight as a probability" (in-file banner, line 111–115). The repo
  already had `normalized_plancherel_weights_3A` whose docstring says the naive
  weights "do NOT sum to 1" at q > 1.
- **Incoherent at A=1.** `B_vol(A=1) = 1·7.58 = 7.58 MeV` for a *free* nucleon,
  whose binding is 0 by definition. The banner records this: "B_gate and B_vol
  both reported 7.58 MeV of BINDING for a free nucleon ... making `err gate`
  read 0.00 as though it were a perfect score."
- **Off the derivation chain.** The chain terminates at `tr_M`; everything
  downstream "must be a function of tr_M" (banner). `a_V` uses one partition's
  Plancherel weight — no character, no sum — and never touches the braid word,
  so it "cannot distinguish two nuclei with the same (Z,N,S) and different
  topology. It is a Wedderburn-layer side-channel around the pairing." This also
  means it fails the dashboard's *own* `DERIVED` definition (line 663:
  "parameter-free from (q₀, m_e) **through the Markov trace**").

## (d) Prediction or postdiction?

**Postdiction / analogy.** The known target (~8 MeV/A liquid-drop volume term)
came first; the construction was assembled to reproduce it — functional form
chosen for size, ×A packaging chosen after the single-partition version broke.
The probe is candid about this in its own words (lines 252–254): *"NOT a fit
(a_V forced by E₀ × a Plancherel weight), but NOT a derivation of the binding
either: a_V≈8 MeV/A is a parameter-free COINCIDENCE with the saturation value."*
That phrasing is the honest register; the dashboard column legend drops it.

## (e) Is the "DERIVED parameter-free" dashboard tag honest?

**No.** It is defensible only under the narrowest reading ("no continuous fit"),
and it is dishonest as presented for four independent reasons:

1. **Self-contradiction on `main`.** The same file carries a dated deprecation
   banner (lines 92–126, "DEPRECATED 2026-08-08: B_gate / B_vol / E_gate / c_λ …
   Removed from the dashboard. They have no basis in the derivation chain.")
   while the code still computes `B_vol` (lines 554–555, 619) and the column
   legend still tags it "**7.584 MeV/nucleon DERIVED parameter-free**" (line
   779). Whichever is newer, the tag and the banner cannot both stand. The
   deprecation was declared in prose but never carried through the code or the
   legend.
2. **Fails the dashboard's own `DERIVED` criterion** ("through the Markov
   trace") — `B_vol` is a Wedderburn side-channel that never touches `tr_M`.
3. **Inconsistent with the dashboard's own provenance table** (lines 671–679),
   which lists `DERIVED` = {B_sym, B_qCLT_fac, m_can, E_C} and *correctly omits
   `B_vol`*. So the machine-printed provenance already excludes it; only the
   hand-written free-text legend mislabels it.
4. **Hides the discrete DOF and the false surprisal framing** — "parameter-free"
   reads as "forced by the framework," which is not what the construct is.

## Corpus-grep (this is already assessed — do not re-declare "open")

- In-file deprecation banner (2026-08-08), lines 92–126: the definitive
  assessment; measured `Σ W ≠ 1`, the A=1 incoherence, the off-chain critique.
- Probe honest verdict, `su4_occupancy_binding_probe.py` lines 245–254.
- Bean `qou-78pt` ("A1: volume term = unnormalized Ocneanu/Markov trace"):
  ROASTs the unnormalised-trace→linear-in-A idea as "a 1-PARAMETER FAMILY …
  Picking the one that yields a_V IS a fit." (That bean targets the SEMF `a_V≈15.6`
  variant; `B_vol` here is the `~8` plateau variant — same defect class.)
- Bean `qou-qlma`: `E₀ = 4.186` is an unexamined default; nothing calibrated
  pins it as the nuclear scale; a Lean floor excludes it for the deuteron.

The only *live* action is hygiene: the dashboard's `B_vol`/`a_V` code + legend
should be brought into line with its own 2026-08-08 deprecation (remove, or
demote the tag from `DERIVED` to `EXPLORATORY`/deprecated with the caveats). Not
fixed here — this is a read-only audit; recorded in bean `qou-lsvj`.

---

## Bottom line (blunt)

`a_V = E₀·ln[3]_q! = 7.584 MeV/nucleon` has no adjustable continuous knob, and
in that narrow sense "parameter-free" is technically true — but that is the least
interesting thing about it and it is not a derivation. The number is `E₀` (a
forced but nuclear-unvalidated electron-scale energy) times the log of the
q-factorial of 3, dressed up as an "occupancy surprisal" even though the weight
isn't a probability. The construction picked the surprisal form over the linear
one *because* surprisal lands near 8, then wrapped it in an ×A "all-knots" story
*after* the single-partition version fell apart — a postdiction of the
long-known ~8 MeV/A liquid-drop plateau, incoherent at A=1, carrying zero
A-structure, and living entirely off the `tr_M` derivation chain. The framework's
own file already says all of this in a deprecation banner dated two weeks before
the "DERIVED parameter-free" tag it sits beside. The 5% agreement is a
coincidence with a 1-sig-fig soft target, and the tag should be corrected.
