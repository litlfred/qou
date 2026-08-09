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
| **C** | full-Hecke Ocneanu / Wenzl $z$-trace | $1/(q^{1/2}+q^{-1/2})$ | $0.49932033418369445$ | $(0.4153958,\,0.2809296,\,0.0227449)$ | $0.998366622585715967$ | pinned-by-definition |
| **D** | SU(2)/Temperley–Lieb (Jones) | $q^3/(q^2+1)$ | $0.61268803714646524$ | $(0.5054042,\,0.2472979,\,0)$ | $0.998562163836787266$ | forced-given-premise |

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
| `mass` | **C** — `prop:categorical-mass-markov` names the trace on the full $\mathrm{H}_n(R,q)$; `rem:markov-axioms-primitive` pins $z = 1/(q^{1/2}+q^{-1/2})$ | **D** — `trM_borromean` → `F_Bor` → `canonical_mass` | **disputed** (bean `qou-3qrv`) |
| `binding` | C | C — `binding_canonical.py` → `closed_form_tau_M` → `markov_z` | agreed |
| `borromean-binding-single-pipeline` | D | D — `borromean_binding_recompute.py` | agreed |

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
| — | `--selftest` replays `regression_cases` and fails if any historical defect is **not** caught | error |

Default is warn-only (`--strict` promotes warnings to failures), matching how
[`lp_dual_witness_validator.py`](../../computations/lp_dual_witness_validator.py)
is wired.

```bash
python3 docs/coordination/trace_convention_registry_validate.py --selftest --lint-docs
python3 docs/coordination/trace_convention_registry_validate.py --strict   # CI gate
```

**Current baseline (2026-08-08):** `PASS`, 0 errors, **21 warnings** — all R5,
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
