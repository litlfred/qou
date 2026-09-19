# A detector is blind to the shape it keys on

**Bean `qou-2ixd`.** Nine detector generations across the convention-C excision,
each of which reported the surface clear, and each of which was blind to a
*shape* rather than to a case. Written down because the pattern recurred often
enough in one arc to be predictive, and because two of the failures were in
tools built specifically to prevent the previous one.

## The claim

Every detector here failed the same way. Not by being wrong about what it
looked at — each was correct on its own terms — but by keying on a **structural
form**, and thereby being unable to see the same fact expressed in a different
form. The blind spot is never a missing case in a list. It is the shape of the
question.

## The forty-six

| # | detector keyed on | blind to | exposed by |
|---|---|---|---|
| 1 | literal decimal strings (grep) | the fifteen spellings of one formula | 70 → 13 → 178, two published miscounts |
| 2 | `1/(sqrt-ish + …)` | the half-argument form `r/(r²+1)` | `y_lambda_cyclotomic_factor.py:48` |
| 3 | assignment **targets** | a convention computed into a `return` | `pyhecke.gram.z_mp`, + 5 live producers |
| 4 | `z`-named bindings | closed forms **derived** from `z` | `trM_sigma1_sq`, `W2`, `census_hopf` |
| 5 | expression **shape** | `1/(t + 1/t)` where `q = t**2` | `qbeta_5two…probe.py:139` |
| 6 | the **registry record** | the record going stale behind the code | R9 red on main; 25 false "leaks" |
| 7 | **module attributes** (R9) | anything computed inside a function | `gram.z_mp()`, `tr_m_mp()` |
| 8 | **each entry independently** (R9) | entries disagreeing with *each other* | `pyhecke.gram` exporting C and D |
| 9 | **static** analysis | a derived form drifting from its own `z` | `TR_M[5] = z³` (2026-05-19) |
| 10 | **the producer** | a *per-anchor artifact* going stale on its own | `atomic-tr-m-mpfr-50dps-proton.witness.json` (#5190) |
| 11 | the **live code path** | prose that is the module's only convention statement | `markov_peel.tr_M_atomic`'s docstring (#5190) |
| 12 | the artifact's own **convention tag** | a tag accurate about the bytes and silent about currency | 9 colour-blind `chi-*` witnesses (#5209) |
| 13 | **`scriptHash`** — the staleness check itself | staleness arriving through a *dependency* | `pyhecke-h3-vs-h3a-impact-comparison` (qou-11wz) |
| 14 | **the file extension** — the tree the tool walks | an entire language's surface, never scanned at all | 7 convention-C sites in `.lean` (qou-cxjq) |
| 15 | **the declaration keyword** — `def`/`abbrev` only | a convention set by a typeclass **field assignment** inside an `instance` | `markovTraceTower_canonical` (qou-cxjq) |
| 16 | **the expression's SHAPE** — every matcher above | the same value under a sqrt-variable spelling, invisible in the *deliberate* bucket too | 21 sites `convention-c-producer-audit.py` reports in NO bucket (qou-t9r1) |
| 17 | **the EXEMPTION's shape** — the dispatcher / co-binding test | a two-arm comparison whose D arm is a **call** to the canonical helper, not an inline re-spelling | `he4_body_order_shortfall_location_probe.z_of` counted ACTIONABLE, and `--propose-ledger` would not stub it either (qou-1jny) |
| 18 | **the EXEMPTION's SCOPE** — co-binding checked within one scope | a two-arm comparison written as SIBLING `def z_C` / `def z_D`, so neither scope contains the other's binding | 16 of the 42 "solo" sites, i.e. 38 % of what looked like residue (qou-t9r1) |
| 19 | **the EXEMPTION's SHAPE, other side** — the D arm assumed to be a Markov parameter | a C-vs-D comparison whose D side is a derived closed form in `h`, never a `z` at all | `probe_convention_d_vs_c_borromean.py`, whose D is `tau_pipe = (4+h^2-3h^4-h^6)/(h^2+4)` (qou-t9r1) |
| 20 | **the EXEMPTION's LANGUAGE** — both arms assumed to be in the same file, hence the same language | a C-vs-D comparison whose D arm is a **Lean declaration**, so no Python-side pairing test can ever see it | `probe_h3_central_idempotents_exact.py` computes the C arm; its D counterpart is Lean `BorromeanMarkovTrace`, and `BorromeanTraceConventionSplit.lean` proves D ≠ C sorry-free (qou-t9r1) |
| 21 | **the GUARD's TYPE** — the anti-invisibility helper is mpmath-only (SCOPE: 1 measured site, NOT a wide class — see note below) | a SYMBOLIC (sympy) consumer cannot call `markov_parameter_convention_C` (`TypeError: cannot create mpf from q`), so it MUST inline `sqrt(q)/(1+q)` — invisible to the very mechanism built to make deliberate C visible | `probes/qbeta_fmap_power_class_prune.py`; helper made polymorphic 2026-08-30 (qou-t9r1) |
| 22 | the **argument-passing form** — positional `args` only | every keyword call, i.e. 87 % of the corpus's call sites | `self_fulfilling_assertion_audit` reported `MEASURED: 0` against a true 56 (qou-3e5m) |
| 23 | the **presence** of a field — every statement-strength matcher keys on a field that is present and *wrong* | a defect that is an **absent** clause: `RothGammaFull` lacked `two_le` and `degPos`, which made `RothLemmaTheta` false at `m = 1` | pre-fix `RothGammaFull` reconstructed; `limit-claim-encoding-audit.py` and `unbounded-quantifier-audit.py` both reported **0** (qou-4lbh) |
| 24 | the **declaration form** — every field-keyed scan begins at `class\|structure … where` | a carrier that is a `def … : Prop`, which is how this corpus states Mahler's Lemma 4 and Roth's Lemma | pre-fix `RothLemma4` reconstructed; `unbounded-quantifier-audit.py` reported `0 candidate(s) over 18 file(s)` (qou-4lbh) |
| 25 | the **assignment's proximity** — every literal-tracer follows a value to the call it sits in | a literal reaching an assertion through a **list slot**: `target_c[2] = sp.Integer(-1)` assigned 211 lines above `computed=float(target_c[2])`, so the assertion compares an input to itself and cannot fail | `qbeta_wenzl_habiro_ansatz_probe.py:479`; `assertion_on_literal_audit` reports it in NO bucket, confirmed by running it (qou-58zw) |
| 26 | the **key's lexical form** — every key scan reads `ast.Constant(str)` | a witness key written as a **keyword argument**, i.e. a Python identifier: `result(A_odd_preimage_positions_on_main_chain=v)` | `qcollatz_backward_tree_structure_probe.py:127`; `witness_key_orphan_audit`'s own first version reported three orphans sitting in plain sight in the file it was auditing (qou-58zw) |
| 27 | the **containment relation** — the matcher yields ANY dict carrying the field set | a **wrapper** whose child is the real record. Producers hoist `primal_obj`/`dual_obj`/`duality_gap`/`active_set`/`y0_star`/`y_star` onto a parent alongside a nested key holding the solve, so each solve counts twice — and because the hoisted copy omits `x_star`, the duplicate also manufactures a phantom "record with no primal vector" | `pn-alpha-lp-dual.witness.json` reported 41 records WITH `x_star` and 41 WITHOUT; they are the same 41 solves, x* one level down on `.lp_dual`. **54 of 241** matches corpus-wide were wrappers (qou-dke6) |
| 28 | the **value's shape at the key** — one match assumed to be one record | a **column-wise aggregate** carrying the same field NAMES with parallel lists across several solves. Discriminator: in a real record `y0_star` is a SCALAR | `nucleus-operator-selection-sdp.witness.json` `.data`, whose `y0_star` is a list of four nuclei; matched as a solve, then reported primal-less because an aggregate has no primal (qou-dke6) |
| 29 | the **key's exact name** — the primal looked up as `x_star` / `x_star_str` | a producer that **prefixes by half** when a row carries two solves | same witness: it carries `lp_x_star_str` AND `sdp_X_star_str`, and was reported as having NO primal while carrying TWO. One `grep` from "fixing" a producer that was already correct (qou-dke6) |
| 30 | a **numeric proxy for a structural fact** — `duality_gap != 0` taken to mean "a solve happened" | (a) producers that build dual-shaped records with **no solver call at all**, whose non-zero gap comes from elsewhere; (b) **closed-form duals** whose gap is 0 *by construction*, so x* is correctly absent | wrong on **6 of 9**: four no-solver producers, plus `sigma_f_electron_shell_chain` (27 records) which writes `"duality_gap": "0"  # closed-form => exact strong duality` and never calls a solver. Only the PRODUCER SOURCE decides (qou-dke6) |
| 31 | the **primal's arity** — a vector `x_star` assumed | an **SDP**, whose primal is the MATRIX `X_star`; a vector `x_star` is correctly absent | `gap_a1_binding_k_sdp_feasibility` → `solve_psd_operator_selection_sdp` (qou-dke6) |
| 32 | the **threshold's discrimination** — a ratio criterion assumed to separate two classes | a **cliff**, where the count measures where the threshold was placed rather than the corpus — and the criterion misses its own confirmed positive | `lp_floor_valued_objective_audit.py`: 62 flagged at fraction 0.96, **7 at 0.98**; and the one producer PROVED floor-valued by a `prec_bits` sweep ranks **59 of 146**. Shipped as a ranking and a recorded NEGATIVE, not a detector (qou-sof3) |
| 33 | the **write path** — the guard is installed at one of an API's several entry points | a producer using any of the others, however careful elsewhere. `WitnessBuilder` has **three** routes into the anchor vocabulary and the guard sits on one: `stamp_staleness_metadata(payload, q0_anchor=…)` is guarded; `save(extra)` is a bare `witness.update(extra)` with no validation; `wrap_legacy(payload)` carries the payload's keys through `_extra_top_level` and, per its own docstring, emits them "verbatim by `build()`" | the one live off-vocabulary producer travels the **third** route: `codata_corpus_literal_scan.py:816` sets `"q0Anchor": "not-applicable"` in a payload, so neither the existing guard nor a `save(extra)` fix could ever warn about it. Offered by the #6696 sibling (bean `qou-3ral`), which also corrected its own "two entry points" to three; structure verified here, counts measured independently at 256/25 against the sibling's 152/22 and NOT reconciled — see below (qou-3ral) |
| 34 | the **residual's name** — an identifier matching `delta`/`err`/`resid` taken to mean the quantity IS the residual, once it also reaches both sides of the comparison | an **error-propagation formula**, which mentions the measured quantities for exactly the same reason the residual does. `borromean_mass_MeV_err` is `sqrt((ratio_err*m_e)**2 + (ratio*m_e_err)**2)` — a 1σ propagated uncertainty, entirely correct, and indistinguishable from a residual by name plus reachability | found by running `tolerance_from_residual_audit.py` on a fix made WITH it: `mass-from-q-symbolic:599` was still reported blocking after being given an independent `expected`. The discriminator is that **a residual is a difference** — requiring a `Sub` in the provenance keeps the `qou-tol0` positive (`delta = M_derived - M_obs`) and drops the class. Note the tier had fired on NOTHING on main, so this was latent: **zero hits is not the same as verified sound**, and the audit doc claimed the second having measured only the first (qou-t0wm) |
| 35 | the **identifier's alphabet** — a bound variable matched with `[A-Za-z_][A-Za-z0-9_']*`, i.e. ASCII-only | a corpus that names its mathematical variables **κ, δ, λ, τ, ρ by convention**, so the pattern is not a narrow limitation but most of the search space. `EXISTS_EQ` in `scripts/lean-vacuous-existential-audit.py` — the detector written for the `∃ x, x = e := ⟨e, rfl⟩` class — could not match a single Greek-bound existential | same tree, same day, changing only that pattern: ASCII reports **0 candidates in 0 files**, which reads as a clean corpus; Unicode (`[^\W\d][\w']*`) reports **8 in 3 files**, every one bound to `κ`, `δ`, `τ_k`, `τ_joint`, `τ_x_k_stab`. Nothing had been drained — they had never been seen. Sharpens row 34's *"zero hits is not the same as verified sound"*: here the zero was reported **while eight instances lived**, and one of them had been NAMED in `2026-08-08-triviality-sweep-corpus-wide.md` a year earlier, so the sweep and the gate disagreed and only the gate was believed. Fixed with a `--self-test` whose first version **failed on two of its own negatives** — it asserted the pipeline's behaviour while exercising only the regex (`EXISTS_EQ` matches `∃ x, x = e ∧ P x`; the conjunct is excluded downstream by `_depth_split_ok`). A companion arm for the `∀`-prefixed shape was **measured before wiring** and is bounded at exactly one instance, already known (qou-ekga) |
| 36 | the **direction of the cast** — a float64 tier keyed on where a double ENTERS a computation | `float(<mpf>)`, precision **LEAVING**. The whole gate family guards f64 in — `mpf(<float>) source`, `f64-into-mpmath`, `raw-float64 ratchet`, `float64-padding ratchet`, `mixed mpf/f64 -> serializer` — and `F64_CAST` states the framing in its own note: *"the tier localises where a double ENTERS A COMPUTATION"*. Nothing covers the exit, which is the more damaging direction: `float(Q)` on an already-f64 `Q` loses nothing, while `float(mpf_50dps)` destroys 33 digits | `mass_binding_dashboard.py` appears **zero times** in the entire 22 KB `precision-gates.sh --changed` output, across all **23** tiers that ran, while carrying **four** `float(<mpf>)` downcasts that put a 1e-16 floor under its own printed accuracy claim (`max\|Δ\| = 8.9e-16 MeV`; the real value is 2.1e-49). Compounding it, the producer **emits no witness — it prints**, so every witness-keyed tier is structurally blind as well, which is exactly the case the "PROBES ARE NOT EXEMPT" directive is about. Discriminator, and the reason this is not simply "ban `float()`": `_disp` is the sanctioned exception — a downcast at the DISPLAY boundary is correct, one in a VALUE position is not (qou-4ohh) |
| 37 | the **numerator is an applied argument** — `RE_C_SQRTVAR = (\w+)\s*/\s*\(\s*\1\s*\^\s*2\s*\+\s*1\s*\)` in `scripts/lean-markov-convention-audit.py` binds `(\w+)` to whatever identifier sits before the `/`, and never looks past the closing paren | `coneCoordRow5 q := coneRow5Numerator q / (q ^ 2 + 1) ^ 2` (`toffoli-lp-stability.lean:590`): the `q` the regex took as the numerator is the ARGUMENT of `coneRow5Numerator q`, and the denominator carries a `^ 2` the pattern ignores. A rational function of `q` over `(q²+1)²` — convention-D by its own docstring — was reported `C-sqrtvar/actionable`, i.e. the sqrt-variable disguise of C. This is the mirror of rows 1-16: a **false positive** from the same shape-matching, which is the direction that costs an agent a "fix" of something that was right | measured 2026-09-06 (qou-htsi): the audit reported 24 C defs / 3 actionable on a tree where one of the three was this site. Guarded in `_sqrtvar_hit` (numerator identifier not preceded by an identifier char or closing bracket; denominator carries no exponent); 24 → 23 C defs, selftest still detects all 18 recorded C sites. Recorded because the next `q`-argument application over `(q²+1)^k` will match again if the guard is "simplified" away |
| 38 | the **value audit's variable resolution** — two spellings of a Markov parameter it cannot evaluate at all, in opposite directions | (a) `z_old = 1.0 / (q0**0.5 + qi0**0.5)` (`probes/nucleon-lp-convention-probe.py:87`) is `1/(√q + 1/√q) = z_C` exactly, but `qi0` is an IMPORTED inverse (`Q_INV`) the evaluator cannot bind and `**0.5` is not the `sqrt` call the sqrt-binding resolver keys on — so the value audit lists it **nowhere**, not C, not D, not unresolved. The shape audit sees it and files it under "probes / exploratory" (actionable) because it is named `z_old` rather than `z_C`, although the file is a labelled three-convention comparison (`OLD / HALF / D`). Neither detector describes the site correctly. (b) `inv = mp.mpf(1)/(Q0 + 1/Q0)` (`qbeta/qbeta_loop_value_pinned_probe.py:176`) with `Q0 = mp.mpf(Q0_STR)` is `1/[2]_q` on a **q**-variable — NOT C — and sat in UNRESOLVED because the fallback name list `_Q_VARS` had `q0` and `Q` but not `Q0`; UNRESOLVED is the bucket qou-t9r1 already recorded as invisible in both directions | (a) found 2026-09-06 by diffing the shape audit's `--list` against the value audit's `--all` on the same tree; the site appears in exactly one of them. Not adjudicable in the value ledger (the matcher only reaches rows the audit resolves), so it is recorded here and in the audit doc rather than "fixed". (b) `Q0` added to `_Q_VARS`; UNRESOLVED 1 → 0, NOT-C 5 → 6. Both are the same root the source already names — a name list inside an audit whose whole point is evaluating values — and the principled fix (resolve every variable at its binding, including `X = mpf(<q-string>)` and `X = 1/Y`) is not done |
| 39 | the **freshness is on the wrong object** — a staleness check asks whether the PRODUCER re-ran, or re-runs it and compares, and calls the witness fresh when it reproduces | a producer that ran AFTER a ruling and consumed inputs computed BEFORE it. `delta-lambda-empirical-tabulation.witness.json` stamps `computedAt 2026-09-06T06:47Z`, a day after the intra-ordering ruling (`7db032fb48`, 2026-09-05 07:53:55), and reads `chi-lithium-{5,6}-h{15,18}-…-matrix-m.witness.json`, last touched **2026-08-15**. A re-run reproduces its numbers exactly, because the stale input is stale in both runs — so the compare-against-a-fresh-run test, which is the strongest staleness test the corpus has, returns CLEAN. `computedAt` records when the producer ran, never when its inputs were computed; `witness_import_cone_staleness_audit.py` keys on **module** drift, not witness-**input** drift, so neither covers it | measured 2026-09-07 (qou-k54t). **The insulated case is the dangerous one and is invisible from outside**: a consumer that READS an intermediate witness is shielded from upstream change, while one that RECOMPUTES is not, and the two are indistinguishable — same script, same invocation, same output shape. Worked pair, same producer, same run: `binding-reeb-phase-decomposition.witness.json` sat at `computedAt 2026-07-06` on `main` **and through a 2026-09-07 commit that re-ran the consumer**, two months frozen. The light atoms (A≤4) read their per-partition data from it and did not move; the Li legs (A≥5) go through `rederive_large_a`, which recomputes from source every run, and moved ~30% immediately. The stability of the A≤4 half read as *agreement* and was in fact *not having looked* — it was recorded as "unmeasured" in `b47a1b949d` on exactly that reading. Discriminator: a witness is only as fresh as the OLDEST cache in its read cone, and no field in the schema records that |
| 40 | the **term as a substring** — a corpus-grep alternation carrying a bare unanchored alphabetic token, e.g. `grep -rliE "o'hara|ohara|..."` over `library/` | nothing. **This row runs the OTHER WAY, and is the first that does**: rows 1-39 are detectors that MISS, failing to a false ALL-CLEAR, which leaves the agent still looking. This one OVER-matches and fails to a false **COVERED** — the agent concludes corpus-grep path 5 is satisfied and STOPS. `ohara` is a substring of at least five surnames in this library: Shin**ohara**, Man**ohara**n, N**ohara**, H**ohara**, I**ohara** | measured 2026-09-13 (qou-zou6) on this repo's own subject. The unanchored grep reported **8 documents covering knot energy**; the true count is **0**. Decomposition, machine-measured: **7** documents are substring hits on those five surnames (14 hits, 0 whole-word), and the 8th is a SEMANTIC false positive — *Knots in the Skyrme-Faddeev model* really does contain the phrase "knot energy", meaning SOLITON energy. Whole-word `O'Hara` across BOTH the `sections/` and `ocr/` tiers: **0 documents**. Guard: `scripts/corpus-grep-overmatch-audit.py`, whose `--selftest` fails unless `ohara` is flagged AND the surnames are named AND `knot energy` is reported *clean* — pinning the limit as well as the catch, since no string test decides the semantic case. Two traps found by using it: my hand account said four surnames and the machine found five, and the missing one (`Hohara`) is in the document a hand re-check had reported as matching NOTHING; and the audit's own first output listed enclosing words **globally**, which let that word be attributed to the wrong document until `--show-words` was made per-document |
| 41 | the **query's character encoding** — corpus-grep path 5 typed in ASCII (`O'Hara`, `Mobius`, `Poincare`) against section text that preserves the source PDF's typographic Unicode (U+2019 apostrophe, precomposed diacritics) | the same name in the other spelling. **And it is BIDIRECTIONAL, which is what makes it unfixable by normalising one way**: neither form is a superset of the other, because a paper's body uses the typographic form while its own bibliography often ASCII-fies co-author names, and extraction sometimes strips diacritics. So no single canonical spelling is the right query | measured 2026-09-13 (qou-6xt9) over `library/*/sections/`, immediately after ingesting the knot-energy literature — **files matched, ASCII query vs Unicode query**: `O'Hara` **0 vs 48**, `Mobius` 5 vs 63, `Schrodinger` 16 vs 25, `Erdos` 8 vs 12 — but `Poincare` **190 vs 145** and `Kahler` **25 vs 18**, where the ASCII form is the BETTER single query. **U+2019 occurs in 5088 of 13671 section files (37%)**, so this is not a corner. The `O'Hara` row is the severe case and the one that bit: an agent running the natural ASCII query gets **zero** on 48 files that are right there — a false ALL-CLEAR on the corpus's own newly-ingested subject. **My own first reading of this was WRONG and is recorded because the error is the point**: seeing 0-vs-48 I concluded 'the Unicode form is the real one, search that' — guidance which `Poincare` and `Kahler` falsify. The correct rule is **search BOTH forms**, never pick one. Pairs with row 40 on the SAME query: bare `ohara` over-matches five surnames and fails to a false COVERED; `O'Hara` under-matches the apostrophe and fails to a false ALL-CLEAR. One term, both failure directions, opposite fixes — anchoring helps row 40 and makes row 41 worse |
| 42 | the **body SHAPE of a projection** — `detectSelfAssuming` matches a bare `ctx.field`, `by exact ctx.field`, a tuple of bare fields, and a tuple of APPLIED fields, but not an applied SINGLE field `ctx.field s t hst` | **the normal case.** A class field carrying a conclusion is almost always `∀ … → …`, so the theorem MUST apply it to the binders — a self-assuming projection with a universally quantified conclusion was invisible BY CONSTRUCTION. `pat` stays undefined and the function RETURNS BEFORE reaching its own `projectionTypeMatchesConclusion` fallback, the structural check that exists precisely for a field whose name escapes `CONCLUSION_FIELD` | 26 → 42 on the QOU Lean tree (2871 `.lean`), i.e. **16 bodies unseen**, every one passing the name gate. Found by fixing an instance the audit never reported — `mobius_frobenius_kernel.lean`, whose class docstring read *"All fields are inputs; none is the conclusion"* over a field that WAS the conclusion. 🛑 **The same repair had already been made one arity over**: `APPLIED_TUPLE_PROJECTION` exists, and its comment diagnoses this exact cause for tuples. Bean `qou-metc`, issue #7329 |
| 43 | **scan SCOPE on the ledger write path** — the `--review-ledger` deletion loop guards on category *ownership* (row 33's fix, added after it destroyed 116 of 268 entries) and not on whether the run ever opened the file | an entry whose file the scan never visited, which is indistinguishable to that loop from one whose candidate stopped flagging. **This is row 33 a second time on the same API** — the `--json` path three hundred lines up already refuses a partial scan, *"a partial scan would overwrite it with a smaller count that reads as a clean corpus"*, and the ledger path never got the rule | a `--review-ledger` run scoped to one subtree rewrote the ledger **−863/+67, destroying 106 of 329 entries** — all in categories the audit DOES produce, so the ownership guard preserved none of them. Caught in the `git diff`, not by any check. The ledger spans 22 roots across two papers; only 223 entries live under the scanned subtree | 
| 44 | the **WORDING of an exemption, as the ledger's key** — `--review-ledger` seeds only candidates whose `exempt_reason` matches `LEDGER_TRACKED_EXEMPT = /triage pending/`, and one of the two emit sites spells its reason *"tracked; **derivation** pending"* | every candidate taking that arm. The exemption is not a verdict here — it is a LANDING concession that is supposed to defer to an agent — so a mis-spelled reason silently converts "queued for a human" into "buried", which is the precise failure the ledger exists to prevent. **Row 43's sibling, one field over**: 43 is scan scope on the ledger write path, this is the ledger KEY on the read path, and both make the ledger quietly not-the-queue-it-claims-to-be | measured 2026-09-13 (beans `qou-metc` / `qou-vh1o`) on `main`, full corpus: flipping the literal to "triage pending" seeds **34** previously-invisible candidates — **21** `applied-field-projection` and **13** pre-existing (`applied-tuple-projection` × 6, `tuple-projection`-as-`def` × 7). 🛑 **The comment eight lines above the bug asserted the opposite in so many words** — *"The 16 it newly reaches still enter the review ledger, so `--check-ledger` demands an agent verdict on each"* (#7332, merged) — and **0** of them did; the population is also 21, not 16. Adjudicated: **15 genuine / 5 advisory / 1 legit**, and the 15 `genuine` verdicts promote through the existing `adjudicatedGenuine` path, taking the corpus from **56 → 71** counted defects. Calibration worth keeping: **all 21 match `CONCLUSION_FIELD`** (`claim_*` × 12, `*_holds` × 6, `exists_*`, `*_iff`, `*_eq`) — my own estimate before measuring was 14 — and the single `legit` is a name-gate match (`dH_eq`), so the name gate's one false positive here sits inside its 21/21 recall |
| 45 | **the expression's SPELLING, for an ALGEBRAIC signature** — a regex for `q**2 - 2*q - 1`, the factor identifying the Q_β base the owner retired on 2026-09-08 | **algebraically identical rewritings an author makes for good reasons.** Two live, both legitimate: the **absolute value PRE-RESOLVED** — `(2*q + 1 - q**2)`, written that way because `q₀²−2q₀−1 = −1.988 < 0` is known, so the source carries no `abs()` and no hint it is the same object — and the **Horner form** `q*(q - 2) - 1`. Distinct from rows 5 and 16, which are the *sqrt-variable* spelling of the Markov parameter: this is a different formula and the rewriting is SEMANTIC (a sign resolved by the author) rather than a change of variable | measured 2026-09-13 (`qou-pdix`, PR #7340). `qbeta_retired_z1_base_consumer_audit.py` reported **29** SINGLE-BASE `.py` files on the direct spelling alone; widened to five spellings it reports **42** — a **45 % undercount**, and the corrected set includes `qbeta_ck_cache.py`, the canonical `c_k` extraction producer. 🛑 **What exposed it is the reusable part, and it is a rule about AUDITS, not about this formula: the audit's calibration check was written as `check(..., True, ...)`** — a hardcoded pass — and was replaced with one that resolves three hand-found consumers to the bucket each actually landed in and **FAILS if any is missing**. It failed immediately: two of the three sat in MENTION-ONLY, impossible for a real consumer, so the classifier was wrong rather than the corpus. Had the hardcoded form stayed, **29 would have shipped with a clean 3/3 beside it**. An audit that self-certifies its calibration cannot discover its own blindness, which is why every row in this table needed a human or a failing check to find it |
| 46 | **the PROOF TERM'S GRAMMAR** — `scripts/lean-self-assuming-audit.py` had two rules, a bare binder and a single qualified projection, and the character `⟨` occurred NOWHERE in the file | **Lean's anonymous constructor, i.e. every conjunctive form of the defect it exists to find.** A theorem concluding `A ∧ B ∧ C` proved by `⟨X.a, X.b, X.c⟩`, where a/b/c are exactly the carrier fields declaring A/B/C, exited the candidate gate BEFORE its conclusion was ever parsed — invisible by construction, not missed case by case. Distinct from row 42, which is the same shape in the OTHER tool: there the constructor was handled and one *arity* was not | measured 2026-09-14 (bean `qou-wbtz`; audit [`2026-09-14-conjunctive-self-assuming-blind-spot.md`](2026-09-14-conjunctive-self-assuming-blind-spot.md)). `content/` (3852 `.lean`) **41 → 48**, the 41 pre-existing hits byte-identical by set comparison on (file, line, decl, variant); new variant `conjunction-is-conclusion` **7**, verdicts **7 genuine / 0 legit / 0 advisory**. 🛑 **Three sub-findings are worth more than the count.** (a) **It was already written down.** Bean `qou-9gpo`, 2026-08-31, says verbatim that the case "is MISSED by `scripts/lean-self-assuming-audit.py`: that tool needs the whole proof term to be a single identifier, so a conjunctive `⟨…⟩` of projections never matches" — correctly named, fourteen days open, so this row records a gap that was CLOSED rather than one that was found. (b) **The sibling TS detector misses three of the seven for reasons that are neither the shape nor a stale ledger**, and the cause was measured with controls rather than inferred from the ledger's silence (row 43): `TUPLE_PROJECTION`'s binder class is `[a-z]`, so `⟨H.degree_zero_vanishes, …⟩` fails on the **binder's CASE** and matches the instant the same body is lowercased; and JS `\w` is ASCII-only (`/\w/.test("Δ")` is `false`), so `⟨ctx.h_ΔE_exp, …⟩` fails on the **identifier's ALPHABET** and matches the instant it is ASCII-ised — row 35 recurring in a second tool and a second language, as a property of the regex ENGINE rather than of the author's pattern. The four the TS detector does see are exactly the four already adjudicated `genuine` in the review ledger, so the overlap is a clean two-way cross-validation and the complement is three declarations no detector in the corpus had ever flagged. (c) **The hand regex that motivated the work over-counted by 6 of 13**: four are `Iff` assemblies (including `q_bkm_criterion`, which AGENTS.md §3b-cond item 5 names the VERIFIED EXEMPLAR of the legitimate pattern) and two are structure-instance constructors that PERMUTE their components. Both are excluded structurally — `A ↔ B` and `S a b c` have no top-level `∧`, so no component count can agree — never by a name list, and the selftest pins the exemplar as a NEGATIVE fixture so the rule cannot widen onto it. |

### 33 — offered by a sibling, taken here to avoid a conflict on the count line (2026-09-04)

Row 33 is **not** this branch's finding. The #6696 sibling (bean `qou-3ral`)
measured it, checked it against all 32 existing rows, named row 21 as the
near-miss and explained why it differs — row 21 is one measured mpmath-vs-sympy
site where a caller *cannot invoke* a helper, whereas this is a second and
third entry point that **bypasses** the helper entirely — and then offered it
rather than adding it, because this PR holds the file and a second PR touching
the count line would conflict on exactly the line being maintained. Taken on
those terms; the finding is theirs.

**What was verified here, and what was not.** AGENTS.md is explicit that a
sibling's bean is not a primary source, so the structural claim was checked
against `tools/qou-substrate/python/qou_substrate/witness.py` directly:

- `stamp_staleness_metadata` takes `q0_anchor` — the guarded route. ✓
- `save(self, extra)` is `if extra: witness.update(extra)`. A bare update, no
  validation. ✓
- `wrap_legacy(payload)`'s own docstring states the keys land in
  `_extra_top_level` and are "emitted verbatim by `build()`". ✓
- `codata_corpus_literal_scan.py:816` carries `"q0Anchor": "not-applicable"`
  in a payload. ✓

**The COUNTS still do not reconcile, and the row now carries MINE with the
method attached.** The sibling reports **152** `wrap_legacy` callers of which
**22** set `q0Anchor`, measured at `6a9c2c44fb9`. Measuring here:

    files under computations/ MENTIONING wrap_legacy      280
    of those, an actual call `wrap_legacy(`               256   <- 24 are comment-only
    of THOSE, setting "q0Anchor"                           25

    same three numbers re-measured AT 6a9c2c44fb9         256 / 25  (identical)

So the gap is **not** drift — their commit gives the same figure as current
main — and not comment-mentions, which account for 24 of a 104-file difference.
Nor is it directory scoping: `computations/*.py` top-level only gives 123/4,
and excluding `probes/` and `audits/` gives 184/12. None is 152/22.

One asymmetry points at the answer without settling it: their set is both
*smaller* and *richer* in `q0Anchor` — 22/152 is 14.5 %, 25/256 is 9.8 % — so
it is a more specific filter than a subdirectory, plausibly witness-emitting
producers only. Their figure may well be the more meaningful denominator; it is
simply not reconstructible from what was published.

**Quote the method, not the number.** The command behind 256/25 is
`grep -rlE '(^|[^a-z_])wrap_legacy\(' --include=*.py computations/`, minus
`_deprecated`, intersected with `"q0Anchor"`. **The structural claim is what
makes the row; the counts only illustrate it, and this is the third figure on
this page whose two independent measurements disagree.**

### 27-32 — added 2026-09-04 (beans `qou-dke6`, `qou-sof3`), and ALL SIX blinded ONE detector

Unlike most of this page, rows 27-32 are not six detectors with one blind spot
each. They are **six blind spots in a single detector**, found one at a time
while it was used, and the sequence is the point:

    "107 of 241 f64-era/unattributable"  ->  1 live record
    "105 undeclared"                     ->  56   (row 27: 54 wrappers)
    "84 blind to the residual check"     ->  44 -> 15 -> 3 -> 0
    "should x_star be a required field?" ->  No, withdrawn

**Every correction made the problem smaller**, and one of them nearly reached
an owner: the `x_star`-as-required-field question was drafted on "84 records
blind to the certified-residual check". The real figure was 15, and requiring
the field would have turned **29 correct records into violations** (row 30's
closed-form duals) while helping a population that a per-producer fix closed
in two commits. A contract change would have *created* defects.

**What separates the classes that fooled this detector**: all six are about
the SHAPE of the data around the fields, never the fields themselves. A
wrapper, an aggregate, a prefixed key, a closed-form dual, an SDP matrix and a
threshold cliff all present *identical field names with plausible values*. No
amount of reading the numbers distinguishes them — rows 30 and 31 are only
decidable by reading the PRODUCER, which is what `_producer_solver` now does.

**The method that worked, again**: opening the witness instead of trusting the
report. Row 29 was caught because a producer the detector called defective had
a comment claiming it already spread `provenance()`; checking the witness found
`lp_x_star_str` sitting there. Row 27 was caught while costing an owner
question rather than while auditing. Row 30 was caught by surveying nine
producers before writing a fix for them — six had no `x_star` to serialize.

Rows 10, 11 and 12 came from a sibling (#5190, #5209), not from this branch —
recorded here because this is the list, and because 10 and 12 each break an
assumption the rest share.

### 25 and 26 — added 2026-08-30 (bean `qou-58zw`), and BOTH were found by spot-checking, not by reasoning

Row 26 is a near-neighbour of **row 22** and the pair is worth reading together:
22 is a detector that could not read a call's *arguments* because it looked only
at positional ones; 26 is a detector that could not read a *key* because a
keyword argument is an identifier and every key scan looks for a string. Same
underlying assumption — that the interesting text is a `str` in the AST — hit
from two directions, in two different audits, two days apart.

Row 25 is the assertion-side twin of the same family: a tracer that follows a
literal to its call site cannot see a literal parked in a list slot two hundred
lines earlier. `assertion_on_literal_audit` was written *for* vacuous assertions
and reports this one in no bucket at all.

**Both were found by spot-checking a detector's own output**, which is the only
method on this page that has ever worked. Row 26 in particular was found in the
output of the audit that introduced it: `witness_key_orphan_audit` reported
three orphaned keys that are visible on line 127 of the file it was auditing.
A detector's first count is a hypothesis.

### 15 — a convention set by an instance field, not a definition body

Added 2026-08-26 (bean `qou-cxjq`), by the scanner from entry #14 — **which had
this blind spot itself**.

`scripts/lean-markov-convention-audit.py` tracked the enclosing declaration with
`^\s*(?:noncomputable\s+)?(?:def|abbrev)\s+(\w+)`. A Lean typeclass instance
does not set its parameters in a `def` body; it sets them as **field
assignments**:

```lean
noncomputable instance markovTraceTower_canonical (q : ℝ) (hq : 1 < q) :
    MarkovTraceTower q where
  z := 1 / (Real.sqrt q + 1 / Real.sqrt q)     -- convention C
```

A def-only pattern cannot see that line as a *site*, so the scanner reported it
nowhere — through every run, while it was being used to drive a migration.

**The instance it hid is the worst one in the tree.** Not an obscure corner:
`markovTraceTower_canonical` is the **canonical** Markov trace tower, the
instance downstream Jones-value code resolves against. Fourteen `def`-shaped
sites were being carefully migrated while the canonical instance sat unmeasured.

Two things worth carrying:

1. **The count went UP when the blind spot closed** — 17 → 18 definitions,
   actionable 4 → 5. A migration that had been reporting steady progress was
   measuring a surface smaller than the real one. A falling count is only
   meaningful against a detector whose reach is known.
2. **This is the fourth consecutive entry found by the tool written to catch the
   previous one** (#12 → #13 → #14 → #15). The pattern is not that detectors are
   badly written; it is that each one encodes the shape its author had just
   learned to see. Expect a #16, and prefer the answer-shaped test — testing what
   a value *is* rather than how it was *written* — wherever one exists.

### 14 — the detector walks one tree and the count is quoted for the repo

Added 2026-08-26 (bean `qou-cxjq`).

[`scripts/convention-c-producer-audit.py`](../../scripts/convention-c-producer-audit.py)
walks the tree four times and every one is `base.rglob("*.py")` (lines 635, 760,
785, 930). It is a **producer** audit, producers are Python, and its numbers are
correct and correctly scoped. The blindness is not in the tool — it is in the
reading: a figure produced by a Python-only walk gets quoted as the corpus's
convention-C surface, and nothing else scans `.lean`, so that surface has never
been counted at all.

**Measured, once someone looked:** 7 convention-C Markov-parameter sites across
6 `.lean` files, and `markovZ` is **five declarations spanning both
conventions** — `z_C(q₀) = 0.49932…` against `z_D(q₀) = 0.61268…` under one
name.

Three properties make this different from #1–#13, and the third is the one worth
carrying:

1. **It is an absent measurement, not a wrong one.** Every prior entry is a
   detector returning a number that is wrong about the thing it scanned. This
   one returns a number that is right, about a tree that is not the corpus.
2. **Only 3 of the 7 are actually hard to see** — the square-root-variable forms
   `u/(u²+1)` and `s/(s²+1)` with `u² = q`, which share no lexeme with `√q/(q+1)`
   and do need the answer-shaped test. The other **4 write `Real.sqrt q` in plain
   sight**. So "a grep cannot in principle catch this" was too strong: mostly
   nothing had grepped.
3. **A migration can deepen the blindness while succeeding at its own goal.**
   The Tier-2 migration replaced `Real.sqrt q` with a generic
   `markovZ (u : R)` where `u² = q`. It removed the square root — its stated
   purpose — and left the convention untouched and *less* visible. When
   evaluating a migration, ask separately what it moved and what it merely
   renamed.

**The reading error this cost.** The bean that surfaced it reported AGENTS.md as
carrying a false convention-C all-clear for `.lean`. There is none: the single
"0 in `.lean`" claim in that document belongs to the **Λ vs Cl₂ naming** guard
(`qou-zdz5`). Two drains, both reported "corpus-wide", conflated by shape rather
than subject — inside a bean about detector blindness. Retracted in
[`2026-08-26-convention-c-in-lean-and-the-markovz-overload.md`](2026-08-26-convention-c-in-lean-and-the-markovz-overload.md).

### 13 — the staleness check said "current" about a stale witness

Every artifact here carries a `scriptHash`: `sha256(producer)[:12]`, compared
against the file on disk. It is the corpus's answer to *"is this witness stale?"*,
and it is used that way — a mismatch is how `qbeta-ck-cache.witness.json` was
proved frozen at convention C (row 10, with the hash as the proof).

It has a hole, and the hole is structural rather than a bug: **`scriptHash`
covers the producer FILE, not what the producer imports.**

`pyhecke-h3-vs-h3a-impact-comparison.witness.json` was materially stale after
`pyhecke/atom.py:691` migrated C → D, because that producer reaches it through
`from hecke_core import atom_per_generator_volumes`. Regenerating moved ten
payload fields:

```
.results[*].max_abs_delta   0.31762140405498  ->  0.40882936812595   (+28.7%)
.results[*].max_rel_pct     32.115175189754   ->  37.847030013816
```

and `scriptHash` read **`2b01c1d6a433` before and `2b01c1d6a433` after**. The
producer file never changed. The check that exists to answer "is this stale"
answered *no*, correctly by its own definition and wrongly in fact.

**Why this is worse than rows 6 and 10 rather than another instance of them.**
Row 6 is a *record* going stale; row 10 is an *artifact* going stale. Both are
caught by asking a checker. This is the **checker** going stale — a green
staleness gate over a stale artifact, which is the one configuration where
looking harder does not help, because the instrument agrees with the wrong
answer.

The repair is the same counter-move as everywhere else in this document: hash
what the run actually *depended on* rather than the one file it started from —
the transitive import closure, or at minimum the library modules the producer
resolves at run time. Until then, treat a matching `scriptHash` as evidence the
producer is unchanged, **never** as evidence the witness is current.

### 12 — a correct label on stale data

The hardest one so far, because **nothing in the artifact is wrong**. Nine
committed witnesses carry colour-**blind** `χ` for words that have a p–n
interface. No producer is at fault: `atom_canonical_crossings` emits exactly one
`averaged_weighted` crossing for every canonical Z≥1, N≥1 word. The **caches**
kept the old answer alive:

```
per_irrep_pole_deuteron_h6   if CHI_CACHE.exists(): return d
per_irrep_pole_atom          resume keyed on PARTITION COVERAGE alone
```

Neither has any notion of *which word* produced the cached entries, so a cache
written before colour-weighting looks complete forever.

**And the convention tag cannot catch it.** Those nine are tagged
`averaged-crossings` by `chi_convention_audit.py --fix` — a tag that is
*accurate about the bytes and silent about the drift*, because it records what an
auditing pass concluded about stored data, not what the current builder would
emit. Every row above is a detector failing to *find* a convention; this is a
detector finding one, reading it correctly, and being wrong anyway.

The repair is the same move as this document's counter-move, applied to caches:
derive the label from what the run actually built rather than from what is
stored. `convention_fingerprint` / `convention_label` in
`canonical_braid_crossings` are computed from the word
(`sigma:11+sigma_inv:7+averaged:4+averaged_weighted:1` for the deuteron) and
compared on cache read; it fired immediately on tritium.

**Carry this into any regeneration sweep.** Six of the tagged witnesses are
*correctly* colour-blind and must **not** be migrated — free words
(`include_inter=False`), dineutron, diproton and single nucleons have no p–n
bond to weight. Which is exactly why the label has to come from the word and not
from a filename pattern. Relevant to `qou-cdh3` and `qou-pvem`.

### 10 — "the producer is migrated" does not mean "every anchor's witness is"

Every other row on this table is a way of failing to find convention C **in the
source**. This one has no source defect at all: the producer is shared, correct,
and convention D. `atomic-tr-m-mpfr-50dps-proton.witness.json` held C values
(proton `1.065306`, deuteron `0.388357`) while its **muon sibling held D** —
because the proton file was last computed 2026-08-09, one day before the
migration commits, and those commits regenerated only the muon file.

A per-anchor artifact goes stale independently of the code that writes it. So
every clean producer-level audit in this campaign — including mine, including the
one whose "0 actionable" reading this document exists to retract — was answering
a question about *source* that says nothing about *artifacts*. `qou-cdh3` is the
tranche that has to close it, and rows 6 and 10 together are why it cannot be
discharged by re-reading code.

### 11 — the only convention statement in the module was the wrong one

`markov_peel.tr_M_atomic`'s docstring advertised `z = 1/(q^½ + q^{−½})` long
after the live path moved to `hecke_symbolic.z_markov = q³/(q²+1)`. `z` is named
nowhere else in that module, so the stale line was the **only** convention
statement a reader would find in the canonical peel entry point. It cost a
session: an `8.71e-8` residual in `Σ y_λ·χ^λ = tr_M` was attributed to a defect
in the weights, when the peel value had been read out of the *muon* witness and
labelled proton.

## The counter-move that beats all eleven: check the RESULT, not the source

The sibling's #5190 supplies the strongest detector in this campaign, and it is
strong precisely because it reads none of the things the eleven rows key on — no
literal, no binding name, no docstring, no registry row, no anchor, no source at
all.

The Markov peel returns an **exact integer-coefficient rational function of `q`**.
For the deuteron its denominator factors as

```
192·q²³·(q² + 1)³        <- verified in computations/peel-anchor-identification.witness.json
```

one `(q² + 1)` **per Markov peel**, because `z = q³/(q² + 1)`. Convention C's
`z = 1/(√q + q^{−½}) = √q/(q+1)` cannot produce that factor — it leaves
half-integer powers of `q`. So

> **`(q² + 1)` divides the denominator**

is a complete convention test on a symbolic result. It needs no source reading,
no `z` grep, and no anchor, and it is immune to rows 1–11 by construction: a
value cannot be stale, mislabelled, re-spelled, returned-instead-of-assigned, or
inherited from a stale record and still factor correctly. Asserted by
`computations/markov/peel_anchor_identification_probe.py`.

The general lesson, which is the one this document was missing: **every detector
here keys on how the convention was WRITTEN; the algebraic form of the answer
keys on what the convention IS.** Where a result is exact and symbolic, prefer
the second.

## The counter-move has its own failure mode: a tolerance set by the wrong arithmetic

Recorded 2026-08-23, from an instance of my own, because it runs **opposite**
to all thirteen rows above. Every row here is a false **negative** — the
detector misses a real violation. This is a false **positive**: the detector
flags a **correct** value as a violation.

It happened inside the counter-move this document recommends. Checking whether
`pyhecke.gram.z_mp` had been migrated to convention D, I compared its value
against `z_D` with an absolute tolerance:

```python
v = gram.z_mp(50)
label = "D" if abs(v - zD) < mp.mpf("1e-20") else "C"     # -> printed "C"
```

`z_mp` **is** convention D. It had been migrated on 2026-08-16 and its own
docstring says so. The detector said C.

**Why.** `z_mp` computes at 50 dps, but its input `q0` enters as a float64.
So the strongest agreement obtainable is ~1e-16, and a 1e-20 threshold cannot
be met by a correct value. The tolerance was set by the *strongest* arithmetic
in the chain rather than by the *weakest*, and the gap between them became a
verdict.

The measured numbers, which is how it was caught — the mislabelled value was
visibly `z_D` in the printout, not flagged by anything:

```
|z_mp - z_D| / z_D  =  1.29679e-17      <- correct convention
|z_mp - z_C| / z_C  =  0.227044
```

**The fix is to make it a comparison, not a threshold.** Ask *which candidate
is closer*, not *is it within ε of this one*. A relative two-way comparison
needs no calibration, survives any input precision, and cannot be defeated by a
mis-scaled ε: here it separates the two conventions by 16 orders of magnitude.

**Why this direction is the more dangerous one in this campaign.** A false
negative leaves a convention-C site undetected — bad, and the thirteen rows
above are about closing that. A false positive says *"this correct D value is
C"*, and the indicated remedy is to **change a correct value to the wrong
one**. In a campaign whose purpose is excising C, a false positive aims the
excision at the wrong target, and the resulting commit looks like progress.

**It recurred within the hour, in the same session, two commits after this
section was written** — which is the strongest argument for the rule and the
reason it is stated as one. Restoring a genuinely G-reading check to
`qbeta_crossing_weight_hecke_probe`, I asserted that the closed-form
q-antisymmetriser annihilates the Gram:

```
‖G·v‖_inf / ‖G‖_max  <  1e-40        # threshold chosen to match "50 dps"
```

It **failed at 7.11794e-18** against a *correct* radical. `gram_matrix_mp`
computes at 50 dps, but `q` was entering as the module's float64 `q0`, so the
cancellation cannot go below the float64 floor no matter what `dps` says.
Supplying `q` at 50 dps instead moves the same quantity to **2.64532e-50** and
the threshold becomes appropriate:

| how `q` enters | ‖G·v‖/‖G‖ |
|---|---|
| float64 `gram.q0` | 7.11794e-18 |
| 50-dps `11/10` | 2.64532e-50 |
| 50-dps substrate `q₀` | 2.6917e-50 |

The `dps` argument names the arithmetic of the *computation*; it says nothing
about the precision of the *inputs*. Two of these three rows are the same
`dps`.

**Practical rule.** When the counter-move is applied to an *exact symbolic*
result — `(q² + 1)` divides the denominator — it is threshold-free and the
concern does not arise; that is why the peel test above is strong. When it is
applied to a *numerical* result, the threshold is part of the detector, and it
must be justified by the weakest arithmetic on the path from `q0` to the value
being tested. State that justification, or use a two-way relative comparison
and avoid needing one.

## Four that are worth reading in full

### 3 — returned, not assigned

`scan()` matched an assignment whose *target name* contained `z`. So:

```python
def z_mp(dps=...):
    return +(1 / (_mp.sqrt(q) + _mp.sqrt(qi_)))
```

had no name to match and was invisible. `"178 → 0 actionable"` was never true;
adding return-scanning took it to 11, of which five were live producers in
`computations/`.

### 4 — migrating `z` is not migrating the file

`tr_M(σ₁²) = h·z + 1` holds for *any* Markov parameter. Written out at `z_C` it
becomes `1 + (q-1)/q^{1/2}` — and **the square root is `z_C`'s, not the
identity's**. So a file could migrate `z` to D and keep a closed form that
silently still described C. Four such sites, under names (`W2`, `W11`,
`trM_sigma1_sq`, `census_hopf`) that no `z`-keyed scan looks at.

The same identity existed in five copies. One of them — the sage example's —
drifted from the library and left `hecke_surface.py` **exiting 1 on main**.

### 5 — shape genuinely cannot decide it

```python
t = sp.symbols("t", positive=True)
q = t ** 2
z = 1 / (t + 1 / t)          # convention C
```

No `sqrt`, no `0.5`, not the `t/(t²+1)` form. And it is *character-for-character*
`1/(q + 1/q)` = `1/[2]_q`, the Temperley–Lieb loop reciprocal, which the
selftest requires **not** be flagged. The two differ only in whether the
variable is `q` or `√q` — a fact no expression shape carries. What decides it is
the file's own declaration `q = t ** 2`.

**A detector that reads only expressions cannot see a fact stated in a
declaration.**

### 6 — the tool inherits the record's staleness

`scan_reexports` derived its verdict from the registry's `blocked_migrations`.
`gram.py` migrated to D; the row still said `stays: C`. So the detector
faithfully reported 25 production sites "receiving convention C" that were
receiving D — and R9, which evaluates code rather than reading records, was red
on `main` the whole time.

This one produced a retraction (`qou-76a6`, scrapped). It is the sharpest form
of the pattern: **the failure the tool was built to find, arriving inside the
tool.**

### 7 — the expression wrapped in a numeric cast (added 2026-08-22)

Found by walking into it, not by looking for it: I went to work the Markov
keystone, read the probe that `MarkovTraceOnHecke.lean` cites as evidence for
ingredient 2, and found it binding

```python
z = float(+(1.0 / (mp.sqrt(Q_MP) + 1.0 / mp.sqrt(Q_MP))))   # = 0.4993203342 = z_C
```

`computations/probes/markov_reduction_h3_to_h4_verify.py:60`. The audit reported
**zero** sites for that file.

The blindness is one `isinstance` deep. Every shape matcher opens with

```python
if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
    return False
```

and the assigned value here is `Call(float, [UnaryOp(+, BinOp(Div, ...))])`, so
it bailed on the first line. Not a subtle shape — the C expression is written
out in full, in the canonical spelling the matcher was built for, one cast away
from visible.

**Fixed** by `unwrap_casts()` in `scripts/convention-c-producer-audit.py`:
strips unary `+`/`-` and single-argument calls to a known cast name (`float`,
`complex`, `mpf`, `mp.mpf`, `Decimal`) before matching. Deliberately
conservative — `Fraction(a, b)` and `round(x, n)` are multi-argument and are not
unwrapped, and `float(q**3/(q**2+1))` is still D. Eight new self-test cases
cover the spelling and those three negatives; the battery is 50 → 58 and every
pre-existing case still passes.

**Yield: exactly one new site**, and it is worth stating precisely because the
number is small and the temptation is to round it up. The other live site the
audit lists, `qbeta_h_frame_rungs_probe.py:73`, was **already** detected — it is
the plain unwrapped form and was the baseline run's "1 site". So the fix moved
the count 1 → 2, not 0 → 2.

**Why one site still matters here.** That site's conclusion is quoted in a Lean
docstring as the evidence for a keystone ingredient. The probe is also float64
end to end (`np.linalg.solve` for the Markov weights, `float(np.trace(M))`,
and a `mp.workdps(100)` block whose result is immediately cast to `float` —
the dps no-op the precision gates exist to catch). So a convention-C, float64
probe is standing as evidence for a general-`n` structural claim, and neither
gate saw it.

This is the fourth blind spelling found **by** a detector written to catch the
previous one, which is the pattern this document exists to record: each fix
closes a shape and reveals that the surface was never measured, only sampled.

### 8 — the intent is stated, but not where the detector looks (added 2026-08-26)

The last convention-C Markov parameter in the Lean tree,
`QOU.BraidsAndKnots.BorromeanCanonicalTraceDerivation.zMarkov`, was reported
`actionable` by `scripts/lean-markov-convention-audit.py` through fourteen runs.
It is not a defect. The module's **first line** reads *"Canonical (convention C)
Markov trace of β_Bor"*, and the whole file exists to derive the C value so that
`BorromeanTraceConventionSplit.conventionD_ne_conventionC` has something to
compare against. Migrating it would make the file derive D and compare it to
itself.

The blindness is structural, not a missing pattern. `_deliberate()` takes
evidence from the declaration's **name** and from its **own** doc-comment,
walking back from the declaration to the opener above it. Intent stated in a
module header, or in a consumer three declarations below, is outside that window
by construction — no widening of the window reaches it, because the evidence is
not adjacent to the declaration at all.

**Fixed at the source, not in the scanner.** The definition now says in its own
doc-comment why it is C and what breaks if it moves. The alternative — teaching
the scanner to accept a module header as deliberateness evidence — was rejected:
it would absolve *every* C definition in any file whose header mentions C, which
is the reassuring direction, and this document's whole subject is errors in that
direction.

**A near-miss worth more than the entry.** Reading the file, its "convention D"
is described by the weight triple `y₃ = [4]/[2]³`, `y₂₁ = 1/[2]²`, `y_{(1³)} = 0`
— the Temperley–Lieb / Jones decomposition. Reading `1/[2]` as the Markov
parameter gives `q/(q²+1) = 0.49729` at `q₀`, which is **not** convention D's
`q³/(q²+1) = 0.61269`; it is the bare kernel `g(q)`, and the separation theorem
`no_kernel_instantiation_is_conventionD` then proves it cannot be D. That is a
complete, self-consistent, Lean-backed argument that the corpus uses "convention
D" for two different objects — and it is **wrong**.

Computing the `z` the weights actually imply, against the character values the
file itself uses (`χ(σ) = q, h, −q⁻¹`), gives

```
y₃·q + y₂₁·h + y₁₁₁·(−q⁻¹) = (q³ + q)/(q + q⁻¹)² = q³/(q²+1)
```

exactly convention D. The error was reading `1/[2]` off the *shape* of the
weights in a normalisation that was never checked. Nothing in the corpus is
wrong; one afternoon of a false "letter collision" finding was avoided by
checking the arithmetic beside the name instead of the name — the same rule
AGENTS.md states for the Λ vs Cl₂ guard, one subject over.

**And the same character bit twice in one edit.** The doc-comment written to fix
this contained the literal opener `` /-- `` as prose. Lean nests block comments,
so the file failed with *"unterminated comment"* 120 lines later; and the
scanner's own walk-back found *that* opener first, so the site still came back
`actionable` with the marker sitting one line above the window. Two different
tools, one character, the same failure. Rephrased, and both are green.


### 16 — the sqrt-variable spelling, invisible in BOTH buckets (added 2026-08-29)

`z = 1 / (sq + 1 / sq)` where `sq = mp.sqrt(q)`, and its sibling `u / (u**2 + 1)`
where `u` is the square root variable. Both are `sqrt(q)/(q+1) = z_C` exactly.
`scripts/convention-c-producer-audit.py` matches neither.

This one is worth a row of its own even though blindness-to-a-spelling is the
theme of the whole document, because of *where* the loss lands. Every earlier
row costs a false **negative** in the actionable bucket: a defect goes
unreported. This spelling is invisible in the **deliberate** bucket too. The
audit does not under-report these sites; it does not know they exist. So the
usual reassurance — "the count is a floor, the deliberates are accounted for" —
does not hold, and an agent draining the actionable list to zero would declare
the excision complete with 21 convention-C bindings still live.

**Measured 2026-08-29 (PR #5972).** `scripts/convention-c-value-audit.py`
evaluates each binding at two sample points rather than matching its shape, and
finds **90 confirmed convention-C bindings** in `computations/` against the
shape audit's 71 rows. **Twenty-one** appear in no bucket of the shape audit.
Their dispositions on inspection: 4 already announced and deliberate (including
`schur_principal_mpmath._wenzl_constants_convention_C_HISTORICAL`, kept on
purpose as the one live C implementation the D-vs-C comparison quotes), 5
migrated in that PR, 4 blocked by a measured obstruction (`qou-pmkh`), 8 still
open (`qou-t9r1`).

**Confirmed from the other side, which is the part to remember.** Five of the
21 were registered in `blocked_on_rederivation` that same day. The audit's
printed count went from 9 actionable to 9 actionable. Registering a site the
detector cannot see changes nothing it prints — so a stable count is not
evidence of a stable surface.

**The counter-move.** Not another matcher. `convention-c-value-audit.py` walks
the AST for any binding whose RHS is a closed arithmetic expression in one free
variable, compiles it, and **evaluates** it against `z_C`, `z_D` and their
sqrt-variable forms at two independent points — one point is a numeric
coincidence, two is functional identity. It cannot be evaded by re-spelling
because it never reads the spelling. All arithmetic is `mpmath.mpf` at 60 dps:
a float64 evaluation bottoms out at ~1e-16 and could not separate `z_C` from a
near-miss, which is the failure the section below on tolerance describes.

**Its own limit, stated rather than papered over.** A `-sqrtvar` match is a
*candidate*: `x/(x**2+1)` is `z_C` when `x` is `sqrt(q)` and is `1/[2]_q`, a
convention-neutral quantity, when `x` **is** `q`. Nothing in the expression
distinguishes them — only what the variable *means* does. The report prints the
variable, triages on a name list, and reports `unresolved` rather than guessing;
on the current corpus that is 3 not-C and 1 unresolved out of 89.

**Two false positives from its own first run**, both fixed with regression
fixtures in `--selftest`, per row 3's lesson that a detector needs fixtures
pinning its narrowing: an attribute *base* counted as a free variable, so every
`mp.mpf(...)` binding looked like a one-variable expression; and NaN comparing
out of every inequality, so an `mp.mpf("nan")` sentinel "agreed" with whatever
it was tested against. Four sites reported, zero real.

## The counter-move that worked, twice

Numeric evaluation. R9 catches what R4/R5 cannot because a docstring and a
registry field can go stale *together* and still agree; code evaluated at `q₀`
cannot. R11 extends that to derived quantities: `z³` and `h·z²+z` are both
perfectly ordinary expressions in `z`, differing only in that one is right, and
**only evaluation distinguishes them**.

That is not an argument against static detectors — static scanning found sites
3, 4 and 5 — but against trusting them alone.

## The counter-move that failed

Breadth. The closed-form detector's first version matched any half-integer power
of `q` in a migrated file: **50 sites, nearly all legitimate**. `q^{1/2}` is not
a convention marker; it is `[2]_{√q}`, and it appears in Wenzl positivity, in
pair-skein formulas, and in the Jones change of variable.

`trace-convention-audit.ts` had already written this down —

> flagging those "would repeat the loose-grep error that once reported 70
> producers where the truth was 13"

— and it was repeated anyway, in a new detector, six weeks later. Narrowing to
trace/weight bindings took it 50 → 4. Most of that detector's selftest fixtures
now pin the *narrowing* rather than the matching, because over-breadth is its
whole risk.

## What the gates cover now

| rule | asks |
|---|---|
| R4/R5 | does the docstring match the registry? *(string vs string)* |
| **R9** | does the **code** return what the registry says, at `q₀`? |
| **R10** | do a module's symbols agree with **each other**? |
| **R11** | does a **derived** quantity match the `z` it was derived from? |

R10 exists because R9 checks entries independently: `pyhecke.gram` had `z`=D and
`z_mp`/`tr_m_mp`=C, all three accurately recorded, R9 confirming all three, and
nothing reported. A caller imports a module, not a registry entry.

## Practical consequences

1. **A local copy of a library value is a defect**, not a convenience. Five
   copies of one identity; the one that drifted broke an example on `main`.
   Canonical home: `closed_form_tau_M.trM_sigma1_sq` / `wenzl_weights_h2`,
   gated once by R11.
2. **A producer that runs at import cannot be gated by anything that imports
   it.** Three did, and rewrote their witnesses as a side effect of `import`.
3. **A detector needs fixtures that pin its narrowing**, not only its matching.
4. **Verify the premise of a record before deriving from it.** The registry is
   an input, not an axiom.

### Row 17 is the first that blinds an EXEMPTION rather than a detector

Rows 1-16 are all ways a defect escapes notice. Row 17 is the mirror image: a
site that IS a labelled comparison fails the test that would have excused it,
so it is reported as a defect forever and no amount of draining removes it.
Both failure directions cost the same thing -- a count nobody can act on.

It is also the second recorded case of one house rule blinding another. The
first (`_is_unit_numerator`, spelling #13) was the NO-FLOAT64 discipline:
writing `mpf(1)` instead of `1`, as the precision rule requires, made a site
invisible to the convention detector. This one is the DRY/canonical-helper
discipline: writing `return markov_z(q)` instead of re-spelling
`q**3/(q**2+1)` inline -- the maintainable choice, the one that survives the
next convention migration -- is what made the comparison look like a leak.

When adding an exemption test, ask what a COMPLIANT author would write, not
only what a careless one would.

### Rows 17-19 are one family, and they cost three passes to see

All three blind an EXEMPTION rather than a detector, and all three were found
the same way: by draining the previous one and finding the count did not fall
as far as it should have.

The convention-C excision surface went 86 -> 49 -> 32 blocking in a single
session, and each step revealed the next spelling:

  * 86 -> 49  adjudicating scope-level co-bound comparisons (37 sites).
  * 49 -> 42  seven co-bound sites whose docstrings do not frame them as
              convention work -- left for an eye, correctly.
  * 42 -> 26  row 18: the D arm as a SIBLING `def`, invisible to a scope-local
              co-binding test. 16 sites, 38 % of the apparent residue.
  * 26 -> 25  row 19: the D arm as a closed form in `h`, not a Markov
              parameter, so no z-shaped pairing test can ever find it.

**The lesson is about counting, not about z.** Every one of these inflated the
*residue*, so each intermediate figure looked like real remaining work and was
quotable as such. An agent reporting "42 sites left to excise" would have been
wrong by 38 % and would have had no way to know from the report alone.

**So: before quoting a residue, ask what would have to be true for a site to be
a legitimate comparison that this tool cannot pair.** That question is cheap and
it is what found rows 18 and 19; grepping harder for C is what found rows 1-16
and would not have found either.

### Row 22 is not about conventions at all, and that is the point

Added 2026-08-30 (bean `qou-3e5m`). Rows 1-21 all come from the convention-C
excision. This one comes from a completely different arc — the NO-FLOAT64
assertion-integrity work — and it is the same failure verbatim, which is the
first evidence in this file that the pattern is not an artifact of one
migration.

`computations/audits/self_fulfilling_assertion_audit.py` exists to catch
`add_assertion(name, X, X)`: an assertion that compares a value to itself,
cannot fail, and reports `passed: true`. It read its operands positionally:

```python
computed, expected = node.args[1], node.args[2]   # and skipped len(args) < 3
```

The word `keywords` did not appear anywhere in the file. Measured on the
corpus at the time:

```
add_assertion calls    487 positional    3300 KEYWORD
```

So it examined **13 %** of its own subject and reported `MEASURED: 0`. The
true figure, once it could see keyword calls, was **56** across 183 files —
and the case that exposed it was found by hand, not by the tool built for it
(`m_p_m_e_li2q.py:134` asserts `codata_mp_me_loaded` with computed and
expected both the literal `1836.152`).

**Two things generalise beyond this file.**

First, the blind shape here is *not* an expression form, a declaration
keyword, or an exemption's scope — the categories rows 1-21 are drawn from. It
is the **calling convention** of a Python function, which no previous row
touches. A detector that resolves a call's operands by position is blind to the
same call written with names, and in this corpus the named form is the
overwhelming majority. Any AST tool reading `node.args[i]` has this hole; grep
for the pattern before trusting a count from one.

Second, **the selftest passed through every wrong version, and its docstring
claimed it would not** — it said it *"guards against a future narrowing
quietly reporting a clean tree"*. It did not, because every fixture in it was
a positional call. A selftest written from the same assumption as the code
under test exercises the assumption's consequences, never the assumption. That
is practical consequence 3 above ("a detector needs fixtures that pin its
narrowing") arriving from a second, unrelated direction — and it is worth
strengthening: the fixture must pin the narrowing *in the dimension the author
did not think of*, which is the one dimension a same-author fixture reliably
misses.

## Provenance

Every count here is from a committed instrument, not a hand survey:
`scripts/convention-c-producer-audit.py` (selftest 42/42),
`scripts/convention-c-witness-audit.py` (16/16),
`content/pipeline/witness-substitution-audit.ts` (19/19),
`docs/coordination/trace_convention_registry_validate.py` (R9/R10/R11).

R11's negative test injected the historical `TR_M[5] = z³` bug and confirmed the
gate fires; the three published miscounts and one retraction in the table above
are recorded in `qou-2ixd` and `qou-76a6` rather than quietly fixed.

## Row 21's scope — a measured NEGATIVE (2026-08-30, qou-t9r1)

Row 21 is a real defect (`markov_parameter_convention_C` raised
`TypeError: cannot create mpf from q` on a sympy Symbol, so a symbolic
consumer could not call the guard built to make deliberate C greppable), but
it is **narrow**, and the obvious follow-up hypothesis — *"then many symbolic
consumers must have inlined C for the same reason"* — was tested and is
**FALSE**.

Surface searched: every `.py` under `computations/` and `tools/` that imports
sympy AND contains a C-shaped `sqrt(q)/(1+q)` text match — 46 files. Against
the value audit's four buckets (BLOCKING 30, ADJUDICATED 61, UNRESOLVED 2,
NOT C 3) and the ledger:

| | count |
|---|---|
| sympy-importing files with a C-shaped TEXT match | 46 |
| of those, BLOCKING in the value audit | 30 |
| of those, adjudicated in the ledger | 18 |
| of those, in neither | 16 |
| **of those 16, actual convention-C BINDINGS** | **0** |

The 16 break down as **15 comment/docstring mentions** and **1 tuple of
string-literal search tokens** (`gswz_program_convention_immunity_probe.py:88`,
`Z_TOKENS = ("z_C", "z_D", "sqrt(q)/(q + 1)", ...)`).

**So the value audit has no symbolic blind spot of this kind, and the count
that looked like one was an artifact of grepping TEXT where the audit
evaluates BINDINGS.** Recorded because the wrong version of this finding — "16
files invisible to the audit" — was one commit away from entering the corpus,
in the document whose subject is detectors that mis-measure. The distinguishing
observation is cheap and should be run before any similar claim: strip
comments, require an assignment, and check whether the right-hand side is an
expression rather than a string.

Only **one** site was ever affected by row 21
(`probes/qbeta_fmap_power_class_prune.py`), and it is fixed.

> **Renumbered twice on merge (2026-08-30).**  These two rows were written as 18 and 19 on the
> Roth arc while `main` was independently using 18 and 19 for the convention-C exemption family
> above; they became 22 and 23.  Later the same day `main` claimed 22 for the argument-passing
> row (`qou-3e5m`), which by then had a prose section and outside references in
> `computations/audits/vacuous_green_witness_audit.py` and `.beans/qou-srvu`, so the Roth rows
> moved again and are now **23 and 24**.  Nothing about their content changed either time.
>
> The collisions are recorded rather than silently resolved, because a reader meeting a
> cross-reference to "row 18" or "row 22" in either arc's commit history needs to know which was
> meant.  That this happened twice in one day is itself the lesson: **a shared append-only numbered
> list has no allocator**, so concurrent branches collide by construction, and the collision is
> invisible to `git merge` — both times it merged clean and both times the numbering was wrong.

### 23 — the defect is an ABSENT field, not a wrong one

Added 2026-08-29 (bean `qou-4lbh`), from the Roth's-Lemma arc.

`limit-claim-encoding-audit.py` and `unbounded-quantifier-audit.py` are the two axes of the
statement-strength question — *weaker than its prose*, *stronger than the truth* — and both
scan `class|structure … where` and key on a field that is **present and wrong**.

The Roth arc's `RothGammaFull` was defective twice (corrections 16 and 20) because it **lacked**
a clause. Every field it carried was correct; `two_le` and `degPos` simply were not there, and
without them `RothLemmaTheta` was **false at `m = 1`** — a counterexample exists and is recorded
at `RothVariableSplit.RothLemma4`. A hypothesis structure missing a clause is a *weaker
hypothesis*, hence a *stronger theorem*: the same direction as rows 1–17, reached by absence.

No field-shaped matcher can see an absence. Confirmed rather than argued: the pre-fix
`RothGammaFull` was reconstructed and both detectors reported **0**.

### 24 — the carrier is a `def : Prop`, not a `class` or `structure`

Same bean, same probe.

`RothLemma4` and `RothLemmaTheta` are `def … : Prop` — which is how this corpus states Mahler's
Lemma 4 and Roth's Lemma, because they are *statements to be proved*, not typeclasses to be
instantiated. Every field-keyed scan in `scripts/` begins at `class|structure … where`, so a
proposition-valued `def` is outside the tree the tools walk.

Correction 25 lived there: `RothLemma4`'s `w`-encoding read `w = Ψ ∨ w² = Ψ`, whose second
disjunct demands a **rational square root** of `Θ' + t`. In the regime §14 runs in (`Ψ < 1`,
where the `√` branch is the operative one) nothing produces one, so the `def` was
unsatisfiable — `False` was not derivable from it, it simply could not be proved. The pre-fix
form was reconstructed and `unbounded-quantifier-audit.py` reported **0**.

This is row 14 one level down. Row 14 was *a language never scanned*; this is **a declaration
form never scanned**, inside a language the scanners do walk. The generalisation both rows
share: the tool's reach is set by a syntactic anchor chosen for the first case it was built
for, and the anchor is invisible in its own output — a `0` from a scan that never reached the
declaration looks exactly like a `0` from a scan that cleared it.

⚠ Practical consequence for `scripts/`: a run over the 18 Roth/Wronskian/Separated modules
reports `0 candidate(s) over 18 file(s)` from both statement-strength detectors, and that number
is true and means nothing. Neither script reports how many *declarations* it reached, only how
many files it opened — so there is no signal in the output distinguishing the two cases.

### 40 — the first row whose failure is a false COVERED (added 2026-09-13)

Every row above is a detector that **misses** something. The shape is always the
same: the scan returns a number that looks like a clean bill, and the agent
keeps working on the assumption that the surface is clear. Row 34 states the
generalisation — *"zero hits is not the same as verified sound"*.

Row 40 is the mirror, and it is the more expensive direction.

A corpus-grep term that matches as a **substring** of longer words reports
documents that carry none of the topic. The agent reads a document count,
concludes corpus-grep path 5 is satisfied, and **stops looking**. A miss leaves
you still searching; this ends the search with the wrong answer.

**The worked case is this repository's own subject.** Running path 5 for
knot-energy literature with a bare unanchored `ohara` in the alternation:

| | documents |
|---|---|
| reported by the unanchored grep | **8** |
| substring hits on surnames (`Shinohara`, `Manoharan`, `Nohara`, `Hohara`, `Iohara`) | 7 |
| semantic false positive (`knot energy` = Skyrme-Faddeev **soliton** energy) | 1 |
| **actually carrying the topic** | **0** |

Whole-word `O'Hara` across both the `sections/` and `ocr/` tiers returns **zero
documents**: the library holds no knot-energy source at all. That absence is
the finding the over-match was concealing, and it matters — bean `qou-bn8e`
needs O'Hara's theorem and the corpus cannot cite it.

**Why a guard is possible here when most rows only get a caveat.** The
substring case is decidable: compare the unanchored match count against the
whole-word match count, and report the *enclosing words*. That turns "8
documents cover knot energy" into "0 documents; 5 surnames", which is
immediately actionable.
[`scripts/corpus-grep-overmatch-audit.py`](../../scripts/corpus-grep-overmatch-audit.py)
does exactly that, in ~4 s over both tiers.

**The limit is pinned, not merely stated.** The semantic case — a term matching
as a genuine word in a document about a different subject — is *not*
mechanisable, so the script's `--selftest` asserts that `knot energy` is
reported **clean**. If someone later widens the check until it flags that too,
the selftest fails, because the script would then be claiming a judgement it
cannot make. A detector that pins its own limit is the part worth copying.

**Two traps, both found by running it rather than by writing it.**

1. **The hand account was short by one surname, and the missing one was in the
   document a hand re-check had cleared.** I reported four surnames; the
   machine found five. The fifth is `Hohara` — "S. Hohara" in a reference list
   of `arxiv-2007.15570v1`, which an earlier by-hand extraction had reported as
   matching *nothing*. So the document that looked like the one benign case was
   the one carrying the unrecorded spelling.
2. **The audit's own first output was not attributable.** Enclosing words were
   counted into a single global `Counter`, so the report named `Hohara` without
   saying which document held it — and it was promptly attributed to the wrong
   one. Fixed by making `--show-words` report per document; the global list is
   now labelled a summary in the output itself. This is row 27-32's family
   (*the shape of the data around the field*) reappearing inside a brand-new
   detector, one hour old, written by someone who had just read those rows.

**Note on the count line in AGENTS.md.** That document said "**thirty-five**
rows" when this row was added and the true count was 39. It has now been stale
six times (13 → 16 → 18 → 22 → 35 → 39). Re-count the table; do not quote the
sentence.
