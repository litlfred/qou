# Trace-convention registry — which Markov trace, in which channel

**Canonical doc.** Machine-readable twin:
[`trace-convention-registry.json`](trace-convention-registry.json)
(schema `trace-convention-registry/v1`). Validator:
[`trace_convention_registry_validate.py`](trace_convention_registry_validate.py)
(`--lint-docs`, `--strict`, `--selftest`).

Supersedes the de-facto registry
[`docs/audits/2026-06-09-binding-trace-convention-split.md`](../audits/2026-06-09-binding-trace-convention-split.md)
(retained as the historical record). Opened under bean `qou-n1dj`.

> **Rule.** Any $\tau$ / $\mathrm{tr}_M$ value quoted below 0.1 % precision, and
> any cross-method comparison of trace values, must name its convention id from
> this registry with the script or Lean decl cited. **Convention-silent trace
> values are not comparable.**

## Why this file exists

Two defects, both of which a machine check catches in under a second:

1. A content block stated that the framework's **mass** computations use the
   full-Hecke Ocneanu trace (convention **C**) while production supplied
   convention **D**. The two differ by **195.8 ppm** on $\beta_{\mathrm{Bor}}$;
   switching the mass channel to the trace the paper named moves $m_p$ by
   **−197 ppm**, destroying the CODATA match. Nothing in the repo compared the
   doc's claim against the code's behaviour, so the disagreement persisted.
2. `markov_peel.tr_M_atomic` was compared against a $\beta_{\mathrm{Bor}}$ value
   as though it were a fifth convention. It traces a **different, 11-crossing**
   braid word, so the resulting 6.7 % "convention gap" was a braid-word
   difference. The registry records it as an **excluded tracer**.

## The conventions

$q_0$ below is the **experimental (proton) pin** $1.1099785827513808$
(`qou_substrate.constants.Q`), per the AGENTS.md owner directive of 2026-08-07.
$\beta_{\mathrm{Bor}} = (\sigma_0\sigma_1^{-1})^3$: 6 crossings, writhe $0$,
$\pi = \mathrm{id} \in S_3$, $\chi^{(2,1)} = 2 - 3h^4 - h^6$ with
$h = q - q^{-1}$.

| id | name | $z$ | $z(q_0)$ | $(y_{(3)},\,y_{(2,1)},\,y_{(1^3)})$ at $q_0$ | $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ | forcing status |
|---|---|---|---|---|---|---|
| **A** | matrix-M parabolic | — | — | — | never evaluated | not-a-$z$-trace |
| **B** | Plancherel $d_q^2/[3A]_q!$, averaged crossings | — | — | — | never evaluated | deprecated |
| **C** | full-Hecke Ocneanu / Wenzl $z$-trace | $1/(q^{1/2}+q^{-1/2})$ | $0.49932033418369445241$ | $(0.4153958,\,0.2809296,\,0.0227449)$ | $0.998366622585715966895$ | pinned-by-definition — **EXCISED 2026-08-09** |
| **D** | SU(2)/Temperley–Lieb (Jones) | $q^3/(q^2+1)$ | $0.61268803714646525160$ | $(0.5054042,\,0.2472979,\,0)$ | $0.998562163836787265951$ | forced-given-premise — **PRODUCTION** |

> **Precision re-record, 2026-08-09 (bean `qou-wgta` item 12).** Every value in
> the JSON twin had been computed from `meta.q0.value = "1.1099785827513808"`,
> a **17-digit truncation** of the canonical
> `q_parameter.Q_50_DIGIT_STR = 1.1099785827513808075916690956107688798744991218736`
> — so the recorded $z(q_0)$, weights and $\mathrm{tr}_M$ were wrong in the
> 18th significant figure against the code that uses the full constant
> ($z_D$ was recorded $\ldots524365$, correct is $\ldots525160$). Nothing
> noticed while the validator only compared strings; **R9 found it on its
> first run.** All JSON values are now recomputed at 50 dps, cross-checked
> two ways: D's weights against the closed forms $[4]_q/[2]_q^3$ and
> $1/[2]_q^2$, and $\mathrm{tr}^D_M(\beta_{\mathrm{Bor}})$ against the Lean
> closed form $(4+h^2-3h^4-h^6)/(h^2+4)$, both agreeing to $<10^{-60}$.

