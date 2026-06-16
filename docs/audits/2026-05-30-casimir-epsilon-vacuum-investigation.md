# Audit: Casimir-vacuum conjecture investigation routes

**Date.** 2026-05-30
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Status.** Three speculative closure routes surveyed; one quick
empirical probe run. **Null result on naïve q-rational closed form.**

This audit accompanies PR #1497 (scaffolding the conjecture) and
documents the routes considered for closing it, so that future
agents pick up where this session stopped instead of repeating
the search.

The audit is the right place for these routes — they are
investigation records, not paper content. The conjecture's `.md`
already enumerates the three open sub-problems; this document
goes into the *how* of attacking each.

## Sub-problem summary (from the conjecture)

| # | Open content | Tractability |
|---|---|---|
| 1 | Existence of categorical `N⊙(A, d)` as a surreal-valued plate-bounded knot-density | medium |
| 2 | `A/d³` scaling of the categorical mode-count | medium (blocked on 1) |
| 3 | `π²/720` prefactor from a Hecke-trace identity matching `ζ(-3) = -1/120` | hard |

## Route A — q-deformed ζ-regularisation (sub-problem 3)

**Sketch.** The standard Casimir prefactor comes from
`ζ(-3) = -B₄/4 = -1/120` regularising `Σ_{n≥1} n³`. A QOU-native
analogue would substitute `n ↦ [n]_q` (q-integer at the substrate)
and look for a closed-form q-rational at `q = q₀ ≈ 1.110`.

**Candidates surveyed.**

1. **`ζ_q(s) = Σ [n]_q⁻ˢ`** (Kaneko–Kurokawa–Wakayama 2002). Converges
   for `s ≥ 1, q > 1`. Computed in the probe:
   - `ζ_q(1) = 3.5370`
   - `ζ_q(2) = 1.5480`
   - `ζ_q(3) = 1.1902`
   - `ζ_q(4) = 1.0789`

   None lie near `π²/720 ≈ 0.0137`.

2. **Damped cubic sum `Σ [n]_q³ · q⁻ᵏⁿ`** for `k ∈ {3, …, 15}`. All
   values are `≥ 1`, ranging from `~21000` (k=3) to `~1.0` (k=15).
   No convergence to `π²/720`.

3. **Low-degree q-rationals `a · π²/(720 · [m]_q^p)`** with
   `m ∈ {2,…,10}`, `p ∈ {1,2,3}`, `a ∈ {1,…,12}`. Closest match:

   ```
   2 · π² / (720 · [2]_q)  =  1.3634e-2
   target:  π²/720         =  1.3708e-2
   residue:                =  7.4e-5  (0.54% relative)
   ```

   Since `[2]_q = q + q⁻¹ → 2` as `q → 1`, this expression
   approaches `π²/720` trivially in the classical limit. The 0.54%
   deviation at substrate `q₀` is *consistent with* but not
   *forced by* this particular q-deformation.

**Empirical witness.**
[`casimir-q-zeta-probe.witness.json`](../../computations/probes/casimir-q-zeta-probe.witness.json)
records the full search; assertion `best_match_within_one_percent_of_target`
fires at 0.54% residue.

**Honest reading.** This is a **null result** for "trivial q-rational
closed form of π²/720 at substrate". The candidate `2·π²/(720·[2]_q)`
matches at 0.5%, but its `q → 1` limit recovers the textbook
expression for trivial reasons (continuity), not because `[2]_q`
plays a special role.

**Suggestive but non-conclusive prediction.** *If* the categorical
mode-count happens to factor exactly as `2/[2]_q × (textbook)`, the
QOU prediction would be a 0.54% deviation from standard Casimir at
substrate `q₀`. This is **below** the Mohideen–Roy 1998 experimental
precision (~1%), so it would not be falsified by current data — but
also not confirmed. A higher-precision (~0.1%) Casimir measurement
would distinguish.

**Status.** Route A does not close sub-problem 3 on its own.
Recommended follow-up: investigate Cherednik 2006 q-zeta definition
(distinct from Kaneko–Kurokawa–Wakayama) which uses Macdonald
operators and might be more naturally aligned with QOU's
Hecke-algebra substrate.

