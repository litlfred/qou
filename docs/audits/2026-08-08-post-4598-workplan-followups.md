# Post-#4598 workplan follow-ups — Δ_λ ℓ¹ consolidation, b₄ scalar, c₃ fibre-Habiro, m_K/m_π truncation (2026-08-08)

Branch `claude/q-deformed-saddle-offsets-bdn992` (PR #4794). Session milestone
bean `qou-9d3x`. Five-front workplan after PR #4598 merged; this records the
foreground doc-consolidations and the two parallel-probe confirmations. Nothing
wired; no closure; every result is an honest negative, a scoping, or an integrity
caveat.

## Task 1 (qou-j6e4) — Δ_λ ℓ¹-ceiling consolidated into the durable ledgers ✓

The 2026-08-07 ℓ¹-ceiling probe (`free_parameters = 0`) proved
`Σ_λ|y_λ χ^λ Δ_λ| ∈ [0.36, 0.59]·target` across D/T/³He/⁴He *with perfect
interference*, so **no re-derivation of Δ_λ can close binding** — a new additive
≥4-body term is required (must supply 41–64 % of each target alone). This was
proved but not cited in the durable ledgers, so agents kept re-running dead
"better Δ_λ" ansätze. Now consolidated into `docs/precision-goals.md` (Δ_λ gate)
and `docs/coordination/delta-lambda-magnitude-derivation.md` (STATUS banner).

## Task 2 (qou-fapk) — the b₄ scalar `m` has NO forward-forced value (scope-(a))

Independent second-route confirmation of the standing `qou-k4ud`/`qou-9nq9`
verdict. The decisive structural fact, Lean-backed:

- **Physicality ceiling `m < 1/√5`** (`det(I+mS)=(1−5m²)(1−m²)>0`,
  `A4InterfaceMagnitude.detG_eq_spectral_product`) prunes the entire *primary*
  Σ(2,3,5) amplitude set (all overshoot); only secondary powers survive, none
  structurally distinguished — selecting one is a menu-fit.
- **`b₄(m) = −ln det(I+mS)` is a strictly-increasing bijection `(0,1/√5)→(0,∞)`**
  (`b4_strictMono_on`, `magnitude_form_surjective`, `option-e.md:1039`). So the
  target→`m` map manufactures a value for **any** target: "pick the `m` that lands
  `B(⁴He)=28.30`" is a fit machine that cannot *not* match. A forward `m` requires
  an independent categorical principle fixing it *before* any AME comparison —
  none exists in the corpus.
- The only *derived* object, `g_reeb = 1/√(1+[2]_v²) ≈ 0.4467`, is the **pole**
  (`b₄→+∞` there), not a finite closing `m`; the finite cumulant target
  `m*≈0.4164` is bracketed by derived constants but matched by none.

**Disposition:** the open object is *not* the scalar `m` — it is the pole
regulator of the near-critical α-condensation (species-symmetric) mode (route to
`qou-9nq9`, `qou-prjo`). Do not re-select `m`; any `m` fitted to `B(⁴He)` is the
forbidden ansatz.

## Task 4 (qou-68ge) — Q_β c₃ fibre-Habiro: VALUE proved-closed, SHAPE open

Independent confirmation of the canonical framing (registry §1). The object splits
cleanly:

- **VALUE leg — PROVED-CLOSED (measurement-limited), scope-(b).** No
  anchor-invariant fibre datum equals the swinging c₃ carrier
  (`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`,
  `MeasurementLimitedFloor.lean`, sorry-free). A fibre-Habiro element cannot
  supply the c₃ *value* below the experimental Q_β floor.
- **SHAPE leg — OPEN.** A fibre derivation *can* supply the bar-odd carrier's
  *shape*. The one cheap, falsifiable, not-yet-run step is **`qou-jcmw`**: compute
  `dim HH¹(H₅(ζ₅))` at the Bring root of unity and test whether the outer class's
  action on the cocenter HH₀ is bar-odd (right kind of carrier) or bar-even (dies
  to the KC21 bar-parity invariant). Even full success gives only the shape — the
  value stays measurement-limited.
- **Proved exclusions to respect:** KC20 (real-q/quadratic c₃ excluded — cubic
  `C(y)` irreducible), KC22 (bar-odd D-ladder non-(q-)holonomic → resurgent, not
  a q-difference recursion), #4293 (c₃ swing non-categorical at strictly real q₀).

**Disposition:** `qou-68ge` is subsumed by the live `qou-jcmw` under milestone
`qou-93jy`. Do **not** spawn a 7th c₃ closed-form attempt; do not wire near-matches.
Report c₃ TIERED (c₂=−1 proved; c₃ empirical/cal-anchored, NOT a prediction).
(Note: the `docs/precision-goals.md` Q_β scope-(b)→(a) over-claim the assessment
flagged is **already fixed** on main — lines re-scoped 2026-08-08, bean `qou-qb8a`.)

## Task 5 (qou-v6oz) — m_K/m_π 100× pass is two-term-truncation-dependent

The block already carries the honest caveat (`meson-em-sinh-closed-form.md`): the
EM factor `(3q²−1)/(2q²)` is the **leading two-term truncation** of
`1+log(1+ℏ_q)`, and the full series fits *worse*. A truncation that beats its own
parent series is a fit signature. This truncation-dependence was **not** on the
`docs/precision-goals.md` L2 headline (which read "m_K/m_π meets 100×" with no
caveat); now added there. Honest state: the `[3]_q[4]_q` core (99.98 %) is
exact/Lean-proved and α_em is derived, so **the ratio itself is parameter-free**;
but the **~47 ppb precision** rests on the 2-term truncation (the full series
gives ~103 ppb, a miss). **Open successor:** derive why `(3q²−1)/(2q²)` is the
physical object (not a truncation) — bean `qou-v6oz`.

## Task 3 (qou-8mbd) — PeriodMapWeight/MOC Lean interface

In progress (parallel agent) at the time of this record; the HodgeWeil codomain
brick already landed on this branch (PR #4794). Any further sorry-free
"automatic-ingredient" lemma will be recorded with its own commit.

## Net

Task 1 banks the week's key negative durably (stops re-running dead Δ_λ ansätze).
Tasks 2 and 4 are independent second-route confirmations of existing verdicts
(valuable per the parallel-exploration directive) — the b₄ **bijection** is the
sharp anti-fit statement; the c₃ **VALUE proved-closed / SHAPE open** split names
the one live falsifiable step (`qou-jcmw`). Task 5 removes a headline overclaim.
Nothing is fitted, wired, or closed.
