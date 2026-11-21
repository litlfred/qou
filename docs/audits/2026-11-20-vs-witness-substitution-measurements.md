# Witness value substitution (epic `qou-v6so`): what W13 changed and what it measured

Date: 2026-11-20. Corpus `917b69399` (origin/main). Platform pin `82b389982`
(`.folio-assistant-pin`). Session workstream W13, coordinator PR #8526.

## 1. VS-1 (`qou-h59j`): the code is in the platform, not here

Two of the bean's three deliverables are code in
`folio-assistant/cat-harness-tools/pipeline/`, a separate repository mounted
through the platform lock. It is not `litlfred/qou`, and this session has push
access to `litlfred/qou` only. So W13 wrote the patch and tested it against the
local mount, but it has not landed anywhere. The patch is committed beside this
note as
[`2026-11-20-vs1-liquid-subdir-and-markdown-val.platform.diff`](2026-11-20-vs1-liquid-subdir-and-markdown-val.platform.diff).

| defect | still present at pin `82b389982`? | patch |
|---|---|---|
| 1. Liquid cannot address a witness in a subdirectory of `computations/` | yes. `resolveKey` takes exactly one segment after the directory id as the entry | walk leading segments as subdirectories while each names an existing directory; the shallowest match wins, so every address that resolved before still names the same file. Segments are already limited to `[A-Za-z0-9_-]`, so nothing can escape the declared directory |
| 2. `:val[…]` reaches the site as a raw token | yes. `render-markdown.ts` calls only `resolveLiquidValues` | new `substituteValuesInMarkdown` in `render-value.ts`: numeral inside existing math, `$numeral$` in prose, fenced code untouched. A repo with no value registry keeps the old behaviour instead of crashing |

Verification, run here with dependencies installed into a scratch
`node_modules` (the lite mount ships none):

- `bun test liquid-values.test.ts render-value-latex.test.ts render-markdown-numbering.test.ts`: **32 pass, 0 fail**.
  The liquid file has 4 new tests: a subdirectory entry, a two-level
  subdirectory, a flat witness that shadows a directory name (the flat file
  still wins), and an unknown entry under a subdirectory.
- Real corpus, with the qou registry preloaded: the three `:val[…]` cells in
  `confinement-operator-selection-table1-data.md` render as `$0.9991$`,
  `$1.220$` and `$0.9891$` on the site path. Before the patch they leak as raw tokens.
- `{{ qou.computations.qbeta.qbeta-ck-cache.computedAt }}` resolves to
  `computations/qbeta/qbeta-ck-cache.witness.json`.
- No `computations/<x>/` directory shares a name with a `computations/<x>.witness.json`
  or `<x>.json` file today. Measured over every top-level subdirectory. So the
  "shallowest wins" rule changes no current resolution.

## 2. A real bug found on the way: the benzene unit printed twice

`benzene-threading-selection.md` wrote
`(:val[benzene_resonance_kcal]{…} kcal/mol)`. The registry entry carries
`units: "kcal/mol"`, and `:val` in text mode appends it. Measured LaTeX output:
`($36$\,kcal/mol kcal/mol)`. W13 replaced the reference with
`{{ qou.computations.molecular-experimental-refs.data.benzene_resonance_kcal | precision: 2 }}`.
It reads the same witness, the same path and the same 2 significant digits, and
now renders `(36 kcal/mol)` in both the PDF and the site. `run-validate` gives
5 issues before the change and 5 after, the same lines.

That leaves **one** `.md` file using `:val`: the confinement table. Its witness
keys (`B₃ = (σ₀σ₁⁻¹)³`, …) are not legal Liquid segments, so it cannot migrate
without a producer change. The markdown half of the patch above covers it.

## 3. VS-1 deliverable 3 (registry repair) is not done, and why

- `rho_q` points at `derived_50_digit.rho_q`, which the anchor-defining witness
  `q-pinning-50-digit.witness.json` does not carry. The only keys there are
  `hbar_q_sq, hbar_q, q, q_inv, H_A, two_q, z_markov, s_skein`. The corpus
  defines `ρ_q = 1/ℏ_q²` and marks it **deprecated**: the scalar substrate
  density, superseded by the graded expansion (`skein-mass-relation.ts`,
  `quantum-temperature.ts`). No `.md` uses `:val[rho_q]`.
