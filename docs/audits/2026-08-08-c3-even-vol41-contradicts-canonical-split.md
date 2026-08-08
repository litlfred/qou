# c₃^even = −Vol(4₁) is not derived — it contradicts the canonical κ·S split

**Date:** 2026-08-08 · **Bean:** `qou-qb8f` · **PR:** #4742
· **Tier:** structural-exact (the contradiction) + scope-(a) (the refutation)
· **Discipline:** no fit, no wiring, no tier change, no Lean edited.
Applies AGENTS.md §"Defined residual ≠ derived decomposition (STRICT, 2026-08-08)"
to the case that motivated it.

## The question

Raised — deliberately **not adjudicated** — in [#4724](https://github.com/litlfred/qou/pull/4724)
when an `S_leak`-based candidate filter was retracted. Flagged for the c₃ owners;
it turned out to be answerable from the corpus, so it is answered here.

[`SLeakZeroCrossing.lean:11`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakZeroCrossing.lean)
defines

```
S_leak(q₀) := c₃(q₀) + Vol(4₁)
```

and reads it as *"the bar-odd residual of c₃ after removing the bar-even
amphichiral `−Vol(4₁)` face"*. That reading requires

> **(H1)** `c₃^even = −Vol(4₁) ≈ −2.0299` — exactly.

Is (H1) derived?

## Why the split was not measured directly

`c₃^even(q) = (c₃(q) + c₃(1/q))/2` requires c₃ at `q ≈ 0.901`. Both substrate
anchors sit at `q ≈ 1.10998`; the bar-partner `1/q_proton ≈ 0.900918283956` is
not an anchor. **No anchor data determines the bar-split** — it must come from an
assumed structural form.

So (H1) was tested for *consistency* against the corpus's other, **derived**
decomposition instead. This is the general move the AGENTS.md guard prescribes:
when a split is not empirically accessible, say which structural form supplies it,
and check that form against what else is known.

## The canonical split

[`2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
§2 (tier: structural-exact) gives

```
c₃^odd = κ_(2,1)(q) · S,      κ_(2,1)(q) = (q−1)³(q+1)/q²
```

with `κ_(2,1)` the **derived** pure-q bar-odd carrier and `S = Q_β/E₀` the single
archimedean scalar — quoted there, independently of anything in the `S_leak`
framing, as `S_proton ≈ 908.4`, `S_muon ≈ 886.8`, `S_p/S_μ ≈ 1.024`.

`κ_(2,1)` is genuinely bar-odd; `κ(1/q) = −κ(q)` is verified symbolically in the
probe (four sample points, `< 1e-40`).

Because those `S` values come from a **different audit than the claim under
test**, they are a free, non-circular cross-check.

## The contradiction

Invert `c₃ = −κ_(2,1)(q)·S` at each anchor **under the hypothesis `c₃^even = 0`**
and compare to the audit's quoted `S`:

| anchor | `κ_(2,1)` | `S` reconstructed | audit's `S` | rel dev |
|---|---|---|---|---|
| proton | 0.002278102210 | **908.3624831** | 908.4 | **4.1e-5** |
| muon | 0.002278102967 | **886.7905751** | 886.8 | **1.1e-5** |

`S_p/S_μ = 1.02432582` against the quoted `1.024`.

Assuming c₃ is **purely bar-odd** reproduces both independently-quoted values to
~1e-5. The canonical decomposition therefore has

```
c₃^even ≈ 0            (canonical)
c₃^even = −2.0299      (H1)
```

a separation of **98.09% of |c₃| itself**. The two readings are **incompatible**,
not merely distinct. (H1) is not merely underived — it contradicts a
structural-exact result.

## What `S_leak` actually is

| anchor | c₃ | `+ Vol(4₁)` → `S_leak` | cancelled |
|---|---|---|---|
| proton | −2.06934258 | −0.039459367 | **98.093%** |
| muon | −2.02020024 | +0.0096829728 | **99.521%** |

Adding `+2.0299` to a number in `[−2.069, −2.020]` does not remove a bar-even
face — it **cancels ~98% of the bar-odd part**. `S_leak` is a near-total
cancellation residual.

This is also the mechanical origin of its hypersensitivity:

```
anchor swing of c₃      2.4325%
anchor swing of S_leak  507.51%
amplification           208.63×      ← cancellation artifact
```

c₃'s own 2.4% anchor swing across an 11.54 ppb interval is **real** — that is the
`dc₃/dq ≈ 4.6e6` obstruction, and it stands. The extra ~209× on top of it is
arithmetic, not structure. Any argument that reads `S_leak`'s *relative* swing as
a measure of structural sensitivity is reading the cancellation, not the physics.

## Scope

**Scope-(a).** What is refuted is the **identification** (H1). Not refuted:

* `Vol(4₁)` as an ingredient anywhere else in the corpus;
* the amphichirality of `4₁`, or its bar-even character;
* **any theorem** in `SLeakZeroCrossing.lean`,
  `SLeakMagnitudeOffsetRatio.lean`, or `SLeakMagnitudeTaylorRatio.lean`. Every
  one is stated for a *generic* function with the anchor signs (or a simple zero)
  as **hypotheses** — `sleak_zero_between_anchors`,
  `sign_definite_carrier_excluded`, `linear_ratio_slope_independent`,
  `exact_ratio_factorization`, … — and each stands exactly as written.

What *is* affected is the interpretive sentence naming `S_leak` "c₃'s bar-odd
residual", and any downstream reasoning that treats the `−Vol(4₁)` face as
established.

**No Lean was edited here.** The theorems are correct; the docstring correction
belongs to the owners of those files, who have been notified on
[#4734](https://github.com/litlfred/qou/pull/4734).

## Two corrections to the bean that raised this

`qou-qb8f` claimed "two inequivalent **splits**", citing `c₃^even ≈ +86.66` from
the 2026-07-07 audit as the rival value. That was imprecise twice over, and the
audit says so itself:

1. **`+86.66` is a projection artifact.** The audit calls the mixed-projection
   rung exactly that — *"the honest rungs are the `e_k`"* (`e₁ = 3√3/4`,
   `e₂ ≈ −15.035`, …, persisting through `s¹⁷` with over-determination margin 9,
   every residual order exactly zero).
2. **It is a different object.** `+86.66` is the k=3 rung **of the bar-even
   channel of `log R`**; (H1) is about the bar-even **part of** the c₃ Taylor
   coefficient. Same glyph `c₃^even`, two referents — precisely the
   overloaded-symbol trap flagged in AGENTS.md §"Conditional-proved ≠
   premise-established" rule 4.

So the sharp statement is **not** "two rival values for one object" but
"(H1) contradicts the derived `κ_(2,1)·S` split". Recorded so the imprecise
framing does not propagate.

## Reproduce

```bash
python3 -u computations/qbeta/c3_even_canonical_split_contradiction.py
```

7/7 assertions, ~1 s. Inputs are corpus-committed anchor values plus exact
evaluations of `κ_(2,1)`; no fit, no witness emitted (`auditOnly`).

## What stays open

* **`qou-qb8e`** — the c₃ **magnitude** channel: the actual open gate.
* **The bar-even part of c₃ is now unclaimed.** If `c₃^even ≈ 0` is right, that
  is itself a structural statement worth stating and proving rather than
  inferring from a 1e-5 cross-check at two anchors.
* Whether the registry's c₃ row should carry a pointer either way (bean question
  (c), unanswered here — it is the registry maintainers' call).

-- Ref: [manuscript] `docs/audits/2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`
-- Ref: [manuscript] `docs/audits/2026-07-03-9fnm-c3even-exact-rational-measurement.md`
-- Ref: [manuscript] `docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`
