# Results: the nucleon gluon segment by the γγ rule

Pre-registration: [`preregistration.md`](preregistration.md) (step 1 `a341245311`,
step 2 `a9ca10d266`, both committed before computing). Probe:
`gg_gluon_segment_probe.py`, witness `gg-gluon-segment.witness.json`, **36/36
checks**. Exact over ℚ(q); proton pin as an exact rational; mpmath 60 dps for
display. Convention D, `z_D = q³/(q²+1)`. Diagnostics only. No element is
selected and the dashboard is not re-scored.

## Step 1: what the γγ rule gives

On three strands the γγ rule (`qou-ales`, `GammaGammaWordSelection.vertex`) has
exactly one vertex, `V = σ₀σ₁⁻¹`. That vertex is the corpus `gluonUnit`
(`toCorpus_vertex_zero`). So the rule fixes the **unit** of the gluon segment
uniquely. It does not fix the **number of units**. The output is the family
`{Vᵏ}`, which is not unique, so step 2 runs.

Corpus side-rules that name members:
- k = 1: the 2-letter slot of the 11-crossing budget.
- k = 3: the gluon treated as its own SDP component, selected like the core.
- k = 0: the retired "B₃ IS the gluon structure" convention.

`σ₀²` is not γγ (`gluonPair_not_gammaGamma`). It was not a bare census pick,
though. The corpus derives it by the H₂ PSD-parity rule (owner 2026-08-30,
`GluonVertexPsdParity`), which ranges over σ₀ᵏ and is a different rule.

## Calibration (all pass)

- The bar-parity-split probe reruns at 24/24.
- On `nuc11_interleaved` with the probe's own code:
  - f matches its closed form;
  - f = h·g;
  - g_odd = −h[2]_q(q²+q⁻²)/8;
  - Δtr = −0.1541948850472397056592555;
  - E₀ = `qbeta_e0.canonical()` = 4.22748335562903 MeV;
  - Q_β = 0.65185631006 MeV (the scored cell);
  - χ_(3) = 1.38249446339 / 1.1221068216 and χ_(2,1) = −0.2805933509 / −0.3719563247 (p / n);
  - reading-1 determinants (2,1) = −1.02197249381 and (1³) = −0.739223570776 / −0.910762214553.
- y_(2,1) = 0.2473 and y_(1³) = 0.
- χ_(2,1)(V³) = +1.994186.
- χ_(2,1) from an explicit seminormal 2×2 representation (braid and Hecke relations checked) equals the trace-formula value exactly on every word.
- P1: `CORE·TAIL·Vᵏ` and `V^{3+k}·TAIL` give identical diagnostics. The trace is cyclic, so the placement of the segment is not a degree of freedom.

## Step 2: elements CORE · TAIL_x · Vᵏ, k = 0..3, all reported, no ranking

| k | gluon segment | letters | (a) g_odd | (b) χ_(2,1) p | χ_(2,1) n | reading 3 (p, n) | (c) Q_β at z_D (MeV) | vs CODATA |
|---|---|---|---|---|---|---|---|---|
| 0 | (none) | 9 | **0** | −0.0919840131 | −0.1820008782 | fail, fail | 0.545664266 | −30.25 % |
| 1 | σ₀σ₁⁻¹ | 11 | **0** | **+0.2170281485** | **+0.4294149854** | **pass, pass** | 0.229517012 | −70.66 % |
| 2 | (σ₀σ₁⁻¹)² | 13 | **0** | −0.1345296130 | −0.2661822081 | fail, fail | 0.589192245 | −24.69 % |
| 3 | (σ₀σ₁⁻¹)³ | 15 | **0** | −0.0766187562 | −0.1515989622 | fail, fail | 0.529944226 | −32.26 % |
| ref | σ₀σ₀ (census, nuc11) | 11 | −h[2]_q(q²+q⁻²)/8 ≠ 0 | −0.2805933509 | −0.3719563247 | fail, fail | 0.651856310 | −16.68 % |

χ_(3) > 0 on every row (each Vᵏ has χ_(3) = 1), and y_(1³) = 0. So the (2,1)
character decides reading 3.

**Reading-3 survivors (both nucleons, proton pin): 1 of 4, k = 1**, the element
`(σ₀σ₁⁻¹)⁴ · TAIL`. It is the member the 11-crossing budget names. The k = 3
member, named by the "select it like the core" side-rule, fails.

