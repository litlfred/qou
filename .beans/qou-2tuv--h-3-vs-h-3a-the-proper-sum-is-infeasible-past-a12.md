---
# qou-2tuv
title: 'H_3 vs H_{3A}: the proper sum is infeasible past A~12, so substitution cannot fix the heavy-atom rows'
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T11:25:45Z
updated_at: 2026-08-23T07:57:44Z
---

## What the audit recommends, and why its Path A is not available

`docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md` recommends **Path A**:
"Fix `pyhecke/atom.py` to compute Wedderburn weights dynamically from
`partitions_of(3A)` → 15+ callers fixed automatically. Path A is much cleaner."

Path A is not reachable. The H_{3A} Wedderburn sum runs over p(3A):

     A     3A          p(3A)
     1      3               3
     2      6              11
     4     12              77
    12     36          17,977
    20     60         966,467
    40    120   1,844,349,560
   418   1254   3.2e35

`mass_at_3A_proper.py` says so in its own header: *"Heavy atoms: full p(3A)
enumeration fails for 3A ≳ 35 (p(36) ≈ 17 000, dim-sum ≈ 3 × 10⁷). Any
truncation is an audit option, never the default."*

So the correct weights are computable to **A ≈ 12** and no further. Any producer
scanning beyond that — `mass_table_comprehensive` goes to **A = 418** — cannot
be fixed by substitution at all. That is a property of the mathematics, not of
the implementation.

## Where per_generator_V_hat_3A SHOULD be used

Callers whose atom range stays within A ≲ 12 can migrate; callers that scan
heavy nuclei cannot. Of the 31 files calling `atom_per_generator_volumes`, the
audit already names the A-bounded ones:

    mass_formula_6term.py            tower_isotope_absolute.py
    mass_formula_6term_mpfr_50dps.py paper_six_term_isotope_sweep.py
    catalan_binding.py               brane_tower_isospin_diagnosis.py
    multi_level_jet_sum.py           entanglement_orders.py
    adjacent_vs_full_probe.py

Those are the migration candidates. `mass_table_comprehensive.py` is NOT one —
it must instead DECLARE the approximation, which it now does (added caveat).

## Measured: how wrong are the H_3 weights?

Deuteron (A=2, 3A=6, 11 partitions — the one case cheap enough to compute both
ways in this container):

    legacy (H_3)   V_hat = [1.08022, 0.94694, 0.34000, 0.94109, 0.94310]
    proper (H_3A)  V_hat = [0.67139, 1.05511, 0.00007, 0.55166, 1.08837]

    sum ln|V|   legacy  -1.1755
                proper -10.3951      ratio 8.84

Since `B = -alpha * sum ln|V|`, the proper weights give **8.84x more binding**
at A=2. The third generator is the striking one: H_3 says 0.34, H_{3A} says
7e-05 — four orders of magnitude, and it is the dominant term in the log sum.

### What this does NOT establish

One data point is not an A-dependence. The heavy-A deficit is a ~3.5x
UNDER-prediction (B_pred/B_AME plateaus at ~0.28 for A >= 12, qou-53p1), so a
correction of this sign and order is what those rows need — but at A=2 the
model is already ~2x OVER (q-CLT D: +97.9%), and multiplying by 8.84 would make
it far worse. So the H_3 fix is **not** a uniform rescale that repairs the
table; it is a large A-dependent correction that plausibly helps heavy and
hurts light.

Getting the actual A-dependence needs the same measurement at A = 3, 4, 6, 8,
12. That is the next step and it is bounded work — p(36) = 17,977 is the
ceiling, and each point is minutes not hours.

## Not done

- The A = 3..12 sweep above.
- Migrating the nine A-bounded callers.
- `atom_mass_derived.py` (audit §6, "DO NOT TRUST OUTPUT", production-wired).


---

# MEASURED: the proper H_{3A} weights make the binding channel WORSE, not better

This bean asked whether the H_3 → H_{3A} fix is the missing scaling factor.
Measured, at the one A where both sides are computable in reasonable time:

    atom  A  3A  t_proper  ratio    B_legacy   B_proper   B_AME   err%_leg  err%_proper
       D  2   6      0.6s  8.843       4.402     38.924   2.225     +97.9      +1649.8

`B = -alpha * sum ln|V|` with `alpha = m_e * 8 * G = 3.744 MeV` (the q-CLT
scale), legacy = `pyhecke.atom.atom_per_generator_volumes` (H_3 weights),
proper = `mass_at_3A_proper.per_generator_V_hat_3A` (full H_{3A} sum).

**The answer is no.** At A = 2 the correct weights multiply the binding by 8.84
and take the deuteron from +98% to **+1650%** — seventeen times worse. The H_3
bug is real and the H_{3A} weights are the mathematically correct ones, but
substituting them into THIS formula does not repair the table; it destroys the
one atom that was closest.

That is a genuine negative result and it constrains the answer to the wider
question (qou-53p1: "wrong scaling factor? what missing?"). It rules out the
most attractive hypothesis — that the heavy-A ~3.5x under-prediction and the
H_3 weight error are the same defect. They are not: the weight error pushes
binding UP by ~9x at A = 2, while the heavy-A rows need ~3.5x UP and the light
rows need to come DOWN. No single weight correction does both.

The per-generator detail shows why it is not a smooth rescale:

    legacy (H_3)   V = [1.08022, 0.94694, 0.34000, 0.94109, 0.94310]
    proper (H_3A)  V = [0.67139, 1.05511, 0.00007, 0.55166, 1.08837]

Generator 3 moves from 0.34 to 7e-05 — four orders of magnitude, and since the
sum is over `ln|V|` that single entry dominates the whole change. A near-zero
V̂ is exactly the row-cap structure convention D's forcing argument predicts
(`y_(1^3) = 0`), so the H_{3A} answer is not obviously wrong — but a log-sum
formula is maximally sensitive to it, which suggests the FORMULA is the wrong
consumer of these volumes, not that the volumes are wrong.

## Practical feasibility is far worse than the module claims

`mass_at_3A_proper.py`'s header says "full p(3A) enumeration fails for
3A >~ 35". Measured in this container:

    3A = 6  (A=2, D)     0.6 s
    3A = 9  (A=3, T)     > 20 min, did not complete

So the practical ceiling is **A = 2**, not A = 12. p(9) is only 30 partitions;
the cost is in building the seminormal matrices, not the partition count. Any
plan that says "migrate the A-bounded callers to per_generator_V_hat_3A" needs
to confront that the implementation is unusable at A = 3 as it stands.

This makes the nine migration candidates listed above **blocked on performance
work**, not merely queued.

## Status

Left `todo`, not completed. What is measured: the A = 2 point, the direction,
and the practical ceiling. What is NOT measured: the A-dependence, because the
A = 3 point does not finish. Getting it needs `per_generator_V_hat_3A` profiled
and sped up first — which is now the actual next step, ahead of any migration.


---

# CORRECTION: the weights were fine. I fed them to the wrong package.

The section above concluded "the proper H_{3A} weights make the binding WORSE"
and called the hypothesis refuted. **That was wrong**, and the owner's instinct
— "maybe missing something else that goes with those weights?" — was right.
Three things go with them, and I had supplied none of them.

## Measured, deuteron (AME 2.22452 MeV)

                  volumes                    consumer   scale      B_MeV      err%
    normalized_plancherel        log-sum, no baseline   alpha    38.9241   +1649.8
    normalized_plancherel      log-sum, free-baseline   alpha    35.7229   +1505.9
    normalized_plancherel      log-sum, free-baseline     E_0     7.4636    +235.5
    normalized_plancherel  Phi_q tower, free-baseline     E_0  2258066.5  +1.0e8

              jones_wenzl        log-sum, no baseline   alpha    74.7505   +3260.3
              jones_wenzl      log-sum, free-baseline   alpha     3.0641     +37.7   <-- BEST
              jones_wenzl      log-sum, free-baseline     E_0     0.6402     -71.2
              jones_wenzl  Phi_q tower, free-baseline     E_0     0.3248     -85.4

               legacy H_3        log-sum, no baseline   alpha     4.4015     +97.9   <-- production today
               legacy H_3      log-sum, free-baseline   alpha     4.0396     +81.6
               legacy H_3      log-sum, free-baseline     E_0     0.8440     -62.1
               legacy H_3  Phi_q tower, free-baseline     E_0   21506.79    +9.7e5

**The H_{3A} weights beat the H_3 weights once their package is supplied:
+37.7% against production's +97.9%.** My -1650% was `normalized_plancherel`
volumes in a consumer that expects neither that scheme nor a baseline.

## The three things, and how much each is worth

**1. The weight scheme — this is the big one.**
`per_generator_V_hat_3A` defaults to `weight_scheme="normalized_plancherel"`,
whose own docstring concedes it is a fudge: it rescales to sum = 1 "even if it
doesn't match the canonical Jones parameter z for tr_M(sigma_i)". It also
claims to keep V_hat "in the physical range [-1, 1] at our q0, which is what
the Phi_q tower needs". **It does not.** Measured on the deuteron:

              scheme                max|V_hat|   > 1 ?   >= Phi_q cap (1.087779) ?
              legacy H_3               1.08022     yes    no
    normalized_plancherel               1.08837     yes    YES
               plancherel               1.07866     yes    no
              jones_wenzl               0.06979      no    no

