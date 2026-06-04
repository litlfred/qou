# Implementation spec — fibre-level Composite 4 (Q_β c_3 residue A)

**For:** the next agent working in an environment with a **runnable
pyhecke** (numpy + `qou_substrate`/`q_parameter` shims) and ideally a
**warm Lean LSP**. This sandbox has neither, so the work below is
specified, not executed.

**Context (read first):**
- Scope + corrected effort estimate: [`2026-06-04-habiro-fibre-composite4-mtau-scope.md`](2026-06-04-habiro-fibre-composite4-mtau-scope.md)
- Reconnaissance result (self-contained probe): [`folio-assistant/computations/qbeta/qbeta_composite4_fibre_root_of_unity_probe.py`](../../folio-assistant/computations/qbeta/qbeta_composite4_fibre_root_of_unity_probe.py) (PR #1811)
- `/25` refutation: PR #1801 (`qbeta_rung1_div25_framing_squared_test.py`)
- CLAUDE.md §"Im(q) at fibre vs observable", §"Q_β c_3 truncation order"

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

## Step 3 — roots-of-unity / Habiro evaluation

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
prerequisites. Two concrete attacks, in priority order:

1. **Cyclotomic (Habiro) expansion of the relevant knot's colored
   Jones.** For torus knots `T(2,2t+1)` the cyclotomic coefficients
   `C_n(q) ∈ ℤ[q]` are known in closed form (Habiro 2002; Masbaum
   2003, *Skein-theoretical derivation of some formulas of Habiro*).
   Build `J_K(q) = Σ_n C_n(q)·(q^{1+N};q)_n(q^{1-N};q)_n` for the knot
   the c_3 rung is assigned to (cinquefoil T(2,5) is the working
   hypothesis from the `/25`; **verify the assignment** against
   `lepton_t2n_torus_tower.py` and the Q_β knot, do not assume it).
   Test whether `C_n` / the Habiro coefficients reproduce the
   c_3 residue-A correction `ℏ_q·[3]_q/25 + ℏ_q³/[2]_q` — in
   particular whether the `/25` emerges as `C_n`'s `[5]`-structure at
   the q=1 evaluation.
2. **Unreduced 5-strand Markov normalisation** (the surviving #1801
   candidate (c)). Use Step 1's `markov_trace_combo` on the
   Jones–Wenzl projector `p_5` in the TL/Hecke tower (needs H_n for
   n=5, beyond the current H_3 `gram.py` — extend the NF basis, or use
   `pyhecke`'s tower module if present). Test whether `tr_M(p_5)` /
   its normalisation gives the undeformed `25` at q=1.

**Acceptance for "derived" (strict):** the chosen element reproduces
c_3 to ≤ its current near-match (≤ 2.65 ppm) at **≥ 3 distinct q₀
anchors** (proton, and two others from `qbeta-c3-habiro-3rung-crossanchor-rigidity`)
with **no per-anchor refit** — i.e. one formal element, evaluated.
Anything that needs a per-anchor constant is a **fitted** result and is
caught by the three-calibration discipline review; record it as
NEGATIVE and extend the bracket count instead.

## Step 5 — Lean side

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
- **Do not** assume the cinquefoil assignment — verify the knot the
  Q_β c_3 rung actually corresponds to before building its Habiro
  expansion.
- m_τ / `[3]_q/49` (task ③) is **downstream** of a separate m_τ
  bare-mass baseline (Vol≈34 knot) and out of scope here.
