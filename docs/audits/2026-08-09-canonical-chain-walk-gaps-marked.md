# Canonical derivation chain, walked step by step, with gaps marked

> **Notation note.** This document predates the 2026-09-05 calibration rename and uses
> the superseded symbols `𝔇_β` (CAL-2) and/or `𝔇_π` (CAL-3). Those are now
> `P_skew^β` (the bar-skew β-channel) and `P_avg^π` (the bar-even π-channel); the
> `𝔇` family is reserved for genuine decay rates (`𝔇_n`, `𝔇_μ`, `𝔇_K` = ℏ/τ).
> The analysis below is left as the record of what was analysed at the time.

**Date**: 2026-08-09
**Branch**: `claude/anchor-followups-2026-08-08`
**Beans**: `qou-qlma` (α scale), `qou-c6gx` (interface), `qou-h7mh` (coordination),
`qou-840k` (float64), `qou-cw27` (Li₂^q guard)
**Status**: Audit. Read-only; no producer run, no witness written.

The chain as AGENTS.md states it:

```
q₀ → categorical action → Yekutieli non-abelian Stokes → H_n(q)
   → Wedderburn (λ ⊢ n) → Frobenius pairing tr_M = Σ_λ y_λ χ_λ
   → confinement SDP → canonical T_w → Archimedean functor at q₀ → MeV
```

Each step below is marked:

| mark | meaning |
|---|---|
| **CAL** | a declared calibration — an input by construction, not a success |
| **DERIVED** | follows from earlier steps with no new input |
| **ASSUMED** | a choice made in the code or the prose without a derivation |
| **GAP** | the chain is broken, unverified, or internally inconsistent here |
| **NOT AUDITED** | outside what this session checked — listed so it is not mistaken for verified |

---

## Step 0 — the three calibrations · **CAL**

AGENTS.md §"calibration canon": the canonical inputs are the decay-width triple
`(m_e, 𝔇_β, 𝔇_π)`, with masses and `Q_β` as *numerical proxies*. Owner ruling
2026-06-26 supersedes the older "three measured masses" wording.

These are inputs. Nothing here is a prediction, and the corpus says so.

## Step 1 — q₀ from CAL-2 · **CAL + DERIVED**, with an **owner-gated fork**

`m_μ/m_e = Vol(4₁)/ℏ_q²`, `ℏ_q = 1 − q₀⁻¹`, `Vol(4₁) = 2·Cl₂(π/3) ≈ 2.0299`,
inverted for `q₀ ≈ 1.10998`.

**Fork (declared, not a defect):** production pins q₀ on the *proton* ratio
`m_p/m_e` (0.06 ppb) rather than the muon ratio (22 ppb). The two anchors differ
by **11.54 ppb**, making `m_μ/m_e` a 9.5σ cross-check. Owner-approved as a
precision substitution, not a fourth calibration.

## Step 2 — categorical action → Yekutieli non-abelian Stokes → H_n(q) · **NOT AUDITED**

This session did not examine these steps. They are the link between the
categorical substrate and the Hecke algebra, and nothing below should be read as
evidence for them.

## Step 3 — the Hecke parameters h, δ · **DERIVED**

`h = q₀ − 1/q₀` and `δ = flavor_split_leading(q₀)`, both exact from q₀ at 50 dps
(the δ path was de-wired 2026-06-29 from a *posited* subleading to a *proven*
leading form). Verified exact this session inside a single `workdps` guard.

## Step 4 — the Markov parameter z · ~~ASSUMED — GAP 1~~ → **DERIVED**