`normalized_plancherel` puts a generator AT the saturation cap, which is
exactly why `binding_3A_tower` returns 1e7 MeV. `jones_wenzl` — the Ocneanu
weights built on z = q^3/(q^2+1), i.e. **convention D** — is the only scheme
that leaves the tower's own precondition intact.

So the default weight scheme is inconsistent with the owner's trace-convention
ruling, and it silently breaks the consumer the volumes exist to feed.

**2. The free-baseline subtraction.** `B ∝ (free − atom)`, W_free =
`include_inter=False`. Worth **86x** for jones_wenzl (+3260% -> +37.7%);
almost nothing for legacy (+97.9% -> +81.6%). That asymmetry is itself
informative — the H_3 volumes barely change between the free and atom words,
which is what an A-independent weighting would do.

**3. The scale, and it is unresolved.** Two live scales differing by 4.79x:

    alpha = m_e * 8G = 3.744460 MeV   (Catalan; the q-CLT proxy)
    E_0             = 0.782333 MeV   (free-neutron beta-decay Q; "no Catalan")

Which is correct flips the deuteron from **+37.7% to -71.2%**. alpha is a
derived volume scale (8G = Vol(Borromean)); E_0 is a calibration. Having both
in the same table, on different channels, is a third incoherence alongside the
convention split (qou-jm5i) and the H_3/H_{3A} split. **This is the open
question and it is a physics call, not a code one.**

## Also found

`mass_from_tower_safe` imports `z_mark` from `mass_endomorphism`, which is
already convention **D** (`q0**3/(q0**2+1)`) — so that is NOT a third C site.
The 2026-04-20 infrastructure audit describes it as C, but that doc predates
the migration.

The free baselines are structurally incompatible between implementations:
`include_inter=False` returns **5** generators from `per_generator_V_hat_3A`
(3A-1, empty words contributing V_hat = sum w = 1) but **4** from
`atom_per_generator_volumes` (2A). Any cross-implementation comparison of free
words has to account for that.

## Revised status

Not refuted, and not a dead end. The H_{3A} migration is worth doing, but it is
a **package swap** — weights + scheme + baseline + scale — not a drop-in
substitution of `per_generator_V_hat_3A` for `atom_per_generator_volumes`. A
caller that swaps only the function gets my -1650%.

Still blocked on: performance (3A=9 does not finish in 20 min, so the
A-dependence is still unmeasured), and the alpha-vs-E_0 scale decision.


---

# The performance blocker: it is the numpy/mpmath dtype leak (qou-5qwb), 642x

Profiled rather than guessed, and my first guess was wrong.

**Not** the seminormal construction — that is fast:

    n=6   11 partitions   _cached_seminormal total  0.01s   sum dim^2 =     720
    n=9   30 partitions   _cached_seminormal total  0.11s   sum dim^2 = 362,880

It is the matrix loop, `M = M @ (c * sigmas[i] + d * I_lam)`. The braid word
from `atom_braid_word_3A(1,2)` carries mpf coefficients in **19 of its 35
steps**:

    c=int  d=int   x16
    c=int  d=mpf   x17
    c=mpf  d=mpf   x2

`sigmas[i]` is a float64 ndarray, but `d` is an mpf, so `c*sigma + d*I`
promotes to **dtype=object** and the matmul leaves BLAS for Python-level
mpmath arithmetic:

    3 matmuls at dim=162:   as-is 18.928s   forced float64 0.0295s   ratio 642x

That is bean **qou-5qwb**'s exact failure mode, and it explains why 3A=9 does
not finish while 3A=6 takes 0.6s: n=9 has partitions of dim up to 216 where
n=6 tops out at 16.

Provenance: the mpf coefficients arrive from `efcaf79ed` — the same NO-FLOAT64
braid-word commit that cost `atom_per_generator_volumes` 11.5x (qou-53p1).
Here it costs 642x, because this consumer does real matrix products.

**The dtype-leak gate did not catch it.** `numpy_mpmath_dtype_leak_audit.py` is
blocking and was GREEN on every run this session. Worth a look on its own.

# "Where else is normalized_plancherel used where it should not be?"

Swept. Four live call sites plus two defaults, and — the bad one — the
deprecation warning itself recommends it:

    tools/pyhecke/python/pyhecke/atom.py:556        <-- the DeprecationWarning TEXT
        "Migrate to mass_at_3A_proper.per_generator_V_hat_3A"
        ... and the audit it cites spells the call with
        weight_scheme="normalized_plancherel"

    computations/binding_via_interface_knot.py:213,216      explicit, atom + free
    computations/delta_lambda_v_hat_z_transfer_phase5d_4.py:109,111  explicit
    computations/trace_convention_reconciliation.py:47      imports the weights directly
    mass_at_3A_proper.py:479 (per_generator_V_hat_3A)       DEFAULT
    mass_at_3A_proper.py:675 (binding_3A_tower)             DEFAULT

`trace_convention_reconciliation.py` is the pointed one: a script whose job is
reconciling trace conventions, built on the weight scheme that its own
docstring says does not match the canonical Jones z.

**And it was already condemned.** `docs/audits/2026-05-11-plancherel-usage-audit.md`
line 245 marks `normalized_plancherel_weights_3A` **DEPRECATED**:

> "rescales d_q^2/[n]_q! to force sum = 1 — Marked DEPRECATED — patch around
> the non-normalised q-deformed weight. The fact that a renormalisation was
> needed is itself the witness that q-deformed != Plancherel."

Three months on it is still the default, still recommended by the live
deprecation warning, and still the scheme that puts V_hat at the Phi_q pole.

(The packaged copy `qou-mass/src/qou_mass/_internal/mass_at_3A_proper.py` is
NOT a diverged fork — it differs from `computations/` only by the
`_path_bridge` import line.)

# alpha vs E_0 — the repo's own taxonomy answers it

    alpha = m_e * 8G  = 3.744460 MeV
            m_e is CAL-1; 8G = Vol(L6a4) is an exact hyperbolic identity.
            DERIVED.

    E_0   = Q_beta(n) = 0.782333 MeV
            `pyhecke.constants.E_0_CALIBRATION_MEV = _Q_NEUTRON_MEV`, and
            binding_canonical.py:160 names it "free-neutron beta-decay
            Q-value, **CAL-3** calibration input".
            A DECLARED CALIBRATION.

So they are not two candidate values of one constant — they are a derived
scale and a fitted one. Under the repo's no-free-parameter discipline (there is
a `no_free_parameter_certificate.py` gate) the derived scale is the one a
prediction may use; E_0 is an acknowledged anchor, legitimate to calibrate
AGAINST but not to predict WITH.

That argues for **alpha**, which is also the choice that gives the best
deuteron measured so far (jones_wenzl + free-baseline + alpha = +37.7%, vs
-71.2% under E_0).

I am flagging rather than deciding: CAL-3 is an *acknowledged* input, and the
repo does use acknowledged anchors in places. Whether the binding channel is
one of them is the owner's call. But the two scales should not both be live in
the same table on different channels, which is the situation today.


---

# CAL-1/2/3: the corpus, and what binding_canonical.py gets wrong

## What the corpus says

`docs/precision-goals.md` states the triple explicitly, in the error
decomposition:

    sigma_total(O) = sigma_theory(O, N)  (+)  sigma_CAL(O)
                     |__ framework's own      |__ propagated experimental error
                         formula residual         of the CAL-1/2/3 inputs
                                                  (m_e, q0<-m_p, m_pi)

So **CAL-1 = m_e, CAL-2 = q0 <- m_p, CAL-3 = m_pi.**

And Q_beta is **scored as a prediction**, not consumed as an input.
`docs/precision-goals.md` L214:

    | Q_beta | prediction (CAL-3 cross-check) | 0.78 ppm | 7.8 ppb |
    | 1279 ppb (1.28 ppm) | misses ~164x (de-fitted; N=5 ladder was a fit) |

`docs/observable-sector-tracker.md` L64 is blunter still:

    | Q_beta | derived (CAL-1+2; **not** CAL-3 — CAL-3 is m_pi) | 1248 ppb |

## What binding_canonical.py says

It says both things, in the same file:

  - **L69** — correct: *"the 3 calibrations are CAL-1 m_e, CAL-2 D_beta,
    CAL-3 D_pi"*.
  - **L160** — wrong: *"Q_beta(n) = 0.78233341 MeV (free-neutron beta-decay
    Q-value, **CAL-3** per prop:three-calibration-inputs)"*.
  - **L519** — repeats the wrong one into the witness text: *"CAL-3
    calibration input"*.

Q_beta is not CAL-3. CAL-3 is m_pi. Q_beta is a framework OUTPUT carrying a
1248-1279 ppb residual that misses its 100x target by ~164x.

## The reconciliation

The file already contains its own answer, two paragraphs below the mislabel:

  - **Naming note (2026-05-17)**: *"This binding-scale parameter is the
    beta-decay Q-value Q_beta(n), **NOT** the canonical energy scale
    E_0 = m_e/(q_0(q_0-1)) ~ 4.186 MeV (a different quantity, ~5x larger).
    Earlier revisions misnamed this parameter `E_0`."*
  - **Witness text**: *"DIAGNOSTIC ONLY: predicted B values are 5-40x smaller
    than AME **because Q_beta is the wrong energy scale**."*

So `binding_canonical.py` knows Q_beta is the wrong scale, declares itself
diagnostic-only, and points at `canonical-mass-table-extended` as the real
pipeline. The only thing to fix in it is the CAL-3 label at L160/L519 — a
docstring and a witness string, no numerics.