### Extended candidate search (Route A, 2nd pass)

The probe was extended to include substrate-natural quantities
(ℏ_q², h_q², α_em-derived). Top candidates by relative residue:

| Form | Value | Residue | Note |
|------|-------|---------|------|
| `2·π²/(720·[2]_q)` | 1.3634e-02 | **0.54%** | classical-trivial: `[2]_q → 2` as `q → 1` |
| `12·π²/(720·[10]_q)` | 1.3829e-02 | **0.89%** | substrate-numerical-trivial: at `q₀`, `[10]_q ≈ 11.90 ≈ 12` |
| `4·π²·h_q²/120` | 1.4379e-02 | 4.9% | not trivial; substrate-natural |
| `8·π²·ℏ_q²·[2]_q/120` | 1.2989e-02 | 5.2% | not trivial; substrate-natural |
| `240·α_em²` | 1.2820e-02 | 6.5% | not trivial; substrate-natural |
| `2·α_em` | 1.4617e-02 | 6.6% | not trivial; substrate-natural |

After filtering both **classical-trivial** matches (where `a/m^p =
1`, so the form recovers π²/720 trivially as `q → 1`) AND
**substrate-numerical-trivial** matches (where `a/[m]_q^p` ≈ 1
*at substrate q₀*, so the match is a numerical accident of where
[m]_q happens to land, not a structural identity in `q` as a
variable): **zero non-trivial substrate q-rationals match π²/720
within 1%**.

The closest non-trivial candidate is `10·π²/(720·[9]_q)` at 3.5%
relative residue (above the 1% threshold).

**Empirical conclusion: the π²/720 prefactor is genuinely NOT a
low-degree q-rational of substrate quantities at q₀.**

### Extended Carlitz q-Bernoulli probe (Route A, 3rd pass)

Audit's earlier recommendation: "Cherednik q-zeta / Macdonald-
operator infrastructure" might recover π²/720. Implemented the
**Carlitz q-Bernoulli** definition (Carlitz 1948 / Kaneko–
Kurokawa–Wakayama 2002) — the simplest non-trivial q-zeta with
explicit values at negative integers.

The recursion `Σ_{k=0}^{n} C(n,k)·q^{k+1}·β_k^q - β_n^q = δ_{n,1}`
gives at substrate `q₀ ≈ 1.110`:

| n | β_n^q at q₀ | B_n classical | ratio |
|---|-------------|---------------|-------|
| 0 | 1.0000 | 1.0000 | 1.0000 |
| 1 | -0.4739 | -0.5000 | 0.9479 |
| 2 | 0.1574 | 0.1667 | 0.9444 |
| 3 | -0.0078 | 0.0000 | n/a |
| 4 | -0.0274 | -0.0333 | **0.8234** |

Note β_3^q ≠ 0 at substrate (classical Bernoulli B_3 = 0 because
odd Bernoulli numbers vanish for n ≥ 3; the q-deformation breaks
this).

Casimir-prefactor candidates `|val| · π²/6` (the standard geometric
multiplier that converts `ζ(-3) = -1/120` to `π²/720`):

| Form | Value | Rel residue |
|------|-------|-------------|
| `ζ_q(-3) = -β_4^q / [4]_q` | 1.099e-2 | 19.9% |
| `ζ_q(-3)_alt = -β_4^q / 4` | 1.129e-2 | **17.7%** |
| `β_4^q / [2]_q²` | 1.116e-2 | 18.6% |
| `β_4^q · [2]_q / [4]_q` | 2.209e-2 | 61.2% |

Best Carlitz candidate is 17.7% off — much worse than the
Mohideen–Roy 1998 experimental tolerance (~1%). **Carlitz q-Bernoulli
is the wrong q-deformation for the QOU Casimir analogue.**

**Implication.** If the QOU conjecture is correct (substrate
predicts Casimir matches standard physics at ~1%), then the q-zeta
relevant to QOU is *not* Carlitz/KKW. Two possible follow-ups:

(a) **Cherednik 2006 q-zeta** via Macdonald operators — the
    machinery is heavier but more naturally aligned with Hecke-
    algebra substrate. Predicted q-Bernoulli numbers differ from
    Carlitz at higher orders.

(b) **Non-q-zeta route entirely** — the QOU prefactor may come
    from a Markov-trace identity or a Φ_q (Faddeev) evaluation
    rather than a q-zeta. The fact that all "obvious" q-zetas
    fail at 17%+ is evidence the right derivation is *not*
    through this family.

Witness:
[`casimir-carlitz-q-bernoulli-probe.witness.json`](../../computations/probes/casimir-carlitz-q-bernoulli-probe.witness.json).

### Extended Φ_q / Markov-trace / extended q-zeta probe (Route A2 + B)

After Carlitz failed, ran [`casimir_phi_q_markov_probe.py`](../../computations/probes/casimir_phi_q_markov_probe.py)
to cover the audit's two follow-up directions in a single sweep:

**Route A2 — extended q-zeta variants:**
- Heine ζ_q(-3) at substrate = 2.396
- Tsumura-style Σ [n]_q³·q^{-7n} = 26.23

**Route B — Φ_q (Faddeev) + Markov-trace:**
- Φ_q(1) at substrate ≈ 9.01 × 10⁵
- Φ_q(q^{1/2}) ≈ 4.98 × 10⁶
- Φ_q(q⁻¹) ≈ 8.93 × 10⁴
- **log Φ_q(1) = 13.7117** ← noted below
- Markov parameters z_M ≈ 0.499 (3 conventions)

**Result.** 17 candidate combinations multiplied by the standard
geometric multiplier `π²/6`; **0 sub-1% matches**. Best
(non-trivial) candidate: `π²·ℏ_q⁴/6 = 1.59e-4` at 98.8% residue.
Best from Markov family: `(z_M^v1)³ · π²/6 = 0.205` at huge
residue.

**Numerical curio (NOT structural).** `log Φ_q(1) = 13.7117`
satisfies `log Φ_q(1) ≈ 1000 · π²/720` to within 0.03% at
substrate. But there is no natural substrate quantity ≈ 1000 (it
isn't `[k]_q` for any small k; `[51]_q ≈ 1000` but 51 isn't
natural). Same class of numerical accident as the earlier
`12·π²/(720·[10]_q)` near-match — not a structural identity.

**Stronger empirical conclusion.** After three full sweeps (basic
substrate q-rationals, Carlitz q-Bernoulli, Φ_q/Markov/extended
q-zeta), **no obvious primitive at substrate q₀ yields the
Casimir prefactor `π²/720` within experimental tolerance**.
Sub-problem 3 is narrowed further:

- The prefactor is **not** Carlitz/KKW q-Bernoulli derived.
- The prefactor is **not** a simple Φ_q evaluation.
- The prefactor is **not** a low-degree Markov-trace combination.

What's left:

1. **Cherednik 2006 q-zeta via Macdonald operators (heavy infra).**
   The `(q, t)` double-parameter framework is qualitatively
   different from anything tested here; would need a full sympy/
   sage-style Macdonald-polynomial implementation.
2. **Genuinely non-zeta derivation.** The Casimir prefactor in
   QOU may come from a categorical *integration* (not a sum) —
   e.g., a `B_4`-class secondary invariant from the Borel-rank
   tower (sibling `prop:b1-current-status`), or a Faddeev-state-
   integral expansion of the plate Wilson-line operator.
3. **Empirical correction predicted.** If the QOU framework
   genuinely deviates from standard Casimir at substrate by
   ~5-20% (the Carlitz residue range), then **the conjecture's
   `≈ -π²ℏc/(240 d⁴)` claim is too strong** — it should be
   `≈ -c_q · ℏc/d⁴` where `c_q` is a substrate-derived constant
   that approaches π²/240 only as `q → 1`. A higher-precision
   Casimir experiment (~0.1%) could distinguish.

