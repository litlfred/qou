---
# qou-wgta
title: 'P0: convention-C excision is INCOMPLETE -- 174 py + 61 lean + tools/ Rust core + a shipped package still on C, incl. 3 hybrids and the registry itself'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T12:42:32Z
updated_at: 2026-10-10T07:47:11Z
parent: qou-cdx1
---


Branch: claude/anchor-followups-2026-08-08. From a full-repo audit 2026-08-09,
dispatched after `tools/pyhecke/python/pyhecke/gram.py` was found on C by
accident -- the THIRD accidental discovery of a missed C site.

## HEADLINE

The excision (73311b57, 33a6c7aa) touched TWO Python files. Still on C:
**174 live Python files, 61 Lean files, 49 content .md/.ts files, the entire
tools/ Rust engine stack (re-exported through 9 language bindings), and a
SHIPPED PYTHON PACKAGE.**

Worse than uniform C: **THREE CONVENTION HYBRIDS** -- D in one factor and C in
another inside a single function -- so the number is reproducible under NEITHER
convention.

## CRITICAL (feeds a predicted observable)

 1. computations/borromean_binding_recompute.py:98  -- HYBRID, production entry
    point. `tau` (l.99) is the Lean D closed form (4+h^2-3h^4-h^6)/(h^2+4), but
    `z = 1/(sqrt(q)+sqrt(qi))` is C and builds f_pp/f_pn/f_nn. Its own docstring
    (l.110-116) DECLARES convention D. Binding = tau(D) x bonds(C). Registry
    channel borromean-binding-single-pipeline, production:true, consumed by the
    dashboard's m_can. Emits B_can0/B_tower for 2H..56Fe.
 2. content/.../observations/neutron-proton-mass-splitting.lean:33-46 -- C baked
    into the INTEGERS (4993). quarkPhiClosedForm -> quarkPhi -> massSplitting ->
    `theorem splitting_value : abs (massSplitting 3.7445 - 1.302) < 0.001`, i.e.
    the published n-p splitting vs CODATA. Under D, z-h/2 goes 0.3948->0.5082
    and z-h goes 0.2903->0.4036; the norm_num theorem would FAIL.
 3. computations/y_lambda_wenzl_bridge.py:122,140,249,472 -- HYBRID. 33a6c7aa
    switched closed_form_tau_M::markov_z to D but NOT this, and
    closed_form_tau_M:390,424 still calls y_lambda_wenzl_bridge_numeric inside
    compute_tau_M_nucleon_H3. So the binding channel's production trace is
    interface=D, constituent=C.
 4. computations/hecke/hecke_symbolic.py:46 -- `z_markov = 1/(q_half+q_half_inv)`
    is the DEFAULT ARG Z_SYMB of tr_M_element. ~20 call sites that omit `z`
    silently get C, including markov/markov_peel.py:272,469 (the production
    Markov-peel path) and binding_canonical.py:318-319.
 5. computations/markov/markov_trace_canonical.py:12,316-322,392 -- registry
    entry_point, production:true, docstring still DECLARES C, never switched.
    l.392 also float64.
 6. computations/binding_canonical.py:24,48,318-319 -- registered C
    implementation, 62 consumers per the registry, never switched.
 7. qou-mass/src/qou_mass/_internal/wedderburn_jones_markov.py:104-190 -- a
    SHIPPED PACKAGE (qou-mass 0.1.0a1) carrying a verbatim PRE-EXCISION copy of
    y_lambda_at, the "~155 consumer" surface. Symbolic branch RETURNS C where
    the live copy now raises. Siblings: _internal/markov_weights_symbolic.py:76,
    _internal/markov_trace_recursive.py:54,149.
 8. computations/markov/markov_weights_symbolic.py:88,160 -- Z_MARK pins the
    Wenzl level for y_lambda_symbolic/solve_y_lambda; feeds y_lambda_at_q0_cache
    which BUILDS the y-lambda witness cache.
 9. computations/schur_principal_mpmath.py:~68-70 -- bypasses y_lambda_at
    entirely; 5 deltalambda probes import y_lambda_at_q0_mpmath directly.
10. tools/hecke-engine/src/gram.rs:34-37,48,547,582 -- `markov_z(q) =
    1/(q.sqrt()+(1/q).sqrt())`, f64, re-exported by NINE bindings (pyhecke-native,
    wasm, node, c, jvm, r, julia, gap, octave). Drives trace_weights and the
    v_std quark-volume channel behind item 2. Also src/main.rs:76 and
    src/tr_m_atomic_mpfr.rs:54,169 (MPFR path -> canonical-mass-table-extended).
11. tools/pyhecke/python/pyhecke/gram.py:45,374,387 -- f64 + C; re-exported into
    constants.py, atom.py, molecular.py, sdp.py and 9 corpus consumers.
12. docs/coordination/trace-convention-registry.json entry_points[2],[3] --
    THE REGISTRY ITSELF still records the binding production entry point as C.
    And check_declarations R4 compares DOCSTRING STRING to REGISTRY STRING,
    never to code -- so stale docstring + stale registry AGREE and the validator
    reports PASS. Fixing either one alone turns it red.