> **Convention C has no live production implementation as of 2026-08-09.**
> The four rows this file used to list under C —
> `markov_trace_canonical::tr_M_element`, `closed_form_tau_M::markov_z` +
> `y_lambda_wenzl_bridge_numeric`, `binding_canonical.py`, and
> `wedderburn_jones_markov::y_lambda_at` — are **all convention D** now
> (bean `qou-wgta`). C survives in exactly **two** places, both deliberate:
> the explicitly-named historical functions in `schur_principal_mpmath` that
> keep the excised convention *quotable* for the D-vs-C comparison in
> `y_lambda_su_n.main()`. R9 asserts both are *still C*; the preserved
> reference stopping being C without anyone noticing is precisely what
> happened to its predecessor.
>
> The third place — `pyhecke/gram.py::z`, the one **blocked migration** —
> moved to D on 2026-08-15 (bean `qou-w8zz`), once `G` was inverted on the
> quotient `H_3/rad` rather than the full NF basis, which removes the
> degeneracy that blocked it. See `resolved_migrations` in the JSON twin.
> The registry row was not updated when the migration landed, so R9 — which
> is written to *assert* the exception — went red on main with *"registry
> says convention C but the CODE returns 0.6126880371464652"*. That is the
> gate working as designed: a numeric evaluator caught a stale record, where
> R4/R5 compare a docstring to a registry field and stay green whenever both
> sides go stale together.

> **Registry gap closed 2026-08-09.**
> `computations/wedderburn_jones_markov.py::y_lambda_at` is convention **C** and
> was **not listed**. Measured `y_λ(3, q₀) = (0.4153957954, 0.2809296310,
> 0.0227449426)` — the C row above, to every digit shown. It is the widest C
> surface in the repo by a wide margin (**155 consumers**, against 62 for
> `binding_canonical`, 46 for `closed_form_tau_M`, 27 for `tr_M_element`), so any
> C→D migration driven off the previously-listed implementations alone would
> have missed most of the change.

- **C and the "Wenzl-bridge $z$-trace" are one convention, not two** — proved as
  a rational-function identity in
  [`probe_convention_d_vs_c_borromean.py`](../../computations/probes/probe_convention_d_vs_c_borromean.py).
- **D's weights are the Jones-closure vector** $([4]_q/[2]_q^3,\ 1/[2]_q^2,\ 0)$
  and its $\beta_{\mathrm{Bor}}$ value equals the Lean closed form
  $(4+h^2-3h^4-h^6)/(h^2+4)$ exactly.
- **$D \neq C$ exactly**, Lean-proved
  (`QOU.BraidsAndKnots.BorromeanTraceConventionSplit.conventionD_ne_conventionC`).

### The gap, in closed form

$$
  \mathrm{tr}^{D}_M(\beta_{\mathrm{Bor}}) - \mathrm{tr}^{C}_M(\beta_{\mathrm{Bor}})
  \;=\;
  \bigl(y^{D}_{(2,1)} - y^{C}_{(2,1)}\bigr)\bigl(-3h^4 - h^6\bigr)
  \;=\; 1.9554\times 10^{-4}
  \quad (195.82\ \text{ppm at } q_0),
$$

exact as a rational function in $q$ — verified symbolically in
[`probe_writhe0_trace_insensitivity.py`](../../computations/probes/probe_writhe0_trace_insensitivity.py).

## The channels — definitional vs production convention

The registry separates **what the corpus defines** from **what the code runs**,
because those can differ, and the mass channel is the case where they do.

| channel | definitional | production | status |
|---|---|---|---|
| `mass` | **D** — owner ruling 2026-08-09 (the row cap $\ell(\lambda)\le 2$ forces it) | **D** — `trM_borromean` → `F_Bor` → `canonical_mass` | agreed |
| `binding` | D | **D** — `binding_canonical.py` → `closed_form_tau_M` → `markov_z`, and `y_lambda_wenzl_bridge_numeric` | agreed |
| `borromean-binding-single-pipeline` | D | **D** — `borromean_binding_recompute.py` | agreed |
| `qbeta-decay` | **null (contradictory)** — the decay blocks write the excised-C value while naming it "the Markov–Jones parameter", whose referent has been D since 2026-08-09; no decay-specific derivation of either exists | **C** — `qbeta_utils.markov_parameter` (`α=(z−1)h/2` feeds every committed $c_k$ extraction), `qbeta_ck_sseries_exact_rational` core, `ZBarParity.lean` | **disputed** (bean `qou-b3nk`) |