> **CORRECTION, same day.** This step was first marked ASSUMED. That was wrong,
> and the correction matters because it eliminates a route.
>
> `y_lambda_at(n, q)` takes **only q** — there is no z argument. Since
> `tr_M = Σ_λ y_λ χ^λ`, the value of `tr_M(σ)` is fully determined by q, and the
> Markov parameter is a *consequence* of the weights rather than an input.
> Checked at n = 2, where `χ^{(2)}(σ) = q` and `χ^{(1,1)}(σ) = −1/q`:
>
> ```
> y_(2)   = 0.69632542639163310909
> y_(1,1) = 0.30367457360836689091     Σ y_λ d_λ = 1 exactly
> tr_M(σ) from y_λ         = 0.49932033418369445241
> 1/(√q + 1/√q)            = 0.49932033418369445241     residual 7.3e-31
> ```
>
> So `z_m` is **derived**, not posited, and it cannot be retuned independently —
> doing so would contradict `y_λ`. The open choice is one level up: *which member
> of the Ocneanu family* (equivalently which N) the weights come from. The corpus
> already states that as open — `ocneanu_N_lockin_probe.py`: "**Why the mass
> channel is the `N = 2` one remains open**", while also proving N = 3 cannot be
> reached by retuning because it re-weights channels the mass pipeline uses.
>
> **And that route is now closed too.** Solving for the N that would reproduce
> AME(²H), in `z = 1/[N]_{√q}`:
>
> ```
> crossing            required z     required N
> colour-weighted     0.6922207      1.4439154
> σ  (d = 0)          0.5877625      1.6999103
> σ⁻¹ (d = −h)        0.7968228      1.2546575
> ```
>
> Every one is **non-integer and below 2** — not an SU(N) quantum-group point at
> all. Adopting one would be a continuous fit to a single datum, which the
> corpus's own anti-fit discipline forbids.
>
> A pleasing identity fell out on the way, worth recording: the isospin projector
> scalars derived earlier *are* the n = 2 Jones–Markov weights —
> `μ₊ = y_(2)` and `μ₋ = y_(1,1)` to 3.6e-31. The eightfold-way decomposition and
> the Wedderburn weights are the same object at n = 2, not two constructions that
> happen to agree.
>
> The original ASSUMED reasoning is kept below because the link-invariance point
> it makes is still true and still unresolved — it is just not a free parameter.

### (original text, retained — the link-invariance defect is real)

`markov-z-reconciliation.md` documents **two** parameters and the corpus uses
the second:

```
z_J = (q−1)/(q^½+q^−½)²  = 0.0274199   Jones; makes tr a LINK INVARIANT
z_m = 1/(q^½+q^−½)       = 0.4993203   ALL mass and binding computations
```

with `z_J = (q−1)·z_m²` (verified). The doc states plainly that `z_m` is the
convention **"without the writhe prefactor"**, and that the `(q−1)` in `z_J` is
exactly what "makes `J_L(q)` independent of the braid representative".

**The gap.** Nothing derives the choice of `z_m`. And the choice has a
consequence the corpus does not draw: under `z_m`, **tr_M is not a link
invariant — it depends on the braid representative**. That is the same defect as
the measured nucleon-ordering dependence (B varies by up to **2.88 MeV** over
permutations of `['p']*Z + ['n']*N`). Two symptoms, one cause.

~~`z_m = 1/[2]_{√q}` is also specifically the **Temperley–Lieb / SU(2)**
value…~~ **CORRECTED 2026-08-09** — see bean `qou-qlma` and `computations/y_lambda_su_n.py`: this is convention **C** (full-Hecke Ocneanu), NOT Temperley–Lieb. TL/SU(2) is convention **D** at `z = q³/(q²+1) = 0.6126880`; `D ≠ C` is Lean-proved and they differ by 195.8 ppm on `β_Bor`. C has `y_(1³) = 0.0227 ≠ 0`, so it does not carry the N=2 row cap, and it matches **no integer N** (effective N = 2.5995). The `1/[3]_q = 0.3285` "SU(3) rival" quoted here was also
invented — the real SU(N) weights are quantum dimensions (hook-content), not
`1/[N]`.

## Step 5 — the braid word and interface templates · **ASSUMED — GAP 2**

`mass_at_3A_proper.py:337-338`: `_X_PP = (1, 0)` (σ) and `_X_NN = (1, −h)` (σ⁻¹)
are hardcoded literals. Only the δ inside the colour-weighted p–n template is
derived.

**Two sub-gaps:**

- The assignment is by **electric charge**, but the strong force is charge
  independent. Lean `charge_independence_iff` proves `L_pp = L_nn ⟺ h = 0`, i.e.
  the σ/σ⁻¹ assignment can satisfy charge independence only at `q = 1`. The
  model's entire ³H/³He mirror splitting, `α(L_nn − L_pp) = 2.2708 MeV`, is an
  artifact of this choice (nature: 0.764 MeV, mostly Coulomb).
- `ordering = ['p']*Z + ['n']*N` is hardcoded. A nucleus has no ordering, so the
  bond multiset is not well defined — up to 2.88 MeV of non-physical freedom, and
  the convention is not even the best choice (`³He = pnp` gives +0.79%,
  canonical `ppn` gives −11.9%).

## Step 6 — Wedderburn weights y_λ · **DERIVED**, with a **precision cap**

`wedderburn_jones_markov.y_lambda_at(n, q₀)` — the closed-form Jones–Markov
hook-length weight, a function of q₀ alone. **Not** an SDP shadow price (an old
audit says otherwise; corrected 2026-08-08).