## MODERATE
13/14. Stale prose on correctly-switched code: mass_binding_dashboard.py:311,
    closed_form_tau_M.py:339-345.
15/16. C-era values hard-pinned in assertions: gram.rs:636 (0.4993203340335982),
    tools/pyhecke/tests/test_gram_values.py:26-27 (same, and against the MUON
    q0 pin, a second staleness).
17/18. Lean C constants as DEFINITIONS: MassTheory/DeuteronNaiveZMagnitude.lean
    (zLo := 4993, rational enclosure false under D),
    LiftingDescent/H3BraneTowerScaffold.lean:71 (60-digit C constant).
19. **THE PAPER.** ~10 content/*-table-data.md files carry C numbers and compile
    via scripts/make-all-tables.py into qou-all-tables.tex (confirmed at
    :1836, :3682, :4951, :7864). Published numbers on an excised convention.
20-26. ~155 further computations/**.py, ~40 f64+C sites, ~57 further .lean,
    ~40 content prose, 8 language-binding READMEs, sage examples, qou-mass table.

## DO NOT TOUCH (correct as-is)
27. probes/probe_convention_d_vs_c_borromean.py, probe_writhe0_trace_insensitivity.py,
    markov_z_full_bar_condition_probe.py, probe3qrv_zpin.py,
    markov_z_fibre_rank_bar_covariance_probe.py, ocneanu_param_from_fibre_dimension.py
    -- these are the D-vs-C COMPARISON probes; two are in discovery.exempt.
28. wedderburn_jones_markov.py::_y_lambda_at_convention_C_HISTORICAL -- deliberate,
    unwired; its only caller is y_lambda_su_n.py:388's D-vs-C self-check. Clean.
29. _deprecated/**, docs/audits/**, .beans/** -- historical record, leave.

## WHY THE SWEEP MISSED THEM (so the next one does not)
 a. Searched by SYMBOL NAME off the registry's `implementations` bookmark list,
    not by FORMULA. Anything computing 1/(sqrt(q)+1/sqrt(q)) inline under a
    different name was invisible.
 b. Assumed computations/ was the world. tools/, qou-mass/, content/**/*.lean and
    content/**/*-table-data.md were never searched. The validator hard-codes this:
    check_declarations R5 iterates (REPO/"computations").rglob("*.py") and nothing else.
 c. The validator compares STRINGS TO STRINGS, never to code. R5's discovery
    filter also requires the name to contain "borromean" and match a tr_M-ish
    def pattern, which structurally excludes markov_z, y_lambda_at,
    y_lambda_wenzl_bridge_numeric, _wenzl_constants, Z_MARK, trace_weights and
    every module-level `z = ...`.
 d. Nobody grepped for the VALUE. `0.4993` appears in a Rust assertion, a Python
    assertion, two Lean defs, a Fraction, and 60+ prose sites -- including item 2,
    where C is disguised as the integer 4993 and the string "sqrt" never appears.

THE CATCH-ALL SEARCH (returns every site above):
  rg -n --hidden -g '!.git' -g '!_deprecated' \
    -e 'sqrt\(q[0-9a-z_]*\)\s*\+\s*1?\s*/?\s*(mp\.|sp\.|_mp\.|math\.)?sqrt' \
    -e 'q[0-9a-z_]*\s*\*\*\s*0\.5\s*\+\s*q?i?[0-9a-z_]*\s*\*\*\s*-?0\.5' \
    -e 'q\.sqrt\(\)\s*\+' -e 'q\^\{?1/2\}?\s*\+\s*q\^\{?-1/2\}?' \
    -e '0\.4993' -e '4993/10000' -e 'Fraction\(4993'

## STRATEGY (from the audit, adopt it)
Fix the DEFINITIONS, not the call sites. Items 4, 8, 9, 10, 11 are five single
`z = ...` lines with dozens of consumers each; switching those five converts the
majority of the 174-file tail automatically. Leaving them means every future fix
is another accidental discovery.

Also: 96 witnesses were already owed regeneration from the original excision and
never done -- and item 9 means several deltalambda paths read C weights WITHOUT
touching the gated y_lambda_at, so regenerating witnesses alone will not clear them.

---

## 2026-08-09 — the C→D excision fixed the CODE and left the WITNESSES on C

`b88aabc73` ("the Wenzl bridge was C under a D interface") changed
`y_lambda_wenzl_bridge.py` at four `z` sites:

    z = 1/(sqrt(q) + 1/sqrt(q))   convention C   (excised)
    z = q**3/(q**2 + 1)           convention D

and its own message lists the consumers moving with it as **"all previously
C"**. But `git show --stat` on that commit is one file: **no consumer witness
was regenerated**. So every witness that read the bridge before it landed still
publishes convention-C numbers, and nothing in those files says so.

### One is proven, and it is not a rounding difference