**But `mass_at_3A_proper` repeats the exact naming error the note says was
fixed.** `pyhecke.constants.E_0_CALIBRATION_MEV = _Q_NEUTRON_MEV`, i.e. the
name `E_0` is bound to Q_beta — 0.782 MeV, not the canonical 4.186 MeV. Every
`binding_3A` / `binding_3A_tower` result is therefore scaled by a quantity the
codebase has already ruled the wrong one, under a name that says otherwise.

# The three scales, measured

    alpha  = m_e * 8G          = 3.744460 MeV   8G = Vol(Borromean), exact geometry
    E_0    = m_e/(q0*(q0-1))   = 4.185981 MeV   CANONICAL per binding_canonical
    Q_beta = beta-decay Q      = 0.782333 MeV   "the wrong energy scale"

    E_0/alpha = 1.1179   alpha/Q_beta = 4.7863   E_0/Q_beta = 5.3506
    (E_0/alpha is close to q0 = 1.10998 but NOT equal — 0.7% off, so it is not
     a q0 factor; do not read one in.)

Deuteron, jones_wenzl volumes + free-baseline (AME 2.22452):

         scale        B_MeV      err%
         alpha       3.0641     +37.7      <-- best
     E_0 canon       3.4254     +54.0
        Q_beta       0.6402     -71.2      <-- what the code uses today

All three are derived from CAL-1 (m_e) except Q_beta, which is a scored
prediction. Using Q_beta as the binding scale feeds a 1248-ppb framework
output back in as an input — circular, and it is also the worst fit.

**Recommendation: alpha or the canonical E_0; never Q_beta.** Choosing between
alpha and E_0 is a real physics question (Borromean volume scale vs the
q0-pole energy scale) and is the owner's. Q_beta is not a third option — it is
a mislabel with a ruling already against it.

# Resolving the channels in one table

`mass-table-comprehensive` publishes two binding columns side by side that
disagree on all three axes:

    column     trace convention    weights      scale       state after this branch
    B_sym      D (closed_form)     n/a          alpha       ok
    B_qCLT     C -> now D          H_3          alpha       convention fixed (qou-jm5i)

and the neighbouring pipelines add a third and fourth combination:

    binding_canonical             D             n/a         Q_beta   self-declared diagnostic
    mass_at_3A_proper             D (jones_wenzl only)  H_3A  Q_beta-as-"E_0"  mislabelled

The resolution is one rule per axis, and two of the three are already decided:

  1. **Convention** — D everywhere. Owner ruling 2026-08-09. This branch closed
     the last unregistered C site (qou-jm5i). DONE.
  2. **Scale** — one scale for every binding channel, and not Q_beta. OPEN,
     owner's call between alpha and E_0.
  3. **Weights** — H_3 is wrong for A > 1 but H_{3A} is unaffordable past
     A ~ 2 today (qou-2tuv). Until that is resolved, a table spanning A = 1..418
     must DECLARE the approximation rather than imply a prediction; this branch
     added that caveat.

Axis 2 is the one blocking, and it is one decision.

---

# THE SCALE DECISION — resolved on axiom grounds, not on fit

