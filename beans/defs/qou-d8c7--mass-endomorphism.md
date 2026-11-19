---
# qou-d8c7
title: Mass endomorphism
status: todo
type: epic
priority: normal
created_at: 2026-10-10T07:00:10Z
updated_at: 2026-11-19T00:40:00Z
---

One home for every bean whose subject is the mathematics of `chap:mass-endomorphism`
(`folio/quantum-observable-universe/mass-endomorphism/`). Before this epic those beans sat
under five unrelated parents (`qou-wp3h`, `qou-10v9`, `qou-rtxm`, `qou-avtq`, `qou-mub3`)
and several were duplicates, empty stubs, or described sorries that no longer exist.
Issue litlfred/qou#7547; survey run on `main` `210c6bd25`, 2026-10-10, owner-approved
bean-only merge.

**Scope rule.** A bean is in scope when a chapter block, its Lean sibling or library
module (`MassEndomorphism`, `TopologicalMass`, `Torsion/MassIdentity`,
`CategoricalMassMarkov`, `BraidKnot/*` chapter refs) or `computations/mass_endomorphism.py`
is its *subject*. About 110 further beans mention the chapter only as one row of a
corpus-wide sweep (voice, forward refs, sidecars, float64, Lean-sibling compilation,
witness status); they stay with their sweeps and are not listed here.

**Reparenting rule.** Carriers whose whole subject is this chapter are children of this
epic. Cross-chapter carriers (vacuity classes, the Q_beta ladder, the keystone programme,
the J^bullet bridge, the kT question) keep their parents and are listed below as
related carriers, each with a pointer note appended.

## Carriers

| # | carrier | absorbs / links | still open (verified 2026-10-10) |
|---|---|---|---|
| M1 | `qou-puwe` mass-identity formulation | `qou-qc6s`, `8jaf`, `qou-5ujw` (completed) | prose = categorical trace, Lean = multiplicative integration; two declarations claim `def:mass-identity` (`QOU.Torsion.MassIdentity` is the ref; sibling `mass-identity.lean` defines `frobeniusMass` / `scalarMass`) |
| M2 | `tmvac` topological-mass cluster | `qou-m5fy` (scrapped), `qou-0w3s`, `qou-wuxx`, `qou-ki4u`, `qou-lf1m` item, `qou-hjf4` trivialVortex item; scrapped `qou-wfhf`, `50p7` | descent inputs open (class `CatDescendedInputs`); norm-additivity open (orthogonal decomposition refuted at free data); `instance trivialVortex` live at `topological-mass-conjecture.lean:180`; `tm_transient_localisation.lean` inputs are zero-satisfiable class fields |
| M3 | `qou-jgp2` Hecke Baer-* | scrapped `qou-bawa`, `qou-yabz` | claim now rests on two axioms in `hecke-baer-star-generic.lean` (`matrix_algebra_baer_right_axiom`, `hecke_baer_star_generic_sketch_axiom`) |
| M4 | `qou-2150` explicit central idempotent | `qou-1bua`, `qou-hqi8` (completed), `qou-t99b` (scrapped) | `ExplicitCentralIdempotentConjecture` has no instance (by design); idempotency via Murphy open |
| M5 | `qou-eddc` per-block chi closed forms | `qou-ox7y`, `qou-g3mz` (scrapped), `qou-m7yh` (scrapped), `qou-18b6` (completed) | `qbeta-delta-tau-surrogate-taylor-coefficients-formal-scope.md` still states the grouped degree-11/7 quotient and "sorry, orders 2..7" |
| M6 | `qou-2cof` convention-C survivors in chapter blocks | `qou-pdfx`, `qou-ft3p` (completed), `qou-zf9n` antipode item, `qou-fq0f` kernel item, `qou-46ab` | proof-block sweep; antipode witness ~1.63 (C) with no assertions; row cap not taken in `tr_m_atom_via_transfer` |
| M7 | new — `mass_endomorphism.py` script health | `qou-47sx`, `qou-oots`, `qou-2tuv` script items; `qou-lbgh`, `qou-bsec` (done) | float64 `Phi_q` / `additive_wedderburn_volumes`; `dim_q^2/[3]!` weights vs ruled Molien; `brane_tower_isospin_diagnosis.py:180` crash |
| M8 | `qou-n1dj` mass fibre functor: TL or full H_3 | `qou-dwf4`, `qou-fq0f`, `qou-qlma` z-sections | premise `MassTraceIsFibreCategorical`; categorical-to-numeric bridge at dim V = 2 |
| M9 | `qou-jgg0` atomic word strand count | `qou-hkwd` line, `qou-q6pp` (downstream) | `atomic-mass-gb-nf.md:3` still `B_n`, n = 3A+Z, against owner ruling (a) |
| M14 | new — citations at chapter blocks | `qou-ghg3`, `qou-7ji4`, `qou-3fe9`, `qou-7ldu`, `qou-u62r`, `qou-ki4u`, `qou-11p0`, `qou-hkaq`; done halves `qou-byu8`, `qou-7fhj`, `qou-wpyh` | six keys in `references.ts` cited in no chapter block; `gelca-nagasato` untracked |

