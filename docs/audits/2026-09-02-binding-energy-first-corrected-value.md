# The first `binding_energy` value the corrected framework has ever produced

**Measured 2026-09-02.** Completes the `qou-sv7h` arc: the Rust LP-accumulator
kernel is wired into both loops, and `binding_energy` runs end to end for the
first time.

## The result

```
atom        Z   N       B_pred (MeV)      secs
deuterium   1   1       -7.271102125      942.3
```

against AME2020 (`ame_binding_mev(Z, A)`, signature confirmed empirically
against three known values — deuteron 2.224566, triton 8.481796, ⁴He 28.295662):

| | value |
|---|---|
| **predicted** `B(²H)` | **−7.271102125 MeV** |
| **AME2020** `B(²H)` | **+2.224566 MeV** |
| sign | **WRONG** |
| \|ratio\| | 3.27× |

Term decomposition, same run: `unified_iterative_correction = −9.1477362310`,
`sdp_cross_channel_contribution = 0.0`, so `binding_from_frobenius_pairing =
+1.8766`. The negative sign is carried by term 1.

## The sign was already negative before the correction

Important, and it constrains what the correction can be blamed for. The
accumulator was negative on the **old** (braid-violating) matrices too —
measured `−0.0319` (k=4) through `−2.1955` (k=8) — and is negative on the
corrected family — `−0.0896` through `−2.0200`. **The correction changed the
magnitude by 71–221 %; it did not introduce the sign.**

So this is not "the fix broke the physics". It is: the framework's binding
accumulator has produced a wrong-signed result all along, and until now nobody
could see it, because the function could not complete.

## What is established

- `binding_energy` **runs**, for the first time, in 942 s for A = 2.
- Its deuteron value has the **wrong sign** against AME2020 and is 3.27× the
  magnitude.
- Both checked-in gates pass on this tree:
  `lp_accumulator_kernel_gate.py` → **7.092e-48**, exit 0.

## What is NOT established

- **One atom.** A = 3 was still running at 28 min when this was written (cost
  grows as A²). A single point is not a pattern, and the sign could plausibly
  differ across the light isotopes. Do not generalise from deuterium.
- **No witness regenerated.** `hadron-knot-table.witness.json` is untouched.
- **Nothing about *why* the sign is wrong.** That is a physics question this
  measurement opens and does not answer.

## `ysn_braid_relation_audit.py` still exits 1 — that is CORRECT

`_build_ysn_matrices` is deliberately **unchanged**. The kernel bypasses it by
building the correct family in Rust; it does not repair the Python one. So the
braid audit continues to flag a real defect in a function that is **no longer on
the binding path**. Do not read its exit 1 as the wiring having failed, and do
not "fix" it by weakening the audit — other callers
(`sdp_cross_channel.py`) still use that builder and are still affected.

## What changed in the code

`unified_iterative_correction`: each partition's whole trajectory is precomputed
in Rust before Pass 1, and the step loop reads `(trace, log_norm)` from it.
**Every line of the accumulation — `raw_delta`, `cumul_partition`,
`final_tr_sign` — and the whole of Pass 2's complementary-slackness gate are
untouched.** That distinction is the point: a reimplementation that drops Pass 2
is wrong by ~4.6× (measured), which is why the kernel is wired *in* rather than
*around*.

`atom_character_raw`: same kernel, taking the final step's trace and log-norm,
which is all that function returns.

Both fall back to the original Python path when `pyhecke_native` is absent — a
bare container has no extension module, and this module must still import there.

---

# Second atom: the wrong sign is SYSTEMATIC, and the magnitude is nearly flat in A

| atom | A | B_pred (MeV) | AME2020 (MeV) | sign | \|pred\|/AME | secs |
|---|---|---|---|---|---|---|
| deuterium | 2 | -7.271102125 | +2.224566 | **WRONG** | 3.269 | 942.3 |
| tritium | 3 | -7.742121347 | +8.481796 | **WRONG** | 0.913 | 1567.6 |

**Both wrong-signed.** Two points is not many, but it is enough to say the sign
is not an A = 2 peculiarity.

**The more informative number is the shape, not the sign.** From A = 2 to A = 3
the prediction moves `-7.271 → -7.742` — **6.5 %** — while the experimental
binding moves `2.225 → 8.482`, **+281 %**. The accumulator is close to
**A-independent** over this range, where real binding grows steeply and roughly
linearly in A.

So the defect is unlikely to be a stray sign convention: flipping the sign would
give `+7.27` and `+7.74` against `2.22` and `8.48`, which is wrong in the
opposite direction at A = 2 and still nearly flat. **Whatever is missing is
extensive in A**, and a sign flip does not supply it.

That is consistent with the standing open problem recorded in AGENTS.md — the
"separate, super-pairwise additive extensive object" that the six Δ_λ closure
ansätze all failed to produce, and the pairwise cap
`QOU.MassTheory.exchangeDet_pow_two_le_four`. This measurement does not solve
that; it is the first time the framework's own binding path has been able to
*exhibit* it end to end.