> **The `qbeta-decay` dispute (registered 2026-08-15, bean `qou-b3nk`) is a
> derivation gap, not a def-vs-code mismatch of the mass kind.** Neither
> convention is *derived* for the decay channel. **C** is a stipulation whose
> cited referent now reads D, and it fails two structural conditions each of
> which would exclude it *if demanded* — the full-bar condition
> $\overline{z} = z - h$ (Lean `QOU.QBeta.zD_full_bar_covariant` /
> `barEven_fullBar_forces_classical`, sorry-free; premise: trace
> bar-compatibility $\mathrm{tr}\circ\mathrm{bar} = \mathrm{bar}\circ\mathrm{tr}$)
> and fixed-rank fibre membership ($N_{\mathrm{eff}}(z_C) = 2.5995$ pointwise,
> $q$-dependent; premise: categorical fibre trace). **D** is conditionally
> forced only on named unproved premises (`conj:binding-qbeta-complex-volume`
> same-object identification, or trace bar-compatibility). **Mutual
> exclusivity is proved** (`decayLadder_zC_threeRow_ne_zero`, sorry-free): any
> faithful normalised Markov trace at the ladder's $z_C$ carries
> $y_{(1^3)} \neq 0$, so the mass channel's two-row forcing cannot transfer
> while the ladder keeps $z_C$ — and a $z$-swap is **not** a migration
> (measured: $c_3 \to \approx -974$, rung convergence collapses). Until
> settled, every $c_3$ / $S$ / $q^*_S$ quote names its convention. Audit:
> [`2026-08-15-qbeta-decay-channel-convention-disputed-registration.md`](../audits/2026-08-15-qbeta-decay-channel-convention-disputed-registration.md);
> numeric shadow: `computations/qbeta/qbeta-decay-channel-convention-status.witness.json` (18/18).

> **All three channels were carrying a convention the code did not supply,
> and the table above said "agreed" throughout.** Found 2026-08-09
> (`qou-wgta`): `closed_form_tau_M` declared C in its docstring while its
> `markov_z` had returned D since `33a6c7aa` **and** its
> `y_lambda_wenzl_bridge_numeric` constituent was still C — three different
> answers in one call path. `borromean_binding_recompute` computed
> $\tau$ from the Lean **D** closed form and its bond factors from a **C**
> $z$, so the single-pipeline binding was reproducible under *neither*
> convention. Both are fixed; see R9 below for why the validator could not
> have told you.

A channel whose two conventions differ **must** carry `status: "disputed"` and a
non-null `open_item` naming a bean and an audit. R8 of the validator enforces
this: a convention disagreement may not be recorded silently.

> **The `mass` dispute is an owner decision.** Blast radius: ~30 `F_Bor`
> consumers and −197 ppm on $m_p$. No agent may switch the production trace to
> close it. D is the value that lands on CODATA, which is precisely why
> deciding by match is forbidden here. Full analysis:
> [`2026-08-08-borromean-trace-convention-forcing.md`](../audits/2026-08-08-borromean-trace-convention-forcing.md)
> and [`2026-08-08-trace-convention-registry-and-doc-fix.md`](../audits/2026-08-08-trace-convention-registry-and-doc-fix.md).

## The writhe-$0$ lemma — what it does and does not buy

For **any** normalised Markov trace on $\mathrm{H}_3(q)$
($\sum_\lambda y_\lambda d_\lambda = 1$, $d = (1,2,1)$) and **any** braid
$\beta \in B_3$ with writhe $0$ and $\pi(\beta) = \mathrm{id}$:

$$
  \mathrm{tr}_M(\beta) \;=\; 1 + y_{(2,1)}\bigl(\chi^{(2,1)}(\beta) - 2\bigr).
$$

Both one-dimensional characters equal $1$ at writhe $0$
($\chi^{(3)} = q^{w}$, $\chi^{(1^3)} = (-q^{-1})^{w}$), so:

- **True.** The *split* between $y_{(3)}$ and $y_{(1^3)}$ is **invisible** on
  such braids — normalisation already pins their sum to $1 - 2y_{(2,1)}$. This
  is why the chirality / transpose-pair asymmetry ($y_{(3)}$ vs $y_{(1^3)}$) is
  unobservable there.
- **False.** That two conventions therefore agree. $y_{(2,1)}$ is **not**
  invisible. Two conventions agree on such a braid iff they share $y_{(2,1)}$ or
  $\chi^{(2,1)}(\beta) = 2$. C and D share neither.