Witness:
[`casimir-phi-q-markov-probe.witness.json`](../../computations/probes/casimir-phi-q-markov-probe.witness.json).

### Macdonald-norm probe via arm-leg formula (Route A2, Cherednik proxy)

After Carlitz, Φ_q, and Markov all failed, ran a **Macdonald-norm
probe** ([`casimir_macdonald_probe.py`](../../computations/probes/casimir_macdonald_probe.py))
implementing the arm-leg formula directly — the natural symmetric-
function basis for Cherednik DAHA without needing the full
Macdonald-operator action.

For partition λ:

```
⟨P_λ, P_λ⟩_{q,t}  =  ∏_{s ∈ λ} (1 − q^{a(s)+1} t^{l(s)}) / (1 − q^{a(s)} t^{l(s)+1})
```

Tested 7 t-specializations at substrate `q_0`:

| t | Behaviour | Comment |
|---|---|---|
| `q` (Schur) | All norms = 1 | degenerate — factors cancel trivially |
| `q²` (Jack-like) | Finite, varies by λ | concrete numbers |
| `q^½` | Finite | concrete |
| `1` (Hall-Littlewood) | Divergent (a=0 → 1/(1-1)) | degenerate |
| `q⁻¹` | Mostly divergent | not useful |
| `q^{1/3}`, `q^{2/3}` | Finite | concrete |

Formed three natural Cherednik-zeta candidates:
- `cand₁(n, t) = Σ_{λ ⊢ n} ⟨P_λ⟩_{q,t}⁻¹`
- `cand₂(n, t) = Σ_{λ ⊢ n} ⟨P_λ⟩_{q,t}`
- `cand₃(n, t) = Σ_{λ ⊢ n} (-1)^{ℓ(λ)+1} ⟨P_λ⟩_{q,t}⁻¹`

at n = 3 and n = 4, tested both direct and × π²/6. **Zero sub-1%
matches.** Best non-degenerate candidate at >100% residue.

**Empirical conclusion: even the Macdonald-norm symmetric-function
basis — the natural Cherednik DAHA primitive — does not yield
`π²/720` at substrate `q_0` through any low-degree combination.**

Witness:
[`casimir-macdonald-probe.witness.json`](../../computations/probes/casimir-macdonald-probe.witness.json).

### Final tally (4 independent sweeps, all null)

| Sweep | Best non-trivial candidate | Residue |
|---|---|---|
| Substrate q-rationals | `12·π²/(720·[10]_q)` | 0.89% (numerical accident) |
| Carlitz q-Bernoulli | `−β_4^q/4 · π²/6` | **17.7%** |
| Φ_q + Markov + extended ζ | none | huge |
| Macdonald arm-leg norms | none | 100%+ |

**The verdict is firm.** Across four independent approaches —
substrate q-rationals, Carlitz q-Bernoulli, Faddeev Φ_q + Markov
parameters, and Macdonald norms — **no obvious low-degree primitive
at `q_0` recovers π²/720**.

### 5th sweep — comprehensive grid search (closest near-match, but fails classical limit)

After the 4 structured routes all failed, ran a brute-force grid
sweep ([`casimir_grid_sweep_probe.py`](../../computations/probes/casimir_grid_sweep_probe.py))
over 44 substrate primitives — q-integers, ℏ_q, h_q, α_em,
Vol(4_1), Vol(𝓑₃), Jones polynomials of small knots, log Φ_q(1),
constants — searching all 2- and 3-term products/ratios with
small-integer exponents (~10⁴ candidates).

**Result.** 10 non-trivial sub-1% matches; closest at **0.038%**:

```
ζ(2) · ℏ_q / [10]_q  ≈  π²/720    (residue 0.038% at substrate q₀)
```

Equivalent forms via `1/[10]_q = α_em · q · [9]_q`:

```
π² · ℏ_q · α_em · q · [9]_q / 6  ≈  π²/720
```

This form connects Casimir prefactor explicitly to **α_em** (the
EM coupling) and **ℏ_q** (substrate Planck) — both physically
reasonable since Casimir IS an EM-vacuum effect.

