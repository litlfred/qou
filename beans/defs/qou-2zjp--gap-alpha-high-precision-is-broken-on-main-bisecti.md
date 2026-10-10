---
# qou-2zjp
title: 'GAP: alpha_high_precision is broken on main — bisection bracket no longer contains a root'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T14:53:43Z
updated_at: 2026-10-04T15:19:43Z
parent: qou-3l2l
---

## What happens

    $ QOU_Q0_ANCHOR=proton python3 computations/alpha/alpha_high_precision.py
    HIGH-PRECISION alpha* DETERMINATION (dps=50)
      q_0 = 1.1099785827513808
      M_p = 938.27208943,  M_n = 939.56542179
      Bracket: err(0.3) = +1.074673%, err(0.32) = +0.649810%
      ERROR: no sign change in bracket
    (exit 1)

The mpmath bisection is hardcoded to the bracket [0.3, 0.32]. Both endpoints
now give a POSITIVE error, so there is no root inside it and the script exits
before writing anything.

## Not caused by the q0 migration

It fails identically at BOTH anchors -- the decomposition harness records
`FAIL(m=1,p=1)`, i.e. the muon leg (its own declared anchor, the state on
main) fails too. So this is pre-existing breakage on main, surfaced by the
migration sweep rather than introduced by it. Its witness cannot be migrated
until the producer runs at all.

## Why it looked silent

It reports the error on STDOUT, not stderr, so a harness capturing only stderr
records rc=1 with an empty message. Worth knowing for any other sweep.

## Next honest step

Someone who knows what alpha* is supposed to be needs to decide whether the
bracket is stale (widen/re-derive it) or whether the root genuinely left the
interval because an upstream constant moved -- in which case the interesting
question is which one, and the committed witness is asserting a value the
current code can no longer reproduce. Do NOT just widen the bracket until it
finds something; that would fit a number rather than derive it.


## DIAGNOSED 2026-08-24 — not a stale bracket. The root MOVED, and convention C→D is why.

The original entry said "someone needs to decide whether the bracket is stale
or the root left the interval". It is the second, and the cause is identifiable.

**The root exists and is well-defined.** `err_n_mp(alpha)` is smooth and
monotonically decreasing; scanning alpha in exact 1/50 steps puts the zero
between 0.34 and 0.36. Bisected: **alpha* = 0.35088642931861095442**.

**The committed witness says alpha_star = 0.3058074307438076264762** — which is
INSIDE the old bracket [0.30, 0.32]. So the bracket was correct when written.
The root has since moved **+14.741 %**.

**It is NOT the q0 anchor.** Measured at both:

    manifest-resolved   alpha* = 0.35088642931861095442
    forced MUON         alpha* = 0.35088642931861095442
    forced PROTON       alpha* = 0.35088641146608020901

The two anchors differ in the 8th decimal — that is the 11.54 ppb separation.
The 14.741 % shift is anchor-independent, so the q0 migration neither caused
nor can fix it.

**It is NOT the producer.** `alpha_high_precision.py` has ZERO commits since the
witness was last regenerated (2026-06-22). Byte-identical source, headline
result moved 14.7 %: textbook import-cone drift.

**It is convention C→D.** The only `hecke_core` commit in the window is
`6086572c4e` (2026-08-15), the owner-approved convention migration, whose own
message records:

    z   0.4993203341836945 -> 0.6126880371464652   (C -> D, +22.70 %)

z feeds the Hecke traces, which feed `V_blend`/`tower`, which is what the
bisection roots. **So the committed alpha* = 0.30580743 is a CONVENTION-C
VALUE**, and the "broken bracket" is a symptom: [0.30, 0.32] brackets the
C-frame root, not the D-frame one.

## What to do, and what NOT to do

Re-centring the bracket on the D-frame root is legitimate and is NOT fitting —
the root is a well-defined zero of a monotone function and its location is
measured above, not chosen to hit a target. But do **not** just widen it and
regenerate: that would silently replace a published alpha* with a value 14.7 %
away under a different convention, with nothing in the witness saying so. The
regenerated witness must record that it is D-frame.

This is the same class as the AGENTS.md standing note that the Q_beta c_k ladder
is C-frame throughout and needs re-derivation under D (bean `qou-cds1`).
alpha* is another C-frame quantity that nobody had flagged.

## Scope: alpha* is probably not alone