- **Refuted (scope (b), named invariant).** The reading "the two traces agree on
  braids whose image lies in $\mathrm{TL}_3$" is not available:
  $\chi^{(1^3)}(\beta) = (-q^{-1})^{w(\beta)}$ is a **unit** for every braid, so
  no braid image has a vanishing three-row component. The invariant is the
  invertibility of the one-dimensional characters.

## Excluded tracers — not conventions

| symbol | file | why it is not a convention |
|---|---|---|
| `tr_M_atomic` (and `_fast` / `_rust` / `_at_q0` / `_lq` aliases) | `computations/markov/markov_peel.py:310` | traces `atom_braid_word_3A`, which for $(Z,N)=(1,0)$ is an **11-crossing** word with core $\sigma_0^3\sigma_1^{-3}$ — a different braid closure from the 6-crossing interleaved $\beta_{\mathrm{Bor}}$. Comparing it to a $\beta_{\mathrm{Bor}}$ value measures a **braid-word** difference. Produced a false 6.7 % "fifth convention" alarm on 2026-08-08. |

R7 makes listing an excluded symbol as a convention implementation an error.

## Symbol collisions — objects that look convention-scoped and are not

Two unrelated matrices are written $G$ in this corpus. Conflating them is the
fastest way to "discover" that a headline number moved under the C → D
excision when it did not.

| symbol | what it is | convention-scoped? |
|---|---|---|
| $G_{ij} = \mathrm{tr}_M(b_i b_j)$ — the **Markov–Gram** | $6 \times 6$, on the $H_3(q)$ normal-form basis. [`prop:frobenius-gram-matrix`](../../content/quantum-observable-universe/mass-theory/frobenius-gram-matrix.md); code `tools/pyhecke/python/pyhecke/gram.py`; Lean `QOU/QBeta/GramSignature.lean` | **YES.** $\det = -0.18920521914403668$ under **C**; $\det = 0$ **exactly** under **D**, where the $(1^3)$ block is the radical, the form is singular and $G^{-1}$ does not exist. `np.linalg.inv` raises nothing there — see the blocking note at the head of `gram.py`. |
| $G_{\mathrm{CS}}$ — the **Chern–Simons pairing Gram** | $2 \times 2$, on the force-carrier pair $(T_{2,9}, T_{3,5})$ on Bring's surface. [`rem:em-coupling-chern-simons`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md), [`prop:gram-determinant-plancherel-ratio`](../../content/quantum-observable-universe/mass-theory/gram-determinant-plancherel-ratio.md); code `computations/substrate/hecke_core_symbolic.py::alpha_em_inv_sym_exact` | **NO.** Built from $\pi$, the torus-knot data $(m_i, n_i)$ and $[2]_q, [3]_q, [5]_q, [9]_q$ alone. No $z$ anywhere. At $q_0$: $\det G^{\mathrm{cl}}_{\mathrm{CS}} = 60.630144110670241284$, $\det G^{q}_{\mathrm{CS}} = 35.21703297433989011$, $\kappa = 1.721614201708788213$ (60 dps). |

**Consequence, checked 2026-08-09 (decision 3 of the detangler review).** The
fine-structure figure $\alpha^{-1} = 137.0359351$
([`sec:fine-structure-data`](../../content/quantum-observable-universe/observations/fine-structure-data.md))
runs through $G_{\mathrm{CS}}$, **not** the Markov–Gram, so it does **not** sit
downstream of a convention-C determinant and is unaffected by the excision.
$\hbar_q = 1 - q^{-1}$ in $\delta_{\mathrm{CS}}$ is likewise $z$-free. Independent
re-evaluation of the producer at 60 dps reproduces every published digit:
bare $136.82320885358258431$, $\delta_{\mathrm{CS}} = 0.0015506021328500969$,
resummed $\alpha^{-1} = 137.03593509397560466$ ($-0.4676$ ppm vs CODATA 2022).
Whether $\kappa$ is *derived* is a separate, still-open question
([`rem:alpha-em-derivation-open-problems`](../../content/quantum-observable-universe/predicted-spectra/alpha-em-derivation-open-problems.md));
this row settles only *which matrix* the symbol denotes.

## Content-layer C surface — what the 2026-08-09 errata pass did and did not touch

The errata commit for decision 1 of the detangler review corrected the
convention at the **normative** definition sites and at every block whose
*claim* (not merely whose $z$) was falsified by the excision:

- the symbol registers — `notation/notation-register-table3-data.md`,
  `appendix-transfer-matrices/tm-notation-table1-data.md`,
  `stochastic-mechanics/bar-involution-table2-data.md`;