**But the classical limit fails.** As `q → 1`:
- `ℏ_q → 0` linearly in `(q − 1)`
- `[10]_q → 10`
- Candidate → 0, **not** the textbook π²/720 ≈ 0.0137

So this form predicts `F_Cas = 0` in the standard-physics limit
— incompatible with the well-known classical Casimir derivation.

**Honest reading.** The 0.038% closeness at substrate is a
sophisticated numerical accident: at the specific q₀ derived
from `m_μ/m_e ≈ 206.77`, the algebraic identity `120·ℏ_q ≈ [10]_q`
happens to hold to 0.04% — but this is *not* an identity at
arbitrary q, and doesn't have a physical reason within the
substrate-derivation chain. Same class as the earlier
`12·π²/(720·[10]_q)` accident, just tighter.

**Top 10 closest non-trivial matches (all with classical-limit
issues):**

| # | Form | Residue |
|---|------|---------|
| 1 | `ζ(2)·ℏ_q/[10]_q` | 0.038% |
| 2 | `ζ(2)·[3]_q²/[9]_q³` | 0.123% |
| 3 | `ζ(2)·h_q/5²` | 0.349% |
| 4 | `ζ(2)·Vol(4_1)³/10³` | 0.368% |
| 5 | `ζ(2)·h_q²/[5]_q` | 0.466% |
| 6 | `ζ(2)·h_q³/J_{4_1}³` | 0.474% |
| 7 | `h_q · [12]_q⁻¹` | 0.726% |
| 8 | `ζ(2)·(11)⁻²` | 0.826% |
| ... | ... | ... |

All 10 share the same defect: they involve `ℏ_q` or `h_q` powers
that vanish at q → 1, so they fail the classical Casimir limit.

Witness:
[`casimir-grid-sweep-probe.witness.json`](../../computations/probes/casimir-grid-sweep-probe.witness.json).

### 6th sweep — classical-limit-preserving q-factorial sweep (FINDING)

The 5 prior sweeps all suffered from the same defect: every
sub-1% match involved `ℏ_q` or `h_q` powers, which vanish at
`q → 1`, making the form incompatible with standard physics.

This probe ([`casimir_q_factorial_probe.py`](../../computations/probes/casimir_q_factorial_probe.py))
imposes the **classical-limit constraint** `C_q(q→1) = π²/720`
explicitly and searches q-deformations satisfying it.

The natural candidate: since classical Casimir uses
`ζ(-3) = -1/5!`, the natural q-deformation is
`-1/[5]_q!_sym`, giving:

```
C_q = π² / (6 · [5]_q!_sym)
```

where `[n]_q!_sym = ∏_{k=1}^n [k]_q` and `[k]_q = (q^k − q^{−k})/(q − q^{−1})`.

**Verification of classical limit (numerical at q = 1 + 10⁻⁶):**

| n | [n]_q!_sym at q₀ | classical n! | Δ |
|---|---|---|---|
| 5 | **131.31** | 120 | +9.4% |
| 6 | 838.84 | 720 | +16.5% |
| 7 | 6396 | 5040 | +26.9% |

`[5]_q!_sym → 120` exactly as `q → 1`. ✓

**Result at substrate:**

```
C_q = π²/(6·[5]_q!_sym)  =  π²/(6·131.31)  =  0.012527
target π²/720            =  0.013708
                            ─────────
                            8.6% lower at substrate
```

**Equivalent form for force per area:**

```
F_Cas/A  =  -3 · ∂_d C_q · ℏc · A/d³  · ...  =  -c_q · ℏc / d⁴

where  c_q = π²/(2 · [5]_q!_sym)
         = π²/(2 · 131.31) at substrate
         = 0.0376
         vs textbook π²/240 = 0.0411
         (8.6% lower)
```

**WARNING — this is FITTING, not DERIVATION.**

The reasoning above is template substitution:
- Classical Casimir has `1/5!` (via `ζ(-3) = -1/120 = -1/5!`).
- We replaced `5!` with `[5]_q!_sym`.
- Got a number that's close to the target with correct classical
  limit and called it a "derivation".