## Still not established

- **Two atoms.** he3, he4, li6, li7 did not complete: the container's worker was
  restarted mid-run (SIGKILL) and the process died. They are not reported.
- **No witness regenerated.** `hadron-knot-table.witness.json` untouched, and it
  should stay that way while the sign is wrong — recording these as a witness
  would publish them.
- **No cause identified.** "Extensive term missing" is a reading of two points,
  consistent with prior work; it is not a measurement of the mechanism.

# Copilot review (#6427) — finding accepted, fix relocated

Copilot flagged, correctly, that the kernel path makes `tr_run` and
`s['log_norm']` `mpmath.mpf`, so `unified_iterative_correction` and
`binding_energy` return `mpf`, and `hadron_knot_table.py:204`'s
`round(B, 4)` then hits
`TypeError: Object of type mpf is not JSON serializable`. **Verified by
reproduction**, not taken on trust.

**Its suggested fix — coerce at the kernel boundary — is wrong for this repo**,
and the fix is applied one level out instead: the casts are at the *public
returns* of `unified_iterative_correction` and `binding_energy`, which is where
the float contract has always been. Coercing at the kernel would discard the
50-dps the kernel exists to carry, through the entire accumulation, which is
exactly what the NO-FLOAT64 discipline forbids.

**And it costs nothing measurable either way**, which is worth stating because
it identifies a real defect Copilot did not flag: `log_cur = s['log_norm'] +
math.log(abs(tr_run))` at line 1604 **already narrows to float64 inside the
loop** — `math.log` returns a Python float whatever it is handed. Measured:
`math.log(mpf(3)/7)` → `-0.8472978603872037` (float) against `mp.log` →
`-0.847297860387203613710107506521`. So this accumulator has been
float64-limited at its log step all along, upstream of any cast. That is a
**pre-existing precision defect**, neither introduced nor repaired here.

---

# Third atom: the prediction is very nearly a CONSTANT

| atom | A | Z | B_pred (MeV) | AME2020 | sign | \|pred\|/AME | secs |
|---|---|---|---|---|---|---|---|
| deuterium | 2 | 1 | -7.271102125 | +2.224566 | **WRONG** | 3.269 | 942 |
| tritium | 3 | 1 | -7.742121347 | +8.481796 | **WRONG** | 0.913 | 1568 |
| he3 | 3 | 2 | -7.456199506 | +7.718041 | **WRONG** | 0.966 | 1496 |

**This is the finding, and it is sharper than the sign.**

```
prediction spread :  -7.742 .. -7.271   =   6.3 % of its mean
AME2020    spread :  +2.225 .. +8.482   = 101.9 % of its mean
```

Across A = 2 → 3, and across two *different* A = 3 nuclei, the framework's
binding accumulator moves **6 %** while the experimental binding it is meant to
reproduce moves **102 %**. The output is essentially **a constant ≈ −7.5 MeV**,
almost independent of both A and Z.

That reframes the defect. A wrong sign suggests a convention; a wrong *magnitude*
suggests a missing coefficient. **A near-constant where the target varies by 4×
suggests the accumulator is not computing a binding energy at all** — it is
producing something whose nuclear dependence is almost entirely absent.

## The mirror pair, stated carefully

⁴³H (tritium, Z = 1) and ³He (Z = 2) are mirror nuclei, and the comparison is
worth making precisely rather than loosely:

```
raw differences (tritium − he3):   prediction  -0.2859      AME  +0.7638
```

Those have **opposite signs as raw differences** — I initially mislabelled them
as agreeing, and that was wrong. The defensible statement is about **ordering
under the global sign flip**: `|pred(tritium)| > |pred(he3)|` and
`B(tritium) > B(he3)`, so the framework does rank the mirror pair the way
experiment does, at **0.37×** the experimental splitting.

That is a genuine but weak positive: some Z-dependence exists and points the
right way. It does not survive as evidence for the sign being a mere convention,
because the near-constancy above is not something a sign flip repairs.

## Consistency with the standing open problem

AGENTS.md records the arc's one real open problem as a **"separate,
super-pairwise additive extensive object"** that six Δ_λ closure ansätze all
failed to produce, with the pairwise cap proved
(`QOU.MassTheory.exchangeDet_pow_two_le_four`). A binding accumulator that is
**flat in A** is exactly what that description predicts you would see if the
extensive term is absent — the intensive part is present and the extensive part
is not.

**This measurement does not prove that reading.** Three points, two of them at
the same A. It is consistent with the standing account, which is a different and
much weaker claim than confirming it.

## Still running / still not established

- **he4 (A = 4) is the real test** and was still running when this was written.
  AME `B(⁴He) = 28.296` — more than 3× the A = 3 values — so if the prediction
  stays near −7.5 there, flatness is established across a 13× range of the
  target. li6/li7 after that.
- **No witness regenerated.** `hadron-knot-table.witness.json` untouched.
- **No mechanism identified.** Flatness is a symptom; where the A-dependence is
  lost in the accumulator is not measured.