Related carriers (parent unchanged):

| # | carrier | links | still open |
|---|---|---|---|
| M10 | `qou-ffwk`, `qou-tmmt` | `qou-hjf4` | residual = 0 placeholders in `hecke-algebra-type-scaffold` (4), `markov-trace-operator-construction` (3), `phi-d-syt-count-conjecture` (instances at 127/136/145 and `defaultGeneralPhiD4F` at 225, the last not named by ffwk); bare projections at `markovTraceRecursiveReducer.lean:64`, `hecke-branching-trace-decomposition.lean:94` |
| M11 | `qou-wzgm` binding-qbeta complex volume | `5nx8`, `0zr0`, `qou-e58e`, `qou-cds1`, `qou-avt1`, `qou-8vt2` | single-V assembly; eta^2 test never run; symbolic delta blocked by `float(h)` |
| M12 | `wpdb` word-depth to partition-depth bridge | `qou-wjbd` (scrapped, verbatim copy), `qou-sw8n` | fourth (confinement-energy) J^bullet reading; needs step-10 LP |
| M13 | `qou-892m` Gibbs / kT | `qou-qnqf`, `qou-y0mc` (done), `qou-zlra` gibbs item | is hbar_q or E_0 the temperature |

Also in scope, not merged: `qou-lrnd` (motivic Galois instance, live math; `qou-oy4r`'s
closure text says `rem:` but the tree has `conj:` per `qou-s0ip`), `qou-y0xk` (rho-k witness
env: clarabel absent, mpmath 1.3.0), `qou-4e5k` (mass-table deuteron colour-blind),
`qou-g7z6`, `qou-39ft`, `qou-iars` (hygiene), `qou-8hm1` (cross-chapter hard sorries).

## Attack-vector catalogue

Classifications are read from the bean texts and spot-checked against the tree; they are
not new results. "Bad data" means the failure was later traced, fully or partly, to a
wrong input (convention C, muon pin, grouped word order, q = 111/100, stale witness).

**Tried, worked.** MassIdentity generic/archimedean split (puwe opt. 1); canonical
borromean (2,1) chi form (eddc); chi_v21 trace identity after the d1/d2 fix (18b6);
canonical Markov n=3 weights (c35w, 6u92); Hecke -> TL surjection (voa6); zeta4-partner
relation as a filter (5nx8); G2 affine-vs-cosine clash (avt1, `LadderCosClash.lean`);
framing-ratio classification, D = sl2 point (dwf4); row cap as exact zero (fq0f); three
tr_M paths agree to 3.4e-25 (4e5k); Jones-Wenzl weight formula (bsec); Phi_3 column picks
strand count A+Z, 19/19 (jgg0); motivic residue non-vanishing, conditional (lrnd);
bar involution acts as isospin conjugation (e58e).

