# (P) and (F) are one statement — and the corpus already has the q=1 case

**Date:** 2026-08-27
**Bean:** `qou-dsif`
**Evidence:** [`computations/y_lambda_pieri_step_probe.py`](../../computations/y_lambda_pieri_step_probe.py), facts 4–8, exact sympy, eleven shapes up to `(4,3,1,1)`

## Summary

Two findings, one of them a correction to framing this repo has been carrying
since [PR #5857](https://github.com/litlfred/qou/pull/5857).

1. **(P) and (F) are not independent.** (F), the SYT branching rule, is the
   `q → 1` shadow of (P), the Pieri step. The general-`n` Macdonald hook
   telescope therefore rests on **one** q-deformed identity, not two.
2. **The `q = 1` case is already machine-checked in this corpus**, and a
   parallel q-hook development already exists that the recent Pieri work did
   not know about.

## 1 — The correction

[PR #5857](https://github.com/litlfred/qou/pull/5857) §4 stated, and
[#5871](https://github.com/litlfred/qou/pull/5871) repeated, that the telescope
follows by induction from **two elementary statements**:

- **(P)** `Σ_{μ = λ+box} s_μ(Q,X) = ((1−X)/(1−Q))·s_λ(Q,X)`
- **(F)** `f_λ = Σ_{ν = λ−box} f_ν`

That framing is wrong in the direction of over-counting the work. Reducing (P)
to one variable (facts 4–7) and then letting `Q → 1` lands exactly on (F).

**The derivation**, which uses only the hook-length update rule already proved
in Lean:

Each factor `(1 − Q^h)/(1 − Q^{h+1}) → h/(h+1)`, so the reduced form of (P) —

```
Σ_r  Q^r · ∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})  =  1
```

— degenerates to `Σ_r ∏_{h ∈ arm ∪ leg(r)} h/(h+1) = 1`.

The update rule (`hookLength_addBoxRow_of_ne_corner` plus the new box's hook
being `1`) says hooks rise by one on `arm ∪ leg` and nowhere else, so

```
∏_{c ∈ μ} h_μ(c)  =  ∏_{c ∈ λ} h_λ(c) · ∏_{h ∈ arm ∪ leg} (h+1)/h.
```

Frame–Robinson–Thrall (`f_ν · ∏hooks(ν) = |ν|!`) then gives

```
f_μ / f_λ  =  (n+1) · ∏_{h ∈ arm ∪ leg} h/(h+1)
```

so `Σ_r ∏ h/(h+1) = 1` **iff** `Σ_{μ = λ+□} f_μ = (n+1)·f_λ` — which is (F).

**Verified independently**, not merely rearranged: the probe computes the `q=1`
sum and the branching rule by separate routes and checks both on eleven shapes.

## 2 — What the corpus already has, and did not get used

The corpus-grep that should have preceded the Pieri work turns up two things the
`List ℕ` tower in `QPartitionCombinatorics` / `WenzlSchurElement` /
`MacdonaldTelescope` did not use:

| declaration | file | status |
|---|---|---|
| `numStandardYoungTableaux_mul_hookLengthProduct` | `QOU/Mathlib/HookLengthFormula.lean:171` | FRT, **sorry-free** |
| `qHookLengthProduct` + `qHookLengthProduct_one` + `qFactorial_one` + `qHookLengthProduct_one_mul_num` | `QOU/Mathlib/QHookProduct.lean` | **sorry-free**, whole file |

`QHookProduct.lean` is a q-hook product on **Mathlib's `YoungDiagram`**, with
the `q = 1` specialisation to FRT already proved. The Pieri tower is a
**parallel development on a bare `List ℕ`** with its own `hookLength`.

That is a duplication, and it is tracked: bean `sp09` (completed) sizes the
bridge as two pieces — per-cell hook agreement (**~40 lines, tractable**) and
an SYT-count bridge between two encodings (**~120–150 lines, moderate**).

**This audit does not recommend doing that bridge now.** It records that the two
developments exist and that the choice between them should be deliberate rather
than accidental. What it does recommend: any further Pieri work check
`QOU/Mathlib/` first.

## 3 — What this means for the open problem

The remaining open item is a **single** q-identity:

```
Σ_r  Q^r · ∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})  =  1
```

- Its `q = 1` case is reachable from corpus material (FRT, sorry-free) plus the
  update rule already proved. **Only the q-deformation is genuinely open.**
- (P2) follows by conjugation (fact 7); (P) follows from the two by
  X-linearity (fact 4). So this one identity carries everything.
- Bean `sp09` records that (F) itself was believed to need Greene–Nijenhuis–Wilf
  or Novelli–Pak–Stoyanovskii. Since (F) is this identity at `q = 1`, the
  q-deformation is at least that hard, and plausibly harder.

## 4 — A route ruled out, and one hazard

**Ruled out (scope (a)):** partial sums in row order do not telescope. Measured
on four shapes; every proper tail is an unstructured rational function. The
cancellation is global across corners. Not a proved exclusion of all recursive
structures — no invariant was sought.

**Hazard for whoever attacks the cyclotomic route:** poles and zeros must be
counted **per root of unity**, not per exponent. At `λ = (4,2,1), r = 0` the
surviving pole exponents are `{3,5,7}` and the zeros `{1,4,6}` — the `(1−Q³)`
pole is cancelled by the `(1−Q⁶)` zero, because both vanish at a primitive cube
root of unity. Exponent-matching would report a spurious pole.
