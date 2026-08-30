# The `y_lambda_at` straddle trap: stale in every particular

**Date:** 2026-08-23 · **Bean:** `qou-qflp`
**Status:** evidence assembled; the AGENTS.md edit is an owner call and is NOT made here.

## What AGENTS.md currently says

[`AGENTS.md` §q₀-anchor convention](../../AGENTS.md), lines ~1609-1618:

> **The specific trap that caused it (check your call sites).**
> `wedderburn_jones_markov.y_lambda_at(n, q)` returns the cached
> **muon-built** `y-lambda-at-q0.witness.json` whenever
> `|q − q_parameter.Q| < 1e-12` — a gate satisfied **trivially** when the
> caller passes `q_parameter.Q` itself. So the ideal-layer cache reaches an
> experimental-layer caller with **no signal that a layer boundary was
> crossed**.

Three factual claims: the accessor **serves the cache**; the cache is
**muon-built**; therefore callers silently **cross a layer boundary**.

## All three are now false

### 1. The accessor no longer serves the cache

`y_lambda_at()` was rewritten for the convention-D owner ruling (2026-08-09).
The live body is twelve lines and reads no file:

```python
if q_val is not None:
    _y = _y_su_n(n, _mp.mpf(str(q_val)), 2)          # live formula
    return {sh: sp.Float(_mp.nstr(v, 30), 30) for sh, v in _y.items()}
return _y_su_n_sym(n, Q_SYM, 2)                       # symbolic, also live
```

The cache-serving code was moved to `_y_lambda_at_convention_C_HISTORICAL`,
whose own docstring opens *"DEAD — convention C, excised 2026-08-09."* The
`|q − Q| < 1e-12` gate AGENTS.md describes lives only in that dead function.

### 2. The cache is not muon-built

`computations/y-lambda-at-q0.witness.json` carries the **proton** pin, and was
regenerated in the convention-D cascade (`7665e0e4b`, `506ac9135`).

### 3. It is not convention-C either — and this contradicts a second doc

`wedderburn_jones_markov.y_lambda_at`'s own docstring says:

> In particular `y-lambda-at-q0.witness.json` holds C weights and must
> **NOT** be served — that cache is why the switch has to happen here rather
> than only at `markov_z`.

The file's actual contents:

```
n=3:  (3) → 0.50540422650393080…    (2,1) → 0.24729788674803459…
```

Convention **D** is `(0.5054042, 0.2472979, 0)`; convention C is
`(0.4153958, 0.2809296, 0.0227449)`. **The file holds D.** So the docstring's
warning is stale too — it was written when the file held C, and the same
convention-D cascade that re-pinned it also re-derived it.

## The one thing that is still true, and it is not what the trap says

**Two producers still load the file directly**, bypassing the accessor entirely:

| producer | line |
|---|---|
| `computations/probe_theta_carry_binding.py` | `d = json.load(open(HERE / "y-lambda-at-q0.witness.json"))` |
| `computations/delta_lambda_empirical_tabulation.py` | `cache_path = _pb.witness_path("y-lambda-at-q0.witness.json", HERE)` |

(`nucleus_sdp_assembly.py` documents reading it in prose; 57 files name the
string in total, mostly in comments.)

Those two get **D weights at the proton pin** — correct under both current
rulings. So there is no live defect here; there is a **warning pointed at the
wrong thing**. An agent following AGENTS.md today would go looking for a muon
cache served by an accessor that no longer serves it, find neither, and either
waste the search or "fix" something that is already right.

## The decision, and why it is yours

The text is in **AGENTS.md**, which is the agent-instruction source of truth.
Editing it changes what every future agent believes about the two-layer
discipline, so it is not an agent's call. Three options:

| | option | what it costs | what it risks |
|---|---|---|---|
| **A** | **Delete the trap paragraph.** The mechanism it describes does not exist. | ~8 lines | Loses the *general* lesson ("a cached-witness accessor that serves on `q == package constant` is a silent layer crossing"), which is still sound advice even though this instance is gone. |
| **B** | **Rewrite it as a closed case** — keep the pattern as a warning, state that this instance was closed by the convention-D rewrite, and point the "check your call sites" instruction at the two direct readers instead. | ~12 lines | Nothing obvious. Preserves the lesson, corrects the facts, keeps the live consumers visible. |
| **C** | **Leave it.** | 0 | It is actively misleading now, and its neighbouring sentence ("Audit any other cached-witness accessor with the same shape") is the part agents act on. |

**My recommendation is B**, for one reason: the paragraph's value was never the
specific accessor — it was the *shape*. `y_lambda_at` is simply the worked
example, and a worked example that no longer works is worse than no example.
Rewriting keeps the transferable half and deletes the false half.

**Also worth fixing under B**, in the same pass and not in AGENTS.md: the
`wedderburn_jones_markov.y_lambda_at` docstring's "holds C weights" claim. That
one *is* an agent's call — it is a code comment, not policy — but it is left
here so both stale statements are corrected together rather than one at a time.

## What was checked

- `AGENTS.md` §q₀-anchor, verbatim.
- `wedderburn_jones_markov.y_lambda_at` live body and its historical twin.
- `y-lambda-at-q0.witness.json`: pin prefix and n=2/n=3 weight values.
- `git log` on the witness (the convention-D cascade commits).
- All 57 files naming the string, separating the two that load it from the
  rest that mention it.
