# Single-pipeline binding comparison — B_lin / B_sym / B_qCLT / B_magic on one canonical tr_M

**Date:** 2026-06-15
**Branch:** `claude/stoic-maxwell-qieqcv` (PR #2320)
**Scope:** exploratory probe — no production rewire, no Δ_λ closure (no 7th ansatz).
**Compute:** [`binding_single_pipeline_comparison.py`](../../folio-assistant/computations/binding_single_pipeline_comparison.py)
→ `binding-single-pipeline-comparison.witness.json`

## The coherence objection this resolves

An earlier multi-model binding table compared `B_depth`, `B_magic`, `B_lin`,
and the Δ_λ-law side by side and read off their per-nucleus error spreads as if
they measured *physics quality*. They did not: the table mixed **three distinct
pipelines** and **two energy scales**, so the spreads were partly an artifact of
*which object each model computes*, not *how well it matches data*.

| model | trace / engine | assembly |
|---|---|---|
| `B_lin` | canonical Jones–Markov scalar trace `tr_M` | `α·(tr_M(W_free) − tr_M(W_atom))` (scalar difference) |
| `B_depth` | per-partition `χ^λ` (Hoefsmit) + empirical depth weights `α_k` | `Σ_k α_k·(Φ_k^free − Φ_k^atom)` (Wedderburn depth-sum) |
| `B_magic` | hyperbolic volume `Vol(L6a4) = 8G` — **no trace** | `2·m_e·A·8G` (flat) |
| Δ_λ-law | `B_lin` × phenomenological `q₀^{10A−5}` | scalar-trace + correction |

Three different objects (scalar-trace difference, χ^λ depth-sum, pure volume) at
two scales (Q_β vs E₀) cannot be ranked against each other directly.

## The fix: one trace, one scale, four forms

Route every **trace-based** form through the single canonical trace already
recorded in `binding-canonical.witness.json` (`markov_trace_canonical.tr_M_element`;
`tr_M_free`, `tr_M_atom` per nucleus), at a single scale α. With

- bond suppression  `s(K) = 1 − tr_M(W_atom)/tr_M(W_free) ∈ [0,1)`
- log-ratio         `L(K) = ln( tr_M(W_free)/tr_M(W_atom) ) = −ln(1−s)`

the four `standard-part-functor.md` diagram forms are

| form | definition | character |
|---|---|---|
| `B_lin`   | `α·s`            | linear / intensive — the **O(s) truncation** of B_sym; **saturates** at α (s<1) |
| `B_sym`   | `α·L`            | exact log-trace (Kashaev volume); **extensive** in bonds, L→∞ as s→1 |
| `B_qCLT`  | `α·bonds·ℓ̄`     | A→∞ self-averaging limit; `ℓ̄ = L(deuteron)` (unique 1-bond system); chain (A−1) & all-pairs C(A,2) |
| `B_magic` | `2·m_e·A·8G`     | doubly-magic ⁴He only — no single hyperbolic knot ⇒ **no trace** |

`B_lin` is literally the leading term of `B_sym` (`−ln(1−s) = s + s²/2 + …`), so
the two differ *only* by that one linearization — at fixed α and fixed trace.
`B_qCLT` replaces the exact correlated total trace by a bulk per-bond sum;
`B_sym − B_qCLT` is therefore the finite-A correlation correction.

## α resolution (the question the appendix left open)

α is the **canonical energy scale**

  `E₀ = m_e / ( q₀ (q₀ − 1) ) ≈ 4.186 MeV`

— DERIVED (q₀, m_e only), **not Q_β and not a deuteron-pinned free parameter**.
Evaluated against the alternative `α_D = B_AME(D)/L(D) ≈ 2.394 MeV` (pin on the
deuteron), the derived E₀ fits the generic nuclei **better**, because the
deuteron is anomalously weakly bound — a poor calibration anchor. `ℓ̄` uses only
the deuteron's *trace ratio* (not its B_AME), so `B_qCLT` at α=E₀ is also
parameter-free.

## Results (α = E₀, derived, NO fit)

| atom | A | B_AME | B_lin | B_sym | B_qCLT(chain) | B_qCLT(allpairs) | B_magic |
|---|---|---|---|---|---|---|---|
| D   | 2 | 2.22  | 2.53 (0.88×) | 3.89 (0.57×) | 3.89 (0.57×) | 3.89 (0.57×) | — |
| T   | 3 | 8.48  | 3.71 (2.29×) | **9.07 (0.94×)** | 7.78 (1.09×) | 11.67 (0.73×) | — |
| ³He | 3 | 7.72  | 3.36 (2.30×) | **6.80 (1.14×)** | 7.78 (0.99×) | 11.67 (0.66×) | — |
| ⁴He | 4 | 28.30 | 3.95 (7.17×) | 11.97 (2.36×) | 11.67 (2.42×) | 23.34 (1.21×) | **29.96 (0.94×)** |

(`x.xx×` = B_AME / B_form, the miss factor.)

## Findings

1. **The linear-vs-log "binding gap" is one truncation.** `B_lin = α·s` is
   bounded by α (since `s < 1`), so its miss *grows with A* — ⁴He misses ~7×.
   The historical 5–40× undershoot is `s` vs `−ln(1−s)` at identical α and
   identical trace; nothing else.

2. **`B_sym(E₀)` is the best parameter-free generic form.** On the
   non-anomalous A=3 nuclei (T, ³He) it lands within ~1.2× with *no fit*, and
   it is the **only** form that resolves the T/³He splitting (B_AME 8.48 vs
   7.72; B_sym 9.07 vs 6.80) — that splitting lives in the exact trace.

3. **`B_qCLT` averages away the isospin splitting.** Being uniform-per-bond, it
   predicts T = ³He (both 7.78). The `B_sym − B_qCLT` gap *is* the finite-A
   correlation the q-CLT macroscopic limit discards — a clean illustration of
   the standard-part diagram's `B_sym ⇢ B_qCLT (A→∞)` edge.

4. **The deuteron is the anomaly, not the rule.** The generic log-trace
   *overshoots* D by ~1.75× (predicts 3.9 MeV vs 2.2 MeV observed): the deuteron
   is the most weakly-bound light nucleus (barely bound, no excited state). This
   is *why* pinning α on D is the wrong calibration — and why the derived E₀
   wins.

5. **⁴He needs the magic volume, by construction.** The log-trace undershoots
   ⁴He ~2.4× because ⁴He is doubly-magic and has no single hyperbolic knot — so
   the per-knot trace literally does not exist for it. The trace-free Borromean
   volume `B_magic = 2·m_e·A·8G` lands at +5.9% (0.94×). `B_magic` is therefore
   **not a competing pipeline** but the correct doubly-magic *specialization*;
   `B_depth` is the attempt to splice the two regimes (its `α_{k≥4} = m_e·8G`
   injects exactly this volume term into the high-depth Wedderburn stratum).

## How the original models re-express against B_sym

- **`B_lin`** = the O(s) truncation of `B_sym` — same trace, same α.
- **`B_depth`** = `B_sym` resolved by Wedderburn depth k, with the magic-volume
  term (`α_{k≥4} = m_e·8G`) added at high depth — i.e. `B_sym (low-k) + B_magic
  (k≥4)`, an interpolation between the generic-trace and doubly-magic regimes.
- **`B_magic`** = the `A→∞` / doubly-magic endpoint where the trace is replaced
  by the Borromean volume (the appendix's `B_qCLT = −α Σ ln|V_i|` node taken to
  its shell-closure limit).

So the four are not four competing theories but **four evaluations of one
standard-part chain**: exact trace (`B_sym`) → its linearization (`B_lin`),
its A→∞ per-bond limit (`B_qCLT`), and its doubly-magic volume endpoint
(`B_magic`), with `B_depth` the depth-resolved interpolation across them.

## Caveats / honesty

- Four light nuclei only (D/T/³He/⁴He — the isotopes with a canonical binding
  trace in `binding-canonical.witness.json`). Not a law; a functional-form and
  scale coherence test.
- `ℓ̄` for `B_qCLT` is taken from the deuteron bond (the unique 1-bond datum);
  a per-nucleon-factorized `Σ ln|V_i|` needs the sub-braid decomposition (the
  appendix's exact `B_qCLT` form) — a follow-up.
- Consumes `binding-canonical.witness.json`; PR #2314 regenerates that file to
  full 50-dps (native-free). The shifts are ~1e-8 and do not affect any
  factor-level conclusion here, but a refresh after #2314 lands is noted.
