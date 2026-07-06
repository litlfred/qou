# Q-parameterised braid-word core — design + staged plan

**Branch:** `claude/q-parameterised-braid-word-core-2026-06-17`
**Motivation:** the canonical atom braid word bakes the substrate `q₀` into its
float crossing coefficients, so `tr_M(q)` is not computable at `q ≠ q₀`
(raises "unrecognised crossing"). This blocks (a) the bar-norm mass-modulus
`√(tr_M(q₀)·tr_M(q₀⁻¹))` (PR #2397, a retarget *bolt-on* this supersedes),
and (b) any consumer that needs `tr_M` at several `q` at once — e.g. the
**N-grid particle-dynamics simulators** (owner directive 2026-06-17).

## The structural fact that makes this exact

Every crossing in the atom word is `(c, d)` with `c = 1` and `d` in a **finite
template set** (verified — `pyhecke.atom.nucleon_gen_chains` + the p-n
interface in `mass_at_3A_proper.atom_braid_word_3A`):

| template | `d` | meaning |
|---|---|---|
| `SIGMA` | `0` | σ (positive crossing) |
| `SIGMA_INV` | `−h` | σ⁻¹ |
| `AVG` | `−h/2` | colour-blind averaged |
| `COLOR_PN` | `−h·(½ − δ/4)` | colour-weighted p-n interface |

with `h = q − q⁻¹` and `δ = flavor_split_subleading(q)` the **only**
q-dependent quantities. So the *structural* word (templates + generator
indices) is **q-independent**; only the materialisation of `d` (and the
seminormal σ-eigenvalues `{q, −q⁻¹}` and the Jones–Markov `y_λ`) depends on q.

## Design

### A canonical template layer (new source of truth)
`pyhecke/atom.py` (or a small `pyhecke/crossing_templates.py`):

```python
class Xing(Enum): SIGMA; SIGMA_INV; AVG; COLOR_PN
def d_at_q(t: Xing, q) -> mpf      # 0 | -(q-1/q) | -(q-1/q)/2 | -(q-1/q)(½-δ(q)/4)
def recognize(d_float, q_build) -> Xing   # for migrating baked-float words
```

### Parameterise the generators (additive, q=None ⇒ q₀ byte-identical)
- `nucleon_gen_chains(quarks, *, q=None)` — `h_loc = h if q is None else q−1/q`.
- `atom_gen_chains(Z, N, *, q=None)`, `atom_braid_word_3A(Z, N, *, q=None, …)`
  thread `q` to the generators + the `COLOR_PN` interface (`δ` at `q`).
- **Invariant:** `q=None` reproduces today's exact float word. All **124**
  existing consumers call without `q` ⇒ behaviour unchanged.

### Thread through the trace path
- `tr_m_atom_zn(Z, N, *, q=None)` already threads `q` to `y_λ` + `chi`; **also
  build the word at `q`** (currently it builds at q₀ → the bug). Fix: pass `q`
  to `atom_braid_word_3A`.
- `word_to_mpfr` / `chi_all_lambda_reduced_block` already accept `q`; with a
  word built *at* `q` they re-lift cleanly (no recognition mismatch).

### Multi-q API (the simulator use case)
```python
def tr_M_multi_q(Z, N, qs: Sequence[mpf], *, include_inter=True) -> dict[mpf, mpf]
```
Builds the **q-free template word once**, then materialises + traces per `q`
(reuses the partition / fine-Bratteli structure; only the q-numerics vary).
This is what an N-grid simulator sweeping `q` over a lattice calls.

## Backward-compatibility + regression (STRICT — canonical compute)

- `q=None` path must be **byte-identical** to current output. Regression
  anchors (must reproduce):
  - `tr_M^atom(D) = 0.388357…` (the #2080 cross-check assertion)
  - `tr_m_atom_zn(Z,N)` for D/³H/³He/⁴He at q₀ unchanged
  - `binding_canonical`, the L1/L2 dashboards, the 1ppQ witnesses unperturbed
- No consumer signature changes; `q` is keyword-only with a `None` default.

## Staging

1. **Stage 1 — DONE** (`ed4569b7`): `nucleon_gen_chains(q=None)` parameterised,
   additive; `q=None` byte-identical to `_PROTON_G0`/`_NEUTRON_G0`. Regression
   test `test_nucleon_gen_chains_q_param.py`.
2. **Stage 2 — DONE** (`b0861118`): threaded `q` through `atom_braid_word_3A`
   → `tr_m_atom_zn`. Verified: word `q=None` vs `q=q₀` max|Δd|=1.4e-17;
   `tr_M^atom(D)` at q₀ = 0.38835728 (canonical #2080, UNCHANGED);
   `tr_M^atom(D)` at q₀⁻¹ = 0.0077684065 — now computes, matches #2397.
3. **Stage 3 — DONE**: `tr_m_atom_multi_q(Z,N,qs)` (the simulator N-grid entry
   point) + `tr_m_bar_norm` (‖tr_M‖ via the canonical path). Bar-norm
   ‖tr_a‖(D)=0.0549265 matches #2397. Regression `test_tr_m_atom_q_param.py`.
   **#2397 is now superseded** — its retarget bolt-on is no longer needed;
   close it (or rebase it to a thin re-export) once this lands.
4. **Stage 4 (follow-up):** opportunistic consumer migration to the template
   word where it buys multi-q; not required (q=None keeps the ~124 consumers
   working unchanged).

## Out of scope / parked

- The `det_q = framing-anomaly` Lean formalization (separate follow-up).
- Changing the canonical q₀ value or any physics convention — this is a pure
  representation refactor; the numbers at q₀ do not move.