`charm-frobenius-block-projection.witness.json` — computed
`2026-08-09T12:31:08Z`, i.e. **59 minutes before** `b88aabc73` landed at
`13:30:23Z`:

    pred_charm_over_light   1.3486556457833476 -> 0.9757693178472477   (28%)
    pred_top_over_light     0.05475486952775208 -> 0.0                (100%)
    y_lambda (1, 1, 1)      0.02274494257734719 -> 0.0                (100%)
    trM_borromean           0.998366622585716  -> 0.9985621638367873

Identified by checking out the **pre-`b88aabc73` bridge** and re-running: it
reproduces the committed values EXACTLY, all three blocks. That is the proof;
everything else was inference. (I first assumed mpmath 1.4.1 vs 1.3.0 and
tested it — downgrading to 1.3.0 gives the NEW values, so the interpreter was
never the cause.)

Regenerated under D on `claude/drain-main-inherited-float64` (`acf6609b4`).
All 7 assertions still pass and the probe's parameter-free NEGATIVE reading is
unchanged — 0.976 vs an observed ~372 is as far off as 1.349 was.

### Why nothing caught it

**Both conventions satisfy the Markov normalisation exactly.**

    C:  0.4153958 + 2(0.2809296) + 0.0227449 = 1.000000
    D:  0.5054042 + 2(0.2472979) + 0.0       = 1.000000

So a normalisation self-check — the obvious local guard — passes under either.
Under D the antisymmetric block is exactly zero, which is the visible signature
to grep for.

### Candidate set: 47 witnesses, membership NOT established

58 live producers import `y_lambda_wenzl_bridge`. Of the witnesses they name,
**47 were computed before 2026-08-09T13:30:23Z**. That is a CANDIDATE list, not
a finding: predating the fix does not prove a witness's numbers depend on `z`.
Only `charm` is established, by the checkout-and-rerun method above.

Whoever picks this up: the method is cheap and decisive — restore
`b88aabc73^:computations/y_lambda_wenzl_bridge.py`, re-run the producer, and
compare. If the committed values come back, that witness is on C.

Earliest candidates by `computedAt`:

    2026-04-14  free-neutron-decay
    2026-05-20  tau-M-proton-closed-form-phase5l1
    2026-05-20  closed-form-tau-M-verification-phase5q
    2026-06-01  phase5/phase3-deuteron-tritium-h-expansion
    2026-06-22  y-lambda-at-q0            <- a CACHE other producers read, and
                                             very likely the "second hybrid"
                                             b88aabc73's own message names
    2026-06-23  atomic-tr-m-mpfr-50dps
    2026-07-03  probes/probe-convention-d-vs-c-borromean

`y-lambda-at-q0.witness.json` deserves going first: it is consumed as a cache
(`delta_lambda_empirical_tabulation.py:293` and others), so if it is on C it
re-seeds C into everything that reads it, and its own `computedAt` is
2026-06-22 — long before the excision.

### A separate precision ceiling, found in the same probe

`charm_frobenius_block_projection_probe.py` does `Q = mp.mpf(q_parameter.Q)` —
`q_parameter.Q` is a **Python float**, not `Q_50_DIGIT_STR`. So the probe's
whole computation is capped at 17 digits, and serializing q0 at 30 dps
fabricates the rest:

    mp.nstr(Q, 30) -> 1.10997858275138083783417641826
    the real anchor   1.1099785827513808075916690956...

diverging at the 17th digit. Written at its true f64 width in `acf6609b4`.
Whether the probe should read `Q_50_DIGIT_STR` is a separate call — it would
move values again.

### The cache is confirmed C, and 15 producers read it AROUND the guard

`wedderburn_jones_markov.py` already knows: its docstring says
`y-lambda-at-q0.witness.json` "holds C weights and must NOT be served — that
cache is why the switch has to happen here rather than only at `markov_z`."
That guard works. **It only covers callers that go through that function.**

The cache itself, verified by reading it:

    0.41539578633234285396775579738846403626500771799236    y_(3,)
    0.28092963398059057548223798645901560186893685925826    y_(2,1)
    0.022744945706475995067768229693504759997118563491127   y_(1,1,1)

Zero convention-D markers anywhere in the file. These are exactly the C values
`wedderburn_jones_markov`'s own docstring quotes, and exactly what the charm
witness turned out to be carrying.

**17 live files open that JSON directly rather than calling the guarded
function**, so the guard never runs for them:

    delta_lambda_empirical_tabulation.py        probe_theta_carry_binding.py
    binding_heat_kernel_weight_probe.py         probe_content_energy_signed_phase.py
    probe_1b_li6_orthogonality.py               probe_1_project_4he_on_dominant.py
    chi_4he_binding_lossless.py                 probe_full_theta_binding.py
    derive_binding_per_block_archimedean.py     probe_binding_measure_search.py
    derive_binding_bond_sum.py                  probe_binding_measure_search.py
    probes/pauli_young_spin_isospin_delta_lambda_probe.py
    qbeta/qbeta_per_block_paper_closed_forms.py
    qbeta/qbeta_per_block_symbolic.py
    qbeta/qbeta_per_block_uniform_rule_verify.py
    schur_principal_mpmath.py                   witness_upstream_declaration_audit.py

