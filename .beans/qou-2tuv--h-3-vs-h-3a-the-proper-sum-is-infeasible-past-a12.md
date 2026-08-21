---
# qou-2tuv
title: 'H_3 vs H_{3A}: the proper sum is infeasible past A~12, so substitution cannot fix the heavy-atom rows'
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T11:25:45Z
updated_at: 2026-08-21T16:38:44Z
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
