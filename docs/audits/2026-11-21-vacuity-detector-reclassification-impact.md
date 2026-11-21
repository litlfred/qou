# Remaining Lean vacuity detectors: measured reclassification impact

Measured 2026-11-21 on `main` at `313bff6b2c7` (4,476 `.lean` files under `folio/`), against
`docs/audits/lean-vacuity-review-ledger.json` (308 entries, updated 2026-11-21). This measurement was
taken before any rule changed; the owner then ruled (see "Decision" at the end).

The vacuity ledger is keyed `file::decl::category`. A detector change "reclassifies" it if it moves an
existing entry (a candidate disappears, or changes variant) or adds unadjudicated candidates.

## Summary

| bean | what changes | new candidates | existing ledger entries moved | where the code lives |
|---|---|---|---|---|
| qou-1ccx | anonymous instance binder `[C X]` + `C.field` enters rule 2 | **+5** | **0** | `scripts/lean-self-assuming-audit.py` (qou) |
| qou-0exp | rule 4: `(h1 : A) (h2 : B) : A ∧ B := ⟨h1, h2⟩`, plus `by exact ⟨…⟩` / `And.intro` unwrapping | **+2** (0 from rule 4 itself) | **0** | same script (qou) |
| qou-sibdup | new cross-file check: a hypothesis equal to a sibling block's conclusion | 0 with a specificity filter, 232 pairs without | n/a (new category) | new script (qou) |
| qou-ommr | prose mention of a `:defterm` before its definition in reading order | 43 bare + 45 `:refterm` (body-defined terms) | n/a (not a vacuity check) | `pipeline/validate-defterm.ts` (**cat-harness-tools**, not qou) |

## qou-1ccx: anonymous instance binder

**What it means.** Rule 2 of the self-assuming audit flags `theorem t [ctx : C] : P := ctx.claim` where the
class field `claim` is declared with type `P`. When the binder has no name (`[C X]`), the projection must
be written `C.claim`, the binder map has no key, and the theorem is skipped. The fix (already written, in
the stale PR #8350, commit `35175f8`, last touched 2026-11-17, now conflicting) keys anonymous binders by
their class name. The same hunk also makes the `:=` split depth-aware, so `(vd := vd)` inside a proof term
no longer steals the split.

**Measured.** Baseline 35 candidates; with the fix 40. No candidate is lost, so none of the 23 baseline
hits that are already adjudicated in the ledger moves. Split by change: the anonymous binder alone gives
+4; the depth-aware split alone gives 0; together +5 (the split is what lets `variational_transport`
through). The five, none in the ledger yet:

- `lean/QOU/QuantumObservableUniverse/GaugeTheory.lean:226` `variational_einstein` := `HasCategoricalEOM.einstein`
- `…/GaugeTheory.lean:238` `variational_yang_mills` := `HasCategoricalEOM.yang_mills`
- `…/GaugeTheory.lean:250` `variational_transport` := `HasCategoricalEOM.transport`
- `q-geometric-langlands/tannaka-krein-isomorphism.lean:102` `tannaka_krein_isomorphism` := `IsTannakaKreinDual.equiv_over_fibre`
- `appendix-qvalues/qbeta-ck-truncation-canonical.lean:86` `qbeta_ck_truncation_canonical_conjecture` := `QbetaCkTruncationCanonicalExists.exists_c`

The three GaugeTheory ones were already confirmed by hand in the bean. The bean's "91 shape matches"
counted binder-and-projection shape only; rule 2 also requires the field's declared type to equal the
conclusion, which 86 of those 91 do not meet. So the bean's fear (row 43 of the detector-blindness
taxonomy, where widening this script destroyed 106 adjudications) does not repeat here: 0 destroyed.

**Cost.** Port one hunk of PR #8350 (about 40 lines plus a selftest unit) onto main, and add 5
`needs-agent` ledger rows. **Risk.** Low; selftest passes; reversible. **Commits to.** Adjudicating the 5
(the GaugeTheory three are a §3b-cond item 5 pattern: the class axiomatises the equation of motion that
the theorem then "derives").

## qou-0exp: hypothesis re-packaging

**What it means.** The escaped case was `(h_pos : 0 < ε) (h_inf : ε < 1) : 0 < ε ∧ ε < 1 := ⟨h_pos, h_inf⟩`.
Rule 3 only accepts tuple components that are fields of one class binder (`b.f`); bare hypotheses were
never considered. The prototype adds rule 4 (every component is a bare explicit hypothesis whose type is
the matching conjunct) and unwraps `by exact ⟨…⟩` and `And.intro a b` so rules 3 and 4 see them.

**Measured.** Fixtures: the original surreal-squeeze shape, `And.intro`, `by exact`, and a reordered
`⟨hb, ha⟩ : b ∧ a` are caught; `⟨ha, hab ha⟩` (real work) is not. Corpus: rule 4 itself finds **0**
(surreal-squeeze was already rewritten), the unwrapping adds **2** rule-3 hits:
`FluidDynamics/acoustic_horizon_conditions.lean:99` `acoustic_horizon_regularity` (new) and
`FluidDynamics/discrete_vortex_spectrum.lean:87` `discrete_vortex_spectrum` (already in the ledger as
`needs-agent`, so it only gains a detector source). No existing entry moves.