**Two of the 17 are NOT contaminated** and should not be counted as such —
they read the cache deliberately, knowing it is C:

  * `schur_principal_mpmath.py` — only in its `__main__` self-audit, and it
    prints "witness y-lambda-at-q0.witness.json is still convention C; this
    module is convention D. The last column is therefore the C-vs-D GAP, not an
    error, until that witness is regenerated."
  * `witness_upstream_declaration_audit.py` — an audit of who declares it.

**Three are verified to serve C weights straight into computation**, by reading
the code at the call site — each loads `by_n[n]` and returns
`{partition: mpf(y_at_q0_50dps)}` as the weights:

    chi_4he_binding_lossless.py:49   docstring calls it "the framework reference"
    derive_binding_bond_sum.py:65
    probe_theta_carry_binding.py:68

The remaining 12 need the same one-line check (does the loaded value feed a
computation, or only a comparison?) — I have not done it, so do not treat 15 as
a confirmed count.

**Why this is the highest-leverage item on this bean.** The excision closed one
door and left these open, and the cache re-seeds C into whatever reads it. Any
witness produced by those 15 since 2026-08-09 is on C no matter how new it is —
`computedAt` is not a safe filter for them, unlike the 47-witness candidate set
above.

Cheapest durable fix, in order:
  1. regenerate `y-lambda-at-q0.witness.json` under D (it is the single
     upstream), then
  2. re-run the direct readers, then
  3. make the direct reads go through the guarded accessor so the next
     convention change has exactly one door again.


## 2026-08-25 — recovery pass, PR #5799 (branch claude/isotope-mass-binding-dashboard-kdvhz6)

Picked up the partial work of an agent that died on a session limit (git stash).
Took only what re-measured: `scripts/convention-c-producer-audit.py` +
`docs/coordination/trace-convention-registry.json`. **Rejected** the three
witness diffs in the same stash — they drop `clarabel: 0.11.1` from the recorded
`environment` block, which is an artifact of that agent's bare container
(clarabel is absent here too), so committing them would record a false
environment on three committed witnesses.

**Live actionable: 7 before, 7 after.** Nothing was migrated, because nothing
in the current actionable set is migratable — all 7 are in the qbeta/decay cone
where a z-swap is invalid per `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
(sorry-free). What changed is that all 7 now carry their blocking reason in the
detector output instead of the uninformative "probes / exploratory" bucket.

Per-site classification (all (ii) blocked on `qou-cds1`):

| site | line | why a z-swap is invalid |
|---|---|---|
| `qbeta/qbeta_prearchimedean_z_recursion.py` | 103 | the RESULT is a 3-term recursion from z_C being algebraic; z_D residuals at n=1,2,3 are 17/2, 3, -5/4, not 0 |
| `probes/qbeta_fmap_power_class_prune.py` | 89 | verbatim mirror of the sorry-free `CanonicalMarkovWeightsH3.explicitInstance`, sqrt(q)-bearing by construction; the Lean must move first |
| `qbeta/qbeta_eta_singularity_probe.py` | 178 | ladder phase alpha moves 20.77 % at the proton pin |
| `qbeta/qbeta_eval_map_bar_decomposition_probe.py` | 48 | z_C bar-EVEN, z_D bar-NEITHER; the exact even/odd split it reports does not exist under D |
| `qbeta/qbeta_h_frame_rungs_probe.py` | 73 | alpha = (z-1)h/2 moves 22.64 % |
| `qbeta/qbeta_t3_carrier_q1_order_preflight_probe.py` | 68 | ord_{q=1}(z-1/2) is 2 under C, 1 under D; the even-order premise of the T3 exclusion is false under D |
| `qbeta/qbeta_z_bar_parity_fmap_class_probe.py` | 72 | parity(z_D^m) is NEITHER for m=1..4; the z-alone exclusion has no D-frame statement |

Two evidence fields in the recovered rows were WRONG and are corrected in place
(conclusions unaffected):

- `qbeta_fmap_power_class_prune` claimed a z-swap "would un-refute the pure-power
  class". False: Arm-1 runs on `dtr`, the z-free atom-word bridge rational;
  `explicit_differs` is True under both conventions. No Arm-1 verdict moves.
- `qbeta_eta_singularity_probe` reported its alpha move as 22.64 %. That is the
  z-dependent part (z-1)h/2; alpha itself also carries u_tilde = 0.0094539479
  and moves 20.77 % (-0.0570630942 -> -0.0452127513). 22.64 % is correct only
  for `qbeta_h_frame_rungs_probe`, whose alpha has no u_tilde term.

The one C-SPECIALISED CLOSED FORM (`qbeta_5two...:133 ocneanu_weights`) is a
detector FALSE POSITIVE, measured by execution: the function returns
W_(3) = (q^4+1)/(q^2+1)^2, W_(2,1) = q^2/(q^2+1)^2, W_(1^3) = 0 — all exactly
q-rational. The sqrt is a back-substitution undoing `q = t**2`. Recorded in the
new `closed_form_measured_clear` registry channel and LABELLED, not suppressed;
a suppression rule would also hide a genuinely C-derived closed form
back-substituted the same way.

The other carried-forward closed form (`_li_2_q_util.borromean_markov_trace_h2`)
is already resolved in-source as the deliberate non-canonical jones-normalisation
comparison column and no longer appears in the report.


## 2026-09-07 — Lean surface re-measured; "0 actionable" had REGRESSED to 1, now back to 0

This bean was last updated 2026-08-25 and its headline figures do not reproduce.
Re-measured with `scripts/lean-markov-convention-audit.py` on `main`:

| | bean (2026-08-25) | AGENTS.md (2026-08-29) | **now (2026-09-07)** |
|---|---|---|---|
| `.lean` convention-C **defs** | "61 lean files" | 14 | **23** |
| of those, actionable / deliberate | — | 0 / 14 | **0 / 23** (was **1 / 22** before this commit) |
| `.lean` convention-D defs | — | 38 | **50** |

**The finding: AGENTS.md's "The Lean surface reaching 0 actionable is real
progress" had SILENTLY REGRESSED to 1.** Both conventions are accreting
definitions (C 14 → 23, D 38 → 50), and one of the new C ones arrived
undeclared.

**The site**
`QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean:1233 markov_parameter`:

    noncomputable def markov_parameter (q : ℝ) : ℝ := Real.sqrt q / (1 + q)

`√q/(1+q)` **is** `z_C` exactly, and it is **consumed** —
`QBetaCanonicalMarkovWeightsInstance.lean:54-56` builds `y3`, `y21`, `y111`
from it.

**It was NOT migrated, deliberately, and swapping in `z_D` would be wrong
twice over:**

1. Its only consumer says in its own header that it exists to prove
   `CanonicalMarkovWeightsH3` **inhabitable** — making the §3b-cond
   conditional theorems non-vacuous — and is "**NOT** a claim that this is THE
   canonical Wenzl–Markov instance". Inhabitation does not need the canonical
   `z`.
2. `markov_parameter_symmetric_form` proves
   `√q/(1+q) = 1/(√q + 1/√q)` — a **true, sorry-free identity about `z_C`**.
   Substituting `z_D` would falsify a theorem, not migrate it.

So the audit's `actionable` verdict means **undeclared**, not **wrong**. Fixed
by declaring it, which is what the other 22 deliberate sites already do.
Re-derivation under D remains a separate tranche (`qou-cds1`); per
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` a plain `z_C → z_D` substitution is
not valid there either.

