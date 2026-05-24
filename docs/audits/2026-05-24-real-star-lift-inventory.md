# Audit — Real.* engineering lift inventory: char p, p-adic, complex, formal-series

**Branch**: `claude/gifted-feynman-U7ckD` (PR #1127).
**Date**: 2026-05-24.
**Companion**: triggered by the q_0-reality discussion; the owner
asked *"any generalization of Lean engineering (e.g. `Real.sqrt`,
`Real.rpow`) so we can make as broadly applicable as possible
(e.g. char p fields, p-adics, etc.)? Can we generalize the paper
similarly? Want to keep as few assumptions as possible out of the
algebra/categorical setup."*

This audit:

1. **Inventories** every use of `Real.*` in the QOU Lean and Python.
2. **Categorizes** each by lift difficulty (LEVEL 1-4).
3. **Reports** per-realization viability (ℝ, ℂ, ℂ_p, 𝔽_q, R⟦h⟧).
4. **Recommends** which substrate files lift trivially, which need
   typeclass machinery, which are genuinely archimedean.

## TL;DR

| Construct | Lean uses | Lift level | Notes |
|---|---:|---|---|
| `Real.sqrt` | 521 | **2** | `HasSqrt R q` typeclass; identities like `b² = 1 − 1/[2]_q²` are algebraic |
| `Real.pi` | 142 | **4** | Genuinely archimedean (transcendental ℝ-constant) |
| `Real.log` | 107 | **3 / 4** | LEVEL 3 (formal series for q-log); LEVEL 4 for archimedean log |
| `Real.exp` | 77 | **3 / 4** | LEVEL 3 (formal series); p-adic exp has restricted radius |
| `Real.rpow` | 43 | **2** | `q^(k:ℤ)` is generic; `q^(x:ℝ)` is archimedean |
| `Real.cos` / `Real.sin` | 26 / 25 | **3** | Formal q-series in any ℚ-algebra |
| `q > 1` ordering predicate | 211 files | **2** | Replace with `‖q‖ > 1` over normed field |

**Substrate / archimedean Lean balance**: 67 files use generic
`{R : Type*}` (§7c-compliant); 492 files are ℝ-specialized
(~12 % generic). **Plenty of room** to push the §7c lift.

## 1. The 4-level lift taxonomy

| Level | Definition | Example | Can lift to |
|---|---|---|---|
| **1 — trivial / algebraic** | Pure ring-theoretic identity; works in any `[CommRing R]` with `q ∈ R^×`. | `[n]_q := (q^n - q^{-n})/(q - q^{-1})`; `h_q := q - q^{-1}` | any CommRing |
| **2 — typeclass** | Needs an extra structural property: `HasSqrt R q`, `IsCompleteNormedField R`, `Field R + AlgClosed R`. | `Real.sqrt q` (Hoefsmit) needs `q` to have a sqrt in R | ℝ, ℂ, ℂ_p (cond.), 𝔽_q (cond.), Hensel-stable rings |
| **3 — formal series** | Lives as formal power series in `R⟦h⟧` or `R⟦q-1⟧`; convergence is realization-specific. | `Φ_q(z) = Σ z^n / (q; q)_n`; `cos_q`, `sin_q` | any ℚ-algebra (formal); analytic in ℝ/ℂ; restricted in ℂ_p |
| **4 — genuinely archimedean** | Transcendental ℝ-constant, ordering, non-discrete topology, CODATA value. Cannot lift without losing the meaning. | `Real.pi`; `q > 1` strict ordering; `CODATA_M_E_MEV = 0.5110` | ℝ only |

## 2. Per-realization viability matrix