- the axiom statements — `thm:jones-markov-trace`,
  `prf:trace-locality-meets-gs-nonlocality`, `prf:algebraic-gns-embedding`,
  `prf:hecke-satisfies-blitvic-hypothesis`, `appendix-transfer-matrices/tm-notation.md`;
- the blocks carrying a falsified claim — `prop:frobenius-gram-matrix`
  (non-degeneracy, "indefinite"), `rem:confinement-nucleon-unit`,
  `prop:confinement-lp`, `prop:toffoli-lp-stability` (+ proof),
  `def:two-row-stratum`, `rem:y-lambda-sign-pattern`,
  `prop:y-lambda-closed-form-wenzl-bridge` (+ tables 1–2, proof),
  `prop:trm-hopf-sigma1-sq-closed-form` (+ tables 1–2, proof),
  `prop:centered-hecke-variance-positive` (+ table, proof),
  `prf:qbeta-canonical-markov-weights-explicit-instance`,
  `braids-and-knots/bar-involution-c5-algebraic-identities.md`.

**Not touched, and this is the tracked backlog: ~30 further content blocks
still define $z$ as convention C.** They were left because each one's
downstream numerals need a producer re-run, not an edit, and because changing
the definition without the numerals would make a block internally inconsistent
rather than merely stale. Enumerate them with

```sh
grep -rnE 'z[^\n]{0,40}=[^\n]{0,30}(1 */ *[\(\[]?q\^\{1/2\}|\(q\^\{1/2\} *\+ *q\^\{-1/2\}\)\^\{-1\}|1/\(\\sqrt\{q\}|1/\[q\^\{1/2\})' content --include='*.md'
```

Two cautions for whoever drains it.

1. **`prop:markov-trace-frobenius-selection` is reserved.** Its lines defining
   $z$ as C are owned by decision 2 of the same review, which restates its
   selection criterion (non-degeneracy is provably false under D). Do not sweep
   it ahead of that.
2. **Not every $q^{1/2}+q^{-1/2}$ is convention C, and not every one that
   isn't is correct.** Three distinct things wear that spelling:
   Wenzl's positivity threshold $q^{1/2}+q^{-1/2} > 2$ (correct as written, and
   its convention-D analogue is **not** yet derived — see the dated open note on
   `prop:centered-hecke-variance-positive`); the Temperley–Lieb loop parameter
   written $\delta = -(q^{1/2}+q^{-1/2})$ in four blocks; and convention C
   itself. The middle one is **wrong in this paper's normalisation** and is a
   separate erratum: under $\sigma_i^2 = (q-q^{-1})\sigma_i + \mathbf{1}$ the TL
   generator is $e_i := q - \sigma_i$, satisfying $e_i^2 = [2]_q e_i$, so
   $\delta = [2]_q = q + q^{-1}$, and $q^{1/2}+q^{-1/2}$ is the loop parameter of
   the *other* ($g$-convention, $Q = q$) normalisation. Under convention D,
   $\mathrm{tr}_M(e_i) = q - z = q/(q^2+1) = 1/[2]_q = 1/\delta$ **exactly** —
   the Jones–Temperley–Lieb normalisation, on the nose. This is `loop_reciprocal`
   in `QOU/QBeta/TemperleyLiebTower.lean`, sorry-free. That identity is the
   cleanest one-line statement of why D and not C, and it is why C looked
   plausible: it is a TL loop reciprocal, attached to the wrong element
   ($\sigma_i$ rather than $e_i$) and evaluated at the wrong argument —
   $1/(x+x^{-1})$ at $x = q^{1/2}$ instead of $x = q$, one square root and
   $0.408\,\%$ apart ($1/\delta = 0.4972905456$ vs $z_C = 0.4993203342$). Bean
   `qou-98g5` tracks the corpus instances of that conflation; it lists
   `mass-theory/h3-markov-wenzl-weights-context.md:69` and
   `docs/coordination/convention-slip-registry.json:79`. The errata pass found
   and fixed a **third**, not on that list:
   `braids-and-knots/bar-involution-c5-algebraic-identities.md:1`, which wrote
   the same false identification in reciprocal form as "$1/z = q^{1/2}+q^{-1/2}$"
   and so matched no search for the convention-C formula for $z$.

## What the validator checks