**Verified:** `lean`-direct with `-DautoImplicit=false -s 65536` and
`LEAN_PATH` over the restored oleans — **0 errors, 0 sorries, 32 warnings**,
and the pre-edit baseline is **identical** (0 / 32), so the edit adds nothing.
Never `lake build`: `.lake/RESTORED-NO-TRACES` is present.

## Also: the "SHIPPED PYTHON PACKAGE" in this bean's headline is not shipped

Item 7 calls `qou-mass 0.1.0a1` "a SHIPPED PACKAGE", and the HEADLINE counts it
as an aggravating factor. Measured today: `pypi.org/pypi/qou-mass/json` →
**HTTP 404**. AGENTS.md already records this for all four in-repo packages
(`qou-mass`, `qou-substrate`, `pyhecke`, `pyhecke-native` — none published).
The convention-C content of that mirror is still real; what is wrong is the
*severity*, since there are **no external consumers**. And the mirror is
**generated** — fix `computations/`, then `scripts/sync-qou-mass-vendor.py
--apply`; never hand-edit `qou-mass/src/qou_mass/_internal/`.

**Bean stays open** — the `computations/` surface is untouched here, and
AGENTS.md's value-audit figure (85 confirmed C bindings, 21 of them invisible
to the shape audit) is the live scope.


## 2026-09-07 (2) — the `computations/` shape audit: 13 actionable, and the growth is LEGITIMATE

`scripts/convention-c-producer-audit.py` on `main`:

    6 sites / 6 files   probes / exploratory
    6 sites / 6 files   computations/qbeta — BLOCKED on the qou-cds1 re-derivation (registry, still actionable)
    1 site  / 1 file    computations/probes — BLOCKED on C by design (registry)
    1 site  / 1 file    computations — live producers
  113 sites             deliberately C-named — labelled comparisons, not defects

  ACTIONABLE (excludes blocked-by-design): 13

AGENTS.md records **9** on 2026-08-29. So the count went **up**.