| Realization | Hecke / bar / Frobenius / Markov | Hoefsmit sqrt | q-series (Φ_q, Li_2^q) | CODATA observables |
|---|---|---|---|---|
| **ℝ, q > 1** *(current)* | ✓ | ✓ `Real.sqrt`, q > 0 ⇒ exists | ✓ analytic | ✓ |
| **ℂ, ‖q‖ > 1** *(PR #1127)* | ✓ | ✓ branch choice (use `Im q ≥ 0` cut) | ✓ analytic in disc | n/a |
| **ℂ_p (p-adic)** | ✓ | ⚠ Hensel-conditional on `1 − 1/[2]_q² ∈ (ℂ_p^×)²` | ✓ (formal); convergence `‖x‖_p < p^{-1/(p-1)}` | n/a |
| **𝔽_p / 𝔽_q (char p > 0)** | ✓ (if `p ∤ q`) | ⚠ Frobenius-conditional; ~½ of `F_p^×` are squares | ⚠ Many q-coefficients vanish for `p ∣ [n]_q` | n/a |
| **R⟦h⟧ formal series** | ✓ | ⚠ formal sqrt only if leading coeff is a square in R | ✓ defining (Faddeev / Rogers as formal series) | n/a |

**Bottom line**: the pre-Archimedean substrate (Hecke quadratic, bar
involution, Frobenius pairing, Markov trace symbolically) lifts to
**ALL** of these realizations. Hoefsmit and q-series lift with
typeclass conditions. CODATA stays in ℝ.

## 3. Recommended substrate lift targets

Files already generic over `{R : Type*}` (§7c-honored, 67 files):

```
braids-and-knots/hq-bi-filtration.lean
braids-and-knots/explicit-central-idempotent.lean
braids-and-knots/bar-involution.lean
braids-and-knots/q-zero-complex-extension.lean    ← new (PR #1127)
braids-and-knots/lusztig-vs-hermitian-bar.lean    ← new (PR #1127)
quantum-observable-universes/categorical-q-lie-bracket.lean
... (62 more)
```

Files specialized to `(q : ℝ) (hq : 1 < q)` that **could** lift to
`(q : R) (hq : IsUnit q)` (no archimedean tactics in proof body —
candidate list, requires per-file verification):

```
braids-and-knots/hecke-quadratic.lean           — pure algebraic
braids-and-knots/markov-trace-symbolic.lean     — symbolic ℤ[q^±]
braids-and-knots/bar-involution-c5-via-q2.lean  — algebraic identity
braids-and-knots/wenzl-hook-content.lean        — combinatorial
... (~15-20 more candidates pending audit)
```

Files **genuinely archimedean** (do not lift):

```
archimedean-universe/*.lean                     — by construction
observations/*-numerology.lean                  — CODATA comparisons
descartes-universe/q-zero-pin.lean              — q_0 ≈ 1.1098 ℝ pin
braids-and-knots/hoefsmit-V21-cos-symmetrization.lean
braids-and-knots/markov-trace-factorization.lean  — uses linarith on q > 1
```

## 4. q-deformed special functions — explicit classification

| Function | Definition | Level | Lift target |
|---|---|---|---|
| $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ | algebraic | **1** | any CommRing with $h_q \neq 0$ |
| $[n]_q! = \prod_{k=1}^n [k]_q$ | algebraic | **1** | any CommRing |
| $\binom{n}{k}_q$ (Gauss binomial) | algebraic | **1** | any CommRing |
| $\hbar_q = (q-1)/q$ | algebraic | **1** | `Field R`, `q ≠ 0` |
| $h_q = q - q^{-1}$ | algebraic | **1** | `GroupWithZero R` |
| $z_{\mathrm{mkv}} = 1/(q^{1/2}+q^{-1/2})$ | needs `q^{1/2}` | **2** | `HasSqrt R q` |
| $\Phi_q(z)$ (Faddeev) | series $\sum z^n / (q;q)_n$ | **3** | ℚ-algebra (formal); analytic in `‖q‖ < 1` |
| $\mathrm{Li}_2^q(z)$ (Rogers) | series | **3** | ℚ-algebra (formal); $\Phi_q$-conjugate |
| $\cos_q(x), \sin_q(x)$ | series | **3** | ℚ-algebra (formal) |
| $\cosh(h), \sinh(h)$ | series (no $q$) | **3** | ℚ-algebra (formal) |

## 5. Hoefsmit sqrt — the only Level 2 entry in production

The Hoefsmit seminormal representation entries involve $\sqrt{f(q)}$
for various $f$. The dominant occurrence:

$$b^2(q) \;=\; 1 \;-\; \frac{1}{[2]_q^2}$$

(`hoefsmit-quantum-two-identity`, [`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md):69).

**Algebraic identity**: states over any `[CommRing R]` with `[2]_q` a unit.

**Sqrt existence**: realization-dependent.
- **ℝ**, $q > 0$, $q \neq 1$: $[2]_q^2 > 1 \Rightarrow 1 - 1/[2]_q^2 > 0 \Rightarrow$ sqrt is real and positive.
- **ℂ**, $\|q\| > 1$: sqrt exists, branch by `Im b ≥ 0`.
- **ℂ_p**: Hensel-conditional on $1 - 1/[2]_q^2 \in (\mathbb{Z}_p^\times)^2$.
- **𝔽_p, p ≠ 2**: $1 - 1/[2]_q^2$ is a square in $\mathbb{F}_p^\times$ ~50 % of the time.

Lift to a `HasSqrt R x` typeclass: trivial. Lean proof of the
$b^2$ identity itself: already generic over `[Field R]` per §7c.

## 6. p-adic specialization — what works, what breaks

| Substrate piece | p-adic status |
|---|---|
| Hecke quadratic `σ_i² = h_q σ_i + 1` | ✓ algebraic |
| Bar involution `q ↦ q^{-1}`, `σ_i ↦ σ_i^{-1}` | ✓ algebraic |
| Frobenius pairing $\langle a, b \rangle_F$ | ✓ algebraic |
| Markov trace $\mathrm{tr}_M$ (symbolic in $\mathbb{Z}_p[q^\pm]$) | ✓ algebraic |
| Hoefsmit seminormal `b² = 1 − 1/[2]_q²` | ⚠ sqrt may not exist in $\mathbb{Z}_p$ (Hensel-conditional) |
| $\Phi_q(z)$ series | ⚠ convergent only for $\|z\|_p < 1$ and $\|q\|_p < 1$ (or similar) |
| $\mathrm{Li}_2^q(z)$ series | ⚠ same |
| Real.log / Real.exp / Real.cos | ⚠ p-adic log/exp restricted radius (`‖x‖_p < p^{-1/(p-1)}`) |
| CODATA-value comparisons | ✗ not meaningful in ℂ_p |

**Verdict**: the substrate algebra is fully p-adic-portable; the
q-series and special functions need formal-series treatment with
convergence diagnostics.

## 7. Characteristic-p (𝔽_p, 𝔽_q) — what works, what breaks

| Substrate piece | char-p status |
|---|---|
| Hecke quadratic | ✓ if `p ∤ q` and `p ≠ 2` |
| Bar involution | ✓ (always — algebraic) |
| Frobenius pairing | ✓ (provided non-degeneracy: $[n]_q! \neq 0$ for relevant `n`) |
| Markov trace | ⚠ `tr_M(L_+) - tr_M(L_-) = (q - q^{-1}) tr_M(L_0)` requires $q \neq q^{-1}$ |
| Hoefsmit sqrt | ⚠ Frobenius-conditional |
| q-series | ⚠ all $[k]_q$ in denominator may vanish for special $q$ |

In particular, **roots of unity** $q^N = 1$ are a special-case zoo
(Verlinde categories, modular tensor categories — well-studied but
not the current QOU realization). The QOU framework's choice
$q_0 \approx 1.110$ is *generic* — no $[n]_q$ vanishes — so all
substrate identities specialize without issue.

## 8. Recommended workplan

| Item | Scope | Effort | When |
|---|---|---:|---|
| **A1** (this audit) | Inventory + classification | done | — |
| **A2 (light)** | Lift ~15-20 substrate Lean files with no archimedean tactics | ~2-3 days | this PR (subject to per-file verification) |
| **A3 (full)** | NormedField R typeclass refactor + realization adapters (ℂ, ℂ_p, 𝔽_q, R⟦h⟧) | ~2-3 weeks | research-grade, separate follow-up branch |

**A2 verification protocol**: for each candidate file, check that
(a) no `Real.sqrt`, `Real.rpow`, `Real.cos`, `Real.exp`, `Real.log`
appears in the proof body; (b) no `linarith` on $q > 1$; (c) no
`norm_num` on a CODATA value. If all three are clean, replace the
signature `(q : ℝ) (hq : 1 < q)` with `{R : Type*} [Field R] (q : R)
(hq : IsUnit q)` (or weaker, per the typeclass cheat-sheet at the
top of [CLAUDE.md §7c](../../CLAUDE.md)).

**A3 architecture sketch** (separate branch):

```
QOU/Realization/Core.lean        — abstract: Realization = (κ : Type) + adapters
QOU/Realization/Real.lean        — κ = ℝ, current archimedean adapter
QOU/Realization/Complex.lean     — κ = ℂ (PR #1127's q-zero-complex)
QOU/Realization/Padic.lean       — κ = ℂ_p, Hensel-conditional adapter
QOU/Realization/FinField.lean    — κ = 𝔽_q, char-p adapter
QOU/Realization/FormalSeries.lean — κ = R⟦h⟧, formal-series adapter
```

Each adapter provides `Has{Sqrt, Pow, Log, Exp}` instances and a
realization-specific convergence/well-definedness check.

## 9. Generalizing the paper similarly

The paper's narrative side already uses generic-$R$ language in some
places (e.g. `def:bar-involution`, [`hecke-mass-element`](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.md)).
Extending this requires:

1. **Notation register**: add a row to
   [`notation-collisions.md`](../../content/quantum-observable-universe/notation/notation-collisions.md)
   for $R$ vs $\kappa$ (realization field). The complement of CAL-2
   (substrate parameter) and the choice of realization should be
   independent in the notation.

2. **Discipline tightening**: §7c currently distinguishes "generic
   R" vs "ℝ specialization". A tighter discipline would distinguish
   "generic R" vs "realization κ" where κ is one of {ℝ, ℂ, ℂ_p, 𝔽_q, …}.
   The current PR is half-way there ($|q| > 1$ vs $q > 1$ in the
   notation update).

3. **Per-realization viability tables**: each substrate proposition
   should record which realizations it is well-defined in (Hoefsmit
   sqrt needs `HasSqrt`; q-series needs `Field R` for convergence
   diagnostics; etc.). Implementing this is a per-block audit task —
   queued as research-grade infrastructure.

## What this audit does *not* claim

- Does **not** rewrite any substrate file today.
- Does **not** assert that any non-ℝ realization is *physically*
  relevant (the QOU observables are ℝ-valued by hypothesis).
- Does **not** propose dropping the ℝ specialization — only
  decoupling it from the substrate.

The substrate ↔ realization decoupling is **infrastructure**: it
makes the framework's algebraic content portable to other realization
fields (e.g. for sister papers, p-adic / number-theoretic analogs,
or for the categorical lift of Im($q_0$) discussed in PR #1127's
companion audit).

## See also

- [`CLAUDE.md` §7c](../../CLAUDE.md) — Base ring convention
- [`docs/audits/2026-05-24-q-zero-reality-audit.md`](2026-05-24-q-zero-reality-audit.md) — sibling audit (q_0 reality)
- [`docs/audits/2026-05-24-q-beta-droppability-cohomology.md`](2026-05-24-q-beta-droppability-cohomology.md) — sibling audit (Q_β droppability)
- [`content/quantum-observable-universe/notation/notation-collisions.md`](../../content/quantum-observable-universe/notation/notation-collisions.md) — base-ring convention + new $\|q\| > 1$ note
- [`content/quantum-observable-universe/braids-and-knots/q-zero-complex-extension.md`](../../content/quantum-observable-universe/braids-and-knots/q-zero-complex-extension.md) — PR #1127's complex-q proposition