## What the diagnostics show (consequences, not selection criteria)

- (a) **Every γγ gluon segment removes the trace-level bar obstruction exactly.**
  `g_odd = 0` identically in q for k = 0, 1, 2, 3. With f = h·g, f is bar-odd for
  each of these words. This sharpens `qou-z08b`: the obstruction comes from the
  census σ₀² specifically. A γγ-ruled gluon does not produce it.
- (b) The reading-3 verdicts depend on q. χ_(2,1) = 0 at q = 1 for every row
  (flavour is invisible at order t⁰, as in `quark_template`). The real roots of
  χ_(2,1) above 1, identical for p and n:

  | k | roots above 1 |
  |---|---|
  | 0 | 1.278895 |
  | 1 | 1.429157 (so k = 1 passes on (1, 1.4292), which contains q₀) |
  | 2 | 1.495025 |
  | 3 | 1.201352 and 1.531129 |

  - The k = 0 values and the root 1.278895 reproduce, independently, the
    `quark_template` record. That record had −0.09198 / −0.18200 and q* = 1.27890
    for the corpus template at k = 0. This was not pre-registered as a check and
    is noted as a corroboration only.
- (c) The Q_β values are reported. None was used to choose anything. The single
  reading-3 survivor sits at −70.66 %. Whether the ruled element changes is an
  owner decision (`qou-99qc`). The dashboard rows are untouched (`qou-iagg`).

## Scope

Scope (a) throughout.
- The quark tail is the census tail, held fixed. Its derivation is
  `qou-ales` option 4 and is still open.
- The verdicts are at the proton pin.
- The γγ condition is the H₃ one. The every-strand-count condition is trivial on
  three strands.
- Nothing here rules on σ₀²'s H₂-parity derivation. It records that the γγ rule
  and that rule give different gluon segments.

## Reconciliation with the owner ruling D1 = A (2026-11-21)

Branch `claude/gg-gluon-7876-reconcile-2026-11-21` (PR #7876 merged with `origin/main`). The
#7876 files were already on `main` through the γγ-probe port `cc055a9d88` (plus the q₀ stamp
`997ce5c291`), so the merge took `main`'s side everywhere. Nothing in this section is a ruling.

### What changed on `main` since #7876 was written