**The detector-vs-corpus confound is RESOLVED, not assumed.** The script itself
changed on 2026-08-29 (`a6f785390c`, *"a D arm written as a CALL defeated both
detectors"*), so 9 → 13 could have been detector inflation. Measured both ways
on today's tree:

| detector | actionable today |
|---|---:|
| pre-`a6f785390c` | **15** |
| current | **13** |

The newer detector reports **fewer**, because it correctly stopped
false-positiving two D arms written as calls. A change that lowers the count
cannot explain a rise — so the **corpus** grew, by at least 4.

**But "regression" is the wrong word, and this is the useful part.** **12 of
the 13** sit in the `c_k` ladder cone — `computations/qbeta/` plus qbeta-axis
probes — and the single **live producer** is `qbeta_ck_cache.py:140`
(`z = sqrt(q) / (1 + q)`), the canonical `c_k` extractor, which AGENTS.md
records **refuses to run under convention D**. Per
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` the C-frame ladder and the mass
channel's three-row forcing are mutually exclusive, so `z_C → z_D` is not a
valid substitution there.

So the growth is **new C-frame `c_k` research continuing while the D
re-derivation is open** — which is correct, not sloppy. What is wrong is the
*label*: 6 qbeta sites are registered `blocked_on_rederivation` and the newer
siblings are not, so identical work is split across two buckets.

**Recommendation (judgement, not a finding):** register the newer qbeta sites
under the same `blocked_on_rederivation` entry as the existing 6. It does not
suppress them — that bucket is explicitly "still actionable" — it just stops
the headline implying an unexplained drift. Not done here: it is a registry
edit affecting what every future agent reads, and it should be visible rather
than folded into a Lean-labelling PR.

**The non-qbeta remainder is the genuinely unattributed part** — 4 probes
(`markov_reduction_h3_to_h4_verify.py:84`,
`nucleon-lp-convention-probe.py:87`,
`ocneanu_weights_are_sl_n_quantum_dimensions.py:207`,
`the_qbeta_bridge_table_and_its_witness_compute_different_z_probe.py:108`).
Three of those four have C in their *purpose* (a convention probe, an
old-vs-new comparison, a two-`z` discrepancy probe), so they are likely
deliberate-but-undeclared, the same shape as the Lean site fixed above. Not
triaged individually here.

## 2026-09-08: this bean is the canonical ledger for the convention-C excision family (audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 2 / §7.3 C3)

Chosen because it is the oldest in-progress full-surface tracker and is cited as predecessor by `qou-cds2` and `qou-eea0`; the owner-ruling milestone is `qou-cdx1` (todo) and the S2 science blocker is `qou-cds2`. Family members and statuses as of 2026-09-08 (each now carries a one-line pointer back here; no status changed):

| bean | status | subject |
|---|---|---|
| qou-wgta | in-progress | P0: excision INCOMPLETE — 174 py + 61 lean + tools/ Rust core (this ledger) |
| qou-janm | in-progress | Session: convention-C full excision (owner directive 2026-08-29) |
| qou-htsi | in-progress (parent qou-2akx) | sibling-found stale C sites + compute-closed gates to re-examine (owner 2026-09-06) |
| qou-t9r1 | completed | 8 unannounced C sites in computations/ (detector-blind spelling); successors qou-dbau, qou-cds1; blocked sites qou-pmkh (todo) |
| qou-eea0 | in-progress | CAMPAIGN: regenerate all 84 convention-C witnesses under D |
| qou-okkz | in-progress | consumer-side detector for deliberate convention-C control arms |
| qou-jyqd | in-progress | audit skips _deprecated, but two deprecated producers are still named by content |
| qou-fq0f | in-progress | convention D is Wenzl level r=2 exactly — the row cap the closure block argues against |
| qou-47sx | in-progress | convention-D atom.py caller sweep — true blast radius |
| qou-cds2 | in-progress (parent qou-cdx1) | S2 (SCIENCE): pyhecke.gram.z and the Gram singularity |

Related, not in the audit's nine: qou-8iru (in-progress, D is Temperley-Lieb), qou-cds1 (in-progress, S1 ladder re-derivation), qou-cdx1 (todo, milestone). Previously measured cross-citation: cds2↔8iru, htsi→t9r1, htsi→cds2, eea0→wgta, cds2→wgta only.

## 2026-09-15 — the tr_M detection gap is closed (`qou-ng7j`)

Owner directive "excise convention C", worked against this hub rather than a
new bean. `qou-ng7j` had recorded since 2026-08-10 that a convention-C `tr_M`
is invisible to every detector, because `_is_convention_c` keys on `y_λ`
tables. It is now covered: `intra_ordering_value_fingerprint_audit` gained a
trace-convention axis, 32 -> 64 live fingerprints, no transcription.

Two things worth carrying into the rest of the campaign:

  * **No production change was needed.** The convention enters through the
    WEIGHTS — `jones_wenzl_weight` already takes `z` — so `tr_M^C = Σ_λ
    ω_λ(q, z_C) · χ^λ(W)` is computable live. I had proposed parameterising
    `Z_MARKOV` and that was the wrong route.
  * **The D pipeline discards what a C value needs.** The Wenzl row cap zeroes
    every >2-row partition, so the bridge evaluates χ on 4 of 11 partitions at
    the deuteron; under C all 7 of 7 of the capped ones are live. Any future C
    detector that re-reads a D breakdown will be structurally blind for this
    reason, not for a missing pattern.

One net finding: `qbeta-habiro-phase5q-dn-refactorize` carries convention-C
proton/neutron traces and a field named `tr_M_D_q0_witness` holding a
convention-C deuteron, in a file that records `z_q0` as the D parameter. Details
and the corroboration against `qou-mass/CHANGELOG.md` are on `qou-ng7j`.

Eight of the twelve C hits are the five `*-c-vs-d-*` comparison probes, now in
the audit's `DELIBERATE` registry — explicitly, not by a shared-stem regex,
per `qou-4bq3`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 🛑 TITLE IS STALE BY ~30× — re-measured 2026-10-10 (bean `qou-am5t`)

This bean's title reads **"174 py + 61 lean + tools/ Rust"**, and `qou-cds2`
names this bean as *"the canonical ledger for the convention-C excision
family"*. So a reader who follows that pointer to find the state of the
migration gets the worst available answer. Measured today on `main`
`77695711d`:

| surface | this title | **measured 2026-10-10** | command |
|---|---|---|---|
| Python, blocking | 174 | **0** | `convention-c-value-audit.py` |
| Python, actionable by shape | — | 13 (12 probes + 1 producer) | `convention-c-producer-audit.py` |
| Lean, actionable | 61 | **0** (23 C defs, all deliberate) | `lean-markov-convention-audit.py` |
| `tools/` Rust | "Rust" | **0 live** (only `archive/v2.rs`) | by hand — no audit scans `.rs` |
| witnesses | — | 0 structural, 1 symbolic | `convention-c-witness-audit.py` |

`BLOCKING` was 6 this morning and is **0** as of `e6a5d23e9`: the six were read
and adjudicated into `docs/audits/convention-c-comparison-ledger.json` (137 →
143 entries) as two-convention comparison arms, with a rationale each.

**What is actually left is one producer and one research question**, not a
drain:

- `computations/qbeta/qbeta_ck_cache.py:140` — the canonical `c_k` producer, the
  only non-probe production file still on C, and the `qbeta-decay` channel
  (registry: definitional D, production **C**, `agreed-migration-pending`).
- It is **not drainable by substituting `z_D`** —
  `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`, sorry-free.
- And it is **not blocked on the ladder phase `α`** (`qou-pdix`), which the
  corpus asserted in two places until 2026-09-14: `cos ≤ 1` caps the N=2 factor
  at `1 − u² = 0.99992745` for every real `α`, while the ruled `z_D` base needs
  `F_required = 1.759` (order-zero `E₀`) or `1.200` (the dashboard-scored cell).
  No `α` reaches either. The live question is what object supplies a factor
  above 1 at all.

**Status proposal, not enacted:** this bean's *claim* — that the excision is
incomplete at that scale — is measurably false, and its role as the family's
canonical ledger is now served by
[`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md),
which carries the command for every number. I have **not** changed the status or
the title: retitling a bean whose body is an append-only ledger of a campaign
would rewrite the record of what the campaign believed, and the owner's call is
whether this becomes `completed` with the residual re-homed on `qou-cds1`, or
stays open as the family root with a corrected title. Nothing downstream depends
on the answer — the status doc is the thing readers should be pointed at either
way.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