| rule | check | severity |
|---|---|---|
| R1 | unique single-letter id, name, `forcing_status` in enum, non-empty `implementations`, `source`; `forced-given-premise` requires `forcing_premise` | error |
| R2 | a recorded $\beta_{\mathrm{Bor}}$ value needs a `verify` recipe or a `value_note` | error |
| R3 | **live value check** — recompute each row's $\beta_{\mathrm{Bor}}$ value from the code it names and compare at $10^{-15}$ relative. *A declared convention that disagrees with what the code produces is an error.* Import failure degrades to a warning, never a silent pass | error |
| R4 | every `entry_points` function declares its convention in its own source (case-insensitive `convention <X>` within the def's leading window), matching the registry | error in `production_files`, else warning |
| R5 | **discovery** — every Borromean trace function found in `computations/` must likewise declare a convention | error in `production_files`, else warning |
| R6 | **doc-vs-code** — each `doc_claims` row's `names_convention` must equal the channel's convention for the stated `layer`. *This is the defect that occurred.* A vanished `quote` is a staleness warning | error |
| R7 | no excluded tracer appears as a convention implementation; `--lint-docs` also warns on doc lines pairing an excluded symbol with a Borromean convention claim | error |
| R8 | a channel whose two conventions differ must be `disputed` **and** carry an `open_item` with a bean and an audit | error |
| **R9** | **EVALUATION** — import every `evaluators` entry, **call it at $q_0$**, and compare against the declared convention's own `z_at_q0` / `weights_at_q0` at $10^{-40}$ absolute. Reports the convention the code *actually* implements. Entries declared **C** are checked just as hard: the preserved historical reference and the one blocked migration must **stay** C | error |
| — | `--selftest` replays `regression_cases` and fails if any historical defect is **not** caught | error |

Default is warn-only (`--strict` promotes warnings to failures), matching how
[`lp_dual_witness_validator.py`](../../computations/lp_dual_witness_validator.py)
is wired.

```bash
python3 docs/coordination/trace_convention_registry_validate.py --selftest --lint-docs
python3 docs/coordination/trace_convention_registry_validate.py --strict   # CI gate
```

### Why R9 exists (read before trusting a `PASS`)

R3 checks two curated $\beta_{\mathrm{Bor}}$ values. **R4 and R5 compare a
docstring string to a registry string and never look at a number.** On
2026-08-09 a stale docstring and a stale registry agreed with each other, and
this validator printed `PASS, 0 errors, 21 warnings` while the repo contained
174 Python files, 61 Lean files and the entire Rust engine stack on the
excised convention — including **four production entry points**, **three
convention hybrids** (D in one factor and C in another *inside one function*),
and a symbolic path serving convention C out of a **JSON witness cache**,
where the string `sqrt` never appears at all. None of those is visible to a
string comparison; none of them survives an evaluation.

Demonstrated, not assumed: reintroducing C at a single definition site
(`hecke_symbolic.z_markov`) and re-running gives

```
ERROR : R9 hecke_symbolic.z_markov: registry says convention D
        (z = 0.61268803714646525159582986394589924802630839154509)
        but the CODE returns 0.4993203341836944524134427
        (|d| = 0.1134 > 1.0e-40) -- it is actually convention C
```

while **R4 stays silent**, because the docstring still says D. That is the
original defect, reproduced and caught.

R9 also found two things on its own first run: the 17-digit-q₀ precision
defect described above, and that `wedderburn_jones_markov.y_lambda_at` — the
widest surface in the repo, ~155 consumers — hard-truncates to **30
significant digits** (`sp.Float(_mp.nstr(v, 30), 30)`, line 152) regardless of
the dps requested, against a 50-dps production floor. That one carries a
documented per-entry tolerance rather than a silent pass.

**Current baseline (2026-08-09):** `PASS`, 0 errors, **21 warnings** — all R5,
i.e. 21 Borromean tracers outside `production_files` that do not yet declare a
convention. That is a tracked backlog, not a silent pass; drain it by adding a
`convention <X>` line to each docstring after confirming which trace it computes
(do not guess from the value). Run the validator for the live count rather than
citing this figure later.

## Adding a row

1. **Convention.** Add to `conventions[]` with its $z$, weights, $\beta_{\mathrm{Bor}}$
   value, implementations, `forcing_status`, and a `verify` recipe registered in
   `VERIFIERS` inside the validator. R3 will then hold the value to the code.
2. **Channel.** Add to `channels[]` with both `definitional_convention` and
   `production_convention`. If they differ, set `status: "disputed"` and supply
   an `open_item`.
3. **Doc claim.** Any doc or content block that names a convention for a channel
   goes in `doc_claims[]` with a verbatim `quote`, the `layer`, and the
   convention it names. R6 then guards the doc against the code forever.