- **D1 = A** (owner, 2026-11-20 18:25; bean `qou-99qc`, PR #8586 `b47929e610`): the scored Q_β is
  `|ε_flavour(V³)|·E₀^tower = 0.325433929 MeV` (−58.402 %). The element is the bare γγ word
  `V³ = (σ₀σ₁⁻¹)³` for both nucleons (γγ + whole-word reading 3, PR #8564,
  `frobeniusSelected_ten_unique`). The functional is the T³ weight split of the z_D trace,
  `ε_flavour = (q⁻¹·tr_{W_n} − q·tr_{W_p})/[2]³` (`docs/audits/2026-11-20-qbeta-flavour-weight-split.md`).
  `nuc11_interleaved` (0.6519 MeV) and Δ_S (0.4491 MeV) are kept as unscored history cells in
  `per-observable-100x-status.witness.json`.
- 2026-11-21: the scorecard uses the covariant all-pairs two-term trace. Its connected part is 0
  on V³, so two-term = one-term for this cell. The electron is σ₀σ₁σ₀ (Hopf link) for now. Neither
  touches the elements below.

### Re-run on current `main`

| producer | result | payload vs committed witness (timestamps/provenance masked) |
|---|---|---|
| `gg_gluon_segment_probe.py` | **35/36 before the fix below, 36/36 after** | 8 leaves moved, none of them a diagnostic |
| `gg_quark_tail_probe.py` | exit 0; 112/216 (V), 108/216 (σ₀²) | byte-identical |
| `step3_rules_with_gluon.py` | calibration vs step-3 table PASS | prints only; identities unchanged |

- **The one failure was a calibration pointer, not a result.** Check C3 compared the probe's
  `nuc11_interleaved` Q_β against the *first* `Q_beta_MeV` in the scorecard witness. Under D1 = A
  that field is now the V³ cell (0.3254), so the check failed while the probe's own value,
  0.65185631006 MeV, was unchanged. C3 now reads the `nuc11_interleaved` unscored history cell
  (`data.qbeta_ruled_base.unscored_history_cells`) and passes to 1e-18. It is renamed
  `C3_Q_beta_nuc11_history_cell`.
- **The other moved leaves are the CODATA denominator.** `codata_constants.Q_BETA_MEV` on `main`
  is 0.78233355931 MeV (was 0.78233341). Every "vs CODATA" percentage moves by ≤ 1.5e-5
  percentage points: k = 0 −30.251698 → −30.251712 %, k = 1 −70.662507 → −70.662512 %,
  k = 2 −24.687833 → −24.687847 %, k = 3 −32.261077 → −32.261090 %, nuc11 −16.67794 → −16.677956 %.
  No χ, no g_odd, no Δtr, no Q_β in MeV and no reading-3 verdict moved.

### Which #7876 results stand

These are statements about words and characters, and D1 = A changes neither:

1. **The γγ unit is V = σ₀σ₁⁻¹, the corpus `gluonUnit`** (`toCorpus_vertex_zero`). Stands. It is
   the same vertex whose cube is the D1 = A element, and the photon's chiral fourth term
   (`γ(0,0,qh)·γ(0,0,−q⁻¹h) = V³`, `borromeanV3A_eq_switched_photon_product`).
2. **g_odd = 0 for every γγ gluon segment, k = 0..3; the trace-level bar obstruction belongs to
   σ₀² alone** (refines `qou-z08b`). Stands as an exact identity in q. Consistent with
   `ε_flavour(V^k)` being exactly bar-odd (`FlavourWeightSplit.lean`).
3. **Reading-3 behaviour.** On CORE·TAIL·Vᵏ, only k = 1 passes at q₀, for both nucleons
   (χ_(2,1) = +0.2170281485 p, +0.4294149854 n; passes on q ∈ (1, 1.429157)). Stands. It does not
   conflict with #8564: #8564's survivor set {V³, V⁶, V⁹} is over bare γγ words, and the census
   tail is not a γγ word, so the two enumerations range over disjoint element sets.
4. **The quark-tail placement pattern** (gluon V admits placement 001 for all 27 parities; σ₀²
   admits 110) stands, byte-identical.

### What D1 = A supersedes

- **#7876 open question 2 ("does CORE·TAIL·V¹ replace `nuc11_interleaved`?").** Superseded for the
  scored cell: `nuc11_interleaved` was replaced on 2026-11-20 by the bare V³, which has no census
  tail and no separate gluon segment. CORE·TAIL·V¹ was one of the four options put to the owner
  before that ruling (bean `qou-99qc`, W5 entry: "CORE·TAIL·V¹, 0.2295 MeV") and was not chosen.
- **#7876's Q_β column.** It is the Markov-trace difference `|τ_zD(X_n) − τ_zD(X_p)|·E₀`, not the
  ruled ε_flavour, so it is not comparable to the scored cell. For the record, the same four
  elements read with ε_flavour (`d1a_functional_arm.py`, not pre-registered; calibration
  `X_p = X_n = V³` reproduces the scorecard cell to 1e-25):

  | element | ε_flavour at q₀ | Q_β (MeV) | vs CODATA |
  |---|---|---|---|
  | V³ (D1 = A, scored) | −0.0769805346014 | 0.325433928735 | −58.402152 % |
  | CORE·TAIL·V⁰ | −0.0598734883872 | 0.2531141756 | −67.646259 % |
  | CORE·TAIL·V¹ | −0.0343136950966 | 0.145060574891 | −81.457963 % |
  | CORE·TAIL·V² | −0.0633926273534 | 0.267991277006 | −65.744627 % |
  | CORE·TAIL·V³ | −0.05860255851 | 0.247741340698 | −68.333029 % |

  Diagnostic only. Nothing here is selected or scored; using these numbers to choose an element
  would be selection against the target.

### What is still open (not decided here)

- **#7876 open question 1 (γγ rule vs H₂ PSD-parity σ₀² for the gluon segment).** D1 = A makes it
  moot for the scored Q_β (V³ has no separate gluon slot), but no ruling closes it as a statement
  about the gluon. It still matters wherever a census-tail nucleon word or σ₀² is used: the H₂ bond
  letters and the old-letter binding redo that `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`
  says waits on #7876. Searched: `docs/audits`, `docs/coordination`, `folio/`, `beans/defs`
  (grep for `qou-ggls`, `7876`, `CORE·TAIL`, `GluonVertexPsdParity`, "gluon segment"); no later
  ruling found. `corpus_search` was not run.
- The census quark tail (`qou-ales` option 4) is still census-derived, but it is no longer in the
  scored element.