See the dedicated 2026-10-10 append on this bean: title stale by ~30x (174 py
+ 61 lean vs a measured 0/0), residual is one producer plus `qou-cds1`. Left
open deliberately -- retitling an append-only campaign ledger rewrites what
the campaign believed; status is an owner call.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-10 re-measure on `main` `606d034db2`: 3 of 4 CRITICALs fixed; the 4th is live and invisible

Every claim below is measured against `main`, not read off a sibling bean.

### The four CRITICALs

| # | site | state |
|---|---|---|
| 1 | `computations/borromean_binding_recompute.py` HYBRID | **FIXED** — the same day this bean was opened |
| 2 | `observations/neutron-proton-mass-splitting.lean` C in the INTEGERS | **🛑 LIVE** |
| 3 | `computations/y_lambda_wenzl_bridge.py` HYBRID | **FIXED** |
| 4 | `computations/hecke/hecke_symbolic.py:46` `Z_SYMB` default arg | **FIXED** |

1. `_params` now reads `E0 = me/(q*(q-1)); z = q**3/(q**2+1)`, with a docstring
   headed *"CONVENTION-HYBRID BUG, fixed 2026-08-09 (bean qou-wgta item 1)"* —
   so item 1 was fixed on the day this bean was filed and the bean never
   recorded it.
3. `y_lambda_wenzl_bridge.py:30` declares *"This module is **convention D**,
   z = q³/(q²+1)"*, and `markov_z_numeric` returns `q**3/(q**2+1)`.
4. `hecke_symbolic.py:60` is `z_markov = q**3 / (q**2 + 1)  # convention D`,
   and it is still the default `Z_SYMB`, so the ~20 call sites that omit `z` now
   silently get **D**.

### Item 2 is live, and it is the one no detector can see

