# Implementation spec — fibre-level Composite 4 (Q_β c_3 residue A)

**For:** the next agent working in an environment with a **runnable
pyhecke** (numpy + `qou_substrate`/`q_parameter` shims) and ideally a
**warm Lean LSP**. This sandbox has neither, so the work below is
specified, not executed.

**Context (read first):**
- Scope + corrected effort estimate: [`2026-06-04-habiro-fibre-composite4-mtau-scope.md`](2026-06-04-habiro-fibre-composite4-mtau-scope.md)
- Reconnaissance result (self-contained probe): [`computations/qbeta/qbeta_composite4_fibre_root_of_unity_probe.py`](../../computations/qbeta/qbeta_composite4_fibre_root_of_unity_probe.py) (PR #1811)
- `/25` refutation: PR #1801 (`qbeta_rung1_div25_framing_squared_test.py`)
- AGENTS.md §"Im(q) at fibre vs observable", §"Q_β c_3 truncation order"

**Goal.** Decide whether the Q_β c_3 *residue A* (the correction beyond
the proved `c_2 = -1`) is the archimedean evaluation of a **Habiro-ring
element** — a knot invariant determined by its values at all roots of
unity — rather than a cal-anchored constant. Success = a single
fibre-level element whose τ-evaluation reproduces c_3 at **multiple q₀
anchors** (cross-anchor rigidity), which would promote c_3 from
NEAR-MATCH/cal-anchored toward derived. Failure = another bounded
NEGATIVE that further constrains the space. **Δ_λ-gate: no fitted
forms.** Report tiered (proved / near-match / fitted), never binary.

## Established facts the spec builds on

1. `nf_tr` (`tools/pyhecke/python/pyhecke/gram.py:107`) is
   `sum(nf[i]·TR_M[i])` — **already linear**. A linear-combination
   trace is a thin wrapper (Step 1), **not** new infra.
2. The archimedean route is dead: real-q₀ q-Pochhammer truncation is
   42/42 NEGATIVE (#1795), and the `/25` denominator does **not**
   q-deform (#1801). The reconnaissance probe (#1811) showed `/25` =
   `[5]_q²` at the **q=1 classical fibre point**, not any finite root
   of unity and not q₀.
3. Therefore the live object is **formal-q / roots-of-unity**, the
   fibre level — the part this spec builds the machinery for.

> **Sandbox-env note (2026-06-04):** pyhecke *is* runnable here after
> `uv pip install --system -e tools/qou-substrate -e tools/pyhecke`
> (numpy also needed). With that, **Step 1 below is now DONE on this
> branch** (PR #1811); Steps 2–5 remain.

## Step 1 — `markov_trace_combo` ✅ DONE (PR #1811)

Implemented in `gram.py` as `nf_of_word(word, *, exact)` +
`markov_trace_combo(terms, *, exact)`, with tests in
`tools/pyhecke/tests/test_markov_combo.py` (6 tests, all pass:
single-word agreement, basis→`TR_M`, linearity, Hecke relation via
trace, exact-ℚ NF reduction, exact-vs-float).

**Finding while implementing:** pyhecke's `exact=True` Fraction path is
*not* exact at the true substrate — it is exact arithmetic at a
**rational model** `q = 111/100`, `z = 4993/10000` (4-digit), so it
differs from the float path (true q₀ = 1.10998…) by ~1e-3. The float
path is the accurate one for trace *values*; the exact path is for
*structural* ℚ identities (NF reduction is genuinely exact there). This
matters for Step 4: a residue-A test needs the **float / high-precision
mpmath** path or a proper formal-q path (Step 2), not the 111/100 model.

### Original spec (kept for reference)

**File:** `tools/pyhecke/python/pyhecke/trace.py` (re-export) +
implementation alongside `nf_tr` in `gram.py`.

```python
def markov_trace_combo(terms, *, exact: bool = False):
    """Markov trace of a linear combination Σ cᵢ·σ_{wᵢ} in H_3(q).

    terms : iterable of (coeff, word) where word is a tuple of generator
            indices (0,1) for B_3 / H_3.
    Returns tr_M(Σ cᵢ σ_{wᵢ}) by linearity:
        reduce each word to its NF 6-vector, sum (weighted), apply nf_tr.
    exact=True uses the Fraction path (hm_exact / _TR_M_FRAC)."""
```

Implementation: for each `(c, word)`, build the NF vector by folding
`hm`/`hm_exact` from the identity NF over the word's generators, scale
by `c`, accumulate into a 6-vector, then `nf_tr` (or dot with
`_TR_M_FRAC`).

**Acceptance test** (`tools/pyhecke/tests/test_markov_combo.py`):
- Linearity: `markov_trace_combo([(2,(0,)),(3,(1,))]) == 2*nf_tr(NF((0,))) + 3*nf_tr(NF((1,)))`.
- Single-term agreement with the existing single-word trace.
- `exact=True` matches the float path to 1e-12.

## Step 2 — formal-q Markov trace ✅ DONE (PR #1811)

Implemented in `tools/pyhecke/python/pyhecke/trace_formal.py` (sympy,
lazy-imported so pyhecke stays sympy-free unless this module is used);
tests in `tools/pyhecke/tests/test_trace_formal.py` (6, all pass).

**Resolution of the z subtlety:** the coefficient ring is **ℚ(s)**
(rational functions in `s = q^½`), *not* Laurent polynomials —
`z = 1/(s+s⁻¹) = s/(s²+1)` (a test asserts this exactly). So `laurent_q.py`
is **not** the right carrier; sympy over `ℚ(s)` is. API:
`nf_of_word_formal`, `nf_tr_formal`, `markov_trace_combo_formal`,
`specialize(expr, s_value)`, and the Step-3 hook
`eval_at_root_of_unity(expr, N, k)` (q = exp(2πik/N) ⇒ s = exp(πik/N)).
Verified: specializing at `s = √q₀` reproduces the float
`markov_trace_combo` and every `gram.TR_M[i]`; the Hecke relation
`σ₀² = h·σ₀ + 1` holds symbolically; root-of-unity evaluation runs.

### Original spec (kept for reference)

**File:** new `tools/pyhecke/python/pyhecke/trace_formal.py`, built on
`laurent_q.py` (`LaurentQ`).

- Re-express the H_3(q) NF data as **Laurent polynomials in q** (not
  floats): the `hm` multiplication tables (coeffs `c·h + d` with
  `h = q - q⁻¹`) and the Markov weights
  `TR_M = [1, z, z, z², z², h·z²+z]`. **Caution:** `z = 1/(q^{1/2}+q^{-1/2})`
  is *not* a Laurent polynomial in q — work in the variable
  `s = q^{1/2}` (so `z = 1/(s+s⁻¹)`, a Laurent poly in `s` after
  clearing the denominator) or carry `z` as a symbolic atom. Decide
  this first; it is the main subtlety.
- `nf_tr_formal(nf) -> LaurentQ` and `markov_trace_combo_formal(terms)`.

**Acceptance:** specializing the formal trace at `q = q₀` (real)
reproduces the float `nf_tr` to 50 dps for the 6 basis elements and for
a random linear combination.

## Step 3 — roots-of-unity / Habiro evaluation ✅ DONE (PR #1811)

Implemented in `trace_formal.py` (3 new functions) with tests appended
to `tools/pyhecke/tests/test_trace_formal.py` (6 new, 12 total, all
pass). `eval_at_root_of_unity` already landed with Step 2; Step 3 adds
the *family* layer on top of it:

- `habiro_profile(expr, N_max, *, k=1, skip_degenerate=True)` — the
  family `{ζ_N ↦ expr(ζ_N)}` over `N = 1..N_max` as `(N, value)` pairs.
  **Degeneracy = pole, not zero**: an `N` is dropped only when `expr`
  has a *pole* at `ζ_N` (a denominator quantum integer `[n]_ζ → 0`;
  for the bare trace `z = s/(s²+1)` that is `N = 2k`). A finite *zero*
  (numerator `[n]_ζ`, e.g. `[5]` at `ζ_5`) is **kept** with value ≈ 0.
  `skip_degenerate=False` keeps poles as `(N, None)`.
- `classical_limit(expr)` — value at the trivial fibre point `q→1`
  (`s→1`, the `N→∞` archimedean shadow), via `sp.limit` so removable
  `0/0` resolves: `[n]_q → n`, hence `[5]₁² = 25` (a test asserts this,
  matching the `/25` of the c_3 rung).
- `quantum_int(n)` — balanced `[n]_q = (sⁿ−s⁻ⁿ)/(s−s⁻¹)`, provided so
  Step-4 callers can build/recognise the `[5]_q²` structure.

A test also pins the **#1811 lesson** directly: `[5]_q² = 25` holds at
`q→1` but **not** at `ζ_7` — a Habiro element is the *whole family*,
not a point. The machinery for Step 4 is now in place.

### Original spec (kept for reference)

**File:** extend `trace_formal.py` with
`eval_at_root_of_unity(laurent, N, k=1)` → evaluate at `ζ = exp(2πik/N)`
(complex, via mpmath `mpc`).

- A Habiro-ring element is **the family** `{value at ζ : ζ root of
  unity}`, *not* a single evaluation (the #1811 probe's key lesson).
  Provide `habiro_profile(element, N_max)` returning the vector of
  evaluations over `N = 1..N_max` (skipping degenerate `[n]_ζ = 0`).
- The archimedean shadow is recovered at the **trivial point q→1**
  (= N→∞), consistent with `/25 = [5]_1²`.

## Step 4 — the actual c_3 residue-A element (the hard math)

This is the genuinely open categorical step; Steps 1–3 are its
prerequisites.

> **Status update (2026-06-05) — attack-1 superseded; the residue-A
> derivation is OWNER-GATED, not a probe.** Three sibling results that
> landed/advanced after this spec was written close the remaining
> single-object routes and re-classify the open work:
>
> 1. **Finite roots of unity refuted** — PR #1821 (merged, c_3 complex-
>    singularity probe): the c_3 hypersensitivity `dc_3/dq ≈ 4.66×10⁶`
>    pins the nearest singularity at `b ≈ |c_3|/|dc_3/dq| ≈ 4.4×10⁻⁷`
>    from q₀, while the nearest root of unity (ζ₁ = 1) is `|q₀−1| ≈ 0.11`
>    — **~2.5×10⁵× farther**. So **no finite root of unity** can source
>    the c_3 structure. This generalises the Hopf-probe NEGATIVE on this
>    branch (only N=1 hit −2): **attack-1 below (Hopf cyclotomic element
>    at a finite root) is retired** — the governing object is the full
>    Habiro element at the **near-real singularity at q₀**, i.e. the
>    residue-A simple pole at `u_substrate` (PR #1713/#1727), which is
>    **anchor-independent**.
> 2. **Single-formula space saturated + formally accepted cal-anchored**
>    — [`2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md`](../audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md):
>    28 single-formula categorical candidates (+ n≤5 partitions +
>    Demazure(sl₃,₄,₅), [`2026-06-04-qbeta-chain4-n5-demazure-verdict.md`](../audits/2026-06-04-qbeta-chain4-n5-demazure-verdict.md))
>    all FAIL the 10 ppm gate. **Do not run a 7th single-formula ansatz.**
> 3. **Obstruction + invariant already formalized by siblings** — the
>    "narrow the probe" formalize-first deliverable is done: the
>    singularity bound (#1821) and the **bar-even §4(b) kernel invariant**
>    (`prop:q-beta-bar-even-kernel-invariant`, PR #1875, Lean + sympy)
>    gate any candidate kernel. The remaining **F(q) kernel construction
>    is owner-gated multi-session research** (refuted-class map §5),
>    composing with PR #1839's `CFinite.recurrence_step` engine.
>
> **Net:** the productive open axis is **trace-level Markov stabilization**
> `Ind_{H₃}^{H₄}` under `tr_M` (PR #1846/#1808), which *reuses* this
> branch's Steps 1–3 machinery (`trace_formal.py` / `markov_trace_combo`)
> and the **trace cyclicity** added to the Step-5 Lean module here (5b).
> No new single-object probe is warranted from this branch.

### Knot-assignment verification ✅ DONE (2026-06-04) — cinquefoil REFUTED for c_3

The spec's own guardrail ("verify the knot the Q_β c_3 rung corresponds
to … do not assume the cinquefoil") has been executed (corpus sweep,
this branch). **Verdict: c_3 is NOT the cinquefoil.** Attack-1 below as
originally written chases the wrong knot and is retired.

| question | verdict | source |
|----------|---------|--------|
| c_3 ← cinquefoil T(2,5)? | **NO** | [`docs/audits/2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`](../audits/2026-06-03-l2-closure-habiro-3-q-25-universal-template.md) — "NOT yet derived for Q_β" |
| c_3 ← any single knot? | **NO — open** | [`docs/audits/2026-05-19-qbeta-ladder-knot-operator-general-statement.md`](../audits/2026-05-19-qbeta-ladder-knot-operator-general-statement.md) — knot-operator `T_β` unidentified |
| structural source of c_3? | **Hopf link** (2-strand sub-braid windings) | [`q-beta-c3-hopf-three-fold-markov.md`](../../content/quantum-observable-universe/mass-theory/q-beta-c3-hopf-three-fold-markov.md) — `c_3 = J_Hopf(q=1) = -2`, proven categorically (Facts 1–4) |
| is `/25` a knot assignment? | **NO — fibre constant** `[5]_q²│_{q=1}` | [`qbeta_composite4_fibre_root_of_unity_probe.py`](../../computations/qbeta/qbeta_composite4_fibre_root_of_unity_probe.py) (#1811) |
| is the real-q `[3]_q/25` form derived? | **NO — FALSIFIED** | [`docs/audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](../audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md) — rigid; swings **4.7M× less** than empirical c_3 |

T(2,5) is the **muon** particle-knot (`lepton_t2n_torus_tower.py:6`;
census `docs/audits/2026-06-01-knot-operator-census-group-actions.md`),
not the c_3 coefficient — the shared `/25` is a coincident fibre
constant, not a shared knot. And the real-q single-knot route is
**closed**: a smooth real-q `f(q)` cannot track `dc_3/dq ≈ 4.6×10⁶`
(falsification audit), so the live object is necessarily **fibre /
root-of-unity** (AGENTS.md §"Im(q) at fibre vs observable" — the c_k
live in the fibre, potentially complex).

### Corrected attacks (priority order)

1. **Hopf-link Habiro element at the fibre level.** The proven anchor
   is `c_3 = J_Hopf(q=1) = -2`; the open question is whether the
   *residue A* (the correction beyond `c_2=-1`) is the τ-evaluation of
   a **complex-analytic root-of-unity Habiro element on the Hopf
   substructure**. Build the Hopf link's cyclotomic / colored-Jones
   expansion and compare its **`habiro_profile`** (Step 3) — the whole
   root-of-unity *family* — to empirical c_3, NOT a single real-q point
   (#1811 + the falsification audit closed that). Hard constraint:
   `classical_limit` of the element must return **−2**. ❌ Do NOT
   reintroduce the cinquefoil / a q-deformed `/[5]_q²` denominator.
2. **(retired)** Cyclotomic expansion of the cinquefoil T(2,5) colored
   Jones — *wrong knot for c_3* (verification table above). Recorded
   only as the refuted route; do not rebuild it.
3. **Unreduced 5-strand Markov normalisation** (surviving #1801
   candidate (c)) — a narrower *q=1 fibre* question: where does the
   bare `25` come from (`tr_M(p_5)` normalisation at q=1, via Step 1's
   `markov_trace_combo` on `p_5`; needs H_n for n=5, beyond `gram.py`'s
   H_3 — extend the NF basis or use `pyhecke.tower`). Lower priority:
   even a clean `/25 = 25` at q=1 does **not** make c_3 derived — the
   cross-anchor *swing* is the obstruction, and it is fibre-level.

**First probe landed (this branch).**
[`qbeta_c3_hopf_habiro_profile_probe.py`](../../computations/qbeta/qbeta_c3_hopf_habiro_profile_probe.py)
wires the Step-3 machinery to the Hopf object: `classical_limit` recovers
the proven `-2` (both framings); the symbolic identity
`J_bal = -[2]_q = -quantum_int(4)/quantum_int(2)` holds;
`habiro_profile(J_bal)` is real and pole-free with **only N=1 (= q=1)
returning -2** (the #1811 lesson on the Hopf object); and the bare real-q
Hopf framing is **rigid** across the proton/muon anchors (swings 2.5×10⁷×
less than empirical c_3). NEGATIVE / bounding — residue A confirmed
fibre-level; the open object is a non-trivial **cyclotomic
(colored-Jones)** element, attack-1's next concrete target.

**Acceptance for "derived" (strict):** the chosen element reproduces
c_3 to ≤ its current near-match (≤ 2.65 ppm) at **≥ 3 distinct q₀
anchors** (proton, and two others from `qbeta-c3-habiro-3rung-crossanchor-rigidity`)
with **no per-anchor refit** — i.e. one formal element, evaluated.
Anything that needs a per-anchor constant is a **fitted** result and is
caught by the three-calibration discipline review; record it as
NEGATIVE and extend the bracket count instead.

## Step 5 — Lean side ✅ DONE — module builds GREEN (verified this branch)

The concrete n=3 Markov-trace functional is **written, committed, and
verified** in
[`MarkovTraceOnHecke.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceOnHecke.lean):
NF free module `Fin 6 → R`, `TRM`/`trM`/`mulσ₀`/`mulσ₁`, with linearity
(`trM_add`/`trM_smul`), the Hecke operator identity (`mulσ₀_hecke`:
`σ₀²=hσ₀+1`), the Markov reduction (`trM_markov_σ₁`: `tr(x·σ₁)=z·tr(x)`
on H₂), and the `markovTrace_realized` bundle. The data mirror `gram.py`
(`hm`, `TR_M`) and `pyhecke.trace_formal`; the mathematics is
additionally cross-verified in Python (randomized vs `gram.py`, symbolic
over ℚ(s) by `test_trace_formal.py`).

**Build:** `lake build QOU.Machinery.MarkovTraceOnHecke` → *"Build
completed successfully (922 jobs)"*, exit 0, **sorry-free**. The sandbox
toolchain block was overcome via the lean-environment-setup.md §"web
sandbox addendum" fix: install Lean v4.24.0 from the **allowlisted GitHub
release asset** (`release.lean-lang.org` and the cache host are
firewalled), then build the ~650-module mathlib subset from source (the
cache is 403-blocked). The companion design doc
[`2026-06-04-step5-markov-trace-h3-concrete-lean.md`](2026-06-04-step5-markov-trace-h3-concrete-lean.md)
records the cross-verification + the toolchain recipe.

**Step 5b — wiring + cyclicity VERIFIED GREEN (2026-06-05):**

- ✅ **Build-verified on a fresh container** — `lake build
  QOU.Machinery.MarkovTraceOnHecke` → *"Build completed successfully
  (922 jobs)"*, exit 0, **sorry-free**, **warning-free**. Toolchain
  v4.24.0 installed from the GitHub release asset; cyclicity's
  `simp only … ; ring` closes as the ℚ(z,h) preflight predicted
  (`ring 617ms`). The earlier "progress" status was pushed *unverified*
  (the Lean env had not finished restoring at the time); this build
  confirms both the cyclicity proof and that the `QOU.lean` wiring does
  not redden the `lake build QOU` graph.
- ✅ **Wired into `QOU.lean`** — `import QOU.Machinery.MarkovTraceOnHecke`
  added to the library root, so the module now sits in CI's `lake build
  QOU` graph (was an orphan, like the other `Machinery/*.lean`).
- ✅ **Trace cyclicity `tr_M(u·v) = tr_M(v·u)` added** (`trM_cyclic`),
  built on the full H₃ algebra product `mulNF` (right-multiplication
  composed along basis words `R_{ab}=R_b∘R_a`). The cyclicity identity
  and the `mulNF` composition order were pinned by a symbolic preflight
  over `ℚ(z,h)` (all 36 basis pairs + the full bilinear statement) before
  formalizing. This is exactly the trace symmetry the `Ind_{H₃}^{H₄}`
  Markov-stabilization axis (PR #1846) relies on.
- ⏳ **`markov_trace_origin` discharge** — still gated on Step 4 naming
  the residue-A element, which is **owner-gated** (see the Step 4 status
  update above); not actionable from this branch without an owner
  decision on the F(q) kernel direction.

**File:** `content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceOnHecke.lean`.

- Replace the `True`-marker `MarkovTrace` class field with a real
  structure: a linear functional on the H_n(q) free module satisfying
  the Markov property `tr(x·σ_n) = z·tr(x)` and trace cyclicity. Start
  at n=3 (mirror `gram.py`'s NF basis + `TR_M`), prove linearity and
  the σ-recursion as lemmas.
- Then the `UniversalHabiroStructure.markov_trace_origin` field
  (currently `True`, in `MmuR9V9Closure.lean`) can be discharged for
  the specific element Step 4 produces — turning the conditional
  closure theorem into an unconditional one for that element.
- Build with the root workspace: `lake build QOU`. If the sandbox
  blocks `lake` (see the web-sandbox addendum in
  `lean-environment-setup.md`), iterate against the LSP only and say so.

## Non-goals / guardrails

- **Do not** re-run archimedean real-q₀ denominator swaps — 42/42 + #1801
  + #1811 have closed that space.
- **Do not** introduce a q-deformed `/[5]_q²` (refuted) or a per-anchor
  fitted constant (Δ_λ-gate).
- **Cinquefoil assignment: VERIFIED REFUTED (2026-06-04)** — c_3's
  structural source is the **Hopf link**, not T(2,5) (which is the
  muon). See the Step 4 verification table. Do not rebuild the
  cinquefoil colored-Jones attack; build on the Hopf substructure at
  the fibre / root-of-unity level.
- m_τ / `[3]_q/49` (task ③) is **downstream** of a separate m_τ
  bare-mass baseline (Vol≈34 knot) and out of scope here.
