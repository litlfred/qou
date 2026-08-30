---
# qou-cds3
title: 'S3 (SCIENCE): muon -> proton witness migration — 870 not ~840, and 69 straddle both pins'
status: todo
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-30T11:33:03Z
---

Parent: `qou-cdx1`. Related: `qou-1c4y` (the tracked migration), `tnjb`
(completed, a *dashboard* defect — do not confuse the two).

## Measured 2026-08-15 (fixed-string, `computations/**/*.witness.json`)

| | count |
|---|---|
| total witnesses | **2941** |
| muon fingerprint `1.109978595` | **870** |
| proton fingerprint `1.1099785827` | **588** |
| **both** | **69** |
| muon-only | **801** |
| proton-only | 519 |

**AGENTS.md's "~840" is low, not stale-high.** The measured figure is 870
(801 muon-only). AGENTS.md was right to flag the number as needing
re-measurement; the error runs the opposite way from what "stale" suggests.

## Do the 69 both-pin witnesses FIRST — they are a defect either way

A witness quoting both pins is either a deliberate comparison or a **layer
straddle**, which AGENTS.md names STRICT: *"Never straddle the two layers inside
one quantity."* The worked precedent is the μ₃ Fréchet probe, which took `y_λ`
from the muon-built cache while evaluating `χ_λ` at the proton `q₀` — an
11.54 ppb separation, ~1e-7 on the result. Triaging these 69 is worth doing
**regardless** of whether the bulk migration is authorised.

## The specific trap to check at every call site

`wedderburn_jones_markov.y_lambda_at(n, q)` returns the cached **muon-built**
`y-lambda-at-q0.witness.json` whenever `|q − q_parameter.Q| < 1e-12` — a gate
satisfied **trivially** when the caller passes `q_parameter.Q` itself. The
ideal-layer cache reaches an experimental-layer caller with **no signal**. For
experimental-anchor compute call
`schur_principal_mpmath.y_lambda_at_q0_mpmath(n, q)` instead.

## Scope question for the owner

**R2's wording does not obviously authorise the bulk rewrite.** The 2026-08-07
directive explicitly did *not*, and R2 states the end state rather than the
sweep. Recommendation in the ruling audit: treat the bulk migration as still
needing its own scoped sign-off; do the 69-witness straddle triage now.

Standing posture until then: new/touched code uses proton; untouched muon
witnesses stay as recorded; never mix within one quantity; every new witness
records its q₀.


## Re-measured 2026-08-25 — 105 both-pin, not 69, and ZERO unpaired straddles

The 69 above is from 2026-08-15; the corpus has grown. Re-measured on main
`2c53783e3d3` over `computations/**/*.witness.json`:

    both-pin witnesses                              105
      DELIBERATE — every site names its own layer    30
      DELIBERATE — computed-at sites layer-PAIRED    19
      ABOUT — audits reporting the pins as data       8
      residue needing a human read                   48
      UNPAIRED computed-at straddles                  0

**The bucket that would be the real defect class is EMPTY.** A witness carrying
both pins is overwhelmingly a deliberate comparison: `/data/muon_anchor/q0`
beside `/data/proton_anchor/q0`, or `/anchors[1]/q` beside `/anchors[0]/q`.
The bean's framing -- "a defect either way" -- does not survive measurement.

**My first classifier said 19 straddles and was wrong.** It required EVERY
mention of a pin to name its layer, so a plain `q0Value` provenance stamp --
which names nothing -- kicked 19 genuine paired comparisons into the straddle
bucket. Testing for PAIRING (is each muon computed-at site matched by a proton
sibling, by name or by index?) absorbed all 19. Five iterations of the
classifier plateaued at ~48 residue, which is the signal that the rest needs
reading rather than more regex.

## TWO confirmed, and they are NOT the same defect