**Not covered.** 39 `exact ⟨h…, h…⟩` lines sit inside multi-line tactic blocks, where earlier tactics
may have derived the components; a static pass cannot judge them (needs elaboration, the triviality
probe's job). The five QA criteria named in the bean title (`proof-no-trivial-true` etc.) are sidecar
criteria in cat-harness-tools and are not touched by this change.

**Cost.** About 30 lines plus fixtures, in the same PR as qou-1ccx. **Risk.** Low. **Commits to.** 1 new
ledger row.

## qou-sibdup: hypothesis assumed in one block, proved in a sibling

**What it means.** Content-block `.lean` files cannot import each other, so a block may assume as a
hypothesis what the file next to it proves. The prototype collects, per chapter directory, every
theorem's explicit hypotheses and every theorem's conclusion, alpha-renames each declaration's own
parameters to positions, and reports a hypothesis equal to a sibling file's conclusion.

**Measured.** It catches the worked case (`hw : ∀ i, ‖W.eigenvalues i‖ = W.q ^ (1/2 : ℝ)` vs
`hasse_weil_bound`) on a fixture. On the corpus (947 content-block files, 4,610 explicit hypotheses, 3,167
conclusions): **232 pairs at 127 hypothesis sites in 9 chapters**, almost all generic side conditions
matched by generic lemmas: `q ≠ 0` 105 times (against `complex_q_ne_zero`, `xi_ne_zero_of_mul_hbar_sq_eq`),
`s ≠ 0` 12, `0 < q` 10 (against `pos_of_mem_magicSet`). With a filter requiring the matched statement to
name at least one non-parameter identifier of 3+ characters, the worked case still hits and the corpus
gives **0**. The original instance was fixed by the WeilZeta library lift (qou-qspc).

So the defect is real but currently absent, and a syntactic match cannot tell "the sibling proves it
under hypotheses I also have" from "the sibling proves it under different hypotheses".

**Options.** (a) Land the filtered version as an advisory regression guard, no ledger category, reports
0 today. (b) Land the unfiltered version and adjudicate 127 sites (mostly noise). (c) Leave the bean as a
design note. **Recommendation (my judgement):** (a). It costs one script and a fixture, and adds nothing to
the ledger.

## qou-ommr: prose forward-reference to a defined term

**What it means.** Extend `validate-defterm.ts` to warn when a block's prose mentions a `:defterm` label
before the defining block in reading order. This code lives in **litlfred/cat-harness-tools**, not qou,
and is a reading-order check, not a vacuity check, so it does not touch the vacuity ledger.
`validateDefterms` currently receives blocks as an unordered map, so the change also needs the chapter
order (the `sections[].blocks[]` order that `detangler-no-forward-ref` already builds).

**Measured** on qou in paper order (37 chapters, 3,685 blocks, 53 `:defterm`s): 122 bare prose mentions
before the definition, in 95 blocks, for 25 terms. **79 of the 122 point at definitions in the glossary
chapter**, which is back matter and therefore always "later". Excluding those: **43 mentions in 38
blocks, 12 terms** (top: `photon` 15, `descent` 11). Separately, **45 `:refterm[…]` links** point forward
to a block defined later (13 in `quantum-universes`, 8 in `mass-endomorphism`).

**Options.** (a) Warn on body-defined terms only, glossary definitions exempt. (b) Warn on everything
(122 + 45, mostly the glossary design). (c) Leave it. **Recommendation (my judgement):** (a) as a
non-blocking warning, PR on cat-harness-tools.

## Decision and what landed

Owner card 2026-11-21, option "All four as recommended" (recorded in
`docs/coordination/owner-rulings.md`).

- `scripts/lean-self-assuming-audit.py`: the PR #8350 hunk for anonymous binders and the depth-aware
  `:=` split (qou-1ccx), and rule 4 `hypotheses-conjunction-is-conclusion` with `by exact` / `And.intro`
  unwrapping (qou-0exp). Full corpus after the change: 42 candidates (34 class-field, 8 conjunction,
  0 rule 4), the 35 + 5 + 2 measured above. Selftest units cover the anonymous binder, the four caught
  spellings, and the `⟨ha, hab ha⟩` negative.
- `scripts/lean-sibling-hypothesis-audit.py` (qou-sibdup): advisory, filtered, exits 0, no ledger
  category. 0 matches on the corpus; `--unfiltered` reproduces the 232; `--selftest` pins the worked case.
- Ledger: 6 new `needs-agent` rows. They use the category `proof-self-assuming-projection-py`, not
  `proof-no-self-assuming-projection`, because the TS audit (`folio/pipeline/lean-vacuity-axiom-audit.ts`)
  owns that category and its `--review-ledger` deletes owned entries it cannot reproduce; its binder
  parser skips anonymous instance binders and it does not unwrap `by exact`, so it would drop all six.
  Porting the two changes into the TS audit is a follow-up.
- qou-ommr: separate PR on litlfred/cat-harness-tools.
