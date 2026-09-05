---
# qou-oots
title: 'Phi_k weight family is unjustified: dim_q^2 misuses a quantum dimension where f^lambda*dim_q (Molien, Lean-proved exactly normalized) or y_lambda (Markov, canonical Frobenius pairing) may belong'
status: completed
type: task
priority: normal
created_at: 2026-09-05T05:55:40Z
updated_at: 2026-09-05T09:27:34Z
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

And **Féray–Méliot §6.1 states this pairing outright**, in the paper §2 already cites — `library/arxiv-1001.2180v2/sections/sec-023-61-decomposition-of-tensor-representations.md`: the module gives the *Schur-Weyl measure* `f^λ·dim U_λ/N^n`, *"the same construction with the regular representation gives rise to the Plancherel measure"*, and *"the Schur-Weyl measure charges only the Young diagrams whose lengths are smaller than N"* — F3, in the literature's own words. The term **"Schur-Weyl measure" appears nowhere outside `library/`** (0 hits in `content/`, `docs/`, `computations/`, `.beans/`).

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