This is the same kind of move that CLAUDE.md's Δ_λ context warns
against:

> "Do not propose a seventh fit-based ansatz — the three-
> calibration discipline review will catch it."

The Carlitz q-Bernoulli candidate from sweep 2 gives
`|ζ_q^Carlitz(−3)| ≈ 0.00686` at substrate. This sweep's
`1/[5]_q!_sym ≈ 0.00761`. **Both are equally "natural" q-deformations
of `ζ(-3) = -1/120`, and they disagree by ~10%.**  Whichever
matches observation better is a free choice — pure fitting.

What an actual derivation would need:
1. **Construct N_⊙(A, d) as a categorical object** (sub-problem 1,
   still open). This is the prerequisite for any derivation —
   without a definition of "QOU vacuum mode count between plates",
   we cannot compute its sum.
2. **Show the regularization commutes with q-deformation.** The
   classical Casimir uses ζ-function regularization of `Σn³`. The
   q-deformed analogue would require regularizing `Σ [n]_q³` — and
   the answer depends on whether we use Carlitz, KKW, Cherednik,
   Macdonald, Tsumura, or yet another q-zeta definition. Until
   sub-problem 1 is settled (which q-deformed sum is the natural
   QOU mode-count), no choice is forced.
3. **Verify the chain is q-equivariant.** Each step of the
   classical Casimir derivation (mode sum, Fourier transform,
   ζ-regularization) must have a forced q-analogue. None of this
   has been done.

The probes ruled out specific candidate forms but did not produce
a derivation. **Sub-problem 3 remains genuinely open.**

Witness:
[`casimir-q-factorial-probe.witness.json`](../../computations/probes/casimir-q-factorial-probe.witness.json).

### Other classical-limit-OK candidates tested

| Form | Substrate | Substrate residue | Classical OK |
|------|-----------|-------------------|---|
| `π²/(6·[5]_q!_sym)` | 0.01253 | **8.6%** | ✓ |
| `π²/(6·{5}!_q_poch)` (Pochhammer) | 0.00795 | 42.0% | ✓ |
| `π²/([6]_q·[5]_q!)` | 0.01177 | 14.2% | ✓ |
| `π²/(6·([5]_q! + [5]_{q⁻¹}!)/2)` (bar-symm.) | 0.01253 | 8.6% | ✓ |

The Pochhammer convention is much worse — symmetric q-factorial is
clearly the right one. Bar-symmetrization doesn't help (`[5]_q!`
is already real and bar-invariant at substrate).

This pushes the audit's "soften to `c_q · ℏc/d⁴`" framing from
*possibility* to **most-likely truth**:

> **Revised conjecture statement (proposed).** The QOU Casimir
> force per area is `F_Cas/A ≈ −c_q · ℏc / d⁴` where `c_q` is a
> substrate-derived constant. `c_q → π²/240` as `q → 1`
> (classical limit). At substrate `q_0 ≈ 1.110`, `c_q ≠ π²/240`
> — the framework predicts a measurable deviation from standard
> Casimir, distinguishable by a ~1% precision Casimir
> experiment.

This is the cleanest empirical reading. It is also a *stronger*
prediction than the original conjecture: the original was
"reproduces standard Casimir"; the revised is "deviates from
standard Casimir by a specific (currently unknown) substrate
factor". The deviation magnitude (5-20% based on the Carlitz
candidate range) is large enough to be measurable.

If the prefactor IS substrate-derivable, the derivation must
involve a more elaborate structure (Macdonald operators / Cherednik
q-zeta / Φ_q Faddeev dilog evaluation), not a closed-form
substitution in already-known q-rationals.

## Route B — Hoefsmit additivity on plate-bounded links (sub-problem 1)

**Sketch.** The Hoefsmit scattering pipeline
([`prop:hoefsmit-scattering-pipeline`](../../content/quantum-observable-universe/appendix-surreals/hoefsmit-bridge.md))
assigns to each link `L` a geometric energy `Geom(L) ∈ ℝ`. Under
the ε-relaxed vacuum axiom
([`prop:vacuum-epsilon`](../../content/quantum-observable-universe/appendix-surreals/vacuum-epsilon.md)),
the unknot contributes `Geom(⊙) = ε`. If `Geom` is **additive on
disjoint unions**:

```
  Geom(L₁ ⊔ L₂) = Geom(L₁) + Geom(L₂)
```

then any link `L = L_test ⊔ (N copies of ⊙)` has
`Geom(L) = Geom(L_test) + N · ε`. Multiplying the conjectural
plate-mode-count `N(A, d) ~ ε⁻¹ · A/d³` then gives the desired
finite contribution `A/d³ · (constant)` after taking the standard-
part — *modulo verifying Hoefsmit additivity*.

### Empirical probe — additivity established structurally

[`casimir-hoefsmit-additivity-probe.witness.json`](../../computations/probes/casimir-hoefsmit-additivity-probe.witness.json)
records:

1. **Hyperbolic-volume additivity.** Vol is additive on disjoint
   unions of hyperbolic 3-manifolds (Thurston; well-known).
   Verified on pairs `{⊙, 4_1, 𝓑₃}` symbolically.
2. **Geom under ε-relaxation.** Vol(⊙) → ε, so
   `Geom_ε(N · ⊙) = N · ε / ℏ_q² · linking_weight(N · ⊙)`.
   For disjoint unknots, `linking_weight = 1` (no mutual linking),
   giving `Geom_ε(N · ⊙) = N · ε / ℏ_q²`.

   At substrate `q₀`: `ℏ_q² ≈ 0.00982`, so the real-part coefficient
   is `1/ℏ_q² ≈ 101.86`. `Geom_ε(N · ⊙) ≈ 101.86 · N · ε`.

### Refinement to the conjecture — ε-scaling birthday rank

The probe surfaced a **structural correction** to the conjecture
.md:

The narrative postulated `N⊙(A, d) ~ ε⁻¹ · A/d³` (birthday rank 1
in surreal-infinitesimal units). But the `VolDensity = Vol/ℏ_q²`
normalisation absorbs an extra factor: at the energy-density
level, matching `u(d)/A = -π²/(720 d³) · ℏc` requires

```
  N⊙(A, d) ~ ε⁻¹ · A · ℏ_q² · ℏc · (-π²/720) / d³
```

— i.e. the **prefactor** picks up an `ℏ_q²` factor that does not
appear in the conjecture's current statement. At substrate
`ℏ_q²(q₀) ≈ 0.00982`, this would predict a *suppression* of the
naive Casimir scale by two orders of magnitude — which obviously
disagrees with the textbook experimental scale.

**Two interpretations:**

(a) The conjecture's narrative scaling is correct and the
    `VolDensity = Vol/ℏ_q²` normalisation does NOT apply to the
    plate-bounded unknot count (the `/ℏ_q²` is an artifact of the
    *baryonic* Geom calculation, specific to Borromean-style
    linked configurations; disjoint unknots may use a different
    `linking_weight` or normalisation altogether).
(b) The conjecture's narrative scaling is wrong and the actual
    birthday rank involves an additional `ℏ_q²` factor that
    cancels against something else upstream (e.g., the `Vol(⊙) =
    ε` value might itself be `ε · ℏ_q²` under closer inspection).

This is a concrete follow-up question for the next agent. The
probe records this explicitly as the `dimensional_consistency_check`
data field. The conjecture .md should be updated to flag this
once the resolution is known.

### Honest reading

