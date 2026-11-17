---
# qou-oots
title: 'Phi_k weight family is unjustified: dim_q^2 misuses a quantum dimension where f^lambda*dim_q (Molien, Lean-proved exactly normalized) or y_lambda (Markov, canonical Frobenius pairing) may belong'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T05:55:40Z
updated_at: 2026-11-17T06:36:38Z
pr: 8228
parent: qou-3l2l
---

## 2026-09-05 — requirement derivation + prune + discriminator (in-progress; the CHOICE is open, the PRUNE is not)

DELIVERABLE: docs/audits/2026-09-05-phi-k-weight-family.md
LEAN: QOU/BraidKnot/DepthStratifiedWeightRequirements.lean (lean-direct exit 0,
      0 sorry, #print axioms clean on all 6 decls)
PROBE: computations/probes/phi_k_weight_family_discriminator.py + witness

THREE REQUIREMENTS DERIVED (Lean, generic over abstract w/m/c, no anchor):
  R3 phiDiff_eq_sum_log_ratio -- the d_q INSIDE the log CANCELS in the
     observable difference (same index set, same weights on free and atom), so
     B = SUM_k a_k SUM_l w_l log|chi_free/chi_atom| is a weighted GEOMETRIC MEAN
     of character ratios. NOT linear in the braid element => Phi is NOT a trace
     => no Markov property is required of w. Consequences BOTH ways: y_lambda's
     only claim to privilege here evaporates, AND
     q_plancherel_vs_y_lambda_probe's "regular-trace family gives z=0, restrict
     to Markov traces" exclusion MUST NOT be imported -- it is scoped to the
     interface bond scalar z = tr(sigma_1), a linear trace evaluation Phi never
     performs. Importing it would be an arity/scope error.
  R1 phi_eq_zero_of_weights_vanish -- w vanishing on the stratum makes Phi_k
     identically 0. y_lambda's SU(N) row cap ([N+c]_q = [0]_q = 0 at the cell of
     content -N; RowCapObstruction.lean) makes y = 0 on EVERY stratum of depth
     >= N. Verified symbolically: N=2 (n=3,4,5,6) and N=3 (n=4,6). Depth 3 is
     killed at BOTH the mass (N=2) and colour (N=3) readings.
     => SCOPE-(b) exclusion of y_lambda. Measured: all three candidate knots
     reproduce the no-FR baseline to the last digit (5.3561249).
  R2 crossRatio_smul -- w -> k_n w multiplies the cross-nucleus metric by
     k_1/k_2; n = 3A differs, so the normaliser must be n-INDEPENDENT. NOTE this
     is WEAKER than "probability measure" -- any n-independent constant does.
     SUM d_q^2/[n]_q! = 0.9946/0.9874/0.9822/0.9822/0.9911 at n=2..6 and
     0.99108/1.11092/1.51713 at the nuclear n=6/9/12 => SCOPE-(b) exclusion of
     d_q^2/[n]_q! for cross-nucleus use (it stays valid same-n, by
     WLambdaNormalizationInvariance.ratio_invariant).
  NOT a requirement: conjugation symmetry. d_q^2 families are symmetric, Molien
  is asymmetric (q^{-kappa}, kappa = n(l')-n(l)) -- but the DEPTH stratification
  already separates l from l', so a symmetric w is not incompatible with a
  chirality channel. Recorded as a property, not derived as a requirement.

TWO SURVIVE: d_q^2/D^2 and the Molien family. THE CHOICE IS OPEN.

NEW IDENTIFICATION (exact in Q(q), every partition, n=2,3,4,5): the corpus's
Lean-proved MOLIEN family f^l q^{-kappa_l} d_q(l)/[n]_q! IS the literature's
q-Plancherel measure M_{n,Q}(l) = Q^{b(l)} dim l / prod{h}_Q
(Feray-Meliot, arxiv-1001.2180v2) under the corpus's own Q = q^2 bridge. One
line of hook arithmetic: prod[h]_q = q^{-(n(l)+n(l'))} prod{h}_Q and
kappa_l = SUM contents = n(l')-n(l). So the corpus HOLDS the literature's
q-Plancherel measure under a different name (molienSum) while calling
d_q^2/[n]_q! "q-Plancherel" -- and it is the FORMER that is exactly normalised.

THE DISCRIMINATOR FLIPPED, AND NOT THE WAY I EXPECTED. The k=3 ranking is NOT
weight-family-invariant. Three scoreable families, three different orderings,
three different winners:
  d_q^2/[n]_q!  no-FR 1.562126  4_1 1.5014667  5_2 1.5394226  6_1 1.6040329  best 4_1
  d_q^2/D^2     no-FR 1.0659881 4_1 1.2425297  5_2 1.2911323  6_1 1.0478474  best 6_1
  molien        no-FR 1.5488755 4_1 1.2308566  5_2 1.2168828  6_1 1.6067832  best 5_2
  y_lambda      5.3561249 for ALL FOUR rows (vacuous, R1)
Under MOLIEN -- the family with the best structural credentials -- the paper's
named 6_1 is the WORST of the three and the ONLY one that makes its own baseline
worse (-3.74%), while 4_1 and 5_2 are near-tied at +20.5%/+21.4%, a far LARGER
FR effect than any family has reported. Robust Molien statement: "{4_1,5_2}
close ~21%, 6_1 opens it" -- the 1.1% between 4_1 and 5_2 is not resolved by
this metric.
HARNESS VALIDATED: under d_q^2/D^2 the companion reproduces the committed
fr-pullback-k3-test witness on all 4 rows to <= 3.1e-16.

TWO DEFECTS FOUND, one mine:
  1. MINE. Hand-typed B_AME["T"] = 8.481798 vs the corpus constant 8.4817962 --
     a uniform 2.12219e-7 disagreement on 3 of 4 rows. Visible only because of
     the cross-validation, diagnosable only because the 4th row (6_1) agreed to
     3e-16 (T is the argmin for the other three, not for 6_1). Same class as the
     self-comparing AME literal fr_pullback_k3_test already caveats.
  2. UPSTREAM, flagged not fixed. fr_pullback_k3_test takes q0 from
     qou_substrate.constants.Q, which is a Python FLOAT; Q_50_DIGIT_STR exists.
     Measured 2.725e-17 relative. Immaterial here (15 orders under the effect)
     and NOT fixed -- changing a producer's anchor moves its published numbers
     and would break the controlled comparison. This probe uses the string.

STILL OPEN (why the bean stays in-progress): which of d_q^2/D^2 and Molien is
correct. My judgement, marked as judgement in the audit: MOLIEN, on exact
normalisation-by-theorem vs by-construction, the correct one-factor q-lift of
Burnside, an independently-named normaliser, and the q-Plancherel
identification. But NONE of that is derived FROM Phi_k, so adopting it would
substitute a good argument for a derivation. What would close it, in order:
  (a) name which object the nucleus is a state in -- V^{tensor n} gives the
      Molien shape f^l d_q(l)/[n]_q!, End(V^{tensor n}) gives d_q^2/D^2. This is
      structural, not numerical, and it is the whole content.
  (b) a same-n within-stratum observable (normalisation-invariant by
      ratio_invariant, but the PROFILE is not -- the two survivors put
      S_3 = 0.349/0.392/0.137 (Molien) vs 0.249/0.469/0.329 (d_q^2/D^2) on the
      depth-3 stratum at D/T/4He).
  (c) more than four nuclei; max/min over n in {6,9,9,12} cannot resolve 1.1%.
PRACTICAL OUTPUT: no k=3 knot conclusion should be quoted without naming the
weight family it was computed under.

## 2026-09-05 (second session, parallel) — ROUTE 1 of §7, measured: the `V^{⊗n}` share is a THIRD measure, and at `dim V = 2` it is NULL on depth 3

**Probe:** `computations/probes/schur_weyl_share_is_a_third_measure_probe.py`, 6/6, exit 0, mpmath 50 dps, zero builtin-float coercions, no witness. Reached independently of the requirements/discriminator work — this is §7 route 1, which that pass did not attempt.

### F1 — §2's identification is CONFIRMED, independently

The Molien family sums to **exactly 1** at n = 2..7 (check A), and the change of variables closes analytically: with `[k]_Q = (Q^k−1)/(Q−1) = q^{k−1}[k]_q` at `Q = q²`, `Σ_cells h = n(λ)+n(λ′)+n` and `κ_λ = n(λ′)−n(λ)`,

    M_{n,Q}(λ) = Q^{b(λ)} f^λ / Π[h]_Q = f^λ q^{−κ_λ} / Π[h]_q

which is the Molien family. So **Molien = Féray–Méliot q-Plancherel** stands on two independent legs now.

### F2 — but the Molien family is NOT the `V^{⊗n}` share

§7 says *"if that object is `V^{⊗n}` … the share is `f^λ d_q(λ)/[n]_q!`-shaped (Molien) and the question is closed."* **"Shaped" is right; "is Molien" is wrong.** Two different measures, each normalised on its own index set (checks A and B both return exactly 1), so neither is a mis-normalisation of the other:

| | weight | index set | normaliser |
|---|---|---|---|
| **`V^{⊗n}` share** | `f^λ · d_q^{SU(N)}(λ)`, `d_q^{SU(N)} = Π[N+c]_q/[h]_q` | λ with **≤ N rows** | `[N]_q^n` |
| **Molien** | `f^λ · q^{−κ_λ} · d_q^{hook}(λ)`, `d_q^{hook} = [n]_q!/Π[h]_q` | **all** λ | `[n]_q!` |

Pairwise max per-λ deviation at N=3, n=6: share↔Molien **0.2716**, share↔Plancherel **0.2206**, Molien↔Plancherel **0.0623** (check E). Three distinct measures.

### F3 — the one that bites: at N = 2 the module share is EXACTLY zero on depth ≥ 3

Mass on partitions with ≥ 3 rows (check C):

| | n=3 | n=6 | n=9 |
|---|---|---|---|
| `V^{⊗n}` share, **N=2** | **0.0** | **0.0** | **0.0** |
| `V^{⊗n}` share, N=3 | 0.035464334084 | 0.306778844906 | 0.602339318062 |
| Molien (all λ) | 0.223435033655 | 0.902265160825 | 0.997608919308 |

because `[N+c]_q = [0]_q = 0` at the cell of content `−N`. The corpus asserts the state space is `V^{⊗3A}` with **`dim V = 2`** (`content/…/nuclear-interactions/per-nucleon-channel-decomposition.md:13` for `V^{⊗3A}`; `computations/state_space_natural_three_sym2_gate.py:8-17` for `dim V = 2` "by the Descartes condition"). Under that reading the module-share measure **vanishes identically on the depth-3 stratum, so Φ₃ ≡ 0 by this bean's own R1** (`phi_eq_zero_of_weights_vanish`).

**So route 1 at N = 2 does not select between the survivors — it excludes the module-share reading for Φ₃**, by exactly the row-cap invariant R1 uses to retire `y_λ`. The route survives only at **N ≥ 3**.

### F4 — the second horn is mis-specified, and the missing candidate is classical Plancherel

`End(V^{⊗n})` is not a rival state space: under q-Schur–Weyl `H_n(q) ≅ End_{U_q sl_N}(V^{⊗n})` (Jimbo) it is the **operator algebra of the same pair**, which the corpus states in Lean (`QOU/MassEndomorphism/MassLeftMulEndomorphism.lean`, `QSchurWeyl.lean:11`). Its block share is `dim M_{f^λ}/dim H_n(q) = (f^λ)²/n!` — **classical Plancherel, the candidate §7 does not list**. It sums to 1 by Burnside at every n (check D) and is **q-independent**, which is its own objection for a substrate observable but is not the row-cap one.

And **Féray–Méliot §6.1 states this pairing outright**, in the paper §2 already cites — `library/arxiv-1001.2180v2/sections/sec-026-61-decomposition-of-tensor-representations.md`: the module gives the *Schur-Weyl measure* `f^λ·dim U_λ/N^n`, *"the same construction with the regular representation gives rise to the Plancherel measure"*, and *"the Schur-Weyl measure charges only the Young diagrams whose lengths are smaller than N"* — F3, in the literature's own words. The term **"Schur-Weyl measure" appears nowhere outside `library/`** (0 hits in `content/`, `docs/`, `computations/`, `.beans/`).

### What route 1 now turns on

**Only `N`.** Not which of two families — which `N` the nucleus is a state at. At N=2 the module reading is excluded for Φ₃; at N=3 it is live and gives a measure that is neither survivor. Note `content/…/mass-theory/schur-weyl-mass-decomposition.md:19` records the corpus keeping λ with rows beyond 3, and the atom's strand count is itself disputed in-corpus (`H_{A+Z}` in `atomic-braid.md:2` vs `H_{3A}` in `schur-weyl-mass-decomposition.md:1` and `hecke/hecke_3a_weights.py:5`), with no block reconciling them.

### Not established

Which family Φ_k should use. Route 1 is **narrowed and partly excluded, not completed**. `d_q²/D²` is the share of neither object here — it is the RT/Verlinde weight of the `S²×S¹` Hilbert space, a third carrier again.

## 2026-09-05 (later) — SETTLED: `N = 2`. And my own "route 1 turns on which N" is RETRACTED.

**Probe:** `computations/probes/which_n_the_nucleus_is_a_state_at_probe.py`, 9/9, exit 0, mpmath 50 dps, zero builtin-float coercions, no witness.
**Audit:** `docs/audits/2026-09-05-which-n-the-nucleus-is-a-state-at.md`.

### The answer: `N = 2` — and it was already recorded, four ways

Not derived here; it follows from the **convention-D owner ruling of 2026-08-15**.

1. `wedderburn_jones_markov.py:177` — `_y_su_n(n, mp.mpf(str(q_val)), 2)`. The third argument **is** `N`.
2. `wedderburn_jones_markov.py:129-133` — *"D's weights are the **SU(2) quantum dimensions** … The defining difference is the row cap: `y_λ = 0` for `ℓ(λ) > 2`"*.
3. `wedderburn_jones_markov.py:386-391` — the vanishing blocks *"span `ker(H_n ↠ TL_n)`, of dimension `n! − Catalan(n)` (1, 10, 78, 588, 4611, 38890 at n = 3..8)"*, citing sorry-free `QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`.
4. **`docs/audits/2026-09-05-phi-k-weight-family.md:105` — *"Production is `N = 2` (convention D)"*.** Stated outright, in the very audit whose §7 I was answering.

### The chain, verified independently (check A)

`Σ_{ℓ(λ)≤2} (f^λ)² = Catalan(n) = dim TL_n`, and `n! − C_n` reproduces **all six** of the corpus's kernel dimensions exactly (5/5/6/1, 14/14/24/10, 42/42/120/78, 132/132/720/588, 429/429/5040/4611, 1430/1430/40320/38890). So:

    H_n(q) ↠ TL_n(q) ≅ End_{U_q sl_2}(V^{⊗n})

and convention D zeroes `y_λ` **precisely on the kernel**. The canonical trace does not merely tolerate `N = 2` — it is **defined on the `N = 2` quotient**. Horn 1 of §7 is the corpus's actual position, structurally rather than in prose; horn 2 is not a rival, because `TL_n` **is** that endomorphism algebra.

### 🛑 RETRACTION — two errors, both mine, both merged in #6768

**(a) Depth is off by one.** The Φ_k audit defines *"Depth `k` means `k+1` rows"* (line 104). So depth 3 is **exactly 4 rows**, and "≥ 3 rows" — what my probe measured — is **depth ≥ 2**. The numbers were right; the stratum name was not.

**(b) The conclusion drawn from it is false.** On the real depth-3 stratum (exactly 4 rows), `N = 3` gives **0.0** too:

| n | #λ depth 3 | N=2 | N=3 | N=4 | Molien | Plancherel |
|---|---|---|---|---|---|---|
| 4 | 1 | **0.0** | **0.0** | 0.003505637 | 0.074351 | 0.04166667 |
| 6 | 2 | **0.0** | **0.0** | 0.03376524 | 0.348728 | 0.2513889 |
| 9 | 6 | **0.0** | **0.0** | 0.1496872 | 0.3916401 | 0.4614446 |

Both caps sit below 4 rows. The first `N` that does not is **4**, which nothing in the corpus proposes. At `n = 3` (proton, A=1) the stratum is **empty** — no 4-row partition of 3 — so Φ₃ has no index set there at all, for any `N` and any family.

**And the Φ_k audit had already said this**, lines 107-108: *"at `N = 3` the cap still lands on depth ≥ 3, so **`k = 3` is vacuous under `y_λ` at both the mass (`N = 2`) and colour (`N = 3`) readings**."* I quoted the paragraph immediately above that sentence and did not carry the sentence itself.

### What route 1 DOES establish — a constraint that eliminates every current candidate

Any family consistent with the canonical trace must **vanish on `ker(H_n ↠ TL_n)`**, i.e. on every λ with ≥ 3 rows. Measured, **both survivors fail it**: Molien carries 0.223 / 0.902 / 0.998 there at n = 3/6/9; unrestricted classical Plancherel is nonzero at every depth-3 row above; `d_q²/D²` fails unless `D²` is restricted to ≤ 2 rows.

So the honest statement is **stronger** than "open": *no candidate on the table satisfies the corpus's own consistency requirement.* The one that does (check C) is the properly-scoped horn-2 share, `(f^λ)²/C_n` over `ℓ(λ) ≤ 2` — normalised exactly (1.0 at n = 4, 6, 8), zero off the cap by construction, a **fifth** measure. **Not endorsed** — it inherits classical Plancherel's q-independence objection; it is named as the only candidate clearing the constraint.

### Not established

- **Φ₁ / Φ₂ are NOT excluded.** Depth 0 and 1 are inside the cap and carry **all** the N=2 mass (check D: 1.0 at n = 3, 6, 9). The exclusion is specific to `k ≥ 2`.
- Which family Φ_k should use. Narrowed by a constraint, not selected.
- Anything about the colour sector — `N = 3` appears only as the tested alternative, and it fails the same way.

### Corrections landed on the merged artifacts

`schur_weyl_share_is_a_third_measure_probe.py` (label + header, still 6/6) and `docs/audits/2026-09-05-schur-weyl-share-is-a-third-measure.md` (correction banner, F3 row, §0 conclusion, §3 caption and closing, §8 open item). F1, F2 and F4 are unaffected — none depends on the depth labelling.

### 2026-09-05 addendum — the corpus-grep: `N = 2` is DERIVED and was closed a month ago, plus a second error of mine

A six-path corpus-grep (path 0 unavailable — `paper-assistant` MCP `ENOENT`, so greps only) strengthens the answer well past "ruled" and finds one more defect in my merged note.

**It is derived, sorry-free, from a framework axiom — and the same axiom excludes `N = 3`.** `VolumeConstraintForcesFibreTwo.lean` (0 sorries), from condition (v) of `def:quantum-observable-universe` (`ε : Λ²V → 𝟙`, `dim Λ²V = C(N,2)`):

    theorem exteriorSquareDim_eq_one_iff (N : ℕ) : exteriorSquareDim N = 1 ↔ N = 2   -- :151
    theorem exteriorSquareDim_three_ne_one  : exteriorSquareDim 3 ≠ 1 := by decide    -- :168

Second route: convention D inverts to Wenzl level `r = 2` on the nose, and `2026-08-16-su-r-level-tower-gap-map.md:57-61` identifies **fibre dimension `N` = Wenzl level `r`**.

**It was closed 2026-08-07.** Bean **`qou-fvzm`** is `completed`: *"CLOSED FOR GOOD 2026-08-07 by main commit `f92a8b15` 'N = 2 is LOCKED IN for the mass pipeline'."* Commit verified: `f92a8b1500`. Its mechanism note is the sharpest statement of why: `χ_λ` are **N-independent**, so all N-dependence sits in the weights, and *"'row cap kills the singlet' and 'Ocneanu weight vanishes' are ONE fact"*. It also records that moving to `N = 3` would **re-weight surviving channels**, not merely add blocks — `y_(2,1)/y_(3) = q[2]_q[N−1]_q/[N+2]_q`.

**The conflation I was entertaining is named in the corpus.** `eightfold-intro.md:26`: *"because we have set `n = 3` and would like `N = 3`. **Setting `n = 3` does not make `N = 3`.**"* And colour does not change the fibre: the canonical `bring_color_weighted` path runs `z_D = q³/(q²+1)` and applies colour as a **δ-perturbation on the p–n interface** (`closed_form_tau_M.py:305-307`); the only `N = 3` fibre in `computations/` is a probe fixture.

### 🛑 A SECOND error in my merged note: F4 computes the share of the wrong algebra

F4 says horn 2's `End(V^{⊗n})` has block share `(f^λ)²/n!`. **At `N = 2` that is `H_n`, which is not the operator algebra of the pair.** `q`-Schur–Weyl is an isomorphism only for `N ≥ n`; at `N = 2`, `n = 3A` the map `H_n(q) ↠ TL_n(q)` is surjective with kernel `n! − C_n`. The correct share is `(f^λ)²/C_n` over `ℓ(λ) ≤ 2` — exactly what check C of the new probe computes.

**The bare `≅` is a live corpus defect in three further places**: `notation-collisions.md:153`, `MassLeftMulEndomorphism.lean:20` (*"literally an endomorphism of `V^⊗ⁿ`"*), `wenzl-bridge-applicability-qou.lean:33`. Self-contradicted by `TraceBlindSector.lean:11` (`TL_n(q) = End_{U_q(sl₂)}(V^{⊗n})`) and by `wedderburn_jones_markov.py:388`'s own kernel dimensions. Two sites get it right: `QSchurWeyl.lean:11` (*"the **image of**"*) and `RowCap.lean:48-56` (*"a number read off `S^λ` for `ℓ(λ) > N` is a number about the algebra, not about the carrier"*).

The `N ≥ n` condition is stated in a **held but uncited** source — `library/black-samson-phd2010sp` pp. 30-31: *"For `d ≤ n`, `π_d` is injective. In the sequel we will be concerned with the other extreme, where `π_d` is **far from injective**"*, at `(m|n) = (2|0)` = Jones = `N = 2`. That is this framework at `d = 3A ≫ 2`. Zero citations outside `library/`.

### Two sourcing errors of mine, corrected

- **Descartes does not force `dim V = 2`.** I cited `state_space_natural_three_sym2_gate.py:8-17`'s *"by the Descartes condition"*. The corpus forbids that: `schur-weyl-eightfold.md:53` (*"compatible with but does not uniquely force"*) and `2026-08-04-ocneanu-trace-parameter-audit.md:114` (***"Do not claim `N = 2` is forced by the Descartes condition"***).
- **`schur-weyl-mass-decomposition.md` does not keep λ with rows beyond 3.** Second-hand and wrong. It is **line 18**, about an approximation discarding *"rows longer than 3"* = `λ₁ > 3`, part **size** — its own examples `(3A−1,1)` and `(3A−2,2)` are two-row partitions. Not the row cap, and no live producer runs it.

### Further corpus defects found, reported not fixed

- **`wedderburn_jones_markov.py` contradicts itself inside one function.** `:355-359` says the `y_λ` path replaces the 2-variable Schur *because* the latter vanishes for >2 rows — implying `y_λ` does not. `:385-395`, same function, says `y_λ` is *"EXACTLY zero for every λ with ≥ 3 rows"*. The docstring is convention-C-era; the body is D.
- **Strand count still unreconciled, with a third site.** `H_{A+Z}` at `atomic-braid.md:2` **and `wedderburn-mass-formula.md:2`** (same chapter as the `3A` claim) against `H_{3A}` at `schur-weyl-mass-decomposition.md:1` and `hecke_3a_weights.py:5`. Does not affect this answer — `N = dim V` is independent of `n`.
- **`markov-trace-frobenius-selection.md:19` calls the fibre-trace premise open** while `TraceBlindSector.lean:26-30` argues it is resolved. Two live positions; they agree on `N = 2` either way, since the volume-axiom route does not go through it.
## 2026-09-05 (later) — the two survivors are now separable, on grounding

Two new measurements, both in exact rational arithmetic, both with their own
witness:

**(1) Molien IS the literature's q-Plancherel measure — now exact, not sampled.**
`probes/molien_feray_meliot_bridge_probe.py` (5/5). The bean already recorded
this identification 'exact in Q(q), n=2,3,4,5'. It is now verified for EVERY
partition of n=1..9 (96 of them) as equality of rationals, plus the two
identities that make the kappa exponent forced rather than chosen
(`sum h = n(lam)+n(lam')+n`, `kappa = n(lam')-n(lam)`, both over n<=10), plus
Feray-Meliot's duality `M_{n,1/Q}(lam') = M_{n,Q}(lam)` over n<=9 — which is
what lets their q<1 theorems reach the substrate's Q = q0^2 ~ 1.232.
`prop:q-plancherel-asymptotic-skeleton` is rehomed onto it (`qou-j7ef`, PR #6771).

**(2) Only Molien is a measure BY IDENTITY.**
`probes/plancherel_deformation_uniqueness_probe.py` (3/3). Of the three
numerators in the corpus, over [n]_q!, exactly one sums to 1:

    (f^lam)^2             -> n!/[n]_q!, falls 0.980 -> 0.326 over n=3..12
    f^lam q^{-kappa} d_q  -> 1, exactly, every n, every q
    d_q^2                 -> rises 0.987 -> 1.517 over the same range

The two failures go in OPPOSITE directions in n, so no single rescaling repairs
both. And the kappa exponent is forced UP TO CONJUGATION: over c in [-3,3],
exactly c = -1 and c = +1 normalise `f^lam q^{c kappa} d_q`, and those two are
one measure on transposed diagrams (conjugation fixes f^lam and the hook
multiset and negates kappa — verified over all partitions of n<=9). I predicted
a unique exponent; the measurement gave two, and the second turned out to be the
same rows-vs-columns duality as in (1), reached from a different direction.

**WHAT THIS DOES AND DOES NOT SETTLE.** It does NOT add a fourth requirement:
R2 asks only for an n-independent normaliser and BOTH survivors satisfy it, so
both remain legitimate probability measures and the choice is still not forced
by the requirement set. What it separates is HOW each earns normalisation —
Molien by a Lean-proved identity for all n and all q>1, `d_q^2/D^2` by dividing
by whatever makes the sum 1 — and Molien additionally carries a literature
asymptotic theorem (LLN for row lengths + CLT at scale sqrt(n)) that
`d_q^2/D^2` has none of.

**MY RECOMMENDATION (judgement, not a finding): Molien.** Normalised by a
theorem rather than by construction, externally grounded, and its kappa is
forced. The cost is that it CHANGES THE k=3 ANSWER — the FR-variance route
names 5_2 under Molien and 6_1 under `d_q^2/D^2`. The paper's structural 6_1
naming comes from the GB-filtration route and carries no weight family at all
(`qou-9b50`), so it is untouched either way; but the FR route's agreement with
it is not.

**STILL OPEN, and it is the author's call**, because wiring a family into the
production Phi_k moves physics-facing numbers and the choice is not derived.


## 2026-09-05 — coordination from #6768, INDEPENDENTLY VERIFIED here

A sibling agent working route 1 posted findings on #6771. I re-checked every
checkable one rather than relaying them; all hold.

- **FM §6.1 states the Schur-Weyl measure outright** —
  `library/arxiv-1001.2180v2/sections/sec-023-...:68`: *'the Schur-Weyl measure
  charges only the Young diagrams whose lengths are smaller than N'*. Neither of
  us had opened that section; I had grepped sec-002/004/021 only.
- **'Schur-Weyl measure' has 0 hits outside `library/`** (content, docs,
  computations, .beans). Verified.
- **`library/arxiv-1009.4034v1`** (Meliot, *Kerov's CLT for Schur-Weyl
  measures*) is held and greppable, **0 citations in references.ts**. Verified.
  Available source, not yet used — deliberately NOT added as a reference entry,
  since an entry nothing cites is noise.
- **The row cap zeroes the `V^{n}` share at N=2** — verified and STRONGER than
  reported: `SU(N) qdim(lam) = 0 IFF lam has more than N rows`, an iff, over
  every partition of n=1..9 at N=2 and N=3. Total `SUM f^lam*qdim` over lam
  with >2 rows is exactly 0.0 at n=3,6,9.

**TWO MORE MEASURES EXIST and my four-family table was implicitly exhaustive.**
Corrected in the #6771 body. Neither is a production path, which the four are:
  - `V^{n}` Schur-Weyl share: `f^lam * prod[N+c]_q/[h]_q`, index set = lam with
    <= N rows, normaliser `[N]_q^n`. Different index set AND normaliser, so it
    is NOT a rescaling of Molien.
  - classical `(f^lam)^2/n!` via `End(V^{n})`. Normalised by Burnside at every
    n — but **q-INDEPENDENT**, which is an objection to it as a Phi_k weight,
    not a feature: it can carry no substrate dependence into the functional.
    Flagged back to #6768.

**WHAT I HAVE THAT ROUTE 1 DOES NOT.** #6768 frames it as *'route 1 now turns on
one thing only: which N the nucleus is a state at'*. True of route 1, but the N
question and the family question are not independent downstream — measured, the
ratio `w_Molien/w_dimq2` at q0 normalised to its own mean spreads
**1.87x at n=3, 22.9x at n=6, 1831x at n=9**, monotone row-to-column (that is
`q^{-kappa}`, extremal on those shapes). Since n = 3A, n=9 is A=3. Picking the
wrong family at the n where the physics lives is a 10^3 error, so selecting a
module reading does not make the family choice a detail. Both stay live.


## 2026-09-05 — CLOSED. Owner ruling: Molien canonical, two-arm reporting.

**Ruling:** *'molien. do the two arm reporting'*. Molien
`f^lam q^{-kappa} dim_q/[n]_q!` is the canonical Phi_k weight; `dim_q^2/D^2`
is retained as a LABELLED comparison arm, not a fallback.

**Delivered:**
- `fr_pullback_k3_test.py` — base measure is now a parameter
  (`base_weights(by_partition, family)`) threaded through the FR pullback, the
  uniform precompute and both binding functions; the pipeline runs twice and
  reports both arms plus a cross-arm comparison. The FR redistribution RULE is
  family-agnostic and unchanged between arms — the two were previously
  conflated in one hard-coded expression, which is the ambiguity this bean was
  about.
- `prop:plancherel-term-7-formulation` — Phi_k defined over Molien, title
  updated, both arms and their disagreement stated in the block itself.

**THE ARMS DISAGREE, which is why one number would have been an overclaim:**

    family              baseline   best knot   best m/m   vs baseline
    molien  CANONICAL     1.5489       5_2       1.2169      +21.4%
    dimq2_selfnorm        1.0660       6_1       1.0478       +1.7%

Under the canonical arm the FR MECHANISM gets substantially stronger support
(+21.4% vs +1.7%) while the paper's 6_1 gets NONE — 6_1 lands at 1.6068x,
WORSE than that arm's own baseline. The paper's structural 6_1 naming is
untouched either way: it comes from the GB-filtration route, which carries no
weight family (qou-9b50), and the verdict string now says so.

**Blast radius, measured (option C):** ~~4 of 36~~ **11 of 37** live
`w_lambda`-referencing files. `w_lambda` is a NAME shared by different objects;
counting the name was the wrong measurement — but so was my replacement for it.

**SUPERSEDED 2026-09-05 (PR #6840).** The 4 was an undercount by a factor of
~2.75, and the sentence it supported — "the one real non-harness consumer
besides the k=3 test is `beta_ew_delta_I_321_and_wedderburn.py`" — is FALSE.
Seven files build `dim_q(...)^2 / q_factorial(...)` and NONE was visible to the
regex, which required the literal token `dim_q`/`d_q` immediately followed by
`**`. The seven spellings that defeated it: `dim_q_num(...)`, `q_dimension(...)`,
`_q_dimension(...)`, `d_q_lam`, `dq[l]`, a single-letter `d`, and — the one that
matters — `dim_q(part) ** 2`, i.e. a CALL to `dim_q` itself, since `dim_?q\w*`
cannot cross a `(`. The detector could only ever match a VARIABLE named dim_q,
never a call to the function it is named after.

Repaired by resolving each operand back through the file's assignments to the
FUNCTION that produced it (`cached_accessor_shape_audit.py` precedent); both
passes retained, buckets are their union, `--selftest` pins the known miss.

**Three of the seven are on the alpha_EM axis** — `alpha_5_jucys_murphy_central`,
`alpha_em_b2_scalar_c_probe`, `alpha_em_b2_canonical_scale_ratio_probe` — an
axis the 4-of-36 figure hid completely. Whether the Molien ruling moves a
physics-facing number there is NOT triaged.

The claim about `beta_ew_delta_I_321_and_wedderburn.py` itself still stands: its
six candidates are same-n ratios — invariant under dim_q^2/[n]_q! ->
dim_q^2/D^2, NOT invariant under Molien.

**Four errors of mine on this bean, all caught by tooling not by me:** scaling
law tested inverted; `(f^lam)^a d_q^b` predicted to normalise at (1,1) when it
gives 0.457 (I had dropped q^{-kappa}); nearly recorded beta_EW as invariant
under the whole choice; and a dated ruling banner in prose plus a JS
string-concatenation bug that broke the manifest. All recorded at the point
where the next reader would repeat them.


### Reconciliation with the parallel route-1 pass (#6768, merged 08:52Z)

That pass reported *'Not established: which family Phi_k should use. Narrowed
and partly excluded, not closed.'* **That was correct and is not contradicted
here.** Route 1 asks which object the nucleus is a state in, and it genuinely
does not select between the two survivors — at N=2 it excludes the module-share
reading altogether, by the same row-cap invariant R1 uses to retire y_lambda.

What closes this bean is not route 1 but the **owner ruling**, which came
after that merge and answers the family question directly. Their F1
(Molien = Feray-Meliot, reached by change of variables) is an independent
second leg under my exact-rational result, and their F2/F3/F4 are why the
`V^{n}` share and classical `(f^lam)^2/n!` are recorded here as further
measures rather than as arms. So: their measurement stands, its 'not closed'
verdict was accurate as of its merge, and the ruling superseded it.

## 2026-09-05 — the alpha_EM axis, triaged (PR #6840)

The corrected blast radius exposed three alpha_EM files the 4-of-36 figure had
hidden. That axis is the one that matters: the corpus's ONE scoreable L2 result
(m_K/m_pi) is alpha_em-conditional.

`probes/alpha_em_b2_weight_family_triage_probe.py` (2/2, 50 dps, no float64).
`alpha_em_b2_scalar_c_probe.py` pins the B2 scalar c on w_(4,1)(q0) and its own
verdict calls that 'the canonical MARKOV normalization'. At lambda=(4,1), n=5:

    Plancherel  d_q^2/[5]_q!        = 0.12862000417524688333   what it COMPUTES
    Molien      f^l q^-k d_q/[5]_q! = 0.07429973308938433194   canonical
    Markov      y_(4,1) at N=2      = 0.12498539716794710592   what it CALLS it

The identification is MEASURED, not inferred from the source shape: the
assertion reproduces the consumer's printed value to 22 digits at 1e-18.

MOLIEN MOVES THIS AXIS BY -42.23 %, AND NO CANCELLATION IS AVAILABLE. This
bean's own result — that a lambda-independent rescale drops out of a same-n
ratio, which is why dim_q^2/[n]_q! -> dim_q^2/D^2 is a no-op for the beta_EW
consumers — DOES NOT REACH HERE. That consumer normalises on a SINGLE
partition, so there is no ratio for anything to cancel from, and Molien's
q^{-kappa} is lambda-dependent besides. Do not carry the beta_EW invariance
result across to this axis; it is scoped to same-n ratios.

The Markov row is the quiet one: 2.83 % from Plancherel, close enough that the
mislabel would never be caught by eye. Presumably how it survived.

NOT a claim that c is wrong: c = (Markov norm)/(Hodge polarization norm) and the
Hodge denominator (Braden-Northover period polarization of Jac(Bring)) is openly
unsupplied, so c is not a delivered number. THE OTHER TWO alpha_EM FILES ARE NOT
TRIAGED.

A precision defect of mine, caught by the gate before commit: the probe first
held its comparison constant as a module-level mp.mpf of a 20-digit literal,
which is evaluated at import when mp.dps is whatever the import order left it
at. At mpmath's default 15 it truncates by 5.98e-18 — LARGER than the 1e-18
tolerance of the assertion comparing against it. It passed only because an
earlier import had already raised dps. Held as a string now;
module_const_precision_audit --strict goes LOSSY 1 -> 0.

## 2026-09-05 — the alpha_EM triage is CLOSED; two of three need no change

Closing the loop the previous entry left open.

`alpha_em_b2_canonical_scale_ratio_probe.py` — NOT AFFECTED, the
counter-example. It tabulates y_lambda and w_wedderburn side by side under
explicit labels and its own comment already states the distinction correctly
("tr(1)=1 for the canonical Markov trace: sum_lam y_lam * f^lam = 1. (NOT
sum_lam w_lam -- that equals 1 only at q=1 ...)"). The mislabel found in the B2
scalar probe is SPECIFIC TO THAT FILE, not general to the axis. Worth stating,
because the natural inference from "three alpha_EM files are affected" is that
the axis is uniformly sloppy, and it is not.

`alpha_5_jucys_murphy_central.py` — AFFECTED IN PRINCIPLE, IMMATERIAL IN FACT.
Its headline compares SUM_{lam |- 3A, ht=6} w_lam c_5(lam) across A = 2,3,4
with w = dim_q^2/[n]_q!; since n = 3A that is a cross-atom metric at three
different n, i.e. exactly this bean's own R2 scope-(b) exclusion. Measured
(probes/alpha5_jm_crossatom_budget_probe.py, 2/2): the height-6 partial budget
B_6(A) spreads 222x across those A, and alpha_5(A) = B_6(A) * <c_5>_A
factorises exactly (1e-40), so a raw spread cannot separate "c_5 moved" from
"the budget moved".

BUT the producer's conclusion is a NEGATIVE reached by all three of its routes:

    NORMALIZED by [3A]_q!   rel spread   482.16 %
    RAW                     rel spread    83.163894
    partial self-normalised rel spread  1327.18 %
    VERDICT: strongly atom-dependent (mechanism orthogonal to JM-central)

including the self-normalised route R2 admits. So the weight-family choice can
neither rescue nor overturn it, and the Molien ruling requires no change to this
file. I was heading for a distortion finding; the measurement says the result is
robust, and the smaller claim is the one recorded.

Verified against the producer rather than modelled on it: the probe reproduces
its printed raw alpha_5 (5.608246e-04 / 1.978017e+00 / 1.645002e+02) and its
partial-norm c_5 (0.4704417 / 42.94229) at q0.

STANDING SCORE for the 11 of 37: 1 file carries a genuine mislabel with a
-42.23 % Molien move (alpha_em_b2_scalar_c_probe, and its c is not a delivered
number anyway); 1 is affected in principle but route-invariant; 1 is a correct
labelled two-arm tabulation. The remaining 8 are NOT triaged.

## 2026-09-05 — the 26 name-gate-missed files, TRIAGED. Net consequence: none.

`probes/../audits/molien_name_gate_missed_triage.py` (1/1). The 26 that the name
gate never examined (13th blindness mode, PR #6867) are NOT a blast radius:

    zero importers                24 of 26
    writes a committed witness     8
    shape_only (may not be family) 5
    my own session harnesses       2

PREMISE CORRECTED FIRST, because I had it wrong in #6867. I wrote there that
mass_endomorphism.py "divides by the sum of its own weights and is therefore
already self-normalised dim_q^2/D^2, which the ruling does not move." THE SECOND
CLAUSE IS FALSE. Self-normalisation cancels a lambda-INDEPENDENT rescale --
which dim_q^2/[n]! -> dim_q^2/D^2 is, same numerator -- but Molien's numerator
change dim_q^2 -> f^lam q^{-kappa} dim_q is lambda-DEPENDENT, so nothing
cancels. Worst |selfnorm - Molien|/Molien, measured at the proton q0:

    n=3   0.3849        n=6   3.8263        n=9   37.516

It GROWS with n. "On a sanctioned arm" and "unmoved by the ruling" are different
claims and only the first holds.

THE ONE FILE WITH REACH, traced end to end -- and it is mass_endomorphism, the
one I had called safe:

    w_sym/w_std/w_alt (L93-99, self-normalised dim_q^2/[3]_q!)
      -> Vf at L132, inside additive_wedderburn_volumes()
      -> v['full']
      -> m_p_m_e_li2q.py:78-80 (electron / proton / neutron)
      -> :48,50,54 into desc/single/cross
      -> mp_me = p_total/e_total  vs  codata_mp_me = 1836.152

The weights do NOT cancel in that ratio: they are module-level constants for
lambda |- 3 applied to the electron (2 strands) and nucleons (3 strands) alike,
and Vf enters non-linearly via Phi_q(|Vf|) and products Vf_i*Vf_j.

AND IT IS IMMATERIAL, WHICH IS THE POINT. The committed witness
m-p-m-e-li2q.witness.json records m_p/m_e = 9310.3278 (err 407.06 %) on the
Phi_q arm and 3.3322 (err 99.82 %) on the Li_2_q arm. The route is ALREADY
recorded as a catastrophic miss, so a 38.5 % weight change can neither rescue
nor damage it.

SO: 24 of 26 are dead ends, and the one with reach feeds an already-refuted
comparison. The Molien ruling has no consequential consumer among the 26.

A BLINDNESS OF MY OWN, committed while measuring this: my first import count for
additive_wedderburn_volumes was ZERO, from a single-line grep
`import.*\bname\b`. BOTH real importers use a parenthesised multi-line import
with the name on a continuation line. Re-measured with ast.ImportFrom: 2. Same
class as everything else in this thread.

NOT FIXED, separate defect: additive_wedderburn_volumes is float64 throughout
(a, b = 0.0, 1.0) on a path ending at a CODATA comparison.

## 2026-09-05 (later still) — 🛑 RETRACTION: my "TL constraint" was a scope error the audit already names

**Probe:** `computations/probes/phi_k_is_not_a_trace_probe.py`, 4/4, exit 0, zero builtin-float coercions, no witness.

### What I claimed, merged in #6806

> *"Any weight family consistent with the corpus's canonical trace must vanish on `ker(H_n ↠ TL_n)` … no candidate currently on the table satisfies the corpus's own consistency requirement."*

### Why it is wrong — three ways, any one sufficient

1. **The Φ_k audit names this as the error it exists to block.** Its **R3** row reads: *"no Markov property is required — **Φ is not a trace** … it removes the reason to want `y_λ` and **blocks a scope error**."* My constraint is exactly that scope error.
2. **Φ_k is not linear on the algebra.** `Φ_k(β) = Σ_{λ: depth k} w_λ·log(|χ^λ(β)|·d_q(λ))` — a log-weighted sum over one stratum. `tr_M = Σ_λ y_λ χ^λ` is a linear functional on `H_n(q)`. A kernel argument about which *algebra elements* act as zero says nothing about which *partitions* a separate functional may weight.
3. **It annihilates its own subject.** Imposed, it forces `w_λ = 0` on every λ with ≥3 rows — every stratum of depth ≥ 2 — so `Φ_k ≡ 0` for **all** `k ≥ 2` by the audit's own R1. A requirement that forbids the object being constructed is a reductio.

### And the "fifth measure" I endorsed FAILS R1

§4 named the TL share `(f^λ)²/C_n` over `ℓ(λ) ≤ 2` as *"the one candidate that clears the constraint"*. It clears it by being zero off the two-row cap — precisely what R1 retires `y_λ` for. Measured per stratum:

| n | d0 | d1 | d2 | d3 | … |
|---|---|---|---|---|---|
| 4 | 0.07143 | 0.9286 | **0.0** | **0.0** | |
| 9 | 0.0002057 | **0.9998** | **0.0** | **0.0** | all 0.0 |

**My proposed solution was the degenerate case.**

### Molien — the ruling's answer — satisfies R1 and R2 on exactly those strata

| n | d0 | d1 | d2 | d3 | d4 |
|---|---|---|---|---|---|
| 6 | 0.0002492 | 0.09749 | 0.4683 | **0.3487** | 0.07958 |
| 9 | 3.941e-8 | 0.002391 | 0.1115 | **0.3916** | 0.3446 |

Nonzero on every depth ≥ 2 stratum — peaking on **depth 3, the chirality channel** — and total mass exactly 1 at n = 3…9 (R2). The owner ruling *"molien. do the two arm reporting"* is unopposed by anything I measured.

### What survives from #6806

§1 (`N = 2`, four corpus witnesses — the question that audit was written to settle), §2 (the TL/Catalan arithmetic and the six kernel dimensions), §3 (the depth off-by-one and the `N = 3`-is-also-null measurement), and the follow-on §4c/§4d defects. **Only §4's constraint and its endorsed measure are withdrawn.**

### Contamination

The same claim was sent to sibling PR #6771 (comment 5550892514) as *"three of your four rows violate it"*. Corrected there. It reached no content block, no Lean file, no witness — the sibling's `qou-oots` closure was reached independently and does not rest on it.

**This is the third error of mine in this arc** — after the depth off-by-one and the wrong-algebra F4 — and it is the same shape as both: a correct local measurement carried into a frame it does not license.

### Route 1 is closed, and the answer is a negative (2026-09-05, same branch)

The retraction above left route 1 of the Φ_k audit §7 standing. It is now closed — measured, not argued — and it closes the *opposite* way to how §7 anticipates.

§7 poses route 1 as a fork: name the object the nucleus is a state in, and the measure follows (`V^{⊗n}` ⇒ Molien-shaped; `End(V^{⊗n})` ⇒ `d_q²/D²`-shaped). At the settled `N = 2` **both horns are supported on `ℓ(λ) ≤ 2` and are exactly zero on every stratum of depth ≥ 2**:

| n | A | Σ h1 | h1 d≥2 | Σ h2 | h2 d≥2 | Σ Molien | Molien d≥2 |
|---|---|---|---|---|---|---|---|
| 3 | 1 | 1.0 | **0.0** | 1.0 | **0.0** | 1.0 | 0.223435 |
| 6 | 2 | 1.0 | **0.0** | 1.0 | **0.0** | 1.0 | 0.902265 |
| 9 | 3 | 1.0 | **0.0** | 1.0 | **0.0** | 1.0 | 0.997609 |
| 12 | 4 | 1.0 | **0.0** | 1.0 | **0.0** | 1.0 | 0.999985 |

h1 = `f^λ d_q^{SU(2)}(λ)/[2]_q^n` (dies at `[2+(−2)]_q = [0]_q = 0`); h2 = `(f^λ)²/Catalan(n)` over `ℓ(λ) ≤ 2` (TL_n *has* no wider blocks). By R1 each gives `Φ_k ≡ 0` for k ≥ 2. **Scope-(b)**, row cap cited.

**The fork was real** — max per-λ gap 0.305/0.205/0.206/0.217 at n = 3/6/9/12 — so §7 was sound at general `N`; it is the `N = 2` ruling, which post-dates it, that collapses it.

**Not a derivation of Molien.** Molien passes R1 where both horns fail it, and the owner ruled it canonical. That is *why the ruling was needed* — the route the audit ranked most decisive cannot answer — not a substitute for one. Routes 2 and 3 stay live.

Probe `computations/probes/route_1_is_degenerate_at_n_two_probe.py` (5/5); audit §4e.

### The "then pick a larger N" rescue is not available (2026-09-05)

§4e said the route-1 fork *would* decide at general `N`, which invites re-choosing `N ≥ 4` to revive both horns on depth ≥ 2. It is not a change of reading: the Ocneanu/Markov weights depend on `N` through a nontrivial rational function of `q`, so moving `N` re-weights every surviving channel.

Reproduced independently at the proton q₀, 50 dps, balanced, against `y_{(2,1)}/y_{(3)} = [2]_q[N−1]_q/[N+2]_q` — the three values #6829 supplied on #6826:

| N | ratio | shift |
|---|---|---|
| 2 | 0.48930712047797097007 | — |
| 3 | 0.77459088135788091778 | **+58.30 %** |
| 4 | 0.95812403128848485757 | +23.69 % |

So a route-1 rescue by re-choosing `N` is a change of **trace**, and the trace is fixed by the convention-D ruling.

**Verified vs cited, kept apart.** The three ratios are verified here. The stronger identification — `N` *is* the Ocneanu parameter `a = q^{N−1}`, so "choose N" and "choose the trace" are one act — is #6829's and is cited, not asserted.

Convention trap, confirmed: `ocneanu_N_lockin_probe`'s docstring writes the form **asymmetrically** (leading `q`) while `y_lambda_su_n` computes **balanced**; the arms differ by exactly that `q` (0.5431 / 0.8598 / 1.0635), so cross-reading them looks like a discrepancy and is not.

Probe `computations/probes/ocneanu_n_lockin_crosscheck_probe.py` (3/3).


### 2026-09-06 — REOPENED. `completed` violated owner rule 13a, which landed today.

**Status changed `completed` → `in-progress`.** Not a new finding; a status this
bean's own body already contradicted.

**The rule.** `c1b63ac76d` (2026-09-06) added AGENTS.md §13a, owner directive,
verbatim *"Don't close beans with open conjectures!!!"*: a bean tracking a
conjecture or an unsupported identification **stays `todo` / `in-progress` until
the mathematics closes — not until the *recording* of its openness is done.**

**Why this bean qualifies, from three independent sources:**

1. **Its own first heading** — *"requirement derivation + prune + discriminator
   (in-progress; **the CHOICE is open**, the PRUNE is not)"*.
2. **AGENTS.md:4426**, the notation-collision register: *"Whether `$\dim_q^2$` is
   even the right numerator — against the Molien `$f^\lambda \dim_q(\lambda)$` …
   — is **open**, bean `qou-oots`."* The repo's own instructions name this bean
   as the live carrier of an open question while the bean says it is done.
3. **This branch's audit §5**, under NOT established: *"**Which family Φ_k should
   use.** §4e removes route 1 as a way to answer it; it does not answer it."*

**What WAS closed, and it is real:** the prune (four families down to two), the
requirement derivation (R1/R2/R3), the discriminator, the α_EM triage, the
26 name-gate-missed triage, and — this branch — route 1, which closes
**negatively**: both horns vanish on depth ≥ 2 at `N = 2`, so the route the audit
ranked most decisive cannot answer. That is why the owner's Molien ruling was
needed, and it is precisely *not* a derivation of the answer.

**So the completion recorded the closing of every sub-task while the subject
stayed open** — the exact shape §13a names. Routes 2 and 3 of the Φ_k audit §7
are still live; §7 route 2 (a same-`n`, within-stratum observable) is the
nearest actionable one.

## 2026-09-08 — re-affirmed by the owner (chat): Molien. The 2026-09-05 ruling stands; the agent's audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §7.1 D2 wrongly listed the choice as open and is corrected on the same branch. Remaining in-progress scope is the α_EM-axis triage (PR #6840), not the choice.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under carrier M7 (qou-g16t) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

2026-10-10 (bean qou-we2d, PR #7557): Lean now proves the Molien weight M_mu(q^2) = q^{-kappa}/prod[h]_q is the z = 0 Markov trace and equals the symmetrising trace tau(T_w)=delta_{w,1} (QOU.SchurWeyl.SeminormalRep.molienMarkovTrace_symmetrising, eq_molien_of_zero; ocneanuWeight q 0 = molienWeight). Consequence for this bean: Molien as a TRACE weight has z = 0, so any channel that needs a Markov property with z != 0 (interface mu = tau(sigma)) cannot use it; Molien as a MEASURE is unaffected.

## 2026-09-14 — the ruling had TWO live carriers still saying "open", and AGENTS.md was one

The 2026-09-08 entry above says the audit doc was corrected. It was — rows D2
of `docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md` (lines 624, 745)
are on `main` and say so in their own words: *"This row was written as open by
mistake; corrected 2026-09-08."* **But the sweep stopped there.** Measured
`grep -rn "right numerator"` across `.md` / `.py` / `.ts`, excluding `.beans/`:
exactly **two** live carriers of the stale claim, and neither was an audit doc.

| carrier | what it said |
|---|---|
| `AGENTS.md:4924` | *"Cross-atom consumers use the self-normalised `d_q^2/D^2` … Whether `dim_q^2` is even the right numerator … is **open**, bean `qou-oots`."* |
| `computations/audits/confinement_filtration_vs_gbdepth_probe.py:180` | *"bean `qou-oots` records that whether dim_q^2 is even the right numerator is OPEN"* |

**AGENTS.md is the one that matters, and it is worse than a stale status
line.** It does not merely *record* the question as open — it gives a
**directive**, "cross-atom consumers use the self-normalised `d_q^2/D^2`", i.e.
it tells every agent to reach for the arm the owner ruled is a labelled
comparison, nine days after the ruling and six after the re-affirmation. And
the arms are not close: Molien gives the FR mechanism **+21.4 %** over its own
baseline (best knot `5_2`), `d_q^2/D^2` gives **+1.7 %** (best knot `6_1`), and
the paper's `6_1` gets **no** support under the canonical arm. An agent
following the old sentence picks the arm that flatters a different knot.

**The second carrier is MINE, and it is the laundering path this repo keeps
recording.** `confinement_filtration_vs_gbdepth_probe.py` merged ~2 h earlier
(PR #7375). I did not measure that claim — I copied it out of AGENTS.md while
writing a probe whose whole §0 is about reading a convention off the corpus
rather than assuming one. A stale instruction file produced a fresh artifact
that then corroborates it; that is the mechanism, not a coincidence.

**One thing the carriers got right by accident, now made explicit.** AGENTS.md
cites the Molien identity `Σ_λ f^λ dim_q(λ) = [n]_q!` as Lean-proved sorry-free
for all `n`, all `q>1`. That identity holds under the **fake-degree**
convention and **fails** under the symmetric one — measured independently in
the probe's §0 (`n = 2..5`, fake holds at all four, symmetric fails at all
four), and recorded from the other side in `notation-collisions.md:34`, which
identifies the corpus's Molien weight with `𝕄_{n,q}` at `Q = q²` exactly. So
AGENTS.md's own cited theorem **already commits to fake-degree** and the line
never said so; resolving a bare `dim_q` to symmetric silently breaks the
theorem being cited. Now stated in the line.

**🛑 Do NOT collapse the two questions — the fix deliberately keeps them
apart.** `qou-oots` ruled the Φ_k **weight family**. The probe's two
conventions are how `dim_q` **itself** is computed inside
`def:knot-operator-energy`'s `E(λ,q)` — a different object from the Φ_k weight.
The ruling reaches the first and, via the Molien identity, fixes fake-degree
for the canonical Φ_k weight; it does **not** reach `E`, whose own block text
pins **symmetric** (it says the minimum `1/[k]_q!` is attained by the trivial
`(k)` *and* `(1^k)` reps, which needs `dim_q = 1` for both — true only without
the `q^{n(λ)}` prefactor). That internal tension in `def:knot-operator-energy`
is **untouched by the ruling and stays open**. The probe carries both arms for
exactly this reason and its conclusion holds under each.

**Scope of the AGENTS.md rewrite — narrower than it may look.** The ruling is
about **Φ_k**. For a cross-atom consumer outside Φ_k the self-normalisation
argument in that line still stands; what changed is that the family is now a
**declared choice**, never an implicit `d_q^2/D^2`. I did not promote Molien to
"all cross-atom consumers" — the ruling does not say that.

**This bean stays open** (§13a). The remaining scope is unchanged and is what
the 2026-09-08 entry names: the **α_EM-axis triage** — three `alpha_em*`
producers build `dim_q^2/[n]_q!` and whether the ruling moves a physics-facing
number there is still untriaged. Nothing here touches that.

### α_EM-axis triage — partial: prior art exists for 1 of 3, and the dashboard row is CLEAN

The entry above names the remaining scope as the α_EM-axis triage. Two findings,
one of them a re-derivation I should have grepped for first.

**1. It is already triaged for `alpha_em_b2_scalar_c_probe`, and I re-derived
the argument before checking.**
[`computations/probes/alpha_em_b2_weight_family_triage_probe.py`](../computations/probes/alpha_em_b2_weight_family_triage_probe.py)
exists, cites this bean by name, and runs clean (2/2). Its result:

    lambda = (4,1), n = 5, q0 = 1.109978582751, f^lambda = 4, kappa = contentSum = 5
    Plancherel  d_q^2/[5]_q!         = 0.12862000417524688333   <- what the consumer computes
    Molien      f^l q^-k d_q/[5]_q!  = 0.07429973308938433194   <- what the ruling makes canonical
    Markov      y_(4,1) at N=2       = 0.12498539716794710592   <- what its verdict CALLS it
    Molien / Plancherel = 0.577668563811813569   (-42.2331 %)

It also carries a finding I did not have: the consumer's verdict **mislabels**
the object, calling `d_q²/[n]_q!` *"the canonical MARKOV normalization"* when the
Markov weight is `y_λ` — three families, one name. And note `κ` is the **content
sum**, not Macdonald's `n(λ)`; I would have guessed wrong.

**2. NEW — the dashboard's `α_em⁻¹` row does NOT depend on the weight family.**
Measured, and it narrows that probe's own stated worry. The row's
`source_witness` is `alpha-em-schwinger-ladder.witness.json ::
data.ladder_proton.form_B_alpha_inv`, produced by
`alpha_em_schwinger_ladder_probe.py`. That producer:

- reads **no** witness and no JSON (`json.load` / `witness.json` / `open(` all absent);
- contains **zero** matches for `dim_q` / `d_q` / `q_dimension` / `q_factorial` /
  `wedderburn` / `plancherel` / `molien` / `weight`;
- imports only `mpmath`, `_path_bridge`, `witness_base`, `_precision`,
  `q_parameter`, `qou_substrate.codata` — and the only two regex hits anywhere in
  that cone are **prose in comments** (`_precision.py:26`, `q_parameter.py:150`).

So the Molien ruling moves the three named producers' internal quantities and
**does not move the one physics-facing α_EM number the dashboard scores**
(238.3× miss, added 2026-09-07). Import cone checked explicitly rather than
file-locally, since that is the documented trap.

**Still open, and this is the live question.** The existing probe's concern is
not the dashboard row — it is that *"the corpus's ONE scoreable L2 result
(m_K/m_π) is α_em-conditional"*. `m_K/m_π`'s α_em is a **CLASS-A acknowledged
anchor** (CS ansatz conditional on the open Witten-κ `sorry`) per its dashboard
`source_witness`. Whether that anchor's value traces to the schwinger ladder
(weight-free, so clean) or to the B2 scalar-c route (weight-dependent, −42.2 %)
is **not yet measured**, and it is what decides whether the ruling reaches the
framework's only sub-100× number. Note the B2 route is not currently delivered
at all — the existing probe states the Hodge denominator (Braden–Northover
period polarization of Jac(Bring)) is not supplied — so the likely answer is
"clean", but that is an expectation, not a measurement.

The other two named producers are **not** triaged: `alpha_5_jucys_murphy_central`
builds `Σ dim_q² c_5 / Σ dim_q²`, a same-`n` weighted average — the `[n]_q!`
cancels but `f^λ q^{−κ} dim_q` vs `dim_q²` differ per λ, so it is **not**
invariant under Molien (it *is* invariant under the `d_q²/D²` comparison arm,
the same asymmetry recorded for `beta_ew_delta_I_321_and_wedderburn.py`);
`alpha_em_b2_canonical_scale_ratio_probe` reports `y_(4,1)` vs `w_(4,1)` as an
explicit two-arm comparison with Molien absent as a third arm.

## Round 51 Formalization & 50-dps Witness (PR #8228)
- [x] **Lean 4 Module (`0 sorry`, `0 axiom`, `0 vacuity`):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/TwoLoopFlatTorusThetaAndWeightTriage.lean` (`jucysMurphy_n5_symmetric_weight_sum_eq_zero`, `jucysMurphy_n5_molien_strictly_negative`, `weight_families_41_strict_ordering`).
- [x] **50-dps Witness:** `computations/probes/round51-two-loop-flat-torus-theta-weight-and-peripheral-slope.witness.json` (`scriptHash: 879cd7fbcdb2`, `scriptCommitSha: bffc9aa954100eaed1adf1a81eb35fe56e86a5f2`).
- [x] **PR:** `litlfred/qou#8228` (`https://github.com/litlfred/qou/pull/8228`, head SHA `8335ad54a1e5c4f7a61669fed19de6b0184f0a4d`).
- [ ] **Reviewer-separated closure:** Kept at `status: in-progress`.