This is the bean's own strongest claim and it holds. The convention is **not a
`z` symbol** — it is a rational folded into integer coefficients:

    quarkPhiClosedForm "uud" = log |(4993·q₀² + 20000·q₀ − 4993)
                                  · (5000·q₀² − 4993·q₀ − 5000) / (2·10⁸ q₀²)|

`4993/10000 = 0.4993` is the rounded `z_C = √q/(q+1) = 0.4993203342` at `q₀`;
the coefficients are `10000·(z q² + 2q − z)`, `5000·(q² − 2z q − 1)` and
`10000·(q² − z q − 1)`. There is no `z`, no `Real.sqrt`, no `markovZ`.

**Confirmed invisible, by running the detectors rather than reasoning about
them:**

| detector | on this file |
|---|---|
| `scripts/lean-markov-convention-audit.py` | does not name it (**23** C defs found, **0 actionable**, 23 deliberate) |
| `scripts/convention-c-value-audit.py` | 0 — does not scan `.lean` |
| `scripts/convention-c-producer-audit.py` | 0 — does not scan `.lean` |
| any detector keyed on the literal | none knows `4993`; the producer audit knows the *decimal* `0.4993203342` and has a selftest for it |

A structural scan of the whole tree for this spelling (a standalone `4993`/`9986`
integer token adjacent to a `q` power, so decimals like `0.4993203342` are
excluded) finds **one `.lean` declaration and its provenance audit doc, and
nothing else** — so it is narrow, not a class. Recorded as **row 54** of the
detector-blindness taxonomy.

### What it publishes, and both frames

`splitting_value : abs (massSplitting 3.7445 - 1.302) < 0.001` is **sorry-free**
and is the framework's published n–p splitting against CODATA. Re-derived at
50 dps, with the harness **calibrated against the file's own rounded
`quarkPhi` constants first** (`Φ(uud)` 5.08e-5, `Φ(udd)` 6.19e-5 — both inside
the docstring's own claimed ~5e-5, and the calibration caught a `log 2` error in
my first reconstruction before any number was reported):

| frame | `z` | `\|ΔΦ\|` | `Δm` (MeV) | vs CODATA `1.29333217` | the theorem |
|---|---|---|---|---|---|
| **C, as published** | `4993/10000` | `0.3476040278` | `1.301603282` | **+0.64 %** | **HOLDS** (`3.967e-4 < 1e-3`) |
| **D, canonical** | `q³/(q²+1)` | `0.2815089929` | `1.054110424` | **−18.5 %** | **FAILS** (`0.2479`, **248×** its tolerance) |

`z_C → z_D` moves `|ΔΦ|` by **−19.01 %**. The bean predicted the theorem would
fail under D; it does, by 248×.

### Scope, and what must NOT be done

**Scope-(a).** Nothing here excludes the quark-ordering-volume route — no proved
invariant forbids a traced volume from carrying the splitting. And the C frame's
closer agreement is **not** evidence for C: it was obtained in the excised
convention, and picking a trace convention by its residual is precisely what
§NO FITTING forbids. **Do not substitute `z_D` into these coefficients to
"improve" the number.** The re-derivation is real work and is not done here.

**Done here:** the `.md` carries the frame in its statement, the `.lean`
docstrings carry it on both `quarkPhiClosedForm` and `splitting_value`, and the
tracking material sits in `authorNotes` where §4d puts it. Verified rather than
assumed — `scripts/lean-content-sweep.sh` **RED 0**, sorry-free, **zero
declaration lines touched**; `qa-sweep` cleared a `[major]
voice-author-notes-pollution` my first draft of the prose note earned (an ISO
date and a bean ID in body prose), which is why the split exists.

### The headline counts are stale, and one is a category error

| the headline | today |
|---|---|
| 174 live Python files on C | `convention-c-value-audit.py` (by VALUE, not shape): **85** bindings in `computations/`; shape audit **9–13 actionable** |
| 61 Lean files on C | **23 defs, 0 actionable, 23 deliberate** — and item 2 is in *none* of them |
| 49 content `.md`/`.ts` | **3** live unscoped (2026-08-29), now 2 with item 2's `.md` scoped |
| 3 convention HYBRIDS | **0** — items 1 and 3 were two of the three |
| "a SHIPPED PYTHON PACKAGE" | **not shipped.** `qou-mass` 404s on PyPI, has no `dist/` and no publish step; AGENTS.md corrects this |

**Re-scoped.** The P0 framing was right about the one thing that mattered — a
convention-C constant feeding a published CODATA comparison — and that is now
scoped rather than silent. What remains is the `z_D` re-derivation of
`quarkPhiClosedForm`, which is mathematics, not a sweep.

### Progress (Round 73 — PR litlfred/qou#8318)
- Formalized in PR `litlfred/qou#8318` (`feat/round73-symsquare-fibretl-mu3slot-sleak-deuteronz-43c1`, Commit 1 `d5360fac6f1464f5fd03c06ef76e726e30c785fd`, Head `e58aca150b7054a3222889e8bb9937602e515ca4`, `scriptHash: 19f0b8589c79`).