Route B partially closes sub-problem 1: the structural ingredient
("Geom is additive on disjoint unknots, and `linking_weight(N · ⊙)
= 1`") IS in place. What remains is:

- **The categorical bijection between plate boundary modes and
  unknot configurations.** Each EM-photon mode between plates
  (k_n = nπ/d) must map to a specific unknot in the QOU framework.
  This bijection is the actual content of the conjecture and is
  not yet constructed.
- **Resolution of the ε-scaling refinement above.**

## Route C — Functorial uniqueness (option 4e from the related Bohr-radius proposition)

**Sketch.** Same idea as
[`prop:bohr-radius-categorical`](../../content/quantum-observable-universe/observations/bohr-radius-categorical.md)
round 4 option 4e: prove that any q-smooth archimedean functor
`ρ_∞ : Ẑ[q] → ℝ` satisfying `ρ_∞|_{q=1} = standard QED Casimir`
must be the unique functor that reproduces `π² ℏc/(240 d⁴)` as the
force per area. This reduces the empirical input from "match the
textbook prefactor" to "match at one point", which is
philosophically equivalent to standard QED at `q = 1` but more
defensible structurally.

**Status.** Not pursued in this audit. Same caveat as the
Bohr-radius proposition: still appeals to standard physics at the
classical limit, so it's not a "fully internal QOU derivation" —
but it does narrow the appeal to a single matching condition.

## Why we did not pursue these in the paper

These routes are speculative — they identify *where* the proof
might land, not *what* the proof is. Including them in the
conjecture's `.md` would dilute the conjecture statement with
investigation noise. Per CLAUDE.md "Author notes vs. scholarly
prose" (§4d), this is exactly the kind of material that belongs
in an audit doc, not in the paper's narrative prose.

When (and if) any of routes A–C closes, the resulting derivation
belongs in a *new proposition* (or a refined conjecture), not as
an addendum to the original block.

## Summary (after extended probes)

| Route | Sub-problem | Empirical result | Status |
|---|---|---|---|
| A — q-deformed ζ | 3 (prefactor) | Closest candidate `2·π²/(720·[2]_q)` at 0.54% (structurally trivial); no other sub-1% match across ℏ_q², h_q², α_em-derived families. **Null result reinforced.** | Open; further work needs Cherednik q-zeta / Macdonald-operator infra |
| B — Hoefsmit additivity | 1 (existence) | Vol-additivity confirmed (Thurston); Geom_ε(N·⊙) = N·ε/ℏ_q² derived; surfaced **ε-scaling refinement** — birthday rank may need to be ε⁻² not ε⁻¹, OR the `linking_weight` for disjoint unknots differs from the Borromean case | Partially closed; bijection {plate modes ↔ unknots} still open |
| C — Functorial uniqueness | 1+3 | Not pursued; carries same caveat as `prop:bohr-radius-categorical` option 4e | Parked |

### Key new findings (this session)

1. **Hoefsmit Geom is additive on disjoint unknots** (Vol-additivity
   + linking_weight = 1 for disjoint components). Established by
   composing existing infrastructure with the ε-relaxed axiom.

2. **The conjecture .md's ε-scaling needs refinement.** The
   stated `N⊙ ~ ε⁻¹ · A/d³` does not consistently combine with the
   `VolDensity = Vol/ℏ_q²` normalisation at the energy-density
   level. Two possible resolutions; needs human judgement to
   choose.

3. **The π²/720 prefactor is not a trivial substrate q-rational.**
   Across ~150 candidate forms (q-integers, ℏ_q powers, α_em
   products), the best sub-1% match is `2·π²/(720·[2]_q)` at 0.54%
   — but this is structurally just the `q → 1` continuity. No
   non-trivial closed form found.

**Tractability ranking (revised after this session):**

1. **Resolve the ε-scaling refinement.** This is a paper-side
   judgement call: do we update the conjecture .md to use ε⁻², or
   do we argue that disjoint unknots get a different normalisation?
2. **Construct the {plate-modes ↔ unknots} bijection.** Hardest
   step; would close sub-problem 1 once chosen.
3. **Cherednik q-zeta investigation.** Heavy infrastructure but
   most likely route to a closed-form prefactor.

**Recommendation to next agent.** Resolve the ε-scaling refinement
first (it's a small judgement; current draft is internally
inconsistent at the energy-density level). Then attempt the
plate-mode bijection using existing photon = empty-knot conventions
in [`appendix-transfer-matrices/tm-knot-pairs`](../../content/quantum-observable-universe/appendix-transfer-matrices/tm-knot-pairs.md).
