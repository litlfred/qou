# Two ordering loose ends: the A=3 helper is the defective side, and ³He/⁴He are deleted by a dedup guard whose premise is false

**Date:** 2026-08-09 · **Bean:** `qou-48is` — stays **OPEN**
**Branch:** `claude/ordering-loose-ends-2026-08-09` · **PR** [#4854](https://github.com/litlfred/qou/pull/4854)
**Predecessor:** [#4851](https://github.com/litlfred/qou/pull/4851) —
[`2026-08-09-canonical-ordering-dof-production-impact.md`](2026-08-09-canonical-ordering-dof-production-impact.md) §8,
which recorded both items as "small separate items surfaced along the way" and
did not settle either.

> **Scope bar (owner, this session): DIAGNOSTIC ONLY.** Production was **not**
> switched to the ground-state ordering, the `A ≥ 3` binding table was **not**
> regenerated, `closed_form_tau_M` was **not** rewired, and **no published
> number changed**. Reconciling the two live ordering conventions remains an
> owner decision and is not taken here.

Probe: [`ground_state_ordering_a3_probe.py`](../../computations/probes/ground_state_ordering_a3_probe.py)
→ [`computations/probes/ground-state-ordering-a3.witness.json`](../../computations/probes/ground-state-ordering-a3.witness.json). `free_parameters = 0`; q₀ =
experimental proton anchor; layer-pure; nothing wired.
Lean: [`QOU/MassTheory/TransferFactorCommute.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TransferFactorCommute.lean)
— sorry-free, zero warnings, `#print axioms = [propext]` on all ten
declarations.

---

## 0. The two answers, in plain language

**Loose end 1 — helper vs proposition at A=3. Classification (a): the helper is
the defective side — but the disagreement is smaller than it looks, and the
reason is a theorem.**

`hecke_core_symbolic._ground_state_ordering` returns `pnp` for ³He;
`prop:ground-state-ordering` rule (iii) says sorted `ppn` wins for `A ≤ 3`.
Computing the proposition's **own** objective `Φ_q = Σᵢ log|V̂ᵢ|` over every
arrangement:

- On the **bare nucleon chain**, `ppn` and `pnp` are **exactly degenerate**
  (both `−0.878523297318204006`). This is not a numerical coincidence — it is
  proved: the transfer factors `T(d) = S + d·1` all **commute**, so the readout
  depends on the crossing coefficients only as a **multiset**, and the two
  arrangements present the same multiset. Rule (iii)'s *"sorted **beats**
  interleaving"* is therefore a **tie** at ³He, not a strict win.
- On the **production** `Φ₁` (nucleons + the `Z`-electron tail, as
  `compute_phi1_full_sym` builds it), sorted `ppn` is the **unique** argmin
  (`−2.3752`) and the helper's `pnp` ranks **last of three** (`−1.7173`).

So both readings put sorted at the optimum and **neither supports the helper's
`pnp`**. The helper is the defective side — and not only at ³He: it performs
**no variational search at all** (it is a fixed interleaving generator,
identical to `_alternating_ordering_sym`), and across an exhaustive sweep it is
the `Φ₁` argmin in only **5 of 16** cases. It does not implement the rule its
own name invokes.

**Not fixed.** A fix leaves the Wedderburn volumes `V̂` untouched (they are
provably ordering-independent) but moves the **Hecke normal-form vector** by up
to **2.5×**, and `build_atom_nf_sym` / `build_atom_nf_mp` feed committed
witnesses. That crosses the scope bar. Filed, not applied.

**Loose end 2 — the missing ³He / ⁴He rows. Classification: generator bug, not
a deliberate exclusion.**

[`mass_table_comprehensive.py:153`](../../computations/mass_table_comprehensive.py):

```python
if a > 4:  # Avoid duplicates with explicitly added H, He isotopes
```

The premise is **false**. The explicit list is
`ISOTOPES = [("p", 1, 0), ("n", 0, 1), ("D", 1, 1), ("T", 1, 2)]` — H-chain
only, every entry `Z ≤ 1`. No He isotope was ever added, and the grid the guard
filters starts at `z = 2`, so **nothing in it can duplicate anything**. The
guard deletes **6 unique `(Z, N)` rows** for no reason; ³He and ⁴He are the only
bound nuclides among them.

---

## 1. Loose end 1 — what the objective actually says

### 1.1 The helper is a generator, not a search

Source, verbatim ([`hecke_core_symbolic.py:236`](../../computations/substrate/hecke_core_symbolic.py)):

```python
def _ground_state_ordering(Z: int, N: int) -> list[str]:
    """Match hecke_core.build_atom_nf — interleaved p/n ordering."""
    A = Z + N
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append("p"); pc += 1
        else:
            ordering.append("n"); nc += 1
    return ordering
```

No `Φ`, no `min`, no permutation enumeration. It is a **fixed interleaving
generator**, and it is bit-for-bit identical to `_alternating_ordering_sym` on
`0 ≤ Z, N ≤ 6` — so `compute_phi1_full_sym`, which calls the latter, evaluates
`Φ₁` **at** this arrangement rather than minimising over arrangements. The
docstring is honest about this (*"interleaved p/n ordering"*); the **name** is
not, because the corpus defines *ground state* as the `Φ_q` minimiser.

### 1.2 The proposition's display formula does not even apply at ³He

`prop:ground-state-ordering` is stated *"for a nucleus with `Z` protons and `N`
neutrons (`A = Z + N`, **`Z ≤ N`**)"*. ³He has `Z = 2 > N = 1`. Applying the
display formula anyway (`ordering[k] = p` iff `k` odd and `k < 2Z`) yields
`npn` — **one** proton where two are required. Measured for four `Z > N` cases:

| `(Z, N)` | display formula | protons placed | required |
|---|---|---:|---:|
| (2, 1) | `npn` | 1 | 2 |
| (3, 1) | `npnp` | 2 | 3 |
| (3, 2) | `npnpn` | 2 | 3 |
| (4, 1) | `npnpn` | 2 | 4 |

So the clause governing ³He is **rule (iii)** (*"for small `A` (`A ≤ 3`), the
sorted ordering (all protons first) beats interleaving"*), which is exactly the
clause the loose end named.

### 1.3 `Φ_q` over every arrangement, at the experimental proton anchor

`q₀ = 1.109978582751380807591669…`. Objective computed through the corpus
implementation `_phi1_from_ordering_sym` (symbolic `q`, anchor substituted only
at the `|V̂|` step). `Φ_nuc` is the bare nucleon chain; `Φ₁` appends the
`Z`-electron tail, as production does.

**³He `(Z, N) = (2, 1)`**

| ordering | `Φ_nuc` | `Φ₁` (production) | |
|---|---:|---:|---|
| `ppn` | **−0.878523297318204006** | **−2.37519810839658325** | sorted — argmin of both |
| `npp` | −0.683640148253447213 | −1.98321927125222633 | |
| `pnp` | **−0.878523297318204006** | −1.71732004705805955 | ← the helper; **last of 3** under `Φ₁` |

`Φ_nuc(ppn) = Φ_nuc(pnp)` to the full 50-dps floor — see §3 for why this is
exact and provable. Under `Φ₁` the separation is **0.657878**.

**T `(Z, N) = (1, 2)` — no dispute**

| ordering | `Φ_nuc` | `Φ₁` |
|---|---:|---:|
| `pnn` | **−1.22611079535300044** | **−2.46308887937445802** |
| `nnp` | −0.960211571158833655 | −2.19718965518029123 |
| `npn` | −0.960211571158833655 | −0.0616214763913148245 |

Here sorted `pnn` **is** the strict argmin under both readings, the helper
returns `pnn` too, and rule (iii) holds as stated. T is the only mixed-species
`A = 3` case satisfying the proposition's own `Z ≤ N` hypothesis — so *within
its stated scope*, rule (iii) is **correct and strict**.

### 1.4 The helper is not a `Φ_q` minimiser anywhere systematic

Exhaustive sweep, all arrangements, `Φ₁`:

| `Z` | `N` | #arr | helper | argmin(`Φ₁`) | helper optimal? | helper rank | gap |
|---:|---:|---:|---|---|---|---:|---:|
| 1 | 1 | 2 | `pn` | `np` | no | 2 | 2.136 |
| 1 | 2 | 3 | `pnn` | `pnn` | **yes** | 1 | 0 |
| 2 | 1 | 3 | `pnp` | `ppn` | no | 3 | 0.658 |
| 2 | 2 | 6 | `pnpn` | `pnpn` | **yes** | 1 | 0 |
| 2 | 3 | 10 | `pnpnn` | `pnnpn` | no | 2 | 0.392 |
| 3 | 2 | 10 | `pnpnp` | `pnpnp` | **yes** | 1 | 0 |
| 3 | 3 | 20 | `pnpnpn` | `npnpnp` | no | **20 / 20** | 8.809 |
| 3 | 4 | 35 | `pnpnpnn` | `pnpnpnn` | **yes** | 1 | 0 |
| 4 | 3 | 35 | `pnpnpnp` | `ppnpnpn` | no | 31 | 6.170 |
| 4 | 4 | 70 | `pnpnpnpn` | `nppnpnpn` | no | 7 | 1.086 |
| 4 | 5 | 126 | `pnpnpnpnn` | `pnpnnpnpn` | no | 30 | 5.512 |
| 5 | 5 | 252 | `pnpnpnpnpn` | `npnpnpnpnp` | no | **252 / 252** | 25.374 |
| 5 | 6 | 462 | `pnpnpnpnpnn` | `pnpnpnpnpnn` | **yes** | 1 | 0 |
| 6 | 6 | 924 | `pnpnpnpnpnpn` | `npnpnnpnpnpp` | no | 374 | 6.183 |
| 6 | 7 | 1716 | `pnpnpnpnpnpnn` | `nnpnpnnpnpnpp` | no | 726 | 6.183 |
| 7 | 7 | 3432 | `pnpnpnpnpnpnpn` | `npnpnpnpnpnpnp` | no | **3432 / 3432** | 31.942 |

**5 / 16.** At three `Z = N` cases the helper is the strict **worst** of every
arrangement. Under the bare-nucleon `Φ_nuc` it does better (**10 / 16**) but is
still not universal.

### 1.5 Candidate (c) — "they optimise different objectives" — tested and rejected

The honest alternative was that the helper minimises *something else*, making
the disagreement definitional. Measured across the same sweep:

| objective | helper optimal |
|---|---:|
| `Φ₁` (production: nucleons + electrons) | 5 / 16 |
| `Φ_nuc` (bare nucleon chain) | 10 / 16 |
| `−Φ₁` (i.e. the *maximiser*) | 5 / 16 |
| `|Φ₁|` (magnitude) | 5 / 16 |

**None of the four** is extremised by the helper across the sweep — neither of
the two the corpus actually names (`Φ₁`, `Φ_nuc`) nor either sign/magnitude
variant. So on the objectives available to test, the disagreement is **not**
definitional. Scope note: this is a negative over four functionals, not a proof
that no functional exists that the helper extremises; the positive statement it
supports is the one in §1.1 — the helper optimises nothing *by construction*,
because it never evaluates anything.

---

## 2. Loose end 1, continued — what a fix would move (measured, not applied)

Three separate consumers, three different answers. Numeric mirrors certified
against the corpus symbolic path (worst `|Δ|` = `8.9e−56` on the atom chain,
`8.5e−55` over 64 `Φ` chains).

**2a. Wedderburn per-generator volumes `V̂₀`, `V̂₁` (`atom_V_full_sym`) — do NOT
move.**

| `(Z, N)` | helper | candidate | rel Δ `V̂₀` | rel Δ `V̂₁` |
|---|---|---|---:|---:|
| (2, 1) | `pnp` | `ppn` | `1.4e−61` | `0.0` |
| (2, 2) | `pnpn` | `nppn` | `0.0` | `0.0` |
| (3, 3) | `pnpnpn` | `npnppn` | `0.0` | `0.0` |

Exactly invariant, and **structurally so**: `_vertex_channels_sym` runs the same
commuting `T(d) = S + d·1` recursion (§3), and `atom_gen_chains_sym` enumerates
**all** `C(A,2)` nucleon pairs — whose type multiset is fixed by `(Z, N)` alone.
Multiset in, multiset out.

**2b. Hecke normal-form vector (`build_atom_nf_sym` / `build_atom_nf_mp`) — DOES
move, a lot.**

| `(Z, N)` | helper | candidate | worst rel Δ on the 6-vector |
|---|---|---|---:|
| (2, 1) | `pnp` | `ppn` | **0.0486** |
| (2, 2) | `pnpn` | `nppn` | **2.516** |
| (3, 3) | `pnpnpn` | `npnppn` | **0.796** |

`hm_sym` is the 6-dimensional Hecke NF multiplication and is **not** of the
commuting `T(d)` form, so the NF is genuinely order-sensitive.

**2c. `Φ₁` itself — moves** (that is the whole of §1.3).

**Verdict: do not fix here.** The blast radius runs through
`build_atom_nf_sym` → `crystal_shift_nf_atomic.py`, `compound_shift_nf.py`,
`atomic_tr_m_mpfr_50dps.py`, and through `compound_shift_nf.build_atom_nf_mp`
(an independent transcription of the same helper, line ~197). Changing the
helper changes committed witness values. Filed as a bean; **not applied**.

---

## 3. Why the ³He degeneracy is exact — the Lean

[`QOU/MassTheory/TransferFactorCommute.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TransferFactorCommute.lean)
— `scripts/lean-verify.sh` **exit 0, zero warnings**; `#print axioms` on all ten
declarations gives `[propext]`. No `sorryAx`, no `axiom`, no `native_decide`, no
`: True`, no tautological conclusion. §7c-clean: generic `{R} [CommRing R]`
throughout, no `ℝ`.

`_phi1_from_ordering_sym`'s inner loop sets
`t00, t01, t10, t11 = h + d, 1, 1, d`, i.e. multiplies by

$$T(d) \;=\; \begin{pmatrix} h + d & 1 \\ 1 & d\end{pmatrix} \;=\; S + d\cdot\mathbf{1}, \qquad S = \begin{pmatrix} h & 1 \\ 1 & 0\end{pmatrix}.$$

Every factor of a chain is the **same** `S` plus a scalar. Hence:

| Declaration | Statement |
|---|---|
| `M2.mulNotComm` | the `2 × 2` carrier is genuinely **non-commutative** (guards the next line against vacuity) |
| `transferFactor_eq_skeleton_add` | `T(d) = S + d·1` componentwise |
| **`transferFactor_comm`** | any two transfer factors of a chain **commute** |
| **`chainProd_perm`** | hence the chain product depends on the crossing coefficients **only as a multiset** |
| `phiReadout_transferFactor` | the readout `V̂ = z·M₁₀ + M₁₁` is not a constant of the state (non-vacuity) |
| **`phiReadout_chainProd_perm`** | so the per-strand `Φ_q` datum is a function of the **suffix multiset** alone |
| **`he3_ppn_pnp_readout_eq`** | the ³He instance: `[a, b]` and `[b, a]` give equal readouts |

At ³He, strand 0 is a proton in both `ppn` and `pnp`; the later strands
contribute `{d(p,p), d(p,n)} = {0, −h/2}` in one order or the other, and strand 1
sees the single coefficient `−h/2` in both. Identical multisets ⇒ identical `V̂`
⇒ **`Φ_nuc(ppn) = Φ_nuc(pnp)` exactly.**

> **`sorry-free ≠ derived`.** The Lean proves the *shape* of the chain. It
> derives no binding energy, no `Δ_λ`, no ordering, and compares nothing to
> AME/CODATA. It does **not** prove `prop:ground-state-ordering`, which remains
> `def … : Prop` with no discharging instance.

### 3.1 Where the production separation actually comes from

`_crossing_coeff_sym` defines `(p, e) ↦ −h` but has **no `(n, e)` case** — it
returns `None`, and `_phi1_from_ordering_sym` **skips** an undefined
coefficient. So a neutron placed before the electron tail contributes a bare
`V̂ = 1` (i.e. `log 0`) for that strand.

The strict ³He separation under the production `Φ₁` is generated **entirely** by
this asymmetry — electrons couple to protons, not to neutrons — and not by the
nucleon ordering as such. That is a defensible physical modelling choice (a
neutron is neutral), but it means the `Φ₁`-level statement *"sorted strictly
beats interleaving at ³He"* is a statement about the **electron term**. Anyone
citing it should say so.

It also explains the deuteron reading: `Φ_nuc(pn) = Φ_nuc(np)` (tie, as the Lean
predicts) while `Φ₁(np) = −2.166` and `Φ₁(pn) = −0.031`. Note this is a
**further way** `Φ_q` and `ln τ_M` differ: #4850 proved the deuteron is *exactly*
ordering-independent under the closed-form Markov trace, and it is not under
`Φ₁`.

---

## 4. Corrections to the predecessor audit's §2 / §3.4 table

#4851 lists three live realisations of the interleaved corpus rule. Two of the
three do not hold up:

| #4851 claim | measured state |
|---|---|
| *"Rust `HeckeEngine.ground_state_ordering`"* | **No such function exists.** `grep` over `tools/hecke-engine/src/` finds no `ground_state` symbol. `ordering_cache._compute_ordering_rust` imports `hecke_rust_bridge.compute_nucleus`, which is absent from the live tree (only `fsh-guts/deprecated/computations/` has a `compute_nucleus`). The Rust path returns `None` unconditionally. |
| *"`ordering_cache.get_ordering`"* realises the interleaved rule | Only for the **270** `(Z, N)` already in `ordering-cache.json`. For anything else the fallback is `_compute_ordering_python` = `[1]*Z + [0]*N` — i.e. **sorted**, the *production* convention, not the interleaved one. |
| the cache realises the proposition's formula | **It does not.** `(2,2) → nppn` (formula: `npnp`); `(3,3) → npnppn` (formula: `npnpnp`); `(6,6) → npnpnpnpnppn` (formula: `npnpnpnpnpnp`). The cache consistently differs from the formula by **swapping the final two strands** — consistent with `Φ` skipping the last strand's own term. And the cache is the `Φ₁` argmin in only **5 / 12** of the swept cases where an entry exists. |
| `hecke_core_symbolic._ground_state_ordering` | correct as cited — but see §1.1: it is a generator, not a minimiser, and its `(2,1)` value is the item at issue. |

So the situation is **worse than "two live conventions"**: there are four
mutually inconsistent artefacts — production's sorted hardcode, the helper's
interleaving, the proposition's closed formula, and the committed cache — and
**none** of them is the `Φ₁` argmin in general. The `(2,1)` cache entry `ppn`
happens to be the one artefact that agrees with both rule (iii) and the measured
argmin.

---

## 5. Loose end 2 — the missing ³He / ⁴He rows

### 5.1 The generator

[`mass_table_comprehensive.py:146-155`](../../computations/mass_table_comprehensive.py):

```python
ISOTOPES = [("p", 1, 0), ("n", 0, 1), ("D", 1, 1), ("T", 1, 2)]
for z in range(2, 119):
    n_min = max(0, int(0.5 * z) - 2)
    n_max = int(2.5 * z) + 5
    for n in range(n_min, n_max + 1):
        a = z + n
        if a > 4:  # Avoid duplicates with explicitly added H, He isotopes
            sym = f"{a}{ELEMENTS[z]}"
            ISOTOPES.append((sym, z, n))
```

Reproduced exactly: the grid holds **14 974** `(Z, N)`; the guard keeps
**14 968** and drops **6**.

| dropped `(Z, N)` | nuclide | bound? |
|---|---|---|
| (2, 0) | ²He (diproton) | no |
| **(2, 1)** | **³He** | **yes** |
| **(2, 2)** | **⁴He** | **yes** |
| (3, 0) | ³Li | no |
| (3, 1) | ⁴Li | no |
| (4, 0) | ⁴Be | no |

### 5.2 The premise is false — this is a bug, not an exclusion

The comment says *"Avoid duplicates with explicitly added H, **He** isotopes"*.
The explicit list contains **no He isotope** — only `p`, `n`, `D`, `T`, whose
`Z` values are `{0, 1}`. The filtered loop starts at `z = 2`. **Intersection:
empty.** Measured: `dropped rows that are actually duplicates of an explicit
entry: NONE`.

Both the list and the guard appear in the file's first commit in history
(`c912f7fd94`) and neither has been touched since, so this is not drift — the
guard was written for a list that never existed. Correcting it means either
dropping the guard for the `z ≥ 2` loop or deduplicating by name instead of
by `A`.

Grep found **no documented reason** to exclude ³He/⁴He from this table anywhere
in `content/`, `computations/`, `docs/audits/`, or `docs/coordination/`, and no
alternative key under which the rows are emitted. The committed witness contains
zero occurrences of `3He` or `4He` — and one of `5He`.

### 5.3 Decisive: the module provisions ³He and ⁴He and then never emits them

This is what settles *deliberate exclusion* versus *bug*. The same file supplies
reference data for both nuclides in **three** separate dicts, all of which the
row loop consumes:

| line | provisioned | consumed at |
|---:|---|---|
| 83 | `AME_BINDING["3He"] = 7.71804` | 441 `AME_BINDING.get(name, 0.0)` |
| 84 | `AME_BINDING["4He"] = 28.2957` | 441 |
| 112 | `CODATA_MASS["3He"] = None  # not in codata_constants; derive from AME` | 444 `CODATA_MASS.get(name)` |
| 113 | `CODATA_MASS["4He"] = float(M_HE4_MEV_VALIDATION)` | 444 |
| 122-123 | `ATLAS_TAG["3He"] / ["4He"] = "principled-derivation (Q-CLT proxy)"` | 471 `ATLAS_TAG[name]` |

Every one of those lookups is keyed on `name`, which — because of the guard —
can never be `"3He"` or `"4He"`. In particular `M_HE4_MEV_VALIDATION` is
imported at line 65 **solely** to populate `CODATA_MASS["4He"]` and is therefore
**dead**, and the `CODATA_MASS["3He"]` comment (*"derive from AME"*) describes a
derivation the table never performs.

An author excluding these two on purpose would not have written their AME
binding energies, their atlas methodology tags, and a dedicated CODATA import
for them. **The exclusion is unintended.**

### 5.4 The collateral: a witness assertion that passes because of the bug

`mass-table-comprehensive.witness.json` carries **exactly one** assertion:

```python
builder.add_assertion(
    name="all_A_leq_4_masses_computed",
    computed=float(all(r["m_approx_MeV"] is not None for r in rows if r["A"] <= 4)),
    expected=1.0, tolerance=0.0,
    source="All A ≤ 4 isotopes have absolute mass predictions",
)
```

It ranges over `[r for r in rows if r["A"] <= 4]`, which **after** the filter is
exactly `{p, n, D, T}`. The assertion cannot see ³He or ⁴He, so it passes while
the two most important `A ≤ 4` nuclides are absent. **The assertion is true of
the emitted rows and false of its own wording** — its coverage claim is
guaranteed by the very filter that voids it.

Not regenerated here: re-running the producer changes published numbers.

---

## 6. Scope classification

Per AGENTS.md §"Before declaring refuted / ruled out / dead end".

**scope-(a) throughout. No scope-(b) exclusion is claimed anywhere in this
audit.**

- **(a⁺) settled.** Loose end 2 is settled outright: the guard, its false
  premise, the exact 6-row drop set, and the vacuous assertion are all read
  directly from source and reproduced mechanically.
- **(a⁺) settled.** Loose end 1's *classification* is settled: the helper runs
  no search (read from source, §1.1), is the `Φ₁` argmin in 5/16 cases, and
  returns the strictly-worst arrangement at ³He under the production objective.
  The candidate-(c) rejection is weaker in kind — a negative over **four**
  functionals (§1.5), not over all conceivable ones. It does not need to be
  stronger: a routine that evaluates nothing extremises nothing by
  construction.
- **(a⁻) not determined.** Which arrangement production *should* use is **not**
  determined here and no ordering is recommended. `prop:ground-state-ordering`
  remains **stated, not proved**; its `A > 14` rule remains an extrapolation;
  the `Φ_q`-vs-`ln τ_M` reconciliation (#4851 §8 item 1) is untouched.
- The `Φ₁` sweep is finite (`A ≤ 14`) and at one anchor. Nothing is excluded
  structurally, so no ingredient is ruled out.

**What is NOT claimed:**

- **Not** that `prop:ground-state-ordering` is *proved*. §1.3 shows rule (iii)'s
  conclusion holds at both `A = 3` mixed cases; §3 shows its *strictness* fails
  at ³He on the nucleon chain. The proposition as a whole is untested here.
- **Not** that the helper should be changed *now*, and **not** that the mass
  table should be regenerated *now*. Both would move published numbers.
- **Not** that any `m_p` / `m_n` / `m_μ` / `Q_β` / `Δ_pn` / `m_K/m_π` number
  moves. None does. The L2 count stays **2/7**.
- **Not** that AME/CODATA selected anything. No experimental quantity appears in
  any selection step of this audit.

---

## 7. Discipline record

- `free_parameters = 0`. No AME/CODATA quantity enters any comparison; the two
  bound nuclides in §5.1 are labelled from physics, not used as a selector.
- q₀ = **experimental proton anchor** (`q_parameter.q_at`; owner directive
  2026-08-07). Layer-pure — no muon-built cache is read anywhere in the probe,
  and in particular `wedderburn_jones_markov.y_lambda_at` is never called.
- Arithmetic: mpmath 50 dps. The fast mirrors are **certified against the corpus
  symbolic implementations** before use (worst `|Δ|` = `8.5e−55` over 64 `Φ`
  chains; `8.9e−56` on the atom chain) — the measured effects exceed that floor
  by ~50 orders.
- Lean sorry-free, zero warnings, `#print axioms = [propext]` on all ten
  declarations; registered in the `QOU` umbrella.
- Run cost ≈ 12 min single process, dominated by the symbolic `_phi1_from_
  ordering_sym` reference used for the `A = 3` tables and the mirror
  certification.
- **No published number changed.** No production file was modified: the only
  changes are a new probe, a new Lean file, its umbrella registration, this
  audit, and a witness.
- Bean `qou-48is` stays **OPEN**; `qou-prjo` untouched.

---

## 8. What would close these

1. **Rename or fix the helper.** Either make `_ground_state_ordering` actually
   minimise `Φ₁` (a suffix-multiset DP — cheap, given `chainProd_perm`), or
   rename it to `_interleaved_ordering` so it stops claiming a variational
   status it does not have. The first option moves committed witnesses (§2) and
   needs owner sign-off; the second is free and honest.
2. **Decide whether `Φ₁` or `Φ_nuc` is the ordering objective**, and close the
   `(n, e)` hole in `_crossing_coeff_sym` deliberately (define it, or document
   that skipping it is the physical statement "electrons do not couple to
   neutrons"). At ³He the whole strict/tie question turns on this.
3. **Fix the `a > 4` guard** and regenerate the mass table, restoring the ³He and
   ⁴He rows — and **restate** `all_A_leq_4_masses_computed` so its wording
   matches its range.
4. **Correct #4851 §2/§3.4** for the three items in §4 above: the Rust
   ground-state search does not exist, `ordering_cache` falls back to *sorted*,
   and the committed cache matches neither the proposition's formula nor the
   `Φ₁` argmin.

### 8.1 Done here (small, in-theme, zero risk)

#4851's two Lean files — `QOU/MassTheory/CanonicalOrderingSaddle.lean` and
`QOU/MassTheory/NucleonOrderingSymmetry.lean` — were **never registered in the
`QOU` umbrella**, so nothing in the library imports them and no build would
notice if they broke. Both verify `lean`-direct **exit 0** on this branch, so
both are registered here alongside `TransferFactorCommute`. This changes no
number; it only puts three ordering-related proofs under the umbrella that is
supposed to cover them.
