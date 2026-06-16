# Binding under-shoot is shell structure, not a uniform law (2026-06-16)

**Status:** audit — negative+positive result. Records a session investigation
(prompted by the `/dashboard-sweep` review) of *why* the standard-part binding
forms under-bind, testing three structural "fix" directions. **Conclusion:** the
categorical binding trace is **not** broken by a uniform factor; the residual is
**nuclear shell structure** (deuteron anomaly + magic closures), which no single
smooth categorical form (trace, volume, or colored-Jones) can capture. This
explains *why* the "q₀⁵-per-site"/Δ_λ-exponent hunt had to fail
([`2026-06-15-binding-qa-followups-investigation.md`](2026-06-15-binding-qa-followups-investigation.md) §5)
and confirms the #2320 coordination note.

**Provenance / caveats.** Numbers are live from the canonical engine
(`mass_binding_dashboard.py` → `tr_m_atom_via_transfer.tr_m_atom_zn`, the
fine-Bratteli transfer trace), run in a **qou-only sandbox** by recovering
`qou_substrate` + `pyhecke` from git history (pre-FolioAssistant-migration commit
`ada4c209^`) onto `PYTHONPATH`. α = E₀ = m_e/(q₀(q₀−1)) (CAL-1);
q₀ = 1.1099785955573347 (canonical proton-anchor, see
[`2026-06-15-binding-qa-followups-investigation.md`](2026-06-15-binding-qa-followups-investigation.md) §2);
binding data = AME2020. **EXPLORATORY** — no production rewire, no fit; the probe
is not reproducible in a qou-only checkout without the migrated deps.

## The key datum: the residual changes sign

`B_sym = α·ln( tr_M(W_free) / tr_M(W_atom) )` — the full per-knot exp-form trace,
parameter-free — vs AME2020:

| nuc | A | B_AME (MeV) | B_sym (MeV) | **B_AME/B_sym** | reading |
|---|---|---|---|---|---|
| D | 2 | 2.22 | 3.89 | **0.57** | trace **over**-binds (deuteron anomaly) |
| T | 3 | 8.48 | 9.07 | **0.94** | ✓ works (~6 %) |
| ³He | 3 | 7.72 | 6.80 | **1.14** | ✓ works (~14 %) |
| ⁴He | 4 | 28.30 | 11.98 | **2.36** | **under** (doubly-magic) |
| ⁶Li | 6 | 31.99 | 20.06 | 1.59 | shell dip |
| ⁷Li | 7 | 39.25 | 25.24 | 1.56 | shell dip |

The ratio is **non-monotonic and changes sign** (0.57 → 2.36): the trace
*over*-binds the weakly-bound deuteron and *under*-binds doubly-magic ⁴He. **A
uniform formula error cannot do that.** This is the signature of nuclear **shell
structure**, and it confirms the #2320 single-pipeline note ("the residual
Δ_λ^sym ≠ 1 lives in the deuteron anomaly and the magic-shell deficit, not a
uniform per-site factor"). Note the trace form **works, parameter-free, to
~6–14 %** for the *generic* light nuclei T/³He.

## Option 1 — binding = hyperbolic volume

- **Single link volume: refuted** (prior, `binding_link_volumes.py`):
  `B = m_e·Vol(K_bind)·Δtr` gives ²H +0.2 % but ³H/³He **−60 %** — Δtr is
  ~A-independent while binding grows ~13×, so the A-dependence cannot live in one
  link.
- **Count × Vol(Borromean): scale right, A-law wrong.** The energy *quantum*
  `m_e·Vol(Borromean = L6a4 = 8G) = 3.744 MeV` ≈ binding-per-nucleon — which is
  exactly *why* `B_magic = 2·m_e·A·Vol` nails ⁴He (0.94). But the required count
  `k = B_AME / 3.744` is the binding-per-nucleon curve itself (D 0.59, T 2.27,
  ³He 2.06, ⁴He 7.56, ⁶Li 8.54, ⁷Li 10.48, ⁹Be 15.53, ¹²C 24.61) — **no clean
  combinatorial count** (A, 2A, A−1, 2(A−1), C(A,2), C(A,3) all fail across the
  range). Volume supplies the *quantum*, not the *A-law*.

## Option 2 — many-body (3-body / Borromean) vs pairwise

**Not the gap.** `B_sym` is the full 3A-strand atom-braid trace — it *already*
contains all many-body correlations, and it gets T/³He to ~1.0. ⁴He's miss is
the **magic shell closure**, not a generic missing 3-body term. (The *pairwise*
`B_qCLT_fac` under-binds vs `B_sym`, but closing that pairwise→full gap does not
touch the `B_sym`→AME gap.)

## Option 3 — colored / complex-q (the deep keystone)

The volume conjecture (Vol = lim_{N→∞} growth of the N-colored Jones at a root of
unity) does say the **N=2, real-q** trace under-represents Vol — a real effect.
But that is a *uniform* rescaling, and the residual here changes **sign** (D over,
⁴He under). So the colored/complex-q level **cannot** fix a shell-structured
residual by rescaling. It may improve the overall normalization; it will not
produce magic numbers.

## Conclusion

The categorical binding trace is a working **smooth** term (parameter-free,
~10 % on generic light nuclei). The misses are **nuclear shell/magic structure**
— deuteron over-binding, ⁴He doubly-magic deficit, Li shell dip — which are
non-smooth in A and which **no single categorical form (trace, volume, or
colored-Jones) can capture**, because shell closures are not a smooth function of
A. The framework's two-formula treatment (generic trace + `B_magic` for ⁴He) is
therefore **correct**: `B_magic` is the first *shell correction*, and it works
*because* ⁴He is special.

**Recommended direction.** Stop hunting a single unified binding law (q₀⁵-per-site,
a uniform volume/colored rescale, a 7th Δ_λ ansatz — see the Δ_λ gate in
CLAUDE.md). Model binding as **smooth categorical term + explicit shell/magic
corrections** (shell-model-like), with `B_magic` as the first such correction.
This retires follow-up 5: the q₀⁵ exponent was a *uniform* law fit to a
*shell-structured* residual — doomed regardless of the exponent.

## References

- [`2026-06-15-binding-qa-followups-investigation.md`](2026-06-15-binding-qa-followups-investigation.md)
  §5 — the q₀⁵ magnitude refutation; this doc explains *why* it had to fail.
- #2320 — single-pipeline `B_lin`/`B_sym` comparison (the coordination note this confirms).
- `computations/binding_link_volumes.py` — the single-link-volume refutation (²H/³H/³He).
- `computations/magic_A_formula.py` — `B_magic` (the working ⁴He shell correction).
- `computations/mass_binding_dashboard.py` — the engine (`/dashboard-low`, `/dashboard-sweep`).
- #2316 / bean `qb5s` — the q₀⁵-per-site starting notes.
