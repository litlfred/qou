# Single-pipeline binding comparison — B_lin / B_sym / B_qCLT / B_magic on one canonical tr_M

**Date:** 2026-06-15
**Branch:** `claude/stoic-maxwell-qieqcv` (PR #2320)
**Scope:** exploratory probe — no production rewire, no Δ_λ closure (no 7th ansatz).
**Compute:** [`binding_single_pipeline_comparison.py`](../../computations/binding_single_pipeline_comparison.py)
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

## Extensions — ⁶Li/⁷Li, Δ_λ columns, factorized q-CLT (2026-06-15, second pass)

Rebased onto the transfer-path rewire on `main` (commits `b7d44378`…`8da3fb39`:
`binding_canonical` routes A≥3 through the fine-Bratteli transfer path,
`binding-canonical.witness.json` regenerated at full 50-dps). The D–⁴He numbers
are **byte-stable to the factor level** after the rewire (the probe's witness
re-run reproduced the committed values), so every finding above survives. Three
extensions then land on the same one canonical trace.

### Opt 2 — ⁶Li / ⁷Li (extend past A=4)

Computed live via the SAME transfer entry point (`tr_m_atom_zn`, ~1–3 s each; no
recorded `binding-canonical` row exists yet); B_AME from the AME-2020 registry
(`ame-2020-binding-energies.witness.json`).

| atom | A | B_AME | B_sym(E₀) | B_qCLT_fac(chain) |
|---|---|---|---|---|
| ⁶Li | 6 | 31.99 | 20.06 (1.59×) | 19.75 (1.62×) |
| ⁷Li | 7 | 39.24 | 25.24 (1.55×) | 24.70 (1.59×) |

Both **undershoot ~1.6×** — like ⁴He, beyond A=3 the per-knot trace forms miss
the shell/magic physics. Reported to bound where the single-trace estimate stops
tracking AME, **not** as a closure.

### Opt 1 — Δ_λ columns (for PR #2316)

PR #2316 frames `Δ_λ = B_AME/B_pred` as the exp-vs-linear gap (`tr ~ exp(Vol)`,
Kashaev) with `B_pred` the **linear** form; numerically Δ_λ is exactly this
probe's miss-factor at α=E₀. Surfacing Δ_λ^lin (vs `B_lin`) and Δ_λ^sym (vs
`B_sym`) side by side:

| atom | A | Δ_λ^lin = B_AME/B_lin | Δ_λ^sym = B_AME/B_sym |
|---|---|---|---|
| D   | 2 | 0.88 | 0.57 |
| T   | 3 | 2.29 | **0.94** |
| ³He | 3 | 2.30 | **1.14** |
| ⁴He | 4 | 7.17 | 2.36 |
| ⁶Li | 6 | 7.71 | 1.59 |
| ⁷Li | 7 | 9.40 | 1.55 |

**Finding for #2316:** the Kashaev log-trace `B_sym` already absorbs most of the
exp-vs-linear Δ_λ. Δ_λ^lin grows 0.9→9× with A (the 5–40× gap #2316 attributes
to a q₀⁵-per-site mechanism); Δ_λ^sym stays ≈1 on the non-anomalous A=3 nuclei.
So **if** the q₀⁵-per-site mechanism IS the exp-vs-linear gap, it is *already
realized* by the exact log-trace for T/³He — the residual Δ_λ^sym ≠ 1 is confined
to the deuteron anomaly (0.57) and the magic-shell deficit (⁴He/Li > 1.5), not a
uniform per-site factor. This **sharpens #2316's target**: the mechanism must
explain the *residual over B_sym*, not the full linear gap.

### Opt 3 — factorized q-CLT `B = α Σ_i ln|V_i|`

The appendix names the A→∞ form `B_qCLT = α Σ_i ln|V_i|`, but the first pass used
a uniform `ℓ̄ = L(deuteron)` for every bond. The factorized form takes each `V_i`
to be the trace ratio of the actual **2-nucleon sub-braid** for that bond type,
from the same transfer path:

| bond type | sub-braid (Z,N) | `L = ln(tr_free/tr_atom)` |
|---|---|---|
| p–p | (2,0) diproton  | 0.6945 |
| p–n | (1,1) deuteron  | 0.9292 |
| n–n | (0,2) dineutron | 1.2370 |

Complete bond graph: `C(Z,2)` p–p, `Z·N` p–n, `C(N,2)` n–n bonds. Two scalings —
the literal complete-graph sum (all-pairs) and the physically-scaled `(A−1)`-bond
chain at the composition-weighted mean:

| atom | A | bonds pp/pn/nn | B_fac chain (A−1) | all-pairs C(A,2) |
|---|---|---|---|---|
| D   | 2 | 0/1/0 | 3.89 (0.57×) | 3.89 (0.57×) |
| T   | 3 | 0/2/1 | **8.64 (0.98×)** | 12.96 (0.66×) |
| ³He | 3 | 1/2/0 | **7.12 (1.08×)** | 10.69 (0.72×) |
| ⁴He | 4 | 1/4/1 | 11.82 (2.39×) | 23.64 (1.20×) |
| ⁶Li | 6 | 3/9/3 | 19.75 (1.62×) | 59.26 (0.54×) |
| ⁷Li | 7 | 3/12/6 | 24.70 (1.59×) | 86.47 (0.45×) |

**Findings:**

1. **The factorized chain q-CLT RESOLVES the T/³He split** — the uniform form
   could not. Tritium (2 p–n, **1 n–n**) gets the strong n–n bond (L=1.24);
   ³He (**1 p–p**, 2 p–n) gets the weak p–p bond (L=0.69). Since `L_nn > L_pp`,
   the factorized form predicts T (8.64) > ³He (7.12), matching B_AME (8.48 >
   7.72). This **refines the appendix claim** that *only* `B_sym` splits T/³He:
   bond-**type** resolution suffices — the split is *composition*, not only
   correlation. (Chain-factorized is in fact *tighter* on T/³He, 0.98/1.08×,
   than `B_sym`'s 0.94/1.14×.)

2. **All-pairs overbinds with A** (0.66→0.45× from T to ⁷Li): the complete bond
   graph `C(A,2) ~ A²/2` overcounts bonds. The `(A−1)`-bond chain form
   (composition-weighted mean bond) is the sensible A→∞ self-averaged scaling.

3. **A≥4 still needs magic/shell physics** — ⁴He/⁶Li/⁷Li undershoot ~1.6–2.4× in
   both trace forms, confirming the per-knot-trace ceiling beyond A=3.

The witness now records **5 assertions, all green**: B_sym within 1.25× on
T/³He; B_magic ⁴He within 10%; E₀ beats the deuteron pin; the factorized chain
q-CLT within 1.25× on T/³He; and the factorized q-CLT resolves the T/³He
ordering.

## Caveats / honesty

- Six light nuclei (D through ⁷Li). Still a functional-form and scale coherence
  test, **not a law** — A≥4 undershoots, and the bond graph (chain vs all-pairs)
  is a modeling choice, not derived.
- The factorized `B_qCLT` uses the three 2-nucleon bond-type ratios as the only
  `V_i` values (no per-bond geometry within a nucleus); the chain count `(A−1)`
  and all-pairs `C(A,2)` bracket the true effective bond number.
- `B_magic` covers only the doubly-magic ⁴He; ⁶Li/⁷Li have no analogous
  trace-free volume here, which is why they undershoot.
- Consumes `binding-canonical.witness.json` (transfer path, 50-dps on `main`);
  ⁶Li/⁷Li recomputed live from the same `tr_m_atom_zn` entry point, so the trace
  source is one pipeline throughout.
