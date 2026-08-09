# The canonical nucleon ordering is a live production DOF — and the corpus's own selection rule disagrees with it

**Date:** 2026-08-09 · **Bean:** `qou-48is` (spun out of `qou-prjo`) — stays **OPEN**
**Branch:** `claude/canonical-ordering-dof-2026-08-09` · **PR** [#4851](https://github.com/litlfred/qou/pull/4851)
**Predecessor:** [#4850](https://github.com/litlfred/qou/pull/4850) —
[`2026-08-09-nastokes-orbit-symmetric-readout.md`](2026-08-09-nastokes-orbit-symmetric-readout.md) §7

---

## 0. The two answers, in plain language

**Q1 — is it live in production, or confined to probes?** **Live in production.**
The `A ≥ 3` binding chain reaches a hardcoded `["p"] * Z + ["n"] * N` inside the
production closed form, and **14 968** mixed-species `A ≥ 3` rows of
[`mass-table-comprehensive.witness.json`](../../computations/mass-table-comprehensive.witness.json)
— the table the canonical-derivation cheat sheet cites for the per-isotope error
budget — carry a `B_pred_MeV` (and hence an `m_symbolic_MeV` and an
`m_err_pct_sym`) that moves when the arrangement changes. On tritium the freedom
is **1.15 MeV = 13.6 % of `B_AME`**; 60 rows exceed 1 % of `B_AME`; the largest
absolute spread is 33.9 MeV. The `L1`/`L2` dashboards are **not** affected — they
carry no `A ≥ 3` observable at all (§2.3).

**Q2 — derivable, multiset-determined, or a free DOF?** The honest answer is
sharper than the three candidates the bean anticipated, and it is worse for the
framework than "no rule exists":

> **A selection rule DOES exist in the corpus — and production does not implement
> it. The two live conventions disagree for every `A ≥ 4`, and on the production
> readout they are opposed in sign.**

`prop:ground-state-ordering`
([`mass-theory/ground-state-ordering.md`](../../content/quantum-observable-universe/mass-theory/ground-state-ordering.md))
states a *variational* rule — minimise `Φ_q = Σ_i log|V̂_i|` — and derives that the
minimiser is **interleaved** (`pnpnpn…`) for `A ≥ 4`, with sorted optimal *only*
for `A ≤ 3`. Production uses sorted for **every** `A`. Measured under the
production trace, the corpus's own ground-state ordering is strictly **less**
bound at every `A ≥ 4`: −0.27 MeV (⁴He), −0.54 (⁶Li), −1.36 (¹²C), −1.91 (¹⁶O),
−6.80 (⁵⁶Fe).

Neither convention is proved. So the degree of freedom is **not closed** — it is
re-described, from *"an unlicensed choice with no rule"* to *"two live
conventions, disagreeing, neither derived."*

Probe: [`canonical_ordering_dof_probe.py`](../../computations/probes/canonical_ordering_dof_probe.py)
→ `canonical-ordering-dof.witness.json`. **22/22 assertions, 41 s.**
`free_parameters = 0`; q₀ = experimental proton anchor; nothing wired; **no
ordering is recommended.**

---

## 1. Q1 — the production trace

### 1.1 The chain

Established from source, not asserted (probe Part 0, six mechanical checks):

| step | file | what it does |
|---|---|---|
| 1 | [`mass_table_comprehensive.py`](../../computations/mass_table_comprehensive.py) `try_binding_symbolic_log_trace` / `try_binding_canonical` | emits the `B_pred_MeV` column of the 65-isotope production table |
| 2 | → [`binding_canonical.py`](../../computations/binding_canonical.py) `binding_canonical(Z, N, use_closed_form=True)` | the appendix calls this a **"production binding consumer … (A ≥ 3)"** — [`mba-step03-markov-trace.md`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step03-markov-trace.md) |
| 3 | → [`closed_form_tau_M.py`](../../computations/closed_form_tau_M.py) `closed_form_tau_M` → `closed_form_ratio` | `τ_M = τ_p^Z · τ_n^N · ∏ᵢ fᵢ(q)` |
| 4 | → `closed_form_ratio` **line 290** | `ordering_list: list[str] = ["p"] * Z + ["n"] * N` |

Line 290 is the whole finding. The same hardcode appears again in
`canonical_interface_kinds` (line 233), so **both** convention branches carry it,
and `mass_at_3A_proper.atom_braid_word_3A` builds the explicit word the same way.

### 1.2 What the arrangement moves

`B_pred = −α·ln(τ_M)` with `α = m_e · 8 · Catalan = 3.744460 MeV`
(`try_binding_symbolic_log_trace`). Because `τ_M` factorises multiplicatively
(§3.1), **the ordering shift is exactly additive**:

$$\Delta B \;=\; -\alpha \ln \bigl(\tau_M(\text{ordering}) / \tau_M(\text{canonical})\bigr).$$

No AME quantity enters that computation. It also propagates to `m_symbolic_MeV`
(`= m_unbound − B_pred`) and to `m_err_pct_sym`.

The reachable range per isotope, at the experimental proton anchor
(`strict_averaged`, the convention `binding_canonical` passes explicitly):

| atom | Z | N | `B_pred` | `B_AME` | ΔB min | ΔB max | spread | % of `B_AME` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| T | 1 | 2 | 8.473 | 8.482 | −1.152 | 0.000 | **1.152** | **13.58** |
| ³He | 2 | 1 | *n/a* | *n/a* | 0.000 | +0.880 | 0.880 | — |
| ⁴He | 2 | 2 | *n/a* | *n/a* | −1.152 | +0.880 | 2.031 | — |
| ⁶Li | 3 | 3 | 18.131 | 31.994 | −1.424 | +0.880 | 2.303 | 7.20 |
| ⁷Li | 3 | 4 | 23.062 | 39.245 | −1.696 | +0.880 | 2.576 | 6.56 |
| ⁹Be | 4 | 5 | 30.357 | 58.165 | −1.968 | +0.880 | 2.848 | 4.90 |
| ¹²C | 6 | 6 | 40.015 | 92.162 | −2.240 | +0.880 | 3.120 | 3.39 |
| ¹⁶O | 8 | 8 | 54.604 | 127.619 | −2.785 | +0.880 | 3.664 | 2.87 |
| ⁴⁰Ca | 20 | 20 | 142.139 | 342.052 | −6.051 | +0.880 | 6.930 | 2.03 |
| ⁵⁶Fe | 26 | 30 | 205.630 | 492.254 | −7.956 | +0.880 | 8.835 | 1.79 |

Whole table: **14 968** exposed rows; **60** with a spread above 1 % of `B_AME`;
largest absolute spread **33.874 MeV** (²³⁷Og).

> **AME's role here is a denominator only.** It expresses the size of an
> already-computed spread. Selecting an ordering because it reproduces AME is
> the forbidden fit, and it is not done anywhere in this audit — which matters
> especially, since the finding is precisely about an unlicensed choice.

*Incidental (not this bean):* ³He `(2,1)` and ⁴He `(2,2)` have **no rows at all**
in `mass-table-comprehensive.witness.json`, although `5He … 12He` do. Recorded
for whoever owns that table.

### 1.3 What is NOT affected — do not inflate this

- **The `L2` 100× dashboard is untouched.**
  [`per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json)
  has exactly seven rows — `m_p`, `m_μ`, `Q_β`, `m_n`, `Δ_pn`, `m_e`, `m_K/m_π` —
  every one of them `A ≤ 1`. `m_D` / `m_T` / `m_3He` / `m_4He` appear in that
  script's `OBSERVABLES` dict as CODATA *targets*, but **no prediction row is
  emitted** for them. The canonical **2/7** count is unchanged.
- **`L1` (`onepb-status-dashboard`) is untouched** — no `A ≥ 3` content.
- **`canonical_mass.py` is untouched.** The facade reads
  `m-p-substrate-identity-50dps.witness.json`; `m_p` / `m_n` come from the
  muon-anchored Hecke energy `m_p = 2(m_μ·F_Bor − 6 m_e)`, whose `F_Bor` is the
  *Borromean* braid — a single-nucleon object with no cross-species arrangement.
  **No nucleon mass moves.**
- **`mass_table_ppb.py` is untouched** — it is the Kashaev volume law over
  atom→knot assignments, and never calls `atom_braid_word_3A`.
- **The deuteron is exactly ordering-independent** (null control, §3.3).

So the blast radius is: the `A ≥ 3` **binding** table and everything downstream
of it. That is a real, published surface, and it is not the headline precision
ledger.

---

## 2. Phase 0 — corpus grep (mandatory)

Per AGENTS.md §"Before declaring open math". Searched `content/`,
`computations/`, `docs/audits/`, `docs/coordination/` for `interface-minimal`,
minimal-crossing, ground-state ordering, variational/SDP selection, Markov-move
and normal-form/Gröbner–Shirshov arguments over arrangements.

**The bean's premise is overturned by this grep.** `qou-48is` records that
*"interface-minimal appears as a cost property, not a selection rule"*. That
reading is correct **about `atom_orbit_reduction.py`** — and it is the wrong
place to have stopped. A selection rule lives elsewhere in the corpus:

| corpus object | says |
|---|---|
| [`mass-theory/ground-state-ordering.md`](../../content/quantum-observable-universe/mass-theory/ground-state-ordering.md) (`prop:ground-state-ordering`) | *"the ground-state nucleon ordering — the one minimising the quantum dilogarithm volume `Φ_q = Σᵢ log\|V̂ᵢ\|` — is, for `A ≥ 4`,"* **interleaved** + tail packing; **(iii)** *"for small `A` (`A ≤ 3`), the sorted ordering (all protons first) beats interleaving"* |
| [`ground-state-ordering-derivation.md`](../../content/quantum-observable-universe/mass-theory/ground-state-ordering-derivation.md) | eigenvalue derivation (`T_pp ↦ q` growth, `T_nn ↦ q⁻¹` decay, `T_pn` traceless "neutral spacer"); *"Exhaustive search over all `C(A,Z)` orderings confirms the derived rule for `A ≤ 14`"*; interleaving wins *"by factors of 2–10× in `\|Φ_q\|`"* |
| [`nuclear-interactions/atomic-nf-witness.md`](../../content/quantum-observable-universe/nuclear-interactions/atomic-nf-witness.md) | *"The ground-state nucleon ordering is the global minimum of `Φ₁` over all `C(A,Z)` permutations."* |
| [`hecke_core_symbolic.py`](../../computations/substrate/hecke_core_symbolic.py) `_ground_state_ordering` | *"Match `hecke_core.build_atom_nf` — interleaved p/n ordering"* |
| [`ordering_cache.py`](../../computations/ordering_cache.py), `HeckeEngine.ground_state_ordering` (Rust), [`hadron_knot_table.py`](../../computations/hadron_knot_table.py) | a cached exhaustive/Rust ground-state search keyed by `(Z, N)` |
| [`atom_orbit_reduction.py`](../../computations/atom_orbit_reduction.py) | *"interface-minimal … the cheapest (canonical) one is always valid"* — the **cost** framing, justified by the `S_Z × S_N` identity, which the arrangement never leaves |

**Negative findings** (recorded so a later agent does not re-search): no
Markov-move argument, no Gröbner–Shirshov normal-form argument, and no LP/SDP
selection over *nucleon arrangements* was found (the LP/SDP ordering selections
that do exist — `h2-lp-dual-binding`, `ch4-tetrahedral-from-phi1` — are
**molecular** strand orderings, a different object). And **no** corpus object
reconciles the sorted production convention with `prop:ground-state-ordering`.

---

## 3. Q2 — the three candidates, decided

The production interface product, with the arrangement supplied instead of
hardcoded, is
`P(o) = ∏_{adjacent pairs} f(type)`, `f_pp = z`, `f_nn = z − h`,
`f_pn = z − h/2` (or `z − h(½ − δ/4)` under `bring_color_weighted`).
The probe's generalisation reproduces the production function **bit-for-bit** on
the canonical string for all `0 ≤ Z, N ≤ 6` and both conventions (worst relative
difference **0.0**), which is what makes everything below a statement about
production and not about a model of it.

### 3.1 The exact structure

$$P(o) \;=\; f_{pp}^{\,n_{pp}}\, f_{nn}^{\,n_{nn}}\, f_{pn}^{\,n_{pn}},
\qquad n_{pp} = Z - b_p,\; n_{nn} = N - b_n,\; n_{pn} = b_p + b_n - 1$$

where `b_p`, `b_n` count the maximal p-runs and n-runs. Hence

$$\boxed{\;\frac{P(o)}{P(\text{canonical})} \;=\; \Bigl(\frac{f_{pn}}{f_{pp}}\Bigr)^{b_p-1}\Bigl(\frac{f_{pn}}{f_{nn}}\Bigr)^{b_n-1}\;}$$

Verified on **all 3140** arrangements of every isotope with `Z, N ≤ 6`,
`Z + N ≤ 10`, both conventions, to **8.0e−51** (the 50-dps floor).

### 3.2 Candidate 1 — an extremal principle selects the canonical: **REFUTED**

At the experimental proton anchor `q₀ = 1.1099785827513808…`:

| | `strict_averaged` | `bring_color_weighted` |
|---|---|---|
| `f_pp = z` | 0.499320334183694 | 0.499320334183694 |
| `f_nn = z − h` | 0.290260035388055 | 0.290260035388055 |
| `f_pn` | 0.394790184785875 | 0.394862086413968 |
| `u = f_pn/f_pp` | **0.790655132103** `< 1` | **0.790799131102** `< 1` |
| `v = f_pn/f_nn` | **1.360125875607** `> 1` | **1.360373590136** `> 1` |

**`u` and `v` sit on opposite sides of 1.** Adding a p-block strictly lowers the
trace; adding an n-block strictly raises it. The canonical `(b_p, b_n) = (1, 1)`
minimises *both* exponents, so it is a **saddle** — the corner of a function
strictly monotone in each argument, and monotone in opposite directions.
Measured, over every arrangement:

| atom | #orderings | argmin | min/canonical | argmax | max/canonical | canonical extremal? |
|---|---:|---|---:|---|---:|---|
| ⁴He | 6 | `pnnp` | 0.7908 | `nppn` | 1.3604 | **no** |
| ⁶Li | 20 | `pnnnpp` | 0.7908 | `nppnpn` | 1.4635 | **no** |
| ⁸Be | 70 | `pppnnnnp` | 0.7908 | `nppnpnpn` | 1.5744 | **no** |
| ⁷Li | 35 | `pnnnnpp` | 0.7908 | `npnpnpn` | 1.5744 | **no** |
| ¹²C | 924 | `pnnnnnnppppp` | 0.7908 | `npnpnpnpnppn` | 1.8220 | **no** |
| ¹⁶O | 12 870 | `ppppnnnnnnnnpp` | 0.7908 | `npnpnpnpnpnpnp` | 2.1086 | **no** |

So **no extremal principle on this functional can select the sorted arrangement.**
That is a **scope-(b)** exclusion — §5.

### 3.3 Candidate 2 — the observable depends only on the interface multiset

**The premise is true** and is now proved in closed form (§3.1) and in Lean
(`ifaceProd_eq_of_ifaces_perm`). Arrangements sharing an interface multiset give
identical traces; #4850 measured that independently at `0.0e+00`/`1e−16`.

**But it does not resolve the question**, because the multiset is *not an
invariant of the isotope*:

| atom | Z | N | #arrangements | **distinct interface multisets** |
|---|---:|---:|---:|---:|
| **D** | 1 | 1 | 2 | **1** ← null control: exactly ordering-independent |
| T | 1 | 2 | 3 | 2 |
| ³He | 2 | 1 | 3 | 2 |
| ⁴He | 2 | 2 | 6 | 4 |
| ⁶Li | 3 | 3 | 20 | 7 |
| ⁹Be | 4 | 5 | 126 | 11 |

The freedom is merely **re-coordinatised** — from *which arrangement* to *which
multiset*, i.e. to the pair `(b_p, b_n)`. Nothing is removed. (The deuteron row
is why #4850's D control came out null: `A = 2` has one interface class, so the
freedom switches on only at `A ≥ 3` with both species present.)

### 3.4 Candidate 3 — a genuine undeclared DOF: **survives, in a sharper form**

Not "no rule exists" but **two live conventions, disagreeing**:

| | production `A ≥ 3` binding | corpus selection rule |
|---|---|---|
| arrangement | **sorted** `p…pn…n`, every `A` | **interleaved** + tail packing for `A ≥ 4`; sorted only for `A ≤ 3` |
| where | `atom_braid_word_3A`, `closed_form_ratio` (hardcoded), `atom_orbit_reduction` | `prop:ground-state-ordering`; `hecke_core_symbolic._ground_state_ordering`, `ordering_cache`, Rust `HeckeEngine` |
| status | convention, no stated justification beyond interface-minimal *cost* | **stated, not proved** — see §3.5 |

Evaluated under the **production** trace (`strict_averaged`, `q₀` proton anchor):

| atom | sorted (production) | interleaved (corpus rule) | `τ` ratio | ΔB (MeV) |
|---|---|---|---:|---:|
| T | `pnn` | `pnn` | 1.000000 | 0.000 |
| ³He | `ppn` | `pnp` | 0.790655 | +0.880 |
| ⁴He | `ppnn` | `pnpn` | 1.075391 | **−0.272** |
| ⁶Li | `pppnnn` | `pnpnpn` | 1.156465 | **−0.544** |
| ⁷Li | `pppnnnn` | `pnpnpnn` | 1.156465 | **−0.544** |
| ⁹Be | `ppppnnnnn` | `pnpnpnpnn` | 1.243651 | **−0.816** |
| ¹²C | `ppppppnnnnnn` | `pnpnpnpnpnpn` | 1.438239 | **−1.361** |
| ¹⁶O | `pppppppp nnnnnnnn` | `pnpnpnpnpnpnpnpn` | 1.663272 | **−1.905** |
| ⁴⁰Ca | sorted | interleaved | 3.978852 | **−5.171** |
| ⁵⁶Fe | sorted | interleaved | 6.153964 | **−6.804** |

The corpus's own ground-state arrangement is **strictly less bound** than the
production one at every `A ≥ 4`. The two conventions are not merely different —
on the production readout they are **opposed in sign**: the arrangement the
corpus calls the ground state is, under production's own trace, the one that
binds *least*.

> **This is a disagreement between two corpus objects, not an arithmetic error
> in either.** `Φ_q = Σᵢ log|V̂ᵢ|` (per-generator transfer-matrix volumes) and
> `ln τ_M` (the closed-form Markov trace) are **different functionals** — `V̂ᵢ`
> depends on the chain-reduced state at generator `i`, not only on the local
> interface type. Reconciling them, or declaring one the binding channel, is
> exactly the work that has not been done.

*Also incidental:* `hecke_core_symbolic._ground_state_ordering` does **not**
implement rule **(iii)** (the `A ≤ 3` boundary correction): at ³He it returns
`pnp`, whereas `prop:ground-state-ordering` (iii) says sorted `ppn` wins for
`A ≤ 3`. So the compute helper and the proposition disagree at `A = 3` as well.

### 3.5 The corpus rule is stated, not proved

[`QOU/ParticleInteractions/ground_state_ordering.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/ground_state_ordering.lean)
is `def ground_state_ordering … : Prop := …` over a context class, with **no
discharging instance** — honestly the open state (§3b), not a proof. The `.md`
derivation is an eigenvalue heuristic plus an exhaustive search verified only for
`A ≤ 14`; the `A > 14` rule is an extrapolation. The `.ts` carries
`validation: "not_checked"`.

So the rule is a **candidate principle, not a closed one**. It cannot be wired to
production as canonical on this evidence, and this audit does not propose wiring
it. What it does establish is that production's convention is not merely
*unlicensed* — it is *contradicted* by the only selection rule the corpus states.

---

## 4. Cross-validation — the closed form is the real trace

The block factorisation is not an artefact of the closed form. Two **independent**
full `H_{3A}` Markov-trace pipelines reproduce the single-interface ratio, each
against the closed form under its own p-n convention:

| pipeline | ratio | measured | closed form | rel. |
|---|---|---|---|---|
| Wenzl bridge, `strict_averaged` word (this session, `n = 9`, 50 dps) | T `npn/pnn` | 1.3601258910929 | 1.3601258756069 | **1.1e−8** |
| " | ³He `pnp/ppn` | 0.79065512657064 | 0.79065513210330 | **7.0e−9** |
| `y_λ × Hoefsmit χ`, `bring_color_weighted` word (#4850 Part B) | T `npn/pnn` | 1.3603735901364 | 1.3603735901364 | **3.4e−14** |
| " | ³He `pnp/ppn` | 0.79079913110164 | 0.79079913110188 | **3.1e−13** |

The same-multiset null control (`pnn` vs `nnp`, full trace) is `4.2e−10` — so the
`1e−8` agreement is ~30× the pipeline's own floor, against an effect of 36 %.

---

## 5. Scope classification

Per AGENTS.md §"Before declaring refuted / ruled out / dead end".

**scope-(b) — for candidate 1 only.** *The sorted arrangement is not an extremum
of the production interface product.* **Cited invariant:** the exact block
factorisation (§3.1, verified on every arrangement with `Z, N ≤ 6`) together with
`f_pn/f_pp < 1 < f_pn/f_nn` at the substrate anchor. Two base ratios on opposite
sides of 1 make the canonical corner a saddle of a function strictly monotone in
each argument — an exclusion by a proved structural property, not a failed search.
Lean: `canonical_saddle` / `canonical_not_extremal` (sorry-free, with the two
inequalities as hypotheses).

**scope-(a) — everything else.**

- **(a⁺)** The chain is traced and the sizes are measured exactly. Q1 is settled.
- **(a⁻)** **Nothing is determined.** This audit does not derive the arrangement
  and does not choose one. A selection rule of a different kind — a confinement
  or SDP argument over arrangements, a Markov-move argument, a normal-form
  argument, a coordination-graph constraint — is **not excluded** and was not
  searched exhaustively; §2 records only that none was found.

**What is NOT claimed:**

- **Not** that `prop:ground-state-ordering` is wrong. It is *unproved*, and it
  *disagrees with production*. Which of the two is right is open.
- **Not** that any published `m_p` / `m_n` / `m_μ` / `Q_β` / `Δ_pn` / `m_K/m_π`
  number moves. None does (§1.3). The `L2` count stays **2/7**.
- **Not** that the ordering should be changed. No ordering is recommended, and
  **no ordering was chosen by comparison to AME** — the forbidden fit, and the
  one that would be most damaging here.
- **Not** that `A ≥ 3` binding is "wrong by 13.6 %". The number is what it is
  under a stated convention; what is undetermined is the convention.

---

## 6. Lean

[`QOU/MassTheory/CanonicalOrderingSaddle.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/CanonicalOrderingSaddle.lean)
— `scripts/lean-verify.sh` **exit 0, zero warnings**; `#print axioms` on all six
declarations gives at most `[propext, Classical.choice, Quot.sound]`. No
`sorryAx`, no `axiom`, no `native_decide`, no `: True`, no tautological
conclusion. §7c-clean: `[CommMonoid R]` for the structural half, and the ordered
half takes `[CommRing R] [LinearOrder R] [IsStrictOrderedRing R]` rather than
specialising to `ℝ`.

| Declaration | Statement |
|---|---|
| `ifaceProd` | the production `closed_form_ratio` product with the arrangement as a parameter |
| **`ifaceProd_eq_of_ifaces_perm`** | the product is a function of the interface **multiset** alone — candidate 2's premise, proved |
| **`ifaces_not_determined_by_species_counts`** | but two arrangements of the *same* `(Z, N)` have different multisets — so candidate 2 re-coordinatises rather than resolves |
| `ifaces_ppnn_not_perm_ifaces_pnnp` | hence the two interface lists are not permutations of one another |
| `ifaceProd_deuteron_ordering_independent` | the `A = 2` null control, for every `f` |
| **`canonical_saddle`** / **`canonical_not_extremal`** | if `f_nn < f_pn < f_pp`, then among arrangements of 2p + 2n one is strictly below the canonical and one strictly above ⇒ not an extremum |

> **`sorry-free ≠ derived`.** The Lean proves the *shape* of the ordering
> dependence. It derives no binding energy, no `Δ_λ`, no `tr_M` value, and
> compares nothing to AME. `canonical_saddle` is a **conditional**: its two
> inequalities are hypotheses, verified numerically at the experimental proton
> anchor by the probe. Cite the theorem and the probe together.

---

## 7. Discipline record

- `free_parameters = 0`. **No AME/CODATA quantity selects anything**; AME appears
  only as a denominator in §1.2 to express the size of an already-computed
  spread. No ordering is recommended and **nothing is wired**.
- q₀ = **experimental proton anchor** (`q_parameter.Q_50_DIGIT_STR`; owner
  directive 2026-08-07) — the same pin the production chain uses. Layer-pure; no
  muon-built cache is read anywhere in this probe.
- Both live p-n conventions (`strict_averaged`, which `binding_canonical` passes
  explicitly, and `bring_color_weighted`, the `atom_braid_word_3A` /
  `closed_form_ratio` default) are covered throughout; the conclusion is
  identical under both.
- Arithmetic: mpmath 50 dps; structural identities verified to `8e−51`; the
  measured effects exceed that floor by ~50 orders.
- Run cost 41 s, single process — no long-compute logging discipline needed.
- Lean sorry-free, `#print axioms` clean on all six declarations.
- Bean `qou-48is` stays **OPEN**; `qou-prjo` is unaffected (this is the fallout
  item #4850 §7 spun out, not a transverse-route matter).

---

## 8. What would close this

Recorded for whoever picks the bean up:

1. **Reconcile the two functionals.** Is `Φ_q = Σᵢ log|V̂ᵢ|` (transfer-matrix,
   the ground-state rule's objective) the same binding channel as `ln τ_M` (the
   closed-form Markov trace, production's objective)? They disagree in sign about
   interleaving. Until that is settled, "the ground state" is ambiguous.
2. **Prove or refute `prop:ground-state-ordering`.** Its Lean is a `Prop` with no
   instance; its derivation is a heuristic plus `A ≤ 14` search. If it is right,
   production is using the wrong arrangement for every `A ≥ 4`.
3. **Or build the observable to not depend on the arrangement** — e.g. a genuine
   sum over arrangements with a derived weight. Note this is *not* the `S_Z × S_N`
   symmetrization, which #4850 proved is the identity map.
4. **Either way, declare the convention explicitly in production** rather than
   leaving it implicit in a hardcoded list literal at `closed_form_tau_M.py:290`.

Fixing `hecke_core_symbolic._ground_state_ordering` to honour rule (iii) at
`A ≤ 3`, and the absent ³He/⁴He rows in `mass-table-comprehensive.witness.json`,
are small separate items surfaced along the way.