**Tried, failed (structural).** Descent identities: independent opaque constants (50p7,
0w3s); orthogonal eigenspace decomposition as stated: refuted at free data (wuxx); D as a
z-swap of the ladder (cds1); alpha as the Q_beta blocker: cos <= 1 caps F at 0.99993 vs
required 1.20 / 1.76 (cds1); counit-to-trace transport overshoots 258-334x (avt1); nine
geometric readings of theta_K, Habiro c3 = [3]_q/25, self-conjugate mode set (8vt2);
three J^bullet readings for the word-partition bridge (wpdb); free-energy reading as
binding, negative summand (qnqf); channel entropy H, extensivity (y0mc); binding via the
Phi_q tower, 5e8 % (2tuv); spectrahedral collapse under D, det = 0 (zf9n); all three
nucleon constructors, parity (1qsw); bar-norm modulus, per-lambda conjugation (e58e);
forall-p norm route, Frob_3 = zeta_6 (lrnd); parameter-free p-n split at D, -179 % (q6pp);
reducer and branching "proofs" are bare projections (tmmt).

**Open.** Categorical trace = multiplicative integration (puwe); norm-additivity (wuxx);
Baer-* without the axioms (jgp2); central-idempotent instance (2150); premise
`MassTraceIsFibreCategorical` (n1dj); single-V assembly and eta^2 test (5nx8, 0zr0);
mu_lambda fibre route (8vt2); fourth J^bullet reading (sw8n); hbar_q vs E_0 (892m); p = 7
unit test (lrnd); towerTerm residual, -18.9 % on 2H (2tuv); canonical c3 for the mu3 arc,
owner call (8jq2); symbolic delta (e58e); TL = End_{U_q sl2} (voa6).

**Failed, possibly bad data.** Old (2,1) form: grouped words (eddc); chi_v21 sorry:
d1/d2 transposed (18b6); 15 % proof-vs-statement gap and 15.4 % cross-check: C at the
muon pin (2cof, pdfx); "no droppable partitions": C-era (fq0f); closure-block 0.6293 vs
1.1458: stale grouped witness (46ab); A=1 residual 5e-4: ordering plus missing electron
letter (hu1f); Jones-Wenzl "only consistent scheme": wrong formula (2tuv); alpha bound on
2H: C-specific (qlma); nucleon net table at q = 111/100 (1qsw); original p-n test, wrong
comparison (q6pp); c3 ~ -974 under D: C extractor fed z_D (cds1); Delta net decimals at
q = 111/100 (cds1); -6.6 ppb ladder headline: deprecated c5 (54g5); c_k block claims:
stale c3 and retired z = 1 cell (00ot); perpetual-obstruction constants 4 / -32 vs 8 / 192
(lrnd); `defaultQBetaCKClosedForms`: fitted values (hjf4); Yekutieli 5.3 locator does not
exist (ki4u); M(4He) = -215 MeV composite readout (55pj); mass-table deuteron colour-blind
(4e5k).

## Closures made with this epic

Scrapped with a pointer to their carrier: `qou-m5fy` -> M2, `qou-g3mz` -> M5,
`qou-wjbd` -> M12. Completed (work already done, status lagged): `qou-qnqf`, `qou-5fd0`
(witness clean as of 2026-10-05), `qou-54g5` (headline resolved; the unexplained 7.133 ppb
epoch offset moved to `qou-cds1`). `qou-2150` was rewritten into the M4 carrier instead of
scrapped, because it is the only open bean on an open conjecture (rule 13a);
`qou-8hm1` is cross-chapter and left alone.

## 2026-10-10 — correction to the M7 row (issue #7552)

The M7 row says the weights are "`dim_q^2/[3]!` weights vs ruled Molien". That
overstates the ruling: the Molien choice is scoped to the Φ_k functional, not to the
H_3 Wedderburn weights in `mass_endomorphism.py`, so no weight change is owed there.
Full correction on `qou-g16t`. The diagnosis-script item of M7 is done (ported, not
retired). M14: the eight citation items are applied in the same PR; the
`terashima-yamazaki2013` entry's authors are corrected to Teschner–Vartanov (id kept).

## 2026-11-19 — core of #7551 ported as #8523

Draft #7551 is closed as superseded by #8523, which carries `FibreQuantumTraceOnV3.lean`, the removal of `phiDConj_V3/V21/V111` and `defaultGeneralPhiD4F`, and `qbeta_delta_net_borromean_word_rerun_probe.py`. `trivialVortex` was already off main. #7551's bean edits and witness regenerations were not carried; its branch `claude/practical-carson-9wopuy` keeps them. Lean exit 0, no sorryAx.