I previously recommended alpha because it fit best. That is the wrong
criterion and the framework says so explicitly (`markov_z`: *"NOT decided by
which value matches experiment"*). Read against the corpus, the question
dissolves: **alpha and E_0 are not two candidates for one slot.** They are
different scales with assigned roles, and the corpus assigns them.

## The admissibility rule (prop:three-calibration-inputs)

    O = O_hat(q_0) * m_e^a * m_pi^b ,   O_hat(q_0) in Z[q_0^{+-1/2}],  a+b in {0,1}

with exactly three external inputs: **CAL-1 m_e, CAL-2 q_0<-m_p (proxy
m_mu/m_e), CAL-3 m_pi**. Beyond these "no further empirical, fitting, or
numerological input is permitted".

That same prop names E_0 directly:

> "the derived hadronic energy scale **E_0 = m_e/(q_0(q_0-1))** and the CAL-2
> proxy **Q_beta** are m_e^1 . Q(q_0) expressions, **not independent factors**."

## Each candidate against the rule

**alpha — COMPLIANT, and it is the binding scale by name.**
`prop:binding-scale-catalan` states:

>  alpha_q = m_e x Vol_q(B_3)  **in Z[q^{1/2}, q^{-1/2}]**
>  ... "*The binding energy scale in the atomic mass formula* is the
>  archimedean evaluation of the algebraic binding scale."

So O_hat = Vol_q(B_3) = prod V_hat_i^{B_3}(q), a=1, b=0. **8G is not an input** —
it is what the admissible Z[q^{+-1/2}] expression EVALUATES to at the CAL-2 pin,
and its proof notes the equality Vol(B_3) = 8G is "a theorem of hyperbolic
geometry, not a canonical approximation", with **zero uncertainty**; all error
in alpha comes from m_e (CAL-1) at 3e-8.

Critically, `Vol_q(B_3) = prod V_hat_i` is the SAME per-generator object
`atom_per_generator_volumes` computes. The scale is not bolted on beside the
volumes — it is built from them.

**E_0 — COMPLIANT, but it is the HADRONIC scale, a different role.**
`three-calibration-inputs-context` gives it three framework-derived forms, all
CAL-1 + CAL-2:

    E_0^(N=0)  = m_e/(q_0(q_0-1))          ~ 4.186 MeV   single Planck-tick
    E_0^full   = E_0^(N=0)/(1-hbar_q^2)    ~ 4.228 MeV   tower-summed
    E_0^(cal)  = Q_beta(n)/|Delta(net)|    ~ 4.155 MeV   CAL-3 cross-check

**Q_beta — FORBIDDEN as a scale.** The same doc forbids "*A second hadronic
scale*", and states E_0 != Q_beta, differing "by the dimensionless factor
1/|Delta(net)| ~ 5.31". Measured here: E_0/Q_beta = **5.3506**. Q_beta is the
CAL-2 proxy and, per `precision-goals.md`, a SCORED PREDICTION carrying
1248-1279 ppb that misses its 100x target by ~164x. Using it as the binding
scale feeds a framework output back in as an input.

## The consumer is part of the same ruling

`binding-scale-catalan-proof` gives the canonical form:

>  m(Z, N) = M_free + **alpha . Phi_atom**,  Phi < 0 for bound nuclei

i.e. alpha scales the **Phi_q tower**, which is exactly the functional
`atom_per_generator_volumes`'s own docstring names
(m(W) = |prod V_i| + sum Phi_q(|V_i|) + z^2 sum Phi_q(|V_i V_j|)).
Production instead uses `sum ln|V|`, whose own name calls it a **proxy**.

So the table is wrong on TWO axes at once, and they interact.

## Measured — deuteron, AME 2.22452

              weights                   consumer    scale        B_MeV       err%
          jones_wenzl    Phi_q tower (canonical)    alpha       1.5545      -30.1   <-- FULLY ALIGNED
          jones_wenzl    Phi_q tower (canonical)      E_0       1.7378      -21.9
          jones_wenzl    Phi_q tower (canonical)   Q_beta       0.3248      -85.4
          jones_wenzl            log-sum (proxy)    alpha       3.0641      +37.7
           legacy H_3            log-sum (proxy)    alpha       4.0396      +81.6   <-- PRODUCTION
           legacy H_3    Phi_q tower (canonical)    alpha  102937.33   +4.6e6
normalized_plancherel    Phi_q tower (canonical)    alpha  10807718     +4.9e8

The full axiom-aligned stack moves the deuteron from **+81.6% to -30.1%** — a
2.7x reduction in |error|, from a change with no fitted content.

Note the tower only survives with `jones_wenzl` volumes; both legacy H_3 and
`normalized_plancherel` put V_hat at or past the Phi_q pole and it diverges.
The three axes are not independent — picking the canonical consumer FORCES the
convention-D weight scheme.

E_0 does score marginally better (-21.9%) than alpha (-30.1%). **That is not a
reason to prefer it**: the fit criterion is the one the framework rejects, and
alpha is the scale its own prop assigns to this formula. A 8% error difference
at one atom is far inside the H_3-vs-H_{3A} weight error still in the stack.

## RECOMMENDATION

**alpha**, on the strength of `prop:binding-scale-catalan`, for every binding
channel — and adopt the Phi_q tower with `jones_wenzl` weights alongside it,
because the prop's formula is `alpha . Phi`, not `alpha . log-sum`.

**Never Q_beta.** It is forbidden as a second hadronic scale, it is a scored
prediction rather than an input, and it is the worst fit of the three. Its
current use in `mass_at_3A_proper` (bound to the NAME `E_0`) is a mislabel with
a ruling already against it.

E_0 stays where the corpus puts it: the hadronic energy scale, not the binding
scale. If anyone wants it in the binding channel, that is a claim that
`prop:binding-scale-catalan` is wrong, and it should be argued as such rather
than settled by a residual.


---

# Item 3: the mpf path is now REAL, and A=3 is still out of reach

`QOU_H3A_MPF=1` builds the seminormal matrices at mpf end to end.
`BlockCache(float(Q0), float(HA_VAL))` — the line `f64_into_mpmath_audit` names
in its own prose — becomes `BlockCache(Q_MP, HA_MP)`, and the two downcasts
INSIDE `per_generator_V_hat_3A` that would have thrown the precision away again
(`V_hat = [0.0]*n_gens` and `tr = float(np.trace(M))`) are conditioned on the
same flag. Verified end to end:

    default        V_hat type float   [0.0077, 0.06534, -0.02411, 0.00253, 0.06979]
    QOU_H3A_MPF=1  V_hat type mpf     V_hat[1] = 0.0653438637921291467625642516848

The disk cache key gains an `_mpf` tag, because it is keyed on q to 10 dp and
an f64 build agrees with an mpf build to far more than that — without the tag,
flipping the flag would load the truncated .npz and report it as full
precision, which is the exact error the flag exists to remove.

**Default is unchanged and stays f64.** Turning it on moves every value this
module produces past digit ~16 for ~20 consumers; that is a migration, not a
flag flip.

## The measurement it was supposed to unblock — still blocked

    D    A=2  3A=6    0.40 s   completes
    T    A=3  3A=9    > 600 s  DID NOT COMPLETE
    4He  A=4  3A=12   not reached

So the A-dependence is **still unmeasured**, and `jones_wenzl` as the new
default did not change that. The cost is not the weight scheme and not the
matrix precision — it is that the braid word carries mpf in 19 of 35 steps
(since `efcaf79ed`), so `c*sigma + d*I` is an object-dtype array either way and
the matmul is Python-level at O(dim^3). At 3A=9 the largest partition has
dim=216 where 3A=6 tops out at 16.

**There is no cheap fix inside the NO-FLOAT64 directive.** The 642x is
inherent to mpf matrix products; the only way to remove it is to cast the braid
word down at the matrix boundary, which is the forbidden direction. The
options are therefore:

  (a) accept that H_{3A} is an A<=2 tool and stop describing the nine
      A-bounded callers as "migration candidates";
  (b) declare a float64 tier for this specific computation, the way the
      raw-float64 audit already honours `precision_tier='float64-integrator'`
      — a DECLARED f64 path is the sanctioned opposite of laundering;
  (c) replace the dense character sum with something that is not O(dim^3) in
      mpf — a real piece of work, not a flag.

(b) is the only one that makes the A-dependence measurable this week, and it is
an owner call because it means writing "this quantity is 16-digit" in a
framework whose directive is NO FLOAT64. The honest framing: the computation is
ALREADY float64 in the default path and merely pretends otherwise; (b) stops
the pretence, it does not lose precision that anyone currently has.


---

# RETRACTION: the jones_wenzl default was wrong, and so was the -30.1% result

An adversarial review of my own diff (four independent reviewers over the
change) produced a HIGH finding I then reproduced myself:

    scheme                  A=1        A=2        A=3     sum omega_lambda
    normalized_plancherel   1.0000     1.0000     1.0000
    jones_wenzl            -0.8230    +0.0547    -0.0009

`per_generator_V_hat_3A`'s own comment, three lines above the weight table,
says *"Weight table — normalized to Sigma = 1 for the Markov identity
tr_M(1) = 1"*. **`jones_wenzl` violates it outright**, and not by a rounding
margin — the weights very nearly cancel.

That destroys the reasoning I gave for the switch. `jones_wenzl` appeared to
fix the Phi_q pole (max|V_hat| 1.08837 -> 0.06979, `binding_3A_tower` 1e7 ->
0.331) **only because near-cancelling weights drive every V_hat toward zero**,
not because the volumes become right. A finite tower obtained that way is not a
correct tower.

## What this retracts

- The **default change is reverted**. `normalized_plancherel` is restored.
- The `pyhecke/atom.py` deprecation text no longer endorses `jones_wenzl`; it
  now states that NEITHER scheme is known-good, with the numbers for both.
- **The "-30.1%, fully axiom-aligned" deuteron is withdrawn.** Every row of
  that table which used `jones_wenzl` volumes — including the one I reported as
  the best canonical-form result — rests on weights that fail the Markov
  identity the whole construction is built on. The comparison was measuring a
  near-zero artefact.

## What SURVIVES

The scale analysis is untouched by this: `prop:binding-scale-catalan` assigns
alpha = m_e x Vol_q(B_3) to the binding slot, `three-calibration-inputs-context`
forbids Q_beta as a second hadronic scale, and none of that depended on the
weight scheme. **alpha remains the answer on axiom grounds.** What is withdrawn
is the claim that any measured stack currently realises it well.

The Phi_q-pole problem is also unchanged and still OPEN: `normalized_plancherel`
genuinely does put V_hat at 1.08837 against a cap of 1.087779, and
docs/audits/2026-05-11-plancherel-usage-audit.md marked it DEPRECATED in May.
**Both schemes are wrong for the tower.** That is the actual finding, and
choosing between them is not the fix — which is why the default is back where
it was rather than moved to the other broken option.

## Still to check from the same review (not yet verified by me)

- `pyhecke-h3-vs-h3a-impact-comparison.witness.json` is written by a bare
  `per_generator_V_hat_3A(Z, N)` call. With the default reverted this is moot,
  but it shows the blast radius of a default change here is wider than the two
  functions I checked.
- The comment I wrote called `jones_wenzl` "the Ocneanu weighting"; a reviewer
  reports the repo's own Ocneanu module derives different weights and documents
  this formula as a FAILED GUESS. If so, `ocneanu_weights_3A` is itself
  misnamed — worth its own item.
- The CAL-3 correction reached one call site; `build_cal_3_q_beta_witness.py`
  and two committed witnesses still assert `calibration_id = "CAL-3"` for
  Q_beta, and `binding-canonical.witness.json` still carries the old wording.


---

# Adversarial review of my own diff: 3 findings survived, 13 refuted

I ran four independent reviewers over this branch's diff with a refutation pass
before opening the PR. 16 findings, **13 refuted, 3 confirmed** — and one of the
three was a defect in my own fix that would have been actively misleading.

## CONFIRMED 1 (worst): the QOU_H3A_MPF flag was precision theatre

Reproduced myself:

    QOU_H3A_MPF=1
      mp.mp.prec       = 53      <- mpmath DEFAULT
      mp.mp.dps        = 15
      V_hat[1] type    = mpf
      mantissa bits    = 52
      exactly float64? = True    <- mpf-typed, float64-VALUED

The flag built `dtype=object` arrays of mpf, paid the full 642x object-matmul
cost, and returned values with a 52-bit mantissa that compare EQUAL to their own
float64 round-trip. It never called `set_compute_dps()`, so mpmath sat at its
default 53 bits throughout.

That is exactly the pattern `pyhecke.atom.reject_float64_q` exists to catch —
"an mpf whose VALUE is a float64's decimal expansion". Shipping it under a flag
named `QOU_H3A_MPF` would have been WORSE than not having the flag: it would
have let a reader believe the precision question was settled.

Fixed — `_q_pair()` now calls `set_compute_dps()` before constructing anything:

      mp.prec 236 (dps 70), mantissa 236 bits, exactly float64? False

Caught by review, **not by any gate** — including the two I added in this same
branch.

## CONFIRMED 2: scan_param_fill has false negatives

A verifier wrote an independent scope-aware AST reference asking the same
question and got **91 lines / 37 files** where my regexes get **64 / 33** — 27
lines the AST catches and the regexes miss (multi-line allocations, and other
forms). The detector is directionally right and validated on the bug it was
written for, but it is a regex approximation of an AST question and understates
the surface by ~30%. Recorded on the PR, not fixed here.

## CONFIRMED 3: the CAL-3 fix self-stales its own witness

`computations/binding-canonical.witness.json` is tracked, unchanged by this
branch, and still publishes "free-neutron beta-decay Q-value, CAL-3 calibration
input" — the exact wording the source edit corrects. And because `scriptHash` is
sha256(source)[:12], editing the docstring makes the committed witness stale
against its own producer.

**Not regenerated here, deliberately.** Regenerating moves more than the label:

    q0  1.1099785827513808...  (proton-pin)  ->  1.1099785955573347...  (canonical)
    tr_M_atom / tr_M_free move at the 8th digit; B_MeV changes

That is a q0-ANCHOR FLIP, environment-driven (this container's `pyhecke_native`
0.9.0 is pre-convention-D and fails its self-check, so every run takes the
pure-Python path). Committing it would smuggle an anchor change into a
labelling branch. The three audit self-outputs that the gate run touched
(`q0-anchor-consistency`, `mpf-import-time-dps`, `q0-value-drift`) were reverted
for the same reason — their substantive lines are that same flip, not counts
moved by anything here.

So the branch knowingly ships a source edit that stales one committed witness.
That is the lesser of the two errors and it is stated rather than hidden;
regeneration belongs with whoever adjudicates the anchor.

## The 13 refuted

Not listed individually, but they included the claim that the constants change
moved a value (it does not — the alias is identical), and several style
objections. Recording the count so nobody re-runs the same pass expecting a
different yield.


---

# Two of the three confirmed findings now closed — and I had one of them backwards

## binding-canonical.witness.json: regenerated, and my earlier revert was WRONG

The verifier proved this decisively and I under-reacted to it. It AST-extracted
the `set_description(...)` literal from both revisions and compared byte-for-byte
against the committed JSON:

    BASE literal == committed witness description : True
    HEAD literal == committed witness description : False

So the witness was in EXACT sync with its producer on main, and this branch is
what broke it. Confirmed by scriptHash: main's producer hashes to 55d683d8c551,
the value recorded in the witness; HEAD's hashes to 29e40a028c7e. The drift
checker moves 781 -> 782 self-stale, with `comm -13` yielding exactly one new
entry and nothing dropping out.

**I had originally refused to regenerate** on the grounds that it also flips q0
(proton-pin -> canonical) and that this was environment drift I should not
smuggle in. **That was wrong.** `q0_anchor_manifest.json` lists
`binding_canonical` under **`ideal_muon`**, while the committed witness carries
`q0Anchor: "proton"`. The producer auto-selects by script stem, so running it
yields the manifest-correct anchor. The committed witness was stale on the
ANCHOR as well as on the label; regenerating corrects both rather than
introducing anything.

Regenerated and committed:

    q0Anchor    proton -> muon          (matches manifest ideal_muon)
    scriptHash  55d683d8c551 -> 29e40a028c7e   (matches this branch's source)
    description "CAL-3 calibration input" -> "CAL-2 proxy — NOT CAL-3"
    q0          1.1099785827513808... -> 1.1099785955573347...
    tr_M_atom / tr_M_free move at the 8th digit — the anchor's doing, expected

### Gate gap this exposes

`q0_anchor_consistency_audit --strict` passes with **Q0_FLIP: 0** on both the
stale and the corrected witness. It checks INTERNAL consistency — does the
declared `q0Anchor` match the `q0Value` — and the stale witness was internally
consistent (declared proton, used proton). It does not check MANIFEST
CONFORMANCE, so a witness can sit on the wrong anchor indefinitely and the flip
detector stays green. Worth its own item; not fixed here.

## scan_param_fill: the undercount is now printed, not hidden

A verifier wrote an independent scope-aware AST reference asking the same
question over the same corpus and got **91 lines / 37 files** against my regexes'
**64 / 33** — 27 missed, chiefly multi-line allocations where `dtype=` or the
subscript target falls on a continuation line. Severity HIGH is fair: the whole
point of the tier is recall for a class the main scan cannot see, and a printed
count that reads as a total while missing 30% is worse than no count.

Not rewritten to AST here — that is a real change to a gate script and wants its
own review. The output now states the shortfall and instructs the reader to
treat the number as a FLOOR. Understating with a stated error bar is defensible;
understating silently was not.


---

# THE PAYOFF, MEASURED: correct weights are WORSE. The Phi_q tower is the problem.

The open question was whether a weight family that actually satisfies the Markov
identity would keep V_hat inside the Phi_q range — i.e. whether "both schemes
are wrong" had a third option. **It does not, and the answer inverts the
diagnosis.**

`ocneanu_weights.omega_lambda_via_inversion` is the correct construction: it
solves the p(n) x p(n) system Sigma_lambda (omega_lambda/d_lambda) chi_lambda(T_w)
= tr_M(T_w) against `markov_trace_canonical.tr_M_element`. Measured:

    n     p(n)    secs    sum omega
    3        3     3.4    1.000000000000    SUMS TO 1
    6       11     0.0    1.000000000000    SUMS TO 1
    9       30     2.0    1.000000000000    SUMS TO 1
   12       77    16.1    1.000000000000    SUMS TO 1

and on **convention D** — its z is 0.6126880371464652 = q^3/(q^2+1) exactly. So
a correct, affordable (n=12 in 16 s), convention-D weight family EXISTS.

Then the decisive table. `phi_q_safe` cap = 0.98*q0 = 1.087779:

    atom   weights        sum w    max|V_hat|   in range?     tower      B_MeV      err%
       D   inversion    1.00000      1.28242    NO — POLE   6.357e+07   4.09e+07  +1.8e9
       D   norm_planch  1.00000      1.08837    NO — POLE   3.190e+07   1.08e+07  +4.9e8
       D   jones_wenzl  0.05466      0.06979    yes             8.588     1.5545   -30.1

       T   inversion    1.00000      1.28242    NO — POLE   9.047e+07   8.17e+07  +9.6e8
       T   norm_planch  1.00000      1.08837    NO — POLE   5.850e+07   5.16e+07  +6.1e8
       T   jones_wenzl -0.00097      0.00123    yes            10.67      0.0360   -99.6

**The CORRECT weights are the worst offender.** max|V_hat| = 1.28242 against
`normalized_plancherel`'s 1.08837 — further past the pole, not closer to it.

## What this means

Every weight family that satisfies Sigma omega = 1 drives V_hat past the Phi_q
pole. The only scheme that keeps V_hat small is the one whose weights nearly
cancel — and its error grows with A exactly as an artefact should: the deuteron
lands at -30.1% and the triton at **-99.6%**, i.e. it is converging on zero
binding, not on the data.

So the defect is **not the weight scheme**. That was the wrong axis all along,
including in my own framing of it. Three candidate families, two correct and one
broken, and the tower diverges on both correct ones. The incompatibility is
between the Phi_q tower and Markov-normalised weights at this q0 and these A —
`phi_q_safe`'s cap is not regularising an edge case, it is masking that the
tower's own precondition (|V_hat| < q0) is violated by construction.

That reframes qou-2tuv's open item. It is not "pick a weight scheme"; it is one
of:
  (a) the Phi_q tower is the wrong consumer for these volumes;
  (b) V_hat's normalisation convention differs from what the tower expects by a
      factor nobody has pinned;
  (c) q0 is outside the tower's radius of convergence for A >= 2 and the
      construction needs a different expansion there.

None of those is a code fix, and none is mine to choose.

## Method note

Measured without editing the repo: the inner loop of `per_generator_V_hat_3A`
was replicated in a scratch script taking a supplied weight table, so all three
families were compared under identical code. 4He (3A=12) hit
`ValueError: setting an array element with a sequence` in that scratch
replication — the sparse-matrix path at dim > 500 — so A=4 is unmeasured. The
A=2 and A=3 rows are sufficient for the conclusion and it is the same at both.

The `jones_wenzl` trend from -30.1% (A=2) to -99.6% (A=3) is worth recording on
its own: last week that -30.1% was briefly reported as the best canonical-form
result. It is a near-zero artefact whose agreement degrades monotonically as A
grows.


---

# Both open threads closed

## 4He measured — the pattern holds, and max|V_hat| is A-INVARIANT

The A=4 row that failed on the sparse path (dim > 500 returns scipy-sparse;
`np.asarray` on that yields a 0-d object array) now runs, mirroring the repo's
own dense/sparse branch:

    atom   weights        sum w    max|V_hat|   in range?     B_MeV        err%
       D   inversion    1.00000      1.28242    NO — POLE   4.09e+07     +1.8e9
       D   norm_planch  1.00000      1.08837    NO — POLE   1.08e+07     +4.9e8
       D   jones_wenzl  0.05466      0.06979    yes           1.5545      -30.1
       T   inversion    1.00000      1.28242    NO — POLE   8.17e+07     +9.6e8
       T   norm_planch  1.00000      1.08837    NO — POLE   5.16e+07     +6.1e8
       T   jones_wenzl -0.00097      0.00123    yes           0.0360      -99.6
     4He   inversion    1.00000      1.28242    NO — POLE   1.23e+08     +4.3e8
     4He   norm_planch  1.00000      1.08837    NO — POLE   6.24e+07     +2.2e8
     4He   jones_wenzl  0.00001      0.00001    yes           0.0004     -100.0

Two things this adds beyond the A=2,3 result:

**1. max|V_hat| is IDENTICAL at A = 2, 3, 4** — 1.28242 for inversion, 1.08837
for normalized_plancherel, at every atom. The pole violation is A-invariant, so
it is structural, not an accident of a light atom or of a particular braid word.
Extrapolating to heavier A is not needed: the quantity does not move.

**2. The jones_wenzl artefact converges on zero**, monotonically:
-30.1% (A=2) -> -99.6% (A=3) -> **-100.0%** (A=4), with sum omega collapsing
0.0547 -> -0.0010 -> 0.00001. It is not a weight family degrading gracefully; it
is a cancellation going to zero as p(3A) grows. Whatever agreement it showed at
the deuteron was coincidence at the one atom where the cancellation had not yet
completed.

## Blast radius: the failed guess is dead code

Checked all three entry points across live (non-`_deprecated`) code:

  - `weight_scheme="jones_wenzl"` — **NO live caller passes it.** The only two
    explicit callers, `binding_via_interface_knot.py:213,216` and
    `delta_lambda_v_hat_z_transfer_phase5d_4.py:109,111`, both pass
    `normalized_plancherel`.
  - `omega_lambda_formula_guess` — genuinely reference-only, as its docstring
    claims. Only the two definitions (computations/ + the qou-mass copy) and the
    two docstring citations I added.
  - `jones_wenzl_weight` — reached only from `ocneanu_weights_3A`, which is
    reached only via `weight_scheme="jones_wenzl"`, which nothing passes.

**So no committed witness is built on the failed guess.** That is a relief and
it is also the direct consequence of reverting the default: had that change
shipped, every bare `per_generator_V_hat_3A(Z, N)` caller would have moved onto
it silently — including the `pyhecke-h3-vs-h3a-impact-comparison` producer the
earlier review flagged.

This retires that review finding as moot rather than unaddressed.

## Housekeeping

The `.cache/seminormal` and `.cache/ocneanu` .npz stores filled the container
disk during these runs (0 MB free at the end of the A=4 sweep). Cleared; 13 GB
back. Worth knowing before anyone repeats an inversion sweep: the caches are
keyed per (n, shape, q) and grow fast at n = 12.


---

# CORRECTION: normalized_plancherel never hit a pole — I tested against the guard band

The `in range?` column in the table above is **wrong for `norm_planch`**. It was
computed as `mx < CAP` with `CAP = 0.98 * q0` — the `phi_q_safe` **guard band**,
not the radius. The radius is `q0 = 1.109979`.

    max|V_hat| = 1.08837   vs   0.98*q0 = 1.087779   -> over the GUARD by 0.05%
    max|V_hat| = 1.08837   vs        q0 = 1.109979   -> INSIDE the RADIUS by 1.9%

Re-decided against the true radius, single **and** cross channel:

    atom       weights    max|V|     vs q0  #sing>q0  #sing>cap | max|ViVj|    vs q0  #cross>q0
       D     inversion   1.28242      OVER         2          2 |   1.14576     OVER          1
       D   norm_planch   1.08837    inside         0          1 |   0.70839   inside          0
       T     inversion   1.28242      OVER         3          3 |   1.14576     OVER          1
       T   norm_planch   1.08837    inside         0          2 |   0.70839   inside          0

**`normalized_plancherel` has no pole anywhere** — zero single-channel arguments
and zero cross-channel arguments exceed `q0`. The cross channel, which takes
*products* `|V_i·V_j|` and was the one place products could plausibly cross the
radius, tops out at 0.70839 — nowhere near. Only `inversion` genuinely exceeds
the radius (1.28242, over by 15.5%).

What actually happens to `norm_planch` is that 1–2 single terms land in the 2%
guard band and get **clamped** by `phi_q_safe` (which clips to ±0.98·q0 — it
never returns `inf` for these).

## The clamp accounts for none of the error

Re-running with the clamp effectively disabled:

    atom  cap_frac  #clamped   tower(atom)          B_MeV         err%
       D      0.98         1   3.18958e+07   10807718.0113   +4.858e+08
       D   0.99999         0   3.29906e+07   10807718.0113   +4.858e+08
       T      0.98         2   5.85012e+07   51579622.7693   +6.081e+08
       T   0.99999         0   6.06909e+07   53118549.4878   +6.263e+08
                                                AME D 2.2245 / T 8.4818

Zero terms clamped, every argument strictly inside the radius, and the tower is
still wrong by **~5x10^8 percent**. D's error does not move at all; T's moves 3%
relative inside an eight-order-of-magnitude discrepancy.

## What this settles

**The radius-of-convergence hypothesis is FALSIFIED.** It was one of the three I
left open. On the correct weights the Φ_q tower is finite, fully in-radius,
unclamped — and catastrophically wrong. Convergence is not the defect.

Two hypotheses remain, and both are about the tower's *meaning*, not its
arithmetic:
  - the Φ_q tower is the wrong consumer for V_hat, or
  - V_hat's normalisation differs from the one the tower expects.

The 8-order gap and the fact that it *grows* with A (4.9e8 -> 6.3e8 -> 2.2e8 at
D/T/4He on the clamped path) points at a per-generator scale factor, since the
generator count grows as 3A−1. That is a measurement I can make next.

## Precedent I walked into

`_li_2_q_util.py:157` already documents this exact failure mode, from bean
`qou-cw27`: *"`li_2_q` hard-returned `inf` for `|z| >= q`, and that GUARD — not
the function — is what made the atom-word brane tower 'diverge for Z >= 2'."*
Same trap, one guard over. Worth a standing rule: when a verdict says "pole",
print the argument, the radius, and the guard as three separate numbers.

## What still stands from the run above

Unaffected — these are measurements on raw V_hat, taken before any tower call:
  - max|V_hat| is A-invariant (1.28242 / 1.08837 at A = 2, 3, 4).
  - `inversion` genuinely exceeds the radius.
  - `jones_wenzl` collapses to zero (-30.1% -> -99.6% -> -100.0%) and is dead code.
  - The Φ_q tower is the defect, not the weight scheme — now on much firmer
    ground, since the surviving explanation cannot be convergence.

Cross-channel maxima were measured at A = 2, 3. At A = 4 the single-channel
conclusion follows from the already-measured max|V_hat| = 1.08837 < q0; the
cross maximum there was not re-measured.



---

## prepare-merge (2026-08-22)

Branch `claude/mass-table-comprehensive-triage` is merged-up, green and pushed
at `b42462c8e`. Base had moved **552 commits** — my earlier "0 behind" reading
was against a stale `origin/main`.

Two files overlapped; one conflicted. **`binding-canonical.witness.json`** — my
commit e429d73f had regenerated it to `q0Anchor: muon`, reasoning from
`q0_anchor_manifest.json`, which at my base listed `binding_canonical` under
`ideal_muon` (256 entries). Main has since migrated (`da2968cc3`, "first
witnesses at the proton pin"): the manifest now lists it under
`physical_proton` (406 entries; `ideal_muon` is down to 3). **My premise was
right at my base and is now superseded** — the muon flip is dropped.

Resolution is neither side verbatim: main's anchor decision **plus** this
branch's producer edit (CAL-3 -> CAL-2 proxy, which moves
`scriptHash 55d683d8c551 -> 29e40a028c7e`), reconciled by regenerating. Result
carries `q0Anchor: proton` + the new hash. Every numeric field is unchanged to
1e-11% or better; only `wall_sec` moves. Regeneration does restamp the
environment (mpmath 1.3.0 -> 1.4.1), and the 1.45e-11% drift on `B_MeV` traces
to that bump — recorded rather than hidden, since closing the scriptHash left no
way to avoid it.

**Gates:** `scripts/precision-gates.sh` exit 0, *"All blocking precision gates
green."* `probe-float64-guard.py --diff` exit 0 — and comparing main's copy of
`mass_at_3A_proper.py` against ours in-tree gives **16 hits each**, so this
branch adds none.

**Not mine, left alone:** running the gates refreshed
`q0-value-drift-audit.witness.json` by +2 `proton-pin` rows
(`gram-restricted-nonsingularity`, `axial-observable-is-the-gram-radical`
gaining `q0Value`). No row changed class and binding-canonical was already
`proton-pin` on both sides, so that is **main's audit witness being stale
against main's own tree**, not fallout from this branch. Reverted rather than
folded in — it belongs to the witness drain (qou-ad4t). Worth someone's
attention: it means the committed drift audit under-reports the proton-pin
count by 2.


---

# What Φ_q actually is — and why it cannot be this consumer

Continuing from the falsified radius hypothesis. I probed Φ_q's shape directly
rather than guessing, and it settles the remaining two hypotheses.

## Φ_q(x) = 1 + |x|/(q0 − 1) + O(x²)

    Phi(0) = 1.0        Phi(x) = Phi(-x)  at every x tested

    (Phi(x)-1)/|x| ->  9.09267974  (x = 1e-8)
         1/(q0 - 1)  =  9.09267946
                        agree to ~3e-8, the O(x^2) term's size at that x

One-sided slopes at 0 are +9.0926600 and −9.0926600. So Φ_q is **even with a
corner at the origin** — C⁰, not C¹. My earlier `Φ_q'(0) = 0` was a
central-difference artifact: the two one-sided slopes cancel. There is no linear
regime to sit in; the function is flat-to-first-order nowhere.

That also retires the linear model I tried on the way here. Calibrating
`B = C·(Σ V_free − Σ V_atom)` on D under-predicts T by **−44.8%** — far better
than 5×10⁸% but still not physics, and now visibly so: the premise (a linear
regime) does not exist.

## Three structural facts, each fatal on its own

**1. Φ_q is even, so the tower discards the sign of V̂.** This is the sharp one.
`binding_canonical.py` carries an explicit correction in its own docstring — the
binding difference is a *SIGNED* categorical difference, and "the double-modulus
form was a non-archimedean misuse". An even consumer throws away precisely the
sign that correction was about. Whatever Φ_q is for, it cannot be the consumer
of a quantity whose signedness was deliberately restored.

**2. Φ_q(0) = 1 and Φ_q ≥ 1 everywhere.** It is a multiplicative, normalising
object — it returns *unity* on the zero input, not zero. The tower feeds it into
`B = ALPHA·(tower_free − tower_atom)`, i.e. treats it as an additive energy. A
function whose neutral element is 1 does not belong in a difference.

**3. The scale mismatch is the whole eight orders.**

    Phi(0.0541)  =        1.65     <- max|V_hat| at the FITTED s* (D)
    Phi(0.0891)  =        2.29     <- same, T
    Phi(0.70839) =     3189.9      <- max cross-channel |V_i V_j|
    Phi(1.08837) = 26604768.9      <- max|V_hat| as V_hat ACTUALLY comes out

V̂'s natural scale lands where Φ_q is ~2.7×10⁷. The answer needs ~1. That gap
*is* the 5×10⁸% error — not an accumulation of small mistakes.

## Correcting the fitted-scale reading, and one earlier overstatement

Solving for s with V̂ → s·V̂ so the tower reproduces B_AME exactly (to ~1e-12):

    atom  A  #gen        s*     s*·#gen
       D  2     5  0.04973646  0.248682
       T  3     8  0.08186724  0.654938

A root exists at both — but s* is **not** constant (1.65× apart) and s*·#gen is
not either. So "normalisation mismatch" in the simple sense of one global factor
is **also insufficient**; no single rescale of V̂ works across A. What s* does do
is land the argument at 0.05–0.09, where Φ_q is order unity — which is the
diagnosis restated, not a fix.

**Overstatement to correct.** I called `inversion`'s 1.28242 a "real pole".
`phi_q_safe` never returns inf — it *saturates*:

    Phi(1.087779) = Phi(1.08837) = Phi(1.28242) = Phi(50.0) = 26604768.897416387

Everything at or past the 0.98·q0 guard returns one identical value. So the
failure mode is a **plateau, not a pole** — which is exactly why the tower
produced a large finite wrong number instead of raising. `inversion` does exceed
the radius (that stands); it just never manifests as a divergence.

## Where this leaves it

Of the three hypotheses I started with, the radius one is falsified and the
plain-normalisation one is now insufficient. **Φ_q is the wrong consumer for
V̂** — on evenness, on Φ(0)=1, and on scale, three independent grounds. The open
question is no longer "why does the tower diverge" (it does not diverge) but
"what is Φ_q's actual role, and what should consume V̂ instead". That is a
question about intent in the source, not a measurement — and it is where I would
want a human read before I go further.


---

# The consumer question is answered in the repo — and swapping it buys eight orders, but does not close it

`_li_2_q_util.py`'s module docstring states the rule outright:

> Li_2^q ... is **canonical for BINDING context** (B(K) = m_atom − Z·m_p − N·m_n,
> Δm_pn, isospin differences) because the bar-symmetric form kills the
> dimensional mass scale — exactly what is wanted when masses cancel in a
> difference.
>
> For MASS context (m_p, m_n, m_e, m_atom absolutes; m_p/m_e ratio) use
> `_phi_q_util.py` instead — its `phi_q` is the COMPACT quantum dilogarithm ...
> the bar-asymmetric archimedean / post-τ form that carries the dimensional mass
> scale.

    T2 = − Σ_i Li_2^q(−|V̂_i|)        T3 = − z²·Σ_{i<j} Li_2^q(−|V̂_i V̂_j|)

> — note the **minus signs** outside and the **negative argument** inside ... the
> alternating series converges far from any pole, **unlike the compact q-dilog
> phi_q which blows up near |z| = q**.

I have been computing **binding energy** — the binding context — through
`phi_q_safe`, the **mass-context** function. Every structural fact I measured
independently is in that paragraph. There is also a Lean-level guard:
`rewrite_2_20_21.py:573` records that `QOU.BraidKnot.QuantumDilogarithm` defines
`towerTerm q V := -li2_q q (-|V|)` and that a type class
`HasCorrectedMassEndomorphismTower` "ensures any instance must use `towerTerm`,
not `phi_q`. This prevents the Φ_q pathology from re-entering the mass formula."
**The Lean side forbids what the Python path does.**

## Swapping the consumer: 5×10⁸% -> ~10¹–10²%

    atom   A  #gen      phi_q      Li_2^q full   Li_2^q adjacent   B_AME
       D   2     5   +4.858e8%        +216.6%           +123.9%   2.2245
       T   3     8   +6.081e8%        +112.3%           +10.55%   8.4818
     4He   4    11   +2.2e8%           +19.36%          −51.02%  28.2957

Eight orders of magnitude, from one function swap. That part is unambiguous.

The `+Li_2^q(+|V̂|)` form returns **inf** on this input — max|V̂| = 1.08837 > 1
and the series needs |z| < 1. That is why the docstring insists on the negative
argument, which routes through `li_2_q_negative_continuation`.

## But my pairing choice was overfitting, and 4He says so

On D and T alone, `adjacent` (the prop's original |i−j| = 1 form, which has the
independent merit of being the documented one) looked like the winner: +123.9%
and **+10.55%**. I flagged at the time that picking among 8 configurations on 2
data points risks selection bias. It did.

**4He is the out-of-sample point and it falsifies the choice.** `adjacent` gives
**−51.02%** there while `full` gives **+19.36%** — and `full` was the loser at T
(+112.3% vs +10.55%). Neither pairing is consistent across the three:

    adjacent:  +123.9%,  +10.55%,  −51.02%   <- sign flips
    full:      +216.6%, +112.3%,   +19.36%   <- monotone, converging with A

So the T = +10.55% that looked like a hit is **not** evidence of a correct
model; it is one point of a curve that crosses zero between T and 4He.

## Where this leaves it

**Necessary, not sufficient.** Φ_q is definitively the wrong consumer — the
repo's own docs, its Lean guard, and an eight-order improvement all agree. But
Li_2^q with either pairing still misses by −51% to +217%, so the consumer swap
alone does not produce the binding energies. Something else is also wrong:
candidates are the weight scheme feeding V̂, the free-nucleon reference the
difference is taken against, the z² marking factor, or the energy scale (ALPHA
≈ 3.7445 vs E_0 ≈ 4.1860 — I tested both; E_0 is uniformly worse).

Worth noting `full`'s errors shrink monotonically with A (+217, +112, +19).
If that continues past A = 4 it points at a small-A / few-generator defect
rather than a structural one — testable at ⁶Li, and the first thing I would
measure next.

**Nothing here touches production code.** These are probes; `mass_at_3A_proper.py`
still calls `phi_q_safe`, and whether that is a live defect depends on whether
its callers are in binding or mass context — which I have not audited.

## Container note

The seminormal/Ocneanu cache is created **relative to the importing module's
directory**. Adding `qou-mass/src/qou_mass/_internal` to `sys.path` put 13 GB in
`_internal/.cache` rather than `computations/.cache`, and filled the disk at the
A = 4 sweep a second time. Clear both paths, not just the one you remember.


---

# Consumer audit: three live `binding_*` functions use the mass-context Φ_q

Per `_li_2_q_util.py`'s rule (binding -> Li_2^q, mass -> phi_q), I traced every
caller of the Φ_q tower and classified it by what it returns.

**Correct — mass context, phi_q is right:**

- `canonical_tower.py:453 calibrate_E0_tower` — runs the tower on a *free
  proton* and calibrates E_0 against 938.272 MeV. An absolute mass. phi_q is the
  documented choice here.

**Wrong — binding context, returns `B_MeV` through phi_q:**

- `canonical_tower.py:477 binding_per_irrep_tower` -> `B = E_0*(m_free_total −
  m_atom_total)`, returned as `"B_MeV"` (line 516/522)
- `canonical_tower.py:545 binding_canonical_tower` -> `B = E_0*(m_f["total"] −
  m_a["total"])`, returned as `"B_MeV"` (line 569/574)
- `mass_at_3A_proper.py:771 binding_3A_tower` -> `"B_MeV": E_0*(total_f −
  total_a)` (line 825)

All three are named `binding_*`, all three return `B_MeV`, and all three route
through `canonical_tower_mass` / `mass_from_tower_safe`, which call
`phi_q_safe`. So the misuse I hit in my probe is **not confined to my probe** —
it is what these functions do. It also contradicts the Lean guard
(`HasCorrectedMassEndomorphismTower`, which exists specifically to keep phi_q
out of the mass formula).

I am **not** patching them. The consumer swap is necessary but demonstrably not
sufficient (Li_2^q still misses by −51%..+217%), so switching them now would
trade a wrong answer for a differently wrong answer while looking like a fix.
This wants a decision from whoever owns the tower.

**Lower severity, deprecated path:** `mass_at_3A_proper.py:829 binding_3A` still
computes `B = E_0*(|tr_free| − |tr_atom|)` — the double-modulus form that
`derive_binding_chain_cooperative.py:12` and `binding_canonical.py:158` both
document as "a non-archimedean misuse" and have already corrected. It carries a
`[DEPRECATED]` marker, so it is on a dead path. It also has a **stray second
docstring**: the deprecation notice was prepended without removing the original,
leaving the old `B = E_0 · ( |tr_M(W_free)| − |tr_M(W_atom)| )` text as a no-op
expression statement at line 841.

# A defect in my own branch, found and fixed

`qou-mass/src/qou_mass/_internal/` is **generated** by
`scripts/sync-qou-mass-vendor.py`, whose own header says the copies are
generated "and `--check` makes a drifted copy a test failure rather than a
discovery three months later".

My commit a3fc90dd3 edited `computations/mass_at_3A_proper.py` (adding the
`QOU_H3A_MPF` path) without re-running the sync. Measured:

    drift between the two copies on origin/main :  2 lines
    drift on my branch before this fix          : 80 lines
    QOU_H3A_MPF refs: computations/ = 4,  vendored = 0

Ran `--apply` and reverted the two witness files it also touched, because
`--check` on origin/main reports those same two as already drifted — they are
main's, not mine. Drift is back to main's 2-line baseline and `QOU_H3A_MPF` is
now 4/4 in both copies.

## Why prepare-merge missed it

I ran `scripts/precision-gates.sh` and it was green. The vendor-mirror check is
wired into a **different** suite — `scripts/staleness-gates.sh:72` — which I did
not run. Two separate gate arrays, and the repo's own warning ("A GATE OUTSIDE
THIS ARRAY IS A GATE NOBODY RUNS") applies across them as well as within them.
`staleness-gates.sh` exits 1 on my branch, but on pre-existing reds: the vendor
mirror (main's 2 witnesses, confirmed by running `--check` at origin/main) and
scriptHash/upstream drift (the 744 self-stale witnesses already recorded above).

**For future prepare-merge on this repo: run both gate suites, not just
`precision-gates.sh`.**

# Correction: ⁶Li is not the next test

I proposed ⁶Li as the out-of-sample point. It is not reachable, though not for
the reason the bean title suggests — "infeasible past A~12" is about A, and
p(18) = 385 is small. The real limit is the seminormal cache, whose size tracks
the dim-sum n! : n = 12 (⁴He) produced 13 GB here, and n = 18 is 18!/12! ~ 10⁷
times larger. So A = 4 is the last atom this measurement reaches, and the
monotone `full` trend (+217, +112, +19) cannot be extended to a fourth point by
this route.


---

# Swapped the production tower to the Lean-mandated term

Decision from the user: **if Lean proves it, swap — even if the numbers do not
improve.** That rule is right and my earlier reasoning for deferring was not.
Using a function the formal development proves is the wrong one is a defect
whatever number falls out; keeping it because its wrongness happens to be
differently sized is how a real error stays hidden.

## What Lean actually proves (stated exactly, not overstated)

`QOU/BraidKnot/QuantumDilogarithm.lean`, **no `sorry`** anywhere:

- `phi_q_ne_li2_q` refutes the historical identity claim
  `Phi_q(z) = -Li_2^q(-z)` by counter-example at z = 0 — Phi_q is the empty
  PRODUCT (1), the other is the empty SUM (0), and 1 != 0.
- `towerTerm q V := -li2_q q (-|V|)` is the corrected per-generator term.
- class `HasCorrectedMassEndomorphismTower` documents the discipline: a consumer
  "should assert `f = towerTerm`, not `f = phi_q`. The latter is the historical
  pathological form preserved only as a diagnostic."

What it does **not** prove: that this makes the physics right. The field
`saddle_phi_q_eq_towerTerm` is labelled conjectural and open in that same file.
Two axioms (`phi_q_residual`, `li2_q_residual`) stand in for everything past the
leading term, so the proved statement is about leading behaviour — and is
genuinely proved.

## The change

- New `tower_term_li2q` in `mass_at_3A_proper.py` implementing `-Li_2^q(-|V|)`.
- `mass_from_tower_safe`, `canonical_tower_mass`, `binding_3A_tower`,
  `binding_per_irrep_tower`, `binding_canonical_tower` take `term=`, defaulting
  to **`"tower_term"`**.
- The two energy-scale calibrations pin `term="phi_q"` explicitly, with comments:
  they compute the proton ABSOLUTE mass against 938.272 MeV / `M_P_MEV`, the mass
  context where Phi_q is the documented correct choice per `_li_2_q_util`. Note
  `_calibrate_E0_per_irrep` reaches that through `binding_per_irrep_tower`, so the
  argument is threaded rather than left to change silently.

## Measured

    atom   term          B_MeV          B_AME       err
       D   tower_term    1.80422       2.2245     -18.9%
       D   phi_q         1.00718e+07   2.2245     +4.5276e+08%

Deuterium lands at **−18.9%**, far better than my standalone probe suggested
(+124% to +217%) — because the production path carries its own calibration
(E_0 = Q_beta = 0.78233341 MeV, not the 3.7445 MeV my probe used), its own
weight scheme, and the `desc` term. The `phi_q` opt-in still reproduces the
historical wrong number exactly, so the diagnostic path is intact.

Tritium was still computing on a cold cache when this was committed.

## Gates

`precision-gates.sh` exit 0, "All blocking precision gates green".
`sync-qou-mass-vendor.py --check` back to main's 2 pre-existing witness drifts.
`probe-float64-guard.py` — **21 hits on main's copies of these two files and 21
on mine**, so the swap adds none; the one new `float()` carries a `float64-ok:`
annotation, which the guard honours.

## Still open, and now visible as itself

The remaining error is real and unexplained. It is no longer buried under a
function that was wrong by eight orders of magnitude, which is the point of
making the swap independent of whether it helped.


---

# Removed my float64 downcast — and it was hiding a real 1e-10 error

The user does not want float64 in this path. My `tower_term_li2q` had a
`float(...)` downcast on its return, carrying a `# float64-ok:` annotation I
wrote myself. Both are now gone.

## Why my annotation was the wrong kind of exception

There are 15 `float64-ok` markers in the tree. Every pre-existing one sits at an
**output boundary**, where a value stops being a computation and becomes text or
JSON:

    option_e_multi_isotope_delta_lambda_probe_v3.py:217  "written to the witness as a JSON number"
    option_e_multi_isotope_delta_lambda_probe_v3.py:221  "JSON number, 2-dp threshold"
    option_e_multi_isotope_delta_lambda_probe_v3.py:246  "console formatting only"

That is a coherent rule: once a number is being printed or serialised, binary64
is the format, and the loss is visible at the boundary where it happens.

**Mine was not at a boundary.** It was the return value of a compute function
whose output flows straight into the tower sums. That is precisely the case the
guard exists to catch — a downcast in the middle of a pipeline, where the loss is
invisible and every downstream term inherits it. My stated reason ("tower
arithmetic is float64 throughout this module") was an argument for matching the
surrounding damage, not a justification.

## The downcast was hiding a second, larger defect

`li_2_q` sets its own series truncation from the ambient precision:
`eps = mpf(10) ** (5 - mp.dps)`. At mpmath's default `mp.dps = 15` that stops
the series at **1e-10**. So the term was not merely being rounded to float64 on
the way out — it was only ever computed to ten digits on the way in.

    dps = 15 (before) : 0.4486225372 8787743201
    dps >= 60 (after) : 0.4486225372 5803283172 35470461371304082152
                                    ^ diverges at the 11th digit

Fixed by wrapping the body in this module's own established idiom, copied from
`_q_h_at_precision` at line 392:

    with _mp.workdps(max(_mp.mp.dps, 60)):

The `q` load had to move inside that block too, for the reason that function
already documents: an mpf keeps the precision it was CREATED at, so loading a
50-digit q under `dps = 15` bakes in a 15-digit q and silently undoes everything
downstream. The cache is now keyed by dps so it cannot serve a low-precision q to
a high-precision caller.

`mpf(v_abs)` on a Python float is exact — it takes the binary64 value verbatim,
with no decimal round-trip — so nothing is lost converting in.

## Verified

    probe-float64-guard : 21 hits on main's copies of these two files, 21 on mine
                          -> this change adds none
    float64-ok markers I own : 0
    f64_into_mpmath_audit    : mass_at_3A_proper is not flagged
    precision-gates.sh       : exit 0, all blocking gates green
    D binding                : 1.8042217338504000779 MeV, -18.893886% (unmoved)

## What is still float64, honestly

The **inputs** are. `per_generator_V_hat_3A` hands the tower float64 volumes, and
`E_0` is a Python float, so the final `B_MeV` still equals its own float64
round-trip even though the term no longer does. That residue is the documented
`QOU_H3A_MPF` territory — the module's own note says flipping it "changes every
value this module produces beyond digit ~16 and costs the full 642x", which is
not a change to make silently on behalf of ~20 consumers.

So: no float64 downcast in the code I wrote, and the term itself is now correct
to 60 digits rather than 10. The remaining float64 is upstream, pre-existing, and
flagged rather than papered over.



---

# Un-hardcoded the precision, and scanned for the dps=15 hazard

## My `60` was wrong twice

```python
with _mp.workdps(max(_mp.mp.dps, 60)):        # before
with _mp.workdps(max(_mp.mp.dps, COMPUTE_DPS)):  # after
```

Not just hardcoded — **the wrong number**. `qou_substrate.precision` defines the
convention as *COMPUTE at OUTPUT_DPS + GUARD, SERIALIZE at OUTPUT_DPS*, with
`OUTPUT_DPS_DEFAULT = 60`, `PRECISION_GUARD_DEFAULT = 10`, and
`COMPUTE_DPS_DEFAULT = 70`. I had picked the **serialization** precision for a
**compute** context, so I was running 10 digits under the guard. Now imports
`COMPUTE_DPS` from `_precision`, which is env-overridable via
`QOU_COMPUTE_DPS` and resolves to 70.

**Rust needs no separate constant.** The crates take `prec: u32` and `dps` as
call parameters (`tl_cable_mpfr.rs:305` `new(q_dec: &str, prec: u32)`,
`jp(&self, word, q_dec, prec)`), so the Python constant is already the single
source of truth — the fix is for callers to pass `COMPUTE_DPS` rather than a
literal, not to mirror a value into Rust.

## The dps=15 scan — already gated, and my number was worse

I scanned for entry points building mpf without ever raising dps and reported 23.
**The repo already has a blocking ratchet for this**, wired into
`precision-gates.sh:60`, and it is green:

    runnable producers never raising dps : 10
    baseline files / constructions       : 46 / 206
    drained since baseline               : 36 file(s), +164
    NEW (not baselined)                  : 0
    REGRESSED                            : 0

The audit's 10 is authoritative — it *runs* the producers, where my scan matched
text — so my 23 was false-positive inflated. There are three such ratchets
(`import-time dps`, `never-raises-dps`, `float64-padding`), all blocking, plus
`module_const_precision_audit.py` whose docstring opens *"Owner directive: NO
FLOAT64."* This ground is covered and actively draining; I re-derived it.

## What the scan did find that is NOT gated

952 sites set precision **below** the canonical `OUTPUT_DPS = 60` — 610 at
dps=50, 213 at 40, 92 at 30 — against 447 at or above, with only 145 files
importing the constants at all. The 50s look like leftovers from before the
2026-05-31 bump (50→60 / 65→70, PR #1595) that never followed.

That is a different defect from never-raises-dps: these DO raise dps, to a value
that stopped being canonical, so no existing ratchet sees them. Filed as
**qou-zo4i** rather than bulk-edited — raising precision changes every value those
producers emit, and whether the 50s are deliberate is an owner call.

## Verified

`precision-gates.sh` exit 0, all blocking green (so all three dps ratchets pass
with this change). Vendored copy re-synced and carries `COMPUTE_DPS`;
`import qou_mass` works. Term now
`0.448622537258032831723547046137130408215229049`, carrying digits beyond
float64.
