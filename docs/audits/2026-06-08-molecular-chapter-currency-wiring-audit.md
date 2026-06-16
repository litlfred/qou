# Chapter 12 "Molecular Construction" — currency + compute-wiring audit (2026-06-08)

**Scope.** Read-only audit of every block in
[`content/quantum-observable-universe/molecular-construction/`](../../content/quantum-observable-universe/molecular-construction/)
against (A) the current QOU mass/binding framework and (B) the
compute-wiring contracts (canonical-package imports, witness
freshness, LP/SDP dual-emission first-class infra). No content,
compute, Lean, or git state was modified.

---

## Summary verdict

The chapter is **structurally sound and less stale than "VERY OLD"
would suggest on the math side, but materially behind on the
compute-wiring side.** None of the three headline purges
(`λ_scale`, `Geom_full`, scalar `ρ_q`) appear anywhere in the
chapter — it is **clean** of all three. The binding scale
`α = m_e × 8G` is **current** (`prop:binding-scale-catalan`,
`8G = Vol(𝓑₃)`, G = Catalan), and `Φ₁` is the **current**
standard-Wedderburn-block transfer-matrix invariant from
`thm:wedderburn-mass-formula` — the chapter uses both consistently.
The conjectural-propagation discipline is correctly applied (all four
LP-dual props are banner-marked "conditional on
`conj:q-integer-mass-formula`"), and all `lean.ref` URIs use the
current `qou:QOU.Molecular.*` package form. Witnesses that exist are
hash-fresh.

**Top 3 issues (all compute / wiring, not math):**

1. **LP/SDP dual-emission infra is entirely absent (HIGH).** The
   chapter's central thesis is "the LP dual shadow price = binding
   energy," yet **0 of 6** molecular compute scripts route through
   the canonical `lp_dual_solver.py`, and **0 of 6** witnesses carry
   any of the mandatory dual fields (`y0_star`, `y_star`,
   `active_set`, `primal_obj`, `dual_obj`, `duality_gap`). The
   scripts do a Frobenius-positivity **enumeration/scan** labelled
   "LP dual"; `cvxpy` is an optional import that falls back when
   absent, and there is no `linprog`/`clarabel` solve. The witnesses
   only assert "binding positive." This is a direct violation of
   CLAUDE.md §"LP / SDP duals — first-class infra."

2. **Four referenced witnesses do not exist (HIGH/MED).**
   `co-molecular-binding.witness.json`,
   `co2-molecular-binding.witness.json`,
   `ch4-molecular-binding.witness.json`,
   `benzene-molecular-binding.witness.json` are named in the
   prose/manifests as the binding witnesses for CO / CO₂ / CH₄ /
   C₆H₆ but are **missing**; the corresponding `.md` blocks still
   say the witness "should be committed" / "should record …".
   Only H₂ has live binding witnesses. So CO/CO₂/CH₄/benzene are
   **narrative-only** — their numeric claims (11.09 eV, 8.28 eV,
   1.56 eV resonance, etc.) are not backed by a committed
   computation.

3. **Chapter is invisible to the canonical-chain compute (MED).**
   The molecular scripts import the in-repo `folio-assistant/
   computations/` substrate modules (`q_parameter`, `hecke_core`,
   `witness_base`) rather than the canonical PyPI packages
   (`pyhecke`, `qou_substrate`, `pyhecke_native`/Rust,
   `hecke_engine`); only `molecular-frobenius-lp.py` partially uses
   `pyhecke.gram`. The chapter's blocks/scripts are **not
   referenced by the MBA appendix** (`appendix-mass-binding-
   algorithms/`), so the maintenance contract that binds props ↔
   Python API does not cover Chapter 12. The binding formula is the
   **leading-order** 3-extremal-Wedderburn-block route
   (`Φ₁` only), not the full per-partition sum / operator-valued
   `ρ_k` expansion — defensible for binding, but worth an explicit
   currency note since `thm:wedderburn-mass-formula` itself flags
   `Φ₁/Φ₂/Φ₃` as the leading-order formula.

**Net:** the chapter does not need a framework rewrite for stale
purges (it has none). It needs (i) LP-dual emission wired through
`lp_dual_solver.py` with dual fields in the witnesses, (ii) the four
missing molecule binding witnesses actually produced, and (iii) a
currency note + appendix linkage clarifying it rides the
leading-order `Φ₁/α` route.

---

## Table 1 — Math-currency findings

| Block (label) | File | Item examined | Quoted phrase | Canonical status / replacement | Severity |
|---|---|---|---|---|---|
| `def:molecular-braid` | `molecular-braid.md` | `α = m_e × 8G` binding scale | "*where $\alpha = m_e \times 8G$ is the same binding scale as in the [atomic mass formula]*" | **CURRENT.** `α = m_e×8G` = `prop:binding-scale-catalan`, `8G = Vol(𝓑₃)`. Not stale. No change. | none |
| `def:molecular-braid` (+ all LP blocks) | `molecular-braid.md`, `h2-*`, `co-*`, `co2-*`, `ch4-*`, `benzene-*` | `Φ₁` usage | "$\mathfrak{E}_{\mathrm{bind}} = \alpha(\sum_i \Phi_1(\mathcal{A}_i) - \Phi_1(\mathcal{M}))$" | **CURRENT but leading-order.** `Φ₁ = Σᵢ ln|z·(Mᵢ)₁₂+(Mᵢ)₂₂|` is the standard-rep invariant of `thm:wedderburn-mass-formula` (the 3-extremal-block *leading-order* formula). The exact route is the per-partition Markov sum; the operator-valued `ρ_k` graded expansion (`prop:rho-k-graded-expansion`) is the deeper object. Add a one-line "leading-order Φ₁ route" currency note. | LOW |
| `thm:wedderburn-mass-formula` (referenced) | `molecular-braid.md`, `h2-binding-energy.md` | Cross-ref target | "*the same binding scale as in the [atomic mass formula](#thm\:wedderburn-mass-formula)*" | **OK** — `thm:wedderburn-mass-formula` exists and is current. Note the chapter rides its leading-order branch. | none |
| `h2-binding-energy` | `h2-binding-energy.md` | numeric value of `8G` | "$\alpha = m_e \times 8G \approx 0.511 \times 7.328 \approx 3.744\,\mathrm{MeV}$" | **CURRENT** (matches `binding-scale-catalan.md` `≈ 3.7445 MeV`). The `7.328` ≈ `Vol(𝓑₃) = 8G`. Consistent. | none |
| `def:covalent-bond-shared-trefoil` | `covalent-bond-shared-trefoil.md` | `Φ₁` contribution column | "$\Phi_1$ contribution \| $\ln\lvert V_e\rvert$ \| $\ln\lvert V_{e,i}\rvert + \ln\lvert V_{e,j}\rvert$" | **CURRENT** — consistent with the `Φ₁ = Σ ln\|…\|` definition. | none |
| `prop:ilp-covalent-bond` | `ilp-covalent-bond.md` | `E_mol` energy scale | "$E_{\mathrm{mol}} = E_{\mathrm{hartree}}/[2]_q^2 = m_e \alpha_{\mathrm{EM}}^2/(q+q^{-1})^2$ … derived from $q_0$ alone" | **CURRENT** (derived, zero-param; `hecke_core` exports `E_MOL`, `E_HARTREE_EV`, `alpha_em` from substrate). | none |
| (whole chapter) | all `.md`/`.ts`/`.lean` | `λ_scale` purge | — | **CLEAN.** `grep` for `lambda_scale`/`λ_scale` over the chapter returns nothing. | none |
| (whole chapter) | all `.md`/`.ts`/`.lean` | `Geom_full` purge | — | **CLEAN.** No `Geom_full` anywhere. | none |
| (whole chapter) | all `.md`/`.ts`/`.lean` | scalar `ρ_q = 1/ℏ_q²` purge | — | **CLEAN.** Chapter uses the `Φ₁/α` route, never the scalar density. The SUPERSEDED-ρ_q banner does **not** apply (no ρ_q usage to flag). | none |
| `prop:shell-closure-nf-term-count`, `prop:palindromicity-orbital-type` | `shell-closure-nf-term-count.md`, `palindromicity-orbital-type.md` | per-partition / NF-growth closure claims | "*growth ratio $\gamma(Z)$ … separates three regimes*"; "*$\ell$ is half the palindromic defect*" | **OK — conjectures, not Δ_λ closures.** These are GS-NF term-count / Bruhat-palindromicity conjectures, **not** per-partition binding-`Δ_λ` closures, so they do **not** collide with the "Δ_λ gate (no 7th ansatz)" rule. Correctly typed as `conjecture`. | none |
| `conj:q-integer-mass-formula` (upstream) | `mass-theory/q-integer-mass-formula.md` | BW-emergence conjecture the 4 LP props are conditional on | "*conditional on conj:palindromicity-orbital-type and conj:shell-closure-nf-term-count*" | **OK** — it is a `conjecture`; the 4 molecular props correctly inherit the conditional banner. Propagation discipline satisfied. | none |
| `prop:ilp-covalent-bond`, `prop:h2-lp-dual-binding`, … | `ilp-covalent-bond.md`, `h2-lp-dual-binding.md` | "Zero fitted parameters" claims | "*Zero fitted parameters.*"; "*$D_0(H_2)=4.4834$ eV (observed 4.478, +0.1%)*" | **Math claim consistent** with three-calibration discipline (no 4th anchor introduced). Caveat: only H₂ is witness-backed; see Table 2. | LOW |

**Math-currency conclusion:** no HIGH/MED stale-math findings. The
only math-side action is a LOW-severity currency note that the
chapter rides the **leading-order `Φ₁`** branch of
`thm:wedderburn-mass-formula` (not the exact per-partition / `ρ_k`
expansion).

---

## Table 2 — Compute-wiring findings

Validator note: `lp_dual_witness_validator.py` could not be executed
in this sandbox (`numpy`/`pyhecke` not installed →
`ModuleNotFoundError`); witness dual-field presence was checked by
direct `grep` instead. Witness freshness checked by recomputing the
`scriptHash` SHA-256 prefix and comparing to the stored value.

| Script | Path | Imports canonical pkgs? | Emits witness? | Witness fresh? | LP dual emitted? | Issue | Severity |
|---|---|---|---|---|---|---|---|
| `h2-molecular-binding.py` | `computations/` | ✗ — `q_parameter`, `hecke_core` (substrate), `witness_base`; no `pyhecke`/`qou_substrate`/`pyhecke_native` | ✓ `h2-molecular-binding.witness.json` | ✓ FRESH (`e36a50636d2c`) | ✗ no `y_star`/`dual_obj`/`active_set` | transfer-matrix enumeration; only `scriptHash`/`scriptCommitSha` in witness | HIGH (dual) |
| `h2-integer-lp.py` | `computations/` | ✗ — same substrate imports | ✓ `h2-integer-lp.witness.json` | ✓ FRESH (`ce19e30d82cc`) | ✗ none | "integer LP" is a crossing-operator scan, not a dual-emitting LP; no `lp_dual_solver` | HIGH (dual) |
| `molecular-frobenius-lp.py` | `computations/` | ◐ partial — uses `pyhecke.gram` (`z`, `NF_BASIS`, `TR_M`) **but** also 3 local impls (`reduce_nf_dict`, `np.linalg.eigvals` Gram) | ✓ `molecular-frobenius-lp.witness.json` | ✓ FRESH (`2fca5a777687`) | ✗ — `cvxpy` optional, falls back; no `y_star`/gap | "Frobenius LP dual" in description but no dual fields emitted; not routed via `lp_dual_solver` | HIGH (dual) |
| `molecular-trefoil-scan.py` | `computations/` | ✗ — substrate imports only | ✓ `molecular-trefoil-scan.witness.json` | ✓ FRESH (`bab7f99afedf`) | ✗ none (scan, not LP) | knot-operator scan; fine as a scan but no canonical-pkg wiring | MED |
| `unified-mass-molecular.py` | `computations/` | ✗ — `q_parameter`, `experimental_constants`, `hecke_core` | ✓ `unified-mass-molecular.witness.json` | ✓ FRESH (`cad39184f169`) | ✗ none | clean of `λ_scale`/`Geom_full`/`mass_endomorphism`; just not canonical-pkg-wired | MED |
| `ch-bond-writhe-lp.py` | `computations/` | ✗ — substrate imports only | ✓ `ch-bond-writhe-lp.witness.json` | ✓ FRESH (`5fc24bf4e87f`) | ✗ none | this is `def:molecular-braid`'s primary `computation.script`; "lp" in name but no dual | HIGH (dual) |

**Missing witnesses referenced by chapter prose/manifests:**

| Referenced witness | Referenced by | Status |
|---|---|---|
| `co-molecular-binding.witness.json` | `co-triple-bond-energy.md` ("*The witness file `co-molecular-binding.witness.json` should record…*") | **MISSING** |
| `co2-molecular-binding.witness.json` | implied by §5 | **MISSING** |
| `ch4-molecular-binding.witness.json` | implied by §6 | **MISSING** |
| `benzene-molecular-binding.witness.json` | implied by §7 | **MISSING** |
| `h2-molecular-binding.witness.json` | `h2-binding-energy.md` ("*should be committed as …*") | **EXISTS** (already committed; the prose note is stale) |

**Manifest `computation` field accuracy:**

- `def:molecular-braid` (`molecular-braid.ts`) → `script:
  ch-bond-writhe-lp.py` + 4 witnesses
  (`ch-bond-writhe-lp`, `molecular-frobenius-lp`,
  `molecular-trefoil-scan`, `unified-mass-molecular`). **All point at
  real, current files.** `status: "experimental"`.
- `prop:h2-lp-dual-binding` (`h2-lp-dual-binding.ts`) → `script:
  h2-integer-lp.py` + witnesses `h2-integer-lp`,
  `h2-molecular-binding`. **Both exist.** `status: "verified"` —
  arguably overstated given no LP-dual fields, but the H₂ binding
  numbers are witness-backed.
- CO / CO₂ / CH₄ / benzene blocks carry **no `computation` field**
  in their `.ts` and reference witnesses that do not exist (above).

**Appendix linkage:** the MBA maintenance-contract appendix
(`appendix-mass-binding-algorithms/`) **does not reference any
molecular block or script** (only `mba-step10-confinement-sdp.md`
matched on the generic "LP" hint, unrelated to Ch 12). So per
CLAUDE.md §"🟧 Mass-and-Binding-Algorithms appendix sync," the
molecular binding compute is outside the contract — flag for the
LP/SDP-dual sidecar (`mba-sidecar-lp-sdp-dual-emission.md`) once the
duals are wired.

---

## Table 3 — Lean / manifest findings

| Block | File | `lean.ref` form | `validation` field | Finding | Severity |
|---|---|---|---|---|---|
| all 16 blocks with Lean | `*.ts` | **current** `qou:QOU.Molecular.*` (e.g. `qou:QOU.Molecular.MolecularBraid`, `qou:QOU.Molecular.covalent_bond_is_ilp_optimal`) | mix of `not_checked` / `not_started` | **No legacy `decl:`/`file:` anywhere.** URI shape is current. | none |
| `def:molecular-braid` | `molecular-braid.lean` | — | — | `.lean` docstring says "**Ch. 10**, §molecular-braid" — **stale chapter number** (chapter is 12, and `ilp-covalent-bond.lean` correctly says "Ch 12"). The binding formula in the docstring `E_bind = α(Σᵢ Φ₁(Aᵢ) − Φ₁(M))` is current. | LOW |
| `prop:ilp-covalent-bond` | `ilp-covalent-bond.lean` | `qou:QOU.Molecular.covalent_bond_is_ilp_optimal` | — | `covalent_bond_is_ilp_optimal` proves only `inverse_trefoil.length = 3` (`rfl`) — a placeholder; the real ILP-optimality claim is unproven. `h2_binding_energy` is an `axiom` with a `-- Ref:` (acceptable for an asserted numeric bound). Plausible/honest, not stale. | LOW |
| `def:molecular-braid` | `molecular-braid.ts` | `validation: "not_checked"` | — | Lean `structure MolecularBraid` is a data scaffold (no proofs); manifest `not_checked` is accurate. | none |
| LP-dual props (h2/co/co2/ch4/shell-filling) | `*.ts` | `validation: "not_started"` | — | Accurately reflects that these Lean decls are stubs. | none |

**Lean conclusion:** manifest shapes are current and honest. Only
LOW items: a stale "Ch. 10" in one docstring and placeholder-level
Lean proofs (expected for an experimental chapter).

---

## Prioritized fix plan

### (i) Mechanical / safe fixes (low risk, high signal)

1. **Delete the 4 stale "witness should be committed/recorded"
   sentences** OR (better) **produce the 4 missing witnesses**
   (`co-`, `co2-`, `ch4-`, `benzene-molecular-binding.witness.json`)
   so CO/CO₂/CH₄/benzene numeric claims are backed. Until produced,
   the prose claims (11.09 eV, 8.28 eV, 1.56 eV resonance) are
   unwitnessed. *(HIGH-value; the witness production is small per
   molecule.)*
2. **Fix the stale chapter number** "Ch. 10" → "Ch. 12" in
   `molecular-braid.lean` docstring.
3. **Drop the now-stale H₂ prose note** "*The witness computation
   should be committed as `h2-molecular-binding.witness.json`*" in
   `h2-binding-energy.md` — it already exists.
4. **Add `computation` manifest fields** to the CO/CO₂/CH₄/benzene
   `.ts` blocks once their scripts/witnesses exist (currently
   absent).

### (ii) Framework-currency rewrites (small, optional)

5. **Add a one-line "leading-order Φ₁ route" currency note** to
   `def:molecular-braid` (and/or the chapter intro) stating the
   molecular binding uses the leading-order standard-Wedderburn-block
   `Φ₁` invariant of `thm:wedderburn-mass-formula`, and that the
   exact per-partition Markov sum / operator-valued `ρ_k` expansion
   (`prop:rho-k-graded-expansion`) is the deeper object — so a reader
   does not mistake `Φ₁` for the full mass functional. *(LOW; this is
   a precision-of-framing note, not a correction.)*
6. **No purge rewrites required** — chapter is clean of `λ_scale`,
   `Geom_full`, scalar `ρ_q`.

### (iii) Compute rewiring (the substantive work)

7. **Route every molecular LP through `lp_dual_solver.py`** —
   `solve_operator_selection_lp(t, G, n_target)` /
   `solve_psd_operator_selection_sdp(...)` — and emit the mandatory
   dual fields (`y0_star`, `y_star`, `active_set`, `primal_obj`,
   `dual_obj`, `duality_gap`) in every molecular witness. Priority
   targets: `ch-bond-writhe-lp.py` (the `def:molecular-braid`
   primary script), `h2-integer-lp.py`, `molecular-frobenius-lp.py`.
   This is the single biggest gap: the chapter's thesis is "shadow
   price = binding energy," so the dual is the load-bearing output
   and is currently never emitted. *(HIGH.)*
8. **Migrate substrate-module imports to canonical packages** where
   cheap: `pyhecke` (Hecke/Gram/Markov), `qou_substrate` (q₀,
   `WitnessBuilder`). `molecular-frobenius-lp.py` already half-uses
   `pyhecke.gram`; finish it and remove the 3 local impls
   (`reduce_nf_dict`, local Gram eig). *(MED.)*
9. **Wire Chapter 12 into the MBA appendix contract.** Either add a
   molecular `alg:`-block, or at minimum register the molecular LP
   scripts/witnesses under `mba-sidecar-lp-sdp-dual-emission.md` once
   the duals exist, so the props↔Python-API contract covers the
   chapter. *(MED.)*

---

## Open questions for the owner

1. **Is Chapter 12 intended to be promoted to production, or remain
   exploratory?** Several props are `status: "experimental"` and CO/
   CO₂/CH₄/benzene are narrative-only. If exploratory, the dual-
   emission + witness-production work (fix plan iii) can be deferred;
   if heading for production, it should land before the chapter is
   cited downstream.
2. **Should the four missing molecule binding witnesses be produced,
   or should the unwitnessed numeric claims (11.09 eV CO, 8.28 eV
   CO₂, 1.56 eV benzene resonance) be demoted to "expected/
   illustrative" until computed?** The H₂ path is the only fully
   witnessed one.
3. **Is the leading-order `Φ₁` binding route the intended final form
   for molecules, or a placeholder for the operator-valued `ρ_k`
   expansion?** The chapter is internally consistent on the `Φ₁/α`
   route, but it does not connect to the `prop:rho-k-graded-
   expansion` machinery that the rest of the mass/binding program has
   moved to. (No action if `Φ₁` is deliberately the molecular-binding
   altitude.)
4. **`prop:h2-lp-dual-binding` carries `status: "verified"` despite
   emitting no LP-dual fields.** Should "verified" be reserved for
   witnesses that actually carry the dual, or is binding-positivity
   sufficient for that label here?

---

*Audit method: static read of all `.md`/`.ts`/`.lean` in the
chapter + the canonical-derivation cheat sheet, `binding-scale-
catalan.md`, `wedderburn-mass-formula.md`, `q-integer-mass-
formula.md`, `kashaev-volume-density.md` (SUPERSEDED-ρ_q banner
source), the MBA appendix, and the 6 molecular compute scripts +
their witnesses. Purge greps, witness-hash recomputation, and
manifest-link resolution run locally. `lp_dual_witness_validator.py`
not run (sandbox missing `numpy`/`pyhecke`); dual-field absence
confirmed by direct grep. No files modified; no git operations.*