- `c_q`, `eta_q`, `chi_q`, `d_H` are closed forms of `q` that the registry
  itself states. Pointing them at real fields needs a producer to emit those
  fields. The obvious producer is `q_pinning_50_digit.py`, and AGENTS.md
  forbids re-running it as part of a sweep, because it **defines** the muon
  anchor.
- No `.md` file uses any of the five entries. Only 4 of the registry's names
  are used anywhere.

So the repair has no reader today, and every way to do it touches either the
anchor witness or a deprecated concept. It goes to the owner (§5).

## 4. VS-2 (`qou-jdrx`): the float64 surface is smaller than the bean says

AST count of `float(...)` calls in the four facades plus the pin files:

| file | `float()` calls | what they are |
|---|---|---|
| `derived_masses.py` | 0 | already mpmath |
| `coulomb_energy.py` | 0 | already mpmath |
| `substrate/hecke_core.py` | 2 | `float("inf")` sentinels, not a precision loss |
| `canonical_mass.py` | 3 | **line 56 `_from_witness` truncates the 50-dps witness to float64**; line 147 is an uncertainty in ppb; line 161 is a display-only `__format__` |
| `substrate/q_parameter.py` | 1 | line 151 `Q = float(_d["q"])`, the deliberate legacy float alias |
| `q_pinning_50_digit.py` | 13 | every one is inside an f-string or a display string |

The one real truncation is `canonical_mass._from_witness`. It feeds
`proton_neutron_mass_mev`, `proton_mass_mev` and `neutron_mass_mev`, which
**20** live producers import. Most are mass compute, which is W2's scope.
`canonical_mass.nucleon_mass_mev` already returns full-precision `mpf`, so the
fix is to retire the float path or route those 20 consumers to the mpf path.
Changing the return type moves witness outputs and can break consumers that
`json.dump` the value. W13 has **not** made that change; it is offered to W2
on #8526.

The bean's other VS-2 items are not precision fixes:

- exporting `q_2t` as a pin;
- making `E₀^{(∞)}` the default;
- making the mirror-projected `α_D` the default;
- making Form-B `α_EM⁻¹` the default;
- regenerating `q-pinning-50-digit.witness.json` with three anchor blocks.

Each one moves a q₀ anchor or the default value of a published observable.
Under the 2026-09-07 rule, and the anchor-defining-witness rule, they need the
owner.

## 5. VS-3 / VS-4 / `qou-w1u2` / `qou-h1lc`: blast radius, and corrections to the beans

Re-measured on `917b69399`:

- `*-table*-data.md`: **443**, of which **2** use Liquid. The bean says 3, and
  names `master-bond-order-table` and `predicted-bond-angles`; neither uses
  Liquid. The other wired file is
  `sigma-shell-from-beta-chain-derivation-table-data.md`.
- `.md` files with any Liquid reference: 34. With `:val`: 1 after this change.
- Liquid references to `q-pinning-50-digit.witness.json`: **28**. Registry
  entries on that witness: **19**. That witness has `q0Anchor: "muon"`. So any
  of these references read without a field-level anchor label is a candidate
  for the ideal/experimental straddle.
- `canonical-isotope-witness-Z*.witness.json`: **119**.
- `docs/prediction-validation-status.md`, which `qou-7p89` lists as a target,
  **does not exist**.
- The `:::observable-dashboard` fence that `qou-7p89` describes is **gone** from
  `per-observable-100x-status-dashboard.md`. The file now has a prose remark
  and no `{{ }}` binding.

Every one of these beans asks for producers to move to "the Wave-2 P0 facade",
which means `q_2t`, Form-B `α_EM`, `E₀^{(∞)}` and the projected `α_D`, followed
by regeneration. That is the same owner decision as §4, repeated over
hundreds of files. It is framed as one ask on #8526 rather than four.