**Cap:** fast-path 2 returns `sp.Float(nstr(y, 30), 30)` — the weights are
truncated to **30 digits** "for consumer compatibility". This is the binding
precision constraint on every tr_M, and it is why the residuals below all sit at
~1e-31 rather than the ~1e-50 the χ^λ path reaches. Corpus claims of "1e-50
agreement" are about χ^λ, not tr_M. Tracked on `qou-840k`.

## Step 7 — the Frobenius pairing tr_M = Σ_λ y_λ χ_λ · **DERIVED**

Checked this session by four routes for ²H:

```
tr_free = tr_p · tr_n              7.9e-31
tr_atom = tr_free·(z + d_cw)       1.2e-31
Markov  tr(W·σ) = z·tr(W)          9.1e-32
Σ y_λ d_λ = 1  (normalisation)     7.7e-31
transfer kernel vs seminormal      4.1e-15   ← the only genuinely independent route
```

**Caveat the corpus already states, and this audit repeats:** the
2026-06-04 handover records that `cross_check_trM_1ppb.py` "proves four methods
*agree* (all share `Σ y_λ χ^λ`). **Agreement ≠ correctness.**" The same applies
here — only the seminormal route is structurally independent, and it is f64,
so it bottoms out at 4e-15.

## Step 8 — the confinement SDP · **DOWNSTREAM — does not validate**

The SDP is *after* the pairing in the chain, so its `n_target` is an **input it
reproduces**, not a check it applies. For ²H it records
`tr_M_rel_err_vs_witness = 1.43e-16`, which confirms only that the solver
reproduced its own input. Compounding this, that `n_target = 0.38828642407479047`
is the colour-**blind** trace (Δ 1.87e-08), not the colour-weighted one the
shipped braid word produces (Δ 7.07e-05) — so the SDP was never solved against
the production word.

## Step 9 — the Archimedean functor: dimensionless → MeV · **DERIVED — GAP 3**

`beta-decay-energy-scale.md` gives the scale as

```
E₀^(N=0) := m_e/(q₀(q₀−1)) ≈ 4.186 MeV     "the electron rest energy per Planck time"
```

derived from CAL-1 + CAL-2 alone, with a tower-summed variant
`E₀^full = E₀/(1−ℏ_q²) ≈ 4.228`.

**Its only validation is at the β-decay scale**, via the dimensionless
normal-form difference `Δ(net) ≈ −0.188291`:

```
E₀^(cal) = Q_β/|Δ(net)| = 0.782333/0.188291 = 4.1549 MeV
E₀ derived                                  = 4.1860 MeV      agreement 0.75%
```

**The gap.** That check fixes the **product** `E₀ × Δ(net)`. The binding formula
reuses `E₀` with a *different* dimensionless multiplier (`ln(tr_free/tr_atom) ≈
0.929` instead of `0.188`), and nothing validates `E₀` at that scale. "One α"
is therefore an assumption, and this session confirmed nothing else pins it:

- the canonical nucleon mass does **not** use E₀ (muon-anchored F_Bor identity
  from a witness, "deliberately NO formula fallback"), so the +1.35/+2.39 ppb
  m_p/m_n agreement is evidence for F_Bor, not for E₀;
- the meson path **does** use E₀ and fails — witness err_ppm from 143220 to
  998158, with one 1677 ppm outlier.

**A live inconsistency inside this step.** Two values occupy the E₀ slot and are
consumed by disjoint script families:

```
E_0 = m_e/(q₀(q₀−1))         = 4.185981 MeV   DERIVED
E_0_CALIBRATION_MEV = Q_β(n) = 0.782333 MeV   CODATA (experimental)
ratio 5.350636
```

`mass_at_3A_proper`'s own `--E0` default is the 0.782 one while the binding path
it feeds uses 4.186. **Owner ruling 2026-08-09: keep only the derived form and
deprecate the other.** Note the derived route already exists for Q_β too —
AGENTS.md gives `Q_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³) ≈ 0.784 MeV`, a 0.17%
cross-check — so "keep only derived" is implementable without losing the Q_β
channel. Not yet applied: ~15 files touch `E_0_CALIBRATION_MEV`, several marked
CAL-3, and wave 4 was mid-run.

## Step 10 — the binding functional · **DERIVED this session**

Not a choice. `tr_M` is multiplicative (Step 7) and energy is extensive, so the
map must satisfy `f(xy) = f(x) + f(y)` — Cauchy on `(ℝ₊,×)`, whose only
continuous solutions are `c·ln x`. Measured: the log form is extensive to 0, the
linear form misses by 1.4875 and carries a hard ceiling `α·tr_free ≈ 4.2 MeV`
that AME exceeds for every nucleus with A ≥ 3.

## Step 11 — the result, and the contradiction · **GAP 4**

