# Where the missing half of strong binding sits: inter-nucleon bonds give half, the rest is per nucleon

**Date** 2026-11-27 · **Gap** G5 follow-up (after #9710) · **Epic** `qou-myts` · **Thread** "Find the missing half of strong binding"
**Lean** [`QOU/MassTheory/StrandEndMergeCeiling.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/StrandEndMergeCeiling.lean): generic field, no measured value (status in §5).
**Probe** [`computations/probes/strand_end_merge_ceiling/`](../../computations/probes/strand_end_merge_ceiling/): `strand_end_merge_ceiling_probe.py` (3/3 checks, mpmath 40 dps, convention D, proton pin, AME not read); `compare_ame.py` (comparison only, scope (a)).
**Scope** (a) for every number; (b) only where a Lean theorem is cited. Nothing is wired, fitted or adopted.

## 0. Result in one paragraph

PR #9710 found that the colour-valence bond count (T3, 1.5 bonds per nucleon) gives about half of the
AME binding. The question here was whether the other half is more bonds between nucleons. **It is
not.** The corpus's one cutoff-free, weight-free binding rule, the uniform long-word limit (3∞) of
PR #9659, saturates the reading-3 merge ceiling, and this note puts it in closed form at every `A`.
Under the ruled law `B = −E₀ ln r` it splits **exactly** into two parts (Lean `Y_three_pow_eq`):

* an **inter-nucleon** part `B_inter(A) = E₀·(A·ln(1+u+u²+u³) + ln(1−u) − ln(1−u^{3A+1}))`, `u = q₀⁻²`,
  which reaches **0.565** of AME for `A ≥ 16` (sd 0.036). That agrees with T3's 0.527 from a different
  count rule. Two routes, colour valence and full saturation, both put the inter-nucleon binding at
  about half;
* a **per-nucleon** part `A·s`, `s = 2.8787 MeV`. This is what each nucleon gains by relaxing from its
  free word `V³` to its own trivial block. The bond words allow it because they contain the
  intra-nucleon letters `V(3j)`. Rule (3∞) as #9659 defines it includes this part, and the total
  reaches **0.920** of AME (sd 0.059).

So the missing half is a **per-nucleon medium term**: the nucleon's internal state relaxing once it is
bonded. It is not a missing inter-nucleon bond. Whether that relaxation counts as binding is not
decided by the corpus. It is a ruling (§4). The light nuclei argue against taking it at face value:
with it, ²H over-binds ×4.1 and ³H ×1.9.

## 1. Closed form of rule (3∞) at every A

PR #9659 showed the uniform average over bond words of length `L` tends, as `L → ∞`, to
`r_∞ = y_(n)/tr(x)`, `y_(n) = [n+1]_q/[2]_q^n`, `n = 3A`, `x` the free word (one `V³` per nucleon). It
evaluated this at `A = 2, 3`. Two exact facts give it at every `A`:

| check | statement | result |
|---|---|---|
| K1 | `tr_{3A}(x) = t₁^A`, `t₁ = tr₃(V³)` (Schur–Weyl trace, `A = 1, 2, 3`) | dev 1e-40; `t₁ = 0.99856216383678726595` |
| K2 | `y_(n) = (1 − u^{n+1})/((1 − u)(1 + u)^n)`, `u = q⁻²` (Lean `qint_div_eq_Y`), `n = 1…240` | rel dev 3e-39 |
| K3 | closed form reproduces #9659's `−ln r_∞` at `A = 2, 3` (2.1571300, 3.8068536) | 2.15713003, 3.80685360 |

Hence

    −ln r_∞(A) = 3A·ln(1 + u) + A·ln t₁ + ln(1 − u) − ln(1 − u^{3A+1}).

The per-strand value is `ln(1 + q₀⁻²) = 0.59424`. Its classical value (`q = 1`) is `ln 2`, one merge per
strand. That is the reading-3 ceiling `n − ⌈log₂(n+1)⌉` merges of `ClassicalReading3MergeBound`
(`max_merges_eq`): about one join per strand **end** in the closure, against one per quark for T3.

## 2. The split (Lean `Y_three_pow_eq`, scope (b))

With `Y(n) = y_(n)` in the variable `u`, over any field, for `u ≠ ±1` and `u^{3A+1} ≠ 1`:

    Y(3)^A = Y(3A) · (1 + u + u² + u³)^A · (1 − u) / (1 − u^{3A+1}).

The per-strand factor `(1 + u)^{3A}` cancels **completely** between `A` free nucleons, each relaxed to
its own trivial block, and the nucleus. So under `B = −E₀ ln r`:

    B_(3∞)(A) = A·s + B_inter(A),   s = B_(3∞)(1) = E₀(3 ln(1+u) + ln t₁ + ln(1−u) − ln(1−u⁴)),
    B_inter(A) = E₀(A·ln(1 + u + u² + u³) + ln(1 − u) − ln(1 − u^{3A+1})).

Per nucleon in bulk: `B_inter/A → E₀ ln(1+u+u²+u³) = 4.6516 MeV`. The classical value is `E₀ ln 4`,
two merges per nucleon (`inter_factor_at_one`). The per-strand reading is spent **inside** each nucleon:
a nucleon's own three strands take two of the three merges per nucleon that the ceiling allows.

## 3. Comparison with AME (scope (a), comparison only)

The readings were fixed before this comparison: `Ra` is #9659's rule verbatim, `Rb` is its inter-nucleon
part, and `T3` is #9710's count. The comparison was run in the same session as the closed form, so it is
**not** pre-registered in the #9710 sense. No reading has a free parameter, and none was changed after
the comparison. AME2020, experimental entries, total binding. AME includes Coulomb repulsion and the
asymmetry term, which no strong reading models, so a correct strong-only reading should sit **above** 1.

| nuclide | AME B (MeV) | Ra = (3∞) | ratio | Rb = inter only | ratio | T3 ratio (#9710) |
|---|---|---|---|---|---|---|
| ²H | 2.2246 | 9.119 | 4.10 | 3.362 | 1.51 | 1.29 |
| ³H | 8.4818 | 16.093 | 1.90 | 7.457 | 0.88 | 1.01 |
| ³He | 7.7180 | 16.093 | 2.09 | 7.457 | 0.97 | 1.11 |
| ⁴He | 28.296 | 23.354 | 0.83 | 11.839 | 0.42 | 0.61 |
| ¹²C | 92.162 | 83.308 | 0.90 | 48.763 | 0.53 | 0.56 |
| ¹⁶O | 127.62 | 113.43 | 0.89 | 67.368 | 0.53 | 0.54 |
| ⁴⁰Ca | 342.05 | 294.16 | 0.86 | 179.01 | 0.52 | 0.50 |
| ⁵⁶Fe | 492.26 | 414.64 | 0.84 | 253.43 | 0.51 | 0.49 |
| ²⁰⁸Pb | 1636.4 | 1559.3 | 0.95 | 960.48 | 0.59 | 0.55 |

Over the 2484 experimental nuclides with `A ≥ 16`: **Ra 0.920 (sd 0.059), Rb 0.565 (sd 0.036), T3 0.527
(sd 0.035)**.

Readings, all scope (a):

1. **The inter-nucleon binding is about half, by two routes.** Rb (saturate the reading-3 ceiling, then
   remove each nucleon's own relaxation) and T3 (colour valence on the nucleon graph) come from different
   premises and land within 7 % of each other, both flat in `A`. Within this corpus, more bonds between
   nucleons do not close the gap. The ceiling allows at most about 2 merges per nucleon between
   nucleons at `q = 1`.
2. **The per-nucleon term is the size of the gap.** `s = 2.88 MeV` per nucleon brings the bulk from 0.565
   to 0.920. Because of Coulomb (§0 of the G3 audit), the strong-only shortfall of Ra is larger than 8 %.
   This note does not compute it.
3. **The light nuclei cut against Ra.** With the per-nucleon term the deuteron is ×4.1 and ³H ×1.9.
   Without it (Rb) they are ×1.5 and ×0.88, close to T3's pattern. A reading in which the relaxation turns
   on with nuclear size would need a derivation. None exists, and choosing one now would be selection
   against the target.
4. **A near-coincidence, not used.** `s/E₀ = 0.68097` and the ruled bond `−ln(z − h/2) = 0.67696` differ by
   0.6 %. No identity relates them. It is recorded so that no later agent "discovers" it as a fit.

## 4. What is not derived

1. **Whether intra-nucleon relaxation is binding.** The ruled law compares the bound word with the
   product of free nucleons `V³`. The bond-word population (#9659) contains the intra-nucleon letters, so
   rule (3∞) includes the relaxation. Nothing in the corpus says a free nucleon cannot relax on its own.
   At `A = 1` there are no bond words, so the rule is silent. That is the decision put to Carl.
2. **That the trivial block is the `q₀` maximum.** Classically it attains the proved ceiling. At `q₀`,
   every measured bond word lies below it: the largest word values recorded are 1.77 nats at `A = 2` (ceiling
   audit, 2.56 merge units) and 2.32 nats at `A = 3` (#9659, rule (1), `V1V4V2V5V5`), against 2.157 and
   3.807. It is not
   proved to be the maximum over all reading-3-admissible elements at `q₀`.
3. **Coulomb and asymmetry.** These belong to the sibling threads (G3 Coulomb, G2 `T(T+1)`).

## 5. Lean status

`StrandEndMergeCeiling.lean`: `Y`, `qint_div_eq_Y`, `Y_three_pow_eq`, `Y_mul_strand_factor`,
`inter_factor_at_one`. Generic `Field K`, no logarithm, no number. The logarithmic reading in §2 is
transcendental and is stated here, not in Lean. Verified 2026-11-27: `lean -DautoImplicit=false -s 65536` exit 0, sorry-free, `#print axioms` = `[propext, Classical.choice, Quot.sound]` on `qint_div_eq_Y`, `Y_three_pow_eq`, `Y_mul_strand_factor`.

## 6. For the sibling threads

* **Extensive binding (A = 4 sweep, #9618 line).** That thread's word-level `q₀` cap at `A = 4` (4
  merges at length ≤ 4) is about finite words. This note is about the `L → ∞` limit, which saturates.
  The two do not conflict.
* **Coulomb (G3), T(T+1) (G2).** These subtract from or reshape Ra and Rb. Neither changes the split.
* **Nucleus 3D word (T3).** Rb agreeing with T3 supports T3 as the inter-nucleon count. The open half
  is per nucleon, not more bonds.