112 producers import `hecke_core`. **30 of their witnesses were computed before
2026-08-15** and so may carry C-frame values. That is an UPPER BOUND, not a
count — importing `hecke_core` does not prove the value depends on z, and
`computedAt` is a proxy for the code version rather than proof of it. alpha* is
the one confirmed instance, measured at 14.741 %. Worth converting the bound
into a real number before anyone regenerates in bulk.


## CORRECTION to the scope figure above: 9 candidates, not 30

The section above reported "30 witnesses predate 2026-08-15" as the upper
bound. That number counted **any** `hecke_core` importer, which is exactly the
over-count it warned about. Re-measured against the z-dependent symbols only:

`hecke_core` re-exports `pyhecke.gram`, where `z = q0**3 / (q0**2 + 1)`
(gram.py:199, convention D). The symbols whose value moves with z are
`z, TR_M, W_SYM, W_STD, W_ALT, NF_BASIS, hm, hm_exact, nf_tr, nf_net,
G, G_PINV, G_INV, RADICAL, INV_TREFOIL_G0/G1, _H_FRAC, _Z_FRAC, _TR_M_FRAC,
_SYM_EIG_FRAC, _ALT_EIG_FRAC`. Everything else `hecke_core` exports (braid
chains, partition helpers) does not.

    importers of hecke_core                       112
    of those, importing a z-DEPENDENT symbol       41
    of those, witness computed before 2026-08-15    9

The nine:

    2026-04-17  toffoli-lp-stability
    2026-05-03  brane_tower_two_avenues_probe
    2026-05-19  paper_six_term_isotope_sweep
    2026-05-19  qbeta_decay_sdp_solver
    2026-06-09  h2o_bond_angle_magnitude_vsepr
    2026-06-12  wedderburn_pair_volumes
    2026-06-17  hadron_knot_table
    2026-06-22  alpha_high_precision          <- the confirmed 14.741 % case
    2026-07-11  qbeta_c3_barodd_binding_sdp_dual_probe

**These are CANDIDATES, not confirmed.** Importing a z-dependent symbol proves
the dependency exists; it does not prove the recorded number moved. Deciding
that needs a re-run per producer, which is real compute and its own tranche.

The causal chain on alpha* is now closed rather than inferred: it imports
`z as Z_MARKOV` from hecke_core directly (alpha_high_precision.py:43-44), so it
consumes the very parameter that moved 0.4993 -> 0.6127 (+22.70 %).

Note `hadron_knot_table` appears here AND in the qou-1c4y keep-on-muon /
timeout set -- it is slow (>240 s per leg) and z-dependent, so whoever re-runs
it for one reason should record both.


## Candidates converted to measurement, 2026-08-24

The nine were listed as candidates on the reasoning that importing a
z-dependent symbol proves a dependency, not that the number moved. Re-ran seven
(alpha_high_precision already measured; hadron_knot_table is >240 s per leg and
deferred), comparing each witness against HEAD with ephemeral meta masked. Tree
restored after every run.

    toffoli-lp-stability                    MOVED
    brane_tower_two_avenues_probe           MOVED
    h2o_bond_angle_magnitude_vsepr          MOVED
    qbeta_c3_barodd_binding_sdp_dual_probe  MOVED
    qbeta_decay_sdp_solver                  UNCHANGED  <- false positive
    paper_six_term_isotope_sweep            TIMEOUT >420 s
    wedderburn_pair_volumes                 rc=1, broken (see below)

**4 of 6 runnable moved; 1 was a false positive.** That is the caution paying
off: `qbeta_decay_sdp_solver` imports a z-dependent symbol AND its witness
predates the C->D commit, yet re-running reproduces it exactly. The import is
real; the dependence of the recorded numbers on z is not. A bulk regeneration
keyed on the import test alone would have rewritten it for nothing.

**What MOVED does and does not establish.** It establishes that the committed
payload no longer matches what the current code produces. It does NOT attribute
the movement to convention C->D. That attribution was earned for alpha* by
isolating it -- measured at both anchors, producer source byte-identical since
its witness, and a direct `z as Z_MARKOV` import. The other four have not had
that isolation done: they are confirmed STALE, not yet confirmed C-frame.

## A second producer broken on main