Both are stamped `proton` while their `parameters.q_0_50dps` is muon-family.
Cross-confirmed from an independent direction: both also appear in the
stamp-vs-payload scan recorded on `qou-khac`.

  he3-brane-tower-structural-gap    q_0_50dps = 1.1099785955573347...  = A
      the CANONICAL muon anchor. A plain mis-stamp; the honest label is `muon`.

  he3-tower-charge-asymmetry        q_0_50dps = 1.1099785955541805...  = B
      the CODATA-2018-derived value, which is NEITHER anchor. Same class as
      `meson_mass_from_hecke` (PR #5742), whose honest label is `ambiguous`
      plus a reason naming the value.

Neither is fixed here -- each needs its producer read, which is separate work.

## The bean's "specific trap" note is STALE — do not act on it

The section above tells the reader to check every `y_lambda_at(n, q)` call site
because it "returns the cached muon-built witness". **That was corrected on
2026-08-23** (beans `qou-c1ya` / `qou-vu19`, and AGENTS.md carries the
correction): the live `y_lambda_at` is five statements, reads no witness, and
its whole call cone is cache-free. The gate and the cache load moved into
`_y_lambda_at_convention_C_HISTORICAL`, which is dead code.

Measured cost of following the stale wording: promoting `y_lambda_at` to a
muon identifier reclassified **56 producers** from `proton` to `BOTH`, hiding
56 clean files behind an association the code no longer has.


## CORRECTION, same day — both "confirmed" are STALE WITNESSES, not defects

The section above names two confirmed both-pin defects and diagnoses them
differently (one a mis-stamp, one the meson class). **Both diagnoses are
wrong.** Reading the producers instead of the witnesses:

`computations/probes/he3_brane_tower_structural_gap.py:46` carries a comment I
had not found:

    # q0 comes from the pin table, never a literal. This held
    # `1.1099785955541805`, the SUPERSEDED muon value -- it matches
    # neither current pin, so nothing could compare it against
    # anything. Owner ruling 2026-08-24, bean `qou/ftuv`.
    Q0 = Q_MP

`Q_MP` is the PROTON pin. So the producer was already fixed by an owner ruling
on 2026-08-24; only its committed witness was stale. And
`he3_tower_charge_asymmetry_probe.py:55` IMPORTS `Q0` from that same module, so
one ruling fixed both.

Verified by re-running, not inferred:

    he3-brane-tower-structural-gap   q_0_50dps  1.1099785955573347 -> 1.1099785827513808
    he3-tower-charge-asymmetry       q_0_50dps  1.1099785955541805 -> 1.1099785827513808

Both now match their own `q0Value: proton` stamp, and both leave the both-pin
population. Regenerated and committed; gates green.

**So the both-pin count is 105 -> 103, and the confirmed-defect count is ZERO.**
Every one of the 105 is a deliberate comparison, an audit reporting the pins as
data, or -- in these two -- a witness stale against a fix already applied at the
producer.

The lesson for whoever drains the remaining 48-by-hand: **read the producer,
not the witness.** Both of these looked like live stamp/payload contradictions
from the witness alone, and both had been fixed upstream a day earlier.


## The 46-by-hand residue, discriminated by SOURCE — and re-run decides nothing

Applying the lesson above (read the producer, not the witness) mechanically:

    residue examined                                          46
      BOTH reads the pin table AND hardcodes a muon literal   21
      READS the pin table — witness could be stale            14
      neither signal                                           5
      HARDCODES a muon literal — deliberate comparison         5
      no scriptFile — cannot reach the producer                1

The 14 are the only ones a re-run can settle, so all 14 were re-run (zero
untracked witnesses verified first; the tree restored afterwards).

**7 of 14 moved. NONE of the moves is a value.** Every one is environment:

    mpmath              1.4.1  -> 1.3.0        (this container is OLDER)
    pyhecke_native_build 30fd920c... -> b843d058...
    clarabel            (absent) -> 0.11.1

Four of the seven have literally zero non-environment lines. Two more are my
own filter leaking the `invocation` block. The seventh,
`deuteron-from-scratch-ledger`, moves LP duality numbers
(`duality_gap 43938.59 -> 43926.64`, ~0.03 %) — and `clarabel 0.11.1` is in the
same environment diff, so that is a SOLVER VERSION difference, not q0 staleness.

**Nothing was committed.** Committing any of them would write this container's
older mpmath and its clarabel over a record made with newer ones — the same
provenance degradation that excluded `atomic_tr_m_helium4` from PR #5736.

## Net result for this bean

    both-pin population                    105 (bean said 69, from 2026-08-15)
    deliberate comparisons / audits         57
    stale witnesses, fixed and committed     2   (he3 pair, PR #5752)
    residue re-run, zero stale values       14
    residue still needing a human read      30
    CONFIRMED DEFECTS                        0

The bean's "a defect either way" premise is measured false. What remains is 30
files that need eyes, and the useful thing learned is that **re-running them in
a container older than the one that wrote them cannot decide anything** — the
environment delta swamps the signal. A future drain needs an environment
matching the recorded one, or it should compare only non-environment fields.


## 2026-08-29 (LATER) — the 36 direct readers: 18 MIGRATED, PR #5992

The work the drain established could not be done by re-running. Source edit +
manifest move + re-run, all three, per producer.

**Landed (18 producers, 19 witnesses to proton).** ideal_muon 45 -> 32.
Zero straddles among the touched witnesses.

**The manifest half is not optional and half the change is a NO-OP.** 14 of
the 20 stems were listed under ideal_muon, so q_parameter.Q_50_DIGIT_STR
resolves to MUON for them and the source edit alone does nothing. Found it
when delta-S-chain-audit came back stamped muon with a muon data.q_0_50dps
after a source-only edit — the payload-first resolver caught it instantly.
AGENTS.md says this ("the manifest reclassification and the witnesses it
re-pins are one change") and it reads as advice about MERGE ORDER; it is also
a statement that half the change is inert.

**5 excluded after reading, not by pattern.** The ledger
(q0-muon-legitimate-producers.json, 17 entries, inherited from PR #5500 rather
than rebuilt) covers 13. Three more on inspection: muon_pin_three_values_probe
(derives inline to COMPARE the three values), lambda_scale_substrate_probe
(self-documents that it reads directly BY DESIGN and measures that), and
q_beta_predicted (no direct read at all — prose label only; reaches muon via
derived_masses, so it is the indirect class).

**2 DEFERRED on a float64 defect — and the mechanism generalises.**
chi_lambda_he4_full_partition_table and gram_matrix_seminormal_h6 turned the
raw-float64 ratchet red (194->196, 130->131). The migration did NOT add
float64: those fields were always f64, evaluated to exactly 1.0 / -1.0 at the
muon pin where the ratchet's INTEGRAL-VALUED CARVE-OUT does not count them,
and to 1.000000000000009 / -0.9999999999999999 / 0.9999999999999998 at proton
where it does.

  🛑 The carve-out hides float64 error whenever the true value is whole.
  A clean ratchet on a determinant-of-±1 or an exact-count character is NOT
  evidence the arithmetic is exact.

Root cause: chi_lambda_braid(..., q0_f64) enters the f64 Rust kernel;
gram_matrix_seminormal_n.py:190,195 uses float(np.linalg.det(M)). Fix is named
by the corpus (precision='mpfr_50dps' / chi_lambda_braid_mpf) but changes the
COMPUTE PATH, so every value in both witnesses moves. Bean qou-k6b3.

## What remains on cds3

  * 2 direct readers, blocked on qou-k6b3
  * ~25 witnesses whose producers reach muon INDIRECTLY (imports, upstream
    witnesses) — these need cone tracing, not a direct edit, and are the
    genuinely unmeasured part
## 2026-08-29 — the sweep RAN, and it cannot finish the migration

Drain: computations/audits/q0_muon_proton_drain.py across 177 producers, 94.7 min.
149 OK + 5 completed-with-failing-assertion, 11 crash, 9 timeout (240 s budget),
3 refuse by design. 131 witness files changed. Landed on
claude/cds3-muon-proton-drain-2026-08-29.

### The population this bean records is stale by ~4x

The body above says 870 witnesses. **Measured: 222**, of which **178 actionable
over 177 producers** — 11 legitimate-muon by ledger, 10 declared
ambiguous/comparison/independent, 20 with no scriptFile, 2 whose producer is
gone, 1 anchor-defining (excluded by name). The 870 is the ten-digit-prefix
reading of an older tree; see AGENTS.md's own warning that three different
values are all called "the muon q0" and the prefix length silently selects which.

### What the re-run bought — and why muon went UP

HEAD vs worktree, identical filters over computations/**/*.witness.json:

    10-digit muon fingerprint    437 -> 431   (-6)
    frozen canonical pin literal  66 ->  42   (-24)
    q0Anchor: "muon"              49 ->  61   (+12)

**The +12 is correct.** resolve_q0_anchor_payload_first (2026-08-24, qou-aj91)
reads the payload's recorded q0 instead of the manifest, so three witnesses that
declared "proton" over a muon computation now declare the layer their numbers
actually belong to (t6-tau-h5-embedding-probe, t6-three-halves-factor-probes,
xi-ell-phi-q-probe). Straddle corrections, not regressions. The -24 is
stale-to-current: the anchor-defining witness on main already holds the
CODATA-2022 derivation 1.10997859564273904..., not the frozen
1.1099785955573347..., so those witnesses were disagreeing with their own anchor.

### 🛑 THE FINDING: re-running producers is structurally incapable of finishing

Of the **61** muon witnesses remaining, **36 have producers that read
computations/q-pinning-50-digit.witness.json directly**. That string IS the muon
anchor's definition — it is what _q0_value_for_anchor("muon") returns — so those
producers compute at muon whatever the manifest says, QOU_Q0_ANCHOR cannot reach
them, and re-running them re-derives the same muon value forever.

**163 producers in the tree read the pinning witness.** Migrating them needs a
per-producer SOURCE EDIT (read q_at() instead), which is a code change, not a
sweep. And the manifest is not the lever either: resolve_q0_anchor_payload_first
deliberately overrules it with payload evidence — that is the function's whole
purpose, so relabelling the manifest would now change nothing at all.

So "re-run the impacted witnesses" — the method this bean assumes — is done, and
it moved 6. The remaining work is 36 producer edits plus 25 whose muon route is
via imports/upstream and needs tracing. That is the real shape of what is left.

### 🛑 AND cds1 BLOCKS IT: four witnesses reverted for live C->D contamination

The re-run put convention-D values into the Q_beta c_k channel, which qou-cds1
explicitly forbids ("c_3 ~ -974 is a sensitivity measurement, not a proposed
value. Do not wire it anywhere"):

    qbeta-ck-basis-constrained-pslq     c3_reproduced_canonical -2.0202 -> -974.38
    qbeta-decay-sdp-full-ck-derivation  c_3 -2.0097 -> -974.12 (c_4/c_6/c_7 dropped)
    qbeta-habiro-integrality-kill-test  three N3 residuals ~1e-44 -> -972.05
    qbeta-borromean-cyclotomic          documented_D_neq_C_split_reproduced FAILED

Detector: assertions flipping passed true -> false across the drain — catches
the class generally rather than by value range. All four reverted to their
committed C-frame state.

**The ladder core is already on D while the ladder itself has not been
re-derived**, so any mechanical re-run of a c_k producer bakes in a value the
corpus says is not a value. cds1 is not merely adjacent to cds3; it gates the
qbeta slice of it.

### Gates

    witness_raw_float64_audit.py --strict   PASS (0 new, 0 regressed; 12 drained)
    q0_anchor_ratchet.py --strict           PASS (0 new; 39 drained)

The float64 ratchet was RED first pass and is green only after fixing
qbeta_exponentiated_per_block_probe.py at the producer. No baseline widened.


## 2026-08-29 (LATER) — the INDIRECT class, partitioned

The direct-reader set is done (20/20, PRs #5992 + #6001). What #5989 called
"~25 whose producers reach muon indirectly" is now measured and split, so the
remaining work is enumerable rather than a gesture.

**25 muon witnesses over 25 producers whose producer does NOT read
q-pinning-50-digit.witness.json directly.** They partition:

    13  listed in ideal_muon      -> THE MANIFEST IS THE LEVER
         binding_via_interface_knot, block_swap_binding, wlambda_q0_continuation,
         fivetwo_stokes_matrix_zq, gram_norm_binding_probe,
         habiro_interpolation_wlambda, hadron_knot_table,
         he3_tritium_cosh_asymmetry_diagnosis,
         lever1_binding_habiro_single_element_test, theta_jet_gb_grading_probe,
         + 3 qbeta c_k (see below)

    10  UNLISTED                  -> muon comes from CODE; needs a cone trace
         canonical_lepton_braid_words, derive_m_p_hecke_full_tower_50dps,
         f_ell_derivation_via_per_braid_mass_tower, qbeta_c4even_exact_sseries_probe,
         rho_k_h3a_residual_decomposition, t6_lepton_h3_3channel_convention,
         t6_tau_h5_embedding_probe, t6_three_halves_factor_probes,
         vhat_std_vs_full_tower_compare, xi_ell_phi_q_probe

     2  DUAL-LAYER — do NOT migrate  (see below)
         canonical_tr_m_via_chi_cache, markov_peel_atomic_witness

**4 are cds1-gated** and must wait for the D re-derivation regardless of which
bucket they sit in: qbeta_c4even_ladder_reconstruction_probe,
qbeta_hoefsmit_tbeta_matrix_build_probe, qbeta_jacobi_anger_tower_general,
qbeta_c4even_exact_sseries_probe.

So the actionable remainder is **10 manifest moves + 10 cone traces**, not 25.

### The 2 dual-layer ones are a ledger gap, not migration work

Both emit ONE WITNESS PER ANCHOR with the muon layer `-muon`-suffixed, and both
document why in their own source. markov_peel_atomic_witness INVERTS the
sibling convention deliberately — six consumers of its base name are not
anchor-aware, so making the base muon would hand them muon values, the very
straddle the split closes.

**The ledger's dual_layer class listed 2 members; there are 4.** Added the two.
The originating regex (PR #5500) keys on an assert / a raise / prose demanding
a muon run — and **a producer that simply writes both layers asserts nothing
and raises nothing**, so it was structurally invisible. The detector that finds
them keys on OUTPUT: a producer emitting two witnesses whose q0Anchor values
DIFFER is dual-layer by construction. Recorded in the class rule.

(My first pass also reported atomic_tr_m_mpfr_50dps as missing. It was not —
dual_layer.members holds DICTS keyed `producer` and my parser looked for
`stem`. The ledger was right; the reader was wrong.)


## 2026-08-29 — indirect class, first half: 8 migrated, 2 held

PR #6001. ideal_muon 31 -> 22. Each of the 8 verified BEFORE the move to have
q_parameter reachable in its cone; otherwise the manifest is not the lever.

  binding_via_interface_knot      gram_norm_binding_probe
  block_swap_binding              he3_tritium_cosh_asymmetry_diagnosis
  wlambda_q0_continuation         lever1_binding_habiro_single_element_test
  fivetwo_stokes_matrix_zq        theta_jet_gb_grading_probe

### hadron_knot_table — HELD, cannot be regenerated

Its committed witness reads durationMs: 53, which is what made it look cheap.
It is not. The three A=1 atoms finish in seconds, then it stalls on DEUTERIUM,
the first bound atom — exactly what AGENTS.md records. Killed at 1297 s.

Moving it in the manifest without a regenerated witness would leave the
manifest asserting proton over a muon witness. Entry reverted; stays
ideal_muon until someone has a route to compute it.

### habiro_interpolation_wlambda — a COMPARISON, and two lessons

Its cone does not reach q_parameter at all, which is what flagged it. Line 389
loops over BOTH pins and reports the cross-pin swing of F_lambda. Migrating it
would destroy the measurement.

**`ambiguous` was my first answer and it was the wrong WORD.** Ambiguous means
UNDETERMINED; this is the opposite — two pins, deliberately, with the
difference as the result. The vocabulary reserves `comparison` for exactly
this, producer-declared, because resolve_q0_anchor structurally cannot return
an intent no manifest lookup can establish.

**🛑 And a manifest entry is SILENTLY INERT for any producer whose
WitnessBuilder is constructed without a script path.** This one is. It kept
stamping `muon` through TWO full re-runs while the manifest said `ambiguous`
and `resolve_q0_anchor(...) == ("ambiguous", None)` agreed. I only found out by
re-running and watching it ignore both. Fixed by declaring at the producer via
`q0_comparison(...)`.

That generalises beyond this file and deserves a detector: any producer whose
builder lacks a script path cannot be steered by the manifest at all, so a
manifest entry for it is a false record. Not filed as its own bean yet.

### Remaining

  10  unlisted producers needing cone traces
   4  cds1-gated qbeta c_k
   1  hadron_knot_table (compute-blocked)


## 2026-08-29 — the INDIRECT remainder is mostly NOT migration work

Traced the 10 "unlisted, muon comes from code" producers. The picture changes
substantially: only **2** are genuine migration candidates.

    6  DERIVE the muon pin from the CAL-2 lepton tower  -> must NOT migrate
    1  rho_k_h3a_residual_decomposition: muon as an explicit COMPARISON
    1  qbeta_c4even_exact_sseries_probe: cds1-gated
    2  derive_m_p_hecke_full_tower_50dps, vhat_std_vs_full_tower_compare
       -> still genuinely unexplained; the only real remainder

### The 6 compute the anchor rather than reading one

    hbar_q_sq = Vol_4_1 / M_MU_OVER_M_E
    hbar_q    = sqrt(hbar_q_sq)
    q0        = 1 / (1 - hbar_q)

That is AGENTS.md's CAL-2 lepton tower verbatim. Re-pinning them to proton is
not a migration, it is incoherent: the quantity they produce IS the
muon-anchored one. Added to the ledger as a NEW class,
`derives_the_muon_pin` (7 classes, 26 members).

  canonical_lepton_braid_words          t6_tau_h5_embedding_probe
  f_ell_derivation_via_per_braid_mass_tower  t6_three_halves_factor_probes
  t6_lepton_h3_3channel_convention      xi_ell_phi_q_probe

### 🛑 Why two independent scans both said "no muon route"

A marker scan over the import cone (q_muon_at, pin_value_for_anchor,
_q0_value_for_anchor, Q0_MUON, the anchor witness, a muon literal,
QOU_Q0_ANCHOR) finds NOTHING. An upstream-witness scan finds nothing either:
zero upstreams. Both are correct.

**The route is a MASS RATIO — not a q0 name, not a witness read.** No q0-shaped
token appears in these files at all. Same shape as the dual_layer gap found an
hour earlier, where the ledger's originating regex could not see a producer
that asserts nothing.

I first tested whether they were merely STALE — committed at muon, never
re-run. They are not: re-running two reproduces muon exactly. That is what
forced looking past the scans to the source.

### Corroboration, from the opposite direction

Three of the six (t6_tau_h5_embedding_probe, t6_three_halves_factor_probes,
xi_ell_phi_q_probe) are EXACTLY the witnesses that flipped proton -> muon in
the #5989 drain, where resolve_q0_anchor_payload_first caught them declaring
proton (the manifest default for an unlisted stem) over a muon computation.
The two findings explain each other.

### Revised remaining work

    2  genuine unexplained migration candidates
    4  cds1-gated qbeta c_k
    1  hadron_knot_table (compute-blocked, stalls on deuterium)

Down from "~25 indirect" to **2**.


## 2026-08-29 — INDIRECT class CLOSED at zero migration work

The last two, derive_m_p_hecke_full_tower_50dps and
vhat_std_vs_full_tower_compare, had no explanation because there is none to
find: both call `load_q_50dps()` bare, which defaults to anchor="proton", and a
plain re-run takes each **muon -> proton** with no code and no manifest change.
Committed at muon before that default flipped; never re-run.

Final partition of the 25:

    13  ideal_muon -> 8 migrated, 1 compute-blocked (hadron_knot_table),
                      1 comparison (habiro), 3 cds1-gated
     6  DERIVE the muon pin (CAL-2 lepton tower) -> ledgered, must not migrate
     2  dual-layer -> ledgered, must not migrate
     2  STALE -> re-run, now proton
     1  rho_k_h3a: muon as a COMPARISON reference
     1  qbeta_c4even_exact_sseries_probe: cds1-gated

Nothing outstanding in the indirect class.

### Stale convention-C docstring on a shared loader, fixed

`load_q_50dps` advertised `z = 1/(q^{1/2}+q^{-1/2})` — convention C. The code
returns `_markov_z(q)`, convention D via the single definition in
closed_form_tau_M, whose own docstring explains it deliberately avoids an
inline respelling because shape-keyed detectors miss those. So the helper is
exemplary and the docstring one frame above it was left behind. ~33 importers;
a reader checking the contract at the function they call would conclude C.

### Whole-of-cds3 status

  DIRECT readers    20/20 migrated (PRs #5992 + #6001)
  INDIRECT class    closed, zero migration work outstanding
  BLOCKED           4 cds1-gated qbeta c_k; hadron_knot_table (compute)
  PROTECTED         26 producers across 7 ledger classes

The sweep this bean opened with -- "870 witnesses" -- was 222, of which the
actionable part is now done except for what cds1 and one long compute gate.


## 2026-08-30 — the "inert manifest entry" detector: NEGATIVE RESULT, 3 shapes tried

This bean names the class and says "Not filed as its own bean yet". Attempted
it. **The general form is not decidable statically**, and the reason is worth
more than the attempt.

### Root cause — TWO steering mechanisms on TWO DIFFERENT stems

    q_parameter.py:107        _stem = Path(sys.argv[0]).stem     ENTRY POINT
    qou_substrate/witness.py  stem  = Path(_script_path).stem    CALLER FRAME
                              (_script_path defaults to inspect.stack()[1])

**The bean's framing describes only the second.** A producer run as
`python3 foo.py` is steered correctly by `q_parameter` whatever its
WitnessBuilder does, because `sys.argv[0]` IS the producer. So "constructs no
WitnessBuilder" does NOT imply "the manifest entry is inert" — which is what
the note above invites a reader to test.

### Three shapes measured, all over-flag — DO NOT REBUILD THESE

1. **"listed but never constructs a WitnessBuilder"** -> **176**.
   `torus_knot_markov_trace_closed_form` builds a plain dict and writes it with
   `json.dumps`, never touching WitnessBuilder, and is steered anyway via
   `q_parameter`'s `sys.argv[0]` lookup at import.

2. **"a scriptFile on many witnesses = a helper stamping foreign witnesses"**
   -> 37 shared basenames, two largest both legitimate.
   `canonical_isotope_witness.py` (120) and `_habiro_coefficient_extract.py`
   (26) are BOTH entry points, BOTH manifest-listed, each emitting its own
   named family (`habiro-coefficients-*`). One producer / many witnesses is
   the normal case here. **A leading underscore is not evidence.**

3. **"scriptFile names a module with no `__main__`"** -> **90**. Those are
   producers running at top level without a guard, each naming its own witness
   (`meson-mass-from-hecke.witness.json` <- `meson_mass_from_hecke.py`).

I reported 176 to myself before checking it. Recording the numbers that were
WRONG as well as the one that survived, because the failure mode is the
detector-blindness pattern this corpus keeps hitting from the other side: here
the detector was too BROAD, not too narrow.

### The residual real cases exist and need a different method

`habiro_interpolation_wlambda` (recorded above) stamped `muon` through TWO full
re-runs while the manifest said `ambiguous`. That is genuine. It was found by
**running the producer and watching it ignore the manifest** — not by any
static shape. No shape tried here separates it from the 176/37/90.

### What DOES survive — 2 entries that cannot bind to anything

    alpha_high_precision  [ideal_muon]       only computations/_deprecated/
    binding_k_enumerator  [physical_proton]  only computations/_deprecated/

Both still have a committed witness carrying their name. The manifest asserts
an anchor class for two RETIRED producers. Decidable without running anything:
either the live tree has the file or it does not, so this class has no
false-positive mechanism.

**Reported, not fixed.** Removing an entry changes what `resolve_q0_anchor`
returns for that stem (unlisted => the `proton` default), and whether those two
witnesses should be retired alongside their producers is an owner call, not a
sweep.

AUDIT: computations/audits/manifest_inert_entry_audit.py (reporting-only; no
witness regenerated, no manifest edited). Its docstring carries the three dead
shapes so the next reader does not re-derive them.

### cds3 status from this session's reading

Everything else on this bean is GATED, not open:

    4  qbeta c_k          -> gated on qou-cds1 (the D re-derivation)
    2  float64 defect     -> gated on qou-k6b3
    1  hadron_knot_table  -> compute-blocked (stalls on deuterium, killed 1297 s)

Direct readers 20/20 and the indirect class closed at zero. There is no
unblocked migration work left on cds3.