Lean `QOU.QBeta.InterfaceScalar`, sorry-free, `lean`-direct exit 0:
`z ≤ 1/2` for every q by AM-GM, `d ≤ 0` from the Hecke range, so `μ ≤ 1/2` and

```
B_bond = −α·log μ ≥ α·log 2 = 2.90150 MeV        vs  B_AME(²H) = 2.22457
```

**AME is 30.43% below a floor that holds for every q, every crossing
convention, every multiplicity, and every N in an SU(N) choice of z.**
Contrapositively `α ≤ B_AME/log 2 = 3.20937 MeV` is required, and the derived
`α = 4.18598` exceeds it.

**This is a genuine internal contradiction, not a modelling shortfall**, and it
is the sharpest open item in the chain.

---

## The gaps, ranked (revised after the Step 4 correction)

| # | step | gap | severity |
|---|---|---|---|
| 4 | 11 | derived α violates the Lean floor by 30.43%; ²H unreachable in principle | **contradiction** |
| 2 | 5 | **the braid word itself** — templates assigned by charge (breaks charge independence), nucleon ordering arbitrary (2.88 MeV), one quark pair out of 3×3 | **primary open route** |
| 3 | 9 | α validated only at the β-decay scale — but see below: α *cancels*, so this is hygiene, not a route | medium |
| 1 | 4 | `z_m` is DERIVED from y_λ. Its link-invariance defect is real and unresolved, but it is **not a free parameter** and cannot be retuned | **eliminated as a route** |
| — | 6 | y_λ capped at 30 digits; "1e-50" claims overstated for tr_M | low |
| — | 8 | SDP is downstream and validates nothing; its n_target is the wrong (colour-blind) trace | medium |
| — | 2 | categorical action → Stokes → H_n(q) not audited | unknown |

## Everything that is *not* the braid word has now been eliminated

Collecting the results, for ²H specifically:

| candidate | status |
|---|---|
| the functional (`−α ln` vs `α·Δtr`) | **derived** — multiplicativity + extensivity force the log form |
| α, in any form `m_e·f(q₀)` | **cancels** — `B(2H)/Q_β` is α-free and off by 1.7355× |
| the Markov parameter z | **derived** from y_λ (7.3e-31) |
| the Ocneanu member / N | **fit-only** — required N is non-integer, 1.25–1.70, no SU(N) point |
| the crossing template d ∈ [−h, 0] | **bounded** — Lean `mu_le_half` ⇒ multiplier ≥ 0.6945 |
| coordination | **absent at A = 2** — one bond has no topology |

With z derived and d bounded, the dimensionless multiplier `−ln(z + d)` is
confined to `[0.694507, 1.236978]`, while ²H needs **0.531432**. That is outside
the range, and every input to the range is now either derived or calibrated.

**So the deuteron is unreachable by any parameter choice in the framework as
structured.** Whatever closes it has to be *structural* — the braid word for ²H
itself: how many strands, how many inter-nucleon crossings, which quark pairs
participate, and whether the closure is the right one. That is GAP 2, and it is
the only route left.

Concretely, the things in GAP 2 that were never derived: the atom word braids
**one** quark pair out of the 3×3 available across the interface; the interface
sits at a single generator `σ_{3k+2}`; the nucleon ordering is hardcoded; and
the transfer kernel structurally cannot express a conjugated (non-monotone)
interface, so alternatives have never been evaluated.

## One constraint on any fix, from the corpus's own discipline

The 2026-06-04 handover rules that **a per-channel E₀ is a fit signature**:
"a per-channel E₀ ≠ the universal `m_e/(q₀(q₀−1))` — that is the fit signature".

So resolving gap 4 by introducing a separate *nuclear* α would be, by the
framework's own standard, a fit. The admissible resolutions are narrower:

1. the universal α is wrong and must change **everywhere** (and then Step 9's
   0.75% β-decay agreement has to survive, which it will not — that agreement is
   what currently fixes α);
2. the dimensionless multiplier is wrong — i.e. `ln(tr_free/tr_atom)` is not the
   right dimensionless binding number, which throws the question back to gaps 1
   and 2 (`z_m`, the templates);
3. the framework records the 30.43% as a known, bounded defect.

**Superseded the same day.** Route (2) said "the dimensionless multiplier is
wrong ... which lands on z_m". The Step 4 correction shows z_m is derived, so
route (2) survives but relocates: the multiplier is wrong because the BRAID WORD
is wrong, not because z is. See "Everything that is not the braid word has now
been eliminated" above.

Given that Step 10 derives the functional and Step 11 proves the floor, **(2) is
the only route that can close ²H without breaking β-decay** — and it lands
squarely on `z_m`, the one parameter in the chain that is neither calibrated nor
derived.