`wedderburn_pair_volumes` exits 1 before writing anything:

    File "computations/wedderburn_pair_volumes.py", line 228
      print(f"    ({p['i']}, {p['j']}): sym={p['sym']:.4f}  std={p['std']:.4f}  "
    TypeError: unsupported format string passed to mpf.__format__

An `mpf` reached an f-string `:.4f`. Unrelated to the anchor and to C->D: it is
the NO-FLOAT64 migration meeting a display path -- the value correctly became
`mpf` and the formatter was never updated. `mp.nstr(x, 5)` is the fix, per the
AGENTS.md rule that `float(x)` is permitted only inside an f-string for display
and `mp.nstr` is preferred.

Two producers are now known broken on `main` and surfaced by this work
(`alpha_high_precision`, `wedderburn_pair_volumes`); neither was caused by it.


## GATE CHECKED 2026-08-24 — NOT LEAN PROVED. Bracket left alone.

The owner conditioned re-centring on Lean backing ("if qou-2zjp is lean proved
then go"). I searched for it. **There is none**, so nothing was re-centred and
no witness was regenerated.

Full search + evidence:
[`docs/audits/2026-08-24-alpha-star-lean-backing-search.md`](../docs/audits/2026-08-24-alpha-star-lean-backing-search.md).
Summary:

**Searched** — all five corpus-grep paths (`content/**/lean/`, `docs/audits/`,
`content/`, `computations/`, `docs/coordination/`, `library/INDEX.md`) for
`alpha_star` / `alphaStar` / `alpha_blend` / `blend` / `err_n` / `bisect` /
`IntermediateValue` / `StrictMono` / `StrictAnti`, plus `lean_local_search` over
the built QOU library. **No `alphaStar` and no `blend` declaration exists.**

**The near-miss, and why it fails.** `thm:frobenius-antipode-unifies-chirality-
and-tower` is a theorem block tagged `alpha-blend` whose remark says the blend
"yields a sub-ppm match at the precise optimal mixing value". Its Lean,
`QOU.BraidKnot.frobenius_antipode_unifies`, is genuinely sorry-free
(`lean_verify` -> axioms `[propext]`). But its statement is

    (∀ i, S (σ i) = (σ i)⁻¹) ∧ (∀ a b, S (a*b) = S b * S a)   with S := (·)⁻¹

on any `Group G` — `rfl` and `mul_inv_rev`. **α does not occur in the file.**
Textbook AGENTS.md "grep the claim SHAPE, not only the topic": the topic has
Lean, the proposition is a generic group fact. It establishes none of existence
of a root of `err_n`, uniqueness, monotonicity, or the value.

Two other near-misses fail the same way: `s_symmetric_ansatz_misses_chirality`
is about a blend but in the 2-element toy type `SEigenvalue` and proves the
blend **cannot** capture chirality (a negative); `frobenius-antipode-lean-stub.
lean` carries `axiom markov_trace_antipode_invariant` (an axiom is not a proof)
and an `antipodeSymmetrize` that is an admitted placeholder returning
`antipodeS n q x` rather than `(x + S x)/2`.

**The corpus argues the opposite, which is the load-bearing part.** This is not
"the proof is elsewhere":

- `docs/alpha-blend-derivation.md` §5 — PSLQ at 25 digits over
  `{1, G, π, 1/π, q₀, h_q}`, `maxcoeff = 1e6`, **no relation**; explicitly
  falsifies `α* = G/3`. Concludes the 2-term blend is "**not a fundamental
  decomposition**".
- `docs/canonicalization-review.md` §3 — α* is **row 1 of seven
  empirical/fitted constants**; §3.1: "There is no closed form for α* in the
  2-term frame because the quantity it patches is structurally outside that
  frame." The plan is to **eliminate α***, not re-derive it.
- `docs/agent-briefs/lambda_scale.md:552` — "numerical root-find", target
  "closed form in q₀" — open.

So α* is a fitted mixing parameter with a documented plan to be removed.

**Symbol collision worth knowing** — 2 of the 6 corpus hits for "α*" are a
different α: `α* = 0.89` is an SDP feasibility fraction
(`2026-05-24-post-1089-followups-ledger.md:57`), and α/α_EM/`alpha_bind :=
m_e·8·catalan_G` are three more. Attributes do not transfer.

**Scope, per the refutation rule: this is scope-(a)** — no such declaration
exists in the corpus today, NOT that none could. What would satisfy the gate: a
declaration whose *statement* mentions the blend parameter — existence +
uniqueness of a zero of `err_n` (IVT + strict monotonicity), or a closed form.
A lemma about a generic monotone function, an axiom, or a conditional-class
instance would not.

**Caution for whoever re-centres it later.** Satisfying the gate fixes the
*bracket* only. It does not make α* derived — the regenerated witness would
still record a fitted parameter, now D-frame, and must say so. The deeper item
is `qou-cds1`-shaped, and per the two documents above the D-frame re-derivation
may conclude the parameter should not exist at all.

**State of the producer: unchanged.** It exits 1 and names where the root is on
stderr. That landed on `main` as `b95cc706d9` (PR #5695) — note the sha, the
rebase-merge rewrote the branch-side `d7cf6dc02b`.


## CORRECTION 2026-08-25 — the +14.741 % is a STRADDLE artifact. Full-D is -7.209 %, the other way.

The diagnosis above is right that the root moved and that convention C→D is
why. The **magnitude and the sign are wrong**, and the reason is worth
recording because it is a general trap.

That measurement was taken with `hecke_core`/`pyhecke.gram` on **D**
(gram.py:199, since 6086572c4e) while `alpha_high_precision.py` was still
computing its **own z locally in convention C** —

    zv = mp.mpf(1)/(mp.sqrt(Q0)+mp.sqrt(QI))        # alpha_high_precision.py:88

so the state measured was neither frame: a **straddle**, D upstream against C
local. Migrating that local binding to `zv = Q0**3 / (Q0**2 + 1)` moves the
root back DOWN, past the committed value:

    committed (C-frame witness)          0.3058074307438076264762
    straddle  (D upstream + C local)     0.35088642931861095442     +14.741 %
    full D    (both migrated)            0.2837621640047978551950792  -7.209 %

Measured by bisecting the file's own `err_n_mp` at dps=50 over [0.28, 0.30],
where it changes sign (+0.097608609 % → -0.41930387 %). Exact mpmath; no
float64 in the arithmetic.

So the bracket guard's own hint moved too: on main it reads "the root is
between 0.34 and 0.36"; post-migration it reads "between 0.28 and 0.30".

**What this does not change.** The bracket is still not re-centred, the
committed alpha* is still a C-frame value, and this is still qou-2zjp's call
rather than the drain's — re-centring replaces a published number. The script
still exits 1 exactly as it did before, which is not a regression.

**What it does change.** Anyone re-deriving alpha* under D should target
≈ 0.28376, not ≈ 0.35089, and the scope paragraph below is worth re-reading in
this light: the nine hecke_core-importing candidates were screened on whether
their *upstream* z moved. A file with its own local C binding is a second,
independent failure mode that screen does not see — the value can be a straddle
rather than either frame. Local z bindings were the whole subject of the
convention-C drain, so the two lists overlap.

Local z migrated in PR #5739 (probe/derived-tower drain group).


## The producer this GAP is about was EXCISED the day after this bean was last updated (2026-08-30)

Found while auditing `computations/q0_anchor_manifest.json` for stems with no live
producer (bean `qou-aj91`). Not a resolution of the GAP — a note that its subject is
no longer on the live surface.

`computations/alpha/alpha_high_precision.py` was moved to
`computations/_deprecated/alpha_high_precision.py` in **f62425070e** (2026-08-25,
on `main`), whose message is *"B2: EXCISE alpha* — it is a fit, and only CAL-1/2/3
are admissible"*. This bean's last update is 2026-08-25T01:03:24Z, so the two
crossed by hours.

**What that does and does not settle.** The bisection-bracket failure recorded
here was real and is not retracted; the diagnosis reached in this bean — that it
is convention-C→D drift in `z`, with two `z` definitions 22.7 % apart inside one
functional — stands as measured. What has changed is only that the file carrying
it is no longer a live producer, so nothing on the live surface runs the broken
bisection any more. If the C→D `z` diagnosis is a *general* one that applies to
other producers, the excision does not touch it and the bean should stay open on
that ground; if the bean's whole scope was this one file, it is moot.

**I am deliberately NOT closing it** — I did not write it, and which of those two
readings applies is a judgement about the bean's scope rather than a measurement.

**A live leftover the excision missed.** `alpha_high_precision` is still listed
under `ideal_muon` in `computations/q0_anchor_manifest.json`. That entry is not
inert: `q_parameter` selects the anchor by `Path(sys.argv[0]).stem`, so running
the deprecated file directly still rebinds the constants to the **muon** pin.
Removing the entry would silently flip that file to proton, which is why I have
left it alone and recorded it instead.
