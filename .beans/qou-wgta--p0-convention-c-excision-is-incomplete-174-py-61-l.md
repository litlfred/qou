---
# qou-wgta
title: 'P0: convention-C excision is INCOMPLETE -- 174 py + 61 lean + tools/ Rust core + a shipped package still on C, incl. 3 hybrids and the registry itself'
status: todo
type: bug
created_at: 2026-08-09T12:42:32Z
updated_at: 2026-08-09T12:42:32Z
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
